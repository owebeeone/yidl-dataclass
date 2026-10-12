# Precompiled YIDL resources: compiler-artifact amendment

Status: proposed owning-layer amendment for two fresh independent Consistency
and Safety reviews. Documentation only; no compiler, backend, product or test
implementation is claimed. Dataclass Stage A is suspended until this boundary
is accepted. Accepted Dataclass design/plan revisions are
`de7cadd25c1d3fd5deac0d978043284fa130da1c` and
`f2514e1c993cb049417b7a10cdf2932bd68bd80f` respectively.

The amendment provides a genuinely missing generic facility. Astichi owns the
complete compiled-template artifact and structural backend registration. YIDL
owns lowering its generated-value graph into that facility. Dataclass, shared
ComparisonCore and Undoable consume it through normal native YIDL composition.
No consumer serializes Astichi internals, warms source-compilation caches,
repairs emitted ASTs or substitutes a cache of completed classes/values.

## 1. Evidence and the missing boundary

The inspected owning-layer APIs establish these distinctions:

| Existing mechanism | Available behavior | Why it does not meet this contract |
| --- | --- | --- |
| YIDL `MatcherGeneratedValue.to_generator` | Lazily calls `astichi.compile(source)`; emitted assembly metadata reconstructs the source wrapper | First resource use still parses source |
| Astichi provenance encoder/decoder | Persists an ast.Module | Does not preserve/reconstitute the complete composable semantics or native parser IR |
| Astichi GeneratedAstCache | Persists final executable AST keyed by graph/runtime | Does not provide unresolved, independently bindable templates before first decoration |
| Python `register_lower_template_binding` | Structurally imports compiled record/scope/marker specs into LowerEngine | A useful metadata seam; not a complete native module loader |
| Native `register_template_snapshot` | Restores structural inventory metadata | `parse_template_snapshot` sets both package_v2 and module to None; native workspace creation rejects missing parser IR |
| Native `register_template_package_v2_source` | Registers package rows with a native ast::ModModule | Builds that module by parsing source |
| NativeTemplateCache | Has a source-registration branch and a snapshot branch | Neither existing branch restores a persisted full native AST plus complete package |
| Native builder-tree copy/specialization | Re-registers native_source; reprojecting a specialized template uses rendered source | Clearing native_source alone would disable native specialization or leave an unusable template |

Read-only local-source probes found a BasicComposable with a native binding;
pickling the whole object failed on NativeTemplateHandle. AST provenance alone
round-tripped an ast.Module. An initial missing-local-dependency import attempt
was corrected before that probe; neither attempt counts as a TDD RED.

The audit also found parsing below the top-level resource wrapper:

- Native external overlays parse expression_source in workspace and recursive
  materialization. Python AssemblyScope currently supplies serialized expressions.
- Native pass placeholders parse `pass`; reference-chain construction parses a
  dotted expression.
- Python `rewrite_hygienically` clones through unparse/parse.
- YIDL nested edge evaluation and assembly diagnostics emit source then use
  compile/eval on strings.

The artifact path must address these calls, not merely make resource construction
eager. Existing normal source compilation remains an explicit supported compiler
boundary. Regex/path validation, JSON decoding and scalar number decoding are not
Python/native source parsing. This amendment does not redefine ordinary source
compilation as parser-free.

## 2. Public Astichi interfaces and supported envelope

Add the following preferred artifact interfaces to `astichi`:

```python
export_compiled_template(composable: Composable, /) -> bytes
load_compiled_template(artifact: bytes, /) -> Composable
compile_ast(tree: ast.Module, /, *, file_name: str = "<astichi-ast>",
            line_number: int = 1, offset: int = 0,
            arg_names: Mapping[str, str] | None = None,
            keep_names: Iterable[str] | None = None,
            source_kind: SourceKind = AUTHORED_SOURCE) -> Composable
```

Export all three functions and the error classes below from `astichi.__init__`.
The signature uses the existing `SourceKind` and `AUTHORED_SOURCE` from
`astichi.frontend`; those concepts are not duplicated by the artifact layer.

