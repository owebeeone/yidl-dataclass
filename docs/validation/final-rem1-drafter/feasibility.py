"""Original installed API probes; fixed-symbol approach is rejected, not product code."""

import ast
import builtins
from contextvars import ContextVar
from dataclasses import dataclass
from importlib.metadata import version
from pathlib import Path
import sys
import astichi
from astichi.lower_engine.native import select_lower_engine

assert Path(astichi.__file__).resolve().is_relative_to(Path(sys.prefix).resolve())
assert version('astichi') == '1.1.3' and version('yidl') == '0.1.0'
selection = select_lower_engine()
assert selection.fallback_scope is None
observed = []
class Meta(builtins.type):
    def __new__(mcls, name, bases, namespace):
        observed.append(name)
        return super().__new__(mcls, name, bases, namespace)
class Base(metaclass=Meta):
    def __init_subclass__(cls):
        observed.append(cls.__name__)
class _u_fixed_result(Base):
    pass
_u_fixed_result.__name__ = '_u_historical_write_scope'
assert observed[-2:] == ['_u_fixed_result', '_u_fixed_result']
print('rejected-fixed-symbol: hooks/metaclass observe internal name before public restoration')

scope = ContextVar('probe', default=None)
def equal(self, other):
    return self is other
@dataclass(frozen=True, slots=True)
class Captures:
    scope: object
    equal: object
capsule = Captures(scope, equal)
for public_name in ('_u_historical_write_scope', '_u_historical_eq', '_u_capture_0'):
    ids = {public_name, public_name + '_Current', public_name + '_Working'}
    index = 0
    while any(name in ids for name in (f'_u_capture_{index}', *(f'_u_capture_{index}_{view}' for view in ('default','current','working')))):
        index += 1
    alias = f'_u_capture_{index}'
    piece = astichi.compile('''def compare(self, other):
    marker = astichi_ref(external=capture_path).scope.get()
    if marker:
        return astichi_ref(external=capture_path).equal(self, other)
    return self is other
''', keep_names=('self','other','compare')).bind(capture_path=alias)
    tree = piece.to_executable_ast()
    namespace = {alias: capsule}
    exec(compile(tree, '<owning-reference-feasibility>', 'exec'), namespace)
    obj = object()
    token = scope.set(True)
    try:
        assert namespace['compare'](obj, obj) and not namespace['compare'](obj, object())
    finally:
        scope.reset(token)
    assert namespace[alias].scope is scope and namespace[alias].equal is equal
    assert sum(isinstance(node, ast.Name) and node.id == alias for node in ast.walk(tree)) == 2
    assert 'astichi_ref' not in ast.unparse(tree)
print('safe-reference-route: direct original ContextVar/function capture attributes, aliases avoid all three public bindings')
print('backend=' + selection.selected_engine)
