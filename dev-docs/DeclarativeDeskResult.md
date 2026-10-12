# Declarative desk evidence — Dataclass and shared comparisons

This is a partial **desk** application of the retained
[v3 instrument](reference/DeclarativeApiEvaluatorV3.md), not a calibrated score,
correctness envelope or frontier result. Passing tests and useful declarations
are separate observations. The toolchain is the Stage G consumer tuple:
Dataclass `0.1.0.dev0`, original Astichi `1.1.3`, YIDL `0.1.0`, and the separately
installed Undoable consumer. Product package hashes and supported-minor/backend
verification are in [StageGResult](Dataclass-StageGResult.md).

## Fixed inputs and boundaries

Author class is `llm`; substrate is Python class methods, descriptors and storage.
The ship boundary is installation followed by public construction. Decoration
checks precede construction, but application callbacks can produce effects during
construction/access/assignment. They are not a guaranteed effect-free dry run.
Archetypes are resolution, lowering and templating; RET is the instrument's v1
with its original universal and applicable archetype classes. No new weights or
scalar are introduced.

The pre-author intent selection is
[`intents-v1.json`](../docs/validation/declarative/intents-v1.json): eight canonical
intentions, four public-documentation authoring tasks and two Undoable seam cases.
The [source/oracle freeze](../docs/validation/declarative/source-oracle-freeze.json)
records actual canonical source and generated-artifact hashes. This is **not**
the instrument's minimum 30-intent exogenous corpus. Six calibration anchors,
three calibration-held-out surfaces and blind second-rater score agreement are
not supplied. Correctness masses, completeness cost, expansion ratio, overall
grade and frontier eligibility therefore remain **unscored**. The rubric has not
been changed to accommodate this run.

## Separate surfaces and gate observations

| Surface | Denotation and gate | Gap-owning behavior / boundary |
| --- | --- | --- |
| Class and field declarations | Public API defaults, field inclusion, storage and selected methods; normalized before lowering | Field kinds, class switches and local flags derive specialized slots/properties/methods. Order is explicit: declared field order controls signature/representation/comparison. Inherited merge order is documented. |
| Named factory dependencies | Callable parameter names identify providers; checked DAG and initialization sources | Processed inputs/defaults/providers feed factories in a deterministic dependency order, even when declarations are out of order. Callback bodies are imperative. |
| Authored YIDL generation assets | Typed contribution facts, inherited modules and matching assemble Python operations | Core, policies, providers, lazy/retention/copy and neutral comparison modules use the original supported composition route. This surface has an SDK/capture seam distinct from model declarations. |
| Explicit callbacks | Arbitrary Python functions/callables | Split off as imperative: their bodies are sequences of effects, not inspected declarative descriptions. Signature checks do not prove purity or correct intent. |

For the first three surfaces, programs-as-data and nontrivial expansion have
concrete evidence: immutable harvested definitions, planned factory calls and
steps, authored YIDL resources, and materialized generated-source goldens. They
pass the identification gate by inspection. Dependency order is explicit and
scoped, not inferred from callback side effects. Accessing undeclared state via
an opted-in `self` callback can introduce ambient behavior; that behavior belongs
to the imperative seam rather than being silently credited to the declaration.

The field/dependency surfaces require **scoped** locality: a field can inherit
class defaults or metadata and name providers; the engine reads the containing
class, supported base and named dependencies. Deterministic multi-step derivation
orders providers and determines direct lazy-provider retention. Normalization,
planning, composition and lowering are feed-forward stages. These support the
instrument's L/S/T categories of scoped/derivation/multi-pass for those surfaces.
They do not establish a whole-framework numeric position. In particular, YIDL
matching is not evidence of a runtime constraint optimizer, and a larger locality
span is not a synonym for better authoring locality.

Evidence: `src/yidl_dataclass/dataclass_harvester.py`, `provider_plan.py`,
`policy_plan.py`, `retention_plan.py`, `dataclass.py`, and
`src/yidl_dataclass/yidl/`. `tests/test_source_contract.py` separately projects
direct stores, specialized property bodies, captured callbacks, neutral shared
comparison source and actual operation sequences from the canonical artifacts.

## Locality and deletion are different observations

