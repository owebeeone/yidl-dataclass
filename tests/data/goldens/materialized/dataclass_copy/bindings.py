"""Test-first ready/absent storage copying and memo/pickle preservation."""

import copy
import pickle
from support.copy_models import CopyModel, EVENTS
from yidl_dataclass import storage_fields, generated_source


def render_case():
    EVENTS.clear()
    first = CopyModel([1])
    first.values.append([2])
    first.management.append("work")
    first.loop = first
    provider = storage_fields(CopyModel)[0].provider_name
    shallow = copy.copy(first)
    deep = copy.deepcopy(first)
    assert EVENTS == []
    assert shallow.values is first.values and shallow.management is first.management
    assert shallow.loop is first and deep.loop is deep
    assert (
        deep.values == first.values
        and deep.values is not first.values
        and deep.values[0] is not first.values[0]
    )
    assert getattr(shallow, provider) is getattr(first, provider) and getattr(
        deep, provider
    ) is not getattr(first, provider)
    unready = pickle.loads(pickle.dumps(first))
    assert EVENTS == [] and unready.loop is unready and unready.management == ["work"]
    assert first.cache == [1] and EVENTS == ["cache"]
    ready_shallow = copy.copy(first)
    ready_deep = copy.deepcopy(first)
    ready_pickle = pickle.loads(pickle.dumps(first))
    assert EVENTS == ["cache"]
    assert ready_shallow.cache is first.cache
    assert ready_deep.cache == first.cache and ready_deep.cache is not first.cache
    assert ready_pickle.cache == first.cache and EVENTS == ["cache"]
    # Explicit primitive readiness/absence is a public protocol requirement.
    state = first.__getstate__()
    assert type(state) is tuple and type(state[0]) is int and state[0] == 1
    assert type(state[1]) is dict
    return {
        "generated_output.py": generated_source(CopyModel),
        "behavior.txt": "unready-no-callback=True; shallow-alias=True; deepcopy-memo=True; retained-provider-copied=True; pickle-ready-absent=True; explicit-state-version=1\n",
    }
