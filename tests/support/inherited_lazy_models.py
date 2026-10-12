"""Module-level lazy inheritance fixtures; protocol readiness must not run factories."""

import copy
from yidl_dataclass import dataclass, lazy, initvar

EVENTS = []
FAIL = False
BUSY_COPY = False


def cache(self, seed):
    EVENTS.append(self.__class__.__name__)
    if FAIL:
        raise ValueError("retry")
    if BUSY_COPY:
        copy.copy(self)
    return list(seed)


@dataclass(repr=False)
class LazyBase:
    seed: list = initvar(default_factory=list)
    value: list = lazy(
        default_factory=cache, allow_self_factory=True, compare=False, repr=False
    )
    readonly: int = lazy(
        default_factory=lambda: 7, mutable=False, compare=False, repr=False
    )


@dataclass(repr=False)
class LazyChild(LazyBase):
    pass


@dataclass(repr=False)
class LazyGrandchild(LazyChild):
    pass


@dataclass(repr=False)
class LazyOverride(LazyGrandchild):
    value: list = lazy(
        default_factory=cache, allow_self_factory=True, compare=False, repr=False
    )
