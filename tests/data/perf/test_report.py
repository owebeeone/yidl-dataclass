import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "perf_summary", Path(__file__).with_name("report.py")
)
summary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(summary)


def document(pid, product_ns=10):
    rows = []
    for variant, value in [
        ("product", product_ns),
        ("stdlib_default", 8),
        ("stdlib_slots", 10),
    ]:
        for batch in range(-10, 20):
            rows.append(
                {
                    "variant": variant,
                    "case": "slot_read",
                    "fields": 3,
                    "batch": batch,
                    "phase": "warmup" if batch < 0 else "measurement",
                    "operations": 100,
                    "elapsed_ns": value * 100,
                    "ns_per_op": value,
                    "source_sha256": "abc",
                }
            )
    return {
        "environment": {
            "python": "3.12.12",
            "process_pid": pid,
            "harness_sha256": "h",
            "support_sha256": "s",
        },
        "warmups": 10,
        "measured_batches": 20,
        "minimum_calibration_ns": 20_000_000,
        "rows": rows,
    }


class Completeness(unittest.TestCase):
    def test_process_medians_precede_ratios(self):
        result = summary.summarize([document(i) for i in range(5)])
        row = result["comparisons"][0]
        self.assertEqual(row["product_ns_per_op"]["median"], 10)
        self.assertEqual(row["baseline"], "stdlib_default")
        self.assertEqual(row["target"], None)
        slots = result["comparisons"][1]
        self.assertEqual(slots["target"], 1.2)
        self.assertEqual(slots["target_verdict"], "pass")

    def test_undoable_pairs_report_explicit_references_without_targets(self):
        documents = [document(i) for i in range(5)]
        for item in documents:
            item["rows"] = [
                row for row in item["rows"] if row["variant"] != "stdlib_slots"
            ]
            for row in item["rows"]:
                row["case"] = "undoable_value_scope:integer_equal"
                if row["variant"] == "stdlib_default":
                    row["variant"] = "frozen_original"
        result = summary.summarize(documents)
        self.assertEqual(len(result["comparisons"]), 1)
        self.assertEqual(result["comparisons"][0]["baseline"], "frozen_original")
        self.assertIsNone(result["comparisons"][0]["target"])
        for item in documents:
            for row in item["rows"]:
                row["case"] = "undoable_eq_prelude"
                if row["variant"] == "frozen_original":
                    row["variant"] = "structural_reference"
        result = summary.summarize(documents)
        self.assertEqual(result["comparisons"][0]["baseline"], "structural_reference")
        self.assertIsNone(result["comparisons"][0]["target"])

    def test_missing_measured_batch_rejected(self):
        documents = [document(i) for i in range(5)]
        documents[0]["rows"].pop()
        with self.assertRaisesRegex(ValueError, "batch"):
            summary.summarize(documents)

    def test_duplicate_process_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            summary.summarize([document(0) for _ in range(5)])

    def test_fewer_processes_rejected(self):
        with self.assertRaisesRegex(ValueError, "five"):
            summary.summarize([document(i) for i in range(4)])

    def test_wrong_normalized_unit_rejected(self):
        documents = [document(i) for i in range(5)]
        documents[0]["rows"][0]["ns_per_op"] = 1
        with self.assertRaisesRegex(ValueError, "unit"):
            summary.summarize(documents)

    def test_unpaired_operation_counts_rejected(self):
        documents = [document(i) for i in range(5)]
        row = documents[0]["rows"][0]
        row["operations"] = 200
        row["elapsed_ns"] = row["ns_per_op"] * 200
        with self.assertRaisesRegex(ValueError, "operation count"):
            summary.summarize(documents)

    def test_memory_aggregates_process_observations_with_zero_dict(self):
        documents = [document(i) for i in range(5)]
        for i, item in enumerate(documents):
            item["memory"] = [
                {
                    "case": "ordinary",
                    "variant": "product",
                    "fields": 3,
                    "instances": 10000,
                    "units": "bytes/object",
                    "instance_shallow_bytes_per_object": 80 + i,
                    "dict_shallow_bytes_per_object": 0,
                    "allocation_bytes_per_object_including_pool": 90 + i,
                    "allocation_bytes_per_object_after_dict_inspection": 100 + i,
                    "list_pool_shallow_bytes": 85200,
                }
            ]
        result = summary.summarize(documents)
        row = result["memory"][0]
        self.assertEqual(row["instance_shallow_bytes_per_object"]["median"], 82)
        self.assertEqual(row["dict_shallow_bytes_per_object"]["median"], 0)
        self.assertEqual(
            row["allocation_bytes_per_object_including_pool"]["median"], 92
        )
        self.assertEqual(
            row["allocation_bytes_per_object_after_dict_inspection"]["median"], 102
        )
        self.assertEqual(row["instances_per_process"], 10000)
        self.assertEqual(row["units"], "bytes/object")

    def test_memory_wrong_sample_count_rejected(self):
        documents = [document(i) for i in range(5)]
        for item in documents:
            item["memory"] = [
                {
                    "case": "ordinary",
                    "variant": "product",
                    "fields": 3,
                    "instances": 99,
                    "units": "bytes/object",
                    "instance_shallow_bytes_per_object": 80,
                    "dict_shallow_bytes_per_object": 0,
                    "allocation_bytes_per_object_including_pool": 90,
                    "allocation_bytes_per_object_after_dict_inspection": 100,
                    "list_pool_shallow_bytes": 85200,
                }
            ]
        with self.assertRaisesRegex(ValueError, "10,000"):
            summary.summarize(documents)

    def test_cold_generation_single_worker_rows_have_no_numeric_target(self):
        documents = [document(i) for i in range(5)]
        for item in documents:
            for row in item["rows"]:
                row["case"] = "decorate_cold"
                row["operations"] = 1
                row["elapsed_ns"] = row["ns_per_op"]
        result = summary.summarize(documents)
        self.assertEqual(result["comparisons"][0]["target"], None)


if __name__ == "__main__":
    unittest.main()
