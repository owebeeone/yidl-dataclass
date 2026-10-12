# Final remediation round 1: drafter handoff

This is one bounded consumer patch against the final Code and State reports. It addresses the four report roots and preserves the original SDK route. It does not close the reports: the owner and same reviewers retrace the settled patch. The original GO clock, Stage B TDD deviation, scope/process lapses and historical compiler experiment remain unchanged.

## Changes and supported route

Dataclass executes the authored YIDL module with separate capture globals and output locals. The returned public class comes from the output locals, while generated methods retain the original builtin/callback objects in their globals. Public identifiers remain accepted, including `type`, `tuple`, `dict`, `int`, `hash` and `_y_dc_converter_0`. No callback serialization, execution at generation, method-source emitter or AST repair was introduced.

Inherited lazy readiness/busy names now use the same inherited-slot exclusion as the other physical slots. Empty child/grandchild classes and same-shape overrides reuse their base's cache state storage. The extended inheritance canonical exercises unready and ready copying, deepcopy/pickle, failure/retry, reset and active-copy rejection; empty subclasses have the base's basicsize and no repeated slots.

Undoable uses consumer-selected private association IDs disjoint from all three public class identifiers. Existing YIDL identifier/reference facilities bind direct attributes of one immutable `ComparisonCaptures` object. It retains the original ContextVar, RuntimeFacade equality/hash functions and object ordering descriptors. The authored prelude and disabled-method resets use those original objects. Class creation names, metaclass and inherited subclass-hook observations remain public names from the outset. Comparator/context ownership behavior and the authoritative neutral comparison resource are unchanged. There is no private-name reservation or runtime field-name dispatch.

The feasibility probe records the rejected fixed internal class-name approach: renaming after creation exposes that internal name to hooks/metaclasses. Both original backends support the selected direct capsule-reference route. Internal ClassId/CmpClassId associations change together; canonical field/view matches and source/bytecode checks pass.

Public docs and the first-use example now distinguish `slots=True` replacement from `slots=False` mutation of and return of the original declaration. Both identity behaviors are asserted in the canonical layout example and public example. The installed public bytes match their source.

## TDD and honest attempt classifications

`increments.jsonl` is append-only and contains exact commands, phases, exit codes, runtime, elapsed wall time and raw/sanitized hashes. `run_fresh.py` selects the separately installed minor environment and explicit original backend. The initial focused target is Python 3.12.12/native-rust; subsequent both-backend/minor coverage is verification.

| Target before correction | Actual RED | Same-target GREEN |
| --- | --- | --- |
| `tests/test_result_namespace.py` | Six original builtin/callback capture recognition failures | Same six targets pass |
| `dataclass_result_names.py` through `run_contracts.py` | Public `type` class breaks shallow copy | Canonical copy/deepcopy/state/pickle/hash/callback protocol passes |
| `dataclass_inheritance_helpers.py` through `run_contracts.py` | Empty child/grandchild repeat lazy physical slots | Same canonical passes after slot reuse and a separately recorded fixture-oracle correction |
| `tests/test_comparison_capture_names.py` | Seven original prelude/hash/order capture failures | Same seven targets pass |

The Undoable narrow tests were refined after GREEN to capture/closure recognition and exact object identity, avoiding duplicate protocol success coverage. The rich `24_comparison_capture_names.py` canonical owns public names, hook/metaclass observations, views, ordering, distinct-child replacement, copied/closed contexts and disabled identity/hash behavior. The original RED tests/logs remain preserved; refinement is verification, not retrospective test-first work.

The first inherited-slot intended GREEN exposed an incorrect new fixture expectation that the busy-copy exception had a wrapped cause. The documented direct RuntimeError subtype has no cause. The oracle was corrected, the failed attempt retained, and the original canonical target rerun. This was not another product defect.

Other failed attempts are retained and classified separately:

- Initial feasibility launcher parsing of `-I`, and three golden-refresh helper imports: setup failures, followed by supported-route retries.
- Three full Python Dataclass source runs: immutable H2 accounting test leaked `ASTICHI_LOWER_ENGINE=native-rust` into later tests. A focused sequence reproduced the leakage. A narrow autouse fixture outside frozen H2 files restores the original value only around that exact accounting mock. Its journal/failure-validation assertions remain unchanged. The three affected Python suites were rerun; the previously passed native suites were not repeated.
- First installed launcher: malformed pytest `-p` argument construction. Corrected only the launcher and retried.
- Six Undoable copied-test attempts included its source-only distribution build, which cannot build from a test-only directory. Those attempts had 349 passing runtime tests and one harness-selection failure each. The source build test remains covered by the full source matrix; the corrected installed gate excludes it and verifies the frozen distribution separately.
- Three no-authority environment preparation attempts used the wrong external locator directory. Corrected the runtime locator, then prepared new environments from original binary wheels.

No import/setup/process failure is labeled behavioral RED. Additional accepted-name audits, richer protocol checks, source/bytecode checks and three-minor/full-corpus expansion are post-GREEN verification.

