# YIDL Dataclass

Status: requirements accepted for detailed design; implementation has not started.

A proposed YIDL-generated dataclass implementation with standard Python dataclass
behavior and metadata where compatible, extended with dependent factories,
initialization-only providers, conversion, validation, constant/lazy fields and
per-field mutability policies. One generated class owns its data and methods;
facades and separate state objects are unnecessary for this model.

[Discussion requirements and open decisions](dev-docs/DataclassConcept.md)
record the starting point. The detailed design, compatibility matrix, TDD plan
and implementation remain to be developed.

Ordinary writable fields use direct slots by default. Fields requiring constant,
frozen, lazy or conversion/validation behavior use specialized generated code.
[Experiment protocol](dev-docs/ExperimentProtocol.md) records the autonomous-run,
TDD, correctness, performance, time and cost measurement requirements.

[Review checkpoint](dev-docs/CurrentProgramCheckpoint.md) records the two
independent review rounds and the operator-accepted field-locality amendment.
[Declarative evaluation](dev-docs/DeclarativeEvaluation.md) records the evaluator
reference and the distinction between locality, authoring layout and correctness.
