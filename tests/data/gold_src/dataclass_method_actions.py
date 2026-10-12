"""Local versus inherited methods, hash actions, recursive/empty repr contrast."""

import dataclasses as std
from yidl_dataclass import dataclass, generated_source


def models(decorator):
    class Base:
        __slots__ = ()

        def __eq__(self, other):
            return "base-eq"

        def __repr__(self):
            return "base-repr"

        def __hash__(self):
            return 17

    @decorator(eq=False, repr=False, slots=True)
    class Inherited(Base):
        value: int

    @decorator(slots=True)
    class Local:
        value: int

        def __eq__(self, other):
            return "local-eq"

        def __repr__(self):
            return "local-repr"

        def __hash__(self):
            return 19

    @decorator(slots=True)
    class Automatic:
        value: int

        def __eq__(self, other):
            return "custom-eq"

    @decorator(unsafe_hash=True, slots=True)
    class Unsafe:
        value: int

        def __eq__(self, other):
            return "unsafe-eq"

    @decorator(slots=True)
    class Recursive:
        value: object

    @decorator(order=True, unsafe_hash=True, slots=True)
    class Empty:
        pass

    @decorator(eq=False, unsafe_hash=True, slots=True)
    class HashOnly:
        value: int

    return Inherited, Local, Automatic, Unsafe, Recursive, Empty, HashOnly


def observation(classes):
    Inherited, Local, Automatic, Unsafe, Recursive, Empty, HashOnly = classes
    recursive = Recursive(None)
    recursive.value = recursive
    return {
        "inherited": (
            repr(Inherited(2)),
            Inherited(2) == Inherited(7),
            hash(Inherited(2)),
        ),
        "local": (repr(Local(2)), Local(2) == Local(7), hash(Local(2))),
        "automatic": (Automatic(2) == Automatic(7), Automatic.__hash__ is None),
        "unsafe": (Unsafe(2) == Unsafe(7), hash(Unsafe(2)) == hash((2,))),
        "recursive": repr(recursive),
        "empty": repr(Empty()),
        "hash_only": (HashOnly(2) == HashOnly(2), hash(HashOnly(2)) == hash((2,))),
        "no_generated_ne": all("__ne__" not in cls.__dict__ for cls in classes),
    }


def render_case():
    actual = models(dataclass)
    reference = models(std.dataclass)
    assert observation(actual) == observation(reference)
    return {
        "generated_output.py": "\n".join(generated_source(cls) for cls in actual),
        "behavior.txt": str(observation(actual)) + "\n",
    }
