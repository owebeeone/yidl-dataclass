# Native structural lowering addendum

**Status: proposed, documentation only; implementation remains paused for fresh
Consistency/Safety review.** This supplements the accepted compiler amendment
`356321965b9a527aeee66585235f6883c0312dd4` and its prerequisite execution
sequence. Public Astichi/YIDL/Dataclass APIs, artifact v1 format/codec, consumer
contracts and source-authoritative provenance remain unchanged. No release,
publication, product implementation or completion claim is authorized here.

## 1. Discovered boundary and retained obligations

P2's current candidate restores complete RustPython modules and typed lower
packages, performs structural copy/specialization, and counts actual native
parser entries. Its focused core check passed 13 tests on CPython 3.12.12. This
establishes that scoped mechanism only. The four-backend canonical corpus does
not pass: its latest attempt has 94 passed and 78 failed. Supported-minor/full
regression and installed native acceptance remain outstanding.

The source frontend has two composition representations. Plain
`BuilderHandle.build()` calls `materialize/api.py::build_merge`, producing an
unmaterialized module containing insertion shells. `BasicComposable.materialize`
historically uses the Python materialization pipeline even with native selected.
`AssemblyScope` instead retains occurrences/edges/overlays and can send those
operations to Rust. Its existing native finalizer does not implement the entire
retained shell language or the Python pipeline's complete lexical hygiene.

Re-adding a flattened build as a single `Root` occurrence supplies neither its
original native edges nor shell lowering. It can also prepend an extra build
path and make descendant references ambiguous. A module and package decoder
alone cannot close this boundary.

This supersedes the assumption in compiler amendment Section 4 and P2's execution
row that full module/package restoration plus the four listed specialization
changes suffice for all native artifact materialization. Those requirements
remain necessary. This addendum additionally requires complete native structural
lowering of the existing marker-rich module before P2 can complete. It does not
reinterpret the old native capability label as proof of that coverage.

The narrow representation envelope remains: native Rust rejects frozenset
`Constant` values, including nested tuple constants, and surrogate code points
in serialized syntax/semantic/package/origin strings, with the exact offending
path before registration. The baseline native parser substituted U+FFFD for
escaped surrogates and rejected raw surrogate text/origins; ordinary source
`frozenset(...)` produces a supported `Call`, and YIDL `from_literal` already
rejects frozenset values. Ordinary Unicode, set/complex expressions, tuple/bytes
constants and arbitrary-precision integers remain required. This exception does
not authorize rejecting insertion shells, staged builds or existing YIDL paths.

## 2. Self-contained input and choice of lowering route

Use the existing marker-rich syntax and saved semantic state as the durable
input. The artifact already contains the module, annotations, scope keep data,
ports, inventory, package references, identifier bindings and origin. A built
module's source-authoritative language retains block/parameter/elif insertion
shells, expression insert calls, synthetic root scopes, target names, `ref`,
`kind`, `order`, payload bodies/signatures and explicit boundary binding syntax.
These describe the remaining materialization semantics independently of the
original mutable Builder graph. Preserve their metadata and stable node
references through artifact load/copy/bind/keep/re-projection.

Do not add a replay recipe, original BuilderGraph, callbacks, live values,
workspace handles or a new wire field to BasicComposable/artifact v1. Do not
reconstruct source text to recover a graph. Native lowering interprets the
retained language, not an invented reconstruction of the original instance graph.

Direct Builder graph lowering is an optional later optimization. Before
`build_merge`, `_resolve_build_graph` retains live root/source placements, ordered
additive edges, descendant/indexed targets, per-edge bindings/keep names,
assignments and explicit identifier wiring. Existing AssemblyScope occurrence,
edge and overlay APIs can lower those inputs without flattening. That route alone
cannot handle already-built/staged/loaded values, which have no original edge
recipe. Its output must agree with the required module lowering route and all
canonical expectations; it is not a P2 completion prerequisite or an escape from
staged-value coverage.

