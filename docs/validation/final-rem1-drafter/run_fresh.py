"""Launch own fresh pinned environments, never resolve editable SDK sources."""
import argparse
import os
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[3]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--minor',choices=('312','313','314'),default='312')
    parser.add_argument('--backend',choices=('native-rust','python'),default='native-rust')
    parser.add_argument('--member',choices=('dataclass','undoable'),default='dataclass')
    parser.add_argument('command',nargs=argparse.REMAINDER)
    args=parser.parse_args()
    external=Path((Path(tempfile.gettempdir())/'yidl-dataclass-final-rem1-pointer.txt').read_text())
    python=external/f'venv-{args.minor}'/'bin/python'
    command=args.command[1:] if args.command[:1]==["--"] else args.command
    command=["--junitxml="+str(ROOT/arg.split("=",1)[1]) if arg.startswith("--junitxml=") else arg for arg in command]
    member=ROOT if args.member=='dataclass' else ROOT.parent/'yidl_undoable'
    environment=dict(os.environ, ASTICHI_LOWER_ENGINE=args.backend, REMEDIATION_EXPECTED_BACKEND=args.backend, PYTHONPATH=os.pathsep.join((str(member/'src'),str(member/'tests'))), PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([str(python),*command],cwd=member,env=environment).returncode

if __name__=='__main__':
    raise SystemExit(main())
