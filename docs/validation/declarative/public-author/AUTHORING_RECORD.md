# Dataclass cold public authoring record

This is an uncalibrated first-day public-author observation. It is not an overall declarativity score or an implementation review/verdict. The author stops after this record awaiting a separate final Code review task.

## Scope and cold boundary

Deliverables: four runnable public-API cards, saved first sources and every repair, exact execution evidence, immutable wheel/documentation checks, and this standalone record. Only this external author directory was written. No repository, installed package, dependency or Git changes were made. Dataclass was the installed immutable product; Astichi 1.1.3 and YIDL 0.1.0 were reference/runtime dependencies. Undoable was unnecessary and not inspected.

Before authoring, AGENTS_GWZ.md and the dispatched author brief were read. The sole product documentation read was the installed README.md, docs/API.md, docs/Generation.md, and examples/first_use.py, reproduced below in the documentation-read stdout and copied under public-docs/. Public callable signatures, public package origins, public performance-counter metadata, standard field helpers, __slots__, and public field descriptors were inspected. No implementation source, callable bodies, private attributes, private documentation, designs/plans, tests/goldens, oracle snapshots, or other-agent reports were read. No agents were spawned and no drafter hints were requested.

## Timing and identity

```json
{
  "actual_author_start_utc": "2026-10-12T15:02:38+00:00",
  "actual_author_end_utc": "2026-10-12T15:07:14.647023+00:00",
  "author_elapsed_seconds": 276.647023,
  "original_go_utc_as_dispatched": "03:36:48Z",
  "immutable_consumer_revision_as_dispatched": "446dc1ee5d9cbe9d2b4c485bb2675eaddbdc138f",
  "wheel_sha256": "50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b",
  "billing_metadata": "Unavailable to author; not zero. Captured separately by owner.",
  "final_programs": [
    "card1_attempt02.py",
    "card2_attempt01.py",
    "card3_attempt01.py",
    "card4_with_cache_attempt02.py",
    "card4_without_cache_attempt02.py"
  ],
  "card_program_executions": 8,
  "card_failed_executions": 3,
  "required_clarification": null,
  "implementation_verdict": "Not performed in author phase"
}
```

The consumer revision is dispatch provenance; no Git inspection was performed. The wheel archive bytes and the four installed documentation files were hashed at the start and end and remained identical. Public package origins were under the isolated interpreter sys.prefix. python -I excluded the author directory, sibling checkouts and PYTHONPATH from import resolution.

## First-day outcomes and author decisions

| Card | Final program | Result |
| --- | --- | --- |
| 1 | card1_attempt02.py | quantity 2.8→2, unit price 5, readonly total 10; writable cache replacement and entry mutation excluded from equality/hash; hidden locale; first/cached receipt; replacement quantity 3 and total 15; public inspection all exercised. |
| 2 | card2_attempt01.py | Nullable None preservation and 4.8→4 conversion work at construction and assignment; explicit converter=None preserves float values despite class convert=True. |
| 3 | card3_attempt01.py | Inherited order value/mode/extra, required keyword-only override, inherited public slot descriptor reuse, and zero-argument super all work. |
| 4 | both card4_*_attempt02.py | Removing only the cache declaration leaves frozen=True/order=True unchanged. Both types independently retain identical equality, inequality, ordering and hash outcomes. |

Initial author choices: use a frozen quote, const(init=False) for the dependent total, named InitVar/lazy providers for locale and receipt, and an ordinary mutable cache explicitly excluded from comparison/hash/repr. The cache explicitly disables inferred conversion because dict is not an inferred constructor type. Receipt is excluded from comparison/hash/repr to keep logical comparisons and presentation from incidentally causing its lazy evaluation; readonly comes from frozen=True. Replacement omits the defaulted locale intentionally to demonstrate the documented reinitialization provider behavior.

The child overrides the base mode field from a defaulted keyword-only field to a required keyword-only field while retaining its ordinary writable storage shape. Card 4 enables order as well as frozen equality/hash and keeps those options unchanged. No handwritten model implementation substitutes for generated behavior.

Three failed executions were preserved. Card 1 had an author expectation error about replacement: its ordinary init=True cache should be carried to the new constructor, not rebuilt. Both Card 4 first executions completed their requested model assertions and printed successful logical outcomes, then failed the author counter assertion because decoration happened outside its collection window. Repairs did not change class options or relax any requested behavior. See exact rationales and source versions below. No required clarification remained.

## Backend evidence

All product executions set ASTICHI_LOWER_ENGINE=native-rust on the exact isolated CPython 3.12 interpreter. The public probe reported 32 native-only batch requests out of 32 engine requests. Final cards reported respectively 270/270, 100/100, 105/105, 106/106 and 88/88 native-only/engine requests. Their runtime assertions require positive native-only counts, equality with all counted engine requests, and zero fallback-labelled counter values. No fallback was observed on these selected lowering requests. This does not claim wholly Rust program execution or a speed/memory advantage; ordinary Python runtime and other SDK work remain visible in the counters.

## Preserved source manifests

### first-attempt-manifest.json

```json
{
  "card1_attempt01.py": {
    "sha256": "af5048367e54c6afe051b72e7f2d15e8b49236fe97aeacb185c29b1de6b8e108",
    "created_before_execution_utc": "2026-10-12T15:04:56.847422+00:00"
  },
  "card2_attempt01.py": {
    "sha256": "6c956b70b656909ccdea33cd1edde9a07c6835042b123bfc122c50f1c8932f03",
    "created_before_execution_utc": "2026-10-12T15:04:56.891764+00:00"
  },
  "card3_attempt01.py": {
    "sha256": "89166b6e08373ef6455bbe0920b846a4c958306f51d2e961fb28378f05dde49a",
    "created_before_execution_utc": "2026-10-12T15:04:56.942154+00:00"
  },
  "card4_with_cache_attempt01.py": {
    "sha256": "f93c065afcfc8f485e8e88a0eedf51cebd20c09b5d304de232763a6ddb1a5acd",
    "created_before_execution_utc": "2026-10-12T15:04:57.039956+00:00"
  },
  "card4_without_cache_attempt01.py": {
    "sha256": "e5ddcaefe36775c9a4328fb40bbe7ed2e8e18739d2fe3832074b50727a431540",
    "created_before_execution_utc": "2026-10-12T15:04:57.192113+00:00"
  }
}
```

### repair-attempt-manifest.json

```json
{
  "card1_attempt02.py": {
    "sha256": "fefbcdcce0ff19adae8f6262b060911a7ed84f0d92f53466eb0519a0429e0d0f",
    "created_before_execution_utc": "2026-10-12T15:05:31.650810+00:00"
  },
  "card4_with_cache_attempt02.py": {
    "sha256": "c2c9f2547e9ed235bf9d80f6fb58a19dcc5d55976d83ae0d5c2b351a1df6f340",
    "created_before_execution_utc": "2026-10-12T15:05:31.675894+00:00"
  },
  "card4_without_cache_attempt02.py": {
    "sha256": "d89eb587cbf6722227880270536c243e703b43e1d8fbff18cff8554e34abf47e",
    "created_before_execution_utc": "2026-10-12T15:05:31.713783+00:00"
  }
}
```

### repairs.json

```json
[
  {
    "card": 1,
    "from": "attempt01",
    "to": "attempt02",
    "failure": "AssertionError at revised cache expectation after successful quote operations",
    "rationale": "Author incorrectly expected every cache to rebuild. Public API Helpers, replacement and copying says existing init=True ordinary fields are read unless changed; this cache has default init=True. Keep declaration unchanged and assert the public cache object is passed to replacement.",
    "change": "Replaced fresh-empty-cache assertion with revised.cache is quote.cache."
  },
  {
    "card": 4,
    "from": "attempt01 (both variants)",
    "to": "attempt02 (both variants)",
    "failure": "All logical assertions passed and result printed, then native lowering count assertion failed because decoration ran before collection started.",
    "rationale": "Author instrumentation error. Decoration must occur within the public performance-counter context; move the existing declaration into main, which is called within that context.",
    "change": "Both variants receive the same indentation/location repair. Their only mutual source difference remains deletion of the cache declaration; frozen=True and order=True are unchanged."
  }
]
```

### card4-declaration-removal.json

```json
{
  "only_deleted_line": "    cache: dict = field(default_factory=dict, mutable=True, compare=False, hash=False, repr=False)\n",
  "unchanged_options": "frozen=True, order=True"
}
```

### end-check.json

```json
{
  "checked_utc": "2026-10-12T15:06:11.190353+00:00",
  "wheel_sha256": "50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b",
  "docs_sha256": {
    "README.md": "bca02bb92faec55dc0eba82132ca1371504fd91b1e36e9bfdf698dc0fcf0774a",
    "docs/API.md": "dc56c40a909d3347c75101a6ee2fe77a279bbe36cc146d314f5c115116702512",
    "docs/Generation.md": "bee2d0798b3f66a6f358a62a46cfb2a645cb0c34b5f18e8dd96538a2f77fb624",
    "examples/first_use.py": "bf78302fb7ff863f6762a7e9c90fc12117edd9c736d6ee7957ac6c9db28363d0"
  },
  "versions": {
    "yidl-dataclass": "0.1.0.dev0",
    "astichi": "1.1.3",
    "yidl": "0.1.0"
  },
  "public_module_origins": {
    "yidl_dataclass": "external:verification-root/venv-3.12/lib/python3.12/site-packages/yidl_dataclass/__init__.py",
    "astichi": "external:verification-root/venv-3.12/lib/python3.12/site-packages/astichi/__init__.py",
    "yidl": "external:verification-root/venv-3.12/lib/python3.12/site-packages/yidl/__init__.py"
  },
  "source_manifests_unchanged": true,
  "card4_only_declaration_removed_both_attempts": true,
  "card4_logical_results_identical": true
}
```

## Every authored card source

### card1_attempt01.py

