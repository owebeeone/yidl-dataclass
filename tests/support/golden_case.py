"""Consumer multi-source canonical convention with explicit-root paths."""
from __future__ import annotations
from collections.abc import Mapping
from importlib.resources import files
from pathlib import Path
import black


def run_multi_source_case(source_path: Path, sources: Mapping[str, str]) -> dict[str, str]:
    """Expose behavior, authored binding fixture, emitted base and readable models."""
    result = dict(sources)
    result["bindings.py"] = source_path.read_text()
    result["decorator.py"] = files("yidl_dataclass").joinpath("_generated_dataclass_base.py").read_text()
    for stem in ("decorator", "generated_output"):
        result[f"{stem}_prettier.py"] = black.format_str(result[f"{stem}.py"], mode=black.FileMode())
    return result
