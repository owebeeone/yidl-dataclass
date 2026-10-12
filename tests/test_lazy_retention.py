"""Test-first failure and explicit seed retention transitions."""

import pytest
from yidl_dataclass import (
    dataclass,
    initvar,
    lazy,
    storage_fields,
    FieldInitializationError,
)


def test_failed_terminal_preserves_provider_and_successful_prerequisite_cache():
    calls = []
    fail = [True]

    def make_second(seed, first):
        calls.append("second")
        if fail[0]:
            raise ValueError("retry")
        return seed + first

    @dataclass(repr=False)
    class Retry:
        seed: int = initvar()
        first: int = lazy(
            default_factory=lambda seed: calls.append("first") or seed, mutable=False
        )
        second: int = lazy(default_factory=make_second, mutable=False)

    instance = Retry(3)
    provider = storage_fields(Retry)[0].provider_name
    with pytest.raises(FieldInitializationError):
        instance.second
    assert calls == ["first", "second"] and hasattr(instance, provider)
    fail[0] = False
    assert instance.second == 6 and calls == ["first", "second", "second"]
    assert not hasattr(instance, provider)


def test_seeded_nonresettable_consumers_release_without_factory_evaluation():
    def forbidden(seed):
        raise AssertionError("seeded cache evaluated")

    @dataclass(repr=False)
    class Seeded:
        seed: int = initvar()
        first: int = lazy(default_factory=forbidden, init=True, mutable=False)
        second: int = lazy(default_factory=forbidden, init=True, mutable=False)

    instance = Seeded(3, 4, 5)
    assert storage_fields(Seeded)[0].retained is True
    provider = storage_fields(Seeded)[0].provider_name
    assert (
        instance.first == 4 and instance.second == 5 and not hasattr(instance, provider)
    )
