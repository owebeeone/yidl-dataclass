import hashlib
import importlib.metadata
import importlib.resources
import json
import pathlib
import sys

root = pathlib.Path('external:public-author')
wheel = pathlib.Path('external:stage-g-artifacts/dataclass-final/yidl_dataclass-0.1.0.dev0-py3-none-any.whl')
sha = hashlib.sha256(wheel.read_bytes()).hexdigest()
assert sha == '50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b'
print('wheel_sha256:', sha)
for name in ['yidl-dataclass', 'astichi', 'yidl']:
    print('distribution:', name, importlib.metadata.version(name))
import yidl_dataclass
import astichi
import yidl
for module in [yidl_dataclass, astichi, yidl]:
    origin = pathlib.Path(module.__file__).resolve()
    assert origin.is_relative_to(pathlib.Path(sys.prefix).resolve()), (module.__name__, origin)
    print('public_origin:', module.__name__, origin)
print('sys.prefix:', sys.prefix)
print('sys.path:', sys.path)
docs = importlib.resources.files('yidl_dataclass').joinpath('documentation')
hashes = {}
for name in ['README.md', 'docs/API.md', 'docs/Generation.md', 'examples/first_use.py']:
    data = docs.joinpath(name).read_bytes()
    hashes[name] = hashlib.sha256(data).hexdigest()
    target = root / 'public-docs' / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    print('\nPUBLIC DOCUMENT:', name, 'sha256:', hashes[name])
    print(data.decode())
(root / 'start-doc-hashes.json').write_text(json.dumps(hashes, indent=2) + '\n')
