"""Test-first provider graph diagnostics and generation ownership failures."""

import pytest
from yidl_dataclass import dataclass, field, DataclassDefinitionError


def test_known_optional_unavailable_provider_is_not_omitted():
    def factory(missing=9):
        return missing

    class Broken:
        missing: int = field(init=False)
        consumer: int = field(init=False, default_factory=factory)

    with pytest.raises(
        DataclassDefinitionError,
        match=r"Broken.*consumer.*unavailable.*missing.*consumer.*missing",
    ):
        dataclass(Broken)


def test_named_cycle_rejected_even_when_inputs_could_bypass_factories():
    class Cycle:
        first: int = field(default_factory=lambda second: second)
        second: int = field(default_factory=lambda first: first)

    with pytest.raises(DataclassDefinitionError, match=r"cycle.*first.*second.*first"):
        dataclass(Cycle)


def test_unknown_required_parameter_rejected():
    class Missing:
        value: int = field(default_factory=lambda unknown: unknown)

    with pytest.raises(DataclassDefinitionError, match=r"value.*unknown.*required"):
        dataclass(Missing)


def test_variadic_factory_rejected():
    class Variadic:
        value: int = field(default_factory=lambda *args: 1)

    with pytest.raises(DataclassDefinitionError, match="variadic"):
        dataclass(Variadic)


def test_factory_callback_failure_is_contextual_and_preserves_cause():
    from yidl_dataclass import FieldInitializationError

    original = ValueError("factory failed")

    def factory():
        raise original

    @dataclass
    class Failure:
        value: int = field(default_factory=factory)

    with pytest.raises(
        FieldInitializationError, match=r"Failure.*value.*factory"
    ) as error:
        Failure()
    assert error.value.__cause__ is original


def test_factory_does_not_wrap_baseexception_or_existing_context_error():
    from yidl_dataclass import FieldConversionError

    for original in (
        KeyboardInterrupt("stop"),
        FieldConversionError("already contextual"),
    ):

        def factory():
            raise original

        @dataclass
        class Failure:
            value: int = field(default_factory=factory)

        with pytest.raises(type(original)) as error:
            Failure()
        assert error.value is original
