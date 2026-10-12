"""Structural projection of the canonical artifacts, independent of behavior."""

import ast
from pathlib import Path
from importlib.resources import files
from yidl.testing.versioned_test_harness import data_golden_dir

ROOT = Path(__file__).resolve().parents[1]


def test_plain_canonical_has_direct_stores_and_plain_class():
    import json
    import sys

    directory = data_golden_dir(ROOT) / "dataclass_plain"
    manifest = json.loads((directory / "runtime_manifest.json").read_text())
    filename = manifest["generated_output.py"][
        f"py{sys.version_info.major}{sys.version_info.minor}"
    ]
    tree = ast.parse((directory / filename).read_text())
    declaration = next(node for node in tree.body if isinstance(node, ast.ClassDef))
    assert declaration.decorator_list == []
    method = next(
        node for node in declaration.body if isinstance(node, ast.FunctionDef)
    )
    targets = [node.targets[0] for node in method.body if isinstance(node, ast.Assign)]
    assert [target.attr for target in targets] == ["count", "label", "reserve"]
    assert all(
        isinstance(target.value, ast.Name) and target.value.id == "self"
        for target in targets
    )
    assert not any(isinstance(node, ast.Call) for node in ast.walk(method))


def test_source_policy_resources_and_decorator_use_sdk_composition():
    package = files("yidl_dataclass")
    source = (package / "dataclass.py").read_text()
    assert "build_DataclassModule" in source and ".to_executable_ast()" in source
    tree = ast.parse(source)
    assert not any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr
        in ("parse", "fix_missing_locations", "unparse", "_process_class", "_init_fn")
        for node in ast.walk(tree)
    )
    template = (package / "yidl/dataclass_core.yidl").read_text()
    assert "self, params__astichi_param_hole__" in template
    assert ".astichi_ref(external=slot_name)._" in template
    assert (
        "matcher ParamContributions" in template
        and "matcher StoreContributions" in template
    )


def test_comparison_resources_generate_direct_specialized_plain_methods():
    import json
    import sys

    directory = data_golden_dir(ROOT) / "dataclass_comparisons"
    manifest = json.loads((directory / "runtime_manifest.json").read_text())
    filename = manifest["generated_output.py"][
        f"py{sys.version_info.major}{sys.version_info.minor}"
    ]
    tree = ast.parse((directory / filename).read_text())
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    assert all(not cls.decorator_list for cls in classes)
    methods = {
        node.name: node for node in classes[0].body if isinstance(node, ast.FunctionDef)
    }
    eq = methods["__eq__"]
    assert {node.attr for node in ast.walk(eq) if isinstance(node, ast.Attribute)} >= {
        "sku",
        "price",
        "currency",
        "tags",
    }
    assert not any(isinstance(node, ast.Call) for node in ast.walk(eq))
    for name in ("__lt__", "__le__", "__gt__", "__ge__", "__hash__"):
        calls = [node for node in ast.walk(methods[name]) if isinstance(node, ast.Call)]
        assert all(
            isinstance(node.func, ast.Name) and node.func.id == "hash" for node in calls
        )
    source = files("yidl_dataclass").joinpath("yidl/shared/comparison.yidl").read_text()
    assert (
        "EqPreludeContributions" in source and "matcher EqStepContributions" in source
    )
    assert not any(
        name in source for name in ("dataclass", "RuntimeFacade", "ContextVar")
    )
    adapter = (
        files("yidl_dataclass").joinpath("yidl/dataclass_comparison.yidl").read_text()
    )
    assert "comparison.ComparisonCore" in adapter and "ComparisonMethods" in adapter


def test_constant_expression_carrier_has_direct_hash_operation_sequence():
    import dis
    from yidl_dataclass import dataclass

    @dataclass(unsafe_hash=True, repr=False)
    class Direct:
        first: int
        second: int

    def reference(self):
        return hash((self.first, self.second))

    def instructions(function):
        return [
            (
                "LOAD_FAST" if item.opname == "LOAD_FAST_BORROW" else item.opname,
                item.argval,
            )
            for item in dis.get_instructions(function)
        ]

    assert instructions(Direct.__hash__) == instructions(reference)


def test_policy_canonical_has_field_local_backing_and_direct_callback_calls():
    import json
    import sys

    directory = data_golden_dir(ROOT) / "dataclass_policies"
    manifest = json.loads((directory / "runtime_manifest.json").read_text())
    name = manifest["generated_output.py"][
        f"py{sys.version_info.major}{sys.version_info.minor}"
    ]
    tree = ast.parse((directory / name).read_text())
    declarations = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    assert all(not node.decorator_list for node in declarations)
    processed = declarations[0]
    assignment = next(
        node
        for node in processed.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "units"
            for target in node.targets
        )
    )
    assert isinstance(assignment.value, ast.Call)
    assert assignment.value.func.id == "_y_dc_property"
    accessor_names = [argument.id for argument in assignment.value.args]
    methods = {
        node.name: node for node in processed.body if isinstance(node, ast.FunctionDef)
    }
    getter, setter, deleter = [methods[name] for name in accessor_names]
    assert all(not method.decorator_list for method in (getter, setter, deleter))
    assert isinstance(getter.body[0].value, ast.Attribute)
    assert getter.body[0].value.attr == "_y_dc_store_1"
    callbacks = [
        node.func.id
        for node in ast.walk(setter)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    ]
    assert "_y_dc_converter_1" in callbacks and "_y_dc_validator_1" in callbacks
    assert not any(
        isinstance(node, ast.Name)
        and node.id in ("getattr", "setattr", "storage_fields", "_pipeline")
        for node in ast.walk(setter)
    )
    stores = [node.targets[0] for node in setter.body if isinstance(node, ast.Assign)]
    assert any(
        isinstance(target, ast.Attribute) and target.attr == "_y_dc_store_1"
        for target in stores
    )
    init = next(
        node
        for node in processed.body
        if isinstance(node, ast.FunctionDef) and node.name == "__init__"
    )
    assert any(
        isinstance(node, ast.Attribute)
        and node.attr == "total"
        and isinstance(node.ctx, ast.Store)
        for node in ast.walk(init)
    )


def test_descriptor_invokes_specialized_bodies_without_runtime_dispatch():
    import dis
    from yidl_dataclass import dataclass, const, lazy

    @dataclass(repr=False)
    class Direct:
        property: int = const(default=1)
        later: int = lazy(default_factory=lambda: 2, mutable=True)

    for name in ("property", "later"):
        descriptor = Direct.__dict__[name]
        assert type(descriptor) is property
        for body in (descriptor.fget, descriptor.fset, descriptor.fdel):
            assert Direct.__dict__[body.__name__] is body
            assert body.__globals__["_y_dc_property"] is property
            assert not {"getattr", "setattr", "storage_fields", "_pipeline"} & {
                instruction.argval
                for instruction in dis.get_instructions(body)
                if instruction.opname == "LOAD_GLOBAL"
            }
    getter = Direct.later.fget
    assert {
        item.argval
        for item in dis.get_instructions(getter)
        if item.opname == "LOAD_ATTR"
    } >= {"_y_dc_ready_1", "_y_dc_store_1", "_y_dc_busy_1"}
