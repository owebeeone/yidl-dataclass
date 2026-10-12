# H2 cold-only sampling checkpoint

This is the bounded implementation of the owner's
`dev-docs/ColdSamplingAmendment.md`, not a new user requirement or product change.
The v1 first attempt's observed startup/provenance wall cost motivated the method
change. It does not establish a product defect or performance threshold failure.
No H2 benchmark measurements were run.

Cold cases now use one distinct fresh-worker pilot, ten fresh-worker warmup rows
and twenty fresh-worker measured rows, each with exactly one first-decoration
operation, per variant/size/parent. All three variants at both field sizes retain
five independent parents per minor. Worker imports/declarations/verification,
startup, transport, journaling and result validation remain outside the clock.
Individual interval units, worker identity, source/provenance and timer resolution
are retained. Cold intervals can be below 20 ms; variance differs from historical
summed batches and no cold numerical parity target is added. Ordinary, extension
and Undoable seam 20 ms calibration, inventory, memory 10k, all other sample counts,
statistical definitions and 1.2/2.0/.15 gates stay unchanged.

The new common definition is `definition.json`, with canonical digest
`c4226335a0ecef51dc52b23906be2594deb68f2d226878c5ad45d2c2e900fc39`
and byte digest
`279995dee0f0a5088030714a4e9935bf51d139d1f92fad20a2b8af566fa3c29b`.
It declares `cold_sampling=single_fresh_worker`, `cold_operations=1` and
`cold_pilot_operations=1`, covers 132 timing/32 memory cases, and hashes all 19
harness/test Python files plus exact original installed minor/SDK/consumer
provenance. Raw results explicitly declare the same method; prior/mismatched
method, definition, worker source and provenance are rejected.

Focused genuine RED→identical-target GREEN covers the old routine's 94 synthetic
worker calls versus 31, pilot exemption while the ordinary minimum stays strict,
acceptance of two-worker cold rows under the old calibrated-count rules, and
acceptance of a result claiming a contradictory historical method. The first
count fixture originally failed on the old calibration diagnostic; a strengthened
pre-fix fixture demonstrated actual `DID NOT RAISE` for the two-worker acceptance
gap. Both attempts are preserved, without overstating the first fixture.
Full synthetic inventory/provenance mutants and later checks are verification.
Two preexisting mechanics assertions described v1 summed/calibrated cold rows;
the recorded all-mechanics attempt failed exactly those obsolete expectations.
They now assert the authorized one-worker/pilot policy. Original adoption's
partial-TDD status and all earlier experiment deviations remain recorded.

Final 3.12.12/3.13.12/3.14.3 mechanics each pass 55 tests and final untimed installed
setup each passes 84 checks; all 18 setup-only cold CLI cases pass against this
same final definition. Final result names begin `h2-final-`; per-minor setup JSON
and definitions are `setup-final-{312,313,314}.json` and
`definition-final-{312,313,314}.json`. The native backend remains explicitly
selected with no fallback and fixed original SDK wheels. No SDK/cache dependency
installation or build occurred; existing Stage G environments were used.

V1 namespace `docs/validation/stage-h-preparation/` is unchanged. The audit verifies
all 121 evidence files against its preserved manifest SHA
`04cbfce3ae6aa7032669ddb35b40851f618618233b1e0385d10c50c114c7901e`.
The original v1 source is settled at `f49b9ec6de476271e7193c99b38af196fed3b49a`.
Its interrupted journal/stderr remain owner-preserved externally; neither those
partial rows nor summed observations are relabeled or mixed into H2 samples.
The H2 original/sanitized evidence archive is separately content-addressed as
`external:yidl-dataclass-stage-h2-preparation-raw`. Append-only journal behavior
and late-validation attempt retention are preserved.

Only `tests/data/perf/`, this new H2 evidence directory, and the plan's relevant
cold clauses changed. The plan refers to the owner amendment and explicitly
preserves the historical 20 ms-for-cold method. Benchmark README commands select
this H2 definition. Product/package/shared resources, public API docs, SDKs,
Lifecycle and Undoable stay unchanged. No Git, publication, author-solution
inspection or numerical H2 sampling occurred. `owned-manifest.json` lists the
exact owned tuple and changed inventory; `qa.json` records the independent-ready
hash/source/raw/JUnit/setup checks.

The drafter stops writes here. Owner verification and a new committed definition
freeze precede restarted measurement. Final Code/State reviews assess the
amendment's scope, provenance, necessity and measurement validity.
