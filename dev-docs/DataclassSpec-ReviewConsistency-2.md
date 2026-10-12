# YIDL Dataclass specification — CONSISTENCY-AXIS REVIEW

**Review object:** `yidl-dataclass/README.md`, `yidl-dataclass/dev-docs/DataclassConcept.md`, `yidl-dataclass/dev-docs/ExperimentProtocol.md`, and `yidl-dataclass/dev-docs/GoldenExamplesAmendment.md` at `0ceb048a98f9e4464366fc1abfb0827888e8fc54`. Requirements-stage draft dated 2026-10-12; no implementation or accepted detailed design.

**Baseline:**

| Repository | HEAD and source revision |
| --- | --- |
| yidl-dataclass | `0ceb048a98f9e4464366fc1abfb0827888e8fc54` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |

Repository evidence was read with `git show SHA:PATH`, adding line numbers for citations. The original three-file specification was also read at `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`. Repository citations below use the baseline revisions unless explicitly identified as original.

**Date:** 2026-10-12, Australia/Sydney.

**Axis:** Consistency against the controlling document graph, including developer Surface review. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — zero open P0, P1, P2 or P3 findings. Both prior Consistency findings are independently closed at the requirements gate. This accepts the brief for detailed design, not implementation, API freeze, standard-library parity or measured performance.

---

## Prior-finding closure table

| Prior finding | Original counterexample retraced | Corrected evidence | Disposition |
| --- | --- | --- | --- |
| P2-1: logical field `compare` collides with managed transaction policy | A managed field must retain `compare="identity"` while being excluded from generated equality and ordering. The pinned Lifecycle marker accepts a string write policy, not a boolean logical flag. | `DataclassConcept.md:72–84` preserves the shared marker and adds decorator-level `compare_fields`. Lines 104–109 express both settings together. Lines 111–116 require independent policy/inclusion checks; `ExperimentProtocol.md:63–66` carries them into later evidence. | **Closed.** The independent settings are expressible without changing Lifecycle markers. This is textual requirements closure; runtime regression evidence remains future work. |
| P3-1: comparison defaults and omitted-argument behavior are unspecified | `@undoable(order=True)` could enable comparisons under dataclass defaults or reject under identity-preserving defaults; bare and empty-parentheses decoration were ambiguous. | `DataclassConcept.md:86–99` fixes `eq=False, order=False`, preserves identity equality/hash when generation is disabled, makes bare/empty decoration equivalent, and explicitly rejects ordering with omitted or false equality. `ExperimentProtocol.md:63–65` requires coverage. | **Closed.** Every originally requested table case now has a stated result. |

The remediation plan’s dispositions at `dev-docs/DataclassSpec-RemPlan.md:8–17` agree with these independently verified closures. No owner assertion was treated as closure evidence by itself.

## Changed-range analysis

Comparison was performed by reading both immutable versions.

| Range | Change and assessment |
| --- | --- |
| `README.md:1–18` | Unchanged. The cold-reader entry surface still identifies a proposal and directs readers to requirements and the experiment protocol. |
| Original `DataclassConcept.md:69–75`; corrected `DataclassConcept.md:69–116` | Replaces the overloaded field control and unspecified defaults with separate logical selection, eligibility/exclusion rules, decoration-time rejection, an option table, a coexistence example and regression requirements. The correction removes both prior root causes. |
| Corrected `DataclassConcept.md:118–221` | Remaining original material is retained with shifted line numbers. Explicitly open design decisions remain open; the comparison amendment does not silently resolve view, type or hash contracts. |
| `ExperimentProtocol.md:63–66` | Adds omitted-option/default coverage, independence of transaction policies and logical inclusion with generation enabled/disabled, and a link to the golden amendment. Other protocol requirements remain intact. |
| `GoldenExamplesAmendment.md:1–38` | Newly included requirement for meaningful contrasts, readable source goldens and observable behavior. It preserves the existing canonical-coverage preference and historical experiment boundary. |
| `CurrentProgramCheckpoint.md:41–58` | Records round-one findings, the corrected four-file object and fresh replacement reviewers. Lines 8–10 identify the historical round-one object; lines 49–54 expressly establish its successor. |

