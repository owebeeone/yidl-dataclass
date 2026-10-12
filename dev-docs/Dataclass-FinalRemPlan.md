# Final implementation review — remediation round 1

Status: **bounded consumer remediation authorized; acceptance pending**.
Original reviewed tuple: Dataclass
`f6c1c561c1670fc26b19da09537fc6822140d8d2`; Undoable
`6e7edd17de5b30568f2ffa96dee24fa023dd3061`.
Both complete independent reports are preserved verbatim in
`Dataclass-FinalReviewCode.md` and `Dataclass-FinalReviewState.md`.

## Deliverables and scope

One merged patch corrects execution-name collisions, inherited lazy storage and
the dictionary-mode identity documentation. Editable components are the
Dataclass consumer/resources/tests/docs/evidence and the requested Undoable
comparison integration. Astichi, YIDL and Lifecycle remain reference-only:
no dependency source/resource changes or rebuilds. Workspace configuration,
publication and paused UndoableLeaf work remain excluded. Existing supported
consumer composition facilities are sufficient; neither reviewer requests a
compiler prerequisite or architecture redesign.

## Finding dispositions and closure

| Finding | Disposition | Required closure |
| --- | --- | --- |
| Code P2-1; State P3-1 | Correct the same inherited lazy-ready/busy slot root once. Adopt the blocking Code severity for acceptance. | Filter already inherited flag slots; canonical base/child/grandchild and same-shape override verify slot reuse, first/cached reads, reset/retry, readonly rejection and copy/pickle readiness on all supported minors/backends. |
| State P2-1 | Correct Dataclass result-binding interference with generated globals and callback captures. | Preserve ordinary supported model names and application callback identity; canonical supported-name cases plus narrow collision diagnostics verify copy/deepcopy/state/pickle/hash, callback-free generation and reproducible resource generation on the six-way matrix. |
| State P2-2 | Correct the distinct Undoable builder-local class/view binding collision with historical comparison dependencies. | Retrace both original names; accepted names retain structural comparison and actual distinct-child replacement semantics, or explicitly reserved private names fail contextually before generation. Audit model/view identifiers; retain native dispatch, copied-context expiry and manager-fence checks. |
| Code P3-1 | Correct public identity wording, preserving implementation. | Document replacement for slots=True and mutation/identity for slots=False; preserve an example/assertion for both and verify packaged guide bytes. |

The two axes independently found inherited lazy-slot redeclaration. Their
severity differs, but the observed root and required correction agree.
Dataclass globals and Undoable lexical closure collisions are separate roots;
neither may be marked closed merely because the other was corrected.

## Implementation and evidence gates

The sole drafter writes one patch with genuine pre-correction failing checks
for new behavioral regressions, then the same-target passing checks. Existing
successful tests are verification, never fabricated RED evidence. Preserve
every failed attempt and scope of each correction. Do not edit the original
review reports or historical measurement data.

The supplied external test environments currently lack Lark source and
distribution metadata. Their earlier recorded final smoke passed, while current
regenerator imports fail. Preserve the current failed observation; the deletion
cause is unknown. Create fresh isolated environments from the original pinned
SDK wheels and normal declared external dependencies, without repairing or
rebuilding dependency source. Record exact versions, artifact hashes and origins.
This is environment restoration for verification, not a product prerequisite.

Regenerate consumer output only where the correction actually changes authored
resources. Rebuild both consumer distributions if their bytes change; verify
installed matrices, public resources and shared authority provenance. Narrow
checks may precede the necessary full affected suites. No SDK build is permitted.

H2 timings remain observations of the original reviewed source and wheel tuple.
Do not relabel them as measurements of remediated bytes. Record which families
are invalidated, and use any necessary new measurement as a separately frozen
supplement, never replacement or favorable rerun. Unchanged bodies may retain
their historical evidence with an explicit provenance limitation.

The owner independently verifies, commits one settled remediation tuple, and
asks the same two reviewers to retrace their findings. No finding is self-closed.
If an implementation proposal changes a shared public interface, architecture,
mutation boundary or compatibility rule, stop that proposal and apply the
review-loop redesign/fresh-pair rule before proceeding. The operator permits
extra bounded rounds; architectural failure requires redesign first.
