# Consumer-only generation amendment

Status: documentation candidate for independent review; no product implementation
or performance acceptance. Operator authority is `ScopeCorrection.md`, recorded
at `ae220ec`. The semantic design/plan remain the accepted starting point; this
amendment changes their generation/dependency boundary only.

## 1. Scope and supersession

Implement Dataclass and its YIDL resources using original Astichi 1.1.3 / YIDL
0.1.0. SDK edits, builds, resources, version increments and new capability/artifact
APIs are outside scope. Compiler P1–P4, strict parser-free decoration, native IR
restoration and wholly Rust-owned lowering are removed from the product gates.
`PrecompiledResourcesDesign.md`, `PrecompiledResourcesImplementation.md`,
`NativeLoweringAddendum.md` and their reports/evidence remain historical records,
not product successes or prerequisites. Preserved SDK prototypes are not candidate
dependencies. No historical evidence, start time, usage or cost is reset.

All public semantics and explicit unsupported combinations remain unchanged:
direct slots by default; one plain generated class; field-specific policies;
named factories without post-init; hidden providers retained only as needed;
lazy failure/retry/release; frozen writable-cache exclusions; metadata/helpers;
version-specific comparison/hash rules; actual Undoable reuse and its complete
ownership/context/callback matrix. Field-local comparison and legacy write policy
remain separate. UndoableLeaf stays paused.

## 2. Existing-API generation route

Follow the Lifecycle-style consumer layout in the design. The regenerator loads
packaged authored `.yidl` files into a map of stable logical source names, calls
`yidl.concept_parser.compile_yidl_files(source_map, entry_name)`, selects the
concept, and calls `yidl.generation.data_def_sys.emit_concept_runtime_source`
with its `plan.build_data_definition()`, `resources` and `assembly_plan`. Check in
that emitted base; default regeneration checks it and `--write` updates it.
The base contains the existing SDK resource wrappers/matchers and assembly code.

At decoration, normalize declarations into immutable typed facts, resolve field
layout/provider graph/method actions, create the generated `new_builder()`, add
ordered facts to its generated collections and freeze them. Call the generated
`build_DataclassModule(facts).to_executable_ast()`, then compile/execute that AST
with captured callbacks/defaults and the user namespace. No std method generator,
handwritten dynamic method-source emitter or feature-specific AST repair is used.

Authored templates use existing identifier/external bindings, holes and inherited
matcher-selected contributions. For example, a static resource containing
`return self.astichi_ref(external=field_name)` bound to `field_name="count"`
produces `return self.count`. The existing transparent assignment form
`self.astichi_ref(external=field_name)._ = value` provides direct stores. A policy
resource selects a private backing name instead; its own getter/setter/factory
call remains specialized. Parameter/argument and expression contributions use
existing SDK ports with distinct binding names, not interpolated Python methods.
Shared comparison uses the same read resource and consumer matcher overrides.

Source parsing during generation is permitted, including lazy template compilation
and existing SDK literal/import/edge-value facilities. Reuse the existing
`MatcherGeneratedValue.to_generator()` template cache; each decoration creates
independent builds and captures. The consumer installs arbitrary callback/default
objects under deterministic private names in the fresh exec namespace; generated
methods reference those names. Existing SDK bindings receive only the validated
name/path strings (or supported literal values), never `.bind(factory=function)`
or another arbitrary object. For example, install a factory at `_y_dc_factory_0`
and bind its authored `astichi_ref` demand to that identifier. An authored builder
function may instead receive captures as ordinary Python arguments and retain
them in closures. Neither route serializes objects, evaluates their repr or calls
the callbacks during generation. The Undoable prelude uses the same route: install
the private ContextVar and `RuntimeFacade.__eq__` method object in its consumer
namespace, and bind only their generated identifiers into the authored prelude.
Do not add a final-value/class cache or silently reuse class-specific bindings.
No requirement that each resource parses exactly once across every generation
path is imposed. Cold/repeated generation cost remains separately measured.

“Native YIDL composition” denotes actual YIDL resources, inheritance/matching and
Astichi composition. It is independent of SDK backend selection and makes no
claim that all work executes in Rust. Consumer smoke covers both existing backend
selections without fallback; there is no new native capability requirement.

## 3. Authoritative comparison resource and reuse

