# Dataclass Stage C evidence

Status: provider/policy checkpoint prepared for owner verification. Only the
Dataclass consumer library, authored resources, generated base, tests, goldens,
README and evidence changed. Original Astichi 1.1.3 / YIDL 0.1.0 wheels are the
runtime dependencies. SDKs are reference-only, with no edits, builds, version or
capability changes. Undoable integration remains a later stage.

## Actual RED, GREEN and preserved attempts

`increments.jsonl` records exact commands, starts, elapsed phase time, runtime,
requested SDK backend, exit, sanitized hashes and original raw hashes. Historical
rows/logs are unchanged; `corrections.jsonl` appends classification clarification.
Raw output is content-addressed in the external archive identified by
`external:yidl-dataclass-stage-c-raw`. Sanitized JUnit retains parseable XML and
replaces machine paths/identifiers with bracket placeholders.

| Increment | Actual pre-fix deficiency | Same-target GREEN |
| --- | --- | --- |
| c01 / c01-errors | Named provider DAG unavailable; missing known optional provider, cycles/signatures and callback failure contract | `c01-final`: rich constructor canonical plus six focused failures, 7 passed; original Python verification also passed |
| c02-corrected | InitVar/local/ClassVar/self provider and extension suppression contract unavailable | `c02`: same canonical and focused target set, 13 passed; original Python also passed |
| c02-default | Hidden provider unhashable default accepted | Identical narrow target passed |
| c03 | Pipeline, validator return/causal/BaseException/atomicity and const/frozen policies unavailable, 28 failures | `c03-final`: identical focused/canonical targets, 28 passed; original Python also passed |
| c04 | Pseudo-kind conflict, bypassing policy copy/state hooks, missing immutable dependency descriptions, inheritance/private-name boundary, 18 failures | Identical targets, 18 passed |
| c05 | Dictionary declaration still exposed hidden-provider and unavailable ordinary Field markers | Identical two targets passed |
| c07 / c07-python | Consumed dictionary fallback selected hidden-provider default resource and left pipeline unresolved | Identical ownership/fallback canonical passed on both original backends |

The first c02 fixture failed a Python class-body name lookup before decoration;
its setup failure and corrected pre-implementation RED are separate records.
Initial YIDL duplicate visible properties/duplicate inherited contributions and
stale-base attempts are generation/setup integration failures, not fabricated
behavioral REDs. The c03 third attempt passed its independent behavior oracle and
27 focused tests but lacked initial golden files; snapshot preparation then gave
the identical-target GREEN. The recorder labels nonzero intended GREEN as
`attempt`, preserving the intended phase.

C06 namespace/stability/deletion/source and packaging checks were broader
**post-GREEN verification**, not retroactively test-first success tests. They
found the remaining fallback defect; c07 captured it before its bounded fix.
The fallback canonical changes the class default before constructing the model,
asserts the dependent result, and checks no fallback instance write. C07 resource
regeneration was labeled `refactor`; its preceding matcher correction was a
behavioral fix, while deletion of unused install fragments was refactoring. This
classification is appended in corrections. C08 formats cohesive modules and
refreshes canonicals after their independent assertions pass.

## Consumer-owned generation boundary

The inherited resource chain is core/comparison → pipelines → factories →
providers → policies → base. Python support modules normalize immutable facts,
validate source/signature/policy constraints and submit YIDL matches. Authored
YIDL/Astichi composition supplies actual methods. No method-source emitter,
AST repair, generic runtime field lookup or std dataclass method generator is
used. Factory/converter/validator/default objects remain in the per-class exec
namespace. Existing SDK bindings receive names, identifiers and paths, not
arbitrary callable objects or their repr. Callbacks are not executed at
class generation, and independent same-shape classes retain separate captures.

Provider DAG validation checks all named edges even when constructor values can
bypass a factory. Topological order is deterministic by declaration order.
Positional-only optional gaps capture their actual defaults; matched arguments
have specialized positional/keyword syntax. `cls` reads `type(self)` and `self`
requires explicit opt-in. Hidden InitVars are processed constructor locals with
no public default, instance field or helper exposure. ClassVars are class reads;
local storage is excluded from std field helpers/comparison/hash. No provider
values are exposed through the dependency descriptions.

Supported original resource alternatives matter: bare imports in funcargs,
plain expression call holes, repeated child aliases and nested bindings failed
in preserved attempts. The working resources use separate positional and named
call regions, outer-bound processed locals, unique child identities, and separate
property function/decorator identifier ports. These are observed source-pattern
limitations, not proven SDK defects or authority to change dependencies.

Each pipeline runs source → conversion → validation → direct installation before
its processed value reaches consumers. Validator success is exact None/True,
rejection is exact False, and every other result is a direct TypeError. Package
context errors and BaseException retain identity; ordinary callback exceptions
carry field context and the original cause. Writable pipeline failures preserve
the prior value. Const/frozen properties use private backing slots; ordinary
writable fields and excluded caches use direct public slots. Source projections
inspect those reads/stores and direct capture calls, with no generic dispatch.

## Checkpoint gates and remaining work

`c09-final-*` runs the entire current consumer suite in separate CPython 3.12.12,
3.13.12 and 3.14.3 environments, with both explicit original SDK backend choices.
The suite includes source regeneration equality, consumer wheel resources/pinned
metadata, minor-specific rich canonical goldens, previous A/B regressions and
new focused diagnostics. Environment files assert SDK origins under the test
prefix and record original wheel SHA256. `evidence-qa.json` records actual final
suite results and verifies original/sanitized hashes and all JUnit; the owned
manifest records repository-relative paths and relation to the Stage B tuple.

This checkpoint claims no SDK modification or publication and no measured
performance outcome. Stage D must add lazy state/retention, complete inheritance,
copy/deepcopy/pickle and version-specific `copy.replace`. Stages E/F must integrate
Undoable and its full ownership/context/callback historical comparison matrix.
Stages G/H still own isolated full installation, final review, docs-only first-day
usability/declarative evaluation and the fixed benchmark gates. Stage B's disclosed
TDD sequencing deviation remains part of the experiment record; this checkpoint
does not erase it or the earlier scope-correction detour.
