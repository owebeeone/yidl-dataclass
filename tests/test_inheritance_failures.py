"""Test-first inheritance policy/creation rejection and ABC/module contracts."""

import abc
import dataclasses as std
import sys
import types
from typing import ClassVar
import pytest
from yidl_dataclass import dataclass, field, const, lazy, DataclassDefinitionError


@pytest.mark.parametrize("frozen", (False, True))
def test_frozen_mixing_rejected(frozen):
    @dataclass(frozen=frozen)
    class Base:
        value: int = 2

    class Child(Base):
        pass

    with pytest.raises(DataclassDefinitionError, match="frozen.*inheritance"):
        dataclass(Child, frozen=not frozen)


@pytest.mark.parametrize("change", ("family", "mutability", "layout"))
def test_inherited_incompatible_shape_rejected(change):
    class Original:
        value: int = (
            lazy(default_factory=lambda: 2, mutable=False)
            if change == "family"
            else (
                field(default=2, mutable=False)
                if change == "mutability"
                else field(default=2, converter=int)
            )
        )

    Base = dataclass(Original)

    class Child(Base):
        value: int = 2

    with pytest.raises(DataclassDefinitionError, match="incompatible.*value"):
        dataclass(Child)


def test_multiple_models_and_std_model_bases_rejected():
    @dataclass(slots=False)
    class One:
        value: int = 2

    @dataclass(slots=False)
    class Two:
        other: int = 3

    class Many(One, Two):
        pass

    with pytest.raises(DataclassDefinitionError, match="multiple.*model"):
        dataclass(Many, slots=False)

    @std.dataclass(slots=True)
    class Standard:
        value: int = 2

    class Mixed(Standard):
        pass

    with pytest.raises(DataclassDefinitionError, match="stdlib.*base"):
        dataclass(Mixed)


def test_merged_provider_graph_revalidated():
    @dataclass
    class Base:
        first: int = 2

    class Cycle(Base):
        first: int = field(init=False, default_factory=lambda second: second)
        second: int = field(init=False, default_factory=lambda first: first)

    with pytest.raises(DataclassDefinitionError, match="cycle.*first.*second.*first"):
        dataclass(Cycle)


def test_custom_metaclass_and_required_subclass_keyword_rejected():
    class Meta(type):
        pass

    class Custom(metaclass=Meta):
        value: int = 2

    with pytest.raises(DataclassDefinitionError, match="metaclass"):
        dataclass(Custom)

    class Hook:
        __slots__ = ()

        def __init_subclass__(cls, *, needed):
            pass

    class Supplied(Hook, needed=3):
        value: int = 2

    with pytest.raises(DataclassDefinitionError, match="subclass.*no.argument"):
        dataclass(Supplied)


def test_abcmeta_and_abstract_property_slot_resolution():
    class Abstract(abc.ABC):
        __slots__ = ()

        @property
        @abc.abstractmethod
        def value(self):
            raise NotImplementedError

    class Concrete(Abstract):
        value: int = 2

    model = dataclass(Concrete)
    assert isinstance(model, abc.ABCMeta) and not model.__abstractmethods__
    assert model().value == 2


def test_abcmeta_without_abc_base_preserved():
    class Declaration(metaclass=abc.ABCMeta):
        value: int = 2

    model = dataclass(Declaration)
    assert type(model) is abc.ABCMeta and model().value == 2


def test_string_pseudo_annotations_use_defining_module_without_eval():
    module = types.ModuleType("dataclass_test_defining_module")
    module.__dict__.update(InitVar=std.InitVar, ClassVar=ClassVar, field=field)
    sys.modules[module.__name__] = module
    try:
        exec(
            'class Declaration:\n    seed: "InitVar[int]" = 3\n    shared: "ClassVar[int]" = 5\n    result: "unevaluated()" = field(init=False, default_factory=lambda seed:seed+1)\n',
            module.__dict__,
        )
        base = dataclass(module.Declaration)

        class Child(base):
            label: str = "ok"

        model = dataclass(Child)
        assert [item.name for item in std.fields(model)] == ["result", "label"]
        assert model().result == 4 and not hasattr(model(), "seed")
    finally:
        sys.modules.pop(module.__name__, None)
