# YIDL Dataclass preparation and review ledger

Status: autonomous Dataclass run authorized; operator has excluded SDK changes.
Compiler detour stopped and preserved; consumer-only Stages A–D are verified and
Stages E/F are also verified. G/H and final product acceptance remain outstanding. The original
Undoable experiment and this experiment's earlier requirements preparation remain
separate measurement stages.

## Checkpoints

| UTC time / revision | Event |
| --- | --- |
| `b9a3788` | Member created and initial discussion requirements captured. |
| `12111c7` | Performance and second-experiment protocol recorded. |
| `f7e00b8` | Reusable comparison generation requirement recorded. |
| `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13` | Undoable selected as real second consumer; initial requirements object. |
| 2026-10-12T03:18:04Z | First recorded requirements-review preparation checkpoint; measurement baseline for this review stage only. Earlier preparation is not included in these deltas. |
| 2026-10-12T03:18:38.479Z | Independent Consistency/Surface reviewer starts. |
| 2026-10-12T03:18:43.234Z | Independent Safety reviewer starts. |
| `8c116f51310343b18e4ebae27ea6a91517f828e4` | Review-scope checkpoint; both reviewers verify pinned tuple at start/end. |
| Round 1 | Both NO-GO, independently finding the same P2 namespace collision; one additional P3 defaults finding from Consistency. |
| Round 1 remediation | One corrected documentation object, incorporating the operator's golden-example addition; fresh reviewers required for changed interface. |
| `0ceb048a98f9e4464366fc1abfb0827888e8fc54` | Both fresh round-2 reviewers GO; original findings independently closed on that draft. |
| Operator locality correction | Decorator mapping rejected; field-local logical comparison and separately named write policy specified. Operator explicitly accepts this amendment without another review round. |
| 2026-10-12T03:36:48Z | Operator says GO for the full autonomous run, without requiring personal review of design/TDD planning. Recorded start: 14:36:48 Australia/Sydney. Detailed design and run measurements begin here; implementation begins only after its design/plan checkpoints. |
| 2026-10-12T03:37:46.089Z | Sole design drafter starts. |
| `9fd44d91943ca706c4c51a0669bd3e9d03260278` | Detailed design settled for independent review. |
| 2026-10-12T03:49:46.792Z / 03:49:51.542Z | Independent Consistency/Surface and Safety design reviewers start. |
| Design round 1 | Both NO-GO. Two distinct bounded P2s (initializer suppression and opaque callback operands) and one P3 stale README. One merged remediation assigned; no implementation or TDD plan started. |
| `5d7883d8838fb9fa170426fbda59a71af3e9188b` | Cycle-1 correction reviewed by the original pair. Both NO-GO, closing initial findings but independently finding dictionary hash-callback drift; Safety additionally finds tuple prefix-callback drift. |
| 2026-10-12T04:15Z | Small write-comparison boundary redesigned before implementation: retain native equality with a scoped historical-identity prelude for Undoable only. Fresh reviewers replace the prior pair because this changes the generation/callback boundary. |
| `de7cadd25c1d3fd5deac0d978043284fa130da1c` | Both fresh design reviewers GO, independently closing all inherited findings. Detailed design accepted only; no implementation or performance claim. |
| 2026-10-12T04:24:33Z | Separate TDD plan drafting begins after design acceptance. Interior single Consistency review tier, auto-escalate for P0/P1/P2 or request; final implementation remains dual Code/State. |
| Design-acceptance usage checkpoint | Latest observations across six disjoint actors estimate approximately $7.07 Standard API-equivalent USD, including design reviews. These are cumulative observations around acceptance, not exact disjoint stage billing; some immediately subsequent planning/output may enter late actor samples. Actual billing unavailable. Elapsed GO-to-acceptance: about 47m45s. |
| `f2514e1c993cb049417b7a10cdf2932bd68bd80f` | Interior TDD-plan Consistency review GO with no findings; no Safety escalation required. |
| 2026-10-12T04:36Z | Product implementation starts with Stage A after design/plan gates. Sole drafter, strict behavioral RED/GREEN, stage checkpoints for owner verification and scoped commits. |
| Stage A inspection | Before product writes or behavioral RED, actual resource/backend inspection reveals missing whole-template artifact restore and native parser-free payload paths. Product work pauses for an explicit Astichi/YIDL compiler-boundary amendment and dual review. This is a design-assumption escape discovered during implementation preparation; the prior GO reports did not establish executed generation evidence. |
| Compiler amendment draft | `PrecompiledResourcesDesign.md` specifies Astichi artifact/structural APIs, necessary native IR/payload work, recursive YIDL opt-in emission, candidate minimums and cross-minor/backend tests. Fresh dual review precedes compiler code. No product/test edits or behavioral RED occurred during this inspection/redesign. |
| `356321965b9a527aeee66585235f6883c0312dd4` | Both compiler amendment reviewers GO with no findings. P1–P4 owning-layer implementation sequence begins; Dataclass Stage A remains paused behind those checks. |
| `9ebd33a9c831e261919076a5ffef590948ffd546` | Owner acceptance/review reports, explicit P1–P4 execution addendum and baseline installed-native evidence committed before compiler writes. |
| Compiler-amendment acceptance usage | Latest observations across eight disjoint actors estimate approximately $13.16 Standard API-equivalent USD. Covers autonomous design, reviews and prerequisite preparation to the observed samples, including late owner processing; not a product-completion or actual-billing result. Cached input is repeated context. |
| 2026-10-12T05:36Z / P1 working | Two-hour checkpoint: latest eight-actor observations estimate approximately $15.94 Standard API-equivalent USD. Python artifact focused and initial canonical gates pass on the working tree; broader prerequisite verification remains ahead. Independent owner inspection discovers context-neutral/identifier validation concerns; the drafter preserves their owning RED/GREEN records. No product Stage A claim. |

