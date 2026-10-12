# Dataclass specification — SAFETY-AXIS REVIEW

**Review object:** `README.md`, `dev-docs/DataclassConcept.md`, `dev-docs/ExperimentProtocol.md`, and `dev-docs/GoldenExamplesAmendment.md` in `yidl-dataclass` at `0ceb048a98f9e4464366fc1abfb0827888e8fc54`. The concept is the controlling DRAFT. Status: requirements readiness for detailed design; no dataclass implementation exists.

**Baseline:**

| Repository | Verified HEAD |
| --- | --- |
| yidl-dataclass | `0ceb048a98f9e4464366fc1abfb0827888e8fc54` |
| yidl_undoable | `f79e4ce6d985ed0a6463552e163baabf1a28942d` |
| yidl-lifecycle | `230362f642d6e9205897698670fe5f87d2c905ce` |
| yidl | `9d374f88445c426a56d5dd1f96fad112d1ec5417` |

Committed documents and supporting sources were read through `git show SHA:PATH`. Paths below are relative to the named repository.

**Date:** 2026-10-12, Australia/Sydney.

**Axis:** Safety — what the requirements permit to go wrong, including compatibility boundaries, changing values, retained inputs, callbacks, misleading experiment conclusions, and unintended adjacent changes. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — the inherited P2-1 is closed at this requirements gate; no new P0, P1, P2, or P3 finding was established. This accepts the brief’s suitability for detailed design, not an implementation, frozen public API, benchmark result, or billing claim.

---

## Prior-finding closure table

| ID | Disposition claimed | Verified on corrected tree | Status |
| --- | --- | --- | --- |
| Safety P2-1 | Preserve managed-write `compare="value"\|"identity"` and introduce independent decorator `compare_fields` overrides. Require policy/inclusion combinations with structural generation enabled and disabled. | Retraced the original excluded identity-policy field against the pinned marker and managed-write path. The corrected declaration uses `managed(compare="identity")` together with `compare_fields={"cache": False}`; the boolean no longer occupies the marker’s existing `compare` position. `DataclassConcept.md`, lines 72–84 and 101–116, requires separate controls and unchanged assignment policies. `ExperimentProtocol.md`, lines 63–66, carries their independent coverage into the experiment. | **Closed for requirements readiness.** No runtime implementation or executed regression is claimed. |

I replace the original Safety reviewer. Closure follows my independent source retrace and inspection of the corrected requirements, rather than the owner’s disposition alone.

## Changed-range analysis

Comparison against original spec object `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13` established:

- `README.md`, lines 1–18, is unchanged.
- The original comparison proposal in `DataclassConcept.md`, lines 69–75, is replaced by the expanded contract at corrected lines 69–116. This separates transaction write detection from logical inclusion, specifies field eligibility and rejection, records effective decorator defaults, supplies the omitted/explicit option table, and requires independent regression coverage.
- `ExperimentProtocol.md` adds corrected lines 63–66, requiring the decorator-default cases, both transaction assignment policies, logical inclusion, enabled/disabled generation, and the golden-example amendment.
- `GoldenExamplesAmendment.md`, lines 1–38, is a newly included operator requirement. It goes beyond collision remediation by requiring meaningful contrasting examples and inspectable generated source. Its final scope boundary keeps actual Undoable example changes within the future integration and preserves the original experiment and paused helper work.
- The remaining concept and protocol requirements retain their prior substance, with line-number shifts.

The eligibility/defaults contract and golden amendment received a fresh safety attack below. They did not establish an additional defect. **No NEW ARCHITECTURAL root cause was identified.**

## 0. Evidence base

Read at `yidl-dataclass` object `0ceb048a98f9e4464366fc1abfb0827888e8fc54`:

- `README.md`, lines 1–18.
- `dev-docs/DataclassConcept.md`, lines 1–221.
- `dev-docs/ExperimentProtocol.md`, lines 1–115.
- `dev-docs/GoldenExamplesAmendment.md`, lines 1–38.
- `dev-docs/CurrentProgramCheckpoint.md`, lines 1–58.
- `dev-docs/DataclassSpec-ReviewSafety.md`, lines 1–112.
- `dev-docs/DataclassSpec-RemPlan.md`, lines 1–23.

Read the original object at `3bea8349c6d4d20ba670c0edcf0403bb4ba20a13`:

- `README.md`, lines 1–18.
- `dev-docs/DataclassConcept.md`, lines 1–180.
- `dev-docs/ExperimentProtocol.md`, lines 1–111.

Read pinned supporting sources:

