"""Untimed supported-minor setup assertions; never calibrates or samples intervals."""

import argparse
import dataclasses as std
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
from types import MappingProxyType


def load(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).with_name(filename)
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-tuple", required=True, type=Path)
    parser.add_argument("--artifact-root", required=True, type=Path)
    parser.add_argument("--sdk-wheel-dir", required=True, type=Path)
    parser.add_argument("--undoable-baseline-dir", required=True, type=Path)
    parser.add_argument("--undoable-baseline-wheel", required=True, type=Path)
    parser.add_argument("--backend", choices=("native-rust",), default="native-rust")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    os.environ["ASTICHI_LOWER_ENGINE"] = args.backend
    provenance = load("perf_provenance", "provenance.py")
    artifact_tuple = json.loads(args.artifact_tuple.read_text())
    verified = provenance.verify_installation(
        artifact_tuple, args.artifact_root, args.sdk_wheel_dir, backend=args.backend
    )
    seam = load("perf_seam", "undoable_cases.py")
    baseline = seam.load_baseline(
        args.undoable_baseline_dir, wheel=args.undoable_baseline_wheel
    )
    harness = load("perf_harness", "harness.py")
    import yidl_dataclass as product
    import yidl_undoable

    checked = []
    for count in (3, 12):
        product_cases = harness.ordinary_cases(product, count, True)
        standard_cases = harness.ordinary_cases(std, count, True)
        for name, case in product_cases.items():
            actual = case["run"](1, None)
            expected = standard_cases[name]["run"](1, None)
            assert (
                std.asdict(actual) == std.asdict(expected)
                if name.startswith("construct_")
                else actual == expected
            )
            checked.append([count, "ordinary", name])
        readonly = harness.readonly_cases(product, count, True)
        assert readonly["readonly_read"]["run"](1, None) == 0
        assert readonly["readonly_reject"]["run"](3, None) == 2
        checked.extend([count, "readonly", name] for name in readonly)
        for name, case in harness.extension_cases(product, count).items():
            prepared = case["prepare"](3) if case["prepare"] else None
            result = case["run"](3, prepared)
            if name.startswith("lazy_"):
                assert result == 7 and len({id(item) for item in prepared}) == 3
                assert all(item.value == 7 for item in prepared)
            elif name == "construct_dependent":
                assert result.total == 6
            checked.append([count, "extension", name])
        generation = harness.generation_cases(product, count, True)["decorate_repeated"]
        assert generation["run"](2, generation["prepare"](2))().f0 == 0
        emission = harness.source_emission_case(product, count)
        assert "self.f0" in emission["run"](1, None)
        checked.extend(
            [
                [count, "generation", "decorate_repeated"],
                [count, "generation", "actual_composable_emission"],
            ]
        )
        for name, definition in harness.memory_models(product, count).items():
            instance = definition["cls"]()
            if definition.get("initialize_ready"):
                assert instance.delayed == 7
            assert instance.f0 == 0
            checked.append([count, "memory_setup", name])
        for variant, cases in seam.cases(
            yidl_undoable, baseline, count, harness.runner
        ).items():
            for name, case in cases.items():
                try:
                    for operations in (3, 4, 3):
                        prepared = (
                            case["prepare"](operations) if case["prepare"] else None
                        )
                        observed_changes = []
                        globals_ = case["run"].__globals__
                        original = globals_.get("obj")
                        if name.endswith("alternate"):

                            def identity(value):
                                if isinstance(value, tuple):
                                    return tuple(identity(item) for item in value)
                                if type(value) is MappingProxyType:
                                    return tuple(
                                        (key, identity(item))
                                        for key, item in value.items()
                                    )
                                return id(value._u_state)

                            class Observer:
                                @property
                                def value(self):
                                    return original.value

                                @value.setter
                                def value(self, value):
                                    before = identity(original.value)
                                    original.value = value
                                    after = identity(original.value)
                                    assert before != after
                                    observed_changes.append((before, after))

                            globals_["obj"] = Observer()
                        try:
                            result = case["run"](operations, prepared)
                        finally:
                            if name.endswith("alternate"):
                                globals_["obj"] = original
                        if name.endswith("alternate"):
                            assert len(observed_changes) == operations
                        if name == "undoable_eq_prelude":
                            assert result is True
                        elif name.endswith("alternate"):
                            manager, parent, *_ = case["keepalive"]
                            choices = case["run"].__globals__["choices"]
                            assert manager._edit.touched
                            final = choices[(operations - 1) % 2]
                            assert identity(parent.value) == identity(final)
                finally:
                    if "cleanup" in case:
                        case["cleanup"]()
                checked.append([count, variant, name])
    result = {
        "scope": "untimed setup only; no performance samples",
        "python": sys.version.split()[0],
        "backend": args.backend,
        "checked": checked,
        "provenance": verified,
        "baseline_wheel_sha256": seam.BASELINE_SHA256,
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(
        json.dumps(
            {
                "python": result["python"],
                "backend": args.backend,
                "untimed_setup_checks": len(checked),
                "scope": result["scope"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
