"""Pure conversion/mutability/layout resolution, separate from generated behavior."""

from dataclasses import replace, MISSING, InitVar
import inspect
import types
import typing
from .dataclass_markers import (
    FieldDeclaration,
    ConstDeclaration,
    LazyDeclaration,
    FieldPolicy,
)
from .field_kinds import ConstKind, LazyKind
from .errors import DataclassDefinitionError

_PRIMITIVES = (int, float, str, bytes, bool)
_ONE_VALUE_BUILTINS = (*_PRIMITIVES, list, dict, set, tuple)


def callback_contract(cls, name, role, callback):
    if any(callback is builtin for builtin in _ONE_VALUE_BUILTINS):
        return
    try:
        inspect.signature(callback).bind(object())
    except (TypeError, ValueError) as exc:
        raise DataclassDefinitionError(
            f"{cls.__qualname__}.{name}: {role} requires one positional value; wrap uninspectable callbacks"
        ) from exc


def derive_converter(cls, name, annotation):
    if isinstance(annotation, InitVar):
        annotation = annotation.type
    if any(annotation is primitive for primitive in _PRIMITIVES):
        return annotation, False
    if typing.get_origin(annotation) in (types.UnionType, typing.Union):
        args = typing.get_args(annotation)
        nonnull = tuple(arg for arg in args if arg is not type(None))
        if (
            len(args) == 2
            and len(nonnull) == 1
            and any(nonnull[0] is primitive for primitive in _PRIMITIVES)
        ):
            return nonnull[0], True
    raise DataclassDefinitionError(
        f"{cls.__qualname__}.{name}: unsupported conversion annotation; supply an explicit converter or converter=None"
    )


def normalize_policies(cls, fields, options, captures):
    if options.freezable and (options.frozen or not options.slots):
        raise DataclassDefinitionError("freezable requires slots=True and frozen=False")
    if options.freezable and any(
        "freeze" in base.__dict__
        for base in cls.__mro__
        if "__yidl_dataclass_definition__" not in base.__dict__
    ):
        raise DataclassDefinitionError("freezable reserves the freeze method name")
    if options.frozen and not options.slots:
        raise DataclassDefinitionError(
            f"{cls.__qualname__}: frozen requires slots=True"
        )
    result = []
    for index, item in enumerate(fields):
        if options.freezable and item.name == "freeze":
            raise DataclassDefinitionError("freezable reserves the freeze method name")
        declaration = cls.__dict__.get(item.name, MISSING)
        policy = (
            declaration.policy
            if isinstance(declaration, FieldDeclaration)
            else item.policy if item.inherited else FieldPolicy()
        )
        if isinstance(declaration, ConstDeclaration) and item.kind.label != "ordinary":
            raise DataclassDefinitionError(f"{item.name}: annotation kind conflict")
        if isinstance(declaration, LazyDeclaration) and item.kind.label != "ordinary":
            raise DataclassDefinitionError(f"{item.name}: annotation kind conflict")
        kind = (
            ConstKind()
            if isinstance(declaration, ConstDeclaration)
            else LazyKind() if isinstance(declaration, LazyDeclaration) else item.kind
        )
        if options.freezable and kind.stored and policy.freeze is MISSING:
            from .freeze_generation import inferred_freeze

            policy = replace(policy, freeze=inferred_freeze(item.field.type))
        if policy.freeze is not MISSING:
            if not options.freezable or not kind.stored:
                raise DataclassDefinitionError(
                    f"{item.name}: freeze requires a stored freezable field"
                )
            callback_contract(cls, item.name, "freeze", policy.freeze)
        converter = policy.converter
        nullable = False
        if kind.label == "classvar":
            if (
                policy.mutable is not None
                or converter is not MISSING
                or policy.validator is not None
                or policy.allow_self_factory
            ):
                raise DataclassDefinitionError(
                    f"{item.name}: ClassVar cannot have an instance policy"
                )
            converter = None
            mutable = False
        else:
            if kind.label == "initvar" and policy.mutable is not None:
                raise DataclassDefinitionError(
                    f"{item.name}: InitVar has no mutability policy"
                )
            if converter is MISSING:
                converter, nullable = (
                    derive_converter(cls, item.name, item.field.type)
                    if options.convert
                    else (None, False)
                )
            mutable = (
                True
                if kind.label == "local_store"
                else (
                    False
                    if kind.label in ("const", "initvar")
                    else (
                        not options.frozen if policy.mutable is None else policy.mutable
                    )
                )
            )
        if converter is not None:
            callback_contract(cls, item.name, "converter", converter)
        if policy.validator is not None:
            callback_contract(cls, item.name, "validator", policy.validator)
        has_pipeline = converter is not None or policy.validator is not None
        has_accessor = kind.stored and (
            kind.label == "lazy" or not mutable or has_pipeline or options.freezable
        )
        if (
            options.frozen
            and kind.stored
            and mutable
            and (item.field.compare or item.field.hash is True)
        ):
            raise DataclassDefinitionError(
                f"{item.name}: frozen writable field requires compare=False and hash=False"
            )
        store_name = f"_y_dc_store_{index}" if has_accessor else item.name
        result.append(
            replace(
                item,
                kind=kind,
                policy=policy,
                mutable=mutable,
                converter=converter,
                validator=policy.validator,
                nullable_converter=nullable,
                store_name=store_name,
                has_accessor=has_accessor,
                ready_name=f"_y_dc_ready_{index}" if kind.label == "lazy" else "",
                busy_name=f"_y_dc_busy_{index}" if kind.label == "lazy" else "",
            )
        )
        if converter is not None:
            captures[f"_y_dc_converter_{index}"] = converter
        if policy.validator is not None:
            captures[f"_y_dc_validator_{index}"] = policy.validator
        captures.update(
            {
                f"_y_dc_conversion_message_{index}": f"{cls.__qualname__}.{item.name}: converter failed",
                f"_y_dc_validation_message_{index}": f"{cls.__qualname__}.{item.name}: validator failed",
                f"_y_dc_validation_rejected_{index}": f"{cls.__qualname__}.{item.name}: validator rejected value",
                f"_y_dc_validation_contract_{index}": f"{cls.__qualname__}.{item.name}: validator must return None, True or False",
                f"_y_dc_factory_message_{index}": f"{cls.__qualname__}.{item.name}: factory failed",
                f"_y_dc_lazy_message_{index}": f"{cls.__qualname__}.{item.name}: lazy field busy or reentered",
                f"_y_dc_frozen_message_{index}": f"{cls.__qualname__}.{item.name}: cannot replace/delete read-only field {item.name}",
            }
        )
    policy_class = (
        options.frozen or options.freezable or any(item.has_accessor for item in result)
    )
    if policy_class:
        for base in cls.__mro__:
            if base is object:
                continue
            for name in (
                "__getattribute__",
                "__setattr__",
                "__delattr__",
                "__copy__",
                "__deepcopy__",
                "__getstate__",
                "__setstate__",
                "__reduce__",
                "__reduce_ex__",
            ):
                owned = base.__dict__.get("__yidl_generated_copy_methods__")
                if (
                    "__yidl_dataclass_definition__" in base.__dict__
                    and type(owned) is types.MappingProxyType
                    and name in owned
                    and owned[name] is base.__dict__.get(name)
                ):
                    continue
                if name in base.__dict__:
                    raise DataclassDefinitionError(
                        f"{cls.__qualname__}: policy interceptor {name} is unsupported"
                    )
    return tuple(result), policy_class
