"""Stage A consumer wheel manifests; isolated execution is Stage G's gate."""

from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def test_consumer_wheel_contains_resources_and_locked_sdk_metadata(tmp_path):
    subprocess.run(
        [
            sys.executable,
            "-m",
            "hatchling",
            "build",
            "-t",
            "wheel",
            "-d",
            str(tmp_path),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    wheel = next(tmp_path.glob("*.whl"))
    with zipfile.ZipFile(wheel) as archive:
        names = archive.namelist()
        assert "yidl_dataclass/yidl/dataclass_core.yidl" in names
        assert "yidl_dataclass/yidl/dataclass_base.yidl" in names
        for module in ("factories", "providers", "pipelines", "policies"):
            assert f"yidl_dataclass/yidl/dataclass_{module}.yidl" in names
        assert "yidl_dataclass/yidl/dataclass_comparison.yidl" in names
        assert "yidl_dataclass/yidl/shared/comparison.yidl" in names
        assert "yidl_dataclass/py.typed" in names
        assert "yidl_dataclass/_generated_dataclass_base.py" in names
        metadata = archive.read(
            next(name for name in names if name.endswith("/METADATA"))
        ).decode()
        assert "Requires-Dist: astichi==1.1.3" in metadata
        assert "Requires-Dist: yidl==0.1.0" in metadata
