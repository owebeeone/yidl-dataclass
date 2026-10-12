# DataclassDesign — SAFETY-AXIS REVIEW

**Review object:** `yidl-dataclass/dev-docs/DataclassDesign.md` and README consistency at `5d7883d8838fb9fa170426fbda59a71af3e9188b`. Status: proposed detailed design awaiting independent acceptance. This is a design re-verdict; no Dataclass implementation exists.

**Baseline:**

| Repository | Exact HEAD |
| --- | --- |
| yidl-dataclass | `5d7883d8838fb9fa170426fbda59a71af3e9188b` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| astichi | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Committed documents were read using `git show SHA:PATH`; the requested two-file revision diff was inspected. All six heads matched at the beginning and end.

**Date:** 2026-10-12  
**Axis:** Safety — failure recovery, identity boundaries, degraded behavior and compatibility blast radius. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on its current report. Filed verbatim by the lane owner.

**Verdict: NO-GO** — the original P2-1 is closed, but two new P2 findings block. Both concern bounded native-container comparison rules. No new architectural root cause was established. I pre-commit to GO on a revision resolving P2-2 and P2-3 as specified.

---

## Prior-finding closure table

| Prior finding | Verdict | Independent closure evidence |
| --- | --- | --- |
| P2-1: recursive projection replaces operands delivered to opaque equality callbacks | **Closed at the design gate** | Revised `dev-docs/DataclassDesign.md:519–526`, `530`, `566–572` and `603–608` preserve original operands and delegate opaque/list boundaries. In the original forward case, the callback receives exactly `inner`; in the reverse case, native list equality returns NotImplemented and the reflected callback receives that same object. Both return True. Lines 750–753 require narrow and staged-working-value integration regressions in both directions, with old/new value-policy spellings and structural generation enabled/disabled. |

This closes the specified design defect, not its future implementation tests. Closure follows the revised decision procedure and independently checked Python dispatch behavior; the owner’s disposition alone was not used as evidence.

## Changed-range analysis

The diff from `9fd44d91943ca706c4c51a0669bd3e9d03260278` to `5d7883d8838fb9fa170426fbda59a71af3e9188b` changes:

- `README.md:11–14`: accurately identifies the proposed design and places the TDD plan and implementation afterward.
- `dev-docs/DataclassDesign.md:271–324` and `412–425`: resolves initializer suppression before constructor availability checks; permits absent ordinary fields without generated consumers; preserves dictionary class-default fallback.
- `dev-docs/DataclassDesign.md:515–612`: replaces rebuilt-value projection with paired traversal, historical facade equality dispatch, a bounded mapping-proxy adapter, per-call recursion tracking and the existing callback ownership fence.
- `dev-docs/DataclassDesign.md:723–727`, `750–762` and `824–830`: adds corresponding regression and reference-evidence obligations.

The initializer corrections did not establish a new safety defect. The paired traversal closes the original operand-substitution counterexample. Its newly specified dictionary lookup and tuple length rules introduce the two bounded defects below.

**New architectural root causes: none established.** Neither finding requires abandoning the one-class model, named factories or shared YIDL comparison productions. Dictionary fidelity does require a concrete corrected mechanism; replacing one inaccurate equivalence claim with another would not close P2-2.

## 0. Evidence base

This re-review read:

- `dev-docs/DataclassDesign-RemPlan.md` and the originating `dev-docs/DataclassDesign-ReviewSafety.md` at the revised Dataclass SHA.
- The complete requested diff for `README.md` and `dev-docs/DataclassDesign.md`.
- Revised design lines 255–375, 405–612, 708–786 and 820–830; README lines 1–24; checkpoint lines 79–98.
- The original controlling requirements and pinned reference-source evidence retained from the originating review. Their relevant invariants are restated in this report.

Commands included `git -C MEMBER rev-parse HEAD`, `git -C MEMBER status --short`, `git show`, and:

```sh
git -C yidl-dataclass diff \
  9fd44d91943ca706c4c51a0669bd3e9d03260278..5d7883d8838fb9fa170426fbda59a71af3e9188b \
  -- README.md dev-docs/DataclassDesign.md
```

Official CPython sources were inspected:

