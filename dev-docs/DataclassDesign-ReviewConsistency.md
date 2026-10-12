# DataclassDesign — CONSISTENCY-AXIS REVIEW

**Review object:** `yidl-dataclass/dev-docs/DataclassDesign.md` at `9fd44d91943ca706c4c51a0669bd3e9d03260278`; proposed detailed design awaiting independent review, dated 2026-10-12. No dataclass runtime implementation is claimed.

**Baseline:**

| Repository | HEAD |
| --- | --- |
| yidl-dataclass | `9fd44d91943ca706c4c51a0669bd3e9d03260278` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| astichi | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

The controlling dataclass documents were read with `git show HEAD:PATH`; numbered source inspections were checked against the pinned repository tuple. All six HEADs matched at the beginning and end. Neighboring working-tree changes were excluded from the review object.

**Date:** 2026-10-12

**Axis:** Consistency against the complete controlling requirements graph, plus the public Surface at this detailed-design interface freeze. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one P2 finding blocks; one P3 documentation finding remains. I pre-commit to GO on a revision that resolves P2-1 and P3-1 as specified.

---

## 0. Evidence base

Read the following documents in the dataclass repository at `9fd44d91943ca706c4c51a0669bd3e9d03260278`:

- `README.md:1–23`, read before the detailed design.
- `dev-docs/DataclassDesign.md:1–679`, including the exact public declarations, compatibility boundary, helper rules, factory/lazy lifetime, inheritance, shared comparison asset, Undoable adapter and verification commitments.
- `dev-docs/DataclassConcept.md:1–258`.
- `dev-docs/ExperimentProtocol.md:1–121`.
- `dev-docs/GoldenExamplesAmendment.md:1–38`.
- `dev-docs/DataclassSpec-OperatorAmendment.md:1–31`.
- `dev-docs/DeclarativeEvaluation.md:1–37`.
- `dev-docs/CurrentProgramCheckpoint.md:1–90`.
- Relevant instrument clauses in `dev-docs/reference/DeclarativeApiEvaluatorV3.md:110–208,314–338,390–432`: locality, search and staging; correctness evidence; E6; and scorecard mode requirements.

Read workspace `AGENTS.md` and `AGENTS_GWZ.md`, the supplied control-flow instructions, and applicable member instructions. No accessible `review-loop/SKILL.md` was found by the targeted filesystem searches; the complete supplied canonical-generated prompt supplied the operative review/report contract. No current-round peer report was accessed and no reviewer or drafter was contacted.

Pinned implementation surfaces inspected:

- YIDL at `9d374f88445c426a56d5dd1f96fad112d1ec5417`:
  - `src/yidl/concept_parser.py:217–320,384–440,1193–1224,3737–3740`.
  - `src/yidl/concept_grammar.lark:34`.
  - `src/yidl/generation/assembly_source.py:20–82`.
  - `tests/data/yidl/yidl_update_a_dataclasses_split/dataclasses_base.yidl:1–250`.
  - Relevant generation rules in `dev-docs/YidlCodingRules.md` and `dev-docs/YidlDesignSummary.md`.
- Astichi at `1c47f781d3804130fdd61cbee07a3b2e4529158a`:
  - Applicable instructions and active summary/coding rules.
  - `src/astichi/lowering/external_ref.py:300–465`, covering external reference lowering and restricted path validation.
- Lifecycle at `230362f642d6e9205897698670fe5f87d2c905ce`:
  - `src/yidl_lifecycle/regenerate_lifecycle_base.py:1–103`.
  - `src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl:1–220`.
- Undoable at `f79e4ce6d985ed0a6463552e163baabf1a28942d`:
  - `src/yidl_undoable/undoable_markers.py:1–33`.
  - `src/yidl_undoable/undoable_harvester.py:1–132`.
  - `src/yidl_undoable/facades.py:20–165`.
  - `src/yidl_undoable/transaction_yidl.py:597–616`.
  - `src/yidl_undoable/values.py:1–133`.
  - `src/yidl_undoable/yidl/undoable_core.yidl:38–120`.

