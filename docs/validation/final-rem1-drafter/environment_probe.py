"""Installed original artifact/version/origin evidence for fresh environments."""
import hashlib
from importlib import metadata, util
import json
from pathlib import Path
import sys
from astichi.lower_engine.native import select_lower_engine

rows={}
for dist in sorted(metadata.distributions(),key=lambda d:d.metadata['Name'].lower()):
    name=dist.metadata['Name']
    rows[name]={'version':dist.version,'metadata_sha256':hashlib.sha256(dist.read_text('METADATA').encode()).hexdigest(),'record_sha256':hashlib.sha256((dist.read_text('RECORD') or '').encode()).hexdigest()}
origins={}
for name in ('astichi','yidl','yidl_cache','yidl_lifecycle','yidl_dataclass','yidl_undoable','lark','pytest','hatchling','black','build'):
    path=Path(util.find_spec(name).origin).resolve()
    assert path.is_relative_to(Path(sys.prefix).resolve())
    origins[name]=path.relative_to(Path(sys.prefix).resolve()).as_posix()
assert rows['astichi']['version']=='1.1.3' and rows['yidl']['version']=='0.1.0'
assert rows['lark']['version']=='1.3.1'
selection=select_lower_engine()
assert selection.fallback_scope is None
print(json.dumps({'python':sys.version.split()[0],'selected_backend':selection.selected_engine,'fallback_scope':selection.fallback_scope,'origins_relative_to_prefix':origins,'distributions':rows,'scope':'Fresh binary-wheel-only installation; no dependency build or repair'},sort_keys=True))