| 2026-10-12T06:03Z / P1 stopped | Sole drafter stops after Python artifact/structural implementation, canonical replay, full supported-minor/source-only 3.15 matrix and strict documentation checks. |
| Astichi `4a62b093498dae7b6d346306eae23e5925aaa004` | Owner verifies source/evidence/raw hashes, installed three-minor source-compile tripwire/ownership probes and downstream YIDL regression, then commits scoped P1. Native support and product work remain outstanding. |
| P1 verification usage checkpoint | Latest eight-actor observations estimate approximately $18.73 Standard API-equivalent USD, about 2h31m after GO at the latest owner sample. Includes design, reviews and prerequisite work; actual billing unavailable. Approximately 90.1M cumulative input tokens include 88.1M repeated cached input; 506,474 output tokens include reasoning. These are request counters, not unique source volume or completed-product cost. |

| 2026-10-12T06:21Z / preliminary portability and P2 envelope | All nine installed Python producer/consumer pairs pass. Native baseline probes confirm surrogate literal substitution and UTF-8 metadata rejection; accepted unsupported-native-combination clauses permit precise rejection rather than sidecars. P2 resumes with path diagnostics before registration. Latest eight-actor observations estimate approximately $20.00 Standard API-equivalent USD, about 2h45m from GO; actual billing unavailable. Product work remains behind compiler prerequisites. |

| 2026-10-12T06:59Z / P2 graph-lowering pause | Working native core reaches 13 passing tests with actual parser counters. Four-backend corpus first reports 120 failed/52 passed; corrected phase-boundary attempt reports 78 failed/94 passed, including further validator-oracle tripwire errors. Counts are not all compiler behavioral REDs. Genuine staged-builder/native operation and hygiene gaps trigger read-only architectural classification before bridge code; no aggregate P2 acceptance. Latest eight-actor observations estimate approximately $23.52 Standard API-equivalent USD, about 3h23m from GO; actual billing unavailable. |

| 2026-10-12T07:37Z / native lowering design accepted | Fresh Consistency and Safety reviewers both GO with no findings on `1f1bc534b460753e8cd91230e5349ea802c90b5c`. Both classify the prior sufficiency assumption as architectural; the addendum requires retained-shell/native hygiene lowering and pre-expansion without changing APIs/artifact v1. Prototype code remains unaccepted. P2 TDD resumes. Latest ten-actor observations estimate approximately $27.06 Standard API-equivalent USD, about four hours after GO; actual billing unavailable. |

