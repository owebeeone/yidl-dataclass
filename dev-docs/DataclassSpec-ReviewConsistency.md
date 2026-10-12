# YIDL Dataclass specification — CONSISTENCY-AXIS REVIEW

**Review object:** `yidl-dataclass/README.md`, `yidl-dataclass/dev-docs/DataclassConcept.md`, and `yidl-dataclass/dev-docs/ExperimentProtocol.md` at `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`. Requirements-stage draft dated 2026-10-12; no implementation or accepted detailed design.

**Baseline:**

- yidl-dataclass HEAD: `8c116f51310343b18e4ebae27ea6a91517f828e4`.
- Specification object: `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`.
- yidl_undoable HEAD: `f79e4ce6d985ed0a6463552e163baabf1a28942d`.
- yidl-lifecycle HEAD: `230362f642d6e9205897698670fe5f87d2c905ce`.
- yidl HEAD: `9d374f88445c426a56d5dd1f96fad112d1ec5417`.

Reviewed repository contents were read with `git show SHA:PATH`, with line numbers added for citation. All repository citations below refer to these exact revisions; the Dataclass checkpoint refers to its HEAD revision.

**Date:** 2026-10-12, Australia/Sydney.

**Axis:** Consistency against the controlling document graph, including developer Surface review. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one P2 finding blocks; one P3 finding also needs correction. I pre-commit to GO on a revision that resolves P2-1 and P3-1 as specified.

---

## 0. Evidence base

The README was read cold before the concept and protocol. Inspection covered:

| Repository | File and lines | Purpose |
| --- | --- | --- |
| yidl-dataclass | `README.md:1–18` | Status, entry surface, promises and navigation |
| yidl-dataclass | `dev-docs/DataclassConcept.md:1–180` | Complete controlling draft |
| yidl-dataclass | `dev-docs/ExperimentProtocol.md:1–111` | Complete workflow, correctness and measurement requirements |
| yidl-dataclass | `dev-docs/CurrentProgramCheckpoint.md:1–42` | Frozen object, authority, deferrals and review gate |
| yidl_undoable | `README.md:1–89` | Existing entry surface and experiment boundary |
| yidl_undoable | `docs/API.md:1–137` | Existing markers, comparison policy, provider and view semantics |
| yidl_undoable | `dev-docs/UndoableDesign.md:1–230` | Marker ownership, identity equality and construction providers |
| yidl_undoable | `src/yidl_undoable/undoable_markers.py:1–33` | Exact Lifecycle marker re-exports |
| yidl_undoable | `src/yidl_undoable/undoable.py:1–76` | Existing decorator signature and composition |
| yidl_undoable | `src/yidl_undoable/undoable_harvester.py:1–132` | Marker normalization and consumer adaptation |
| yidl_undoable | `src/yidl_undoable/facades.py:1–190` | Providers, facades, identity equality and hashing |
| yidl_undoable | `src/yidl_undoable/transaction_yidl.py:570–635` | Existing managed-write use of `compare` |
| yidl-lifecycle | `README.md:1–76` | Existing lazy contract |
| yidl-lifecycle | `src/yidl_lifecycle/lifecycle_markers.py:1–440` | Marker signatures, defaults and validation |
| yidl-lifecycle | `src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl:1–713` | Specialized dependency facts, templates and matching |
| yidl | `tests/data/yidl/yidl_update_a_dataclasses_split/dataclasses_base.yidl:1–130` | Existing dataclass example facts and defaults |

Official references were inspected:

