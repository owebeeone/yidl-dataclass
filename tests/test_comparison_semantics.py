"""Controlled std differential equality reads, callbacks and raw result identity."""

from __future__ import annotations
import dataclasses as std
from dataclasses import dataclass as support_dataclass
import pytest
from yidl_dataclass import dataclass, field


@support_dataclass
class Truth:
    label: str
    truth: bool | None
    events: list[str]

    def __bool__(self):
        self.events.append(f"bool:{self.label}")
        if self.truth is None:
            raise ValueError("truth failure")
        return self.truth


@support_dataclass
class Operand:
    label: str
    result: object
    events: list[str]

    def __eq__(self, other):
        self.events.append(f"eq:{self.label}")
        if isinstance(self.result, Exception):
            raise self.result
        return self.result


def scenario(decorator, make_field, mode):
    events = []

    @decorator(repr=False, slots=True)
    class Triple:
        label: str = make_field(compare=False)
        first: object
        second: object
        third: object

        def __getattribute__(self, name):
            if name in ("first", "second", "third"):
                label = object.__getattribute__(self, "label")
                events.append(f"read:{label}:{name}")
            return object.__getattribute__(self, name)

    false = Truth("false", False, events)
    true = Truth("true", True, events)
    final = Truth("final", mode != "final_false", events)
    error = Truth("error", None, events)
    first_result = {
        "false": false,
        "truth_error": error,
        "equality_error": ValueError("equality failure"),
        "reverse": NotImplemented,
    }.get(mode, true)
    first = Operand("first", first_result, events)
    second = Operand("second", false if mode == "middle_false" else true, events)
    third = Operand("third", final, events)
    right_first = first if mode == "shared" else Operand("reflected", true, events)
    right_second = second if mode == "shared" else object()
    right_third = third if mode == "shared" else object()
    left = Triple("left", first, second, third)
    right = Triple("right", right_first, right_second, right_third)
    events.clear()
    try:
        raw = Triple.__eq__(left, right)
        result = ("return", raw is false, raw is final, raw is True, tuple(events))
    except ValueError as exc:
        result = ("raise", type(exc).__name__, str(exc), tuple(events))
    events.clear()
    assert Triple.__eq__(left, object()) is NotImplemented
    foreign = tuple(events)
    events.clear()
    assert Triple.__eq__(left, left) is True
    self_events = tuple(events)
    return result, foreign, self_events


@pytest.mark.parametrize(
    "mode",
    (
        "false",
        "middle_false",
        "last",
        "final_false",
        "shared",
        "reverse",
        "truth_error",
        "equality_error",
    ),
)
def test_equality_callback_read_truth_and_raw_result_match_std(mode):
    assert scenario(dataclass, field, mode) == scenario(std.dataclass, std.field, mode)


def test_shared_nonreflexive_scalar_and_subclass_dispatch_matches_std():
    def observe(decorator):
        @decorator(slots=True, repr=False)
        class Value:
            item: object

        class SubValue(Value):
            __slots__ = ()

        shared = float("nan")
        first, second = Value(shared), Value(shared)
        return (
            first == second,
            first == first,
            Value.__eq__(first, SubValue(shared)) is NotImplemented,
        )

    assert observe(dataclass) == observe(std.dataclass)


def test_ordered_reads_callbacks_and_raw_order_result_match_std():
    def observe(decorator, operation):
        events = []
        final = Truth("ordered", True, events)

        class Ordered:
            def __eq__(self, other):
                events.append("eq")
                return False

            def __lt__(self, other):
                events.append("lt")
                return final

            def __le__(self, other):
                events.append("le")
                return final

            def __gt__(self, other):
                events.append("gt")
                return final

            def __ge__(self, other):
                events.append("ge")
                return final

        @decorator(order=True, slots=True, repr=False)
        class Pair:
            first: object
            second: object

            def __getattribute__(self, name):
                if name in ("first", "second"):
                    events.append(f"read:{name}")
                return object.__getattribute__(self, name)

        left, right = Pair(Ordered(), 1), Pair(object(), 2)
        events.clear()
        raw = getattr(Pair, operation)(left, right)
        return raw is final, tuple(events)

    for operation in ("__lt__", "__le__", "__gt__", "__ge__"):
        assert observe(dataclass, operation) == observe(std.dataclass, operation)


def test_repr_failure_cleans_recursion_guard_and_hash_failure_propagates():
    def observe(decorator):
        class Unstable:
            fail = True

            def __repr__(self):
                if self.fail:
                    raise ValueError("repr failure")
                return "recovered"

        @decorator(unsafe_hash=True, slots=True)
        class Value:
            item: object

        payload = Unstable()
        value = Value(payload)
        try:
            repr(value)
        except ValueError as exc:
            first = str(exc)
        payload.fail = False
        second = repr(value)
        value.item = []
        try:
            hash(value)
        except TypeError as exc:
            third = str(exc)
        return first, second, third

    assert observe(dataclass) == observe(std.dataclass)


@pytest.mark.parametrize("first_truth", (False, True))
def test_ephemeral_intermediate_truth_result_lifetime_matches_std(first_truth):
    def observe(decorator):
        events = []

        class Ephemeral:
            def __init__(self, label):
                self.label = label

            def __bool__(self):
                events.append(f"bool:{self.label}")
                return first_truth if self.label == "first" else True

            def __del__(self):
                events.append(f"release:{self.label}")

        class Produces:
            def __init__(self, label):
                self.label = label

            def __eq__(self, other):
                events.append(f"eq:{self.label}")
                return Ephemeral(self.label)

        @decorator(slots=True, repr=False)
        class Triple:
            first: object
            second: object
            third: object

        left = Triple(Produces("first"), Produces("second"), Produces("final"))
        right = Triple(object(), object(), object())
        result = Triple.__eq__(left, right)
        events.append("returned")
        del result
        return events

    assert observe(dataclass) == observe(std.dataclass)


def test_invalid_truth_result_is_released_with_retained_exception_traceback():
    def observe(decorator):
        events = []

        class InvalidTruth:
            def __bool__(self):
                events.append("invalid-bool")
                return 1

            def __del__(self):
                events.append("release")

        class Produces:
            def __eq__(self, other):
                events.append("eq")
                return InvalidTruth()

        @decorator(slots=True, repr=False)
        class Pair:
            first: object
            second: object

        left, right = Pair(Produces(), 2), Pair(object(), 3)
        caught = None
        try:
            Pair.__eq__(left, right)
        except TypeError as exc:
            caught = exc
        assert caught is not None
        events.append("caught-with-traceback")
        before = tuple(events)
        caught.__traceback__ = None
        events.append("traceback-cleared")
        return before, tuple(events)

    assert observe(dataclass) == observe(std.dataclass)


@pytest.mark.parametrize("exception_type", (ValueError, KeyboardInterrupt, SystemExit))
def test_truth_exception_and_baseexception_cleanup_matches_std(exception_type):
    def observe(decorator):
        events = []

        class Throws:
            def __bool__(self):
                events.append("bool")
                raise exception_type("stopped")

            def __del__(self):
                events.append("release")

        class Produces:
            def __eq__(self, other):
                events.append("eq")
                return Throws()

        @decorator(slots=True, repr=False)
        class Pair:
            first: object
            second: object

        left, right = Pair(Produces(), 2), Pair(object(), 3)
        caught = None
        try:
            Pair.__eq__(left, right)
        except BaseException as exc:
            caught = exc
        assert type(caught) is exception_type
        before = tuple(events)
        caught.__traceback__ = None
        return before, tuple(events)

    assert observe(dataclass) == observe(std.dataclass)
