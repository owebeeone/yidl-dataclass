"""Verify G raw/sanitized evidence, artifact relation and owned file tuple."""

from __future__ import annotations
import hashlib
import json
from pathlib import Path
import socket
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = ROOT / "docs/validation/stage-g"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    rows = [
        json.loads(line)
        for line in (EVIDENCE / "increments.jsonl").read_text().splitlines()
    ]
    installed = [
        json.loads(line)
        for line in (EVIDENCE / "installed-junit.jsonl").read_text().splitlines()
    ]
    raw = Path(tempfile.gettempdir()) / "yidl-dataclass-stage-g-raw"
    references = []
    for row in rows:
        assert row["phase"] != "green" or row["exit_code"] == 0
        references.extend(row["artifacts"])
    references.extend(installed)
    for item in references:
        assert digest(ROOT / item["path"]) == item["sha256"], item["path"]
        assert digest(raw / (item["raw_sha256"] + ".raw")) == item["raw_sha256"]
    assert len(installed) == 18
    expected = {
        (consumer, backend, minor, absent)
        for consumer, absent in (
            ("dataclass", False),
            ("undoable", False),
            ("undoable", True),
        )
        for backend in ("native-rust", "python")
        for minor in ("312", "313", "314")
    }
    assert {
        (row["consumer"], row["backend"], row["minor"], row["dataclass_absent"])
        for row in installed
    } == expected
    suites = []
    for row in installed:
        suite = ET.parse(ROOT / row["path"]).getroot().find("testsuite")
        assert suite is not None and row["exit_code"] == 0
        assert suite.attrib["failures"] == "0" and suite.attrib["errors"] == "0"
        count = (
            197
            if row["consumer"] == "dataclass"
            else 334 if row["dataclass_absent"] else 341
        )
        assert int(suite.attrib["tests"]) == count
        skips = (
            (3 if row["minor"] == "312" else 2 if row["minor"] == "313" else 1)
            if row["consumer"] == "dataclass"
            else 0
        )
        assert int(suite.attrib["skipped"]) == skips
        suites.append(
            {
                key: row[key]
                for key in ("path", "consumer", "backend", "minor", "dataclass_absent")
            }
            | {"tests": count, "skipped": skips, "passed": count - skips}
        )
    successes = {row["increment"] for row in rows if row["exit_code"] == 0}
    assert all(
        f"g09-source-only-{backend}-{minor}" in successes
        and f"g11-final-smoke-{backend}-{minor}" in successes
        for backend in ("native-rust", "python")
        for minor in ("312", "313", "314")
    )
    initial = json.loads((EVIDENCE / "artifact-tuple-initial.json").read_text())
    final = json.loads((EVIDENCE / "artifact-tuple-final.json").read_text())
    for consumer in ("dataclass", "undoable"):
        before = initial["consumers"][consumer]
        after = final["consumers"][consumer]
        runtime = lambda row: {
            name: value
            for name, value in row["package_hashes"].items()
            if "/documentation/" not in name
        }
        assert runtime(before) == runtime(after)
        assert after["wheel_sha256"] == after["rebuilt_wheel_sha256"]
    prior = json.loads(
        (ROOT / "docs/validation/stage-d/owned-manifest.json").read_text()
    )
    previous = {row["path"]: row["sha256"] for row in prior["files"]}
    paths = [
        ROOT / name
        for name in (
            "README.md",
            "pyproject.toml",
            ".gitignore",
            "docs/API.md",
            "docs/Generation.md",
        )
    ]
    for directory in (ROOT / "src", ROOT / "tests", ROOT / "examples", EVIDENCE):
        paths.extend(
            path
            for path in directory.rglob("*")
            if path.is_file()
            and "__pycache__" not in path.parts
            and path.name not in ("owned-manifest.json", "evidence-qa.json")
        )
    assert all(
        previous[path.relative_to(ROOT).as_posix()] == digest(path)
        for path in paths
        if path.relative_to(ROOT).as_posix().startswith("src/")
    )
    forbidden = (
        str(ROOT),
        str(Path.home()),
        tempfile.gettempdir(),
        socket.gethostname(),
    )
    for path in paths:
        assert not any(
            part in path.read_text() for part in forbidden
        ), path.relative_to(ROOT)
    xmls = sorted(EVIDENCE.glob("*.junit.xml"))
    for path in xmls:
        ET.parse(path)
    qa = {
        "increments": len(rows),
        "installed_runs": len(installed),
        "artifact_references": len(references),
        "distinct_raw_hashes": len({row["raw_sha256"] for row in references}),
        "junit_files": len(xmls),
        "installed_suites": suites,
        "source_only_gate_runs": 6,
        "final_artifact_smoke_runs": 6,
        "absolute_path_or_hostname_matches": 0,
        "runtime_source_unchanged_from_d": True,
        "final_runtime_payload_unchanged_from_installed_corpus": True,
        "sdk_or_lifecycle_changes_or_builds": False,
        "cold_public_author_attempt": "pending owner",
    }
    qa_path = EVIDENCE / "evidence-qa.json"
    qa_path.write_text(json.dumps(qa, sort_keys=True, indent=2) + "\n")
    paths.append(qa_path)
    manifest = {
        "stage": "G public/package checkpoint",
        "baseline_owner_commit": "ac0aba3c11d3b6e33cf98d8c8ec22e67b4d0f145",
        "evidence_index": "docs/validation/stage-g/increments.jsonl",
        "raw_archive": "external:yidl-dataclass-stage-g-raw",
        "final_artifacts": "docs/validation/stage-g/artifact-tuple-final.json",
        "files": [],
    }
    for path in sorted(paths):
        name = path.relative_to(ROOT).as_posix()
        sha = digest(path)
        manifest["files"].append(
            {
                "path": name,
                "sha256": sha,
                "bytes": path.stat().st_size,
                "stage_d_relation": (
                    "new"
                    if name not in previous
                    else "unchanged" if previous[name] == sha else "changed"
                ),
            }
        )
    output = EVIDENCE / "owned-manifest.json"
    output.write_text(json.dumps(manifest, sort_keys=True, indent=2) + "\n")
    print(
        json.dumps(
            {
                "owned_files": len(paths),
                "manifest_sha256": digest(output),
                "qa_sha256": digest(qa_path),
                "final_artifact_tuple_sha256": digest(
                    EVIDENCE / "artifact-tuple-final.json"
                ),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
