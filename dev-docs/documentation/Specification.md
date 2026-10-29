# Public documentation specification

## Scope and provenance

The requested outcome is an end-user documentation set comparable in detail to
stdlib dataclasses documentation, following the successful Lifecycle documentation
approach. Deliverables are the README, progressive public pages, full reference,
troubleshooting, complete runnable examples, contributor guidance, this scope
specification and independent docs-only build/deployment configuration.

Permitted changes are documentation, supporting examples, MkDocs configuration,
documentation requirements/helpers/workflow and ignored documentation output in
`yidl-dataclass`. Library implementation, generated source, SDKs, package metadata,
packaging inclusion lists and package-release workflows are outside scope.
Astichi, YIDL, Lifecycle and Undoable are reference-only; Lifecycle's proven site
configuration and helper design supply the documentation pattern. No source or
API changes in those projects are prerequisites for these deliverables. No
commit, push, Pages settings change or deployment is performed by the author.

## Reader outcomes

A reader should be able to install a supported published package, construct and
inspect an ordinary model, choose field families, express dependent initialization
with named providers, apply conversion and validation, delay/reset lazy values,
select immediate or runtime freezing, reason about partial freeze failure, and
choose replacement versus state-preserving copy. The reference must retain
precise callback arguments, option defaults, accepted/rejected combinations,
helper interoperability, inheritance limits and exception contracts.

Preserve existing API and generation page paths and existing example programs.
Add learner guides rather than making implementation/review history the first
thing readers encounter. The stdlib documentation is a detail benchmark, not a
required layout. Callback conventions must be specific to Dataclass: named
factory providers include `cls=type(self)`, optional unknown arguments retain
defaults and positional-only arguments work; converter/validator/freeze callbacks
receive values positionally.

Runtime freezing is essential coverage: permanent opt-in setup-to-freeze,
field-local callbacks and typed-child inference, shallow restrictions, no rollback,
partial failure/retry, lazy materialization, copy preservation and unchanged hash
selection. Distinguish it from `frozen=True` and from transaction systems.

The user supplied the motivation for rejecting `__post_init__`: manual coordination
of inherited hooks can duplicate/omit shared initialization, particularly in
incorrectly coordinated diamonds. Explain declaration/dependency composition
without claiming cooperative Python MRO cannot work, arbitrary multiple generated
bases are supported, or a factory runs once forever. Explicit input bypasses a
factory and lazy evaluation/reset has its own lifetime.

## Verification and publication boundary

Execute all standalone examples and every complete guide block against installed
published 0.1.1 using CPython 3.12 and `ASTICHI_LOWER_ENGINE=python`. Record actual
package origins and check results in the task handoff. This is a documentation
verification, not a fresh library version/backend acceptance claim.

Build with strict MkDocs validation. Inspect the built site's local links,
anchors, assets, repository base path and search. Exclude `docs/validation` and
all development/history records from site output and search. Keep docs dependencies
pinned, action references pinned, and the package-release workflow untouched.
Pull requests build without deployment; canonical-repository `main` builds can
publish only after checks, using the same Pages policy as Lifecycle.

A separate independent adversarial review must assess technical accuracy,
learnability, callback contracts, freeze semantics, rationale wording, stable
URLs, runtime examples, scope/provenance and deployment boundaries before the
parent handles publication. A successful local build is not deployment or review
approval.

## Recorded limitations outside this scope

The package currently bundles a selected public-documentation subset rather than
all progressive site pages. The existing inclusion list in `pyproject.toml`
confirms that. The complete guides are available in the repository/site; changing
wheel/sdist inclusion is a packaging follow-up and does not block this site.
No implementation or packaging change is authorized by documenting this finding.
