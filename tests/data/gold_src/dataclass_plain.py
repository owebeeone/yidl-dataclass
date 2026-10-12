"""Canonical direct-storage and constructor contrast; no comparison/repr yet."""

from inspect import signature
from yidl_dataclass import dataclass, generated_source


def render_case():
    @dataclass(eq=False, repr=False)
    class Inventory:
        count: int
        label: str = "stock"
        reserve: int = 2

    assert Inventory.__slots__ == ("count", "label", "reserve")
    first = Inventory(3)
    second = Inventory(8, "custom", 5)
    third = Inventory(count=0, reserve=9)
    assert not hasattr(first, "__dict__")
    first.count = 4
    assert (first.count, first.label, first.reserve) == (4, "stock", 2)
    assert (second.count, second.label, second.reserve) == (8, "custom", 5)
    assert (third.count, third.label, third.reserve) == (0, "stock", 9)

    class SharedSlot:
        __slots__ = ("inherited",)

    class Declaration(SharedSlot):
        inherited: int
        units: int = 6

    Replacement = dataclass(Declaration, eq=False, repr=False)
    assert Replacement.__bases__ == (SharedSlot,)
    assert Declaration not in Replacement.__mro__
    assert Replacement.__slots__ == ("units",)
    inherited = Replacement(12)
    assert (inherited.inherited, inherited.units) == (12, 6)
    assert not hasattr(inherited, "__dict__")
    return {
        "generated_output.py": generated_source(Inventory)
        + "\n"
        + generated_source(Replacement),
        "behavior.txt": "\n".join(
            (
                "slots=count,label,reserve; instance-dict=False",
                str(signature(Inventory)),
                "first=4,stock,2; second=8,custom,5; third=0,stock,9",
                "replacement-bases=SharedSlot; declaration-base=False; inherited=12; units=6",
            )
        )
        + "\n",
    }
