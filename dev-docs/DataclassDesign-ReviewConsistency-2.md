# DataclassDesign — CONSISTENCY-AXIS REVIEW

**Review object:** `yidl-dataclass/dev-docs/DataclassDesign.md` and README consistency at `5d7883d8838fb9fa170426fbda59a71af3e9188b`; proposed detailed design awaiting acceptance. No dataclass implementation or executed implementation regression suite exists.

**Baseline:**

| Repository | HEAD |
| --- | --- |
| yidl-dataclass | `5d7883d8838fb9fa170426fbda59a71af3e9188b` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| astichi | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Documents were read using `git show HEAD:PATH`; the correction was inspected with the requested Git diff. All six HEADs matched the revised tuple at the beginning and end.

**Date:** 2026-10-12

**Axis:** Consistency against the controlling requirements graph, plus public Surface at the detailed-design freeze. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on its current report. Filed verbatim by the lane owner.

**Verdict: NO-GO** — both original findings are closed, but one new P2 finding blocks. No new architectural root cause was identified. I pre-commit to GO on a revision resolving P2-2 as specified.

---

## Prior-finding closure table

| Original finding | Status | Independent closure evidence |
| --- | --- | --- |
| P2-1 — unconditional provider availability contradicts ordinary initializer suppression | **Closed at the design gate** | `dev-docs/DataclassDesign.md:271–324,412–423` resolves initializer action first, permits source-free ordinary fields when no generated consumer requires them, preserves custom/suppressed initialization, and specifies dictionary class-default fallback. Lines 723–727 require the original counterexamples and unavailable-consumer diagnostic in the differential corpus. |
| P3-1 — README says the detailed design remains unwritten | **Closed** | `README.md:11–14` directly links the proposed design and compatibility matrix, states that independent acceptance remains pending, and leaves the TDD plan and implementation as subsequent work. This agrees with the checkpoint. |

Closure rests on the revised contract and retraced counterexamples, not the remediation owner’s disposition. Runtime verification remains a later implementation obligation.

## Changed-range analysis

The requested diff from `9fd44d91943ca706c4c51a0669bd3e9d03260278` to `5d7883d8838fb9fa170426fbda59a71af3e9188b` changes:

- `README.md:11–14`: corrects design discoverability and status.
- `dev-docs/DataclassDesign.md:271–324,412–423`: resolves ordinary initializer suppression, actual provider availability and dictionary defaults.
- `dev-docs/DataclassDesign.md:515–612`: replaces rebuilt-value projection with paired comparison of original operands, adds historical facade dispatch, and specifies a bounded mapping-proxy adapter.
- `dev-docs/DataclassDesign.md:723–727,750–762`: adds regression obligations for both corrections.
- `dev-docs/DataclassDesign.md:824–830`: adds mapping-proxy reference evidence.

The initializer changes satisfy the original correction without changing the public marker API or accepted architecture.

The paired comparison preserves opaque operands and addresses the merged remediation’s original-operand example. Its exact-dictionary branch, however, equates `dict.get` lookup with native dictionary-equality lookup. Those operations invoke different key-hashing behavior, producing new finding P2-2.

**Architectural classification:** P2-2 is a bounded compatibility defect in the proposed Undoable-owned write detector. It does not refute the one-class dataclass architecture, field-local controls or reusable YIDL comparison generation.

## 0. Evidence base

Read at the revised dataclass SHA:

- `README.md:1–24`.
- `dev-docs/DataclassDesign.md`, with detailed inspection of Sections 5, 6, 8 and 10 and the added references.
- `dev-docs/DataclassDesign-RemPlan.md:1–17`.
- The complete filed prior Consistency report, `dev-docs/DataclassDesign-ReviewConsistency.md`.
- `dev-docs/DataclassDesign-PromptConsistency.md` and the supplied re-verdict prompt.
- `dev-docs/CurrentProgramCheckpoint.md:79–98`.

The controlling concept, protocol, golden amendment, operator amendment and declarative-evaluation graph remain unchanged from the first review. The first review’s pinned YIDL/Astichi composition inspection remains applicable because those repository revisions are unchanged.

Additional pinned Undoable inspections:

- `src/yidl_undoable/transaction_yidl.py:525–568,597–616`.
- `src/yidl_undoable/values.py:82–133`.
- `src/yidl_undoable/undoable.py:1–76`.
- Relevant custom freeze/thaw declarations in existing canonical examples.

Consulted primary CPython sources:

