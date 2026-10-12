# YIDL Dataclass

Status: concept and specification stage.

A proposed YIDL-generated dataclass implementation with standard Python dataclass
behavior and metadata where compatible, extended with dependent factories,
initialization-only providers, conversion, validation, constant/lazy fields and
per-field mutability policies. One generated class owns its data and methods;
facades and separate state objects are unnecessary for this model.

[Discussion requirements and open decisions](dev-docs/DataclassConcept.md)
record the starting point. The detailed design, compatibility matrix, TDD plan
and implementation remain to be developed.
