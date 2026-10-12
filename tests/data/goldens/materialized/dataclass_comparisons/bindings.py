"""Rich logical/storage contrast, standard method oracle, and field deletion."""

import dataclasses as std
from typing import ClassVar
from yidl_dataclass import dataclass, field, generated_source


def models(decorator, make_field):
    @decorator(order=True, unsafe_hash=True, slots=True)
    class Quote:
        sku: str
        price: int
        currency: str = "AUD"
        tags: tuple = make_field(default=(), hash=False)
        note: str = make_field(default="", compare=False)
        cache: dict = make_field(
            default_factory=dict, compare=False, hash=False, repr=False
        )
        audit: int = make_field(default=0, compare=False, repr=False)
        category: ClassVar[str] = "quote"

    @decorator(order=True, unsafe_hash=True, slots=True)
    class Removed:
        sku: str
        price: int
        currency: str = "AUD"
        tags: tuple = make_field(default=(), hash=False)
        note: str = make_field(default="", compare=False)
        category: ClassVar[str] = "quote"

    @decorator(order=True, unsafe_hash=True, slots=True)
    class Excluded:
        visible: int = make_field(default=1, compare=False)
        hidden: str = make_field(default="hidden", compare=False, repr=False)

    @decorator(slots=True)
    class Unhashable:
        value: int

    return Quote, Removed, Excluded, Unhashable


def observation(classes):
    Quote, Removed, Excluded, Unhashable = classes
    first = Quote("item", 100, note="first", audit=1)
    same = Quote("item", 100, note="second", audit=9)
    later = Quote("item", 101)
    tags = Quote("item", 100, tags=("changed",))
    first.cache["cached"] = 8
    return {
        "repr": repr(first),
        "eq": (first == same, first == later, first == tags),
        "order": (first < later, first <= same, later > first, later >= first),
        "hash": (hash(first) == hash(same), hash(first) == hash(tags)),
        "exact": Quote.__eq__(first, Removed("item", 100)) is NotImplemented,
        "excluded": (
            Excluded(1) == Excluded(8),
            Excluded(1) < Excluded(8),
            hash(Excluded()) == hash(()),
            repr(Excluded()),
        ),
        "unhashable": Unhashable.__hash__ is None,
        "deleted": "cache" not in Removed.__dataclass_fields__
        and "audit" not in Removed.__dataclass_fields__,
    }


def render_case():
    actual = models(dataclass, field)
    reference = models(std.dataclass, std.field)
    assert observation(actual) == observation(reference)
    deleted = generated_source(actual[1])
    assert "cache" not in deleted and "audit" not in deleted
    return {
        "generated_output.py": "\n".join(generated_source(cls) for cls in actual),
        "behavior.txt": str(observation(actual)) + "\n",
    }
