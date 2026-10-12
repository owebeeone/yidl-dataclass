# Revised cold sampling — owner freeze

The bounded `ColdSamplingAmendment.md` is implemented and independently
owner-verified. No H2 performance result exists yet. Product source/resources,
consumer artifacts, original SDK/Lifecycle wheels and Undoable are unchanged.

The new common definition is
`docs/validation/stage-h2-preparation/definition.json`, canonical SHA256
`c4226335a0ecef51dc52b23906be2594deb68f2d226878c5ad45d2c2e900fc39`
(file SHA256 `279995dee0f0a5088030714a4e9935bf51d139d1f92fad20a2b8af566fa3c29b`).
It covers the same 132 timing/32 memory cases and exact per-minor installed
provenance, hashes nineteen harness/test Python sources, and explicitly declares
one fresh-worker operation per cold pilot/warmup/measurement row. Cold alone is
exempt from accumulated20ms calibration; ordinary/extension/seam calibration and
all other counts, targets and reporting rules remain unchanged.

Owner integrity audit, direct source-map checks, exact per-minor setup provenance
comparison and independent mechanics runs are in
`docs/validation/stage-h2-owner-preparation/`. Mechanics pass 55 tests on each
supported minor. Drafter raw/JUnit evidence separately records those same gates,
84 untimed setup checks per minor and all eighteen cold setup-only cases. Owner
also verifies all 121 v1 evidence files and the original v1 manifest unchanged.
The v1 source is retained at its Git freeze and exact archived source/definition.

The H2 manifest SHA256 is
`b952c001c2dcdffcc0389dbd7f502fd38aa6d20c9e465239462b435ab9a74b17`.
New narrow RED/GREEN records and obsolete-v1 assertion attempts are preserved in
the separate H2 namespace; no old failed attempt or accumulated cold observation
is relabeled as new-method success. The plan records this owner amendment as a
correction to an implementation choice, not an operator sampling requirement.
Final Code/State reviews must assess necessity, scope and measurement validity.

The drafter stopped writes. Next: commit this new source/definition freeze,
restart serial complete process sets, and retain every raw observation before
aggregation. The interrupted v1 dataset is excluded from those sets.