| Post-acceptance P2 classification erratum | The seven tripwires partition as four provenance oracle executions and three genuine commented-renderer parses. Latest 78 failures therefore mean four oracle errors plus 74 genuine behavior/metadata/parser defects. Original output and reviewed seven/71 claim remain historical; appended correction supersedes that classification. Parser-free commented emission was already required by the accepted architecture; its guard stays intact. |

| 2026-10-12T08:07Z / P2 implementation checkpoint | Latest ten-actor observations estimate approximately $29.48 Standard API-equivalent USD, about 4h30m from GO; actual billing unavailable. Working focused gates pass for structural comment rendering, native workspace ownership/name rewrites and read-only lexical planning; defaulted-hole native-to-Python replay now passes. Lifecycle marker correspondence, complete native shell/lowering integration and broader installed/minor gates remain outstanding. P2 and product work are not accepted. |

| 2026-10-12T08:22Z / operator progress report | Latest ten-actor observations estimate approximately $30.91 Standard API-equivalent USD, about 4h46m from GO; actual billing unavailable. Native metadata/artifact refactor gate reports 58 passed and one skipped; raw invalid-table registration was independently reproduced and verified rejected without consuming index or parser entry after its owning RED/GREEN fix. Native node-identity conversion preflight has a new focused RED. Full native lowering, P3/P4 and product A–H remain outstanding. |

| 2026-10-12T08:37:48.284477+00:00 / operator scope correction | Operator states no Astichi/YIDL SDK changes were in scope. Owner acknowledges introducing an unnecessarily strict parser-free/native-restoration prerequisite. SDK implementation stops; P1/P2 remain a preserved detour, not active product prerequisites. Original installed SDK probe passes core slots/equality/frozen-hash/direct-field-reference/cache checks for both backend selections. Product design/plan correction follows; original elapsed time and cumulative usage remain intact. |

| 2026-10-12T08:42:15.586264+00:00 / corrected-scope assessment | Independent owner and sole-drafter original-SDK probes identify no concrete blocker to consumer-only generation. Latest ten-actor samples estimate $32.98 Standard API-equivalent USD at about 5h01m from original GO; actual billing unavailable. This run has required a post-GO operator scope correction and must not be described as an uninterrupted successful one-shot. Consumer design/plan amendment is assigned; no product code exists yet. |

| 2026-10-12T08:56:06.871213+00:00 / consumer amendment accepted | Fresh independent Consistency and Safety reviewers both GO with zero findings on `382d389172f38e33de8a00af350b1b6b21d46f5b`. Original-SDK source generation, consumer captures and build-only shared-resource reuse are accepted as the product route. SDK prototypes remain stopped/excluded. Product Stage A resumes next; full semantics, installed gates, benchmarks and final reviews remain ahead. |

| 2026-10-12T09:00Z / product Stage A resumed | Sole drafter begins consumer-only product work after amendment acceptance, using separate original-SDK environments and behavioral slot/constructor RED rather than import/setup failures. Latest twelve-actor observations estimate approximately $35.37 Standard API-equivalent USD, about 5h23m from original GO; actual billing unavailable. This includes the preserved scope detour, operator correction and independent amendment review, not a completed-product cost. SDK source/build changes remain forbidden. |

## Autonomous scope and intervention rules

At 2026-10-12T15:07:14.647023Z the fresh final-Code reviewer finishes its
public-only author phase before implementation inspection: four final cards
pass in 276.647023 seconds, eight executions/three failures and documented
repairs retained. Failures were replacement-cache expectation and counter-window
errors, not established product defects. No required clarification remains.
The author-only actor observation estimates $0.249136 Standard API-equivalent
USD; actual billing unavailable. It is one actor now added to experiment totals,
not a calibrated authoring score or final Code verdict. Raw/verbatim evidence
is externally content-addressed with explicitly sanitized committed derivatives.

At 2026-10-12T14:58Z Stage G package/installation gates are owner-verified.
All 18 installed suites and six owner final public-example smokes pass; wheel
and sdist inventories/hashes are independently checked, with runtime/resources
unchanged from verified D/EF. Cold public-only author and H/final reviews remain.
Eight canonical/two seam source/oracle snapshots are frozen before authoring.
Latest twelve-actor observations estimate $67.5929676 Standard API-equivalent
USD, about 11h22m from GO; actual billing unavailable. Input 346,714,543 includes
340,224,000 cached tokens; output 1,782,759 includes 984,904 reasoning tokens.
No timing measurement or final completion is claimed.

