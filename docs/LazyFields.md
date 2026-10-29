# Delay expensive values

A lazy field postpones its factory until the value is read. A successful result
is cached. This is useful when some objects never need an expensive derived
value. Lazy fields remain ordinary public data for helpers and comparison unless
you exclude them.

## Read once, then reuse

```python
from yidl_dataclass import dataclass, lazy

calls = []

def render(heading):
    calls.append(heading)
    return heading.upper()

@dataclass
class Document:
    heading: str
    preview: str = lazy(default_factory=render, repr=False, compare=False)

document = Document("draft")
assert calls == []
document.heading = "ready"
assert document.preview == "READY"
assert document.preview == "READY"
assert calls == ["ready"]
```

The factory sees providers at evaluation time. Changing a provider after a
successful read does not invalidate the cached result. Repr, equality, ordering,
hashing, `asdict` and `astuple` can read lazy fields that participate in those
operations. Exclude a lazy field from repr/comparison when those operations
should not compute it. An eager factory depending on a lazy field materializes
it during construction.

## Override, reset or seed a value

In a nonfrozen model, lazy fields are mutable by default. `mutable=True` makes
that choice explicit. Assignment runs conversion/validation and marks the value
ready; deletion resets it so the next read evaluates the factory again.

```python
document.preview = "manual"
assert document.preview == "manual"
del document.preview
document.heading = "final"
assert document.preview == "FINAL"
assert calls == ["ready", "final"]
```

Select `mutable=False` for a read-only lazy field. `lazy(init=True, ...)` accepts
an explicit constructor seed; omission still leaves evaluation delayed.
`frozen=True` makes lazy fields read-only by default while still permitting their
internal first evaluation.

## Failures, recursion and hidden inputs

A failed lazy evaluation returns to the unready state, so a later read retries.
A `BaseException` also clears the busy state. Recursive access to the same busy
field raises `LazyInitializationError`; concurrent first access raises that error
too. There is no lock for coordinating first access. Do not mutate the provider
model inside its evaluating callbacks.

InitVars directly needed by delayed consumers are retained privately. If every
such consumer is nonresettable, retained providers can be released after all have
succeeded. A resettable consumer keeps its required provider for the lifetime of
the instance. An eager intermediate cuts this retention path. Hidden values never
become public attributes or helper entries.

Copy and pickle preserve whether the field is ready without forcing evaluation;
copying during evaluation is rejected. Runtime [freezing](Freezing.md) materializes
all lazy stored fields before completion, so factory or pipeline failure can
interrupt freezing. The operation does not roll back already processed fields.

Run [lazy_fields.py](../examples/lazy_fields.py) to see caching and reset with a
hidden InitVar. See [the reference](API.md#lazy-evaluation-retry-and-hidden-provider-lifetime)
for the exact retention contract.
