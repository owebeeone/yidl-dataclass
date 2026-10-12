# Dataclass specification — SAFETY-AXIS REVIEW

**Review object:** `yidl-dataclass/README.md`, `yidl-dataclass/dev-docs/DataclassConcept.md`, and `yidl-dataclass/dev-docs/ExperimentProtocol.md` at `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`. The concept is the controlling DRAFT. Status: requirements stage; no implementation exists.

**Baseline:**

| Repository | Verified HEAD |
| --- | --- |
| yidl-dataclass | `8c116f51310343b18e4ebae27ea6a91517f828e4` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |

Reviewed documents and supporting source were read with `git show SHA:PATH`; working-tree searches located supporting files but did not determine their reviewed contents.

**Date:** 2026-10-12, Australia/Sydney.

**Axis:** Safety — what the text permits to go wrong, including compatibility boundaries, changing values, callbacks, retained inputs, and experiment evidence. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one P2 finding blocks. I pre-commit to GO on a revision that resolves P2-1 as specified. This verdict concerns fitness as a requirements brief, not implementation readiness.

---

## 0. Evidence base

Read the following immutable specification and authority material:

- At spec object `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`:
  - `yidl-dataclass/README.md`, lines 1–18.
  - `yidl-dataclass/dev-docs/DataclassConcept.md`, lines 1–180.
  - `yidl-dataclass/dev-docs/ExperimentProtocol.md`, lines 1–111.
- At dataclass HEAD `8c116f51310343b18e4ebae27ea6a91517f828e4`:
  - `yidl-dataclass/dev-docs/CurrentProgramCheckpoint.md`, lines 1–42.
- Workspace `AGENTS.md` and `AGENTS_GWZ.md`.
- The local `review-loop/SKILL.md` process authority, including peer blindness, immutable draft objects, severity definitions, and the rule that deferrals do not exempt interface shape.

Read these pinned reference sources:

- Undoable at `f79e4ce6d985ed0a6463552e163baabf1a28942d`:
  - `README.md`, lines 1–89.
  - `docs/API.md`, lines 1–137.
  - `src/yidl_undoable/undoable.py`, lines 1–76.
  - `src/yidl_undoable/undoable_markers.py`, lines 1–33.
  - `src/yidl_undoable/facades.py`, lines 1–170.
  - `src/yidl_undoable/values.py`, lines 1–133.
  - `src/yidl_undoable/graph.py`, lines 1–50.
  - `src/yidl_undoable/transaction_yidl.py`, lines 585–627.
- Lifecycle at `230362f642d6e9205897698670fe5f87d2c905ce`:
  - `README.md`, lines 1–76.
  - `src/yidl_lifecycle/lifecycle_markers.py`, lines 1–240 and 335–425.
  - `src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl`, lines 1–285.
  - `src/yidl_lifecycle/yidl/lifecycle_const_static.yidl`, lines 1–125.
- YIDL at `9d374f88445c426a56d5dd1f96fad112d1ec5417`:
  - `tests/data/yidl/yidl_update_a_dataclasses_split/dataclasses_base.yidl`, lines 1–165.

Ran only read-only inspection commands: `cat`, `rg`, `nl`, `sed`, `git show`, `git rev-parse HEAD`, and `git status --short`. No tests, builds, writes, or Git mutations were performed.

The four HEAD values matched the supplied tuple at the beginning and end. Dataclass initially had a clean working tree; the final status additionally showed the owner-announced, out-of-scope `dev-docs/GoldenExamplesAmendment.md`. Its contents were not read. Neighboring working-tree changes were excluded, and no current-round reviewer report was read.

## 1. Findings

### [P2-1] The proposed Undoable `compare` selector collides with its existing transaction policy

**Location:** `yidl-dataclass/dev-docs/DataclassConcept.md` at `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`, lines 69–75, particularly “`compare` selects a field for both.” Supporting experiment requirements are at `dev-docs/ExperimentProtocol.md`, lines 58–62, at the same SHA.

**Violated invariant:** Adding generated object equality and ordering must not reinterpret the independent policy controlling whether a managed assignment records a changed value. The consumer boundary must distinguish those controls before the integration is designed.

The pinned API already assigns `compare` a different meaning:

- `yidl_undoable/docs/API.md` at `f79e4ce6d985ed0a6463552e163baabf1a28942d`, lines 65–66: `"value"` performs equality and truth conversion; `"identity"` skips only the same reference.
- `yidl-lifecycle/src/yidl_lifecycle/lifecycle_markers.py` at `230362f642d6e9205897698670fe5f87d2c905ce`, lines 169–193: `managed(compare="value", ...)`.
- The same file, lines 411–412, rejects every value other than `"value"` or `"identity"`.
- `yidl_undoable/src/yidl_undoable/undoable_markers.py` at its pinned SHA, lines 1–18, re-exports Lifecycle’s marker factories rather than defining an independent declaration dialect.
- `yidl_undoable/src/yidl_undoable/transaction_yidl.py` at its pinned SHA, lines 607–616, consumes `fact["compare"]` to choose identity or value comparison before recording a managed write.