- [Dictionary equality and `dict.get` implementation](https://github.com/python/cpython/blob/3.12/Objects/dictobject.c), particularly `dict_equal` and `dict_get_impl`.
- [Mapping-proxy traversal and comparison forwarding](https://github.com/python/cpython/blob/3.14/Objects/descrobject.c).
- [GC referent inspection documentation](https://docs.python.org/3.14/library/gc.html#gc.get_referents).

Read-only in-memory probes used:

```text
PYTHONDONTWRITEBYTECODE=1 yidl/.venv/bin/python -
```

On CPython 3.12.12 they confirmed:

- Custom initialization supplied the required ordinary `init=False` slot.
- Decorator `init=False` permitted later explicit assignment.
- Generated construction permitted an unconsumed ordinary field to remain absent.
- Dictionary simple-default fallback left the instance dictionary empty and reflected a later class-default update.
- Native dictionary equality performed zero additional calls to an opaque key’s `__hash__`; the designed `right.get(key, sentinel)` called it once and raised when that callback rejected the additional invocation.
- Exact mapping-proxy GC inspection returned its original backing dictionary.
- Proxy/proxy comparison used right-backing/left-backing value comparison; proxy/dict used left-backing/right; dict/proxy used right-backing/left, agreeing with the revised forwarding directions.

A pinned Undoable in-memory probe used:

```text
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=astichi/src:yidl/src:yidl_undoable/src:yidl-lifecycle/src \
yidl/.venv/bin/python -
```

A managed field with `freeze=lambda value: None` accepted staged exact dictionaries containing an opaque hashable key. Comparing equal replacement dictionaries invoked that key’s hash zero times inside the historical comparison boundary and preserved the original staged dictionary.

An earlier attempt omitted the Astichi source path and failed during import; correcting the probe environment succeeded. That import failure is not a design finding.

No files, Git state, generated sources or builds were modified. No current-round peer report was accessed.

## 1. Findings

### [P2-2] `dict.get` adds key-hash callbacks that native dictionary equality avoids

**Location:** Dataclass repository, `dev-docs/DataclassDesign.md:531–537`, also reached through the dict-backed proxy branch at `:557–562`, at `5d7883d8838fb9fa170426fbda59a71af3e9188b`.

**Violated invariant:** The Undoable adapter must preserve existing value-write behavior while substituting historical node identity for engine-generated facade equality. The design explicitly claims that its dictionary lookup preserves native hashing behavior. `DataclassConcept.md:127–132` requires preservation of both transaction policies.

**Reproduction:**

```python
class Key:
    def __init__(self):
        self.calls = 0
        self.reject = False

    def __hash__(self):
        self.calls += 1
        if self.reject:
            raise RuntimeError("extra key hashing")
        return 17

key = Key()
left = {key: [1]}
right = {key: [1]}

key.calls = 0
key.reject = True

assert left == right
assert key.calls == 0

right.get(key, object())  # Raises RuntimeError; calls becomes 1.
```

The read-only probe produced precisely those outcomes.

Native CPython dictionary equality obtains the hash already stored with the left entry and performs a known-hash lookup in the right dictionary. `dict.get` instead invokes `PyObject_Hash` for this key. Using the original key object preserves operand identity but does not preserve the callback boundary. [CPython source](https://github.com/python/cpython/blob/3.12/Objects/dictobject.c)

This case is within the existing working-value surface: the pinned Undoable probe staged exact dictionaries with opaque keys under a custom freeze callback. It confirmed zero key-hash calls inside the historical equality boundary and no replacement for equal dictionaries. The defect does not require structural handles as dictionary keys.

**Impact:** Previously successful value-policy assignments can gain callback side effects or fail inside the comparison ownership fence. The change also affects native dict-backed proxies because they ultimately enter the same dictionary branch. A constant-returning hash callback that merely records calls already makes the incompatibility observable; the exception variant makes the behavioral failure explicit.

**Required correction:** Replace the prescribed `.get` algorithm with a settled strategy that preserves native cached-hash lookup semantics while comparing original value pairs through the historical facade detector. Document the feasible boundary and any necessary version-specific adapter before implementation. An ordinary subscript or membership lookup is not sufficient because it also hashes the key again.

Do not close this by weakening the existing opaque-callback or transaction-compatibility promises, or by restoring logical facade equality as a fallback.

**Closure/regression test:** Require:

1. Exact dictionaries sharing an opaque key whose constant-returning `__hash__` records calls; detector equality must add no hash calls.
2. A key that permits dictionary construction but rejects later hashing; native equality and the detector must still agree.
3. Equivalent dict-backed proxy cases in all specified operand directions.
4. An actual staged-working-value integration with a custom freeze callback, checking callback counts and unchanged write/no-write behavior for legacy/new value-policy spellings with structural generation enabled and disabled.
5. Coverage across supported CPython minors, preserving original operands and the existing ownership fence.

At this design gate, closure requires an implementable corrected strategy and those explicit obligations. No nonexistent runtime test result is required.

## 2. Invariant analysis

The original suppression counterexamples now have a single outcome. The revised text distinguishes metadata/storage setup from generated candidate evaluation, preserves dictionary fallbacks without instance writes, and retains unavailable-provider rejection only where a generated consumer actually requires the value.

The revised paired traversal addresses the merged original-operand example: an opaque comparison receives the original nested list in both directions rather than a reconstructed payload. Exact container checks prevent accidental descent into container subclasses. Top-level opaque self-equality remains distinct from container-element identity shortcuts.

The mapping-proxy adapter has an explicit CPython boundary, original-referent identity requirement, supported-minor contract tests and fail-closed behavior. The forwarding directions match the inspected CPython source and the probe. Opaque proxy boundaries delegate through native forwarding rather than manually substituting callback operands. [CPython mapping-proxy source](https://github.com/python/cpython/blob/3.14/Objects/descrobject.c)

Historical facade dispatch, generated-descriptor identification, strict-subclass priority, `NotImplemented`, truth conversion and ownership fencing are specified. Active recursion pairs replace cached comparison results, preserving repeated comparisons of shared acyclic subobjects.

The unchanged public API, hidden-provider lifetime, field-local flags, comparison-generation defaults and modular YIDL/Astichi generation boundaries remain coherent with the controlling brief. No additional finding was established there.

## 3. Risks and next action

Historical rich-comparison dispatch and CPython adapters still need their required implementation corpus; the design correctly distinguishes proposed behavior from executed evidence.

The next action is a bounded revision of the dictionary comparison strategy addressing P2-2, followed by same-axis re-verdict on the new exact tuple. Both original Consistency findings remain closed.