**NEW ARCHITECTURAL root causes:** None found.

## 0. Evidence base

The README was read cold before the concept, protocol and prior report.

| Repository | Files and ranges inspected | Purpose |
| --- | --- | --- |
| Workspace root | `AGENTS.md`; `AGENTS_GWZ.md` | Workspace authority, canonical path and read-only operating constraints |
| yidl-dataclass | `README.md:1–18`; `dev-docs/DataclassConcept.md:1–221` | Complete entry surface and controlling draft |
| yidl-dataclass | `dev-docs/ExperimentProtocol.md:1–115`; `dev-docs/GoldenExamplesAmendment.md:1–38` | Complete evidence, performance and canonical-example requirements |
| yidl-dataclass | `dev-docs/CurrentProgramCheckpoint.md:1–58` | Authority, deferrals, original object and corrected-object boundary |
| yidl-dataclass | `dev-docs/DataclassSpec-ReviewConsistency.md:1–173`; `dev-docs/DataclassSpec-RemPlan.md:1–23` | Every prior finding, counterexample and required closure |
| yidl-dataclass, original SHA | `README.md:1–18`; `DataclassConcept.md:1–180`; `ExperimentProtocol.md:1–111` | Original-to-corrected comparison |
| yidl_undoable | `docs/API.md:1–137` | Existing field, provider, transaction and view contracts |
| yidl_undoable | `dev-docs/UndoableDesign.md:150–235` | Provider ordering, construction context and node/view identity |
| yidl_undoable | `src/yidl_undoable/undoable_markers.py:1–33`; `undoable.py:1–76`; `undoable_harvester.py:1–132` | Exact shared markers, existing decorator and supported field families |
| yidl_undoable | `src/yidl_undoable/facades.py:1–200`; `transaction_yidl.py:570–635` | Provider storage, existing equality/hash and managed write detection |
| yidl-lifecycle | `README.md:1–76`; `src/yidl_lifecycle/lifecycle_markers.py:1–491` | Lazy semantics, marker signatures and validation |
| yidl-lifecycle | `src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl:1–135,340–465` | Dependency facts and specialized generated factory wiring |
| yidl | `tests/data/yidl/yidl_update_a_dataclasses_split/dataclasses_base.yidl:1–130` | Existing decorator/field facts and composable generation example |

Official reference verification covered:

