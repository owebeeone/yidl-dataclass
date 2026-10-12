"""Consumer-only external wheel/sdist and isolated installed-runtime gates."""

from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[3]
POINTER = Path(tempfile.gettempdir()) / "yidl-dataclass-stage-g-artifacts-pointer.txt"


def run(command, *, cwd, environment=None):
    result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True)
    if result.returncode:
        print(result.stdout.decode(errors="replace"))
        print(result.stderr.decode(errors="replace"))
        raise RuntimeError(
            f"consumer gate command failed ({result.returncode}): {command[0]}"
        )
    return result.stdout.decode()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package_rows(wheel, package):
    with zipfile.ZipFile(wheel) as archive:
        return {
            name: hashlib.sha256(archive.read(name)).hexdigest()
            for name in archive.namelist()
            if name.startswith(package + "/")
        }


CONFTEXT = """import importlib,importlib.metadata,json,os,pathlib,sys
import pytest
from astichi.lower_engine import select_effective_lower_engine

def pytest_sessionstart(session):
 expected=os.environ["STAGE_G_CONSUMER"]
 names=["astichi","yidl",expected]
 if expected=="yidl_undoable":names.append("yidl_lifecycle")
 rows={}
 for name in names:
  module=importlib.import_module(name)
  origin=pathlib.Path(module.__file__).resolve()
  assert origin.is_relative_to(pathlib.Path(sys.prefix).resolve()),(name,origin)
  rows[name]=origin.relative_to(pathlib.Path(sys.prefix).resolve()).as_posix()
 assert importlib.metadata.version("astichi")=="1.1.3"
 assert importlib.metadata.version("yidl")=="0.1.0"
 selected=select_effective_lower_engine().selected_engine
 assert selected==os.environ["ASTICHI_LOWER_ENGINE"]
 if os.environ.get("STAGE_G_WITHOUT_AUTHORITY")=="1":
  assert importlib.util.find_spec("yidl_dataclass") is None
 print("INSTALLED_GATE "+json.dumps({"python":sys.version.split()[0],"origins":rows,"backend":selected,"dataclass_absent":os.environ.get("STAGE_G_WITHOUT_AUTHORITY")=="1"},sort_keys=True))
"""


