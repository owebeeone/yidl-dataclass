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
