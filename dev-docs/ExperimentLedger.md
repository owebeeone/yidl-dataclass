# YIDL Dataclass preparation and review ledger

Status: requirements preparation and independent review, before detailed design
or autonomous implementation. The original Undoable experiment remains separate.

## Checkpoints

| UTC time / revision | Event |
| --- | --- |
| `b9a3788` | Member created and initial discussion requirements captured. |
| `12111c7` | Performance and second-experiment protocol recorded. |
| `f7e00b8` | Reusable comparison generation requirement recorded. |
| `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13` | Undoable selected as real second consumer; initial requirements object. |
| 2026-10-12T03:18:04Z | First recorded requirements-review preparation checkpoint; measurement baseline for this review stage only. Earlier preparation is not included in these deltas. |
| 2026-10-12T03:18:38.479Z | Independent Consistency/Surface reviewer starts. |
| 2026-10-12T03:18:43.234Z | Independent Safety reviewer starts. |
| `8c116f51310343b18e4ebae27ea6a91517f828e4` | Review-scope checkpoint; both reviewers verify pinned tuple at start/end. |
| Round 1 | Both NO-GO, independently finding the same P2 namespace collision; one additional P3 defaults finding from Consistency. |
| Round 1 remediation | One corrected documentation object, incorporating the operator's golden-example addition; fresh reviewers required for changed interface. |
| `0ceb048a98f9e4464366fc1abfb0827888e8fc54` | Both fresh round-2 reviewers GO; original findings independently closed on that draft. |
| Operator locality correction | Decorator mapping rejected; field-local logical comparison and separately named write policy specified. Operator explicitly accepts this amendment without another review round. |

The round-2 GO reports apply to their exact historical object. The subsequent
locality amendment is operator-accepted rather than independently re-reviewed.
See `DataclassSpec-OperatorAmendment.md` for the explicit override and remaining
regression obligations. No architectural root cause was reported in either round.

## Measurement limits

Review-stage sanitized token observations are retained separately from implementation
metrics. Counter deltas use the last observed cumulative sample before the recorded
review baseline for the owner; fresh reviewers have their own independent baselines.
Reasoning output is included in output totals, not counted again. Cached input is
repeated request context, not unique source volume.

Actual billing is unavailable. No cost estimate has yet been calculated or claimed.
Any later estimate must verify applicable dated model rates and request conditions;
the first experiment's rates must not be assumed automatically. A completed-stage
sample cannot include subsequent owner output. Formal design/implementation start
times remain unset; this ledger does not label requirements review as implementation.
