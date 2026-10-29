# YIDL Dataclass

Build Python data models with explicit rules for individual fields. Ordinary
fields are writable slots. Add a converter for incoming text, a validator for
accepted values, a factory for a dependent value, or a lazy field for work that
should wait until first access.

When a model is assembled in stages, `freezable=True` adds a permanent `freeze()`
operation. You choose which fields cascade to child models or transform mutable
containers. When a model should be read-only from construction, use `frozen=True`.

## Learn in order

1. [Your first model](GettingStarted.md): install, declare fields, construct and inspect.
2. [Fields and generated behavior](Concepts.md): defaults, field families, equality and slots.
3. [Initialize dependent values](Initialization.md): factory arguments, hidden inputs and pipelines.
4. [Delay expensive values](LazyFields.md): first access, cached results and reset.
5. [Freeze a finished model](Freezing.md): field policies, shallow freezing and partial failure.
6. [Copy and extend models](ModelOperations.md): replacement, copying and inheritance.

Use the [API reference](API.md) for signatures, option constraints and callback
contracts, and [troubleshooting](Troubleshooting.md) for common errors.
The [runnable examples](../examples/README.md) are complete programs.

## Requirements

The release tests CPython 3.12–3.15 subject to the
[platform/backend boundary](GettingStarted.md#platform-and-backend-boundary).
Windows CPython 3.15 is outside the release qualification because Astichi 1.1.3
has no binary wheel for it and its source build has not been qualified.
Install `yidl-dataclass` from PyPI; its declared runtime dependencies are
Astichi 1.1.3 and YIDL 0.1.2. The library generates Python
methods from YIDL templates when you decorate a class. Application code imports
`yidl_dataclass`; it does not need to author YIDL. See [generation and source
inspection](Generation.md) when you want to inspect those methods.

Annotations do not automatically check runtime types. Ordinary models accept
values as supplied; select conversion and validation to enforce field rules.
The supported behavior overlaps stdlib `dataclasses`, with deliberate extensions
and constraints documented throughout these guides.
