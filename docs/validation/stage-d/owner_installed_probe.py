import os,sys,pathlib,json,copy,weakref,gc,dataclasses as std,inspect
os.environ['ASTICHI_LOWER_ENGINE']=sys.argv[1]
import astichi,yidl,yidl_dataclass as p
from astichi.lower_engine.native import select_lower_engine
selected=select_lower_engine()
assert selected.selected_engine==sys.argv[1] and selected.fallback_scope is None
for module in (astichi,yidl,p):
    assert pathlib.Path(module.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
class Seed:
    def __init__(self,value): self.value=value
calls=[]
def compute(seed):
    calls.append(seed.value)
    return seed.value*2
@p.dataclass(frozen=True)
class Delayed:
    seed:object=p.initvar()
    total:int=p.lazy(default_factory=compute,repr=False,compare=False,hash=False)
    cache:dict=p.local_store(default_factory=dict)
s=Seed(4); ref=weakref.ref(s); original=Delayed(seed=s);del s
assert calls==[] and ref() is not None and not hasattr(original,'seed')
shallow=copy.copy(original); deep=copy.deepcopy(original)
assert calls==[] and shallow.cache is original.cache and deep.cache is not original.cache
assert original.total==8 and calls==[4] and ref() is not None
assert shallow.total==8 and calls==[4,4]
gc.collect();assert ref() is None
assert deep.total==8 and calls==[4,4,4]
assert [f.name for f in std.fields(original)]==['total']
assert std.asdict(original)=={'total':8}
replacement=p.replace(original,seed=Seed(9))
assert calls==[4,4,4] and replacement.total==18
attempts=[]
def flaky(seed):
    attempts.append(seed.value)
    if len(attempts)==1: raise ValueError('retry')
    return seed.value
@p.dataclass
class Resettable:
    seed:object=p.initvar()
    total:int=p.lazy(default_factory=flaky,mutable=True,repr=False,compare=False,hash=False)
s=Seed(5);ref=weakref.ref(s);r=Resettable(seed=s);del s
try: r.total
except p.FieldInitializationError as error: assert isinstance(error.__cause__,ValueError)
else: raise AssertionError('lazy failure absent')
assert r.total==5 and ref() is not None
r.total=12;assert r.total==12 and attempts==[5,5]
del r.total;assert r.total==5 and attempts==[5,5,5] and ref() is not None
del r;gc.collect();assert ref() is None

@p.dataclass
class Base:
    x:int=3
    def greeting(self):return 'base'
class OriginalChild(Base):
    x:int=6
    y:int=p.field(default=4,kw_only=True)
    def greeting(self):return super().greeting()+' child'
old_function=OriginalChild.greeting
old_cell=old_function.__closure__[old_function.__code__.co_freevars.index('__class__')]
old_class=OriginalChild
Child=p.dataclass(OriginalChild)
assert Child().greeting()=='base child'
assert old_cell.cell_contents is old_class
assert Child.greeting.__closure__[Child.greeting.__code__.co_freevars.index('__class__')].cell_contents is Child
assert set(Child.__slots__)=={'y'}
assert [field.name for field in std.fields(Child)]==['x','y']
assert std.asdict(Child())=={'x':6,'y':4}
assert inspect.signature(Child).parameters['y'].kind is inspect.Parameter.KEYWORD_ONLY
plain=p.replace(Child(),y=11)
assert (plain.x,plain.y)==(6,11)
assert std.replace(Child(),y=12).y==12
if sys.version_info[:2]>=(3,13):
    assert copy.replace(Child(),y=13).y==13
else:
    assert '__replace__' not in Child.__dict__
print(json.dumps({'python':sys.version.split()[0],'backend':sys.argv[1],'lazy_copy_and_retention_release':'pass','hidden_provider_helpers':'pass','replace_reconstruction':'pass','retry_mutable_reset_retention':'pass','scope':'Stage D bounded extension subset; full installed/Undoable/perf gates separate'},sort_keys=True))
