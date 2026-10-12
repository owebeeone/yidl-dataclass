import astichi,ast,os,sys,pathlib,builtins,json
os.environ["ASTICHI_LOWER_ENGINE"]="python"
assert pathlib.Path(astichi.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
payload=pathlib.Path(sys.argv[1]).read_bytes()
original=builtins.compile
fresh=[]
def guarded(source,*args,**kwargs):
 if isinstance(source,(str,bytes,bytearray)):
  filename=args[0] if args else kwargs.get("filename")
  p=pathlib.Path(filename) if isinstance(filename,str) else None
  if p is not None and p.is_absolute() and p.is_file() and p.suffix==".py" and p.read_bytes()==(source.encode() if isinstance(source,str) else bytes(source)):
   return original(source,*args,**kwargs)
  fresh.append(type(source).__name__)
  raise AssertionError("runtime parsed source")
 return original(source,*args,**kwargs)
builtins.compile=guarded
try:
 p=astichi.load_compiled_template(payload)
 t=p.bind(seed=(41,"café",{"nested":[True,None]})).to_executable_ast()
finally:builtins.compile=original
ns={};exec(original(t,"<portable>","exec"),ns)
obj=ns["Frame"]()
assert obj.read()==(41,"café",{"nested":[True,None]})
assert not hasattr(obj,"__dict__")
assert not fresh
print(json.dumps({"consumer_python":sys.version.split()[0],"protected_source_compilations":0,"generic_class_execution":"pass","slotted":"pass"},sort_keys=True))
