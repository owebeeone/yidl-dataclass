# Freeze a finished model

Choose `frozen=True` when data fields should be read-only as soon as construction
finishes. Choose `freezable=True` when callers need a mutable setup phase followed
by an explicit, permanent `freeze()` operation. Both operate on field bindings;
arbitrary objects stored in those fields do not automatically become immutable.

| Behavior | `frozen=True` | `freezable=True` |
| --- | --- | --- |
| Initial state | Data fields read-only after initialization | Ordinary fields mutable until `freeze()` |
| Transition | Construction establishes restrictions | Explicit permanent `instance.freeze()` |
| Field `freeze` callbacks | Not supported | Transform selected stored values on transition |
| Writable management storage | `local_store` and explicitly excluded `mutable=True` fields allowed | All stored field setters/deleters blocked after completion |
| Containers and children | Shallow restrictions | Shallow unless field policies cascade or transform |
| Hashing | Existing frozen/equality rules | Existing options; freezing does not activate a hash |

Both require `slots=True` and generated initialization. `frozen=True` and
`freezable=True` cannot be combined. A freezable hierarchy must use consistent
freezable settings. The name `freeze` is reserved for the generated operation.

## Populate, then freeze

```python
from dataclasses import FrozenInstanceError
from yidl_dataclass import dataclass, field

@dataclass(freezable=True)
class Item:
    name: str

@dataclass(freezable=True)
class Catalog:
    title: str
    item: Item
    tags: object = field(default_factory=list, freeze=tuple)

catalog = Catalog("draft", Item("initial"))
catalog.title = "ready"
catalog.item.name = "prepared"
catalog.tags.append("release")
catalog.freeze()
assert catalog.tags == ("release",)
try:
    catalog.item.name = "changed"
except FrozenInstanceError:
    pass
else:
    raise AssertionError("child remained writable")
catalog.freeze()  # A completed freeze can be called again safely.
```

The resolved `Item` annotation selects an inferred child policy: call that same
child object's `freeze()` and retain it. `freeze=tuple` replaces the tags list
with a tuple. After success, assignment and deletion of all stored fields are
blocked, including lazy fields and local management stores. There is no thaw.

## Select a field policy

A `freeze` callback receives exactly one positional argument, the current field
value, and returns the stored replacement. It receives no field name, model or
keyword arguments. It runs after input conversion and validation have already
happened; its return value is installed without rerunning either pipeline.
Choose annotations that honestly describe the before/after representations.

An omitted hook only infers cascading for a resolved annotation that is itself a
freezable YIDL Dataclass type. There is no inference from runtime values, container
elements, unions, unresolved/string annotations, or an arbitrary method named
`freeze`. An explicit hook wins over inference. For nullable children, use a
callback that preserves `None` and freezes non-None values explicitly.

A container hook can also cascade to each child:

```python
def freeze_items(values):
    for value in values:
        value.freeze()
    return tuple(values)

@dataclass(freezable=True)
class Shelf:
    items: object = field(default_factory=list, freeze=freeze_items)

shelf = Shelf([Item("one"), Item("two")])
shelf.freeze()
assert isinstance(shelf.items, tuple)
```

Tuple conversion freezes the container's shape, not mutable objects inside it.
A field without a hook retains its value. Even after its binding is frozen, a
retained list can still be appended to. A read-only mapping view also retains
aliases to the original mutable dictionary; it does not detach that dictionary.
`const` and `frozen=True` have the same shallow-container limitation.

## Partial failure and retry

Freezing visits stored fields in normalized field order, including inherited
fields and local storage. Lazy values are materialized along the way. Every stored
field is read; an absent field, for example after deletion, can fail with
`AttributeError`. It is an
optimistic operation with no staging, transaction or rollback. A failure
propagates the callback exception directly, clears the parent's in-progress
marker for retry, and can leave earlier field transformations and completed
children in place.

```python
attempts = []

def finish(value):
    attempts.append(value)
    if len(attempts) == 1:
        raise ValueError("try again")
    return value

@dataclass(freezable=True)
class Draft:
    tags: object = field(freeze=tuple)
    status: str = field(freeze=finish)

draft = Draft(["one"], "ready")
try:
    draft.freeze()
except ValueError:
    pass
else:
    raise AssertionError("expected first attempt to fail")
assert draft.tags == ("one",)  # Already transformed; no rollback.
draft.status = "retry"         # Parent did not complete freezing.
draft.freeze()                 # tuple accepts the earlier tuple again.
assert attempts == ["ready", "retry"]
```

Hooks must tolerate a retry on partially processed data. A previously frozen child
stays frozen even if its parent later fails. The in-progress marker terminates
recursive visits through cycles and shared objects; it is not a concurrency
control mechanism. Concurrent freezing is not guaranteed safe.

Copy, deepcopy and pickle preserve completed frozen state. They reject copying
while a freeze is active. Package `replace()` constructs a new mutable model,
although unchanged values may still share already frozen children or immutable
representations. Default freezable equality models remain unhashable after
freezing. `unsafe_hash=True` does not become safe merely because a future freeze
is planned; never mutate values used as dictionary or set keys.

Run [runtime_freeze.py](../examples/runtime_freeze.py) and
[freeze_failure.py](../examples/freeze_failure.py) for complete examples.
