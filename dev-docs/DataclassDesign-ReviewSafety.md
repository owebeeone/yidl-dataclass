# DataclassDesign — SAFETY-AXIS REVIEW

**Review object:** `yidl-dataclass/dev-docs/DataclassDesign.md` at `9fd44d91943ca706c4c51a0669bd3e9d03260278`, status “design proposed for independent review,” dated 2026-10-12. This review assesses the implementation-ready design and its controlling requirements; no Dataclass implementation exists.

**Baseline:**

| Repository | Exact HEAD |
| --- | --- |
| yidl-dataclass | `9fd44d91943ca706c4c51a0669bd3e9d03260278` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| astichi | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Committed evidence was read with `git show SHA:PATH`, supplemented by targeted source searches. All six heads matched at the beginning and end.

**Date:** 2026-10-12  
**Axis:** Safety — attack failure recovery, retained state, identity boundaries, degraded paths and compatibility blast radius. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — one P2 finding blocks. Its root cause is bounded to the proposed Undoable write-detection adapter; no architectural root cause was established. I pre-commit to GO on a revision that resolves P2-1 as specified.

---

## 0. Evidence base

The following controlling documents were read at Dataclass SHA `9fd44d91943ca706c4c51a0669bd3e9d03260278`:

- `dev-docs/DataclassDesign.md`, lines 1–679, especially storage/pipeline/failure rules at 190–253, lazy lifetime at 255–317, inheritance/hash at 319–380, reusable generation at 382–430, Undoable integration at 432–505, and verification/evidence obligations at 583–663.
- `README.md`, lines 1–23.
- `dev-docs/CurrentProgramCheckpoint.md`, lines 1–90.
- `dev-docs/DataclassConcept.md`, lines 1–258.
- `dev-docs/ExperimentProtocol.md`, lines 1–121.
- `dev-docs/GoldenExamplesAmendment.md`, lines 1–38.
- `dev-docs/DeclarativeEvaluation.md`, lines 1–37.
- `dev-docs/DataclassSpec-OperatorAmendment.md`, lines 1–31.
- `dev-docs/reference/DeclarativeApiEvaluatorV3.md`, lines 1–355 and 405–463, covering declared evidence modes, locality, correctness, seams, oracle independence and authoring measurements.

Reference-source inspection included:

- Undoable at `f79e4ce6d985ed0a6463552e163baabf1a28942d`: `src/yidl_undoable/facades.py`, lines 1–328; `undoable_harvester.py`, lines 1–132; `undoable_markers.py`, lines 1–33; `values.py`, lines 1–133; `graph.py`, lines 1–50; `candidates.py`, lines 1–8; `transaction_yidl.py`, lines 126–163, 506–616 and 643–666; callback ownership/mutation guards in `callbacks.py`.
- Lifecycle at `230362f642d6e9205897698670fe5f87d2c905ce`: `src/yidl_lifecycle/regenerate_lifecycle_base.py`, lines 1–103, and `yidl/lifecycle_core.yidl`, lines 1–155.
- YIDL at `9d374f88445c426a56d5dd1f96fad112d1ec5417`: `src/yidl/concept_parser.py`, lines 185–300; `tests/data/yidl/yidl_update_a_dataclasses_split/dataclasses_combined.yidl`, lines 1–13; relevant generation and binding searches; the active design summary and coding rules.
- Astichi at `1c47f781d3804130fdd61cbee07a3b2e4529158a`: `docs/reference/marker-ref.md`, lines 1–110; `dev-docs/AstichiSingleSourceSummary.md`, especially lines 210–410; `dev-docs/AstichiCodingRules.md`, lines 1–263.

Root `AGENTS.md`, `AGENTS_GWZ.md`, relevant member instructions and the review-loop skill were read. No files were changed, no builds or mutation-bearing tests were run, and no drafter or other reviewer was contacted.

`git -C MEMBER rev-parse HEAD` and `git -C MEMBER status --short` were checked at both boundaries. Dataclass, Astichi and Cache were clean. The named neighboring Undoable, Lifecycle and YIDL documentation drafts remained outside scope; their status listings were unchanged.

