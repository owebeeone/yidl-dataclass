# Dataclass Stage A owner checkpoint

Stage A is verified as a partial product checkpoint, not final implementation
acceptance. Owner verification completed at 2026-10-12T09:38:25Z. The original
experiment start remains 2026-10-12T03:36:48Z, including the unauthorized SDK
detour and operator intervention. Answering status questions had incorrectly
ended owner turns; the operator's continuing GO is now being carried forward.

Scope: Dataclass package, authored YIDL resources, generated base, tests,
documentation and evidence only. No SDK or Undoable changes in this checkpoint.

The drafter's final source matrix has 41 passed and one intentional Field.doc
version skip on each of CPython 3.12.12, 3.13.12 and 3.14.3. Its explicit Python
backend canonical smoke has three passed. Owner inspection confirmed direct
generated stores and genuine SDK composition without consumer AST repair.

The owner independently built the Dataclass wheel and installed it without
editable source into three external environments using original Astichi 1.1.3
and YIDL 0.1.0. The native extension identifies as 1.0.7, without prototype
artifact capabilities. Isolated execution (`-I`, external working directory)
passed the owner probe on all three minors under both Python and native-rust
selections. Verified import origins are under the environment prefix.

The probe checks direct slots/assignment/weakrefs, actual std Field metadata,
asdict/replace, captured annotations, independent hostile-repr defaults,
declaration Field ownership and dictionary class-default fallback. Results are
in `docs/validation/stage-a/owner-installed-results.json`; the probe source is
`docs/validation/stage-a/owner_installed_probe.py`. These are independent bounded
checks, not the full later installed or compatibility matrix.

All 114 owned-manifest file hashes matched; all 26 JUnit files parse. Every raw
artifact hash in the increment ledger is present in the external raw archive
(54 distinct raw file hashes). The owned files contain no machine-specific
filesystem paths. Historical failure labels/corrections remain append-only.

Stages B–H remain: comparison/repr/hash; factory dependencies and field policies;
lazy/inheritance/copying; actual Undoable reuse and write-context compatibility;
complete packaging/installed checks; benchmarks/declarative evidence and final
independent Code/State reviews. Next action is Stage B under the same consumer
boundary, with the sole drafter stopped again for verification before commit.
