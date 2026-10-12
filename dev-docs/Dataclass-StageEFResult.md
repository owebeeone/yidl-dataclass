# Shared comparison and native write context — E/F checkpoint

Status: **implemented and independently owner-verified; final implementation
acceptance remains pending**. Stages G/H and final Code/State reviews remain.
Astichi, YIDL SDK and Lifecycle remain reference-only original wheels.
Undoable implementation checkpoint: `bedec080d1d3531d7a250b9e4f729040c57645c7`.

Undoable's stopped full matrix has **340 passed, zero failures/errors/skips in
each of six runs**: Python 3.12.12, 3.13.12 and 3.14.3, each with native-rust
and Python selection without fallback. This includes legacy behavior, richer
comparison goldens, source/regeneration and context/fault tests. Dataclass has
eight affected checks in each combination; its unchanged product retains the
verified D source `23833598e4c7e78d073f20cf152c731fa5bb7bbe` and full D matrix.

The independent checksum/JUnit/path audit verifies Undoable's 256 owned files,
79 increments, 135 artifact references, 120 distinct original raw hashes and
56 JUnit files. Its manifest digest is
`cda9e277c1e57806b2d7be3d64792bf79efde201a0d749c30cf1f798bb60c6a2`;
drafter QA digest is
`752f87b6cedf9b1f4f2ebfe21fd253bd31789ce80b2e14bacb6f620d6a564832`.
Dataclass affected evidence has 260 owned files, six increments and 12 artifact
references/raw hashes, with manifest
`1e0674ab9aa6ceba547c1ca8efe6a0fbaa6886862bf184b5e98d39144a8bfc94`.
Both owner audits are in their respective `docs/validation/stage-ef/` folders.

The owner independently built and installed only the Undoable consumer wheel:
SHA256 `629b590ef1b926c7d8b039f9b12ec51bd320aab6e76182502952cad00215bc07`,
49,241 bytes. Six isolated installed probes pass structural equality and
management exclusion, distinct equal-child replacement plus undo/redo,
identity-write reference distinctions, original opaque equality operands,
closed copied-context behavior and BaseException cleanup. SDK, Lifecycle and
Undoable imports resolve inside each environment. Installed regeneration
matches on both backend selections. The probe and results are preserved in
Undoable's Stage E/F folder. These are bounded probes, not a claim that the
complete installed corpus has already run.

The second consumer uses the actual Dataclass-owned shared comparison YIDL
authority from the pinned D wheel, digest
`2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef`.
There is no maintained copy or Dataclass runtime dependency. Consumer indexed
matching, existing outer-binding markers and an explicit public unhashability
adapter resolve multi-view composition. No SDK change, method-source emitter,
AST repair or recursive payload comparator substitutes for authored generation.
The historical prelude's constant-True statement carrier is eliminated by
compilation; source/bytecode checks verify actual calls, ordering and jumps.

Write detection remains native `bool(old == value)` with original operands
inside the existing ownership fence. A fresh private ContextVar marker stores
only an active boolean and closes before reset on every exit. Enabled Undoable
equality selects the captured historical facade method while it is active;
ordinary structural equality resumes afterward. Identity writes create no
scope; hash/order and snapshot-node policies are unchanged.

Failures and interpretation corrections remain append-only. E's declaration
removal case was authored after core comparison passed: a TDD sequencing
deviation. F's retained-root precondition was corrected, and an attempted
hash-slot RED already passed; both are verification. A separate genuine emitted
hash-name RED/GREEN and the actual rich multi-view Python failures are preserved.
Final assessment must not claim strict all-features-first TDD or an uninterrupted
successful one-shot.

Owner benchmark setup passes 24 integrated/frozen-original seam cases in each
installed combination, without a timing/performance claim. A preliminary D
source-archive rebuild produces the identical D wheel. Stage G still owns the
final installed corpus, public documentation, Dataclass field-removal case and
fresh public-only author; H owns fixed measurements and final reviews.

Latest observations at 2026-10-12T14:16Z total $64.6097148 Standard
API-equivalent USD across twelve disjoint actors, about 10h39m after original
GO. Actual billing is unavailable. The original scope detour, interventions,
failed attempts and process deviations remain included.
