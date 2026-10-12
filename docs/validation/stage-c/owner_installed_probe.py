import os,sys,pathlib,json,dataclasses as std
os.environ['ASTICHI_LOWER_ENGINE']=sys.argv[1]
import astichi,yidl,yidl_dataclass as p
from astichi.lower_engine.native import select_lower_engine
selected=select_lower_engine()
assert selected.selected_engine==sys.argv[1] and selected.fallback_scope is None
for module in (astichi,yidl,p):
    assert pathlib.Path(module.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())

def positive(value):
    if value==99:
        return 1
    if value<0:
        return False
    return None

@p.dataclass(kw_only=True)
class Quote:
    total:int=p.field(init=False,default_factory=lambda quantity,price:quantity*price)
    quantity:int=p.field(default_factory=lambda seed:seed+1,converter=int,validator=positive)
    price:int=p.const(default=3,converter=int)
    cache:dict=p.local_store(default_factory=dict)
    seed:int=p.initvar(converter=int)

q=Quote(seed=2.9)
assert (q.quantity,q.price,q.total)==(3,3,9)
assert not hasattr(q,'seed')
q.quantity=2.9
assert q.quantity==2 and q.total==9
old=q.quantity
for value,expected in ((-1,p.FieldValidationError),('invalid',p.FieldConversionError),(99,TypeError)):
    try:
        q.quantity=value
    except expected as error:
        if value=='invalid':
            assert isinstance(error.__cause__,ValueError)
    else:
        raise AssertionError((value,'assignment accepted'))
    assert q.quantity==old
try:
    q.price=4
except std.FrozenInstanceError:
    pass
else:
    raise AssertionError('const assignment accepted')
q.cache['memo']=1
other=Quote(seed=1)
assert other.cache=={}

@p.dataclass(frozen=True)
class Frozen:
    value:int=4
    cache:dict=p.local_store(default_factory=dict)
f=Frozen(); f.cache={'memo':7}
assert f.cache=={'memo':7} and hash(f)==hash((4,))
try:
    f.value=5
except std.FrozenInstanceError:
    pass
else:
    raise AssertionError('frozen assignment accepted')

try:
    @p.dataclass(kw_only=True)
    class Missing:
        provider:int=p.field(init=False)
        consumer:int=p.field(init=False,default_factory=lambda provider=17:provider)
except p.DataclassDefinitionError as error:
    assert 'provider' in str(error) and 'consumer' in str(error)
else:
    raise AssertionError('unavailable optional known provider accepted')

@p.dataclass(slots=False)
class Fallback:
    value:int=p.field(init=False,default=4)
    consumed:int=p.field(init=False,default_factory=lambda value:value+1)
assert Fallback().consumed==5
Fallback.value=8
assert Fallback().consumed==9
print(json.dumps({'python':sys.version.split()[0],'backend':sys.argv[1], 'scope':'Stage C extension subset only; lazy/inheritance/copy deferred','dependency_order_and_processed_providers':'pass','hidden_provider':'pass','atomic_pipeline_failures':'pass','readonly_and_frozen_cache':'pass','unavailable_optional_provider':'pass'},sort_keys=True))
