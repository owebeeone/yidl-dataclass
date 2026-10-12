# Cold generation sampling amendment

This is an explicit owner correction to a self-imposed benchmark method, not a
new operator requirement or a product/interface/dependency change. It replaces
only the requirement that **cold** batches accumulate twenty milliseconds of
generator intervals. Ordinary in-process operation calibration remains at least
20 ms; all ordinary targets, 10 warmups, 20 measured observations, five independent
process sets per supported minor, memory count and statistical reporting rules
remain unchanged. Final Code/State reviews must assess the method and this
requirement provenance instead of assuming the prior plan authorizes it.

## Observed problem and preserved first attempt

Frozen v1 definition canonical SHA256:
`668c864ea59b976a950557ab9d608e351eae9b0aa7e3ef84e2c59f5046191983`,
source checkpoint `f49b9ec6de476271e7193c99b38af196fed3b49a`.
Its first Python 3.12 process ran from 2026-10-12T15:46:20.378291Z to
15:57:57.981879Z (697.603588 seconds), then received a controlled SIGINT.
The journal records completed ordinary/extension/seam and cold observations plus
failure cleanup. No full validated process result exists; those partial rows
will not be mixed into a revised full process set.
The [v1 archive manifest](../docs/validation/perf/v1-interrupted/manifest.json)
identifies gzip-compressed path-sanitized derivatives, uncompressed original raw
hashes and an exact Git archive of the frozen source/definition. Original raw
bytes remain in the named external content-addressed archive. The journal has
2,757 individual cold-worker observations, 1,967 completed aggregate timing rows,
397 calibration rows and sixteen memory observations, ending in failure cleanup.
Compression is lossless; path substitution is explicitly a derivative and never
represented as a verbatim original.

Observed 3-field cold calibration selected one product worker (81,281,125 ns),
40 default-stdlib workers (summed 29,582,289 ns), and 80 slotted-stdlib workers
(summed 25,460,625 ns). Thirty batches of the last case alone require 2,400
fresh interpreters per parent process. Repeating that across sizes, minors and
parent process sets primarily spends wall time on startup and provenance checks,
which are explicitly outside the generation interval. The original journal and
stderr remain preserved; this is a sampling-cost discovery, not a product defect,
compiler blocker or failed performance threshold. Original aggregate observations
are retained rather than silently converted to single-operation samples.

## Revised measurement boundary

For cold generation, one row contains **one first-decoration interval in one
fresh interpreter**. Keep a separate one-worker pilot, ten warmup observations
and twenty measured observations for every variant/field size in each of five
independent parent process sets per minor. Preserve each worker's provenance,
source identity, interval and process identity. Imports, declaration preparation,
startup, transport and journaling remain outside the generation clock. Report
timer resolution and the interval units; retain outliers and uncertainty rather
than adding a numerical cold-parity target.

An individual interval can be shorter than 20 ms. That is an explicit exception
to the prior cold method, not a claim that it met the prior accumulation gate.
The 20 ms calibration remains mandatory for every ordinary/extension/seam
in-process timing case. Complete source/definition/minor provenance, full case
coverage and sample-count validation still precede a successful result. Failed or
interrupted v1 evidence has a separate definition/hash boundary and is excluded
from revised aggregation.

This keeps fresh-process observation meaningful without thousands of interpreter
startups merely to lengthen a sum. It does not claim the two sampling methods
have identical variance. Cold results are descriptive, have no numeric parity
gate and must be reported with their smaller per-row observation count. OS and
filesystem caches may be warm; SDK/import activity outside the timed invocation
can initialize supporting code. The observation is first decoration of the
prepared model after imports/setup, not the complete interpreter startup path.

The original 20 ms-for-cold choice came from the generated plan, not an explicit
user sampling requirement. The user required performance comparison, recorded
experiment cost/time and autonomous completion. This localized correction avoids
changing the product or broader infrastructure and is within the authorized
benchmark component. It neither hides the original choice nor turns optional
compiler optimization into a prerequisite. Frozen v1 source/definition and
partial raw evidence must remain auditable. The amended harness and definitions
will have a new committed freeze before restarted measurement.
