# PrecompiledResourcesDesign.md — CONSISTENCY-AXIS REVIEW

**Review object:** `yidl-dataclass/dev-docs/PrecompiledResourcesDesign.md` at `356321965b9a527aeee66585235f6883c0312dd4`; proposed compiler-artifact amendment, documentation only.

**Baseline:**

| Repository | HEAD |
| --- | --- |
| yidl-dataclass | `356321965b9a527aeee66585235f6883c0312dd4` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| astichi | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Sources were inspected using `cat`, `sed`, `nl`, and repository-local `rg`; the object and accepted design/plan compiler clauses were also checked using `git show` at their named revisions. All six heads matched at the beginning and end.

**Date:** 2026-10-12

**Axis:** Consistency against the controlling graph, including public Surface, structural feasibility, generated-value coverage, compatibility, and evidence gates. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — no P0, P1, P2, or P3 findings. This accepts the proposed prerequisite design, not implementation, runtime proof, performance, or release readiness.

---

## 0. Evidence base

Reviewed the amendment’s Sections 1–10. Public signatures in Section 2 and emission/dependency options in Sections 6–7 were read before detailed implementation inspection.

Controlling context inspected:

- Workspace `AGENTS.md` and `AGENTS_GWZ.md`.
- Review-loop skill, particularly settled-object, peer-blindness, Surface, severity, and redesign rules.
- Dataclass `dev-docs/CurrentProgramCheckpoint.md`, `DataclassDesign-ReviewResult.md`, and `DataclassPlan-ReviewResult.md`.
- Accepted `DataclassDesign.md`, particularly Sections 7–10, including generation stages and specialization requirements.
- Accepted `DataclassPlan.md`, particularly ownership, Stage A, Stage G parser/installation gates, and measurement requirements.
- Astichi `AGENTS.md`, active `dev-docs/AstichiSingleSourceSummary.md` Sections 2–9, and `AstichiCodingRules.md`.
- YIDL `AGENTS.md`, active `dev-docs/YidlDesignSummary.md` Sections 26–27 and consolidated generation rules, and `YidlCodingRules.md`.

Actual implementation seams inspected:

- Astichi `src/astichi/frontend/api.py:57–249` and `frontend/compiled.py`.
- Astichi `src/astichi/model/basic.py:41–210`, native specialization around `619–690`, and specialized reconstruction around `845–905`.
- Astichi `src/astichi/lower_engine/facade.py:107–152`, `492–550`, and `1547–1625`; effective native discovery/selection in `lower_engine/native.py`.
- Astichi `src/astichi/model/inventory.py`, including AST-backed owner/resource names and expression/funcargs payloads; `lower_engine/package_v2.py` row families and `package_extract.py` node-reference use.
- Astichi hygiene classification and structural occurrence definitions in `src/astichi/hygiene/api.py`; the existing parse/unparse clone at `274–287`.
- Astichi external-value validation/conversion in `src/astichi/model/external_values.py`.
- Native `occurrence_store.rs:1662–1691`, `template_package_v2.rs:183–234`, and `materialize_ir.rs` workspace, external-expression, pass, and reference construction paths.
- Native `parser_ir.rs` AST constructors, locations/source-map conversion, type parameters, and constants; `capabilities.rs` and `Cargo.toml`.
- YIDL `src/yidl/generation/matcher_values.py:20–440`, `matcher.py:419–660`, and its public forwarding method.
- YIDL `assembly_source.py:20–135`, `container_runtime_source.py` operation resources, empty suppression, recursive constructor discovery, and value expressions; `assembly_runtime.py` production roots, contribution resolution, empty suppression, and diagnostics.
- YIDL compatibility facade `generation/data_def_sys.py`, and capsule `build_mapper.py` and `recorded_builder.py` resource recognition/emission boundaries.
- Current Astichi/YIDL package metadata and Astichi public exports.

No builds, regeneration, tests, or Python probes were run. An initial read-only GWZ inventory attempt failed because the local command had no configured version; direct permitted `git rev-parse HEAD` inspections subsequently established the complete tuple. No files or Git state were changed. Dataclass status showed only the two untracked review prompts.

## 2. Invariant analysis

### Changed boundary and architectural feasibility

The amendment correctly identifies an owning-layer prerequisite. Existing native snapshot restoration cannot supply a materializable template: `parse_template_snapshot` explicitly leaves both `package_v2` and `module` absent, while workspace creation requires native parser IR. Existing source registration supplies that IR by parsing.

Sections 3–4 require a complete syntax graph, semantic package, and direct RustPython AST construction. They do not treat metadata restoration as equivalent to module restoration. The native tree is composed of typed AST fields already traversed by the Python artifact bridge; direct construction is a concrete implementable boundary, although its implementation remains substantial.

