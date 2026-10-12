"""Test-first lazy retry, cancellation, busy/recursion and availability edges."""

import threading
import pytest
from yidl_dataclass import (
    dataclass,
    field,
    lazy,
    LazyInitializationError,
    FieldInitializationError,
    FieldConversionError,
    FieldValidationError,
    DataclassDefinitionError,
)


@pytest.mark.parametrize("role", ("factory", "converter", "validator", "cancellation"))
def test_lazy_failure_is_unready_and_retries(role):
    original = (
        KeyboardInterrupt("cancel") if role == "cancellation" else ValueError("failed")
    )
    failed = [False]

    def fail(candidate=2):
        if not failed[0]:
            failed[0] = True
            raise original
        return int(candidate) if role != "validator" else True

    factory = fail if role in ("factory", "cancellation") else lambda: "2"

    @dataclass(repr=False)
    class Retry:
        value: int = lazy(
            default_factory=factory,
            converter=fail if role == "converter" else int,
            validator=fail if role == "validator" else None,
        )

    instance = Retry()
    error_type = {
        "factory": FieldInitializationError,
        "converter": FieldConversionError,
        "validator": FieldValidationError,
        "cancellation": KeyboardInterrupt,
    }[role]
    with pytest.raises(error_type) as caught:
        instance.value
    assert (
        caught.value is original
        if role == "cancellation"
        else caught.value.__cause__ is original
    )
    assert instance.value == 2


def test_opaque_recursion_busy_guard_clears_after_failure():
    repeat = [True]

    def factory(self):
        return self.value if repeat[0] else 3

    @dataclass(repr=False)
    class Recursive:
        value: int = lazy(default_factory=factory, allow_self_factory=True)

    instance = Recursive()
    with pytest.raises(LazyInitializationError, match="Recursive.*value.*busy"):
        instance.value
    repeat[0] = False
    assert instance.value == 3


def test_concurrent_access_and_set_delete_while_busy_rejected():
    entered = threading.Event()
    release = threading.Event()
    results = []

    def factory():
        entered.set()
        assert release.wait(5)
        return 7

    @dataclass(repr=False)
    class Busy:
        value: int = lazy(default_factory=factory)

    instance = Busy()
    thread = threading.Thread(target=lambda: results.append(instance.value))
    thread.start()
    try:
        assert entered.wait(5)
        with pytest.raises(LazyInitializationError, match="busy"):
            instance.value
        with pytest.raises(LazyInitializationError, match="busy"):
            instance.value = 3
        with pytest.raises(LazyInitializationError, match="busy"):
            del instance.value
    finally:
        release.set()
        thread.join(5)
    assert results == [7] and not thread.is_alive()


def test_lazy_named_cycle_and_unavailable_optional_provider_rejected():
    class Cycle:
        first: int = lazy(default_factory=lambda second: second)
        second: int = lazy(default_factory=lambda first: first)

    with pytest.raises(DataclassDefinitionError, match="cycle.*first.*second.*first"):
        dataclass(Cycle)

    class Missing:
        absent: int = field(init=False, repr=False)
        value: int = lazy(default_factory=lambda absent=3: absent)

    with pytest.raises(DataclassDefinitionError, match="value.*unavailable.*absent"):
        dataclass(Missing)