At 2026-10-12T14:16Z E/F is owner-verified: Undoable full source/regeneration
matrix passes 340 tests in each of six original-backend/minor combinations;
Dataclass product remains unchanged from D with eight affected checks per run.
Independent evidence/raw/JUnit audits and six installed owner probes pass;
installed regeneration matches on both backends. `Dataclass-StageEFResult.md`
records manifest and wheel identities. G/H and final reviews remain. E's
post-implementation removal case, F setup/oracle corrections and the genuine
rich multi-view/hash-name failures stay explicitly distinguished.

Latest twelve-actor observations estimate $64.6097148 Standard API-equivalent
USD, about 10h39m from original GO. Input totals 331,221,935 tokens including
324,934,272 repeated cached input; output totals 1,677,907 including 922,579
reasoning tokens. Actual billing remains unavailable. SDK detour and operator
interventions remain included; no uninterrupted successful one-shot or strict
all-features-first TDD claim is made.

Historical observations around 2026-10-12T13:44Z across twelve disjoint actors
estimate $60.9429478 Standard API-equivalent USD, about 10h07m from original GO.
Input is 314,637,200 tokens including 308,613,760 repeated cached input; output
is 1,601,183 tokens including 883,878 reasoning tokens. Actual billing remains
unavailable. D is verified; E's identical targeted API/canonical gates pass
62 tests on each original backend. F's staged/context REDs are preserved and
composition is still undergoing correction. E's richer declaration-removal
fixture was authored after core comparison behavior and already passed, explicitly
recorded as post-GREEN verification rather than the planned feature-first proof.
No combined E/F, final installation or performance acceptance is claimed.

External benchmark preparation retains calibration observations separately from
warm/measured batches. The new calibration-observer API first failed as missing;
its first test expectation incorrectly assumed count2 instead of the existing
1.1 safety multiplier's count3, so the corrected result is verification rather
than an unchanged RED→GREEN claim. Current mechanics observations and external
source hashes are in `docs/validation/perf-preparation/`; coverage validation
checks are post-drafting verification. No numerical gate was relaxed, and no
measurement inventory or artifact tuple is yet accepted as final.

At 2026-10-12T13:13Z Stage D is owner-verified: post-fix D13 has 198 cases in
each original backend/minor source run, with 195/196/197 passes and only 3/2/1
version-specific skips. All 24 owner installed calls and both installed
regeneration checks pass. The independent audit verifies 444 owned hashes,
117 records, 188 artifact references, 149 distinct raw hashes and 71 JUnit artifacts.
`Dataclass-StageDResult.md` names the exact stopped manifest and wheel hashes.
Private builtin aliases fix independently reproduced C constructor collisions;
all old RED/attempt records remain. E–H and final reviews remain outstanding.
Latest twelve-actor samples estimate $57.8898954 Standard API-equivalent USD
around 9h36m from original GO; actual billing unavailable. Prior scope/process
lapses and test-sequencing limitations remain in the experiment, not reset.

At 2026-10-12T12:54Z the independent owner pre-integration Undoable source
baseline at `f79e4ce6d985ed0a6463552e163baabf1a28942d` passes all six original
SDK backend/minor runs, each with 215 tests and no failures/errors/skips.
`docs/validation/baseline/undoable-before-integration/` preserves sanitized logs,
JUnit, raw digests and installed-origin checks. Original Astichi 1.1.3, YIDL
0.1.0 and existing Lifecycle wheel are used; no reference dependency rebuild is
performed. Undoable source remains unchanged, including its paused helper work.
This is the Stage E regression baseline, not integration acceptance.

