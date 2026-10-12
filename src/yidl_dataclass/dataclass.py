"""Consumer normalization and genuine YIDL/Astichi class execution."""

from __future__ import annotations
import dataclasses as std
import sys
from .method_actions import resolve_methods
from .dataclass_definition import DataclassOptions
from .dataclass_harvester import harvest
from .dataclass_markers import require_bool
from .stdlib_adapter import params_for, recursive_repr_decorator


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
        actions = resolve_methods(declaration, options)
        from .copy_generation import helper_actions, COPY_METHODS

        copy_support, generate_replace = helper_actions(declaration, definition)
        names = {item.name for item in definition.fields}
        from .inheritance_plan import namespace_value

        namespace = {
            name: namespace_value(value)
            for name, value in declaration.__dict__.items()
            if name not in (*names, "__dict__", "__weakref__", "__classcell__")
        }
        namespace.pop("__yidl_generated_copy_methods__", None)
        namespace["__qualname__"] = declaration.__qualname__
        namespace["__annotations__"] = annotations
        namespace["__dataclass_fields__"] = {
            item.name: item.field for item in definition.fields if item.kind.metadata
        }
        namespace["__dataclass_params__"] = params_for(options)
        namespace["__yidl_dataclass_definition__"] = definition
        if options.match_args and "__match_args__" not in namespace:
            namespace["__match_args__"] = tuple(
                item.name
                for item in definition.fields
                if item.kind.parameter and item.field.init and not item.field.kw_only
            )
        for item in definition.fields:
            if item.field.default is not std.MISSING and (
                item.kind.label == "classvar"
                or (item.is_instance and not item.has_accessor and not options.slots)
            ):
                namespace[item.name] = item.field.default
        captures.update(
            _y_dc_namespace=namespace,
            _y_dc_metaclass=type(declaration),
            _y_dc_bases=declaration.__bases__,
            _y_dc_factory_sentinel=std._HAS_DEFAULT_FACTORY,
            _y_dc_recursive_repr=recursive_repr_decorator(),
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
                has_planned_init=definition.planned_init,
                has_helper_methods=copy_support or generate_replace,
                has_lazy=any(item.kind.label == "lazy" for item in definition.fields),
                has_properties=any(item.has_accessor for item in definition.fields),
            ),
        )
        logical = tuple(
            item
            for item in definition.fields
            if item.is_instance and item.field.compare
        )
        hashed = tuple(
            item
            for item in definition.fields
            if item.is_instance
            and (
                item.field.hash is True
                or (item.field.hash is None and item.field.compare)
            )
        )
        hashed_names = {item.name for item in hashed}
        last_compare_name = logical[-1].name if logical else None
        hash_selection = actions.hash.lower()
        builder.add(
            generated.ComparisonClassesCollection,
            generated.ComparisonClass(
                cmp_class_id="Model",
                cmp_eq=actions.eq,
                cmp_order=actions.order,
                cmp_hash=hash_selection.generate,
                cmp_hash_none=hash_selection.disable,
                use_tuple_equality=sys.version_info[:2] == (3, 12),
                has_compare_operands=bool(logical),
                has_hash_operands=bool(hashed),
            ),
        )
        builder.add(
            generated.MethodClassesCollection,
            generated.DataclassMethodClass(
                repr_class_id="Model",
                generate_repr=actions.repr,
                has_repr_fields=any(
                    item.kind.stored and item.field.repr for item in definition.fields
                ),
            ),
        )
        for index, item in enumerate(definition.fields):
            if not (item.kind.stored or item.kind.parameter):
                continue
            metadata = item.field
            builder.add(
                generated.ComparisonOperandsCollection,
                generated.ComparisonOperand(
                    cmp_operand_id=f"Model.{item.name}",
                    cmp_owner="Model",
                    cmp_operand_order=index,
                    cmp_read_path=item.name,
                    cmp_compare=metadata.compare and item.is_instance,
                    cmp_hash_included=item.name in hashed_names,
                    cmp_last=item.name == last_compare_name,
                ),
            )
            builder.add(
                generated.ReprFieldsCollection,
                generated.DataclassReprField(
                    field_id=f"Model.{item.name}",
                    field_owner="Model",
                    field_name=item.name,
                    field_order=index,
                    include_repr=metadata.repr and item.kind.stored,
                ),
            )
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
        from .factory_generation import add_initialization_facts

        add_initialization_facts(generated, builder, definition, declaration, captures)
        from .policy_generation import add_policy_facts

        add_policy_facts(generated, builder, definition, captures)
        from .retention_generation import add_retention_facts

        add_retention_facts(generated, builder, definition)
        from .copy_generation import add_copy_facts

        add_copy_facts(generated, builder, definition, declaration, captures, replace)
        composable = generated.build_DataclassModule(builder.freeze())
        source = composable.emit_commented()
        tree = composable.to_executable_ast()
        # Output names belong to module locals; methods keep unmodified captures.
        results = {}
        exec(
            compile(tree, "<yidl-dataclass-model>", "exec", dont_inherit=True),
            captures,
            results,
        )
        model = results[declaration.__name__]
        if not options.slots:
            for name in names:
                if name in declaration.__dict__ and name not in model.__dict__:
                    delattr(declaration, name)
            for name, value in model.__dict__.items():
                if name not in ("__dict__", "__weakref__"):
                    setattr(declaration, name, value)
            model = declaration
        if options.slots:
            from .inheritance_plan import clone_class_cells

            clone_class_cells(declaration, model)
        from types import MappingProxyType

        model.__yidl_generated_copy_methods__ = MappingProxyType(
            {name: model.__dict__[name] for name in COPY_METHODS}
            if copy_support
            else {}
        )
        model.__yidl_generated_source__ = source
        return model

    return decorate if cls is None else decorate(cls)


def generated_source(cls):
    return cls.__yidl_generated_source__


def storage_fields(class_or_instance):
    return class_or_instance.__yidl_dataclass_definition__.fields


def replace(obj, /, **changes):
    definition = obj.__yidl_dataclass_definition__
    by_name = {item.name: item for item in definition.fields}
    for name in changes:
        item = by_name.get(name)
        if item is None or item.kind.label == "classvar":
            raise TypeError(f"unknown replacement field: {name}")
        if not item.field.init:
            raise ValueError(f"{name}: replacement of init=False field is unsupported")
    values = dict(changes)
    for item in definition.fields:
        if not item.kind.parameter or not item.field.init or item.name in values:
            continue
        if item.kind.label == "initvar":
            if (
                item.field.default is std.MISSING
                and item.field.default_factory is std.MISSING
            ):
                raise ValueError(f"{item.name}: required InitVar must be supplied")
        else:
            values[item.name] = getattr(obj, item.name)
    return type(obj)(**values)
