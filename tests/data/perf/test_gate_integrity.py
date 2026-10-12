"""New H integration contract tests written before fixing prototype gaps."""

import gc
import importlib.util
from pathlib import Path
import tracemalloc
import pytest


def load(name):
    path = Path(__file__).with_name(name + ".py")
    spec = importlib.util.spec_from_file_location("gate_" + name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_complete_inventory_cannot_accept_one_batch_per_case():
    validation = load("validation")
    definition = {
        "timing_keys": [[3, "slot_read", "product"]],
        "memory_keys": [],
        "minimum_calibration_ns": 20,
        "warmups": 10,
        "measured_batches": 20,
        "timing_source_sha256": {"3:product:slot_read": "source"},
    }
    document = {
        "rows": [
            {
                "fields": 3,
                "case": "slot_read",
                "variant": "product",
                "operations": 3,
                "elapsed_ns": 30,
                "ns_per_op": 10,
                "phase": "measurement",
                "batch": 0,
                "source_sha256": "source",
            }
        ],
        "calibration_rows": [
            {
                "fields": 3,
                "case": "slot_read",
                "variant": "product",
                "operations": 3,
                "elapsed_ns": 30,
                "ns_per_op": 10,
            }
        ],
        "memory": [],
    }
    with pytest.raises(ValueError, match="batch"):
        validation.validate(document, definition)


def test_memory_failure_always_stops_tracing():
    harness = load("harness")

    class Broken:
        def __init__(self):
            raise RuntimeError("allocation failed")

    try:
        with pytest.raises(RuntimeError, match="allocation failed"):
            harness.memory_row(Broken, 10)
        assert not tracemalloc.is_tracing()
    finally:
        tracemalloc.stop()
        gc.collect()


def test_unverified_baseline_package_is_rejected_before_execution(tmp_path):
    seam = load("undoable_cases")
    (tmp_path / "__init__.py").write_text("unverified_source = True\n")
    with pytest.raises(ValueError, match="baseline"):
        seam.load_baseline(tmp_path)


def test_raw_measurement_units_are_validated_before_aggregation():
    validation = load("validation")
    fixture = load("test_validation")
    document, definition = fixture.inputs()
    for row in document["rows"]:
        row.update(elapsed_ns=30, ns_per_op=10, units="ns/op", elapsed_units="ns")
    document["rows"][0]["ns_per_op"] = 999
    with pytest.raises(ValueError, match="normaliz"):
        validation.validate(document, definition)


def test_public_measurement_cli_requires_frozen_definition():
    import subprocess
    import sys

    result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("harness.py")), "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "--definition" in result.stdout
    assert "--artifact-root" in result.stdout
    assert "--sdk-wheel-dir" in result.stdout
    assert "--include-cold" not in result.stdout  # Full inventory is mandatory.


def test_cold_worker_cli_requires_same_frozen_tuple_and_untimed_setup_mode():
    import subprocess
    import sys

    result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("cold_worker.py")), "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "--definition" in result.stdout and "--artifact-root" in result.stdout
    assert "--setup-only" in result.stdout


def test_completed_cold_observation_survives_later_worker_failure():
    import inspect

    measurement = load("measurement")
    completed = []
    calls = 0

    def worker():
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError("next worker failed")
        return {"operations": 1, "elapsed_ns": 10}

    options = (
        {"on_observation": completed.append}
        if "on_observation" in inspect.signature(measurement.cold_sample).parameters
        else {}
    )
    with pytest.raises(RuntimeError, match="next worker failed"):
        measurement.cold_sample(worker, 2, **options)
    assert completed == [{"operations": 1, "elapsed_ns": 10}]


def test_failed_final_validation_preserves_completed_result(tmp_path, monkeypatch):
    import json
    import sys
    from types import SimpleNamespace

    measure = load("measure")
    definition_path = tmp_path / "definition.json"
    definition_path.write_text(json.dumps({"source_sha256": {}, "artifact_tuple": {}}))
    output = tmp_path / "result.json"
    result = {"environment": {}, "rows": [{"completed": True}], "memory": []}
    validation = SimpleNamespace(
        validate_definition=lambda d: None,
        validate=lambda *a: (_ for _ in ()).throw(ValueError("late validation")),
    )
    provenance = SimpleNamespace(
        source_hashes=lambda: {},
        verify_installation=lambda *a, **kw: {},
        canonical_digest=lambda d: "digest",
    )
    seam = SimpleNamespace(
        load_baseline=lambda *a, **kw: object(), BASELINE_SHA256="baseline"
    )
    harness = SimpleNamespace(
        run_process=lambda *a, **kw: result, environment=lambda: {}
    )
    monkeypatch.setattr(
        measure,
        "load",
        lambda name, filename: {
            "validation.py": validation,
            "provenance.py": provenance,
            "undoable_cases.py": seam,
            "harness.py": harness,
        }[filename],
    )
    monkeypatch.setitem(sys.modules, "yidl_dataclass", SimpleNamespace())
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "measure.py",
            "--definition",
            str(definition_path),
            "--artifact-root",
            str(tmp_path),
            "--sdk-wheel-dir",
            str(tmp_path),
            "--undoable-baseline-dir",
            str(tmp_path),
            "--undoable-baseline-wheel",
            str(tmp_path / "wheel"),
            "--output",
            str(output),
            "--process-label",
            "synthetic",
        ],
    )
    with pytest.raises(ValueError, match="late validation"):
        measure.main()
    assert (
        not output.exists()
    )  # Final valid JSON is never published for a failed attempt.
    assert json.loads(output.with_suffix(".attempt.json").read_text())["rows"] == [
        {"completed": True}
    ]