Native pre-expansion is a required seam before generic graph merge or indexed
edge resolution; deferring direct complete graph-to-operation lowering does not
defer it. The read-only `_resolve_build_graph` supplies live instances/edges;
current `build_merge` then performs Python `unroll_tree` before resolving indexed
targets. Do not invoke that transforming path for a strict native build. Derive
the existing expansion decision from the requested `unroll` and live indexed
edges: `True` expands live instances, `auto` expands iff an indexed edge exists,
and `False` with indexed edges retains the existing early conflict diagnostic.
When expansion is requested, clone destination-owned native template/workspaces,
expand their loops in Rust, then project fresh syntax/port/shell-index facts for
read-only target validation and graph planning. No source reparse, Python
`unroll_tree`, transformed-Python-tree registration or new durable expansion flag
is permitted. These prepared views/workspaces belong to this build only; original
templates remain unchanged and reusable.

For strict native Builder use, the generic frontend may recognize and resolve
placements against those prepared views. It must not perform unroll, identifier
rewrites, hygiene or other newly native-required semantic transformations.
Author the same insertion-shell language in Rust from referenced owned modules.
This is shell construction, not direct occurrence-edge lowering: it preserves
the required staged representation. The Python planner must not call
`build_merge` as a transforming merge/finalizer for this route. Existing generic
frontend assembly remains available to ordinary source/Python profiles.
All code-changing shell construction, normalization, unroll, identifier
resolution, hygiene and realization in the strict native profile executes on
Rust-owned IR. The compiler must not run the old Python materializer and then
register its result as native work.

Retained-module finalization consumes the current marker-rich module, not a
replay of the pre-expansion request. Expanded loops have already been replaced by
their copied bodies and refined holes; finalization neither restores nor expands
them again. Only still-present loop markers selected by the current build-stage
request can be expanded in Rust. Within one build, transient phase completion
prevents reapplying its expansion plan; across copy/export/load, the structural
absence of consumed markers is sufficient. Preserve existing stage behavior for
unrequested loops and newly supplied contributions, without a wire field, saved
recipe or changed public unroll API.

## 3. Owning boundaries and plan interface

Paths in this table are relative to the named owning repository; additions are
proposed, not implemented interfaces.

| Owner | File/component and responsibility |
| --- | --- |
| Astichi | `src/astichi/lowering/native_plan.py`: frozen typed plan/view carriers, plan ownership/shape validation and phase orchestration; no user-code transformation or runtime field dispatch |
| Astichi | `src/astichi/materialize/gate_facts.py`: extract existing gate recognition into reusable read-only queries, shared by Python and native frontends |
| Astichi | `src/astichi/hygiene/plan.py`: pure lexical occurrence/collision planning extracted from existing owning analysis; both backends consume the same decisions |
| Astichi | `src/astichi/materialize/api.py`, `model/basic.py`, `assembler/scope.py`: route the structural profile through the native workspace finalizer, preserving metadata/result APIs and prohibiting fallback |
| Astichi native | `native_engine/src/structural_lowering.rs`: phase/workspace coordinator, plan validation, generation checks and transactional result publication |
| Astichi native | `native_engine/src/structural_lowering/shells.rs`: block, root, parameter, elif and expression/funcargs shell realization, ordered structural splices and suite repair |
| Astichi native | `native_engine/src/structural_lowering/names.rs`: identifier/boundary resolution, precise lexical field rewrites and suffix removal |
| Astichi native | `native_engine/src/structural_lowering/unroll.rs`: typed-domain body copying, substitutions, indexed hole refinement and nested expansion |
| Astichi native | `native_engine/src/structural_lowering/directives.rs`: default/fallback normalization, pass/ref, managed imports, comments and residual directive cleanup |
| Astichi native | Existing `artifact_codec.rs`, `artifact_decode.rs`, `template_package_v2/artifact_rows.rs`, `materialize_ir.rs`, `parser_ir.rs`: complete codecs/package checks, reusable native transforms and final AST projection; avoid adding another compiler to the large workspace file |

Reuse marker/surface behavior objects, shell/ref resolution, parameter/funcargs
recognition, unroll-domain validation and lexical occurrence analysis. Separate
read-only planning from any existing helper that mutates a Python tree. A planner
may consume a newly projected caller-owned syntax view after a Rust phase; it
must not call `materialize_composable`, `build_merge` as a finalizer,
`rename_scope_collisions`, `unroll_tree`, `_realize_*`, `_flatten_*`, or a Python
AST transformer to prepare a transformed tree for Rust. The Python backend keeps
its existing pipeline, consuming shared pure decisions where refactoring is
necessary. Refactors must preserve its golden outputs and failure diagnostics.

