# YIDL Dataclass TDD implementation plan

Status: proposed plan awaiting its own review. The design was accepted by both
replacement reviewers at `de7cadd25c1d3fd5deac0d978043284fa130da1c`, with no
findings. This plan implements that design; it does not claim code, executed
regressions or benchmark results. The owner records acceptance, exact tuples,
reports, checkpoints and experiment timing separately.

The review tier for this interior plan is one Consistency-axis review. Any
P0/P1/P2 finding or request for Safety coverage automatically escalates it to
Safety review; the owner records the tier and resulting verdicts. Implementation
starts only after this plan's gate passes. Final implementation retains the
independent Code and State axes of the review-loop implementation gate;
`ExperimentProtocol.md` requires final review but does not rename those axes.
Architectural/design conflicts stop implementation for redesign and review;
bounded remediation may exceed two cycles. Do not reinterpret a failing test to
change the accepted API. UndoableLeaf remains paused.

## 1. Ownership, execution and evidence

Implement Dataclass in this member, neutral reusable comparison assets in YIDL,
and the actual second consumer plus write-context prelude in Undoable. Lifecycle
is a layout/semantic reference and future comparison consumer; it is not changed
by this plan. Do not edit workspace membership, GWZ-managed configuration,
neighboring unrelated work or the original Undoable experiment's results.
Workspace operations use GWZ. The owner settles revisions and maintains the
multi-repository tuple; workers do not silently include unrelated changes.

Paths in this document are relative to the named owning member. Development
dependency references in Dataclass configuration use relative sibling paths;
installed packages never depend on those paths. Read each member's instructions
before its first edit, including YIDL's canonical design/coding rules and
Astichi's rules if a genuine shared composition defect requires work there.

For every behavior-sized increment within a stage:

1. Add the smallest canonical scenario or focused test expressing the missing
   behavior. Run it against the preceding implementation and preserve a genuine
   RED result. Name the intended assertion/diagnostic; an environment/import
   failure unrelated to that behavior does not count as its RED evidence.
2. Implement the minimum complete slice through the YIDL resource/matcher and
   normalized facts path. Run the same target to GREEN. Do not temporarily route
   user methods through std method generators, Python source-string emitters or
   generic access dispatch.
3. Refactor responsibility boundaries while rerunning that focused target.
   Record whether refactoring changed anything; do not manufacture a refactor.
4. At the stated stage checkpoint, run the relevant wider regression scope and
   record its revision/environment. Expand checks after changes or failures;
   do not repeatedly run unchanged full suites merely to accumulate passes.

The owner keeps an append-only evidence index with stage/increment, actor, test
case, command, interpreter, expected RED deficiency, exit/result, GREEN result,
refactor result, artifact paths and exact member tuple. Store complete stdout,
stderr and JUnit records under versioned `tests/actual_test_results/`; retain the
review/delivery subset under `docs/validation/`. Logs in version control must
redact machine-specific filesystem prefixes and unrelated sensitive data, keeping
raw observations separately when necessary. Do not fabricate a RED after GREEN,
count collection errors as behavioral coverage, or overwrite historical evidence.

Use explicit-root functions from `yidl.testing.versioned_test_harness` for golden
discovery, rendering and versioned output paths. Reuse its canonical
`run_multi_source_case` convention. Do not import its CLI `main` and assume that
its implicit YIDL project root becomes this member's root. A thin local runner
may invoke pytest with this member as cwd; it must not fork compiler semantics.
Tests and source inspection target stable behavioral names, not stage numbers.

Focused commands, once the package/dev configuration exists, run from the
owning member, for example:

```sh
uv run --python 3.12 --extra dev python -m pytest tests/test_markers.py -q
uv run --python 3.12 --extra dev python -m pytest tests/test_yidl_goldens.py -q
uv run --python 3.12 --extra dev python -m pytest tests/test_differential.py -q
```

