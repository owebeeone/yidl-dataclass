# YIDL Dataclass and shared Undoable comparisons — STATE-AXIS REVIEW

**Review object:** Corrected consumer implementation at Dataclass `4b8987299d591f13f7c6db61fd5826db8ee9f346` and Undoable `a689b98dce22f69dece2a2a48ac14472c55b67e2`. Remediation round 1; final acceptance pending.

**Baseline:** Original project baselines: Dataclass `d0cc37c061efb8b02bd126e547c01eb87baa904f`, Undoable `f79e4ce6d985ed0a6463552e163baabf1a28942d`. Correction comparison: Dataclass `f6c1c561c1670fc26b19da09537fc6822140d8d2`, Undoable `6e7edd17de5b30568f2ffa96dee24fa023dd3061`. Pinned checkout reads and `git diff` were used.

**Date:** 2026-10-13, Australia/Sydney.

**Axis:** State machines, recovery, retained authority, copying, native write-comparison semantics and evidence integrity. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on its current re-verdict. Filed verbatim by the lane owner.

**Verdict: GO** — State P2-1, P2-2 and P3-1 are closed. Zero open P0, P1, P2 or P3 findings were established in this focused correction review. This accepts the corrected functional/package tuple; it does not attribute historical H2 timings to the corrected bytes.

---

## 0. Evidence base

### Tuple and review boundary

The complete canonical `dev-docs/Dataclass-FinalPromptState-2.md` was read first. Both HEADs were verified at the start and end and remained exactly pinned.

Dataclass status contained only the two authorized untracked round-2 prompts. Undoable retained its excluded modified checkpoint and untracked UndoableLeaf document. No writes, builds, installations, regeneration, Git mutations or benchmark executions were performed. No current peer report was opened, requested or used.

The original State context and controlling requirements remain applicable. This round additionally read:

- Both original final reports, the complete `dev-docs/Dataclass-FinalRemPlan.md` and `Dataclass-FinalRemResult.md`.
- `docs/validation/final-rem1-drafter/README.md`, `qa.json`, `owned-manifest.json`, `package-rebuilds.json`, increments and sanitation records.
- `docs/validation/final-review-round1/owner_baseline_manifest.json`, corrected manifest, closure probe/wrapper, six closure results, dependency audit, drafter audit and historical-performance guard.
- The supported-route feasibility source, backend-leak/restoration evidence and relevant checkpoint updates.

Correction inspection covered:

| Owner | Locations |
| --- | --- |
| Dataclass | `src/yidl_dataclass/dataclass.py:208–241`; `dataclass_harvester.py:173–196`; complete correction diff for runtime source |
| Dataclass | `tests/test_result_namespace.py`; `tests/data/gold_src/dataclass_result_names.py`; expanded inheritance canonical and its support models |
| Dataclass | `tests/conftest.py:1–18`; frozen `tests/data/perf/test_gate_integrity.py:146–210`; backend-restoration assertion and failed/passing logs |
| Undoable | `src/yidl_undoable/comparison_captures.py:1–29`; `undoable.py:25–86,112–145`; `yidl/undoable_comparison.yidl:157–198` |
| Undoable | `tests/test_comparison_capture_names.py`; complete `tests/data/gold_src/24_comparison_capture_names.py` |
| Undoable | Correction diffs for `transaction_yidl.py`, `write_comparison_context.py`, `callbacks.py` and `facades.py`: no changes |

The authoritative neutral comparison resource, all nineteen frozen H2 sources, definition and committed raw performance data have no correction diff.

### Fresh installed probes

Original counterexamples were independently retraced using inline Python on CPython **3.12.12, 3.13.12 and 3.14.3**, each with separately selected **native-rust and Python** lowering:

```sh
PYTHONDONTWRITEBYTECODE=1 ASTICHI_LOWER_ENGINE=native-rust \
  <installed-env>/bin/python -I - <<'PY'
# Original counterexamples and bounded correction-risk probes.
PY
```

