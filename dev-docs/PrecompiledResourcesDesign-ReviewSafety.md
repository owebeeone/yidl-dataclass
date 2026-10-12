# PrecompiledResourcesDesign — SAFETY-AXIS REVIEW

**Review object:** `dev-docs/PrecompiledResourcesDesign.md` in yidl-dataclass at `356321965b9a527aeee66585235f6883c0312dd4`; proposed owning-layer amendment, documentation only, reviewed 2026-10-12.

**Baseline:**

| Repository | HEAD |
| --- | --- |
| yidl-dataclass | `356321965b9a527aeee66585235f6883c0312dd4` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| astichi | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were inspected with read-only commands. Targeted `git diff HEAD -- …` checks confirmed that the reviewed amendment, controlling Dataclass documents/checkpoint, and inspected Astichi/YIDL sources matched their committed versions. All six heads matched the tuple at both the start and end.

**Date:** 2026-10-12

**Axis:** Safety — attack degraded paths, malformed state, ownership, accidental execution or retention, backend failures and parser-free boundary escapes. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — zero findings. This accepts the proposed design boundary only; it establishes no compiler implementation, runtime, installation, portability, performance or release result.

---

## 0. Evidence base

Paths below are relative to the named owning repository.

| Owner | Evidence inspected |
| --- | --- |
| Workspace | `AGENTS.md`; `AGENTS_GWZ.md`; canonical Safety prompt; review-loop process instructions |
| yidl-dataclass | `dev-docs/PrecompiledResourcesDesign.md`, lines 1–587; `CurrentProgramCheckpoint.md`; accepted `DataclassDesign.md` and `DataclassPlan.md`; both corresponding `ReviewResult` documents |
| astichi | `AGENTS.md`; active `dev-docs/AstichiSingleSourceSummary.md`, especially composition, native handoff, inventory, hygiene, source authority and artifact-copy sections; `dev-docs/AstichiCodingRules.md` |
| yidl | `AGENTS.md`; active `dev-docs/YidlDesignSummary.md`, especially §§26, 26.1, 30 and 34; `dev-docs/YidlCodingRules.md` |
| astichi | `src/astichi/frontend/api.py`: source compilation, marker validation, native selection and registration; `model/basic.py`: stored trees, identifier/keep/external specialization and re-projection |
| astichi | `src/astichi/lower_engine/facade.py`: binding carrier, Python/native caches, structural metadata registration and artifact-copy helpers; `lower_engine/native.py`: effective engine selection and capability discovery |
| astichi | `src/astichi/model/inventory.py`, `model/ports.py`, `model/external_values.py`, `asttools/clone.py`; native fallback in `assembler/scope.py` |
| astichi native | `native_engine/src/occurrence_store.rs`: template ownership and metadata-only snapshot restoration; `template_package_v2.rs`: package rows and source registration; `parser_ir.rs`: AST conversion catalog; `materialize_ir.rs`: module requirements, external overlays, pass and reference parsing; `handles.rs`; `capabilities.rs` |
| yidl | `src/yidl/generation/matcher_values.py`: generated-value union, lazy compilation, literals/imports, constructors, edge evaluation; `matcher.py`: structural expression pieces; `assembly_source.py`; `assembly_runtime.py`: roots, contributions, empty suppression, bindings and diagnostic evaluation; generated-value call sites in `container_runtime_source.py` |

Read-only in-memory probes ran with `PYTHONDONTWRITEBYTECODE=1`:

- A shared AST with fourteen repeated tuple levels contained 31 unique input nodes. Existing `clone_ast` expanded it to 49,152 walked nodes. This establishes why non-singleton occurrence identity must be validated before reconstruction.
- Standard JSON decoding accepted nesting depth 512 and raised `RecursionError` at depth 2,000 for a 4,001-byte input. This establishes a malformed-input case the owning decoder must translate and reject under the proposed error contract.

These probes exercised existing primitives, not proposed APIs. No files were written; no builds, regeneration, Git mutations or implementation tests ran. No current peer report was read and no drafter or peer was contacted.

## 2. Invariant analysis

### Complete native restoration is an owning-layer requirement

The missing prerequisite is real. `parse_template_snapshot` constructs a native template with `package_v2: None` and `module: None`; native materialization operations require the module. Current package registration obtains that module through source parsing.

The amendment does not disguise either mechanism as restoration. Lines 209–256 require direct construction of a complete RustPython module, complete package restoration, correspondence validation and destination-engine registration. The existing module and package types provide concrete owning seams for this addition. Their missing decoder and structural registration APIs today are implementation obligations, not design findings.

The change is architectural in scope: it introduces a reusable structural compiler/artifact boundary in Astichi and recursive resource lowering in YIDL. No architectural defect was established. Feasibility remains conditional on implementing the complete codec and source-free specialization route; lines 582–587 require redesign if that contract cannot be met.

### Parser-free execution reaches below the resource wrapper

The attack found actual parsing in existing native external overlays, pass construction, reference-chain construction and specialized re-registration. Existing YIDL edge and diagnostic evaluation also compiles emitted expression strings.

Lines 244–256 explicitly replace the native fragment-parsing paths. Lines 269–281 preserve the parser-free policy through composition and specialization and prevent existing fallback catches from concealing a native failure. Lines 370–398 require AST evaluation and policy-aware resolution for nested and dynamically produced resources.