Latest observations at 2026-10-12T12:45Z across twelve disjoint actors estimate
$55.0345382 Standard API-equivalent USD, about 9h09m after original GO. Input is
280,452,538 tokens including 274,960,384 repeated cached input; output is
1,453,133 tokens including 805,880 reasoning tokens. Actual billing remains
unavailable. The drafter reports focused D inheritance, copy/deepcopy, pickle
cycle, replacement and annotation checks passing against both original backends;
source/descriptor proof and the complete matrix still precede owner acceptance.
An owner-installed C probe independently exposed a valid `property` field
shadowing the bare builtin; the drafter records RED on both backends and GREEN
with a private builtin binding. The raw owner failure and unchanged probe are
retained for independent installed D verification. No SDK change is authorized.

External benchmark drafts now include ordinary/frozen operations, extension
pipelines, fresh lazy pools, repeated generation with declarations outside timing,
actual commented-source emission from an untimed captured owned build result,
and the memory inventory. Six deterministic harness checks pass; generation and
source-emission setup smoke passes on installed C with both backends. These are
preparation/verification observations after code drafting, not a test-first claim
or measured performance result. Cold sampling retains its pre-measurement note;
Undoable seam, full product matrix and final independent reviews remain ahead.

Latest observations around 2026-10-12T12:27Z across twelve disjoint actors
estimate $53.6625282 Standard API-equivalent USD, about 8h51m after original GO.
Input is 273,743,835 tokens, including 268,366,080 repeated cached input; output
is 1,416,892 tokens, including 779,736 reasoning tokens. Actual billing is
unavailable. Stage D is active: lazy/retention and inheritance focused checks
have passed, while copying/replacement and 3.14 annotation boundaries are being
implemented. Full D acceptance and E–H remain; this is not final product cost.
The provisional property-constructor spelling for lazy accessors is recorded as
an existing-resource source choice for final Code/provenance assessment, without
runtime helper dispatch. Cold benchmark sampling preparation is separate from
final measured performance (`BenchmarkSamplingNotes.md`).

At 2026-10-12T11:42Z Stage C is owner-verified: all six complete source runs
have 156 passed/one version-specific skip; all six isolated installed extension
probes and both installed regeneration checks pass. Owner independently checks
286 owned hashes, 75 increment records, 123 artifact references, 103 distinct raw
hashes and 48 JUnit artifacts. `Dataclass-StageCResult.md` records exact source and
wheel provenance. D–H and final reviews remain. The unsupported owner `--check`
CLI attempt is preserved as setup; default invocation performs the supported
check. Latest twelve-actor observations estimate $49.880027 Standard
API-equivalent USD at about 8h05m from original GO: 253,224,491 input tokens,
248,081,408 repeated cached input, and 1,288,423 output tokens including 700,065
reasoning tokens. Actual billing remains unavailable; this is not a
completed-product cost. Source-only scope, prior intervention and sequencing
limitations remain unchanged.

At 2026-10-12T11:18:26Z the owner preserved an Undoable pre-integration wheel
for later write-path comparison. An unnecessary packaging-only Lifecycle wheel
build breached the recorded dependency no-rebuild boundary. No new source edit
occurred; its artifact digest equals the already available original wheel. The
new build is excluded and the original wheel remains the reference. This process
lapse is retained in `../docs/validation/baseline/undoable-before-integration.json`
and final compliance assessment. It does not authorize any dependency work.

At approximately 2026-10-12T11:10Z, twelve disjoint actor observations estimate
$47.369159 Standard API-equivalent USD, about 7h33m after the original GO.
Cumulative input is 240,052,815 tokens, including 235,106,048 repeated cached
input. Output is 1,206,353 tokens, including 658,257 reasoning tokens. Actual
billing is unavailable; these are incomplete-run counters including the SDK
detour and intervention. Stage C named-factory checks have reached seven passes
and hidden/local/provider-kind checks thirteen passes on both original backends;
the stage is not accepted. Conversion/validation/frozen policies remain active.
Owner is preparing benchmark accounting outside the repository while the sole
drafter implements product code. No provisional benchmark is a product
performance claim, and the Section 5 measurement gates remain unchanged.

At 2026-10-12T10:53:08Z the operator requested status and an estimate without
stopping work. Owner reported A/B implemented/verified, C in progress, D–H and
final acceptance outstanding, and an uncertain remaining estimate of 4–6 hours.
That estimate is prospective, not a measured completion time. No pause or new
approval gate was inferred; the sole drafter continued.

