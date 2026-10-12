"""Measurement/accounting; no product dependency or performance claims."""

import math
import random
import statistics
import time


def sample(run, count, *, prepare=None, clock=time.perf_counter_ns):
    if type(count) is not int or count < 1:
        raise ValueError("operations must be a positive integer")
    prepared = prepare(count) if prepare is not None else None
    start = clock()
    consumed = run(count, prepared)
    elapsed = clock() - start
    # Keep the returned observation live until after the measurement boundary.
    del consumed
    if elapsed < 0:
        raise ValueError("clock must be monotonic")
    return {"operations": count, "elapsed_ns": elapsed, "ns_per_op": elapsed / count}


def cold_sample(worker, count, *, on_observation=None):
    if type(count) is not int or count < 1:
        raise ValueError("operations must be a positive integer")
    observations = []
    for _ in range(count):
        row = worker()
        if type(row["operations"]) is not int or row["operations"] != 1:
            raise ValueError("cold worker must observe one first generation")
        if type(row["elapsed_ns"]) is not int or row["elapsed_ns"] < 0:
            raise ValueError("cold worker elapsed unit must be nonnegative nanoseconds")
        observations.append(row)
        if on_observation is not None:
            on_observation(row)
    elapsed = sum(row["elapsed_ns"] for row in observations)
    return {
        "operations": count,
        "elapsed_ns": elapsed,
        "ns_per_op": elapsed / count,
        "cold_observations": observations,
        "timing_boundary": "sum of worker generator intervals; import/setup/transport excluded",
    }


def calibrate(
    measured, *, minimum_ns=20_000_000, maximum_count=100_000_000, on_observation=None
):
    if minimum_ns <= 0 or maximum_count < 1:
        raise ValueError("calibration limits must be positive")
    count = 1
    while True:
        row = measured(count)
        if on_observation is not None:
            on_observation(row)
        elapsed = row["elapsed_ns"]
        if elapsed >= minimum_ns:
            return count
        if count >= maximum_count:
            raise RuntimeError("calibration did not reach minimum batch duration")
        scale = (
            10
            if elapsed == 0
            else min(10, max(2, math.ceil(minimum_ns / elapsed * 1.1)))
        )
        count = min(maximum_count, count * scale)


def percentile(values, fraction):
    ordered = sorted(values)
    if not ordered:
        raise ValueError("observations are required")
    index = (len(ordered) - 1) * fraction
    lower = int(index)
    upper = min(len(ordered) - 1, lower + 1)
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (index - lower)


def descriptive(values):
    if not values or any(value <= 0 or not math.isfinite(value) for value in values):
        raise ValueError("finite positive observations are required")
    median = statistics.median(values)
    return {
        "median": median,
        "min": min(values),
        "max": max(values),
        "iqr_over_median": (percentile(values, 0.75) - percentile(values, 0.25))
        / median,
    }


def summarize_pairs(product, baseline, *, target=None, seed=20261012, resamples=10_000):
    if len(product) != len(baseline) or len(product) < 5:
        raise ValueError("at least five complete process pairs are required")
    if resamples < 1:
        raise ValueError("resamples must be positive")
    p = descriptive(product)
    b = descriptive(baseline)
    ratios = [left / right for left, right in zip(product, baseline)]
    generator = random.Random(seed)
    samples = [
        statistics.median(generator.choices(ratios, k=len(ratios)))
        for _ in range(resamples)
    ]
    interval = [percentile(samples, 0.025), percentile(samples, 0.975)]
    noisy = p["iqr_over_median"] > 0.15 or b["iqr_over_median"] > 0.15
    verdict = None
    if target is not None:
        if noisy:
            verdict = "inconclusive"
        elif interval[0] > target:
            verdict = "regression"
        elif interval[1] <= target:
            verdict = "pass"
        else:
            verdict = "inconclusive"
    return {
        "product_ns_per_op": p,
        "baseline_ns_per_op": b,
        "paired_ratios": ratios,
        "ratio_median": statistics.median(ratios),
        "ratio_ci95": interval,
        "noisy": noisy,
        "target": target,
        "target_verdict": verdict,
        "bootstrap_seed": seed,
        "bootstrap_resamples": resamples,
        "bootstrap_statistic": "median of process-paired ratios",
    }