The operator's rule is field-specific intent on that field declaration, so
removing it removes the policy without cleaning a detached name map. Dataclass
uses field-local `compare`/`hash` flags; Undoable keeps logical `compare` beside the
field and separates managed `write_compare`. Class decorators carry class-wide
booleans. Legitimate named dependencies remain references to other declarations;
removing their provider requires a missing-reference diagnostic.

The independent author produced before/after models with identical
`frozen=True, order=True` options. The final programs differ only by deleting the
cache declaration. The [raw removal observation](../docs/validation/declarative/field-removal-observation.json)
counts 26 deleted lexical Python tokens, using the entire saved programs as its
boundary (including imports, assertions and instrumentation), excluding comments,
encoding/end markers, indentation and line separators. Counts are 343 before and
317 after. There is no separately measured natural-language intent token delta,
so this is neither an E6 ratio nor a corpus median.

`tests/data/gold_src/dataclass_field_removal.py` verifies the generated operands,
metadata and storage removal. Its missing-provider mutant exercises the different
case where a remaining declaration legitimately still refers to the removed
field. A dependency diagnostic does not violate the one-line policy rule.

## R3 vocabulary and interaction inventory

The declared counting unit here is **public construct families plus keyword
names at their declaring API role**, not every Python token or generated method.
The field/class declaration vocabulary has 31 units: seven constructs (`dataclass`,
`field`, `const`, `lazy`, `initvar`, `classvar`, `local_store`), eleven decorator
options and thirteen `field` options listed in `docs/API.md`. A keyword shared
between decorator and field roles is counted once per role. Convenience functions
reuse these options; helpers, Python annotations, arbitrary callback syntax and
the separately evaluated YIDL asset surface are outside this F boundary.

The following 27 documented interaction clauses are an explicit inventory for
that boundary. These are counts of clauses, not all possible combinations:

1. `weakref_slot` requires slots.
2. `order=True` requires equality.
3. Order generation conflicts with local ordering methods.
4. Hash generation combines equality/frozen/unsafe-hash and explicit methods.
5. `hash=True, compare=False` is rejected.
6. Frozen writable fields require comparison/hash exclusion.
7. Defaults and factories are mutually exclusive.
8. Field keyword-only selection overrides the decorator default/fence.
9. Match arguments exclude keyword-only init fields; hidden InitVars cannot satisfy attribute patterns.
10. Const rejects explicit mutable inclusion.
11. Lazy requires a factory and excludes an ordinary default.
12. Hidden InitVar kind excludes ordinary repr/comparison/hash/helper inclusion.
13. ClassVar excludes instance factories and policies.
14. Marker families must agree with pseudo-annotation kinds.
15. Generated-initializer suppression conflicts with extension/policy/provider needs.
16. Named providers beat callable defaults when that provider exists.
17. A named but unavailable provider fails rather than using an optional callback default.
18. Instance factory injection requires `allow_self_factory`.
19. Eager factories materialize lazy dependencies.
20. Conversion precedes validation, storage and dependent consumers.
21. Explicit `converter=None` overrides class conversion.
22. Derived conversion supports exact scalar nullable annotations; other annotations need an explicit choice.
23. Frozen requires slots, while nonfrozen policies permit dictionary mode.
24. Lazy mutability determines override/reset; BUSY state blocks setter/deleter.
25. Direct lazy InitVar consumers retain privately; resettable consumers extend retention lifetime and eager intermediates cut retention.
26. Replacement rebuilds init-false/local/lazy state and requires new hidden inputs under the documented InitVar rules.
27. Inherited override may change policy/defaults but not kind/storage/effective mutability; frozen bases must agree and merged dependencies are rechecked.

This inventory is grounded in `docs/API.md` and corresponding canonical cases
(`dataclass_policies`, `dataclass_initialization`, `dataclass_lazy`,
`dataclass_inheritance_helpers`, `dataclass_comparisons`). Its observed documented
ratio is 27/31. It omits any still-undetected silent U12 mutants and does not cover
the separate generator vocabulary. It is therefore a **partial R3 observation**,
not a completed R3 floor pass or numeric regularizer grade. Classifying callback
behavior as imperative does not erase the need to test its interactions.

## Oracles and containment

