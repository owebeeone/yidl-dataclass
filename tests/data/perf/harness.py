"""Benchmark harness: cases are prepared outside each timing boundary."""

import argparse
import dataclasses as std
import gc
import hashlib
import importlib.util
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import random
import sys
import subprocess
import time
import tracemalloc

_support_path = Path(__file__).with_name("measurement.py")
_spec = importlib.util.spec_from_file_location("perf_support", _support_path)
support = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(support)
SEED = 20261012


def sibling(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).with_name(filename)
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


case_setup = sibling("perf_cases", "cases.py")
memory_support = sibling("perf_memory", "memory.py")
extension_cases = case_setup.extension_cases
generation_cases = case_setup.generation_cases
memory_models = case_setup.memory_models
model = case_setup.model
ordinary_cases = case_setup.ordinary_cases
readonly_cases = case_setup.readonly_cases
runner = case_setup.runner
source_emission_case = case_setup.source_emission_case
memory_row = memory_support.memory_row


def cold_generation_batches(
    variant, count, *, warmups=10, batches=20, worker_arguments=(), observe=None
):
    worker_path = Path(__file__).with_name("cold_worker.py")

    def worker():
        result = subprocess.run(
            [
                sys.executable,
                "-I",
                str(worker_path),
                "--variant",
                variant,
                "--fields",
                str(count),
                "--backend",
                os.environ.get("ASTICHI_LOWER_ENGINE", "native-rust"),
                *worker_arguments,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            if observe is not None:
                observe(
                    "cold_worker_failure",
                    {
                        "variant": variant,
                        "fields": count,
                        "exit_code": result.returncode,
                        "stdout": result.stdout,
                        "stderr": result.stderr,
                    },
                )
            raise RuntimeError("cold worker failed; raw journal retains stdout/stderr")
        try:
            return json.loads(result.stdout)
        except (ValueError, TypeError):
            if observe is not None:
                observe(
                    "cold_worker_invalid_output",
                    {
                        "variant": variant,
                        "fields": count,
                        "stdout": result.stdout,
                        "stderr": result.stderr,
                    },
                )
            raise

    source_digest = hashlib.sha256(worker_path.read_bytes()).hexdigest()
    context = {"phase": "calibration"}

    def emit(kind, row):
        tagged = dict(
            row,
            fields=count,
            case="decorate_cold",
            variant=variant,
            source_sha256=source_digest,
            units="ns" if kind == "cold_worker" else "ns/op",
            elapsed_units="ns",
            **context,
        )
        if observe is not None:
            observe(kind, tagged)
        return tagged

    def measured(n):
        return support.cold_sample(
            worker, n, on_observation=lambda row: emit("cold_worker", row)
        )

    calibration = []

    def calibrated(row):
        tagged = emit("calibration", row)
        calibration.append(tagged)

    operations = support.calibrate(measured, on_observation=calibrated)
    rows = []
    for batch in range(warmups + batches):
        context = {
            "phase": "warmup" if batch < warmups else "measurement",
            "batch": batch - warmups,
        }
        row = measured(operations)
        rows.append(emit("timing", row))
    return {
        "rows": rows,
        "calibration_operations": operations,
        "calibration_rows": calibration,
        "sampling_note": "Each operation is first decoration in a fresh worker. Batches aggregate measured generation intervals; imports, declaration preparation and transport are excluded. Counts calibrate per variant; no generation parity target.",
    }


def environment():
    import astichi, yidl, yidl_dataclass

    for module in (astichi, yidl, yidl_dataclass):
        if (
            not Path(module.__file__)
            .resolve()
            .is_relative_to(Path(sys.prefix).resolve())
        ):
            raise RuntimeError(
                "benchmark imports must originate in isolated installed environment"
            )
    if (
        importlib.metadata.version("astichi") != "1.1.3"
        or importlib.metadata.version("yidl") != "0.1.0"
    ):
        raise RuntimeError("benchmark requires unchanged original SDK wheels")
    from astichi.lower_engine.native import select_lower_engine

    selection = select_lower_engine()
    if selection.fallback_scope is not None:
        raise RuntimeError("benchmark backend fallback forbidden")

    def command(argv):
        try:
            result = subprocess.run(argv, capture_output=True, text=True, check=False)
        except FileNotFoundError:
            return {
                "exit_code": None,
                "availability": "command unavailable",
                "command": argv,
            }
        lines = [
            line for line in result.stdout.splitlines() if "hibernatefile" not in line
        ]
        return {
            "exit_code": result.returncode,
            "stdout": "\n".join(lines),
            "path_values": "system hibernate path omitted",
        }

    return {
        "python": sys.version,
        "implementation": platform.python_implementation(),
        "gil_enabled": (
            sys._is_gil_enabled() if hasattr(sys, "_is_gil_enabled") else True
        ),
        "thread_inherit_context": getattr(sys.flags, "thread_inherit_context", None),
        "executable_build": platform.python_build(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "load_average": list(os.getloadavg()),
        "clock": vars(time.get_clock_info("perf_counter")),
        "seed": SEED,
        "garbage_collection": "enabled; collection outside timed access/memory setup where recorded",
        "power_settings": command(["pmset", "-g", "custom"]),
        "cpu": command(["sysctl", "-n", "machdep.cpu.brand_string"]),
        "process_pid": os.getpid(),
        "selected_backend": selection.selected_engine,
        "fallback_scope": selection.fallback_scope,
        "dependencies": {
            name: importlib.metadata.version(name)
            for name in ("astichi", "yidl", "yidl-dataclass")
        },
        "harness_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "support_sha256": hashlib.sha256(_support_path.read_bytes()).hexdigest(),
    }


def run_process(
    product,
    *,
    warmups=10,
    batches=20,
    minimum_ns=20_000_000,
    include_cold=False,
    undoable_baseline=None,
    cold_worker_arguments=(),
    observe=None,
):
    variants = {
        "product": (product, True),
        "stdlib_default": (std, False),
        "stdlib_slots": (std, True),
    }

    class ObservedList(list):
        def __init__(self, kind):
            self.kind = kind

        def append(self, row):
            if self.kind != "memory":
                row.update(units="ns/op", elapsed_units="ns")
            if observe is not None:
                observe(self.kind, row)
            super().append(row)

    rows = ObservedList("timing")
    memory = ObservedList("memory")
    sources = {}
    classifications = {}
    calibration_rows = ObservedList("calibration")

    def measure_family(cases, count):
        names = list(cases["product"])
        random.Random(SEED + count).shuffle(names)
        for case_name in names:
            available = [name for name in cases if case_name in cases[name]]
            counts = []
            for variant in available:
                case = cases[variant][case_name]
                sources[f"{count}:{variant}:{case_name}"] = case["source"]
                classifications[f"{count}:{variant}:{case_name}"] = case.get(
                    "classification", "ordinary comparable operation"
                )
                if "reference_method_source" in case:
                    sources[f"{count}:{variant}:{case_name}:reference_method"] = case[
                        "reference_method_source"
                    ]
                measured = lambda n, case=case: support.sample(
                    case["run"], n, prepare=case["prepare"]
                )

                def calibrated(row, variant=variant, case=case):
                    calibration_rows.append(
                        dict(
                            row,
                            fields=count,
                            case=case_name,
                            variant=variant,
                            phase="calibration",
                            source_sha256=hashlib.sha256(
                                case["source"].encode()
                            ).hexdigest(),
                        )
                    )

                counts.append(
                    support.calibrate(
                        measured, minimum_ns=minimum_ns, on_observation=calibrated
                    )
                )
            operations = max(counts)
            for batch in range(warmups + batches):
                order = available[:]
                if batch % 2:
                    order.reverse()
                for variant in order:
                    case = cases[variant][case_name]
                    row = support.sample(
                        case["run"], operations, prepare=case["prepare"]
                    )
                    rows.append(
                        dict(
                            row,
                            variant=variant,
                            case=case_name,
                            fields=count,
                            batch=batch - warmups,
                            phase="warmup" if batch < warmups else "measurement",
                            source_sha256=hashlib.sha256(
                                case["source"].encode()
                            ).hexdigest(),
                        )
                    )

    for count in (3, 12):
        cases = {}
        for name, (api, slots) in variants.items():
            cases[name] = {
                **ordinary_cases(api, count, slots),
                **readonly_cases(api, count, slots),
                **generation_cases(api, count, slots),
            }
        cases["product"].update(extension_cases(product, count))
        cases["product"]["source_emission"] = source_emission_case(product, count)
        run, source = runner("result = index", {})
        cases["product"]["harness_only"] = {
            "run": run,
            "source": source,
            "prepare": None,
            "classification": "loop observation; never subtracted from operation estimates",
        }
        measure_family(cases, count)
        for variant, (api, slots) in variants.items():
            memory.append(
                dict(
                    memory_row(model(api, count, slots=slots)),
                    variant=variant,
                    fields=count,
                    case="ordinary",
                )
            )
            memory.append(
                dict(
                    memory_row(model(api, count, slots=slots, frozen=True)),
                    variant=variant,
                    fields=count,
                    case="frozen",
                )
            )
            memory.append(
                dict(
                    memory_row(
                        model(
                            api,
                            count,
                            slots=slots,
                            **({"weakref_slot": True} if slots else {}),
                        )
                    ),
                    variant=variant,
                    fields=count,
                    case="weakref",
                    baseline_note="explicit weakref slot for slotted model; ordinary dictionary model already supports weak references",
                )
            )
            if variant != "product":
                namespace = {
                    "__annotations__": {
                        **{f"f{i}": int for i in range(count)},
                        "cache": dict,
                    },
                    "__module__": __name__,
                    **{f"f{i}": i for i in range(count)},
                    "cache": std.field(
                        default_factory=dict,
                        init=False,
                        repr=False,
                        compare=False,
                        hash=False,
                    ),
                }
                local = std.dataclass(slots=slots)(type("LocalMemory", (), namespace))
                memory.append(
                    dict(
                        memory_row(local, inputs="unique cache dict per instance"),
                        variant=variant,
                        fields=count,
                        case="local",
                        baseline_note="standard cache field storage analogue; metadata exposure differs from product local_store",
                    )
                )
        for label, definition in memory_models(product, count).items():
            if label in ("ordinary", "frozen", "weakref"):
                continue
            memory.append(
                dict(
                    memory_row(
                        definition["cls"],
                        initialize_ready=definition.get("initialize_ready", False),
                        inputs=definition["inputs"],
                    ),
                    variant="product",
                    fields=count,
                    case=label,
                )
            )
        if undoable_baseline is not None:
            seam_path = Path(__file__).with_name("undoable_cases.py")
            seam_spec = importlib.util.spec_from_file_location(
                "perf_undoable", seam_path
            )
            seam = importlib.util.module_from_spec(seam_spec)
            seam_spec.loader.exec_module(seam)
            import yidl_undoable

            seam_cases = seam.cases(yidl_undoable, undoable_baseline, count, runner)
            try:
                measure_family(seam_cases, count)
            finally:
                for variant_cases in seam_cases.values():
                    for case in variant_cases.values():
                        if "cleanup" in case:
                            case["cleanup"]()
        if include_cold:
            for variant in variants:
                observations = cold_generation_batches(
                    variant,
                    count,
                    warmups=warmups,
                    batches=batches,
                    worker_arguments=cold_worker_arguments,
                    observe=observe,
                )
                rows.extend(observations["rows"])
                calibration_rows.extend(
                    dict(
                        row,
                        fields=count,
                        case="decorate_cold",
                        variant=variant,
                        phase="calibration",
                    )
                    for row in observations["calibration_rows"]
                )
                sources[f"{count}:{variant}:decorate_cold"] = (
                    Path(__file__).with_name("cold_worker.py").read_text()
                )
                classifications[f"{count}:{variant}:decorate_cold"] = observations[
                    "sampling_note"
                ]
    for row in rows:
        row.update(units="ns/op", elapsed_units="ns")
    for row in calibration_rows:
        row.update(units="ns/op", elapsed_units="ns")
    return {
        "environment": environment(),
        "warmups": warmups,
        "measured_batches": batches,
        "minimum_calibration_ns": minimum_ns,
        "rows": rows,
        "memory": memory,
        "definition_boundary": "Dataclass families plus optional frozen-original Undoable seam; cold omitted unless explicitly selected",
        "undoable_seam_included": undoable_baseline is not None,
        "sources": sources,
        "classifications": classifications,
        "cold_included": include_cold,
        "calibration_rows": calibration_rows,
    }


if __name__ == "__main__":
    cli = sibling("perf_cli", "measure.py")
    raise SystemExit(cli.main())
