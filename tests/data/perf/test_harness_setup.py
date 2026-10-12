import dataclasses
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "harness", Path(__file__).with_name("harness.py")
)
harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harness)


class HarnessShape(unittest.TestCase):
    def test_case_inputs_and_write_isolation(self):
        cases = harness.ordinary_cases(dataclasses, 3, True)
        self.assertIs(cases["eq_equal"]["run"](1, None), True)
        cases["slot_write"]["run"](2, None)
        self.assertIs(cases["eq_equal"]["run"](1, None), True)
        self.assertIs(cases["eq_early_mismatch"]["run"](1, None), False)
        self.assertIs(cases["eq_late_mismatch"]["run"](1, None), False)
        self.assertIs(cases["order"]["run"](1, None), True)

    def test_batch_operation_count(self):
        obj = type("Counter", (), {"reads": 0})()
        run, _ = harness.runner("obj.reads += 1", {"obj": obj}, result="obj.reads")
        self.assertEqual(run(17, None), 17)
        self.assertEqual(obj.reads, 17)

    def test_multiline_exception_case_preserves_loop_scope(self):
        obj = type(
            "Rejector",
            (),
            {
                "__setattr__": lambda self, name, value: (_ for _ in ()).throw(
                    ValueError()
                )
            },
        )()
        run, _ = harness.runner(
            "try:\n    obj.value = 7\nexcept ValueError:\n    result = index",
            {"obj": obj},
        )
        self.assertEqual(run(17, None), 16)

    def test_memory_pool_and_units(self):
        row = harness.memory_row(harness.model(dataclasses, 3, slots=True), 10)
        self.assertEqual(row["instances"], 10)
        self.assertEqual(row["dict_shallow_bytes_per_object"], 0)
        self.assertEqual(row["units"], "bytes/object")
        self.assertGreater(row["list_pool_shallow_bytes"], 0)

    def test_repeated_generation_prepares_distinct_declarations(self):
        case = harness.generation_cases(dataclasses, 3, True)["decorate_repeated"]
        prepared = case["prepare"](7)
        self.assertEqual(len({id(item) for item in prepared}), 7)
        self.assertTrue(
            all("__dataclass_fields__" not in item.__dict__ for item in prepared)
        )
        generated = case["run"](7, prepared)
        self.assertEqual(dataclasses.asdict(generated()), {"f0": 0, "f1": 1, "f2": 2})
        self.assertTrue(
            all("__dataclass_fields__" in item.__dict__ for item in prepared)
        )

    def test_dictionary_inspection_allocation_boundary_is_explicit(self):
        row = harness.memory_row(harness.model(dataclasses, 3, slots=False), 100)
        self.assertEqual(
            row["allocation_boundary"],
            "pool initialization before getsizeof/dictionary inspection",
        )
        self.assertGreaterEqual(
            row["allocation_bytes_per_object_after_dict_inspection"],
            row["allocation_bytes_per_object_including_pool"],
        )
        self.assertGreater(row["dict_shallow_bytes_per_object"], 0)

    def test_readonly_rejection_is_handled_per_operation(self):
        cases = harness.readonly_cases(dataclasses, 3, True)
        self.assertEqual(cases["readonly_read"]["run"](1, None), 0)
        self.assertEqual(cases["readonly_reject"]["run"](17, None), 16)


if __name__ == "__main__":
    unittest.main()
