# Declarative evaluation reference

Source: `DeclarativeApiEvaluatorV2.md`, titled "Declarative API Evaluator &
Identifier — v3". Identical bytes also occur as `DeclarativeApiEvaluatorV3.md`.
Source SHA-256: `20a72d189d1ad032a9f0ab9bbfc1b63636cade0062c1d05bbae0383e7fb0e815`.
The exact self-contained instrument is retained as
[reference/DeclarativeApiEvaluatorV3.md](reference/DeclarativeApiEvaluatorV3.md).
Its introductory historical links point to the original surrounding corpus,
which is not bundled; its definitions and scoring procedure are self-contained.
This is a reference summary, not a completed scorecard or substitute for the full
instrument. The detailed experiment plan must pin its scoring inputs and mode.

## Relevant criteria

- B.1 **Locality**: the span of description the engine must read to resolve an
  element. Local depends on the element itself; scoped depends on its enclosing
  scope or named elements; global depends on the whole description/external state.
  This measures resolution scope, not physical adjacency or a binary test of
  whether an API is declarative.
- E6 **Edit-proportionality**: description diff size relative to intent-change
  size. Removing a field should remove its field-specific policy in that edit,
  rather than also requiring cleanup in a separate decorator field-name map.
- R5 **Oracle independence**: designer-authored goldens alone are not an
  independent correctness oracle. Differential tests against standard dataclasses
  provide a separate source of evidence for the compatible subset.
- R3 **Predictable compositionality**: make combined field-policy behavior explicit
  and test interactions instead of relying on isolated happy paths.

The operator requires field-local policies and class-wide boolean generation
switches. This is an authoring constraint alongside the instrument, not an invented
numeric score. Named factory dependencies still legitimately refer to other fields.

The instrument separates declarative richness/generativity from correctness;
never collapse them into one unsupported grade. Design-stage results are projected,
inspection-only results are desk evaluations, and measured claims need executed
evidence and the instrument's required corpus/calibration inputs. Without the
relevant authoring harness, LLM-loop measurements remain unscored.