```python
import json
from astichi.perf_counters import collect_perf_counters
from yidl_dataclass import (
    FrozenInstanceError, const, dataclass, field, fields, initvar, lazy,
    replace, storage_fields,
)


def main():
    receipt_calls = []

    def receipt_text(locale, total):
        receipt_calls.append((locale, total))
        return f'{locale}: total={total}'

    @dataclass(frozen=True, convert=True)
    class Quote:
        quantity: int
        unit_price: int = 5
        total: int = const(
            default_factory=lambda quantity, unit_price: quantity * unit_price,
            init=False,
        )
        cache: dict = field(
            default_factory=dict, mutable=True, compare=False, hash=False,
            repr=False, converter=None,
        )
        locale: str = initvar(default='en-AU')
        receipt: str = lazy(
            default_factory=receipt_text, compare=False, hash=False, repr=False,
        )

    quote = Quote(2.8, locale='en-NZ')
    assert quote.quantity == 2 and type(quote.quantity) is int
    assert quote.unit_price == 5 and quote.total == 10
    assert not hasattr(quote, 'locale')
    assert receipt_calls == []
    first_receipt = quote.receipt
    cached_receipt = quote.receipt
    assert first_receipt == cached_receipt == 'en-NZ: total=10'
    assert receipt_calls == [('en-NZ', 10)]

    equivalent = Quote(2, locale='en-NZ')
    assert quote == equivalent
    original_hash = hash(quote)
    quote.cache['old'] = 1
    assert quote == equivalent and hash(quote) == original_hash
    replacement_cache = {'replacement': 2}
    quote.cache = replacement_cache
    assert quote.cache is replacement_cache
    quote.cache['entry'] = 3
    assert quote == equivalent and hash(quote) == original_hash
    for name in ('quantity', 'unit_price', 'total', 'receipt'):
        try:
            setattr(quote, name, 999)
        except FrozenInstanceError:
            pass
        else:
            raise AssertionError(f'{name} unexpectedly writable')

    revised = replace(quote, quantity=3)
    assert revised.quantity == 3 and revised.total == 15
    assert revised.cache == {} and revised.cache is not quote.cache
    assert receipt_calls == [('en-NZ', 10)]
    assert revised.receipt == 'en-AU: total=15'
    assert receipt_calls == [('en-NZ', 10), ('en-AU', 15)]
    names = [description.name for description in fields(quote)]
    assert names == ['quantity', 'unit_price', 'total', 'cache', 'receipt']
    metadata = [
        {'name': description.name, 'kind': description.kind.label,
         'mutable': description.mutable,
         'dependencies': list(description.dependencies),
         'retained': description.retained}
        for description in storage_fields(quote)
    ]
    print(json.dumps({
        'quantity': quote.quantity, 'unit_price': quote.unit_price,
        'total': quote.total, 'receipt_first': first_receipt,
        'receipt_cached': cached_receipt, 'receipt_calls': receipt_calls,
        'cache': quote.cache, 'logical_equality_after_cache_change': quote == equivalent,
        'hash_unchanged': hash(quote) == original_hash,
        'replacement_quantity': revised.quantity, 'replacement_total': revised.total,
        'replacement_receipt': revised.receipt, 'public_fields': names,
        'storage_metadata': metadata,
    }, sort_keys=True))


if __name__ == '__main__':
    with collect_perf_counters() as counters:
        main()
    assert counters.counts['native_scope_batch_native_only'] > 0
    assert counters.counts['native_scope_batch_native_only'] == counters.counts['native_scope_batch_engine_request_count']
    assert sum(value for name, value in counters.counts.items() if 'fallback' in name) == 0
    print('backend_counts:', json.dumps(dict(counters.counts), sort_keys=True))
```

### card1_attempt02.py

```python
import json
from astichi.perf_counters import collect_perf_counters
from yidl_dataclass import (
    FrozenInstanceError, const, dataclass, field, fields, initvar, lazy,
    replace, storage_fields,
)


def main():
    receipt_calls = []

    def receipt_text(locale, total):
        receipt_calls.append((locale, total))
        return f'{locale}: total={total}'

    @dataclass(frozen=True, convert=True)
    class Quote:
        quantity: int
        unit_price: int = 5
        total: int = const(
            default_factory=lambda quantity, unit_price: quantity * unit_price,
            init=False,
        )
        cache: dict = field(
            default_factory=dict, mutable=True, compare=False, hash=False,
            repr=False, converter=None,
        )
        locale: str = initvar(default='en-AU')
        receipt: str = lazy(
            default_factory=receipt_text, compare=False, hash=False, repr=False,
        )

    quote = Quote(2.8, locale='en-NZ')
    assert quote.quantity == 2 and type(quote.quantity) is int
    assert quote.unit_price == 5 and quote.total == 10
    assert not hasattr(quote, 'locale')
    assert receipt_calls == []
    first_receipt = quote.receipt
    cached_receipt = quote.receipt
    assert first_receipt == cached_receipt == 'en-NZ: total=10'
    assert receipt_calls == [('en-NZ', 10)]

    equivalent = Quote(2, locale='en-NZ')
    assert quote == equivalent
    original_hash = hash(quote)
    quote.cache['old'] = 1
    assert quote == equivalent and hash(quote) == original_hash
    replacement_cache = {'replacement': 2}
    quote.cache = replacement_cache
    assert quote.cache is replacement_cache
    quote.cache['entry'] = 3
    assert quote == equivalent and hash(quote) == original_hash
    for name in ('quantity', 'unit_price', 'total', 'receipt'):
        try:
            setattr(quote, name, 999)
        except FrozenInstanceError:
            pass
        else:
            raise AssertionError(f'{name} unexpectedly writable')

    revised = replace(quote, quantity=3)
    assert revised.quantity == 3 and revised.total == 15
    assert revised.cache is quote.cache
    assert receipt_calls == [('en-NZ', 10)]
    assert revised.receipt == 'en-AU: total=15'
    assert receipt_calls == [('en-NZ', 10), ('en-AU', 15)]
    names = [description.name for description in fields(quote)]
    assert names == ['quantity', 'unit_price', 'total', 'cache', 'receipt']
    metadata = [
        {'name': description.name, 'kind': description.kind.label,
         'mutable': description.mutable,
         'dependencies': list(description.dependencies),
         'retained': description.retained}
        for description in storage_fields(quote)
    ]
    print(json.dumps({
        'quantity': quote.quantity, 'unit_price': quote.unit_price,
        'total': quote.total, 'receipt_first': first_receipt,
        'receipt_cached': cached_receipt, 'receipt_calls': receipt_calls,
        'cache': quote.cache, 'logical_equality_after_cache_change': quote == equivalent,
        'hash_unchanged': hash(quote) == original_hash,
        'replacement_quantity': revised.quantity, 'replacement_total': revised.total,
        'replacement_receipt': revised.receipt, 'public_fields': names,
        'storage_metadata': metadata,
    }, sort_keys=True))


if __name__ == '__main__':
    with collect_perf_counters() as counters:
        main()
    assert counters.counts['native_scope_batch_native_only'] > 0
    assert counters.counts['native_scope_batch_native_only'] == counters.counts['native_scope_batch_engine_request_count']
    assert sum(value for name, value in counters.counts.items() if 'fallback' in name) == 0
    print('backend_counts:', json.dumps(dict(counters.counts), sort_keys=True))
```

### card2_attempt01.py

```python
import json
from astichi.perf_counters import collect_perf_counters
from yidl_dataclass import dataclass, field


def main():
    @dataclass(convert=True)
    class Nullable:
        amount: int | None
        unchanged: int = field(converter=None)

    missing = Nullable(None, 4.8)
    converted = Nullable(4.8, 4.8)
    assert missing.amount is None
    assert converted.amount == 4 and type(converted.amount) is int
    assert missing.unchanged == converted.unchanged == 4.8
    assert type(converted.unchanged) is float
    construction = [(missing.amount, missing.unchanged), (converted.amount, converted.unchanged)]
    missing.amount = 4.8
    converted.amount = None
    converted.unchanged = 7.9
    assert missing.amount == 4 and type(missing.amount) is int
    assert converted.amount is None
    assert converted.unchanged == 7.9 and type(converted.unchanged) is float
    print(json.dumps({'construction': construction,
                      'after_assignment': [(missing.amount, missing.unchanged),
                                           (converted.amount, converted.unchanged)]}))


if __name__ == '__main__':
    with collect_perf_counters() as counters:
        main()
    assert counters.counts['native_scope_batch_native_only'] > 0
    assert counters.counts['native_scope_batch_native_only'] == counters.counts['native_scope_batch_engine_request_count']
    assert sum(value for name, value in counters.counts.items() if 'fallback' in name) == 0
    print('backend_counts:', json.dumps(dict(counters.counts), sort_keys=True))
```

### card3_attempt01.py

```python
import inspect
import json
from astichi.perf_counters import collect_perf_counters
from yidl_dataclass import dataclass, field, fields


def main():
    @dataclass
    class Base:
        value: int
        mode: str = field(default='base', kw_only=True)

        def describe(self):
            return f'{self.value}:{self.mode}'

    @dataclass
    class Child(Base):
        mode: str = field(kw_only=True)
        extra: int = 7

        def describe(self):
            return super().describe() + f':child={self.extra}'

    base = Base(1)
    child = Child(1, mode='child')
    assert base.describe() == '1:base'
    assert child.describe() == '1:child:child=7'
    assert [description.name for description in fields(Child)] == ['value', 'mode', 'extra']
    assert 'mode' in Base.__slots__ and 'mode' not in Child.__slots__
    assert Child.__slots__ == ('extra',)
    assert not hasattr(child, '__dict__')
    assert Base.mode is Child.mode
    child.mode = 'updated'
    assert child.mode == 'updated' and child.describe() == '1:updated:child=7'
    failures = []
    for description, args in [('omitted required keyword', (1,)),
                              ('keyword passed positionally', (1, 7, 'child'))]:
        try:
            Child(*args)
        except TypeError as error:
            failures.append({'case': description, 'message': str(error)})
        else:
            raise AssertionError(description + ' unexpectedly accepted')
    print(json.dumps({'field_order': [description.name for description in fields(Child)],
                      'signature': str(inspect.signature(Child)),
                      'base_slots': Base.__slots__, 'child_slots': Child.__slots__,
                      'reused_public_descriptor': Base.mode is Child.mode,
                      'super_result': child.describe(), 'required_keyword_failures': failures},
                     sort_keys=True))


if __name__ == '__main__':
    with collect_perf_counters() as counters:
        main()
    assert counters.counts['native_scope_batch_native_only'] > 0
    assert counters.counts['native_scope_batch_native_only'] == counters.counts['native_scope_batch_engine_request_count']
    assert sum(value for name, value in counters.counts.items() if 'fallback' in name) == 0
    print('backend_counts:', json.dumps(dict(counters.counts), sort_keys=True))
```

