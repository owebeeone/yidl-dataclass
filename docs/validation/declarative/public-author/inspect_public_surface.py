import inspect
import os
import astichi
import yidl_dataclass

print('ASTICHI_LOWER_ENGINE:', os.environ.get('ASTICHI_LOWER_ENGINE'))
for module in [astichi, yidl_dataclass]:
    names = [name for name in dir(module) if not name.startswith('_')]
    print(module.__name__, 'public names:', names)
    for name in names:
        value = getattr(module, name)
        if callable(value):
            try:
                print(name, inspect.signature(value))
            except (TypeError, ValueError):
                print(name, 'signature unavailable')
