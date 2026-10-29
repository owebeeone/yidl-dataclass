# Copy and extend models

Use inspection helpers to describe public data, replacement to construct an
updated model, and copy/pickle to preserve current instance state. These operations
have different effects on factories, lazy values and hidden constructor inputs.

## Inspect public fields or storage policies

`fields`, `is_dataclass`, `asdict` and `astuple` are the standard `dataclasses`
helpers re-exported by this package. They omit InitVars, ClassVars, local stores
and private state. `asdict` and `astuple` read public fields and recursively copy
their values, so they can evaluate lazy fields and propagate getter errors.
Their normal cyclic-graph limitations still apply.

`storage_fields(Model)` includes extension and management kinds as well as
ordinary fields. Use it to inspect policies and dependency names, without gaining
access to retained hidden provider values.

```python
from yidl_dataclass import asdict, dataclass, field, fields, local_store, storage_fields

@dataclass
class Task:
    title: str
    labels: list = field(default_factory=list)
    cache: dict = local_store(default_factory=dict)

task = Task("Write docs")
assert [item.name for item in fields(task)] == ["title", "labels"]
assert [item.name for item in storage_fields(task)] == ["title", "labels", "cache"]
assert asdict(task) == {"title": "Write docs", "labels": []}
```

## Replace means reconstruct

```python
from yidl_dataclass import replace

new_task = replace(task, title="Review docs")
assert new_task.title == "Review docs" and task.title == "Write docs"
assert new_task.labels is task.labels
assert new_task.cache is not task.cache
```

`replace` calls the model constructor. Unchanged `init=True` public fields are
read from the original, including lazy fields when they accept constructor input.
`init=False` factories, lazy caches and management storage rebuild. Changes to
unknown or `init=False` fields are errors. Required `init=True` InitVars must be
supplied again. Omitted defaulted or factory-backed InitVars use their declaration
again; hidden retained values are never replayed.

Prefer the package helper over `dataclasses.replace` when using hidden InitVars.
The stdlib helper's omitted/defaulted hidden InitVar getter behavior is outside
the supported subset. On CPython 3.13–3.15, generated `__replace__` supports
`copy.replace`; a local custom method is preserved. No method is added on 3.12.
Replacing a runtime-frozen model creates a mutable model, but unchanged child
references may still point to frozen children.

## Copy means preserve state

```python
from copy import copy, deepcopy

shallow = copy(task)
deep = deepcopy(task)
assert shallow.labels is task.labels
assert deep.labels is not task.labels
```

Copy, deepcopy and pickle preserve ready/unready/absent storage, lazy caches,
management state, still-retained InitVars and runtime-frozen state without
running lazy factories. Shallow copy shares values; deepcopy uses its memo to
preserve sharing and cycles where supported. Pickle requires a normally importable
module-level model class. Lazy evaluation or runtime freezing in progress makes
copying/pickling fail rather than capturing an intermediate state. Policy models
reject custom copy/state/reduction hooks that would bypass this behavior.

## Extend one generated base

```python
@dataclass
class BaseRecord:
    key: str

@dataclass
class DetailedRecord(BaseRecord):
    description: str = ""

record = DetailedRecord("A1", "ready")
assert record.key == "A1"
assert [item.name for item in fields(record)] == ["key", "description"]
```

The supported subset is one generated model base plus compatible plain mixins.
Fields merge in reverse-MRO order; an override retains the field's position and
can change defaults, factories, pipelines and participation options. It cannot
change field family, storage shape or effective mutability. The merged dependency
graph is checked again. Frozen and nonfrozen models cannot mix, and freezable
settings must agree throughout a model hierarchy.

Slotted models reject bases with an instance dictionary. Mixins for those models
must be compatible with that restriction, for example by declaring `__slots__ = ()`.
Multiple generated bases and stdlib-dataclass bases are rejected. An undecorated
subclass inherits behavior but does not acquire newly declared field metadata.
Decorate each subclass whose annotations should add fields.

See [the reference](API.md#inheritance-and-explicit-exclusions) before adding
custom metaclasses, attribute access or copy methods. Slotted decoration replaces
the class and can repeat a base's `__init_subclass__` callback; supported copied
methods retain zero-argument `super()` behavior through fresh class cells.
