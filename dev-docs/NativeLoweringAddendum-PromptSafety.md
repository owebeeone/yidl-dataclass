You are an independent, adversarial, READ-ONLY reviewer. Your job is to try to
refute this object's fitness, not to appreciate it. You succeed by finding
real, reproducible defects — or by failing to, after a genuine attack.

ROLE AND OUTPUT
- Axis: Safety
AXIS: SAFETY — what the text permits to go wrong.
Attack: degraded and mixed-version paths; irreversible steps and their
preconditions; disclosure/privacy scale; stuck states reachable under the
text's own rules; whether "never worse than the status quo" claims survive
concrete interleavings; scope creep that widens blast radius.
- Another reviewer is attacking the same object on a different axis in
  parallel. You must not see, request, or reason about their report. Your
  verdict is formed from your own evidence alone. (Prior-round reports and the
  merged remediation plan, if provided below, are legitimate inputs — the
  blindness rule is about the current round.)
- Your final message must be the COMPLETE report in the mandated format, and
  nothing else. It will be filed verbatim as dev-docs/NativeLoweringAddendum-ReviewSafety.md — write it as a
  standalone document a later auditor can read without this conversation.

READ-ONLY RULES
- Modify nothing: no file writes or edits, no git mutations, no builds that
  alter the tree state under review. Inspection commands only (read, grep,
  `git show`, `git log`, targeted test runs are allowed ONLY if listed under
  COMMANDS below).
- Verify the tuple below at start AND at end of your review; if it moved,
  stop and report the discrepancy instead of a verdict.

EXACT TUPLE (the object under review — nothing else is in scope)
- yidl-dataclass HEAD 1f1bc534b460753e8cd91230e5349ea802c90b5c
astichi HEAD 4a62b093498dae7b6d346306eae23e5925aaa004
yidl HEAD 9d374f88445c426a56d5dd1f96fad112d1ec5417
yidl_undoable HEAD f79e4ce6d985ed0a6463552e163baabf1a28942d
yidl-lifecycle HEAD 230362f642d6e9205897698670fe5f87d2c905ce
yidl-cache HEAD a4ae595e0f9835a86dadec3bedebd383ebf9ae2f
- Object: dev-docs/NativeLoweringAddendum.md and supporting docs/validation/prerequisites/p2-paused-manifest.json in yidl-dataclass at 1f1bc534b460753e8cd91230e5349ea802c90b5c
- Controlling DRAFT document: dev-docs/NativeLoweringAddendum.md at 1f1bc534b460753e8cd91230e5349ea802c90b5c
- Out of scope: Code acceptance is OUT OF SCOPE. Astichi P2 prototype code/evidence is uncommitted, paused and hash-frozen in the committed supporting manifest; it may be inspected only after verifying its listed hashes and must not be treated as accepted implementation. Neighboring edits, root staging/configuration, paused UndoableLeaf, current peer reports and drafter messages are excluded. Owner prompts/reports may appear uncommitted after freeze; HEADs remain fixed.

AUTHORITY AND DEFERRALS
- Process authority: review-loop SKILL.md, CurrentProgramCheckpoint.md, root AGENTS.md/AGENTS_GWZ.md. User permits bounded remediation beyond two cycles and autonomous redesign, but no implementation until redesign is accepted.
- Controlling documents to check the object against: NativeLoweringAddendum; accepted PrecompiledResourcesDesign at 356321965b9a527aeee66585235f6883c0312dd4; current PrecompiledResourcesImplementation, accepted DataclassDesign/DataclassPlan and their exact ReviewResult boundaries; active AstichiSingleSourceSummary/AstichiCodingRules and YidlDesignSummary/YidlCodingRules; actual owning graph/materialization/hygiene/native APIs.
- Explicitly deferred (do not report as findings): Runtime proof and performance are future gates, not existing claims. Dataclass model API, frozen/field-local/no-facade design, pure slot/generated field access, artifact v1 bytes and no native fallback remain retained requirements. Direct complete graph-to-native lowering is optional only as optimization; native pre-expansion before indexed merge and retained-shell lowering are required. Do not re-litigate settled product preferences..
  Deferrals cover a decision's OUTCOME only. Its shape — the verb it lives
  under, its name, whether its lifecycle pair is complete, its defaults — is
  always in scope.

