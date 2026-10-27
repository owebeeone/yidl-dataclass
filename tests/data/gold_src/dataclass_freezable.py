"""Acceptance fixture for the agreed optimistic runtime-freeze extension.

Intentionally red until freezable=True and field(freeze=...) are implemented.
Generated-source goldens must be captured and reviewed after implementation.
"""

from dataclasses import FrozenInstanceError
from types import MappingProxyType

from yidl_dataclass import dataclass, field, generated_source


def render_case():
    calls = []

    def freeze_children(value):
        calls.append("children")
        for child in value.values():
            child.freeze()
        return MappingProxyType(dict(value))

    @dataclass(freezable=True)
    class Scope:
        name: str
        children: object = field(default_factory=dict, freeze=freeze_children)

    parent = Scope("root")
    child = Scope("child")
    parent.children["child"] = child
    child.children["parent"] = parent
    retained_container = parent.children
    parent.name = "edited"
    parent.freeze()
    parent.freeze()
    assert calls == ["children", "children"]
    assert parent.children["child"] is child
    assert child.children["parent"] is parent
    retained_container.clear()
    assert parent.children["child"] is child
    assert not hasattr(parent, "__dict__")
    for instance in (parent, child):
        try:
            instance.name = "bad"
        except FrozenInstanceError:
            pass
        else:
            raise AssertionError("assignment accepted after freezing")
        try:
            del instance.children
        except FrozenInstanceError:
            pass
        else:
            raise AssertionError("deletion accepted after freezing")
        try:
            instance.children["bad"] = child
        except TypeError:
            pass
        else:
            raise AssertionError("frozen container accepted mutation")
    return {
        "generated_output.py": generated_source(Scope),
        "behavior.txt": (
            "mutable-before=True; permanent-after=True; hook-one-value=True; "
            "cascade=True; cycle=True; repeat-noop=True; retained-container-safe=True\n"
        ),
    }
