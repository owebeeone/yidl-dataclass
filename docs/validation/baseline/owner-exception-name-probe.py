import os,sys
os.environ['ASTICHI_LOWER_ENGINE']=sys.argv[1]
from yidl_dataclass import dataclass,field,FieldInitializationError

def fail():raise ValueError('original callback')
@dataclass(repr=False)
class Names:
    Exception:int=0
    value:object=field(init=False,default_factory=fail,repr=False,compare=False)
try:Names()
except FieldInitializationError as error:assert isinstance(error.__cause__,ValueError)
else:raise AssertionError('expected wrapped factory failure')
print('Exception field preserves factory cause: pass')
