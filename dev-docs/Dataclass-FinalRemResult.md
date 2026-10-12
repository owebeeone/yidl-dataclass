# Final remediation round 1 — owner verification

Status: **one bounded consumer patch verified; reviewer closure pending**.
The controlling plan is `Dataclass-FinalRemPlan.md`; original reports remain
verbatim. No finding is self-closed by this result.

The patch separates Dataclass result locals from method capture globals,
reuses inherited lazy flag slots, allocates Undoable comparison capture aliases
without changing public class creation names, and corrects dictionary-mode
identity documentation. The neutral comparison resource, native managed-write
comparator, callback fence and context lifetime remain unchanged. There is no
new class-name reservation, SDK change or AST repair.

## Independent owner checks

`docs/validation/final-review-round1/owner_baseline_manifest.json` preserves
nine actual failures on the original installed G wheels. The same probe passes
all nine cases in all six corrected installed combinations. The separate
wrapper checks selected backend, no fallback, exact versions and installed
origins. Copy/deepcopy/pickle/hash/callback identity, inherited physical slots
and both original Undoable naming failures pass.

All 32 Dataclass and 30 Undoable Python/YIDL source payloads match their frozen
wheels. Packaged README/API/example bytes match source. All original Astichi,
YIDL, cache and Lifecycle payloads match their original wheels in every fresh
minor environment: respectively 85, 39, 8 and 21 files per environment.

An independent audit, without importing the drafter QA generator, verifies
222 owned file hashes, 93 increment records, 140 artifact references, 123
distinct original raw hashes, 47 JUnit files and all 16 explicit sanitation
chains. All final source and installed XML counts reconcile. The shared
authority remains
`2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef`;
Undoable contains no hand-maintained copy.

| Corpus, both backends | Python 3.12 | Python 3.13 | Python 3.14 |
| --- | --- | --- | --- |
| Dataclass source | 259 pass / 3 skip | 260 pass / 2 skip | 261 pass / 1 skip |
| Dataclass installed | 202 pass / 3 skip | 203 pass / 2 skip | 204 pass / 1 skip |
| Undoable source | 350 pass | 350 pass | 350 pass |
| Undoable installed | 349 pass | 349 pass | 349 pass |
| Undoable without Dataclass | 342 pass / 2 deselected | 342 pass / 2 deselected | 342 pass / 2 deselected |

The drafter handoff documents exact installed exclusions, genuine RED/GREEN,
oracle corrections, setup failures and failed backend-leak attempts. The narrow
fixture restores the prior environment around the frozen accounting test;
it changes neither that test's assertions nor the 19 frozen harness sources.
Previously passing native source suites were not repeated for that fixture.

## Artifact and historical measurement boundary

Dataclass wheel:
`2c72e83f76dc8b81680d90f27602fb54fb0c4e7c7a5f826349dcfbfbb79cc9eb`;
sdist: `f58f7951b0f118e87b0547d8acba91dbe40ec17c53a55fb521432b933274bbfc`.
Undoable wheel:
`2974b01923a10acb60573c46bc3bd95b1bb8ec90198345b9162173bd327219cb`;
sdist: `2996fadce36c2b6f5d1d3035ff1da6ab3755c4a1f7f4a31294f4c450648977ad`.
The recorded sdist rebuilds reproduce the frozen wheels byte for byte, and
all six installed regeneration/public-example smokes pass.

The drafter manifest is
`73b91590153fd6a4027d68ddb7d7022b8d6b51ddb0dd854272fe554167773c51`;
QA: `6d2bc456ef8c0720448f0e9d133b37501152f9f492b2c6e93b3df9cdeee1efc1`.

All H2 sources, definition and raw data remain unchanged. Their timing results
retain the original source/wheel tuple. Dataclass decoration setup changes and
Undoable prelude/dependent setter paths are not measured final-byte results.
Inherited lazy layouts were outside the original benchmark cases. No favorable
rerun, final-wheel numerical parity or universal performance acceptance is
claimed. The next action is focused independent re-verdict by the same two axes.

Source/documentation whitespace checks pass. Preserved diagnostic log/XML
whitespace is explicitly exempt; their audited hashes remain unchanged.