R5 evidence is bounded. Canonical plain/comparison/metadata/helper cases construct
stdlib dataclasses independently and compare observations for the compatible
subset, including minor-specific equality behavior. This is stronger than the
designer goldens alone. Extension factories, private retention, writable frozen
exceptions and lazy reset have documented contracts, explicit callback
observations and failure tests, but no independent stdlib implementation of those
extensions. Running both original SDK backends checks divergence; it does not
make two independent semantic oracles. Neutral comparison reuse is a real second
consumer, not proof of all extension semantics.

Dataclass callbacks are visible escapes (`default_factory`, `converter`,
`validator`, and explicit instance injection), and **leaky**: Python bodies may
mutate external state or the model. Field pipelines install only after success;
`tests/test_pipelines.py` covers failures, cause preservation, contract errors and
BaseException atomicity. This does not roll back arbitrary callback side effects,
constitute an ownership fence, or guarantee transactional construction. Private
storage is an implementation boundary, not a security sandbox.

The Undoable write-callback seam is separate. Its native `bool(old == incoming)`
uses original operands within the existing manager ownership fence. An expiring
ContextVar marker selects historical facade equality only during that callback;
structural equality resumes afterward. `tests/test_write_comparison_context.py`
in the Undoable repository covers native reflected/NotImplemented behavior,
truth-conversion failures, captured contexts, cancellation, nested callbacks,
reentrant operations and ownership faults. The existing manager fence is not a
promise to reverse arbitrary external side effects. Seam correctness histograms
remain unscored; Stage EF preserves executed evidence separately.

## Error observations and remaining envelope gaps

Decoration rejects unknown/invalid options, incompatible kinds, missing required
providers, factory cycles, invalid callback signatures, conflicting methods and
unsupported layout/inheritance. These checks address parts of U1/U2/U3/U4/U9/U12
and E-R1/E-R2. Construction/assignment/access can first signal callback conversion,
validation, runtime recursion or unavailable values. Named dependency diagnostics
include the field/path; an annotation alone does not prove runtime value type.

Valid-but-wrong values, wrong units, mistaken defaults, accidental callable state,
and arbitrary escape misuse remain possible (U6/U7/U8/U16/U17 and seam cases).
Python can overwrite a declaration before the decorator sees it; this is not a
deleted duplicate-declaration footgun. Unsupported legitimate intents are coverage
limitations, not deleted errors. Source goldens reveal lowering, but source shape
alone cannot exclude silent semantic mistakes. No per-class RET masses are
assigned from these examples; passing a few mutants cannot justify a universal
pre-ship correctness claim.

## Public-documentation authoring observation

The peer author used only the installed Stage G wheel's public documentation,
signatures and public metadata before implementation review. All four tasks
eventually passed in 276.647023 seconds. Eight executions include three failures:
one incorrect expectation about a replacement cache and two instrumentation
windows which started after decoration. Every attempted source, command, exit,
output and repair is retained in the [author archive](../docs/validation/declarative/public-author/AUTHORING_RECORD.md),
with path-sanitized repository derivatives and original raw hashes identified by
its owned manifest. Neither the initial failures nor the later successes were
used to tune product code. This is an observed cold authoring exercise, not a
few-shot curve, k80, calibrated repair median or message-actionability score.

## Logged conclusion and limits

The declarations demonstrably derive more than a thin wrapper: storage selection,
dependent initialization, retention and field-selected methods are inspectable.
The useful authoring result is backed by executed tasks and deletion evidence.
Correctness evidence has independent stdlib support for the compatible subset;
extensions still depend on their stated contract and targeted checks.

Generated behavior and fixed resource provenance are recorded, but application
callbacks prevent a claim of totality or effect-free determinism. Supported
minor/backend conformance is measured separately from cross-version evolution;
the experimental dev version is pinned and not a migration/deprecation guarantee.
Engine cost and elapsed/token/API-equivalent monetary observations are in the
experiment ledger; actual billing is unavailable. Coverage percentage is not
invented from passing test counts.

All Part E metrics, calibrated C/regularizer aggregates, expansion/corpus ratios,
frontier and overall grade remain unscored. Completing them would require the
instrument's exogenous corpus, mutation accounting and calibration/rater program;
those omissions are explicitly retained rather than replaced with a favorable
score. Independent final implementation reviews assess the concrete product and
these evidence limits separately.