Dataclass owns `src/yidl_dataclass/yidl/shared/comparison.yidl`, exporting the
neutral `ComparisonCore` contract from design Section 7. Include it in its wheel
and sdist. Method bodies/guards/order/hash remain in this resource. Dataclass and
Undoable adapt inputs through their own inherited concepts; no generic Python
tuple helper replaces generation. Dataclass selects the empty equality prelude;
Undoable selects its authored historical-write prelude before structural guards.

Both regenerators use `shared/comparison.yidl` plus `dataclass/<name>.yidl` or
`undoable/<name>.yidl`; consumer imports use `../shared/comparison.yidl`.
Dataclass reads its package authority via `importlib.resources`. Undoable's
regeneration environment installs a pinned Dataclass candidate wheel as a
build-only dependency and reads that same resource. Its lock/provenance records
the candidate version, authority SHA256, all local source digests and SDK versions.
Missing/mismatched authority fails before generation, with no sibling-path or
unversioned remote fallback. A new authority revision requires regeneration and
checks of both consumer bases.

The existing emitter embeds resource/matcher source in the generated Undoable
base. Undoable ships that base and its own adapter YIDL; no handwritten duplicate
comparison file or runtime Dataclass dependency is added. Ordinary wheel/sdist
builds use the checked-in base. Explicit regeneration from an sdist requires its
pinned build-only dependency and must reproduce the base/digests. Generated
provenance is evidence, never a replacement for edited authoritative source.
Installed Undoable comparison execution with Dataclass absent proves this
runtime boundary. SDK packaging stays untouched.

Candidate Dataclass build/runtime locks use `astichi==1.1.3` and `yidl==0.1.0`;
record compatible dependency wheel hashes and exact Python patches. Consumer
candidate versions and the integration revision are separate from SDK versions.
No release/publication is authorized by this amendment.

## 4. Evidence, remaining gates and stage order

`docs/validation/baseline/original_sdk_probe.py` and
`docs/validation/baseline/original-sdk-results.json` record original installed
SDK feasibility on 3.12.12 with verified import origins. Both Python/native-rust
selections pass existing YIDL slots/equality/frozen hashing, direct reference
specialization and cached resource reuse. Split import/inheritance inspection
supports the modular route. This is not full Dataclass parity, ordering, extension,
three-minor or performance evidence. The example's expanded ordering attempt
duplicated a binding; the consumer must use distinct ports/bindings and prove its
own ordering composition. Incorrect attribute-marker assumptions were setup
corrections, not behavioral RED or proof of SDK necessity.

The existing strict RED→same-target GREEN→refactor evidence rules, canonical
contrasts/deletion examples, three-minor differential/installed gates, predeclared
benchmark cases/thresholds, five-process measurements and grounded declarative
evaluation remain unchanged. Remove only parser-free/full-Rust/SDK prerequisite
assertions. The compact product sequence remains:

| Stage | Product checkpoint |
| --- | --- |
| A | Consumer package/normalization, genuine plain slotted YIDL class, deterministic base regeneration and original-SDK environments |
| B | Dataclass-owned neutral ComparisonCore, inherited read matching, repr/comparison/hash including version semantics |
| C | Provider DAG, named factories, conversion/validation, const/local/pseudo-field layers and direct specialized access |
| D | Lazy retention/recovery, copy/helpers, inheritance and class replacement; complete Dataclass differential checkpoint |
| E | Actual Undoable build-time reuse, field-local wrappers/view comparisons, unchanged Lifecycle markers and disabled defaults |
| F | Historical-write scope/prelude, every original counterexample and the full ownership/context/callback matrix |
| G | Consumer wheel/sdist regeneration, authority digest checks, independent captures/cache ownership, both backend smokes and public-only usability |
| H | Frozen benchmark/declarative evidence and final independent Code/State review/delivery |

Focused source checks inspect direct accesses, plain class storage, method origin
and disabled policy resources. First/second generation with different names,
defaults and callbacks proves independent capture despite template reuse. Tests
must prove no generation callback/repr execution and no dynamic consumer emitter
or AST repair. Canonical cases own success assertions; narrow failures cover
missing/stale build authority and binding leakage. Installed three-minor checks
use locked original SDKs, not preserved prototype sources. Actual product gaps
must be reported; a proven SDK blocker requires operator scope resolution rather
than another SDK implementation detour. Stop at stage checkpoints for owner
verification/commit. Personal design/TDD approval remains waived; the independent
review workflow still applies before product code resumes.