**Reproduction/state sequence:** Consider a managed field whose transaction policy is `"identity"` and which must be excluded from generated object equality and ordering. The new brief calls its exclusion control `compare=False`, but the existing `managed(compare=...)` position is already occupied. Following the boolean spelling against the pinned marker raises `LifecycleDefinitionError`. Replacing the existing metadata value with `False` to admit that spelling makes the pinned write path select value comparison instead of identity comparison.

For two distinct but equal immutable values, an identity-policy assignment should record the replacement. That conflated path suppresses it. Conversely, retaining `"identity"` and treating its truthiness as field selection makes the field participate in generated comparisons when the declaration intended exclusion. One metadata control cannot independently express both decisions.

This is a source-traced counterexample, not an executed implementation test. It identifies an existing public-name collision and the unsafe interpretation the brief leaves available.

**Impact:** The integration can change transaction write detection, reject the advertised selector, or force edits to Lifecycle’s shared marker API even though Lifecycle is only a prospective comparison consumer. Testing existing behavior only with generated comparisons disabled does not establish independence when the new feature is enabled.

**Required correction:** Amend the brief to require independently representable transaction comparison policy and generated equality/ordering inclusion. State that existing `"value"`/`"identity"` behavior remains unchanged with generated comparisons both enabled and disabled. Give the new selector an unambiguous name or explicitly separate metadata namespace; do not silently repurpose the shared marker’s `compare` value. Its detailed storage and generation mechanism may remain a design decision.

**Closure/regression test:** At this requirements gate, verify the amendment explicitly permits all four combinations of transaction policy (`"value"`/`"identity"`) and logical comparison inclusion (included/excluded). Require the subsequent TDD plan to exercise those combinations with generated equality enabled and disabled: distinct equal values must still record replacement under identity policy, same-reference writes must still skip, and excluded fields must not affect equality or ordering. Existing Lifecycle marker behavior must remain unchanged unless a separate amendment explicitly authorizes changing it.

## 2. Invariant analysis

The remaining attacks did not establish a defect in this requirements-stage object:

- **Hash keys after writes and history movement:** A frozen class with mutable logical fields, or a live Undoable facade with value-based equality, can invalidate dictionary/set assumptions. The brief explicitly requires equality/hash consistency and rules for changing facade values (`DataclassConcept.md`, lines 62–79), and separately requires hash-stability rules for lazy fields (lines 131–134). It does not promise that every such combination is hashable. A reviewed design can reject unsafe combinations or make them unhashable without contradicting the requirements.

- **Hashability within managed collections:** Undoable currently uses identity equality and stable node hashing (`facades.py`, lines 153–157), while `values.py`, lines 68–78, decodes managed frozensets into facade collections. Value-comparison integration therefore needs explicit restrictions or suitable handling. The required consumer-specific compatibility and hash contract can resolve this; the brief does not require unchanged collection support for every newly enabled comparison mode.

- **Lazy reads of retained initialization inputs:** Reusing one private provider across several delayed factories raises aliasing, cleanup, and copy questions. Lines 95–99 require retention without ordinary exposure, representation, equality, or serialization and require an explicit retention/copying rule. Lines 131–134 require availability for delayed factories and failure/reentrancy rules. Snapshot versus retained-reference semantics remain a legitimate design choice.

- **Conversion/validation failures and callback reentry:** The stated pipeline validates before installation or provision to dependents (lines 103–108); lazy failure leaves the target unset for retry (lines 126–134). The text does not claim rollback of arbitrary external callback effects. Callback behavior and diagnostics require later rules, so an implementation cannot treat their current omission as an accepted failure contract.

- **Cache mutation and frozen objects:** The brief distinguishes reference replacement from mutable contents and calls for excluding caches from logical comparisons and hashing (lines 112–122). Private cache mutation need not violate frozen logical state. It makes no recursive immutability claim.

- **Direct slots versus policy enforcement:** Ordinary writable fields have a direct public-slot path; fields needing conversion, validation, lazy, or read-only behavior may use specialized properties (lines 28–47). These requirements do not force assignment validation through an ordinary slot or conceal that property overhead in ordinary-slot benchmarks.

- **Misleading experimental conclusions:** The protocol separates compatible behavior from extensions, ordinary slots from policy paths, first lazy access from cached access, generation from steady-state work, and billed cost from dated estimates. It requires raw observations, variation, missing-coverage disclosure, operator-intervention records, independent installation, and separate integration revisions. No benchmark, billing, or one-pass-correctness result is asserted.

- **Scope creep:** The concept authorizes planning the Undoable integration rather than an immediate runtime edit, leaves Lifecycle prospective, and excludes transaction machinery from the dataclass model. The checkpoint excludes adjacent drafts and preserves original Undoable measurements. P2-1 is the specific remaining hole in that boundary.

## 3. Risks and next action

The detailed design must resolve callback reentry, lazy dependency cycles and retry behavior, retained-provider copying and cleanup, frozen inheritance, writable logical fields and hashing, Undoable cross-view comparisons, and facade collection hashability. These are explicit future decisions, not additional findings against this brief.

The single next action is to correct P2-1 in the committed requirements object and return the revised tuple for a focused safety re-verdict. Implementation should remain behind the subsequent detailed-design review and TDD-plan gates.