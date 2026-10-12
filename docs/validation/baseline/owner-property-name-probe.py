import os,sys
os.environ['ASTICHI_LOWER_ENGINE']=sys.argv[1]
from yidl_dataclass import dataclass,const
@dataclass
class Names:
    property:int=const(default=1)
    other:int=const(default=2)
assert (Names().property,Names().other)==(1,2)
print('property field name and second descriptor: pass')