Export/load are distinct from emit/provenance and operate on complete compiled
build data. `compile_ast` is the lower-level structural compiler entry required
for AST/literal resources derived at generation time; source `compile` remains
the normal authoring entry. Both compile paths share marker validation,
classification, port and inventory derivation. This is a reasoned raw input
surface, not an alternative source DSL or a Dataclass-specific AST generator.

Export accepts a BasicComposable template that has not been materialized or
specialized with external runtime values. Explicit compile-time identifier
bindings and keep names are supported and preserved. Reject unsupported custom
Composable implementations, materialized/opaque hot-path placeholders without
recoverable compiled state, and externally specialized templates. Obtain the
complete compiled tree/module through owning-layer artifact-copy APIs during
export; a build-time source compile is permitted, but runtime load never calls
it. Export never invokes factory/converter/validator objects or their repr.

`compile_ast` takes ownership by cloning the supplied AST before validation.
It applies the same supported construct/marker semantics as source compilation,
registers the selected backend structurally, and returns an independently owned
composable. It is not an API to bypass marker checks. Unknown nodes/attributes,
missing fields, invalid locations and inconsistent marker surfaces fail before
registration. Custom AST subclasses and arbitrary attached Python objects are
not accepted structural inputs. No source-render/parse reconstruction is used.

Artifact v1 supports CPython 3.12, 3.13 and 3.14 and the existing Python backend
plus the upgraded native Rust backend. It is independent of OS, machine paths,
Python cache tags and live process handles. Other interpreter/minor/backend
combinations fail clearly; the normal source API is unaffected. A future native
CPP backend must implement the same structural capability before loading v1;
there is no CPP implementation in the inspected owning tree and no speculative
C++ patch in this amendment.

Use the existing effective engine selector. If it selects Python, restore the
Python structural backend. If it selects a native backend, require that backend's
new `native.compiled_template_artifact.v1` capability and structural payload ABI.
Missing/incompatible capability fails; do not change engine environment settings,
label a Python binding as native, or silently fall back because artifact load is
unsupported. Normal `auto` selection retains its preexisting discovery semantics;
artifact capability is checked after selection, before registration.

## 3. Artifact v1: complete, portable and reproducible state

The returned bytes are UTF-8 canonical JSON, not pickle/marshal or an executable
provenance trailer. An immutable internal CompiledTemplateArtifact value owns
validated canonical rows and produces bytes. Its contents are:

- Format identity `astichi.compiled-template.v1`, semantic codec revision,
  supported Python-minor adapter set and required syntax features.
- Producer Astichi artifact ABI/codec revision, surface-bundle signature and
  canonical lower-package schema identity. Package distribution versions are
  provenance, not a substitute for ABI compatibility checks.
- Exact authored-source digest when source exists, and logical origin: file
  name, line and offset. Structural compile inputs have an explicit absent
  authored-source digest and a required canonical syntax digest; do not invent
  source or parse rendered text to populate that field.
  Source text may be retained for diagnostics/location mapping and source
  comparison, but is never reparsed on load or specialization.
- A complete normalized marker-bearing syntax graph, including node kinds,
  named fields, scalar constants, child references, contexts/operators and
  location/provenance data needed by Python and native materialization.
- Recognized markers, name classification, demand/supply ports, inventory and
  lower package rows, including defaults/fallbacks, clauses, funcargs payloads,
  scope boundaries, imports/exports/pass, unroll/ref/comment metadata,
  keep names and initial identifier bindings.
- SHA-256 integrity digest of the canonical body. No timestamps, memory ids,
  native engine/handle ids, callbacks, user classes, modules or opaque objects.

Encoding sorts unordered semantic sets/maps and preserves all meaningful ordered
sequences. Syntax nodes receive deterministic ids from field-ordered traversal;
metadata references nodes through those ids/structural paths instead of id(node).
Distinct occurrences remain distinct; shared singleton operator/context objects
may be canonicalized. All referenced ids/paths are checked on decode. Semantic
payloads use registered codecs for existing behavior-bearing marker/port/
inventory classes; wire discriminators name those existing schema entities.
Do not introduce enums or scatter passive tag comparisons through runtime code.

