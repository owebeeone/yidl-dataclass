"""Narrow marker/normalization rejection and std Field ownership tests."""

import dataclasses as std
import sys
import pytest
from yidl_dataclass import dataclass, field


@pytest.mark.parametrize("option", ("init", "repr", "compare", "kw_only"))
def test_field_flags_are_strict_booleans(option):
    with pytest.raises(TypeError, match=option):
        field(**{option: 1})


@pytest.mark.parametrize(
    "option",
    (
        "init",
        "repr",
        "eq",
        "order",
        "unsafe_hash",
        "frozen",
        "match_args",
        "kw_only",
        "slots",
        "weakref_slot",
        "convert",
    ),
)
def test_decorator_flags_are_strict_booleans(option):
    with pytest.raises(TypeError, match=option):
        dataclass(**{option: 1})


def test_imported_field_is_not_mutated_or_shared():
    declaration = std.field(default=2, metadata={"label": "same"})

    class One:
        value: int = declaration

    class Two:
        other: int = declaration

    first = dataclass(One, eq=False, repr=False)
    second = dataclass(Two, eq=False, repr=False)
    assert declaration.name is None and declaration.type is None
    assert (
        first.__dataclass_fields__["value"] is not second.__dataclass_fields__["other"]
    )
    assert first.__dataclass_fields__["value"].name == "value"
    assert second.__dataclass_fields__["other"].name == "other"


def test_unsupported_minor_fails_before_generation(monkeypatch):
    monkeypatch.setattr(sys, "version_info", (3, 16, 0))
    with pytest.raises(TypeError, match="3.12.*3.15"):
        dataclass(type("Future", (), {}), eq=False, repr=False)


@pytest.mark.skipif(
    sys.version_info >= (3, 14), reason="non-None Field.doc is supported on 3.14"
)
def test_field_doc_rejected_on_older_minors():
    with pytest.raises(TypeError, match="doc"):
        field(doc="unsupported")


@pytest.mark.skipif(
    sys.version_info < (3, 14), reason="Field.doc is a Python3.14 surface"
)
def test_field_doc_is_carried_by_real_std_field():
    marker = field(doc="recorded documentation")
    assert isinstance(marker, std.Field)
    assert marker.doc == "recorded documentation"


def test_factory_objects_are_not_formatted_compared_or_called_during_generation():
    class Factory:
        def __repr__(self):
            raise AssertionError("factory repr executed")

        def __eq__(self, other):
            raise AssertionError("factory equality executed")

        def __call__(self):
            raise AssertionError("factory executed")

    factory = Factory()

    class Record:
        value: object = field(default_factory=factory)

    dataclass(Record, eq=False, repr=False)
