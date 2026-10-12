"""Run a consumer test command and preserve raw/sanitized append-only evidence."""

from __future__ import annotations
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import socket
import getpass
import subprocess
import sys
import tempfile
import time


def main() -> int:
    increment, phase, deficiency, *command = sys.argv[1:]
    root = Path.cwd()
    dest = root / "docs/validation/final-rem1-drafter"
    dest.mkdir(parents=True, exist_ok=True)
    stem = f"{increment}-{phase}"
    log_path = dest / f"{stem}.log"
    xml_path = dest / f"{stem}.junit.xml"
    if log_path.exists():
        raise RuntimeError("Evidence exists; use a new attempt name")
    raw_root = Path(tempfile.gettempdir()) / "yidl-dataclass-final-rem1-drafter-raw"
    raw_root.mkdir(exist_ok=True)
    started = dt.datetime.now(dt.UTC).isoformat()
    then = time.perf_counter()
    arguments = (
        [*command, f"--junitxml={xml_path.relative_to(root)}"]
        if "pytest" in command
        else command
    )
    result = subprocess.run(arguments, capture_output=True)
    elapsed = time.perf_counter() - then
    output = result.stdout + result.stderr
    artifacts = []
    raw_artifacts = [(log_path.name, output)]
    if xml_path.exists():
        raw_artifacts.append((xml_path.name, xml_path.read_bytes()))
    for name, raw in raw_artifacts:
        digest = hashlib.sha256(raw).hexdigest()
        (raw_root / f"{digest}.raw").write_bytes(raw)
        text = raw.decode(errors="replace")
        prefixes = (
            (str(root), "[consumer-root]"),
            (str(Path.home()), "[home]"),
            (str(Path(tempfile.gettempdir()).resolve()), "[temp]"),
            (tempfile.gettempdir(), "[temp]"),
            (str(Path(sys.base_prefix).resolve()), "[runtime-root]"),
            (sys.base_prefix, "[runtime-root]"),
            (socket.gethostname(), "[host]"),
            (f"pytest-of-{getpass.getuser()}", "pytest-of-user"),
        )
        for prefix, replacement in prefixes:
            text = text.replace(prefix, replacement)
        text = text.replace(str(Path(os.sep,'opt','homebrew')), '[package-runtime-root]')
        cooked = text.encode()
        (dest / name).write_bytes(cooked)
        artifacts.append(
            {
                "path": f"docs/validation/final-rem1-drafter/{name}",
                "raw_sha256": digest,
                "sha256": hashlib.sha256(cooked).hexdigest(),
            }
        )
    record = {
        "increment": increment,
        "phase": "attempt" if phase == "green" and result.returncode else phase,
        "intended_phase": phase,
        "expected_deficiency": deficiency,
        "started_utc": started,
        "elapsed_seconds": elapsed,
        "command": command,
        "runtime": sys.version.split()[0],
        "requested_sdk_backend": os.environ.get("ASTICHI_LOWER_ENGINE", "default"),
        "exit_code": result.returncode,
        "artifacts": artifacts,
        "raw_archive": "external:yidl-dataclass-final-rem1-drafter-raw",
        "outcome": "pass" if result.returncode == 0 else "failed_attempt",
    }
    with (dest / "increments.jsonl").open("a") as stream:
        stream.write(json.dumps(record, sort_keys=True) + "\n")
    print(output.decode(errors="replace")[-6500:])
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
