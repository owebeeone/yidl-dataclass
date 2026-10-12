# Stage H preparation checkpoint

This checkpoint freezes a **candidate** benchmark definition for owner review and
commit before measurements. No product timing or 10,000-object memory run was
performed. Mechanics tests use synthetic timing and small stdlib allocation
fixtures; setup runs invoke case operations without clocks.

The final common definition has 132 timing cases and 32 memory cases, unchanged
20 ms calibration/10 warmups/20 measured batches, five independent processes per
minor, 10,000 memory instances, 10,000 bootstrap resamples, seed 20261012 and the
accepted 1.2/2.0/.15 thresholds. Canonical definition digest:
`668c864ea59b976a950557ab9d608e351eae9b0aa7e3ef84e2c59f5046191983`.
File-byte digest:
`805548ffd088cbbd635667757d6ecf62d655064351aeb63255369b154aeab708`.
The definition includes the exact final Stage G consumer wheels and unchanged
original SDK wheel identities, plus per-minor installed payload/origin and
stdlib-source provenance. All eighteen Python harness/test sources are hashed.

Final Python 3.12.12, 3.13.12, and 3.14.3 gates each pass 49 mechanics tests and
84 untimed setup checks on original native-rust. Six cold-worker setup-only
checks per minor also pass against the same final common definition. Final
logs/JUnit are `h19-mechanics-{312,313,314}-verification.*`, setup results are
`setup-final-{312,313,314}.json`, and the cold setup logs are
`h20-cold-setup-{312,313,314}-verification.log`. Earlier candidate definitions and
setup proofs are explicitly archived in `prior-candidate-v1/` and indexed in
`prior-candidate-observations.json`; the initial definition is retained too.

New focused behavioral RED→identical-target GREEN increments cover missing
batch completeness, failed-allocation tracing cleanup, unverified baseline
execution, raw normalization, mandatory CLI provenance, failed-worker and late
validation evidence retention, calibration source/memory units, and cold worker
journal units. Later configuration, plumbing, expanded synthetic fixtures and
cross-minor setup assertions are labeled verification. Cohesive relocation and
formatting checks are labeled refactor. Adoption of the seven owner prototypes
and four mechanics programs is not claimed as wholesale strict TDD; their
original observations remain in
`docs/validation/perf-preparation/owner-mechanics-observations.json`.

The observed local preparation defects are corrected. A final audit initially
assumed synthesized wheel documentation lived under `src`; that audit setup
attempt is preserved as `h22-qa-attempt-verification.log`, followed by the
corrected source mapping. It is not behavioral RED. Earlier pytest cache warnings
from the isolated configuration are preserved and the final launcher disables
cacheprovider. Seven historical diagnostics needed additional path sanitization:
`sanitization-corrections.json` records old sanitized hashes, final hashes and
unchanged original raw hashes. The prior sanitized bytes and original raw bytes
remain in the external content-addressed `yidl-dataclass-stage-h-preparation-raw`
archive; `increments.jsonl` retains original records and appends the correction.

The append-only journal preserves completed observations outside clocks, with
premeasurement source/installed/environment identity. It flushes and syncs each
completed calibration/batch/memory/worker row; partial failures and cold worker
stdout/stderr remain available. A completed full attempt is stored before late
validation; a final success JSON requires complete coverage and provenance.
Cold workers, declaration preparation, transport, journaling and validation stay
outside the measured generator interval. Actual cold calibration counts and
elapsed process cost remain unknown until the owner starts measurement; no gate
was relaxed or predicted from prototype cost.

`tests/data/perf/README.md` documents the exact fifteen-invocation measurement
and aggregation commands, source boundaries, raw retention and reporting gates.
`check_preparation.py` checks the final definition/source/setup tuple and all
sanitized/raw/JUnit references, with the correction map applied explicitly.
`owned-manifest.json` enumerates only `tests/data/perf/` and this evidence directory;
all paths are relative to the Dataclass owning repository. The experiment's
original GO time, B sequencing deviation, compiler scope correction and other
historical process lapses are untouched.

Product source, shared comparison resource, public docs/examples, consumer wheel
tuple, Undoable, SDKs and Lifecycle remain unchanged. No dependency build, Git
operation, publication, held-out author solution inspection, or benchmark
measurement occurred. Next action belongs to the owner: independent audit,
commit frozen definitions, then orchestrate measurement and final Code/State
reviews. The drafter stops writes at this checkpoint.
