# YIDL Dataclass experiment protocol

Status: autonomous experiment in progress following the operator GO at
2026-10-12T03:36:48Z. Semantic design and TDD plan were accepted; the operator
removed all SDK prerequisites through `ScopeCorrection.md`. The active consumer
generation amendment is independently accepted; Dataclass Stage A is verified
and Stage B are verified product checkpoints. Stages C–H and final acceptance
remain; Stage B records a test-first sequencing deviation.
Astichi/YIDL SDK edits, builds, version increments and resource additions are
outside this experiment; use original Astichi 1.1.3 / YIDL 0.1.0 APIs. `CurrentProgramCheckpoint.md` records the
live boundary and `ExperimentLedger.md` records measurements. This protocol
defines obligations, not completed implementation or performance claims.

## Questions and outcome

Determine whether an LLM can produce an accurate, usable YIDL dataclass library
from the agreed brief in one autonomous run, how long it takes, what token usage
and cost it incurs, and how its performance compares with Python dataclasses.
The finished library must be usable from its published API and documentation by
people and other LLMs without relying on this conversation.

One-shot means minimizing operator intervention after the brief is agreed. It
includes design review, testing and bounded corrections, rather than claiming
that the first generated implementation is final. Record operator interventions,
review rounds, remediation and any redesign explicitly.

## Workflow and evidence

1. Produce a detailed design and explicit compatibility/extension matrix from
   `DataclassConcept.md`. Resolve or declare assumptions for remaining decisions.
2. Apply the review-loop workflow with independent reviews of a committed design
   checkpoint. Correct structural problems through redesign before implementation.
3. Create a separate TDD implementation plan after the design is reviewed. Follow
   Lifecycle's repository layout and composable, inheritable YIDL module approach,
   using matching to select field facilities. Require specialized generated access
   and factory wiring rather than Undoable's generic runtime dispatch pattern.
   Put equality and ordering generation in a separate reusable YIDL module with
   explicit field-selection and access-expression inputs, owned in Dataclass and
   reused at Undoable regeneration from a pinned consumer build dependency.
   Existing SDK source compilation/caching during generation is allowed. Native
   YIDL composition means resources/matching/Astichi composition; it does not
   mean wholly Rust-owned backend execution. No dynamic method-source emitter
   or consumer AST repair substitutes for those resources.
4. Implement through observable failing tests followed by passing behavior. Prefer
   canonical examples/goldens for successful generated code and end-to-end use;
   use narrow tests for failures and mechanics that those examples cannot express.
5. Review the committed implementation and run final compatibility, extension,
   package-installation and performance checks. Preserve reviewer reports and the
   exact revisions, environments and commands underlying conclusions.

Keep the experiment ledger and checkpoints separate from the original Undoable
experiment. Do not reuse its costs or elapsed times as measurements for this run.
Documentation preparation is a separate stage; record actual design and autonomous
run start times when those stages begin.

## Correctness and compatibility

Use differential tests against the standard library on explicitly selected Python
versions for agreed compatible behavior: constructor signatures and defaults,
metadata and inspection, equality and ordering, hashing, inheritance, keyword-only
fields, slots, pattern matching, frozen behavior and applicable copy helpers.
Check unsupported combinations and exception behavior as well as successful cases.

Use extension tests for named factory dependencies, initialization-only providers
including private retention for lazy use, conversion, validation, const/lazy
fields, local storage and writable exceptions in frozen classes. Document
intentional differences, particularly slots by default and replacing post-init
initialization with dependency resolution. Do not treat those as standard parity.

Publish generated examples that make the storage and access paths inspectable.
Use Undoable as the second consumer of the comparison module, with canonical
examples proving reuse and tests of explicit comparison flags and selected views.
Verify its existing behavior with comparisons disabled and document the integration
revision separately from the frozen original Undoable experiment results.
Cover the decorator defaults/omitted-option table and both transaction assignment
policies independently from logical field inclusion, with structural generation
enabled and disabled. Golden examples must fulfill the inspection and contrast
requirements in [Golden examples amendment](GoldenExamplesAmendment.md).
Verify field-local comparison declarations, preservation of legacy managed write
policies, and rejection of conflicting old/new write-policy spellings. Include a
field-removal generation example: its policy disappears with the declaration,
without a detached selector. Required provider references still diagnose missing
dependencies. Evaluate declarative qualities separately from correctness using
the mode/evidence rules summarized in [Declarative evaluation](DeclarativeEvaluation.md).
Exercise independent installation and an example built using only the public
documentation. Report remaining limitations instead of inferring correctness from
a test count alone.

## Performance comparison

Compare equivalent standard-library dataclasses and YIDL dataclasses on the same
interpreter and machine, with both the standard default and explicit slotted
standard-library baselines. Use equivalent fields and inputs, with separate
results for extensions that have no direct standard-library equivalent.

Measure at least:

- Ordinary slot reads and writes; require inspection of generated code to confirm
  that these paths do not pass through properties or generic helpers.
- Constant/frozen reads and rejected writes, separately from mutable slot access.
- Construction with supplied values, ordinary factories and dependent factories.
- Lazy first access and cached access as different operations.
- Conversion/validation overhead when enabled, with a disabled-policy baseline.
- Equality, ordering, hashing and representation on equivalent logical fields.
- Generation/decorator cost and memory footprint separately from hot instance use.

Use a reproducible benchmark harness with warmups, repeated independent runs and
an account of variation. Record interpreter version, benchmark definitions,
environment details, commit, sample counts, raw results and relative comparisons.
Keep setup and code generation outside steady-state access measurements. Choose
any numerical regression thresholds in the reviewed plan before interpreting the
results; do not promise speedup or parity without measurement.

## Time, tokens and cost

Record timestamps at documentation preparation, design start, reviewed design,
plan completion, implementation start, each review/remediation checkpoint, final
validation and delivery. Report elapsed wall time and any available active work
measurements separately.

Where exposed, preserve input, cached-input and output token usage for the main
agent and every reviewer/worker, with actor and stage attribution. State missing
coverage and avoid double-counting cumulative counters or shared records. Retain
raw observations so totals can be audited.

Separate actual billed cost, when available, from API-equivalent estimates. An
estimate must identify model, applicable dated prices and cached-token treatment.
Unknown billing is unavailable rather than zero. Do not equate repeated cached
context tokens with the volume of unique source written.

The final report should connect time and cost to quality evidence, operator
interventions, supported behavior and measured performance. Preserve enough
instructions and raw results for another operator to reproduce the evaluation.
