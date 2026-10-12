# YIDL Dataclass

Status: semantic design and TDD plan independently accepted; product
implementation has not started. The operator-directed consumer-only generation
amendment is independently accepted at the
[recorded boundary](dev-docs/ConsumerOnlyGenerationAmendment-ReviewResult.md). Astichi/YIDL SDK changes are outside
scope; original Astichi 1.1.3 / YIDL 0.1.0 generation is the candidate baseline.

A proposed YIDL-generated dataclass implementation with standard Python dataclass
behavior and metadata where compatible, extended with dependent factories,
initialization-only providers, conversion, validation, constant/lazy fields and
per-field mutability policies. One generated class owns its data and methods;
facades and separate state objects are unnecessary for this model.

[Discussion requirements and open decisions](dev-docs/DataclassConcept.md)
record the starting point. The [detailed design and compatibility
matrix](dev-docs/DataclassDesign.md) are accepted at the
[recorded review checkpoint](dev-docs/DataclassDesign-ReviewResult.md).
The [TDD plan](dev-docs/DataclassPlan.md) retains the product stages A–H.
The [consumer generation amendment](dev-docs/ConsumerOnlyGenerationAmendment.md)
and [scope correction](dev-docs/ScopeCorrection.md) supersede the historical
compiler prerequisites; their time and evidence remain in the experiment record.

Ordinary writable fields use direct slots by default. Fields requiring constant,
frozen, lazy or conversion/validation behavior use specialized generated code.
[Experiment protocol](dev-docs/ExperimentProtocol.md) records the autonomous-run,
TDD, correctness, performance, time and cost measurement requirements.

[Review checkpoint](dev-docs/CurrentProgramCheckpoint.md) records the two
independent review rounds and the operator-accepted field-locality amendment.
[Declarative evaluation](dev-docs/DeclarativeEvaluation.md) records the evaluator
reference and the distinction between locality, authoring layout and correctness.
