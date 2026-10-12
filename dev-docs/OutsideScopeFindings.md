# Findings outside the Dataclass implementation scope

These observations do not authorize SDK work. Astichi evidence refers to original
revision `1c47f781d3804130fdd61cbee07a3b2e4529158a`; YIDL evidence refers to
`9d374f88445c426a56d5dd1f96fad112d1ec5417`. Source paths below are relative to
their named owning repository. Prototype defects from the stopped detour are not
presented as defects in those original dependencies.

## Complete persistent template restoration

- Classification: confirmed missing facility, not a demonstrated violation of
  the existing APIs' contract.
- Evidence: original Astichi `native_engine/src/occurrence_store.rs`,
  `parse_template_snapshot`, constructs metadata with `package_v2: None` and
  `module: None`. Existing provenance/final-AST caching is distinct from loading
  a complete unresolved composable. The prior compiler design records the API
  inspection; it is historical, not active scope authority.
- Impact: the chosen persisted, parser-free template route was unavailable.
  Existing source-based generation remains available and passes the original-SDK
  feasibility probe.
- Suggested improvement: a separately scoped compiled-template save/load API if
  a future use case requires persisted unresolved templates.
- Blocks the requested Dataclass outcome: **no**. Direct slots and specialized
  methods do not require persistent template restoration.

## Source parsing inside supported generation

- Classification: confirmed implementation characteristic and possible
  optimization opportunity; no measured regression or contract defect established.
- Evidence: original YIDL `src/yidl/generation/matcher_values.py`,
  `MatcherGeneratedValue.to_generator`, lazily compiles source and caches the
  composable. Original Astichi `native_engine/src/materialize_ir.rs` uses
  `parse_expression_module` for external expression overlays.
- Impact: generation can parse source; this does not add indirection to the
  resulting instance field accesses. Generation cost remains a benchmark subject.
- Suggested improvement: evaluate structural resource/payload paths only if
  measured generation cost or another authorized use case justifies them.
- Blocks the requested Dataclass outcome: **no**. The original generation route
  is supported and the template compilation cache already exists.

## Expanded example ordering binding collision

- Classification: confirmed failure of an expanded reference fixture; general SDK
  defect and required correction are not established.
- Evidence: the earlier original-SDK probe enabled ordering and unsafe hashing in
  YIDL's `tests/data/yidl/dataclasses_example.yidl`; Python selection failed at
  `SelfLeOrderContribution` because `field_name_text` was already queued. Attempt
  history is retained in `docs/validation/baseline/original-sdk-results.json`.
- Impact: that expanded fixture cannot be used unchanged as proof of the new
  comparison generator. Consumer resources can use distinct binding names/ports.
- Suggested improvement: independently assess the reference fixture's naming and
  add an ordering scenario in its owning project only under separate authorization.
- Blocks the requested Dataclass outcome: **not demonstrated**. The product's own
  ordering composition and both consumer cases still require their planned tests.

## Reference binding inside parameter annotations

- Classification: observed limitation of a chosen resource pattern; violation of
  a documented SDK contract is not established.
- Evidence: the drafter's Stage A setup attempts found global `astichi_ref` calls
  remaining in parameter annotation payloads with original Astichi 1.1.3.
  Existing identifier demand/binding sites correctly emit captured annotation
  and default names. Attempts are retained in `docs/validation/stage-a/`.
- Impact: the consumer uses existing identifier bindings for captured parameter
  expressions and reference bindings for direct attribute reads/stores.
- Suggested improvement: separately document or investigate supported annotation
  reference contexts if needed; no SDK patch is part of this task.
- Blocks the requested Dataclass outcome: **no for the observed cases**. The
  existing identifier-binding alternative produced the first canonical GREEN.

## Nested equality expression-tail binding pattern

- Classification: confirmed failure of the chosen consumer resource arrangement;
  a general SDK defect or documented-contract violation is not established.
- Evidence: Stage B attempts in `docs/validation/stage-b/` leave a later child
  `term_path` binding unresolved while assembling nested equality terms with
  original SDKs. `Dataclass-StageBResult.md` records the successful alternative.
- Impact: that arrangement cannot be used unchanged for the version-specific
  comparison sequence. Authored flat prefix statements preserve ordered reads,
  raw returns, truth conversion and temporary release, including exceptional
  cleanup, with no helper dispatch or SDK patch.
- Suggested improvement: separately document supported nested expression/binding
  compositions or investigate the failed pattern under owning-repository scope.
- Blocks the requested Dataclass outcome: **no**. Six source matrices and six
  independent installed std differential probes pass the consumer alternative.

## Expression carriers differ between existing backend routes

- Classification: observed source-pattern/backend limitation; SDK contract
  violation and general defect are not established.
- Evidence: Stage B explicit Python attempts reject bare value-form reference
  fragments; tuple funcargs carriers have different lowering behavior from the
  native route. The existing authored `direct_ref if True else None` carrier
  passes both routes. Its compiled hash operation sequence matches a direct
  reference, allowing only the 3.14 LOAD_FAST/LOAD_FAST_BORROW ownership choice.
- Impact: portable resources need a carrier accepted by both existing routes;
  the constant branch adds no runtime conditional or extra allocation in the
  verified projection. Generation parsing remains allowed by the task boundary.
- Suggested improvement: separately clarify the supported carrier contexts in
  SDK documentation and assess backend consistency with owning tests if desired.
- Blocks the requested Dataclass outcome: **no for the verified cases**. The
  alternative preserves direct reads, and complete Stage B suites pass both
  selections on all supported minors. No SDK work is authorized by this finding.
