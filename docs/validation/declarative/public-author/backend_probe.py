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