Stage B is verified and committed at
`d3997d6f27f178b5b16df6e479f3e41c920b69cf`. Its final six source runs have
86 passed/one skip and all six independent installed std differential probes
pass. The shared resource remains consumer-owned; original SDKs are unchanged.
Flat authored short-circuit steps replace a failed nested-expression pattern;
genuine temporary-lifetime RED/GREEN fixes cover true and retained-exception
paths. Expanded hash/neutral/recursion checks added after core GREEN are recorded
as verification, not the test-first increments promised by the plan. This process
deviation remains part of final requirement assessment.

Latest twelve-actor observations at approximately 10:31Z estimate $43.3339886
Standard API-equivalent USD, about 6h54m from original GO. Cumulative input is
222,137,545 tokens, including 217,841,664 repeated cached input. Output is
1,105,657 tokens including 588,625 reasoning tokens. Actual billing is unavailable.
Stage C has begun; this is not a completed-product cost or performance claim.

Product Stage A was independently verified and committed at
`9fdcd7cfa8c8bea4e343965f48dab7ed9382e30a` on 2026-10-12 around 09:39Z.
Its three-minor source suite and six isolated installed owner probes pass the
bounded core subset. See `Dataclass-StageAResult.md`; full completion remains
ahead. The operator had to ask why work stopped after status replies; the owner
acknowledged incorrectly ending active turns and resumed the existing GO.
This is additional intervention, not an uninterrupted one-shot success.

Latest twelve-actor observations at 09:39Z estimate $38.607173 Standard
API-equivalent USD, approximately six hours after original GO. The cumulative
194,894,321 input tokens include 190,959,488 repeated cached input; 993,275 output
tokens include 527,280 reasoning tokens (a subset, not added again). Actual
billing remains unavailable. Stage B comparison generation is now in progress;
these figures include historical detours and are not completed-product cost.

The run includes compact detailed design, a separate TDD plan, native YIDL-generated
Dataclass implementation, real Undoable comparison integration, canonical goldens,
independent reviews, correctness/performance/declarative evaluation, package checks
and final evidence. No operator approval is required at intermediate design or plan
checkpoints. Bounded remediation may exceed two cycles; architectural failures
require redesign before continuation. No remote creation or publication of the new
member is inferred from implementation authorization.

Baseline Dataclass documentation HEAD at go-ahead:
`d0cc37c061efb8b02bd126e547c01eb87baa904f`, verified against Git. Undoable baseline:
`f79e4ce6d985ed0a6463552e163baabf1a28942d`. Its existing modified checkpoint and
untracked `UndoableLeaf.md` belong to a paused unrelated change and must remain
uncommitted and untouched by this run.

The round-2 GO reports apply to their exact historical object. The subsequent
locality amendment is operator-accepted rather than independently re-reviewed.
See `DataclassSpec-OperatorAmendment.md` for the explicit override and remaining
regression obligations. No architectural root cause was reported in either round.

## Measurement limits

Review-stage sanitized token observations are retained separately from implementation
metrics. Counter deltas use the last observed cumulative sample before the recorded
review baseline for the owner; fresh reviewers have their own independent baselines.
Reasoning output is included in output totals, not counted again. Cached input is
repeated request context, not unique source volume.

For the earlier requirements-review stage, actual billing is unavailable and no
cost estimate was calculated or claimed.
Any later estimate must verify applicable dated model rates and request conditions;
the first experiment's rates must not be assumed automatically. A completed-stage
sample cannot include subsequent owner output. Formal design/implementation start
times were unset at requirements-review close; the subsequent go-ahead above
starts design. This ledger does not label requirements review as implementation.

## Autonomous usage and pricing basis

Autonomous-run observations are written to `experiment/usage.jsonl` by
`experiment/record_usage.py`, with each actor's own baseline at the go-ahead.
Aggregate only the latest observation for each disjoint actor/segment, not every
checkpoint's cumulative delta. Preserve missing coverage and counter resets rather
than turning them into zero or negative usage. Reasoning output remains a subset
of output and is not added twice.

