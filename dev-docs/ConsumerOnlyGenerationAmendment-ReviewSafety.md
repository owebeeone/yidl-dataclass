# Consumer-only generation amendment — SAFETY-AXIS REVIEW

**Review object:** `yidl-dataclass` documentation candidate at `382d389172f38e33de8a00af350b1b6b21d46f5b`: controlling `dev-docs/ConsumerOnlyGenerationAmendment.md` and corresponding README, DataclassDesign, DataclassPlan and ExperimentProtocol edits from `ae220ec`. Documentation-only review; no implementation or performance acceptance.

**Baseline:**

| Repository | Settled HEAD |
| --- | --- |
| yidl-dataclass | `382d389172f38e33de8a00af350b1b6b21d46f5b` |
| astichi | `4a62b093498dae7b6d346306eae23e5925aaa004` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Committed documents were read with `git show HEAD:PATH`. Original Astichi source was read exclusively with `git show 1c47f781d3804130fdd61cbee07a3b2e4529158a:PATH`; original YIDL source was read at `9d374f88445c426a56d5dd1f96fad112d1ec5417`. SDK working-tree changes and prototype binaries were excluded.

**Date:** 2026-10-12

**Axis:** Safety — degraded and mixed-version paths, recovery, capture/cache ownership, disclosure, dependency authority and scope containment. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — zero P0, P1, P2 or P3 findings. This accepts the proposed generation/dependency boundary at the documentation gate only.

---

## 0. Evidence base

All six HEADs were verified with `git -C MEMBER rev-parse HEAD` at both the start and end. Every result matched the settled tuple above.

The following authority and product documents were inspected:

- Workspace `AGENTS.md` and `AGENTS_GWZ.md`; the invoked review-loop `SKILL.md`; the complete canonical-generated Safety prompt.
- `dev-docs/ScopeCorrection.md` and `dev-docs/CurrentProgramCheckpoint.md`, including the operator boundary and retained historical prerequisite records.
- `dev-docs/ConsumerOnlyGenerationAmendment.md`, lines 1–150.
- `README.md`, lines 1–31.
- `dev-docs/DataclassDesign.md`, particularly public declarations and storage/helper contracts; Sections 5–8, lines 266–706; and generation/verification obligations, lines 708–870.
- `dev-docs/DataclassPlan.md`, including ownership/environment rules, lines 23–142; corpus allocation, lines 144–179; stages A–H, lines 181–419; benchmark gates, lines 421–487; and declarative/completion requirements, lines 489–541.
- `dev-docs/ExperimentProtocol.md`, lines 1–131; `DataclassConcept.md`; `DataclassSpec-OperatorAmendment.md`; `GoldenExamplesAmendment.md`; and `DeclarativeEvaluation.md`.
- Object diffs from `ae220ec`, plus comparisons of the current design against accepted semantic revision `de7cadd` and the current plan against `f2514e1`.

Original-API reference evidence was inspected through these owning-repository paths:

| Repository | Evidence |
| --- | --- |
| yidl | `src/yidl/concept_parser.py`, lines 217–320 and 345–420: source-map compilation, import diagnostics and concept extension |
| yidl | `src/yidl/generation/data_def_sys.py`: existing emitter export |
| yidl | `src/yidl/generation/assembly_source.py`, lines 20–99: emitted resources, assembly metadata and build entry points |
| yidl | `src/yidl/generation/container_runtime_source.py`, lines 382–416: fresh generated builder and freeze route |
| yidl | `src/yidl/generation/matcher_values.py`, lines 19–188 and constructor rendering through line 287: cached templates and resource reconstruction |
| yidl | `src/yidl/generation/assembly_runtime.py`, lines 251–285 and 670–758: fresh assembly scope and per-build bindings |
| yidl | `tests/data/yidl/dataclasses_example.yidl`: comparison contributions and repeated external binding names |
| astichi | `src/astichi/model/basic.py`, lines 43–155 and 190–285: composable ownership, executable AST and binding semantics |
| astichi | `src/astichi/model/external_values.py`, lines 10–129: supported external values |
| astichi | `src/astichi/lowering/external_ref.py`, lines 1–29, 55–78 and 135–270: validated reference lowering and transparent assignment targets |
| astichi | `src/astichi/assembler/scope.py`, lines 2512–2545: duplicate binding rejection and replacement of per-build instances |
| astichi | `src/astichi/builder/api.py`, lines 8–10, and relevant builder-handle definitions |
| astichi / yidl | Original `pyproject.toml`: versions, Python requirements and declared interpreter matrix |
| yidl-lifecycle | `src/yidl_lifecycle/regenerate_lifecycle_base.py`, lines 20–99: established emitter route and check-by-default/`--write` interface |

The committed `docs/validation/baseline/original_sdk_probe.py`, lines 1–33, and `original-sdk-results.json` were read. Their recorded results were not rerun.

Inspection used read-only `git show`, `git diff`, `git rev-parse`, `cat`, `rg`, `nl` and `sed`. No tests, builds, installs, regeneration, file writes or Git mutations were performed. No current peer report or drafter message was read.

## 2. Invariant analysis

### Original SDKs remain the bounded dependency authority

The attempted failure sequence was: preserve prototype SDK code, retain an old prerequisite clause, then accidentally validate or ship the consumer against prototype capabilities.

