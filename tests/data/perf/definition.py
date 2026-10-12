"""Prepare complete definitions before any timed product observations."""

import argparse
import dataclasses as std
import hashlib
import importlib.util
import json
from pathlib import Path
import os


def load(name, filename):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_definition(product, baseline, *, artifact_tuple):
    harness = load("perf_harness", "harness.py")
    seam = load("perf_seam", "undoable_cases.py")
    import yidl_undoable

    timing = []
    memory = []
    sources = {}
    source_text = {}
    classifications = {}
    setup = {}
    variants = {
        "product": (product, True),
        "stdlib_default": (std, False),
        "stdlib_slots": (std, True),
    }
    for count in (3, 12):
        for variant, (api, slots) in variants.items():
            cases = {
                **harness.ordinary_cases(api, count, slots),
                **harness.readonly_cases(api, count, slots),
                **harness.generation_cases(api, count, slots),
            }
            if variant == "product":
                cases.update(harness.extension_cases(product, count))
                cases["source_emission"] = harness.source_emission_case(product, count)
                run, source = harness.runner("result = index", {})
                cases["harness_only"] = {
                    "run": run,
                    "source": source,
                    "classification": "loop observation; never subtracted",
                }
            for name, case in cases.items():
                key = f"{count}:{variant}:{name}"
                timing.append([count, name, variant])
                sources[key] = hashlib.sha256(case["source"].encode()).hexdigest()
                source_text[key] = case["source"]
                classifications[key] = case.get(
                    "classification", "ordinary comparable operation"
                )
            cold_key = f"{count}:{variant}:decorate_cold"
            timing.append([count, "decorate_cold", variant])
            sources[cold_key] = hashlib.sha256(
                Path(__file__).with_name("cold_worker.py").read_bytes()
            ).hexdigest()
            source_text[cold_key] = (
                Path(__file__).with_name("cold_worker.py").read_text()
            )
            classifications[cold_key] = (
                "first decoration in a fresh worker; sum of generator intervals; per-variant calibration; no numerical target"
            )
            memory.extend(
                [count, name, variant]
                for name in ("ordinary", "frozen", "weakref", "local")
            )
            if variant == "product":
                memory.extend(
                    [count, name, variant]
                    for name in (
                        "lazy_unready",
                        "lazy_ready",
                        "retained_shared",
                        "retained_unique",
                    )
                )
        seam_cases = seam.cases(yidl_undoable, baseline, count, harness.runner)
        for variant, cases in seam_cases.items():
            for name, case in cases.items():
                key = f"{count}:{variant}:{name}"
                timing.append([count, name, variant])
                sources[key] = hashlib.sha256(case["source"].encode()).hexdigest()
                source_text[key] = case["source"]
                classifications[key] = case["classification"]
                if "setup" in case:
                    setup[key] = case["setup"]
                if "reference_method_source" in case:
                    setup[key] = {
                        "handwritten_benchmark_reference_source": case[
                            "reference_method_source"
                        ]
                    }
                if "cleanup" in case:
                    case["cleanup"]()
    return {
        "scope": "Frozen sampling definition; no result or numerical acceptance",
        "artifact_tuple": artifact_tuple,
        "model_fields": [3, 12],
        "timing_keys": sorted(timing),
        "memory_keys": sorted(memory),
        "memory_source_files": {
            name: hashlib.sha256(
                Path(__file__).with_name(name).read_bytes()
            ).hexdigest()
            for name in ("cases.py", "memory.py")
        },
        "memory_source_boundary": "All model factories in cases.py; allocation/dictionary inspection in memory.py; per-minor stdlib source in minor_provenance. These exact source files govern all32 memory keys.",
        "timing_source_sha256": sources,
        "timing_sources": source_text,
        "classifications": classifications,
        "seam_setup": setup,
        "minimum_calibration_ns": 20_000_000,
        "warmups": 10,
        "measured_batches": 20,
        "minimum_processes_per_minor": 5,
        "minors": ["3.12", "3.13", "3.14"],
        "memory_instances": 10_000,
        "bootstrap_resamples": 10_000,
        "seed": 20261012,
        "noisy_iqr_over_median": 0.15,
        "slot_stdlib_slots_target": 1.2,
        "ordinary_target": 2.0,
        "extension_generation_memory_undoable_targets": None,
        "harness_files": {
            name: hashlib.sha256(
                Path(__file__).with_name(name).read_bytes()
            ).hexdigest()
            for name in (
                "harness.py",
                "measurement.py",
                "report.py",
                "validation.py",
                "undoable_cases.py",
                "cold_worker.py",
            )
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-tuple", required=True, type=Path)
    parser.add_argument("--undoable-baseline-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--artifact-root", required=True, type=Path)
    parser.add_argument("--sdk-wheel-dir", required=True, type=Path)
    parser.add_argument("--undoable-baseline-wheel", required=True, type=Path)
    parser.add_argument("--backend", choices=["native-rust"], default="native-rust")
    args = parser.parse_args()
    os.environ["ASTICHI_LOWER_ENGINE"] = args.backend
    provenance = load("perf_provenance", "provenance.py")
    artifact_tuple = json.loads(args.artifact_tuple.read_text())
    installed = provenance.verify_installation(
        artifact_tuple, args.artifact_root, args.sdk_wheel_dir, backend=args.backend
    )
    import yidl_dataclass

    seam = load("perf_seam", "undoable_cases.py")
    baseline = seam.load_baseline(
        args.undoable_baseline_dir, wheel=args.undoable_baseline_wheel
    )
    result = make_definition(
        yidl_dataclass,
        baseline,
        artifact_tuple=artifact_tuple,
    )
    result["selected_backend"] = args.backend
    result["provenance"] = installed
    result["source_sha256"] = provenance.source_hashes()
    result["baseline_wheel_sha256"] = seam.BASELINE_SHA256
    validation = load("perf_validation", "validation.py")
    validation.validate_definition(result)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(
        json.dumps(
            {
                "timing_cases": len(result["timing_keys"]),
                "memory_cases": len(result["memory_keys"]),
                "backend": args.backend,
                "definition_sha256": provenance.canonical_digest(result),
                "scope": "untimed frozen definition preparation",
            },
            sort_keys=True,
        )
    )