- [3.12 dictionary implementation](https://github.com/python/cpython/blob/3.12/Objects/dictobject.c): `dict_equal` and `dict_get_impl`.
- [3.14 dictionary implementation](https://github.com/python/cpython/blob/3.14/Objects/dictobject.c): `dict_equal_lock_held` and `dict_get_impl`.
- [3.12 tuple implementation](https://github.com/python/cpython/blob/3.12/Objects/tupleobject.c): `tuplerichcompare`.
- [3.14 tuple implementation](https://github.com/python/cpython/blob/3.14/Objects/tupleobject.c): `tuple_richcompare`.
- [3.14 descriptor implementation](https://github.com/python/cpython/blob/3.14/Objects/descrobject.c): mapping-proxy traversal and rich-comparison forwarding.
- [GC referent documentation](https://docs.python.org/3.14/library/gc.html#gc.get_referents).

Read-only in-memory probes used CPython 3.12.12 with bytecode writes disabled. The following consolidated command was executed from that interpreter’s `bin` directory:

```sh
PYTHONDONTWRITEBYTECODE=1 ./python3.12 - <<'PY'
import gc, sys
from types import MappingProxyType
print('Python', sys.version.split()[0])
class AcceptOriginal:
    def __init__(self, expected):
        self.expected = expected
    def __eq__(self, other):
        print('original operand:', other is self.expected)
        if other is not self.expected:
            raise RuntimeError('operand replaced')
        return True
inner = [object()]
old, value = (AcceptOriginal(inner),), (inner,)
print('forward:', old == value)
print('reverse:', value == old)
class Key:
    calls = 0
    fail = False
    def __hash__(self):
        self.calls += 1
        if self.fail:
            raise RuntimeError('unexpected rehash')
        return 42
key = Key()
a, b = {key: 1}, {key: 1}
before = key.calls
print('native dict:', a == b, 'extra hashes:', key.calls - before)
before = key.calls
sentinel = object()
print('get:', b.get(key, sentinel), 'extra hashes:', key.calls - before)
key.fail = True
print('native dict after hash failure enabled:', a == b)
try:
    b.get(key, sentinel)
except RuntimeError as exc:
    print('get failure:', exc)
class Bomb:
    def __eq__(self, other):
        raise RuntimeError('tuple prefix callback')
left, right = (Bomb(),), (object(), 2)
try:
    left == right
except RuntimeError as exc:
    print('native tuple failure:', exc)
print('early length gate:', len(left) == len(right))
class Value:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        print('proxy direction:', self.name, '->', other.name)
        return True
ld, rd = {'x': Value('left')}, {'x': Value('right')}
lp, rp = MappingProxyType(ld), MappingProxyType(rd)
print('referent:', len(gc.get_referents(lp)), gc.get_referents(lp)[0] is ld)
lp == rp
lp == rd
ld == rp
PY
```

Observed:

```text
Python 3.12.12
original operand: True
forward: True
original operand: True
reverse: True
native dict: True extra hashes: 0
get: 1 extra hashes: 1
native dict after hash failure enabled: True
get failure: unexpected rehash
native tuple failure: tuple prefix callback
early length gate: False
referent: 1 True
proxy direction: right -> left
proxy direction: left -> right
proxy direction: right -> left
```

Additional probes confirmed ordinary custom-init, suppressed-init, absent-field and dictionary fallback behavior against stdlib dataclasses. Observations were: custom initialization produced 7; suppressed/generated source-free fields remained absent; explicit assignment succeeded; an `init=False` dictionary default left an empty instance dictionary and changed from 3 to 9 after updating the class default.

Opaque-proxy probes also confirmed the asymmetry of native forwarding: plain-proxy/opaque-proxy comparison delivered the original plain backing dict to the user callback, while the reverse delivered the original plain proxy. Delegating the original comparison preserves that distinction.

No files were modified, no builds or mutation-bearing tests were run, and no drafter or current peer reviewer was contacted. Dataclass, Astichi and Cache were clean at the final check; neighboring documentation drafts remained outside scope.

## 1. Findings

### [P2-2] Dictionary `get` adds hashing absent from native dictionary equality

**Location.** `yidl-dataclass/dev-docs/DataclassDesign.md` at `5d7883d8838fb9fa170426fbda59a71af3e9188b`, lines 531–537. This also affects dict-backed proxy traversal at lines 557–561.

**Violated invariant.** Value-write detection must preserve existing callback behavior while preventing structural facade equality from confusing node identity. The design specifically claims native hashing/identity behavior and preservation of opaque callbacks.

**Reproduction.** The probe creates two distinct exact dictionaries sharing one custom key whose hash always returns 42. Native `a == b` performs zero additional hash calls. The specified `b.get(key, sentinel)` performs one.

Enabling a subsequent hash failure makes the difference observable as an exception: native dictionary equality still returns True, whereas the required lookup raises `RuntimeError("unexpected rehash")`.

The key need not change its hash value. Even the nonthrowing constant-hash version proves that an additional application callback is introduced.

CPython dictionary equality reuses each entry’s stored hash for its opposite-dictionary lookup. `dict.get` obtains the key’s hash again. This distinction exists in both inspected 3.12 and 3.14 sources. [CPython dictionary implementation](https://github.com/python/cpython/blob/3.12/Objects/dictobject.c)

**Impact.** Existing value-policy assignments can gain callbacks, side effects or exceptions with structural generation disabled as well as enabled. Custom working dictionaries remain expressible through managed fields with custom freeze/thaw behavior. The existing ownership fence catches prohibited manager mutation; it cannot make this extra hash invocation equivalent to the prior comparison.

**Required correction.** Specify a dictionary-comparison mechanism that preserves cached-hash lookup behavior and original callback operands while applying node-identity comparison to values. Do not claim `.get`, subscription or membership testing is equivalent without proving its callback behavior. Preserve lookup direction, early exit and key-equality exception behavior. Any required platform adapter must have an explicit supported-version and failure contract.

**Classification.** New bounded algorithm-contract root cause. No architectural failure is established, but the corrected mechanism must be implementation-ready rather than an intention to preserve native behavior.

**Closure/regression.** Require zero additional custom-key hash calls relative to native equality after input preparation. Include constant-hash counters, a hash callback that raises upon unexpected reuse, equal distinct keys, collisions and key-equality exceptions. Exercise direct dictionaries and all supported dict/proxy directions; retain distinct-child node replacement tests. Add a staged-working-dictionary integration case for legacy/new value policies with generation on/off.

### [P2-3] Tuple length rejection suppresses native common-prefix callbacks

**Location.** `yidl-dataclass/dev-docs/DataclassDesign.md` at `5d7883d8838fb9fa170426fbda59a71af3e9188b`, lines 527–530.

**Violated invariant.** The adapter promises native container callback/dispatch behavior. The shared rule for exact lists and tuples checks lengths before visiting elements, but native tuple equality does not reject differing lengths first.

**Reproduction.** Compare `(Bomb(),)` with `(object(), 2)`, where `Bomb.__eq__` raises.

Native equality invokes the first element’s callback and raises `RuntimeError("tuple prefix callback")`. The specified early length gate returns False without invoking it. No facade or container subclass is involved.

Native tuple equality compares the common prefix and only compares lengths after exhausting that prefix without a mismatch. Lists have an early unequal-length check; tuples do not. Both inspected CPython versions retain this distinction. [CPython tuple implementation](https://github.com/python/cpython/blob/3.12/Objects/tupleobject.c)

**Impact.** An assignment that previously failed through its equality callback can instead proceed as an unequal write. Other callback effects and diagnostics can disappear. This is reachable with staged tuple values and a custom freeze callback, and affects disabled-generation compatibility too.

**Required correction.** Separate list and tuple procedures. Preserve list length rejection. For tuples, visit common-prefix pairs in order with native identity-or-equality semantics and short-circuit behavior; compare lengths only when that prefix is exhausted successfully.

**Classification.** New bounded algorithm-order root cause, independent of dictionary hashing and the closed operand-substitution finding.

**Closure/regression.** Compare unequal-length tuples whose common-prefix callbacks return True, return False, raise, or return an object with observable truth conversion. Include reversed operands and identical nonreflexive elements. Match native callback count/order, result and exception behavior. Pair with unequal-length list cases to prevent applying the tuple correction to lists.

## 2. Invariant analysis

**Original opaque-operand failure.** Paired traversal now stops at the opaque/list boundary and preserves original arguments in both directions. The revised tests cover the original staged-working-value scenario and the legacy/new option matrix. P2-1 is closed.

**Initializer suppression and provider availability.** Suppression precedes DAG/source enforcement, so ordinary custom or inherited initializers are not rejected merely because metadata lacks a generated source. Unconsumed ordinary fields may remain absent. Actual eager or delayed generated consumers still require available providers, including matched optional parameters. Dictionary fallback remains a read without an instance write; slotted/default-factory initialization remains distinct. The probed stdlib outcomes agree with this correction.

**Mapping-proxy boundary.** The single-referent adapter and forwarding directions agree with the inspected CPython implementation and 3.12.12 observations. User-mapping proxies remain opaque. Delegation preserves native forwarding even where the eventual callback argument differs by direction. The exact-dict traversal reached through the adapter remains subject to P2-2.

**Historical facade dispatch.** The revised procedure preserves type-MRO lookup, reflected strict-subclass priority, descriptor binding, NotImplemented continuation and one truth conversion. Restoring RuntimeFacade’s historical False against a nonfacade prevents an accidental extra opaque callback. Original state identity remains the write criterion across views. No additional counterexample was established in that boundary.

**Per-call recovery.** Recursion tracking uses active pairs rather than cached equality results, preserving repeated comparisons of shared acyclic branches. Detector state does not enter history and is discarded after failure. The entire operation remains inside the existing ownership fence. Identity-write policy remains `old is value`.

**Unchanged safeguards.** Lazy failure/retry and provider retention, active-copy rejection, private copy restoration, read-only public setters, storage-compatible inheritance, frozen writable-field exclusions, facade unhashability and node-ID membership remain governed by the original reviewed clauses. This revision does not weaken those boundaries.

**Evidence claims.** The design still distinguishes projected inspection from executed implementation evidence. The proxy adapter’s three-minor tests, runtime regressions and benchmarks remain future gates; a 3.12 probe does not establish the full support matrix.

## 3. Risks and next action

The remaining material risk is faithful reproduction of native container behavior without changing application callback demand. P2-2 shows that using a native Python operation does not automatically reproduce the native comparison operation’s internals.

Revise the dictionary and tuple decision procedures and their regression obligations, then obtain the required design re-verdict before advancing to the TDD plan or implementation.
