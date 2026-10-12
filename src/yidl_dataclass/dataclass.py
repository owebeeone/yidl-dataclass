"""Consumer normalization and genuine YIDL/Astichi class execution."""

from __future__ import annotations
import dataclasses as std
from .dataclass_definition import DataclassOptions
from .dataclass_harvester import harvest
from .dataclass_markers import require_bool
from .stdlib_adapter import params_for


def dataclass(
    cls=None,
    /,
    *,
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
    match_args=True,
    kw_only=False,
    slots=True,
    weakref_slot=False,
    convert=False,
):
    options = DataclassOptions(
        init,
        repr,
        eq,
        order,
        unsafe_hash,
        frozen,
        match_args,
        kw_only,
        slots,
        weakref_slot,
        convert,
    )
    for name in options.__dataclass_fields__:
        require_bool(name, getattr(options, name))

    def decorate(declaration):
        from . import _generated_dataclass_base as generated

        definition, annotations, captures = harvest(declaration, options)
        names = {item.name for item in definition.fields}
        namespace = {
            name: value
            for name, value in declaration.__dict__.items()
            if name not in (*names, "__dict__", "__weakref__", "__classcell__")
        }
        namespace["__annotations__"] = annotations
        namespace["__dataclass_fields__"] = {
            item.name: item.field for item in definition.fields
        }
        namespace["__dataclass_params__"] = params_for(options)
        namespace["__yidl_dataclass_definition__"] = definition
        if options.match_args and "__match_args__" not in namespace:
            namespace["__match_args__"] = tuple(
                item.name
                for item in definition.fields
                if item.is_instance and item.field.init and not item.field.kw_only
            )
        for item in definition.fields:
            if item.field.default is not std.MISSING and (
                not item.is_instance or not options.slots
            ):
                namespace[item.name] = item.field.default
        captures.update(
            _y_dc_namespace=namespace,
            _y_dc_bases=declaration.__bases__,
            _y_dc_factory_sentinel=std._HAS_DEFAULT_FACTORY,
        )
        builder = generated.new_builder()
        builder.add(
            generated.ClassesCollection,
            generated.DataclassClass(
                class_id="Model",
                class_name=declaration.__name__,
                namespace_name="_y_dc_namespace",
                bases_name="_y_dc_bases",
                slot_names=definition.slot_names,
                use_slots=options.slots,
                generate_init=definition.generate_init,
            ),
        )
        for index, item in enumerate(definition.fields):
            if not item.is_instance:
                continue
            metadata = item.field
            install_default = (
                not metadata.init
                and metadata.default is not std.MISSING
                and options.slots
            )
            install_factory = (
                not metadata.init and metadata.default_factory is not std.MISSING
            )
            builder.add(
                generated.FieldsCollection,
                generated.DataclassField(
                    field_id=f"Model.{item.name}",
                    field_owner="Model",
                    field_name=item.name,
                    field_order=index,
                    annotation_name=item.annotation_name,
                    default_name=item.default_name,
                    factory_name=item.factory_name,
                    has_default=metadata.default is not std.MISSING,
                    has_factory=metadata.default_factory is not std.MISSING,
                    include_param=metadata.init,
                    param_order=item.parameter_order,
                    kw_only=metadata.kw_only,
                    install_default=install_default,
                    install_factory=install_factory,
                ),
            )
        composable = generated.build_DataclassModule(builder.freeze())
        source = composable.emit_commented()
        tree = composable.to_executable_ast()
        exec(
            compile(tree, "<yidl-dataclass-model>", "exec", dont_inherit=True), captures
        )
        model = captures[declaration.__name__]
        if not options.slots:
            for name, value in model.__dict__.items():
                if name not in ("__dict__", "__weakref__"):
                    setattr(declaration, name, value)
            model = declaration
        model.__yidl_generated_source__ = source
        return model

    return decorate if cls is None else decorate(cls)


def generated_source(cls):
    return cls.__yidl_generated_source__


def storage_fields(class_or_instance):
    return class_or_instance.__yidl_dataclass_definition__.fields


def replace(obj, /, **changes):
    # The Stage A ordinary subset follows the independent std helper directly.
    return std.replace(obj, **changes)
