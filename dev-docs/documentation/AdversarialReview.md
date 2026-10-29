# Adversarial review of Dataclass end-user documentation

Date: 2026-10-29.

**Verdict: GO for the reviewed documentation candidate identified below.** No
blocking findings remain. One confirmed installation/support overclaim was
corrected during review before this verdict. This is documentation acceptance,
not certification of a new library implementation, platform or live deployment.

## Scope and requirement provenance

The user requested Dataclass end-user documentation using Lifecycle's successful
format and stdlib dataclasses as a detail benchmark, plus the supplied rationale
for avoiding manually coordinated post-init initialization. The reviewed
specification records progressive guides, complete examples, precise references,
site verification, and documentation-only deployment configuration.

The editable delivery boundary is this repository's documentation, examples,
site configuration, docs workflow and helpers. Library/generated implementation,
SDKs, package metadata/inclusion lists and package publication remain
reference-only. Lifecycle and Undoable were not modified or reviewed as
implementation dependencies. No broader implementation change is required for
the requested result. This reviewer authored only this report and performed no
commit, push, deployment or release action.

The review read repository/workspace instructions, the specification, README,
public guides/reference/generation page, examples, contributor guidance, docs
workflow/configuration/helpers, and relevant Dataclass source. It independently
checked candidate behavior against installed published Dataclass 0.1.1 rather
than treating the author's checks as acceptance.

## Severity-ranked findings

### R1 — P2, resolved: Python version support was presented as universal wheel availability

The initial getting-started text recommended CPython 3.12–3.15, offered Windows
activation, then said installation included SDK wheels and no SDK builds were
needed. This exceeded the existing release evidence:
`dev-docs/Python315Release.md:57–59` and `109–110`, plus
`dev-docs/Python315DependencyFindings.md`, record no Astichi 1.1.3 Windows cp315
or Windows abi3 wheel and an unqualified source-build route. The practical
counterexample is a Windows CPython 3.15 binary-only install: the pinned
dependency's recorded artifact set cannot satisfy it. This is a wheel-coverage
limitation, not proof that a source build fails or a compiler/runtime defect.

The author corrected `docs/GettingStarted.md:22–39` to identify macOS/local and
Ubuntu/CI 3.15 qualification, exclude Windows 3.15 from that qualification, avoid
endorsing an untested source build, and show the checked Python backend setting.
README, index, API, and generation pages now qualify/cross-link the same boundary.
`docs/Generation.md:47–53` and `80–84` also qualify its former no-rebuild claims.
The PowerShell activation command was corrected. Reassessment finds the
remediation sufficient. No dependency or infrastructure implementation change
was authorized or needed.

### Remaining blockers

None established. The following are bounded observations, not publication holds:

- The example checker verifies five complete programs and selected Python guide
  blocks. It does not execute descriptive API signatures or establish every
  reference assertion; source tracing and focused probes supply additional
  evidence. It also does not establish Windows/backend-wide qualification.
- The package's existing wheel/sdist inclusion lists expose a selected document
  subset. The specification and generation guide disclose that progressive
  guides are repository/site content. Broader packaging changes are explicitly
  outside scope and do not demonstrably block the website.
- This review does not claim reader retention improvement, comprehensive
  accessibility testing, or a new platform matrix. A successful site build is
  not proof of deployed hosting or live search behavior.

## Technical and learning review

The introductory sequence is appropriate end-user material: ordinary fields and
inspection precede conversion/validation, named initialization, lazy state, and
permanent freezing. Each guide gives an executable model or a continuation
within its page, with observable assertions. The detailed API remains directly
accessible. This is a learning-design judgment, not a reader-study result.

The no-post-init explanation at `docs/Initialization.md:117–140` preserves the
user's rationale without claiming Python cooperative `super()` cannot work.
It explains duplicate/omitted shared initialization as a manual coordination
risk, then relates declarations to checked dependencies and shared provider
results within the relevant evaluation. It explicitly limits support to one
generated model base plus compatible plain mixins, rejects multiple generated
bases, and distinguishes input overrides and lazy reset lifetimes from a
factory running once forever. Source checks in `inheritance_plan.py` and
`provider_plan.py` support those boundaries. No unsupported arbitrary generated
model diamond is promised.

The callback/reference contracts agree with the inspected implementation:

- Factory binding supports positional-only/ordinary/keyword-only signatures,
  known optional providers, unknown optional defaults, default bridging, runtime
  `cls=type(self)`, and opt-in partial-instance `self`; variadic and unavailable
  provider cases are rejected. The checked dependency plan uses processed
  provider values and rejects cycles before construction overrides.
- Converters and validators receive one positional value. Conversion precedes
  validation; only `None` or exact `True` accepts, exact `False` rejects, and
  another validator result is a direct contract `TypeError`. Failed assignment
  preserves prior field storage, without promising callback-effect rollback.
- Lazy state/retry/reset and hidden-provider lifetime match the generated lazy
  resources and `retention_plan.py`: direct delayed InitVar consumers retain
  providers, eager intermediates cut that path, and resettable consumers retain
  their providers for the declared lifetime. Public helpers may evaluate lazy
  getters; copying preserves state without ordinary evaluation.
- The freezing guide distinguishes immediate `frozen=True` restrictions and
  writable cache/local-store exceptions from `freezable=True`'s later permanent
  restriction of all stored bindings. Runtime freezing visits normalized stored
  fields, materializes lazy values, invokes explicit/inferred policies without
  rerunning the input pipeline, and is shallow without cascading policies.
  Partial failure, completed children, retry, cycle guards, absence of rollback,
  unchanged hash selection, and copy versus reconstruction are stated clearly.
  These match `freeze_generation.py`, `policy_plan.py`, and
  `yidl/dataclass_freeze.yidl`.

