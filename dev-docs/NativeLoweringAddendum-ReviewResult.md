# Native structural lowering design acceptance

Status: **accepted at yidl-dataclass `1f1bc534b460753e8cd91230e5349ea802c90b5c` after both independent reviews reported GO with no findings.** This accepts the addendum as the P2 architecture only; it accepts no prototype code, native parity, package result, performance or product completion. The reviewed document retains its proposed snapshot header; this result records the subsequent acceptance.

The Consistency and Safety reports are preserved verbatim as
`NativeLoweringAddendum-ReviewConsistency.md` and `NativeLoweringAddendum-ReviewSafety.md`.
Both independently identify the earlier prerequisite sufficiency assumption as an
architectural gap: a restored module/package does not lower the retained Builder
shell language or preserve full lexical hygiene. Both found the new required
module finalizer, native pre-expansion and pure-planning/Rust-mutation boundary
coherent against the actual owning source. No architectural finding remains open
on this document and no remediation review was required.

## Exact reviewed tuple and inspection boundary

| Owner | Revision |
| --- | --- |
| yidl-dataclass | `1f1bc534b460753e8cd91230e5349ea802c90b5c` |
| astichi | `4a62b093498dae7b6d346306eae23e5925aaa004` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl-cache | `a4ae595e0f9835a86dadec3bedebd383ebf9ae2f` |

Addendum SHA256: `0aff58c92dd6da67f6011c12ed33e29ece719260e4e15fa3fc52d4e23bf7f639`.
Committed supporting manifest SHA256: `2ae8318e5ab85dac81b6d2c3a6c167f88cadf0793dd42d4167d452f440ebcf17`.
The manifest is at `docs/validation/prerequisites/p2-paused-manifest.json`.
Its paths are relative to its owning Astichi repository. Prototype code remains
uncommitted and was inspected only after hash checks. It is not accepted code.
Owner verification covered 25 code/test files, 26 evidence files, three binaries,
nine JUnit documents and 24 raw/sanitized mappings. Reviewers independently checked
the applicable source/evidence hashes at start/end and all six HEADs.

The initial four-backend attempt has 120 failures/52 passes; 51 failures arise
from an over-broad oracle tripwire. The corrected attempt has 78 failures/94
passes: seven remaining oracle-boundary errors and 71 genuine unresolved native
behavior/metadata issues. Append-only classification records preserve these
boundaries. The focused 13-test core GREEN is a scoped fact, not P2 completion.

The two prompts were generated from the review-loop canonical template.
Stored prompts replace the sent originals' machine-specific workspace prefix
with equivalent environment-cwd wording to obey repository path rules. Sent
originals are archived outside version control; role, scope and verdict requirements
are unchanged. No current peer reports or drafter messages were available to reviewers.

## Next action and measurement

Resume sole-drafter P2 TDD under the accepted addendum. Capture genuine failures
and same-target successes for bounded native phases, preserve canonical expected
outputs, and stop at the full P2 gate for owner verification. Any new architectural
failure requires redesign before proceeding. Product Stage A remains behind P1–P4.
No release, publication, tags, remotes or unrelated edits are authorized.

Latest observations across ten disjoint actors estimate approximately **$27.06
Standard API-equivalent USD**, about four hours from the 2026-10-12T03:36:48Z GO.
Actual billing is unavailable. Approximately 133.7M cumulative request input tokens
include 130.8M repeated cached input; 707,906 output tokens include reasoning.
These are observed cumulative counters, not unique source volume or a completed
product cost. Raw usage rows and actor alias handling remain in the experiment ledger.

## Subsequent evidence-classification erratum

After documentation acceptance, the sole drafter traced the seven tripwire cases
more closely. Four `provenance_absorb_roundtrip` failures are deliberate oracle
verification. The two `comment_marker` failures and one Python-to-Python
`lifecycle_template_surfaces` failure parse generated commented output inside the
renderer; those are genuine protected-generation defects. The same 78-failure
attempt therefore contains **four oracle errors and 74 genuine native/parser/
metadata defects**, superseding the earlier seven/71 partition. The total result,
original outputs, reviewed document and verbatim reports remain unchanged.

The accepted addendum already requires parser-free commented emission and bars
reusing that parse-based renderer. This correction does not revise its architecture,
public API, artifact bytes or guards. Owning append-only evidence records the
correction before structural renderer implementation. Architecture GO is retained;
these failures remain open implementation obligations.
