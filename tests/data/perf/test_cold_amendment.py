"""Owner-amended cold one-worker sampling contract; synthetic observations only."""

import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import pytest


def load(name):
    spec = importlib.util.spec_from_file_location(
        "h2_" + name, Path(__file__).with_name(name + ".py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_cold_uses_one_pilot_worker_and_one_worker_per_batch(monkeypatch):
    harness = load("harness")
    calls = []
    observed = []

    def worker(*a, **kw):
        calls.append(1)
        return SimpleNamespace(
            returncode=0,
            stdout=json.dumps(
                {"operations": 1, "elapsed_ns": 10_000_000, "units": "ns"}
            ),
            stderr="",
        )

    monkeypatch.setattr(harness.subprocess, "run", worker)
    result = harness.cold_generation_batches(
        "stdlib_slots", 3, observe=lambda kind, row: observed.append((kind, row))
    )
    assert len(calls) == 31
    assert all(row["operations"] == 1 for row in result["rows"])
    assert len(result["pilot_rows"]) == 1 and result["pilot_rows"][0]["operations"] == 1
    assert result["pilot_rows"][0]["phase"] == "pilot"
    assert len([row for kind, row in observed if kind == "cold_worker"]) == 31


def cold_inputs():
    document, definition = load("test_validation").inputs()
    definition["timing_keys"] = [[3, "decorate_cold", "product"]]
    definition["timing_source_sha256"] = {"3:product:decorate_cold": "expected"}
    definition.update(
        cold_sampling="single_fresh_worker", cold_operations=1, cold_pilot_operations=1
    )
    for row in document["rows"]:
        row.update(case="decorate_cold", operations=1, elapsed_ns=10, ns_per_op=10)
    document["calibration_rows"] = []
    document["cold_pilot_rows"] = [dict(document["rows"][0], phase="pilot", batch=None)]
    return document, definition


def test_cold_pilot_is_exempt_but_ordinary_minimum_is_mandatory():
    validation = load("validation")
    document, definition = cold_inputs()
    assert validation.validate(document, definition)["timing_cases"] == 1
    ordinary, standard = load("test_validation").inputs()
    ordinary["calibration_rows"][0].update(elapsed_ns=3, ns_per_op=1)
    with pytest.raises(ValueError, match="minimum"):
        validation.validate(ordinary, standard)


def test_cold_count_greater_than_one_is_rejected():
    validation = load("validation")
    document, definition = cold_inputs()
    for row in document["rows"]:
        row.update(operations=2, elapsed_ns=20)
    document["calibration_rows"] = [dict(document["rows"][0], phase="calibration")]
    with pytest.raises(ValueError, match="cold.*count"):
        validation.validate(document, definition)


def full_inputs():
    import copy

    provenance = load("provenance")
    root = Path(__file__).resolve().parents[3]
    definition = json.loads(
        (root / "docs/validation/stage-h-preparation/definition.json").read_text()
    )
    definition.update(
        cold_sampling="single_fresh_worker", cold_operations=1, cold_pilot_operations=1
    )
    installed = copy.deepcopy(definition["minor_provenance"]["3.12"])
    document = {
        "rows": [],
        "cold_sampling": "single_fresh_worker",
        "cold_operations": 1,
        "calibration_rows": [],
        "cold_pilot_rows": [],
        "memory": [],
        "provenance": installed,
        "definition_sha256": provenance.canonical_digest(definition),
        "environment": {
            "python": installed["python"],
            "selected_backend": "native-rust",
            "fallback_scope": None,
        },
    }
    for fields, case, variant in definition["timing_keys"]:
        cold = case == "decorate_cold"
        n = 1 if cold else 100
        elapsed = 10_000 if cold else 20_000_000
        row = {
            "fields": fields,
            "case": case,
            "variant": variant,
            "operations": n,
            "elapsed_ns": elapsed,
            "ns_per_op": elapsed / n,
            "units": "ns/op",
            "elapsed_units": "ns",
            "source_sha256": definition["timing_source_sha256"][
                f"{fields}:{variant}:{case}"
            ],
        }
        if cold:
            row["cold_observations"] = [
                {
                    "operations": 1,
                    "elapsed_ns": elapsed,
                    "units": "ns",
                    "source_sha256": row["source_sha256"],
                    "selected_backend": "native-rust",
                    "definition_sha256": document["definition_sha256"],
                    "provenance": installed,
                    "pid": 123,
                }
            ]
            document["cold_pilot_rows"].append(dict(row, phase="pilot", batch=None))
        else:
            document["calibration_rows"].append(dict(row, phase="calibration"))
        document["rows"].extend(
            dict(row, phase="warmup" if i < 0 else "measurement", batch=i)
            for i in range(-10, 20)
        )
    for fields, case, variant in definition["memory_keys"]:
        document["memory"].append(
            {
                "fields": fields,
                "case": case,
                "variant": variant,
                "instances": 10000,
                "units": "bytes/object",
                "instance_shallow_bytes_per_object": 1,
                "dict_shallow_bytes_per_object": 0,
                "allocation_bytes_per_object_including_pool": 1,
                "allocation_bytes_per_object_after_dict_inspection": 1,
                "list_pool_shallow_bytes": 1,
            }
        )
    return document, definition


def test_full_synthetic_inventory_pilots_and_source_provenance_isolation():
    import copy

    validation = load("validation")
    document, definition = full_inputs()
    result = validation.validate(document, definition)
    assert result["timing_cases"] == 132 and result["memory_cases"] == 32
    assert result["cold_pilot_observations"] == 6
    for mutant, match in [
        ("pilot", "pilot inventory"),
        ("source", "cold worker"),
        ("provenance", "cold worker"),
        ("definition", "definition drift"),
    ]:
        bad = copy.deepcopy(document)
        if mutant == "pilot":
            bad["cold_pilot_rows"].pop()
        elif mutant == "source":
            bad["cold_pilot_rows"][0]["cold_observations"][0][
                "source_sha256"
            ] = "not-original"
        elif mutant == "provenance":
            bad["cold_pilot_rows"][0]["cold_observations"][0]["provenance"] = {}
        else:
            bad["definition_sha256"] = "v1-definition"
        with pytest.raises(ValueError, match=match):
            validation.validate(bad, definition)


def test_v1_definition_cannot_be_interpreted_as_h2():
    root = Path(__file__).resolve().parents[3]
    old = json.loads(
        (root / "docs/validation/stage-h-preparation/definition.json").read_text()
    )
    with pytest.raises(ValueError, match="sampling definitions"):
        load("validation").validate_definition(old)


def test_full_result_cannot_claim_historical_sum_policy():
    document, definition = full_inputs()
    document.update(cold_sampling="historical_sum", cold_operations=1)
    with pytest.raises(ValueError, match="cold sampling policy"):
        load("validation").validate(document, definition)
