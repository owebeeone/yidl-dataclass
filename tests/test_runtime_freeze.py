"""Red acceptance tests; no implementation shim, skips or xfail masking.

The canonical fixture owns the success path. These tests cover edge cases and
failure semantics: direct optimistic freezing, without rollback or thaw.
"""

from dataclasses import FrozenInstanceError
from copy import copy, deepcopy

import pytest
from yidl_dataclass import (
    DataclassDefinitionError,
    FieldValidationError,
    dataclass,
    field,
    lazy,
    local_store,
    replace,
)


def test_freeze_without_hook_is_shallow_and_blocks_field_writes():
    @dataclass(freezable=True)
    class Value:
        items: list = field(default_factory=list)

    value = Value()
    original = value.items
    value.freeze()
    assert value.items is original
    # No implicit deep policy: the user deliberately supplied no freeze hook.
    original.append(1)
    assert value.items == [1]
    with pytest.raises(FrozenInstanceError):
        value.items = []
    with pytest.raises(FrozenInstanceError):
        del value.items


def test_hook_receives_current_value_and_installs_result_once():
    calls = []

    def freeze_value(value):
        calls.append(value)
        return tuple(value)

    @dataclass(freezable=True)
    class Value:
        items: object = field(default_factory=list, freeze=freeze_value)

    value = Value()
    value.items = [2, 3]
    supplied = value.items
    assert calls == []
    value.freeze()
    value.freeze()
    assert len(calls) == 1 and calls[0] is supplied
    assert value.items == (2, 3)


def test_freeze_visits_shared_child_only_once():
    calls = []

    def freeze_name(value):
        calls.append(value)
        return value

    def freeze_children(value):
        for child in value:
            child.freeze()
        return tuple(value)

    @dataclass(freezable=True)
    class Node:
        name: str = field(freeze=freeze_name)
        children: object = field(default_factory=list, freeze=freeze_children)

    child = Node("child")
    parent = Node("parent", [child, child])
    parent.freeze()
    assert calls.count("child") == 1
    assert parent.children[0] is parent.children[1] is child


def test_failure_propagates_and_clears_in_progress_state():
    failure = ValueError("synthetic freeze failure")
    calls = []

    def freeze_value(value):
        calls.append(value)
        if len(calls) == 1:
            raise failure
        return tuple(value)

    @dataclass(freezable=True)
    class Value:
        items: object = field(default_factory=list, freeze=freeze_value)

    value = Value([1])
    # Wrapping is permitted; the original failure must remain diagnosable.
    with pytest.raises(Exception) as raised:
        value.freeze()
    error = raised.value
    while error is not failure and error.__cause__ is not None:
        error = error.__cause__
    assert error is failure
    value.items = [2]
    value.freeze()
    assert len(calls) == 2
    assert value.items == (2,)
    with pytest.raises(FrozenInstanceError):
        value.items = []


def test_parent_failure_does_not_thaw_completed_child():
    fail = True

    def freeze_children(value):
        for child in value:
            child.freeze()
        if fail and value:
            raise ValueError("after child freeze")
        return tuple(value)

    @dataclass(freezable=True)
    class Node:
        name: str
        children: object = field(default_factory=list, freeze=freeze_children)

    child = Node("child")
    parent = Node("parent", [child])
    with pytest.raises(Exception):
        parent.freeze()
    with pytest.raises(FrozenInstanceError):
        child.name = "changed"
    fail = False
    parent.freeze()
    assert parent.children[0] is child


def test_freezing_does_not_revalidate_transformed_representation():
    @dataclass(freezable=True)
    class Value:
        items: object = field(
            default_factory=list,
            validator=lambda value: isinstance(value, list),
            freeze=tuple,
        )

    value = Value([1])
    with pytest.raises(FieldValidationError):
        value.items = "invalid"
    value.freeze()
    # Validation describes mutable input; freeze may change its representation.
    assert value.items == (1,)


def test_replacement_constructs_mutable_object_and_preserves_original():
    @dataclass(freezable=True)
    class Value:
        name: str

    original = Value("old")
    original.freeze()
    revision = replace(original, name="new")
    revision.name = "edited"
    assert original.name == "old"
    with pytest.raises(FrozenInstanceError):
        original.name = "changed"


