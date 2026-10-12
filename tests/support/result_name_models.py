"""Module-level canonical named models for exact pickle resolution."""

import builtins
from yidl_dataclass import dataclass, const, field

EVENTS = []


def convert(value):
    EVENTS.append(value)
    return builtins.int(value)


NAMES = ("type", "tuple", "dict", "int", "hash", "_y_dc_converter_0")
MODELS = []
for name in NAMES:
    declaration = builtins.type(
        name,
        (),
        {
            "__module__": __name__,
            "__annotations__": {"value": builtins.int},
            "value": (
                field(default=3, converter=convert)
                if name.startswith("_y_dc_")
                else const(default=3)
            ),
        },
    )
    model = dataclass(declaration, frozen=name == "hash")
    globals()[name] = model
    MODELS.append(model)
assert EVENTS == []
