import importlib.resources as resources,json,os,pathlib,runpy,sys
os.environ['ASTICHI_LOWER_ENGINE']=sys.argv[1]
import astichi,yidl,yidl_dataclass,yidl_undoable,yidl_lifecycle
from astichi.lower_engine.native import select_lower_engine
s=select_lower_engine();assert s.selected_engine==sys.argv[1] and s.fallback_scope is None
for package in (astichi,yidl,yidl_dataclass,yidl_undoable,yidl_lifecycle):assert pathlib.Path(package.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
for name in ('yidl_dataclass','yidl_undoable'):
 docs=resources.files(name).joinpath('documentation')
 assert docs.joinpath('README.md').is_file()
 assert docs.joinpath('docs/API.md').is_file()
 example=docs.joinpath('examples/first_use.py')
 with resources.as_file(example) as path:runpy.run_path(str(path),run_name='__main__')
print(json.dumps({'python':sys.version.split()[0],'backend':sys.argv[1],'isolated_original_origins':'pass','both_packaged_public_examples':'pass','scope':'Owner installed final package/public-resource smoke; complete corpus separately audited'}))
