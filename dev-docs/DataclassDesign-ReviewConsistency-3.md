# DataclassDesign — CONSISTENCY-AXIS REVIEW

**Review object:** `yidl-dataclass` README and `dev-docs/DataclassDesign.md` at `de7cadd25c1d3fd5deac0d978043284fa130da1c`. Proposed detailed design, dated 2026-10-12. No dataclass product implementation exists; this is a design verdict.

**Baseline:**

| Repository | HEAD |
| --- | --- |
| yidl-dataclass | `de7cadd25c1d3fd5deac0d978043284fa130da1c` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| astichi | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

The README was read cold using `git show HEAD:README.md`, before design or implementation inspection. Other sources were inspected with `cat`, `nl`, `sed` and `rg`; targeted `git diff HEAD -- PATHS` checks confirmed that inspected controlling documents and implementation surfaces matched committed bytes. All six HEADs matched the tuple at the beginning and end.

**Date:** 2026-10-12

**Axis:** Consistency against the controlling requirements graph, including internal coherence, implementable generation boundaries, inherited counterexamples and public Surface. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on its current report. Filed verbatim by the lane owner.

**Verdict: GO** — zero open findings. All three inherited Consistency findings are closed at the design gate. This accepts the reviewed design contract, not runtime implementation, release readiness or measured performance.

---

## Prior-finding closure table

| Original finding | Status | Independent retrace and closure evidence |
| --- | --- | --- |
| P2-1 — unconditional provider availability contradicts ordinary initializer suppression | **Closed at the design gate** | `dev-docs/DataclassDesign.md:278–318,419–430` resolves initializer action before availability checks. A custom initializer may establish an ordinary required `init=False` slot; suppressed initialization permits later assignment; generated initialization may leave an unconsumed ordinary field absent. Dictionary-mode simple defaults remain class fallbacks without instance writes. A generated factory consuming an unavailable provider still fails decoration. The original stdlib counterexamples were independently rerun. Lines 783–788 retain differential regression duties. |
| P3-1 — README says the detailed design remains unwritten | **Closed** | Cold reading of `README.md:11–15` reaches the proposed design and compatibility matrix directly. It identifies the redesigned boundary and pending fresh reviews, with TDD planning and implementation subsequent. This agrees with the checkpoint’s current next action. |
| P2-2 — `dict.get` adds key-hash callbacks that native dictionary equality avoids | **Closed at the design gate** | `dev-docs/DataclassDesign.md:542–562,627–635` replaces the manual lookup algorithm with exactly one native `bool(old == value)` over unchanged operands. No preliminary traversal, lookup or normalization remains. The original constant-hash/raising-hash counterexample was rerun: native equality added zero hashes; `.get` added one and raised. Lines 652,661–669,810–814 require actual managed-field integration and supported-minor regression evidence. |

Closure is based on the corrected contract and independent retracing, rather than accepting the remediation owner’s disposition. Runtime closure remains an implementation obligation.

## Changed-range analysis

The diff from `5d7883d8838fb9fa170426fbda59a71af3e9188b` to the reviewed object changes the README and these design areas:

- `:17–22` explicitly retires both rebuilt-container projection and manual paired traversal.
- `:455–459,480–485` adds the shared equality prelude surface, with an empty Dataclass selection and an Undoable-owned contribution.
- `:517–523` documents contextual historical equality as a public behavioral boundary.
- `:542–672` replaces the manual comparator with native equality inside a temporary ContextVar scope, defines prelude placement, cleanup, nesting, copied-context lifetime and the regression matrix.
- `:810–814,844–847` adds integration and performance obligations for the new boundary.
- `:880–893` distinguishes Python primitive observations from unexecuted generated integration.
- `README.md:13–15` updates the review status.

The inherited initializer correction remains intact.

**Architectural classification:** This is a component redesign of write comparison and its generation extension surface. It changes where historical behavior is selected and explicitly withdraws the earlier exception allowing opaque callbacks to observe structural facade equality during write detection. It does not alter the accepted one-class Dataclass architecture, direct ordinary slots or field-local policy model. No new architectural defect was established.

The merged remediation’s original-operand and unequal-length tuple counterexamples were also independently retraced. Native equality preserves the original nested list argument and the tuple’s prefix callback execution; it preserves the contrasting list length rejection. These conclusions do not rely on a current peer report.

## 0. Evidence base

Read the following in `yidl-dataclass`:

- `README.md:1–25`, cold first.
- `dev-docs/DataclassDesign.md:1–893`.
- `dev-docs/DataclassConcept.md`, including standard compatibility, single-class storage, reusable comparisons, write-policy preservation, field locality and factory/provider requirements.
- `dev-docs/ExperimentProtocol.md:1–121`.
- `dev-docs/GoldenExamplesAmendment.md`.
- `dev-docs/DeclarativeEvaluation.md`.
- `dev-docs/DataclassSpec-OperatorAmendment.md`.
- `dev-docs/CurrentProgramCheckpoint.md`, including both design rounds and the replacement-review boundary.
- Both prior Consistency design reports.
- Both merged design remediation plans.
- The complete canonical round-3 Consistency prompt.
- Relevant evaluator passages at `dev-docs/reference/DeclarativeApiEvaluatorV3.md:110–208,314–338,390–432`.

