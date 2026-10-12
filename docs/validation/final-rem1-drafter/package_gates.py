"""Verify frozen consumer distributions against original binary SDKs only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tarfile
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = Path(__file__).parent
EXTERNAL = Path((Path(tempfile.gettempdir()) / 'yidl-dataclass-final-rem1-pointer.txt').read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rebuild():
    result = {}
    for member in ('dataclass', 'undoable'):
        project = ROOT if member == 'dataclass' else ROOT.parent / 'yidl_undoable'
        folder = EXTERNAL / (member + '-final')
        wheel = next(folder.glob('*.whl'))
        sdist = next(folder.glob('*.tar.gz'))
        extracted = folder / 'sdist-extracted'
        extracted.mkdir()
        with tarfile.open(sdist) as archive:
            assert all(not Path(item.name).is_absolute() and '..' not in Path(item.name).parts for item in archive.getmembers())
            archive.extractall(extracted, filter='data')
        destination = folder / 'sdist-rebuilt'
        subprocess.run([str(EXTERNAL / 'venv-312/bin/python'), '-m', 'hatchling', 'build', '-t', 'wheel', '-d', str(destination)], cwd=next(extracted.iterdir()), check=True)
        rebuilt = next(destination.glob('*.whl'))
        assert sha(rebuilt) == sha(wheel), 'Consumer sdist did not reproduce exact wheel'
        package = 'yidl_' + member
        with zipfile.ZipFile(wheel) as archive:
            rows = {name: hashlib.sha256(archive.read(name)).hexdigest() for name in archive.namelist() if name.startswith(package + '/')}
            for name in ('py.typed', '_generated_' + member + '_base.py', 'regenerate_' + member + '_base.py', 'documentation/README.md', 'documentation/docs/API.md', 'documentation/examples/first_use.py'):
                assert package + '/' + name in rows
            for name in ('README.md', 'docs/API.md', 'examples/first_use.py'):
                assert archive.read(package + '/documentation/' + name) == (project / name).read_bytes()
            shared = package + '/yidl/shared/comparison.yidl'
            assert (shared in rows) == (member == 'dataclass')
            if member == 'dataclass':
                assert rows[shared] == '2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef'
        result[member] = {'wheel': wheel.name, 'wheel_sha256': sha(wheel), 'sdist': sdist.name, 'sdist_sha256': sha(sdist), 'rebuilt_wheel_sha256': sha(rebuilt), 'package_sha256': rows}
    (EVIDENCE / 'package-rebuilds.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print('Both consumer sdists reproduced byte-identical wheels; public bytes and resource ownership PASS')


def installed(args):
    python = EXTERNAL / ('venv-' + args.minor) / 'bin/python'
    env = dict(os.environ, ASTICHI_LOWER_ENGINE=args.backend, PYTHONDONTWRITEBYTECODE='1')
    env.pop('PYTHONPATH', None)
    if args.mode == 'provenance':
        result = subprocess.run([str(python), '-I', str(EVIDENCE / 'environment_probe.py')], cwd=EXTERNAL, env=env, check=True, capture_output=True)
        data = json.loads(result.stdout)
        assert data['selected_backend'] == args.backend
        (EVIDENCE / ('environment-' + args.minor + '-' + args.backend + '.json')).write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
        print(result.stdout.decode())
    else:
        script = '''import importlib.resources as r,runpy,pathlib,sys
from astichi.lower_engine.native import select_lower_engine
from yidl_dataclass.regenerate_dataclass_base import render_dataclass_base_source
from yidl_undoable.regenerate_undoable_base import check_undoable_base
selection=select_lower_engine()
assert selection.selected_engine==sys.argv[1] and selection.fallback_scope is None
assert render_dataclass_base_source()==r.files('yidl_dataclass').joinpath('_generated_dataclass_base.py').read_text()
assert check_undoable_base()==(True,'')
for package in ('yidl_dataclass','yidl_undoable'):
 root=r.files(package)
 assert pathlib.Path(str(root)).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
 runpy.run_path(str(root.joinpath('documentation/examples/first_use.py')),run_name='__main__')
print('installed-regeneration-public-examples=PASS')
'''
        subprocess.run([str(python), '-I', '-c', script, args.backend], cwd=EXTERNAL, env=env, check=True)


def without(args):
    wheelhouse = Path((Path(os.sep, 'tmp', 'yidl-dataclass-dependency-wheels-root.txt')).read_text().strip())
    python = EXTERNAL / ('venv-' + args.minor) / 'bin/python'
    target = EXTERNAL / ('venv-' + args.minor + '-without-authority')
    uv = str(Path(os.sep, 'opt', 'homebrew', 'bin', 'uv'))
    subprocess.run([uv, 'venv', '--python', str(python), str(target)], check=True)
    sdk = [wheelhouse / name for name in ('astichi-1.1.3-cp312-abi3-macosx_11_0_arm64.whl', 'yidl-0.1.0-py3-none-any.whl', 'yidl_cache-0.1.0-py3-none-any.whl', 'yidl_lifecycle-0.1.0-py3-none-any.whl')]
    expected = json.loads((ROOT / 'docs/validation/stage-g/artifact-tuple-final.json').read_text())['original_sdk_wheels']
    assert all(sha(path) == expected[path.name] for path in sdk)
    own = next((EXTERNAL / 'undoable-final').glob('*.whl'))
    subprocess.run([uv, 'pip', 'install', '--python', str(target / 'bin/python'), '--only-binary', ':all:', *map(str, sdk), str(own), 'pytest==9.0.2', 'black==26.3.1'], check=True)
    result = subprocess.run([str(target / 'bin/python'), '-I', '-c', "from importlib.util import find_spec; assert find_spec('yidl_dataclass') is None; from yidl_undoable import undoable; print('Undoable imports with Dataclass absent=PASS')"], cwd=EXTERNAL, check=True)
    print(json.dumps({'minor':args.minor,'original_sdk_wheel_sha256':{p.name:sha(p) for p in sdk},'undoable_wheel_sha256':sha(own),'dataclass_absent':True},sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('rebuild', 'provenance', 'smoke', 'without'))
    parser.add_argument('--minor', choices=('312', '313', '314'))
    parser.add_argument('--backend', choices=('native-rust', 'python'))
    args = parser.parse_args()
    if args.mode == 'rebuild': rebuild()
    elif args.mode == 'without': without(args)
    else: installed(args)


if __name__ == '__main__': main()
