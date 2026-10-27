# Python 3.15 dependency findings

## Astichi 1.1.3 Windows binary wheel coverage

Observation confirmed against PyPI's version-specific JSON on 27 October 2026:
`https://pypi.org/pypi/astichi/1.1.3/json` lists these Windows artifacts:

- `astichi-1.1.3-cp312-cp312-win_amd64.whl`
- `astichi-1.1.3-cp313-cp313-win_amd64.whl`
- `astichi-1.1.3-cp314-cp314-win_amd64.whl`

There is no cp315 Windows wheel or Windows abi3 wheel in that release. Its Linux
and macOS wheels use the cp312 stable ABI; the macOS wheel has passed the current
Dataclass 3.15.2 suites with both lowering backends. Ubuntu publication jobs cover
Linux separately.

Practical impact: a Windows CPython 3.15 binary-only installation cannot obtain
Astichi 1.1.3 from this artifact set. A source build may be possible, but it has
not been qualified by this pass. This is an observed wheel-coverage limitation,
not a demonstrated runtime/compiler defect or evidence that a source build fails.

Suggested follow-up: qualify Windows 3.15 and publish a compatible Astichi wheel
through its own release process, then validate the consumer tuple there. The
operator authorized changes/releases for YIDL, Lifecycle, Dataclass and Undoable;
Astichi remains reference-only. This finding does not require broad compiler or
API work and does not block the verified macOS/Linux path. Do not describe the
current four-package pass as Windows Python 3.15 qualification.
