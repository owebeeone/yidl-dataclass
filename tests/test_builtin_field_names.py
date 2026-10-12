"""Test-first valid builtin-like field names cannot shadow descriptor creation."""

from yidl_dataclass import dataclass, const, lazy, generated_source


def test_property_field_does_not_shadow_later_descriptor_creation():
    @dataclass
    class Names:
        property: int = const(default=1)
        other: int = const(default=2)
        later: int = lazy(default_factory=lambda other: other + 1, mutable=False)

    instance = Names()
    assert (instance.property, instance.other, instance.later) == (1, 2, 3)
    assert type(Names.__dict__["property"]) is property
    assert type(Names.__dict__["other"]) is property
    assert type(Names.__dict__["later"]) is property
    assert "_y_dc_property" in generated_source(Names)


def test_type_parameter_does_not_shadow_class_provider_or_classvar_read():
    from typing import ClassVar
    from yidl_dataclass import field

    @dataclass(repr=False)
    class Names:
        type: int = 2
        shared: ClassVar[int] = 4
        owner: object = field(
            init=False, default_factory=lambda cls: cls, repr=False, compare=False
        )
        value: int = field(init=False, default_factory=lambda shared: shared)

    instance = Names()
    assert instance.type == 2 and instance.owner is Names and instance.value == 4


def test_exception_parameter_preserves_factory_error_and_cause():
    import pytest
    from yidl_dataclass import field, FieldInitializationError

    original = ValueError("factory")

    def failed():
        raise original

    @dataclass(repr=False)
    class Names:
        Exception: int = 0
        value: int = field(init=False, default_factory=failed)

    with pytest.raises(FieldInitializationError) as caught:
        Names()
    assert caught.value.__cause__ is original


def test_typeerror_parameter_preserves_validator_contract_diagnostic():
    import pytest
    from yidl_dataclass import field

    @dataclass(repr=False)
    class Names:
        TypeError: int = 0
        value: int = field(default=2, validator=lambda value: object())

    with pytest.raises(TypeError, match="validator must return"):
        Names()