- `yidl_undoable` at `f79e4ce6d985ed0a6463552e163baabf1a28942d`:
  - `docs/API.md`, lines 1–137.
  - `src/yidl_undoable/undoable.py`, lines 1–76.
  - `src/yidl_undoable/undoable_markers.py`, lines 1–33.
  - `src/yidl_undoable/facades.py`, lines 1–328.
  - `src/yidl_undoable/values.py`, lines 1–133.
  - `src/yidl_undoable/transaction_yidl.py`, lines 585–635.
  - Committed `dev-docs/CurrentProgramCheckpoint.md`, lines 1–73, as supporting scope evidence; its working-tree revision was excluded.
- `yidl-lifecycle` at `230362f642d6e9205897698670fe5f87d2c905ce`:
  - `AGENTS.md`.
  - `dev-docs/README.md`, lines 1–65.
  - `src/yidl_lifecycle/lifecycle_markers.py`, lines 1–245 and 335–430.
  - `src/yidl_lifecycle/yidl/lifecycle_const_static.yidl`, lines 1–125.
  - `src/yidl_lifecycle/yidl/lifecycle_default_factories.yidl`, targeted lines 89–145, 188–278, and 396–472.
- `yidl` at `9d374f88445c426a56d5dd1f96fad112d1ec5417`:
  - `tests/data/yidl/yidl_update_a_dataclasses_split/dataclasses_base.yidl`, lines 1–165.

Read workspace `AGENTS.md` and `AGENTS_GWZ.md`, the supplied control-flow instructions, and local process authority `review-loop/SKILL.md` and `review-loop/references/review-prompt-template.md`.

Commands were read-only: `cat`, `rg --files`, `nl`, `sed`, `git show`, `git rev-parse HEAD`, and `git status --short`. No tests, builds, writes, or Git mutations were performed.

All four HEAD values matched the supplied tuple at both start and end. The dataclass working tree was clean at both checks. Neighboring working-tree changes were unchanged and excluded. No current-round peer report was read or requested, and no other reviewer was contacted.

## 2. Invariant analysis

### Transaction comparison and logical inclusion remain independently expressible

The original counterexample required an identity-policy managed field excluded from object comparisons. At the pinned Lifecycle SHA, `lifecycle_markers.py`, lines 169–193 and 411–412, reserves `compare` for `"value"` or `"identity"` and rejects a boolean. Undoable re-exports that marker in `undoable_markers.py`, lines 3–18. Its managed-write path uses the same fact at `transaction_yidl.py`, lines 607–616.

The correction leaves that contract intact. For each assignment policy, `compare_fields` can independently include or exclude the managed field. Corrected concept lines 111–116 require distinct equal values to record replacement under identity policy, same-reference writes to skip, and excluded fields to affect neither equality nor ordering. They also require the policies to remain unchanged with structural generation enabled or disabled.

The original boolean-marker rejection and metadata-reinterpretation sequences therefore no longer follow the advertised requirements. This is requirements closure; implementation must later demonstrate the specified behavior.

### New comparison defaults do not silently replace identity behavior

Pinned `facades.py`, lines 153–157, implements equality by shared node state and hashing by manager identity plus node ID. Corrected concept lines 86–99 preserve this as the effective default:

- Bare and empty-parentheses decoration disable structural generation.
- Explicit `eq=False, order=False` has the same result.
- Equality and ordering require explicit compatible opt-in.
- `order=True` alone rejects because omitted `eq` remains false.

Thus existing bare declarations are not required to acquire value equality, changing hashes, lazy materialization, or field-comparison callbacks. The pinned decorator does not yet support the new syntax; concept line 111 expressly identifies it as proposed rather than implemented.

### Selection excludes private and ambiguous storage

Corrected concept lines 77–84 define inclusion defaults for ordinary, const, static/lazy, managed, and binding fields. Initialization-only providers, class variables, transient fields, and local storage are excluded. Inclusion attempts for those families, unknown names, and nonboolean overrides must reject at decoration.

I attacked an initialization provider included to expose a retained secret, a transient field included to compare incompatible state views, and a misspelled exclusion that would otherwise leave a cache included. Each conflicts with the explicit decoration-time rejection contract.

Eligible values may still be mutable, unorderable, or callback-bearing. Eligibility does not claim universal ordering success or hashability; consumer-specific type/view rules remain required at concept lines 62–67 and 118–121.

### Hash keys after mutation or history movement remain a design obligation

The concrete unsafe sequence is: hash an object as a dictionary/set key, mutate a participating value or move Undoable history, then attempt lookup after its structural hash changes.

The brief does not require retaining identity hashing alongside structural equality, nor does it promise all opt-in comparison classes remain hashable. Concept lines 62–67 require equality/hash consistency; lines 118–121 require explicit rules for changing facade values; lines 172–175 require lazy hash-stability rules. A design can reject unsafe combinations or make changing objects unhashable without contradicting the brief.

