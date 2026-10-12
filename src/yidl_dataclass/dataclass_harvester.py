"""Declaration normalization into immutable facts and independent captures."""

from __future__ import annotations
import dataclasses as std
import inspect
import keyword
import types
from typing import Any
from .dataclass_definition import DataclassDefinition, DataclassOptions, StorageField
from .dataclass_markers import FieldDeclaration, LazyDeclaration, LocalStoreDeclaration
from .field_kinds import OrdinaryKind, InitvarKind, ClassvarKind, LocalKind
from .errors import DataclassDefinitionError
from . import stdlib_adapter as adapter
from .provider_plan import plan_initialization
from .policy_plan import normalize_policies


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
    from .inheritance_plan import (
        model_base_for,
        inherited_fields,
        validate_inherited_layout,
    )

    model_base = model_base_for(cls, options)
    for base in cls.__mro__[1:]:
        if "__yidl_dataclass_definition__" in base.__dict__:
            continue
        for name in base.__dict__:
            if name.startswith("_y_dc_"):
                raise DataclassDefinitionError(f"reserved generated name: {name}")
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
        raw = value.field if isinstance(value, FieldDeclaration) else value
        default = raw.default if isinstance(raw, std.Field) else raw
        if (
            default is not std.MISSING
            and not isinstance(default, types.MemberDescriptorType)
            and hasattr(type(default), "__get__")
        ):
            raise DataclassDefinitionError(
                f"{name}: descriptor-valued defaults are unsupported"
            )
    items = adapter.fields_for(cls, annotations, kw_only=options.kw_only)
    kinds = {}
    for item in items:
        declaration = inspect.getattr_static(cls, item.name, std.MISSING)
        kind = (
            LocalKind()
            if isinstance(declaration, LocalStoreDeclaration)
            else (
                InitvarKind()
                if adapter.is_initvar(item)
                else ClassvarKind() if adapter.is_classvar(item) else OrdinaryKind()
            )
        )
        kinds[item.name] = kind
    inherited = inherited_fields(model_base)
    merged_items = {item.name: item.field for item in inherited}
    merged_kinds = {item.name: item.kind for item in inherited}
    merged_items.update((item.name, item) for item in items)
    merged_kinds.update(kinds)
    instance = tuple(
        item for item in merged_items.values() if merged_kinds[item.name].parameter
    )
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
        item.name
        for item in items
        if kinds[item.name].stored and item.name not in inherited_slots
    )
    if options.weakref_slot and not any(
        base.__weakrefoffset__ for base in cls.__bases__
    ):
        slot_names += ("__weakref__",)
    generate_init = options.init and "__init__" not in cls.__dict__
    definitions = []
    inherited_by_name = {item.name: item for item in inherited}
    captures = {"__name__": cls.__module__}
    local_names = {item.name for item in items}
    for index, item in enumerate(merged_items.values()):
        annotation_name, default_name, factory_name = (
            f"_y_dc_{role}_{index}" for role in ("annotation", "default", "factory")
        )
        captures[annotation_name] = item.type
        if item.default is not std.MISSING:
            captures[default_name] = item.default
        if item.default_factory is not std.MISSING:
            factory = item.default_factory
            captures[factory_name] = factory
        definitions.append(
            std.replace(
                inherited_by_name[item.name],
                annotation_name=annotation_name,
                default_name=default_name,
                factory_name=factory_name,
                parameter_order=orders.get(item.name, index),
            )
            if item.name not in local_names
            else StorageField(
                item.name,
                item,
                annotation_name,
                default_name,
                factory_name,
                orders.get(item.name, index),
                adapter.is_instance_field(item) and kinds[item.name].metadata,
                kind=kinds[item.name],
                allow_self_factory=(
                    inspect.getattr_static(cls, item.name).policy.allow_self_factory
                    if isinstance(
                        inspect.getattr_static(cls, item.name, None), FieldDeclaration
                    )
                    else False
                ),
            )
        )
    definitions, policy_class = normalize_policies(
        cls, tuple(definitions), options, captures
    )
    validate_inherited_layout(cls, model_base, definitions)
    annotations = {item.name: item.field.type for item in definitions}
    slot_names = tuple(
        item.store_name
        for item in definitions
        if item.kind.stored and item.store_name not in inherited_slots
    ) + (("__weakref__",) if "__weakref__" in slot_names else ())
    slot_names += tuple(
        name
        for item in definitions
        if item.kind.label == "lazy"
        for name in (item.ready_name, item.busy_name)
    )
    steps, calls, planned = plan_initialization(
        cls, definitions, options, generate_init, captures
    )
    from .retention_plan import plan_retention

    definitions, steps, retention = plan_retention(definitions, calls, steps)
    slot_names += tuple(
        item.provider_name
        for item in definitions
        if item.retained and item.provider_name not in inherited_slots
    )
    dependencies = {call.field_name: call.dependencies for call in calls}
    definitions = tuple(
        std.replace(item, dependencies=dependencies.get(item.name, ()))
        for item in definitions
    )
    definition = DataclassDefinition(
        options,
        tuple(definitions),
        slot_names,
        generate_init,
        steps,
        calls,
        planned,
        policy_class,
        retention=retention,
    )
    return definition, annotations, captures
