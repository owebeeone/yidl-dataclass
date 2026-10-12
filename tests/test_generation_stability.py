"""Test-first deterministic dictionary lazy guard planning across hash seeds."""

import os
from pathlib import Path
import subprocess
import sys


def test_dictionary_lazy_source_stable_across_hash_seeds():
    script = "from yidl_dataclass import dataclass,lazy,generated_source\nclass Dictionary:\n first:int=lazy(default_factory=lambda:1)\n second:int=lazy(default_factory=lambda:2)\nprint(generated_source(dataclass(Dictionary,slots=False,repr=False)))\n"
    outputs = []
    for seed in ("1", "2", "3"):
        environment = dict(os.environ, PYTHONHASHSEED=seed, PYTHONPATH="src")
        outputs.append(
            subprocess.check_output(
                [sys.executable, "-c", script],
                cwd=Path(__file__).resolve().parents[1],
                env=environment,
            )
        )
    assert outputs[0] == outputs[1] == outputs[2]
