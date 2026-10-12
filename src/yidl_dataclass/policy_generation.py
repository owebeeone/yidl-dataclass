"""Lower field-local access/pipeline facts; callbacks stay in each exec namespace."""

from dataclasses import FrozenInstanceError
from .errors import FieldConversionError, FieldValidationError


def add_policy_facts(generated, builder, definition, captures):
    captures.update(
        _y_dc_FieldConversionError=FieldConversionError,
        _y_dc_FieldValidationError=FieldValidationError,
        _y_dc_FrozenInstanceError=FrozenInstanceError,
    )
    indexes = {item.name: index for index, item in enumerate(definition.fields)}

    def add_pipeline(item, constructor, value_name):
        index = indexes[item.name]
        builder.add(
            generated.PipelineSitesCollection,
            generated.DataclassPipelineSite(
                pipeline_id=f"Model.{item.name}.{'constructor' if constructor else 'setter'}",
                pipeline_owner=f"Model.{item.name}",
                constructor_site=constructor,
                pipeline_identity=index * 2 + (0 if constructor else 1),
                pipeline_value_name=value_name,
                has_converter=item.converter is not None,
                has_validator=item.validator is not None,
                nullable_converter=item.nullable_converter,
                converter_name=f"_y_dc_converter_{index}",
                validator_name=f"_y_dc_validator_{index}",
                conversion_message=f"_y_dc_conversion_message_{index}",
                validation_message=f"_y_dc_validation_message_{index}",
                validation_rejected=f"_y_dc_validation_rejected_{index}",
                validation_contract=f"_y_dc_validation_contract_{index}",
            ),
        )

    if definition.planned_init:
        by_name = {item.name: item for item in definition.fields}
        for step in definition.initialization:
            if not step.fallback and not step.class_provider:
                add_pipeline(
                    by_name[step.field_name],
                    True,
                    f"_y_dc_value_{indexes[step.field_name]}",
                )
    for index, item in enumerate(definition.fields):
        if not item.has_accessor:
            continue
        builder.add(
            generated.PolicyFieldsCollection,
            generated.DataclassPolicyField(
                field_id=f"Model.{item.name}",
                field_owner="Model",
                field_name=item.name,
                accessor_order=index,
                backing_name=item.store_name,
                writable_accessor=item.mutable,
                frozen_message=f"_y_dc_frozen_message_{index}",
            ),
        )
        if item.mutable:
            add_pipeline(item, False, "value")
