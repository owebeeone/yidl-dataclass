# Public API and behavior

Import declarations/helpers from `yidl_dataclass`. CPython 3.12–3.15 is supported;
other runtimes/minors fail decoration. An annotation declares a field; it does
not validate its runtime type unless conversion/validation is selected.

## Decorator defaults

```python
dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
          unsafe_hash=False, frozen=False, match_args=True, kw_only=False,
          slots=True, weakref_slot=False, convert=False, freezable=False)
```

All switches require exact booleans. Use `@dataclass` or `@dataclass(...)`.
With `slots=True` (the default), decoration returns a generated replacement class
with the declaration's bases, name/module/qualified name and supported
methods/attributes. Bind that result as usual; retain the old declaration only
for inspection. With `slots=False`, decoration updates and returns the original
declaration, so existing references see its generated methods and metadata.
`weakref_slot=True` requires slots.
An existing local custom initializer or `init=False` suppresses ordinary generated
initialization, including factories. A source-free ordinary `field(init=False)`
may remain absent. Policy/frozen/InitVar/local-store/named-provider models require
generated initialization and reject these initializer overrides.

Local custom repr/equality methods follow the std suppression rules. `order=True`
requires equality and rejects conflicting local ordering methods. Hash generation
follows std's equality/frozen/unsafe-hash action table and explicit-hash conflicts:
ordinary equality models are unhashable; frozen equality models normally hash
included fields. `eq=False` normally preserves inherited identity/hash behavior.
`hash=True, compare=False` is rejected. In frozen models, explicitly writable fields must be excluded
from comparison and hashing. `hash=None` with compare=False qualifies; repr=False
is useful for management caches but is not required.

Equality/order require the exact same generated class. Python 3.12 uses tuple
equality; 3.13/3.14 use a self shortcut followed by ordered field comparisons.
Callback order, short-circuiting and raw nonboolean equality results follow that
minor's std behavior. Ordering and hashing use selected field tuples. Repr is
recursive-safe and uses `repr=True` fields; it may evaluate lazy fields.

## Fields and metadata

```python
field(*, default=MISSING, default_factory=MISSING, init=True, repr=True,
      hash=None, compare=True, metadata=None, kw_only=MISSING, doc=None,
      mutable=None, converter=MISSING, validator=None, allow_self_factory=False,
      freeze=MISSING)
const(**field_options)
lazy(*, default_factory, init=False, **field_options)
initvar(**field_options)
classvar(*, default=MISSING, metadata=None, doc=None)
local_store(*, default=MISSING, default_factory=MISSING, repr=False,
            metadata=None, doc=None, converter=MISSING, validator=None,
            allow_self_factory=False, freeze=MISSING)
```

An ordinary default and factory are mutually exclusive. Mutable unhashable
literal defaults retain std rejection; use a factory. A stdlib `dataclasses.Field`
is accepted and copied, so reusing it across declarations does not share name/type
mutation. Std metadata is a read-only mapping; values remain application objects.
`doc` is accepted only on 3.14 when non-None. `kw_only` inherits the decorator
unless explicit. `KW_ONLY` creates the standard local keyword-only fence.
Unknown keywords and invalid option types fail instead of being ignored.
`match_args=True` selects positional init fields excluding keyword-only fields;
InitVars can appear in that tuple but their hidden attributes cannot satisfy an
attribute pattern. String pseudo-annotations are recognized in their defining
module without arbitrary eval; unresolved annotations can remain metadata when
conversion is disabled.

| Declaration | Constructor and storage | Inspection/operations |
| --- | --- | --- |
| Ordinary annotation/default/`field` | `init=True` by default; writable public slot unless policy needs a property | Included in std fields/helpers; repr/compare/hash flags are local |
| `const` | Read-only after initialization; rejects mutable=True | Standard instance field; included by its flags |
| `lazy` | Factory required; no default; `init=False` by default; init=True accepts an explicit seed | Standard instance field; included operations can trigger its getter |
| `initvar` or `InitVar[T]` | Construction provider, with optional default/factory/init=False | No public attribute, repr/compare/hash/helper entry |
| `classvar` or `ClassVar[T]` | Class storage, no instance pipeline/factory | Std pseudo-field; omitted from fields/helpers and instance operations |
| `local_store` | Eager per-instance management storage, always writable/init=False | Omitted from std fields/helpers/compare/hash; repr=False unless requested |

Convenience InitVars default repr/compare/hash to false and reject explicit
inclusion. Ordinary std Field pseudo-field flags retain their metadata, but kind
still excludes them from instance operations. Contradictory annotations/marker
families fail. Field names `self`/`cls` and generated `_y_dc_` names are reserved.
Private storage is an implementation detail, not a security boundary.

## Named factories and initialization order

Factory signature parameters name providers. For example, a factory named
`def doubled(value): return value * 2` receives the processed `value` field when
assigned to another field's `default_factory`. Declaration order need not place
the provider first. Dependencies form a checked DAG; cycles fail decoration even
when an explicit constructor input might bypass a factory.

