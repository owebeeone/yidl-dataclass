# YIDL Dataclass checkpoint

Status: requirements-stage independent adversarial review pending. Implementation
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

Next action: dispatch both independent reviews of the same immutable object,
file their full reports and record the merged verdict and required decisions.
