"""Wheel-only corpus with copied test helpers; owning pytest source fallback defeated."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[3]
EVIDENCE=Path(__file__).parent

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--minor',choices=('312','313','314'),required=True)
    parser.add_argument('--backend',choices=('native-rust','python'),required=True)
    parser.add_argument('--member',choices=('dataclass','undoable'),required=True)
    parser.add_argument('--attempt',default='v3')
    parser.add_argument('--without-authority',action='store_true')
    args=parser.parse_args()
    external=Path((Path(tempfile.gettempdir())/'yidl-dataclass-final-rem1-pointer.txt').read_text())
    project=ROOT if args.member=='dataclass' else ROOT.parent/'yidl_undoable'
    suffix='-without-authority' if args.without_authority else ''
    target=external/f'installed-{args.member}-{args.minor}-{args.backend}-{args.attempt}{suffix}'
    target.mkdir()
    shutil.copytree(project/'tests',target/'tests',ignore=shutil.ignore_patterns('__pycache__','.pytest_cache',*(['perf'] if args.member=='dataclass' else [])))
    plugin=target/'origin_guard.py'
    plugin.write_text('''from importlib import util,metadata\nfrom pathlib import Path\nimport sys\nfrom astichi.lower_engine.native import select_lower_engine\ndef pytest_sessionstart(session):\n for name in ('astichi','yidl','yidl_cache','yidl_lifecycle','yidl_dataclass','yidl_undoable'):\n  assert Path(util.find_spec(name).origin).resolve().is_relative_to(Path(sys.prefix).resolve()), name\n assert metadata.version('astichi')=='1.1.3' and metadata.version('yidl')=='0.1.0'\n assert metadata.version('lark')=='1.3.1'\n selection=select_lower_engine()\n assert selection.selected_engine==''' + repr(args.backend)+''' and selection.fallback_scope is None\n''')
    if args.without_authority:
        plugin.write_text(plugin.read_text().replace("'yidl_dataclass',",'')+"\n from importlib.util import find_spec\n assert find_spec('yidl_dataclass') is None\n")
    assert not (target/'src').exists() and not (target/'pyproject.toml').exists()
    xml=EVIDENCE/f'rem1-installed-{args.member}-{args.minor}-{args.backend}-{args.attempt}{suffix}-verification.junit.xml'
    command=[str(external/f'venv-{args.minor}{suffix}/bin/python'),'-I','-m','pytest','-c',os.devnull,'-p','no:cacheprovider','--override-ini',f'pythonpath={target}:{target/"tests"}','-q',str(target/'tests'), '--junitxml='+str(xml)]
    if args.member=='dataclass':
        command.extend('--ignore='+str(target/'tests'/name) for name in ('test_installation.py','test_distribution_contract.py'))
    else:
        command.append('--ignore='+str(target/'tests/test_distribution_contract.py'))
    if args.without_authority:
        command.extend(['--ignore='+str(target/'tests/test_generation.py'), '-k', 'not 11_layers and not test_undoable_scope_does_not_change_dataclass_equality'])
    environment=dict(os.environ,ASTICHI_LOWER_ENGINE=args.backend,PYTHONDONTWRITEBYTECODE='1')
    environment.pop('PYTHONPATH',None)
    # Bootstrap only the test plugin/helper path; installed consumer/SDK origins remain guarded.
    rootconftest=target/'tests/conftest.py'
    old=rootconftest.read_text() if rootconftest.exists() else ''
    rootconftest.write_text(old+'\n'+plugin.read_text())
    return subprocess.run(command,cwd=target,env=environment).returncode

if __name__=='__main__':raise SystemExit(main())