### card4_with_cache_attempt01.py

```python
import json
from astichi.perf_counters import collect_perf_counters
from yidl_dataclass import dataclass, field, fields


@dataclass(frozen=True, order=True)
class Model:
    value: int
    cache: dict = field(default_factory=dict, mutable=True, compare=False, hash=False, repr=False)


def main():
    first, equal, greater = Model(2), Model(2), Model(3)
    initial_hash = hash(first)
    assert first == equal and first != greater
    assert first < greater and greater > first
    assert hash(first) == hash(equal)
    has_cache = 'cache' in [description.name for description in fields(Model)]
    if has_cache:
        first.cache['entry'] = 1
        first.cache = {'replacement': 2}
        first.cache['new-entry'] = 3
        assert first.cache == {'replacement': 2, 'new-entry': 3}
    assert first == equal and first != greater
    assert first < greater and greater > first
    assert hash(first) == hash(equal) == initial_hash
    print(json.dumps({'has_cache': has_cache,
                      'logical': {'equal': first == equal, 'different': first != greater,
                                  'ordered': first < greater, 'equal_hashes': hash(first) == hash(equal),
                                  'stable_hash': hash(first) == initial_hash}}, sort_keys=True))


if __name__ == '__main__':
    with collect_perf_counters() as counters:
        main()
    assert counters.counts['native_scope_batch_native_only'] > 0
    assert counters.counts['native_scope_batch_native_only'] == counters.counts['native_scope_batch_engine_request_count']
    assert sum(value for name, value in counters.counts.items() if 'fallback' in name) == 0
    print('backend_counts:', json.dumps(dict(counters.counts), sort_keys=True))
```

### card4_with_cache_attempt02.py

```python
import json
from astichi.perf_counters import collect_perf_counters
from yidl_dataclass import dataclass, field, fields


def main():
    @dataclass(frozen=True, order=True)
    class Model:
        value: int
        cache: dict = field(default_factory=dict, mutable=True, compare=False, hash=False, repr=False)


    first, equal, greater = Model(2), Model(2), Model(3)
    initial_hash = hash(first)
    assert first == equal and first != greater
    assert first < greater and greater > first
    assert hash(first) == hash(equal)
    has_cache = 'cache' in [description.name for description in fields(Model)]
    if has_cache:
        first.cache['entry'] = 1
        first.cache = {'replacement': 2}
        first.cache['new-entry'] = 3
        assert first.cache == {'replacement': 2, 'new-entry': 3}
    assert first == equal and first != greater
    assert first < greater and greater > first
    assert hash(first) == hash(equal) == initial_hash
    print(json.dumps({'has_cache': has_cache,
                      'logical': {'equal': first == equal, 'different': first != greater,
                                  'ordered': first < greater, 'equal_hashes': hash(first) == hash(equal),
                                  'stable_hash': hash(first) == initial_hash}}, sort_keys=True))


if __name__ == '__main__':
    with collect_perf_counters() as counters:
        main()
    assert counters.counts['native_scope_batch_native_only'] > 0
    assert counters.counts['native_scope_batch_native_only'] == counters.counts['native_scope_batch_engine_request_count']
    assert sum(value for name, value in counters.counts.items() if 'fallback' in name) == 0
    print('backend_counts:', json.dumps(dict(counters.counts), sort_keys=True))
```

### card4_without_cache_attempt01.py

```python
import json
from astichi.perf_counters import collect_perf_counters
from yidl_dataclass import dataclass, field, fields


@dataclass(frozen=True, order=True)
class Model:
    value: int


def main():
    first, equal, greater = Model(2), Model(2), Model(3)
    initial_hash = hash(first)
    assert first == equal and first != greater
    assert first < greater and greater > first
    assert hash(first) == hash(equal)
    has_cache = 'cache' in [description.name for description in fields(Model)]
    if has_cache:
        first.cache['entry'] = 1
        first.cache = {'replacement': 2}
        first.cache['new-entry'] = 3
        assert first.cache == {'replacement': 2, 'new-entry': 3}
    assert first == equal and first != greater
    assert first < greater and greater > first
    assert hash(first) == hash(equal) == initial_hash
    print(json.dumps({'has_cache': has_cache,
                      'logical': {'equal': first == equal, 'different': first != greater,
                                  'ordered': first < greater, 'equal_hashes': hash(first) == hash(equal),
                                  'stable_hash': hash(first) == initial_hash}}, sort_keys=True))


if __name__ == '__main__':
    with collect_perf_counters() as counters:
        main()
    assert counters.counts['native_scope_batch_native_only'] > 0
    assert counters.counts['native_scope_batch_native_only'] == counters.counts['native_scope_batch_engine_request_count']
    assert sum(value for name, value in counters.counts.items() if 'fallback' in name) == 0
    print('backend_counts:', json.dumps(dict(counters.counts), sort_keys=True))
```

### card4_without_cache_attempt02.py

```python
import json
from astichi.perf_counters import collect_perf_counters
from yidl_dataclass import dataclass, field, fields


def main():
    @dataclass(frozen=True, order=True)
    class Model:
        value: int


    first, equal, greater = Model(2), Model(2), Model(3)
    initial_hash = hash(first)
    assert first == equal and first != greater
    assert first < greater and greater > first
    assert hash(first) == hash(equal)
    has_cache = 'cache' in [description.name for description in fields(Model)]
    if has_cache:
        first.cache['entry'] = 1
        first.cache = {'replacement': 2}
        first.cache['new-entry'] = 3
        assert first.cache == {'replacement': 2, 'new-entry': 3}
    assert first == equal and first != greater
    assert first < greater and greater > first
    assert hash(first) == hash(equal) == initial_hash
    print(json.dumps({'has_cache': has_cache,
                      'logical': {'equal': first == equal, 'different': first != greater,
                                  'ordered': first < greater, 'equal_hashes': hash(first) == hash(equal),
                                  'stable_hash': hash(first) == initial_hash}}, sort_keys=True))


if __name__ == '__main__':
    with collect_perf_counters() as counters:
        main()
    assert counters.counts['native_scope_batch_native_only'] > 0
    assert counters.counts['native_scope_batch_native_only'] == counters.counts['native_scope_batch_engine_request_count']
    assert sum(value for name, value in counters.counts.items() if 'fallback' in name) == 0
    print('backend_counts:', json.dumps(dict(counters.counts), sort_keys=True))
```

## Supporting scripts

### run_record.py

```python
import datetime
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).parent
label = sys.argv[1]
command = sys.argv[2:]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(command, cwd=root, capture_output=True, text=True)
ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
(root / (label + '.stdout')).write_text(result.stdout)
(root / (label + '.stderr')).write_text(result.stderr)
record = {'label': label, 'command': command, 'cwd': str(root), 'started_utc': started, 'ended_utc': ended, 'exit_code': result.returncode}
(root / (label + '.execution.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
print(result.stdout, end='')
print(result.stderr, end='', file=sys.stderr)
sys.exit(result.returncode)
```

### read_public_docs.py

```python
import hashlib
import importlib.metadata
import importlib.resources
import json
import pathlib
import sys

root = pathlib.Path('external:public-author')
wheel = pathlib.Path('external:stage-g-artifacts/dataclass-final/yidl_dataclass-0.1.0.dev0-py3-none-any.whl')
sha = hashlib.sha256(wheel.read_bytes()).hexdigest()
assert sha == '50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b'
print('wheel_sha256:', sha)
for name in ['yidl-dataclass', 'astichi', 'yidl']:
    print('distribution:', name, importlib.metadata.version(name))
import yidl_dataclass
import astichi
import yidl
for module in [yidl_dataclass, astichi, yidl]:
    origin = pathlib.Path(module.__file__).resolve()
    assert origin.is_relative_to(pathlib.Path(sys.prefix).resolve()), (module.__name__, origin)
    print('public_origin:', module.__name__, origin)
print('sys.prefix:', sys.prefix)
print('sys.path:', sys.path)
docs = importlib.resources.files('yidl_dataclass').joinpath('documentation')
hashes = {}
for name in ['README.md', 'docs/API.md', 'docs/Generation.md', 'examples/first_use.py']:
    data = docs.joinpath(name).read_bytes()
    hashes[name] = hashlib.sha256(data).hexdigest()
    target = root / 'public-docs' / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    print('\nPUBLIC DOCUMENT:', name, 'sha256:', hashes[name])
    print(data.decode())
(root / 'start-doc-hashes.json').write_text(json.dumps(hashes, indent=2) + '\n')
```

### inspect_public_surface.py

```python
import inspect
import os
import astichi
import yidl_dataclass

print('ASTICHI_LOWER_ENGINE:', os.environ.get('ASTICHI_LOWER_ENGINE'))
for module in [astichi, yidl_dataclass]:
    names = [name for name in dir(module) if not name.startswith('_')]
    print(module.__name__, 'public names:', names)
    for name in names:
        value = getattr(module, name)
        if callable(value):
            try:
                print(name, inspect.signature(value))
            except (TypeError, ValueError):
                print(name, 'signature unavailable')
```

### backend_public_signatures.py

```python
import inspect
import astichi

for module in [astichi.lowering, astichi.perf_counters]:
    print('module:', module.__name__)
    for name in dir(module):
        if not name.startswith('_'):
            value = getattr(module, name)
            if callable(value):
                try:
                    print(name, inspect.signature(value))
                except (ValueError, TypeError):
                    print(name, 'signature unavailable')
            elif isinstance(value, (str, int, bool, type(None))):
                print(name, value)
            else:
                print(name, 'public value type:', type(value).__name__)
```

