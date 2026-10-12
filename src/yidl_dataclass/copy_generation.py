"""Specialize storage protocol rows without any instance-value inspection."""

from copy import deepcopy
import sys
import types
from .copy_support import restore

COPY_METHODS = frozenset(
    ("__getstate__", "__setstate__", "__copy__", "__deepcopy__", "__reduce_ex__")
)


def helper_actions(declaration, definition):
    return (
        definition.policy_class,
        sys.version_info[:2] >= (3, 13) and "__replace__" not in declaration.__dict__,
    )


def add_copy_facts(
    generated, builder, definition, declaration, captures, package_replace
):
    storage_copy, generate_replace = helper_actions(declaration, definition)
    captures.update(
        _y_dc_deepcopy=deepcopy,
        _y_dc_restore=restore,
        _y_dc_replace=package_replace,
        _y_dc_copy_busy_message=f"{declaration.__qualname__}: active lazy copy/pickle is unsupported",
    )
    builder.add(
        generated.CopyClassesCollection,
        generated.DataclassCopyClass(
            cpy_class_id="Model",
            generate_storage_copy=storage_copy,
            generate_replace=generate_replace,
            has_storage_dictionary=not definition.options.slots,
        ),
    )
    if not storage_copy:
        return
    needed = [item.store_name for item in definition.fields if item.kind.stored]
    needed.extend(
        name
        for item in definition.fields
        if item.kind.label == "lazy"
        for name in (item.ready_name, item.busy_name)
    )
    needed.extend(item.provider_name for item in definition.fields if item.retained)
    inherited = [
        name
        for base in declaration.__mro__[1:]
        for name, value in base.__dict__.items()
        if isinstance(value, types.MemberDescriptorType)
        and name not in ("__weakref__", "__dict__")
    ]
    if definition.options.slots:
        slots = list(
            dict.fromkeys(
                (
                    *needed,
                    *(
                        name
                        for name in inherited
                        if not name.startswith("_y_dc_") or name in needed
                    ),
                )
            )
        )
    else:
        slots = list(dict.fromkeys(inherited))
    busy = tuple(
        item.busy_name for item in definition.fields if item.kind.label == "lazy"
    )
    # Dictionary-backed flags need guards but no duplicate numeric storage capture.
    rows = list(dict.fromkeys((*slots, *busy)))
    for index, name in enumerate(rows):
        builder.add(
            generated.StateSlotsCollection,
            generated.DataclassStateSlot(
                cpy_slot_id=f"Model.{name}",
                cpy_slot_owner="Model",
                cpy_slot_path=name,
                cpy_slot_index=index,
                cpy_is_busy=name in busy,
                cpy_is_slot=name in slots,
            ),
        )