- [Python 3.14 dataclasses documentation](https://docs.python.org/3.14/library/dataclasses.html), especially decorator options, `field`, helpers and version changes.
- [Python 3.12 dataclasses documentation](https://docs.python.org/3.12/library/dataclasses.html).
- [CPython 3.14 dataclasses source](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py), including comparison generation at source lines 1062–1094.
- [Pydantic field documentation](https://docs.pydantic.dev/latest/concepts/fields/), especially validated-data factories.

Commands were limited to reads, searches, `git show`, `git rev-parse HEAD`, and `git status --short`. No tests, builds, writes or Git mutations were performed. A search included a nonexistent `tests/test_policies.py` path; the relevant behavior was subsequently verified directly in pinned source.

The exact four-repository HEAD tuple matched at both the beginning and end. The committed Dataclass checkpoint was also reread unchanged at the end. Existing neighboring dirty files were excluded. During review, an untracked `dev-docs/GoldenExamplesAmendment.md` appeared in the Dataclass member; it was explicitly outside the frozen object and was not read.

The supplied canonical review prompt provided the operative review contract. No separately accessible `review-loop/SKILL.md` was exposed or found in the searched skill/plugin locations. No current-round reviewer report was read or requested.

## 1. Findings

### [P2-1] Undoable’s requested field `compare` flag collides with its existing transaction policy

**Location:** `yidl-dataclass/dev-docs/DataclassConcept.md:69–75`, particularly the requirement that “`compare` selects a field for both.” Related evidence requirement: `dev-docs/ExperimentProtocol.md:58–62`.

**Violated invariant:** Adding logical equality/ordering selection must preserve the existing Undoable marker contract and leave transaction change detection independently expressible.

Undoable already exposes `compare="value"` or `compare="identity"` for a different purpose. `yidl_undoable/docs/API.md:65–66` describes that contract. The exact re-export is visible in `src/yidl_undoable/undoable_markers.py:3–18`; Lifecycle’s `managed` signature accepts the string policy at `src/yidl_lifecycle/lifecycle_markers.py:169–193`, and its validator rejects other values at lines 411–412. Undoable’s managed setter consumes this policy at `src/yidl_undoable/transaction_yidl.py:607–616` to decide whether an assignment records a touched value.

**Reproduction/state sequence:**

1. An existing declaration uses `managed(default=..., compare="identity")` to retain identity-based assignment detection.
2. The application opts into generated logical equality and ordering.
3. It needs that managed field excluded from logical comparisons while retaining its existing assignment policy.
4. The brief assigns both controls the public name `compare`, without a separate namespace or coexistence rule.
5. `compare=False` loses the string policy and is rejected by the pinned marker validator. Keeping `compare="identity"` provides no independent exclusion flag. A single keyword cannot simultaneously carry both settings.

This is a requirements collision, not a claim that the nonexistent Dataclass implementation currently fails. Overloading the accepted value types alone would still leave the two independent settings unrepresentable together.

**Impact:** A literal implementation must either break existing declarations, change transaction recording behavior, omit required field selection for managed fields, or invent an unrecorded public control. The third-party consumer cannot satisfy both contracts from the stated interface.

**Required correction:** Amend the brief to distinguish logical comparison inclusion from transaction change detection. Preserve existing Undoable `compare="value"|"identity"` semantics and require an independently expressible inclusion setting or separate comparison configuration. State which field kinds support it and its default. Specify the impact on the shared Lifecycle markers and Undoable adapter; do not silently redefine the shared marker.

**Closure/regression test:** At this gate, a textual declaration/configuration example must express both identity-based managed assignment detection and exclusion from generated equality/ordering. The later canonical integration example should demonstrate that changing only the excluded field leaves logical comparison unchanged while its managed assignment still follows the original identity policy. Retain compatibility cases for existing `"value"` and `"identity"` declarations with generated comparisons disabled.

### [P3-1] Undoable comparison options have no explicit defaults or omitted-argument behavior

**Location:** `yidl-dataclass/dev-docs/DataclassConcept.md:71–75`; `dev-docs/ExperimentProtocol.md:61–62`.

**Violated invariant:** A named option needs a default and predictable omitted-argument behavior. The review contract keeps defaults in scope even when detailed implementation choices are deferred.

The brief requests dataclass-style `eq` and `order`, preserves bare `@undoable`, and asks the detailed design to specify backward-compatible defaults. It supplies no effective defaults for the proposed option-bearing spelling.

The baseline is concrete: `src/yidl_undoable/undoable.py:54` accepts only a class, while `src/yidl_undoable/facades.py:153–157` provides node-identity equality and hashing. Disabling new generation therefore preserves existing equality behavior; it does not imply the absence of equality.

**Reproduction/state sequence:**

1. A developer reads “dataclass-style” options and tries `@undoable(order=True)`.
2. With the standard dataclass default `eq=True`, that request enables equality and ordering.
3. With a default of `eq=False` chosen to preserve existing Undoable behavior, that request fails under the brief’s ordering-without-equality rejection.
4. The brief does not tell the developer which result applies, or whether `@undoable()` and bare `@undoable` have identical effective defaults.

Python’s standard decorator uses `eq=True` and `order=False`; those defaults cannot simply be assumed for the existing Undoable surface. [Python dataclasses documentation](https://docs.python.org/3.14/library/dataclasses.html)

**Impact:** This leaves a bounded but consequential surface guess for both the designer and documentation author. It also leaves the “comparisons disabled” compatibility evidence without a specified public invocation.

**Required correction:** Record effective defaults and omitted-argument behavior for bare and option-bearing decoration. Explicitly state that disabling structural generation preserves existing identity equality/hash behavior. Define the result of `order=True` with `eq` omitted, while retaining rejection of an explicit incompatible combination.

**Closure/regression test:** Add a requirements-level option table covering bare decoration, empty-parentheses decoration if supported, explicit disabled generation, equality-only generation, ordering with omitted equality, and explicit `eq=False, order=True`. Carry these cases into the later canonical decorator and compatibility checks.

## 2. Invariant analysis

### Controlling graph and scope

The README’s concept-stage status agrees with the concept and protocol. It does not claim an available package API. The committed checkpoint identifies the correct immutable object and limits acceptance to a usable requirements brief.

The accepted choices—one generated class, slots by default, specialized access, named factories replacing post-init, and Undoable as the second comparison consumer—agree across all three reviewed files and the checkpoint. No implementation or performance claim is smuggled into the requirements.

There is no enumerated superseded-clause list in this object to verify. The proposed Undoable integration is explicitly planning authorization at concept lines 79–80. It does not itself replace the pinned Undoable implementation or historical experiment record. P2-1 identifies the missing compatibility boundary that the amendment must acknowledge.

### Storage and performance

The direct-slot requirements are mutually satisfiable. Concept lines 28–30 reserve public slots for ordinary writable fields. Lines 34–47 allow specialized properties and callbacks for policy-bearing fields. Conversion/validation fields are explicitly benchmarked separately.

Protocol lines 69–90 use standard default and slotted baselines, isolate extension costs, separate generation from hot access, and require generated-code inspection. No universal speedup or numerical threshold is asserted. The performance evidence is satisfiable after the reviewed plan selects its harness and thresholds.

### Factories, initialization providers and lazy fields

Named dependency resolution, explicit constructor inputs and defaults can coexist. Initialization-only status is correctly distinguished from signature inclusion at concept lines 90–99. Private retention supplies a feasible path for delayed factories while excluding providers from normal representation and logical comparison.

The existing Lifecycle and Undoable provider systems support the referenced class-provider and opt-in instance-provider concepts. The brief requests those concepts without demanding identical storage machinery. Private-provider cleanup/copying, cycles, recursion and callback rules remain expressly open. Those decisions must be resolved at the detailed-design gate, but they do not make the requirements contradictory.

Lazy successful caching and retry after failure agree between concept lines 126–134 and the protocol’s first/cached-access measurements. Internal initialization is explicitly permitted for read-only lazy fields, so it does not conflict with public replacement restrictions.

### Frozen, constants, caches and hashing

The brief distinguishes reference replacement from mutation of stored contents. That permits constant references and mutable cache contents without requiring recursive freezing.

Tri-state mutability has a stated semantic default—inherit the class policy—even though its final spelling and precedence remain open. Cache/local storage exclusion and equality/hash consistency establish design constraints. Hash stability for lazy or writable participating fields still needs a concrete design rule; the brief explicitly requires that work and tests rather than claiming it is solved.

### Standard parity and reusable comparison

Decorator generation controls and per-field inclusion are conceptually distinct in the Dataclass requirements. Ordering without equality is explicitly rejected, and field selection applies to both equality and ordering.

Version-specific comparison parity needs deliberate treatment: Python 3.12 used tuple equality, whereas later versions compare fields individually; ordering remains tuple-based. Shared non-reflexive values can expose the difference. The brief leaves supported Python versions open and requires differential checks on explicitly selected versions, so this is a detailed-design obligation rather than a present contradiction. [Python dataclasses documentation](https://docs.python.org/3.14/library/dataclasses.html), [CPython comparison generation](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py)

The consumer-supplied field order and read expressions provide a feasible generation boundary. Dataclass storage, private providers and Undoable transaction metadata need not leak into that module. Cross-view/type and changing-history hash outcomes are expressly assigned to the adapter’s detailed contract.

Pydantic is accurately treated as reference material: its data-aware factories receive earlier validated fields through a dictionary. The brief neither denies that capability nor imports its entire framework into scope. [Pydantic field documentation](https://docs.pydantic.dev/latest/concepts/fields/)

### Required Surface trace

| Developer action | What the brief establishes | Remaining guess and disposition |
| --- | --- | --- |
| Declare and construct ordinary fields | Standard behavior objective; slots default; ordinary access direct | Package/decorator/marker spelling is explicitly open. Resolve in detailed design. |
| Declare dependent factories | Parameter names select providers; supplied/default values participate; resolve dependency order | Callable signature support, diagnostics and cycle handling remain design work. |
| Use initialization-only inputs with delayed factories | Inputs may be omitted from the signature; retain privately when needed later | Copy and retention lifecycle must be settled before implementation. |
| Read lazy fields | Compute/convert/validate once successfully; failures retry; comparisons may materialize | Supplied-value and mutable deletion/invalidation details need the policy matrix. |
| Override frozen behavior for caches | Class policy inherited unless explicitly overridden; cache exclusion intended | Final spelling and precedence remain open with an adequate semantic starting point. |
| Opt into Undoable equality/order | Reuse required; selected views and hash behavior must be explicit | `compare` collision blocks under P2-1; defaults remain deficient under P3-1. |

The README cannot teach executable usage because this member has no implementation. It does correctly direct a cold reader to requirements and open decisions. The unresolved API spellings above may remain at this gate because they are expressly declared open; the identified Undoable naming collision requires a correction to the brief itself.

### Experiment evidence

The protocol separates documentation preparation, design, implementation and delivery timestamps. It separates billed cost from estimates, identifies missing token coverage, avoids cumulative-counter double counting, and keeps this experiment independent of Undoable’s original results.

Canonical generated examples, differential compatibility tests, narrow failure checks, installation checks and documented-public-use evidence can all be produced under a coherent later design. No requirement depends on a nonexistent benchmark or billing result.

## 3. Risks and next action

Detailed design must still resolve supported Python versions, exact helper interoperability, callable/provider rules, frozen inheritance, lazy mutable deletion behavior, private-provider copying, exception contracts, and hash stability. These are residual design obligations explicitly acknowledged by the object, not additional findings.

The next action is to correct the Undoable comparison namespace and defaults in a new committed requirements checkpoint, then recheck the two bounded findings before proceeding to detailed design. No implementation or baseline runtime change is needed to close this review.