Consulted the primary CPython [3.12 implementation](https://github.com/python/cpython/blob/3.12/Lib/dataclasses.py), [3.13 implementation](https://github.com/python/cpython/blob/3.13/Lib/dataclasses.py) and [3.14 implementation](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py) for constructor suppression, dictionary defaults, replacement and version-selected equality.

Two read-only, in-memory stdlib probes were run using:

```text
PYTHONDONTWRITEBYTECODE=1 yidl/.venv/bin/python -
```

The interpreter reported CPython `3.12.12`. Observations:

1. A dictionary dataclass with `x = field(init=False, default=1)` had an empty instance dictionary. Updating the class default to `2` changed the instance read to `2`. A plain `field(init=False)` without a default was accepted and initially absent.
2. A slotted dataclass with `x = field(init=False)` and a local custom initializer assigning `self.x = 3` decorated and constructed successfully. A slotted class with decorator `init=False` also permitted later assignment to that slot.

These were stdlib probes, not tests of a nonexistent dataclass implementation. No builds, regeneration, mutation-bearing tests, file writes or Git mutations were performed.

## 1. Findings

### [P2-1] The unconditional provider-availability rule contradicts ordinary initializer suppression

**Location:** Dataclass repository, `dev-docs/DataclassDesign.md:271–285` and `:373–377`, at `9fd44d91943ca706c4c51a0669bd3e9d03260278`.

**Violated invariant:** A settled detailed design must give one outcome for every admitted declaration. Section 6 explicitly permits purely ordinary classes with a local custom initializer or decorator `init=False` to follow stdlib suppression semantics. Section 5 independently requires rejection of every `init=False` required field without a default/factory, without an exception for those classes or a requirement that the field actually be consumed by a generated factory.

**Reproduction:**

```python
@dataclass
class Model:
    value: int = field(init=False)

    def __init__(self):
        self.value = 3
```

This uses ordinary writable storage, no conversion or validation, no providers, no policy fields and no generated initialization requirement.

- Under lines 376–377, preserve the local initializer and follow std suppression semantics; construction produces `value == 3`.
- Under lines 273–274, reject decoration because `value` is `init=False` and has neither a default nor a factory.

The read-only CPython 3.12.12 probe accepted this declaration with `slots=True` and produced `3`, confirming that the suppression contract is consequential. The stdlib method decision table preserves a local initializer. [CPython 3.12 source](https://github.com/python/cpython/blob/3.12/Lib/dataclasses.py)

The same contradiction applies to a purely ordinary declaration with decorator `init=False`, where application code initializes the slot later.

**Impact:** Implementers must choose between contradicting the advertised ordinary-field compatibility contract and contradicting the mandatory graph validation rule. The versioned differential corpus cannot assert both outcomes. This is an implementation-readiness defect, rather than a request for broader unsupported parity.

**Required correction:** Resolve the initializer action before enforcing generated-initialization availability. Distinguish:

- fields whose values must be established by generated construction;
- providers actually required by generated factory calls;
- ordinary fields governed by suppressed initialization.

Preserve the explicitly promised std suppression behavior for the last category. Retain the unavailable-provider diagnostic when a generated consumer requires a value that construction cannot supply.

Also make the ordinary dictionary-mode rule explicit: an unconverted, unvalidated `init=False` field with a simple default remains a class-default fallback rather than being installed into every instance. The current “evaluate all eager fields” instruction should explain this exception. The probe demonstrated the observable difference after changing the class default; CPython’s `_field_init` implements that distinction. [CPython 3.12 source](https://github.com/python/cpython/blob/3.12/Lib/dataclasses.py)

**Closure/regression test:** Add versioned differential cases for:

1. A plain required `init=False` field initialized by a local custom initializer.
2. A plain required `init=False` field with decorator `init=False`, followed by explicit assignment.
3. A dictionary-mode `init=False` simple default, checking the instance dictionary and subsequent class-default changes.
4. A generated dependent factory whose required provider is unavailable, verifying that the intended diagnostic still fires.

At the design gate, close the finding by making these outcomes unambiguous in Sections 5 and 6. Runtime closure belongs in the subsequent implementation corpus.

### [P3-1] The cold README still says the reviewed detailed design remains unwritten

**Location:** Dataclass repository, `README.md:11–13`, contrasted with `dev-docs/DataclassDesign.md:3–13` and `dev-docs/CurrentProgramCheckpoint.md:84–90`, all at `9fd44d91943ca706c4c51a0669bd3e9d03260278`.

**Violated invariant:** The public entry point and controlling checkpoint must identify the same document state.

**Reproduction:** Read the README without conversation context. It says that the detailed design and compatibility matrix remain to be developed, and links the starting concept but not the existing detailed design. The checkpoint says that `DataclassDesign.md` is ready for dual review, and that document contains the settled API and compatibility matrix under review.

**Impact:** A developer or later reviewer entering through the README is directed toward the requirements-era open decisions and receives an incorrect account of the current contract’s existence.

**Required correction:** Link `dev-docs/DataclassDesign.md` from the README and identify it as a proposed design awaiting independent acceptance. Keep the TDD plan and implementation described as subsequent work.

**Closure test:** A cold README read should reach the current proposed API and compatibility matrix directly, with acceptance status agreeing with the checkpoint. No runtime test is needed.

## 2. Invariant analysis

The following attacks did not establish additional findings:

- **Accepted architecture and authoring locality:** The design preserves one generated class, direct public storage for ordinary writable fields, specialized policy properties, named factories and field-local comparison controls. It does not reintroduce a decorator field-name selection map. These agree with `DataclassConcept.md:21–47,69–103,140–159` and the operator amendment.
- **Defaults and policy precedence:** Decorator defaults are explicit. Mutability inherits `not frozen`; const fixes read-only behavior; local storage remains writable and excluded from comparison/hash. Frozen mutable exceptions must be excluded from both comparison and effective hash. These rules are internally compatible.
- **Public helpers and hidden providers:** Real std Field metadata is separated from local storage. Standard inspection/data helpers exclude pseudo-fields and extension backing state. Standard replacement’s hidden-InitVar limitation is expressly bounded; package replacement reruns construction without replaying retained values. Copy/pickle preserve lazy readiness and retained-provider state, with active evaluation rejected.
- **Lazy lifetime:** Named cycles are rejected before construction. Busy guards cover opaque runtime reentry. Failed evaluation permits retry; successful dependencies remain cached. Retention follows direct delayed consumers and keeps providers for resettable consumers. The design does not claim concurrency, reactive invalidation or rollback of arbitrary callback side effects.
- **Version-selected comparison:** The 3.12 tuple mode and the 3.13/3.14 self-identity shortcut plus conjunction mode agree with the inspected CPython implementations. Ordering remains tuple-based; selected lazy operands materialize according to actual evaluation. [CPython 3.12](https://github.com/python/cpython/blob/3.12/Lib/dataclasses.py), [CPython 3.13](https://github.com/python/cpython/blob/3.13/Lib/dataclasses.py), [CPython 3.14](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py)
- **Class replacement and inheritance:** Supported bases, frozen inheritance, slot-shape compatibility, override families, closure-cell cloning, descriptor set-name calls and repeated subclass creation are explicitly bounded. The design acknowledges observable replacement effects rather than promising transparent support for arbitrary metaclass protocols.
- **Native composition feasibility:** The pinned YIDL compiler accepts source maps and relative logical imports, supports multiple concept extensions, and emits assembly entry-point builders. The inspected Astichi path lowering supports the proposed restricted Name/Attribute binding approach. These surfaces support the proposed modular construction; no evidence required a fallback parser, consumer string formatter or std method generator.
- **Shared comparison ownership:** The neutral asset is assigned to YIDL; consumer adapters supply operands and target surfaces; shared productions own method bodies. Stable logical source keys and installed-resource loading address sibling-checkout dependence. The neutral fixture and two real consumers remain mandatory future implementation evidence.
- **Undoable behavior:** Disabled structural generation retains the existing defaults. Enabled generation has explicit view/type guards and disables hashing on every facade. Logical inclusion and legacy write policy remain separate. The proposed value-write projection addresses the actual `old == value` call site and preserves node identity independently of generated logical equality. Hash-container restrictions are stated rather than bypassed.
- **Evidence and measurement:** The design distinguishes future verification from completed evidence, requires independent std differential checks, and keeps historical Undoable measurements separate. Canonical source/behavior examples, installation/resource checks and benchmark methodology are specified. Numeric thresholds are assigned to the subsequent reviewed TDD plan before results.

No superseded controlling clause list is asserted by this design. It resolves requirements-era open choices while retaining the operator-accepted architecture and locality boundary.

## 3. Risks and next action

Private stdlib adapters, closure cloning, lazy-state copying and the identity-preserving Undoable write projection still require implementation evidence across supported interpreters. The design’s stated gates appropriately cover those risks; source inspection alone does not establish their correctness or performance.

The next action is a bounded design revision resolving ordinary initialization suppression and correcting the README, followed by re-verdict on the new exact tuple. The separate TDD plan and runtime implementation remain behind that acceptance gate.