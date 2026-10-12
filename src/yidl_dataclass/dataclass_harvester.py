"""Declaration normalization into immutable facts and independent captures."""

from __future__ import annotations
import dataclasses as std
import inspect
import keyword
import types
from typing import Any
from .dataclass_definition import DataclassDefinition, DataclassOptions, StorageField
from .dataclass_markers import FieldDeclaration
from .errors import DataclassDefinitionError
from . import stdlib_adapter as adapter

_ZERO_ARG_BUILTINS = (list, dict, set, tuple, int, float, str, bytes, bool)


def harvest(
    cls: type, options: DataclassOptions
) -> tuple[DataclassDefinition, dict[str, Any], dict[str, Any]]:
    adapter.ensure_supported_runtime()
    if not isinstance(cls, type):
        raise DataclassDefinitionError("dataclass requires a class")
    if "__slots__" in cls.__dict__:
        raise DataclassDefinitionError("manual __slots__ is unsupported")
    if options.weakref_slot and not options.slots:
        raise DataclassDefinitionError("weakref_slot requires slots=True")
    if options.order and not options.eq:
        raise DataclassDefinitionError("order=True requires eq=True")
    if options.slots and any(base.__dictoffset__ for base in cls.__bases__):
        raise DataclassDefinitionError(
            "slotted model cannot inherit an instance dictionary"
        )
    if hasattr(cls, "__post_init__"):
        raise DataclassDefinitionError(
            "__post_init__ is unsupported; use named factories"
        )
    if options.frozen or options.convert:
        raise NotImplementedError("policy generation belongs to Stage C")
    if options.eq or options.repr or options.order or options.unsafe_hash:
        raise NotImplementedError(
            "comparison/repr/hash generation belongs to Stage B; Stage A requires eq=False, repr=False"
        )
    annotations = adapter.annotations_for(cls)
    for name in (*annotations, *cls.__dict__):
        if name.startswith("_y_dc_"):
            raise DataclassDefinitionError(f"reserved generated name: {name}")
    for name, value in cls.__dict__.items():
        if isinstance(value, (std.Field, FieldDeclaration)) and name not in annotations:
            raise DataclassDefinitionError(f"{name}: field requires a type annotation")
    for name in annotations:
        if (
            not name.isidentifier()
            or keyword.iskeyword(name)
            or name in ("self", "cls", "__dict__", "__weakref__")
        ):
            raise DataclassDefinitionError(f"invalid or reserved field name: {name}")
        value = inspect.getattr_static(cls, name, std.MISSING)
        default = value.default if isinstance(value, std.Field) else value
        if (
            default is not std.MISSING
            and not isinstance(default, types.MemberDescriptorType)
            and hasattr(type(default), "__get__")
        ):
            raise DataclassDefinitionError(
                f"{name}: descriptor-valued defaults are unsupported"
            )
        if isinstance(cls.__dict__.get(name), FieldDeclaration):
            raise NotImplementedError("extension fields belong to Stage C")
    items = adapter.fields_for(cls, annotations, kw_only=options.kw_only)
    if any(adapter.is_initvar(item) for item in items):
        raise NotImplementedError("InitVar initialization belongs to Stage C")
    instance = tuple(item for item in items if adapter.is_instance_field(item))
    positional = tuple(item for item in instance if item.init and not item.kw_only)
    keyword_only = tuple(item for item in instance if item.init and item.kw_only)
    seen_default = False
    for item in positional:
        if item.default is not std.MISSING or item.default_factory is not std.MISSING:
            seen_default = True
        elif seen_default:
            raise DataclassDefinitionError(
                f"non-default argument {item.name!r} follows default argument"
            )
    orders = {
        item.name: index for index, item in enumerate((*positional, *keyword_only))
    }
    inherited_slots = {
        name
        for base in cls.__mro__[1:]
        for name, value in base.__dict__.items()
        if isinstance(value, types.MemberDescriptorType)
    }
    slot_names = tuple(
        item.name for item in instance if item.name not in inherited_slots
    )
    if options.weakref_slot and not any(
        base.__weakrefoffset__ for base in cls.__bases__
    ):
        slot_names += ("__weakref__",)
    generate_init = options.init and "__init__" not in cls.__dict__
    definitions = []
    captures = {"__name__": cls.__module__}
    for index, item in enumerate(items):
        annotation_name, default_name, factory_name = (
            f"_y_dc_{role}_{index}" for role in ("annotation", "default", "factory")
        )
        captures[annotation_name] = item.type
        if item.default is not std.MISSING:
            captures[default_name] = item.default
        if item.default_factory is not std.MISSING:
            factory = item.default_factory
            if (
                generate_init
                and not any(factory is builtin for builtin in _ZERO_ARG_BUILTINS)
                and inspect.signature(factory).parameters
            ):
                raise NotImplementedError(
                    f"{item.name}: named factory graph belongs to Stage C"
                )
            captures[factory_name] = factory
        definitions.append(
            StorageField(
                item.name,
                item,
                annotation_name,
                default_name,
                factory_name,
                orders.get(item.name, index),
                adapter.is_instance_field(item),
            )
        )
    definition = DataclassDefinition(
        options, tuple(definitions), slot_names, generate_init
    )
    return definition, annotations, captures
