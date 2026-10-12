"""Test-first supported names with callback identity and copy/state/hash/pickle."""

import builtins
import copy
import pickle
from support.result_name_models import MODELS, EVENTS, convert
from yidl_dataclass import generated_source


def render_case():
    EVENTS.clear()
    rows = []
    for model in MODELS:
        value = model()
        before = list(EVENTS)
        shallow = copy.copy(value)
        deep = copy.deepcopy(value)
        restored = model.__new__(model)
        restored.__setstate__(value.__getstate__())
        pickled = pickle.loads(pickle.dumps(value))
        assert all(
            item.value == 3 and item.__class__ is model
            for item in (shallow, deep, restored, pickled)
        )
        assert EVENTS == before
        if model.__name__ == "hash":
            assert builtins.hash(value) == builtins.hash((3,))
        if model.__name__ == "_y_dc_converter_0":
            assert value.__init__.__globals__["_y_dc_converter_0"] is convert
        rows.append(
            model.__name__ + ": copy,deepcopy,state,pickle,callback-identity=True"
        )
    assert EVENTS == [3]
    return {
        "generated_output.py": "\n".join(generated_source(model) for model in MODELS),
        "behavior.txt": "\n".join(rows)
        + "\nhash-builtin=True; no-generation-callbacks=True\n",
    }
