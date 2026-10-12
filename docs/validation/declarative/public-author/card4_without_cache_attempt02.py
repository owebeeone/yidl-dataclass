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
