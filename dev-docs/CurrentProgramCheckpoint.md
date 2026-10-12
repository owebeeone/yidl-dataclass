# YIDL Dataclass checkpoint

Status: **operator scope correction: no Astichi or YIDL SDK changes belong to
this task**. All SDK implementation is stopped. The committed P1 and partial P2
work are a preserved out-of-scope detour, not active Dataclass prerequisites.
P2 source currently does not compile; its last successful prototype binary
predates the unfinished statement-splice addition. SDK bytes remain available
for inspection and a separate verified backup exists. No detour was published.

The original installed Astichi 1.1.3 / YIDL 0.1.0 route passes focused generation
checks for slots, equality, frozen hashing, direct field reference specialization
and existing resource caching with both backend selections. This establishes
core feasibility only, not the full requested product. Product implementation
has not started. Next action: finish the read-only original-API assessment and
correct the consumer design/plan to remove SDK prerequisites before resuming.

GO/start remains 2026-10-12T03:36:48Z. The detour's time, tokens and estimated
cost remain part of the experiment record; no retrospective success claim or
metric reset. Historical reviews below retain their original exact scope but
do not authorize SDK work against the operator's correction.

## Requirements review history and authority

The review object is the committed README, `dev-docs/DataclassConcept.md` and
`dev-docs/ExperimentProtocol.md` at
`3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`.
The concept is the controlling draft; it is not an accepted detailed design.
Review-loop process applies, with two peer-blind reviewers: Consistency plus
Surface, and Safety. Reports are preserved verbatim beside these documents.

Reference tuple:

- Undoable: `f79e4ce6d985ed0a6463552e163baabf1a28942d`.
- Lifecycle: `230362f642d6e9205897698670fe5f87d2c905ce`.
- YIDL: `9d374f88445c426a56d5dd1f96fad112d1ec5417`.

Scope: whether the captured requirements are coherent and suitable as the brief
for a detailed design and TDD plan. Accepted choices include a single generated
class, slots by default, specialized accessors, named factories replacing
post-init, and Undoable as the comparison generator's second consumer. Reviewers
may challenge missing boundaries and contradictions without re-litigating those
choices merely because they differ from standard dataclasses.

Choices explicitly marked open are not claims of completed implementation.
Determine whether each can safely remain a detailed-design decision or makes the
brief contradictory, untestable or impossible to satisfy. A GO at this gate would
accept the requirements only, not a public API freeze or implementation readiness.

## Isolation and next action

Reviewers inspect only; no writes, builds, implementation or Git mutations.
Neighboring work, workspace metadata, and Undoable's paused initialization-helper
draft are outside scope. The original Undoable experiment's measurements stay
unchanged. The owner files prompts/reports and merges verdicts after both reviews.
Any structural defect requires a redesign before implementation proceeds.

## Round 1 result and correction

Both axes returned NO-GO on the original object. They independently identified
the collision between logical field inclusion and Undoable's existing transaction
`compare` setting. Consistency also found missing comparison option defaults.
See both verbatim reports and `DataclassSpec-RemPlan.md` for dispositions and
closure requirements. No finding is self-closed by the owner.

The corrected object consists of README, the concept, the protocol, and the new
`GoldenExamplesAmendment.md` in the same commit as this checkpoint. It separates
transaction policy from decorator-level logical inclusion and records option
defaults. Fresh Consistency/Surface and Safety reviewers replace the original two
because the comparison interface changed. Round 2 prompts will name the exact
commit and inherit every prior finding on their axis.

## Round 2 and operator acceptance

Both fresh reviewers returned GO on
`0ceb048a98f9e4464366fc1abfb0827888e8fc54`, independently closing the original
findings at the requirements gate. See their verbatim `-ReviewConsistency-2.md`
and `-ReviewSafety-2.md` reports. No new architectural root cause was reported.

The operator rejected the decorator field-name mapping and directed a field-local
comparison flag, a separate transaction write policy and preservation of legacy
declarations. The operator explicitly accepted that spec amendment without another
review. `DataclassSpec-OperatorAmendment.md` records the override and evidence
boundary. The two GO reports do not review the final amended bytes.

Accepted requirements revision: `2abedb40c2c0b3037420d59d5a45eefe13503bee`.
See `DataclassSpec-ReviewResult.md` for exact object/verdict boundaries.

