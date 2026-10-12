# NativeLoweringAddendum — CONSISTENCY-AXIS REVIEW

**Review object:** `yidl-dataclass/dev-docs/NativeLoweringAddendum.md` and `yidl-dataclass/docs/validation/prerequisites/p2-paused-manifest.json` at `1f1bc534b460753e8cd91230e5349ea802c90b5c`. Proposed documentation only; implementation remains paused.

**Baseline:**

| Repository | HEAD |
| --- | --- |
| yidl-dataclass | `1f1bc534b460753e8cd91230e5349ea802c90b5c` |
| astichi | `4a62b093498dae7b6d346306eae23e5925aaa004` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Controlling documents and baseline source were read with `git show` at the named revisions. Hash-verified working-tree prototype files were inspected separately as supporting evidence.

**Date:** 2026-10-12

**Axis:** Consistency against the controlling document graph, internal requirements, actual owning APIs, phase order, public workflow and satisfiability of the evidence gates. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — zero P0, P1, P2 or P3 findings. This accepts the architectural documentation only. It does not accept the frozen P2 prototype, claim native parity, or establish P2 completion.

---

## 0. Evidence base

The following inspection was performed without builds, tests, regeneration, file writes or Git mutations.

### Authority and controlling documents

- Root `AGENTS.md` and `AGENTS_GWZ.md`, including repository ownership, canonical workspace naming, read-only inspection and coverage rules.
- Applicable `astichi/AGENTS.md` and `yidl/AGENTS.md`.
- The complete generated `yidl-dataclass/dev-docs/NativeLoweringAddendum-PromptConsistency.md`.
- The review-loop `SKILL.md`.
- `yidl-dataclass/dev-docs/CurrentProgramCheckpoint.md`.
- The complete addendum, lines 1–399, and its committed supporting manifest.
- Accepted `PrecompiledResourcesDesign.md` at `356321965b9a527aeee66585235f6883c0312dd4`, particularly:
  - public interfaces and effective backend selection, lines 53–109;
  - complete v1 state, stable references and limits, lines 111–189;
  - native registration, specialization and parser-free policy, lines 191–281;
  - ownership and errors, lines 283–309;
  - recursive YIDL resources and dynamic generation, lines 311–398;
  - dependency truth and superseded assumptions, lines 400–458;
  - owning seams and prerequisite checks, lines 460 onward.
- Current `PrecompiledResourcesImplementation.md`, lines 1–44.
- `DataclassDesign.md`, including the retained public/storage contracts and Section 9 specialization contract, lines 694–768.
- `DataclassPlan.md`, including evidence rules, canonical coverage ownership and prerequisite placement.
- Exact acceptance boundaries in `PrecompiledResourcesDesign-ReviewResult.md`, `DataclassDesign-ReviewResult.md` and `DataclassPlan-ReviewResult.md`.
- Active `astichi/dev-docs/AstichiSingleSourceSummary.md`, particularly the current snapshot, non-negotiable rules, Builder/materialization surfaces, migrated lower subset and hygiene contract.
- Active `AstichiCodingRules.md`, `yidl/dev-docs/YidlDesignSummary.md` and `YidlCodingRules.md`.
- Public `astichi/docs/reference/compiled-templates.md`, lines 1–59, for the existing artifact workflow, backend selection, ownership and failure expectations.

### Owning source

Committed Astichi source was inspected at the baseline, including:

- `src/astichi/builder/handles.py::BuilderHandle.build`, lines 1344–1354.
- `src/astichi/materialize/api.py`:
  - `_resolve_build_graph`, lines 998–1071;
  - `build_merge`, especially lines 1074–1240 and 1491–1548;
  - root shell construction, lines 1883–1938;
  - expression shell construction, lines 2376–2404;
  - parameter realization and signature-validation helpers;
  - default normalization, lines 3243–3320;
  - the complete materialization sequence, lines 3323–3642;
  - gate, retained-shell, boundary and cleanup helpers;
  - identifier-field resolution, lines 5046–5117;
  - boundary import/pass resolution, lines 5120–5245.
- `src/astichi/model/basic.py`, especially emission and executable/materialization routing, lines 162–230, and native-specialization entry points.
- `src/astichi/assembler/scope.py`, especially build selection, lines 1007–1043, and native materialization/fallback behavior, lines 1707–1783.
- `src/astichi/hygiene/api.py`, especially scope/trust construction, collision naming and the lexical visitor, lines 296–478 and 880–1180.
- `src/astichi/lowering/unroll.py`, including expansion, validation, substitution, shadowing and indexed suffix construction.
- `src/astichi/lowering/unroll_domain.py`, lines 20–147.
- `src/astichi/lowering/external_ref.py`, including direct chain construction, restricted path evaluation and sentinel contexts.
- `src/astichi/lowering/payload_prefix.py` and `parameters.py`.
- Native `materialize_ir.rs`, including recursive occurrence composition and operation dispatch; `parser_ir.rs` projection surfaces; and `template_extract.rs` marker, payload, parameter, fallback, ref and unroll recognition.

