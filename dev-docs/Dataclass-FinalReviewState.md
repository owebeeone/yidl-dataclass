# YIDL Dataclass and shared Undoable comparisons — STATE-AXIS REVIEW

**Review object:** Dataclass `f6c1c561c1670fc26b19da09537fc6822140d8d2`; Undoable `6e7edd17de5b30568f2ffa96dee24fa023dd3061`. Implemented consumer source, resources, documentation, tests and evidence; final acceptance pending.

**Baseline:** Dataclass `d0cc37c061efb8b02bd126e547c01eb87baa904f`; Undoable `f79e4ce6d985ed0a6463552e163baabf1a28942d`. Sources were read from the pinned checkouts; relevant baseline behavior was inspected with `git diff`.

**Date:** 2026-10-13, Australia/Sydney.

**Axis:** State machines, failed-operation recovery, retained authority, copying, native write-comparison semantics and evidence integrity. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — two P2 findings block acceptance; one P3 finding also remains. No P0 or P1 finding was established. I pre-commit to GO on a revision that resolves P2-1, P2-2 and P3-1 as specified, passes their targeted closure checks and introduces no new defect.

---

## 0. Evidence base

### Tuple and inspection boundary

`git rev-parse HEAD` and `git status --short` were run in each owning repository at the start and end. Both HEADs remained exactly pinned.

Dataclass initially had the two untracked final-review prompts; its final status also listed the owner-filed `dev-docs/Dataclass-FinalReviewCode.md`. That report was **not opened or used**. Undoable retained only its excluded modified checkpoint and untracked UndoableLeaf document. No files, Git state, environments or artifacts were changed by this review.

Workspace instructions and the complete canonical `dev-docs/Dataclass-FinalPromptState.md` were read. No additional member AGENTS files were found.

The controlling documents inspected were:

- `README.md`, `docs/API.md`, `docs/Generation.md`.
- `dev-docs/DataclassConcept.md`, `DataclassSpec-OperatorAmendment.md`, `GoldenExamplesAmendment.md`, `ExperimentProtocol.md`.
- `dev-docs/TaskBoundary.md`, `ScopeCorrection.md`, `ConsumerOnlyGenerationAmendment.md`, `OutsideScopeFindings.md`.
- `dev-docs/DataclassDesign.md`, §§1–10 and reference inspection; `DataclassPlan.md`, §§1–7.
- Prior `DataclassDesign-ReviewSafety-3.md` and both design remediation plans.
- Stage D, E/F, G, H and H2 preparation result documents, `ColdSamplingAmendment.md`, `DeclarativeDeskResult.md`, the checkpoint and experiment ledger.

Principal implementation inspection included these repository-relative locations:

| Owner | Files/ranges |
| --- | --- |
| Dataclass | `src/yidl_dataclass/dataclass.py:1–271`; `dataclass_harvester.py:1–211`; `provider_plan.py:1–246`; `policy_plan.py:1–184`; `retention_plan.py:1–45`; `retention_generation.py:1–39`; `copy_generation.py:1–87`; `inheritance_plan.py:1–146` |
| Dataclass | `src/yidl_dataclass/yidl/dataclass_pipelines.yidl:1–130`; `dataclass_policies.yidl:1–176`; `dataclass_lazy.yidl:1–306`; `dataclass_lazy_init.yidl:1–101`; `dataclass_retention.yidl:1–65`; `dataclass_copy.yidl:1–202`; shared comparison hash resources at `shared/comparison.yidl:96–103` |
| Undoable | `src/yidl_undoable/write_comparison_context.py:1–24`; `callbacks.py:1–98`; `transaction_yidl.py:510–645`; `facades.py:1–230`; decorator/harvester integration and authored comparison adapter |
| Undoable | `src/yidl_undoable/yidl/undoable_core.yidl:38–103`; `undoable_comparison.yidl:157–173`; view resources |

Relevant canonical and diagnostic sources were read, including Dataclass copy, lazy retention, pipeline ownership and inheritance cases; lazy/copy/pipeline failure tests; Undoable comparison/write goldens; and the complete `tests/test_write_native_dispatch.py` and `tests/test_write_comparison_context.py`.

### Installed probes

Only narrow inline probes were executed:

