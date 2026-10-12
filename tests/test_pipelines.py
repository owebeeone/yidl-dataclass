"""Test-first pipeline failure/cause/cancellation and atomic install mechanics."""

import pytest
from yidl_dataclass import (
    dataclass,
    field,
    const,
    initvar,
    FieldConversionError,
    FieldValidationError,
    DataclassDefinitionError,
    FrozenInstanceError,
)


@pytest.mark.parametrize("result", (0, 1, "yes", object()))
def test_invalid_validator_result_is_direct_typeerror_and_preserves_value(result):
    @dataclass
    class Value:
        item: int = field(
            default=2, validator=lambda value: True if value == 2 else result
        )

    instance = Value()
    with pytest.raises(TypeError, match="validator.*return") as caught:
        instance.item = 3
    assert type(caught.value) is TypeError
    assert instance.item == 2


def test_converter_failure_is_contextual_atomic_and_preserves_cause():
    error = ValueError("bad conversion")

    def converter(value):
        if value == "bad":
            raise error
        return int(value)

    @dataclass
    class Value:
        item: int = field(default=2, converter=converter)

    instance = Value()
    with pytest.raises(FieldConversionError, match=r"Value.*item.*converter") as caught:
        instance.item = "bad"
    assert caught.value.__cause__ is error and instance.item == 2


def test_validator_failure_rejection_and_existing_context_preserved():
    error = RuntimeError("validator failed")
    contextual = FieldValidationError("already contextual")

    def validator(value):
        if value == 3:
            raise error
        if value == 4:
            raise contextual
        return value != 5

    @dataclass
    class Value:
        item: int = field(default=2, validator=validator)

    instance = Value()
    with pytest.raises(FieldValidationError) as caught:
        instance.item = 3
    assert caught.value.__cause__ is error and instance.item == 2
    with pytest.raises(FieldValidationError) as caught:
        instance.item = 4
    assert caught.value is contextual and instance.item == 2
    with pytest.raises(FieldValidationError) as caught:
        instance.item = 5
    assert caught.value.__cause__ is None and instance.item == 2


@pytest.mark.parametrize("role", ("converter", "validator"))
def test_pipeline_baseexception_is_unwrapped_and_assignment_atomic(role):
    cancellation = KeyboardInterrupt("cancel")

    def callback(value):
        if value == 3:
            raise cancellation
        return value if role == "converter" else True

    @dataclass
    class Value:
        item: int = field(default=2, **{role: callback})

    instance = Value()
    with pytest.raises(KeyboardInterrupt) as caught:
        instance.item = 3
    assert caught.value is cancellation and instance.item == 2


def test_derived_conversion_exact_primitive_nullable_and_explicit_disable():
    @dataclass(convert=True)
    class Value:
        number: int
        optional: int | None = None
        untouched: object = field(default="raw", converter=None)

    first = Value("3")
    second = Value("4", "8")
    assert (first.number, first.optional, first.untouched) == (3, None, "raw")
    assert (second.number, second.optional) == (4, 8)
    first.optional = "9"
    assert first.optional == 9
    first.optional = None
    assert first.optional is None


@pytest.mark.parametrize("annotation", (list[int], object, "unresolved", int | str))
def test_unsupported_type_derived_conversion_requires_explicit_converter(annotation):
    class Value:
        pass

    Value.__annotations__ = {"item": annotation}
    with pytest.raises(DataclassDefinitionError, match="explicit converter"):
        dataclass(Value, convert=True)


def test_processed_initvar_reaches_factory_without_public_retention():
    @dataclass
    class Value:
        source: int = initvar(converter=int)
        result: int = field(init=False, default_factory=lambda source: source + 1)

    instance = Value("4")
    assert instance.result == 5 and not hasattr(instance, "source")


@pytest.mark.parametrize("role", ("converter", "validator"))
def test_callback_signature_must_accept_one_positional_value(role):
    def invalid(*, value):
        return value

    class Value:
        item: int = field(**{role: invalid})

    with pytest.raises(DataclassDefinitionError, match="one positional"):
        dataclass(Value)
