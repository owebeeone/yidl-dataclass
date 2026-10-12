# Benchmark sampling preparation

Status: owner preparation during Stage D; no final performance result or new
numerical gate. Final implementation review must assess these sampling boundaries
against `DataclassPlan.md` Section 5 before accepting the report. Product Stages
A–D are verified; E–H remain. Prototype tools are external and are not shipped
product facilities.

Ordinary operations use one common calibrated operation count across product and
both standard variants, alternating measurement order. Setup remains outside
the clock. Process medians precede paired ratios/bootstrap intervals; noisy
observations remain inconclusive. Every batch, including warmup, is retained.
The existing 1.20/2.00 targets, five-process minimum, 10 warmups, 20 measured
batches, 20 ms calibration, one justified rerun and 10,000-resample seed remain.

Cold generation needs fresh interpreters. The prepared worker imports its API
and creates the declaration outside the measured interval, then times exactly
one first decorator invocation using perf_counter_ns. OS/filesystem caches may
be warm; this is cold compiler/process state, not a claim about cold disk. To
reach the batch minimum, cold batches aggregate the measured intervals from
enough independent fresh workers. Their elapsed value is the sum of generator
intervals, not parent transport/startup time. Preserve each worker observation
and its source hash. Calibration counts are per variant for this case; ordinary
cases retain common counts. Generation has no numerical parity target.

An early Stage C timing-boundary feasibility run on CPython 3.12.12 measured
287,307,708 ns for product first decoration, 452,458 ns for the default stdlib
variant and 472,209 ns for the slotted stdlib variant (three ordinary fields).
One std operation therefore does not meet the planned 20 ms batch minimum.
These single observations establish a sampling issue; they are not repeated
benchmarks, confidence intervals, a speed claim or final product evidence.
The worker source SHA256 was
`bfce9f5bd37ac774dce26f6c9ac6d1350e8357d486d7f8b71d801533bae5670e`.
That external source and observation are preserved separately from the later
prototype worker. No target was tuned from these observations.

Accounting checks cover preparation outside timing, operation units, isolated
case inputs, paired process aggregation, missing/duplicate batches, duplicate
processes, mismatched ordinary operation counts and worker error propagation.
Provisional tools still need the complete agreed case inventory, final installed
tuple/provenance, extension/Undoable cases, memory variants, actual measurements
and independent assessment. Passing tool checks does not satisfy those gates.

After D owner verification, extension setup smoke passes on installed D with
both original backends for 3/12-field pipelines, dependent construction, lazy
first/cached pools and all product memory variants. This is setup verification,
not a timing result. Repeated decoration prepares each declaration before timing.
Source emission times the existing composable emitter captured from the owned
builder during untimed setup and restored immediately; it does not time reading
a cached exported string or modify an SDK.

Memory reporting separates the construction/pool allocation delta from the
after-dictionary-inspection delta, because inspecting a managed instance
dictionary can materialize it. Shallow instance/dictionary and pool bytes remain
separate. Standard weak-reference and excluded-cache storage analogues are
labeled; a standard cache Field's metadata exposure differs from local_store.
New accounting tests first fail on missing memory aggregation/count validation
and inspection-boundary output, then pass; earlier prototype checks added after
drafting remain verification. The full inventory and frozen-artifact measurement
are still pending, including the Undoable seam.

The external Undoable seam preparation now includes full managed-setter cases
for equal integers, reflected opaque incoming equality, and alternating node,
tuple-node and mapping-node values at both model sizes. Original consumer
baseline setup passes on all three minors; integrated-wheel setup and all timing
remain pending. Initial preparation incorrectly tried to store an unsupported
opaque stable value. That setup failure was corrected to use a stable integer
old value and an opaque incoming operand whose equality skips storage; this is
benchmark preparation, not a product defect or strict test-first claim. A direct
handwritten structural comparison on original facade getters is explicitly a
benchmark reference only, with no independent correctness-oracle claim.

Independent EF-wheel setup also passes 24 integrated/original-reference cases
in each of the six backend/minor combinations. Subsequent preparation adds an
untimed right-value reset before alternating-node batches, making every timed
assignment a node change; the changed setup is rechecked on both 3.12 backends.
Final frozen setup across supported minors remains a Stage H prerequisite.
The external summary now reports explicitly labeled original-consumer and
handwritten structural-reference pairs without numerical targets; a focused
missing-pair RED precedes its GREEN. Frozen-row source and calibration-count
checks likewise have actual RED/GREEN records. The four deterministic mechanics
programs currently pass 35 checks; this is no performance or corpus-completeness
claim. Final sampling must pin artifacts, sources and the entire case inventory.
