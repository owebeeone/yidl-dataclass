# Standalone consumer packaging — G checkpoint

Status: **package/installation gates independently owner-verified; cold public
author completed; Stage H/final reviews remain pending**. No final acceptance claim.
Undoable package checkpoint: `6e7edd17de5b30568f2ffa96dee24fa023dd3061`.

The isolated installed corpus passes on each original backend: Dataclass has
197 collected tests, with 194/195/196 passes and 3/2/1 version-specific skips
on Python 3.12/3.13/3.14. Three source-only tests pass separately in each
combination. Undoable passes 341 installed tests with its build authority, and
334 with Dataclass absent; exclusions/deselections are explicitly recorded in
the Stage G README. External test-only trees, -I, original-version/backend and
installed-origin guards prevent sibling/editable source fallback.

The owner independently verifies owned files, raw/sanitized hashes and all
18 installed JUnit results. Dataclass manifest:
`47a42d991de23328a28af92b741c76d048e5694cb63c096945975192677459fd`;
Undoable manifest:
`08592be9180a518cf3c305e8a5a171f965ca3cc8d2019f601b1502c15070456f`.
Owner audits and final artifact inventory checks are in Stage G evidence.

Final wheels reproduce byte-identically from consumer sdists. Independent
archive comparison proves every runtime/resource member unchanged from the
owner's verified D/EF wheels. Final Dataclass wheel SHA256:
`50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b`;
Undoable: `346dcf928dd4bf52362195e1a351b0b716fe03a77ffc7a97b8a5e69310b4281d`.
The final artifact tuple digest is
`e94b6d2991ecf4d15f94b949d1fd8d6a4e290a4ec97829b30129d1d3e41f4434`.
Original SDK/Lifecycle wheels were neither edited nor rebuilt.

Standalone public README, API/generation guides and introductory examples are
packaged with working relative layouts. Six independent owner installed smokes
execute both public examples. The held-out combined solution was not authored.
The eight canonical and two seam source/oracle snapshots are frozen before the
fresh public-only author; designer extension goldens are not independent oracles.

Dataclass declaration removal and expanded binding-isolation goldens already
passed when authored, so remain post-implementation verification rather than
manufactured RED. Actual missing public-package resource RED/GREEN is preserved.
Previous scope detour, interventions and TDD/process limitations remain recorded.

Latest observations around 2026-10-12T14:58Z estimate $67.5929676 Standard
API-equivalent USD across twelve actors, about 11h22m from original GO.
Actual billing remains unavailable. Performance is unmeasured; final
Code/State review has not started.

The fresh Code reviewer completed the four frozen public-author cards before
reading implementation: actual interval 15:02:38–15:07:14.647023 UTC, 276.647023
seconds. Eight card executions include three preserved failures (one incorrect
replacement-cache expectation, two instrumentation-window errors). Final models
pass all requested behaviors without product changes or clarification. Verbatim
originals are content-addressed externally; committed path-sanitized derivatives
are explicitly labeled in `docs/validation/declarative/public-author/`. This is
an uncalibrated usability observation, not an implementation review or grade.
The one-line cache declaration deletion removes 26 lexical tokens; complete
before/after programs have 343/317 tokens with layout/comments excluded. The
first author actor observation estimates $0.249136 Standard API-equivalent USD;
actual billing remains unavailable.
