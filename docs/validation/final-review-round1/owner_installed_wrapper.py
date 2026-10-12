import importlib.metadata as metadata
import os
from pathlib import Path
import runpy
import sys
import astichi
import yidl
import yidl_dataclass
import yidl_undoable
import yidl_lifecycle
from astichi.lower_engine.native import select_lower_engine
selected = select_lower_engine()
assert selected.selected_engine == os.environ['ASTICHI_LOWER_ENGINE']
assert selected.fallback_scope is None
for package in (astichi, yidl, yidl_dataclass, yidl_undoable, yidl_lifecycle):
    assert Path(package.__file__).resolve().is_relative_to(Path(sys.prefix).resolve())
for name, version in (('astichi','1.1.3'),('yidl','0.1.0'),('yidl-lifecycle','0.1.0'),('yidl-dataclass','0.1.0.dev0'),('yidl-undoable','0.1.0')):
    assert metadata.version(name) == version
assert metadata.version('lark') == '1.3.1'
runpy.run_path(sys.argv[1], run_name='__main__')
