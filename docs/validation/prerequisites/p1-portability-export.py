import astichi,os,sys,pathlib
os.environ["ASTICHI_LOWER_ENGINE"]="python"
assert pathlib.Path(astichi.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
source="""astichi_bind_external(seed)
class Portable__astichi_arg__[T]:
    __slots__ = ("value",)
    def __init__(self):
        self.value = seed
    def read(self):
        return self.value
"""
piece=astichi.compile(source,file_name="portable/generic.py",arg_names={"Portable":"Frame"},keep_names=("self","__slots__","__init__","read","Frame","T"))
pathlib.Path(sys.argv[1]).write_bytes(astichi.export_compiled_template(piece))
