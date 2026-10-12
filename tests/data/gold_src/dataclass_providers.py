"""Construction-scoped providers, eager management storage and captured self/class."""

from dataclasses import InitVar, fields, asdict
from yidl_dataclass import (
    dataclass,
    field,
    initvar,
    local_store,
    classvar,
    replace,
    storage_fields,
    generated_source,
)


def render_case():
    events = []

    def make_total(seed, scale):
        events.append(("total", seed, scale))
        return seed * scale

    def make_management(total):
        events.append(("local", total))
        return [total]

    def owner_tag(self, cls):
        events.append(("self", self.total, cls.__name__))
        return (self.total, cls.__name__)

    class Box:
        def __init__(self, total):
            events.append(("box", total))
            self.total = total

    @dataclass
    class Configuration:
        total: int = field(init=False, default_factory=make_total)
        seed: int = initvar(default=5)
        scale: int = classvar(default=2)
        management: list = local_store(default_factory=make_management, repr=True)
        tag: tuple = field(
            init=False, default_factory=owner_tag, allow_self_factory=True
        )
        box: object = field(init=False, default_factory=Box, repr=False, compare=False)

    assert events == []
    first, second = Configuration(), Configuration(8)
    assert not hasattr(first, "seed") and not hasattr(Configuration, "seed")
    assert Configuration.__slots__ == ("total", "management", "tag", "box")
    assert tuple(item.name for item in fields(Configuration)) == ("total", "tag", "box")
    assert tuple(item.name for item in storage_fields(Configuration)) == (
        "total",
        "seed",
        "scale",
        "management",
        "tag",
        "box",
    )
    assert set(asdict(first)) == {"total", "tag", "box"}
    assert (first.total, first.management, first.tag, first.box.total) == (
        10,
        [10],
        (10, "Configuration"),
        10,
    )
    assert (second.total, second.management, second.tag, second.box.total) == (
        16,
        [16],
        (16, "Configuration"),
        16,
    )
    rebuilt = replace(second)
    assert rebuilt.total == 10 and rebuilt.management is not second.management

    @dataclass
    class StandardProvider:
        seed: InitVar[int] = field(default_factory=lambda: 7)
        answer: int = field(init=False, default_factory=lambda seed: seed + 3)

    standard = StandardProvider()
    assert standard.answer == 10 and not hasattr(standard, "seed")
    assert tuple(item.name for item in fields(StandardProvider)) == ("answer",)
    return {
        "generated_output.py": generated_source(Configuration)
        + "\n"
        + generated_source(StandardProvider),
        "behavior.txt": str(events)
        + "\nfields=total,tag,box; hidden-seed=True; local-excluded=True; replacement-seed=5; std-initvar-factory=True\n",
    }
