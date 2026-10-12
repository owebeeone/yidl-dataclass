"""Test-first active-copy/state failure and replacement interoperability."""

import copy
import dataclasses as std
import pickle
import sys
import pytest
from support import copy_models
from yidl_dataclass import dataclass, field, initvar, lazy, local_store, replace


@pytest.mark.parametrize("operation", (copy.copy, copy.deepcopy, pickle.dumps))
def test_active_lazy_copy_and_pickle_rejected(operation):
    copy_models.ACTIVE_OPERATION = operation
    instance = copy_models.ActiveModel()
    try:
        with pytest.raises(RuntimeError, match="active.*lazy|lazy.*active"):
            instance.value
    finally:
        copy_models.ACTIVE_OPERATION = None


def test_state_rejects_invalid_schema_without_callbacks():
    instance = copy_models.CopyModel([1])
    with pytest.raises((TypeError, ValueError), match="state.*schema|schema.*state"):
        instance.__setstate__((True, {}, None))


def test_package_and_std_replace_hidden_provider_rules():
    calls = []

    @dataclass(repr=False)
    class Model:
        seed: int = initvar(default=3)
        value: int = field(default=2)
        eager: int = field(init=False, default_factory=lambda seed, value: seed + value)
        cached: int = lazy(
            default_factory=lambda seed: calls.append(seed) or seed, mutable=False
        )
        local: list = local_store(default_factory=list)

    original = Model(seed=8)
    original.local.append("used")
    replaced = replace(original, value=5)
    assert replaced.eager == 8 and replaced.local == [] and calls == []
    assert replaced.cached == 3 and original.cached == 8
    with pytest.raises(AttributeError):
        std.replace(original)
    assert std.replace(original, seed=4).eager == 6
    with pytest.raises(ValueError, match="init=False"):
        replace(original, cached=4)
    with pytest.raises(TypeError, match="unknown"):
        replace(original, unknown=4)


def test_required_provider_is_not_replayed_from_retained_state():
    @dataclass(repr=False)
    class Required:
        seed: int = initvar()
        cached: int = lazy(default_factory=lambda seed: seed, mutable=False)

    first = Required(8)
    with pytest.raises(ValueError, match="seed.*required"):
        replace(first)
    assert replace(first, seed=4).cached == 4


def test_copy_replace_version_method_and_local_override():
    @dataclass
    class Model:
        value: int = 2

    if sys.version_info[:2] == (3, 12):
        assert "__replace__" not in Model.__dict__
    else:
        assert "__replace__" in Model.__dict__
        assert copy.replace(Model(), value=8).value == 8

    @dataclass
    class Custom:
        value: int = 2

        def __replace__(self, **changes):
            return ("custom", changes)

    assert Custom().__replace__(value=3) == ("custom", {"value": 3})
