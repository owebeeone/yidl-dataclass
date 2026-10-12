# YIDL Dataclass + Undoable comparison integration — CODE-AXIS REVIEW

**Review object:** Implemented, unreleased consumer candidate at Dataclass `f6c1c561c1670fc26b19da09537fc6822140d8d2` and Undoable `6e7edd17de5b30568f2ffa96dee24fa023dd3061`, including source, authored resources, public documentation, tests and committed evidence.

**Baseline:** Dataclass `d0cc37c061efb8b02bd126e547c01eb87baa904f`; Undoable `f79e4ce6d985ed0a6463552e163baabf1a28942d`. Tracked working-tree files were read after verifying HEAD; baseline comparisons used `git diff BASELINE HEAD`. Both HEADs and their scoped statuses were unchanged at review end.

**Date:** 2026-10-13 Australia/Sydney; review completed 2026-10-12T17:38:08Z.

**Axis:** Code and Surface — architecture, interfaces, call sites, compatibility, implementation provenance and public usability. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on its report. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one P2 storage-contract finding blocks; one P3 documentation finding is nonblocking. I pre-commit to GO on a revision that resolves **P2-1** as specified.

---

## 0. Evidence base

Paths below are relative to their named owning repository. Probe commands use `<installed-G-env>/bin/python` as an external interpreter placeholder.

### Controlling documents and public-first prerequisite

Before private-source review, the public-author phase read only the installed wheel’s four public documents and permitted signatures/public metadata. Its immutable wheel SHA256 was:

`50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b`

The author completed four cards in 276.647023 seconds. Eight executions retained three failures: an incorrect replacement-cache expectation and two counter-collection-window mistakes. Those were author repairs, not product changes or an implementation GO. The standalone record and preserved derivatives are under Dataclass `docs/validation/declarative/public-author/`.

This review read the full canonical Code prompt and the controlling requirements, including:

- `README.md`, `docs/API.md`, `docs/Generation.md`.
- `dev-docs/DataclassConcept.md`, `DataclassSpec-OperatorAmendment.md`, `GoldenExamplesAmendment.md`, `ExperimentProtocol.md`.
- `dev-docs/TaskBoundary.md`, `ScopeCorrection.md`, `ConsumerOnlyGenerationAmendment.md`.
- `dev-docs/DataclassDesign.md`, Sections 1–10; `DataclassPlan.md`, product stages, numerical gates and declarative boundaries.
- Stage D, E/F, G, H and H2 result documents; `ColdSamplingAmendment.md`, `DeclarativeDeskResult.md`, `CurrentProgramCheckpoint.md`, `OutsideScopeFindings.md` and experiment-ledger records.
- Workspace instructions and `AGENTS_GWZ.md`.

### Implementation inspection

Dataclass inspection covered:

- `src/yidl_dataclass/dataclass.py:1–271`: declaration/build execution, namespace installation, comparison selection and replacement.
- `dataclass_harvester.py:1–211`: validation, inherited merge and physical-slot planning.
- `inheritance_plan.py:1–146`: supported bases, override compatibility, copied class cells and descriptors.
- `stdlib_adapter.py:1–172`, `method_actions.py:1–78`, marker/field-kind definitions.
- Provider, policy, retention and copy planning/generation modules.
- Authored core, policy, pipeline, lazy, retention and copy resources.
- `yidl/shared/comparison.yidl`, particularly guards, equality resources, temporary cleanup, ordering/hash shells and productions.
- Canonical inheritance, policy and comparison artifacts; source-contract, hash-action, inheritance and copy tests.

Undoable inspection covered the baseline-to-object implementation diff, its marker/harvester/decorator adapters, regenerator and:

- `src/yidl_undoable/transaction_yidl.py:598–617`: actual managed-write call site.
- `write_comparison_context.py:1–24`: native equality, marker lifetime and cleanup.
- `yidl/undoable_comparison.yidl:1–214`: actual shared productions, view indexing, historical prelude and disabled-inheritance resets.
- Comparison-definition/source tests and the native-dispatch/context test inventory.

Installed resource reads independently matched all 32 Dataclass and 29 Undoable `.py`/`.yidl` source files to the reviewed repository bytes. The shared authority digest was independently confirmed as:

`2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef`

Undoable contained no separately maintained `yidl/shared/comparison.yidl`.

### Executed checks

No builds, installations, regeneration, benchmark executions, file writes or Git mutations were performed.

Narrow installed probes used:

```sh
env PYTHONDONTWRITEBYTECODE=1 ASTICHI_LOWER_ENGINE=native-rust \
  <installed-G-env>/bin/python -I -
```

