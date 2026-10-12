"""Isolate the immutable H2 accounting mock's backend environment mutation."""
import os
from pathlib import Path
import pytest

@pytest.fixture(autouse=True)
def preserve_backend_after_frozen_cli_mock(request):
    target=Path(__file__).parent/'data/perf/test_gate_integrity.py'
    affected=(request.node.path==target and request.node.name=='test_failed_final_validation_preserves_completed_result')
    previous=os.environ.get('ASTICHI_LOWER_ENGINE')
    try:
        yield
    finally:
        if affected:
            if previous is None:
                os.environ.pop('ASTICHI_LOWER_ENGINE',None)
            else:
                os.environ['ASTICHI_LOWER_ENGINE']=previous
