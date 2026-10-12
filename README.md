# YIDL Dataclass

Status: Stages A–C are owner-verified; Stage D lazy/inheritance/copy checkpoint is
ready for owner verification. Semantic design and TDD plan are independently
accepted. Stages E–H remain outstanding. The operator-directed consumer-only generation
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
inspection/data helpers, repr, equality, ordering and hashing on CPython 3.12–3.14.
Equality follows each minor: tuple comparison on 3.12 and ordered field comparisons
with the self shortcut on 3.13/3.14. Repr omits excluded fields and handles recursion.
Field-local `compare`/`hash` flags select direct generated operands;
`hash=True, compare=False` is rejected to preserve equal-object hash consistency.
Named factories resolve a checked provider DAG and receive converted/validated
values through specialized calls. Constant/frozen fields, writable cache
exceptions, construction-scoped InitVars, ClassVars and local storage are
implemented. Conversion/validation accessors have individual backing storage;
failed assignments preserve the previous value. Lazy fields implement busy/ready/retry and optional mutable seed/reset policies.
Delayed calls read current fields/ClassVars and retain only directly consumed
hidden InitVars; terminal consumers release providers once all are ready.
One generated model base with plain mixins supports compatible overrides, reused
slots and independent copied class cells. Copy/deepcopy/pickle preserve readiness,
absence, caches and retained providers without running lazy factories; active
lazy copies fail precisely. Replacement uses constructor semantics and never
replays hidden providers; CPython 3.13/3.14 receive generated `__replace__` when
no local override exists. Undoable integration and performance gates remain
outstanding. This is an unreleased partial implementation.

```python
from yidl_dataclass import dataclass, field, asdict, generated_source

@dataclass
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

Accessors use a public `field = _y_dc_property(private_getter, private_setter,
private_deleter)` assignment. `_y_dc_property` captures the builtin; each private
function is that field's specialized body with direct backing-storage access.
Constructor fragments likewise capture required builtins privately so fields
named `type`, `Exception` or `TypeError` retain their normal public names.
This source-spelling choice is equivalent descriptor construction to `@property`
and `@field.setter`. Separately composed public decorators could acquire distinct
scoped identifiers on the original Python backend; private functions plus one
assignment are the working authored-resource route. Descriptor identity and
source/bytecode checks verify no additional runtime access dispatcher.

For development, install the locked original SDK wheels and test dependencies in
separate environments, then run `python -m pytest`. The regeneration command is
`python -m yidl_dataclass.regenerate_dataclass_base` (check by default, `--write`
to update). The [Stage A evidence](docs/validation/stage-a/README.md) records
scope, exact RED/GREEN commands, failures and validation limits. The
[Stage B evidence](docs/validation/stage-b/README.md) includes the std differential
callback matrix and independently inherited neutral comparison consumer. The
[Stage C evidence](docs/validation/stage-c/README.md) records provider DAGs,
hidden providers, pipeline atomicity and namespace ownership. The
[Stage D evidence](docs/validation/stage-d/README.md) records lazy retention,
inheritance, descriptor hygiene and copy/replace protocols.
The authoritative `yidl/shared/comparison.yidl` is included in the consumer wheel;
future Undoable integration will reuse it at build time. No performance result is
claimed at this checkpoint.
