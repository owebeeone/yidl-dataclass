"""Postimplementation verification of complete field-policy deletion and mutant."""

from yidl_dataclass import (
    dataclass,
    field,
    const,
    local_store,
    fields,
    storage_fields,
    generated_source,
    DataclassDefinitionError,
)


def render_case():
    @dataclass(order=True, unsafe_hash=True)
    class Before:
        code: int
        measure: int = 3
        obsolete: int = const(default="4", converter=int)
        label: str = field(default="old", compare=False, hash=False)
        doubled: int = field(init=False, default_factory=lambda measure: measure * 2)
        management: dict = local_store(default_factory=dict)

    @dataclass(order=True, unsafe_hash=True)
    class After:
        code: int
        measure: int = 3
        label: str = field(default="old", compare=False, hash=False)
        doubled: int = field(init=False, default_factory=lambda measure: measure * 2)
        management: dict = local_store(default_factory=dict)

    old = Before(1)
    changed = Before(1, obsolete="5")
    equal = After(1, label="different")
    new = After(1)
    later = After(2)
    assert old.obsolete == 4 and old != changed
    assert new == equal and new < later and hash(new) == hash(equal)
    assert not hasattr(new, "obsolete")
    assert "obsolete" not in After.__annotations__ and "obsolete" not in After.__dict__
    assert "obsolete" not in After.__slots__
    assert [item.name for item in fields(new)] == [
        "code",
        "measure",
        "label",
        "doubled",
    ]
    assert [item.name for item in storage_fields(new)] == [
        "code",
        "measure",
        "label",
        "doubled",
        "management",
    ]
    assert "obsolete" not in generated_source(After)
    assert "_y_dc_converter_2" not in After.__init__.__globals__

    # Declaration deletion must also remove any dependent factory's reference.
    class MissingProvider:
        code: int
        remaining: int = field(init=False, default_factory=lambda obsolete: obsolete)

    try:
        dataclass(MissingProvider)
    except DataclassDefinitionError as error:
        assert (
            "remaining" in str(error)
            and "obsolete" in str(error)
            and "required" in str(error)
        )
    else:
        raise AssertionError("deleted required provider accepted")
    return {
        "generated_output.py": generated_source(Before)
        + "\n"
        + generated_source(After),
        "behavior.txt": "declaration-and-policy-deleted=True; slot-and-method-operands-removed=True; contrast-instances=True; missing-provider-diagnosed=True\n",
    }
