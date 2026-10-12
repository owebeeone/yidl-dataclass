"""Specialized pipelines, atomic assignments and read-only/frozen cache contrast."""

from dataclasses import asdict, FrozenInstanceError
from yidl_dataclass import (
    dataclass,
    field,
    const,
    local_store,
    generated_source,
    FieldValidationError,
)


def render_case():
    events = []

    def convert_units(value):
        events.append(("convert", value))
        return int(value)

    def positive(value):
        events.append(("validate", value))
        return value >= 0

    @dataclass
    class Processed:
        total: int = field(init=False, default_factory=lambda units: units * 3)
        units: int = field(default="2", converter=convert_units, validator=positive)
        token: int = const(default=4)
        management: list = local_store(default_factory=lambda units: [units])

    assert events == []
    first = Processed()
    assert (first.units, first.total, first.management) == (2, 6, [2])
    first.units = "5"
    assert first.units == 5 and first.total == 6
    try:
        first.units = "-2"
    except FieldValidationError:
        pass
    else:
        raise AssertionError("negative accepted")
    assert first.units == 5
    del first.units
    assert not hasattr(first, "units")
    first.units = "9"
    assert first.units == 9
    try:
        first.token = 8
    except FrozenInstanceError:
        pass
    else:
        raise AssertionError("const replaced")

    @dataclass(frozen=True)
    class Frozen:
        amount: int
        cache: dict = field(
            default_factory=dict, mutable=True, compare=False, hash=False, repr=False
        )
        management: list = local_store(default_factory=list)

    immutable = Frozen(7)
    immutable.cache = {"count": 3}
    immutable.management.append("work")
    assert hash(immutable) == hash((7,))
    assert asdict(immutable) == {"amount": 7, "cache": {"count": 3}}
    try:
        del immutable.amount
    except FrozenInstanceError:
        pass
    else:
        raise AssertionError("frozen deleted")
    assert isinstance(Processed.__dict__["units"], property)
    assert isinstance(Processed.__dict__["token"], property)
    assert not isinstance(Frozen.__dict__["cache"], property)
    assert not hasattr(immutable, "__dict__")
    return {
        "generated_output.py": generated_source(Processed)
        + "\n"
        + generated_source(Frozen),
        "behavior.txt": str(events)
        + "\nconverted-provider-total=6; assignment-atomic=True; mutable-delete=True; const=True; frozen-hash=amount; writable-cache=True; local-excluded=True\n",
    }