The syntax schema names constructors/fields explicitly; it never imports a type
named by the payload or calls eval to instantiate rows. It has a closed catalog
covering currently supported Astichi constructs, including the class/function,
parameter, expression, control-flow/exception, assignment, decorator and literal
forms used by the three consumers. Node-reference codecs cover CodeNodeResourceName,
code-owner paths, expression/funcargs payloads and marker AST references. Preserve
the complete semantic state; an AST-only loader is not sufficient.

Constants use typed data encoding: decimal arbitrary-precision integers, exact
float/complex bit representations, Unicode strings, bytes and the remaining
supported AST constants. NaN/infinity do not rely on nonstandard JSON numbers.
This is structural constant representation, not general object serialization.
Runtime external-value support keeps Astichi's existing validated domain:
None/bool/int/float/str and nested tuple/list/dict, with the existing depth/cycle
rules. Do not broaden it to user objects or callback capture.

Python adapters reconstruct the target minor's AST using explicit field maps.
They may fill newly required empty/None fields only where their semantics are
identical; they must not drop a meaningful newer field. Artifact v1's required
syntax feature set must be representable on all three supported minors before
export succeeds. Newer syntax not in that common supported set is an export
error, even if the source compiler on one interpreter accepts it. No bytecode or
CPython AST pickle ABI crosses minor boundaries. The 3-by-3 export/load matrix
must prove this portable subset; same-minor tests alone do not establish it.

Logical origins are virtual names or repository-relative resource keys. Reject
absolute origin/provenance paths and process-object repr in metadata, using the
existing package normalizer as a model. Do not reject an ordinary user string
literal merely because it resembles a path. Location data and source maps are
preserved as data; emitting diagnostic/source text is allowed outside parsing.

Decode limits are 64 MiB per artifact, 100,000 syntax nodes, 100,000 semantic
records and syntax depth 512; existing external-value depth remains 32. The flat
node table permits bounded validation without recursive object construction.
Reject duplicate JSON keys, duplicate ids, unknown/missing fields, cycles in the
syntax graph, invalid references, unsupported scalar encodings and inconsistent
locations/semantic rows. Do not register partial native templates while validating.

These are trusted package/build artifacts, with the authority of generated code,
not an untrusted interchange format or a security sandbox. The digest detects
corruption, not adversarial re-signing. Import/install normal Python code and
JSON decoding are not disguised template compilation. Loading an artifact does
not execute its template body or import arbitrary modules named in artifact data.

## 4. Structural registration on the selected backend

### Python backend

Load validates and reconstructs a fresh typed syntax/semantic graph. Restore
BasicComposable's origin, markers, classification, ports, inventory, keep names
and identifier bindings with node references rebound to that fresh AST. Import
lower metadata through `register_lower_template_binding`/LowerEngine using stable
surface keys. No SourceKind/marker meaning changes occur.

The Python hygiene path must replace its parse/unparse clone with the owning
AST clone and structural renaming operation. Preserve the intended syntax,
locations and supported provenance; recompute derived scope indexes where needed
rather than transferring stale object ids. This generic Astichi fix is checked
against the existing hygiene/roundtrip corpus, not implemented in a consumer.

### Native Rust backend: necessary new facility

Metadata-only `register_template_snapshot` is not reused as if it were complete.
Add an owning native structural syntax codec and full registration entry:

```text
register_template_artifact(engine, syntax_rows, semantic_package, origin_rows)
    -> NativeTemplateHandle
template_artifact_snapshot(engine, template) -> canonical syntax/package rows
```

The first entry validates the rows, constructs a complete RustPython
ast::ModModule directly from typed fields, validates marker/package correspondence,
then registers NativeTemplate::from_package(package, Some(module), locator_base).
The second exports complete module and package state without handle ids. Decode
has direct constructors for the existing RustPython AST types; no parse_module,
parse_native_module, compile, source registration or from-source helper is called.
There is no dependency on an unspecified serde feature or whole-object pickle.
Unsupported node/field combinations fail with the corresponding artifact path.

The Python-facing canonical syntax rows and native codec share the same schema
catalog. Native offsets/source maps and Python location attributes are explicit
data with adapters, not reconstructed by reparsing emitted source. Validate each
lower locator/marker/scope reference against the decoded module before registration.
Rebind registered surface handles from stable keys in the destination engine;
never carry source-engine handles across registration.