A separately identified Python-backend probe used `ASTICHI_LOWER_ENGINE=python`.

The probes verified:

- Original Astichi 1.1.3/YIDL 0.1.0, installed package origins and selected backend with `fallback_scope=None`.
- The inherited-lazy-slot counterexample on CPython 3.12.12, 3.13.12 and 3.14.3 with native selection, and separately on 3.12.12 with Python selection.
- `slots=False` declaration identity.
- Undoable exact-view comparison, unhashability, historical callback equality and structural equality in an escaped context after marker closure.

Read-only JSON/hash/XML inspection independently checked:

- All 336 Dataclass Stage G owned-file hashes.
- All 18 installed JUnit hashes and recorded counts.
- All 79 primary compressed and uncompressed evidence hashes, plus four generated-table hashes.
- Fifteen selected complete process results: 59,400 timing rows, 480 memory rows, 90 cold pilots and five distinct parent processes per minor.
- Every 132-case process inventory’s ten warmup and twenty measured batches, normalized units, successful calibration endpoints and 2,790 single-worker cold observations.
- All 216 reported ratio vectors against raw measured process medians.
- All 216 ratio medians and bootstrap intervals through an independent 10,000-resample calculation.
- The H2 canonical definition and nineteen frozen harness-source hashes.
- Interrupted-v1 evidence/source-archive hashes and its separate definition boundary.

Initial audit selections counted preserved `.attempt.json` snapshots alongside final results; selection was corrected to `summary.json`’s fifteen `raw_files`. A separate overstrict assertion assumed globally unique cold PID numbers. Twenty-seven PID numbers recur across the collection; fresh-worker execution is established by a new interpreter subprocess per row, not permanent OS PID uniqueness. These audit corrections did not alter evidence or product bytes.

### Failed live CLI probe retained

Importing the installed regeneration entry point for `main(["--help"])` failed in each supplied G environment:

```text
ImportError: cannot import name 'Lark' from 'lark' (unknown location)
```

Read-only metadata inspection found `lark` version `None`, missing package initialization/metadata, and no `lark-parser` distribution. YIDL’s dependency declaration remains `lark>=1.1`. Recorded G final-smoke evidence reports regeneration/public resources passing.

The present external environments therefore cannot reproduce that live CLI check without restoring their missing dependency files. The deletion cause was not established. This is recorded separately from consumer dependency declarations and archived successful installation evidence; no package or SDK repair was attempted.

## Problem, requirement provenance, and scope

The requested outcome is a near-standard dataclass consumer with direct ordinary storage, specialized policy/lazy behavior, hidden initialization providers, standard metadata/helpers, field-local comparison selection and genuine reusable comparison generation integrated into Undoable. Tests, inspectable goldens, installation evidence, measurements and independent reviews were explicitly requested.

Authorized implementation components are Dataclass and the requested Undoable comparison integration. Original Astichi, YIDL and Lifecycle are reference-only. Workspace configuration, publication and paused UndoableLeaf work remain outside scope.

The original parser-free/full-native-restoration prerequisite was an implementation preference promoted beyond that authority. The correction is adequately disclosed: the original installed-SDK feasibility probe demonstrates slots, equality, hashing, direct reference specialization and template caching on both selected routes. Actual consumer code now uses generated builders, authored resources and existing composition APIs. It does not require the preserved SDK prototype.

The property workaround also follows the supported route. Separately composed decorator fragments had identifier-scope failures; the delivered consumer installs a captured builtin property over exact field-specific functions. This preserves the requested descriptor/access behavior without dependency changes. Literal `@property` spelling was not delivered and is not claimed here.

The cold-sampling amendment addresses a concrete measurement-cost problem within the authorized benchmark component. It changes only cold observation accumulation, retains the original partial attempt, freezes a new definition before collection and leaves hot-operation targets unchanged. It is not a compiler prerequisite or a user sampling requirement.

No new unauthorized component expansion or unsupported infrastructure prerequisite was established. The current missing-Lark environment condition blocks a live CLI reproduction, not an established fresh-install dependency route. It does not authorize dependency implementation work.

P2-1 is a localized violation inside authorized Dataclass inheritance planning. Its remedy requires neither SDK changes nor a new architecture.

## 1. Findings

### [P2-1] Inherited lazy readiness and busy slots are redeclared in every child

**Location:** Dataclass `src/yidl_dataclass/dataclass_harvester.py:178–183`.

**Violated invariant:** Supported inheritance must reuse inherited physical slots. `dev-docs/DataclassDesign.md`, Section 6, explicitly requires reuse without redeclaration to avoid latent shadow storage; `docs/API.md:197–200` promises inherited-slot reuse.