### backend_probe.py

```python
import json
from astichi.perf_counters import collect_perf_counters
from yidl_dataclass import dataclass

with collect_perf_counters() as counters:
    @dataclass
    class Probe:
        value: int

    assert Probe(3).value == 3
print(json.dumps(dict(counters.counts), sort_keys=True))
print(json.dumps(dict(counters.seconds), sort_keys=True))
```

### end_check.py

```python
import datetime
import hashlib
import importlib.metadata
import importlib.resources
import json
import pathlib
import sys
import astichi
import yidl
import yidl_dataclass

root = pathlib.Path('external:public-author')
wheel = pathlib.Path('external:stage-g-artifacts/dataclass-final/yidl_dataclass-0.1.0.dev0-py3-none-any.whl')
wheel_hash = hashlib.sha256(wheel.read_bytes()).hexdigest()
assert wheel_hash == '50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b'
docs = importlib.resources.files('yidl_dataclass').joinpath('documentation')
initial = json.loads((root / 'start-doc-hashes.json').read_text())
final = {name: hashlib.sha256(docs.joinpath(name).read_bytes()).hexdigest() for name in initial}
assert initial == final
for manifest_name in ['first-attempt-manifest.json', 'repair-attempt-manifest.json']:
    for name, entry in json.loads((root / manifest_name).read_text()).items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == entry['sha256']
removed_line = '    cache: dict = field(default_factory=dict, mutable=True, compare=False, hash=False, repr=False)\n'
for attempt in ['01', '02']:
    with_source = (root / f'card4_with_cache_attempt{attempt}.py').read_text()
    without_source = (root / f'card4_without_cache_attempt{attempt}.py').read_text()
    line = removed_line if attempt == '01' else '    ' + removed_line
    assert with_source.count(line) == 1
    assert with_source.replace(line, '') == without_source
with_logical = json.loads((root / 'card4_with_cache_attempt02.stdout').read_text().splitlines()[0])['logical']
without_logical = json.loads((root / 'card4_without_cache_attempt02.stdout').read_text().splitlines()[0])['logical']
assert with_logical == without_logical
versions = {name: importlib.metadata.version(name) for name in ['yidl-dataclass', 'astichi', 'yidl']}
assert versions == {'yidl-dataclass': '0.1.0.dev0', 'astichi': '1.1.3', 'yidl': '0.1.0'}
origins = {module.__name__: str(pathlib.Path(module.__file__).resolve()) for module in [yidl_dataclass, astichi, yidl]}
assert all(pathlib.Path(origin).is_relative_to(pathlib.Path(sys.prefix).resolve()) for origin in origins.values())
result = {'checked_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'wheel_sha256': wheel_hash, 'docs_sha256': final, 'versions': versions,
          'public_module_origins': origins,
          'source_manifests_unchanged': True,
          'card4_only_declaration_removed_both_attempts': True,
          'card4_logical_results_identical': True}
(root / 'end-check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
```

## Every captured execution

### 00-public-docs

```json
{
  "label": "00-public-docs",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/read_public_docs.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:03:00.778358+00:00",
  "ended_utc": "2026-10-12T15:03:01.127945+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/read_public_docs.py
```

stdout:

```text
wheel_sha256: 50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b
distribution: yidl-dataclass 0.1.0.dev0
distribution: astichi 1.1.3
distribution: yidl 0.1.0
public_origin: yidl_dataclass external:verification-root/venv-3.12/lib/python3.12/site-packages/yidl_dataclass/__init__.py
public_origin: astichi external:verification-root/venv-3.12/lib/python3.12/site-packages/astichi/__init__.py
public_origin: yidl external:verification-root/venv-3.12/lib/python3.12/site-packages/yidl/__init__.py
sys.prefix: external:verification-root/venv-3.12
sys.path: ['external:python-install/cpython-3.12.12-macos-aarch64-none/lib/python312.zip', 'external:python-install/cpython-3.12.12-macos-aarch64-none/lib/python3.12', 'external:python-install/cpython-3.12-macos-aarch64-none/lib/python3.12/lib-dynload', 'external:verification-root/venv-3.12/lib/python3.12/site-packages']

PUBLIC DOCUMENT: README.md sha256: bca02bb92faec55dc0eba82132ca1371504fd91b1e36e9bfdf698dc0fcf0774a
# YIDL Dataclass

`yidl_dataclass` creates Python dataclasses from modular YIDL templates. Ordinary
fields use direct writable slots by default. Named factories, conversion,
validation, constant and lazy fields add specialized generated methods for the
fields that need them.

This is an unreleased consumer candidate for **CPython 3.12, 3.13 and 3.14**.
Stages A–F are independently verified; public packaging/usability and performance
assessment remain in progress. No speed or memory advantage is claimed.

Install the supplied wheel with the original SDK wheels available locally:

```sh
python -m pip install --no-index --find-links wheelhouse wheelhouse/yidl_dataclass-0.1.0.dev0-py3-none-any.whl
```

The locked runtime dependencies are Astichi 1.1.3 and YIDL 0.1.0. Sibling SDK
checkouts and SDK rebuilds are unnecessary. The wheel contains this README,
public guides and the first-use example under `yidl_dataclass/documentation`.

```python
from yidl_dataclass import dataclass, field, fields, asdict, replace

@dataclass
class Inventory:
    count: int
    label: str = "stock"
    tags: list = field(default_factory=list, compare=False, repr=False)

item = Inventory(3)
item.count = 4
assert asdict(item) == {"count": 4, "label": "stock", "tags": []}
assert not hasattr(item, "__dict__")
assert replace(item, count=5).count == 5
assert [description.name for description in fields(item)] == ["count", "label", "tags"]
```

Run [examples/first_use.py](examples/first_use.py) for the complete introductory
example. The [API guide](docs/API.md) covers defaults, field families, factories,
pipelines, lazy state, inspection, copying, replacement and supported inheritance.
The [generation guide](docs/Generation.md) explains emitted source, packaging,
regeneration and the reusable comparison resource.

The main differences from stdlib dataclasses are slots enabled by default, strict
boolean flags, generated class replacement, no `__post_init__`, hidden InitVars,
field-specific read-only properties, and explicitly excluded writable frozen
caches. Several advanced combinations are rejected rather than silently ignored;
the API guide lists them. Std `Field`, `MISSING`, `InitVar`, `KW_ONLY`, inspection
and data helpers remain interoperable on the documented subset.

Development checks use the original SDK wheels: `python -m pytest -q` and
`python -m yidl_dataclass.regenerate_dataclass_base`. Regeneration checks by
default; `--write` refreshes the base from the packaged authored YIDL resources.
`python -m hatchling build` builds only this consumer. Source compilation/cache
reuse during generation is permitted; no parser-free or wholly Rust execution
claim is made.

The [experiment record](dev-docs/CurrentProgramCheckpoint.md) preserves the
original GO time, scope correction, dependency detour, TDD deviations, independent
reviews and actual evidence. The [active boundary](dev-docs/TaskBoundary.md)
keeps SDKs/Lifecycle reference-only. The authoritative shared comparison resource
is owned here; Undoable consumes it at regeneration time and has no Dataclass
runtime dependency. See [E/F evidence](docs/validation/stage-ef/README.md).


PUBLIC DOCUMENT: docs/API.md sha256: dc56c40a909d3347c75101a6ee2fe77a279bbe36cc146d314f5c115116702512
# Public API and behavior

Import declarations/helpers from `yidl_dataclass`. CPython 3.12–3.14 is supported;
other runtimes/minors fail decoration. An annotation declares a field; it does
not validate its runtime type unless conversion/validation is selected.

## Decorator defaults

```python
dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
          unsafe_hash=False, frozen=False, match_args=True, kw_only=False,
          slots=True, weakref_slot=False, convert=False)
```

All switches require exact booleans. Use `@dataclass` or `@dataclass(...)`.
Decoration returns a generated replacement class with the declaration's bases,
name/module/qualified name and supported methods/attributes. Bind that result as
usual; retain the old declaration only when deliberately inspecting it.
`slots=False` selects dictionary storage. `weakref_slot=True` requires slots.
An existing local custom initializer or `init=False` suppresses ordinary generated
initialization, including factories. A source-free ordinary `field(init=False)`
may remain absent. Policy/frozen/InitVar/local-store/named-provider models require
generated initialization and reject these initializer overrides.

Local custom repr/equality methods follow the std suppression rules. `order=True`
requires equality and rejects conflicting local ordering methods. Hash generation
follows std's equality/frozen/unsafe-hash action table and explicit-hash conflicts:
ordinary equality models are unhashable; frozen equality models normally hash
included fields. `eq=False` normally preserves inherited identity/hash behavior.
`hash=True, compare=False` is rejected. In frozen models, explicitly writable fields must be excluded
from comparison and hashing. `hash=None` with compare=False qualifies; repr=False
is useful for management caches but is not required.

Equality/order require the exact same generated class. Python 3.12 uses tuple
equality; 3.13/3.14 use a self shortcut followed by ordered field comparisons.
Callback order, short-circuiting and raw nonboolean equality results follow that
minor's std behavior. Ordering and hashing use selected field tuples. Repr is
recursive-safe and uses `repr=True` fields; it may evaluate lazy fields.

## Fields and metadata

```python
field(*, default=MISSING, default_factory=MISSING, init=True, repr=True,
      hash=None, compare=True, metadata=None, kw_only=MISSING, doc=None,
      mutable=None, converter=MISSING, validator=None, allow_self_factory=False)
const(**field_options)
lazy(*, default_factory, init=False, **field_options)
initvar(**field_options)
classvar(*, default=MISSING, metadata=None, doc=None)
local_store(*, default=MISSING, default_factory=MISSING, repr=False,
            metadata=None, doc=None, converter=MISSING, validator=None,
            allow_self_factory=False)
