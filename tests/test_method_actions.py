"""Narrow std hash policy table and conflict diagnostics; frozen storage is Stage C."""

import dataclasses as std
import itertools
import pytest
from yidl_dataclass import dataclass
from yidl_dataclass.dataclass_definition import DataclassOptions
from yidl_dataclass.method_actions import resolve_methods
from yidl_dataclass.errors import DataclassDefinitionError


@pytest.mark.parametrize(
    "unsafe,eq,frozen,explicit", tuple(itertools.product((False, True), repeat=4))
)
def test_hash_selection_matches_independent_std_action(unsafe, eq, frozen, explicit):
    original_hash = lambda self: 41
    actual_decl = type("Policy", (), {"__hash__": original_hash} if explicit else {})
    std_decl = type("Policy", (), {"__hash__": original_hash} if explicit else {})
    options = DataclassOptions(unsafe_hash=unsafe, eq=eq, frozen=frozen)
    try:
        reference = std.dataclass(eq=eq, frozen=frozen, unsafe_hash=unsafe)(std_decl)
    except TypeError:
        with pytest.raises(DataclassDefinitionError, match="explicit __hash__"):
            resolve_methods(actual_decl, options)
    else:
        result = resolve_methods(actual_decl, options).hash.lower()
        hash_method = reference.__dict__.get("__hash__", object.__hash__)
        assert result.disable == (hash_method is None and not explicit)
        assert result.generate == (
            hash_method is not None
            and hash_method not in (original_hash, object.__hash__)
        )


@pytest.mark.parametrize("method", ("__lt__", "__le__", "__gt__", "__ge__"))
def test_local_order_conflict_rejected(method):
    declaration = type("Conflict", (), {method: lambda self, other: False})
    with pytest.raises(DataclassDefinitionError, match=method):
        dataclass(declaration, order=True)


def test_order_requires_equality():
    with pytest.raises(DataclassDefinitionError, match="requires eq"):
        dataclass(type("Conflict", (), {}), eq=False, order=True)


@pytest.mark.parametrize("hash_value", (None, lambda self: 4))
def test_unsafe_hash_explicit_local_hash_rejected(hash_value):
    declaration = type("Conflict", (), {"__hash__": hash_value})
    with pytest.raises(DataclassDefinitionError, match="explicit __hash__"):
        dataclass(declaration, unsafe_hash=True)
