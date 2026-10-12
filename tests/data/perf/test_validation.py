import importlib.util, pathlib, unittest

spec = importlib.util.spec_from_file_location(
    "coverage", pathlib.Path(__file__).with_name("validation.py")
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def inputs():
    definition = {
        "timing_keys": [[3, "slot_read", "product"]],
        "memory_keys": [[3, "ordinary", "product"]],
        "minimum_calibration_ns": 20,
        "timing_source_sha256": {"3:product:slot_read": "expected"},
    }
    document = {
        "rows": [
            {
                "fields": 3,
                "case": "slot_read",
                "variant": "product",
                "operations": 3,
                "source_sha256": "expected",
                "elapsed_ns": 30,
                "ns_per_op": 10,
                "units": "ns/op",
                "elapsed_units": "ns",
                "phase": "warmup" if batch < 0 else "measurement",
                "batch": batch,
            }
            for batch in range(-10, 20)
        ],
        "calibration_rows": [
            {
                "fields": 3,
                "case": "slot_read",
                "variant": "product",
                "operations": 3,
                "elapsed_ns": 30,
                "ns_per_op": 10,
                "units": "ns/op",
                "elapsed_units": "ns",
                "source_sha256": "expected",
            }
        ],
        "memory": [
            {
                "fields": 3,
                "case": "ordinary",
                "variant": "product",
                "instances": 10000,
                "units": "bytes/object",
                "instance_shallow_bytes_per_object": 1,
                "dict_shallow_bytes_per_object": 0,
                "allocation_bytes_per_object_including_pool": 1,
                "allocation_bytes_per_object_after_dict_inspection": 1,
                "list_pool_shallow_bytes": 1,
            }
        ],
    }
    return document, definition


class Integrity(unittest.TestCase):
    def test_complete_inventory_and_calibration(self):
        document, definition = inputs()
        row = module.validate(document, definition)
        self.assertEqual(row["timing_cases"], 1)
        self.assertEqual(row["memory_cases"], 1)

    def test_missing_family_rejects(self):
        document, definition = inputs()
        document["rows"] = []
        with self.assertRaisesRegex(ValueError, "inventory"):
            module.validate(document, definition)

    def test_short_calibration_rejects(self):
        document, definition = inputs()
        document["calibration_rows"][0].update(elapsed_ns=3, ns_per_op=1)
        with self.assertRaisesRegex(ValueError, "minimum"):
            module.validate(document, definition)

    def test_larger_paired_count_is_allowed(self):
        document, definition = inputs()
        for row in document["rows"]:
            row.update(operations=9, elapsed_ns=90)
        self.assertEqual(module.validate(document, definition)["timing_cases"], 1)

    def test_cold_count_must_match_own_variant(self):
        document, definition = inputs()
        definition["timing_keys"][0][1] = "decorate_cold"
        definition["timing_source_sha256"] = {"3:product:decorate_cold": "expected"}
        for row in document["rows"]:
            row.update(case="decorate_cold", operations=9, elapsed_ns=90)
        document["calibration_rows"][0]["case"] = "decorate_cold"
        with self.assertRaisesRegex(ValueError, "count"):
            module.validate(document, definition)

    def test_row_source_drift_rejects(self):
        document, definition = inputs()
        document["rows"][0]["source_sha256"] = "different"
        with self.assertRaisesRegex(ValueError, "source"):
            module.validate(document, definition)

    def test_nonpositive_calibration_count_rejects(self):
        document, definition = inputs()
        document["calibration_rows"][0]["operations"] = 0
        with self.assertRaisesRegex(ValueError, "operation"):
            module.validate(document, definition)

    def test_extra_memory_case_rejects(self):
        document, definition = inputs()
        document["memory"].append(
            {"fields": 3, "case": "unknown", "variant": "product"}
        )
        with self.assertRaisesRegex(ValueError, "memory inventory"):
            module.validate(document, definition)


if __name__ == "__main__":
    unittest.main()
