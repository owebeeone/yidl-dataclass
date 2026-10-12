# YIDL Dataclass preparation and review ledger

Status: autonomous Dataclass run authorized; operator has excluded SDK changes.
Compiler detour stopped and preserved; consumer design correction precedes Stage A. The original
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

## Autonomous scope and intervention rules

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