```

An ordinary default and factory are mutually exclusive. Mutable unhashable
literal defaults retain std rejection; use a factory. A stdlib `dataclasses.Field`
is accepted and copied, so reusing it across declarations does not share name/type
mutation. Std metadata is a read-only mapping; values remain application objects.
`doc` is accepted only on 3.14 when non-None. `kw_only` inherits the decorator
unless explicit. `KW_ONLY` creates the standard local keyword-only fence.
Unknown keywords and invalid option types fail instead of being ignored.
`match_args=True` selects positional init fields excluding keyword-only fields;
InitVars can appear in that tuple but their hidden attributes cannot satisfy an
attribute pattern. String pseudo-annotations are recognized in their defining
module without arbitrary eval; unresolved annotations can remain metadata when
conversion is disabled.

| Declaration | Constructor and storage | Inspection/operations |
| --- | --- | --- |
| Ordinary annotation/default/`field` | `init=True` by default; writable public slot unless policy needs a property | Included in std fields/helpers; repr/compare/hash flags are local |
| `const` | Read-only after initialization; rejects mutable=True | Standard instance field; included by its flags |
| `lazy` | Factory required; no default; `init=False` by default; init=True accepts an explicit seed | Standard instance field; included operations can trigger its getter |
| `initvar` or `InitVar[T]` | Construction provider, with optional default/factory/init=False | No public attribute, repr/compare/hash/helper entry |
| `classvar` or `ClassVar[T]` | Class storage, no instance pipeline/factory | Std pseudo-field; omitted from fields/helpers and instance operations |
| `local_store` | Eager per-instance management storage, always writable/init=False | Omitted from std fields/helpers/compare/hash; repr=False unless requested |

Convenience InitVars default repr/compare/hash to false and reject explicit
inclusion. Ordinary std Field pseudo-field flags retain their metadata, but kind
still excludes them from instance operations. Contradictory annotations/marker
families fail. Field names `self`/`cls` and generated `_y_dc_` names are reserved.
Private storage is an implementation detail, not a security boundary.

## Named factories and initialization order

Factory signature parameters name providers. For example, a factory named
`def doubled(value): return value * 2` receives the processed `value` field when
assigned to another field's `default_factory`. Declaration order need not place
the provider first. Dependencies form a checked DAG; cycles fail decoration even
when an explicit constructor input might bypass a factory.

Functions, lambdas, callable objects and class factories need an introspectable
signature. The builtins list/dict/set/tuple/int/float/str/bytes/bool are supported as
zero-argument factories. Wrap other nonintrospectable callables. Positional-only,
positional-or-keyword and keyword-only parameters work. Unknown optional
parameters keep their callable defaults; positional default bridging preserves
argument positions. An unknown required parameter or variadic signature fails.
A parameter matching a known field always selects that provider, even if optional;
if its declaration has no available source, decoration reports the dependency
path instead of silently using the callable's default.

`cls` receives `type(self)`. `self` receives the partially initialized instance
only with `allow_self_factory=True`; prefer named providers because their ordering
can be checked. These special providers do not appear as API fields. Eager
consumers materialize a lazy dependency first. Factory/converter/validator calls
happen during construction/access/assignment, not decoration; generation inspects
signatures and captures application objects without serializing or repr-ing them.

For generated initialization, explicit input/default/factory result flows through
conversion, then validation, then storage installation, then dependent consumers.
An ordinary source-free init=False field is legal when nothing consumes it.
Dictionary-mode ordinary init=False simple defaults use class fallback (including
later class-default changes); init=False factories still initialize an instance.
These fallback rules do not bypass a policy pipeline.

## Conversion, validation and mutability

`converter=MISSING` inherits decorator `convert`; `converter=None` explicitly
disables conversion. With `convert=True`, exact int/float/str/bytes/bool annotations
and their one-type nullable unions select that constructor (None is preserved for
nullable conversion). Other/unresolved annotations need an explicit converter or
None. There is no inferred container conversion or runtime annotation validator.
An explicit converter takes one positional candidate.

A validator takes the converted value: None or exact True succeeds, exact False
rejects, and any other result raises a direct TypeError contract error. The same
pipeline applies to permitted assignment; failure leaves the previous value
unchanged. Deleting a mutable eager field leaves it absent until reassignment.
Read-only fields reject replacement/deletion with FrozenInstanceError.

`frozen=True` makes fields read-only through field-specific properties. It is
shallow: mutating a contained object remains possible. A writable cache exception
uses `mutable=True, compare=False, hash=False, repr=False`; local_store already
has those exclusions. Such caches may be assigned/deleted. Freezing does not add a
generic attribute dispatcher. Frozen models require slots=True; unknown slotted
attributes raise ordinary AttributeError rather than std FrozenInstanceError.
Nonfrozen policy models can use slots=False.

## Lazy evaluation, retry and hidden-provider lifetime

A lazy getter has UNREADY/BUSY/READY state. Its first successful read calls its
specialized factory/pipeline and caches the result. Failure returns to UNREADY
for retry; BaseException also clears busy state. Opaque recursive access and a
concurrent second first access raise LazyInitializationError. Concurrent first
access is unsupported, rather than automatically locked.

Delayed factories read current public fields/properties/ClassVars at evaluation
time. A named cycle fails decoration; callbacks must not mutate their provider
model during evaluation. Effective ordinary/lazy mutability is explicit `mutable` when supplied, otherwise
`not frozen`. Select `mutable=False` for a read-only lazy field. `mutable=True`
enables explicit override and reset
(`del instance.lazy_field`); assignment runs its pipeline and marks it ready.
`init=True` accepts an explicit initial seed; omission remains delayed.
Setter/deleter access while that field is BUSY is rejected.

Only InitVars directly needed by delayed consumers receive private retention.
An eager intermediate cuts the retention graph. Failed reads retain providers.
When every nonresettable direct consumer becomes ready, their provider is released;
if any consumer can reset, its provider remains for the instance's lifetime.
Hidden providers never become public fields or helper entries.

## Helpers, replacement and copying

`MISSING`, `Field`, `InitVar`, `KW_ONLY`, `FrozenInstanceError`, `fields`,
`is_dataclass`, `asdict` and `astuple` are stdlib objects/helpers. Data helpers read
public instance fields, including compare=False fields; they evaluate lazy fields
and use their usual recursive copying. They omit InitVars/ClassVars/local storage
and private state. Standard cyclic-graph limitations and getter errors apply.

`storage_fields(model_or_instance)` returns an immutable tuple of descriptions
including extension/provider/local kinds in field order. A description exposes
`name`, `kind.label`, `field` (std metadata), `mutable`, `converter`, `validator`,
`dependencies` and `retained`; it never exposes retained provider values. Treat
`__yidl_dataclass_definition__` as read-only versioned generation metadata.

`replace(obj, /, **changes)` constructs a new model. Existing init=True ordinary/
const fields are read unless changed; init=True lazy fields are also materialized
unless changed. init=False fields, lazy caches and local stores rebuild. Required
init=True InitVars must be supplied again; omitted defaulted/factory InitVars use
the declaration again; init=False InitVars recompute. Hidden retained values are
never replayed. Unknown changes or changes to init=False fields fail.

Std `dataclasses.replace` works when there are no InitVars or every init=True
InitVar is supplied. Its omitted hidden/defaulted InitVar getter behavior is an
unsupported subset; use the package helper. On 3.13/3.14 generated `__replace__`
supports `copy.replace`; a local custom method is preserved. No method is added
on 3.12.

Copy/deepcopy/pickle preserve ready/unready/absent storage, caches/local state and
still-retained providers without evaluating lazy factories. Shallow copy shares
references; deepcopy uses its memo. Copy/pickle while lazy evaluation is active
raises RuntimeError. Pickle uses explicit state, not sentinel identity; normal
module-level class importability is still required. Policy models reject custom
copy/state/reduction hooks that could bypass this contract.

## Inheritance and explicit exclusions

One generated model base plus compatible plain mixins is supported. Fields merge
in reverse-MRO order; overrides retain their position and inherited slots are
reused. Same-shape defaults/factories/pipelines/init/kw-only/repr/compare/hash may
change; field family, storage shape and effective mutability may not. Frozen and
nonfrozen generated models cannot mix. The merged provider graph is rechecked.
Undecorated subclasses receive normal inherited behavior without new metadata.

Generated slotted models reject any base with an instance dictionary. Plain
unslotted bases are permitted with slots=False. Multiple model bases, std-dataclass
bases, manual slots, descriptor-valued field defaults, required subclass-creation
keywords and custom metaclasses are rejected. type/ABCMeta and no-argument subclass
hooks work; abstract-method state is updated. Normal descriptors receive
__set_name__. Copied supported methods/descriptors get fresh __class__ cells for
zero-argument super without mutating the old declaration; class replacement can
repeat a base __init_subclass__ callback.

There is **no `__post_init__` mechanism**: local or inherited hooks are rejected;
use named factories/pipelines. Policy models reject custom __getattribute__,
__setattr__, __delattr__ and bypassing copy/state hooks. Aliases, whole-model
validation, JSON/schema frameworks and arbitrary metaclasses are outside this
release.

## Failure classes

DataclassDefinitionError is a TypeError for declaration/availability/conflict
errors. Factory failures raise FieldInitializationError (RuntimeError), converter
failures FieldConversionError (TypeError), and validator rejection/failure
FieldValidationError (ValueError). Lazy recursion/concurrent access raises
LazyInitializationError (RuntimeError). Diagnostics identify the model/field/role
and known dependency path; original callback exceptions remain causes. Existing
contextual errors propagate without repeated wrapping; BaseException is not
relabeled. Construction/assignment do not roll back application callback side
effects or a self factory leaking a partially initialized instance.


PUBLIC DOCUMENT: docs/Generation.md sha256: bee2d0798b3f66a6f358a62a46cfb2a645cb0c34b5f18e8dd96538a2f77fb624
# Generation, source inspection and distributions

The consumer uses original Astichi 1.1.3 and YIDL 0.1.0. Authored modules live in
`yidl_dataclass/yidl`: core layout/constructor, comparison adapter, factories,
providers, pipelines, policies, lazy initialization/retention and copy support.
Inheritance and matching select only the field-specific contributions needed by
a declaration. The generated user class is plain Python; std dataclass method
generators do not produce its behavior.

Ordinary writable fields have public slots and direct operations. Policy fields
have individual private backing storage and generated bodies. The public property
is assigned from captured builtin property plus its field-specific getter/setter/
deleter functions. This is equivalent descriptor construction to @property and
@field.setter; separated public decorator contributions scoped identifiers
inconsistently on the original Python backend. There is no additional runtime
field access dispatcher. Private builtin captures also protect valid user names
such as property/type/Exception from accidental shadowing.

`generated_source(Model)` exposes the actual generated composition as readable
inspection source. It references a consumer-installed capture namespace and is
not a standalone model module. Defaults, factories/converters/validators and
callable argument defaults remain application objects in that namespace; existing
SDK name/path bindings refer to them. Objects are not supplied to literal SDK
bindings, serialized or repr-ed into source. Fresh decoration owns fresh captures;
shared resource compilation/caches do not share live user values or final classes.

YIDL/Astichi composition is the generation architecture. It does not imply wholly
Rust backend execution or parser-free decoration. Existing source templates may
compile/cache during generation. Both explicit original SDK selections,
`ASTICHI_LOWER_ENGINE=python` and `ASTICHI_LOWER_ENGINE=native-rust`, are verified.
No handwritten dynamic method-source generator or consumer AST repair is used.

Run `python -m yidl_dataclass.regenerate_dataclass_base` from an installed wheel to
check its base against packaged resources; `--write` is for intentional consumer
source maintenance. Stable logical source names make regeneration independent of
checkout/install paths. The wheel and sdist include all authored resources,
compiled Python base, regeneration code and py.typed, plus public documentation
and the introductory example. Rebuilding the wheel from the sdist requires the
same fixed SDK wheels and the build tool, not SDK source/rebuilds.

`yidl/shared/comparison.yidl` is a neutral, reusable native YIDL module. Dataclass
and independently authored consumers inherit its actual equality/order/hash
productions and override read/prelude matching as needed. The Undoable consumer
loads the pinned authoritative Dataclass wheel resource at regeneration time,
checks version and SHA256, and embeds generated resources/provenance in its own
base. It has no hand-maintained shared copy or Dataclass runtime dependency.

Undoable defaults eq=False/order=False. Its logical field compare is boolean,
while managed write_compare=value/identity is separate; legacy compare strings
retain write meaning. Enabled default/current/working views compare selected
exposed values with exact-class guards and are unhashable. During historical
value-write detection only, native bool(old == value) runs on original operands
within its existing ownership fence; an expiring ContextVar marker makes generated
facade equality use historical state identity for that callback scope. Normal
structural equality resumes outside it. Dataclass comparison has no such prelude.
See the Undoable public API for its separate transaction/view contracts.

The experimental candidate is not published. Packaging and correctness evidence
is separate from performance measurements and independent review; source shape
alone proves no speed/memory claim.


PUBLIC DOCUMENT: examples/first_use.py sha256: bf78302fb7ff863f6762a7e9c90fc12117edd9c736d6ee7957ac6c9db28363d0
"""Introductory ordinary-field model; works from an installed consumer wheel."""

from yidl_dataclass import dataclass, field, fields, asdict, replace


@dataclass
class Inventory:
    count: int
    label: str = "stock"
    tags: list = field(default_factory=list, compare=False, repr=False)


def main():
    first = Inventory(3)
    second = Inventory(3)
    first.tags.append("reviewed")
    assert first == second and second.tags == []
    first.count = 4
    assert not hasattr(first, "__dict__")
    assert replace(first, count=5).count == 5
    assert [item.name for item in fields(first)] == ["count", "label", "tags"]
    assert asdict(first) == {"count": 4, "label": "stock", "tags": ["reviewed"]}
    print(
        "ordinary-slots; independent-factories; field-local-comparison; standard-helpers"
    )


if __name__ == "__main__":
    main()

```

