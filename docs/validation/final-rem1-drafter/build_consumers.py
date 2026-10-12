"""Build only consumer wheels/sdists in external fresh verification storage."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[3]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('member',choices=('dataclass','undoable'))
    args=parser.parse_args()
    external=Path((Path(tempfile.gettempdir())/'yidl-dataclass-final-rem1-pointer.txt').read_text())
    project=ROOT if args.member=='dataclass' else ROOT.parent/'yidl_undoable'
    destination=external/(args.member+'-final')
    destination.mkdir()
    subprocess.run([sys.executable,'-m','hatchling','build','-d',str(destination)],cwd=project,check=True)
    rows=[{'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(destination.iterdir())]
    (ROOT/'docs/validation/final-rem1-drafter'/(args.member+'-artifacts.json')).write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps({'member':args.member,'artifacts':rows},sort_keys=True))

if __name__=='__main__':main()
