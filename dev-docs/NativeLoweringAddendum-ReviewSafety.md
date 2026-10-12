# NativeLoweringAddendum.md — SAFETY-AXIS REVIEW

**Review object:** Proposed, documentation-only `yidl-dataclass/dev-docs/NativeLoweringAddendum.md` and supporting `yidl-dataclass/docs/validation/prerequisites/p2-paused-manifest.json` at `1f1bc534b460753e8cd91230e5349ea802c90b5c`, reviewed on 2026-10-12.

**Baseline:**

| Repository | HEAD |
| --- | --- |
| yidl-dataclass | `1f1bc534b460753e8cd91230e5349ea802c90b5c` |
| astichi | `4a62b093498dae7b6d346306eae23e5925aaa004` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Committed sources were read primarily through `git show HEAD:PATH`, with accepted design revisions selected explicitly. Hash-verified working-tree P2 files supplied inspection evidence only.

**Date:** 2026-10-12  
**Axis:** Safety — degraded paths, false composition, stale ownership, expansion limits, cancellation, cleanup, disclosure and scope expansion. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — zero P0, P1, P2 or P3 findings. This accepts the proposed documentation boundary only. It does not accept the paused P2 prototype, native functionality, runtime parity, installation results or performance.

---

## 0. Evidence base

### Authority and controlling documents

Read the canonical Safety prompt fully, root `AGENTS.md` and `AGENTS_GWZ.md`, applicable member instructions, the review-loop `SKILL.md`, and `yidl-dataclass/dev-docs/CurrentProgramCheckpoint.md`.

Inspected:

- `yidl-dataclass/dev-docs/NativeLoweringAddendum.md`, lines 1–399, in full.
- Its committed supporting paused manifest.
- Accepted `PrecompiledResourcesDesign.md` at `356321965b9a527aeee66585235f6883c0312dd4`, particularly public interfaces, artifact state, structural registration, ownership, recursive resource policy and dependency truth.
- Current `PrecompiledResourcesImplementation.md`.
- Accepted Dataclass design and plan requirements governing generated storage, comparison composition, native generation and final acceptance, together with their exact `ReviewResult` boundaries.
- Astichi’s active summary and coding rules; YIDL’s active design summary and coding rules, particularly AST ownership, explicit wiring, generated-value resources and parser boundaries.

No current peer report or drafter communication was consulted.

### Source trace

The principal committed Astichi evidence was:

- `src/astichi/builder/handles.py`, lines 1344–1354: plain Builder dispatch.
- `src/astichi/materialize/api.py`:
  - lines 998–1209: live graph selection, cloning, pre-expansion, binding preparation and indexed-target validation;
  - lines 1480–1548 and 1718–1940: retained contributions, root shells and merged metadata;
  - lines 2461–2543 and 3243–3302: parameter realization and fallback selection;
  - lines 3324–3643: gate, identifier/boundary resolution, external refs, lexical hygiene, realization, managed imports, cleanup and result metadata;
  - lines 3645–3693: executable/commented output paths;
  - lines 5353–5385: ordered block splices.
- `src/astichi/model/basic.py`: materialization, executable AST access, copy, bind, identifier and keep routes.
- `src/astichi/assembler/scope.py`, especially lines 1007–1046 and 1707–1837: operation-stream routing, existing native finalization and fallback behavior.
- `src/astichi/path_resolution.py`, lines 311–376 and 442–553: synthetic-root transparency, shell indexing, descendant references and ambiguity rejection.
- `src/astichi/hygiene/api.py`, lines 145–186, 296–474 and selected scope visitor sections: occurrence carriers, trust/preservation distinction, collision domains, ordering and mutation boundary.
- `src/astichi/lowering/unroll.py`, lines 47–112 and 346–434, plus domain validation: expansion order, substitutions, scope/shadowing rules and index refinement.
- External-ref, call-argument payload, payload-prefix and managed-import helpers.
- Artifact schema, policy, validation and API entry points.

