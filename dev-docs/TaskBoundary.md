# Active task boundary and requirement provenance

This records the operator's corrected boundary and replacement workspace scope
rules. Designs, plans, tests and review verdicts do not enlarge that authority.

## Deliverables and allowed changes

- `yidl-dataclass`: the consumer library, modular authored YIDL resources,
  generated base, metadata/adapters, examples, documentation, canonical goldens,
  narrow failure tests, installation/regeneration checks, benchmarks and experiment
  time/token/cost records.
- `yidl_undoable`: the explicitly requested second consumer of comparison
  generation, its field-local comparison flags and associated regression/docs
  work. Preserve the unrelated paused UndoableLeaf change.
- Astichi, YIDL SDK and Lifecycle are reference-only. No source, internal
  implementation, resources, packaging, versions, capabilities or rebuilds in
  those dependencies are authorized. Root workspace membership/configuration and
  unrelated members remain outside scope. No publication is authorized.

The original SDK wheels and existing supported composition route are the product
baseline. Independent feasibility evidence is recorded in
`docs/validation/baseline/original-sdk-results.json`; it establishes a route for
core generation, not full product acceptance. Preserved SDK prototypes are not
product dependencies.

## Provenance of controlling constraints

| Constraint | Authority |
| --- | --- |
| Near-standard dataclass decorator, field options, metadata and helpers | Operator's dataclass requirements and accepted concept |
| One class, slots by default, specialized direct field access | Operator's explicit storage/performance instructions |
| Conversion/validation, named factories, construction-scoped providers, lazy retention, const and frozen cache exceptions | Operator's field-policy requirements |
| Field-local comparison participation and reusable comparison YIDL module; actual Undoable reuse | Operator's locality correction and second-consumer instructions |
| TDD, richer inspectable goldens, independent reviews, benchmarks and metrics | Operator's experiment instructions and review-loop request |
| No SDK implementation changes | Operator's explicit scope correction, now reinforced by replacement workspace instructions |
| Existing source compilation/caching during generation | Consumer implementation choice supported by original-API evidence; not a relaxation of requested instance field behavior |
| Supported-minor locks, private metadata adapter and documented compatibility exclusions | Bounded implementation choices in the reviewed consumer design; not independent authority to alter dependencies |
| No machine-specific committed paths; GWZ operations; canonical success coverage; explicit C-style scopes | Applicable workspace rules |

The former parser-free decoration/full-native-restoration profile was an owner
implementation preference incorrectly promoted into a prerequisite. It is
superseded, and its detour remains recorded. The operator correction is a real
intervention in the experiment; no uninterrupted one-shot claim is permitted.

Outside-scope discoveries belong in `OutsideScopeFindings.md`, with evidence,
impact, classification, suggested improvement and explicit blocker assessment.
An optional improvement cannot become a product prerequisite. Before requesting
broader authorization, test the supported route and consumer alternatives. A
proven dependency blocker must be reported; discovery never authorizes its fix.
Future design and implementation review prompts must check this provenance and
boundary in addition to technical correctness.