Repeat explicitly for 3.13 and 3.14 at the matrix checkpoints. Pin/record the
actual patch versions and dependency lock. Use separate interpreter environments
for concurrent matrix runs; never race uv recreation of a shared `.venv`.
Development runs must resolve the changed local YIDL/Astichi/Undoable sources,
not accidentally test older published dependencies. Installed-wheel checks later
use only the built artifact tuple and locked dependencies.

## 2. Intended product and test layout

Dataclass follows the accepted Lifecycle-style layout:

```text
src/yidl_dataclass/
  __init__.py, py.typed
  dataclass.py, dataclass_markers.py, dataclass_definition.py
  dataclass_harvester.py, factory_graph.py, stdlib_adapter.py
  class_replacement.py, errors.py, regenerate_dataclass_base.py
  _generated_dataclass_base.py
  yidl/
    dataclass_core.yidl, dataclass_policies.yidl, dataclass_factories.yidl
    dataclass_lazy.yidl, dataclass_initvar_classvar.yidl
    dataclass_local_store.yidl, dataclass_comparison.yidl
    dataclass_copy.yidl, dataclass_base.yidl
tests/
  test_markers.py, test_definition.py, test_factory_graph.py
  test_differential.py, test_failures.py, test_lazy_failures.py
  test_class_replacement.py, test_source_contract.py
  test_yidl_goldens.py, test_regeneration.py, test_installation.py
  support/                      named typed corpus/support records
  data/gold_src/                canonical cases listed below
  data/goldens/materialized/    readable source plus behavior artifacts
  data/perf/                    benchmark definitions/runner
  actual_test_results/          per-minor observations
examples/, docs/validation/, dev-docs/
```

Create files when their cohesive responsibility appears, not empty placeholders.
Compiler/support state uses typed, preferably frozen std dataclasses. Generated
model classes remain plain Python classes. Semantic support objects own policy
validation/lowering; do not add enums or passive emitter tags as shortcuts.

| Owning member | Files/resources |
| --- | --- |
| YIDL | `src/yidl/library/comparison/comparison.yidl`, `resources.py`, `__init__.py`; neutral composition canonical case; explicit package-resource inclusion |
| Undoable | `src/yidl_undoable/undoable_markers.py`, `undoable_harvester.py`, `undoable.py`, `yidl/undoable_comparison.yidl`, `write_comparison_context.py`, existing class/view/transaction integration, regenerated base; canonical comparison/write-compatibility cases and focused context/failure tests |

Regeneration source maps use the accepted logical keys
`shared/comparison.yidl`, `dataclass/<filename>.yidl` and
`undoable/<filename>.yidl`; consumer imports use `../shared/comparison.yidl`.
Load the shared bytes with `importlib.resources` from YIDL's installed package.
Generated provenance includes resource digests and stable logical names, never
checkout locations. No duplicate comparison source is checked into a consumer.

## 3. Canonical corpus and coverage ownership

Each canonical case emits `decorator.py`, readable formatted decorator source,
`generated_output.py`, readable formatted model source, external-binding fixture
and deterministic behavioral output. Version-sensitive outputs use an explicit
minor-keyed manifest; common outputs remain shared. Do not regenerate goldens
until the expected behavior and source shape have been reviewed against the
accepted design and independent oracle. A golden update is not a GREEN by itself.

