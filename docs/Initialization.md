# Initialize dependent values

A named factory receives providers by parameter name. Use it when a field needs
another field's processed value or a constructor-only input. The decorator checks
the dependency graph and arranges evaluation, so dependency order does not have to
match declaration order.

## Derive one field from another

```python
from yidl_dataclass import dataclass, field

def amount_for(quantity, price):
    return quantity * price

@dataclass
class Line:
    total: int = field(init=False, default_factory=amount_for)
    quantity: int = field(converter=int)
    price: int = field(converter=int)

line = Line("2", "15")
assert line.total == 30
line.quantity = "3"
assert line.quantity == 3 and line.total == 30
```

The factory sees converted and validated providers. It initializes `total` once
for this construction; it does not create a reactive formula. Editing `quantity`
does not recalculate `total`. If a field has `init=True`, an explicit constructor
value bypasses its default factory, but still runs that field's conversion and
validation. A dependency cycle is rejected at decoration even if a caller could
bypass one of its factories with explicit input.

## Keep constructor inputs private

```python
from yidl_dataclass import asdict, initvar

def reference_for(prefix, cls):
    return f"{prefix}-{cls.__name__}"

@dataclass
class Order:
    prefix: str = initvar(default="WEB")
    reference: str = field(init=False, default_factory=reference_for)

order = Order()
assert order.reference == "WEB-Order"
assert not hasattr(order, "prefix")
assert asdict(order) == {"reference": "WEB-Order"}
```

An InitVar supplies factories without becoming a public attribute or helper
entry. `cls` is a special provider for `type(self)`. `ClassVar` providers supply
class data. A factory can also request `self` with `allow_self_factory=True`, but
it sees a partially initialized object and its implicit accesses cannot be
planned. Prefer explicit named providers.

## Factory argument rules

| Parameter shape | Behavior |
| --- | --- |
| Name matches a field or InitVar | Receives that provider; an optional parameter still selects it |
| `cls` | Receives the runtime class, `type(self)` |
| `self` | Receives the partial instance only when `allow_self_factory=True` |
| Unknown optional parameter | Keeps the callable's default |
| Unknown required parameter | Definition error |
| Positional-only, ordinary or keyword-only | Supported; arguments preserve those calling conventions |
| `*args` or `**kwargs` | Rejected |

Callables need an introspectable signature. The builtins `list`, `dict`, `set`,
`tuple`, `int`, `float`, `str`, `bytes` and `bool` have explicit zero-argument
factory support. Wrap another nonintrospectable callable in a small Python
function. A known provider with no source is an error, even when the matching
factory parameter has a default.

## Convert, then validate

A field converter receives one positional candidate and returns the value to
store. A validator receives that converted value. It must return `None` or exact
`True` to accept, or exact `False` to reject; truthy objects such as `1` do not
satisfy the validator contract. Raising an exception rejects the value too.

```python
from yidl_dataclass import FieldValidationError

@dataclass(convert=True)
class Measurement:
    count: int = field(validator=lambda value: value >= 0)
    note: str = field(default="", converter=None)

measurement = Measurement("7")
assert measurement.count == 7
try:
    measurement.count = "-2"
except FieldValidationError:
    pass
else:
    raise AssertionError("negative count accepted")
assert measurement.count == 7
```

Decorator `convert=True` infers conversion only for exact `int`, `float`, `str`,
`bytes`, `bool` annotations and their single-type nullable unions. Nullable
conversion preserves `None`. It does not infer conversion for containers or
arbitrary classes. Use `converter=callable` explicitly for those, or
`converter=None` to disable inherited conversion. Builtin `bool` follows Python's
normal truth conversion: nonempty text such as `"false"` becomes `True`; use a
custom parser when accepting textual booleans.

The pipeline runs during construction and permitted assignment. Storage changes
only after conversion and validation succeed. This protects the field's old value
on failure, but does not roll back a callback's external side effects.

## Why no `__post_init__`?

YIDL Dataclass rejects local and inherited `__post_init__` hooks. The motivation
is initialization that composes through declarations rather than manually chained
methods. With inherited post-init methods, authors must coordinate calls and MRO;
in a diamond, shared initialization can be duplicated or omitted when that
coordination is wrong. Python's cooperative `super()` can coordinate such a
hierarchy, but it leaves that discipline to every participating author.

Named factory dependencies express which values an initialization step needs.
The dependency plan orders required evaluations and shares a provider's result
within an initialization evaluation, instead of asking authors to chain hooks.
The `Line` example above replaces a hook assigning `self.total`: its factory
names the two values it needs and receives their processed results.

This is a motivation for the design, not a promise of arbitrary multiple model
inheritance. The current supported subset is one generated model base plus
compatible plain mixins; multiple generated bases are rejected. An explicit
constructor value can bypass a factory, and a lazy field has its own later
initialization and reset lifetime. A required step runs once within the relevant
evaluation, not once forever across instances or resets.

Use factories for derived values, converters for normalization and validators for
field acceptance. Whole-model validation and post-construction notification hooks
are outside this release. See [copying and inheritance](ModelOperations.md) and
the complete [callback reference](API.md#callback-argument-summary).

Run [dependent_fields.py](../examples/dependent_fields.py) for a complete program.