```sh
PYTHONDONTWRITEBYTECODE=1 ASTICHI_LOWER_ENGINE=native-rust \
  <installed-env>/bin/python -I - <<'PY'
# Inline counterexample or read-only evidence audit.
PY
```

A separately labeled CPython 3.12 probe selected `ASTICHI_LOWER_ENGINE=python`. Backend substitution was not used to repair a failing observation.

The original environments reported CPython 3.12.12, 3.13.12 and 3.14.3. On 3.12, consumer and SDK import origins were verified beneath the installed environment; versions were Dataclass 0.1.0.dev0, Undoable 0.1.0, Astichi 1.1.3, YIDL 0.1.0 and Lifecycle 0.1.0. All 37 Dataclass and 34 Undoable packaged file hashes matched `docs/validation/stage-g/artifact-tuple-final.json`; Dataclass runtime/resource source hashes also matched.

Probes covered constructor DAG processing and partial-instance leakage; cancellation/retry; seeded terminal release; shallow/deep/pickle cyclic memo state; dictionary copying/fallback; inherited frozen caches; active copying; native original operands; cached dictionary hashes; tuple/list prefix behavior; copied/thread/task contexts; manager reentrancy/ownership faults; facade pins and history movement; and the counterexamples in Findings.

Both naming defects reproduced on all three installed native-rust minors. The Dataclass builtin-name failures and Undoable scope-name failure also reproduced on explicitly selected Python lowering on 3.12.

No build, install, regeneration, full test matrix or benchmark was run.

### Complete performance evidence audit

Read-only gzip/JSON/hash parsing verified all **79 primary manifest members**, including their compressed and decoded derivative hashes. The nineteen frozen harness-source hashes matched the H2 definition.

All fifteen complete process results and attempts were inspected. Independent accounting verified:

- Five processes per supported minor; fifteen distinct parent PIDs.
- **59,400 timing rows:** 19,800 warmup and 39,600 measured.
- Complete 132-case timing inventories, batch ranges, source identities and reconciled ns/op units.
- Completed ordinary/extension/seam calibrations at least 20 ms.
- **480 memory observations**, each using 10,000 instances.
- **90 cold pilots** and **2,790 individual cold workers**, one operation per cold row, with matching provenance and distinct worker identities within each parent.
- **74,353 journal rows**, contiguous zero-based sequences, matching timing/memory payloads and terminal validation.
- Attempt/result equality for every completed process.

All **216 paired comparison summaries** were independently recomputed from process medians, including ratios, dispersion, 10,000 seeded pair resamples, intervals and verdicts. Results matched **73 pass, 47 inconclusive, zero confirmed regressions**. The 180 absolute product summaries and 96 memory summaries also reconciled to raw observations.

The five interrupted-v1 derivative members and frozen source archive hash verified. Its journal retains 2,757 cold workers, 1,967 timing rows, 397 calibration rows, sixteen memory rows and terminal `KeyboardInterrupt`; these rows were excluded from H2 aggregation.

Reviewer audit setup failures were corrected without modifying evidence: treating list-shaped inventory keys as strings, assuming exact equality of explanatory source/classification dictionaries, including attempt files in a result glob, and assuming PIDs could not be reused across different parent lifetimes. These were reviewer assumptions, not product failures. Probe/audit stdout and tracebacks remain in the review transcript; no additional raw-output file was invented.

## Problem, requirement provenance, and scope

The authorized outcome is a near-standard single generated Dataclass with direct ordinary slots, specialized const/lazy/pipeline behavior, construction-only providers, safe retained-provider lifetime, writable excluded frozen caches, real metadata/helpers and reusable authored comparison YIDL actually consumed by Undoable. Tests, inspectable goldens, installation, measurements and independent reviews are explicit experiment deliverables.

Authorized implementation components are the Dataclass consumer and its resources/evidence, plus Undoable’s requested comparison integration. Original Astichi, YIDL and Lifecycle are reference-only; workspace configuration, publication and the paused UndoableLeaf work are excluded.

The preserved SDK detour addressed an owner-imposed parser-free/full-native preference, not demonstrated necessity for this outcome. `ScopeCorrection.md`, `TaskBoundary.md` and `docs/validation/baseline/original-sdk-results.json` distinguish this clearly. The original supported consumer route has concrete feasibility evidence on both backend selections, and the inspected installed artifacts use that route. No dependency change is needed to correct these findings.

