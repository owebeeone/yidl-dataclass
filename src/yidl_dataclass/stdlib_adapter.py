"""Bounded std private metadata harvesting; never generates user methods."""

from __future__ import annotations
import copy
import dataclasses as std
import inspect
import typing
import sys
from typing import Any, ClassVar
from .dataclass_definition import DataclassOptions
from .dataclass_markers import (
    require_bool,
    FieldDeclaration,
    InitvarDeclaration,
    ClassvarDeclaration,
    LocalStoreDeclaration,
)
from .errors import DataclassDefinitionError


def ensure_supported_runtime() -> None:
    if sys.implementation.name != "cpython" or sys.version_info[:2] not in (
        (3, 12),
        (3, 13),
        (3, 14),
    ):
        raise DataclassDefinitionError(
            "supported runtimes are CPython 3.12 through 3.14"
        )


def annotations_for(cls: type) -> dict[str, Any]:
    if sys.version_info[:2] >= (3, 14):
        import annotationlib

        return annotationlib.get_annotations(
            cls, format=annotationlib.Format.FORWARDREF
        )
    return inspect.get_annotations(cls, eval_str=False)


def fields_for(
    cls: type, annotations: dict[str, Any], *, kw_only: bool
) -> tuple[std.Field[Any], ...]:
    attributes = {"__module__": cls.__module__}
    for name in annotations:
        value = inspect.getattr_static(cls, name, std.MISSING)
        if value is not std.MISSING:
            if isinstance(value, FieldDeclaration):
                value = value.field
            attributes[name] = (
                copy.copy(value) if isinstance(value, std.Field) else value
            )
    harvest = type(cls.__name__, (), attributes)
    result = []
    fence_seen = False
    for name, annotation in annotations.items():
        if annotation is std.KW_ONLY or (
            isinstance(annotation, str)
            and std._is_type(
                annotation,
                harvest,
                std,
                std.KW_ONLY,
                lambda a, module: a is module.KW_ONLY,
            )
        ):
            if fence_seen:
                raise DataclassDefinitionError("KW_ONLY specified more than once")
            kw_only = True
            fence_seen = True
            continue
        value = attributes.get(name, std.MISSING)
        factory = value.default_factory if isinstance(value, std.Field) else std.MISSING
        if factory is not std.MISSING:
            value.default_factory = std.MISSING
        declaration = inspect.getattr_static(cls, name, std.MISSING)
        original_type = annotation
        if isinstance(declaration, (InitvarDeclaration, ClassvarDeclaration)):
            annotated_initvar = std._is_initvar(original_type, std) or (
                isinstance(original_type, str)
                and std._is_type(
                    original_type, harvest, std, std.InitVar, std._is_initvar
                )
            )
            annotated_classvar = std._is_classvar(original_type, typing) or (
                isinstance(original_type, str)
                and std._is_type(
                    original_type, harvest, typing, typing.ClassVar, std._is_classvar
                )
            )
            opposite = (
                annotated_classvar
                if isinstance(declaration, InitvarDeclaration)
                else annotated_initvar
            )
            if opposite:
                raise DataclassDefinitionError(f"{name}: annotation kind conflict")
            annotation = (
                std.InitVar[original_type]
                if isinstance(declaration, InitvarDeclaration)
                else ClassVar[original_type]
            )
        try:
            item = std._get_field(harvest, name, annotation, kw_only)
        except (TypeError, ValueError) as error:
            raise DataclassDefinitionError(
                f"{cls.__qualname__}.{name}: {error}"
            ) from error
        if factory is not std.MISSING:
            if is_classvar(item):
                raise DataclassDefinitionError(
                    f"{name}: ClassVar cannot have a factory"
                )
            item.default_factory = factory
        item.type = original_type
        if (
            is_initvar(item)
            and item.default is not std.MISSING
            and item.default.__class__.__hash__ is None
        ):
            raise DataclassDefinitionError(
                f"{name}: mutable default is unsupported; use a factory"
            )
        if isinstance(declaration, LocalStoreDeclaration) and not is_instance_field(
            item
        ):
            raise DataclassDefinitionError(f"{name}: annotation kind conflict")
        for option in ("init", "repr", "compare"):
            require_bool(f"{name}.{option}", getattr(item, option))
        if item.hash is not None:
            require_bool(f"{name}.hash", item.hash)
        if item.kw_only is not std.MISSING:
            require_bool(f"{name}.kw_only", item.kw_only)
        if is_instance_field(item) and item.hash is True and item.compare is False:
            raise DataclassDefinitionError(f"{name}: hash=True requires compare=True")
        result.append(item)
    return tuple(result)


def is_instance_field(item: std.Field[Any]) -> bool:
    return item._field_type is std._FIELD


def is_classvar(item: std.Field[Any]) -> bool:
    return item._field_type is std._FIELD_CLASSVAR


def is_initvar(item: std.Field[Any]) -> bool:
    return item._field_type is std._FIELD_INITVAR


def params_for(options: DataclassOptions):
    return std._DataclassParams(
        options.init,
        options.repr,
        options.eq,
        options.order,
        options.unsafe_hash,
        options.frozen,
        options.match_args,
        options.kw_only,
        options.slots,
        options.weakref_slot,
    )


def recursive_repr_decorator():
    """Select the interpreter's actual recursion guard, not a method generator."""
    if sys.version_info[:2] == (3, 12):
        return std._recursive_repr
    return std.recursive_repr()
