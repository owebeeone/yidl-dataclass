"""Stage G distribution/public-documentation artifact contract (test first)."""

from pathlib import Path
import subprocess
import sys
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def test_wheel_and_sdist_include_public_documentation_and_example(tmp_path):
    subprocess.run(
        [sys.executable, "-m", "hatchling", "build", "-d", str(tmp_path)],
        cwd=ROOT,
        capture_output=True,
        check=True,
    )
    with zipfile.ZipFile(next(tmp_path.glob("*.whl"))) as wheel:
        names = set(wheel.namelist())
        for name in (
            "README.md",
            "docs/API.md",
            "docs/Generation.md",
            "examples/first_use.py",
        ):
            packaged = "yidl_dataclass/documentation/" + name
            assert packaged in names, name
            assert wheel.read(packaged) == (ROOT / name).read_bytes()
    with tarfile.open(next(tmp_path.glob("*.tar.gz"))) as sdist:
        names = {name.partition("/")[2] for name in sdist.getnames()}
        assert {
            "README.md",
            "docs/API.md",
            "docs/Generation.md",
            "examples/first_use.py",
        } <= names