def prepare():
    authority = Path(os.environ["STAGE_G_WHEELHOUSE"])
    undoable = Path(os.environ["STAGE_G_UNDOABLE_ROOT"])
    roots = {"dataclass": ROOT, "undoable": undoable}
    artifact = Path(tempfile.mkdtemp(prefix="yidl-dataclass-stage-g-artifacts-"))
    POINTER.write_text(str(artifact))
    tuples = {}
    python = ROOT / ".venv/bin/python"
    for consumer, source in roots.items():
        folder = artifact / consumer
        folder.mkdir()
        run([str(python), "-m", "hatchling", "build", "-d", str(folder)], cwd=source)
        wheel = next(folder.glob("*.whl"))
        sdist = next(folder.glob("*.tar.gz"))
        extracted = folder / "extracted"
        extracted.mkdir()
        with tarfile.open(sdist) as archive:
            for member in archive.getmembers():
                name = Path(member.name)
                assert not name.is_absolute() and ".." not in name.parts
            archive.extractall(extracted, filter="data")
        rebuilt_root = next(extracted.iterdir())
        rebuilt = folder / "rebuilt"
        run(
            [
                str(python),
                "-m",
                "hatchling",
                "build",
                "-t",
                "wheel",
                "-d",
                str(rebuilt),
            ],
            cwd=rebuilt_root,
        )
        rebuilt_wheel = next(rebuilt.glob("*.whl"))
        package = "yidl_" + consumer
        rows = package_rows(wheel, package)
        assert rows == package_rows(rebuilt_wheel, package)
        assert digest(wheel) == digest(
            rebuilt_wheel
        ), "consumer wheel reproduction differs"
        required = [
            f"{package}/py.typed",
            f"{package}/_generated_{consumer}_base.py",
            f"{package}/regenerate_{consumer}_base.py",
            f"{package}/documentation/README.md",
            f"{package}/documentation/examples/first_use.py",
        ]
        assert all(name in rows for name in required)
        if consumer == "dataclass":
            assert "yidl_dataclass/yidl/shared/comparison.yidl" in rows
        else:
            assert "yidl_undoable/yidl/shared/comparison.yidl" not in rows
        test_root = artifact / f"{consumer}-tests"
        test_root.mkdir()
        shutil.copytree(
            source / "tests",
            test_root / "tests",
            ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"),
        )
        (test_root / "tests/conftest.py").write_text(CONFTEXT)
        (test_root / "pytest.ini").write_text(
            "[pytest]\npythonpath = tests\ntestpaths = tests\n"
        )
        tuples[consumer] = {
            "wheel": wheel.name,
            "wheel_sha256": digest(wheel),
            "wheel_bytes": wheel.stat().st_size,
            "sdist": sdist.name,
            "sdist_sha256": digest(sdist),
            "sdist_bytes": sdist.stat().st_size,
            "rebuilt_wheel_sha256": digest(rebuilt_wheel),
            "package_files": len(rows),
            "resource_count": sum(name.endswith(".yidl") for name in rows),
            "package_hashes": rows,
            "source_fallback": False,
        }
    sdk_files = [
        authority / "astichi-1.1.3-cp312-abi3-macosx_11_0_arm64.whl",
        authority / "yidl-0.1.0-py3-none-any.whl",
        authority / "yidl_cache-0.1.0-py3-none-any.whl",
        authority / "yidl_lifecycle-0.1.0-py3-none-any.whl",
    ]
    sdk_hashes = {path.name: digest(path) for path in sdk_files}
    expected = json.loads(
        (
            undoable / "docs/validation/stage-ef/environment-native-rust-312.json"
        ).read_text()
    )["original_wheel_sha256"]
    assert all(sdk_hashes[name] == value for name, value in expected.items())
    for minor in ("312", "313", "314"):
        source_python = ROOT / (
            ".venv/bin/python" if minor == "312" else f".venvs/py{minor}/bin/python"
        )
        executable = run(
            [str(source_python), "-c", "import sys;print(sys._base_executable)"],
            cwd=ROOT,
        ).strip()
        for without in (False, True):
            env = artifact / f"venv-{minor}{'-without-authority' if without else ''}"
            run(["uv", "venv", "--python", executable, str(env)], cwd=artifact)
            wheels = [
                *map(str, sdk_files),
                str(artifact / "undoable" / tuples["undoable"]["wheel"]),
            ]
            if not without:
                wheels.append(
                    str(artifact / "dataclass" / tuples["dataclass"]["wheel"])
                )
            run(
                [
                    "uv",
                    "pip",
                    "install",
                    "--python",
                    str(env / "bin/python"),
                    "--only-binary",
                    ":all:",
                    *wheels,
                    "pytest==9.1.1",
                    "black==26.3.1",
                    "hatchling==1.32.4",
                ],
                cwd=artifact,
            )
    (artifact / "artifact-tuple.json").write_text(
        json.dumps(
            {
                "consumers": tuples,
                "original_sdk_wheels": sdk_hashes,
                "dependency_builds": False,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    shutil.copyfile(
        artifact / "artifact-tuple.json",
        ROOT / "docs/validation/stage-g/artifact-tuple.json",
    )
    print(
        json.dumps(
            {
                "consumer_artifacts": {
                    name: {
                        key: value
                        for key, value in row.items()
                        if key != "package_hashes"
                    }
                    for name, row in tuples.items()
                },
                "original_sdk_wheels": sdk_hashes,
                "environments": 6,
            },
            sort_keys=True,
        )
    )


def installed(args):
    artifact = Path(POINTER.read_text())
    consumer = args.consumer
    without = args.without_authority
    assert not without or consumer == "undoable"
    python = (
        artifact
        / f"venv-{args.minor}{'-without-authority' if without else ''}"
        / "bin/python"
    )
    test_root = artifact / f"{consumer}-tests"
    environment = dict(
        os.environ,
        ASTICHI_LOWER_ENGINE=args.backend,
        STAGE_G_CONSUMER="yidl_" + consumer,
    )
    environment.pop("PYTHONPATH", None)
    if without:
        environment["STAGE_G_WITHOUT_AUTHORITY"] = "1"
    command = [
        str(python),
        "-I",
        "-m",
        "pytest",
        "-c",
        str(test_root / "pytest.ini"),
        "-q",
        "-s",
    ]
    if consumer == "dataclass":
        command += [
            "--ignore=tests/test_installation.py",
            "--ignore=tests/test_distribution_contract.py",
            "--ignore=tests/test_generation_stability.py",
        ]
    else:
        command += ["--ignore=tests/test_distribution_contract.py"]
        if without:
            command += [
                "--ignore=tests/test_generation.py",
                "--deselect=tests/test_canonical.py::test_generated_story[11_layers]",
                "--deselect=tests/test_comparison_source.py::test_undoable_scope_does_not_change_dataclass_equality",
            ]
    xml = (
        test_root
        / f"{consumer}-{args.backend}-{args.minor}{'-without-authority' if without else ''}.junit.xml"
    )
    command.append("--junitxml=" + str(xml))
    result = subprocess.run(
        command, cwd=test_root, env=environment, capture_output=True
    )
    print(result.stdout.decode(errors="replace"))
    print(result.stderr.decode(errors="replace"))
    destination = ROOT / "docs/validation/stage-g" / xml.name
    destination.write_bytes(xml.read_bytes())
    raw = destination.read_bytes()
    raw_root = Path(tempfile.gettempdir()) / "yidl-dataclass-stage-g-raw"
    raw_root.mkdir(exist_ok=True)
    raw_sha = hashlib.sha256(raw).hexdigest()
    (raw_root / f"{raw_sha}.raw").write_bytes(raw)
    cooked = raw.decode().replace(str(artifact), "[installed-artifact-root]")
    import socket, getpass

    cooked = (
        cooked.replace(str(Path.home()), "[home]")
        .replace(str(Path(tempfile.gettempdir()).resolve()), "[temp]")
        .replace(tempfile.gettempdir(), "[temp]")
        .replace(socket.gethostname(), "[host]")
        .replace(f"pytest-of-{getpass.getuser()}", "pytest-of-user")
    )
    destination.write_text(cooked)
    record = {
        "consumer": consumer,
        "backend": args.backend,
        "minor": args.minor,
        "dataclass_absent": without,
        "path": destination.relative_to(ROOT).as_posix(),
        "raw_sha256": raw_sha,
        "sha256": digest(destination),
        "exit_code": result.returncode,
    }
    with (ROOT / "docs/validation/stage-g/installed-junit.jsonl").open("a") as stream:
        stream.write(json.dumps(record, sort_keys=True) + "\n")
    return result.returncode


def refresh_final():
    artifact = Path(POINTER.read_text())
    initial = json.loads((artifact / "artifact-tuple.json").read_text())
    shutil.copyfile(
        ROOT / "docs/validation/stage-g/artifact-tuple.json",
        ROOT / "docs/validation/stage-g/artifact-tuple-initial.json",
    )
    final = dict(initial)
    final["consumers"] = {}
    roots = {"dataclass": ROOT, "undoable": Path(os.environ["STAGE_G_UNDOABLE_ROOT"])}
    python = ROOT / ".venv/bin/python"
    for consumer, source in roots.items():
        folder = artifact / (consumer + "-final")
        folder.mkdir()
        run([str(python), "-m", "hatchling", "build", "-d", str(folder)], cwd=source)
        wheel = next(folder.glob("*.whl"))
        sdist = next(folder.glob("*.tar.gz"))
        extracted = folder / "extracted"
        extracted.mkdir()
        with tarfile.open(sdist) as archive:
            assert all(
                not Path(member.name).is_absolute()
                and ".." not in Path(member.name).parts
                for member in archive.getmembers()
            )
            archive.extractall(extracted, filter="data")
        run(
            [
                str(python),
                "-m",
                "hatchling",
                "build",
                "-t",
                "wheel",
                "-d",
                str(folder / "rebuilt"),
            ],
            cwd=next(extracted.iterdir()),
        )
        rebuilt = next((folder / "rebuilt").glob("*.whl"))
        assert digest(wheel) == digest(rebuilt)
        package = "yidl_" + consumer
        rows = package_rows(wheel, package)
        previous = initial["consumers"][consumer]["package_hashes"]
        runtime = lambda data: {
            name: value for name, value in data.items() if "/documentation/" not in name
        }
        assert runtime(rows) == runtime(
            previous
        ), "runtime payload changed after installed corpus"
        final["consumers"][consumer] = {
            **initial["consumers"][consumer],
            "artifact_directory": folder.name,
            "wheel_sha256": digest(wheel),
            "wheel_bytes": wheel.stat().st_size,
            "sdist_sha256": digest(sdist),
            "sdist_bytes": sdist.stat().st_size,
            "rebuilt_wheel_sha256": digest(rebuilt),
            "package_hashes": rows,
            "installed_corpus_runtime_payload_unchanged": True,
        }
    for minor in ("312", "313", "314"):
        python = artifact / f"venv-{minor}" / "bin/python"
        for consumer in ("dataclass", "undoable"):
            row = final["consumers"][consumer]
            wheel = artifact / row["artifact_directory"] / row["wheel"]
            run(
                [
                    "uv",
                    "pip",
                    "install",
                    "--reinstall",
                    "--no-deps",
                    "--python",
                    str(python),
                    str(wheel),
                ],
                cwd=artifact,
            )
        without = artifact / f"venv-{minor}-without-authority" / "bin/python"
        row = final["consumers"]["undoable"]
        run(
            [
                "uv",
                "pip",
                "install",
                "--reinstall",
                "--no-deps",
                "--python",
                str(without),
                str(artifact / row["artifact_directory"] / row["wheel"]),
            ],
            cwd=artifact,
        )
    (artifact / "artifact-tuple-final.json").write_text(
        json.dumps(final, sort_keys=True, indent=2) + "\n"
    )
    (ROOT / "docs/validation/stage-g/artifact-tuple-final.json").write_text(
        json.dumps(final, sort_keys=True, indent=2) + "\n"
    )
    print(
        json.dumps(
            {
                "final_consumers": {
                    name: {
                        key: value
                        for key, value in row.items()
                        if key != "package_hashes"
                    }
                    for name, row in final["consumers"].items()
                },
                "runtime_payload_unchanged": True,
            },
            sort_keys=True,
        )
    )


def smoke(args):
    artifact = Path(POINTER.read_text())
    python = artifact / f"venv-{args.minor}" / "bin/python"
    environment = dict(os.environ, ASTICHI_LOWER_ENGINE=args.backend)
    environment.pop("PYTHONPATH", None)
    script = """import hashlib,importlib.metadata,importlib.resources,pathlib,runpy,sys
from astichi.lower_engine import select_effective_lower_engine
assert select_effective_lower_engine().selected_engine==sys.argv[1]
for name in ('astichi','yidl','yidl_dataclass','yidl_undoable'):
 module=__import__(name);assert pathlib.Path(module.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
from yidl_dataclass.regenerate_dataclass_base import render_dataclass_base_source
from yidl_undoable.regenerate_undoable_base import check_undoable_base
assert render_dataclass_base_source()==importlib.resources.files('yidl_dataclass').joinpath('_generated_dataclass_base.py').read_text()
assert check_undoable_base()==(True,'')
for name in ('yidl_dataclass','yidl_undoable'):
 root=importlib.resources.files(name)
 runpy.run_path(str(root.joinpath('documentation/examples/first_use.py')),run_name='__main__')
 assert root.joinpath('documentation/docs/API.md').read_text()
print('final-wheel-regeneration-examples-public-resources=PASS')
"""
    print(
        run(
            [str(python), "-I", "-c", script, args.backend],
            cwd=artifact,
            environment=environment,
        )
    )
    print(
        json.dumps(
            {
                "python_minor": args.minor,
                "backend": args.backend,
                "final_artifact_smoke": True,
                "runtime_payload_unchanged_from_installed_corpus": True,
            },
            sort_keys=True,
        )
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("prepare", "run", "refresh-final", "smoke"))
    parser.add_argument("--consumer", choices=("dataclass", "undoable"))
    parser.add_argument("--minor", choices=("312", "313", "314"))
    parser.add_argument("--backend", choices=("native-rust", "python"))
    parser.add_argument("--without-authority", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
        return 0
    if args.mode == "refresh-final":
        refresh_final()
        return 0
    if args.mode == "smoke":
        smoke(args)
        return 0
    return installed(args)


if __name__ == "__main__":
    raise SystemExit(main())