Value-storage slots and retained-provider slots are filtered against `inherited_slots`. Lazy readiness/busy slots are appended without that filter. A child with no new fields consequently introduces new descriptors and storage for names already owned by its base.

**Reproduction:**

```sh
env PYTHONDONTWRITEBYTECODE=1 ASTICHI_LOWER_ENGINE=native-rust \
  <installed-G-env>/bin/python -I - <<'PY'
from yidl_dataclass import dataclass, lazy

@dataclass
class Base:
    value: int = lazy(default_factory=lambda: 7)

@dataclass
class Child(Base):
    pass

print(Base.__slots__)
print(Child.__slots__)
print(Base.__basicsize__, Child.__basicsize__)
print(Child().value)
PY
```

Observed on all three supported minors:

```text
('_y_dc_store_0', '_y_dc_ready_0', '_y_dc_busy_0')
('_y_dc_ready_0', '_y_dc_busy_0')
40 56
7
```

The separately selected Python backend reproduces the same result. A further child increases `__basicsize__` to 72 despite introducing no fields.

**Impact:** Supported inheritance violates its physical-storage contract. Each level allocates two unnecessary slots per inherited lazy field; descendant descriptors shadow ancestor state descriptors. Ordinary lazy reads and copying passed the narrow probe, so no data corruption is asserted. The blocking classification is the concrete supported-layout/parity failure.

**Required correction:** Filter lazy readiness and busy names against inherited physical slots, consistently with value/provider storage planning. Preserve names, field order and specialized getter/setter behavior.

**Closure/regression test:** Extend the canonical inheritance scenario with a base/child/grandchild containing inherited lazy fields and a same-shape override. Verify no inherited physical slot is redeclared, while first/cached reads, mutable reset, readonly rejection and copy/pickle readiness remain correct. Run the affected canonical/source checks across the three supported minors and both original backend selections. Preserve the new artifact provenance; existing H measurements should not be silently relabeled as measurements of changed bytes.

### [P3-1] Public documentation promises replacement even when `slots=False` updates the declaration

**Location:** Dataclass `docs/API.md:15–19`; actual behavior at `src/yidl_dataclass/dataclass.py:217–224`.

**Violated invariant:** Public class-identity and mutation behavior must match the supported interface. The guide unconditionally says decoration returns a generated replacement class and suggests retaining the old declaration for inspection. Dictionary mode instead updates and returns the declaration itself, as the accepted design permits.

**Reproduction:**

```python
from yidl_dataclass import dataclass

class Declaration:
    value: int

model = dataclass(Declaration, slots=False)
assert model is Declaration
assert "__dataclass_fields__" in Declaration.__dict__
```

The installed probe confirmed the assertion. The alleged “old declaration” is the decorated class and receives generated metadata/methods.

**Impact:** Consumers retaining class references can infer incorrect identity and isolation behavior from the public guide. The implementation itself follows `dev-docs/DataclassDesign.md:37–42`.

**Required correction:** Qualify replacement as the `slots=True` behavior and document that `slots=False` updates and returns the declaration. Retain the implemented behavior rather than introducing an unnecessary compatibility change.

**Closure test:** Preserve a small public example or documentation assertion demonstrating both identity cases, and verify the corrected guide is included in the resulting wheel.

## 2. Invariant analysis

### Generation architecture and original-SDK workaround

The decoration call graph lowers harvested facts into fresh generated builders, freezes them, composes `build_DataclassModule`, obtains the executable AST and compiles/executes it with fresh captures. Production model behavior is not emitted by stdlib method generators or a handwritten dynamic method-source generator.

The stdlib private boundary is bounded metadata processing and parameter-shape construction. Authored resources own constructors, policy pipelines, lazy state, copying and comparisons. Ordinary instance fields retain direct public slots. Policy descriptors hold specialized functions over direct backing attributes; comparison operands are specialized public reads.

The property spelling difference is documented and supported by source/descriptor/bytecode projections. Constant expression/statement carriers are likewise disclosed rather than represented as wholly Rust execution.

### Compatibility and helpers

Inspection and evidence attack strict flags, copied real Field metadata, pseudo-field exclusions, keyword-only partitioning, hash-action conflicts, exact-class comparisons and minor-specific equality behavior. Shared equality resources preserve the 3.12 tuple route and later self/short-circuit route, including raw-result return and temporary cleanup.

Named providers, nullable conversion, explicit conversion disabling, readonly caches, hidden InitVar lifetime and replacement rules were exercised in the cold author phase. Its mistaken cache-rebuild expectation was corrected against the documented `init=True` replacement contract.