| Canonical case | Successful behavior and source evidence owned here |
| --- | --- |
| `dataclass_plain` | Required/default/independent-factory fields, public writable slots, dictionary alternative, repr/compare exclusions, several differing/equal instances, standard Field inputs and metadata, kw-only/KW_ONLY, ClassVar, weakrefs and matching |
| `dataclass_initialization` | Named function/lambda/class factories, positional-only/keyword arguments, optional parameters, cls/self providers, processed input/default/result ordering, eager InitVars including init=False; contrasting independent and dependent factories |
| `dataclass_policies` | Ordinary/converted/validated/read-only const fields and frozen writable excluded caches side by side; decorator conversion versus explicit disable/override; nullable conversion, local storage and repr selection |
| `dataclass_lazy` | Eager/lazy contrast, explicit lazy seeding, first/cached/reset access, readonly lazy comparisons/hash/repr/data-helper reads, retained InitVars and eager-only nonretention, release after terminal consumers versus lifetime retention for resettable consumers |
| `dataclass_inheritance_helpers` | Same-shape overrides and field order, inherited slots, stateless mixins, zero-argument super and descriptors, inspection, std/package replacement, copy/deepcopy/pickle of ready/unready values and local storage, version-specific copy.replace |
| `dataclass_comparisons` | Included/excluded equality/order/hash operands, empty fields, different classes/options and multiple instances, 3.12 tuple versus 3.13+ conjunction/self shortcut, recursive repr; std differential observations linked to this case |
| `dataclass_field_removal` | Before/after declaration deletion with policy removed in the same edit and corresponding slots/method operands disappearing; companion missing-provider mutant diagnoses separately |
| Neutral YIDL `comparison_composition` | ComparisonCore generates an independently named plain class with supplied read paths, custom inherited read matcher and empty prelude; no Dataclass metadata dependency or runtime tuple helper |
| Undoable `undoable_comparisons` | Defaults table, eq/order classes and several nodes/views/pins; ordinary/const/lazy/managed/binding inclusion versus excluded management families; boolean logical compare and legacy/new write policies shown separately in metadata/source |
| Undoable `undoable_write_compatibility` | Native original-operand/hash/tuple/proxy callback traces through real staged working values/custom freeze/thaw; equal distinct child replacement and same-node views; parent comparisons disabled with enabled children; field-removal pair |

Selected examples use six to ten meaningful fields and two or more related
classes where that makes storage, selection and wiring inspectable. Include at
least three instances distinguishing included-field changes from management-only
changes. This is a readability guide, not a universal quota: keep each case
cohesive. Stable callback counters/event labels replace addresses and object repr.

Canonical cases own success-path assertions. `test_source_contract.py` reads the
same emitted artifacts for structural inspection rather than recreating models.
Differential tests run the same declarative compatible corpus against stdlib and
the product, comparing observations; they do not duplicate designer-golden
expectations. Focused tests own diagnostics, callback failure/recovery, parser
boundaries, binding mechanics and cases needing controlled context/exception
instrumentation. The evidence manifest assigns every assertion to one primary
scenario; additional projections must name their independent purpose.

## 4. TDD stages and checkpoints

### Stage A — package, normalization and one genuine generated class

RED a canonical `dataclass_plain` slice requiring public slot storage and a
generated constructor, plus focused marker/stdlib-adapter contracts. GREEN the
package configuration, exact public declarations/errors, immutable definition
carriers, copied std Field metadata, supported-minor adapter and basic
`dataclass_core.yidl` assembly. Establish regeneration check/default and --write
CLI, wheel resource manifests and the explicit-root golden harness here.

The first successful class must already come from YIDL/Astichi; a handwritten
temporary model or applying std dataclass to the user's class does not complete
this stage. Add subsequent RED slices for dictionary defaults, keyword-only
signature order, Field/params inspection, ClassVar and match/weakref behavior.
Reject unsupported interpreters and field doc on pre-3.14 with explicit tests.

Carry the original initializer finding now: ordinary source-free init=False with
custom init; decorator init=False then assignment; generated init with no consumer;
dictionary init=False simple default leaving `__dict__` empty and reflecting a
later class-default update. Their std differential cases are the success oracle.
Keep the actual unavailable generated-provider diagnostic RED until Stage C
introduces that consumer, then close it there. Test Field copying so one class's
normalization never mutates another declaration or a reused std Field.

Checkpoint: focused normalization/golden/source tests, then this member's full
current suite on all three minors. Confirm default writable fields are public
slots and the slotted replacement inherits declared bases without inheriting the
declaration class's instance dictionary. No other member's full suite is required
until it changes.

### Stage B — neutral comparison composition and Dataclass methods

RED the neutral ComparisonCore canonical class and Dataclass comparison corpus,
then GREEN the packaged neutral YIDL asset and Dataclass inheritance/matcher
adapter. Method bodies must live in shared native YIDL productions; comparison
read paths use precompiled structural bindings. Dataclass's `eq_prelude` is empty
and emits no context branch/import. No generic Python tuple helper is acceptable.