A read-only in-memory probe reproduced P2-1 on CPython 3.12.12. An earlier exploratory run also reproduced it on 3.11.16; that run is not evidence of supported-version compatibility. The exact 3.12 command, run from the installed interpreter’s `bin` directory, appears below. It models the specified projection operation, not an existing Dataclass implementation.

## 1. Findings

### [P2-1] Recursive projection changes operands delivered to opaque equality callbacks

**Location.** `yidl-dataclass/dev-docs/DataclassDesign.md` at `9fd44d91943ca706c4c51a0669bd3e9d03260278`, lines 470–482, specifically projecting facade leaves before native container equality while retaining ordinary noncontainer equality callbacks.

**Violated invariant.** The adapter must preserve existing value-write behavior except for preventing logical facade equality from confusing node identity. The controlling concept at the same SHA, `dev-docs/DataclassConcept.md`, lines 127–132, requires preservation of transaction assignment policies. The design itself promises that ordinary noncontainer leaves retain existing equality callbacks.

Retaining the callback object is insufficient: rebuilding its opposite operand changes the callback’s inputs.

**Counterexample.** Let an opaque leaf accept one specific native list by identity. Its equality callback neither reads facade fields nor invokes facade equality:

```python
class AcceptOriginal:
    def __init__(self, expected):
        self.expected = expected

    def __eq__(self, other):
        if other is not self.expected:
            raise RuntimeError("comparison operand was replaced")
        return True
```

Create `inner = [child_facade]`, `old = (AcceptOriginal(inner),)` and `value = (inner,)`.

1. Native `old == value` calls the opaque leaf with the original `inner` list and returns `True`.
2. Under the specified projection, `old` retains its opaque leaf. `value` becomes a tuple containing a newly built list whose facade element is an identity token.
3. Native equality of the projected tuples calls the same leaf with that replacement list.
4. The callback raises. The memo cannot fix this: it preserves sharing among projected objects, but the unchanged opaque leaf still refers to the original list.

The design’s exception for user equality that invokes facade equality does not cover this callback.

Exact probe:

```sh
PYTHONDONTWRITEBYTECODE=1 ./python3.12 - <<'PY'
import sys
from dataclasses import dataclass
print(sys.version.split()[0])
@dataclass(frozen=True)
class IdentityToken:
    manager_id: int
    node_id: int
class Handle:
    pass
class AcceptOriginal:
    def __init__(self, expected):
        self.expected = expected
    def __eq__(self, other):
        if other is not self.expected:
            raise RuntimeError('comparison operand was replaced')
        return True
handle = Handle()
inner = [handle]
old = (AcceptOriginal(inner),)
value = (inner,)
print('native equality:', old == value)
projected_old = (old[0],)
projected_value = ([IdentityToken(1, 1)],)
try:
    print('projected equality:', projected_old == projected_value)
except RuntimeError as exc:
    print(type(exc).__name__ + ': ' + str(exc))
PY
```

Observed:

```text
3.12.12
native equality: True
RuntimeError: comparison operand was replaced
```

`Handle` isolates the substitution effect; it need not implement equality. Replacing it with a RuntimeFacade triggers precisely the projection required by the design.

This is reachable in Undoable’s existing extension surface. A managed field with a custom freeze callback can have an opaque working value. Stage `old` first, then assign `value` in the same edit. The pinned implementation reads staged values through `transaction_yidl.py:525–534`, preserves opaque leaves through `values.py:92–93`, and compares `old == value` at `transaction_yidl.py:607–616`. Custom freezing provides the stable candidate representation at commit. No model mutation inside the equality callback is needed.

**Impact.** A previously successful assignment can raise or make a different write/no-write decision. The adapter applies to value-write detection generally, so this can affect models with structural generation disabled and legacy managed declarations. The damage is broader than the newly enabled facade comparison surface.

**Required correction.** Replace whole-value projection followed by native equality with a specified comparison procedure that preserves original operands at opaque boundaries. A bounded solution is paired traversal of supported native container shapes, using manager/node identity when comparing two RuntimeFacade leaves and preserving native identity shortcuts, while delegating opaque comparisons using their original operands and Python’s dispatch rules. Keep the existing callback ownership fence and cycle diagnostics. Do not broaden traversal into arbitrary user objects.

