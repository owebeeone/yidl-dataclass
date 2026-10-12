"""Second native YIDL consumer: inherited nested operand matcher specialization."""

from importlib.resources import files
from pathlib import Path
from types import SimpleNamespace
import sys
from yidl.concept_parser import compile_yidl_files
from yidl.generation.data_def_sys import emit_concept_runtime_source


def render_case():
    resource = (
        files("yidl_dataclass").joinpath("yidl/shared/comparison.yidl").read_text()
    )
    fixture = Path(__file__).parent.parent / "yidl/comparison_neutral.yidl"
    concept = compile_yidl_files(
        {"shared/comparison.yidl": resource, "neutral.yidl": fixture.read_text()},
        "neutral.yidl",
    ).concepts["NeutralComparison"]
    runtime = emit_concept_runtime_source(
        concept.plan.build_data_definition(),
        resources=concept.resources,
        assembly_plan=concept,
    )
    capture = {}
    exec(compile(runtime, "<neutral-runtime>", "exec", dont_inherit=True), capture)
    builder = capture["new_builder"]()
    builder.add(
        capture["ComparisonClassesCollection"],
        capture["ComparisonClass"](
            cmp_class_id="Nested",
            cmp_eq=True,
            cmp_order=True,
            cmp_hash=True,
            use_tuple_equality=sys.version_info[:2] == (3, 12),
            has_compare_operands=True,
            has_hash_operands=True,
        ),
    )
    for index, name in enumerate(("rank", "size")):
        builder.add(
            capture["ComparisonOperandsCollection"],
            capture["ComparisonOperand"](
                cmp_operand_id=name,
                cmp_owner="Nested",
                cmp_operand_order=index,
                cmp_read_path=name,
                cmp_last=index == 1,
            ),
        )
    piece = capture["build_NeutralModule"](builder.freeze())
    tree = piece.to_executable_ast()
    exec(compile(tree, "<neutral-class>", "exec", dont_inherit=True), capture)
    Neutral = capture["Neutral"]
    first = Neutral(SimpleNamespace(rank=2, size=4))
    equal = Neutral(SimpleNamespace(rank=2, size=4))
    later = Neutral(SimpleNamespace(rank=2, size=7))
    assert first == equal and first < later and hash(first) == hash((2, 4))
    assert not hasattr(Neutral, "__dataclass_fields__") and not hasattr(
        first, "__dict__"
    )
    source = piece.emit_commented()
    assert "self.payload.rank" in source and "other.payload.size" in source
    return {
        "generated_output.py": source,
        "behavior.txt": "neutral-slots=payload; dataclass-metadata=False; nested-eq=True; nested-order=True; nested-hash=True\n",
    }
