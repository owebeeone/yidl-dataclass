"""Test-first pseudo-field kinds, suppression and ownership diagnostics."""

import dataclasses as std
from typing import ClassVar
import pytest
from yidl_dataclass import (
    dataclass,
    field,
    initvar,
    classvar,
    local_store,
    replace,
    DataclassDefinitionError,
)


@pytest.mark.parametrize(
    "marker,annotation",
    (
        (initvar, ClassVar[int]),
        (classvar, std.InitVar[int]),
        (local_store, std.InitVar[int]),
    ),
)
def test_convenience_annotation_kind_conflict(marker, annotation):
    declaration = type(
        "Conflict",
        (),
        {"__annotations__": {"value": annotation}, "value": marker(default=3)},
    )
    with pytest.raises(DataclassDefinitionError, match="kind.*conflict"):
        dataclass(declaration)


@pytest.mark.parametrize("marker", (initvar, local_store))
def test_source_free_extension_provider_rejected(marker):
    declaration = type(
        "Unavailable",
        (),
        {
            "__annotations__": {"value": int},
            "value": marker(init=False) if marker is initvar else marker(),
        },
    )
    with pytest.raises(DataclassDefinitionError, match="value.*source"):
        dataclass(declaration)


@pytest.mark.parametrize("custom", (False, True))
def test_extension_initialization_cannot_be_suppressed(custom):
    namespace = {"__annotations__": {"seed": int}, "seed": initvar(default=3)}
    if custom:
        namespace["__init__"] = lambda self: None
    with pytest.raises(DataclassDefinitionError, match="requires generated init"):
        dataclass(type("Suppressed", (), namespace), init=custom)


def test_named_dependency_initialization_cannot_be_suppressed():
    class Suppressed:
        base: int
        value: int = field(default_factory=lambda base: base)

    with pytest.raises(DataclassDefinitionError, match="requires generated init"):
        dataclass(Suppressed, init=False)


def test_self_provider_requires_opt_in():
    class SelfProvider:
        value: object = field(default_factory=lambda self: self)

    with pytest.raises(DataclassDefinitionError, match="allow_self_factory"):
        dataclass(SelfProvider)


def test_imported_extended_field_is_copied_without_mutating_factory_metadata():
    declaration = initvar(default_factory=lambda: 2)

    class First:
        seed: int = declaration
        value: int = field(init=False, default_factory=lambda seed: seed)

    class Second:
        seed: int = declaration
        value: int = field(init=False, default_factory=lambda seed: seed)

    one, two = dataclass(First), dataclass(Second)
    assert declaration.field.name is None and declaration.field.type is None
    assert one.__dataclass_fields__["seed"] is not two.__dataclass_fields__["seed"]
    assert (
        one.__dataclass_fields__["seed"].default_factory
        is declaration.field.default_factory
    )


def test_required_initvar_replace_and_disallowed_changes():
    @dataclass
    class Required:
        seed: int = initvar()
        value: int = field(init=False, default_factory=lambda seed: seed)

    first = Required(3)
    with pytest.raises(ValueError, match="seed.*required"):
        replace(first)
    assert replace(first, seed=7).value == 7
    with pytest.raises(ValueError, match="init=False"):
        replace(first, seed=7, value=8)


def test_hidden_provider_unhashable_default_rejected():
    class MutableProvider:
        seed: object = initvar(default=[])

    with pytest.raises(DataclassDefinitionError, match="mutable default"):
        dataclass(MutableProvider)
