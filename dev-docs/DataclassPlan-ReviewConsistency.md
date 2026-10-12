# DataclassPlan — CONSISTENCY-AXIS REVIEW

**Review object:** `yidl-dataclass/dev-docs/DataclassPlan.md` at `f2514e1c993cb049417b7a10cdf2932bd68bd80f`. Proposed TDD implementation plan, dated 2026-10-12. No Dataclass product implementation or executed product regression evidence exists.

**Baseline:**

| Repository | HEAD |
| --- | --- |
| yidl-dataclass | `f2514e1c993cb049417b7a10cdf2932bd68bd80f` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| astichi | `1c47f781d3804130fdd61cbee07a3b2e4529158a` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

The README was read first using `git show HEAD:README.md`. The plan and supporting sources were inspected with numbered reads and targeted searches. Targeted `git diff HEAD -- PATHS` checks confirmed that inspected files matched committed bytes. The accepted design is unchanged from `de7cadd25c1d3fd5deac0d978043284fa130da1c`. All six HEADs matched at the beginning and end.

**Date:** 2026-10-12

**Axis:** Consistency and plan readiness against the accepted design, controlling requirements, actual harness interfaces and required evidence gates. Independent, adversarial, read-only. This is the recorded interior single-axis tier; no current Safety report exists or was consulted. Filed verbatim by the lane owner.

**Verdict: GO** — zero findings. No Safety escalation is requested. This verdict accepts implementation-plan readiness only; it establishes no runtime, installation or performance result.

---

## 0. Evidence base

Read in `yidl-dataclass`:

- `README.md`, cold first.
- `dev-docs/DataclassPlan.md:1–516`.
- `dev-docs/CurrentProgramCheckpoint.md`, including the accepted design boundary, recorded single-axis plan tier and final Code/State gate.
- `dev-docs/DataclassDesign-ReviewResult.md`.
- Both merged design remediation plans.
- The complete canonical plan-review prompt.

The controlling graph and both prior Consistency design reports were read during the preceding design review in this same reviewer session. Their inspected bytes remain unchanged. The accepted design’s relevant generation and verification sections, `dev-docs/DataclassDesign.md:650–893`, were inspected again. The comparison to `de7cadd25c1d3fd5deac0d978043284fa130da1c` produced no design diff.

Controlling requirements include `DataclassConcept.md`, `ExperimentProtocol.md`, `GoldenExamplesAmendment.md`, `DeclarativeEvaluation.md` and `DataclassSpec-OperatorAmendment.md`. Relevant evaluator passages were previously inspected, and a read-only digest calculation confirmed that `dev-docs/reference/DeclarativeApiEvaluatorV3.md` matches the plan’s stated SHA-256:

```text
20a72d189d1ad032a9f0ab9bbfc1b63636cade0062c1d05bbae0383e7fb0e815
```

Read workspace instructions and the owner-supplied `review-loop/SKILL.md`. The recorded checkpoint tier agrees with the skill’s interior-review rule and automatic escalation condition.

Additional pinned source inspections:

- YIDL `src/yidl/testing/versioned_test_harness.py:1–135`, with targeted inspection of its CLI root selection and matrix/environment functions.
- YIDL `tests/test_yidl_goldens.py:1–114`.
- YIDL `tests/data/gold_src/support/golden_case.py`.
- YIDL’s split dataclass canonical fixture, including `run_multi_source_case`, rendering, validation, AST execution and external bindings.
- YIDL, Undoable and Astichi `pyproject.toml` files.
- Previously inspected pinned compiler, Astichi binding, Lifecycle regeneration and Undoable comparison/ownership surfaces remain applicable because their revisions are unchanged.

No Dataclass `pyproject.toml` exists yet. The plan expressly creates package/dev configuration in Stage A and qualifies its example commands accordingly; this is not an existing-command claim.

Only inspection commands and an in-memory digest calculation were run. No checkpoint tests, builds, package installation, regeneration, benchmark execution, file writes or Git mutations occurred. No drafter or current peer was contacted.

## 2. Invariant analysis

### Meaningful RED → GREEN → refactor

