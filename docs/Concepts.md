# Fields and generated behavior

A model declaration describes stored data and the operations that use it. The
`@dataclass` decorator generates methods specialized for those fields. A policy
on one field does not require every ordinary field to use a property.

## Ordinary fields, defaults and constructors

Fields follow annotation order, including inherited fields. Required positional
fields precede defaulted positional fields. Use `kw_only=True` on a field or the
decorator when callers should supply names. The standard `KW_ONLY` annotation
makes following local fields keyword-only.

```python
from yidl_dataclass import KW_ONLY, dataclass, field

@dataclass
class Request:
    path: str
    _: KW_ONLY
    retries: int = 3
    headers: dict = field(default_factory=dict)

request = Request("/items", retries=2)
assert request.retries == 2
assert Request.__match_args__ == ("path",)
```

`default` and `default_factory` are alternatives. Factories run only when a value
was omitted, except an `init=False` factory runs as part of generated
initialization. A field with `init=False` cannot be passed to the constructor.
An ordinary source-free `init=False` field can remain absent until assigned;
reading it before assignment raises `AttributeError`.

## Choose a field family

| Declaration | Use it for | Public data helpers |
| --- | --- | --- |
| `field(...)` or annotation | Ordinary eager data with optional policies | Included |
| `const(...)` | One field that is read-only after initialization | Included |
| `lazy(default_factory=...)` | Data computed on first access | Included; reading helpers can compute it |
| `initvar(...)` or `InitVar[T]` | Constructor input needed by factories but hidden afterward | Omitted |
| `classvar(...)` or `ClassVar[T]` | Shared class data rather than instance storage | Omitted |
| `local_store(...)` | Per-instance management state or caches | Omitted |

```python
from yidl_dataclass import asdict, classvar, const, local_store

@dataclass
class Record:
    key: str = const()
    category: str = classvar(default="record")
    cache: dict = local_store(default_factory=dict)

record = Record("A1")
record.cache["seen"] = True
assert asdict(record) == {"key": "A1"}
assert Record.category == "record"
```

`const` blocks replacing or deleting its field; it does not freeze an object
stored inside it. Local storage is writable by default, including in a
`frozen=True` model. A completed runtime `freeze()` blocks its assignment and
deletion too. See the [freezing guide](Freezing.md) for this distinction.

## Representation, equality, ordering and hashes

By default, generated representation includes each ordinary field and equality
compares fields with `compare=True`. Both sides must have the same generated
class. `repr=False` and `compare=False` select participation independently.
Lazy fields participating in these operations can be evaluated by them.
`order=True` adds ordering and requires `eq=True`.

Default mutable equality models are unhashable. Frozen equality models normally
hash their included fields, so those values must themselves be hashable. Field
`hash=None` follows `compare`; `hash=False` explicitly excludes a field. Selecting
`hash=True, compare=False` is rejected. `unsafe_hash=True` requests a generated
hash despite mutability and can break dictionary/set lookup when values change.
Runtime `freeze()` does not activate hashing: a default freezable equality model
remains unhashable afterward.

## Slots and class replacement

Slots prevent accidental new attributes and avoid an instance dictionary.
With the default `slots=True`, decoration returns a new class carrying the
supported declaration methods and attributes. The normal `@dataclass` binding
already refers to this result. With `slots=False`, decoration updates the
original class. `weakref_slot=True` adds weak-reference support and requires slots.
Frozen and freezable models require slots.

Use [the full reference](API.md) for custom-method suppression, pseudo-annotation
recognition, inheritance constraints and the precise standard-helper subset.
