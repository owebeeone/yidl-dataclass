"""Named factory DAG: reversed declaration, positional bridge, class/self providers."""

from typing import ClassVar
from yidl_dataclass import dataclass, field, generated_source


def render_case():
    events = []
    bridge = object()

    def make_total(unused=bridge, units=0, /, *, rate, cls):
        assert unused is bridge
        events.append(("total", units, rate, cls.__name__))
        return units * rate

    def make_summary(total, units):
        events.append(("summary", total, units))
        return (total, units)

    @dataclass
    class Order:
        summary: tuple = field(init=False, default_factory=make_summary)
        total: int = field(init=False, default_factory=make_total)
        units: int
        rate: ClassVar[int] = 7

    assert events == []
    first = Order(3)
    second = Order(4)
    assert (first.total, first.summary) == (21, (21, 3))
    assert (second.total, second.summary) == (28, (28, 4))
    assert events == [
        ("total", 3, 7, "Order"),
        ("summary", 21, 3),
        ("total", 4, 7, "Order"),
        ("summary", 28, 4),
    ]
    return {
        "generated_output.py": generated_source(Order),
        "behavior.txt": str(events) + "\n",
    }