The cold amendment similarly corrects a self-imposed measurement method. Preserved v1 calibration selected many fresh stdlib workers merely to accumulate 20 ms of generator intervals. Single-worker cold observations address that sampling cost locally, retain uncertainty and leave product behavior, ordinary calibration and numerical thresholds unchanged. They are not relabeled as satisfying the old cold method.

Scope and necessity therefore hold for the present implementation boundary. The blocking defects below are localized consumer-generation defects within that boundary. Prior designs and GO verdicts do not exempt them.

Outside-scope compiler limitations remain separately classified in `OutsideScopeFindings.md`, with evidence, impact, suggested follow-up and a nonblocking assessment. They do not justify reopening SDK implementation.

## 1. Findings

### [P2-1] Dataclass’s generated class binding overwrites names required by its methods

**Location:** Dataclass `src/yidl_dataclass/dataclass.py:210–216`; `src/yidl_dataclass/yidl/dataclass_copy.yidl:52–104`; `src/yidl_dataclass/yidl/shared/comparison.yidl:96–103`. Private-name checks at `dataclass_harvester.py:51–54` do not check the declaration’s class name.

**Violated invariant:** A supported model name must not change copy/state/hash behavior or replace captured application callbacks. Class generation must preserve its runtime dependencies.

The class is executed under its declared name in the same globals dictionary used by generated methods. That output binding can replace a builtin lookup or an existing private capture:

- Class `type`: generated copy calls `type(self)`, which invokes the generated model instead of builtin `type`.
- Classes `tuple`, `dict` and `int`: state validation compares against the generated model instead of the builtin schema type.
- Frozen class `hash`: generated hashing invokes the model constructor instead of builtin `hash`.
- Class `_y_dc_converter_0`: the output overwrites its converter capture, causing recursive construction.

Reproduction from the installed package:

```sh
PYTHONDONTWRITEBYTECODE=1 ASTICHI_LOWER_ENGINE=native-rust \
  <installed-env>/bin/python -I - <<'PY'
import builtins
import copy
from yidl_dataclass import dataclass, const, field

for name in ("type", "tuple", "dict", "int", "hash", "_y_dc_converter_0"):
    marker = (
        field(default=3, converter=builtins.int)
        if name.startswith("_")
        else const(default=3)
    )
    model = dataclass(
        builtins.type(
            name, (),
            {"__annotations__": {"value": builtins.int}, "value": marker},
        ),
        frozen=name == "hash",
    )
    try:
        obj = model()
        if name == "hash":
            builtins.hash(obj)
        else:
            copy.copy(obj)
    except BaseException as exc:
        print(name, exc.__class__.__name__, str(exc))
PY
```

Observed on all three native-rust minors:

| Name | Result |
| --- | --- |
| `type` | `TypeError: object.__new__(X): X is not a type object (type)` |
| `tuple`, `dict`, `int` | `ValueError: unsupported dataclass state schema` |
| `hash` | `TypeError: __hash__ method should return an integer` |
| `_y_dc_converter_0` | `FieldConversionError`; underlying recursion |

`copy.deepcopy` has the same `type` failure. A `tuple` model also rejects the exact state returned by its own `__getstate__`.

**Impact:** Decoration and construction can succeed, followed by failure of documented copy/state/hash operations. Private capture collision can instead fail construction and run unintended constructor/pipeline calls. This is a compatibility and state-restoration defect, not a performance concern.

**Required correction:** Make the generated output binding independent of names required by generated methods and application captures. Preserve ordinary valid names such as `type`, `tuple`, `dict`, `int` and `hash`; do not solve this by silently narrowing that public subset. Audit the complete generated builtin/capture surface, including copy, reduction, hashing and callbacks. Any intended private namespace reservation must reject consistently at decoration and be documented.

This is a bounded consumer execution/resource correction using existing SDK facilities. It requires neither SDK work nor architectural redesign.

**Closure test:** Add narrow collision recognition/failure coverage and canonical supported-name behavior. Verify shallow/deep copy, valid state roundtrip, module-level pickle, generated hash and callback identity across the three minors and both original backend selections. Confirm generation executes no callbacks and the shared-resource regeneration boundary remains reproducible.