An ArtifactTemplateBinding owns this structural state and registration policy.
It is a real native binding when native was selected. NativeTemplateCache imports
it with register_template_artifact into each destination engine. Builder tree
copy derives its AST from the decoded module, not native_source. Direct bind,
identifier bind, keep-name application and specialized re-projection use workspace
AST operations; they reconstruct/re-index a specialized structural package from
the resulting module without rendering/parsing source. `_can_native_specialize`
must recognize the structural binding rather than require native_source. The
source-backed binding path remains supported for ordinary source consumers.

The scoped backend changes required for source-free specialization are:

1. External overlays carry validated typed literal/AST payload rows instead of
   expression_source strings. Workspace and recursive materializers construct
   Rust AST constants/tuple/list/dict expressions directly. Keep insertion order,
   scalar values, contexts, depth/cycle rejection and ownership checks equivalent
   to the existing bind policy.
2. Reference paths lower through direct Name/Attribute constructors with the
   requested Load/Store/Delete contexts. Keep existing path/identifier validation;
   do not parse joined dotted strings.
3. Empty statement placeholders construct ast::StmtPass directly. No `pass` parse.
4. Native re-projection/register operations accept a decoded/specialized module
   with structural metadata. No source re-registration is hidden in copy/keep/bind.

These Rust changes are necessary because the current APIs store module=None or
parse source; no C++/platform rewrite is proposed. Put the codec in its own
cohesive native module rather than enlarging materialize_ir with a second compiler.
Reuse existing AST type semantics and validators. Do not introduce new enums.
All new/modified control-flow bodies use braces. Conditional sections have
cfg_if boundaries or enclosing conditional modules; no individual conditional
imports/unbraced declarations. Run a fast syntax-aware changed-source check that
also reads disabled branches; do not claim a broader existing-code migration.

### Parser-free profile and failure behavior

Artifact-loaded and compile_ast composables carry an owning parser-free policy.
Composition, copy and specialization preserve it. A parser-free scope accepts
artifact/structural resources and typed literal overlays; it rejects source-backed
resources that would need compilation or source re-registration. It does not
silently export/recompile a new resource during decoration. No native-to-Python
materializer fallback is allowed after native selection for this profile.

Existing source-backed compilation retains its old profile. This amendment does
not force every historical emitter/client onto artifact mode, nor redefine the
source API's selection behavior. Backend errors on the artifact path must escape
existing broad fallback catches as contextual CompiledTemplateBackendError.
Partial registration/failed specializations close or roll back their newly owned
engine/workspace resources; the original template remains usable.

## 5. Ownership and errors

Export bytes and internal normalized rows are immutable snapshots of unbound
template shape. Load creates fresh AST objects, typed metadata references and
destination-engine handles. No caller receives writable access to a shared
canonical AST. Independently loaded resources and independently bound branches
must not alias mutable AST/native workspace state; builder operations consume
owned clones and never specialize the artifact itself.

YIDL may retain immutable artifact bytes/validated rows as template shape data.
Its compiled generated-value wrapper produces independently owned composables;
it must not retain the last field record, class, callback, default object,
binding result or completed generated value. This is a template facility, not a
live-value cache. Repeated loading/binding costs are measured before attempting
any optimization. Private runtime engine handles belong to loaded instances and
are released with their owning objects, never serialized into the artifact.

Expose `CompiledTemplateError(ValueError)`, `CompiledTemplateFormatError`,
`CompiledTemplateCompatibilityError` and `CompiledTemplateBackendError`; the last
three derive from the first. Diagnostics name artifact/resource, schema/feature path, requested
and selected backend where relevant, and the action needed (regenerate/rebuild
the dependency tuple or choose a supported explicit backend). Digest mismatch,
unsupported version/minor, unknown syntax/semantic fields, incompatible bundle,
missing native capability and unexpected decoder shape fail before user class
execution. No source fallback, guessed field omission, backend relabeling or
opaque object reconstruction is permitted. Preserve causes for owning-layer
failures; do not relabel BaseException cancellation as a format error.

## 6. Generic YIDL emission and runtime generated values