Python selection used the same command with `ASTICHI_LOWER_ENGINE=python`.

Every invocation checked the selected engine and absence of fallback, exact consumer/SDK versions, installed origins and Lark 1.3.1. All six original-counterexample retraces passed. They included:

- Dataclass `type`, `tuple`, `dict`, `int`, `hash` and `_y_dc_converter_0`.
- Shallow/deep copy, valid state restoration, module-level pickle, generated hash and preserved converter identity without generation-time callback execution.
- Empty Base→Child→Grandchild lazy inheritance with no repeated slots or basicsize growth.
- Undoable `_u_historical_write_scope` and `_u_historical_eq`, structural comparisons and actual equal-valued distinct-child replacement.

Additional alias-collision probes used `_u_capture_0` and its default/current/working association-name variants. They verified all three views, exact original capture objects and public names observed by metaclass/subclass hooks at creation.

Focused adverse probes on 3.12, under both explicit backends, also passed inherited cancellation/retry, seeded retention and release, unready copying, native original operands, cached dictionary hashes, tuple/list prefix behavior, distinct child identity, truth-conversion cancellation, nested scope expiry, same-manager reentrancy and ownership loss after BaseException.

### Artifact and evidence checks

The frozen wheels were read and hashed:

- Dataclass: `2c72e83f76dc8b81680d90f27602fb54fb0c4e7c7a5f826349dcfbfbb79cc9eb`.
- Undoable: `2974b01923a10acb60573c46bc3bd95b1bb8ec90198345b9162173bd327219cb`.

All installed package-inventory members matched the recorded artifacts. All **32 Dataclass** and **30 Undoable** Python/YIDL source payloads matched their repository source and wheel hashes. Existing sdist-rebuilt wheels were byte-identical to the frozen wheels; sdists and packaged public files also reconciled. This review read those artifacts rather than rebuilding them.

Original dependency wheel hashes and installed payload bytes were independently compared in every minor environment:

| Original dependency | Matching payload files per environment |
| --- | ---: |
| Astichi 1.1.3 | 85 |
| YIDL 0.1.0 | 39 |
| YIDL cache 0.1.0 | 8 |
| Lifecycle 0.1.0 | 21 |

The shared authority remains:

`2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef`

Independent read-only hash/XML accounting reconciled **222 owned files**, **93 increments**, **140 artifact references**, **123 distinct original raw-hash identities**, **47 JUnit files**, **16 sanitation steps**, and all **30 final source/installed gate records**. Each final gate had zero failures/errors. The recorded passing counts are:

| Corpus, each backend | 3.12 | 3.13 | 3.14 |
| --- | ---: | ---: | ---: |
| Dataclass source | 259 / 3 skips | 260 / 2 skips | 261 / 1 skip |
| Dataclass installed | 202 / 3 skips | 203 / 2 skips | 204 / 1 skip |
| Undoable source | 350 | 350 | 350 |
| Undoable installed | 349 | 349 | 349 |
| Undoable without Dataclass | 342 | 342 | 342 |

Installed exclusions and the two absent-authority deselections are explicitly recorded in the drafter README. Source-only builds, frozen benchmark mechanics and authority-dependent cases retain their separate coverage.

Two reviewer setup assumptions failed and were corrected without changing evidence: treating a top-level native extension as an `importlib.resources` package, and assuming each sanitized artifact had only one correction step. Distribution file lookup and ordered sanitation-chain traversal resolved those inspection errors. Their tracebacks remain in the review transcript; they are not product failures.

## Problem, requirement provenance, and scope

The authorized outcome remains a near-standard single generated Dataclass with direct ordinary slots, specialized field policies, hidden construction providers, safe lazy/copy behavior and reusable authored comparison generation actually integrated into Undoable. Correctness, inspectable goldens, installation, measurements and independent review are explicit deliverables.

