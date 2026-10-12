# YIDL Dataclass

Status: Stage A product checkpoint is ready for owner verification; semantic
design and TDD plan are independently accepted. Stages B–H remain outstanding. The operator-directed consumer-only generation
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

The current candidate implements ordinary-field constructors/storage and standard
inspection/data helpers on CPython 3.12–3.14. During this staged checkpoint, explicitly
use `eq=False, repr=False`; comparison/repr/hash generation arrives in Stage B.
Frozen/policy fields, named factories, InitVars and extension kinds remain later
stages and currently raise `NotImplementedError` when selected. This is an
unreleased partial implementation, not the completed compatibility matrix.

```python
from yidl_dataclass import dataclass, field, asdict, generated_source

@dataclass(eq=False, repr=False)
class Inventory:
    count: int
    label: str = "stock"
    tags: list = field(default_factory=list)

item = Inventory(3)
item.count = 4
assert asdict(item) == {"count": 4, "label": "stock", "tags": []}
assert not hasattr(item, "__dict__")
print(generated_source(Inventory))
```

Models with `slots=True` replace the declaration and inherit its declared bases;
plain slotted mixins work, while bases with an instance dictionary are rejected.
`slots=False` supports ordinary dictionary storage/class-default fallback. Local
custom initializers and `init=False` suppress generated initialization. Factories
are captured as Python objects and called by specialized generated constructors;
they are never serialized into source. Generated source references its capture
namespace and is an inspection artifact rather than a standalone model module.

For development, install the locked original SDK wheels and test dependencies in
separate environments, then run `python -m pytest`. The regeneration command is
`python -m yidl_dataclass.regenerate_dataclass_base` (check by default, `--write`
to update). The [Stage A evidence](docs/validation/stage-a/README.md) records
scope, exact RED/GREEN commands, failures and validation limits. No performance
result is claimed at this checkpoint.
