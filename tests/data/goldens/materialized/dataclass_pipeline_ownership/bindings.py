"""Post-GREEN verification: namespace captures, fallback and policy deletion."""

from yidl_dataclass import dataclass, field, generated_source


def render_case():
    events = []

    class Hostile:
        def __repr__(self):
            raise AssertionError("default repr executed")

    class Convert:
        def __init__(self, offset):
            self.offset = offset

        def __repr__(self):
            raise AssertionError("callback repr executed")

        def __call__(self, value):
            events.append((self.offset, value))
            return int(value) + self.offset

    default = Hostile()

    def declare(converter):
        class Owned:
            value: int = field(default="2", converter=converter)
            untouched: object = field(default=default, repr=False, compare=False)

        return dataclass(Owned)

    first, second = declare(Convert(1)), declare(Convert(10))
    assert events == []
    assert generated_source(first) == generated_source(second)
    a, b = first(), second()
    assert (a.value, b.value) == (3, 12)
    a.value = "4"
    assert (a.value, b.value) == (5, 12)
    assert a.untouched is default and b.untouched is default

    @dataclass
    class Removed:
        value: int = 2

    removed = Removed()
    removed.value = "unconverted"
    assert removed.value == "unconverted"
    assert not isinstance(Removed.__dict__["value"], property)

    @dataclass(slots=False)
    class Fallback:
        result: int = field(init=False, default_factory=lambda source: source * 2)
        source: int = field(init=False, default=7)
        absent: int = field(init=False, repr=False, compare=False)

    Fallback.source = 9
    fallback = Fallback()
    assert fallback.source == 9 and fallback.result == 18
    assert "source" not in fallback.__dict__ and not hasattr(fallback, "absent")
    return {
        "generated_output.py": generated_source(first)
        + "\n"
        + generated_source(second)
        + "\n"
        + generated_source(Removed)
        + "\n"
        + generated_source(Fallback),
        "behavior.txt": str(events)
        + "\nnamespace-owned=True; stable-shape=True; no-repr-generation=True; policy-deleted=True; dictionary-fallback=9; absent-unset=True\n",
    }
