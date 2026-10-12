# Baseline verification

Before implementation, the workspace Python 3.12.12 environment passed:

| Repository / revision | Command from member root | Result |
| --- | --- | --- |
| Undoable `f79e4ce6d985ed0a6463552e163baabf1a28942d` | `../.venv/bin/python -m pytest -q` | 215 passed in 4.06 seconds |
| YIDL `9d374f88445c426a56d5dd1f96fad112d1ec5417` | `../.venv/bin/python -m pytest tests/generation/test_yidl_lark_parser.py::test_yidl_lark_dataclasses_source_fixture_compiles -q` | 1 passed in 0.52 seconds |

These are baseline checks, not Dataclass implementation evidence. The existing
Undoable checkpoint modification and untracked initialization-helper draft remain
outside the run. Final verification must additionally cover the new implementation,
integration, supported interpreter versions and independently installed packages.