The internal pair is a Python phase planner and a Rust workspace plan applier.
A frozen `NativeLoweringPlan` contains only validated immutable facts/actions:
owner/workspace generation, phase identity, stable node/scope references, expected
node kinds/field spellings, ordered operand references, literal data, lexical
rewrites and logical diagnostics. Existing semantics use existing behavior
objects/operation keys; new action classes own validation/lowering behavior.
No enums, scattered magic tags, arbitrary objects, AST nodes, executable source,
user callbacks or transformed output modules enter plans. Plan instances are
transient compiler data, never exported as artifact semantics.

`NativeSyntaxView` pairs a fresh read-only projection with a separate node-address
map. It does not stamp new unsupported attributes onto artifact AST nodes.
Workspace-owned node identities are independent of Python `id`, current list
indexes and process handles serialized in artifacts. On decode, associate native
nodes with canonical input row identities. Within a workspace, a logical node
key is its input origin identity plus deterministic copy lineage; a scope key
uses its owning node key and existing lexical-scope identity. Native copies assign
fresh lineage for each occurrence/unroll iteration, while moved nodes retain
identity. Synthesized nodes obtain deterministic phase/parent/ordinal identities.
Identities and location attributes are separate; preserve original locations,
source annotations and singleton metadata. Address operator/context data by its
parent node and field occurrence, preserving canonical shared-singleton metadata
without pretending those unit values are independent lexical scopes. A plan can target a particular copy
without unintentionally rewriting its siblings.

The Rust applier checks exact plan type/closed fields, limits, owner/epoch,
workspace generation, referenced nodes/scopes and expected old values before
mutation. It resolves stable keys in its own current index, not a stale Python
path. Applying a phase increments workspace generation; reuse of an old plan
fails. A structural splice rebuilds the native index before another view/plan is
issued. Deterministic identities are internal addressing, not new public AST or
artifact fields. A projected view is disposable; fingerprint it before/after
read-only planning and reject planner mutation. Never import its possibly mutated
AST back into the native workspace.

The internal native entry points are `prepare_structural_workspace` (clone owned
module/package and establish identities), `structural_workspace_view` (fresh
projection plus address map/epoch), `apply_structural_plan` (validate and execute
one typed phase), and `finish_structural_workspace` (postconditions, fresh result
projection and semantic facts). They accept destination-owned handles and exact
compiler-owned carriers only. No general callable, source-string or replacement
module argument exists. Action classes form a closed private catalog with paired
Rust handlers; malformed or unknown classes fail before traversal. Rust owns
suite edits, field edits, copies and synthesized nodes; Python owns recognition
and immutable decisions only. Both high-level entry routes use this coordinator.
Future backends must implement the same ownership/semantic contract before
advertising support.

## 4. Required phase order and semantics

Follow the ordinary source pipeline's order, including interactions that are
observable through hygiene and diagnostics. The table describes Rust execution;
read-only recognition and immutable decision planning can remain Python-owned.

| Phase | Required behavior |
| --- | --- |
| Build-time expansion, where requested | Respect existing `unroll=True/False/auto`, indexed-target requirements and root/source reachability. Required native template/workspace pre-expansion precedes any generic graph merge and indexed edge resolution; derive fresh port/shell facts afterward. For a retained module, expand only still-present loop markers selected by the current stage, never replay an earlier expansion or import a Python-expanded tree. |
| Default normalization and gate | Recognize required/defaulted/fallback block and expression holes without making a default mandatory. Determine locally satisfied block/parameter/elif/expression targets, unmatched supplies, external demands and unresolved identifier slots. Fail before hygiene or callback execution. Read-only gate queries must understand supplies inside the retained shell language. |
| Identifier and parameter resolution | Resolve explicit `__astichi_arg__` sites, boundary imports/passes and identity bindings, preserving explicit wiring state. Realize parameter shells into their owning signatures before lexical analysis; preserve positional-only/regular/keyword-only/variadic groups, defaults, annotations and collision rules. Remove optional annotation holes. Reject unresolved boundary demands with the existing names/locations/hints. |
| External reference lowering | Apply typed external overlays and direct `Name`/`Attribute` refs with proper Load/Store/Delete contexts. Preserve original base expressions, evaluation order, shadowing and nested ownership. No dotted-string/expression parsing. |
| Complete lexical hygiene | Compute the same scope identities, role classifications, collision domains, ordinals, trust/preservation decisions, synthetic import bindings and exact emitted spellings as the Python source pipeline. Apply precise node-field rewrites in Rust before flattening fresh scopes. |
| Realization | Capture payload-local directives. Realize expression/call-argument inserts, flatten block/root shells, realize elif chains, then insert planned managed imports. Preserve stable source order and existing order tie-breaking. Validate variadic/dictionary shapes and duplicate/conflicting arguments before publication. |
| Residual cleanup | Capture pre-strip demand/supply facts using the same semantics; strip residual directives under executable/comment-preserving policy, remove keep suffixes, assert no arg suffix/pyimport/insertion machinery remains, repair required empty suites with direct Pass nodes, and compute post-strip classification/result metadata. |

