# Troubleshooting

Declaration errors usually describe a model, field or dependency path. Runtime
callback errors identify the field and role, and retain the original exception as
`__cause__`. Start with that context and the callback's own traceback.

| Symptom | Cause and next step |
| --- | --- |
| An annotated `int` still holds text | Annotations do not validate or convert by default. Set `converter=int` or opt into supported `convert=True` inference. |
| A validator returns `1` and raises `TypeError` | Only `None`, exact `True` and exact `False` are valid results. Return a boolean expression or raise a meaningful error. |
| A factory reports an unknown provider | Its required parameter names must name fields, InitVars, `cls` or enabled `self`. Correct the name or use an optional default for a genuinely external argument. |
| An optional factory argument does not use its default | Its name matched a known provider. Matching providers always win, and unavailable ones are errors. |
| A factory reports a cycle | Break the named dependency cycle. Supplying one field explicitly at construction does not make a cyclic declaration valid. |
| A changed provider does not update a derived field | Eager factories initialize; lazy results cache. Reconstruct the model or explicitly reset a mutable lazy field. |
| Repr, equality or `asdict` runs expensive work | The operation reads a participating lazy field. Exclude it from repr/comparison as appropriate; public data helpers still read it. |
| `LazyInitializationError` on first access | A callback recursively read a busy field, or another first access is active. Break recursion and coordinate concurrent access outside the model. |
| An InitVar attribute is missing | It is intentionally a hidden constructor provider. Use a stored field when the value must remain public. |
| `replace` asks for a required InitVar | A new construction needs it again. Supply it explicitly; retained private values are never replayed. |
| An unexpected attribute assignment fails | Slots are on by default. Declare the field or use `slots=False` for an eligible nonfrozen model. |
| Slotted decoration rejects a mixin | A base may introduce an instance dictionary or unsupported model shape. Use a compatible slots-only plain mixin and one generated base. |
| `__post_init__` is rejected | Express derived initialization as named factories and per-field pipelines. See [the design motivation](Initialization.md#why-no-__post_init__). |
| `frozen=True` data still contains a mutable list | Field bindings are read-only; freezing is shallow. Choose an immutable value or a runtime freeze policy. |
| A child remains mutable after runtime freezing | Only resolved freezable model annotations infer cascading. Containers, nullable unions, strings and runtime-only values need explicit hooks. |
| A failed freeze already changed some fields | The operation is nontransactional. Inspect partial state and retry only with hooks designed to tolerate it; completed children stay frozen. |
| A frozen model is still unhashable | Runtime `freeze()` does not change hash generation. Default freezable equality models remain unhashable. |
| `field(doc=...)` fails on 3.12/3.13 | Non-None field documentation requires CPython 3.14 or 3.15. |

## Errors you can catch

`DataclassDefinitionError` subclasses `TypeError` and covers unsupported or
inconsistent declarations. `FieldInitializationError` subclasses `RuntimeError`
and wraps factory failures. `FieldConversionError` subclasses `TypeError` and
wraps conversion failures. `FieldValidationError` subclasses `ValueError` and
covers validator rejection/failure. An invalid validator return is a direct
`TypeError`. `LazyInitializationError` subclasses `RuntimeError` and identifies
busy/recursive evaluation. `FrozenInstanceError` is the stdlib exception for
read-only field writes and deletion; an unknown slotted attribute instead raises
ordinary `AttributeError`.

Freeze callback exceptions propagate directly. Existing contextual callback
errors are not repeatedly wrapped, and `BaseException` is not relabeled.
Assignment failure preserves the old stored field value; callback side effects
elsewhere are not undone. Neither construction nor runtime freeze provides a
transaction or rollback mechanism.

## Report a problem

Include a small declaration, the construction/access that failed, the complete
traceback, CPython minor version and installed `yidl-dataclass`, Astichi and YIDL
versions. If generation matters, record `ASTICHI_LOWER_ENGINE` and inspect
`generated_source(Model)` as described in the [generation guide](Generation.md).
Submit the reproduction through [GitHub issues](https://github.com/owebeeone/yidl-dataclass/issues).
