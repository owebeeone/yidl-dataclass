# YIDL Dataclass checkpoint

Status: requirements accepted by the operator after dual round-2 GO and a
subsequent operator-approved locality amendment without re-review. Implementation
has not started. This checkpoint governs this member's experiment preparation.

## Object and authority

The review object is the committed README, `dev-docs/DataclassConcept.md` and
`dev-docs/ExperimentProtocol.md` at
`3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`.
The concept is the controlling draft; it is not an accepted detailed design.
Review-loop process applies, with two peer-blind reviewers: Consistency plus
Surface, and Safety. Reports are preserved verbatim beside these documents.

Reference tuple:

- Undoable: `f79e4ce6d985ed0a6463552e163baabf1a28942d`.
- Lifecycle: `230362f642d6e9205897698670fe5f87d2c905ce`.
- YIDL: `9d374f88445c426a56d5dd1f96fad112d1ec5417`.

Scope: whether the captured requirements are coherent and suitable as the brief
for a detailed design and TDD plan. Accepted choices include a single generated
class, slots by default, specialized accessors, named factories replacing
post-init, and Undoable as the comparison generator's second consumer. Reviewers
may challenge missing boundaries and contradictions without re-litigating those
choices merely because they differ from standard dataclasses.

Choices explicitly marked open are not claims of completed implementation.
Determine whether each can safely remain a detailed-design decision or makes the
brief contradictory, untestable or impossible to satisfy. A GO at this gate would
accept the requirements only, not a public API freeze or implementation readiness.

## Isolation and next action

Reviewers inspect only; no writes, builds, implementation or Git mutations.
Neighboring work, workspace metadata, and Undoable's paused initialization-helper
draft are outside scope. The original Undoable experiment's measurements stay
unchanged. The owner files prompts/reports and merges verdicts after both reviews.
Any structural defect requires a redesign before implementation proceeds.

## Round 1 result and correction

Both axes returned NO-GO on the original object. They independently identified
the collision between logical field inclusion and Undoable's existing transaction
`compare` setting. Consistency also found missing comparison option defaults.
See both verbatim reports and `DataclassSpec-RemPlan.md` for dispositions and
closure requirements. No finding is self-closed by the owner.

The corrected object consists of README, the concept, the protocol, and the new
`GoldenExamplesAmendment.md` in the same commit as this checkpoint. It separates
transaction policy from decorator-level logical inclusion and records option
defaults. Fresh Consistency/Surface and Safety reviewers replace the original two
because the comparison interface changed. Round 2 prompts will name the exact
commit and inherit every prior finding on their axis.

## Round 2 and operator acceptance

Both fresh reviewers returned GO on
`0ceb048a98f9e4464366fc1abfb0827888e8fc54`, independently closing the original
findings at the requirements gate. See their verbatim `-ReviewConsistency-2.md`
and `-ReviewSafety-2.md` reports. No new architectural root cause was reported.

The operator rejected the decorator field-name mapping and directed a field-local
comparison flag, a separate transaction write policy and preservation of legacy
declarations. The operator explicitly accepted that spec amendment without another
review. `DataclassSpec-OperatorAmendment.md` records the override and evidence
boundary. The two GO reports do not review the final amended bytes.

Accepted requirements revision: `2abedb40c2c0b3037420d59d5a45eefe13503bee`.
See `DataclassSpec-ReviewResult.md` for exact object/verdict boundaries.

The final requirements object adds `DeclarativeEvaluation.md` to the concept,
protocol and golden amendment. The owner records its exact committed revision in
the review result. Acceptance covers suitability as a brief for detailed design
only, not a completed design, implementation, release or performance result.

Next action: detailed design and compatibility/extension matrix, then a separately
reviewed design and TDD plan. No implementation has begun and no new reviewer
dispatch is required for the accepted locality amendment.