Extend these existing emitters with keyword-only `precompile_resources=False`:
`emit_concept_runtime_source`, `emit_container_runtime_source`, and
`emit_matcher_runtime_source`. Propagate the policy through
`build_matcher_runtime_composable` as well. The default retains the existing source-emission
constructor surface and golden outputs. A single typed emission-policy object
threads the choice through recursive generation; do not add consumer-specific
rewriters or a second method-body emitter.

Opt-in emission traverses the entire generated-value graph before emitting:

| Generated-value position | Opt-in lowering |
| --- | --- |
| Authored code/template resource | Compile once at build, export full artifact, emit a compiled generated-value constructor |
| AstichiTemplateValue | Lower its template plus edge_arg_names/edge_bind/edge_keep_names recursively; preserve edge semantics and keep/identifier bindings |
| ImportedGeneratedValue | Precompile its static import/name composable at build; retain import semantics without serializing an imported object |
| Static literal-generated resource | Use the existing YIDL literal AST domain, compile_ast and export; no literal repr is executed |
| Property defaults, computed/production conditions and identity expressions | Recursively lower nested generated values, including tuple/list/dict containers; preserve ordinary nongenerated values and their supported import references |
| Rule/default resources, matcher-result productions and operation matchers | Use compiled generated-value constructors wherever resources enter generated runtime code; no remaining source-backed constructor on the opt-in engine path |

`constructor_expr_for`, `render_value_constructor`, constructor-import discovery
and matcher `_generated_value_piece` all consume the same policy. The compiled
constructor is `from_compiled_template(artifact_bytes)` in YIDL's generated-value
module. Its behavior-bearing wrapper satisfies the existing generated-value
contract and owns independent to_generator loading. Raw Composable/Python objects
do not become matcher resources. Empty contributions retain explicit empty
resource metadata so suppression does not depend on reconstructing source text.

The emitted module may embed immutable artifact bytes in normal generated Python
literal constructors. Resource names, logical origins/digests and authored .yidl
files remain inspectable; model output remains ordinary readable Python. No
separate consumer-maintained blob format is introduced. Wheel/sdist manifests
include the generated module, source resources and shared source digests.

Dynamic generation is explicitly bounded:

- Matchers selecting among precompiled resources or generating a validated
  literal/expression from current records remain supported. Dynamic from_literal
  returns a frozen LiteralGeneratedValue that owns normalized immutable syntax
  rows, constructed immediately from the existing YIDL literal AST converter.
  Its to_generator reconstructs a fresh AST and uses compile_ast without source
  parsing. Do not retain the input list/dict/set or cache those record values.
  Extend generated-value recognition, AstichiTemplateValue edge validation and
  constructor discovery to this behavior-bearing wrapper and the compiled
  wrapper, rather than assuming every resource is MatcherGeneratedValue.
  Preserve YIDL's None/bool/int/float/complex/str and nested tuple/list/dict/set
  literal domain, including its existing ordered dict and deterministic set
  emission semantics. This differs from Astichi's narrower external-bind
  domain; do not replace it with external value_to_ast or broaden external bind
  to complex/set. Default source emission of this wrapper renders the same
  from_astichi_code literal constructor as before, preserving existing goldens.
  Source rendering for diagnostics/emission is permitted; parsing it is not.
- A dynamically returned from_import(module, name) validates its existing dotted
  module/identifier inputs and constructs the astichi_pyimport marker plus name
  expression structurally through compile_ast. It never imports/captures the
  symbol during resource creation. Static instances are exported at build;
  dynamic instances receive fresh structural composables without a source
  fragment. Default emitted from_import constructors remain unchanged.
- Nested edge/self-data expressions use their compiled expression artifact.
  Materialize an executable AST, require its defined expression shape and
  compile ast.Expression in eval mode, with the same record/builtin scope as
  before. Evaluate per record; do not emit/parse strings or memoize evaluated
  mappings containing live data. The same rule covers assembly diagnostic
  expressions currently using emitted-source eval.
