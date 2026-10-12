"""Locate own external G environments and invoke only untimed preparation gates."""

import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("definition", "setup", "cold-setup", "mechanics"))
    parser.add_argument("--minor", choices=("312", "313", "314"), required=True)
    parser.add_argument("--junitxml", type=Path)
    args = parser.parse_args()
    artifact = Path(
        (
            Path(tempfile.gettempdir()) / "yidl-dataclass-stage-g-artifacts-pointer.txt"
        ).read_text()
    )
    python = artifact / f"venv-{args.minor}" / "bin/python"
    benchmark = ROOT / "tests/data/perf"
    evidence = ROOT / "docs/validation/stage-h2-preparation"
    common = [
        "--artifact-root",
        str(artifact),
        "--sdk-wheel-dir",
        os.environ["PERF_SDK_WHEELHOUSE"],
    ]
    baseline = [
        "--undoable-baseline-dir",
        os.environ["PERF_BASELINE_DIR"],
        "--undoable-baseline-wheel",
        os.environ["PERF_BASELINE_WHEEL"],
    ]
    environment = dict(os.environ, ASTICHI_LOWER_ENGINE="native-rust")
    environment.pop("PYTHONPATH", None)
    if args.mode == "mechanics":
        command = [str(python), "-I", "-m", "pytest", "-p", "no:cacheprovider", "-c", os.devnull, str(benchmark), "-q"]
        if args.junitxml:
            command.append("--junitxml=" + str(ROOT / args.junitxml))
        return subprocess.run(command, cwd=artifact, env=environment).returncode
    if args.mode == "definition":
        command = [
            str(python),
            "-I",
            str(benchmark / "definition.py"),
            "--artifact-tuple",
            str(ROOT / "docs/validation/stage-g/artifact-tuple-final.json"),
            *common,
            *baseline,
            "--output",
            str(evidence / f"definition-final-{args.minor}.json"),
        ]
        return subprocess.run(command, cwd=artifact, env=environment).returncode
    if args.mode == "setup":
        command = [
            str(python),
            "-I",
            str(benchmark / "setup_check.py"),
            "--artifact-tuple",
            str(ROOT / "docs/validation/stage-g/artifact-tuple-final.json"),
            *common,
            *baseline,
            "--output",
            str(evidence / f"setup-final-{args.minor}.json"),
        ]
        return subprocess.run(command, cwd=artifact, env=environment).returncode
    for variant in ("product", "stdlib_default", "stdlib_slots"):
        for count in (3, 12):
            command = [
                str(python),
                "-I",
                str(benchmark / "cold_worker.py"),
                "--variant",
                variant,
                "--fields",
                str(count),
                *common,
                "--definition",
                str(evidence / "definition.json"),
                "--setup-only",
            ]
            result = subprocess.run(command, cwd=artifact, env=environment)
            if result.returncode:
                return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
