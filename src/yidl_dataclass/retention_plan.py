"""Pure direct-consumer retention facts; no instance liveness tables."""

from dataclasses import dataclass, replace


@dataclass(frozen=True, slots=True)
class RetainedProvider:
    field_name: str
    consumers: tuple[str, ...]
    lifetime: bool


def plan_retention(fields, calls, steps):
    by_name = {item.name: item for item in fields}
    consumers = {
        item.name: tuple(
            call.field_name
            for call in calls
            if by_name[call.field_name].kind.label == "lazy"
            and item.name in call.dependencies
        )
        for item in fields
        if item.kind.label == "initvar"
    }
    retention = tuple(
        RetainedProvider(
            name, names, any(by_name[consumer].mutable for consumer in names)
        )
        for name, names in consumers.items()
        if names
    )
    needed = {item.field_name for item in retention}
    fields = tuple(
        replace(
            item,
            retained=item.name in needed,
            provider_name=f"_y_dc_provider_{index}" if item.name in needed else "",
        )
        for index, item in enumerate(fields)
    )
    steps = tuple(
        replace(step, install=True) if step.field_name in needed else step
        for step in steps
    )
    return fields, steps, retention