These inspections establish the current seams and limitations; they do not constitute execution proof.

### Frozen supporting evidence and integrity

Before inspecting the prototype, an in-memory Python check verified byte lengths and SHA-256 values for all manifest entries:

- 25 code/test files;
- 26 evidence files;
- three ignored prototype build products.

No mismatches occurred. The same complete verification was repeated at review end, again with no mismatches.

The addendum SHA-256 is:

`0aff58c92dd6da67f6011c12ed33e29ece719260e4e15fa3fc52d4e23bf7f639`

It matches the committed manifest’s `related_design.sha256`.

Hash-verified prototype inspection included `src/astichi/artifacts/policy.py`, `native_bridge.py`, `tests/artifact_golden_runner.py`, the append-only `increments.jsonl`, and retained JUnit evidence. In-memory XML inspection independently confirmed:

| Attempt | Tests | Failed | Passed |
| --- | ---: | ---: | ---: |
| `p2-native-core-green` | 13 | 0 | 13 |
| `p2-canonical-backend-red` | 172 | 120 | 52 |
| `p2-canonical-boundary-classification` | 172 | 78 | 94 |

The latest terminal diagnostics match the addendum’s partition: seven oracle tripwires, 45 native finalization failures, 11 parameter failures, four descendant ambiguities, two dynamic pyimport failures, two missing `Holder` names, two hygiene output differences and five package/module correspondence failures.

All six repository HEADs matched the exact tuple at both start and end. No current peer report or drafter message was read or requested.

## 2. Invariant analysis

### The discovered gap is architectural and accurately scoped

The source confirms the addendum’s distinction.

`BuilderHandle.build()` delegates to `build_merge`. That path creates retained insertion shells and synthetic root scope boundaries; its result is not an already-finalized operation stream. `BasicComposable.materialize()` delegates to the Python materializer at the accepted P1 baseline.

AssemblyScope has a separate lower/native route. Its existing native call produces a projected module, checks an incomplete supported subset and can return to a fallback path. The active summary explicitly describes incomplete parameter, dynamic import, boundary and broader hygiene coverage.

The root cause addressed by this proposal is therefore an **architectural design gap**: complete native restoration does not supply complete interpretation of the retained composition language. It is not merely a decoder defect or a parser-counter defect.

The addendum closes that gap by requiring retained-module lowering and common finalization semantics. It expressly preserves the separate codec/metadata defects in the failure partition. I found no claim that the new route alone resolves all 71 native issues.

### The required route does not depend on recovering a lost graph

The retained language contains the information the ordinary materializer actually consumes: target anchors, contribution shells, payload syntax, ordering/ref metadata, scope keeps, explicit boundary binding state, identifier bindings and source locations.

The materialization pipeline operates on that state rather than replaying the original BuilderGraph. Consequently, the proposed module route does not require a new durable recipe.

The optional direct graph optimization cannot substitute for this route. Lines 66–74 explicitly retain staged/loaded coverage as mandatory. The separate native shell-construction requirement also preserves the unresolved staged representation instead of forcing every build to finalize immediately.

The extra-Root attack fails against the revised text: lines 104–112 and 206–211 require direct retained-module consumption and prohibit adding a logical Root solely to invoke finalization.

### Expansion precedes indexed target resolution

The actual baseline order is:

1. Determine live instances and edges with `_resolve_build_graph`.
2. Derive `do_unroll` from the public request and live indexed edges.
3. Clone and expand instance trees.
4. Refresh ports and shell indexes.
5. Apply explicit wiring and resolve/validate indexed targets.
6. Construct retained contributions and output roots.

The addendum preserves this ordering while moving expansion into Rust. It explicitly prohibits using transforming `build_merge` or Python `unroll_tree` for strict native generation.

The `True`, `False` and `auto` behavior agrees with the baseline. Reachability remains based on live roots and their sources. Fresh projections after expansion supply the target facts needed by the generic planner.

Across staging/export/load, consumed loops are structurally absent. Within one build, transient phase completion prevents replay. These two mechanisms are compatible and require no additional v1 field. Still-present loops and new contributions remain subject to the current build request.

### The proposed phase sequence agrees with the source pipeline

The important observable order is preserved:

- select default/fallback branches before the gate;
- reject unresolved mandatory state and unmatched supplies;
- resolve identifier and boundary bindings;
- realize parameter contributions and remove optional annotation holes;
- reject unresolved boundary demands;
- lower refs;
- recognize managed imports and their synthetic bindings;
- assign lexical scope/role/trust facts and rename collisions;
- capture payload-local directives;
- realize expressions, flatten blocks, realize elif chains and insert imports;
- capture pre-strip ports;
- strip directives and suffixes, repair suites and derive final metadata.

