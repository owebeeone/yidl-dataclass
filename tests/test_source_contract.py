"""Structural projection of the canonical artifacts, independent of behavior."""
import ast
from pathlib import Path
from yidl.testing.versioned_test_harness import data_golden_dir

ROOT = Path(__file__).resolve().parents[1]


def test_plain_canonical_has_direct_stores_and_plain_class():
    tree = ast.parse((data_golden_dir(ROOT) / "dataclass_plain/generated_output.py").read_text())
    declaration = next(node for node in tree.body if isinstance(node, ast.ClassDef))
    assert declaration.decorator_list == []
    method = next(node for node in declaration.body if isinstance(node, ast.FunctionDef))
    targets = [node.targets[0] for node in method.body if isinstance(node, ast.Assign)]
    assert [target.attr for target in targets] == ["count", "label", "reserve"]
    assert all(isinstance(target.value, ast.Name) and target.value.id == "self" for target in targets)
    assert not any(isinstance(node, ast.Call) for node in ast.walk(method))


def test_source_policy_resources_and_decorator_use_sdk_composition():
    package = ROOT / "src/yidl_dataclass"
    source = (package / "dataclass.py").read_text()
    assert "build_DataclassModule" in source and ".to_executable_ast()" in source
    tree = ast.parse(source)
    assert not any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in ("parse", "fix_missing_locations", "unparse", "_process_class", "_init_fn") for node in ast.walk(tree))
    template = (package / "yidl/dataclass_core.yidl").read_text()
    assert "self, params__astichi_param_hole__" in template
    assert ".astichi_ref(external=slot_name)._" in template
    assert "matcher ParamContributions" in template and "matcher StoreContributions" in template
