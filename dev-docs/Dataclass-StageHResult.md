# Measured performance — primary H2 result

All fifteen complete native process samples pass the frozen coverage/provenance
validation: five each on CPython 3.12.12, 3.13.12 and 3.14.3, Apple M3 Pro,
original Astichi 1.1.3/YIDL 0.1.0 and unchanged G consumer wheels. Collection ran
2026-10-12T16:10:09.487589Z–17:16:44.425022Z, **66m34.937433s** wall time.
This is local benchmark collection time, not LLM active time or generator latency.
Final implementation Code/State acceptance is still pending at this checkpoint.

**Threshold results: 73 pass, 47 inconclusive, zero confirmed regressions.**
There are 120 thresholded comparisons and 96 additional contextual comparisons.
Forty-six threshold conclusions are inconclusive because product or baseline
process-median IQR/median exceeds .15; one stable interval straddles its target.
No outlier, failed first attempt or inconvenient interval was dropped. No
universal performance-parity claim follows from these results.

## Frozen method and independent checks

Source/definition freeze: `fc5a47fd325c8a2ad01fb87b120e5319ce38ab1c`.
Definition canonical SHA256:
`c4226335a0ecef51dc52b23906be2594deb68f2d226878c5ad45d2c2e900fc39`.
The consumer package tuple remains G; no product/SDK optimization was introduced.
Ordinary/extension/seam batches calibrate to at least 20 ms, then 10 warmups and 20
measurements; paired variants alternate order with a common maximum count.
Cold alone uses the explicit [ColdSamplingAmendment](ColdSamplingAmendment.md):
separate one-worker pilot, 10 warmup and 20 measured first-decoration intervals.
Imports/setup/startup/transport/journaling are excluded from those intervals;
OS/filesystem caches may be warm. Cold has no numeric parity threshold.

The full primary dataset contains **59,400 aggregate timing rows** (39,600 measured,
19,800 warmup), **480 memory observations**, **90 cold pilots** and **2,790 individual
cold-worker observations**. There are132 timing and 32 memory cases per process.
Every memory observation uses 10,000 live instances; classes/shared inputs are
outside allocation accounting. All calibrations and raw journal rows are retained.

The independent owner audit imports no benchmark code. It rechecks all raw units,
counts, source/installed hashes, complete batch inventories, unique process IDs,
ordinary calibration minimums, one-worker cold rows/pilots and journal completion.
It recomputes all 216 paired ratios, process medians, dispersions and95% bootstrap
intervals independently using explicit pair-index resampling (10,000 samples,
seed 20261012). Every comparison and verdict matches the report. The first owner
journal audit assumed one-based sequence IDs; inspection showed contiguous
zero-based IDs, and the external audit was corrected. That setup mistake is not
product RED; its traceback remains in session tool output rather than an invented
raw file.

## Threshold summary by minor

| CPython | Pass | Inconclusive | Confirmed regression |
| --- | ---: | ---: | ---: |
| 3.12 | 20 | 20 | 0 |
| 3.13 | 33 | 7 | 0 |
| 3.14 | 20 | 20 | 0 |

## Ordinary direct slot access versus stdlib slots

Ratios are product/baseline; below 1 means smaller observed time. Target is 1.20.
These are medians of process-paired ratios, with the retained 95% interval.

| CPython | Fields | Operation | Ratio | 95% interval | Conclusion |
| --- | ---: | --- | ---: | --- | --- |
| 3.12 | 3 | slot_read | 0.9993 | 0.8636–1.0095 | pass |
| 3.12 | 3 | slot_write | 1.0003 | 0.9846–1.0401 | pass |
| 3.12 | 12 | slot_read | 0.9988 | 0.8821–1.0096 | inconclusive |
| 3.12 | 12 | slot_write | 0.9975 | 0.9783–1.0453 | inconclusive |
| 3.13 | 3 | slot_read | 1.0031 | 1.0006–1.1106 | pass |
| 3.13 | 3 | slot_write | 0.9998 | 0.9987–1.1265 | pass |
| 3.13 | 12 | slot_read | 1.0000 | 0.9983–1.0139 | pass |
| 3.13 | 12 | slot_write | 0.9989 | 0.9730–0.9998 | pass |
| 3.14 | 3 | slot_read | 0.9984 | 0.9247–1.0042 | inconclusive |
| 3.14 | 3 | slot_write | 1.0018 | 0.9367–1.0877 | inconclusive |
| 3.14 | 12 | slot_read | 1.0006 | 0.9130–1.0018 | pass |
| 3.14 | 12 | slot_write | 0.9995 | 0.9980–1.0165 | pass |

All twelve point estimates are near 1.0; eight access conclusions pass and four
remain inconclusive under the unchanged noise rule. Source/bytecode checks separately
establish direct public slot operations; they do not turn noisy timing into a pass.

## Twelve-field frozen hashing — unresolved boundary

The hash operation uses frozen models on both sides, as defined before measurement.
Product frozen fields use requested specialized properties; stdlib frozen slots
use member descriptors. That is an observable implementation difference and a
plausible source of overhead, not a measured causal attribution. The public hash
path still reads public fields. No backing-slot bypass or threshold change was
introduced after seeing data.

| CPython | Baseline | Ratio | 95% interval | Noisy | Conclusion |
| --- | --- | ---: | --- | --- | --- |
| 3.12 | stdlib_default | 1.3697 | 1.2459–1.4924 | True | inconclusive |
| 3.12 | stdlib_slots | 1.9735 | 1.9483–2.0810 | True | inconclusive |
| 3.13 | stdlib_default | 1.2885 | 1.1770–1.2974 | False | pass |
| 3.13 | stdlib_slots | 1.9174 | 1.8729–2.0829 | False | inconclusive |
| 3.14 | stdlib_default | 1.9433 | 1.9355–2.1956 | True | inconclusive |
| 3.14 | stdlib_slots | 2.0347 | 1.9915–2.2910 | True | inconclusive |

