# Runnable examples

Install `yidl-dataclass` in a supported CPython 3.12–3.15 environment, then run
these scripts from the repository root with `python examples/<name>.py`.
No SDK source checkout is needed.

| Example | What it demonstrates |
| --- | --- |
| [first_use.py](first_use.py) | Slots, defaults, independent factories, comparison and standard helpers |
| [dependent_fields.py](dependent_fields.py) | Named providers, conversion/validation, hidden InitVars and management storage |
| [lazy_fields.py](lazy_fields.py) | Delayed construction, caching, reset and retained InitVars |
| [runtime_freeze.py](runtime_freeze.py) | Mutable setup, permanent freeze, typed-child inference and list-to-tuple policy |
| [freeze_failure.py](freeze_failure.py) | Partial completion, retry-safe policies and failure recovery |

Every file is a complete program with assertions and a short success message.
The [documentation verifier](../dev-docs/documentation/verify_examples.py) runs all
of them against the installed package, alongside runnable guide blocks.
