"""Lower the immutable constructor plan to original-SDK YIDL facts/captures."""

from .errors import (
    DataclassDefinitionError,
    FieldInitializationError,
    FieldConversionError,
    FieldValidationError,
    LazyInitializationError,
)


def add_initialization_facts(generated, builder, definition, declaration, captures):
    captures.update(
        _y_dc_type=type,
        _y_dc_Exception=Exception,
        _y_dc_TypeError=TypeError,
        _y_dc_AttributeError=AttributeError,
        _y_dc_ContextErrors=(
            DataclassDefinitionError,
            FieldInitializationError,
            FieldConversionError,
            FieldValidationError,
            LazyInitializationError,
        ),
        _y_dc_FieldInitializationError=FieldInitializationError,
    )
    if not definition.planned_init:
        return
    by_name = {item.name: item for item in definition.fields}
    values = {
        item.name: f"_y_dc_value_{index}"
        for index, item in enumerate(definition.fields)
    }
    calls = {call.field_name: call for call in definition.factory_calls}
    for step in definition.initialization:
        item = by_name[step.field_name]
        builder.add(
            generated.InitializationFieldsCollection,
            generated.DataclassInitializationField(
                field_id=f"Model.{item.name}",
                field_owner="Model",
                field_name=item.name,
                constructor_order=step.order,
                value_name=values[item.name],
                factory_name=item.factory_name,
                default_name=item.default_name,
                candidate_input=step.input,
                candidate_lazy=step.lazy,
                materialize_lazy=step.materialize,
                candidate_ready_name=item.ready_name,
                candidate_factory=step.factory,
                has_factory_arguments=(
                    bool(calls[item.name].arguments) if item.name in calls else False
                ),
                candidate_default=step.default,
                candidate_fallback=step.fallback,
                class_provider=step.class_provider,
                install_value=step.install,
                store_name=(
                    item.provider_name
                    if item.retained
                    else item.store_name or item.name
                ),
                factory_message=f"{declaration.__qualname__}.{item.name}: factory failed",
            ),
        )
    argument_identity = 0
    for call in definition.factory_calls:
        for index, argument in enumerate(call.arguments):
            builder.add(
                generated.FactoryArgumentsCollection,
                generated.DataclassFactoryArgument(
                    argument_id=f"Model.{call.field_name}.{index}",
                    caller_field_id=f"Model.{call.field_name}",
                    argument_order=index,
                    argument_identity=argument_identity,
                    argument_name=argument.name,
                    positional_argument=argument.positional,
                    instance_argument=argument.instance,
                    class_argument=argument.owner_class,
                    captured_argument=bool(argument.capture),
                    argument_capture=argument.capture,
                    provider_value=values.get(argument.provider, ""),
                    delayed_path=(
                        (
                            by_name[argument.provider].provider_name
                            or by_name[argument.provider].name
                        )
                        if argument.provider
                        else ""
                    ),
                    delayed_class_provider=bool(
                        argument.provider
                        and by_name[argument.provider].kind.label == "classvar"
                    ),
                ),
            )
            argument_identity += 1