Block insertion and synthetic root shells are compiler scope boundaries, not
runtime function calls. Flatten their bodies only after imports/passes, scope
trust and lexical renaming have been resolved. Preserve nested/descendant `ref`
addressing, explicit user aliases, source-only palettes, repeated independent
contributions, staged class/function heads and empty contributions. Do not prepend
another logical `Root` path merely to invoke the finalizer.

Parameter and elif payload shells are declarations of compiler contributions;
remove their wrapper definitions after applying their signature/clause payloads.
Expression wrappers handle scalar, tuple/list expansion and positional/named
funcargs domains, including payload-local directives and transparent sentinels.
Preserve outer binding and zero/one/many element behavior rather than routing a
set/complex YIDL literal through the narrower external-binding domain.

Default/fallback selection follows the existing gate and ordered contribution
rules. Keep comments/origins through the same phase at which ordinary
`emit_commented` preserves them. Executable mode strips comment markers; comment
mode returns the source renderer's supported comment data without executing a
Python materializer. Managed pyimports accept the existing dotted-name and
validated typed-literal module forms, preserve symbol/alias semantics, collision
renames and final import order; they do not import user modules during planning.

Unroll is macro expansion, not scope introduction. Copies share the enclosing
scope; expand outer loops before inner domains, substitute Load occurrences,
refine hole names with existing index suffixes and preserve tuple unpacking.
Reuse existing rebind/name-bearing marker restrictions and rejection of reserved
else/async forms. Empty domains erase their contribution. Bounds apply to expanded
output, not merely the original compact graph; plan size cannot authorize an
unbounded or cyclic copy operation.

Hygiene must cover the entire existing lexical model, not only pyimport
collisions. Reuse role classification of names/arguments, definitional bindings,
imports, suffixes, explicit boundary targets, nested fresh scopes and synthetic
import bindings. Pin identifier-resolution targets only at hygiene-relevant
positions; keyword labels alone do not protect unrelated lexical bindings.
Trusted explicit keep declarations and preserved-but-untrusted binding targets
remain distinct. Preserve the first-preserved/earliest-scope tie-breaking and
sorted collision-group numbering (`__astichi_scoped_N`), including collisions
across sibling root contributions. Honor global/nonlocal/class/function/lambda/
comprehension scope behavior, shadowing, nested declaration ownership, metadata
scope keeps and existing closure semantics. Preserve exact canonical spellings,
including cases whose permissive semantics require explicit import wiring.

## 5. Routing, state and compatibility

Artifact/compile_ast native `BasicComposable.materialize`, executable AST access,
commented emission and merged/staged values use this finalizer directly on their
owned module. `NativeTemplateCache` restores the complete module/package into
its destination engine. Copy, keep, identifier/external binds and specialization
remain structural native operations; re-projection rebuilds metadata without
parsing source. AssemblyScope operation-stream composition feeds its result into
the same finalization semantics, so the two routes cannot silently differ in
hygiene, residual directives, defaults or result ports.

Normal source compilation and its existing default profile remain supported.
This addendum does not switch every legacy consumer to native finalization or
change its fallback/discovery policy. The new strict profile is checked after
effective backend selection and never falls back to Python materialization,
source registration, emitted-source parsing or a final transformed-Python-tree
re-import. Python artifact mode remains a real supported backend.

