"""Execute the user-facing examples and complete guide blocks against the install."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import re
import runpy

ROOT = Path(__file__).resolve().parents[2]
GUIDES = (
    "README.md", "docs/GettingStarted.md", "docs/Concepts.md",
    "docs/Initialization.md", "docs/LazyFields.md", "docs/Freezing.md",
    "docs/ModelOperations.md", "docs/Generation.md",
)


def check():
    examples = sorted((ROOT / "examples").glob("*.py"))
    for path in examples:
        with redirect_stdout(io.StringIO()):
            runpy.run_path(str(path), run_name="__main__")
        print("PASS", path.relative_to(ROOT))

    count = 0
    for name in GUIDES:
        path = ROOT / name
        namespace = {"__name__": "__main__", "__file__": str(path)}
        with redirect_stdout(io.StringIO()):
            for block in re.findall(r"```python\n(.*?)```", path.read_text(), re.S):
                exec(compile(block, str(path), "exec"), namespace)
                count += 1
        print("PASS guide", name)
    evidence = {"examples": len(examples), "guide_blocks": count}
    output = ROOT / "build/docs-example-evidence.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(evidence, indent=2) + "\n")
    return evidence


if __name__ == "__main__":
    print(json.dumps(check(), sort_keys=True))