**Classification.** Bounded semantic defect in the Undoable-owned write-detection boundary. It does not require changing Dataclass storage architecture or the shared YIDL comparison productions.

**Closure and regression.** The revised design must state a decision procedure that produces `True` for this counterexample and passes the original `inner` object to the callback. Add a narrow adapter regression and an Undoable integration regression using custom freeze/working values. Cover legacy and new value-policy spellings, structural generation enabled and disabled, and both callback operand directions. Retain the existing obligations proving that distinct equal-valued child nodes record replacements, same-node views preserve identity write semantics, native nested containers work, and cyclic containers diagnose.

## 2. Invariant analysis

The following attacks did not establish additional defects. These are design-level conclusions, not claims of executed implementation coverage.

**Pipeline failure and partial construction.** Installation follows conversion and validation, so a failing setter need not replace the previous value. Invalid validator returns have a separate contract diagnostic. Callback exceptions retain causes, and cancellation is not relabelled. Construction explicitly disclaims rollback of callback side effects and leaked self-providers. The callback prohibition on model mutation/reentry prevents treating such behavior as promised setter atomicity.

**Lazy retry, recursion and release.** Busy flags are initialized before evaluation and cleared in `finally`; readiness follows successful installation. A failed dependent getter leaves successful prerequisite caches intact. Retention follows direct lazy consumers, stops at eager public values, and remains lifelong when a consumer can reset. Consequently, resetting a mutable dependent lazy field does not require released prerequisites of an already cached read-only intermediate field. Concurrent first access is explicitly unsupported and diagnosed.

**Copy, pickle and read-only restoration.** The design preserves absent and ready states without running factories, uses deepcopy memoization, encodes pickle readiness separately from sentinel identity, and rejects copying during active evaluation. Internal restoration bypasses public rejecting setters deliberately. Private backing storage is explicitly outside the immutability/security boundary; that escape is not advertised as secure freezing.

**Inheritance and frozen hash consistency.** Same-shape overrides reuse inherited slots and revalidate the graph. Mutability and storage-family changes are rejected. Writable frozen exceptions must be excluded from equality and hashing, and `hash=True, compare=False` is rejected. Mutable contents and callback-derived hash stability remain explicit user responsibilities, consistent with shallow freezing.

**Facade views, pins and membership.** Exact generated-class guards prevent logical comparison across default/current/working views. Enabled facades are unhashable, including pins; hash-container failures are explicitly accepted rather than bypassed with identity hashes. No atomic history snapshot is promised. The inspected membership and graph paths use node IDs and manager/state identity: `transaction_yidl.py:141–160`, `643–654`, `values.py:18–25`, and `graph.py:12–17`. Candidate reads decode node references; the proposed logical comparison does not require using facade equality for membership.

**Legacy declaration separation.** Logical inclusion and transaction write policy occupy separate wrapper facts. Legacy strings preserve their write policy, explicit old/new conflicts reject, and excluded families remain excluded. The interface prevents the earlier compare-option collision. P2-1 concerns the new execution adapter rather than this metadata separation.

**Generation and portability.** Astichi’s documented external reference binding supports validated structural attribute paths. YIDL accepts an in-memory source map and resolves imported logical paths, supporting the proposed packaged shared-resource scheme. Precompiled resources, external runtime bindings and per-decoration composition avoid executable callback repr text and cross-class binding reuse. Wheel/sdist installation and provenance remain explicit future gates.

**Evidence claims.** The design makes no speedup or measured-correctness claim. It separates decoration from instance benchmarks, requires repeated independent processes and raw observations, distinguishes designer goldens from differential evidence, and keeps unavailable telemetry and authoring measurements unscored. The separately reviewed TDD plan must still fix thresholds and turn these gates into observable checks.

## 3. Risks and next action

The principal residual implementation risks are private stdlib metadata adapters across three Python minors, closure preservation during class replacement, faithful Python equality dispatch in the corrected write detector, and generated copy/liveness code. They have explicit verification obligations; their difficulty alone is not an additional finding.

The next action is to revise the write-detection contract and its regression obligations for P2-1, then obtain the required design re-review before starting the separate TDD plan or implementation.