A cached legacy wrapper does not become an approved artifact resource merely because its first compilation happened earlier. The protected profile rejects resources needing source compilation or re-registration and does not export them opportunistically during decoration.

### Structural and semantic state must agree before registration

The artifact contains more than executable syntax: marker objects, classification, ports, inventory, defaults, scope boundaries, payloads, bindings and lower-package rows are part of the contract.

That matches actual state requiring restoration, including node-backed resource names and expression/funcargs inventory payloads. Lines 138–153 require stable references and registered semantic codecs; lines 178–183 reject invalid references and inconsistent semantic rows; lines 218–232 require module/package correspondence validation before native registration.

A decoder that merely checks that a locator reaches some node would not satisfy these provisions. Marker meaning, scope ownership and payload correspondence remain required validation, including on the Python path.

### Corruption and resource limits have explicit rejection rules

The design supplies byte, syntax-node, semantic-record and syntax-depth limits, rejects duplicate keys/ids, cycles, unknown fields and unsupported scalar forms, and forbids partial registration during validation.

The shared-node probe did not establish a permitted counterexample. Lines 139–142 require distinct occurrences to remain distinct and allow canonical sharing only for operator/context singletons. An acyclic non-singleton DAG accepted solely because its unique row count is small would violate that rule. Reconstruction and cloning tests must enforce it before expansion.

Malformed JSON nesting is likewise an implementation failure case. Syntax depth is not JSON parser depth; decoder recursion/shape failures must emerge through the contextual artifact-error contract rather than escape as incidental exceptions. No current decoder implementation is claimed.

### Ownership and exceptional cleanup are paired

Lines 280–298 require fresh mutable state for each load and bound branch, destination-engine handles, immutable retained shape data, and cleanup or rollback of failed registration/specialization resources. The original template must remain usable.

These requirements fit the existing engine-owned template/state/workspace model and its ownership checks. Serializing source-engine handles, sharing mutable workspaces between loads or leaving a failed specialization attached to its original resource would violate the contract.

Cancellation is not authorized to bypass cleanup: the general failure-cleanup obligation applies, while line 309 forbids relabeling `BaseException` cancellation as a format error. Stale handles, engine closure and independent workspaces are explicit future tests.

### Backend and dependency failures cannot silently change the result

Lines 103–109 check the artifact capability after effective engine selection. Once native is selected, missing structural capability or payload ABI fails; Python materialization cannot substitute for it.

The existing selector’s normal `auto` discovery behavior remains explicitly distinct from an artifact-path fallback. Candidate package versions alone are insufficient: lines 421–427 require locked artifact identities and real native capability/version checks, including rejection of stale binaries. Installed checks remove editable-source and workspace-path escape routes.

### Whole-graph policy prevents mixed-resource escapes

The amendment covers authored templates, nested edge expressions, imported values, literals, defaults, conditions, matcher-result productions and operation resources. Constructor rendering/import discovery and runtime consumption share the policy.

This addresses actual closed-union and direct-`to_generator` assumptions in the inspected YIDL code. Dynamic literals retain normalized immutable syntax rather than input containers; dynamic imports construct import syntax without capturing the symbol; empty resources retain explicit suppression metadata.

The distinct YIDL literal domain and Astichi external-binding domain remain preserved. The design does not obtain parser freedom by narrowing supported complex/set literals or broadening external binding to opaque objects.

### Export/load do not execute or retain live consumer state

Export rejects externally specialized and unsupported opaque composables and forbids invoking callbacks or their `repr`. Load uses closed constructors and does not execute template bodies or import arbitrary payload-named types/modules.

The trusted-build-artifact boundary is stated accurately: an integrity digest detects corruption and does not authenticate a maliciously rewritten artifact. Ordinary generated-code execution and explicitly authored callback compiler calls remain separate boundaries; they do not authorize the engine to parse fragments internally.

### Source remains authoritative

Compiled artifacts are explicitly separate build data. Edited emitted source is compiled as edited source; provenance cannot override it. Bundled source/artifact digest mismatch fails regeneration/package verification instead of triggering runtime recompilation.

This preserves the controlling Astichi source-authority rule while permitting complete semantic state in the new artifact format. It does not turn the existing AST/provenance trailer into a hidden composable-state serializer.

### Scope and acceptance remain bounded

The proposed APIs and emitter defaults are stated. Ownership is assigned to Astichi/YIDL, without consumer serialization, final-value caching or feature-specific AST repair. New semantic concepts use behavior-bearing objects rather than unauthorized enums.

Modified Rust code must follow braced control flow and enclosing conditional boundaries, with syntax-aware checks inspecting disabled branches. The amendment does not claim an existing-code migration.

The nine producer/consumer minor pairs, cross-backend cases, installed wheel/sdist checks and native parser-entry tripwires remain mandatory evidence. No release authorization or advance performance claim is introduced.

## 3. Risks and next action

The largest residual risk is implementation completeness: the native codec must preserve every supported syntax field, semantic payload, locator and location mapping, and specialization must avoid all source-registration paths. Negative cases should include non-singleton shared references, deeply nested malformed JSON, inconsistent marker/package rows, cancellation during resource acquisition and stale native capabilities.

Those risks are already covered by the design’s invariants and prerequisite gates; this review does not claim they have been discharged.

The next action is for the lane owner to merge the two independent verdicts. If both accept this revision, record design acceptance and the prerequisite implementation sequence, then implement and verify the owning-layer facility before resuming Dataclass Stage A.
