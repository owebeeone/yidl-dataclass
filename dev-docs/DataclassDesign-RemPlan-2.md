# Detailed design remediation — cycle 2, comparison-boundary redesign

Reviewed object: `5d7883d8838fb9fa170426fbda59a71af3e9188b`.
Both original design reviewers returned NO-GO, independently closing their
initial findings and discovering two new native-equality compatibility defects.
Both classify these defects as bounded rather than architectural failures.

| Finding | Disposition | Closure obligation |
| --- | --- | --- |
| Consistency P2-2 and Safety P2-2 | Replace manual dictionary traversal with native equality inside a temporary historical-identity comparison context. Native dictionary equality retains cached hashes and original callback operands. | Re-run the original hash-counter and raising-hash counterexamples; include collisions, distinct equal keys, key equality exceptions, proxy wrappers and both operand directions. Specify legacy/new write policies and equality generation on/off. |
| Safety P2-3 | Remove manual tuple/list traversal. Native equality preserves each container's own length and prefix callback ordering. | Re-run the original unequal-length tuple with a raising prefix comparator. Cover true/false/raising and observable truth callbacks, reverse operands, identical nonreflexive elements and the contrasting native list behavior. |

This is a redesign of the small write-comparison boundary before product code,
not a further patch to paired traversal. An active ContextVar scope selects a
historical-identity prelude in generated Undoable equality only. Dataclass
comparison code has no context branch. Native equality continues to receive the
original values; ownership checks remain around callback execution.

The revised design must define cleanup, nested scopes, copied-context lifetime,
thread boundaries and the intentional identity behavior of facade comparisons
inside opaque equality callbacks. A scope closes before its ContextVar is reset;
a copied context cannot prolong its authority. It must retain no manager or node.
Hashing and ordering do not switch behavior.

Two fresh reviewers replace the prior pair because the comparison-generation
prelude and callback boundary change. They inherit all earlier counterexamples
on their respective axes. No finding is owner-closed; TDD planning and product
implementation remain behind the detailed-design gate.