### [P2-2] Undoable class identifiers can lexically shadow historical comparison captures

**Location:** Undoable `src/yidl_undoable/yidl/undoable_core.yidl:42–76`; `src/yidl_undoable/yidl/undoable_comparison.yidl:157–162`; `src/yidl_undoable/undoable.py:115–135`.

**Violated invariant:** The generated equality prelude must read the captured ContextVar and invoke the captured historical facade method, irrespective of the model’s accepted name.

Unlike P2-1’s global overwrite, this site creates a lexical binding. A class named `_u_historical_write_scope` or `_u_historical_eq` is defined inside `build_undoable_class`. Python consequently treats that name as a builder local, and generated equality closes over the model class instead of resolving the intended global capture.

Exact installed counterexample:

```sh
PYTHONDONTWRITEBYTECODE=1 ASTICHI_LOWER_ENGINE=native-rust \
  <installed-env>/bin/python -I - <<'PY'
import builtins
from yidl_undoable import undoable, managed, UndoRedoManager

for name in ("_u_historical_write_scope", "_u_historical_eq"):
    model = undoable(
        builtins.type(
            name, (),
            {"__annotations__": {"value": int}, "value": managed(default=2)},
        ),
        eq=True,
    )

    @undoable
    class Parent:
        children: tuple = managed(default=())

    manager = UndoRedoManager()
    a = model(transaction_manager=manager)
    b = model(transaction_manager=manager)
    parent = Parent(children=(a,), transaction_manager=manager)
    manager.initialize(parent, a, b)
    manager.begin()
    try:
        if name.endswith("scope"):
            a == b
        else:
            parent.children = (b,)
    except BaseException as exc:
        print(name, exc.__class__.__name__, str(exc))
    finally:
        manager.rollback()
PY
```

Observed on CPython 3.12.12, 3.13.12 and 3.14.3:

- `_u_historical_write_scope`: `AttributeError`, because the generated class has no `.get()`.
- `_u_historical_eq`: outside-scope structural equality succeeds, but replacing an equal-valued distinct child raises `TypeError` because the prelude calls the generated constructor with `(self, other)`.

The second failure leaves the edit and old child intact; no corruption was observed. It nevertheless prevents the required native value-write operation for an accepted declaration.

**Impact:** Ordinary equality or a later managed assignment fails after successful decoration/construction. Historical write compatibility becomes dependent on the class identifier.

**Required correction:** Prevent generated class/view bindings from shadowing prelude dependencies in the builder’s lexical scope, or reject an explicitly reserved private class namespace before generation with a clear documented diagnostic. Audit both class and view identifiers against the new comparison captures. A Dataclass globals fix alone does not close this separate site.

This is a bounded Undoable consumer-template/validation correction; no comparator redesign or SDK change is necessary.

**Closure test:** Retrace both names on the supported minor/backend matrix. Accepted declarations must preserve structural equality outside scope and historical identity during actual equal-valued distinct-child replacement. If private names are deliberately reserved, assert contextual decoration errors before any generation/runtime operation. Retain copied-context cleanup and manager-fence checks.

### [P3-1] Inherited lazy flags are redeclared as shadow slots

**Location:** Dataclass `src/yidl_dataclass/dataclass_harvester.py:173–183`.

**Violated invariant:** `docs/API.md`, inheritance section, and `dev-docs/DataclassDesign.md`, §6, require inherited slots to be reused without latent shadow storage.

Backing/provider slots are filtered against inherited descriptors, but lazy ready/busy slots are appended unconditionally.

Installed layout inspection:

```python
@dataclass(repr=False)
class Base:
    value: int = lazy(default_factory=lambda: 3)

@dataclass(repr=False)
class Child(Base):
    pass

@dataclass(repr=False)
class Grandchild(Child):
    pass
```

Observed on CPython 3.12:

| Class | Local `__slots__` | Shallow instance bytes |
| --- | --- | ---: |
| Base | store, ready, busy | 56 |
| Child | ready, busy again | 72 |
| Grandchild | ready, busy again | 88 |

The identically named descriptors are distinct. Normal lazy reads still return 3, but every empty generated inheritance level adds two unused shadow storage cells per inherited lazy field.

**Impact:** Deterministic storage growth and duplicate hidden descriptors contradict the stated reuse contract. No new stuck state or incorrect ordinary read was established, so this is P3 rather than a blocking semantic finding.

