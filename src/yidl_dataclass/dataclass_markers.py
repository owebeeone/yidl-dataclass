"""Public field declarations; extension policy objects own their validation."""

from __future__ import annotations
from dataclasses import dataclass, Field, MISSING, _MISSING_TYPE
import dataclasses as std
import sys
from collections.abc import Callable
from typing import Any
from .errors import DataclassDefinitionError


def require_bool(name: str, value: object) -> None:
    if type(value) is not bool:
        raise DataclassDefinitionError(f"{name} must be bool")


@dataclass(frozen=True, slots=True)
class FieldPolicy:
    mutable: bool | None = None
    converter: object = std.field(default_factory=lambda: MISSING)
    validator: object = None
    allow_self_factory: bool = False
    freeze: Callable[[Any], Any] | _MISSING_TYPE = std.field(
        default_factory=lambda: MISSING
    )


@dataclass(frozen=True, slots=True)
class FieldDeclaration:
    field: Field
    policy: FieldPolicy


@dataclass(frozen=True, slots=True)
class ConstDeclaration(FieldDeclaration):
    pass


@dataclass(frozen=True, slots=True)
class LazyDeclaration(FieldDeclaration):
    pass


@dataclass(frozen=True, slots=True)
class InitvarDeclaration(FieldDeclaration):
    pass


@dataclass(frozen=True, slots=True)
class ClassvarDeclaration(FieldDeclaration):
    pass


@dataclass(frozen=True, slots=True)
class LocalStoreDeclaration(FieldDeclaration):
    pass


def field(
    *,
    default=MISSING,
    default_factory=MISSING,
    init=True,
    repr=True,
    hash=None,
    compare=True,
    metadata=None,
    kw_only=MISSING,
    doc=None,
    mutable=None,
    converter=MISSING,
    validator=None,
    allow_self_factory=False,
    freeze: Callable[[Any], Any] | _MISSING_TYPE = MISSING,
):
    for name, value in (
        ("init", init),
        ("repr", repr),
        ("compare", compare),
        ("allow_self_factory", allow_self_factory),
    ):
        require_bool(name, value)
    if kw_only is not MISSING:
        require_bool("kw_only", kw_only)
    if hash is not None:
        require_bool("hash", hash)
    if mutable is not None:
        require_bool("mutable", mutable)
    if converter is not MISSING and converter is not None and not callable(converter):
        raise DataclassDefinitionError("converter must be callable, None or MISSING")
    if validator is not None and not callable(validator):
        raise DataclassDefinitionError("validator must be callable or None")
    if freeze is not MISSING and not callable(freeze):
        raise DataclassDefinitionError("freeze must be callable")
    if doc is not None and sys.version_info[:2] < (3, 14):
        raise DataclassDefinitionError("field doc requires Python 3.14")
    options = dict(
        default=default,
        default_factory=default_factory,
        init=init,
        repr=repr,
        hash=hash,
        compare=compare,
        metadata=metadata,
        kw_only=kw_only,
    )
    if sys.version_info[:2] >= (3, 14):
        options["doc"] = doc
    result = std.field(**options)
    if (
        mutable is None
        and converter is MISSING
        and validator is None
        and not allow_self_factory
        and freeze is MISSING
    ):
        return result
    return FieldDeclaration(
        result, FieldPolicy(mutable, converter, validator, allow_self_factory, freeze)
    )


def _as_declaration(value, cls):
    if isinstance(value, Field):
        return cls(value, FieldPolicy())
    return cls(value.field, value.policy)


def const(**field_options):
    if field_options.get("mutable") is not None:
        require_bool("mutable", field_options["mutable"])
    if field_options.get("mutable") is True:
        raise DataclassDefinitionError("const mutable must be False")
    field_options["mutable"] = False
    return _as_declaration(field(**field_options), ConstDeclaration)


def lazy(*, default_factory, init=False, **field_options):
    if "default" in field_options:
        raise DataclassDefinitionError("lazy does not accept default")
    return _as_declaration(
        field(default_factory=default_factory, init=init, **field_options),
        LazyDeclaration,
    )


def initvar(**field_options):
    for option in ("repr", "compare"):
        if field_options.get(option) is True:
            raise DataclassDefinitionError(f"initvar {option} must be False")
        field_options.setdefault(option, False)
    if field_options.get("hash") is True:
        raise DataclassDefinitionError("initvar hash must be False")
    field_options.setdefault("hash", False)
    return _as_declaration(field(**field_options), InitvarDeclaration)


def classvar(*, default=MISSING, metadata=None, doc=None):
    return _as_declaration(
        field(default=default, metadata=metadata, doc=doc), ClassvarDeclaration
    )


def local_store(
    *,
    default=MISSING,
    default_factory=MISSING,
    repr=False,
    metadata=None,
    doc=None,
    converter=MISSING,
    validator=None,
    allow_self_factory=False,
    freeze: Callable[[Any], Any] | _MISSING_TYPE = MISSING,
):
    return _as_declaration(
        field(
            default=default,
            default_factory=default_factory,
            init=False,
            repr=repr,
            compare=False,
            hash=False,
            metadata=metadata,
            doc=doc,
            mutable=True,
            converter=converter,
            validator=validator,
            allow_self_factory=allow_self_factory,
            freeze=freeze,
        ),
        LocalStoreDeclaration,
    )
