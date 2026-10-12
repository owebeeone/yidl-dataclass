import datetime
import hashlib
import importlib.metadata
import importlib.resources
import json
import pathlib
import sys
import astichi
import yidl
import yidl_dataclass

root = pathlib.Path('external:public-author')
wheel = pathlib.Path('external:stage-g-artifacts/dataclass-final/yidl_dataclass-0.1.0.dev0-py3-none-any.whl')
wheel_hash = hashlib.sha256(wheel.read_bytes()).hexdigest()
assert wheel_hash == '50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b'
docs = importlib.resources.files('yidl_dataclass').joinpath('documentation')
initial = json.loads((root / 'start-doc-hashes.json').read_text())
final = {name: hashlib.sha256(docs.joinpath(name).read_bytes()).hexdigest() for name in initial}
assert initial == final
for manifest_name in ['first-attempt-manifest.json', 'repair-attempt-manifest.json']:
    for name, entry in json.loads((root / manifest_name).read_text()).items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == entry['sha256']
removed_line = '    cache: dict = field(default_factory=dict, mutable=True, compare=False, hash=False, repr=False)\n'
for attempt in ['01', '02']:
    with_source = (root / f'card4_with_cache_attempt{attempt}.py').read_text()
    without_source = (root / f'card4_without_cache_attempt{attempt}.py').read_text()
    line = removed_line if attempt == '01' else '    ' + removed_line
    assert with_source.count(line) == 1
    assert with_source.replace(line, '') == without_source
with_logical = json.loads((root / 'card4_with_cache_attempt02.stdout').read_text().splitlines()[0])['logical']
without_logical = json.loads((root / 'card4_without_cache_attempt02.stdout').read_text().splitlines()[0])['logical']
assert with_logical == without_logical
versions = {name: importlib.metadata.version(name) for name in ['yidl-dataclass', 'astichi', 'yidl']}
assert versions == {'yidl-dataclass': '0.1.0.dev0', 'astichi': '1.1.3', 'yidl': '0.1.0'}
origins = {module.__name__: str(pathlib.Path(module.__file__).resolve()) for module in [yidl_dataclass, astichi, yidl]}
assert all(pathlib.Path(origin).is_relative_to(pathlib.Path(sys.prefix).resolve()) for origin in origins.values())
result = {'checked_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'wheel_sha256': wheel_hash, 'docs_sha256': final, 'versions': versions,
          'public_module_origins': origins,
          'source_manifests_unchanged': True,
          'card4_only_declaration_removed_both_attempts': True,
          'card4_logical_results_identical': True}
(root / 'end-check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
