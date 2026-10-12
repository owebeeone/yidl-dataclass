"""Immutable normalized product facts, separate from generated model classes."""

from __future__ import annotations
from dataclasses import dataclass, Field
from typing import Any


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


@dataclass(frozen=True, slots=True)
class DataclassDefinition:
    options: DataclassOptions
    fields: tuple[StorageField, ...]
    slot_names: tuple[str, ...]
    generate_init: bool
    generation_schema: int = 1