The addendum does not move hygiene after flattening, make a fallback mandatory, let signature collisions become hygiene repairs, or discard payload-local directives before their port effects are captured.

The required parameter behavior preserves existing group/default rules. “Preserve positional-only” concerns the owning target signature; it does not override the existing validator’s rejection of positional-only parameter payloads.

### Pure planning has a concrete native execution boundary

The plan/view interface is sufficiently specified for this architectural gate.

Plans contain immutable facts and references, rather than Python AST nodes or replacement modules. Rust owns copies, field changes, synthesized nodes and structural splices. The explicit forbidden-call list excludes the old mutating helpers and materializers.

Stable keys combine input identities with copy lineage; moved nodes retain identities and synthesized nodes receive deterministic phase/parent/ordinal identities. Operator/context metadata is addressed through parent-field occurrences. This avoids conflating shared singleton values with independent lexical scopes.

Generation and owner/epoch checks reject stale or foreign plans. Expected kinds and old values prevent accidental positional reassociation. Structural edits rebuild the native index before the next view. Projection fingerprinting detects planner mutation, and the view is never imported back as transformed native input.

The private prepare/view/apply/finish lifecycle has success publication and failure/cancellation rollback requirements. No public workspace-management setting or caller lifecycle obligation is introduced.

### Lexical and directive obligations are retained

The proposal requires the same owning lexical decisions, including:

- preserved versus trusted names;
- scope-local keep metadata;
- explicit imports/passes and identity wiring;
- synthetic import bindings;
- hygiene-relevant identifier targets without keyword-label over-pinning;
- deterministic collision groups, ordinals and emitted spellings;
- nested ownership, shadowing and closure behavior.

The existing permissive source semantics are retained. The addendum does not invent an additional unresolved-free-name gate or silently capture an outer binding.

Ref contexts, transparent sentinels, parameter/default payloads, expression/funcargs shapes, managed import order, comments and executable suite repair all have explicit obligations. The broader lexical cases remain implementation parity obligations rather than claims that the frozen prototype already supports them.

### Compatibility and public workflow remain coherent

The public artifact workflow remains compile/export/load/specialize/build/materialize, with existing backend selection. The addendum adds no user option, wire field or new artifact constructor.

Its strict capability guard strengthens the accepted amendment’s fail-closed policy: both artifact and lowering capabilities, ABI 1 and codec 1 are required after effective selection. A restoration-only binary cannot qualify merely through its version or provisional artifact flag.

Ordinary source behavior and Python artifact mode remain supported. The extra lowering flag is internal dependency truth, and the text names the resulting backend error and rebuild action. It does not hide a new user configuration requirement.

The narrow native representation exceptions are stated explicitly. They do not widen the external-binding domain or prohibit ordinary YIDL set/complex expressions.

### Supersession and acceptance boundaries are consistent

The superseded assumption is confined to compiler amendment Section 4 and the P2 completion row: restoration plus the four structural specialization changes is insufficient.

Those requirements remain necessary. The addendum supplements them with full lowering rather than withdrawing registration, portability, ownership or parser-free requirements.

Dataclass model APIs, generated direct access, frozen/field-local behavior, comparison semantics, source authority and performance thresholds remain intact. Historical design/plan GO results remain scoped documentation gates, and P1 remains an accepted Python checkpoint.

### Evidence gates are satisfiable and honest

The evidence counts and failure partition agree with the retained JUnit records.

The seven remaining tripwire failures are not relabeled as native success. Their intended correction is an explicit oracle boundary with counter assertions and restored generation protection. The remaining 71 failures must satisfy the original canonical expectations.

Parser counts alone are expressly insufficient: the new gates also require native operation counts and forbidden-Python-transformation checks. Expansion ordering and duplicate-expansion regressions are named.

Malformed plans, oversized expansion, stale ownership, cancellation, rollback, independent reuse and exact metadata/scalar preservation have focused gates. Successful end-to-end assertions stay in the established corpus. No skip, fallback or golden weakening is authorized as closure.

## 3. Risks and next action

Full native lowering remains substantial unimplemented work. Shared pure analysis must be extracted without changing Python outputs or diagnostics, and both entry routes must retain scope semantics until hygiene is complete. Projection, planning and cloning costs may be material; this review establishes no performance result.

The frozen prototype remains incomplete supporting evidence. Its provisional capability advertisement must not be treated as releasable support, and all unresolved canonical failures remain future acceptance work.

**Next action:** the lane owner should combine the two independent documentation verdicts. If both are GO on this tuple, record documentation acceptance and begin the specified owning-layer TDD increments; keep product work behind the P1–P4 prerequisite gates.