The final requirements object adds `DeclarativeEvaluation.md` to the concept,
protocol and golden amendment. The owner records its exact committed revision in
the review result. Acceptance covers suitability as a brief for detailed design
only, not a completed design, implementation, release or performance result.

The operator has delegated the full remaining task, without requiring personal
review of the detailed design or TDD plan. Run the independent design and final
implementation review gates autonomously. The waiver applies to the accepted
locality amendment, not the remainder of the experiment's review workflow.

Detailed design draft: `DataclassDesign.md`, reviewed at
`9fd44d91943ca706c4c51a0669bd3e9d03260278` with dual NO-GO. It is not yet
accepted. Required design tier: dual peer-blind
review at this interface freeze. Prior requirements reviews do not accept this
new design object. The TDD plan and implementation remain behind that gate.

Cycle-1 findings are filed verbatim with `DataclassDesign-RemPlan.md`: one
initializer-suppression contradiction, a stale README and a write-comparison
adapter replacing opaque callback operands. All have bounded corrections; no
architectural failure was reported. The merged design/README correction is ready
for both original reviewers' independent re-verdicts.

Cycle-1 correction was reviewed at
`5d7883d8838fb9fa170426fbda59a71af3e9188b`. Both original reviewers returned
NO-GO while independently closing the initial findings. They independently found
that manual dictionary lookup adds hash callbacks; Safety also found that a
length-first tuple comparison suppresses native prefix callbacks. Reports and
`DataclassDesign-RemPlan-2.md` preserve the evidence and dispositions.

The owner selected a redesign of the small write-comparison boundary: native
equality under a temporary historical-identity context, with an Undoable-only
generated equality prelude. Two fresh reviewers replace the prior pair for this
changed generation and callback boundary. No product implementation has started.

Status: **detailed design accepted at
`de7cadd25c1d3fd5deac0d978043284fa130da1c` after both replacement reviewers
reported GO**. Their verbatim round-3 reports and `DataclassDesign-ReviewResult.md`
define the acceptance boundary. All inherited design findings are independently
closed; implementation and performance remain unverified.

The separate `DataclassPlan.md` is drafted and awaits its gate. Recorded plan tier: interior single-axis
Consistency, with automatic second-axis Safety escalation for any P0/P1/P2 or
reviewer request. No new interface or architectural decision belongs in that plan;
such a change must return to the dual design gate. Final implementation acceptance
uses dual Code/State review. Product code starts only after the plan gate passes.
Status: **TDD plan accepted at `f2514e1c993cb049417b7a10cdf2932bd68bd80f`
after `DataclassPlan-ReviewConsistency.md` reported GO with no findings**.
No second-axis escalation was required. Product implementation starts at Stage A,
with genuine native generation and direct public slots. The drafter stops at
stage checkpoints for owner verification/commits. Final acceptance remains ahead.
Stage-A inspection found that YIDL resource wrappers compile source lazily and
Astichi has no supported whole-template artifact restore path. Its native snapshot
registration carries metadata without the parser IR required for materialization;
some native external/ref/pass operations also parse expression source. Existing
final-AST caching and provenance do not satisfy reusable-template restoration.

Next action: draft and independently review `PrecompiledResourcesDesign.md`, an
Astichi/YIDL owning-layer amendment, before Stage A proceeds. No cache warming,
consumer serialization workaround or backend substitution closes this gap.

The amendment draft is ready for a fresh dual Consistency/Safety gate. It adds
explicit generic artifact/structural compiler APIs, full native IR restoration,
recursive YIDL resource policy and candidate dependency versions. The owner
settles its exact tuple; the sole drafter has made no code or test changes.

Status: **compiler prerequisite design accepted at
`356321965b9a527aeee66585235f6883c0312dd4` after both fresh reviewers reported
GO with no findings**. See its review result and implementation addendum.
Next action: P1 Python artifact support with genuine RED/GREEN; product Stage A
remains paused until P1–P4 prerequisites pass. Native/installed behavior has not
yet been implemented or verified.

P1 checkpoint: Python artifact APIs and structural frontend verified at Astichi
`4a62b093498dae7b6d346306eae23e5925aaa004`. See
`PrecompiledResources-P1Result.md` for exact scope, four source-matrix results,
installed owner probes and evidence. Source/native legacy behavior is distinct
from new native artifact capability, which remains absent. Next action: sole
drafter P2 native IR restoration, strict parser counters and no fallback.