Add RED increments for repr recursion, equality/order empty and excluded fields,
all method-conflict/hash actions, exact class guards, self/nonreflexive/NaN values,
callback evaluation order and version-specific equality. Check unsafe_hash,
explicit/local eq/hash distinctions, hash=True/compare=False rejection and
compare=True/hash=False acceptance. Canonical/differential behavior chooses
expected outcomes; no test derives expected comparisons by calling the generated
helper itself.

Checkpoint: full current Dataclass suite and YIDL neutral/layering/resource tests
on three minors; YIDL full relevant regression once after its asset/build changes.
Leave compiler semantics untouched unless an actual compiler defect is proven.

### Stage C — factory DAG, policies and specialized access

RED `dataclass_initialization` and `dataclass_policies` in small facility slices;
GREEN the factory graph and inheritable policies/factories/InitVar/ClassVar/local
layers. Resolve constructor action, source availability, binding/order/layout and
all known paths before generating direct stores/calls. Capture callbacks and
defaults as objects, not executable repr text. A field's pipeline runs before
its value reaches dependent calls.

Focused RED cases cover unsupported signatures/unknown providers, missing actual
providers (including known optional parameters), cycles, kind conflicts, invalid
booleans/flags/options, unhashable defaults, conversion types/nullable rules,
validator returns/causes, setter atomicity, explicit const mutability conflicts
and frozen writable-field comparison/hash exclusions. Standard `__post_init__`
and extension/custom-init combinations must fail as designed. Do not require
absent ordinary fields to initialize merely because they exist in metadata.

Inspect canonical AST: ordinary stores/reads are direct; policies have individual
backing slots/properties; callback calls have specialized argument lists and
capture names. Test callbacks/hostile repr are not executed during generation,
bindings cannot leak across classes, and the same shape/version/resource tuple
gives stable emitted structure without ids or filesystem names.

Checkpoint: focused callbacks/diagnostics/source and changed canonicals, then full
current Dataclass suite on three minors. Run shared compiler/Astichi regression
only if their implementation changed, not for every new consumer fixture.

### Stage D — lazy state, retention, copying and inheritance

RED `dataclass_lazy` and `dataclass_inheritance_helpers` increments; GREEN lazy
and copy layers, retention analysis and class replacement. Test eager consumers
of lazy values as well as truly delayed reads. Source shows field-specific busy/
ready guards and direct retained-provider release, not a runtime liveness map.

Focused failure tests own retry after factory/converter/validator/BaseException,
successful prerequisite preservation, opaque recursion/busy guards, attempted
replacement/deletion, mutable reset, absent eager properties, concurrent first
access rejection, and active copy/pickle rejection. Include multiple terminal
consumers and a resettable consumer, eager intermediates cutting retention and
provider absence after safe release. Canonical copy outcomes check no callback
materialization and correct shallow/deep aliasing/memo behavior.

Inheritance/mechanics tests own private-name collisions, old/new __class__ cells
remaining independent, supported descriptor wrappers, repeated set-name/subclass
creation, ABC abstract status, incompatible frozen/layout/family/mutability
overrides, manual slots, model/dict/multiple bases and unsupported interceptors/
state hooks. Use the canonical inheritance case for successful model behavior.
Check std helper subset versus explicitly unsupported hidden-default InitVar
inference, package replacement recomputation and required provider inputs.

Checkpoint: full Dataclass three-minor suite, complete differential matrix and
regeneration/source checks. This is the first complete Dataclass API checkpoint,
not the experiment's completion: real Undoable reuse remains required.

### Stage E — real Undoable consumer, local markers and view methods

Before edits record the pinned existing Undoable regression result and full
baseline tuple. RED `undoable_comparisons`, declaration parsing/defaults table and
field-removal pair. GREEN the Undoable-owned wrapper translating write policies
to unchanged Lifecycle markers, separate logical facts, decorator options, shared
ComparisonCore/view matcher adapter and regenerated class bundle.

