# ConsumerOnlyGenerationAmendment — CONSISTENCY-AXIS REVIEW

**Review object:** Documentation candidate at yidl-dataclass `382d389172f38e33de8a00af350b1b6b21d46f5b`: `dev-docs/ConsumerOnlyGenerationAmendment.md` and corresponding README, DataclassDesign, DataclassPlan and ExperimentProtocol edits from `ae220ec`. No implementation or performance acceptance.

**Baseline:**

| Repository | Frozen HEAD |
| --- | --- |
| yidl-dataclass | `382d389172f38e33de8a00af350b1b6b21d46f5b` |
| astichi | `4a62b093498dae7b6d346306eae23e5925aaa004` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Committed documents and reference source were read with `git show`. Astichi source was read exclusively at original revision `1c47f781d3804130fdd61cbee07a3b2e4529158a`; its current prototype source and binaries were excluded. Original YIDL source was read at the frozen YIDL revision.

**Date:** 2026-10-12  
**Axis:** Consistency against the controlling requirements, accepted semantic design and plan, operator scope correction, original SDK APIs, and documented Surface. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — zero P0, P1, P2 or P3 findings. This accepts the documentation boundary correction only.

---

## 0. Evidence base

All six HEADs were verified with `git -C MEMBER rev-parse HEAD` at review start and end. Every value matched the frozen tuple on both checks.

The Surface read began with yidl-dataclass `README.md`, cold, before reading design, plan or implementation references.

Inspection covered:

- Workspace `AGENTS.md`/operator-supplied instructions and `AGENTS_GWZ.md`; review-loop `SKILL.md`.
- yidl-dataclass:
  - `README.md`, lines 1–31.
  - `dev-docs/ConsumerOnlyGenerationAmendment.md`, lines 1–150.
  - `dev-docs/ScopeCorrection.md`, lines 1–46.
  - `dev-docs/CurrentProgramCheckpoint.md`, including the current scope statement and historical review/checkpoint sequence.
  - `dev-docs/DataclassConcept.md`, all requirement sections.
  - `dev-docs/DataclassSpec-OperatorAmendment.md` and `GoldenExamplesAmendment.md`.
  - `dev-docs/DataclassDesign.md`, Sections 1–10 and reference inspection, particularly comparison ownership at lines 438–510, unchanged Undoable semantics at lines 512–706, and generation/verification at lines 708 onward.
  - `dev-docs/DataclassPlan.md`, lines 1–541, including A–H, original-SDK environments, canonical coverage, installed gates, benchmark thresholds and declarative evaluation.
  - `dev-docs/ExperimentProtocol.md`, lines 1–131; `DeclarativeEvaluation.md`.
  - `dev-docs/DataclassDesign-ReviewResult.md` and `DataclassSpec-ReviewResult.md` for acceptance boundaries.
  - Committed `docs/validation/baseline/original_sdk_probe.py` and `original-sdk-results.json`.
- Original YIDL:
  - `src/yidl/concept_parser.py`: compiled-concept structure, `compile_yidl_files`, import resolution and inherited contribution-matcher composition.
  - `src/yidl/generation/data_def_sys.py`: emitter facade.
  - `src/yidl/generation/assembly_source.py`: embedded resources and generated `build_<assembly>` functions.
  - `src/yidl/generation/container_runtime_source.py`: generated builder and frozen container.
  - `src/yidl/generation/matcher_values.py`: cached template compilation and resource reconstruction.
  - `src/yidl/generation/assembly_runtime.py`: independent assembly builds and binding requests.
  - `tests/data/yidl/dataclasses_example.yidl`: comparison contributions and repeated ordering binding names.
  - Split dataclass example imports, inheritance and matcher extensions.
- Original Astichi:
  - `src/astichi/lowering/external_ref.py`, including direct attribute chains and Store/Del context propagation.
  - `src/astichi/lowering/sentinel_attrs.py`.
  - `src/astichi/model/basic.py`, including immutable binding and executable-AST materialization.
  - `src/astichi/model/external_values.py`, including supported literal values and rejection of unsupported objects.
- Lifecycle and Undoable committed regenerators and packaging script declarations, used to compare command naming and default-check/explicit-write shape.

Diffs inspected were:

- `ae220ec..382d389` for the corresponding README, design, plan and protocol edits.
- `de7cadd..382d389` for the accepted semantic design.
- `f2514e1..382d389` for the accepted plan.

Only read-only inspection commands were used. No tests, builds, installations, regeneration, edits or Git mutations were performed. No current-round peer report was read or requested.

## 2. Invariant analysis

### 2.1 Operator boundary and exact supersession

The amendment’s lines 10–17 remove compiler P1–P4, strict parser-free decoration, native IR restoration, wholly Rust-owned lowering and prototype candidate dependencies. This agrees with `ScopeCorrection.md`, lines 5–17 and 40–46.

The corresponding design, plan and protocol changes remove the active SDK prerequisites and move comparison ownership into Dataclass. Searches of the active design and plan found no surviving requirement to implement SDK artifacts, restore native IR, use prototype candidates or achieve zero parsing.

