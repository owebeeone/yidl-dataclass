# Baseline verification

Before implementation, the workspace Python 3.12.12 environment passed:

| Repository / revision | Command from member root | Result |
| --- | --- | --- |
| Undoable `f79e4ce6d985ed0a6463552e163baabf1a28942d` | `../.venv/bin/python -m pytest -q` | 215 passed in 4.06 seconds |
| YIDL `9d374f88445c426a56d5dd1f96fad112d1ec5417` | `../.venv/bin/python -m pytest tests/generation/test_yidl_lark_parser.py::test_yidl_lark_dataclasses_source_fixture_compiles -q` | 1 passed in 0.52 seconds |
| Astichi `1c47f781d3804130fdd61cbee07a3b2e4529158a` | `../.venv/bin/python -m pytest -q` | 2544 passed, 104 skipped in 31.55 seconds |
| YIDL `9d374f88445c426a56d5dd1f96fad112d1ec5417` | `../.venv/bin/python -m pytest -q` | 299 passed, 2 skipped in 38.28 seconds |

These are baseline checks, not Dataclass implementation evidence. The existing
Undoable checkpoint modification and untracked initialization-helper draft remain
outside the run. Final verification must additionally cover the new implementation,
integration, supported interpreter versions and independently installed packages.

## Dependency artifact preparation

Before product implementation, unchanged Astichi, Cache and Lifecycle wheels were
built with `uv build --wheel --python <verification-python> --out-dir <wheelhouse> MEMBER`.
Astichi compiled its native extension successfully; its CPython 3.12 ABI3 wheel
is intended for the supported interpreter matrix. Build paths are external
verification locations, not package dependencies. This is preparation evidence;
imports and compatibility in all three installed environments remain future gates.

The unchanged wheel tuple subsequently passed isolated `-I` import-origin and
native-generated plain-slot smoke checks on 3.12.12, 3.13.12 and 3.14.3, selecting
`native-rust` on each. See `docs/validation/baseline/installed-wheel-smoke.json`.
An initial setup attempt retained a newline in a temporary path; correcting that
reader allowed installation. It is not TDD RED or a product failure. These checks
do not establish the new artifact facility, Dataclass or integration behavior.

| Wheel | SHA-256 | Bytes |
| --- | --- | --- |
| `astichi-1.1.3-cp312-abi3-macosx_11_0_arm64.whl` | `8f0e6b6c53e6a9d429d131647f072fc4433b461d9a8ed75bfd83e0b1b160e597` | 1803265 |
| `yidl_cache-0.1.0-py3-none-any.whl` | `cd59c988bb4f62cf4ef324330e60b71db3301ff33f919b91f6b42760f19c7e95` | 15380 |
| `yidl_lifecycle-0.1.0-py3-none-any.whl` | `6f9f21c60f1fc360ee41e68f4de0289836f1f00a5e1f2c116be6cb4f3473cb4f` | 100592 |

## Existing source support outside artifact v1

The available CPython 3.15.0a5 environment passed an isolated installed unchanged
Astichi 1.1.3 plain-slot source compile/materialize/execution smoke on Python and
native-rust, with import origin verified. See
`docs/validation/baseline/legacy-python315-smoke.json`. This is a limited historical
source baseline, not a full-suite or newest-release claim. Artifact v1 and
Dataclass explicitly support only 3.12–3.14; the owning source matrix also needs
preservation, without relabeling 3.15 as artifact support.
