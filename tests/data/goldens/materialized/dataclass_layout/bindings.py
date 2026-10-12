"""Layout and suppressed-init contracts against independent std declarations."""

import dataclasses as std
import inspect
import weakref
from yidl_dataclass import dataclass, field, generated_source, KW_ONLY


def missing_factory(required):
    raise AssertionError("suppressed factory must never execute")


def layouts(decorator, make_field):
    @decorator(eq=False, repr=False, slots=False)
    class Dictionary:
        value: int = make_field(init=False, default=4)

    @decorator(eq=False, repr=False, slots=True, init=False)
    class AssignedLater:
        value: int = make_field(init=False)
        pending: object = make_field(default_factory=missing_factory)

    @decorator(eq=False, repr=False, slots=True)
    class Custom:
        value: int = make_field(init=False)

        def __init__(self, value):
            self.value = value

    @decorator(eq=False, repr=False, slots=True)
    class Unconsumed:
        value: int = make_field(init=False)

    @decorator(eq=False, repr=False, slots=True, weakref_slot=True)
    class Keywords:
        first: int
        fence: KW_ONLY
        later: int
        optional: str = "default"

    return Dictionary, AssignedLater, Custom, Unconsumed, Keywords


def observation(classes):
    Dictionary, AssignedLater, Custom, Unconsumed, Keywords = classes
    d = Dictionary()
    assert d.__dict__ == {}
    first = d.value
    Dictionary.value = 10
    later = d.value
    assigned = AssignedLater()
    assert not hasattr(assigned, "value") and not hasattr(assigned, "pending")
    assigned.value = 3
    custom = Custom(7)
    unconsumed = Unconsumed()
    assert not hasattr(unconsumed, "value")
    keyword = Keywords(2, later=6)
    assert weakref.ref(keyword)() is keyword
    return (
        first,
        later,
        assigned.value,
        custom.value,
        str(inspect.signature(Keywords)),
        Keywords.__match_args__,
        (keyword.first, keyword.later, keyword.optional),
    )


def render_case():
    class SlottedDeclaration:
        value: int

    class DictionaryDeclaration:
        value: int

    assert dataclass(SlottedDeclaration) is not SlottedDeclaration
    assert dataclass(DictionaryDeclaration, slots=False) is DictionaryDeclaration
    assert "__dataclass_fields__" in DictionaryDeclaration.__dict__
    actual = layouts(dataclass, field)
    reference = layouts(std.dataclass, std.field)
    assert observation(actual) == observation(reference)
    return {
        "generated_output.py": "\n".join(generated_source(cls) for cls in actual),
        "behavior.txt": str(observation(layouts(dataclass, field)))
        + "\nslotted-replacement=True; dictionary-identity-and-metadata=True\n",
    }
