# DataclassDesign — SAFETY-AXIS REVIEW

**Review object:** In `yidl-dataclass`, `dev-docs/DataclassDesign.md` and `README.md` at `de7cadd25c1d3fd5deac0d978043284fa130da1c`. Status: design proposed for independent review. No Dataclass product implementation exists.

**Baseline:**

| Repository | Exact HEAD |
| --- | --- |
| yidl-dataclass | `de7cadd25c1d3fd5deac0d978043284fa130da1c` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| astichi | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Committed evidence was read with `git show HEAD:PATH`; the requested design/README diff was inspected. All six HEADs matched the exact tuple at the beginning and end.

**Date:** 2026-10-12  
**Axis:** Safety — attack failure recovery, identity and callback boundaries, degraded behavior, retained authority and compatibility blast radius. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — zero open P0, P1, P2 or P3 findings. All three inherited Safety findings are closed at the design gate. This verdict accepts the specified mechanism and regression duties; it does not certify generated runtime behavior, manager integration, supported-version execution or performance.

---

## Prior-finding closure table

Locations in this table belong to `yidl-dataclass`.

| Prior finding | Design disposition | Independent retrace and closure evidence |
| --- | --- | --- |
| P2-1: recursive projection replaces operands delivered to opaque equality callbacks | **Closed; original counterexample retraced again** | `dev-docs/DataclassDesign.md:542–559`, `627–640` require native comparison of the original operands without rebuilding or inspecting containers. The original `(AcceptOriginal(inner),)` versus `(inner,)` case returned True in both directions in a read-only primitive probe; the callback received the exact original list. Lines 654 and 661–669 retain integration and declaration-matrix duties. |
| P2-2: dictionary `get` adds hashing absent from native dictionary equality | **Closed** | Lines 542–559 and 627–635 eliminate the manual lookup. The shared-key hash-counter and post-construction raising-hash counterexample completed with zero additional hashes through direct dict and all three dict/proxy directions. A separate collision probe produced identical native and scoped callback traces. Lines 652 and 661–669 require the broader key-exception and managed-working-value regressions. |
| P2-3: tuple length rejection suppresses native common-prefix callbacks | **Closed** | Lines 627–635 leave length and prefix ordering to the native expression. The original unequal-length tuple with a raising prefix comparator raised; the contrasting unequal-length list returned False without invoking that comparator. Lines 653 and 661–669 preserve true/false/raising/truth-conversion, reverse-direction and integration duties. |

Closure is a design retrace, not acceptance of unexecuted implementation tests. The remediation plans’ dispositions were checked against the revised decision procedure and independent observations.

## Changed-range analysis

The inspected range is `5d7883d8838fb9fa170426fbda59a71af3e9188b..de7cadd25c1d3fd5deac0d978043284fa130da1c`, restricted to `README.md` and `dev-docs/DataclassDesign.md`.

The revision changes:

- `README.md:11–15`: identifies the redesigned comparison boundary and fresh review gate.
- `dev-docs/DataclassDesign.md:17–22`: explicitly records replacement of both earlier comparison procedures.
- Lines 455–459 and 480–485: introduce the optional native YIDL `eq_prelude`; Dataclass selects an empty contribution, while Undoable binds its ContextVar and historical equality method.
- Lines 517–523 and 542–672: replace manual traversal with scoped native equality, define the contextual callback contract, and specify cleanup, nesting, copied contexts, thread/task behavior and regression obligations.
- Lines 810–814, 844–847 and 880–893: update public-documentation, integration, cost and evidence obligations.

**Architectural classification:** This is a component redesign of write comparison and an extension of shared comparison generation. It introduces a documented dynamic equality rule and therefore merits the replacement independent review specified by the checkpoint. No new architectural defect was established. The one-class Dataclass storage model, field-local policy separation and shared native YIDL method ownership remain intact.

The redesign removes the three earlier algorithmic roots: operand reconstruction, rehashing lookup and manually imposed container ordering. It does not retain them behind a fallback.

## 0. Evidence base

### Committed documents and source

In `yidl-dataclass`, I read:

- `dev-docs/DataclassDesign.md`, lines 1–893, with targeted numbered rereads of storage/failure/lifetime rules, initializer suppression, shared generation, the complete rewritten comparison boundary and verification obligations.
- `README.md`, lines 1–25.
- `dev-docs/DataclassConcept.md`.
- `dev-docs/ExperimentProtocol.md`.
- `dev-docs/GoldenExamplesAmendment.md`.
- `dev-docs/DeclarativeEvaluation.md`.
- `dev-docs/DataclassSpec-OperatorAmendment.md`.
- `dev-docs/CurrentProgramCheckpoint.md`.
- Both prior Safety design reports and both merged design remediation plans.
- The canonical `dev-docs/DataclassDesign-PromptSafety-3.md`.