Public source emission stays readable and source-authoritative. Compiled artifact
bytes remain distinct build data; no provenance payload or edited source is
superseded by a hidden recipe. All three public artifact APIs and v1 fields stay
unchanged. Plans/native addressing are recreated per owned workspace, never
serialized into producer/consumer artifacts. Meaningful unsupported newer syntax
and artifact CPython 3.15 remain rejected; normal source regression on the
configured 3.15 runtime remains required.

The candidate binary's current artifact capability advertisement is provisional,
not an accepted full-feature claim. Do not ship/release it or resume product work.
Final capability advertisement must cover complete restoration, ownership,
structural specialization and this lowering pipeline, with a rebuilt extension
and truthful structural ABI/codec metadata. A stale or restoration-only extension
must fail the strict-profile capability guard. Require both
`native.compiled_template_artifact.v1` and
`native.compiled_template_lowering.v1`, structural payload ABI 1 and codec 1 after
selection. The latter flag is published only when the full pipeline and required
gates pass; the current candidate does not provide it. This internal capability
addition retains artifact v1 and candidate version minima. Version numbers alone
do not establish support.

## 6. Errors, preflight and cleanup

Preflight closed syntax/package/origin/plan data before expansion, custom hooks,
normalization or registration. Preserve artifact byte/node/depth budgets and add
an explicit expanded-node/action budget under the existing 100,000-node envelope;
reject predictable overflow before cloning and enforce the bound while applying
copies. A plan referring to deleted, wrong-kind, foreign or stale-generation nodes
fails with phase/node/resource context, never guesses a current positional match.

Retain ordinary invalid-source/marker/signature/boundary/hole diagnostics and
relative logical origin locations. Unsupported native representation or missing
backend functionality produces contextual CompiledTemplateBackendError;
corruption/schema/reference contradictions produce CompiledTemplateFormatError.
Actual user/compiler semantic errors are not relabeled as success or hidden by
fallback catches. BaseException cancellation is propagated unchanged.

Work on a private Rust workspace clone; publish the result only after every phase
and postcondition succeeds. Newly created templates/workspaces/plans and temporary
views are destination-owned and released/rolled back on all failure/cancellation
paths. The original composable/template/bytes remain usable for another independent
bind/build. Cross-engine plans, stale handles and closed engines reject. No module,
manager, user callback, input container or transformed Python tree is retained in
immutable shape caches. Plans may retain only their bounded immutable compiler
facts until application, then are discarded.

## 7. Evidence classification and required exit gates

Astichi evidence paths are under `dev-docs/experiment-evidence/precompiled/p2/`.
Preserve all attempts/hashes; append corrections rather than rewriting history.
`p2-frozen-manifest.json` records the paused code/test/evidence hashes, ignored
prototype build products and original raw-to-sanitized evidence mapping. It
excludes its own digest; the owner records that digest separately. This freezes a
provisional tuple for review, not an accepted P2 implementation checkpoint.

| Attempt | Classification |
| --- | --- |
| `p2-native-initial-red` | Six genuine missing-native-restoration/path-diagnostic failures after a working baseline; retained RED |
| `p2-native-core-green` | 13 focused tests pass; scoped core only, not full native/cross-minor acceptance |
| `p2-singleton-metadata-red` | Its new equality assertion passed and did not prove annotation loss; only the existing re-projection failure was RED |
| `p2-explicit-singleton-red` / `p2-singleton-identity-red` | Explicit annotation assertion and then frozen-input/shared-singleton identity check expose actual codec/metadata requirements; retain input-precondition strengthening history |
| `p2-canonical-backend-red` | 120 failed/52 passed; 51 failures are over-broad tripwire rejection of canonical oracle source execution after generation, not behavioral RED |
| `p2-canonical-boundary-classification` | 78 failed/94 passed; seven remaining tripwire failures are deliberate intermediate source-execution oracles inside build callbacks and require an explicit oracle boundary; remaining failures/output mismatches are unresolved native behavior |

