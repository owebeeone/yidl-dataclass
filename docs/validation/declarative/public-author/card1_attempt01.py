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