Functions, lambdas, callable objects and class factories need an introspectable
signature. The builtins list/dict/set/tuple/int/float/str/bytes/bool are supported as
zero-argument factories. Wrap other nonintrospectable callables. Positional-only,
positional-or-keyword and keyword-only parameters work. Unknown optional
parameters keep their callable defaults; positional default bridging preserves
argument positions. An unknown required parameter or variadic signature fails.
A parameter matching a known field always selects that provider, even if optional;
if its declaration has no available source, decoration reports the dependency
path instead of silently using the callable's default.

`cls` receives `type(self)`. `self` receives the partially initialized instance
only with `allow_self_factory=True`; prefer named providers because their ordering
can be checked. These special providers do not appear as API fields. Eager
consumers materialize a lazy dependency first. Factory/converter/validator calls
happen during construction/access/assignment, not decoration; generation inspects
signatures and captures application objects without serializing or repr-ing them.

For generated initialization, explicit input/default/factory result flows through
conversion, then validation, then storage installation, then dependent consumers.
An ordinary source-free init=False field is legal when nothing consumes it.
Dictionary-mode ordinary init=False simple defaults use class fallback (including
later class-default changes); init=False factories still initialize an instance.
These fallback rules do not bypass a policy pipeline.

## Conversion, validation and mutability

`converter=MISSING` inherits decorator `convert`; `converter=None` explicitly
disables conversion. With `convert=True`, exact int/float/str/bytes/bool annotations
and their one-type nullable unions select that constructor (None is preserved for
nullable conversion). Other/unresolved annotations need an explicit converter or
None. There is no inferred container conversion or runtime annotation validator.
An explicit converter takes one positional candidate.

A validator takes the converted value: None or exact True succeeds, exact False
rejects, and any other result raises a direct TypeError contract error. The same
pipeline applies to permitted assignment; failure leaves the previous value
unchanged. Deleting a mutable eager field leaves it absent until reassignment.
Read-only fields reject replacement/deletion with FrozenInstanceError.

`frozen=True` makes fields read-only through field-specific properties. It is
shallow: mutating a contained object remains possible. A writable cache exception
uses `mutable=True, compare=False, hash=False, repr=False`; local_store already
has those exclusions. Such caches may be assigned/deleted. Freezing does not add a
generic attribute dispatcher. Frozen models require slots=True; unknown slotted
attributes raise ordinary AttributeError rather than std FrozenInstanceError.
Nonfrozen policy models can use slots=False.

## Opt-in optimistic runtime freezing

`freezable=True` creates a slotted model that starts mutable and exposes an
irreversible `freeze()` operation. It requires `frozen=False`, generated
initialization and consistent `freezable` settings throughout model inheritance.
The name `freeze` is reserved for that operation. Existing `const` and other
read-only fields retain their construction-time restrictions.

`field(freeze=callback)` and `local_store(freeze=callback)` accept a callable
invoked with exactly one positional argument, the current field value. Its return
value replaces that field's backing storage without rerunning input conversion or
validation. The annotation accepts `Callable[[Any], Any]` or the missing sentinel;
noncallables and callbacks requiring additional arguments fail definition.
Freeze hooks require stored fields in a freezable model. Hook exceptions propagate.

When the hook is omitted and the resolved field annotation is itself a YIDL
Dataclass with `freezable=True`, the generated field policy calls the child's
`freeze()` and retains that same child object. Recognition uses normalized YIDL
definition metadata, not the presence of a method named `freeze`. Explicit hooks
take precedence. This also applies to lazy fields. There is no inference from
runtime values, container elements, unions or unresolved/string annotations;
those cases require explicit field hooks. The containing model must still opt in.

Fields are visited in normalized field order, including inherited fields and
management storage. Lazy fields materialize before freezing completes. Fields
without hooks retain their values; runtime freezing is shallow unless their
policies explicitly cascade or produce immutable containers. For example, `tuple`
freezes a list's container shape, while a custom hook can call `freeze()` on its
elements and then return a tuple. Retained aliases to mutable containers remain
the hook author's responsibility; a read-only view of the original dict does not
detach it from those aliases.

After successful freezing all public field setters/deleters reject writes with
`FrozenInstanceError`, including lazy and management fields. Repeated freezing is
a no-op. An in-progress marker terminates recursive visits through shared objects
or back-references; there is no staging, rollback or concurrency guarantee. A
failure clears the parent's in-progress marker for retry, but completed children
and already transformed fields can remain frozen. Hooks should tolerate this
partial-completion state. No thaw operation is provided.

Copy/deepcopy/pickle preserve the frozen state and reject copying during active
freezing. Package `replace` constructs a new mutable object; unchanged values may
still reference immutable or shared contents from the original. Hash selection
retains the existing dataclass options: default equality models remain unhashable
after freezing too. This iteration does not activate hashing on freeze; explicit
`unsafe_hash` remains unsafe and should not be used for mutable collection keys.

This uses Dataclass-owned YIDL resources and field-specific accessors. Lifecycle
is not a dependency and its freeze/transaction machinery is not reused.