The 3.13 slotted interval straddles 2.00 without the noise flag. The 3.12/3.14
slotted intervals also cross 2.00 and are noisy. These are unresolved measurements,
not passes or demonstrated regressions. They warrant a separate quieter/profiled
follow-up if this workload matters; this run does not claim they are solved.

## Ordinary allocation footprint

Instance/dictionary sizes are shallow getsizeof observations; traced allocation
includes the held list pool and is measured **before** dictionary inspection.
Inspection can materialize managed dictionaries, so the full memory CSV reports
its separate after-inspection delta. Class/framework memory and shared input
payloads are outside per-instance allocation accounting.

| CPython | Fields | Variant | Instance B | Dict B | Traced B/object incl. pool before inspection |
| --- | ---: | --- | ---: | ---: | ---: |
| 3.12 | 3 | product | 56 | 0 | 64.5232 |
| 3.12 | 3 | stdlib_default | 48 | 96 | 96.8192 |
| 3.12 | 3 | stdlib_slots | 56 | 0 | 64.5232 |
| 3.12 | 12 | product | 128 | 0 | 136.5232 |
| 3.12 | 12 | stdlib_default | 48 | 168 | 176.6496 |
| 3.12 | 12 | stdlib_slots | 128 | 0 | 136.5232 |
| 3.13 | 3 | product | 56 | 0 | 64.5232 |
| 3.13 | 3 | stdlib_default | 48 | 96 | 104.8376 |
| 3.13 | 3 | stdlib_slots | 56 | 0 | 64.5232 |
| 3.13 | 12 | product | 128 | 0 | 136.5232 |
| 3.13 | 12 | stdlib_default | 48 | 168 | 184.6616 |
| 3.13 | 12 | stdlib_slots | 128 | 0 | 136.5232 |
| 3.14 | 3 | product | 56 | 0 | 64.5392 |
| 3.14 | 3 | stdlib_default | 48 | 96 | 104.8536 |
| 3.14 | 3 | stdlib_slots | 56 | 0 | 64.5392 |
| 3.14 | 12 | product | 128 | 0 | 136.5392 |
| 3.14 | 12 | stdlib_default | 48 | 168 | 184.6776 |
| 3.14 | 12 | stdlib_slots | 128 | 0 | 136.5392 |

Product ordinary instances match stdlib slots in these allocation observations:
56/128 shallow bytes for 3/12 fields with no dictionary. This does not imply equal
class-generation/framework memory. Frozen, weakref, local-cache, lazy ready/unready
and shared/unique retained-provider cases are all in the 96-row memory summary.
The stdlib local-cache variant is a storage analogue with different metadata exposure.

## Extension/generation context

The complete JSON/CSV contains source emission, dependent construction, pipelines,
lazy first/cached access, readonly reads/rejections and actual Undoable prelude/full
managed-setter cases. They have no unsupported parity target. Across the observed
minors/sizes, product first-decoration medians are approximately 69–109 ms, repeated
new-declaration generation 6.1–24.2 ms, and actual composable source emission 0.46–1.55 ms.
These are generation costs; ordinary field access does not run generation.

Undoable setter baselines use its verified pre-integration wheel; the structural
facade comparison baseline is explicitly handwritten benchmark-only reference,
not an independent semantic oracle or replacement product generator. Case shapes,
reset/prepare boundaries and all ratios remain in the frozen definition/CSV.
Neither these context results nor two correctness backends prove universal speed.

## Environment and rerun disposition

Power settings remain unchanged across all samples and GIL is enabled. Recorded
system load varies considerably (end one-minute averages approximately 4.28–136.08).
Before-measurement and end contexts remain in raw journals/results. Load variation
is evidence of an uncontrolled environment, but no specific corrected environmental
cause is established. Therefore the optional one-rerun allowance is not used to
select a favorable result. No unrelated process, power setting or SDK was changed.
All noisy cases remain inconclusive, including point estimates comfortably below
an engineering target. This machine/run is not a portable performance guarantee.

## Auditable artifacts

- [Summary JSON](../docs/validation/perf/primary/summary.json): all 216 comparisons,
  180 product absolute summaries and96 memory summaries, with process medians,
  min/max, IQR, pair ratios, intervals and units.
- [Comparison CSV](../docs/validation/perf/primary/comparisons.csv) and
  [memory CSV](../docs/validation/perf/primary/memory.csv) for independent analysis.
- [Independent audit](../docs/validation/perf/primary/owner-independent-audit.json).
- [Primary manifest](../docs/validation/perf/primary/manifest.json): all 79 original
  files are preserved externally by raw hash, with gzip-compressed explicitly
  path-sanitized repository derivatives. Uncompressed original/sanitized hashes
  and compressed hashes are separate. Compression is lossless; substitution is
  never called verbatim. Complete attempts, journals, stdout/stderr and commands
  remain available, not just favorable summary numbers.
- [Interrupted v1 manifest](../docs/validation/perf/v1-interrupted/manifest.json)
  keeps the original accumulated-cold method/source/partial attempt separate;
  none of it enters these fifteen complete process sets.

Performance evaluation is complete with stated inconclusive boundaries. Final
Code/State reviewers must independently assess method validity, scope provenance,
code correctness and these limitations before implementation acceptance.
