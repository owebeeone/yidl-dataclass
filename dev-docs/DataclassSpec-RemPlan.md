# Dataclass spec remediation plan — round 1

Original object: `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`.
Both independent reviewers returned NO-GO with the same concrete P2 collision.
Consistency also returned a P3 about defaults. Their full reports are preserved
in `DataclassSpec-ReviewConsistency.md` and `DataclassSpec-ReviewSafety.md`.

| Finding | Disposition | Required closure evidence |
| --- | --- | --- |
| Consistency P2-1 | Correct. Keep existing transaction `compare` unchanged; add separate decorator `compare_fields` overrides for logical comparison. Specify eligibility/defaults. | Declaration expresses identity assignment detection and logical exclusion together; independently test every combination with generation on/off. No Lifecycle marker change. |
| Safety P2-1 | Correct, same root as Consistency P2-1. | Both write-detection policies retain their behavior; included/excluded settings remain independent. Distinct equal identity-policy writes record; same-reference writes skip. |
| Consistency P3-1 | Correct. Explicit Undoable defaults `eq=False, order=False`, bare/empty equivalence, and omitted/explicit incompatible cases. | Requirements option table includes every requested case and explains preserved identity behavior. |

One consolidated documentation patch makes these corrections and incorporates
the operator's subsequent golden-example requirement. No runtime changes or
tests are claimed at this requirements gate; canonical regression requirements
are carried into the future TDD plan.

The logical-selection interface and defaults have changed materially, so two
fresh reviewers replace the original two for round 2. Each must retrace the
original counterexamples from its axis and assess the consolidated spec,
including `GoldenExamplesAmendment.md`. Findings remain open until independently
verified on the corrected object. No implementation may start on this verdict.
