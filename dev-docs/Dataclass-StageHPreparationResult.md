# Performance preparation — owner freeze

Stage H harness preparation is independently owner-verified. **No benchmark
samples or numerical performance verdict exist at this checkpoint.** Product
source, original SDK/Lifecycle wheels and the Stage G consumer artifacts are
unchanged. The sole drafter has stopped writes.

The frozen common definition is
`docs/validation/stage-h-preparation/definition.json`, canonical SHA256
`668c864ea59b976a950557ab9d608e351eae9b0aa7e3ef84e2c59f5046191983`
(file SHA256 `805548ffd088cbbd635667757d6ecf62d655064351aeb63255369b154aeab708`).
It contains 132 timing cases, 32 memory cases, eighteen Python source hashes,
the exact consumer/SDK tuple and all three minors' installed provenance.

The owner independently checks 140 owned files, 60 increment records,
99 evidence references, 81 distinct raw hashes and 33 JUnit files. Seven explicit
sanitization corrections reconcile current derivatives with their preserved prior
derivatives and original raw bytes; they do not rewrite the original records.
The owned manifest SHA256 is
`04cbfce3ae6aa7032669ddb35b40851f618618233b1e0385d10c50c114c7901e`.
The final source map matches the common definition after formatting.

Owner verification runs pass 49 mechanics tests on each of Python 3.12/3.13/3.14.
Independent untimed installed setup runs pass 84 checks each, and their installed
provenance matches the frozen definition exactly. Drafter evidence separately
preserves all eighteen cold-worker setup-only successes. Owner evidence is in
`docs/validation/stage-h-owner-preparation/`; the owner stdout/stderr is in session
tool output, explicitly not claimed as a verbatim on-disk raw archive.

An initial owner setup attempt selected older verification environments without
the pinned yidl-cache package and failed preflight on all three minors. The
already complete Stage G environments pass without an install, source change or
dependency rebuild. This is an instrumentation selection error, not product RED
or a missing compiler prerequisite. The complete tracebacks remain in the session;
the owner evidence records the limitation rather than inventing raw files.

The harness journals completed calibration, warmup, measurement, memory and cold
subobservations outside their timing boundaries. It preserves partial failures and
writes full attempts before late validation; only full validated coverage becomes
a successful process result. Definitions retain 20 ms calibration, 10 warmups,
20 measured batches, five independent processes per minor, 10,000 live instances
for memory and the original statistical targets. No numerical gate was relaxed.

Next: commit this freeze, then serially measure fifteen fresh process attempts on
the quietest available machine. Preserve all raw observations and load/power/build
context, aggregate process medians and report uncertainty/regressions honestly.
Cold calibration counts and resulting wall time are unknown until observed.
Final Code/State reviews follow the settled measured/evidence tuple.