- Truly new source strings constructed at runtime are not precompilable. In
  opt-in mode reject a source-backed generated-value result before to_generator
  with a named resource/matcher diagnostic; advise returning a precompiled
  resource or structural literal/expression. Arbitrary callback bodies that
  explicitly invoke a compiler are outside the engine's parser-free promise;
  the engine must not invoke such a path as its own implementation. Source mode
  continues to support its existing runtime-source behavior.

Use a generated-runtime resource policy to validate every consumed result,
including operation-produced and dynamically returned generated values, not
only ASSEMBLY_RESOURCES. Code objects compiled from validated AST may be reused
without retaining record/evaluation results; this is not final-value caching.
Imports/normal Python module compilation and the final generated AST compile
are legitimate execution boundaries, not fresh fragment parsing.

Build-time matcher AST pieces currently assembled as BasicComposable by
`_expr_piece` are routed through compile_ast in opt-in mode so they carry validated
metadata and the structural policy. Runtime expression producers may return a
supported literal wrapper or compiled resource; an arbitrary caller-owned AST
or raw Composable is not implicitly accepted as a generated value. All resource
consumption in AssemblyScope and nested edge evaluation goes through the same
policy-aware resolver before to_generator; no closed-union/type-check escape
allows a legacy source wrapper to compile inside the protected interval.

## 7. Consumer selection and dependency truth

Dataclass regeneration selects precompile_resources=True from its first working
class. ComparisonCore is ordinary reusable .yidl and receives the same treatment
when consumed. Undoable's comparison/class regeneration later selects the mode,
including its context prelude. Unconditional field access and all accepted
Dataclass/Undoable semantics remain unchanged; this amendment changes the
compiler artifact boundary, not those public models.

Current published Astichi 1.1.3 and YIDL 0.1.0 do not provide this facility. Use
explicit local development candidates before product consumers are built:

| Distribution | Candidate and minimum dependency intent |
| --- | --- |
| Astichi | `1.1.4.dev0`, with artifact APIs and rebuilt native capability; package __version__ and build metadata agree |
| YIDL | `0.1.1.dev0`, requiring `astichi>=1.1.4.dev0` for its owning generation facility |
| Dataclass | Initial `0.1.0.dev0`, requiring `yidl>=0.1.1.dev0` and `astichi>=1.1.4.dev0` |
| Undoable integration | `0.1.1.dev0`, requiring the same candidate YIDL/Astichi minimums; Lifecycle marker dependency remains unchanged |

These are unpublished experimental build candidates, not authorized releases.
No tags, registry publication or public release workflow is invoked. Keep the
original Undoable tuple/results unchanged. Lock exact artifact hashes/member
revisions for the experiment's local wheelhouse; later compatible version numbers
alone do not prove the required APIs. Startup/decorating capability checks verify
the artifact ABI and selected native extension capability, rejecting stale native
binaries even when Python package versions match. Native capability/version
metadata must be updated when that facility is implemented, and its binary must
be rebuilt; do not fake capability flags on the existing extension.

Development uses current local sources. Installed checks disable editable sources
and workspace PYTHONPATH and install the exact wheelhouse tuple. Dependency
minimums must actually exclude published versions lacking the feature. A future
release may replace development minima only after its real capability exists;
release planning is a separate authorized task.

## 8. Amendment to the accepted design and plan

The accepted model APIs, field families, native comparison module, contextual
write equality, helper/retention rules and benchmark thresholds are retained.
These specific compiler assumptions are superseded:

- Design Section 9's ordinary generated-base emitter alone is insufficient for
  precompiled resources; regeneration now selects the generic opt-in artifact
  emitter and packages its outputs.
- Plan Stage A cannot start its successful native class until this owning-layer
  prerequisite passes. Insert the prerequisite checkpoints below before Stage A.
- Plan Stage G's first-decoration parser gate moves forward into those prerequisite
  and Stage A checks, and remains an independent installed first/second-decoration
  gate. A warm second decoration is not sufficient.
- Source/provenance roundtrip rules remain source-authoritative: edited emitted
  source is compiled as edited source, not overridden by an artifact/provenance
  payload. Artifacts are explicitly separate compiled build data. Editing a .yidl
  resource requires regeneration; mismatched bundled source/artifact digests fail
  the regeneration/package check rather than trigger runtime recompilation.