The observed correction problems were concrete: Dataclass result bindings replaced runtime dependencies; Undoable builder-local class names shadowed historical comparison captures; inherited lazy flags allocated duplicate physical storage. These are localized defects in the authorized consumers.

The implemented remedies use existing consumer execution and YIDL reference facilities. Separating globals/results addresses Dataclass’s binding root directly. Disjoint aliases and an immutable original-object carrier address Undoable’s lexical root while preserving public creation names. Filtering inherited flags restores the existing storage contract.

The rejected fixed-internal-class-name approach is retained as feasibility evidence because hooks would observe the internal name before renaming. The selected route avoids that observable compatibility change. Neither a new class-name restriction nor SDK implementation was necessary or introduced.

Fresh environments restore normal declared dependencies after the prior missing-Lark observation. Original SDK/Lifecycle/cache payload comparisons establish that this was environment restoration, not dependency redesign or rebuilding.

The narrow backend-restoration fixture is within test/evidence scope. It targets only the exact frozen accounting mock that changes `ASTICHI_LOWER_ENGINE`; it restores the previous value in `finally`. The original late-validation, preserved-attempt and unpublished-final-result assertions remain unchanged. The retained failed sequence and passing restoration sequence demonstrate the distinction. It does not rewrite expected backend behavior or conceal product failure.

Reference-only dependencies, workspace configuration, publication and UndoableLeaf remain outside implementation scope. No unsupported prerequisite or unauthorized expansion was established.

H2 remains historical evidence for its original source/wheel tuple. Keeping those observations, unchanged thresholds and uncertainty is appropriate; assigning them to the corrected decoration/prelude paths would not be. No such final-byte claim appears in the correction result.

## Prior-finding closure

| Original State finding | Original counterexample retrace | Corrected mechanism and regression evidence | Status |
| --- | --- | --- | --- |
| **P2-1 — Dataclass output/capture naming** | All six original names now construct and complete copy/deepcopy/state/pickle; frozen `hash` returns the tuple hash; `_y_dc_converter_0` retains the original converter and executes no callback during generation. Independently passed all six minor/backend combinations. | `dataclass.py:213–220` executes with separate capture globals and result locals. No generated class output enters method globals. `tests/test_result_namespace.py` owns narrow capture recognition; `dataclass_result_names.py` owns protocol behavior. Genuine original failures and same-target passing evidence are retained. | **Closed** |
| **P2-2 — Undoable lexical naming** | Both original names now support ordinary structural comparison and actual distinct-child replacement. Alias-name collisions also pass across all six combinations; metaclass/subclass hooks observe the public names from creation. | `comparison_captures.py:17–29` allocates identifiers disjoint from all public model/view bindings. `undoable.py:117–130` installs one immutable carrier containing the exact original objects. Authored prelude/reset resources use direct carrier attributes. Narrow identity/closure tests and canonical story 24 cover names, views, hooks and disabled inheritance resets. | **Closed** |
| **P3-1 — inherited lazy shadow slots** | Empty Child and Grandchild now have `__slots__ == ()` and the base basicsize. Lazy access/reset and copy/pickle remain correct. Independently passed all six combinations; focused cancellation/provider tests also pass. | `dataclass_harvester.py:178–183` filters ready/busy names against inherited descriptors. Expanded canonical inheritance coverage includes an empty chain, same-shape override, failure/retry, active-copy rejection, reset, readonly behavior and ready/unready protocols. | **Closed** |

The prior Code report’s higher severity for the same inherited-slot root is respected by the merged plan. Its closure is established by the same physical-layout correction and regressions, not by downgrading severity.

No new finding was established.

## 2. Invariant analysis

**Capture integrity and public names.** Dataclass’s output binding no longer overwrites builtins or callbacks used by generated methods. Successful copy/state/hash behavior and exact converter identity defeat the original counterexamples. Separate result locals do not rename the class or change supported declaration names.

