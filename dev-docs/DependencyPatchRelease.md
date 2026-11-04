# YIDL 0.1.4 and Astichi 1.1.5 dependency patch

Target: **yidl-dataclass 0.1.3**. The patch moves the exact pins from Astichi
1.1.3 and YIDL 0.1.2 to Astichi 1.1.5 and YIDL 0.1.4. Astichi 1.1.4 fixed the
CPython 3.15 provenance round-trip and added a stable-ABI Windows wheel; 1.1.5
fixes native-engine name hygiene for block pieces spliced through
`AssemblyScope`. The decorator API and generated base are unchanged.

## Changes

- `pyproject.toml` pins `astichi==1.1.5` and `yidl==0.1.4`.
- `tests/test_installation.py` expects those `Requires-Dist` entries.
- User docs drop the Windows CPython 3.15 exclusion that came from Astichi 1.1.3
  having no Windows 3.15 wheel, and state the new pins.

Historical evidence (benchmarks, earlier validation records and
`Python315Release.md`) keeps its original tuple. The benchmark harness still
requires the original SDK wheels it measured.

## Qualification

On Windows with CPython 3.15.2, a clean registry environment confirmed YIDL
0.1.4 and Astichi 1.1.5, then regenerated the base with each explicit backend
(`python` and `native-rust`). Both matched the committed base.

`scripts/check_release.py` (Gearu's release check) passed on Windows for
CPython 3.12.14, 3.13.5, 3.14.7 and 3.15.2, with each explicit backend and no
fallback: 301–303 passed per cell, with one to three version-specific skips.
Strict Twine checks passed for the wheel and sdist, and each artifact's
installed examples and regeneration passed on every minor and backend.

These are qualification results for a dependency patch, not new independent
reviews or performance measurements.