def test_complete_memory_gate_rejects_wrong_units_and_instance_count():
    validation = load("validation")
    document, definition = load("test_validation").inputs()
    document["memory"][0].update(instances=1, units="kilobytes/object")
    with pytest.raises(ValueError, match="memory"):
        validation.validate(document, definition)


def test_calibration_source_drift_is_rejected():
    validation = load("validation")
    document, definition = load("test_validation").inputs()
    document["calibration_rows"][0]["source_sha256"] = "different"
    with pytest.raises(ValueError, match="calibration source"):
        validation.validate(document, definition)


def test_journal_is_append_only_and_survives_failure(tmp_path):
    import json

    measure = load("measure")
    path = tmp_path / "observations.jsonl"
    journal = measure.Journal(path)
    try:
        journal.append("calibration", {"elapsed_ns": 10})
        journal.append("cold_worker", {"elapsed_ns": 20})
        journal.append("failure", {"exception_type": "RuntimeError"})
    finally:
        journal.close()
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    assert [row["sequence"] for row in rows] == [0, 1, 2]
    assert [row["kind"] for row in rows] == ["calibration", "cold_worker", "failure"]
    with pytest.raises(FileExistsError):
        measure.Journal(path)


def test_common_definition_retains_all_minor_provenance_and_rejects_drift():
    import copy

    freeze = load("freeze_definition")
    rows = [
        {
            "minors": ["3.12", "3.13", "3.14"],
            "source": "same",
            "provenance": {"python": minor + ".1"},
        }
        for minor in ("3.12", "3.13", "3.14")
    ]
    result = freeze.merge(rows)
    assert set(result["minor_provenance"]) == {"3.12", "3.13", "3.14"}
    assert "provenance" not in result
    bad = copy.deepcopy(rows)
    bad[1]["source"] = "different"
    with pytest.raises(ValueError, match="drift"):
        freeze.merge(bad)
    with pytest.raises(ValueError, match="three"):
        freeze.merge(rows[:2])


def test_process_completed_calibrations_timings_and_memory_are_observed(monkeypatch):
    harness = load("harness")
    observed = []
    case = {"run": lambda n, pool: n, "prepare": None, "source": "synthetic"}
    monkeypatch.setattr(harness, "ordinary_cases", lambda *a: {"test": case})
    monkeypatch.setattr(harness, "readonly_cases", lambda *a: {})
    monkeypatch.setattr(harness, "generation_cases", lambda *a: {})
    monkeypatch.setattr(harness, "extension_cases", lambda *a: {})
    monkeypatch.setattr(harness, "source_emission_case", lambda *a: case)
    monkeypatch.setattr(harness, "runner", lambda *a: (case["run"], "synthetic"))
    monkeypatch.setattr(harness, "model", lambda *a, **kw: type("Synthetic", (), {}))
    monkeypatch.setattr(harness, "memory_models", lambda *a: {})
    monkeypatch.setattr(harness, "memory_row", lambda *a, **kw: {"instances": 10000})
    monkeypatch.setattr(harness, "environment", lambda: {})
    # Synthetic accounting only: neither real clock nor product case is invoked.
    monkeypatch.setattr(
        harness.support,
        "sample",
        lambda *a, **kw: {"operations": 1, "elapsed_ns": 20, "ns_per_op": 20},
    )

    def calibrate(measured, **kw):
        kw["on_observation"](measured(1))
        return 1

    monkeypatch.setattr(harness.support, "calibrate", calibrate)
    result = harness.run_process(
        object(),
        warmups=1,
        batches=1,
        observe=lambda kind, row: observed.append((kind, dict(row))),
    )
    for kind, name in (
        ("calibration", "calibration_rows"),
        ("timing", "rows"),
        ("memory", "memory"),
    ):
        assert [row for actual, row in observed if actual == kind] == result[name]


def test_cold_worker_journal_retains_worker_ns_unit(monkeypatch):
    import json
    from types import SimpleNamespace

    harness = load("harness")
    seen = []
    monkeypatch.setattr(
        harness.subprocess,
        "run",
        lambda *a, **kw: SimpleNamespace(
            returncode=0,
            stdout=json.dumps({"operations": 1, "elapsed_ns": 20, "units": "ns"}),
            stderr="",
        ),
    )

    def calibrate(measured, **kw):
        kw["on_observation"](measured(1))
        return 1

    monkeypatch.setattr(harness.support, "calibrate", calibrate)
    harness.cold_generation_batches(
        "product",
        3,
        warmups=0,
        batches=0,
        observe=lambda kind, row: seen.append((kind, row)),
    )
    assert seen[0][0] == "cold_worker" and seen[0][1]["units"] == "ns"
    assert seen[1][0] == "cold_pilot" and seen[1][1]["units"] == "ns/op"