A related attack is a managed frozenset containing nodes whose newly enabled structural comparison makes them unhashable. Pinned `values.py`, lines 68–78, decodes such contents into facade frozensets. That integration requires an explicit collection/hashability decision. The requirements do not force unchanged collection support for every opt-in structural mode, so this is a mandatory detailed-design question rather than a newly established requirements defect.

### Retained initialization providers have an explicit privacy and lifecycle boundary

I retraced the sequence where two lazy factories share an initialization-only input: the first materializes, cleanup discards the provider, and the second later fails. Concept lines 136–140 require private retention and an explicit retention/cleanup/copying rule; lines 172–175 require providers to remain available for delayed factories.

I also attacked retaining a mutable provider, mutating it between lazy reads, and copying an instance before all dependent fields materialize. Snapshot-versus-reference semantics and copying remain explicitly open. Those choices need resolution, but the brief does not falsely promise snapshot behavior.

Private providers must remain outside normal field access, representation, equality, and serialization. The comparison amendment reinforces their exclusion. No requirement authorizes exposing retained inputs in generated behavioral output or ordinary serialization.

### Failed conversion, validation, and lazy callbacks do not install a successful target

Concept lines 144–149 require conversion and validation before installation or provision to dependent factories. Lines 167–175 require successful lazy results to be cached and failed targets to remain unset for retry.

I attacked a converter failure after a factory returns, a validator failure before a dependent factory runs, and recursive lazy access during a callback. The first two have a clear required noninstallation boundary. Recursion, dependency cycles, callback behavior, and diagnostics require detailed rules and tests.

Arbitrary external callback side effects are not promised to roll back. The brief therefore does not assert transactional recovery it cannot provide. Its safety acceptance remains conditional on the later design specifying supported reentry and retry behavior.

### Cache mutation does not have to change logical equality or hashes

Concept lines 153–163 allow writable exceptions in frozen classes, require cache exclusion from equality/ordering and hashing, and distinguish replacement from mutable contents. Lines 34–38 and 167–170 require read-only fields to reject public replacement/deletion while permitting internal initialization.

The cache-mutation attack does not establish a contradiction: a cache can be writable while excluded from logical comparison. The text makes no recursive immutability claim. Hash policy for explicitly writable logical fields remains a separate detailed-design obligation.

### Direct slots and policy enforcement are compatible requirements

Concept lines 28–47 reserve direct public slots for ordinary writable fields and permit specialized properties for fields requiring conversion, validation, lazy, constant, or frozen behavior. Actual callbacks and failure guards remain runtime work.

The requirements do not force assignment validation through an unmediated ordinary slot. Protocol lines 80–87 also separate ordinary-slot measurements from policy-bearing access and separate first lazy access from cached reads.

### Golden examples improve inspection without authorizing adjacent runtime work

The amendment requires contrasts among field policies, dependencies, eager/lazy initialization, comparison inclusion, class compatibility, and conversion/validation. Lines 30–34 require readable generated source paired with canonical behavioral output where supported, reusing canonical scenarios rather than duplicating success assertions.

These requirements expose the selected operands and access paths; they do not establish correctness by source snapshots alone. The protocol retains differential, extension, failure, installation, and public-documentation checks.

Amendment lines 36–38 constrain existing Undoable example changes to the planned integration and explicitly preserve the original measurements and paused helper work. No immediate neighboring runtime edit is authorized by this requirements review.

### Experiment evidence cannot legitimately substitute unlike costs or paths

Protocol lines 73–94 require equivalent inputs, the same interpreter/machine, standard default and slotted baselines, separate extension results, setup outside steady-state measurements, repeated runs, variation, and retained raw evidence.

Lines 98–115 separate stage timestamps, active work from elapsed time, actual billing from estimates, missing usage from zero, and cumulative counters from independently attributable observations. Lines 14–17 require interventions and remediation to be recorded.

These boundaries defeat the attacks of counting preparation as implementation time, omitting reviewer costs while claiming complete totals, presenting cached lazy reads as first-access performance, or using the original Undoable experiment as the new integration’s evidence. No actual performance or cost conclusion is asserted.

## 3. Risks and next action

The detailed design must resolve facade view/type compatibility, hashing and managed collection behavior under structural equality, comparison callback/reentry rules, lazy cycles and retries, retained-provider cleanup/copying, frozen inheritance, and assignment-time conversion/validation. These remain explicit design obligations rather than additional findings against this brief.

The single next action is for the lane owner to file this report and merge the independent round-2 verdicts on the exact tuple. If both axes return GO, proceed to detailed design and its review; this verdict does not authorize implementation acceptance or publication.