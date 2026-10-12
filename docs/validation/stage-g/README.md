# Stage G public packaging and installed verification

Status: public artifact tuple ready for owner verification and the **pending cold
public-doc-only author attempt**. The sole drafter did not implement that held-out
combined task or launch another author/reviewer. H timing/final reviews remain.
Original GO and all historical scope/TDD/process deviations remain in owner records.

## Scope, public documentation and canonical changes

Only the two consumers changed. SDKs Astichi 1.1.3/YIDL 0.1.0 and Lifecycle 0.1.0
remain fixed original wheels, with no source/resource/version/packaging/build edits.
Dataclass runtime source/resources remain byte-identical to verified D; Undoable
runtime source/resources remain byte-identical to verified E/F. Changes are public
docs/examples, consumer packaging, tests/goldens and verification support/evidence.
Paused UndoableLeaf/checkpoint and workspace configuration are untouched.

README plus docs/API.md and docs/Generation.md stand alone: option/field defaults,
std-compatible subset and differences, metadata/helpers, named providers, pipelines,
mutability/frozen cache exclusions, lazy retry/retention and copy/replace effects,
inheritance and errors. The public Inventory example is introductory ordinary-field
usage, not the held-out combined quote/provider/lazy/cache solution. Both wheels
preserve README-relative docs/examples directories under `documentation`.

`dataclass_field_removal` shows before/after declarations, a deleted const/converter
policy, vanished slots/metadata/method operands, contrasting instances and the
missing required-provider mutant. Behavior already worked: G03 is verification,
not a retroactive test-first RED. Existing pipeline ownership canonical now checks
same-shape distinct default/callback objects, independent classes and differing
field shapes; hostile repr and no generation callback observations remain canonical.
The expanded case already worked and is also labeled verification.

G01 on each consumer genuinely failed its independently built-wheel public-resource
contract, then passed the same target after docs/package inclusion. Initial flat
public-resource targets and their GREEN remain preserved; subsequent packaging
verification preserves relative docs/examples links. New sdists exclude private
experiment/validation archives (and unrelated paused Undoable docs), with those
original files preserved. Source/resource inspections now read the actual imported
package through importlib.resources, so installed checks inspect wheel code rather
than a secretly copied source tree. Missing/version/hash authority failures run
before generation; new missing-authority coverage is post-GREEN verification.

## Isolated installed corpus

`installed_gate.py prepare` builds both consumer wheel/sdist pairs, safely extracts
sdists and rebuilds identical wheels. It installs only those consumers plus original
SDK/Lifecycle wheels and binary test tools into separate environments on each minor.
No dependency is rebuilt. SDK hashes and full consumer package inventories are in
artifact-tuple JSON. Test-only trees are copied externally, with no src/pyproject or
workspace pytest.ini. A dedicated pytest.ini adds only the external test helper
directory; `-I` and absent PYTHONPATH defeat source fallback. Session guards assert
consumer/SDK origins under sys.prefix, exact original versions and actual selected
backend. The no-authority environments assert Dataclass cannot be discovered.

| Installed corpus, each backend | 3.12 | 3.13 | 3.14 |
| --- | --- | --- | --- |
| Dataclass runtime (197 collected) | 194 passed / 3 version skips | 195 passed / 2 version skips | 196 passed / 1 version skip |
| Undoable with build authority | 341 passed | 341 passed | 341 passed |
| Undoable with Dataclass absent | 334 passed / 2 explicit deselections | 334 passed / 2 explicit deselections | 334 passed / 2 explicit deselections |

Dataclass excludes its two source packaging tests and one source-layout hash-seed
test from installed coverage. Those three source-only tests pass separately on all
six combinations (G09). Undoable excludes its source distribution test; the absent-
authority corpus also excludes five generation/authority tests, the build-only
layer canonical and the Dataclass cross-consumer test. Two latter tests are explicit
pytest deselections; ignored modules are not mislabeled skips. The full installed
with-authority corpus covers them separately. Dataclass source regeneration and
Undoable packaged regeneration/authority diagnostics occur in the installed corpus.

## Final artifact tuple and evidence ownership

After the installed corpus, an API prose clarification changed only packaged docs.
The initial artifact tuple is retained. G10 builds final wheels/sdists, verifies
byte-identical sdist wheel reproduction and proves **every runtime/resource payload
hash unchanged** from the installed corpus. Final wheels are reinstalled without
resolving/rebuilding dependencies. G11 verifies final packaged regeneration,
public resources and examples on all six selections. Repeating unchanged runtime
correctness is unnecessary under the accepted packaging-only gate.

`artifact-tuple-final.json` identifies final artifacts, bytes, SHA256 and package
inventories; runtime unchanged proof relates them to `artifact-tuple-initial.json`.
All physical artifacts/environments are external. Public resource paths are:

- yidl_dataclass/documentation/README.md
- yidl_dataclass/documentation/docs/API.md
- yidl_dataclass/documentation/docs/Generation.md
- yidl_dataclass/documentation/examples/first_use.py
- Corresponding yidl_undoable paths use docs/Architecture.md.

`increments.jsonl` preserves actual commands, phases, times, exit statuses and
raw/sanitized output hashes. `installed-junit.jsonl` separately maps all 18 actual
installed JUnit files to original/sanitized hashes. Raw bytes are externally
content-addressed at `external:yidl-dataclass-stage-g-raw`; setup/evidence corrections
append without changing historical rows. Some runner rows identify recorder runtime;
installed logs identify actual child patch/backend/origins. Corpus elapsed times
are correctness-run observations, **not performance measurements**.

`check_evidence.py` verifies every raw/sanitized hash and JUnit, all installed and
source/smoke gates, public path hygiene and unchanged runtime/resource payloads,
then freezes owned hashes. Undoable's own Stage G packaging/source rows and hashes
have a separate owning manifest. No SDK/private owner docs are included in those
owned inventories. Cold public-only authoring and final reviews belong to the owner.