Required options are bare/empty/explicit disabled, eq-only, eq+order, omitted-eq
order rejection and explicit false-eq order rejection. Cover all eligible/excluded
families, strict boolean logical inclusion, valid/invalid write strings, legacy
strings without warning, legacy+explicit write conflict even for equal spelling,
direct Lifecycle marker inputs and inherited wrapper facts. Reject unsupported
write_compare on nonmanaged kinds without modifying Lifecycle's shared API.

Generate comparisons on default/current/working facade classes with exact-class
guards, explicit exposed-value semantics and unhashability when enabled. Check
cross-view/model/subclass NotImplemented, pins, history movement, getters' existing
lazy/thaw effects, ordering and SnapshotNode's unchanged identity/data behavior.
Hash-container restrictions remain explicit rather than switching hash modes.

Checkpoint: Undoable focused new canonical/options/failure tests, regenerated-base
check, then full Undoable suite on three minors and affected shared/Dataclass
composition tests. Do not refactor its existing access dispatcher or resume the
paused initialization-helper work.

### Stage F — historical write context and inherited review counterexamples

RED native callback/write-compatibility cases against the structural integration
from Stage E; show where distinct child nodes would otherwise compare equal.
GREEN only the accepted small scope boundary and adapter-selected precompiled
YIDL prelude. Native `bool(old == value)` receives original operands inside `_call`;
the identity policy stays `old is value`. The prelude precedes all self/type guards
and returns bound RuntimeFacade identity equality only for an active marker.
Dataclass retains the empty prelude; hash/order never switch.

This stage must carry every earlier finding and the complete design Section 8
matrix. Its primary allocation is:

| Obligation | Test/evidence owner |
| --- | --- |
| Logical inclusion independently crossed with value/identity write policy and eq on/off | `undoable_comparisons`/`undoable_write_compatibility` canonical variants; excluded fields cannot affect generated eq/order; distinct equal values record under identity and same reference skips where the baseline returns that reference |
| AcceptOriginal original inner list in both directions | Native-reference callback trace plus staged custom-freeze integration in `undoable_write_compatibility`; legacy/new value spelling and generation on/off |
| Shared or equal distinct keys, constant-hash counters, raising-after-preparation hash, collisions, key equality exceptions | Narrow native-versus-scoped callback trace plus staged working dictionaries; zero additional hashes relative to native comparison, matching callback order/result/errors |
| Unequal tuple lengths with True/False/raising/truth-returning prefix; reverse direction; identical nonreflexive elements; unequal list contrast | Native-reference traces and staged tuples/lists; never introduce a shared manual length gate |
| Dict/proxy, proxy/dict, proxy/proxy, escaped and custom mapping-backed proxies | Native original-argument/forwarding trace and staged working-value integration; no unwrap/GC/private-C adapter |
| Equal-valued distinct child nodes, same-state views/pins, nested native containers; disabled parent/enabled children | Canonical write decisions with state identity independent of structural fields; no logical facade equality for graph/history membership |
| Opaque callback explicitly comparing handles; nonfacade historical False, reflected subclasses, NotImplemented, truth conversion | Controlled callback tests under `_call`; intentional contextual identity plus normal structural equality after closure |
| Success, equality/truth exception, BaseException, ownership corruption | Focused `test_write_comparison_context.py`/ownership tests: marker closed before reset, preserved notes/fault behavior, next ordinary equality structural |
| Nested/cross-manager scopes; captured outer/inner contexts; async task before/after closure | Focused lifecycle tests with deterministic events/barriers, no sleeps; restore outer marker, closed copied inner cannot revive outer, marker stores bool only |
| Explicit empty/copied thread contexts and in-flight sampling | Focused context tests with synchronization; record interpreter thread-context defaults; no atomic-cutover or concurrent-manager claim |
| Identity branch, unhashability, structural ordering and native cycle outcomes | Focused boundary tests: no extra scope/equality in identity branch; unchanged hash/order; native outcomes versus existing read/freeze/graph cycle diagnostics |
| Native YIDL prelude and absence of Dataclass overhead | Shared/consumer source artifact checks, branch ordering, external scope/method bindings, regenerated output origin and parser-free runtime instrumentation |