**Required correction:** Exclude already inherited ready/busy descriptors when forming local slots, while retaining generated initialization/access through the inherited names.

**Closure test:** Extend canonical inheritance source/layout coverage with an inherited lazy field and an empty generated subclass chain. Assert no repeated slots across the MRO and preserve retry, copy and provider-release behavior.

## 2. Invariant analysis

**Constructor and pipeline recovery.** A deliberately reordered provider/consumer declaration processed input conversion before passing its value to an eager consumer. Validator rejection installed no terminal value. A self factory retained a partially initialized object with earlier fields present, exactly as documented. Field installation atomicity held; arbitrary callback effects and escaped partial instances are not transactionally reversed.

**Lazy states and retention.** Cancellation cleared BUSY and permitted retry. Failed reads retained their provider. A seeded nonresettable consumer plus later successful terminal evaluation released the provider. Copy/deepcopy/pickle preserved unready/ready states and cyclic aliases without executing delayed factories. Active copying failed and busy cleanup completed. Direct retention, eager cuts and resettable lifetime are expressed in generation facts and canonical coverage; no runtime liveness table was introduced.

**Frozen/mutable behavior.** Inherited read-only lazy values rejected deletion. Writable excluded caches could be replaced and mutated without changing the tested hash. Dictionary policy copying and ordinary `init=False` class fallback preserved their distinct semantics. P3-1 concerns duplicate storage, not observed frozen/lazy value behavior.

**Prior native-comparison roots.** All three inherited design counterexamples were retraced through actual managed setters using custom working payloads:

- AcceptOriginal received the exact original inner list in both directions.
- Prepared dictionary and dict/proxy comparisons added no hash callbacks.
- Unequal tuples executed raising common-prefix callbacks in both directions; unequal lists retained native early length rejection.

Nested containers of distinct structurally equal child nodes recorded replacement under historical identity. A comparisons-disabled parent still entered the required scope.

**Fence and context lifetime.** Truth conversion ran inside the historical scope. Captured contexts returned to structural equality after closure. Explicit empty/copied thread contexts observed structural/historical behavior respectively; delayed tasks observed the expired marker. Cancellation restored the ContextVar. Same-manager reentry preserved the original token and callback depth; ownership loss during BaseException produced `HistoryFaultError` after marker closure. Source and existing controlled tests cover nested restoration, reflection/NotImplemented, in-flight sampling, hash/order and native cycles. P2-2 identifies a declaration-dependent failure before those normal prelude guarantees can operate.

**Views and history.** Default/working comparisons observed staged values while current/pinned comparisons observed committed revisions. Pins retained old values after publication; undo/redo restored the expected comparison outcomes. The transaction source diff changes only the value-comparison call and import; identity policy, operand acquisition, staging and existing fence remain otherwise unchanged.

**Evidence and performance limits.** Complete raw data reconcile; summaries do not discard unfavorable observations. Forty-seven threshold conclusions remain inconclusive. The frozen twelve-field hash boundary and environmental variability are not solved by test counts or near-one ordinary-slot estimates. Cold results describe first decoration after imports/setup, not interpreter startup. Memory measurements exclude class/shared-input costs and distinguish dictionary-inspection effects; tracing cleanup is in `finally`.

The declarative desk report explicitly excludes imperative callback/assembly seams from containment credit and retains its missing corpus/calibration/rater inputs. Four repaired public-author tasks are bounded usability observations, not an overall grade. Original GO, SDK detour, intervention, failed attempts and TDD deviations remain disclosed. API-equivalent cost observations remain separate from unavailable actual billing and unmeasured active-work time.

## 3. Risks and next action

The probes are bounded adversarial observations, not a replacement for the preserved installed matrix. External original raw archives were identified by manifests; this review directly verified repository derivatives, not separately fetched external originals. Concurrent first lazy access and concurrent manager operation remain outside the documented guarantees.

The single next action is bounded consumer remediation of P2-1, P2-2 and P3-1, followed by the specified regressions, regenerated consumer/artifact provenance and same-axis retrace on a new pinned tuple. Preserve the current measurements and failed counterexamples; assess only checks and benchmark families invalidated by the changes. No dependency expansion, publication or architecture/API redesign is required.