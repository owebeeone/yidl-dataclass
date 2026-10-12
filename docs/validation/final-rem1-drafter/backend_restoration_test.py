"""Requested backend survives the preceding frozen benchmark CLI mock."""
import os
from astichi.lower_engine.native import select_lower_engine

def test_requested_backend_survives_frozen_cli_mock():
    expected=os.environ['REMEDIATION_EXPECTED_BACKEND']
    assert os.environ['ASTICHI_LOWER_ENGINE']==expected
    selection=select_lower_engine()
    assert selection.selected_engine==expected and selection.fallback_scope is None
