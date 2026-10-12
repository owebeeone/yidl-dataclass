import os,sys
os.environ['ASTICHI_LOWER_ENGINE']=sys.argv[1]
from yidl_dataclass import dataclass,field
@dataclass(repr=False)
class Names:
    type:int=2
    owner:object=field(init=False,default_factory=lambda cls:cls,repr=False,compare=False)
x=Names()
assert x.type==2 and x.owner is Names
print('type field with class provider: pass')
