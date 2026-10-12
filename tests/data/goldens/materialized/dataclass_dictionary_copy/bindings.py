"""Post-GREEN verification: dictionary absence/cache and unrelated attributes."""

import copy
from yidl_dataclass import (
    dataclass,
    field,
    initvar,
    lazy,
    generated_source,
    storage_fields,
)


def render_case():
    calls = []

    @dataclass(slots=False, repr=False)
    class Dictionary:
        seed: int = initvar(default=3)
        source: int = field(init=False, default=7)
        first: int = lazy(
            default_factory=lambda source: calls.append("first") or source * 2,
            mutable=False,
        )
        second: int = lazy(
            default_factory=lambda seed: calls.append("second") or seed, compare=False
        )

    first = Dictionary()
    first.extra = ["custom"]
    shallow = copy.copy(first)
    deep = copy.deepcopy(first)
    assert (
        calls == []
        and "source" not in shallow.__dict__
        and "source" not in deep.__dict__
    )
    assert (
        shallow.extra is first.extra
        and deep.extra == first.extra
        and deep.extra is not first.extra
    )
    assert shallow.first == 14 and shallow.second == 3
    Dictionary.source = 9
    assert deep.first == 18
    assert first.first == 18
    provider = storage_fields(Dictionary)[0].provider_name
    assert hasattr(deep, provider) and not hasattr(deep, "seed")
    return {
        "generated_output.py": generated_source(Dictionary),
        "behavior.txt": str(calls)
        + "\ndictionary-absence=True; unrelated-attrs=True; unready-no-callback=True; fallback-current=True; hidden-provider-copied=True\n",
    }
