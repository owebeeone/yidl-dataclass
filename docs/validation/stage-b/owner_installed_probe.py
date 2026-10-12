import os, sys, dataclasses as std, json, inspect, pathlib, importlib.metadata
os.environ['ASTICHI_LOWER_ENGINE'] = sys.argv[1]
import astichi, yidl, yidl_dataclass as product
for module in (astichi, yidl, product):
    assert pathlib.Path(module.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
assert importlib.metadata.version('astichi') == '1.1.3'
assert importlib.metadata.version('yidl') == '0.1.0'
from astichi.lower_engine.native import select_lower_engine
selection = select_lower_engine()
assert selection.selected_engine == sys.argv[1] and selection.fallback_scope is None

def observe(decorator, field):
    attrs = {'__module__': __name__, '__annotations__': {'first': int, 'second': int, 'cache': int}, 'second': 2, 'cache': field(default=99, repr=False, compare=False, hash=False)}
    Model = decorator(type('Model', (), attrs), order=True, unsafe_hash=True, slots=True)
    a, b, c = Model(1), Model(1, cache=77), Model(2)
    assert a == b and a < c and a <= b and c > a and c >= a
    assert Model.__eq__(a, object()) is NotImplemented
    assert Model.__lt__(a, object()) is NotImplemented
    return_value = {'repr': repr(a), 'hash': hash(a), 'equality': a == b, 'less': a < c,
                    'signature': tuple(inspect.signature(Model).parameters),
                    'methods': tuple(name for name in ('__eq__', '__lt__', '__le__', '__gt__', '__ge__', '__hash__') if name in Model.__dict__)}
    Empty = decorator(type('Empty', (), {'__module__': __name__}), order=True, unsafe_hash=True, slots=True)
    assert Empty() == Empty() and not Empty() < Empty() and hash(Empty()) == hash(())
    Mutable = decorator(type('Mutable', (), {'__module__': __name__, '__annotations__': {'value': int}}), slots=True)
    assert Mutable.__hash__ is None
    Identity = decorator(type('Identity', (), {'__module__': __name__, '__annotations__': {'value': int}}), eq=False, slots=True)
    assert Identity(1) != Identity(1)
    Local = decorator(type('Local', (), {'__module__': __name__, '__annotations__': {'value': int}, '__eq__': lambda self, other: 'local'}), slots=True)
    assert Local.__eq__(Local(1), object()) == 'local'
    Recursive = decorator(type('Recursive', (), {'__module__': __name__, '__annotations__': {'value': object}}), slots=True)
    r = Recursive(None); r.value = r
    return_value['recursive_repr'] = repr(r)
    calls = []
    class Operand:
        def __eq__(self, other):
            calls.append('equal')
            return False
    Probe = decorator(type('Probe', (), {'__module__': __name__, '__annotations__': {'value': object}}), slots=True)
    shared = Operand(); left, right = Probe(shared), Probe(shared)
    return_value['shared_operand_equal'] = left == right
    return_value['shared_operand_calls'] = len(calls)
    calls.clear()
    return_value['self_equal'] = left == left
    return_value['self_calls'] = len(calls)
    releases = []
    retained_errors = []
    class Ephemeral:
        def __bool__(self):
            return 1
        def __del__(self):
            releases.append('release')
    class ProducesEphemeral:
        def __eq__(self, other):
            return Ephemeral()
    Lifetime = decorator(type('Lifetime', (), {'__module__': __name__, '__annotations__': {'first': object, 'last': int}, 'last': 1}), slots=True)
    try:
        Lifetime(ProducesEphemeral()) == Lifetime(ProducesEphemeral())
    except TypeError as error:
        retained_errors.append(error)
    else:
        raise AssertionError('invalid truth result accepted')
    return_value['truth_error_release_with_retained_exception'] = list(releases)
    return return_value

expected = observe(std.dataclass, std.field)
actual = observe(product.dataclass, product.field)
assert actual == expected, (actual, expected)
print(json.dumps({'python': sys.version.split()[0], 'backend': sys.argv[1], 'stdlib_differential': 'pass', 'observations': actual, 'scope': 'Stage B ordinary methods only; frozen/policies/extended inheritance deferred'}, sort_keys=True))