Use native equality and the frozen baseline engine as oracles where applicable;
never a manually rebuilt/paired comparator. Opaque callback bodies receive
historical facade identity while scope is active as intentionally documented.
No equality callback is permitted to mutate the owning manager; test the fence
while the context is active and after exceptional closure. Scope state contains
no manager/node/operand/parent/token references and never enters history/schema.
Do not keep long-lived contexts just to make a test pass.

Checkpoint: focused native/context/ownership and new canonical cases on all
minors, then full Undoable and Dataclass matrix plus affected shared YIDL tests.
No hand-normalization pass, monkey-patching, cached-hash emulation or global
boolean may substitute for the accepted ContextVar mechanism.

### Stage G — generation/installation gates and public usability

RED independently built-wheel resource discovery, regeneration and docs-only
example failures, then GREEN manifests/loaders/docs without changing accepted
runtime semantics. Verify Dataclass/YIDL/Undoable wheels and sdists contain all
required `.yidl`, generated bases, loader code and py.typed. Build the whole
artifact tuple and install from a local wheelhouse into clean environments for
each minor with no editable installs or workspace `PYTHONPATH`. Check imported
module origins are in those environments. Rebuild wheels from sdists and compare
regenerated outputs/digests using stable logical source keys.

Parser-free instrumentation runs the first and a second decoration after imports
in a fresh process: prohibit `ast.parse`, fresh `astichi.compile` source parsing
and Python compile of source strings in decorator/generated-helper paths, while
allowing the final `compile(ast.Module, ...)` step. Warm caches must not conceal a
first-decoration parse. Authored template parsing belongs to regeneration/build;
source rendering/formatting occurs outside that protected runtime. Inspect all
generated method/source paths, including unmatched/disabled policy resources.
If the compiler cannot satisfy this contract, resolve the real generic boundary
through a tested supported surface and review any design change; do not insert
consumer source-string workarounds or Astichi-specific AST surgery.

Pin a public-docs-only task before its author attempts it: create a small quote
model with converted quantity, dependent total, hidden initialization locale for
a lazy receipt, read-only fields and mutable excluded cache; exercise construction,
comparison, lazy reads, replacement and inspection. Give the author only installed
public documentation/README/examples and importable packages, not dev-docs,
private source, the implementation conversation or solution fixture. Record first
attempt source, commands/errors, elapsed time, available tokens and every repair/
clarification. Run it in an isolated wheel environment. A failure is repaired by
public documentation or product changes through RED/GREEN, then retried with the
changed evidence preserved. It is a first-day usability observation, not a
calibrated LLM authoring score. Public docs also include the std differences,
unsupported combinations and contextual Undoable equality rule.

Checkpoint: complete three-minor installed corpus, source/regeneration checks,
docs-only runnable artifact and final changed-member regressions. Package-only
changes require packaging tests; repeat runtime regressions only when runtime or
dependencies also change.

### Stage H — measured evaluation, implementation review and delivery

Freeze the validated artifact tuple and benchmark definitions below before
measurement. Run the benchmark/declarative evaluation, then independent final
Code-axis and State-axis implementation reviews on the settled tuple with the design, plan, original
findings and complete evidence index. Fix bounded findings through new RED/GREEN
records and retrace the changed scopes; architectural breaks require redesign.
After accepted final review, perform the installed smoke and any checks invalidated
by remediation, without endlessly rerunning unchanged matrices.

Deliver public docs, generated contrasts, support/limitation matrix, raw validation
and benchmark data, declarative desk evidence, independent reports and separate
Dataclass/Undoable integration revisions. Record final wall/active time and
available actor/stage token data. Actual billing is unavailable unless observed;
API-equivalent estimates need dated model prices and cached-token treatment.
Missing measurements are unavailable, never zero. Do not reopen or reuse original
Undoable experiment timing/cost results.

