"""Owning class-creation and immutable inherited-field normalization."""

import abc
import copy
import inspect
import types
import sys
from dataclasses import replace
from .errors import DataclassDefinitionError


def model_base_for(cls, options):
    if type(cls) not in (type, abc.ABCMeta):
        raise DataclassDefinitionError(f"{cls.__qualname__}: unsupported metaclass")
    models = [
        base for base in cls.__bases__ if hasattr(base, "__yidl_dataclass_definition__")
    ]
    if len(models) > 1:
        raise DataclassDefinitionError(
            f"{cls.__qualname__}: multiple generated model bases are unsupported"
        )
    for base in cls.__mro__[1:]:
        if (
            "__dataclass_fields__" in base.__dict__
            and "__yidl_dataclass_definition__" not in base.__dict__
        ):
            raise DataclassDefinitionError(
                f"{cls.__qualname__}: stdlib dataclass base is unsupported"
            )
        if "__init_subclass__" in base.__dict__ and base is not object:
            try:
                inspect.signature(getattr(base, "__init_subclass__")).bind()
            except (TypeError, ValueError) as error:
                raise DataclassDefinitionError(
                    f"{cls.__qualname__}: subclass hook must support no-argument creation"
                ) from error
    model = models[0] if models else None
    if model is not None:
        if "__yidl_dataclass_definition__" not in model.__dict__:
            raise DataclassDefinitionError(
                "generated model base must be directly decorated"
            )
        options_base = model.__yidl_dataclass_definition__.options
        if options.freezable != options_base.freezable:
            raise DataclassDefinitionError(
                "freezable mixing in inheritance is unsupported"
            )
        if options.frozen != options_base.frozen:
            raise DataclassDefinitionError(
                f"{cls.__qualname__}: frozen mixing in inheritance is unsupported"
            )
        if options.slots != options_base.slots:
            raise DataclassDefinitionError(
                f"{cls.__qualname__}: incompatible storage in inheritance"
            )
    return model


def inherited_fields(model):
    if model is None:
        return ()
    return tuple(
        replace(item, field=copy.copy(item.field), inherited=True)
        for item in model.__yidl_dataclass_definition__.fields
    )


def validate_inherited_layout(cls, model, fields):
    if model is None:
        return
    prior = {item.name: item for item in model.__yidl_dataclass_definition__.fields}

    def family(item):
        return "eager" if item.kind.label in ("ordinary", "const") else item.kind.label

    for item in fields:
        old = prior.get(item.name)
        if old is not None and (
            family(item) != family(old)
            or item.mutable != old.mutable
            or item.has_accessor != old.has_accessor
        ):
            raise DataclassDefinitionError(
                f"{cls.__qualname__}: incompatible inherited field {item.name} family/storage/mutability"
            )


def clone_class_cells(declaration, model):
    """Clone only copied local functions; preserve all old and inherited cells."""

    def clone(function):
        if function is None or "__class__" not in function.__code__.co_freevars:
            return function
        cells = list(function.__closure__)
        position = function.__code__.co_freevars.index("__class__")

        def new_cell():
            return model

        cells[position] = new_cell.__closure__[0]
        copied = types.FunctionType(
            function.__code__,
            function.__globals__,
            function.__name__,
            function.__defaults__,
            tuple(cells),
        )
        copied.__kwdefaults__ = function.__kwdefaults__
        if sys.version_info[:2] >= (3, 14) and function.__annotate__ is not None:
            annotate = function.__annotate__
            copied.__annotate__ = (
                clone(annotate)
                if isinstance(annotate, types.FunctionType)
                else annotate
            )
        else:
            copied.__annotations__ = function.__annotations__.copy()
        if hasattr(function, "__type_params__"):
            copied.__type_params__ = function.__type_params__
        copied.__dict__.update(function.__dict__)
        copied.__module__ = function.__module__
        copied.__qualname__ = function.__qualname__
        copied.__doc__ = function.__doc__
        return copied

    for name, value in declaration.__dict__.items():
        if isinstance(value, types.FunctionType):
            replacement = clone(value)
        elif type(value) is classmethod:
            replacement = classmethod(clone(value.__func__))
        elif type(value) is staticmethod:
            replacement = staticmethod(clone(value.__func__))
        elif type(value) is property:
            replacement = property(
                clone(value.fget), clone(value.fset), clone(value.fdel), value.__doc__
            )
            if hasattr(value, "__name__"):
                replacement.__name__ = value.__name__
        else:
            continue
        if replacement is not value:
            setattr(model, name, replacement)
    abc.update_abstractmethods(model)


def namespace_value(value):
    """Do not let replacement set-name mutate an old builtin property wrapper."""
    if type(value) is property:
        return property(value.fget, value.fset, value.fdel, value.__doc__)
    return value
