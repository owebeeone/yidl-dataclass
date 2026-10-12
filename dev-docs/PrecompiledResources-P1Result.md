# Python compiler prerequisite checkpoint

Status: implementation verified and committed at Astichi
`4a62b093498dae7b6d346306eae23e5925aaa004`. This verifies P1's Python artifact
and structural frontend only; it is not aggregate Code/State acceptance, native
artifact support, YIDL precompile integration or Dataclass completion.

The sole drafter stopped before owner verification. Its 31-file source/doc/test
manifest and 81 latest evidence hashes were verified; 20 raw archive hashes and
all JUnit documents were also checked. Historical hashes remain with appended
sanitization mappings. The owner removed only the generated documentation site.
Astichi's working tree is clean after the scoped GWZ commit.

| Check | Actual result |
| --- | --- |
| Final full 3.12.12 | 2634 passed, 104 skipped, 27.61s |
| Final full 3.13.12 | 2634 passed, 104 skipped, 36.22s |
| Final full 3.14.3 | 2724 passed, 14 skipped, 38.17s |
| Final artifact/structural/canonical subset, each supported minor | 86 passed, 1 unsupported-minor test skipped; 43 existing canonical source expectations reused |
| Existing source matrix on available 3.15.0a5 | 2547 passed, 192 skipped, 21.52s; new artifact positives explicitly excluded, all three artifact APIs reject this minor |
| Strict owning documentation build | Passed |
| Owner downstream YIDL regression | 299 passed, 2 skipped, 40.11s |
| Owner installed candidate probes, all three supported minors | Origin/version verified; zero fresh source-string compilations during load/bind/materialization; independent ASTs/engines and invalid-shape rejection |

The 3.13/3.14 full suites report 814 legacy provenance-unpickle warnings each;
3.15 reports 30. These source/provenance observations are retained separately
from the new JSON artifact path. No newest-3.15-release claim is made.

Owning exact commands, RED/GREEN/refactor results and archived raw/sanitized hash
mappings are in Astichi's `dev-docs/experiment-evidence/precompiled/p1/`.
Its broad artifact corpus exposed legitimate nullable list entries and the focused
checks exposed context-neutral fragments, invalid identifiers, policy propagation,
custom hooks, large integers, aggregate budgets, exact schema types and lost
composition specialization facts. Corrections remained within the accepted design.

Independent reproduction uses an isolated installation of the recorded candidate
wheel, then `python -I docs/validation/prerequisites/artifact_runtime_probe.py`
from this repository. See `p1-installed-owner-probe.json` for wheel SHA-256 and
interpreter results, and `docs/validation/evidence-index.jsonl` for their hashes.
Normal static module import compilation is allowed only when bytes exactly match
the actual module file; fresh runtime source fragments remain forbidden.

Candidate Astichi 1.1.4.dev0 is unpublished. Its existing native binary has no
`native.compiled_template_artifact.v1` capability and the artifact profile rejects
native selection. P2 must add full native IR restoration and structural payloads,
then P3/P4 must verify YIDL and portable installed behavior before Stage A resumes.