def test_inherited_fields_freeze_with_derived_fields():
    @dataclass(freezable=True)
    class Base:
        base: int

    @dataclass(freezable=True)
    class Derived(Base):
        extra: int

    value = Derived(1, 2)
    value.base = 3
    value.extra = 4
    value.freeze()
    with pytest.raises(FrozenInstanceError):
        value.base = 5
    with pytest.raises(FrozenInstanceError):
        del value.extra


def test_equal_mutable_models_are_unhashable_before_freeze():
    @dataclass(freezable=True)
    class Value:
        identity: str

    value = Value("id")
    with pytest.raises(TypeError):
        hash(value)


@pytest.mark.parametrize("option", (1, None, "yes"))
def test_freezable_requires_exact_boolean(option):
    with pytest.raises(DataclassDefinitionError, match="freezable.*bool"):
        dataclass(
            type("Value", (), {"__annotations__": {"value": int}}), freezable=option
        )


@pytest.mark.parametrize("hook", (1, False, "tuple"))
def test_freeze_hook_must_be_callable(hook):
    with pytest.raises(DataclassDefinitionError, match="freeze.*callable"):
        field(freeze=hook)


def test_copy_preserves_freeze_state_before_and_after_transition():
    @dataclass(freezable=True)
    class Value:
        name: str

    value = Value("initial")
    copied = copy(value)
    copied.name = "mutable copy"
    value.freeze()
    for frozen_copy in (copy(value), deepcopy(value)):
        assert frozen_copy.name == "initial"
        with pytest.raises(FrozenInstanceError):
            frozen_copy.name = "bad"


def test_lazy_field_materializes_and_freezes_management_storage():
    calls = []

    def make_values():
        calls.append("factory")
        return [1, 2]

    @dataclass(freezable=True)
    class Value:
        items: object = lazy(default_factory=make_values, freeze=tuple, mutable=True)
        cache: object = local_store(default_factory=list, freeze=tuple)

    value = Value()
    assert calls == []
    value.cache.append(3)
    value.freeze()
    assert calls == ["factory"]
    assert value.items == (1, 2) and value.cache == (3,)
    with pytest.raises(FrozenInstanceError):
        value.items = []
    with pytest.raises(FrozenInstanceError):
        del value.items
    with pytest.raises(FrozenInstanceError):
        value.cache = []


def test_freezing_empty_model_and_copy_are_repeatable():
    @dataclass(freezable=True)
    class Empty:
        pass

    value = Empty()
    value.freeze()
    copy(value).freeze()


def test_freeze_callable_must_accept_one_positional_value():
    class Value:
        items: list = field(default_factory=list, freeze=lambda first, second: first)

    with pytest.raises(DataclassDefinitionError, match="freeze.*one positional"):
        dataclass(Value, freezable=True)


@pytest.mark.parametrize(
    "namespace", ({"freeze": lambda self: None}, {"__annotations__": {"freeze": int}})
)
def test_freeze_method_name_is_reserved(namespace):
    with pytest.raises(DataclassDefinitionError, match="freeze.*method name"):
        dataclass(type("Value", (), namespace), freezable=True)


def test_inference_recognizes_metadata_not_method_names_or_runtime_values():
    calls = []

    class Pretender:
        def freeze(self):
            calls.append("pretender")

    @dataclass(freezable=True)
    class Child:
        value: int

    @dataclass(freezable=True)
    class Parent:
        typed: Child
        untyped: object
        pretender: Pretender

    typed = Child(1)
    untyped = Child(2)
    parent = Parent(typed, untyped, Pretender())
    parent.freeze()
    with pytest.raises(FrozenInstanceError):
        typed.value = 3
    untyped.value = 4
    assert calls == []


def test_unresolved_annotation_requires_explicit_policy():
    @dataclass(freezable=True)
    class Child:
        value: int

    @dataclass(freezable=True)
    class Parent:
        child: "UnresolvedChild"

    child = Child(1)
    Parent(child).freeze()
    child.value = 2


def test_typed_child_inference_also_applies_to_lazy_fields():
    @dataclass(freezable=True)
    class Child:
        value: int

    @dataclass(freezable=True)
    class Parent:
        child: Child = lazy(default_factory=lambda: Child(1))

    parent = Parent()
    parent.freeze()
    with pytest.raises(FrozenInstanceError):
        parent.child.value = 2
