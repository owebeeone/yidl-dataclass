# YIDL Dataclass

`yidl_dataclass` creates Python dataclasses from modular YIDL templates. Ordinary
fields use direct writable slots by default. Named factories, conversion,
validation, constant and lazy fields add specialized generated methods for the
fields that need them.

This package supports **CPython 3.12, 3.13, 3.14 and 3.15**. Its original supported
functional/package implementation and Undoable comparison integration are
[accepted after both independent final reviews reported GO](https://github.com/owebeeone/yidl-dataclass/blob/main/dev-docs/Dataclass-FinalReviewResult.md).
Historical benchmarks measured an earlier artifact tuple; corrected final paths
have not been timed. No universal speed or memory advantage is claimed.

Install from PyPI:

```sh
python -m pip install yidl-dataclass
```

The locked runtime dependencies are Astichi 1.1.3 and YIDL 0.1.2. Sibling SDK
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

Run [examples/first_use.py](https://github.com/owebeeone/yidl-dataclass/blob/main/examples/first_use.py) for the complete introductory
example. The [API guide](https://github.com/owebeeone/yidl-dataclass/blob/main/docs/API.md) covers defaults, field families, factories,
pipelines, lazy state, inspection, copying, replacement and supported inheritance.
The [generation guide](https://github.com/owebeeone/yidl-dataclass/blob/main/docs/Generation.md) explains emitted source, packaging,
regeneration and the reusable comparison resource.

The main differences from stdlib dataclasses are slots enabled by default, strict
boolean flags, replacement of slotted declarations, no `__post_init__`, hidden InitVars,
field-specific read-only properties, and explicitly excluded writable frozen
caches. Several advanced combinations are rejected rather than silently ignored;
the API guide lists them. Std `Field`, `MISSING`, `InitVar`, `KW_ONLY`, inspection
and data helpers remain interoperable on the documented subset.

Opt-in `freezable=True` models can be populated and then permanently frozen using
`freeze()`. Per-field `freeze` callbacks select the frozen representation and can
cascade to child objects. The transition is optimistic: cycles and repeated calls
are handled, but failures do not roll back earlier work. See the API guide for
field policies, inheritance and shallow-freeze limitations. Frozen hashing still
follows the existing dataclass options; freeze-time hash activation is not added.
The runtime-freeze extension is an experimental addition beyond the historical
review baseline above; its acceptance tests and goldens do not constitute a new
independent release review.
Run [examples/runtime_freeze.py](https://github.com/owebeeone/yidl-dataclass/blob/main/examples/runtime_freeze.py) for mutable setup,
permanent freezing, typed-child inference and a list-to-tuple field policy.

Development checks use the original SDK wheels: `python -m pytest -q` and
`python -m yidl_dataclass.regenerate_dataclass_base`. Regeneration checks by
default; `--write` refreshes the base from the packaged authored YIDL resources.
`python -m hatchling build` builds only this consumer. Source compilation/cache
reuse during generation is permitted; no parser-free or wholly Rust execution
claim is made.

The [experiment record](https://github.com/owebeeone/yidl-dataclass/blob/main/dev-docs/CurrentProgramCheckpoint.md) preserves the
original GO time, scope correction, dependency detour, TDD deviations, independent
reviews and actual evidence. The [active boundary](https://github.com/owebeeone/yidl-dataclass/blob/main/dev-docs/TaskBoundary.md)
keeps SDKs/Lifecycle reference-only. The authoritative shared comparison resource
is owned here; Undoable consumes it at regeneration time and has no Dataclass
runtime dependency. See [E/F evidence](https://github.com/owebeeone/yidl-dataclass/blob/main/docs/validation/stage-ef/README.md).
The [publication record](https://github.com/owebeeone/yidl-dataclass/blob/main/dev-docs/Publication.md) distinguishes the later initial
GitHub upload from the completed experiment and its measurements.

Releases use [Gearu](https://owebeeone.github.io/gearu/); see [RELEASE.md](https://github.com/owebeeone/yidl-dataclass/blob/main/RELEASE.md).
Release preparation and current checks are recorded in
[dev-docs/RELEASE_TODOS.md](https://github.com/owebeeone/yidl-dataclass/blob/main/dev-docs/RELEASE_TODOS.md). GitHub releases run
`.github/workflows/publish.yml`: both backends on all supported Python minors,
wheel checks and trusted publishing. The release tag must match the package
version, for example `v0.1.0`.
