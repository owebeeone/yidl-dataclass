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
