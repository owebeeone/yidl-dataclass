# Detailed design remediation — cycle 1

Reviewed design: `9fd44d91943ca706c4c51a0669bd3e9d03260278`.
Both independent reviewers returned NO-GO. The findings below are bounded
corrections; Safety explicitly identified no architectural root cause.

| Finding | Disposition | Closure obligation |
| --- | --- | --- |
| Consistency P2-1 | Correct initializer-availability contradiction. Decide initializer action before requiring generated values; preserve ordinary suppressed/custom-init semantics. | Design gives unambiguous outcomes for plain required init=False with custom init, decorator init=False then assignment, dict-mode class-default fallback and class-default updates, and unavailable providers actually consumed by generated factories. Later differential cases on all minors. |
| Consistency P3-1 | Correct stale README. | README links the proposed detailed design and identifies its review status, while TDD/implementation remain subsequent work. |
| Safety P2-1 | Replace rebuilt-value projection with paired traversal preserving opaque operands and Python comparison dispatch. | Retrace AcceptOriginal callback with the original list object, both operand directions and old/new write-policy spellings with generation on/off. Preserve node identity and native container identity shortcuts; cycles diagnose; keep existing ownership fence. Add narrow and integration regressions. |

One drafter makes one merged documentation patch. The intent and public API stay
unchanged: ordinary initializer suppression follows the promised std behavior and
write detection preserves the promised original comparison boundaries. Same-axis
reviewers recheck their exact counterexamples and assess changed ranges. No owner
self-closure, no runtime implementation yet.
