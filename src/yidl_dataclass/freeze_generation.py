"""Lower opt-in optimistic freezing to specialized YIDL methods and field hooks."""

from dataclasses import MISSING


def _freeze_typed_child(value):
    value.freeze()
    return value


def inferred_freeze(annotation):
    """Infer only resolved YIDL types; never guess from a method's spelling."""
    from .dataclass_definition import DataclassDefinition

    if not isinstance(annotation, type):
        return MISSING
    definition = getattr(annotation, "__yidl_dataclass_definition__", None)
    if isinstance(definition, DataclassDefinition) and definition.options.freezable:
        return _freeze_typed_child
    return MISSING


def add_freeze_facts(generated, builder, definition, captures):
    if not definition.options.freezable:
        return
    captures.update(_y_dc_getattr=getattr)
    for index, item in enumerate(definition.fields):
        if not item.kind.stored:
            continue
        hook = item.policy.freeze
        hook_name = f"_y_dc_freeze_{index}"
        if hook is not MISSING:
            captures[hook_name] = hook
        builder.add(
            generated.FreezeFieldsCollection,
            generated.DataclassFreezeField(
                freeze_field_id=f"Model.{item.name}",
                freeze_field_owner="Model",
                freeze_field_order=index,
                freeze_field_name=item.name,
                freeze_store_name=item.store_name,
                freeze_has_hook=hook is not MISSING,
                freeze_hook_name=hook_name,
            ),
        )
