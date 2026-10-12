# Dataclass Stage B evidence

Status: Stage B product checkpoint prepared for owner verification. Only Dataclass
product/resources/tests/evidence changed; Undoable integration remains a later
stage. Original Astichi 1.1.3 and YIDL 0.1.0 wheels are the runtime dependencies.
No SDK source, build, resource, version or capability change is a dependency.
Stages C–H and performance evaluation remain outstanding.

## Actual increments and preserved attempts

`increments.jsonl` records actual commands, timestamps, elapsed phase times,
interpreter versions, exits, sanitized artifact hashes and original raw hashes.
`corrections.jsonl` preserves classifications without changing historical rows.
The raw archive is external, identified by `external:yidl-dataclass-stage-b-raw`;
raw files are content-addressed by the recorded SHA256. Sanitized JUnit retains
parseable XML with bracket placeholders for machine identifiers and locations.
Later rows also explicitly record requested SDK backend selection.

| Increment | Observed RED | Same-target GREEN |
| --- | --- | --- |
| b01 | Rich Dataclass canonical could not generate repr/equality/order/hash | `b01-green.log`: one canonical passed on 3.12 |
| b02 | Three controlled 3.13 equality scenarios could not generate the nested term bindings | `b02-flat-corrected-green.log`: same three scenarios passed |
| b03 | Explicit Python backend generation failed on repeated disabled order instance names; corrected attempts then exposed factory reassignment hygiene and tuple carrier limitations | `b03-python-static-expression-green.log`: same rich canonical renderer/std oracle passed |
| b11 | Ephemeral true intermediate result released after the next comparison | `b11-lifetime-green.log`: same focused test passed |
| b12 | Invalid truth result retained by generated frame locals while its exception traceback was held | `b12-truth-cleanup-green.log`: same focused test passed |

The neutral fixture's initial missing closing brace and missing assembly entry
were setup failures, not behavioral RED. The first flat-step intended GREEN used
a stale generated base after an unrecorded tool-level regeneration launch lacked
consumer `PYTHONPATH`; its failed run and corrected regeneration are retained.
Inherited production/default naming attempts, unsupported bare ref carriers and
nested wildcard bindings are preserved as observed source-pattern limitations,
not proof of SDK defects or authority to fix dependencies. The successful route
uses existing authored resources, path/identifier bindings and consumer captures.

The full hash policy table, neutral matcher override, recursive/local-method
canonical and extended callback/source checks were verification additions after
core implementation. They were **not** separate test-first RED increments as
requested by the plan. This is a TDD sequencing deviation, not waived or hidden.
The b11/b12 defects each have real product-level pre-fix RED and identical focused
GREEN targets. Further stages must test each new facility before implementing it.

## Existing-API generation and equality equivalence

`yidl/shared/comparison.yidl` owns neutral method resources and matching/production
rules. `yidl/dataclass_comparison.yidl` inherits it and DataclassCore. The independent
`tests/data/yidl/comparison_neutral.yidl` inherits the same core, overriding operand
matchers to read `self.payload.rank`/`size`; its plain slotted model has no Dataclass
metadata. No generic Python comparison helper, dynamic method source emitter or
AST surgery supplies these methods. The consumer wheel includes both modules and
the authoritative neutral asset. Undoable build-time reuse is still unimplemented.

The failed recursive expression-hole path left later child external bindings
unresolved with the original SDKs. The accepted consumer alternative uses flat,
ordered authored statement contributions on 3.13/3.14. For each nonfinal operand,
read left then right, evaluate `==`, assign its raw result to a private local,
truth-test it once, and return it unchanged if false-y. A `finally` deletes that
local on true, false-return and exception/BaseException paths. Return evaluation
retains a false-y object on the return stack; a true result is released before the
next operand read. The last comparison returns its raw result directly without
truth conversion. Thus each stage matches the corresponding `and` transition,
including observable ephemeral-result release and traceback retention. The kept
private local `_y_cmp_result` gives stable source across both SDK backends; it is
an internal method binding, never a field or runtime metadata dispatcher.

3.12 uses generated operand tuples. 3.13/3.14 retain the self shortcut before the
exact-class guard and ordered comparisons. Differential tests compare against
independently decorated std classes for ordered reads, shared/nonreflexive values,
reflection, false-y/raw final identity, bool/equality exceptions, invalid bool,
BaseException and release timing. Ordering/hash retain Python tuple operations.
Repr uses the selected interpreter's actual recursion guard, with specialized
field reads and std exception cleanup behavior.

An authored `direct_ref if True else None` resource is a valid expression carrier
for both original SDK backends; bare value-form ref and tuple funcargs routes had
different observed limitations. The constant branch disappears when compiling
executable AST. The direct hash bytecode projection matches an authored direct
hash except CPython 3.14's LOAD_FAST versus LOAD_FAST_BORROW optimization. The test
normalizes only that opcode pair; it still rejects extra jumps/calls/allocations.
This is syntax/semantic evidence, not a performance result.

## Checkpoint matrix and limits

The final `b13-final-*` records run the entire current suite in separate 3.12,
3.13 and 3.14 environments, each with explicit native-rust and Python SDK selection.
All six final runs passed 86 tests with one intentional Field.doc minor skip.
Earlier full attempts are retained: an overstrict 3.14 borrow-opcode projection and
Python 3.13/3.14 temporary-name source differences preceded the current fixture
and kept-local corrections. No canonical expectation or behavioral oracle was
removed. Each versioned case has an explicit minor-to-source manifest and compares
its unmodified emitted text plus formatted source. The formatter warning from an
earlier default-target invocation remains in its log; final authored files use
`--target-version py312` and all current sources execute on every supported minor.

The six canonical cases contrast fields, classes and instances, including policy
field deletion, compare/hash exclusions, empty operands, local versus inherited
methods, recursive/empty repr and the neutral nested-read adapter. Source checks
establish plain classes, direct reads/stores, actual YIDL composition, no Dataclass
context prelude, resource packaging, exact regeneration and constant-carrier
bytecode. Environment JSON verifies original wheel hashes and module origins
relative to each isolated prefix.

The 16-case independent std hash table verifies the compiler selection, including
frozen selection. Actual frozen instance storage is Stage C and currently raises
`NotImplementedError`; no generated frozen behavior is claimed here. Named
factories, conversion/validation, const/lazy/provider fields, generated inheritance,
complete helper semantics, actual Undoable integration, final installed/differential
acceptance and benchmarks remain C–H. There is no performance claim or completed
one-shot claim; the operator scope intervention and compiler detour remain in the
historical record.
