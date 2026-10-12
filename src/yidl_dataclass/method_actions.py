"""Compiler-only std method conflict and hash selection; no method bodies."""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, MISSING
from .dataclass_definition import DataclassOptions
from .errors import DataclassDefinitionError


@dataclass(frozen=True, slots=True)
class HashSelection:
    generate: bool
    disable: bool


class HashAction(ABC):
    __slots__ = ()

    @abstractmethod
    def lower(self) -> HashSelection:
        raise NotImplementedError


class PreserveHash(HashAction):
    __slots__ = ()

    def lower(self) -> HashSelection:
        return HashSelection(False, False)


class DisableHash(HashAction):
    __slots__ = ()

    def lower(self) -> HashSelection:
        return HashSelection(False, True)


class GenerateHash(HashAction):
    __slots__ = ()

    def lower(self) -> HashSelection:
        return HashSelection(True, False)


@dataclass(frozen=True, slots=True)
class MethodActions:
    repr: bool
    eq: bool
    order: bool
    hash: HashAction


def resolve_methods(cls: type, options: DataclassOptions) -> MethodActions:
    namespace = cls.__dict__
    if options.order and not options.eq:
        raise DataclassDefinitionError("order=True requires eq=True")
    if options.order:
        for name in ("__lt__", "__le__", "__gt__", "__ge__"):
            if name in namespace:
                raise DataclassDefinitionError(f"cannot overwrite local {name}")
    local_hash = namespace.get("__hash__", MISSING)
    explicit_hash = not (
        local_hash is MISSING or (local_hash is None and "__eq__" in namespace)
    )
    if options.unsafe_hash and explicit_hash:
        raise DataclassDefinitionError("unsafe_hash cannot overwrite explicit __hash__")
    if options.unsafe_hash or (options.eq and options.frozen and not explicit_hash):
        action = GenerateHash()
    elif options.eq and not options.frozen and not explicit_hash:
        action = DisableHash()
    else:
        action = PreserveHash()
    return MethodActions(
        options.repr and "__repr__" not in namespace,
        options.eq and "__eq__" not in namespace,
        options.order,
        action,
    )
