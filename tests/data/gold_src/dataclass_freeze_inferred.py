"""Typed-child inference uses YIDL metadata, with explicit field overrides."""

from dataclasses import FrozenInstanceError
from yidl_dataclass import dataclass, field, generated_source


def render_case():
    @dataclass(freezable=True)
    class Child:
        value: int

    @dataclass(freezable=True)
    class Parent:
        child: Child

    child = Child(1)
    parent = Parent(child)
    child.value = 2
    parent.freeze()
    assert parent.child is child
    try:
        child.value = 3
    except FrozenInstanceError:
        pass
    else:
        raise AssertionError("typed child was not frozen")

    events = []

    def explicit(value):
        events.append(value.value)
        return value

    @dataclass(freezable=True)
    class Explicit:
        child: Child = field(freeze=explicit)

    supplied = Child(4)
    Explicit(supplied).freeze()
    supplied.value = 5
    assert events == [4]
    return {
        "generated_output.py": "\n".join(
            generated_source(model) for model in (Child, Parent, Explicit)
        ),
        "behavior.txt": (
            "metadata-inferred=True; same-child=True; explicit-hook-wins=True\n"
        ),
    }
