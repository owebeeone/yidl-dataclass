"""Consumer-root canonical generated source/behavior coverage."""
from pathlib import Path
import runpy
import pytest
from support.golden_case import run_multi_source_case
from yidl.testing.versioned_test_harness import discover_golden_cases, data_gold_src_dir, data_golden_dir

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("case", discover_golden_cases(ROOT))
def test_canonical_case(case, tmp_path):
    source_path = data_gold_src_dir(ROOT) / case
    sources = run_multi_source_case(source_path, runpy.run_path(str(source_path))["render_case"]())
    expected = data_golden_dir(ROOT) / Path(case).stem
    for name, actual in sources.items():
        (tmp_path / name).write_text(actual)
        assert actual == (expected / name).read_text(), name
