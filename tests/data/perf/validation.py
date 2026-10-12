"""Validate a measured document against a previously frozen inventory."""

from collections import defaultdict
import hashlib, json, math


def validate(document, definition):
    required = {tuple(row) for row in definition["timing_keys"]}
    actual = {}
    for row in document["rows"]:
        key = (row["fields"], row["case"], row["variant"])
        if type(row["operations"]) is not int or row["operations"] < 1:
            raise ValueError("measurement operation count must be positive integer")
        source_key = f"{row['fields']}:{row['variant']}:{row['case']}"
        if row["source_sha256"] != definition["timing_source_sha256"].get(source_key):
            raise ValueError("batch source digest differs from frozen definition")
        actual.setdefault(key, []).append(row)
    if set(actual) != required:
        raise ValueError("timing inventory differs from frozen definition")
    for key, rows in actual.items():
        warmups = definition.get("warmups", 10)
        measured = definition.get("measured_batches", 20)
        warm = [row.get("batch") for row in rows if row.get("phase") == "warmup"]
        samples = [
            row.get("batch") for row in rows if row.get("phase") == "measurement"
        ]
        if (
            len(rows) != warmups + measured
            or sorted(warm) != list(range(-warmups, 0))
            or sorted(samples) != list(range(measured))
        ):
            raise ValueError("missing, duplicate or unrecognized measured batch")
    for row in document["rows"]:
        if row.get("units") != "ns/op" or row.get("elapsed_units") != "ns":
            raise ValueError(
                "measurement normalization requires explicit ns/op and ns units"
            )
        if (
            type(row.get("elapsed_ns")) is not int
            or row["elapsed_ns"] < 0
            or not math.isfinite(row.get("ns_per_op", float("nan")))
            or not math.isclose(
                row["ns_per_op"], row["elapsed_ns"] / row["operations"], rel_tol=1e-12
            )
        ):
            raise ValueError("measurement normalization does not reconcile")
    calibration = defaultdict(list)
    for row in document["calibration_rows"]:
        key = (row["fields"], row["case"], row["variant"])
        if key not in required:
            raise ValueError("unknown calibration case")
        if type(row["operations"]) is not int or row["operations"] < 1:
            raise ValueError("calibration operation count must be positive integer")
        if not math.isclose(
            row["ns_per_op"], row["elapsed_ns"] / row["operations"], rel_tol=1e-12
        ):
            raise ValueError("calibration normalization does not reconcile")
        source_key = f"{row['fields']}:{row['variant']}:{row['case']}"
        if row.get("source_sha256") != definition["timing_source_sha256"].get(
            source_key
        ):
            raise ValueError("calibration source drift")
        if (
            row.get("units") != "ns/op"
            or row.get("elapsed_units") != "ns"
            or type(row["elapsed_ns"]) is not int
            or row["elapsed_ns"] < 0
        ):
            raise ValueError("calibration units must be nonnegative ns and ns/op")
        calibration[key].append(row)
    if set(calibration) != required:
        raise ValueError("calibration inventory differs from frozen definition")
    for key, rows in calibration.items():
        if rows[-1]["elapsed_ns"] < definition["minimum_calibration_ns"]:
            raise ValueError("case calibration did not reach declared minimum")
        if any(row["operations"] != rows[-1]["operations"] for row in actual[key]):
            # Ordinary pairing may intentionally choose a slower peer's larger count.
            if key[1] == "decorate_cold" or any(
                row["operations"] < rows[-1]["operations"] for row in actual[key]
            ):
                raise ValueError(
                    "measurement count not compatible with recorded calibration"
                )
    memory_keys = {tuple(row) for row in definition["memory_keys"]}
    if {
        (row["fields"], row["case"], row["variant"]) for row in document["memory"]
    } != memory_keys:
        raise ValueError("memory inventory differs from frozen definition")
    if len(document["memory"]) != len(memory_keys):
        raise ValueError("duplicate memory case")
    for row in document["memory"]:
        if (
            row.get("instances") != definition.get("memory_instances", 10_000)
            or row.get("units") != "bytes/object"
        ):
            raise ValueError("memory requires 10000 instances and bytes/object units")
        for name in (
            "instance_shallow_bytes_per_object",
            "dict_shallow_bytes_per_object",
            "allocation_bytes_per_object_including_pool",
            "allocation_bytes_per_object_after_dict_inspection",
            "list_pool_shallow_bytes",
        ):
            if not math.isfinite(row.get(name, float("nan"))) or row[name] < 0:
                raise ValueError("memory quantities must be finite and nonnegative")
    if "minor_provenance" in definition:
        validate_provenance(document, definition)
        for row in [*document["rows"], *document["calibration_rows"]]:
            if row["case"] == "decorate_cold":
                validate_cold(row, definition, document["provenance"])
    return {
        "timing_cases": len(required),
        "memory_cases": len(memory_keys),
        "calibration_observations": len(document["calibration_rows"]),
        "definition_sha256": hashlib.sha256(
            json.dumps(definition, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def expected_inventory():
    ordinary = (
        "slot_read",
        "slot_write",
        "construct_supplied",
        "construct_defaults",
        "construct_factory",
        "eq_equal",
        "eq_early_mismatch",
        "eq_late_mismatch",
        "order",
        "hash",
        "repr",
        "readonly_read",
        "readonly_reject",
        "decorate_repeated",
        "decorate_cold",
    )
    extension = (
        "pipeline_plain",
        "pipeline_converted",
        "pipeline_validated",
        "pipeline_both",
        "lazy_first",
        "lazy_cached",
        "construct_dependent",
        "source_emission",
        "harness_only",
    )
    writes = tuple(
        "undoable_value_scope:" + shape
        for shape in (
            "integer_equal",
            "opaque_equal",
            "child_alternate",
            "tuple_child_alternate",
            "dict_child_alternate",
        )
    )
    timing = {
        (count, name, variant)
        for count in (3, 12)
        for name in ordinary
        for variant in ("product", "stdlib_default", "stdlib_slots")
    }
    timing |= {(count, name, "product") for count in (3, 12) for name in extension}
    timing |= {
        (count, name, variant)
        for count in (3, 12)
        for name in writes
        for variant in ("product", "frozen_original")
    }
    timing |= {
        (count, "undoable_eq_prelude", variant)
        for count in (3, 12)
        for variant in ("product", "structural_reference")
    }
    memory = {
        (count, name, variant)
        for count in (3, 12)
        for name in ("ordinary", "frozen", "weakref", "local")
        for variant in ("product", "stdlib_default", "stdlib_slots")
    }
    memory |= {
        (count, name, "product")
        for count in (3, 12)
        for name in ("lazy_unready", "lazy_ready", "retained_shared", "retained_unique")
    }
    return timing, memory


def validate_definition(definition):
    timing, memory = expected_inventory()
    if set(map(tuple, definition["timing_keys"])) != timing or len(
        definition["timing_keys"]
    ) != len(timing):
        raise ValueError("frozen definition must contain complete132 timing inventory")
    if set(map(tuple, definition["memory_keys"])) != memory or len(
        definition["memory_keys"]
    ) != len(memory):
        raise ValueError("frozen definition must contain complete32 memory inventory")
    constants = {
        "minimum_calibration_ns": 20_000_000,
        "warmups": 10,
        "measured_batches": 20,
        "minimum_processes_per_minor": 5,
        "memory_instances": 10_000,
        "bootstrap_resamples": 10_000,
        "seed": 20261012,
        "noisy_iqr_over_median": 0.15,
        "slot_stdlib_slots_target": 1.2,
        "ordinary_target": 2.0,
    }
    if any(definition.get(name) != value for name, value in constants.items()):
        raise ValueError("frozen sampling definitions/gates differ from accepted plan")
    if definition.get("selected_backend") != "native-rust":
        raise ValueError(
            "primary frozen measurement backend must be original native-rust"
        )
    keys = {f"{count}:{variant}:{name}" for count, name, variant in timing}
    if (
        set(definition["timing_source_sha256"]) != keys
        or set(definition["timing_sources"]) != keys
    ):
        raise ValueError("frozen case source inventory incomplete")
    for key, source in definition["timing_sources"].items():
        if (
            hashlib.sha256(source.encode()).hexdigest()
            != definition["timing_source_sha256"][key]
        ):
            raise ValueError("frozen timing source digest mismatch")
    return {"timing_cases": len(timing), "memory_cases": len(memory)}


def validate_provenance(document, definition):
    provenance = document.get("provenance", {})
    minor = ".".join(provenance.get("python", "").split(".")[:2])
    if provenance != definition["minor_provenance"].get(minor):
        raise ValueError(
            "process provenance differs from frozen minor/source/artifact tuple"
        )
    environment = document.get("environment", {})
    if (
        environment.get("selected_backend") != definition["selected_backend"]
        or environment.get("fallback_scope") is not None
    ):
        raise ValueError("measured backend mismatch or fallback")
    if environment.get("python", "").split()[0] != provenance["python"]:
        raise ValueError("measured Python identity differs from provenance")
    if (
        document.get("definition_sha256")
        != hashlib.sha256(
            json.dumps(definition, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
    ):
        raise ValueError("raw definition drift")


def validate_cold(row, definition, provenance):
    observations = row.get("cold_observations", [])
    if len(observations) != row["operations"]:
        raise ValueError("missing cold worker observations")
    expected_digest = hashlib.sha256(
        json.dumps(definition, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    for observation in observations:
        if (
            observation.get("operations") != 1
            or observation.get("units") != "ns"
            or type(observation.get("elapsed_ns")) is not int
            or observation["elapsed_ns"] < 0
            or observation.get("source_sha256") != row["source_sha256"]
            or observation.get("selected_backend") != definition["selected_backend"]
            or observation.get("definition_sha256") != expected_digest
            or observation.get("provenance") != provenance
        ):
            raise ValueError("cold worker units/source/backend/provenance mismatch")
    if (
        sum(observation["elapsed_ns"] for observation in observations)
        != row["elapsed_ns"]
    ):
        raise ValueError("cold aggregate interval does not reconcile")