The public signatures/options and exact-boolean requirements were compared with
`dataclass_markers.py`, `dataclass.py`, `provider_plan.py`, and related policy
code. The API retains explicit supported standard-helper and inheritance
subsets, rather than promising complete stdlib interoperability. Existing API
and generation URL paths remain in navigation. No unresolved misleading claim
was established in these reviewed contracts.

## Independent execution evidence

The reviewer confirmed installed import origin outside the repository's `src`
tree and metadata versions Dataclass 0.1.1, YIDL 0.1.2, and Astichi 1.1.3 on
CPython 3.12.12. With `ASTICHI_LOWER_ENGINE=python`:

- All five programs and nineteen guide blocks passed the documentation checker.
- Strict MkDocs build and site checker passed: 11 HTML pages, 392 local
  links/assets, and 54 search entries. Whitespace checking passed.
- Focused installed-package probes independently confirmed positional-only
  factory default bridging, a converted named provider, and runtime subclass
  `cls`; invalid truthy validator return produces direct `TypeError`;
  `frozen=True` local storage remains assignable/deletable; runtime freeze blocks
  local-store replacement and leaves default equality models unhashable; copy
  preserves runtime-frozen state; and an inherited `__post_init__` is rejected.

The existing complete freeze-failure and typed-child examples also passed,
including earlier tuple transformation surviving a later hook failure and
successful retry. This is focused documentation verification, not a full new
library regression run or platform/backend release acceptance.

## Site and publication boundary

The reviewed workflow installs the packaged checkout using registry dependencies,
runs executable checks before strict site checking and artifact upload, and
allows deployment only for the named canonical repository's `main`, outside
pull requests, after build success. Actions are pinned by commit. Pages/OIDC
write permissions are confined to the deploy job; the package publishing
workflow is unchanged. Public HTML/search excludes development and validation
records, and source-only repository links are rewritten rather than copied.
No scope expansion to SDK/library/package publication was found.

The workflow/configuration review does not verify GitHub Pages environment
settings or live hosting. Those remain parent-task publication/verification
actions within user authorization, after this review.

## Reviewed candidate identity

Baseline: `f672cac613f116a9b1cddab5739872b4c813f956`.
The manifest below identifies all changed/new candidate files against that
baseline, excluding this report. Unchanged existing examples are identified by
the baseline. The SHA-256 of the literal manifest lines below, each terminated
by LF, is `a656daef86150cd9f1e442f322cdec44cd3b05b0a203d7965bb445e410120df6`.
Any subsequent substantive candidate change requires reassessment.

```text
e1282d4a6a4d0b49ad0f5522c97d7498202d8f3a83395cc093ca4e8a6dc2db3d  .github/workflows/docs.yml
df11686a4d073456dc4d572f696fc99738144940f34971f239e366b7cd5ef464  .gitignore
79eba9e8064a7b5555e728aae74cb73823dde0fed50eac070023215bfc573a1f  CONTRIBUTING.md
4723ddf2a81b4b8707f37d0cfdb7cb5de3574e766ee4e270131a41186faaf490  README.md
1f2bdb4dbdc2bb473dd2fee51d164891b672676d807d8b02ce3e05b2b6a37776  dev-docs/documentation/Specification.md
2af9b3ec6e117c20432b03a4ce9866b915c3602407217c5f8463a2bfd28e3584  dev-docs/documentation/check_site.py
d3b17e95db69314c5d7d37f8c6239f78864f95530a53e8f5dc508426bfd9b006  dev-docs/documentation/site_hooks.py
56995055ba72bdf607106de1234121aa45aecea4ae19e24686e1dac17f5a71b8  dev-docs/documentation/verify_examples.py
dcaede80d4840150535ddacd7723e95b04bd604f12dbf7605dc63acd51dfb182  docs-requirements.txt
7ea95aeef6be3c4200990e86dc085db19bb2f321f8d0ca887fdaad67cf2dcf23  docs/API.md
5d3f8eea751b3d01021b3bf5dfba87aed1f7d94e089d3ead3547d9b56cef4da6  docs/Concepts.md
3b2d591854809475083b766a8ac71b7efc05f1d097d3c2ba61068c0972b401b2  docs/Freezing.md
fa3edbbc29d0f0bc0f7204a0c65658db026e5ef525c90357fc4f260ba2000d70  docs/Generation.md
a1d0dfc1a2f41c1c1b5d01501a890ec66e2c92fdc883540477d15f024a979c0f  docs/GettingStarted.md
1cb4b8d50f60240614930ffb3f93375e987d979caf25ce5986d9f4651485b487  docs/Initialization.md
c8813b04febb757f3c1acde12f83ddea326eed6f05b18930516f15e8d74caede  docs/LazyFields.md
a8cbe3e926fffa044d77960a2373ab9dfa553554f6d0b0193a699fd5f07ede33  docs/ModelOperations.md
57f1c1830f39e4125ffd4f06d7703df0bf54a1b64f526023a78806b554025c6f  docs/Troubleshooting.md
23a427b3f4977587d363dcea275383502b621b082a1423690bdbf24077afaea1  docs/index.md
10081e0ee90e6a6cfbc3b03aa51b503fb45384cfd71f47c4055d55c058a7952b  examples/README.md
0313b34515e051eacd0b31c81eed13e48b45b60061466e3ba242a35db0ecece3  examples/dependent_fields.py
d902fb49415a3015864d1200fb5fbcbed4fc7f41c15c329f9dc246cfc2efc264  examples/freeze_failure.py
37df23d77c3a4c035e69b753c067490e4a2fe84bf95bb62e803be058eb628950  examples/lazy_fields.py
295893823b05d5d10b6a3d5d89a4b1b099000faa514e2775bb108e42ae10b51f  mkdocs.yml
```
