# Dataclass Stage C owner checkpoint

Stage C is owner-verified as a partial product checkpoint. Lazy lifetime,
inheritance, copying, actual Undoable reuse, full installed/public authoring,
benchmarks and final independent acceptance remain Stages D–H.

The consumer implements named provider DAGs, signature validation/default
bridging, construction-scoped InitVars, ClassVars/local storage, conversion,
validation, constants and frozen field exceptions through specialized authored
YIDL. Ordinary writable fields retain public slots; policy properties use direct
private backing slots and captured callbacks. Metadata remains real standard
Field objects with independent ownership and version-specific doc behavior.

All six complete source suites pass 156 tests with one version-specific skip:
CPython 3.12.12/3.13.12/3.14.3 with original native-rust and Python backends.
The skip on older minors is positive Field.doc coverage; the skip on 3.14 is its
older-version rejection test. Source/bytecode/resource/regeneration and prior
A/B regressions are included. The owner independently built the stopped consumer
wheel and ran six isolated installed probes outside the repository. All pass:
processed hidden dependencies, atomic conversion/validation failure, causal
errors, exact validator return rules, readonly fields, writable frozen caches,
unavailable optional known providers and live class-default fallback. Backend
selection, absence of fallback and installed module origins are asserted.
Installed regeneration matches under both selections. One unsupported owner
`--check` invocation is preserved as a CLI setup mistake; the supported default
check invocation succeeds without a product change.

The owner independently verified all 286 manifest hashes, 75 increment records,
123 original/sanitized artifact references, 103 distinct raw hashes and 48 JUnit
artifacts. Owned files contain no machine filesystem paths. The manifest SHA256
is `c9a432c4112d8d151754e4800eafc1f6a47266dc51510a8b965e4f8a6e71f664`;
the installed wheel SHA256 is
`602024966e2b034fb6e484283da06abebeea6aee4ec05f6d523d88ed33fe5d3a`.
Probe, integrity audit and installed results are in `docs/validation/stage-c/`.

New provider/policy behavior has genuine preimplementation RED and same-target
GREEN. Broader C06 source/ownership/packaging checks are labeled post-GREEN
verification. Their fallback finding has a genuine C07 RED/GREEN fix. The prior
Stage B sequencing deviation remains; no strict all-test-first compliance or
uninterrupted one-shot claim is made. The owner dependency-packaging lapse is
recorded separately in the experiment ledger and baseline provenance.

Next: Stage D lazy state, provider retention, inheritance, copying/serialization
and replacement. SDKs remain reference-only; no dependency change is a
prerequisite. No performance, publication or final completion claim is made.