REVIEW AREAS
Review this architectural lowering addendum, NOT P2 code acceptance. It closes a discovered gap between plain Builder.build/build_merge retained insertion-shell ASTs and AssemblyScope native operation streams. Trace actual source: materialize/api.py::_resolve_build_graph/build_merge/materialize_composable, builder/handles.py, model/basic.py, assembler/scope.py, hygiene analysis/rename pipeline, native materialize_ir/parser_ir/template_extract and supported marker/ref/unroll/payload helpers. Determine whether existing retained syntax+semantic state is sufficient for direct/staged/loaded/default/parameter/expression/elif/root/boundary/ref/pyimport/unroll/hygiene semantics, with no original graph recipe or v1 wire changes. Check exact source phase order, native pre-expansion before indexed target resolution, avoiding double expansion, and generic Python assembly versus prohibited semantic transforms. Assess concrete pure-planning/native-execution boundary: planners cannot mutate Python ASTs, call old materializers or deliver pre-transformed output modules as disguised native work. Stable node/scope keys, copy lineage, fresh projections, generation/epoch validation, exact old values, closed actions/limits and transaction publication must support all current transformations. No new enums/passive tag workarounds. Check full lexical role/trust/keep/collision/closure/global/nonlocal/comprehension semantics and canonical naming, comments and executable cleanup, no extra Root ambiguity. Verify dependency/capability guard remains fail-closed for restoration-only/stale binaries; default source/Python mode remains compatible. Expanded-node/action budgets, cycles/custom/shared data, wrong references/owners, cancellation/cleanup and independent reuse must be concrete. Check test-method classification: 13 core passes are scoped; 78 failures include seven oracle boundary errors and 71 genuine native issues; preserve all failures/canonical expectations, no skips/fallback/golden weakening to claim success. Public APIs/artifact bytes unchanged: Consistency additionally read public workflow cold and check whether the addendum hides any new user-facing setting, failure or dependency need. Missing future implementation is not a finding; an unimplementable/underspecified seam or contradiction is. Explicitly classify any architectural root cause. Prior compiler amendment reviews were GO with no findings; no open same-axis findings to inherit. Do not read the current peer or consult drafter. Report full standalone verdict.

COMMANDS
Canonical workspace root is the operator-specified environment cwd. Read-only git -C MEMBER rev-parse HEAD/status --short/show SHA:PATH/diff, rg/cat/nl/sed inside members. Prefer committed baseline via git show. Supporting uncommitted P2 files may be read only if their SHA256 matches docs/validation/prerequisites/p2-paused-manifest.json (paths relative to owner_repository astichi); verify any inspected hashes again at end. No builds/tests/regeneration/files/Git mutations. In-memory Python inspection with PYTHONDONTWRITEBYTECODE=1 allowed only when it writes no files. No code acceptance claim from prototype. Verify all six HEADs at start/end. Use repository-relative paths in report; no absolute machine paths. Final COMPLETE report only.

SEVERITY AND VERDICT CONTRACT
- Findings use IDs P0-n / P1-n / P2-n / P3-n:
  P0 = active corruption, data loss, credential exposure, or false composition.
  P1 = likely destructive or unrecoverable release blocker.
  P2 = concrete correctness, recovery, compatibility, parity, or
       diagnosability defect.
  P3 = bounded robustness, coverage, maintainability, or documentation defect
       with a concrete consequence.
- Verdict is GO or NO-GO. NO-GO while any P0, P1, or P2 is open.
- Each finding: ONE root cause, exact location, violated invariant, credible
  reproduction or state/interleaving sequence, impact, required correction,
  and a closure/regression test. Separate independent root causes.
- Style preferences and speculative unease are not defects. Do not pad.
  Interface shape is not style: wrong command placement, a misleading name,
  a missing half of a lifecycle pair, or an option without a default is a
  finding (P2 or P3), on every axis.
- If your verdict is NO-GO but every blocking finding has a bounded,
  text-or-code-fixable remedy, you may pre-commit: "I pre-commit to GO on a
  revision that resolves {IDs} as specified." This makes the re-verdict cheap
  and is encouraged when honest.

MANDATED REPORT FORMAT
# {OBJECT} — {AXIS}-AXIS REVIEW

**Review object:** {object at exact SHA / doc path + status + date}
**Baseline:** {per-repo SHAs; note how sources were read, e.g. `git show HEAD:`}
**Date:** {date}
**Axis:** {one line: mandate}. Independent, adversarial, read-only. The other
axis runs in parallel; nothing here relies on it. Filed verbatim by the lane
owner.

**Verdict: {GO | NO-GO}** — {counts, e.g. "two P1 and three P2 findings
block"}. {If NO-GO and honest: pre-commit-to-GO clause naming the finding IDs.}

---

## 0. Evidence base
{What was actually read/run: files with line ranges, documents with sections,
commands with results. This section is what makes the verdict auditable.}

## 1. Findings
### [P1-1] {one-line root-cause title}
{Location · violated invariant · reproduction or state sequence · impact ·
remedy · closure test.}
{… one subsection per finding, severity-ordered. Omit section if none.}

## 2. Invariant analysis
{The invariants attacked and the evidence they held — attacks that FAILED are
part of the result; they are what a GO rests on.}

## 3. Risks and next action
{Residual risks below the finding bar; the single next action this verdict
implies.}

Required analysis: phase/call-graph feasibility and architectural classification against actual source, frozen prototype only as supporting data; complete report final, no writes or peer contact.
