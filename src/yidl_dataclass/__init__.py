"""YIDL Dataclass public declarations and standard inspection helpers."""

from dataclasses import (
    MISSING,
    Field,
    InitVar,
    KW_ONLY,
    FrozenInstanceError,
    fields,
    is_dataclass,
    asdict,
    astuple,
)
from .dataclass import dataclass, generated_source, replace, storage_fields
from .dataclass_markers import field, const, lazy, initvar, classvar, local_store
from .errors import (
    DataclassDefinitionError,
    FieldConversionError,
    FieldValidationError,
    FieldInitializationError,
    LazyInitializationError,
)

__all__ = [
    "dataclass",
    "field",
    "const",
    "lazy",
    "initvar",
    "classvar",
    "local_store",
    "replace",
    "storage_fields",
    "generated_source",
    "MISSING",
    "Field",
    "InitVar",
    "KW_ONLY",
    "FrozenInstanceError",
    "fields",
    "is_dataclass",
    "asdict",
    "astuple",
    "DataclassDefinitionError",
    "FieldConversionError",
    "FieldValidationError",
    "FieldInitializationError",
    "LazyInitializationError",
]
