"""Test-first policy layout, exclusions and suppressed-init failures."""

import pytest
from yidl_dataclass import (
    dataclass,
    field,
    const,
    DataclassDefinitionError,
    FrozenInstanceError,
)


@pytest.mark.parametrize(
    "options", ({"compare": True}, {"compare": False, "hash": True})
)
def test_frozen_writable_fields_must_be_excluded(options):
    class Frozen:
        cache: int = field(default=2, mutable=True, **options)

    with pytest.raises(DataclassDefinitionError, match="compare|hash"):
        dataclass(Frozen, frozen=True, unsafe_hash=True)


def test_frozen_dictionary_mode_rejected():
    with pytest.raises(DataclassDefinitionError, match="frozen.*slots"):
        dataclass(type("Frozen", (), {}), frozen=True, slots=False)


@pytest.mark.parametrize("custom", (False, True))
def test_policy_initialization_cannot_be_suppressed(custom):
    namespace = {"__annotations__": {"value": int}, "value": const(default=3)}
    if custom:
        namespace["__init__"] = lambda self: None
    with pytest.raises(DataclassDefinitionError, match="requires generated init"):
        dataclass(type("Suppressed", (), namespace), init=custom)


@pytest.mark.parametrize("method", ("__getattribute__", "__setattr__", "__delattr__"))
def test_policy_interceptors_are_rejected_including_inherited(method):
    base = type("Intercept", (), {"__slots__": (), method: getattr(object, method)})

    class Policy(base):
        value: int = const(default=3)

    with pytest.raises(DataclassDefinitionError, match="interceptor"):
        dataclass(Policy)


def test_const_invalid_mutability_flag_is_not_overwritten():
    with pytest.raises(DataclassDefinitionError, match="bool"):
        const(mutable=1)


def test_readonly_policy_requires_constructor_source_even_without_consumer():
    class Missing:
        value: int = const(init=False)

    with pytest.raises(DataclassDefinitionError, match="value.*source"):
        dataclass(Missing)


def test_mutable_pipeline_deletion_and_readonly_delete_errors():
    @dataclass
    class Value:
        mutable: int = field(default=2, converter=int)
        readonly: int = const(default=3)

    instance = Value()
    del instance.mutable
    with pytest.raises(AttributeError):
        _ = instance.mutable
    instance.mutable = "8"
    assert instance.mutable == 8
    with pytest.raises(FrozenInstanceError, match="readonly"):
        del instance.readonly
    with pytest.raises(FrozenInstanceError, match="readonly"):
        instance.readonly = 4
