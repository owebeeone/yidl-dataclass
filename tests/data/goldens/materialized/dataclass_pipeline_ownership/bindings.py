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

    first_default, second_default = Hostile(), Hostile()

    def declare(converter, default):
        class Owned:
            value: int = field(default="2", converter=converter)
            untouched: object = field(default=default, repr=False, compare=False)

        return dataclass(Owned)

    first = declare(Convert(1), first_default)
    second = declare(Convert(10), second_default)
    assert events == []
    assert generated_source(first) == generated_source(second)
    a, b = first(), second()
    assert (a.value, b.value) == (3, 12)
    a.value = "4"
    assert (a.value, b.value) == (5, 12)
    assert a.untouched is first_default and b.untouched is second_default
    assert first is not second

    @dataclass
    class Different:
        quantity: int = field(default_factory=lambda: 7)

    assert Different().quantity == 7
    assert "quantity" in generated_source(Different)

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
        + generated_source(Different)
        + "\n"
        + generated_source(Removed)
        + "\n"
        + generated_source(Fallback),
        "behavior.txt": str(events)
        + "\nnamespace-owned=True; distinct-defaults=True; distinct-final-classes=True; differing-field-name=True; stable-shape=True; no-repr-generation=True; policy-deleted=True; dictionary-fallback=9; absent-unset=True\n",
    }