The owning active Astichi summary/coding docs and YIDL generated-value/emit docs
must be updated with this reviewed distinction during implementation. This
amendment does not rewrite historical documents or claim that existing source
consumers have all migrated.

## 9. TDD prerequisite checkpoints and review evidence

### Owning files and canonical seams

The following paths are relative to each named owning repository, not to the
workspace or this document's repository. New module boundaries are:

| Owner | Files and responsibility |
| --- | --- |
| Astichi | `src/astichi/artifacts/api.py` owns export/load; `codec.py` owns canonical syntax/semantic rows; `schema.py` owns the closed codecs, adapters and immutable frozen data carriers; `errors.py` owns the four errors. `src/astichi/__init__.py` exports the public functions/errors. |
| Astichi | `src/astichi/frontend/api.py` owns compile_ast and shared compile validation; `src/astichi/lower_engine/facade.py` and `native.py` own structural registration/capability checks; `src/astichi/model/basic.py` and `src/astichi/assembler/scope.py` preserve structural bindings and strict materialization; `src/astichi/hygiene/api.py` owns structural cloning/renaming. |
| Astichi native | `native_engine/src/artifact_codec.rs` owns direct typed AST codecs; `template_package_v2.rs`, `occurrence_store.rs` and `materialize_ir.rs` receive only the registration/package/payload integration they own. `lib.rs` exposes the new entries and `capabilities.rs` advertises them only after implementation. |
| YIDL | `src/yidl/generation/compiled_resources.py` owns the typed emission/runtime policies and recursive lowering/resolver. `matcher_values.py` owns the compiled/literal behavior-bearing wrappers and shared recognition/constructor APIs. `assembly_source.py`, `container_runtime_source.py`, `matcher.py` and `assembly_runtime.py` thread/use the policy. |

Astichi canonical artifact cases live in `tests/data/gold_src/compiled_template_resources.py`
and the existing golden harness, comparing original source compilation with
artifact compilation on each backend. Focused tests live in
`tests/test_compiled_template_artifacts.py` and
`tests/test_native_compiled_template_artifacts.py`; they own decoder, portability,
parser boundary and independent-state failures rather than duplicate the golden
success assertions. Extend the existing native literal/handoff/strict-fallback
tests where their established seam owns a changed mechanism.

YIDL canonical fixtures live in `tests/data/gold_src/dds_precompiled_resources.py`
and `tests/data/yidl/yidl_update_a_precompiled_resources/`, with existing source/
operation harnesses. Focused policy/forbidden-result tests live in
`tests/generation/test_precompiled_resources.py`. Keep default-source golden
outputs unchanged. Extend both existing `tests/versioned_test_harness.py` entry
points for the artifact matrix/installed runner without changing their owning
root discovery. The later Dataclass Stage A paths remain those in its accepted
plan. New helper modules stay cohesive; these paths do not authorize broad
compiler/backend rewrites.

### Observable increments

The owner records a reviewed amendment, a short implementation addendum/sequence
and its exact tuple before compiler/backend code. Each increment has observable
behavioral RED on the preceding implementation, identical-target GREEN and
focused refactor evidence; environment import failures do not count.

1. **Astichi artifact/structural compiler seam.** RED export/load and compile_ast
   roundtrip behavior, independent binds and first-use parser tripwires. GREEN
   the complete Python codec/backend and immutable ownership. Canonical source/
   AST comparisons cover holes, direct external/identifier binding, keep-name
   hygiene, params/funcargs, clauses, scopes, imports/exports/pass/ref/unroll,
   fallback/default holes, comments, origins and empty contributions. Narrow
   tests own corruption, limits, unsupported states and shape/ABI errors.
   Initial tests import the already-working owning package, create a baseline
   composable and assert the proposed public artifact/structural capability as
   the feature contract before exercising it. A missing proposed capability is
   an explicit behavioral assertion failure; a missing package/native library
   or broken test import is an environment failure and cannot serve as RED.
2. **Native structural restoration and payloads.** RED metadata-only snapshot
   workspace failure and parser-entry counts under load/copy/bind/materialize.
   GREEN full native IR/package registration and structural literal/ref/pass/
   re-projection routes. Test destination-engine ownership, engine-close/stale
   handles, independent workspaces and no native-to-Python fallback. Explicit
   native selection must remain native through emitted AST handoff; missing
   capability must fail without silently compiling source.