## 5. Benchmark definitions and predeclared numerical gates

Create the harness in `tests/data/perf/`, raw JSON/CSV under
`docs/validation/perf/`, with an immutable manifest of case definitions, units,
inputs, tuple and commands. Use the same interpreter/machine for product and
stdlib default/slotted baselines. All ordinary comparable cases use both 3-field
and 12-field models with identical values/options; exclude management fields from
logical-operation baselines only when both models exclude them identically.

| Case | Timed operation and setup boundary |
| --- | --- |
| `slot_read`, `slot_write` | One public field read/write repeated; models/instances/code generation outside timing; consume read result; keep assignment values comparable |
| `readonly_read`, `readonly_reject` | One const/frozen read, or one rejected public replacement with exception handled; std frozen baseline labeled as its different implementation |
| `construct_supplied`, `construct_defaults`, `construct_factory` | One equivalent instance creation, supplied values/simple defaults/zero-argument factories; generated classes outside timing |
| `construct_dependent` | One named-factory construction; separate extension result, optional handwritten equivalent labeled reference rather than std parity |
| `lazy_first`, `lazy_cached` | One unready getter versus one ready getter; prepare a pool with one fresh unready instance per timed first-access operation outside each batch, and a separately prepared ready pool for cached access; never reuse one freshly computed instance as multiple first-access samples |
| `pipeline_plain`, `pipeline_converted`, `pipeline_validated` | Same public assignment or construction with pipeline disabled/converter/validator/both; use trivial documented callbacks and label policy overhead |
| `eq_equal`, `eq_early_mismatch`, `eq_late_mismatch`, `order`, `hash`, `repr` | One operation on equivalent logical values; empty/equal/mismatched selections stated; hash baseline frozen; ready lazy values outside ordinary timing |
| `decorate_cold`, `decorate_repeated` | One generation/decorator invocation with declaration classes prepared beforehand; cold fresh-process observation versus in-process repeat; source emission timed separately |
| `memory` | Bytes: shallow instance including any dict plus aggregate allocation per instance; ordinary/frozen/lazy/retained-provider/weakref/local variants; instance count and retained references stated |
| `undoable_eq_prelude`, `undoable_value_scope` | Enabled structural equality outside scope against an equivalent explicitly labeled structural reference; native value-write comparison with scope versus frozen pre-integration write path; parent/child and callback/container shapes stated |

Do not subtract an empty-loop cost into negative/unstable operation estimates;
keep harness overhead consistent and report a separate harness-only observation.
Use perf_counter_ns, calibrate batches to at least 20 ms, 10 warmup batches and
20 measured batches per timed case in each of at least five independent process
runs per minor. Alternate paired product/baseline order and predeclare the random
seed. Preserve every batch in ns/op and every memory observation in bytes/object,
including outliers. Aggregate process medians first; report median, min/max,
IQR/median, paired ratios and bootstrap 95% intervals using a fixed seed and
10,000 resamples over process pairs. Record CPU/OS/build, power settings, load,
sample counts, warmup/calibration and code hashes.
Memory cases use 10,000 instances per variant in each process, with classes and
shared input objects prepared before measurement. Report getsizeof instance/dict
totals separately from tracemalloc aggregate allocation deltas; include list-pool
overhead consistently and state whether provider/cache values are shared or
uniquely allocated. Cleanup/GC and pool preparation occur outside timed access
batches. Raw units and operation counts must make these boundaries auditable.

These gates are fixed before inspecting results:

- Correctness, source-access shape and installed-resource gates have zero tolerated
  failures. Performance does not excuse a semantic or source-boundary failure.
- Plain slot read/write product/slotted-stdlib ratio target is at most 1.20.
  Ordinary supplied/default/independent-factory construction and repr/eq/order/
  hash target ratios are at most 2.00. These are engineering regression targets,
  not advance speed claims or parity requirements for extension policies.
- IQR/median above 0.15 for a comparable case makes its performance conclusion
  inconclusive. Permit one documented five-process rerun after correcting an
  environmental cause; preserve both runs. Do not choose the better run silently.
