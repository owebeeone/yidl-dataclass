"""Explicit canonical artifact refresh after independent fixture oracles pass."""

from pathlib import Path
import json
import runpy
import sys
from support.golden_case import run_multi_source_case
from yidl.testing.versioned_test_harness import (
    discover_golden_cases,
    data_gold_src_dir,
    data_golden_dir,
)

ROOT = Path(__file__).resolve().parents[2]
VERSIONED = {
    "dataclass_plain",
    "dataclass_layout",
    "dataclass_metadata",
    "dataclass_comparisons",
    "dataclass_method_actions",
    "comparison_neutral",
    "dataclass_initialization",
    "dataclass_providers",
    "dataclass_policies",
    "dataclass_pipeline_ownership",
    "dataclass_lazy",
    "dataclass_lazy_retention",
    "dataclass_inheritance_helpers",
    "dataclass_copy",
    "dataclass_dictionary_copy",
    "dataclass_field_removal",
    "dataclass_result_names",
    "dataclass_freezable",
    "dataclass_freeze_inferred",
}


def main():
    minor = f"py{sys.version_info.major}{sys.version_info.minor}"
    selected = set(sys.argv[1:])
    for case in discover_golden_cases(ROOT):
        if selected and case not in selected:
            continue
        source_path = data_gold_src_dir(ROOT) / case
        sources = run_multi_source_case(
            source_path, runpy.run_path(str(source_path))["render_case"]()
        )
        expected = data_golden_dir(ROOT) / Path(case).stem
        expected.mkdir(parents=True, exist_ok=True)
        manifest = (
            {
                name: {
                    f"py3{minor}": name.replace(".py", f"_py3{minor}.py")
                    for minor in (12, 13, 14, 15)
                }
                for name in ("generated_output.py", "generated_output_prettier.py")
            }
            if Path(case).stem in VERSIONED
            else {}
        )
        for name, actual in sources.items():
            (expected / manifest.get(name, {}).get(minor, name)).write_text(actual)
        if manifest:
            (expected / "runtime_manifest.json").write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n"
            )
            for name in manifest:
                (expected / name).unlink(missing_ok=True)


if __name__ == "__main__":
    main()