3. **YIDL whole generated-value graph.** RED opted-in emitted concept, standalone
   matcher and operation fixture with nested edge/self-data/import/literal/default
   resources and runtime literal results. GREEN recursive policy propagation,
   independent generated wrappers and AST evaluation. A forbidden runtime-source
   result must fail before engine parsing. Compare default-source emission to
   original goldens unchanged; compare opted-in semantic/source behavior to the
   independent original source-mode case, not an artifact-only self-consistency
   assertion. Verify source metadata cannot capture current records/callbacks.
   Include dynamic complex/set literals as well as ordinary literal containers,
   dynamic imports, compiled edge wrappers and empty resources so the narrower
   external-bind domain or old closed GeneratedValue union cannot drop a path.
4. **Portable installed artifact seam.** Export on each supported minor and load
   on all three (nine pairs), including Python/native cross-backend roundtrips.
   Test incompatible minor/codec/backend capability failures with no fallback.
   Wheel/sdist install and regeneration use only packaged resources/logical names
   and locked candidate dependencies; old published dependency/stale-extension
   combinations reject clearly. Run first and second Dataclass-style class build
   from precompiled resources in fresh installed processes.
5. **Resume Dataclass Stage A.** Add the product's genuine RED/through-YIDL GREEN
   first class and normalization/slot/signature/metadata corpus. The new generic
   facility must not become a reason to omit its behavioral RED. Re-run the
   supported-minor Stage A checkpoint before the owner commits/sends Stage B.

Source parsing tripwires guard ast.parse, astichi.compile of fragments and Python
compile of strings within resource/runtime helper paths, allowing only validated
AST compilation. Normal importing of static Python modules is distinguished from
fragment generation. Start native parser-entry accounting before resource load;
instrument/count the owning parse_native_module/parse-expression entry paths so
private native reparsing cannot hide behind a successful Python tripwire. Assert
zero new source-parse entries for first and second load/decoration/bind/copy/
materialization. Source compilation at build remains observable outside that
protected interval. Tests do not force Python selection to conceal missing native
support or pre-call to_generator to warm parser caches.

Use richer canonical examples at the owning layers for success and source shape;
focused tests cover invalid metadata, failure cleanup, parser boundary and
ownership mechanics. Add syntax-aware source checks over modified Rust files,
including disabled branches. Run focused suites after each change, then full
relevant Astichi/YIDL suites and three-minor artifact matrix at the owning
checkpoints. Preserve the observed pre-amendment baselines (3.12: Astichi
2544 passed/104 skipped; YIDL 299 passed/2 skipped) with their owner's exact logs,
without interpreting those results as evidence for this facility. Record all
new skips/unsupported syntax/backend cases and retain failures before remediation.

## 10. Performance limits and acceptance

This facility avoids source parsing at resource use; it does not promise faster
generation. JSON validation, complete AST reconstruction, native conversion,
destination registration and cloning can cost more time/memory than existing
cached-source paths. Persisted full syntax plus semantic rows are larger than
AST provenance alone, and native/Python artifact views may coexist. Any immutable
shape-data caching must preserve fresh binds and avoid live field/default/callback
retention; optimize only after measurement.

Extend the accepted measurement manifest with cold/warm artifact load, structural
registration/bind/materialization, build/export time, artifact byte size and
peak allocated/native memory; label Python versus selected native backend and
source-mode reference explicitly. Use the plan's repeated-process/raw-unit/
variation methodology. Existing instance-access thresholds stay unchanged;
compiler artifact measurements have no invented advance parity threshold. A
performance limitation is reported rather than worked around by source parsing
or a hidden backend change.

Acceptance requires both fresh review verdicts, then actual owning-layer and
installed cross-minor/backend evidence. It does not accept unsupported native
snapshot semantics merely because the APIs have familiar names. If full IR/
semantic codec or source-free native specialization cannot meet this contract,
stop and redesign that owning boundary; do not resume product code on an
inaccurate parser-free claim.
