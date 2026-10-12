"""Pure conversion/mutability/layout resolution, separate from generated behavior."""

from dataclasses import replace, MISSING, InitVar
import inspect
import types
import typing
from .dataclass_markers import FieldDeclaration, ConstDeclaration, FieldPolicy
from .field_kinds import ConstKind
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
    if options.frozen and not options.slots:
        raise DataclassDefinitionError(
            f"{cls.__qualname__}: frozen requires slots=True"
        )
    result = []
    for index, item in enumerate(fields):
        declaration = inspect.getattr_static(cls, item.name, MISSING)
        policy = (
            declaration.policy
            if isinstance(declaration, FieldDeclaration)
            else FieldPolicy()
        )
        if isinstance(declaration, ConstDeclaration) and item.kind.label != "ordinary":
            raise DataclassDefinitionError(f"{item.name}: annotation kind conflict")
        kind = ConstKind() if isinstance(declaration, ConstDeclaration) else item.kind
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
        has_accessor = kind.stored and (not mutable or has_pipeline)
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
                mutable=mutable,
                converter=converter,
                validator=policy.validator,
                nullable_converter=nullable,
                store_name=store_name,
                has_accessor=has_accessor,
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
                f"_y_dc_frozen_message_{index}": f"{cls.__qualname__}.{item.name}: cannot replace/delete read-only field {item.name}",
            }
        )
    policy_class = options.frozen or any(item.has_accessor for item in result)
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
                if name in base.__dict__:
                    raise DataclassDefinitionError(
                        f"{cls.__qualname__}: policy interceptor {name} is unsupported"
                    )
    return tuple(result), policy_class
