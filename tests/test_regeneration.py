"""Package-based source regeneration, with no SDK source-tree dependency."""
from importlib.resources import files
from yidl_dataclass.regenerate_dataclass_base import render_dataclass_base_source, main


def test_committed_base_matches_authoritative_resources():
    assert render_dataclass_base_source() == files("yidl_dataclass").joinpath("_generated_dataclass_base.py").read_text()
    assert main([]) == 0
