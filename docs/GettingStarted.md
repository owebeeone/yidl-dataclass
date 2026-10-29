# Your first model

A dataclass saves you from writing repetitive constructors, representations and
comparisons. YIDL Dataclass adds field policies while keeping the ordinary case
small. This tutorial creates a simple inventory entry, then adds input conversion.

## Install

The release tests CPython 3.12, 3.13, 3.14 and 3.15, with the platform boundary
below. Create a virtual environment:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install yidl-dataclass
```

On Windows PowerShell, activate the environment with
`.venv\Scripts\Activate.ps1` instead of the second line. Dependencies install
automatically; no sibling repositories or generation step are required.

### Platform and backend boundary

The CPython version matrix does not qualify every platform/backend combination.
The Python 3.15 release qualification covers macOS locally and Ubuntu in CI.
Astichi 1.1.3 has no Windows CPython 3.15 binary wheel, and a source build on that
combination has not been qualified. Windows CPython 3.15 is therefore outside
that release qualification. Select a platform/version with the required published
SDK wheels rather than assuming an untested SDK source build is supported.

To reproduce the documentation examples' backend selection, set it before
starting Python:

```sh
export ASTICHI_LOWER_ENGINE=python
```

In PowerShell: `$env:ASTICHI_LOWER_ENGINE = "python"`. This selects the generation
backend; it does not change field policy semantics.

## Declare and construct

```python
from yidl_dataclass import asdict, dataclass, field, fields, replace

@dataclass
class Inventory:
    count: int
    label: str = "stock"
    tags: list = field(default_factory=list, compare=False, repr=False)

first = Inventory(3)
second = Inventory(count=3)
assert first == second
assert repr(first) == "Inventory(count=3, label='stock')"
first.tags.append("checked")
assert second.tags == []
```

Each annotation declares a field. `count` is required; `label` has a default.
`default_factory=list` creates a fresh list for each instance. Use factories for
mutable values instead of a shared list literal. Here `tags` is excluded from
comparison and representation, but remains a stored field.

## Edit and inspect

```python
first.count = 4
assert not hasattr(first, "__dict__")
assert [item.name for item in fields(first)] == ["count", "label", "tags"]
assert asdict(first) == {"count": 4, "label": "stock", "tags": ["checked"]}
updated = replace(first, count=5)
assert updated.count == 5 and first.count == 4
```

Models use slots by default, so you cannot attach arbitrary new attributes.
`fields` and `asdict` are the standard library helpers. `replace` is this package's
helper: it constructs a new model and also understands hidden InitVars and lazy
fields. Dictionary mode is available with `@dataclass(slots=False)`.

## Accept input with a field rule

```python
from yidl_dataclass import FieldValidationError

@dataclass
class Quantity:
    count: int = field(converter=int, validator=lambda value: value >= 0)

quantity = Quantity("12")
assert quantity.count == 12
quantity.count = "15"
assert quantity.count == 15
try:
    quantity.count = "-1"
except FieldValidationError:
    pass
else:
    raise AssertionError("negative quantity was accepted")
assert quantity.count == 15
```

Conversion happens before validation, both during construction and permitted
assignment. An unsuccessful assignment leaves the old value installed. An
annotation such as `count: int` alone does not perform either operation.

Run [first_use.py](../examples/first_use.py) for the complete ordinary-field
example. Continue with [field concepts](Concepts.md), then [dependent
initialization](Initialization.md). To make a completed object permanently
read-only, follow [freezing](Freezing.md).
