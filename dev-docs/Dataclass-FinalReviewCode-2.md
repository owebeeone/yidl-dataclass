# YIDL Dataclass + Undoable comparison integration — CODE-AXIS REVIEW

**Review object:** Remediation round 1 at Dataclass `4b8987299d591f13f7c6db61fd5826db8ee9f346` and Undoable `a689b98dce22f69dece2a2a48ac14472c55b67e2`. Implemented consumer source/resources, public documentation, tests, corrected distributions and remediation evidence.

**Baseline:** Original experiment baselines remain Dataclass `d0cc37c061efb8b02bd126e547c01eb87baa904f` and Undoable `f79e4ce6d985ed0a6463552e163baabf1a28942d`. Focused remediation diffs were inspected against the previous review tuple: Dataclass `f6c1c561c1670fc26b19da09537fc6822140d8d2` and Undoable `6e7edd17de5b30568f2ffa96dee24fa023dd3061`. Tracked files were read after verifying HEAD.

**Date:** 2026-10-13 Australia/Sydney; completed 2026-10-12T18:37:00Z.

**Axis:** Code and Surface — focused prior-finding closure, capture ownership, supported names, inheritance/storage compatibility, scope and corrected installation evidence. Independent, adversarial, read-only. The current other-axis report was not read or requested; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — both original Code findings are closed; zero open P0/P1/P2 findings and no new finding established. This accepts the corrected functional/package object, not numerical performance of its final bytes.

---

## 0. Evidence base

Paths below are relative to their named owning repository. Interpreter and archive locations use external placeholders.

### Tuple and review boundary

`git rev-parse HEAD` and `git status --short` verified the exact tuple at start and end. Dataclass retained only the two authorized untracked round-2 prompt files. Undoable retained its excluded checkpoint modification and untracked UndoableLeaf document. Neither HEAD moved.

The complete `dev-docs/Dataclass-FinalPromptCode-2.md` was read first. Legitimate prior-round inputs included both original review reports, `Dataclass-FinalRemPlan.md`, `Dataclass-FinalRemResult.md` and `docs/validation/final-rem1-drafter/README.md`. The original cold public-author prerequisite remains preserved; it was neither repeated nor reclassified as implementation acceptance.

No file writes, builds, installations, regeneration, Git mutations, full-suite executions or benchmark executions were performed.

### Changed mechanisms inspected

Dataclass:

- `src/yidl_dataclass/dataclass.py:210–228`: separate capture globals/output locals and unchanged dictionary-mode identity.
- `dataclass_harvester.py:173–194`: inherited value, lazy-flag and provider-slot filtering.
- `docs/API.md:15–25` and `examples/first_use.py`: corrected class-identity documentation and both identity assertions.
- `tests/data/gold_src/dataclass_inheritance_helpers.py` and `tests/support/inherited_lazy_models.py`: inherited chain/override, retry/reset, readonly and ready/unready protocols.
- `tests/test_result_namespace.py`, result-name canonical and support models: original builtin/callback collisions.
- `tests/conftest.py` and the unchanged frozen accounting test: narrowly scoped backend restoration.

Undoable:

- `src/yidl_undoable/comparison_captures.py:1–29`: immutable original-object carrier and disjoint association identifiers.
- `undoable.py:25–82,112–144`: association wiring, public creation names and capture installation.
- `yidl/undoable_comparison.yidl:157–187`: direct authored carrier references for prelude and disabled-method resets.
- Capture-recognition tests and `tests/data/gold_src/24_comparison_capture_names.py`: original names, alias collisions, creation hooks, views, writes and disabled inheritance.

Diff checks confirmed no changes to the neutral comparison authority, native write-comparison helper, managed-write call site, facade implementation or callback fence. The Dataclass correction requires no authored-resource change or consumer AST repair.

### Executed installed retraces

Narrow inline probes ran in all six fresh installed combinations:

```sh
env PYTHONDONTWRITEBYTECODE=1 ASTICHI_LOWER_ENGINE=<native-rust-or-python> \
  <installed-env>/bin/python -I -
```

Every run confirmed:

