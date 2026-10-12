"""Record original-wheel versions/origins without importing workspace SDKs."""

from __future__ import annotations
import hashlib
import importlib.metadata as metadata
import json
import os
from pathlib import Path
import sys
import astichi
import yidl
from astichi.lower_engine import select_effective_lower_engine


def main() -> None:
    output = Path(sys.argv[1])
    wheelhouse = Path(os.environ["SDK_WHEELHOUSE"])
    prefix = Path(sys.prefix).resolve()
    modules = {}
    for module, expected in ((astichi, "1.1.3"), (yidl, "0.1.0")):
        origin = Path(module.__file__).resolve()
        assert origin.is_relative_to(prefix), module.__name__
        assert metadata.version(module.__name__) == expected
        modules[module.__name__] = {
            "version": expected,
            "origin_relative_to_prefix": origin.relative_to(prefix).as_posix(),
        }
    wheels = {}
    for name in (
        "astichi-1.1.3-cp312-abi3-macosx_11_0_arm64.whl",
        "yidl-0.1.0-py3-none-any.whl",
    ):
        wheels[name] = hashlib.sha256((wheelhouse / name).read_bytes()).hexdigest()
    payload = {
        "python": sys.version,
        "implementation": sys.implementation.name,
        "sdk_modules": modules,
        "original_wheel_sha256": wheels,
        "selected_backend": select_effective_lower_engine().selected_engine,
        "dependencies": {
            item.metadata["Name"]: item.version for item in metadata.distributions()
        },
    }
    output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")


if __name__ == "__main__":
    main()
