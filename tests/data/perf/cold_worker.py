"""One first generator interval; imports/declaration/transport remain outside clock."""

import argparse
import dataclasses as std
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time


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
    parser.add_argument(
        "--variant",
        choices=("product", "stdlib_default", "stdlib_slots"),
        required=True,
    )
    parser.add_argument("--fields", choices=(3, 12), type=int, required=True)
    parser.add_argument("--backend", choices=("native-rust",), default="native-rust")
    parser.add_argument("--definition", required=True, type=Path)
    parser.add_argument("--artifact-root", required=True, type=Path)
    parser.add_argument("--sdk-wheel-dir", required=True, type=Path)
    parser.add_argument("--setup-only", action="store_true")
    args = parser.parse_args()
    os.environ["ASTICHI_LOWER_ENGINE"] = args.backend
    definition = json.loads(args.definition.read_text())
    provenance = load("perf_provenance", "provenance.py")
    validation = load("perf_validation", "validation.py")
    validation.validate_definition(definition)
    if provenance.source_hashes() != definition["source_sha256"]:
        raise ValueError("cold worker source drift from frozen definition")
    installed = provenance.verify_installation(
        definition["artifact_tuple"],
        args.artifact_root,
        args.sdk_wheel_dir,
        backend=args.backend,
    )
    if "minor_provenance" in definition:
        minor = ".".join(installed["python"].split(".")[:2])
        if installed != definition["minor_provenance"].get(minor):
            raise ValueError(
                "cold installed provenance differs from frozen minor tuple"
            )
    if args.variant == "product":
        import yidl_dataclass as api
    else:
        api = std
    namespace = {
        "__module__": __name__,
        "__annotations__": {f"f{i}": int for i in range(args.fields)},
    }
    namespace.update({f"f{i}": i for i in range(args.fields)})
    declaration = type("Fields", (), namespace)
    if args.setup_only:
        model = api.dataclass(slots=args.variant != "stdlib_default", order=True)(
            declaration
        )
        assert model().f0 == 0
        print(
            json.dumps(
                {
                    "scope": "untimed cold-worker setup only",
                    "variant": args.variant,
                    "fields": args.fields,
                    "selected_backend": args.backend,
                    "python": sys.version.split()[0],
                },
                sort_keys=True,
            )
        )
        return 0
    start = time.perf_counter_ns()
    model = api.dataclass(slots=args.variant != "stdlib_default", order=True)(
        declaration
    )
    elapsed = time.perf_counter_ns() - start
    assert model().f0 == 0
    print(
        json.dumps(
            {
                "variant": args.variant,
                "fields": args.fields,
                "operations": 1,
                "elapsed_ns": elapsed,
                "units": "ns",
                "python": sys.version.split()[0],
                "imports_and_declaration_setup": "outside measured interval",
                "cache_boundary": "new interpreter; filesystem/OS caches may be warm",
                "pid": os.getpid(),
                "selected_backend": args.backend,
                "source_sha256": hashlib.sha256(
                    Path(__file__).read_bytes()
                ).hexdigest(),
                "definition_sha256": provenance.canonical_digest(definition),
                "provenance": installed,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
