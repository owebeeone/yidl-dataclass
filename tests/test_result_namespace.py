"""Test-first narrow capture/builtin recognition, separate from canonical protocols."""

import builtins
import pytest
from yidl_dataclass import dataclass, const, field


@pytest.mark.parametrize(
    "name", ("type", "tuple", "dict", "int", "hash", "_y_dc_converter_0")
)
def test_result_binding_does_not_replace_method_dependencies(name):
    events = []

    def converter(value):
        events.append(value)
        return builtins.int(value)

    private = name.startswith("_y_dc_")
    model = dataclass(
        builtins.type(
            name,
            (),
            {
                "__annotations__": {"value": builtins.int},
                "value": (
                    field(default=3, converter=converter)
                    if private
                    else const(default=3)
                ),
            },
        ),
        frozen=name == "hash",
    )
    assert events == []
    expected = converter if private else getattr(builtins, name)
    assert model.__init__.__globals__.get(name, expected) is expected
