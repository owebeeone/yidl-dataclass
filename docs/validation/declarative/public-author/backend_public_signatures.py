import inspect
import astichi

for module in [astichi.lowering, astichi.perf_counters]:
    print('module:', module.__name__)
    for name in dir(module):
        if not name.startswith('_'):
            value = getattr(module, name)
            if callable(value):
                try:
                    print(name, inspect.signature(value))
                except (ValueError, TypeError):
                    print(name, 'signature unavailable')
            elif isinstance(value, (str, int, bool, type(None))):
                print(name, value)
            else:
                print(name, 'public value type:', type(value).__name__)