The amendment explicitly removes compiler P1–P4, parser-free decoration, native IR restoration and wholly Rust-owned lowering from the product gates (lines 10–17). The design, plan and protocol carry the same correction. Plan lines 84–89 require original locked wheels, verified import origins and wheel digests across all three supported minors. Historical checkpoint entries remain records beneath an explicit scope-correction status; they do not supply active authority to resume SDK work.

A concrete original-API blocker must stop the affected slice for operator scope resolution. Consumer AST repair, dynamic method-source emission, new SDK artifacts and prototype dependency overrides cannot close it.

### The proposed route uses existing composition surfaces

The original YIDL parser accepts a logical source map and resolves imports within it. Concept extension is passed into the recorded concept builder. The original emitter reconstructs resources and assembly metadata in generated Python and provides `build_<assembly>` entry points. The generated container supplies a fresh builder and frozen facts, and assembly execution creates a fresh Astichi scope.

Original Astichi reference lowering supports the stated Name/Attribute specialization and transparent Store/Del target forms. The amendment therefore does not require an unsupported whole-template restoration API to obtain direct accesses.

This is source-inspection support for the route, not proof that every future Dataclass resource will compose successfully.

### Runtime captures do not cross the SDK serialization boundary

The attempted failure sequence was: bind a factory or default object directly into the SDK, trigger unsupported serialization or executable repr, then hide that failure behind generated-source repair.

Original Astichi external-value validation supports a bounded literal family and rejects other objects. Amendment lines 57–67 instead put arbitrary callback/default objects in a fresh consumer namespace or authored builder closure. SDK bindings receive validated identifier/path strings. The Undoable ContextVar and historical equality method use that same capture route.

Design lines 790–805 preserve deterministic structure and source inspection without exposing capture repr. Plan Stage C and Stage G explicitly require hostile-repr and generation-side-effect checks. The text does not authorize callback execution or arbitrary object serialization during generation.

### Template reuse is separated from class-specific state

The attempted interleaving was: decorate class A, populate template bindings with A’s names and captures, decorate class B through the warm cache, then make A call B’s callback or access B’s field.

`MatcherGeneratedValue.to_generator()` caches the compiled template. Original assembly execution creates fresh scopes; pending bindings belong to those scopes and replace their registered instances. `BasicComposable.bind()` returns a new composable and clones the Python tree on its ordinary path.

The amendment requires fresh builds and captures and prohibits final-class/value caching or reuse of class-specific bindings. Design lines 786–798 and Plan lines 368–376 retain explicit first/second-decoration isolation checks, including both differing captures and differing shapes. Mutable/native template internals still require those future tests, but no permitted consumer path silently shares class captures.

### Comparison reuse has an authoritative source and a reproducible bootstrap

The attempted degraded paths were missing Dataclass authority, a stale candidate wheel, a sibling-checkout fallback, and an Undoable runtime installation without Dataclass.

Amendment lines 79–103 establish one packaged Dataclass authority, a pinned build-only wheel for Undoable regeneration, resource SHA256 and local-source provenance, and failure before generation on missing/mismatched authority. A changed authority requires regeneration and checks of both bases.

The original emitter embeds resource constructors and assembly metadata, supporting an Undoable generated base that executes with existing SDK dependencies. Ordinary builds use the checked-in base; explicit sdist regeneration requires the pinned authority and must reproduce the base/digests. Runtime execution with Dataclass absent remains an explicit Stage G gate. A handwritten comparison duplicate or unversioned fallback is forbidden.

The bootstrap is acyclic: the initial Dataclass distribution does not depend on Undoable, and Undoable consumes the Dataclass wheel only for regeneration.

### Semantic and recovery contracts remain intact

The baseline-to-current diffs change resource ownership, generation and dependency assumptions without replacing the accepted field, factory, lazy, frozen, helper or comparison policies.

The complete historical-write scope contract remains: original operands, native `bool(old == value)`, existing ownership fence, fresh markers, close-before-reset cleanup, and recovery on exceptions and BaseException. Captured contexts cannot reactivate closed markers. No manager/node state enters the marker or history. Hash/order restrictions and the dictionary, tuple, proxy, opaque-callback and context matrix remain required.

The known ordering collision is not presented as successful ordering evidence. Distinct consumer binding/port names and independent ordering composition are required at Stage B.

### Evidence and delivery gates are not weakened

The committed probe proves only its focused installed 3.12 feasibility cases. The amendment expressly excludes full parity, ordering, extensions, three-minor and performance conclusions.

Canonical contrasts, declaration deletion, independent differential coverage, wheel/sdist checks, five-process measurements, fixed numerical thresholds, grounded declarative evaluation and final Code/State reviews remain in the plan. No release/publication or consumer-durable-storage change is authorized.

## 3. Risks and next action

Full resource composition, cache isolation across both backend selections, three-minor installation, packaging reproducibility and performance remain future A–H obligations. The focused probe cannot establish those outcomes. Unsupported original-SDK behavior may still block a product slice; the documents require reporting it rather than widening SDK scope.

No architectural defect was established in this amendment. The next action is for the lane owner to merge the two independent verdicts. If the documentation gate is accepted, product work may resume at Stage A under the original-SDK boundary and recorded stage checkpoints.
