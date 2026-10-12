import dataclasses as dc
import dis
import inspect
import json
import sys
from typing import ClassVar

@dc.dataclass(slots=True, order=True, frozen=True)
class Model:
    kind: ClassVar[str] = 'model'
    seed: dc.InitVar[int] = 3
    value: int = 7
    cache: int = dc.field(default=0, compare=False, hash=False, repr=False, init=False)
    def __post_init__(self, seed):
        object.__setattr__(self, 'cache', seed)

calls=[]
class Operand:
    def __eq__(self, other):
        calls.append('eq')
        return True
@dc.dataclass
class Pair:
    first: object
    second: object
shared=Operand()
a,b=Pair(shared,shared),Pair(shared,shared)
assert a==b
shared_calls=list(calls)
calls.clear()
assert a==a
self_calls=list(calls)
assert dc.fields(Model)[0].name=='value'
assert dc.asdict(Model())=={'value':7,'cache':3}
assert dc.replace(Model(),value=11).value==11
assert not hasattr(Model(),'__dict__')
assert Model(2)==Model(9)
assert hash(Model(2))==hash(Model(9))
params=Model.__dataclass_params__
field=dc.fields(Model)[0]
result={
 'python':sys.version.split()[0],
 'field_type':type(field).__name__,
 'params_type':type(params).__name__,
 'params_slots':list(type(params).__slots__),
 'field_slots':list(type(field).__slots__),
 'field_function_parameters':list(inspect.signature(dc.field).parameters),
 'decorator_parameters':list(inspect.signature(dc.dataclass).parameters),
 'dataclass_params_signature':str(inspect.signature(dc._DataclassParams)),
 'get_field_signature':str(inspect.signature(dc._get_field)),
 'all_field_names':list(Model.__dataclass_fields__),
 'helper_field_names':[f.name for f in dc.fields(Model)],
 'match_args':list(Model.__match_args__),
 'shared_operand_eq_calls':shared_calls,
 'self_eq_calls':self_calls,
 'eq_bytecode_opnames':[instruction.opname for instruction in dis.get_instructions(Pair.__eq__)],
 'stdlib_helper_baseline':'pass',
}
print(json.dumps(result,sort_keys=True))
