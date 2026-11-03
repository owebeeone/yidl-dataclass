"""Configurable method names preserve ordinary field names and child policy."""

from dataclasses import FrozenInstanceError
from functools import partial
import pytest
from yidl_dataclass import dataclass, lazy, replace, DataclassDefinitionError


def test_custom_name_frees_the_default_name_for_a_field():
    @dataclass(freezable=True, freeze_method="_taut_freeze")
    class Record:
        freeze: int

    value = Record(1)
    value.freeze = 2
    value._taut_freeze()
    value._taut_freeze()
    assert value.freeze == 2
    with pytest.raises(FrozenInstanceError):
        value.freeze = 3
    with pytest.raises(FrozenInstanceError):
        del value.freeze


def test_inferred_children_use_their_own_configured_name_including_lazy():
    @dataclass(freezable=True, freeze_method="seal")
    class Child:
        freeze: int

    @dataclass(freezable=True, freeze_method="finish")
    class Parent:
        child: Child
        delayed: Child = lazy(default_factory=lambda: Child(2))

    value = Parent(Child(1))
    value.finish()
    assert not hasattr(value, "freeze")
    for child in (value.child, value.delayed):
        with pytest.raises(FrozenInstanceError):
            child.freeze = 3


def test_shared_configured_decorator_and_consistent_inheritance():
    record = partial(dataclass, freezable=True, freeze_method="_taut_freeze")

    @record
    class Base:
        freeze: int

    @record
    class Derived(Base):
        more: int

    value = Derived(1, 2)
    value._taut_freeze()
    with pytest.raises(FrozenInstanceError):
        value.more = 3
    revision = replace(value, freeze=4)
    revision.more = 5
    assert (revision.freeze, revision.more) == (4, 5)
    with pytest.raises(DataclassDefinitionError, match="freeze_method"):
        dataclass(
            type("Different", (Base,), {"__annotations__": {"extra": int}}),
            freezable=True,
        )


@pytest.mark.parametrize(
    "name",
    [None, False, 1, "", "a.b", "a-b", "class", "__init__", "__repr__", "_y_dc_frozen"],
)
def test_invalid_names_fail_at_decoration(name):
    with pytest.raises(DataclassDefinitionError, match="freeze_method"):
        dataclass(freezable=True, freeze_method=name)(type("Record", (), {}))


@pytest.mark.parametrize(
    "namespace", [{"__annotations__": {"seal": int}}, {"seal": lambda self: None}]
)
def test_custom_name_collisions_rejected(namespace):
    with pytest.raises(DataclassDefinitionError, match="seal.*method name"):
        dataclass(type("Record", (), namespace), freezable=True, freeze_method="seal")


def test_custom_name_requires_freezable():
    with pytest.raises(DataclassDefinitionError, match="freezable"):
        dataclass(freeze_method="seal")(type("Record", (), {}))