- A ratio whose 95% interval lies wholly above its target is a regression requiring
  investigation and bounded remediation. An interval straddling the target is
  inconclusive, not a pass or a demonstrated regression. A stable interval wholly
  at/below target passes that target. Never relax the target after seeing data.
- Extension/frozen-property rejection, generation latency, memory and Undoable
  context/prelude cost have no unsupported numerical parity promise: publish
  absolute measurements and applicable within-harness deltas/ratios. For later
  remediation of the same validated implementation, a stable >20% median slowdown
  with a 95% ratio interval wholly above 1.20 is a new regression signal.

Benchmark harness validity is tested with deterministic units/setup accounting,
not by asserting noisy wall-clock performance inside pytest. If remediation is
needed, rerun only changed benchmark families plus relevant correctness tests;
the final report lists unresolved regressions/inconclusive cases candidly and
does not declare universal performance success. A change to these reviewed
definitions/gates requires an explicit plan amendment before interpreting new
measurements, with earlier results retained.

## 6. Grounded declarative evaluation

Use `dev-docs/reference/DeclarativeApiEvaluatorV3.md` (instrument SHA-256
`20a72d189d1ad032a9f0ab9bbfc1b63636cade0062c1d05bbae0383e7fb0e815`). Freeze
`dataclass-intents-v1`: the eight Dataclass/neutral canonical intentions above plus
four held-out documentation-only variations (readonly dependent quote, optional
nullable conversion, inherited keyword-only override and removable management
cache). The held-out author receives intent/public docs but no solution; these
variations are not used to tune the engine before their first recorded attempt.
The two Undoable cases form a separately identified seam corpus. Store the exact
sources, intent text, oracle selection and edits/digests under
`docs/validation/declarative/` before issuing any card.

Mode is **desk**, author class **llm**, substrate Python model methods/storage,
ship boundary installation plus public construction, archetypes **resolution,
lowering and templating**. Include RET v1 universal classes and these archetypes'
E classes with unchanged instrument tiers. No new domain weights or scalar.
Declare separate units: field/class declarations, named callable dependencies,
YIDL generation assets, and their seams. Explicit callback bodies remain
imperative escape surfaces; the write-context callback seam is evaluated
separately from field authoring.

Record the DAPI gate and L/S/T reasoning against actual normalization, dependency
resolution, inheritance/matching and generation artifacts. B.1 locality is
resolution span, not physical distance or a claim that larger L is better. Record
the operator's field-local authoring constraint separately; the declaration
deletion pair must remove its policy with no detached selector. Legitimate
provider references remain scoped dependencies with missing-reference diagnostics.
Report R3 interaction clauses with a declared vocabulary counting unit, R5 std/native
differential evidence only for the subset it independently supports, and callback
escape containment from the actual ownership tests. Use Python tokenizer tokens
for any reported expansion or edit sizes, with fixture exclusions and numerator/
denominator stated.

This run does not supply the instrument's six-anchor/three-held-out-surface
calibration program or full authoring harness. Therefore publish a desk evidence
card with calibration/rater gaps named; no measured frontier, weighted correctness
envelope, k80/few-shot curve or overall grade is claimed. All Part E authoring-loop
metrics remain unscored. The docs-only attempt and field-removal token diff are
raw observations, not a calibrated E6 score. Executed mutants/failure tests can
show their actual first detection stage without upgrading the whole card to
measured mode. Missing corpus/calibration/oracle coverage is unscored, not inferred
from passing designer-authored goldens.

## 7. Completion criteria

The experiment completes only when the accepted API is implemented through native
YIDL composition, all supported-minor correctness/installation/source gates pass,
actual Undoable reuse and scoped identity obligations pass, public-only usage
runs, final independent implementation reviews accept the settled tuple, and
reproducible measurements/limitations plus time/token/cost evidence are delivered.
This plan's acceptance alone starts implementation; it establishes none of those
results. The owner updates the checkpoint and ledger at each real boundary.
