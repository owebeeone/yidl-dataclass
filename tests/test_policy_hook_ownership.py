"""Test-first generated protocol ownership cannot excuse user interception."""

import pytest
from yidl_dataclass import dataclass, const, DataclassDefinitionError


def test_fake_generated_name_marker_does_not_allow_custom_interceptor():
    class Pretend:
        __slots__ = ()
        __yidl_generated_copy_methods__ = ("__setattr__",)

        def __setattr__(self, name, value):
            pass

    class Policy(Pretend):
        value: int = const(default=2)

    with pytest.raises(DataclassDefinitionError, match="__setattr__"):
        dataclass(Policy)


def test_replaced_generated_state_hook_is_rejected_by_policy_subclass():
    @dataclass
    class Base:
        value: int = const(default=2)

    Base.__getstate__ = lambda self: None

    class Child(Base):
        other: int = const(default=3)

    with pytest.raises(DataclassDefinitionError, match="__getstate__"):
        dataclass(Child)