## Settled checks

Each row below covers explicit native-rust and Python selections, with exact original SDK versions and no fallback. Installed tests run from external copied test-only trees with pytest's owning source path disabled; only helper directories are added. Consumers/SDK module origins are guarded under the fresh environment prefix. No editable sibling or SDK source fallback is used.

| Python | Dataclass full source | Dataclass installed runtime | Undoable full source | Undoable installed runtime | Undoable installed, Dataclass absent |
| --- | --- | --- | --- | --- | --- |
| 3.12.12 | 259 passed, 3 skipped | 202 passed, 3 skipped | 350 passed | 349 passed | 342 passed, 2 deselected |
| 3.13.12 | 260 passed, 2 skipped | 203 passed, 2 skipped | 350 passed | 349 passed | 342 passed, 2 deselected |
| 3.14.3 | 261 passed, 1 skipped | 204 passed, 1 skipped | 350 passed | 349 passed | 342 passed, 2 deselected |

Dataclass's installed corpus omits the 55 frozen benchmark mechanics and two source/distribution build tests; all remain covered by the full source suite. Its subprocess generation-stability test runs installed because its external cwd has no `src`. Undoable's no-authority corpus additionally omits five generation-authority tests and deselects the canonical authoring-layer and cross-consumer Dataclass-equality cases. Runtime absence is asserted before collection. All five authority/version/hash/missing diagnostic tests run with the authority installed in the full installed corpus.

Final source result names are `rem1-source-*-verification.junit.xml`, using the `python-restored` Dataclass suffix for the three corrected full Python runs. Final installed result names are:

- Dataclass: `rem1-installed-dataclass-{312,313,314}-{native-rust,python}-v2-verification.junit.xml`.
- Undoable: `rem1-installed-undoable-{312,313,314}-{native-rust,python}-v3-verification.junit.xml`.
- Undoable without authority: corresponding `-v3-without-authority-verification.junit.xml`.

`package-rebuilds.json` records exact package member hashes and byte-identical consumer wheel rebuilds from both sdists. Packaged regeneration and both public examples pass on all six installed combinations. The Dataclass comparison authority retains SHA256 `2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef`; Undoable has no copied shared resource and no runtime Dataclass dependency. `environment-*.json` records module origins relative to the environment prefix and distribution version/METADATA/RECORD hashes. Original SDK/cache/Lifecycle wheels were installed unchanged; only consumer wheels/sdists were built.

## Frozen artifacts and benchmark limits

| Consumer | Wheel SHA256 | Sdist SHA256 |
| --- | --- | --- |
| Dataclass 0.1.0.dev0 | `2c72e83f76dc8b81680d90f27602fb54fb0c4e7c7a5f826349dcfbfbb79cc9eb` | `f58f7951b0f118e87b0547d8acba91dbe40ec17c53a55fb521432b933274bbfc` |
| Undoable 0.1.0 | `2974b01923a10acb60573c46bc3bd95b1bb8ec90198345b9162173bd327219cb` | `2996fadce36c2b6f5d1d3035ff1da6ab3755c4a1f7f4a31294f4c450648977ad` |

H2's 19 source hashes, definition, raw observations and reported outcomes remain historical and unchanged; no timings were run during remediation. They describe the old artifact tuple, not these final wheels. The Dataclass correction changes generation execution setup and globals ownership; cold/repeated generation and memory provenance cannot be silently transferred. Its ordinary standalone emitted methods are not changed by this correction, but that does not establish final-wheel numerical parity. The inherited physical layout correction concerns layouts outside the standalone measured cases.

Undoable's capsule references change authored equality prelude/reset bodies. Thus old facade-structural and child-containing/tuple/mapping write seam timings are not direct final-body timings. The native write comparator/context helper is unchanged; integer and reflected-opaque setters do not invoke the changed facade prelude, but their numerical rows still retain the old wheel/source provenance. No new timing, favorable rerun, target adjustment or relabeling is claimed. The owner decides any explicitly separate supplement and final interpretation.

## Audit and ownership

`changed-distribution-paths.json` identifies 35 Dataclass and 21 Undoable changed/new shipped source/test/public paths against the original G sdists. `owned-manifest.json` additionally includes this drafter evidence directory; owning-repository paths remain relative. Owner reports, plans, checkpoint, metrics, `owner_*` evidence and paused Undoable files are excluded. There were no Git, remote, SDK/Lifecycle edits or dependency builds.

Raw logs/JUnit are content-addressed in external `yidl-dataclass-final-rem1-drafter-raw`. `sanitation-corrections.jsonl` explicitly preserves the previous sanitized hashes and original raw hashes for residual runtime-prefix sanitation; prior sanitized bytes are separately archived. Historical increment rows are unchanged. `qa.json` records effective sanitation-chain, JUnit, manifest, complete final matrix, wheel/package and frozen H2 source checks. The final handoff supplies the external root rather than storing an absolute machine path here.