- CPython 3.12.12, 3.13.12 or 3.14.3.
- Original Astichi 1.1.3, YIDL/cache/Lifecycle 0.1.0 and intact Lark 1.3.1.
- Requested backend, `fallback_scope=None` and package origins beneath the installed prefix.
- Byte equality with the original dependency wheel payloads: Astichi 85 files, YIDL 39, cache 8 and Lifecycle 21 per environment.
- Original Code counterexamples passing.
- Dataclass builtin/callback-name copy, deepcopy, state, pickle and hash cases passing without generation callback execution.
- Original Undoable naming failures and four capture-alias boundary names passing structural comparison, actual distinct-child replacement and disabled-method restoration.
- Packaged identity wording corrected.
- Shared authority digest unchanged and no maintained Undoable copy.

An additional narrow CPython 3.12/native probe verified inherited lazy base/child/grandchild/override retry, reset, readonly rejection and ready/unready copy/deepcopy/pickle. It also independently verified unchanged public metaclass/subclass-hook names, exact original capture objects and structural equality in an escaped context after historical-marker closure.

The previous live CLI import limitation no longer reproduces. Both regeneration entry points successfully displayed `--help` in the fresh environment; no regeneration was performed.

### Artifact and recorded-gate audit

Independent read-only checks verified:

- Corrected wheel SHA256:
  - Dataclass: `2c72e83f76dc8b81680d90f27602fb54fb0c4e7c7a5f826349dcfbfbb79cc9eb`.
  - Undoable: `2974b01923a10acb60573c46bc3bd95b1bb8ec90198345b9162173bd327219cb`.
- Existing sdist-rebuilt wheels byte-identical to those frozen wheels.
- All 32 Dataclass and 30 Undoable installed Python/YIDL payloads matching the reviewed sources.
- Packaged README/API/example bytes matching source.
- All 222 owned-file hashes.
- All 93 increment records, 140 artifact references, 123 distinct original raw hashes and 47 JUnit files.
- All 16 explicit sanitation transitions, including archived intermediate derivatives.
- All 30 final source/installed/no-authority XML gate counts.
- Thirteen owner closure/audit manifest hashes.

Audit setup attempts initially mishandled a relative owning root, an external archive placeholder, repeated sanitation transitions and a summary count mistaken for a hash map. These read-only assumptions were corrected; no evidence was modified and no audit failure was attributed to the product.

Recorded final gates, on each backend:

| Corpus | 3.12 | 3.13 | 3.14 |
| --- | --- | --- | --- |
| Dataclass source | 259 pass / 3 skip | 260 pass / 2 skip | 261 pass / 1 skip |
| Dataclass installed | 202 pass / 3 skip | 203 pass / 2 skip | 204 pass / 1 skip |
| Undoable source | 350 pass | 350 pass | 350 pass |
| Undoable installed | 349 pass | 349 pass | 349 pass |
| Undoable without Dataclass | 342 pass / 2 deselected | 342 pass / 2 deselected | 342 pass / 2 deselected |

Installed Dataclass excludes 55 frozen benchmark-mechanics tests and two source/distribution tests, which remain covered by its source suite. Installed Undoable excludes its source distribution test. The no-authority corpus additionally excludes generation-authority tests and the two documented authoring-layer/cross-consumer cases. These exclusions are explicit, not claims of exhaustive installed regeneration without authority.

## Problem, requirement provenance, and scope

The authorized outcome remains the original single-class Dataclass consumer and requested Undoable comparison integration, including direct ordinary storage, specialized policy behavior, metadata/helpers, real shared comparison generation and independently recorded evidence.

The remediation addresses three concrete roots: inherited lazy-slot duplication, Dataclass output/capture interference and Undoable lexical capture collisions. The public identity wording is corrected without changing its accepted implementation.

The remedies stay inside authorized consumer source/resources/tests/docs/evidence. Original SDK/Lifecycle/cache payloads remain unchanged. There is no new class-name reservation, dependency capability, runtime field dispatcher, comparator redesign, publication or workspace change.

The earlier SDK detour remains historical and excluded. Existing composition facilities support the corrected route. Fresh environments restore ordinary declared dependencies for verification; they do not repair or rebuild dependency source. The cause of the previous Lark deletion remains unknown, and no broader infrastructure mandate is inferred.

The test fixture corrects an observed environment leak from one immutable accounting mock. It neither suppresses that test nor changes its failed-validation/journal assertions. Restoring the requested backend is necessary for valid subsequent Python-backend verification; it is not a substitute for repairing product failures.

No unauthorized expansion or unsupported prerequisite was established.

## 2. Invariant analysis

### Prior Code findings

