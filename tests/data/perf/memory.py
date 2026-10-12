"""Allocation boundaries and memory inventory rows; no timing comparisons."""

import dataclasses as std
import gc
import sys
import tracemalloc


def memory_row(
    cls, count=10_000, *, initialize_ready=False, inputs="shared immutable integers"
):
    gc.collect()
    tracemalloc.start()
    try:
        baseline = tracemalloc.get_traced_memory()[0]
        pool = [cls() for _ in range(count)]
        if initialize_ready:
            for item in pool:
                item.delayed
        current = tracemalloc.get_traced_memory()[0]
        instance_bytes = sum(sys.getsizeof(item) for item in pool)
        dictionary_bytes = sum(
            sys.getsizeof(item.__dict__) for item in pool if hasattr(item, "__dict__")
        )
        after_inspection = tracemalloc.get_traced_memory()[0]
        row = {
            "instances": count,
            "instance_shallow_bytes_per_object": instance_bytes / count,
            "dict_shallow_bytes_per_object": dictionary_bytes / count,
            "allocation_bytes_per_object_including_pool": (current - baseline) / count,
            "allocation_bytes_per_object_after_dict_inspection": (
                after_inspection - baseline
            )
            / count,
            "allocation_boundary": "pool initialization before getsizeof/dictionary inspection",
            "inspection_effect": "dictionary inspection may materialize managed instance dictionaries; construction and after-inspection deltas reported separately",
            "list_pool_shallow_bytes": sys.getsizeof(pool),
            "input_values": inputs,
            "class_generation": "outside measurement",
            "units": "bytes/object",
            "public_dataclass_field_count": len(std.fields(cls)),
            "slot_names": list(getattr(cls, "__slots__", ())),
            "logical_model_size": "ordinary field count plus explicitly labeled extension/provider/storage variant",
        }
        del pool
        return row
    finally:
        tracemalloc.stop()
        gc.collect()
