import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "perf_support", Path(__file__).with_name("measurement.py")
)
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)


class Accounting(unittest.TestCase):
    def test_preparation_is_outside_clock_boundary(self):
        events = []
        ticks = iter((100, 300))

        def clock():
            events.append("clock")
            return next(ticks)

        def prepare(count):
            events.append(("prepare", count))
            return "pool"

        def run(count, pool):
            events.append(("run", count, pool))
            return 9

        row = support.sample(run, 10, prepare=prepare, clock=clock)
        self.assertEqual(
            events, [("prepare", 10), "clock", ("run", 10, "pool"), "clock"]
        )
        self.assertEqual(row, {"operations": 10, "elapsed_ns": 200, "ns_per_op": 20.0})

    def test_zero_operations_rejected(self):
        with self.assertRaises(ValueError):
            support.sample(lambda n, p: None, 0)

    def test_calibration_reaches_minimum_duration(self):
        counts = []

        def measured(count):
            counts.append(count)
            return {"operations": count, "elapsed_ns": count * 10, "ns_per_op": 10.0}

        count = support.calibrate(measured, minimum_ns=200)
        self.assertGreaterEqual(count * 10, 200)
        self.assertEqual(counts[0], 1)

    def test_calibration_preserves_observed_batches(self):
        seen = []

        def measured(count):
            return {"operations": count, "elapsed_ns": count * 10, "ns_per_op": 10.0}

        count = support.calibrate(measured, minimum_ns=20, on_observation=seen.append)
        self.assertEqual(count, 3)
        self.assertEqual([row["operations"] for row in seen], [1, 3])
        self.assertEqual([row["elapsed_ns"] for row in seen], [10, 30])

    def test_ratios_are_paired_by_process(self):
        rows = support.summarize_pairs(
            [10, 10.2, 10.4, 10.6, 10.8],
            [5, 5.1, 5.2, 5.3, 5.4],
            target=2.0,
            seed=72,
            resamples=100,
        )
        self.assertEqual(rows["paired_ratios"], [2.0] * 5)
        self.assertEqual(rows["ratio_ci95"], [2.0, 2.0])
        self.assertEqual(rows["target_verdict"], "pass")

    def test_noise_and_straddling_remain_inconclusive(self):
        rows = support.summarize_pairs(
            [1, 3, 2, 4, 2], [1] * 5, target=2.0, seed=72, resamples=1000
        )
        self.assertEqual(rows["target_verdict"], "inconclusive")

    def test_units_distinguish_elapsed_and_normalized(self):
        row = support.sample(lambda n, p: None, 4, clock=iter((20, 28)).__next__)
        self.assertEqual(row["elapsed_ns"], 8)
        self.assertEqual(row["ns_per_op"], 2)

    def test_cold_batch_sums_only_worker_generator_intervals(self):
        observations = iter(
            (
                {"operations": 1, "elapsed_ns": 3, "pid": 4},
                {"operations": 1, "elapsed_ns": 7, "pid": 5},
            )
        )
        row = support.cold_sample(lambda: next(observations), 2)
        self.assertEqual(row["operations"], 2)
        self.assertEqual(row["elapsed_ns"], 10)
        self.assertEqual(row["ns_per_op"], 5)
        self.assertEqual([entry["pid"] for entry in row["cold_observations"]], [4, 5])

    def test_worker_failure_does_not_become_successful_sample(self):
        def failed():
            raise RuntimeError("worker failed")

        with self.assertRaisesRegex(RuntimeError, "worker failed"):
            support.cold_sample(failed, 1)

    def test_cold_worker_unit_rejected(self):
        with self.assertRaisesRegex(ValueError, "one first generation"):
            support.cold_sample(lambda: {"operations": 2, "elapsed_ns": 10}, 1)


if __name__ == "__main__":
    unittest.main()
