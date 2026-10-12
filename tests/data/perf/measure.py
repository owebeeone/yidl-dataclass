"""Mandatory full-inventory benchmark CLI; invoked only after owner freezes definitions."""

import argparse
import datetime as dt
import importlib.util
import json
import os
from pathlib import Path
import sys


def load(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).with_name(filename)
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class Journal:
    """Append completed observations outside clocks; retain partial failed attempts."""

    def __init__(self, path):
        self.stream = path.open("x", encoding="utf-8")
        self.sequence = 0

    def append(self, kind, row):
        self.stream.write(
            json.dumps(
                {"sequence": self.sequence, "kind": kind, "observation": row},
                sort_keys=True,
            )
            + "\n"
        )
        self.stream.flush()
        os.fsync(self.stream.fileno())
        self.sequence += 1

    def close(self):
        self.stream.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--definition", required=True, type=Path)
    parser.add_argument("--artifact-root", required=True, type=Path)
    parser.add_argument("--sdk-wheel-dir", required=True, type=Path)
    parser.add_argument("--undoable-baseline-dir", required=True, type=Path)
    parser.add_argument("--undoable-baseline-wheel", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--process-label", required=True)
    parser.add_argument("--backend", choices=("native-rust",), default="native-rust")
    args = parser.parse_args()
    if any(
        path.exists()
        for path in (
            args.output,
            args.output.with_suffix(".attempt.json"),
            args.output.with_suffix(".journal.jsonl"),
        )
    ):
        raise ValueError("raw output exists; never overwrite observations")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    journal = Journal(args.output.with_suffix(".journal.jsonl"))
    journal.append(
        "started",
        {
            "process_label": args.process_label,
            "backend": args.backend,
            "process_pid": os.getpid(),
            "python": sys.version,
            "started_utc": dt.datetime.now(dt.UTC).isoformat(),
        },
    )
    try:
        return execute(args, journal)
    except BaseException as exc:
        journal.append("failure", {"exception_type": type(exc).__name__})
        raise
    finally:
        journal.close()


def execute(args, journal):
    os.environ["ASTICHI_LOWER_ENGINE"] = args.backend
    definition = json.loads(args.definition.read_text())
    validation = load("perf_validation", "validation.py")
    validation.validate_definition(definition)
    provenance = load("perf_provenance", "provenance.py")
    if provenance.source_hashes() != definition["source_sha256"]:
        raise ValueError("harness source drift from frozen definition")
    installed = provenance.verify_installation(
        definition["artifact_tuple"],
        args.artifact_root,
        args.sdk_wheel_dir,
        backend=args.backend,
    )
    if "minor_provenance" in definition:
        minor = ".".join(installed["python"].split(".")[:2])
        if installed != definition["minor_provenance"].get(minor):
            raise ValueError("installed provenance differs from frozen minor tuple")
    journal.append(
        "provenance",
        {
            "installed": installed,
            "definition_sha256": provenance.canonical_digest(definition),
        },
    )
    seam = load("perf_seam", "undoable_cases.py")
    baseline = seam.load_baseline(
        args.undoable_baseline_dir, wheel=args.undoable_baseline_wheel
    )
    harness = load("perf_harness", "harness.py")
    import yidl_dataclass

    journal.append("environment_before_measurement", harness.environment())

    worker_arguments = (
        "--definition",
        str(args.definition),
        "--artifact-root",
        str(args.artifact_root),
        "--sdk-wheel-dir",
        str(args.sdk_wheel_dir),
    )
    result = harness.run_process(
        yidl_dataclass,
        include_cold=True,
        undoable_baseline=baseline,
        cold_worker_arguments=worker_arguments,
        observe=journal.append,
    )
    result.update(
        provenance=installed,
        definition_sha256=provenance.canonical_digest(definition),
        process_label=args.process_label,
        frozen_original_undoable_wheel_sha256=seam.BASELINE_SHA256,
    )
    result["environment"]["provenance"] = installed
    result["environment"]["process_label"] = args.process_label
    # Preserve the complete attempt even when a late schema/coverage gate rejects it.
    args.output.with_suffix(".attempt.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    validation.validate(result, definition)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    journal.append("validated", {"definition_sha256": result["definition_sha256"]})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