The frozen prototype inspection included relevant portions of `native_engine/src/materialize_ir.rs`, `parser_ir.rs`, `template_extract.rs`, `artifact_codec.rs`, `artifact_decode.rs`, `handles.rs`, `capabilities.rs`, and `src/astichi/artifacts/native_bridge.py`. These establish available primitives and remaining gaps; they are not accepted implementation.

### Verification performed

All six HEADs matched the mandated tuple at start and end.

Before prototype inspection and again at review end, in-memory Python checked every listed byte count and SHA256 in the supporting manifest:

- 25 code/test files: no mismatches.
- 26 evidence files: no mismatches.

The committed design digest matched the manifest:

`0aff58c92dd6da67f6011c12ed33e29ece719260e4e15fa3fc52d4e23bf7f639`

The supporting manifest digest was:

`2ae8318e5ab85dac81b6d2c3a6c167f88cadf0793dd42d4167d452f440ebcf17`

In-memory XML inspection confirmed 13 core test cases with no failures and 172 canonical test cases with 78 failures. Terminal diagnostics independently reproduced the documented partition: seven oracle failures, 45 finalization failures, 11 parameter failures, four Root ambiguities, two pyimport failures, two Holder failures, two hygiene/output differences and five correspondence failures.

No builds, tests, regeneration, file writes or Git mutations were performed.

## 2. Invariant analysis

### Phase and call-graph feasibility

The existing Builder path performs Python unroll before indexed-target resolution, then constructs marker-bearing shells. The ordinary materializer consumes those shells without needing the original graph. Its ordering supports the proposed retained-module route: fallback selection and completeness checks precede hygiene; identifier and parameter realization precede lexical analysis; expression/block/elif realization follows hygiene; residual cleanup follows realization.

The proposed native pre-expansion seam preserves this dependency. An indexed hole must be validated against a fresh projection of the expanded native workspace, not the original compact template. Sections 2 and 4 explicitly require that sequence and prohibit using the existing transforming `build_merge` path to manufacture native input.

I attacked staged reuse by considering an already-expanded template exported or copied, then inserted in a later build. The addendum consumes the current structure and does not replay an earlier expansion request. Removed loop markers and transient within-build phase completion prevent duplicate bodies and repeated index suffixes. Still-present markers remain subject to the current stage’s existing unroll decision.

The direct complete graph route is safely optional because retained-shell lowering is mandatory. Its omission cannot excuse loaded or staged values. The syntax retains payloads, target names, order, refs and explicit boundary declarations; saved semantic state retains identifier bindings, keeps and package references. I found no required replay-only information missing from that envelope.

### Architectural classification

The discovered defect is an **architectural design gap in the earlier prerequisite sufficiency assumption**: restoring a module/package and implementing several specialization primitives does not equate Builder shells with AssemblyScope operation streams. The addendum changes that boundary explicitly and supplies a required structural finalizer.

The existing native operation-stream path eagerly lowers markers and performs narrower naming work. It cannot be retained unchanged and then followed by full hygiene after scope information has been discarded. The addendum’s requirement to resolve scope trust and naming before flattening, and to use the same coordinator for both routes, excludes that implementation.

The saved-package correspondence failures remain codec/metadata integration defects. The text does not claim that the structural finalizer fixes them or permit weaker correspondence validation. No additional architectural root cause was established against the proposed revision.

### Pure planning and genuine native execution

A fresh projected AST is sufficient for recognition and lexical analysis, while its separate address map identifies native nodes. Existing hygiene analysis already distinguishes occurrence gathering from the mutating collision renamer; extraction into a pure planner is feasible.

The text excludes the tempting escape paths: old Python materialization, Python unroll, Python AST transformation, transformed-module import, source re-registration and emitted-source parsing. Rust owns shell creation and every code-changing phase. Operation counters and forbidden-transformation guards supplement parser counters, so a zero parser count alone cannot certify native execution.