The artifact binding, destination registration, builder-tree projection, specialization eligibility, and structural re-projection requirements address the actual source dependencies in `NativeTemplateCache`, builder copying, and `BasicComposable` specialization. The design also separately addresses external-expression parsing, dotted-reference parsing, and parsed pass placeholders.

No architectural defect was established. The architectural change is explicit and belongs to Astichi and YIDL; consumers remain behind its acceptance gates.

### Complete semantics and independent state

The proposed artifact is more than an AST snapshot. It expressly includes marker/classification state, ports, inventory, package rows, identifier bindings, keep names, defaults, clauses, scopes, imports, references, unroll metadata, comments, origins, and locations.

The node-reference requirement matches actual AST-backed inventory objects, including `CodeNodeResourceName`, owner paths, expression payloads, and funcargs payloads. Deterministic structural references and rebinding to fresh nodes avoid carrying process identities into loaded graphs. Derived scope indexes are recomputed rather than copied with stale identities.

Ownership rules require fresh loads and independently bound branches, immutable canonical shape data, destination-owned native handles, and cleanup after failed registration/specialization. These requirements cover current sharing/copy seams without claiming those seams already satisfy the new contract.

### Whole generated-value graph

Section 6 reaches beyond `ASSEMBLY_RESOURCES`: authored templates, nested template-edge expressions, imports, literals, defaults, conditions, identities, matcher productions, and operations all receive policy-aware lowering.

The distinction between YIDL’s literal domain and Astichi’s narrower external-binding domain is accurate. Complex/set literals remain structural generated expressions; they are not forced through external binding. Dynamic imports construct marker/name syntax without capturing imported objects. Nested edge expressions and assembly diagnostics move from emitted-source evaluation to validated expression AST compilation.

The runtime resolver must reject newly returned source-backed values before `to_generator`. Explicit empty metadata replaces source-string checks. Recognition, edge validation, and constructor discovery must include the new wrappers. Those obligations prevent the existing closed union from serving as a runtime parsing escape.

Historical source consumers remain supported. The amendment’s whole-graph promise applies to opted-in generation and its protected runtime interval; it does not falsely claim every older capsule/client path is already migrated.

### Surface walkthrough

The proposed first-use workflow is coherent:

1. Compile an authored template at build time, or use `compile_ast` for structural input.
2. Export the supported unmaterialized template to bytes.
3. Load those bytes under the effective engine selection.
4. Independently bind/copy/compose loaded resources and materialize executable AST.
5. Release loaded ownership with its objects; artifact bytes require no separate lifecycle API.

Export/load are distinct from source emit/provenance. `compile_ast` has explicit defaults, clones caller input, shares marker validation, and cannot serve as a validation bypass. Export’s restricted input envelope is stated despite its general `Composable` annotation.

`precompile_resources=False` supplies the default for all three named emitters. Opt-in propagation and constructor discovery are explicit. The artifact path preserves ordinary `auto` discovery, then checks the selected backend’s new capability; failure does not authorize backend substitution.

The four error classes, their inheritance, diagnostic requirements, and unsupported-state behavior provide a usable failure surface. No missing lifecycle pair or unstated option default was established.

### Authority, compatibility, and evidence gates

The amendment preserves source-authoritative provenance: edited emitted source remains source input, while artifacts are separate compiled build data. It requires active owning documents to record that distinction during implementation. It does not repurpose provenance to transport hidden composition semantics.

Its superseded Dataclass clauses accurately address the insufficient ordinary emitter and the timing of the first-decoration gate. Model APIs, field policies, native comparison composition, and write-context semantics remain retained.

The candidate dependency minima exclude the currently published featureless versions. Exact local artifact hashes and revisions supplement version constraints; startup capability/ABI checks reject stale extensions. Candidate work does not authorize publication.

Cross-minor compatibility is bounded to a common syntax subset, with meaningful newer fields rejected rather than dropped. The nine export/load pairs and cross-backend roundtrips are appropriate future obligations. Decoder limits, malformed-state rejection, and pre-registration validation are specified.

The TDD gates distinguish behavioral RED from broken environments, require independent source-mode comparison, guard private native parser entries, and test first use without warming wrappers. Installed checks remove editable/workspace leakage and retain wheel/sdist regeneration evidence. Changed-source syntax checks include disabled Rust branches and expressly avoid claiming a completed historical migration.

## 3. Risks and next action

The largest residual risk is implementation breadth: full semantic codecs, native source maps, specialization re-indexing, and strict failure propagation must all work together. Present APIs establish feasible seams, not a runtime proof.

Implementation tracing should retain the capsule mapper’s separate template-type guard and public forwarding methods in its compatibility inventory. The existing source-mode suite remains important when `from_literal` gains a new behavior-bearing wrapper. Portable-field tests should exercise the existing native type-parameter/default-field adapters as well as ordinary method syntax.

The next action is to merge the two independent verdicts. If both accept this revision, record the reviewed amendment and implementation sequence, then execute the owning-layer prerequisite checkpoints before resuming Dataclass Stage A.
