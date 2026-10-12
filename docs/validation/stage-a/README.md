# Dataclass Stage A evidence

Status: product checkpoint ready for owner verification; no Stage B work or final
implementation/performance claim. Scope is Dataclass product/resources/tests and
this evidence. Original Astichi 1.1.3 and YIDL 0.1.0 wheels are reference-only
runtime dependencies. No SDK source/build/version/capability or Undoable changes.
The original experiment start and historical detour accounting are unchanged.

`increments.jsonl` contains actual timestamps, elapsed phase times, commands,
runtimes, exits and raw/sanitized artifact hashes. `corrections.jsonl` is
append-only: failed intended-GREEN runs are attempts, never GREEN outcomes; it
also maps initial placeholder/hash hygiene corrections and empty non-test
artifacts. Original rows/logs are retained. Original raw bytes are archived
externally by SHA256 under the archive label recorded in each row. Sanitized
JUnit uses bracket placeholders and remains parseable. An initial regeneration
bootstrap import failure was captured only in the tool transcript before the
recorder accepted general commands; it is setup evidence, not behavioral RED.

| Increment | RED deficiency | Same-target GREEN |
| --- | --- | --- |
| a01 | Scaffold lacked `__slots__` and generated constructor; one canonical failure | `a01-green.log`, one passed |
| a02 | Strict field/decorator flags, Field ownership, supported-minor check and metadata absent; 18 failures, two passes | `a02-corrected-green.log`, 20 passed |
| a03 | Empty parameter/optional contribution resources were not complete for the dictionary/suppressed-init corpus; one failure, ten passes | `a03-corrected-green.log`, 11 passed |
| a04 | Invalid declarations accepted and factory equality invoked during recognition; six failures, 28 passes, one skip | `a04-green.log`, 34 passed, one skip |
| a05 | Refactor/verification of typed support facts, formatting, existing slotted-mixin capability and source projections | `a05-refactor.log`, 24 passed, one skip; no invented RED/refactor behavior |
| a06 | ClassVar metadata incorrectly subjected to an instance hash-selection restriction; one canonical failure | `a06-green.log`, one passed |

RED and GREEN use these identical targets within their increment:

```sh
.venv/bin/python -m pytest tests/test_yidl_goldens.py -q
.venv/bin/python -m pytest tests/test_markers.py tests/test_yidl_goldens.py -q
.venv/bin/python -m pytest tests/test_yidl_goldens.py tests/test_failures.py -q
.venv/bin/python -m pytest tests/test_markers.py tests/test_failures.py -q
.venv/bin/python -m pytest 'tests/test_yidl_goldens.py::test_canonical_case[dataclass_metadata.py]' -q
```

The recorder adds `--junitxml` and preserves raw bytes before sanitizing. Exact
recorded command arrays identify each invocation; no late RED was manufactured.
Setup/generation attempts include record-list grammar correction, bootstrap
loading, global-reference annotation capture and a factory assignment with wrong
Store context. Existing identifier bindings fix annotation/default loads, and a
plain authored identifier assignment fixes the factory target. No AST repair or
SDK changes were made. The template return annotation was corrected to stdlib's
`-> None`; compile(AST) uses `dont_inherit=True` so consumer-module future flags
cannot replace real captured annotations with generated-name strings.

Two oracle setup mistakes remain visible: the weakref reference initially omitted
stdlib's required `slots=True`, and the later params comparison initially used
stdlib default slots versus product default slots. They were corrected to equal
explicit options; neither is behavioral RED or a reason to modify an SDK.
A missing initial golden file was golden preparation, not another behavior RED.
Reviewed behavior assertions and the independent std oracle ran before snapshots
were recorded. Goldens include authored binding fixtures, emitted runtime base,
readable/formatted generated models and deterministic behavior. Source projection
checks independently establish plain classes/direct stores, while canonical and
stdlib differential observations own successful instance behavior.

## Checkpoint coverage and limits

Final current-suite commands run in three independent environments:

```sh
.venv/bin/python -m pytest -q
.venvs/py313/bin/python -m pytest -q
.venvs/py314/bin/python -m pytest -q
```

Each supported minor has 42 collected tests, 41 passed and one intentional
Field.doc version skip. The final matrix follows a06's adapter change; the earlier
successful matrix is preserved separately. Environment records verify SDK versions
and origins under each isolated prefix, and record original wheel hashes.
All three canonical cases also pass with explicit Python backend selection on
3.12; the full matrix uses the recorded default native-rust selection. This is
not the complete Stage G backend/installed matrix.
Packaging checks build only the Dataclass wheel and verify its authored resources,
plain generated base, `py.typed` and exact SDK dependencies. Installed-wheel
execution/public-only usability remain Stage G obligations, not results here.

Stage A supports ordinary slots/dictionary storage, independent zero-argument
factories, positional/keyword-only defaults and fences, ClassVar exclusion/metadata,
std Field/params/helper interoperability, custom/disabled initialization, weakrefs,
and direct declared-base replacement with inherited plain slots. Narrow failures
cover flags, ordering/defaults, reused Fields, descriptors, unannotated/reserved
fields, unsupported interpreters, post-init and storage conflicts. Support carriers
use typed frozen dataclasses; generated models/framework remain plain classes.

Stages B–H retain comparison/repr/hash, extension policies/provider DAG, lazy
retention/recovery, model inheritance/closure cloning/copying, actual Undoable
reuse/context ownership, installed checks, public-only usage and measurements.
The actual unavailable generated-provider diagnostic remains Stage C work because
there is no named-factory consumer generation yet. Defaults still specify the
accepted final API; selecting unimplemented facilities at this checkpoint raises
`NotImplementedError`, and the public example explicitly disables repr/eq.
No extension success, complete inheritance support, wholly Rust-owned generation,
zero-parser execution or performance result is inferred from this test count.
