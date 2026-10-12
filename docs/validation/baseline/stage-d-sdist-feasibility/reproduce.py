import hashlib,json,pathlib,subprocess,sys,tarfile,zipfile
root=pathlib.Path(sys.argv[1])
folder=root/'stage-d-sdist-feasibility';sdist=folder/'yidl_dataclass-0.1.0.dev0.tar.gz'
extracted=folder/'extracted';extracted.mkdir(exist_ok=True)
with tarfile.open(sdist) as archive:
 members=archive.getmembers()
 assert all(not pathlib.PurePosixPath(m.name).is_absolute() and '..' not in pathlib.PurePosixPath(m.name).parts for m in members)
 archive.extractall(extracted,filter='data')
source=extracted/'yidl_dataclass-0.1.0.dev0'
subprocess.run([str(root/'venv-3.12/bin/python'),'-m','hatchling','build','-t','wheel','-d',str(folder/'rebuilt')],cwd=source,check=True,capture_output=True,text=True)
wheel=folder/'rebuilt/yidl_dataclass-0.1.0.dev0-py3-none-any.whl'
original=root/'stage-d-wheels/yidl_dataclass-0.1.0.dev0-py3-none-any.whl'
def package_members(path):
 with zipfile.ZipFile(path) as archive:
  return {n:hashlib.sha256(archive.read(n)).hexdigest() for n in archive.namelist() if n.startswith('yidl_dataclass/')}
first,second=package_members(original),package_members(wheel)
assert first==second
names=list(second)
assert 'yidl_dataclass/py.typed' in names
assert 'yidl_dataclass/_generated_dataclass_base.py' in names
assert 'yidl_dataclass/regenerate_dataclass_base.py' in names
assert 'yidl_dataclass/yidl/shared/comparison.yidl' in names
out={'boundary':'Owner pre-G feasibility only at verified D runtime; no final packaged corpus or public authoring claim',
 'sdist_sha256':hashlib.sha256(sdist.read_bytes()).hexdigest(),'rebuilt_wheel_sha256':hashlib.sha256(wheel.read_bytes()).hexdigest(),
 'original_wheel_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),
 'package_files_identical':True,'package_file_count':len(names),'yidl_resource_count':sum(n.endswith('.yidl') for n in names),
 'py_typed_generated_base_regeneration_and_shared_authority':'present','dependencies_rebuilt':False}
(folder/'result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
