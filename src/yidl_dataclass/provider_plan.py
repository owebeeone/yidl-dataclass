"""Immutable signature binding and constructor DAG; no runtime provider lookup."""

from __future__ import annotations
from dataclasses import dataclass, MISSING
import inspect
from .errors import DataclassDefinitionError

_ZERO_ARG_BUILTINS = (list, dict, set, tuple, int, float, str, bytes, bool)


@dataclass(frozen=True, slots=True)
class FactoryArgument:
    name: str
    positional: bool
    provider: str = ""
    capture: str = ""
    instance: bool = False
    owner_class: bool = False


@dataclass(frozen=True, slots=True)
class FactoryCall:
    field_name: str
    arguments: tuple[FactoryArgument, ...]
    dependencies: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class InitializationStep:
    field_name: str
    order: int
    input: bool = False
    factory: bool = False
    default: bool = False
    fallback: bool = False
    class_provider: bool = False
    install: bool = True


def resolve_factory(cls, item, providers, captures, index):
    factory = item.field.default_factory
    if not callable(factory):
        raise DataclassDefinitionError(
            f"{cls.__qualname__}.{item.name}: factory must be callable"
        )
    if any(factory is builtin for builtin in _ZERO_ARG_BUILTINS):
        return FactoryCall(item.name, (), ())
    try:
        parameters = tuple(inspect.signature(factory).parameters.values())
    except (TypeError, ValueError) as exc:
        raise DataclassDefinitionError(
            f"{cls.__qualname__}.{item.name}: factory signature unavailable; wrap it in an introspectable function"
        ) from exc
    if any(p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD) for p in parameters):
        raise DataclassDefinitionError(
            f"{cls.__qualname__}.{item.name}: variadic factory signature is unsupported"
        )
    selected = {}
    dependencies = []
    for position, parameter in enumerate(parameters):
        name = parameter.name
        if name in providers:
            selected[position] = FactoryArgument(
                name, parameter.kind is parameter.POSITIONAL_ONLY, provider=name
            )
            dependencies.append(name)
        elif name == "cls":
            selected[position] = FactoryArgument(
                name, parameter.kind is parameter.POSITIONAL_ONLY, owner_class=True
            )
        elif name == "self":
            if not getattr(item, "allow_self_factory", False):
                raise DataclassDefinitionError(
                    f"{cls.__qualname__}.{item.name}: self factory requires allow_self_factory=True"
                )
            selected[position] = FactoryArgument(
                name, parameter.kind is parameter.POSITIONAL_ONLY, instance=True
            )
        elif parameter.default is parameter.empty:
            raise DataclassDefinitionError(
                f"{cls.__qualname__}.{item.name}: factory unknown required provider {name}"
            )
    last_positional = max(
        (index for index in selected if selected[index].positional), default=-1
    )
    for position in range(last_positional):
        if position not in selected:
            parameter = parameters[position]
            capture = f"_y_dc_arg_default_{index}_{position}"
            captures[capture] = parameter.default
            selected[position] = FactoryArgument(parameter.name, True, capture=capture)
    return FactoryCall(
        item.name,
        tuple(selected[position] for position in sorted(selected)),
        tuple(dependencies),
    )


def plan_initialization(cls, fields, options, generate_init, captures):
    if not generate_init:
        needs_init = options.frozen or any(
            item.kind.extension_init
            or item.has_accessor
            or item.converter is not None
            or item.validator is not None
            for item in fields
        )
        for item in fields:
            factory = item.field.default_factory
            if factory is MISSING or any(
                factory is builtin for builtin in _ZERO_ARG_BUILTINS
            ):
                continue
            try:
                parameters = inspect.signature(factory).parameters
            except (TypeError, ValueError):
                continue
            if any(
                name in {field.name for field in fields} or name in ("self", "cls")
                for name in parameters
            ):
                needs_init = True
        if needs_init:
            raise DataclassDefinitionError(
                f"{cls.__qualname__}: extension requires generated init"
            )
        return (), (), False
    by_name = {item.name: item for item in fields}
    calls = tuple(
        resolve_factory(cls, item, by_name, captures, index)
        for index, item in enumerate(fields)
        if item.field.default_factory is not MISSING
    )
    dependencies = {item.name: () for item in fields}
    for call in calls:
        dependencies[call.field_name] = call.dependencies
    active = []
    visited = set()

    def check_cycle(name):
        if name in active:
            path = active[active.index(name) :] + [name]
            raise DataclassDefinitionError(
                f"{cls.__qualname__}: factory cycle {' -> '.join(path)}"
            )
        if name in visited:
            return
        active.append(name)
        for provider in dependencies[name]:
            check_cycle(provider)
        active.pop()
        visited.add(name)

    for item in fields:
        check_cycle(item.name)
    consumed = {name for call in calls for name in call.dependencies}

    def available(item):
        return (
            (item.kind.parameter and item.field.init)
            or item.field.default is not MISSING
            or item.field.default_factory is not MISSING
        )

    for item in fields:
        if (
            item.kind.mandatory_source
            or item.has_accessor
            or item.converter is not None
            or item.validator is not None
        ) and not available(item):
            raise DataclassDefinitionError(
                f"{cls.__qualname__}.{item.name}: initialization source is unavailable"
            )
    for call in calls:
        for provider in call.dependencies:
            if not available(by_name[provider]):
                raise DataclassDefinitionError(
                    f"{cls.__qualname__}.{call.field_name}: factory unavailable provider {provider}; dependency path {call.field_name} -> {provider}"
                )
    remaining = {
        item.name
        for item in fields
        if available(item)
        and (item.kind.stored or item.kind.extension_init or item.name in consumed)
    }
    order = []
    while remaining:
        ready = [
            item.name
            for item in fields
            if item.name in remaining and not (set(dependencies[item.name]) & remaining)
        ]
        if not ready:
            raise AssertionError("acyclic constructor graph has no ready provider")
        name = ready[0]
        remaining.remove(name)
        order.append(name)
    steps = []
    for position, name in enumerate(order):
        item = by_name[name]
        metadata = item.field
        fallback = (
            item.kind.class_fallback
            and not item.has_accessor
            and not metadata.init
            and not options.slots
            and metadata.default is not MISSING
            and metadata.default_factory is MISSING
        )
        if fallback and name not in consumed:
            continue
        steps.append(
            InitializationStep(
                name,
                position,
                input=item.kind.parameter and metadata.init,
                factory=metadata.default_factory is not MISSING,
                default=metadata.default is not MISSING,
                fallback=fallback,
                class_provider=item.kind.label == "classvar",
                install=item.kind.stored and not fallback,
            )
        )
    return (
        tuple(steps),
        calls,
        bool(calls)
        or options.frozen
        or any(
            item.kind.extension_init
            or item.converter is not None
            or item.validator is not None
            or item.has_accessor
            for item in fields
        ),
    )
