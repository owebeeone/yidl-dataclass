"""Append explicit sanitation corrections without changing original raw hashes."""
import hashlib
import json
import os
import re
from pathlib import Path
import tempfile

EVIDENCE=Path(__file__).parent
RAW=Path(tempfile.gettempdir())/'yidl-dataclass-final-rem1-drafter-raw'
records=[json.loads(line) for line in (EVIDENCE/'increments.jsonl').read_text().splitlines()]
artifacts={row['path']:dict(row) for record in records for row in record['artifacts']}
correction_path=EVIDENCE/'sanitation-corrections.jsonl'
if correction_path.exists():
    for line in correction_path.read_text().splitlines():
        row=json.loads(line)
        artifacts[row['path']]['sha256']=row['sha256']
for path in sorted(EVIDENCE.iterdir()):
    if path.suffix not in ('.log','.xml'):continue
    before=path.read_bytes()
    after=before.replace(str(Path(os.sep,'opt','homebrew')).encode(),b'[package-runtime-root]')
    after=re.sub(rb"/(?:private/)?var/folders/[^\s'\"<>]*", b'[external-truncated-path]', after)
    if before==after:continue
    old=hashlib.sha256(before).hexdigest();new=hashlib.sha256(after).hexdigest()
    relative=path.relative_to(EVIDENCE.parents[2]).as_posix()
    assert artifacts[relative]['sha256']==old
    (RAW/(old+'.sanitized-before-correction')).write_bytes(before)
    path.write_bytes(after)
    correction={'path':relative,'prior_sanitized_sha256':old,'sha256':new,'original_raw_sha256':artifacts[relative]['raw_sha256'],'archived_prior_sanitized':'external:yidl-dataclass-final-rem1-drafter-raw/'+old+'.sanitized-before-correction','reason':'Remove remaining package-manager or truncated temporary runtime prefix from source-only distribution-test selection failures; original raw bytes and increment rows remain unchanged.'}
    with (EVIDENCE/'sanitation-corrections.jsonl').open('a') as stream:stream.write(json.dumps(correction,sort_keys=True)+'\n')
print('Explicit residual runtime-prefix corrections complete')
