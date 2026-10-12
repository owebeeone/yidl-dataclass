"""Test-first no-evaluation cloning and supported descriptor metadata."""

import sys
import pytest
from yidl_dataclass import dataclass


@pytest.mark.skipif(
    sys.version_info[:2] != (3, 14),
    reason="lazy function annotations are a CPython 3.14 contract",
)
def test_class_cell_clone_does_not_evaluate_lazy_function_annotations():
    events = []

    def mark():
        events.append("annotation")
        return int

    class Declaration:
        value: int = 2

        def own(self, argument: mark()) -> __class__:
            return __class__

    model = dataclass(Declaration)
    assert events == []
    assert model().own(3) is model
    assert Declaration().own(3) is Declaration
    assert model.own.__annotations__["return"] is model
    assert events == ["annotation"]


@pytest.mark.skipif(
    sys.version_info[:2] < (3, 13),
    reason="property name metadata starts in CPython 3.13",
)
def test_cloned_property_preserves_explicit_name_metadata():
    class Declaration:
        value: int = 2

        @property
        def label(self):
            return __class__.__name__

    Declaration.label.__name__ = "authored_name"
    model = dataclass(Declaration)
    assert model.label.__name__ == "authored_name"
    assert Declaration.label.__name__ == "authored_name"
    assert model().label == "Declaration"
