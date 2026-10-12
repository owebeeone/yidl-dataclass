# Frozen benchmark preparation

Stage H2 preparation defines 132 timing cases and 32 memory cases, at 3 and 12
fields. The candidate definition is
`docs/validation/stage-h2-preparation/definition.json`. This preparation contains
no product performance observations or numerical verdict. Owner review and a
committed definition freeze precede measurement.

`cases.py` owns untimed declarations and identical loop sources. `harness.py`
coordinates calibrated paired batches; `measurement.py` owns accounting and
statistics. `memory.py` separates allocation from dictionary inspection.
`undoable_cases.py` verifies the frozen original consumer wheel before loading
its extracted package; its handwritten facade equality reference is benchmark
code, not a correctness oracle or product generator. `cold_worker.py` isolates
first decoration in a new interpreter. `provenance.py`, `definition.py`,
`freeze_definition.py`, `validation.py`, `measure.py`, and `report.py` enforce the
source, artifact, inventory, and reporting boundaries.

The final setup selects the original `native-rust` backend explicitly. Installed
consumer and original SDK payload bytes must match the Stage G wheel tuple.
Module origins must lie under the isolated interpreter prefix. Each supported
minor has an exact Python patch, stdlib dataclasses source digest, installed
payload inventory, and harness source map in the common definition. A source,
artifact, version, or backend mismatch fails before a measured interval. SDKs
and Lifecycle are unchanged reference dependencies. Only the two consumer
wheels were built for the frozen tuple.

Every case source and all harness Python files have recorded hashes. Memory
model factories and allocation/inspection sources are identified separately;
stdlib implementations have per-minor source hashes. Repeated generation uses
fresh declarations prepared before each timed batch. Source emission measures
the actual captured composable's `emit_commented()` call; capture and cleanup
occur outside the clock. It does not time an exported string cache.

Ordinary paired cases use the maximum of each variant's calibration count,
alternating variant order. Calibration reaches a 20 ms measured batch, followed
by 10 warmups and 20 retained measured batches. `lazy_first` prepares one UNREADY
instance per operation outside the clock; `lazy_cached` prepares separate READY
instances. Undoable alternating writes reset to the right operand outside each
batch so every operation changes node identity. Setup verifies each change
without adding instrumentation to measured runs. Integer/opaque-equal setter
cases skip storage using the original public setter path. Facade prelude costs
and extension/generation/memory costs have no numerical parity target.

Cold generation follows the owner's explicit `dev-docs/ColdSamplingAmendment.md`.
Every variant/field-size case has one separate fresh-worker pilot, ten fresh-worker
warmup rows and twenty fresh-worker measured rows in each of five independent
parent processes per minor. Each row contains one first-decoration interval, with
imports, declarations, dependency verification, startup, transport and journaling
outside the clock. The worker reports its interval in ns, timer resolution,
provenance/source identity and process identity. OS/filesystem caches may be warm.
This is first model decoration after setup, not whole interpreter startup.

Cold intervals may be shorter than 20 ms. The ordinary/extension/seam 20 ms
calibration stays mandatory. Single-worker cold rows have different variance from
v1 summed batches and have no numerical parity target; retain every pilot,
warmup, measured observation and outlier and report uncertainty. The owner's
first v1 attempt was interrupted after 697.603588 seconds and 2757 fresh workers;
v1's selected stdlib counts multiplied startup/provenance wall cost outside the
clock. This motivates the bounded owner method change; it is not a user request,
product defect or failed performance threshold. Frozen v1 definition/evidence
remain in `docs/validation/stage-h-preparation/` and source checkpoint
`f49b9ec6de476271e7193c99b38af196fed3b49a`. V1 aggregate/partial observations must
not be converted or mixed into revised successful process sets.

Memory uses 10,000 simultaneously live instances per case. It records shallow
instance size, dictionary size, pool size, allocation before dictionary
inspection and allocation after inspection in bytes/object. Inputs distinguish
shared from unique retained objects and READY from UNREADY lazy caches. No
memory parity target is imposed.

Every completed calibration, warmup, measured, memory, and individual cold-worker
observation is appended, flushed, and synced to an exclusive raw journal outside
timed intervals. A later worker failure preserves earlier observations and the
worker stdout/stderr; BaseException cleanup closes the journal. Completed full
attempts are written to `.attempt.json` before coverage validation. Only fully
validated attempts produce the final `.json`; partial attempts remain evidence,
not successful process samples. Existing output, attempt, or journal files are
never overwritten. Retain journals, attempts, all raw rows and outliers alongside
the final reports, including failed process attempts.

After the owner freezes the definition, use five independent invocations for
each supported minor. Paths below are operator-supplied external locations; the
benchmark never resolves sibling source checkouts or rebuilds dependencies.
Run from the Dataclass repository root with each exact installed interpreter:

```sh
for PERF_PROCESS in 1 2 3 4 5; do
  "$PERF_PYTHON" -I tests/data/perf/harness.py \
    --definition docs/validation/stage-h2-preparation/definition.json \
    --artifact-root "$PERF_ARTIFACT_ROOT" \
    --sdk-wheel-dir "$PERF_SDK_WHEELHOUSE" \
    --undoable-baseline-dir "$PERF_BASELINE_DIR" \
    --undoable-baseline-wheel "$PERF_BASELINE_WHEEL" \
    --backend native-rust --process-label "$PERF_MINOR-$PERF_PROCESS" \
    --output "$PERF_RAW_ROOT/$PERF_MINOR-$PERF_PROCESS.json"
done
```

Repeat with `PERF_MINOR=3.12`, `3.13`, and `3.14`, changing `PERF_PYTHON` to the
matching isolated installed interpreter. Preserve nonzero exits and partial
journals; they do not count toward the five complete independent processes. Do
not run process samples concurrently on the same machine. No partial-inventory
CLI or reduced calibration flag is offered. Then aggregate the fifteen complete
raw documents (use their explicit filenames):

```sh
set --
for PERF_MINOR in 3.12 3.13 3.14; do
  for PERF_PROCESS in 1 2 3 4 5; do
    set -- "$@" "$PERF_RAW_ROOT/$PERF_MINOR-$PERF_PROCESS.json"
  done
done
"$PERF_PYTHON" -I tests/data/perf/report.py \
  --definition docs/validation/stage-h2-preparation/definition.json \
  --output "$PERF_RAW_ROOT/summary.json" "$@"
```

The explicit filenames select only final raw process documents. The report requires
all three minor process sets, full inventory, explicit units, reconciled raw
intervals, ordinary calibration rows, separate cold pilots/subobservations, matching provenance, and
source hashes. Each process contributes its median of 20 measured batches.
Pair-bootstrap uses 10,000 resamples, seed 20261012. IQR/median greater than .15
is noisy. Slot read/write vs stdlib slots target at most 1.2×; ordinary
construction/repr/equality/order/hash target at most 2.0×. Confidence intervals
produce pass/regression/inconclusive without changing gates or removing
outliers. These thresholds are unchanged from the accepted plan.

Mechanics tests use synthetic clocks and small stdlib-only memory fixtures;
they are setup/accounting evidence, not benchmark observations. Owner prototype
adoption was not wholesale strict test-first: the original history remains in
`docs/validation/perf-preparation/owner-mechanics-observations.json`.
Stage H's new behavioral RED→GREEN increments are separately recorded under
`docs/validation/stage-h-preparation/` and the cold amendment under
`docs/validation/stage-h2-preparation/`. Later plumbing, expanded fixture and
supported-minor checks are explicitly verification.
