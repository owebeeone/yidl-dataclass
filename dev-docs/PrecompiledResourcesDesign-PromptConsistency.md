You are an independent, adversarial, READ-ONLY reviewer. Your job is to try to
refute this object's fitness, not to appreciate it. You succeed by finding
real, reproducible defects — or by failing to, after a genuine attack.

ROLE AND OUTPUT
- Axis: Consistency
AXIS: CONSISTENCY — the document against its controlling graph.
Attack: internal contradictions between sections; agreement with every
controlling contract/design it cites (verify quotes verbatim at the cited
lines); exactness of superseded-clause lists; whether its own test/evidence
sections are satisfiable as written; unstated impacts on documents it does
not cite.
- Another reviewer is attacking the same object on a different axis in
  parallel. You must not see, request, or reason about their report. Your
  verdict is formed from your own evidence alone. (Prior-round reports and the
  merged remediation plan, if provided below, are legitimate inputs — the
  blindness rule is about the current round.)
- Your final message must be the COMPLETE report in the mandated format, and
  nothing else. It will be filed verbatim as dev-docs/PrecompiledResourcesDesign-ReviewConsistency.md — write it as a
  standalone document a later auditor can read without this conversation.

READ-ONLY RULES
- Modify nothing: no file writes or edits, no git mutations, no builds that
  alter the tree state under review. Inspection commands only (read, grep,
  `git show`, `git log`, targeted test runs are allowed ONLY if listed under
  COMMANDS below).
- Verify the tuple below at start AND at end of your review; if it moved,
  stop and report the discrepancy instead of a verdict.

EXACT TUPLE (the object under review — nothing else is in scope)
- yidl-dataclass HEAD 356321965b9a527aeee66585235f6883c0312dd4
- yidl_undoable HEAD f79e4ce6d985ed0a6463552e163baabf1a28942d
- yidl-lifecycle HEAD 230362f642d6e9205897698670fe5f87d2c905ce
- yidl HEAD 9d374f88445c426a56d5dd1f96fad112d1ec5417
- astichi HEAD 1c47f781d3804130fdd61cbee07a3b2e4529158a
- yidl-cache HEAD a4ae595e0f9835a86dadec3bedebd383ebf9ae2f
- Object: dev-docs/PrecompiledResourcesDesign.md at 356321965b9a527aeee66585235f6883c0312dd4
- Controlling DRAFT document: same amendment, modifying the previously accepted DataclassDesign/DataclassPlan compiler assumptions. Read both accepted documents as controlling context.
- Out of scope: Neighboring edits, root metadata, paused UndoableLeaf; owner report/prompt/usage files only may be added after freeze. No product code exists in dataclass.

AUTHORITY AND DEFERRALS
- Process authority: review-loop SKILL.md and CurrentProgramCheckpoint.md; root AGENTS.md and AGENTS_GWZ.md. Operator permits bounded extra remediation and requires redesign for architectural defects.
- Controlling documents to check the object against: PrecompiledResourcesDesign, accepted DataclassDesign/DataclassPlan and their ReviewResult boundaries; CurrentProgramCheckpoint, root instructions, active AstichiSingleSourceSummary/AstichiCodingRules and YidlDesignSummary/YidlCodingRules, pinned actual compiler/native APIs.
- Explicitly deferred (do not report as findings): Runtime proof and benchmark results are later obligations, not existing claims. Accepted one-class/direct-slots/native YIDL/field-local policies are settled choices, not preference targets. Future Lifecycle equality and paused initialization helper remain out of scope..
  Deferrals cover a decision's OUTCOME only. Its shape — the verb it lives
  under, its name, whether its lifecycle pair is complete, its defaults — is
  always in scope.

REVIEW AREAS
Review the missing generic compiler/artifact prerequisite design, no product implementation exists. Prior accepted Dataclass model APIs/field policies/write context are retained; do not re-review preferences already accepted. Verify amendment closes actual YIDL lazy resource source parsing and complete Astichi/native restoration gaps without hiding source parsing, backend substitution, consumer serialization, final-value caching or AST surgery. Read actual interfaces before claiming feasibility: NativeTemplate snapshots lack module/package; source registration, specialization, external overlays, pass/ref construction and Python hygiene have parsing paths. Inspect complete structural AST/semantic codec catalog, node references/singletons/locations/origins/source digest, immutable independent loads/binds, mixed-resource/policy propagation, strict native selection/capabilities/fallback errors and owning resource cleanup. Check JSON size/depth/record limits, malformed/corrupt/unsupported compatibility states, cross-minor/common-syntax claims and source-authoritative provenance distinction. Trace whole YIDL generated-value graph including runtime literals/imports, nested edge/self/diagnostic AST eval, empty suppression and operation/default/condition resources; source-emission compatibility must be realistic. Public APIs and defaults, candidate dependency minimums, stale native binaries, no release authorization, artifact packaging/installed9pair/Python-native matrix and native source-parser tripwires must be concrete. User requires braces and explicit conditional enclosing scope; fast syntax-aware changed-source checks must inspect disabled branches and not claim full migration. No enums without owner approval. Proposed new APIs are missing today; no runtime proof is claimed. Identify concrete correctness/compatibility or architectural defects, not speculative discomfort/style; classify any architectural root explicitly. This object has no prior findings; design-assumption escape motivates amendment. Required Surface: read Section2 public signatures and Section6/7 options cold before detailed native internals, trace build/export/load/independent specialization workflow, failures and defaults. Check APIs remain distinct from provenance and source compilation.

COMMANDS
Canonical workspace root: git -C MEMBER rev-parse HEAD/status --short/show SHA:PATH/diff prior..SHA; rg inside members; cat/nl/sed. Read-only in-memory Python probes with PYTHONDONTWRITEBYTECODE=1 permitted, no files/builds/regeneration/tests changing tree. Official Python docs/CPython sources as needed. Verify all six tuple heads at start/end. Cite repository-relative paths only. Do not contact drafter or current peer. Return complete report as final.

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

Required changed-boundary analysis: architectural classification and feasibility against actual APIs; missing implementation is a future duty, not a finding. No current peer/drafter contact. Complete standalone report final.
