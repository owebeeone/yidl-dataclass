"""Immutable normalized product facts, separate from generated model classes."""

from __future__ import annotations
from dataclasses import dataclass, Field, field as support_field
from typing import Any
from .provider_plan import FactoryCall, InitializationStep
from .field_kinds import FieldKind, OrdinaryKind


@dataclass(frozen=True, slots=True)
class DataclassOptions:
    init: bool = True
    repr: bool = True
    eq: bool = True
    order: bool = False
    unsafe_hash: bool = False
    frozen: bool = False
    match_args: bool = True
    kw_only: bool = False
    slots: bool = True
    weakref_slot: bool = False
    convert: bool = False


@dataclass(frozen=True, slots=True)
class StorageField:
    name: str
    field: Field[Any]
    annotation_name: str
    default_name: str
    factory_name: str
    parameter_order: int
    is_instance: bool
    retained: bool = False
    kind: FieldKind = support_field(default_factory=OrdinaryKind)
    allow_self_factory: bool = False
    mutable: bool = True
    converter: object = None
    validator: object = None
    nullable_converter: bool = False
    store_name: str = ""
    has_accessor: bool = False
    dependencies: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class DataclassDefinition:
    options: DataclassOptions
    fields: tuple[StorageField, ...]
    slot_names: tuple[str, ...]
    generate_init: bool
    initialization: tuple[InitializationStep, ...] = ()
    factory_calls: tuple[FactoryCall, ...] = ()
    planned_init: bool = False
    policy_class: bool = False
    generation_schema: int = 1
