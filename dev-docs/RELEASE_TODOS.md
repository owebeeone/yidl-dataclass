# Release readiness — 27 October 2026

Baseline inspected: `0f2fce6` on `main`. Target: first PyPI release, 0.1.0 (completed).
The subsequent four-package Python 3.15 patch pass is recorded in
`Python315Release.md`; its expanded scope supersedes this initial audit boundary.
Authorized scope: Dataclass release preparation, documentation, consumer fixes,
packaging and publication through Gearu. Undoable is audited separately. Astichi,
YIDL, Lifecycle and other dependencies are reference-only; no SDK changes or
rebuilds are required.

## Runtime-freeze contract

`@dataclass(freezable=True)` creates an initially mutable model. `freeze()`
permanently blocks ordinary writes/deletions, applies explicit field freeze
hooks, materializes lazy values and infers child freezing from resolved
annotations of freezable YIDL classes. Cycles and repeated completed calls are
handled. Unannotated mutable contents remain shallow unless a hook converts them.
This is optimistic, non-transactional freezing: failure propagates, clears the
parent's in-progress flag, and permits retry, but earlier changes and frozen
children are not rolled back. There is no thaw. Copy/deepcopy/pickle preserve
state; constructor-based replacement creates a new, initially mutable instance.
Freezing does not activate hashing. See `docs/API.md` and
`examples/runtime_freeze.py`.

## Confirmed defect and bounded correction

The native backend passed the pre-existing suite, but explicit Python lowering
failed while decorating even a simple freezable model. `FreezeFieldRead` used a
bare external-reference expression; Astichi correctly diagnosed that the marker
is value-form only. The consumer YIDL now assigns the expression to its temporary
instead. No SDK changes, dynamic field-name dispatch or new runtime abstraction
were added. Regenerated the base and all affected canonical goldens through the
supported helpers. The golden refresher's versioned-case registry also now
includes both runtime-freeze fixtures; they previously had versioned manifests
but were missing from that registry.

## Current verification

Final local full-suite results, with explicit backend selection and no fallback:

| CPython | Python lowering | Native Rust lowering |
| --- | --- | --- |
| 3.12.12 | 285 passed, 3 skipped | 285 passed, 3 skipped |
| 3.13.12 | 286 passed, 2 skipped | 286 passed, 2 skipped |
| 3.14.3 | 287 passed, 1 skipped | 287 passed, 1 skipped |

The source tests used published Astichi 1.1.3 and YIDL 0.1.0 wheels. A fresh
CPython 3.13 environment resolved the same runtime dependencies from PyPI, built
wheel/sdist metadata passed strict Twine checks, and installed-wheel checks
covered runtime freezing, typed children, lazy fields, local storage, cycles,
copy/deepcopy/pickle, replacement and regeneration. Undoable transaction and
history smoke checks also passed in that environment. The first matrix attempt
exposed stale versioned golden expectations, which were refreshed; the table
reports the complete rerun, not the failed attempt.

This is local release verification, not a new independent review of the
runtime-freeze extension and not a fresh Windows/Linux runtime campaign.
Historical reviews, experiment times, token/cost evidence, limitations and scope
corrections remain in `dev-docs/`; no historical measurements are relabelled as
measurements of this release. No new performance advantage is claimed.

## Release gate

- [x] Verify runtime freezing against its documented non-transactional contract.
- [x] Correct the Python-backend freeze defect and refresh generated artifacts.
- [x] Pass the complete six-cell local source matrix.
- [x] Add a packaged runtime-freeze example and distribution coverage.
- [x] Include README metadata and working absolute documentation links for PyPI.
- [x] Configure Gearu, including isolated full-suite, regeneration and installed
  wheel/sdist checks for both backends on CPython 3.12–3.14.
- [x] Add `.github/workflows/publish.yml`, matching the operator's pending PyPI
  publisher: `owebeeone/yidl-dataclass`, workflow `publish.yml`, no environment.
- [x] Inspect `gearu plan 0.1.0` from the committed clean candidate.
- [x] Run `gearu release 0.1.0 --push --github-release`; Gearu owns the version
  change, verification and immutable tag. Do not publish locally.
- [x] Confirm the release workflow and fresh PyPI installation after publication.

The workflow runs both backends on Ubuntu for all three supported minors, checks
regeneration, builds distributions, checks metadata and exercises an installed
wheel. Only `release.published` runs the OIDC upload job. A failed check prevents
publication. The tag must match the package version. Ordinary pushes and manual
workflow runs cannot upload.

## Separate findings

Undoable's `dev-docs/RELEASE_TODOS.md` records its current `schema` name collision,
paused root helper and obsolete optional Dataclass regeneration pin. None blocks
this package's runtime publication. YIDL 0.1.1 exists, but the tested Dataclass and
Lifecycle tuple pins 0.1.0; broadening that compatibility is a separate decision.
No license declaration/file is currently present in this member; this task does
not select a license on the owner's behalf.
