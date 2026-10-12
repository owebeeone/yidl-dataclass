# Dataclass Stage D evidence

Status: lazy/inheritance/copy checkpoint ready for owner verification. Only the
Dataclass consumer changed. Original Astichi 1.1.3 / YIDL 0.1.0 remain locked,
reference-only dependencies; no SDK/Lifecycle/Undoable edits or builds occurred.

## Actual increments and corrections

`increments.jsonl` preserves exact commands, runtime/backend, start/elapsed time,
exit status, sanitized output/JUnit hashes and original raw hashes. Nonzero
intended GREEN runs are attempts. Original raw bytes remain externally
content-addressed at `external:yidl-dataclass-stage-d-raw`; corrections append to
`corrections.jsonl` without rewriting old evidence.

| Increment | Pre-fix behavior | Subsequent same-target evidence |
| --- | --- | --- |
| d01 | Lazy extension unavailable; busy/recursion/concurrency/cycle/availability tests fail | Rich lazy canonical and focused targets pass; factory/converter fixture corrections described below |
| d02-corrected | Direct hidden-provider retention/release unavailable | Retention canonical and two focused targets pass on both original backends |
| d03 | Generated inheritance unavailable; field-layout and hook boundaries fail | Inheritance canonical and focused targets pass on both original backends; event oracle corrected below |
| d04 | Copy state/readiness/cycles and replacement protocols unavailable | Canonical and focused targets pass on both original backends; separate 3.13 replacement-method RED/GREEN |
| d05 | 3.14 lazy annotation evaluator invoked during cloning; property wrapper name mutated | Identical annotation/property targets pass after fresh class-cell/wrapper handling |
| d06 | Valid field named `property` shadows descriptor creation | Identical regression passes on both original backends with captured builtin |
| d07 | Fake name-only marker excuses custom interceptor; replaced inherited state hook trusted | Identical two rejection targets pass after generated-function identity ownership checks |
| d12 | Constructor parameters named type/Exception/TypeError shadow builtin class-provider reads, exception handling and validator diagnostics | Identical four-target set passes on both original backends after private builtin captures |

D01's first class-body factory name lookup failure was setup, corrected before
implementation. Three retry/cancellation test preconditions were corrected after
implementation: an optional parameter named like its own field created a real
named cycle, and a converter oracle expected an integer from a string result.
Those corrected cases are **post-implementation verification**, not a claimed
unchanged RED→GREEN proof. The valid busy/recursion/named-cycle and canonical
failures preceded implementation. D02 strengthened a previously vacuous seeded
retention assertion and captured an actual corrected RED before implementation.
D03 corrected its expected `__set_name__`/`__init_subclass__` order after code;
class creation already followed Python's normal set-name-before-hook order.

Repeated original-resource composition attempts are preserved. They include
inherited production naming, child collection visibility, repeated scoped child
identities, setter processed-local binding, state subscript ports and pickle
memoization. A pickle restore-arguments state recipe recursed on self-cycles;
the corrected generated reduce tuple allocates first and applies state through
pickle's memoized state phase. These are consumer mechanics, not SDK authority.

D08's three hash seeds already produced identical source: that passing run is
verification, **not behavioral RED**. Ordered busy-row planning is a determinism
refactor. Dictionary copy canonical, expanded descriptor/source checks and final
matrix are post-GREEN verification. The initial formatter command also touched
generated goldens; authoritative resource regeneration and full canonical refresh
restore all such outputs before final checks. Historical output remains intact.
Stage B's prior TDD sequencing deviation and the earlier compiler scope detour
remain disclosed; this stage does not erase them.

The first full matrix passed all behavior checks. Its two 3.12 runs found three
golden-only mismatches: previously common plain/layout/metadata output now differs
because `__replace__` is generated only on 3.13/3.14. Minor manifests and exact
per-minor refresh correct that harness gap; both 3.12 full suites are rerun and
affected canonical/source checks are repeated on the other minors. Failed runs
remain preserved. D12 then records independent escaped Stage C builtin-name
defects and their narrow RED/GREEN fixes; those resource changes justify another
full three-minor/two-backend matrix after authoritative refresh.

## Authored generation and accessor spelling

The inherited resources extend policy generation with retention → lazy → lazy
initialization → copy. Immutable support facts specialize direct authored
factory calls, property bodies, private provider deletion, busy flags and storage
state rows. No runtime provider/liveness table, generic field-access dispatcher,
method-source emitter, AST repair or std method generator is used. Callback and
default objects are per-class exec namespace captures referenced through existing
SDK name/path bindings; generation does not invoke them.

Separately composed `@property`/`@field.setter` fragments obtained distinct public
scoped identifiers on the original Python backend. The viable existing route is
unique private getter/setter/deleter functions and one public assignment through
captured `_y_dc_property`. This is a source-spelling choice: the builtin property
holds those exact specialized functions, with direct backing storage and no new
runtime helper dispatch. The source/bytecode projection verifies body identity,
direct lazy flag/storage reads, specialized converter/validator calls and absence
of generic lookup. Capturing the builtin also permits a user field named
`property`; other generated method builtin reads use their globals rather than
class-body field lookup. Constructor fragments also capture type, Exception,
TypeError and AttributeError privately so valid public parameter names cannot
shadow them. The audit found no other bare constructor builtin call/exception
reference; copy-only methods have fixed self/state/memo/protocol parameter names.

Named delayed providers read current public fields/properties and ClassVars.
Only directly consumed InitVars are retained; an eager intermediate cuts the
retention graph. Successful terminal consumers release private providers after
all nonresettable consumers are ready; any resettable direct consumer retains its
provider for the instance lifetime. Failed access keeps providers and clears busy
state in finally. Concurrent first access remains precisely unsupported.

Inheritance revalidates the merged DAG and layout, reuses inherited physical
slots and preserves field order. Local copied functions receive fresh class cells;
old cells stay unchanged, including supported descriptor and 3.14 deferred
annotation functions. Copy/deepcopy/pickle restore explicit absence/readiness and
retained providers without invoking lazy factories, preserve shallow aliases and
deep memo cycles, and reject active lazy state. Dictionary state preserves absent
class-default fallbacks and unrelated attributes. Replace uses constructor rules,
requires caller-supplied required InitVars and never replays retained providers.

## Gates and remaining scope

`d13-final-*` is the final current suite on CPython 3.12.12, 3.13.12 and 3.14.3,
using both explicit original SDK backends in separate environments. It includes
A/B/C regressions, richer versioned goldens, resource regeneration equality,
consumer wheel resource/pin checks and the narrow D failure/source checks.
The final D13 suites have zero failures/errors: 3.12 has 195 passed/3 skipped,
3.13 has 196 passed/2 skipped, and 3.14 has 197 passed/1 skipped, on each backend.
Environment records assert original installed SDK origins/versions and wheel
hashes. `evidence-qa.json` verifies raw/sanitized hashes and all JUnit; the owned
manifest uses repository-relative paths against the Stage C committed tuple.

Stages E/F retain real Undoable reuse and the complete ownership/context/callback
matrix. Stage G still owns final isolated installation, review, docs-only first-day
usability/declarative evaluation and the required `dataclass_field_removal.py`
before/after deletion plus missing-provider mutant canonical; D does not claim
that absent fixture passed. Stage H retains fixed five-process benchmark gates.
No release/publication or measured performance result is claimed here.
