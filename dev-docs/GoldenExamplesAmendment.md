# Golden examples: inspection as well as verification

Status: additional operator requirement recorded during the initial independent
spec review, outside that round's frozen object. Included in the consolidated
requirements object for the second review round; not yet an accepted design.

Canonical examples and their generated goldens have two purposes: verify that
generation produces the expected result, and make the generated behavior easy
for a developer or another LLM to inspect. Examples must therefore show meaningful
contrasts among field options, not only the smallest possible success case.

Expand selected examples with additional fields, instances or classes. Roughly
doubling the fields in some small examples is a useful starting point, not a
mechanical quota. Keep each example cohesive and show several contrasting policies
side by side where that clarifies the generated code.

For the dataclass experiment and its Undoable comparison integration, include
examples contrasting:

- Ordinary writable fields, constant fields and writable cache exceptions.
- Default values, independent factories and named dependent factories.
- Eager and lazy initialization, including privately retained initialization inputs.
- Fields included in or excluded from equality, ordering and hashing.
- Several instances that differ in included fields, and instances differing only
  in excluded management fields, so comparison outcomes are observable.
- Different classes and enabled/disabled comparison options where that exposes
  type-compatibility and generation behavior clearly.
- Enabled conversion/validation alongside otherwise comparable plain fields.

Pair readable generated-source goldens with canonical behavioral output when the
harness supports both. Show the access paths, selected comparison operands,
dependency wiring and resulting behavior without requiring hidden knowledge from
the implementation. Reuse the same canonical scenarios rather than duplicating
success-path assertions in bespoke unit tests.

Actual changes to existing Undoable examples belong to the planned integration;
this requirement does not reopen its original experiment measurements or resume
the separately paused initialization-helper change.
