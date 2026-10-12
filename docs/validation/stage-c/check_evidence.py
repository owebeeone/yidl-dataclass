"""Validate actual Stage C evidence and freeze consumer-owned file hashes."""

from __future__ import annotations
import hashlib
import json
from pathlib import Path
import socket
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = ROOT / "docs/validation/stage-c"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    rows = [
        json.loads(line)
        for line in (EVIDENCE / "increments.jsonl").read_text().splitlines()
    ]
    raw = Path(tempfile.gettempdir()) / "yidl-dataclass-stage-c-raw"
    references = []
    for row in rows:
        assert row["phase"] != "green" or row["exit_code"] == 0, row["increment"]
        for artifact in row["artifacts"]:
            assert (
                digest((ROOT / artifact["path"]).read_bytes()) == artifact["sha256"]
            ), artifact["path"]
            assert (
                digest((raw / f'{artifact["raw_sha256"]}.raw').read_bytes())
                == artifact["raw_sha256"]
            ), artifact["path"]
            references.append(artifact)
    suites = []
    xml_files = sorted(EVIDENCE.glob("*.junit.xml"))
    for path in xml_files:
        tree = ET.parse(path)
        if path.name.startswith("c09-final-"):
            suite = tree.getroot().find("testsuite")
            assert suite is not None
            assert (
                suite.attrib["errors"] == "0" and suite.attrib["failures"] == "0"
            ), path.name
            suites.append(
                {
                    "path": path.relative_to(ROOT).as_posix(),
                    **{
                        key: int(suite.attrib[key])
                        for key in ("tests", "failures", "errors", "skipped")
                    },
                }
            )
    assert len(suites) == 6
    paths = [ROOT / ".gitignore", ROOT / "README.md", ROOT / "pyproject.toml"]
    for directory in (ROOT / "src", ROOT / "tests", EVIDENCE):
        paths.extend(
            path
            for path in directory.rglob("*")
            if path.is_file()
            and "__pycache__" not in path.parts
            and path.name not in ("owned-manifest.json", "evidence-qa.json")
        )
    forbidden = (
        str(ROOT),
        str(Path.home()),
        tempfile.gettempdir(),
        socket.gethostname(),
    )
    for path in paths:
        text = path.read_text()
        assert not any(part in text for part in forbidden), path.relative_to(ROOT)
    qa = {
        "increments": len(rows),
        "artifact_references": len(references),
        "raw_hashes_verified": len(references),
        "sanitized_hashes_verified": len(references),
        "junit_files": len(xml_files),
        "final_full_runs": suites,
        "owned_text_hygiene_files": len(paths),
        "absolute_path_or_hostname_matches": 0,
        "owned_sdk_changes": False,
    }
    qa_path = EVIDENCE / "evidence-qa.json"
    qa_path.write_text(json.dumps(qa, sort_keys=True, indent=2) + "\n")
    paths.append(qa_path)
    prior = json.loads(
        (ROOT / "docs/validation/stage-b/owned-manifest.json").read_text()
    )
    previous = {item["path"]: item["sha256"] for item in prior["files"]}
    manifest = {
        "stage": "C",
        "baseline_owner_commit": "d3997d6f27f178b5b16df6e479f3e41c920b69cf",
        "dependencies": {"astichi": "1.1.3", "yidl": "0.1.0"},
        "evidence_index": "docs/validation/stage-c/increments.jsonl",
        "corrections": "docs/validation/stage-c/corrections.jsonl",
        "raw_archive": "external:yidl-dataclass-stage-c-raw",
        "files": [],
    }
    for path in sorted(paths):
        data = path.read_bytes()
        name = path.relative_to(ROOT).as_posix()
        sha = digest(data)
        manifest["files"].append(
            {
                "path": name,
                "bytes": len(data),
                "sha256": sha,
                "stage_b_relation": (
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
                "manifest_sha256": digest(output.read_bytes()),
                "evidence_qa_sha256": digest(qa_path.read_bytes()),
                "raw_archive": "external:yidl-dataclass-stage-c-raw",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