`DataclassPlan.md:35–58` requires each behavior-sized increment to identify its intended assertion or diagnostic, preserve the preceding implementation’s genuine RED, run that same target to GREEN and record any refactor. Unrelated import/environment failures and retroactively fabricated RED results are expressly excluded.

Stages A–F provide concrete missing behaviors rather than generic “add tests” steps. Stage A’s first successful model must already use YIDL/Astichi. Stage B requires actual neutral composition. Stage E introduces the real Undoable consumer; Stage F tests the structural integration’s incorrect child-node write decision before adding the accepted historical boundary.

The stages permit an incomplete intermediate checkpoint without presenting it as implementation acceptance. Stage D explicitly leaves real Undoable reuse outstanding. Final completion still requires the complete API, matrix, installation, evidence and independent implementation review.

The plan also separates behavioral validation from golden maintenance. Lines 131–136 prohibit treating golden regeneration as GREEN. Lines 157–164 assign canonical success assertions, independent differential observations, source inspection and narrow failure/mechanics tests distinct purposes.

### Coverage-obligation mapping

| Accepted design obligation | Plan allocation |
| --- | --- |
| Public declarations, supported minors, standard metadata, direct slots, dictionary mode, signatures, matching and weakrefs | Canonical `dataclass_plain`; Stage A, `:168–195`; three-minor checkpoints |
| Version-selected equality, ordering/hash actions, method conflicts, repr recursion and excluded operands | `dataclass_comparisons`; Stage B, `:197–215`; shared neutral fixture and std differential observations |
| Factory binding, actual provider availability, conversion/validation, const/frozen policies and local storage | `dataclass_initialization` and `dataclass_policies`; Stage C, `:217–242` |
| Lazy seeding, retry/reset, retention/release, copying/pickling and inheritance/class replacement | `dataclass_lazy` and `dataclass_inheritance_helpers`; Stage D, `:244–269` |
| Reusable native comparison generation and actual second consumer | Neutral fixture in Stage B; Undoable adapter and regenerated bundle in Stage E |
| Field-local inclusion, legacy/new write policies, defaults, conflicts and removal | Stage E, `:271–295`; Stage F’s crossed variants and canonical field-removal evidence |
| Native historical write comparison, contextual callback behavior, ownership and context lifetime | Stage F, `:297–336`, including every row of design Section 8’s matrix |
| Parser-free decoration, stable resources, installed wheels/sdists and regeneration provenance | Stage A setup and Stage G, `:338–376` |
| Public-documentation usability, grounded declarative evaluation, reproducible measurements and final review | Stages G/H and Sections 5–7, `:360–516` |

The plan carries the original initializer counterexamples into Stage A at `:183–189`: custom initialization of a required `init=False` field, suppressed init followed by assignment, an unconsumed absent ordinary field, and dictionary class-default fallback with a later class-default change. The actual unavailable-provider failure is assigned to Stage C rather than prematurely “closed” without a generated consumer.

The original AcceptOriginal operand-substitution example is retained at `:313`; the hash-counter/raising-hash defect and collision/error variants at `:314`; the unequal-length tuple-prefix defect and list contrast at `:315`. These are assigned both native-reference evidence and actual staged working-value integration where appropriate.

Stage F also carries:

- Same-state views/pins and equal-valued distinct nodes.
- Disabled parent comparisons with enabled child comparisons.
- Opaque callbacks directly comparing handles.
- Reflected subclass dispatch, NotImplemented and truth conversion.
- Success, equality/truth exceptions, BaseException and ownership loss.
- Nested and cross-manager scopes.
- Outer/inner copied contexts, async tasks and explicit thread contexts.
- In-flight sampling without an atomic-cutover claim.
- Unhashability, structural ordering and native cycle outcomes.
- Prelude placement and absence of Dataclass context overhead.

No design obligation was found to have been replaced by a self-derived comparator oracle or a scope-only probe.

### Harness and packaging feasibility

The named explicit-root functions exist in the pinned YIDL harness. They accept the caller’s project root for discovery and result paths, and `run_golden_case` accepts an explicit cwd. The plan correctly avoids importing the harness CLI and assuming its implicit YIDL root becomes the Dataclass root.