- [Python 3.14 dataclasses documentation](https://docs.python.org/3.14/library/dataclasses.html): decorator defaults, comparison generation, field flags, hashing, slots and helper boundaries.
- [Python 3.12 dataclasses documentation](https://docs.python.org/3.12/library/dataclasses.html): earlier tuple equality and comparison behavior.
- [CPython 3.14 dataclasses source](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py), particularly lines 1062–1094: individual-field equality, self-identity shortcut, exact-type check and tuple ordering.
- [Pydantic field documentation](https://docs.pydantic.dev/latest/concepts/fields/): factories receiving a dictionary of earlier validated fields.

Inspection commands were restricted to `cat`, `rg --files`, `git show`, line-number/range reads, `git rev-parse HEAD`, `git status --short`, and official-reference browsing. No tests, builds, writes or Git mutations were performed.

The exact four-repository tuple matched at both start and end. Dataclass status was clean. Neighboring dirty files were unchanged and excluded; pinned committed contents were used throughout.

No separately accessible `review-loop/SKILL.md` was found in the searched workspace, skill and plugin locations. The supplied canonical-generated prompt provided the operative review and report contract. No current-round peer report was read or requested, and no other reviewer was contacted.

## 2. Invariant analysis

### Controlling graph and compatibility boundaries

The README, concept, protocol and checkpoint consistently describe requirements preparation. None claims an implemented API, completed compatibility matrix, accepted benchmark or actual billing result.

The single generated class applies to Dataclass storage. It does not prohibit Undoable’s existing facades in the second consumer. `DataclassConcept.md:56–60,118–122` explicitly permits consumer-specific access expressions and assigns Undoable view semantics to its adapter.

No enumerated superseded-clause list exists to verify. The correction replaces the original comparison paragraph within the Dataclass brief; it does not claim to replace Undoable’s controlling runtime design or historical experiment measurements. `ExperimentProtocol.md:61–62` and `GoldenExamplesAmendment.md:36–38` preserve that boundary.

### Logical comparison and transaction write policy

The original collision is reproducible from pinned source:

- Lifecycle’s `managed` exposes `compare: str = "value"` at `lifecycle_markers.py:169–193`.
- Its validator rejects values outside `"value"` and `"identity"` at lines 411–412.
- Undoable re-exports those exact factories at `undoable_markers.py:3–18`.
- Its managed setter uses identity or value equality at `transaction_yidl.py:607–616`.

The corrected example can retain `managed(compare="identity")` and independently specify `compare_fields={"cache": False}`. Generation flags, logical field selection and managed write detection now occupy separate controls.

The new eligibility list accounts for every pinned supported kind in `undoable_harvester.py:25–35`: ordinary `field`, `const`, `static`/`lazy`, `managed` and `binding` are eligible; `initvar`, `classvar`, `transient` and `local_store` are excluded. Lifecycle’s `static = lazy` alias at `lifecycle_markers.py:166` explains their shared classification.

The rejection wording is coherent: an excluded kind cannot be included; unknown names and nonboolean overrides fail at decoration. A false override cannot make an excluded kind participate. Omitted overrides leave the stated kind defaults in effect.

Included binding or ordinary values can be unorderable. That does not make ordering generation unsatisfiable: field selection and generated operators do not guarantee that every supplied Python value supports ordering. Exception behavior belongs in the required compatibility and failure checks.

### Defaults and backwards compatibility

The proposed defaults preserve the pinned node-identity equality/hash implementation at `facades.py:153–157`. Equality generation remains an explicit opt-in.

The seven-row option table covers bare decoration, empty-parentheses decoration, explicit disabled generation, equality alone, equality plus ordering, omitted equality with ordering, and explicitly incompatible flags. Its distinction from standard dataclass defaults is stated, so “dataclass-style” no longer supplies an ambiguous default.

`compare_fields` describes inclusion in generated methods; it does not independently enable generation. Consequently, excluding a field with `eq=False, order=False` cannot disable existing node identity equality or alter its transaction policy.

### Standard and version-specific dataclass parity

The brief separates decorator generation controls from the Dataclass field’s boolean `compare` flag. Selection applies to both equality and ordering; hashing remains subject to a separately defined consistency contract.

Python versions matter. Python 3.12 uses tuple equality; Python 3.14 compares selected fields individually and retains tuple ordering. Shared non-reflexive values and self-comparison can expose differences. The official source confirms these distinct algorithms. [Python 3.12 documentation](https://docs.python.org/3.12/library/dataclasses.html), [CPython 3.14 comparison generation](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py)

`DataclassConcept.md:218–221` leaves supported versions open, while `ExperimentProtocol.md:46–50` requires differential checks on selected versions. A design can therefore select and document a coherent version contract. The requirements do not assert one universal comparison implementation has already achieved every version’s behavior.

The cited Pydantic factory description is accurate: its data-aware factory receives earlier validated fields through a dictionary. That reference does not impose Pydantic’s complete framework on this experiment. [Pydantic field documentation](https://docs.pydantic.dev/latest/concepts/fields/)

### Storage and performance

Ordinary writable fields have a direct public-slot path under `DataclassConcept.md:28–30`. Policy-bearing fields may use specialized properties and private backing slots under lines 34–47. These requirements admit a generated implementation without generic access dispatch.

Factory dependencies can be resolved during generation while actual callbacks, validation and lazy checks remain runtime work. The prohibition on generic dispatch does not prohibit necessary guards or shared generation helpers.

The protocol requires equivalent standard default/slotted baselines, separate extension costs, generated-source inspection, first versus cached lazy access, generation cost and reproducible measurements. It does not require an unmeasured speedup. Its evidence obligations are satisfiable.

### Factories, initialization providers and lazy lifecycle

The brief separates initialization-only status from constructor-signature inclusion. An eager-only provider can remain a constructor local; one needed later can be retained privately. These are compatible with named dependency wiring and provider exclusion from ordinary field access and comparisons.

Pinned Lifecycle templates demonstrate both local and stored provider expressions at `lifecycle_default_factories.yidl:438–463`; Undoable’s access-time path recognizes privately retained initvars at `facades.py:94–109`. The Dataclass proposal requests the useful concepts without requiring either consumer’s storage machinery.

Successful lazy caching, retry after failed initialization and internal writes to read-only backing storage agree across the concept and protocol. Cleanup, copying, recursion, cycles, supplied-value handling and mutable invalidation remain explicit design obligations. No completed lifecycle guarantee is asserted for those open choices.

### Constants, frozen overrides, caches and hashing

Read-only reference replacement and mutable stored contents are distinguished. Internal lazy initialization is expressly permitted, so frozen/read-only policy does not prevent first materialization.

Tri-state mutability has a semantic default: inherit the class policy. Its final spelling and precedence remain open, as the prompt permits at this gate. Cache exclusion and equality/hash consistency constrain that later choice.

Undoable’s opted-in structural equality must eventually specify hash behavior, view/type compatibility and changing-history values. `DataclassConcept.md:118–120` explicitly assigns this work to the adapter. A stable identity hash cannot simply be assumed correct for newly structural equality. This is a required design decision, not an omitted claim of current correctness.

### Required Surface trace

| Developer action | Established requirement | Remaining guess and gate |
| --- | --- | --- |
| Construct ordinary fields | Standard behavior objective, slots by default, direct access and metadata preservation | Public package/decorator spelling and exact compatible subset remain declared design work. |
| Add a dependent factory | Parameter names identify providers; supplied/default values participate; dependency order is resolved | Callable-signature support, reserved provider names and diagnostics must be resolved in detailed design. |
| Share initialization-only inputs across factories | Signature inclusion is independent; privately retain inputs required by delayed factories | Retention, cleanup and copying rules are expressly required before implementation. |
| Declare lazy fields | Cache a successful converted/validated result; leave unset after failure; comparison/hash may materialize | Supplied inputs, recursion and mutable deletion/invalidation require the policy matrix. |
| Override frozen policy for a cache | Inherit class policy unless explicitly overridden; writable caches should be excluded from logical comparisons/hash | Final option spelling and precedence remain explicitly open. |
| Opt into Undoable equality/order | `eq=True` enables equality; `order=True` additionally requires equality; defaults preserve identity | Facade/type/hash outcomes remain detailed-design decisions. |
| Exclude an identity-policy managed field | Decorator `compare_fields` and marker `compare="identity"` independently express both settings | No remaining requirements-level naming or default guess. |
| Select unsupported comparison fields | Excluded-kind inclusion, unknown names and nonboolean overrides reject at decoration | Exact exception diagnostics can be specified in the design. |

The README is an adequate requirements-stage entry point. It does not teach executable construction because no API is implemented or frozen. The remaining guesses are identified design decisions and do not prevent the corrected brief from guiding that work.

### Golden and experiment evidence

The golden amendment requires contrasts rather than a numerical field quota. Its examples can show selected operands, direct versus specialized access, eager/lazy wiring, retained providers and observable comparison results within cohesive canonical scenarios.

Hash inclusion contrasts can be demonstrated in Dataclass examples while Undoable’s hash contract is separately designed. The amendment does not require every listed feature to exist in every consumer.

Generated-source goldens and canonical behavioral output are complementary; pairing is conditional on harness support. Reusing canonical scenarios agrees with the root instruction against duplicating successful end-to-end assertions in bespoke unit tests.

Time and cost requirements keep preparation, design and implementation starts separate, preserve missing token coverage, prevent cumulative-counter double counting, and distinguish billing from estimates. They make no unsupported measurement claim.

## 3. Risks and next action

Detailed design must resolve supported Python versions, public marker/decorator signatures, comparison overrides and inheritance, factory/provider diagnostics, helper interoperability, frozen inheritance, private-provider lifecycle, lazy mutation and hash/view contracts. These are acknowledged design obligations below the finding bar at this requirements gate.

The single next action is to merge this independent verdict with the other axis’s verdict. If that combined gate permits progression, prepare the detailed design and compatibility/extension matrix, carrying both closed findings’ regression requirements and the golden amendment into its later TDD plan.