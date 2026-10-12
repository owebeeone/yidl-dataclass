"""Test-first remaining extension ownership and rejected composition boundaries."""

import dataclasses as std
from typing import ClassVar
import pytest
from yidl_dataclass import (
    dataclass,
    const,
    field,
    storage_fields,
    DataclassDefinitionError,
)


@pytest.mark.parametrize("annotation", (ClassVar[int], std.InitVar[int]))
def test_const_conflicts_with_pseudo_field_annotation(annotation):
    declaration = type(
        "Conflict",
        (),
        {"__annotations__": {"value": annotation}, "value": const(default=3)},
    )
    with pytest.raises(DataclassDefinitionError, match="kind.*conflict"):
        dataclass(declaration)


@pytest.mark.parametrize(
    "hook",
    (
        "__copy__",
        "__deepcopy__",
        "__getstate__",
        "__setstate__",
        "__reduce__",
        "__reduce_ex__",
    ),
)
@pytest.mark.parametrize("inherited", (False, True))
def test_policy_classes_reject_bypassing_copy_state_hooks(hook, inherited):
    namespace = {hook: lambda *args: None}
    base = type("Hook", (), dict(namespace, __slots__=())) if inherited else object
    declaration = type(
        "Policy",
        (base,),
        dict(
            {} if inherited else namespace,
            __annotations__={"value": int},
            value=const(default=3),
        ),
    )
    with pytest.raises(DataclassDefinitionError, match=hook):
        dataclass(declaration)


def test_dependencies_are_immutable_provider_names_without_values():
    @dataclass
    class Dependencies:
        base: int = 2
        value: int = field(init=False, default_factory=lambda base, cls: base + 1)

    descriptions = storage_fields(Dependencies)
    assert tuple((item.name, item.dependencies) for item in descriptions) == (
        ("base", ()),
        ("value", ("base",)),
    )
    with pytest.raises((AttributeError, std.FrozenInstanceError)):
        descriptions[1].dependencies = ("other",)


@pytest.mark.parametrize("private_name", ("_y_dc_store_0", "_y_dc_factory_0"))
def test_inherited_private_generated_name_collision_rejected(private_name):
    base = type("Private", (), {"__slots__": (private_name,)})
    declaration = type(
        "Collision",
        (base,),
        {"__annotations__": {"value": int}, "value": const(default=3)},
    )
    with pytest.raises(DataclassDefinitionError, match="reserved generated name"):
        dataclass(declaration)
