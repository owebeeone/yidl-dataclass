# Configurable freezing patch release

Status: preparation for yidl-dataclass0.1.2; no public upload yet. The human
authorized a point release after the paired YIDL/Taut prototype. Scope is this
consumer package and optional Taut Python record integration, not Astichi/YIDL
SDK implementation, shape engines or another Rust foundation release.

The new freeze_method keyword defaults to freeze. It accepts a nonreserved
Python identifier, requires freezable for a custom name, rejects field/method
collisions and requires consistent names in a model inheritance family.
Resolved child inference invokes the child's configured method. Existing field
callbacks, shallow behavior without hooks, optimistic failure, no rollback/thaw,
copying and hashing contracts are retained.

The local prototype passed302 tests with two3.14-only skips on Windows3.13;
the original default freeze regressions and16 new cases pass. Only the common
generated decorator and its formatted snapshots changed in19 golden cases;
model source and behavior expectations are unchanged. This is preliminary
evidence, not complete supported-platform release qualification.

Required release gates: Gearu's complete3.12–3.15 source/regeneration matrix with
both explicit lowering engines and no fallback; strict wheel/sdist checks and
installed examples/regeneration; two peer-blind Code+Surface/State source
reviews on the committed pair; immutable Gearu tag/GitHub Release; terminal
OIDC workflow success; fresh public package and installed configurable-name
consumer. Release this dependency before Taut0.11.2.

Paired controlling DRAFT: Taut's dev-docs/YIDLRecordsPatchRelease-DRAFT.md.
Historical experiment timing, prior reviews, skipped-version reasons and failed
attempts retain their original attribution. No new performance advantage is claimed.