Read workspace `AGENTS.md`, `AGENTS_GWZ.md` and applicable member instructions. Targeted searches found no accessible `review-loop/SKILL.md` in the available skill directory or plugin cache; the complete canonical-generated reviewer prompt supplied the operative review/report contract. No current peer report was accessed, and no drafter, owner or peer was contacted for additional information.

Pinned implementation surfaces inspected:

| Repository | Evidence |
| --- | --- |
| yidl_undoable | `src/yidl_undoable/facades.py:1–205`, especially historical equality at `:153–157`; `transaction_yidl.py:475–635`; `callbacks.py:1–98`; marker exports, decorator/build path and harvester; `values.py:1–133`; `graph.py:1–50`; existing first-use and working-container examples |
| yidl | Active design/coding guidance; `src/yidl/concept_parser.py:217–320,1015–1134,3316–3397`; concept extension grammar; `src/yidl/generation/assembly_source.py:20–82`; split dataclass composition fixtures |
| astichi | Active summary/coding guidance; `src/astichi/lowering/external_ref.py:300–465` |
| yidl-lifecycle | Current documentation index; `src/yidl_lifecycle/lifecycle_markers.py:70–286`; regeneration entry point; `lifecycle_default_factories.yidl:1–220` |
| yidl-cache | Repository dependency and ownership boundaries; no cache integration is claimed or required by this initial design |

