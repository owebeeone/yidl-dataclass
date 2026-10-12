"""Standard-library oracle for metadata, annotations and independent factories."""
import dataclasses as std
import inspect
from typing import ClassVar
from yidl_dataclass import dataclass, field, generated_source


def declarations(decorator, make_field):
    @decorator(eq=False, repr=False, slots=True)
    class Catalog:
        count: int
        label: str = "stock"
        retired: int = make_field(default=11, init=False)
        tags: list = make_field(default_factory=list, metadata={"role": "labels"})
        kind: ClassVar[str] = make_field(default="catalog", compare=False, hash=True, repr=False)
        limit: int = make_field(default=8, kw_only=True)
    return Catalog


def observation(cls):
    instance = cls(3, limit=9)
    other = cls(7)
    instance.tags.append("first")
    return {
        "signature": str(inspect.signature(cls)),
        "fields": [(f.name, f.type, f.init, f.kw_only, dict(f.metadata)) for f in std.fields(cls)],
        "values": std.asdict(instance),
        "factory_independent": other.tags == [],
        "classvar": cls.kind,
        "classvar_flags": (cls.__dataclass_fields__["kind"].compare, cls.__dataclass_fields__["kind"].hash, cls.__dataclass_fields__["kind"].repr),
        "params": [(name, getattr(cls.__dataclass_params__, name)) for name in type(cls.__dataclass_params__).__slots__],
        "match": cls.__match_args__,
    }


def render_case():
    actual = declarations(dataclass, field)
    reference = declarations(std.dataclass, std.field)
    assert std.is_dataclass(actual)
    assert observation(actual) == observation(reference)
    assert "kind" not in actual.__slots__
    return {"generated_output.py": generated_source(actual),
            "behavior.txt": str(observation(actual)) + "\n"}
