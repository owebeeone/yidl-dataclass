"""Test-first merged metadata/layout and independent class-cell replacement."""

import dataclasses as std
import copy
import pickle
from dataclasses import FrozenInstanceError
from support import inherited_lazy_models as inherited
from yidl_dataclass import dataclass, const, generated_source


def render_case():
    events = []

    class Named:
        def __set_name__(self, owner, name):
            events.append((owner.__name__, name))

    class Mixin:
        __slots__ = ()

        def greet(self):
            return "mixin"

        def __init_subclass__(cls):
            events.append((cls.__name__, "subclass"))

    class BaseDeclaration(Mixin):
        "base documentation"

        units: int = 2
        token: int = const(default=3)
        named = Named()

        def greet(self):
            return super().greet() + "/base"

        @classmethod
        def owner(cls):
            return __class__.__name__, cls.__name__

        @staticmethod
        def declared():
            return __class__.__name__

        @property
        def title(self):
            return __class__.__name__

    original_cell = BaseDeclaration.greet.__closure__[0]
    Base = dataclass(BaseDeclaration)
    assert original_cell.cell_contents is BaseDeclaration
    assert Base.greet.__closure__[0] is not original_cell
    assert Base.greet.__closure__[0].cell_contents is Base

    @dataclass
    class Child(Base):
        units: int = 5
        token: int = const(default=8)
        tag: str = "child"

        def greet(self):
            return super().greet() + "/child"

    value = Child()
    assert value.greet() == "mixin/base/child"
    assert [item.name for item in std.fields(Child)] == ["units", "token", "tag"]
    assert std.asdict(value) == {"units": 5, "token": 8, "tag": "child"}
    assert Child.__slots__ == ("tag",)
    assert Base.__doc__ == "base documentation" and value.title == "BaseDeclaration"
    assert (
        Base.owner() == ("BaseDeclaration", "BaseDeclaration")
        and Base.declared() == "BaseDeclaration"
    )
    assert not hasattr(value, "__dict__")
    assert events == [
        ("BaseDeclaration", "named"),
        ("BaseDeclaration", "subclass"),
        ("BaseDeclaration", "named"),
        ("BaseDeclaration", "subclass"),
        ("Child", "subclass"),
        ("Child", "subclass"),
    ]
    lazy_models = (
        inherited.LazyBase,
        inherited.LazyChild,
        inherited.LazyGrandchild,
        inherited.LazyOverride,
    )
    assert all(model.__slots__ == () for model in lazy_models[1:])
    assert all(
        model.__basicsize__ == lazy_models[0].__basicsize__ for model in lazy_models
    )
    inherited.EVENTS.clear()
    for model in lazy_models:
        item = model([2])
        before = list(inherited.EVENTS)
        copies = (
            copy.copy(item),
            copy.deepcopy(item),
            pickle.loads(pickle.dumps(item)),
        )
        assert inherited.EVENTS == before
        assert all(not hasattr(other, "_y_dc_store_1") for other in copies)
        inherited.FAIL = True
        try:
            item.value
        except Exception as exc:
            assert isinstance(exc.__cause__, ValueError)
        else:
            raise AssertionError("failed factory accepted")
        finally:
            inherited.FAIL = False
        inherited.BUSY_COPY = True
        try:
            item.value
        except Exception as exc:
            assert isinstance(exc, RuntimeError)
        else:
            raise AssertionError("active copy accepted")
        finally:
            inherited.BUSY_COPY = False
        assert item.value == [2] and item.value is item.value
        ready = (copy.copy(item), copy.deepcopy(item), pickle.loads(pickle.dumps(item)))
        before = list(inherited.EVENTS)
        assert all(other.value == [2] for other in ready) and inherited.EVENTS == before
        item.value = [8]
        assert item.value == [8]
        del item.value
        assert item.value == [2] and item.readonly == 7
        try:
            item.readonly = 9
        except FrozenInstanceError:
            pass
        else:
            raise AssertionError("readonly assignment accepted")
    return {
        "generated_output.py": generated_source(Base)
        + "\n"
        + generated_source(Child)
        + "\n"
        + "\n".join(generated_source(model) for model in lazy_models),
        "behavior.txt": str(events)
        + "\nmerged-order=units,token,tag; slots-reused=True; class-cells-independent=True; super=mixin/base/child\nlazy-empty-chain-and-override=slots-reused; retry,busy-copy,reset,readonly,ready-and-unready-protocols=True\n",
    }
