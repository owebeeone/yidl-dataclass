# Dataclass Stage B owner checkpoint

Stage B is owner-verified as a partial product checkpoint. Final independent
implementation acceptance and Stages C–H remain outstanding. Scope is Dataclass
only; no SDK or Undoable implementation belongs to this checkpoint.

The shared authoritative `yidl/shared/comparison.yidl` and inherited Dataclass
adapter generate repr, equality, ordering and hash methods. A separate neutral
adapter reads nested operands without Dataclass metadata. Rich canonical examples
contrast per-field participation and removal, local/inherited methods, empty
operands and representation. Frozen hash action selection is checked mechanically;
actual frozen storage remains Stage C.

All six final source runs have 86 passed and one intentional Field.doc skip:
CPython 3.12.12/3.13.12/3.14.3 with explicit Python/native-rust backends. The owner
built the stopped consumer wheel and independently installed it in three external
original-SDK environments. Six isolated std differential probes pass, checking
repr/recursive repr, equality/order/hash, excluded fields, signatures/method
selection, exact-class rejection, local equality preservation, version-specific
shared operands and temporary release with a retained exception traceback.
Selected backend and absent fallback are asserted, not inferred from the request.
Installed regeneration also passes on 3.12 under both selections. Probe/results
are in `docs/validation/stage-b/owner_installed_probe.py` and
`owner-installed-results.json`.

The owner checked all 203 manifest file hashes, parsed 39 JUnit artifacts and
verified every raw hash reference from 65 increment rows against the external
archive (87 distinct hashes). No machine-specific filesystem paths appear in
owned files. The original attempts and classifications remain auditable.

## Faithful source composition without SDK changes

Nested expression-tail bindings failed in a chosen original-SDK resource pattern.
The equivalent authored flat prefix evaluates each comparison once, truth-tests
once, returns the original false-y result, and returns the final raw result
without testing it. A finally block releases each prefix temporary before the
next read and on exceptional exits. Genuine b11/b12 RED/GREEN tests establish
observable lifetime corrections; the owner independently confirmed the exception
case against std before the fix and against the installed product after it.
This preserves the public standard behavior without making literal BoolOp nesting
an SDK prerequisite. Constant-True expression carriers compile away; the bytecode
projection normalizes only the 3.14 LOAD_FAST/LOAD_FAST_BORROW ownership choice.
No comparison helper, dynamic method-source emitter or consumer AST repair is used.

## Process limitation and next action

The full hash table, neutral override, recursion/local-method and expanded source
checks were added after core GREEN. They are verification, not separate test-first
increments promised by the plan. This deviation is recorded and not waived or
retroactively repaired; final reviews and experiment results must assess it.
Subsequent new facilities require real preimplementation tests.

Next: Stage C provider DAG, conversion/validation, const/frozen/local and pseudo
fields with specialized direct access. Lazy lifetime, inheritance/copy, actual
Undoable reuse/context semantics, full installed/public-only checks, benchmarks
and final independent reviews remain unfinished. There is no performance or
uninterrupted one-shot success claim.
