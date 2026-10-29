# YIDL Dataclass

YIDL Dataclass turns annotated Python classes into slotted data models. Start with
ordinary dataclass fields, then add named factories, conversion, validation,
read-only fields, lazy values or permanent runtime freezing where you need them.

```python
from yidl_dataclass import asdict, dataclass, field, replace

@dataclass
class Inventory:
    count: int
    label: str = "stock"
    tags: list = field(default_factory=list, compare=False, repr=False)

item = Inventory(3)
item.count = 4
assert asdict(item) == {"count": 4, "label": "stock", "tags": []}
assert not hasattr(item, "__dict__")
assert replace(item, count=5).count == 5
```

Install with `python -m pip install yidl-dataclass`. The release tests
**CPython 3.12, 3.13, 3.14 and 3.15**, subject to the
[platform/backend boundary](https://owebeeone.github.io/yidl-dataclass/GettingStarted/#platform-and-backend-boundary).
Windows CPython 3.15 is outside the release qualification: Astichi 1.1.3 has no
binary wheel for that combination and its source build has not been qualified.
Installation brings the pinned Astichi 1.1.3 and YIDL 0.1.2 dependencies; on
platforms with their published wheels, SDK checkouts and rebuilds are unnecessary.
Type annotations describe fields; conversion and validation are explicit options.

Read the [documentation](https://owebeeone.github.io/yidl-dataclass/), starting with
[your first model](https://owebeeone.github.io/yidl-dataclass/GettingStarted/) and
[field concepts](https://owebeeone.github.io/yidl-dataclass/Concepts/). Practical
guides cover [dependent initialization](https://owebeeone.github.io/yidl-dataclass/Initialization/),
[lazy values](https://owebeeone.github.io/yidl-dataclass/LazyFields/) and
[permanent freezing](https://owebeeone.github.io/yidl-dataclass/Freezing/).
The existing [API reference](https://github.com/owebeeone/yidl-dataclass/blob/main/docs/API.md)
and [generation guide](https://github.com/owebeeone/yidl-dataclass/blob/main/docs/Generation.md)
remain available in the repository. Run the complete programs in
[examples](https://github.com/owebeeone/yidl-dataclass/tree/main/examples).

`freezable=True` lets you populate a model and then call `instance.freeze()` once
it is ready. Field policies can freeze child models or replace containers with
immutable representations. Freezing is shallow unless policies cascade, permanent,
and nontransactional: a failed hook can leave earlier transformations in place.
Use `frozen=True` instead when fields should be read-only immediately after
construction. Neither option recursively freezes arbitrary Python objects.

Compared with stdlib dataclasses, slots are enabled by default, flags require exact
booleans, InitVars have no public attributes, and read-only fields use individual
properties. Slotted decoration returns a replacement class. `__post_init__` is
rejected; named factories and field pipelines provide dependent initialization.
The [reference](https://owebeeone.github.io/yidl-dataclass/API/) specifies the
supported inheritance and standard-helper interoperability subset.

For development, see [CONTRIBUTING.md](https://github.com/owebeeone/yidl-dataclass/blob/main/CONTRIBUTING.md).
For release procedures, see [RELEASE.md](https://github.com/owebeeone/yidl-dataclass/blob/main/RELEASE.md).
Historical experiments, review records and measurements are preserved in
[dev-docs](https://github.com/owebeeone/yidl-dataclass/tree/main/dev-docs); those
records do not claim a universal speed or memory advantage.