| Original finding | Original counterexample retrace | Corrected mechanism | Regression evidence | Status |
| --- | --- | --- | --- | --- |
| **P2-1 — inherited lazy flag slots redeclared** | Base/child/grandchild now have equal basicsizes; empty descendants have `__slots__ == ()`; lazy reads still succeed. Passed all six installed selections. | `dataclass_harvester.py:183` excludes already inherited readiness/busy names, consistently with value/provider slots. | Extended canonical inheritance scenario covers empty chain, same-shape override, retry, active-copy rejection, reset, readonly behavior and ready/unready protocols. Additional independent installed protocol probe passed. | **Closed** |
| **P3-1 — unconditional replacement wording** | `slots=True` returns a different class; `slots=False` returns and updates the declaration. Passed all six selections. | `docs/API.md:16–20` now states both behaviors explicitly; implementation identity remains unchanged. | Public example and canonical assertions cover both identities; corrected packaged guide/example bytes match source. | **Closed** |

The closure satisfies the original Code pre-commitment. Neither finding is closed merely from a drafter assertion.

### Dataclass result/capture ownership

The changed `exec` call uses `captures` as globals and a separate `results` dictionary as locals. The generated class output is read from `results`; generated methods retain capture globals that were not overwritten by the class declaration’s name.

Independent installed cases for `type`, `tuple`, `dict`, `int`, `hash` and `_y_dc_converter_0` passed construction and the relevant copy/state/pickle/hash operations. The converter was not executed during generation. No name restriction was substituted for the fix.

Class replacement, namespace installation and dictionary-mode mutation retain their prior semantics. Canonical class-cell/descriptor behavior remains covered by the final source/installed gates.

### Undoable capture and creation-name hygiene

`capture_ids` selects identifiers disjoint from the public model, current and working names. The same aliases are used for assembly associations, operand ownership and runtime capture installation.

The frozen `ComparisonCaptures` carrier stores the original ContextVar, facade equality/hash functions and object ordering descriptors. Authored resources read fixed attributes of that carrier through supported SDK reference bindings. This is generation-capture access, not a runtime field-name dispatcher.

Original failure names remain accepted. Alias-boundary names also pass. Independent hook/metaclass observations show public names during creation, including `_UserBase`, default, current and working classes; there is no internal-name creation followed by a compatibility-changing rename.

The native comparator, original operands, ownership fence and marker cleanup are unchanged. The corrected prelude still selects historical identity while active and structural comparison after closure. Disabled inheritance restores the original equality/hash/order objects.

### Backend-leak correction and honest evidence

`tests/conftest.py` restores the prior environment only around `test_failed_final_validation_preserves_completed_result`. Its `finally` handles exceptional exits; it does not catch assertion failures or rewrite accounting output.

The frozen test still requires the late-validation exception, absence of a published valid result and preservation of the completed attempt rows. The separate restoration sequence verifies the requested effective backend afterward. Three failed full Python attempts remain preserved; their corrected runs supply the final Python evidence.

Other setup/oracle corrections remain labeled as such. Original nine failures and six corrected owner retraces are preserved separately from post-GREEN verification.

### Historical performance and declarative boundaries

All nineteen H2 source hashes and its canonical definition still match:

`c4226335a0ecef51dc52b23906be2594deb68f2d226878c5ad45d2c2e900fc39`

Diff inspection also confirms the frozen performance sources/data were not changed by remediation. No benchmark was rerun.

The historical **73 pass / 47 inconclusive / zero confirmed regression** result remains tied to its original artifact tuple. Dataclass execution setup and Undoable prelude/dependent setter paths changed; inherited lazy layouts were outside those benchmark cases. Those old rows do not establish numerical performance of these corrected wheels.

The cold amendment, interrupted-v1 preservation, inconclusive noise/hash boundaries and unscored declarative calibration remain as previously assessed. The cold public-author observation remains a bounded usability record, not a calibrated grade or acceptance of subsequently changed bytes.

## 3. Risks and next action

The remaining limitations are documented callback effects, shallow immutability/hash responsibility, unsupported concurrent lazy first access, bounded private stdlib metadata compatibility and incomplete declarative calibration. Final-byte timing is unavailable; historical H2 conclusions retain their original provenance and unresolved intervals.

The next action is for the owner to merge this **GO** with the independent current State re-verdict on the same tuple and record the resulting implementation acceptance. No further Code remediation is required by this review.