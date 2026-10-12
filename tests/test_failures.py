"""Focused Stage A definition errors; successful layouts belong to goldens."""
import dataclasses as std
import pytest
from yidl_dataclass import dataclass, field, KW_ONLY


def plain(cls, **options):
    return dataclass(cls, eq=False, repr=False, **options)


def test_unslotted_base_rejected_for_slots():
    class Base:
        pass
    class Child(Base):
        value: int
    with pytest.raises(TypeError, match="instance dictionary"):
        plain(Child)


def test_manual_slots_rejected():
    class Manual:
        __slots__ = ()
    with pytest.raises(TypeError, match="manual __slots__"):
        plain(Manual)


def test_invalid_default_order_rejected():
    class Invalid:
        first: int = 2
        later: int
    with pytest.raises(TypeError, match="non-default argument"):
        plain(Invalid)


def test_multiple_kw_only_fences_rejected():
    class Invalid:
        first: KW_ONLY
        second: KW_ONLY
    with pytest.raises(TypeError, match="KW_ONLY"):
        plain(Invalid)


def test_reserved_field_rejected():
    class Invalid:
        _y_dc_hidden: int
    with pytest.raises(TypeError, match="reserved"):
        plain(Invalid)


def test_unhashable_default_rejected():
    class Invalid:
        value: list = []
    with pytest.raises(TypeError, match="mutable default"):
        plain(Invalid)


def test_post_init_rejected_even_with_init_suppressed():
    class Invalid:
        def __post_init__(self):
            pass
    with pytest.raises(TypeError, match="named factories"):
        plain(Invalid, init=False)


def test_weakref_requires_slots():
    with pytest.raises(TypeError, match="requires slots"):
        plain(type("Invalid", (), {}), slots=False, weakref_slot=True)


def test_decorator_requires_class():
    with pytest.raises(TypeError, match="class"):
        plain(42)


def test_unannotated_field_is_rejected():
    class Invalid:
        value = field(default=3)
    with pytest.raises(TypeError, match="annotation"):
        plain(Invalid)


def test_descriptor_default_is_rejected():
    class Invalid:
        value: int = property(lambda self: 3)
    with pytest.raises(TypeError, match="descriptor"):
        plain(Invalid)


@pytest.mark.parametrize("name", ("__dict__", "__weakref__", "self", "cls"))
def test_reserved_storage_names_are_rejected(name):
    declaration = type("Invalid", (), {"__annotations__": {name: int}})
    with pytest.raises(TypeError, match="reserved"):
        plain(declaration)