stderr (empty block means empty stderr):

```text
```

### 01-public-signatures

```json
{
  "label": "01-public-signatures",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/inspect_public_surface.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:03:10.572306+00:00",
  "ended_utc": "2026-10-12T15:03:10.722001+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/inspect_public_surface.py
```

stdout:

```text
ASTICHI_LOWER_ENGINE: native-rust
astichi public names: ['Composable', 'ComposableDescription', 'ComposableHole', 'GeneratedAstCache', 'TargetAddress', 'ast_provenance', 'asttools', 'build', 'builder', 'cache', 'compile', 'diagnostics', 'frontend', 'hygiene', 'lowering', 'model', 'path_resolution', 'perf_counters', 'shell_refs']
Composable ()
ComposableDescription (holes: 'tuple[ComposableHole, ...]' = (), demand_ports: 'tuple[PortDescriptor, ...]' = (), supply_ports: 'tuple[PortDescriptor, ...]' = (), external_binds: 'tuple[ExternalBindDescriptor, ...]' = (), identifier_demands: 'tuple[IdentifierDemandDescriptor, ...]' = (), identifier_supplies: 'tuple[IdentifierSupplyDescriptor, ...]' = (), productions: 'tuple[ProductionDescriptor, ...]' = ()) -> None
ComposableHole (name: 'str', descriptor: 'HoleDescriptor', address: 'TargetAddress', port: 'PortDescriptor', add_policy: 'AddPolicy', has_default: 'bool' = False, when_empty: 'ClauseEmptyPolicy | None' = None) -> None
GeneratedAstCache (cache_dir: 'str | os.PathLike[str]') -> 'None'
TargetAddress (target_name: 'str', root_instance: 'str | None' = None, ref_path: 'RefPath' = (), leaf_path: 'tuple[int, ...]' = ()) -> None
build () -> 'BuilderHandle'
compile (source: 'str', file_name: 'str | None' = None, line_number: 'int' = 1, offset: 'int' = 0, *, arg_names: 'Mapping[str, str] | None' = None, keep_names: 'Iterable[str] | None' = None, source_kind: 'SourceKind | str' = _AuthoredSource(name='authored')) -> 'Composable'
yidl_dataclass public names: ['DataclassDefinitionError', 'Field', 'FieldConversionError', 'FieldInitializationError', 'FieldValidationError', 'FrozenInstanceError', 'InitVar', 'KW_ONLY', 'LazyInitializationError', 'MISSING', 'asdict', 'astuple', 'classvar', 'const', 'dataclass', 'dataclass_definition', 'dataclass_harvester', 'dataclass_markers', 'errors', 'field', 'field_kinds', 'fields', 'generated_source', 'initvar', 'is_dataclass', 'lazy', 'local_store', 'method_actions', 'policy_plan', 'provider_plan', 'replace', 'retention_plan', 'stdlib_adapter', 'storage_fields']
DataclassDefinitionError signature unavailable
Field (default, default_factory, init, repr, hash, compare, metadata, kw_only)
FieldConversionError signature unavailable
FieldInitializationError signature unavailable
FieldValidationError signature unavailable
FrozenInstanceError signature unavailable
InitVar (type)
LazyInitializationError signature unavailable
asdict (obj, *, dict_factory=<class 'dict'>)
astuple (obj, *, tuple_factory=<class 'tuple'>)
classvar (*, default=<dataclasses._MISSING_TYPE object at 0x103bd5250>, metadata=None, doc=None)
const (**field_options)
dataclass (cls=None, /, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=True, weakref_slot=False, convert=False)
field (*, default=<dataclasses._MISSING_TYPE object at 0x103bd5250>, default_factory=<dataclasses._MISSING_TYPE object at 0x103bd5250>, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=<dataclasses._MISSING_TYPE object at 0x103bd5250>, doc=None, mutable=None, converter=<dataclasses._MISSING_TYPE object at 0x103bd5250>, validator=None, allow_self_factory=False)
fields (class_or_instance)
generated_source (cls)
initvar (**field_options)
is_dataclass (obj)
lazy (*, default_factory, init=False, **field_options)
local_store (*, default=<dataclasses._MISSING_TYPE object at 0x103bd5250>, default_factory=<dataclasses._MISSING_TYPE object at 0x103bd5250>, repr=False, metadata=None, doc=None, converter=<dataclasses._MISSING_TYPE object at 0x103bd5250>, validator=None, allow_self_factory=False)
replace (obj, /, **changes)
storage_fields (class_or_instance)
```

stderr (empty block means empty stderr):

```text
```

### 02-backend-signatures

```json
{
  "label": "02-backend-signatures",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/backend_public_signatures.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:03:19.771467+00:00",
  "ended_utc": "2026-10-12T15:03:19.902192+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/backend_public_signatures.py
```

stdout:

```text
module: astichi.lowering
CALL_CONTEXT public value type: _CallContext
COMMENT public value type: _CommentMarker
DECORATOR_CONTEXT public value type: _DecoratorContext
DEFINITIONAL_CONTEXT public value type: _DefinitionalContext
DOUBLE_STAR_FUNC_ARG_REGION public value type: _DoubleStarFuncArgRegion
DirectiveFuncArgItem (directive_name: 'str', name: 'str', call: 'ast.Call') -> None
DoubleStarFuncArgItem (expr: 'ast.expr') -> None
FuncArgPayload (items: 'tuple[FuncArgPayloadItem, ...]') -> None
FuncArgPayloadItem () -> None
FuncArgRegion ()
IDENTIFIER_CONTEXT public value type: _IdentifierContext
KeywordFuncArgItem (name: 'str', expr: 'ast.expr') -> None
MARKERS_BY_NAME public value type: dict
MarkerContext ()
MarkerSpec ()
PARAMS_PAYLOAD_NAME astichi_params
PLAIN_FUNC_ARG_REGION public value type: _PlainFuncArgRegion
PayloadLocalDirective (spec: 'MarkerSpec', name: 'str') -> None
PortTemplate (shape: 'MarkerShape', mutability: 'PortMutability', origin: 'PortOrigin') -> None
PositionalFuncArgItem (expr: 'ast.expr') -> None
PyImportDeclaration (marker: 'RecognizedMarker', module_path: 'tuple[str, ...] | None', names: 'tuple[ast.Name, ...]', as_name: 'ast.Name | None') -> None
PyImportLocalBinding (marker: 'RecognizedMarker', node: 'ast.Name') -> None
RecognizedMarker (spec: 'MarkerSpec', node: 'ast.AST', context: 'MarkerContext', shape: 'MarkerShape | None' = None) -> None
STARRED_FUNC_ARG_REGION public value type: _StarredFuncArgRegion
StarredFuncArgItem (expr: 'ast.expr') -> None
StatementPrefixScan (body: 'tuple[ast.stmt, ...]', prefix_statements: 'tuple[ast.Expr, ...]', first_non_prefix_index: 'int') -> None
apply_external_bindings (tree: 'ast.Module', bindings: 'dict[str, object]') -> 'None'
apply_external_ref_lowering (tree: 'ast.Module') -> 'None'
boundaries public value type: module
call_argument_payloads public value type: module
collect_payload_local_directives (tree: 'ast.Module') -> 'tuple[PayloadLocalDirective, ...]'
desugar_external_ref_kwargs (tree: 'ast.AST') -> 'None'
direct_funcargs_directive_calls (call: 'ast.Call') -> 'tuple[ast.Call, ...]'
evaluate_restricted_path_expression (node: 'ast.expr') -> 'tuple[str, ...]'
external_bind public value type: module
external_ref public value type: module
extract_dotted_reference_chain (node: 'ast.AST') -> 'tuple[str, ...]'
extract_funcargs_payload (call: 'ast.Call') -> 'FuncArgPayload'
extract_params_payload_from_body (body: 'list[ast.stmt]') -> 'ast.arguments | None'
group_markers_by_astichi_scope (tree: 'ast.Module', markers: 'tuple[RecognizedMarker, ...]') -> 'dict[int, _ScopeMarkers]'
has_params_payload (body: 'list[ast.stmt]') -> 'bool'
is_astichi_funcargs_call (node: 'ast.AST') -> 'bool'
is_astichi_params_def (node: 'ast.AST') -> 'bool'
lower_payload_for_region (payload: 'FuncArgPayload', *, region: 'FuncArgRegion', hole_name: 'str', transform_expr: 'Callable[[ast.expr], ast.expr]') -> 'tuple[list[ast.expr], list[ast.keyword]]'
marker_contexts public value type: module
marker_metadata_name_node_ids (markers: 'Iterable[RecognizedMarker]') -> 'set[int]'
marker_metadata_name_nodes (markers: 'Iterable[RecognizedMarker]') -> 'tuple[ast.Name, ...]'
markers public value type: module
param_hole_name (argument: 'ast.arg') -> 'str | None'
parameters public value type: module
payload_prefix public value type: module
pyimport public value type: module
pyimport_local_bindings (markers: 'tuple[object, ...]') -> 'tuple[PyImportLocalBinding, ...]'
recognize_markers (tree: 'ast.AST') -> 'tuple[RecognizedMarker, ...]'
register_explicit_keyword (name: 'str', seen: 'set[str]') -> 'None'
scan_statement_prefix (body: 'Sequence[ast.stmt]', *, allowed_specs: 'Container[MarkerSpec]') -> 'StatementPrefixScan'
sentinel_attrs public value type: module
validate_boundary_interaction_matrix (tree: 'ast.Module', markers: 'tuple[RecognizedMarker, ...]') -> 'None'
validate_boundary_marker_placement (tree: 'ast.Module') -> 'None'
validate_call_argument_payload_surface (tree: 'ast.Module') -> 'None'
validate_external_ref_surface (tree: 'ast.AST') -> 'None'
validate_parameter_hole_surface (tree: 'ast.Module', markers: 'tuple[RecognizedMarker, ...]') -> 'None'
validate_parameter_payload_surface (tree: 'ast.Module') -> 'None'
validate_payload_for_region (payload: 'FuncArgPayload', *, region: 'FuncArgRegion', hole_name: 'str', seen_explicit_keywords: 'set[str] | None' = None) -> 'None'
validate_pyimport_declarations (tree: 'ast.Module', markers: 'tuple[RecognizedMarker, ...]') -> 'tuple[PyImportDeclaration, ...]'
module: astichi.perf_counters
AstichiPerfCounters (counts: 'Counter[str]' = <factory>, seconds: 'Counter[str]' = <factory>, max_seconds: 'dict[str, float]' = <factory>) -> None
Callable ()
ContextVar signature unavailable
Counter (iterable=None, /, **kwds)
Iterator ()
P public value type: ParamSpec
ParamSpec signature unavailable
T public value type: TypeVar
TypeVar signature unavailable
active_perf_counters () -> 'AstichiPerfCounters | None'
annotations public value type: _Feature
collect_perf_counters () -> 'Iterator[AstichiPerfCounters]'
contextmanager (func)
counted_perf_call (key: 'str') -> 'Callable[[Callable[P, T]], Callable[P, T]]'
dataclass (cls=None, /, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)
field (*, default=<dataclasses._MISSING_TYPE object at 0x102ff93a0>, default_factory=<dataclasses._MISSING_TYPE object at 0x102ff93a0>, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=<dataclasses._MISSING_TYPE object at 0x102ff93a0>)
perf_counter signature unavailable
wraps (wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__', '__type_params__'), updated=('__dict__',))
```

stderr (empty block means empty stderr):

```text
```

### 03-backend-probe

```json
{
  "label": "03-backend-probe",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/backend_probe.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:03:30.465058+00:00",
  "ended_utc": "2026-10-12T15:03:30.884609+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/backend_probe.py
```

stdout:

```text
{"copy_python_ast": 1, "external_literal_payload": 8, "lower_build_selection": 1, "lower_materialization_artifact": 1, "materialize_composable": 1, "native_compile_validate_source": 41, "native_scope_append_occurrence": 1, "native_scope_batch": 20, "native_scope_batch_apply_count": 0, "native_scope_batch_candidate_count": 33, "native_scope_batch_engine": 20, "native_scope_batch_engine_candidate_count": 33, "native_scope_batch_engine_request_count": 32, "native_scope_batch_native_only": 32, "native_scope_batch_size": 32, "yidl_chained_contribution_batches": 7, "yidl_chained_contribution_request_count": 19}
{"copy_python_ast": 0.00164816714823246, "materialize_composable": 1.084059476852417e-06, "native_compile_validate_source": 0.012510835658758879, "native_scope_batch": 0.0038155000656843185}
```

stderr (empty block means empty stderr):

```text
```

### card1_attempt01

```json
{
  "label": "card1_attempt01",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/card1_attempt01.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:05:04.943406+00:00",
  "ended_utc": "2026-10-12T15:05:05.473108+00:00",
  "exit_code": 1
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/card1_attempt01.py
```

stdout:

```text
```

stderr (empty block means empty stderr):