Class-cell cloning preserves old cells while supporting copied local methods/descriptors. The canonical inheritance case verifies ordinary/const slot reuse and zero-argument `super`; it does not cover inherited lazy flags, explaining why P2-1 escaped.

### Genuine shared comparison and Undoable write semantics

Comparison method productions reside in one neutral Dataclass-owned resource. Both adapters inherit it. Undoable regeneration checks the pinned version/digest and embeds the resource through generated output; runtime execution has no Dataclass authority lookup.

The actual managed-write call retains original operand acquisition and invokes native `bool(old == value)` inside the existing `_call` fence. Identity writes remain `old is value`. The marker stores only an active boolean, closes before ContextVar reset and has no parent/manager/operand retention.

The generated historical prelude precedes structural guards. Hash and ordering do not switch by context. The installed escaped-context attack confirmed historical identity during the callback and structural equality after closure, with enabled facades remaining unhashable.

The native-dispatch/context corpus addresses original operand identity, cached dictionary hashes, tuple/list prefix behavior, proxies, reflection, truth conversion, exceptions, BaseException, ownership faults, nested/copied contexts and disabled-parent/enabled-child cases. No replacement container comparator was found.

### Source, installed and packaging evidence remain distinct

Stage D’s six source runs report 198 cases with only documented minor-specific skips. Stage G independently records:

| Installed corpus, each backend | 3.12 | 3.13 | 3.14 |
| --- | --- | --- | --- |
| Dataclass, 197 collected | 194 pass / 3 skips | 195 pass / 2 skips | 196 pass / 1 skip |
| Undoable with authority | 341 pass | 341 pass | 341 pass |
| Undoable without authority | 334 pass | 334 pass | 334 pass |

The absent-authority runs have explicit ignored build-authority modules and two deselections; they are not complete regeneration runs or mislabeled skips. Dataclass’s three source-only tests are separately recorded.

The artifact inventories and build records distinguish independent consumer sdist rebuilds from unchanged original dependency wheels. Runtime/resource equality connects final documentation-only packaging to the installed corpus. These checks establish the recorded subset; they do not defeat a newly reproduced counterexample such as P2-1.

### H2 measurements and their boundaries

The original accumulated-cold method remains preserved and excluded. H2 measures one first-decoration interval per fresh worker after imports/declaration preparation, with separate pilot/warmup/measured rows. It does not meet the old accumulated-20ms cold rule and does not claim identical variance.

Hot operations retain calibrated batches, common paired counts and alternating variant order. Lazy-first preparation is outside the clock and supplies one unready instance per operation. Generation, source emission and instance operations are separated. Memory accounting includes list-pool overhead and separately reports dictionary-inspection effects.

Independent raw/statistical reconciliation reproduced **73 threshold passes, 47 inconclusive conclusions and zero confirmed regressions**. Forty-six inconclusive conclusions are noisy; one stable interval straddles its target. High recorded system load and unresolved frozen-hash intervals remain limitations. Neither near-one slot-access point estimates nor zero confirmed regressions establish universal performance acceptance.

### Declarative and experiment evidence

The desk result keeps declaration surfaces separate from imperative callbacks and declaration-assembly effects. Field-local comparison policy and one-line deletion are demonstrated; legitimate named-provider references still require diagnostics.

The 31-unit vocabulary and 27-clause interaction inventory are explicitly partial. Independent stdlib/native evidence supports bounded subsets, while designed extension goldens are not independent semantic oracles. Global-capable Python callbacks prevent an effect-free or containment-floor claim.

Calibration anchors, exogenous corpus, second-rater agreement, authoring curves, correctness masses and overall grade remain unscored. The cold author observation is not promoted into those measures.

The experiment preserves the original GO time, SDK detour, operator scope correction and post-GREEN test deviations. API-equivalent estimates remain distinct from unavailable billing. No uninterrupted one-shot, strict all-features-first TDD or final billed-total claim is justified.

## 3. Risks and next action

Residual limitations are the documented callback effects, shallow freezing/hash responsibility, unsupported concurrent lazy first access, private stdlib metadata coupling, incomplete declarative calibration and noisy performance conclusions. The current external Lark damage prevents live CLI reproduction; its cause remains unknown and requires separate environment restoration rather than consumer/SDK source changes.

The next action is a bounded Dataclass remediation of **P2-1**, with its canonical inheritance regression and updated artifact provenance, followed by re-review of that changed scope. Correct **P3-1** in the same documentation pass. No dependency redesign, benchmark-target change or broader workspace work is required.