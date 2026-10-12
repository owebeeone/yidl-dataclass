"""Aggregate observed benchmark families; complete product coverage is a separate gate."""

import argparse
from collections import defaultdict
import importlib.util
import json
import math
from pathlib import Path
import statistics

spec = importlib.util.spec_from_file_location(
    "perf_support", Path(__file__).with_name("measurement.py")
)
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)


def summarize_memory(documents):
    by_minor = defaultdict(list)
    quantities = (
        "instance_shallow_bytes_per_object",
        "dict_shallow_bytes_per_object",
        "allocation_bytes_per_object_including_pool",
        "allocation_bytes_per_object_after_dict_inspection",
    )
    for document in documents:
        minor = ".".join(document["environment"]["python"].split()[0].split(".")[:2])
        seen = {}
        for row in document.get("memory", []):
            key = (row["fields"], row["case"], row["variant"])
            if key in seen:
                raise ValueError("duplicate memory case")
            if row["instances"] != 10000:
                raise ValueError("memory requires 10,000 instances per process")
            if row["units"] != "bytes/object":
                raise ValueError("memory unit must be bytes/object")
            if any(
                not math.isfinite(row[name]) or row[name] < 0 for name in quantities
            ):
                raise ValueError("memory observations must be finite and nonnegative")
            seen[key] = row
        by_minor[minor].append(seen)
    result = []

    def describe(values):
        median = statistics.median(values)
        return {
            "process_observations": values,
            "median": median,
            "min": min(values),
            "max": max(values),
            "iqr_over_median": (
                None
                if median == 0
                else (
                    support.percentile(values, 0.75) - support.percentile(values, 0.25)
                )
                / median
            ),
        }

    for minor, processes in sorted(by_minor.items()):
        keys = set(processes[0])
        if any(set(row) != keys for row in processes):
            raise ValueError("memory cases differ across processes")
        for fields, case, variant in sorted(keys):
            result.append(
                {
                    "minor": minor,
                    "fields": fields,
                    "case": case,
                    "variant": variant,
                    "units": "bytes/object",
                    "instances_per_process": 10000,
                    **{
                        name: describe(
                            [row[(fields, case, variant)][name] for row in processes]
                        )
                        for name in quantities
                    },
                    "pool_shallow_bytes_per_process": [
                        row[(fields, case, variant)]["list_pool_shallow_bytes"]
                        for row in processes
                    ],
                    "numerical_parity_target": None,
                }
            )
    return result


def summarize(documents):
    processes = defaultdict(list)
    seen = set()
    hashes = set()
    for document in documents:
        environment = document["environment"]
        minor = ".".join(environment["python"].split()[0].split(".")[:2])
        identity = (minor, environment["process_pid"])
        if identity in seen:
            raise ValueError("duplicate process observation")
        seen.add(identity)
        hashes.add((environment["harness_sha256"], environment["support_sha256"]))
        if (
            document["warmups"] != 10
            or document["measured_batches"] != 20
            or document["minimum_calibration_ns"] < 20_000_000
        ):
            raise ValueError("measurement configuration does not match accepted plan")
        groups = defaultdict(list)
        operation_counts = defaultdict(set)
        for row in document["rows"]:
            count = row["operations"]
            if type(count) is not int or count < 1:
                raise ValueError("invalid operation unit")
            if not math.isclose(
                row["ns_per_op"], row["elapsed_ns"] / count, rel_tol=1e-12
            ):
                raise ValueError("normalized unit does not reconcile")
            groups[(row["fields"], row["case"], row["variant"])].append(row)
            count_variant = row["variant"] if row["case"] == "decorate_cold" else None
            operation_counts[(row["fields"], row["case"], count_variant)].add(count)
        if any(len(counts) != 1 for counts in operation_counts.values()):
            raise ValueError("operation count differs within a paired case")
        medians = {}
        for key, rows in groups.items():
            warmup = [row["batch"] for row in rows if row["phase"] == "warmup"]
            measured = [row for row in rows if row["phase"] == "measurement"]
            if sorted(warmup) != list(range(-10, 0)) or sorted(
                row["batch"] for row in measured
            ) != list(range(20)):
                raise ValueError("missing or duplicate batch")
            if len(rows) != 30 or len({row["source_sha256"] for row in rows}) != 1:
                raise ValueError("batch source/configuration drift")
            medians[key] = statistics.median(row["ns_per_op"] for row in measured)
        processes[minor].append(medians)
    if len(hashes) != 1:
        raise ValueError("harness hash drift across process samples")
    result = {
        "scope": "observed families only; final coverage gate required",
        "comparisons": [],
        "absolute_product": [],
        "process_counts": {},
        "memory": summarize_memory(documents),
    }
    target_two = {
        "construct_supplied",
        "construct_defaults",
        "construct_factory",
        "repr",
        "eq_equal",
        "eq_early_mismatch",
        "eq_late_mismatch",
        "order",
        "hash",
    }
    for minor, medians in sorted(processes.items()):
        if len(medians) < 5:
            raise ValueError("at least five independent processes per minor required")
        keys = set(medians[0])
        if any(set(row) != keys for row in medians):
            raise ValueError("case families differ across process samples")
        result["process_counts"][minor] = len(medians)
        for fields, case, variant in sorted(keys):
            if variant != "product":
                continue
            values = [row[(fields, case, variant)] for row in medians]
            result["absolute_product"].append(
                {
                    "minor": minor,
                    "fields": fields,
                    "case": case,
                    "units": "ns/op",
                    "process_medians": values,
                    **support.descriptive(values),
                }
            )
            for baseline in (
                "stdlib_default",
                "stdlib_slots",
                "frozen_original",
                "structural_reference",
            ):
                key = (fields, case, baseline)
                if key not in keys:
                    continue
                target = 2.0 if case in target_two else None
                if case in ("slot_read", "slot_write") and baseline == "stdlib_slots":
                    target = 1.2
                comparison = support.summarize_pairs(
                    values, [row[key] for row in medians], target=target
                )
                result["comparisons"].append(
                    dict(
                        comparison,
                        minor=minor,
                        fields=fields,
                        case=case,
                        baseline=baseline,
                    )
                )
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--definition", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    definition = json.loads(args.definition.read_text())
    spec = importlib.util.spec_from_file_location(
        "perf_validation", Path(__file__).with_name("validation.py")
    )
    validation = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validation)
    validation.validate_definition(definition)
    documents = [json.loads(path.read_text()) for path in args.inputs]
    expected_digest = (
        __import__("hashlib")
        .sha256(json.dumps(definition, sort_keys=True, separators=(",", ":")).encode())
        .hexdigest()
    )
    for document in documents:
        if document.get("definition_sha256") != expected_digest:
            raise ValueError("raw source/definition drift")
        validation.validate(document, definition)
    result = summarize(documents)
    if set(result["process_counts"]) != set(definition["minors"]):
        raise ValueError("all three supported minors require independent process sets")
    result["scope"] = (
        "complete frozen inventory and process aggregation; targets unchanged"
    )
    result["definition_sha256"] = expected_digest
    result["raw_files"] = [
        {
            "name": path.name,
            "sha256": __import__("hashlib").sha256(path.read_bytes()).hexdigest(),
        }
        for path in args.inputs
    ]
    if args.output.exists():
        raise ValueError("summary exists; never overwrite prior result")
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