## Lazy evaluation, retry and hidden-provider lifetime

A lazy getter has UNREADY/BUSY/READY state. Its first successful read calls its
specialized factory/pipeline and caches the result. Failure returns to UNREADY
for retry; BaseException also clears busy state. Opaque recursive access and a
concurrent second first access raise LazyInitializationError. Concurrent first
access is unsupported, rather than automatically locked.

Delayed factories read current public fields/properties/ClassVars at evaluation
time. A named cycle fails decoration; callbacks must not mutate their provider
model during evaluation. Effective ordinary/lazy mutability is explicit `mutable` when supplied, otherwise
`not frozen`. Select `mutable=False` for a read-only lazy field. `mutable=True`
enables explicit override and reset
(`del instance.lazy_field`); assignment runs its pipeline and marks it ready.
`init=True` accepts an explicit initial seed; omission remains delayed.
Setter/deleter access while that field is BUSY is rejected.

Only InitVars directly needed by delayed consumers receive private retention.
An eager intermediate cuts the retention graph. Failed reads retain providers.
When every nonresettable direct consumer becomes ready, their provider is released;
if any consumer can reset, its provider remains for the instance's lifetime.
Hidden providers never become public fields or helper entries.

## Helpers, replacement and copying

`MISSING`, `Field`, `InitVar`, `KW_ONLY`, `FrozenInstanceError`, `fields`,
`is_dataclass`, `asdict` and `astuple` are stdlib objects/helpers. Data helpers read
public instance fields, including compare=False fields; they evaluate lazy fields
and use their usual recursive copying. They omit InitVars/ClassVars/local storage
and private state. Standard cyclic-graph limitations and getter errors apply.

`storage_fields(model_or_instance)` returns an immutable tuple of descriptions
including extension/provider/local kinds in field order. A description exposes
`name`, `kind.label`, `field` (std metadata), `mutable`, `converter`, `validator`,
`dependencies` and `retained`; it never exposes retained provider values. Treat
`__yidl_dataclass_definition__` as read-only versioned generation metadata.

`replace(obj, /, **changes)` constructs a new model. Existing init=True ordinary/
const fields are read unless changed; init=True lazy fields are also materialized
unless changed. init=False fields, lazy caches and local stores rebuild. Required
init=True InitVars must be supplied again; omitted defaulted/factory InitVars use
the declaration again; init=False InitVars recompute. Hidden retained values are
never replayed. Unknown changes or changes to init=False fields fail.

Std `dataclasses.replace` works when there are no InitVars or every init=True
InitVar is supplied. Its omitted hidden/defaulted InitVar getter behavior is an
unsupported subset; use the package helper. On 3.13/3.14 generated `__replace__`
supports `copy.replace`; a local custom method is preserved. No method is added
on 3.12.

Copy/deepcopy/pickle preserve ready/unready/absent storage, caches/local state and
still-retained providers without evaluating lazy factories. Shallow copy shares
references; deepcopy uses its memo. Copy/pickle while lazy evaluation is active
raises RuntimeError. Pickle uses explicit state, not sentinel identity; normal
module-level class importability is still required. Policy models reject custom
copy/state/reduction hooks that could bypass this contract.

## Inheritance and explicit exclusions

One generated model base plus compatible plain mixins is supported. Fields merge
in reverse-MRO order; overrides retain their position and inherited slots are
reused. Same-shape defaults/factories/pipelines/init/kw-only/repr/compare/hash may
change; field family, storage shape and effective mutability may not. Frozen and
nonfrozen generated models cannot mix. The merged provider graph is rechecked.
Undecorated subclasses receive normal inherited behavior without new metadata.

Generated slotted models reject any base with an instance dictionary. Plain
unslotted bases are permitted with slots=False. Multiple model bases, std-dataclass
bases, manual slots, descriptor-valued field defaults, required subclass-creation
keywords and custom metaclasses are rejected. type/ABCMeta and no-argument subclass
hooks work; abstract-method state is updated. Normal descriptors receive
__set_name__. Copied supported methods/descriptors get fresh __class__ cells for
zero-argument super without mutating the old declaration; class replacement can
repeat a base __init_subclass__ callback.

There is **no `__post_init__` mechanism**: local or inherited hooks are rejected;
use named factories/pipelines. Policy models reject custom __getattribute__,
__setattr__, __delattr__ and bypassing copy/state hooks. Aliases, whole-model
validation, JSON/schema frameworks and arbitrary metaclasses are outside this
release.

## Failure classes

DataclassDefinitionError is a TypeError for declaration/availability/conflict
errors. Factory failures raise FieldInitializationError (RuntimeError), converter
failures FieldConversionError (TypeError), and validator rejection/failure
FieldValidationError (ValueError). Lazy recursion/concurrent access raises
LazyInitializationError (RuntimeError). Diagnostics identify the model/field/role
and known dependency path; original callback exceptions remain causes. Existing
contextual errors propagate without repeated wrapping; BaseException is not
relabeled. Construction/assignment do not roll back application callback side
effects or a self factory leaking a partially initialized instance.
