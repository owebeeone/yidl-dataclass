"""Test-first direct-only hidden retention, terminal release and reset lifetime."""

import gc
import weakref
from yidl_dataclass import (
    dataclass,
    field,
    initvar,
    lazy,
    storage_fields,
    generated_source,
)


def render_case():
    class Seed:
        def __init__(self, value):
            self.value = value

    @dataclass(repr=False)
    class Terminals:
        seed: object = initvar()
        first: int = lazy(default_factory=lambda seed: seed.value, mutable=False)
        second: int = lazy(default_factory=lambda seed: seed.value + 1, mutable=False)

    seed = Seed(5)
    ref = weakref.ref(seed)
    terminals = Terminals(seed)
    del seed
    gc.collect()
    assert ref() is not None
    assert terminals.first == 5 and ref() is not None
    assert terminals.second == 6
    gc.collect()
    assert ref() is None
    assert not hasattr(terminals, "seed")

    @dataclass(repr=False)
    class Reset:
        seed: object = initvar()
        once: int = lazy(default_factory=lambda seed: seed.value, mutable=False)
        repeated: int = lazy(default_factory=lambda seed: seed.value, compare=False)

    seed = Seed(3)
    reset_ref = weakref.ref(seed)
    reset = Reset(seed)
    del seed
    assert reset.once == 3 and reset.repeated == 3
    reset_ref().value = 8
    del reset.repeated
    assert reset.repeated == 8 and reset_ref() is not None

    @dataclass(repr=False)
    class Cut:
        seed: object = initvar()
        middle: int = field(init=False, default_factory=lambda seed: seed.value)
        final: int = lazy(default_factory=lambda middle: middle + 1, mutable=False)

    seed = Seed(9)
    cut_ref = weakref.ref(seed)
    cut = Cut(seed)
    del seed
    gc.collect()
    assert cut_ref() is None and cut.final == 10

    @dataclass(repr=False)
    class Derived:
        seed: object = initvar()
        derived: int = initvar(init=False, default_factory=lambda seed: seed.value)
        final: int = lazy(default_factory=lambda derived: derived * 2, mutable=False)

    seed = Seed(4)
    derived_ref = weakref.ref(seed)
    derived = Derived(seed)
    del seed
    gc.collect()
    assert derived_ref() is None and derived.final == 8
    assert [
        (item.name, item.retained)
        for item in storage_fields(Derived)
        if item.kind.label == "initvar"
    ] == [("seed", False), ("derived", True)]
    return {
        "generated_output.py": "\n".join(
            generated_source(cls) for cls in (Terminals, Reset, Cut, Derived)
        ),
        "behavior.txt": "terminal-release=all-ready; reset-lifetime=True; eager-cut=True; derived-only=True; public-provider=False\n",
    }
