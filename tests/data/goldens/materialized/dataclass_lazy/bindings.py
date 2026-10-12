"""Test-first lazy cache, seeding, direct current providers and eager consumer."""

from yidl_dataclass import (
    dataclass,
    field,
    lazy,
    classvar,
    generated_source,
    FrozenInstanceError,
)


def render_case():
    events = []

    def make_total(units, rate, cls):
        events.append(("total", units, rate, cls.__name__))
        return units * rate

    def make_cache(units):
        events.append(("cache", units))
        return str(units + 1)

    @dataclass(repr=False)
    class Lazy:
        units: int = 2
        rate: int = classvar(default=3)
        total: int = lazy(default_factory=make_total, mutable=False)
        cache: int = lazy(
            default_factory=make_cache,
            converter=int,
            validator=lambda value: value > 0,
            compare=False,
        )
        seeded: int = lazy(
            default_factory=lambda units: units * 10, init=True, compare=False
        )

    assert events == []
    first = Lazy(seeded=99)
    assert events == [] and first.seeded == 99
    first.units = 4
    Lazy.rate = 5
    assert first.total == 20 and first.total == 20
    assert first.cache == 5
    first.units = 8
    assert first.total == 20 and first.cache == 5
    del first.cache
    assert first.cache == 9
    first.cache = "40"
    assert first.cache == 40
    try:
        first.total = 1
    except FrozenInstanceError:
        pass
    else:
        raise AssertionError("immutable lazy replaced")

    @dataclass(repr=False)
    class Eager:
        result: int = field(init=False, default_factory=lambda delayed: delayed + 1)
        delayed: int = lazy(default_factory=lambda base: base * 2, mutable=False)
        base: int = 4

    eager = Eager()
    assert eager.result == 9 and eager.delayed == 8
    assert not hasattr(first, "__dict__")
    return {
        "generated_output.py": generated_source(Lazy) + "\n" + generated_source(Eager),
        "behavior.txt": str(events)
        + "\nseeded=99; immutable-cache=20; reset-current=9; eager-lazy=9; slots=True\n",
    }