Primary Python references checked include the public [ContextVar API](https://docs.python.org/3.14/library/contextvars.html), [CPython dictionary equality](https://github.com/python/cpython/blob/3.12/Objects/dictobject.c), [tuple comparison](https://github.com/python/cpython/blob/3.12/Objects/tupleobject.c), and dataclass implementations for [3.12](https://github.com/python/cpython/blob/3.12/Lib/dataclasses.py), [3.13](https://github.com/python/cpython/blob/3.13/Lib/dataclasses.py) and [3.14](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py).

Read-only in-memory probes used CPython 3.12.12 with bytecode writing disabled:

```text
PYTHONDONTWRITEBYTECODE=1 yidl/.venv/bin/python -
```

They independently confirmed:

- All original ordinary initializer-suppression and dictionary class-default outcomes.
- Zero extra native equality hashes for the original opaque key, including rejection of later hashing.
- Zero extra hashes for distinct equal colliding keys and dict/proxy operand directions.
- Raising tuple prefix callbacks in both unequal-length operand directions, versus list rejection without invoking them.
- AcceptOriginal receiving the exact original inner list in both directions.
- Native identity shortcuts for identical nonreflexive elements.
- Native cyclic-container self equality and RecursionError for distinct recursive lists.
- ContextVar nested restoration, closed inner/outer copied markers, cleanup after Exception, BaseException and truth failure, explicit empty/copied thread contexts, and an async task observing a closed copied marker after teardown.

A separate in-memory probe imported the pinned historical Undoable implementation:

```text
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=astichi/src:yidl/src:yidl_undoable/src:yidl-lifecycle/src \
yidl/.venv/bin/python -
```

It confirmed that equal staged opaque-key dictionaries add zero hashes **inside the existing comparison callback** and retain the old staged reference. Direct calls to the pinned historical method confirmed cross-view state identity and False against a nonfacade.

An initial probe incorrectly asserted zero hashes across the whole assignment. Existing operand-acquisition projection hashes independently. The corrected probe measured the comparison callback, matching the prior finding’s boundary and the revised design’s explicit preservation of operand acquisition. That probe correction is not a product finding.

The context probes exercised Python primitives, not generated Undoable equality. No product builds, regeneration, mutation-bearing repository tests, file writes or Git mutations were performed.

## 2. Invariant analysis

### Native write comparison and historical facade behavior

The proposed prelude uses the exact pinned historical implementation:

```python
return isinstance(other, RuntimeFacade) and self._u_state is other._u_state
```

Its placement before self shortcuts, exact-class guards and structural reads matters. It restores same-state equality across default/current/working and pinned handles, preserves False when the facade method receives a nonfacade, and avoids structural field reads during write detection. Python retains rich-comparison dispatch and subclass priority. The design does not attempt to emulate those mechanisms.

Outside an active scope, enabled facade equality follows the specified structural view/type contract. Inside one, opaque callbacks that directly compare generated facades observe historical identity. That behavior is explicitly documented rather than left as an inconsistent exception.

The original dictionary defect is removed at its cause. Native equality receives both original dictionaries and performs its own cached-hash lookup. The design adds no `.get`, subscription, membership lookup or container rebuild. Native dictionary equality’s known-hash lookup is visible in the primary implementation. [CPython dictionary source](https://github.com/python/cpython/blob/3.12/Objects/dictobject.c)

Likewise, leaving the tuple expression native preserves prefix comparison before length resolution. The manual comparator’s shared length-first rule is gone. [CPython tuple source](https://github.com/python/cpython/blob/3.12/Objects/tupleobject.c)

Hash behavior never switches: enabled structural handles remain unhashable in every context. Ordering remains structural and receives no prelude. SnapshotNode behavior remains outside this generated boundary.

### Scope lifetime, ownership and retention

Each invocation owns a fresh marker with only `active`, while its token remains in the synchronous stack frame. Closing the marker before resetting the ContextVar prevents an escaped context or task from prolonging historical behavior. Inner reset restores the outer marker in the original context; a copied inner context retains its closed inner marker and does not resurrect the outer one.

Explicit empty contexts and live copied contexts have distinct, documented outcomes. The design also acknowledges in-flight concurrent sampling and does not promise an atomic cutover or new manager concurrency support. The set/reset and shallow-copy mechanism is compatible with the public ContextVar contract. [Python context documentation](https://docs.python.org/3.14/library/contextvars.html)

The entire scoped expression, including truth conversion and cleanup, remains inside the existing `_call` fence. The pinned callback implementation checks ownership after normal return and after BaseException, and blocks same-manager mutation through callback depth. Scope cleanup occurs before that fence completes. No manager, node, operand or parent chain is retained by copied scope markers.

Cycle behavior is also consistent: native equality keeps native outcomes, while existing acquisition, freeze and graph boundaries retain their own diagnostics. The revised contract no longer claims a uniform comparison-cycle exception.

### Reusable generation and dependency direction

The shared module owns method bodies and neutral operand/compatibility inputs. Undoable supplies its prelude; Dataclass selects an empty contribution and emits no context lookup, branch or import. Ordering and hash expose no contextual hook.

The pinned compiler supports logical source maps, relative imports, concept extension and inherited matcher rules. Astichi supports the prescribed restricted attribute paths. Nothing inspected requires consumer string formatting, fresh parsing or post-generation method repair.

Inherited defaults cannot be redefined directly in the pinned compiler. Consumer selection must therefore use the supported inherited matcher-rule mechanism rather than replacing the base default. The design’s consumer-matching contract is implementable that way; the future neutral composition/source checks must prove the actual wiring.

The new private context support remains Undoable-owned. The neutral comparison resource imports no transaction or dataclass machinery. Dataclass’s initial dependencies remain YIDL and Astichi; no requirement pulls Lifecycle, Undoable or live-value caching into its runtime boundary.

### Surface trace

The cold README accurately identifies a proposed product and leads to the detailed declarations. No runtime walkthrough is claimed.

The public surface has coherent names, placement and defaults:

- `dataclass` retains standard switches with explicit `slots=True` and `convert=False` differences.
- `field` provides field-local comparison/hash, tri-state mutability, conversion, validation and self-provider permission.
- `const`, `lazy`, `initvar`, `classvar` and `local_store` have explicit family restrictions and effective defaults.
- Standard inspection/data helpers remain standard exports; package replacement, storage inspection and generated-source inspection have stated extension contracts.
- Hidden InitVars, lazy materialization, copy/pickle state, frozen writable exceptions and unsupported combinations have explicit boundaries.

Undoable’s decorator defaults remain `eq=False, order=False`. Logical inclusion stays field-local and separate from managed `write_compare="value"`. Legacy string compare retains assignment policy and inclusion; explicit old/new conflicts fail. Excluded families reject inclusion, and declaration deletion removes its policy. Shared Lifecycle marker semantics remain unchanged.

The design resolves initialization suppression before availability validation, specifies dictionary fallback behavior, and retains actual unavailable-consumer diagnostics. Lazy retention, retry, copying, conversion-before-install and failed-setter preservation remain internally coherent.

### Evidence obligations and controlling graph

The proposed verification sections are satisfiable as future gates: independent stdlib differential evidence, canonical generated source/behavior, narrow failure coverage, installed-package resource checks, real Undoable integration and separately measured prelude/scope costs.

The requirements, operator amendment and checkpoint agree on accepted architecture, field locality, independent transaction policies and the remaining design/TDD gates. Historical status statements in requirements documents are identified as captured starting states, not current acceptance claims.

The redesign identifies the superseded comparator mechanisms and callback exception. It does not claim that runtime regressions or measurements have already passed, and it does not reuse historical Undoable results as Dataclass evidence.

## 3. Risks and next action

Generated prelude placement, matcher wiring, callback binding, three-minor metadata compatibility and installed-resource discovery still require implementation evidence. Context propagation is an observable part of the opted-in Undoable API and must appear in public documentation and the regression corpus. Performance remains unmeasured.

The next action implied by this verdict is to proceed to the separately reviewed TDD plan once the lane owner has both independent design verdicts. That plan must carry forward the original counterexamples and the complete Section 8 matrix; this GO does not waive them.