```text
Traceback (most recent call last):
  File "external:public-author/card1_attempt01.py", line 90, in <module>
    main()
  File "external:public-author/card1_attempt01.py", line 63, in main
    assert revised.cache == {} and revised.cache is not quote.cache
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

### card4_with_cache_attempt01

```json
{
  "label": "card4_with_cache_attempt01",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/card4_with_cache_attempt01.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:05:04.943406+00:00",
  "ended_utc": "2026-10-12T15:05:05.452948+00:00",
  "exit_code": 1
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/card4_with_cache_attempt01.py
```

stdout:

```text
{"has_cache": true, "logical": {"different": true, "equal": true, "equal_hashes": true, "ordered": true, "stable_hash": true}}
```

stderr (empty block means empty stderr):

```text
Traceback (most recent call last):
  File "external:public-author/card4_with_cache_attempt01.py", line 36, in <module>
    assert counters.counts['native_scope_batch_native_only'] > 0
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

### card4_without_cache_attempt01

```json
{
  "label": "card4_without_cache_attempt01",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/card4_without_cache_attempt01.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:05:04.943410+00:00",
  "ended_utc": "2026-10-12T15:05:05.451815+00:00",
  "exit_code": 1
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/card4_without_cache_attempt01.py
```

stdout:

```text
{"has_cache": false, "logical": {"different": true, "equal": true, "equal_hashes": true, "ordered": true, "stable_hash": true}}
```

stderr (empty block means empty stderr):

```text
Traceback (most recent call last):
  File "external:public-author/card4_without_cache_attempt01.py", line 35, in <module>
    assert counters.counts['native_scope_batch_native_only'] > 0
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

### card2_attempt01

```json
{
  "label": "card2_attempt01",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/card2_attempt01.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:05:04.943841+00:00",
  "ended_utc": "2026-10-12T15:05:05.436016+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/card2_attempt01.py
```

stdout:

```text
{"construction": [[null, 4.8], [4, 4.8]], "after_assignment": [[4, 4.8], [null, 7.9]]}
backend_counts: {"copy_python_ast": 1, "external_literal_payload": 24, "lower_build_selection": 1, "lower_materialization_artifact": 1, "materialize_composable": 1, "native_compile_validate_source": 55, "native_scope_append_occurrence": 1, "native_scope_batch": 52, "native_scope_batch_apply_count": 0, "native_scope_batch_candidate_count": 127, "native_scope_batch_engine": 52, "native_scope_batch_engine_candidate_count": 127, "native_scope_batch_engine_request_count": 100, "native_scope_batch_native_only": 100, "native_scope_batch_size": 100, "yidl_chained_contribution_batches": 21, "yidl_chained_contribution_request_count": 69}
```

stderr (empty block means empty stderr):

```text
```

### card3_attempt01

```json
{
  "label": "card3_attempt01",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/card3_attempt01.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:05:04.944094+00:00",
  "ended_utc": "2026-10-12T15:05:05.432059+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/card3_attempt01.py
```

stdout:

```text
{"base_slots": ["value", "mode"], "child_slots": ["extra"], "field_order": ["value", "mode", "extra"], "required_keyword_failures": [{"case": "omitted required keyword", "message": "Child.__init__() missing 1 required keyword-only argument: 'mode'"}, {"case": "keyword passed positionally", "message": "Child.__init__() takes from 2 to 3 positional arguments but 4 were given"}], "reused_public_descriptor": true, "signature": "(value: int, extra: int = 7, *, mode: str) -> None", "super_result": "1:updated:child=7"}
backend_counts: {"copy_python_ast": 2, "external_literal_payload": 31, "lower_build_selection": 2, "lower_materialization_artifact": 2, "materialize_composable": 2, "native_compile_validate_source": 44, "native_scope_append_occurrence": 2, "native_scope_batch": 55, "native_scope_batch_apply_count": 0, "native_scope_batch_candidate_count": 110, "native_scope_batch_engine": 55, "native_scope_batch_engine_candidate_count": 110, "native_scope_batch_engine_request_count": 105, "native_scope_batch_native_only": 105, "native_scope_batch_size": 105, "yidl_chained_contribution_batches": 29, "yidl_chained_contribution_request_count": 79}
```

stderr (empty block means empty stderr):

```text
```

### card4_with_cache_attempt02

```json
{
  "label": "card4_with_cache_attempt02",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/card4_with_cache_attempt02.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:05:37.179051+00:00",
  "ended_utc": "2026-10-12T15:05:37.586395+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/card4_with_cache_attempt02.py
```

stdout:

```text
{"has_cache": true, "logical": {"different": true, "equal": true, "equal_hashes": true, "ordered": true, "stable_hash": true}}
backend_counts: {"copy_python_ast": 1, "external_literal_payload": 28, "lower_build_selection": 1, "lower_materialization_artifact": 1, "materialize_composable": 1, "native_compile_validate_source": 68, "native_scope_append_occurrence": 1, "native_scope_batch": 59, "native_scope_batch_apply_count": 0, "native_scope_batch_candidate_count": 125, "native_scope_batch_engine": 59, "native_scope_batch_engine_candidate_count": 125, "native_scope_batch_engine_request_count": 106, "native_scope_batch_native_only": 106, "native_scope_batch_size": 106, "yidl_chained_contribution_batches": 25, "yidl_chained_contribution_request_count": 72}
```

stderr (empty block means empty stderr):

```text
```

### card4_without_cache_attempt02

```json
{
  "label": "card4_without_cache_attempt02",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/card4_without_cache_attempt02.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:05:37.179052+00:00",
  "ended_utc": "2026-10-12T15:05:37.584282+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/card4_without_cache_attempt02.py
```

stdout:

```text
{"has_cache": false, "logical": {"different": true, "equal": true, "equal_hashes": true, "ordered": true, "stable_hash": true}}
backend_counts: {"copy_python_ast": 1, "external_literal_payload": 22, "lower_build_selection": 1, "lower_materialization_artifact": 1, "materialize_composable": 1, "native_compile_validate_source": 66, "native_scope_append_occurrence": 1, "native_scope_batch": 52, "native_scope_batch_apply_count": 0, "native_scope_batch_candidate_count": 99, "native_scope_batch_engine": 52, "native_scope_batch_engine_candidate_count": 99, "native_scope_batch_engine_request_count": 88, "native_scope_batch_native_only": 88, "native_scope_batch_size": 88, "yidl_chained_contribution_batches": 21, "yidl_chained_contribution_request_count": 57}
```

stderr (empty block means empty stderr):

```text
```

### card1_attempt02

```json
{
  "label": "card1_attempt02",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/card1_attempt02.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:05:37.179355+00:00",
  "ended_utc": "2026-10-12T15:05:37.606343+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/card1_attempt02.py
```

stdout:

```text
{"cache": {"entry": 3, "replacement": 2}, "hash_unchanged": true, "logical_equality_after_cache_change": true, "public_fields": ["quantity", "unit_price", "total", "cache", "receipt"], "quantity": 2, "receipt_cached": "en-NZ: total=10", "receipt_calls": [["en-NZ", 10], ["en-AU", 15]], "receipt_first": "en-NZ: total=10", "replacement_quantity": 3, "replacement_receipt": "en-AU: total=15", "replacement_total": 15, "storage_metadata": [{"dependencies": [], "kind": "ordinary", "mutable": false, "name": "quantity", "retained": false}, {"dependencies": [], "kind": "ordinary", "mutable": false, "name": "unit_price", "retained": false}, {"dependencies": ["quantity", "unit_price"], "kind": "const", "mutable": false, "name": "total", "retained": false}, {"dependencies": [], "kind": "ordinary", "mutable": true, "name": "cache", "retained": false}, {"dependencies": [], "kind": "initvar", "mutable": false, "name": "locale", "retained": true}, {"dependencies": ["locale", "total"], "kind": "lazy", "mutable": false, "name": "receipt", "retained": false}], "total": 10, "unit_price": 5}
backend_counts: {"copy_python_ast": 1, "external_literal_payload": 72, "lower_build_selection": 1, "lower_materialization_artifact": 1, "materialize_composable": 1, "native_compile_validate_source": 73, "native_scope_append_occurrence": 1, "native_scope_batch": 111, "native_scope_batch_apply_count": 0, "native_scope_batch_candidate_count": 350, "native_scope_batch_engine": 111, "native_scope_batch_engine_candidate_count": 350, "native_scope_batch_engine_request_count": 270, "native_scope_batch_native_only": 270, "native_scope_batch_size": 270, "yidl_chained_contribution_batches": 66, "yidl_chained_contribution_request_count": 225}
```

stderr (empty block means empty stderr):

```text
```

### 99-end-check

```json
{
  "label": "99-end-check",
  "command": [
    "env",
    "ASTICHI_LOWER_ENGINE=native-rust",
    "external:verification-root/venv-3.12/bin/python",
    "-I",
    "external:public-author/end_check.py"
  ],
  "cwd": "external:public-author",
  "started_utc": "2026-10-12T15:06:10.896493+00:00",
  "ended_utc": "2026-10-12T15:06:11.231147+00:00",
  "exit_code": 0
}
```

Exact shell rendering of captured argument vector:

```sh
env ASTICHI_LOWER_ENGINE=native-rust external:verification-root/venv-3.12/bin/python -I external:public-author/end_check.py
```

stdout:

```text
{
  "checked_utc": "2026-10-12T15:06:11.190353+00:00",
  "wheel_sha256": "50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b",
  "docs_sha256": {
    "README.md": "bca02bb92faec55dc0eba82132ca1371504fd91b1e36e9bfdf698dc0fcf0774a",
    "docs/API.md": "dc56c40a909d3347c75101a6ee2fe77a279bbe36cc146d314f5c115116702512",
    "docs/Generation.md": "bee2d0798b3f66a6f358a62a46cfb2a645cb0c34b5f18e8dd96538a2f77fb624",
    "examples/first_use.py": "bf78302fb7ff863f6762a7e9c90fc12117edd9c736d6ee7957ac6c9db28363d0"
  },
  "versions": {
    "yidl-dataclass": "0.1.0.dev0",
    "astichi": "1.1.3",
    "yidl": "0.1.0"
  },
  "public_module_origins": {
    "yidl_dataclass": "external:verification-root/venv-3.12/lib/python3.12/site-packages/yidl_dataclass/__init__.py",
    "astichi": "external:verification-root/venv-3.12/lib/python3.12/site-packages/astichi/__init__.py",
    "yidl": "external:verification-root/venv-3.12/lib/python3.12/site-packages/yidl/__init__.py"
  },
  "source_manifests_unchanged": true,
  "card4_only_declaration_removed_both_attempts": true,
  "card4_logical_results_identical": true
}
```

stderr (empty block means empty stderr):

```text
```

## Artifact inventory


- 00-public-docs.execution.json
- 00-public-docs.stderr
- 00-public-docs.stdout
- 01-public-signatures.execution.json
- 01-public-signatures.stderr
- 01-public-signatures.stdout
- 02-backend-signatures.execution.json
- 02-backend-signatures.stderr
- 02-backend-signatures.stdout
- 03-backend-probe.execution.json
- 03-backend-probe.stderr
- 03-backend-probe.stdout
- 99-end-check.execution.json
- 99-end-check.stderr
- 99-end-check.stdout
- assemble_record.py
- author-metadata.json
- backend_probe.py
- backend_public_signatures.py
- card1_attempt01.execution.json
- card1_attempt01.py
- card1_attempt01.stderr
- card1_attempt01.stdout
- card1_attempt02.execution.json
- card1_attempt02.py
- card1_attempt02.stderr
- card1_attempt02.stdout
- card2_attempt01.execution.json
- card2_attempt01.py
- card2_attempt01.stderr
- card2_attempt01.stdout
- card3_attempt01.execution.json
- card3_attempt01.py
- card3_attempt01.stderr
- card3_attempt01.stdout
- card4-declaration-removal.json
- card4_with_cache_attempt01.execution.json
- card4_with_cache_attempt01.py
- card4_with_cache_attempt01.stderr
- card4_with_cache_attempt01.stdout
- card4_with_cache_attempt02.execution.json
- card4_with_cache_attempt02.py
- card4_with_cache_attempt02.stderr
- card4_with_cache_attempt02.stdout
- card4_without_cache_attempt01.execution.json
- card4_without_cache_attempt01.py
- card4_without_cache_attempt01.stderr
- card4_without_cache_attempt01.stdout
- card4_without_cache_attempt02.execution.json
- card4_without_cache_attempt02.py
- card4_without_cache_attempt02.stderr
- card4_without_cache_attempt02.stdout
- end-check.json
- end_check.py
- first-attempt-manifest.json
- inspect_public_surface.py
- public-docs/README.md
- public-docs/docs/API.md
- public-docs/docs/Generation.md
- public-docs/examples/first_use.py
- read_public_docs.py
- repair-attempt-manifest.json
- repairs.json
- run_record.py
- start-doc-hashes.json


The standalone record is AUTHORING_RECORD.md. All raw .execution.json/.stdout/.stderr files and exact first/repaired source files remain beside it. No product defect or implementation verdict is inferred from the author corrections.
