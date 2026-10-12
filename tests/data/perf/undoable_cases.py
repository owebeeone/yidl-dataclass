"""Benchmark-only references; never installed as product runtime."""

import hashlib
import importlib.util
from pathlib import Path
import sys
import zipfile
from types import MappingProxyType

BASELINE_SHA256 = "e63818caa79b4c361d8c6203f572f79d4bb098f6ece09a3bf6b149e6206e5620"


def extract_baseline(wheel, destination):
    """Run once before workers; workers load a read-only extracted own-consumer tree."""
    wheel, destination = Path(wheel), Path(destination)
    if hashlib.sha256(wheel.read_bytes()).hexdigest() != BASELINE_SHA256:
        raise ValueError("frozen original consumer wheel digest mismatch")
    with zipfile.ZipFile(wheel) as archive:
        for name in archive.namelist():
            source = Path(name)
            if (
                not source.parts
                or source.parts[0] != "yidl_undoable"
                or name.endswith("/")
            ):
                continue
            if ".." in source.parts or source.is_absolute():
                raise ValueError("unsafe archive path")
            target = destination.joinpath(*source.parts[1:])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(name))
    return destination


def load_baseline(destination, *, wheel=None):
    destination = Path(destination)
    if wheel is None:
        raise ValueError("baseline loading requires frozen wheel/source verification")
    wheel = Path(wheel)
    if hashlib.sha256(wheel.read_bytes()).hexdigest() != BASELINE_SHA256:
        raise ValueError("frozen baseline wheel digest mismatch")
    with zipfile.ZipFile(wheel) as archive:
        expected = {
            name.removeprefix("yidl_undoable/"): archive.read(name)
            for name in archive.namelist()
            if name.startswith("yidl_undoable/") and not name.endswith("/")
        }
    actual = {
        path.relative_to(destination).as_posix(): path.read_bytes()
        for path in destination.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    if actual != expected:
        raise ValueError("baseline extracted source differs from frozen wheel")
    name = "_undoable_perf_baseline"
    spec = importlib.util.spec_from_file_location(
        name, destination / "__init__.py", submodule_search_locations=[str(destination)]
    )
    package = importlib.util.module_from_spec(spec)
    sys.modules[name] = package
    spec.loader.exec_module(package)
    return package


def field_namespace(api, count):
    return {
        "__module__": __name__,
        "__annotations__": {f"f{i}": int for i in range(count)},
        **{f"f{i}": api.managed(default=i) for i in range(count)},
    }


def structural_reference(api, count):
    """Historical facade getters, direct tuple comparison, no ContextVar prelude.

    This is explicitly handwritten benchmark reference code, not a standard
    dataclass, an independent correctness oracle, or product implementation.
    """
    cls = api.undoable(type("StructuralReference", (), field_namespace(api, count)))
    left = ", ".join(f"self.f{i}" for i in range(count)) + ","
    right = ", ".join(f"other.f{i}" for i in range(count)) + ","
    source = (
        "def reference_equal(self, other):\n"
        "    if other.__class__ is self.__class__:\n"
        f"        return ({left}) == ({right})\n"
        "    return NotImplemented\n"
    )
    bindings = {}
    exec(compile(source, "<benchmark-structural-reference>", "exec"), bindings)
    cls.__eq__ = bindings["reference_equal"]
    cls.__hash__ = None
    return cls, source


def setup_equal(cls, api):
    manager = api.UndoRedoManager()
    left, right = cls(transaction_manager=manager), cls(transaction_manager=manager)
    manager.initialize(left, right)
    assert left == right
    return left, right


def write_case(api, count, shape, runner, *, integrated):
    child_namespace = field_namespace(api, count)
    child_cls = (
        api.undoable(eq=True)(type("WriteChild", (), child_namespace))
        if integrated
        else api.undoable(type("WriteChild", (), child_namespace))
    )
    namespace = field_namespace(api, count)
    namespace["__annotations__"]["value"] = object
    namespace["value"] = api.managed()
    cls = api.undoable(type("WriteParent", (), namespace))
    manager = api.UndoRedoManager()
    left_child = child_cls(transaction_manager=manager)
    right_child = child_cls(transaction_manager=manager)

    class Opaque:
        def __eq__(self, other):
            # Record only untimed setup checks; timed callbacks have no accumulation.
            return other == 7

    opaque = Opaque()
    if shape == "integer_equal":
        left = right = 7
    elif shape == "opaque_equal":
        left, right = 7, opaque
    elif shape == "child_alternate":
        left, right = left_child, right_child
    elif shape == "tuple_child_alternate":
        left, right = (left_child,), (right_child,)
    elif shape == "dict_child_alternate":
        left, right = MappingProxyType({"node": left_child}), MappingProxyType(
            {"node": right_child}
        )
    else:
        raise ValueError(shape)
    parent = cls(transaction_manager=manager, value=left)
    manager.initialize(parent, left_child, right_child)
    manager.begin()
    # Same value must skip; distinct node values must retain historical identity,
    # even when ordinary integrated child equality is structural.
    parent.value = left
    assert not manager._edit.touched
    parent.value = right
    expects_touch = shape.endswith("alternate")
    assert bool(manager._edit.touched) == expects_touch
    if expects_touch:
        parent.value = left
    if integrated:
        assert left_child == right_child
    run, source = runner(
        "obj.value = choices[index % 2]", {"obj": parent, "choices": (left, right)}
    )

    def prepare(_count):
        if expects_touch:
            parent.value = right
        return None

    return {
        "run": run,
        "source": source,
        "prepare": prepare if expects_touch else None,
        "classification": "full public managed setter inside one active transaction; untimed reset to right precedes each alternating batch so every timed operation changes node identity; no commit/rollback timed",
        "setup": {
            "shape": shape,
            "ordinary_managed_fields": count,
            "additional_value_field": 1,
            "child_fields": count,
            "callback": "opaque incoming value reflected equality with stable integer old; true equality skips storing unsupported opaque input; no accumulation",
        },
        "keepalive": (manager, parent, left_child, right_child),
        "cleanup": manager.rollback,
    }


def cases(product, baseline, count, runner):
    result = {"product": {}, "frozen_original": {}, "structural_reference": {}}
    product_cls = product.undoable(eq=True)(
        type("ProductEq", (), field_namespace(product, count))
    )
    left, right = setup_equal(product_cls, product)
    run, source = runner("result = left == right", {"left": left, "right": right})
    result["product"]["undoable_eq_prelude"] = {
        "run": run,
        "source": source,
        "prepare": None,
        "classification": "generated structural equality outside historical scope; full historical facade getters; no numerical parity promise",
    }
    reference_cls, reference_source = structural_reference(baseline, count)
    left, right = setup_equal(reference_cls, baseline)
    run, source = runner("result = left == right", {"left": left, "right": right})
    result["structural_reference"]["undoable_eq_prelude"] = {
        "run": run,
        "source": source,
        "prepare": None,
        "classification": "explicit handwritten frozen-baseline facade structural reference; no context prelude; comparison policy not a std dataclass",
        "reference_method_source": reference_source,
    }
    for shape in (
        "integer_equal",
        "opaque_equal",
        "child_alternate",
        "tuple_child_alternate",
        "dict_child_alternate",
    ):
        key = f"undoable_value_scope:{shape}"
        result["product"][key] = write_case(
            product, count, shape, runner, integrated=True
        )
        result["frozen_original"][key] = write_case(
            baseline, count, shape, runner, integrated=False
        )
    return result