Undoable methods no longer close over the problematic model identifiers. Installed inspection confirmed that every carrier references the original ContextVar and `RuntimeFacade.__eq__`/`__hash__`; ordering resets retain the original object descriptors. Alias allocation is deterministic from the public model/view identifiers. Hook probes observed the expected public UserBase, model, current and working names, with no fixed internal-name exposure or new reservation.

**Inherited lazy recovery.** Descendants initialize and access the inherited flags directly. Cancellation clears BUSY; failure preserves the delayed provider; unready copy/deepcopy/pickle execute no factory; successful terminal evaluation releases the provider after the seeded companion is ready. Reset behavior and active-copy rejection remain covered by the expanded canonical. No duplicate descendant state descriptors or new stuck state was found.

**Native write semantics.** The native comparator, operand acquisition, `_call` fence and marker helper are unchanged. The carrier changes how the generated prelude obtains original objects, not the comparison expression or authority boundary.

Actual managed-write probes again preserved the original inner-list operands in both directions, added no dictionary hash callbacks, retained tuple prefix exceptions and list length rejection, and distinguished equal-valued child states by historical identity. No recursive comparator, payload reconstruction or unwrapping was introduced.

**Cleanup and ownership.** A nonboolean equality result whose truth conversion raises `KeyboardInterrupt` ran within historical scope, then left captured contexts closed and ordinary equality structural. Nested scopes restored the active outer marker; escaped inner contexts did not resurrect it. Same-manager reentry preserved the original transaction. Ownership loss after cancellation faulted the manager only after marker closure, with callback depth restored.

The original thread/task and in-flight-sampling limitations remain applicable. The exact ContextVar and lifetime helper are preserved; this correction introduces no stronger concurrency promise.

**Generation and artifact authority.** Authored YIDL still owns the comparison bodies and adapter prelude. Carrier reads use the existing direct external-reference route; there is no AST repair, runtime field-name dispatcher, SDK change or handwritten comparison replacement. The neutral shared resource remains unchanged and authoritative. Installed-without-Dataclass evidence preserves Undoable’s build-only authority boundary.

**Failure evidence and backend selection.** Genuine naming/layout REDs remain distinct from fixture-oracle repairs, launcher/import errors, source-only test selection failures and the accounting mock’s environment leak. Final XML arithmetic and hashes reconcile. The restoration fixture preserves the accounting test’s fail-closed result-publication assertions and restores the requested backend afterward. It does not turn setup failures into behavioral REDs.

**Performance and experiment truthfulness.** The previous full H2 audit remains applicable to its unchanged dataset: 73 threshold passes, 47 inconclusive conclusions and zero confirmed regressions. No exhaustive statistical recomputation was repeated in this focused round.

Dataclass execution setup and Undoable carrier/prelude paths changed. Their corrected bytes have no new timing result. Inherited lazy layouts were outside the original measured cases. Historical raw data, original artifact provenance and uncertainty remain explicit; no favorable rerun, target relaxation, final-wheel parity or universal speed claim follows from this GO.

Original GO timing, SDK detour, operator intervention, TDD deviations, partial attempts and unavailable actual billing remain preserved. Declarative desk calibration and containment limits remain unchanged.

## 3. Risks and next action

Residual limits are the documented callback side effects, shallow freezing/hash responsibility, unsupported concurrent first lazy access, private stdlib metadata coupling, incomplete declarative calibration and historical performance uncertainty. Narrow probes and recorded matrices do not establish universal correctness.

External raw originals remain identified by their content hashes; this review directly checked repository derivatives, sanitation chains and supplied physical consumer/dependency artifacts. It did not independently retrieve every external raw archive.

The next action is to record this State closure with the independent peer re-verdict and complete delivery of the corrected tuple, keeping functional/package acceptance separate from historical H2 measurements. No further State remediation, SDK expansion or architectural redesign is required.