This also covers the existing commented renderer, which reparses emitted text to obtain comment spans. That helper cannot be reused unchanged in the strict profile: Sections 5 and 7 expressly prohibit the parse and require commented-emission coverage.

### Identity, stale plans and copy isolation

I considered a plan made before a splice, a plan targeting one of several copies, and a plan passed to another engine. The specified checks reject all three unsafe substitutions:

- owner/epoch and workspace generation;
- stable node/scope identities and deterministic copy lineage;
- expected kinds, fields and exact old values;
- index rebuilding after structural edits and generation advancement after application.

Locations are separate from identity, and singleton context/operator metadata is addressed through owning field occurrences. This avoids confusing copied lexical nodes with shared unit objects. Projected-tree mutation is detected and the projection is never imported back.

### Gates, hygiene and realization

A missing required parameter cannot disappear during cleanup: completeness is gated before hygiene, then payloads are incorporated into the owning signature. Optional annotation holes retain their separate removal behavior.

Discarded fallback branches remain inactive. Payload-local directives are captured before wrappers disappear. Block/root boundaries survive until naming and explicit wiring are resolved. The prohibition on adding another logical Root addresses the observed descendant ambiguities.

The hygiene requirements preserve trusted keeps separately from preserved-but-untrusted targets, lexical role/domain/ordinal decisions, synthetic import bindings and canonical suffix numbering. Keyword labels do not blanket-pin unrelated bindings. Nested ownership, closures, global/nonlocal declarations and comprehension behavior remain required rather than being reduced to pyimport collision handling.

Managed imports remain structural compiler data and do not import user modules during planning. External refs preserve contexts and base-expression evaluation; YIDL set/complex literals are not forced through the narrower external-binding domain.

### Limits, failure and recovery

Compact input limits alone do not bound unroll or repeated contributions. The addendum therefore requires expanded-node/action limits, predictable-overflow rejection before cloning, and enforcement during copies. Existing eager domain expansion is not an acceptable way to evade those limits.

Closed input and plan preflight excludes custom objects, cycles and malformed references before transformation. Unknown actions fail before traversal. Semantic failures remain semantic failures; corruption and missing backend functionality have contextual error classes. Cancellation propagates unchanged.

Publication occurs only after all phases and postconditions pass. Failure and cancellation release or roll back newly owned state while preserving the original for another bind/build. Repeated independent use cannot rely on mutable shape-cache state or retained caller containers.

### Mixed versions, disclosure and scope

A restoration-only or stale binary cannot satisfy the new strict guard merely by advertising artifact support or matching package versions. Both capability flags, ABI 1 and codec 1 are required after effective backend selection. Python artifact mode and normal source selection retain their supported paths.

No new durable field, graph recipe, process handle, runtime value or callback enters artifact v1. Existing logical-origin restrictions remain controlling. The proposal does not widen artifact authority into a sandbox claim or change Dataclass/Undoable model semantics.

### Evidence integrity

The 13 core passes are explicitly scoped. The seven oracle failures require an explicit oracle boundary; they do not authorize weakening generation protection. The other 71 failures remain genuine unresolved obligations.

The required gates preserve canonical outputs and validators, prohibit new skips/fallback/golden weakening, and require first/second use, backend/minor matrices, ownership/cancellation failures and isolated installed probes. None of the inspected evidence is relabeled as completed P2 acceptance.

## 3. Risks and next action

The substantial remaining risk is implementation parity across interacting phases, particularly operation-stream scope retention, pure helper extraction, comment rendering without reparsing, bounded domain expansion and metadata preservation through native copies. These are explicit implementation and exit-gate obligations, not contradictions permitting an unsafe shortcut.

The next action is for the lane owner to merge this verdict with the independent Consistency verdict. If both accept this exact revision, resume bounded P2 TDD increments under the addendum. Native capability publication and product Stage A remain gated on the complete prerequisite evidence.
