"""Frozen source/artifact identity checks before any benchmark interval."""

import hashlib
import importlib.util
import importlib.metadata
import json
from pathlib import Path
import sys
import zipfile

SOURCE_ROOT = Path(__file__).parent
BASELINE_SHA256 = "e63818caa79b4c361d8c6203f572f79d4bb098f6ece09a3bf6b149e6206e5620"


def canonical_digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def source_hashes():
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(SOURCE_ROOT.glob("*.py"))
    }


def verify_wheel(path, expected_sha256):
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected_sha256:
        raise ValueError("frozen wheel digest mismatch: " + path.name)
    rows = {}
    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            parts = Path(name).parts
            if name.endswith("/") or not parts or parts[0].endswith(".dist-info"):
                continue
            if Path(name).is_absolute() or ".." in parts or parts[0].endswith(".data"):
                raise ValueError("unsupported wheel payload path")
            actual = Path(sys.prefix).joinpath(
                "lib",
                f"python{sys.version_info.major}.{sys.version_info.minor}",
                "site-packages",
                name,
            )
            if not actual.is_file() or actual.read_bytes() != archive.read(name):
                raise ValueError("installed payload differs from frozen wheel: " + name)
            rows[name] = hashlib.sha256(archive.read(name)).hexdigest()
    return rows


def verify_installation(artifact_tuple, artifact_root, sdk_wheel_dir, *, backend):
    artifact_root, sdk_wheel_dir = Path(artifact_root), Path(sdk_wheel_dir)
    versions = {
        "astichi": "1.1.3",
        "yidl": "0.1.0",
        "yidl-cache": "0.1.0",
        "yidl-lifecycle": "0.1.0",
        "yidl-dataclass": "0.1.0.dev0",
        "yidl-undoable": "0.1.0",
    }
    for name, version in versions.items():
        if importlib.metadata.version(name) != version:
            raise ValueError("installed version differs from frozen tuple: " + name)
    origins = {}
    for name in (
        "astichi",
        "yidl",
        "yidl_cache",
        "yidl_lifecycle",
        "yidl_dataclass",
        "yidl_undoable",
    ):
        spec = importlib.util.find_spec(name)
        path = Path(spec.origin).resolve()
        if not path.is_relative_to(Path(sys.prefix).resolve()):
            raise ValueError("benchmark source/editable fallback forbidden: " + name)
        origins[name] = path.relative_to(Path(sys.prefix).resolve()).as_posix()
    for name, row in artifact_tuple["consumers"].items():
        path = artifact_root / row["artifact_directory"] / row["wheel"]
        verified = verify_wheel(path, row["wheel_sha256"])
        if verified != row["package_hashes"]:
            raise ValueError(
                "consumer package inventory differs from frozen tuple: " + name
            )
    sdk_payloads = {
        name: verify_wheel(sdk_wheel_dir / name, sha)
        for name, sha in artifact_tuple["original_sdk_wheels"].items()
    }
    from astichi.lower_engine.native import select_lower_engine

    selection = select_lower_engine()
    if selection.selected_engine != backend or selection.fallback_scope is not None:
        raise ValueError("actual benchmark backend mismatch or fallback")
    import dataclasses

    return {
        "artifact_tuple_sha256": canonical_digest(artifact_tuple),
        "versions": versions,
        "origins_relative_to_prefix": origins,
        "sdk_payload_inventory_sha256": canonical_digest(sdk_payloads),
        "source_sha256": source_hashes(),
        "backend": backend,
        "python": sys.version.split()[0],
        "stdlib_dataclasses_sha256": hashlib.sha256(
            Path(dataclasses.__file__).read_bytes()
        ).hexdigest(),
    }
