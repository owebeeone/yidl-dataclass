"""Module-level canonical pickle fixtures, authored before copy support."""

from yidl_dataclass import dataclass, const, field, initvar, lazy, local_store

EVENTS = []
ACTIVE_OPERATION = None


def make_cache(seed):
    EVENTS.append("cache")
    return list(seed)


@dataclass(repr=False)
class CopyModel:
    seed: list = initvar(default_factory=list)
    values: list = field(default_factory=list, compare=False)
    readonly: int = const(default=3)
    cache: list = lazy(
        default_factory=make_cache, mutable=False, compare=False, repr=False
    )
    reset: list = lazy(
        default_factory=lambda seed: list(seed), compare=False, repr=False
    )
    management: list = local_store(default_factory=list)
    loop: object = field(default=None, compare=False, repr=False)


def active_factory(self):
    return ACTIVE_OPERATION(self)


@dataclass(repr=False)
class ActiveModel:
    value: object = lazy(
        default_factory=active_factory, allow_self_factory=True, compare=False
    )
