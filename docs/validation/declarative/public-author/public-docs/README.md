# YIDL Dataclass

`yidl_dataclass` creates Python dataclasses from modular YIDL templates. Ordinary
fields use direct writable slots by default. Named factories, conversion,
validation, constant and lazy fields add specialized generated methods for the
fields that need them.

This is an unreleased consumer candidate for **CPython 3.12, 3.13 and 3.14**.
Stages A–F are independently verified; public packaging/usability and performance
assessment remain in progress. No speed or memory advantage is claimed.

Install the supplied wheel with the original SDK wheels available locally:

```sh
python -m pip install --no-index --find-links wheelhouse wheelhouse/yidl_dataclass-0.1.0.dev0-py3-none-any.whl
```

The locked runtime dependencies are Astichi 1.1.3 and YIDL 0.1.0. Sibling SDK
checkouts and SDK rebuilds are unnecessary. The wheel contains this README,
public guides and the first-use example under `yidl_dataclass/documentation`.

```python
from yidl_dataclass import dataclass, field, fields, asdict, replace

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
assert [description.name for description in fields(item)] == ["count", "label", "tags"]
```

Run [examples/first_use.py](examples/first_use.py) for the complete introductory
example. The [API guide](docs/API.md) covers defaults, field families, factories,
pipelines, lazy state, inspection, copying, replacement and supported inheritance.
The [generation guide](docs/Generation.md) explains emitted source, packaging,
regeneration and the reusable comparison resource.

The main differences from stdlib dataclasses are slots enabled by default, strict
boolean flags, generated class replacement, no `__post_init__`, hidden InitVars,
field-specific read-only properties, and explicitly excluded writable frozen
caches. Several advanced combinations are rejected rather than silently ignored;
the API guide lists them. Std `Field`, `MISSING`, `InitVar`, `KW_ONLY`, inspection
and data helpers remain interoperable on the documented subset.

Development checks use the original SDK wheels: `python -m pytest -q` and
`python -m yidl_dataclass.regenerate_dataclass_base`. Regeneration checks by
default; `--write` refreshes the base from the packaged authored YIDL resources.
`python -m hatchling build` builds only this consumer. Source compilation/cache
reuse during generation is permitted; no parser-free or wholly Rust execution
claim is made.

The [experiment record](dev-docs/CurrentProgramCheckpoint.md) preserves the
original GO time, scope correction, dependency detour, TDD deviations, independent
reviews and actual evidence. The [active boundary](dev-docs/TaskBoundary.md)
keeps SDKs/Lifecycle reference-only. The authoritative shared comparison resource
is owned here; Undoable consumes it at regeneration time and has no Dataclass
runtime dependency. See [E/F evidence](docs/validation/stage-ef/README.md).