Historical actor labels `owner` and `lane-owner` identify the same session;
`design-drafter` and `dataclass-drafter` likewise identify one continuing worker.
Normalize those aliases before selecting the latest observations. There are six
disjoint actors at design acceptance, not eight. Raw rows remain unchanged for
audit; future samples use `lane-owner` and `dataclass-drafter` consistently.

Standard API-equivalent prices checked on 2026-10-12 in the
[official GPT-6.1 Sol documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol):
$2/M uncached input, $0.10/M cached input, $2.50/M cache writes, $10/M output.
This is an explicit Standard, ordinary-context estimate; actual service-tier,
regional/tool charges and Codex billing are not established. The recorder checks
observed request sizes against the 272K ordinary-context limit; otherwise it leaves
the estimate unavailable unless complete per-request counters support pricing
each request separately. Above 272K input, the official rates multiply input and
cache charges by 2 and output by 1.5 for the full request. Duplicate cumulative
observations are ignored; a gap that cannot be reconciled to the reported last
request makes that estimate unavailable. At the comparison-redesign checkpoint,
the owner log's changed samples all reconcile exactly; its updated estimate uses
those per-request rates. Actual billing remains unavailable.

## Declarative desk checkpoint — 2026-10-12T15:27:49Z

Elapsed since original GO is approximately 11 hours 51 minutes. Stages A–G and
the independent public-documentation authoring exercise are complete; performance
harness preparation and final implementation reviews remain. The desk report
preserves missing corpus/calibration inputs instead of assigning an overall
declarativity grade.

Latest disjoint-actor observations (13 actors, historical aliases normalized) sum
to 360,321,069 input tokens including 353,624,448 cached input, and 1,859,650 output
tokens. Reasoning output 1,022,577 is a subset of output. Standard API-equivalent
estimate is **USD 70.3599266**; actual billing remains unavailable. These are
cumulative observations including the SDK detour, waiting/coordination and
document work, not just implementation or a finished-run cost. The held-out
author actor contributes USD 0.249136 at its preserved phase-end observation.
Owner/drafter counters are sampled during active work; later output is not yet
included. Raw sanitized counters remain in `experiment/usage.jsonl`.

## Performance measurement start — 2026-10-12T15:46:20.378291Z

The owner-verified definition/source freeze is committed at
`f49b9ec6de476271e7193c99b38af196fed3b49a`. Native measurement started serially
with Python 3.12 process 1; no reviewer/other task agents are running CPU-heavy
work alongside it. The full fifteen-process sequence preserves journals and
failed attempts. Definition digest is
`668c864ea59b976a950557ab9d608e351eae9b0aa7e3ef84e2c59f5046191983`.
Product and original dependencies remain unchanged. Approximately 12h09m since
GO is wall elapsed, including historical detour, intervention, verification and
preparation; it is not timed generator cost or measured active coding time.

## Cold sampling correction — 2026-10-12T15:57:57.981879Z

The owner controlled-interrupted the first v1 parent after 697.603588 seconds.
Its journal retains 2,757 first-worker observations and all completed aggregate
rows; this is not a successful full process sample. The self-imposed accumulated
20ms cold method selected40/80 stdlib workers per batch, multiplying external
startup/provenance cost across the planned matrix. `ColdSamplingAmendment.md`
records the bounded cold-only correction and its necessity/provenance. Ordinary
20ms calibration, sample/process counts and performance thresholds stay intact.
No failed threshold, product bug or missing compiler facility was inferred.
V1 source/raw observations remain distinct from the planned H2 dataset; the
original experiment start and cumulative cost/time are unchanged.

## Revised measurement start — 2026-10-12T16:10:09.487589Z

H2 source/definition freeze is committed at
`fc5a47fd325c8a2ad01fb87b120e5319ce38ab1c`, definition canonical SHA256
`c4226335a0ecef51dc52b23906be2594deb68f2d226878c5ad45d2c2e900fc39`.
The revised sequence uses original installed G consumers/SDKs with no concurrent
CPU-heavy task agents. First complete Python 3.12 and 3.13 process durations are
260.755524 and 233.652457 seconds. Each validates the complete 132 timing cases,
3,960 aggregate timing rows and 32 memory observations. These are sample-coverage
successes, not aggregate numerical performance conclusions. Full parent process
sets remain pending; the original v1 interrupted observations stay excluded.
