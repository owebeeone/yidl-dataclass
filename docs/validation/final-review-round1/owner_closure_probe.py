import builtins
import copy
import json
import pickle
import sys
import types
from yidl_dataclass import dataclass, const, field, lazy
from yidl_undoable import undoable, managed, UndoRedoManager

results = []
module = types.ModuleType('owner_collision_models')
sys.modules[module.__name__] = module
for name in ('type', 'tuple', 'dict', 'int', 'hash', '_y_dc_converter_0'):
    try:
        calls = []
        def converter(value):
            calls.append(value)
            return builtins.int(value)
        marker = field(default=3, converter=converter) if name.startswith('_') else const(default=3)
        cls = builtins.type(name, (), {'__module__': module.__name__, '__annotations__': {'value': builtins.int}, 'value': marker})
        model = dataclass(cls, frozen=name == 'hash')
        assert not calls, 'generation invoked converter'
        setattr(module, name, model)
        value = model()
        assert value.value == 3
        assert copy.copy(value).value == 3
        assert copy.deepcopy(value).value == 3
        assert pickle.loads(pickle.dumps(value)).value == 3
        if name == 'hash':
            assert builtins.hash(value) == builtins.hash((3,))
        results.append({'case': 'dataclass-' + name, 'pass': True})
    except BaseException as exc:
        results.append({'case': 'dataclass-' + name, 'pass': False, 'error': builtins.type(exc).__name__, 'message': str(exc)[:180]})

try:
    @dataclass(repr=False)
    class Base:
        value: int = lazy(default_factory=lambda: 7)
    @dataclass(repr=False)
    class Child(Base):
        pass
    @dataclass(repr=False)
    class Grandchild(Child):
        pass
    assert Child.__slots__ == Grandchild.__slots__ == (), (Child.__slots__, Grandchild.__slots__)
    assert Base.__basicsize__ == Child.__basicsize__ == Grandchild.__basicsize__
    assert Grandchild().value == 7
    results.append({'case': 'inherited-lazy-slots', 'pass': True})
except BaseException as exc:
    results.append({'case': 'inherited-lazy-slots', 'pass': False, 'error': builtins.type(exc).__name__, 'message': str(exc)[:180]})

for name in ('_u_historical_write_scope', '_u_historical_eq'):
    manager = None
    try:
        model = undoable(builtins.type(name, (), {'__annotations__': {'value': builtins.int}, 'value': managed(default=2)}), eq=True)
        @undoable
        class Parent:
            children: tuple = managed(default=())
        manager = UndoRedoManager()
        a = model(transaction_manager=manager)
        b = model(transaction_manager=manager)
        parent = Parent(children=(a,), transaction_manager=manager)
        manager.initialize(parent, a, b)
        assert a == b
        manager.begin()
        parent.children = (b,)
        assert parent.children[0] is b
        manager.rollback()
        results.append({'case': 'undoable-' + name, 'pass': True})
    except BaseException as exc:
        results.append({'case': 'undoable-' + name, 'pass': False, 'error': builtins.type(exc).__name__, 'message': str(exc)[:180]})
        if manager is not None:
            try:
                manager.rollback()
            except BaseException:
                pass
print(json.dumps({'python':sys.version.split()[0], 'cases':results}, indent=2))
raise SystemExit(0 if all(r['pass'] for r in results) else 1)