Historical checkpoint statements do not create an active contradiction: `CurrentProgramCheckpoint.md`, lines 3–20, expressly stops SDK work and identifies the later historical records as subordinate to the operator correction. Elapsed time, usage and detour evidence remain preserved.

### 2.2 Original generation route

The proposed route matches original APIs:

1. `compile_yidl_files` returns compiled concepts carrying their plan, resources and assembly metadata.
2. `emit_concept_runtime_source` embeds source-based resource constructors, matchers and assembly metadata.
3. The emitted runtime provides `new_builder()` and named `build_<assembly>` entrypoints.
4. Assembly execution creates an independent Astichi build and consumes resource templates.
5. The resulting composable exposes `to_executable_ast()`.

Original `MatcherGeneratedValue.to_generator()` caches the unbound compiled template. Original Astichi binding returns a new composable and validates bound values. Thus template reuse and independent class generation are coherent requirements.

The direct-read example is supported by original `external_ref.py`: an attribute-surface reference appends the validated path to its base. Transparent `._` targets propagate Store context. These are reference evidence for the proposed consumer templates, not a full-product implementation result.

### 2.3 Arbitrary objects remain consumer captures

Amendment lines 57–67 and design lines 763–776 distinguish runtime objects from SDK bindings. Factories, defaults, the ContextVar and historical method object remain in the fresh consumer namespace or ordinary builder-function captures; SDK bindings receive validated identifiers/paths or supported literals.

This distinction matters because original Astichi rejects unsupported arbitrary external-binding objects. The amendment does not require function serialization, executable repr or callback invocation during generation.

Independent-capture, hostile-repr and generation-side-effect checks remain explicit in Stages C and G. No final-class/value cache is authorized.

### 2.4 Genuine comparison reuse and dependency ownership

Amendment lines 79–103, design Section 7 and plan lines 128–142 agree on one authoritative Dataclass resource, packaged in wheel and sdist.

Undoable regeneration consumes that authority from a pinned candidate Dataclass wheel, checks its SHA256 and records provenance. Missing or mismatched authority fails before generation. Authority changes require regeneration and checks of both bases.

The original emitter reconstructs resources from embedded source, so a generated Undoable base can execute without a runtime Dataclass lookup. The documentation preserves the distinction between authoritative authored source and mechanically generated embedded output; it does not authorize a maintained handwritten duplicate.

The sdist route is specified: ordinary builds use the checked-in base; explicit regeneration requires the pinned build dependency. Stage G must reproduce packaged outputs and execute Undoable comparisons with Dataclass absent. This is a satisfiable dependency contract, with execution proof still pending.

### 2.5 Semantic and evidence obligations remain intact

The accepted-design diff does not alter field, factory, lazy, frozen, metadata/helper, comparison/hash or Undoable context semantics. The amendment explicitly preserves them.

The amended plan retains:

- A–H product stages and owner checkpoints.
- Genuine behavioral RED → same-target GREEN → refactor evidence.
- Canonical success ownership and independent differential observations.
- Original-SDK correctness and installed checks on Python 3.12, 3.13 and 3.14.
- The complete original-operand, dictionary-hash, tuple-prefix, proxy, ownership and copied-context matrix.
- Distinct consumer ports/binding names, with ordering composition requiring its own proof.
- Five-process measurements, predeclared ratios, variation and interval rules.
- Grounded desk evaluation and unscored missing authoring/calibration evidence.
- Final independent Code and State review.

The committed probe establishes slots/equality/frozen hashing, direct reference specialization and resource caching under two backend selections. Amendment lines 112–121 correctly exclude full ordering, feature parity, three-minor and performance acceptance. The failed expanded ordering attempt remains a limitation to address in consumer resources.

No new architectural inconsistency was established.

### 2.6 Required Surface assessment

The cold README accurately states that product implementation has not started and the amendment awaits review. It identifies the intended library, ordinary slot default, extension families and relevant documentation. It does not present the feasibility probe as product acceptance.

The intended `yidl-dataclass-regenerate-base` command follows the existing Lifecycle/Undoable naming family. Its documented default checks the generated base; `--write` explicitly updates it. The target is a derived artifact of authoritative YIDL source. The amendment clearly separates generation/build dependencies from runtime dependencies.

The cold first-day walkthrough correctly stops at the stated documentation-candidate boundary: there is no claim of an installable implementation or existing product `--help`. Actual installation and use remain the explicitly required Stage-G public-documents-only exercise. Missing future implementation was not treated as a current defect.

## 3. Risks and next action

The principal residual uncertainty is whether the complete accepted semantics can be composed with the original SDKs across all supported minors. The probe and source inspection establish a credible route, not that outcome. Consumer ordering bindings, arbitrary-object capture isolation and packaged two-consumer regeneration particularly require their planned evidence.

The next action is for the lane owner to merge this independent verdict with the other axis. If both accept the same frozen object, record acceptance and resume product Stage A under the consumer-only boundary. A demonstrated original-SDK blocker must be reported for operator scope resolution; it does not authorize SDK implementation work.