Pinned reference inspection included:

- `yidl_undoable`: `src/yidl_undoable/facades.py:1–328`, particularly historical equality/hash at 153–157; `transaction_yidl.py:480–670`, particularly operand acquisition and write comparison at 597–616; `callbacks.py:1–98`; `undoable_harvester.py:1–132`; and `values.py:1–133`.
- `yidl`: `src/yidl/concept_parser.py:185–305`, `1015–1158` and `3316–3397`; the split Dataclass composition fixture and selected default/empty-contribution and inherited-matcher definitions; active design and coding-rule documents.
- `yidl-lifecycle`: `src/yidl_lifecycle/regenerate_lifecycle_base.py:1–103` and `yidl/lifecycle_core.yidl:1–155`; member documentation instructions.
- `astichi`: the active single-source summary and coding rules, plus `docs/reference/marker-ref.md:1–115`.

Root `AGENTS.md`, `AGENTS_GWZ.md`, the supplied control-flow instructions and applicable member instructions were read. No separately accessible `review-loop/SKILL.md` was found in the searched workspace, skill or plugin locations. The complete canonical-generated reviewer prompt supplied the operative review and report contract.

Official documentation was checked for ContextVar set/reset, shallow context copies and module-level ownership; thread context inheritance; and task context copying/eager execution. These support the public primitives used by the design. [Context variables](https://docs.python.org/3.14/library/contextvars.html), [Thread context behavior](https://docs.python.org/3.14/library/threading.html#threading.Thread), [Asyncio tasks](https://docs.python.org/3.12/library/asyncio-task.html#asyncio.Task)

### Read-only probes

Two in-memory probes ran on CPython **3.12.12**, with `PYTHONDONTWRITEBYTECODE=1`. They modeled the exact scope sequence and prelude with small support classes:

```python
marker = Scope(active=True)
token = scope.set(marker)
try:
    return bool(old == value)
finally:
    marker.active = False
    scope.reset(token)
```

The modeled generated prelude read the ContextVar, returned the historical RuntimeFacade method when its marker was active, and otherwise entered structural equality. The historical method reproduced the pinned implementation’s `isinstance(other, RuntimeFacade) and self._u_state is other._u_state`.

Observed results:

| Attack | Observation |
| --- | --- |
| Original AcceptOriginal case, both directions | True; exact original list received |
| Distinct equal-valued facade states | Structural True outside scope; historical False inside |
| Same-state handles in different views | Historical True |
| Facade slot against nonfacade | Historical False |
| Shared dictionary key refusing later hashing, direct/proxy directions | Comparison succeeded; zero additional hash calls |
| Distinct equal collision keys | Scoped and native callback traces identical |
| Original unequal-length tuple bomb | Prefix callback raised |
| Contrasting unequal-length list | Early False; prefix callback not invoked |
| Nested scope and inner-context escape | Outer restored in original context; escaped inner copy stayed closed |
| Explicit empty/copied thread contexts during active scope | Structural/historical respectively |
| Copied thread context run after closure | Structural |
| Equality error, truth error and KeyboardInterrupt | Context restored; captured marker closed |
| Ordinary async task captured during scope | Closed marker and structural behavior when subsequently run |
| Eager task | Historical before suspension while active; structural after closure |
| Reflected strict-subclass comparator returning observable truth object | Right comparator first; one truth conversion |
| Hash/order | No hash-mode switch; ordering retained its structural path |
| Native cyclic lists | Identity comparison succeeded; distinct recursive lists raised RecursionError; scope restored |

Additional stdlib probes independently retraced the initializer corrections: custom initialization assigned 7; suppressed and source-free ordinary fields remained absent until assignment; dictionary `init=False` simple defaults left the instance dictionary empty and followed a later class-default change from 3 to 9.

These are observations of Python primitives and a handwritten model of the specified boundary. No generated Dataclass/Undoable comparison, real manager integration, build, regeneration, installed-package test or benchmark was executed.

Commands were inspection-only: `git rev-parse`, `git show`, the restricted `git diff`, `rg`, `cat`, numbered source reads and the permitted in-memory probes. No files or Git state were changed. No drafter, owner-for-details or current peer reviewer was contacted; no current peer report was accessed.

## 2. Invariant analysis

**Original operands and native callback demand.** The revised operation is the same native expression used by pinned `_write_managed`, with original operand acquisition left in place. The scope contributes no normalization, hashing, traversal or operand replacement. Dictionary lookup internals, collision order, tuple/list prefix differences, proxy forwarding, subclass dispatch and truth conversion remain Python’s responsibility. The original three counterexamples therefore no longer encounter the operations that caused their failures.

**Historical identity precedes structural behavior.** Pinned `RuntimeFacade.__eq__` uses NodeState identity and returns False against nonfacades. The prelude precedes both the self shortcut and exact-class guard, so same-state cross-view handles retain the historical result and distinct equal-valued nodes remain unequal during write detection. It bypasses structural getters entirely. Native reflected dispatch still chooses the method; user-owned subclass methods are preserved.

**Opaque callback authority is explicit.** The design withdraws the earlier exception allowing opaque callbacks to observe structural equality internally during value-write detection. Generated facade equality called from those callbacks now follows historical identity throughout the active context, including other generated Undoable models. This is the baseline behavior the compatibility adapter needs to preserve. The wider contextual effect is documented at lines 517–523 and 593–602, rather than hidden behind a claim of invisible equivalence.

**Scope cleanup and ownership recovery.** Scope setup, native equality, result truth conversion and teardown remain inside the existing manager `_call` fence. That fence captures operation ownership, rejects same-manager mutation through callback depth, checks ownership after successful callbacks, and faults on ownership loss after failure. Closing and resetting the comparison marker does not replace or relax these checks. Marker teardown precedes `_call`’s post-callback ownership decision, so an ownership fault cannot leave this scope intentionally active.

**Nested and escaped contexts.** Fresh markers and stack-held tokens prevent an inner invocation from closing its outer marker. Reset restores the outer marker only in the original setting context. Copies share the captured marker object; closing it before reset makes later checks in escaped copies structural. A copy captured at inner depth has no parent-marker chain capable of resurrecting the outer scope. The primitive probes confirmed these distinctions.

**Thread/task boundaries.** Explicit empty contexts are structural; explicitly copied contexts can observe an active historical scope. A synchronous function need not await for task execution to occur: eager task execution can run immediately, and the design’s before/after-closure contract handles that case. Closing a shared marker invalidates later checks in captured contexts. An invocation that already sampled an active marker may finish afterward; lines 621–624 explicitly disclaim atomic cutover and new manager concurrency guarantees. No stronger safety promise was inferred.

**Retention and mutation blast radius.** The marker contains only `active`; tokens remain on synchronous stack frames. Copies can retain closed markers but gain no manager, node, operands or parent chain through this mechanism. No global registry or class mutation is proposed. Private scope state is not advertised as a security boundary against deliberate manipulation of internals.

**Hashing, ordering and cycles.** Enabled facade classes remain unhashable in every context. Ordering has no context branch. These explicit restrictions prevent identity equality from being paired with a temporary hash switch. Native equality retains its own cyclic outcomes; read/projection/freeze/graph diagnostics remain at their existing boundaries. The design no longer promises one new uniform comparison-cycle diagnostic.

**Generation feasibility and isolation.** Pinned YIDL supports inherited contribution matchers, defaults and consumer-specific rules, while Astichi supports precompiled statement contributions and external identifier/path binding. The empty default plus an Undoable-specific matched contribution is expressible without replacing emitted methods or modifying compiler semantics. Implementation must use those additive matcher capabilities rather than attempting to redefine an inherited default. Dataclass selects the empty contribution and is expressly required to emit no context import, lookup or branch.

**Initializer and unchanged failure rules.** Suppression precedes source availability checks; an unused source-free ordinary field can remain absent, while an actual generated consumer still requires its provider. Dictionary class fallback remains a read without an instance write. Pipeline installation follows successful conversion/validation; lazy busy state clears in finally; failed lazy evaluation retains required providers; resettable consumers retain providers for their lifetime. Copy/pickle reject active lazy evaluation and preserve readiness/absence explicitly. No weakened safety boundary was established in these unchanged clauses.

**Evidence discipline.** The revised reference-inspection section labels primitive observations separately from generated runtime proof. The design requires supported-minor integration tests, public documentation of contextual equality, packaged composition checks and separate Undoable overhead measurements. It makes no executed compatibility or speedup claim that these probes could substantiate.

## 3. Risks and next action

Residual implementation risks are correct native YIDL contribution selection, stable external binding of the historical method and ContextVar, complete manager-fence integration, and faithful cleanup across the supported interpreter matrix. They remain explicit regression obligations, not additional design defects.

The single next action is to record both independent design verdicts and proceed to the separately reviewed TDD plan. That plan must preserve the inherited counterexamples and Section 8’s context/ownership matrix before implementation begins.
