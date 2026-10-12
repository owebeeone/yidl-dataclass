"""Bounded std private metadata harvesting; never generates user methods."""

from __future__ import annotations
import copy
import dataclasses as std
import inspect
import sys
from typing import Any
from .dataclass_definition import DataclassOptions
from .dataclass_markers import require_bool
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
        try:
            item = std._get_field(harvest, name, annotation, kw_only)
        except (TypeError, ValueError) as error:
            raise DataclassDefinitionError(
                f"{cls.__qualname__}.{name}: {error}"
            ) from error
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