`run_multi_source_case` is an existing canonical convention supporting several emitted artifacts plus behavioral validation. The plan calls for reusing that convention, not importing it from an unsupported package export or copying compiler semantics.

The example `uv run --python … --extra dev python -m pytest …` commands are scoped to owning members after their configuration exists. The inspected members use Hatch and dev extras. The plan separately requires interpreter environments for concurrent matrix runs and resolution of changed local sources during development.

Installed checks at `:340–347` require the built artifact tuple, clean environments, no editable installs or workspace `PYTHONPATH`, imported-module origin checks, and rebuilding from sdists. Logical resource keys and digests are preserved; installed loading cannot rely on sibling checkout paths.

The first and second decoration instrumentation at `:349–358` addresses warm-cache concealment of runtime parsing. It permits final compilation of an AST while prohibiting fresh source parsing in decoration/generated-helper paths. A genuine generic composition defect returns to its owning layer and review boundary rather than authorizing consumer string emitters or AST repair.

### Fixed measurements and honest conclusions

Section 5 predeclares comparable model sizes, standard default/slotted baselines, timed operations, setup boundaries, units and extension labels. Lazy first access receives fresh unready instances prepared outside timing; cached access uses separately prepared ready instances. Generation and source emission remain separate from instance operations. Shallow storage and aggregate allocations are reported separately.

Sampling specifies calibrated batches, warmups, repeated measured batches and at least five independent process runs per minor. It retains raw observations and outliers, alternates paired order and reports variation plus process-pair bootstrap intervals.

The targets are explicit before results:

- Plain slot read/write ratio target: 1.20.
- Ordinary construction and repr/equality/order/hash ratio targets: 2.00.
- Excess variation: inconclusive.
- An interval straddling its target: inconclusive.
- An interval wholly above target: investigate and remediate.
- No unsupported numerical parity promise for extensions, memory, generation or context/prelude costs.

No noisy wall-clock assertion is placed in pytest. Reruns preserve both observations and cannot silently select the better result. Numerical amendments require an explicit plan amendment with earlier evidence retained.

Cold decoration must retain its stated fresh-process boundary when the benchmark manifest is implemented; batching/warmup infrastructure must not turn it into the separately named repeated-decoration case. The plan’s setup-accounting validation and immutable manifest requirements provide the necessary implementation gate.

### Public usability and declarative evidence

The public-only task at `:360–371` supplies installed documentation and packages, excludes private material and the solution fixture, records the first attempt and repairs, and runs in a wheel environment. It is explicitly a usability observation, not a calibrated authoring score.

Section 6 fixes the instrument digest, corpus intentions, held-out variations, units, archetypes and desk mode. It distinguishes resolution locality from physical layout and keeps the operator’s field-local authoring requirement separate.

Missing calibration and authoring-harness evidence remains unscored. The plan does not claim a measured frontier, weighted correctness envelope, few-shot curve or overall grade from designer-authored goldens. Executed failure observations may establish their actual detection stage without upgrading the whole card.

### Authority and scope preservation

The plan introduces no replacement API or architectural decision. It retains the accepted native YIDL path, shared ownership, Undoable-only contextual prelude, unchanged Lifecycle markers and separate assignment policy.

It requires an exact tuple, preserved evidence, final independent Code/State acceptance and new RED/GREEN records for remediation. Architectural conflicts return to redesign/review. Paused UndoableLeaf, unrelated work, GWZ-managed configuration and original experiment measurements remain outside the implementation scope.

Paths are owning-member-relative. Committed logs must redact machine-specific filesystem prefixes while preserving raw observations separately.

**Classification:** No bounded defect or new architectural root cause was established. The remaining uncertainties are implementation evidence duties already assigned to explicit gates.

## 3. Risks and next action

The plan is substantial, and passing its interior gate does not reduce the required three-minor corpus or replace installed-artifact evidence. Parser-free first decoration, actual inherited matcher wiring, captured-context behavior and benchmark setup accounting remain particularly important implementation checks.

The next action is for the lane owner to record this plan’s acceptance at the exact tuple and begin Stage A through the specified RED → GREEN workflow. Final implementation acceptance remains behind the independent Code/State gate and complete evidence requirements.