The latest 78 failures partition by their terminal diagnostic as follows:
seven oracle-tripwire failures; 45 native finalization failures; 11 unresolved
parameter payloads; four extra-Root descendant ambiguities; two dynamic pyimport
failures; two missing identifier-bound `Holder` names; two lexical-hygiene output
differences; and five saved-package/module correspondence failures. The latter
five occur for native producers: two defaulted-hole, two Lifecycle-surface and
one class-head case. These remain ordinary codec/metadata integration defects;
fix exact semantic correspondence, including defaults and locators, rather than
relaxing validation. The structural shell/hygiene route addresses the inspected
finalization assumption, not every defect in this partition. They must pass the original expectations; no new
skip, fallback, weakened source comparison or golden regeneration closes them.
The initial corpus count is not itself an architectural verdict. This proposal
addresses the inspected representation/finalization boundary.

After acceptance, strict TDD increments separately cover gate/default and
parameter/boundary phases, lexical plans/native rewrites, shell/expression/elif/
root realization, pyimport/ref/pass/comments, and unroll/staged integration.
Each captures an actual behavioral RED, identical-target GREEN and focused
refactor evidence. No environment or oracle-tripwire failure is counted as RED.
Keep canonical success assertions in the established 43-case corpus and focused
units for malformed plans/diagnostics/ownership; do not duplicate its positive
behavior assertions in another unit suite.

Required gates before P2 completion:

1. All 43 existing canonical cases under four Python/native producer-consumer
   pairs on each supported minor, with unchanged independent source-mode expected
   outputs and behavioral validators. Include first and second resource use,
   direct/staged Builder and AssemblyScope paths; source authority/regeneration
   corpus remains unchanged. Existing cases own parameter/funcargs/class-head/
   default, elif, root, boundary, ref, pyimport, unroll and hygiene success coverage.
2. Actual lowest native parser-entry counter stays unchanged through first/second
   load, structural compilation, copy/bind/keep/identifier specialization,
   build/unroll/materialization/commented emission and final AST projection.
   Python tripwires block fresh fragment parsing and allow only static module
   imports plus AST compilation. Deliberate canonical source execution is bracketed
   outside generation at an explicit oracle boundary, after counter assertions;
   restore protection before any further generation. Do not whitelist virtual
   filenames or warm resources. Guard every new planner and generic graph assembly seam against calling old
   Python mutators/materializers, including `unroll_tree`, or accepting a transformed
   output module. Assert native pre-expansion precedes indexed-target validation
   and generic merge, and retained/staged finalization does not duplicate bodies
   or indexed hole suffixes already produced by that expansion.
3. Focused failures: unresolved/mismatched shells, duplicate signature/keyword
   contributions, illegal unroll domains/rebinds, foreign/stale node/scope/plan
   references, malformed/cyclic/shared/custom/oversized rows, invalid contexts,
   unsupported literals/metadata, closed engines and wrong destination owners.
   Test cancellation at view/planning/apply/publication boundaries, unchanged
   originals, partial-registration rollback, independent copies and fresh binds.
   Include original-source annotations on singleton and ranged nodes, module/
   argument/type-ignore metadata, exact huge integers without changing digit
   limits, Unicode and signed/nonfinite float/complex bits.
4. Complete owning Astichi suite on 3.12/3.13/3.14 and configured ordinary source
   suite on 3.15 once the final implementation stabilizes; preserve legacy warnings
   and unsupported-artifact skips honestly. Re-run changed focused targets after
   each increment, not the full unchanged matrix repeatedly. Native selected means
   actual Rust transformations at every code-changing phase, verified by operation
   counts and forbidden-Python-transformation tests as well as parser counts.
5. Rebuilt wheel/sdist capability and installed native probes, followed by the
   accepted P4 nine-minor/four-backend matrix where applicable. Confirm origin,
   ABI, stale-extension rejection and parser freedom in isolated installations.
   Run the owner's syntax-aware Rust scope checker on all changed/new files,
   including disabled conditional branches. No broader migration is claimed.

Planning/projection/clone costs are recorded separately from native application,
artifact load and total materialization using the accepted repeated-process/raw
units methodology. No advance speed/parity claim or new favorable threshold is
introduced. This addendum returns to dual design review before implementation;
P1 acceptance and its installed Python portability evidence remain scoped facts.
