# YIDL Dataclass detailed design

Status: design proposed for independent review. This document resolves the
accepted requirements into an implementation contract; it is neither an
implementation claim nor the TDD plan. Implementation and the separate TDD plan
begin only after the owner records a reviewed design. The autonomous GO was given
at `2026-10-12T03:36:48Z`; stage timestamps and measurements belong in the owner's
experiment ledger.

The controlling brief is `DataclassConcept.md`, `ExperimentProtocol.md`,
`GoldenExamplesAmendment.md`, `DeclarativeEvaluation.md`, and
`DataclassSpec-OperatorAmendment.md`, with the acceptance boundary recorded in
`CurrentProgramCheckpoint.md`. Bounded corrections may exceed two review cycles;
an architectural defect requires redesign. The paused UndoableLeaf proposal is
outside this design.

## 1. Product and compatibility boundary

Deliver a `yidl-dataclass` distribution exporting `yidl_dataclass`. Support
CPython 3.12, 3.13 and 3.14; later minors and other interpreters are unsupported
until their metadata adapters and differential suites pass. Fail decoration with
an informative `DataclassDefinitionError` on unsupported interpreters. Package
metadata states this range. No performance claim follows from the architecture.

Every decorated model has one generated class, its own instance storage and
methods. With `slots=True`, decoration replaces the declaration class with a class
having the same declared bases, name, module and qualified name. The declaration
class is not an instance-state base. With `slots=False`, ordinary fields use the
instance dictionary and policy fields still use their own private attributes;
the decorator may update the declaration class. Generated public behavior comes
from YIDL resources composed through Astichi into an executable AST. The stdlib
decorator never generates a model's methods.

| Surface | Contract |
| --- | --- |
| Decorator switches | Stdlib spellings and effective defaults, except `slots=True`; strict booleans |
| Plain fields | Stdlib `field()` options, std `Field` inputs, defaults, factories, keyword-only fence and signatures |
| Annotation-only fields | Ordinary required fields; annotations are not runtime validators |
| Constructor/repr/comparison/hash | Stdlib compatible subset, version-selected semantics and method-conflict rules below |
| Storage | Public writable slots without generated accessors; explicit dictionary option |
| Frozen | Field-specific read-only properties; writable excluded cache exceptions; shallow freezing |
| Inspection/data helpers | Std `Field` metadata, `fields`, `is_dataclass`, `asdict`, `astuple`; extensions have the exclusions below |
| Copy with changes | Std `replace` on the compatible subset; package `replace` handles hidden/defaulted InitVars |
| Pattern matching | Std positional init-field selection, including InitVars; hidden InitVars consequently fail an attribute pattern |
| Inheritance | One generated model base plus storage-compatible plain mixins; ordered field merging and compatible overrides |
| Initialization | Named providers; no `__post_init__` mechanism |
| Outside initial scope | Descriptor-valued field defaults, custom metaclasses, manual slots, multiple model bases, std-dataclass bases, whole-model validation, aliases, JSON/schema frameworks |

Rejected combinations are decoration errors, not silently reduced features.
Plain user descriptors unrelated to fields remain supported with their normal
`__set_name__` behavior. Ordinary unslotted plain bases are allowed only with
`slots=False`; a slotted model must not inherit an instance dictionary.

## 2. Exact public declarations

The public surface is:

```python
dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
          unsafe_hash=False, frozen=False, match_args=True, kw_only=False,
          slots=True, weakref_slot=False, convert=False)

field(*, default=MISSING, default_factory=MISSING, init=True, repr=True,
      hash=None, compare=True, metadata=None, kw_only=MISSING, doc=None,
      mutable=None, converter=MISSING, validator=None,
      allow_self_factory=False)
const(**field_options)
lazy(*, default_factory, init=False, **field_options)
initvar(**field_options)
classvar(*, default=MISSING, metadata=None, doc=None)
local_store(*, default=MISSING, default_factory=MISSING, repr=False,
            metadata=None, doc=None, converter=MISSING, validator=None,
            allow_self_factory=False)
replace(obj, /, **changes)
storage_fields(class_or_instance)
generated_source(cls)
```

`MISSING`, `Field`, `InitVar`, `KW_ONLY`, and `FrozenInstanceError` are the stdlib
objects. Re-export `fields`, `is_dataclass`, `asdict`, and `astuple` from the
stdlib; their processing remains the independent interoperability test.
`storage_fields` returns immutable extension descriptions including local storage
and initialization providers, in declaration order. Descriptions expose kind,
standard Field metadata, effective mutability, conversion/validation, dependencies,
and whether an InitVar requires private retention. They expose no provider values.
`__yidl_dataclass_definition__` carries the same versioned class definition plus
resolved decorator options, layout and generation schema. Treat it as read-only.

All marker calls validate their accepted keyword set. Defaults must not coexist
with factories. `init`, `repr`, `compare`, and explicit `kw_only` are booleans;
`hash` is bool or None; `mutable` is bool or None. Distinguish an omitted option
from an explicit value when resolving family defaults. Unknown keywords raise
TypeError. Std `Field` declarations are accepted without extension options;
extension marker objects wrap a copied std `Field` and separate policy data.

`const` fixes `mutable=False` and rejects `mutable=True`. `lazy` requires a factory,
rejects `default`, and allows `init=True` to seed a cache from an explicit argument;
its omitted parameter uses the factory sentinel, without eager computation.
`initvar` may use `init=False`, a default or a dependent factory. It has no public
instance attribute, property, repr/comparison/hash operand or data-helper entry.
`ClassVar[T]` and `InitVar[T]` select the corresponding kinds on ordinary field
declarations; contradictory annotations and convenience kinds fail. ClassVars
have no instance policy, converter, validator or factory. Recognize `KW_ONLY`
once per local declaration, following std ordering rules.

Convenience InitVar declarations default repr/compare/hash to exclusion and
reject explicit attempts to include them. Std Field inputs on pseudo-fields may
carry their standard default flags in metadata; the pseudo-field category always
excludes them from generated instance operations, as std inspection does.

Local storage is public per-instance management storage, initialized eagerly,
always writable and `init=False`, excluded from comparison/hash and std field
inspection/data helpers. Its declaration has no `compare`, `hash`, `init` or
`mutable` override. `repr=True` explicitly adds it to the generated repr.
It participates as a named factory provider. An ordinary field's `compare=False`
does not remove it from inspection or serialization.

`doc=None` works on all supported minors. Non-None field `doc` is supported only
on 3.14; reject it on earlier minors instead of inventing std Field attributes.
All instance/provider defaults follow the std unhashable-default rejection;
use a factory for mutable defaults. ClassVars follow std's separate rules.

## 3. Metadata and standard helper rules

`__dataclass_fields__` is an ordered mapping to real, independent std `Field`
objects: ordinary, const and lazy fields have the std instance-field category;
InitVars and ClassVars have their std pseudo-field categories. Local storage
appears only in the extension definition. Preserve user metadata via the std
mapping proxy without commandeering its keys. Preserve the declared annotation,
defaults and factory object; a named factory is an intentional extension to the
usual zero-argument factory contract.

`stdlib_adapter.py` is the only boundary using std private metadata machinery.
It uses public `dataclasses.field` for construction, a copied Field and bounded
`_get_field` processing for ordinary/class-variable recognition and validation,
the std field-category objects, and the version-appropriate `_DataclassParams`
constructor. It never calls `_process_class`, `_init_fn` or any std method
generator. For extended InitVar factories, recognize the annotation with a
factory-free temporary Field, then restore the true factory metadata and apply
this design's checks. Temporary harvest classes are not decorated and never
escape. Imported Field objects are copied before normalization. Unsupported
private shapes fail the adapter contract tests rather than falling back.

Retain std best-effort recognition of string annotations in their defining
module; do not evaluate arbitrary annotation strings. On 3.14 use annotationlib
FORWARDREF inspection to avoid eagerly executing unresolved annotations. An
unresolved annotation is acceptable until type-derived conversion is requested.
Inherited annotations retain their defining module for pseudo-field recognition.

`__dataclass_params__` is the interpreter's actual std params object; preserve its
version-specific shape. New switches absent from older private params shapes
remain available in the extension definition. Ordinary field defaults remain
class defaults only in dictionary mode as the stdlib does; policy properties
override class access. Hidden InitVars deliberately have no public class defaults.

Std `fields` and `is_dataclass` must work with no package-specific dispatcher.
`asdict`/`astuple` read all public instance fields, including excluded comparison
fields; they materialize lazy fields and perform their usual recursive copying.
They omit ClassVars, InitVars, local storage and backing state. Errors from lazy
reads propagate. Cyclic object graphs have the std helper's limitations.

Std `replace` is supported when no hidden InitVar must be inferred: there are no
InitVars, or every `init=True` InitVar is supplied in `changes`. An omitted hidden
defaulted InitVar is an unsupported std-helper combination (its std getter can
raise AttributeError); do not expose providers to make it work. Required InitVars
remain explicitly required. Package `replace` reruns generated construction:
ordinary/const `init=True` fields are read unless changed; `init=True` lazy fields
are likewise read and materialized; `init=False` fields, lazy caches and local
stores are rebuilt. Required `init=True` InitVars must be supplied; omitted
defaulted/factory InitVars use their declaration again; `init=False` InitVars
recompute. Neither helper replays hidden retained values. Unknown changes and
changes to `init=False` fields fail. The wrapper works recursively only where the
caller chooses to invoke it; it is not a new serialization framework.

Generate `__replace__` on 3.13/3.14 using this package replacement contract for
`copy.replace`. A local custom `__replace__` is preserved. No method is added on
3.12. Ordinary `copy.copy`, `copy.deepcopy` and pickle have generated storage
support for extension classes: preserve materialized/unmaterialized state without
calling factories, preserve local storage, and preserve only still-retained
providers. Shallow copy shares references; deepcopy uses the memo and deep-copies
stored values. Pickle encodes readiness/absence explicitly, not process-local
sentinel identity. Restore internal storage directly. Copy/pickle during active
lazy evaluation raises RuntimeError. A normally pickleable module-level model is
required; local classes retain ordinary Python restrictions. Policy classes
reject custom copy/state/reduction hooks that would bypass this contract; plain
classes may retain them.

## 4. Storage, access, conversion and failure

For every field resolve a layout plan before generation:

| Effective policy | Instance layout and generated access |
| --- | --- |
| Writable eager, no converter/validator | Public `name` slot, direct reads/writes, no property |
| Writable eager, pipeline enabled | Private value slot; field-specific getter/setter/deleter |
| Read-only eager | Private value slot; field-specific getter and rejecting setter/deleter |
| Lazy | Private value, ready and busy slots; field-specific getter; policy-specific setter/deleter |
| Eager-only InitVar | Constructor local only |
| InitVar reachable by lazy factory | Private provider slot only while required |
| ClassVar | Class namespace value |

`slots=False` uses the same specialized properties over private attributes instead
of slots. Reject `frozen=True, slots=False` in this release: dict-level arbitrary
attribute freezing would require an additional general assignment interceptor.
Reject manual `__slots__`; `weakref_slot=True` requires `slots=True`, adds
`__weakref__` only when absent from bases. Private generated names use a reserved
`_y_dc_` prefix; reject collisions in fields and user namespace.

Effective mutability for ordinary/lazy fields is explicit `mutable` when given,
otherwise `not frozen`. `const` is always read-only; local storage is always
writable. In a frozen class every writable public field must have `compare=False`
and effective `hash=False` (`hash=None` with compare false qualifies). This is a
decoration check, including with `unsafe_hash=True`. The cache may use
`repr=False`. Freezing prevents replacement/deletion, not mutation of stored
containers. Read-only setter/deleter raise std `FrozenInstanceError` naming the
field. A frozen slotted object's unknown attributes raise normal AttributeError;
this differs from std frozen arbitrary-name rejection. No generic `__setattr__`
or `__getattribute__` dispatcher is generated. Private backing access is internal,
not an immutability/security boundary.

Pipeline: candidate source -> converter -> validator -> install -> provide to
dependent factories. Apply to explicit inputs, defaults, factory results and
public assignments wherever applicable. `converter=None` disables conversion;
MISSING inherits decorator `convert`. With `convert=False`, omission does nothing.
With `convert=True`, derive only exact `int`, `float`, `str`, `bytes`, `bool`, or
their one-type nullable union annotations; use the corresponding constructor,
preserving None for a nullable annotation. Unsupported/unresolved types require
an explicit converter or `converter=None`, otherwise fail decoration. Do not
infer container conversion or validation. Explicit converter is a callable taking
one positional value. Validator takes the converted value and succeeds with None
or exact True, rejects with exact False, and has a TypeError contract error for
other return values.

Expose `DataclassDefinitionError(TypeError)`,
`FieldConversionError(TypeError)`, `FieldValidationError(ValueError)`,
`FieldInitializationError(RuntimeError)` and
`LazyInitializationError(RuntimeError)`. Diagnostics include model, field, role
and dependency path when known. Preserve original callback exceptions as causes;
do not intercept BaseException to relabel cancellation. Factory exceptions are
FieldInitializationError; converter exceptions FieldConversionError; validator
exceptions/rejection FieldValidationError. Failed assignment preserves the old
stored value. Failed construction returns no object, but callback side effects
and a self-provider leaking a partially constructed object are not rolled back.
Already contextual package errors propagate without repeated wrapping, including
lazy-recursion errors raised through a dependent factory. An invalid validator
return is the direct TypeError contract diagnostic, distinct from callback failure.

Mutable eager properties permit deletion, leaving the slot/attribute absent and
subsequent reads raising AttributeError; later assignment runs the pipeline.
Ordinary writable slots retain normal Python deletion. A mutable lazy setter
converts/validates a new value, marks it ready and replaces the cache; deletion
clears readiness and permits later recomputation. Reject setter/deleter reentry
while that lazy field is busy.

## 5. Named factory graph and lazy lifetime

Inspect factory signatures once during harvesting. A parameter matching a field
name receives that provider's processed value. `cls` receives `type(self)`;
`self` receives the instance only with `allow_self_factory=True`. These two names
are reserved field names. Plain functions, lambdas, callable objects and class
factories with introspectable signatures work. Positional-only arguments are
emitted positionally, other matched parameters by keyword. Unknown required
parameters fail decoration. Unknown optional parameters are omitted; if needed
to bridge an earlier positional-only optional argument, bind its actual default
object into the generated call. Reject variadic signatures except known std
zero-argument builtins `list`, `dict`, `set`, `tuple`, `int`, `float`, `str`,
`bytes`, `bool`, for which emit an empty call. Uninspectable other factories fail
with advice to wrap them in an introspectable function. Optional parameters that
match a provider are dependencies and receive it.

Resolve the initializer action before enforcing value availability. A local
custom initializer suppresses generated init even with decorator `init=True`;
decorator `init=False` also suppresses it and preserves the inherited initializer,
if any. The extension restrictions in Section 6 still apply. Suppression means
no generated candidate evaluation, factory calls or constructor dependency DAG;
do not require an ordinary field to have a constructor source merely to decorate
it. Class defaults and public storage declarations still receive normal setup.

When init is generated, build a deterministic dependency DAG over its actual
candidate evaluations and named provider reads, including lazy, InitVar, local
and ClassVar nodes. Reject any named cycle even if explicit constructor inputs
might bypass factories. Require a source for policy fields, InitVars and local
storage that generated initialization must establish, and for every provider
actually consumed by a generated eager or delayed factory call. Sources are
constructor inputs, defaults/factories, readable ClassVars and the dictionary
fallback below. An ordinary `init=False` field without a source may remain absent
if no generated consumer requires it. If one does, reject decoration with the
model, consumer, unavailable provider and dependency path; do not assume later
application assignment will satisfy generated construction or lazy reads. A
matched optional factory parameter is still a bound provider and needs a source.

| Ordinary field and initializer action | Required outcome |
| --- | --- |
| Local custom init assigns a required `init=False` field | Decorate successfully; preserve that initializer and its assignment |
| Decorator `init=False`, required `init=False` field | Decorate successfully; field can be absent until application assignment |
| Generated init, required `init=False` field, no consumer | Decorate successfully; no assignment to that field |
| Generated factory consumes a source-free `init=False` provider | Decoration fails with the unavailable-provider diagnostic |
| Generated init, dictionary-mode plain `init=False` simple default | Keep a class-default fallback; do not install an instance value |

The last row applies only to writable ordinary fields without conversion or
validation. Such a dictionary instance reads its class default until assigned;
changing the class default changes reads on instances without an overriding
instance attribute. For a generated factory needing that provider, read
`self.name` into its processed provider local at evaluation time, without an
instance write. A later lazy factory reads `self.name` again. In slot mode the
same simple default is installed in the public instance slot. A dictionary-mode
`init=False` default_factory does create an instance value when init is generated.
With suppressed init, no factories execute: dictionary simple defaults remain
class fallbacks, and slotted fields remain unset until an inherited/custom
initializer or application code assigns them. These rules do not change
`init=True` fields installed by generated construction.

Topological ordering ties use declaration order. Constructor parameter order is
independent: preserve reverse-MRO merged field order, then std positional/keyword-
only partition, and reject non-default positional parameters following defaulted
parameters. Initialize lazy busy/ready flags before evaluating generated
candidates. Evaluate required eager candidates and InitVars in DAG order, skipping
absent ordinary fields and treating dictionary fallbacks as reads only; retain
needed InitVars as each becomes available. An eager factory depending on a lazy
field materializes it during construction after its providers are initialized.
Inputs are never reprocessed when used as providers. Generated eager calls read
processed local values; generated delayed calls directly read public field
properties/slots and private retained InitVars. No runtime provider-name table
lookup is introduced.

Factory dependencies describe initialization, not a reactive graph. A lazy field
reads current provider values when first evaluated or after an allowed reset;
an already cached value is not invalidated when a provider changes. ClassVars are
read at evaluation time. Factories/converters/validators must not mutate the
model or reenter its construction. Arbitrary self-provider reads cannot be
statically analyzed: only named dependencies order eager prerequisites. Reads of
an unavailable ordinary field fail; lazy reentry has the guard below. This
document does not promise side-effect isolation or hidden dependency discovery.

Lazy getter: return the ready cached value; otherwise reject busy reentry, set
busy, invoke the specialized factory call, convert/validate into a local, install
and mark ready only after success, and clear busy in finally. Failure leaves it
unready for retry; successful dependency caches remain successful. A generation-
time cycle diagnostic covers named cycles; busy guards cover runtime recursion
through opaque callbacks. Concurrent first accesses are unsupported: a second
access while busy raises LazyInitializationError. No thread-local recursion map,
lock or exactly-once concurrent guarantee is hidden in the implementation.

Retain only InitVars directly needed by delayed lazy factory calls. Following a
lazy-to-lazy dependency reaches that other getter's own provider requirements;
following an eager public value stops, because its eager prerequisites are no
longer needed. An eagerly computed InitVar is retained if itself needed, without
retaining the prerequisites used to compute it. Eager-only providers never become
slots. For each retained provider generation computes its direct consuming lazy
fields. If any consumer can reset, retain for the instance lifetime. Otherwise,
after all consumers cache successfully, delete that provider slot. Use generated
readiness checks and direct private deletions; no runtime liveness map. Failure
preserves needed providers. Reference retention is shallow; mutating a retained
object before evaluation affects the later factory. Copy and pickle preserve this
exact state. Required InitVars for replacement remain caller-supplied even if an
old instance still retains them.

## 6. Generated methods, inheritance and hashes

Follow the interpreter's std local-method decision table for `__init__`,
`__repr__`, `__eq__`, ordering and hash. Local repr/eq are preserved; disabling a
switch preserves inherited methods. `order=True` requires `eq=True` and rejects
any local ordering method. `unsafe_hash=True` rejects an explicit local hash.
Treat an automatic `__hash__=None` paired with a local eq as std does. Use no
generated `__ne__`. Repr uses the actual class qualified name and std recursive
repr protection; selected lazy reads materialize normally.

If eq is generated, different exact classes return NotImplemented. On 3.12 emit
tuple equality of the selected operands, preserving its evaluation and element
identity behavior. On 3.13/3.14 emit the std self-identity shortcut and the ordered
`and` chain of field equalities. Thus self comparison on those minors need not
materialize lazy fields, and a mismatch can avoid later reads. Ordering on all
supported minors uses selected operand tuples with the requested operator,
including tuple evaluation/identity behavior. Empty tuples and an empty equality
chain retain the matching std behavior. Hash reads selected fields in order and
hashes a generated tuple; it is not cached. Included lazy fields materialize as
these operations actually read them; exceptions propagate.

Use the std hash action table: eq+mutable normally sets None, eq+frozen normally
generates a hash, eq disabled normally preserves an existing/inherited hash, and
unsafe_hash requests generated hashing subject to explicit-hash conflicts.
An effective hash operand is `hash=True` or `hash=None and compare=True`.
Additionally reject `hash=True, compare=False`: otherwise logically equal objects
could differ in generated hash. `compare=True, hash=False` is permitted. Writable
frozen exceptions are excluded as above. Lazy read-only fields can be hashed;
provider/cache values may still contain mutable objects. Like std frozen models,
hash stability of such contents and arbitrary callbacks remains the user's
responsibility. In particular, unsafe_hash never guarantees stability.

Merge inherited model fields in reverse MRO and preserve an overridden field's
position. Allow one direct generated model base and plain mixins without model
metadata. Reject mixed frozen/nonfrozen generated inheritance, incompatible
public/private slot shapes, changes between lazy/eager/provider/local families,
and inherited mutability downgrades/upgrades. Same-shape overrides may change
defaults, factories, converter/validator, init/kw_only and repr/compare/hash;
revalidate the complete graph and policy rules. Reuse inherited slots; do not
redeclare them. This restriction avoids latent shadow storage. Undecorated
subclasses retain ordinary Python inherited-method behavior and get no new field
metadata automatically. Multiple model bases and std dataclass bases fail
explicitly in this release.

Preserve user methods, class/static methods, properties, docstring and unrelated
class attributes. For slotted replacement, clone copied functions having a
`__class__` closure with a fresh closure cell bound to the replacement class,
including supported descriptor wrappers; never mutate the old class's cells.
This supports zero-argument super and inherited model methods. Permit `type` and
ABCMeta only, call `abc.update_abstractmethods`, and reject required class-creation
keywords/unsupported metaclass protocols. User descriptors get normal set-name
calls on the replacement. Re-execution of base `__init_subclass__` is observable,
as with class replacement; plain mixins must support no-argument subclass creation.

Reject a local or inherited `__post_init__` with a migration diagnostic naming
factories. Classes requiring extension initialization (frozen, policy fields,
InitVars, local storage or named dependencies) reject `init=False` or a local
custom `__init__`. For purely ordinary fields, `init=False` and local custom init
follow std suppression semantics, including no generated initialization of
default factories and no availability requirement for their absent ordinary
fields. Resolve this suppression before the Section 5 availability checks;
retaining metadata is not a request to generate initialization. A plain required
`field(init=False)` is valid with a custom initializer, with decorator init=False,
or without a generated consumer; its absence has normal AttributeError behavior.
Dictionary-mode simple defaults follow Section 5's class fallback rule, including
subsequent class-default changes. Reject custom `__getattribute__`, `__setattr__` and
`__delattr__` on policy classes, including inherited interceptors, since they
would defeat the generated access contract.

## 7. Native reusable comparison generation

Own neutral assets in the `yidl` distribution under
`src/yidl/library/comparison/`: `comparison.yidl`, `resources.py` (resource loader
only), `__init__.py`. This is an actual two-consumer library asset, not a compiler
semantic change. Both wheels must include its source resource. Consumers load
it through `importlib.resources`; never depend on a sibling checkout, scratch
file, site-packages filesystem shape or installed absolute path.

`comparison.yidl` exports `ComparisonCore`, defining ordered `ComparisonClass`
and `ComparisonOperand` facts, precompiled guard/read resources, and equality,
four ordering and optional hash productions. Concrete generation inputs are:

- Class identity/order and selected class-body target surface; requested method
  switches; equality mode (`UseTupleEquality` resolved for the interpreter);
  explicit hash action (generate, None or leave untouched).
- Ordered operands keyed by owner and field identity, inclusion already resolved
  separately for compare and hash; direct left/right structural read paths such
  as `self.price`, `other.price`, and a hash read path.
- A selected compatibility resource. Initial consumers select exact-class
  compatibility. The resource has no dataclass/transaction imports.

Read-path inputs are validated Name/Attribute paths, not arbitrary Python source;
the shared attribute-read resource lowers them using Astichi's `astichi_ref`
external path binding. Consumer extension resources may provide another structural
read expression through inherited matchers, not parsed strings or runtime getters.
The shared YIDL method productions consume those expression contributions into
named guard and operand holes. Equality/order/hash method definitions live here,
not in consumer Python helpers. Empty selections are handled by native YIDL
matchers/resources. Tuple expressions in emitted methods are permitted; a generic
Python tuple-comparison helper is not the reusable implementation.

Dataclass's `dataclass_comparison.yidl` extends `ComparisonCore` and the class
core, adapting effective public fields and target surfaces with matchers.
Undoable's `undoable_comparison.yidl` independently extends the same concept and
its view layers, adapting each facade class and view getters. Both materialize
the shared productions into their existing class bundles. A canonical neutral
composition fixture plus both consumers proves inheritance, field order,
specialized read expressions and generation independence from dataclass metadata.
Lifecycle is a future consumer; this run does not enable comparisons there.

At regeneration, compiler source maps use stable logical keys:
`shared/comparison.yidl`, `dataclass/<filename>.yidl`, and
`undoable/<filename>.yidl`. Consumer imports refer to
`../shared/comparison.yidl`. Load the shared bytes from the installed package and
place them under that logical key. Local consumer files receive the same logical
keys whether in a checkout, wheel or sdist. Record the shared source digest in
generated-base provenance. No copied comparison source is maintained in a
consumer repository.

## 8. Undoable integration in this experiment

Extend `undoable(cls=None, /, *, eq=False, order=False)` with strict booleans.
Bare, empty-parentheses and explicit false options preserve current node-state
identity equality/hash across facades. `order=True` with omitted/false eq fails.
`eq=True` generates logical comparison on default, current and working facade
classes; `order=True` also generates ordering. Each facade compares the values
returned by its own public getters: default's existing transaction-dependent
view, current's committed/pinned state and working's staged state. Comparison
does not commit, rollback or move history; existing lazy/thaw getter effects
remain observable. There is no promise of an atomic multi-field history snapshot.

Compatibility is exact generated facade class. Default/current/working are
different classes and their methods return NotImplemented across views; different
models and model subclasses also fail that guard. Two pins of the same current
class compare their respective exposed revisions. Explicit structural generation
sets `__hash__=None` on every facade, including pinned ones, because history and
working values can change. Disabling generation preserves existing identity hash.
Reject custom logical comparison/hash methods conflicting with enabled generation.
No new Undoable unsafe-hash option is introduced.

Consequently structural facade handles cannot be set/frozenset elements or mapping
keys. Managed tuple/list/value-map edges remain supported. A thaw/freeze callback
that constructs a hash container of structural handles receives normal TypeError;
do not restore identity hashing to bypass this restriction. Data-only SnapshotNode
handles keep their existing snapshot/node identity behavior and do not participate
in these generated facade comparisons.

Undoable owns its declaration wrapper in `undoable_markers.py`; Lifecycle marker
objects and `Compare: str` semantics remain untouched. New eligible declarations
accept boolean `compare=True` and a separate managed `write_compare="value"`.
The wrapper contains the original Lifecycle marker plus logical inclusion and
whether write_compare was explicitly supplied. Harvesting unwraps into the
existing synthetic Lifecycle declaration for transaction metadata, while storing
logical flags in Undoable schema separately. New managed declarations translate
their write policy into the legacy Lifecycle marker's string compare. Preserve
all existing marker parameters and function exports.

Preserve transaction node identity as well as the spelling of the write policy.
The present value-write path compares exposed values with `old == value`; after
structural generation that can accidentally equate distinct child nodes. Add an
Undoable-owned `write_detection.py` boundary used only by value-write detection:
paired traversal of original operands, never rebuilt containers, substituted
payloads or identity tokens. Its procedure is `write_equal(left, right)` with an
internal container-element context and an active recursion-pair stack:

1. In container-element context, `left is right` succeeds before invoking any
   equality method, including an opaque/nonreflexive leaf. This is native
   container identity-or-equality behavior. At the top level an opaque object's
   self equality is still invoked; do not add a blanket identity shortcut.
2. For two exact lists, or two exact tuples, use native same-container identity
   success, check lengths and visit element pairs in index order, applying the
   container-element rule and short-circuiting at the first false result. Do not
   traverse a list against a tuple, a container subclass or an opaque object.
3. For two exact dictionaries, preserve same-container identity success, check
   lengths, iterate left entries in native order, and perform one native lookup
   of each original left key in the original right dict (`get` with a private
   absence sentinel). A miss returns false; key hashing/equality exceptions
   propagate. Compare the original value pair in container-element context.
   Do not clone keys or values or implement a separate key matcher. This keeps
   key lookup direction and native hashing/identity behavior.
4. Exact set/frozenset combinations delegate to their original native equality,
   preserving hash-table lookup, identity shortcuts and comparison dispatch.
   Structural handles, including native hashable containers containing them,
   cannot be supported keys/elements because those handles are unhashable.
   Nested sets reached as list/tuple/dict values retain this same rule; opaque
   hashable objects are not opened to search for handles.
5. A MappingProxyType can wrap a user mapping, so its exact type alone does not
   authorize descent. Use a bounded CPython adapter on exact proxies only:
   `gc.get_referents(proxy)` must expose exactly one original backing mapping.
   Descend only when that referent is an exact dict. The adapter never calls
   `.copy()`, `.items()` or another mapping method on a user mapping, does not
   inspect any user object's referents, and returns the original backing object,
   not a reconstructed payload: the returned reference must be pointer-identical
   to the original backing dict in the adapter corpus. Contract-test this CPython
   shape on every supported minor. An unexpected referent count fails closed
   with UndoableDefinitionError before equality and fails the release gate; a
   single non-exact-dict referent stays opaque as specified below. No guessed
   fallback or ctypes/C-layout access. It needs no retained proxy registry or provenance
   mutation and works on previously escaped/input proxies as well as engine reads.
   With two dict-backed proxies, traverse backing-right/backing-left: left proxy
   forwarding first meets the right proxy, whose reflected forwarding determines
   this order. With dict-backed proxy on the left and exact dict on the right,
   traverse backing-left/right. With exact dict on the left and dict-backed proxy
   on the right, traverse backing-right/left: native dict equality defers to the
   proxy's reflected forwarding. A proxy wrapping a user mapping, including a dict
   subclass, is opaque and keeps its original callback/forwarding boundary; never
   substitute its mapping for a callback argument. If either side of a mixed
   comparison is opaque, do not unwrap the other operand. No freeze/thaw is called.
6. All remaining boundaries use original operands and historical rich-equality
   dispatch. If neither operand resolves to an engine-generated facade equality
   method, delegate directly to `bool(left == right)`. Otherwise perform the
   Python rich-equality slot procedure below with the engine-generated slot
   replaced by its pre-generation identity slot. Never invoke the newly generated
   facade equality as an accidental fallback of write detection. Explicit
   user-owned equality methods remain opaque callbacks.

The historical dispatch procedure looks up `__eq__` descriptors on each operand's
type MRO, bypassing instance attributes. Engine-generated logical equality
descriptors have a recorded historical replacement, `RuntimeFacade.__eq__`;
inherited engine descriptors use that same replacement. A user subclass's own
descriptor is retained. If the right type is a strict subtype of the left type,
try its bound descriptor first with the original left operand. Then try the left
descriptor with the original right operand; then the right descriptor unless
already tried. Bind descriptors using their normal descriptor protocol; a missing
method or exact NotImplemented continues dispatch. Convert the first implemented
result to bool once. If all return NotImplemented, use operand identity. This
preserves reflected-subclass priority, descriptor callbacks and NotImplemented
fallback. The historical RuntimeFacade slot returns False against a nonfacade,
rather than NotImplemented: a facade-left/opaque-right comparison must not start
calling the opaque method unless native subtype priority requires it. Two ordinary
engine facade leaves retain state identity across views, even if their logical
fields are equal. An opaque callback that deliberately compares facades internally
owns those comparisons; do not inspect or rewrite it.

Only active traversal pairs are tracked, not cached equality results: revisiting
an active pair raises the existing managed-container cycle diagnostic; shared
acyclic subobjects are compared again where native comparison would do so.
Identity shortcuts can avoid entering a graph at all. Native/opaque boundaries
that are delegated retain their native exception behavior. The entire procedure,
including original key lookup, descriptor calls and result truth conversion,
runs inside the existing manager `_call` comparison ownership fence. The
identity-write branch stays exactly `old is value` without traversal, callbacks
or extra truth conversion. Detector state is per call, discarded on success or
failure, and never enters history.

For the Safety regression, let `inner = [child_facade]` and let an opaque
`AcceptOriginal(inner).__eq__` accept only `other is inner`. Comparing
`(AcceptOriginal(inner),)` with `(inner,)` descends once, then delegates the
original opaque/list pair. The callback gets exactly `inner`. Reversing the outer
operands delegates the original list/opaque pair; the list's NotImplemented lets
the opaque callback receive that same original `inner`. Both return true without
visiting its child or substituting its contents. Test equal-valued distinct child
nodes and nested child edges separately under both write policies. Engine
membership, history and graph identity continue to use node IDs/state identity,
never logical facade equality.

Legacy `managed(compare="value"|"identity")` preserves that write policy and
logical inclusion=True. Reject a legacy string plus any explicit write_compare,
even an equal spelling. Boolean compare and a valid write_compare are independent.
No warning is emitted for the supported legacy spelling in this release. Old
Lifecycle markers imported directly remain accepted with logical inclusion=True;
excluded families remain excluded. Reject other nonbooleans and invalid policies.
write_compare applies only to managed fields; reject it on other families.

Eligible ordinary, const, static/lazy, managed and binding fields default to
logical inclusion=True. Initialization-only, class-variable, transient and local
storage kinds are excluded; their wrappers reject explicit compare=True and
accept compare=False where a common declaration API supplies it. Field deletion
removes its wrapper policy. Missing provider references still fail separately.
Undoable's inheritance adapter carries both controls without changing its existing
kind/transaction-key override constraints. Existing generic Undoable getter paths
are not refactored in this integration; shared methods emit direct public
attribute reads and introduce no additional name-based dispatcher.

## 9. Files, generation stages and specialization contract

Follow Lifecycle's repository structure:

```text
src/yidl_dataclass/
  __init__.py, py.typed
  dataclass.py                 decorator/build execution and source inspection
  dataclass_markers.py         public declarations and immutable policy objects
  dataclass_harvester.py       inheritance, normalization and definition checks
  dataclass_definition.py      typed immutable support carriers and layout plans
  factory_graph.py             signature binding, DAG and retention analysis
  stdlib_adapter.py            version-bounded std metadata processing
  class_replacement.py         namespace and closure preservation
  errors.py
  regenerate_dataclass_base.py
  _generated_dataclass_base.py
  yidl/
    dataclass_core.yidl
    dataclass_policies.yidl
    dataclass_factories.yidl
    dataclass_lazy.yidl
    dataclass_initvar_classvar.yidl
    dataclass_local_store.yidl
    dataclass_comparison.yidl
    dataclass_copy.yidl
    dataclass_base.yidl
tests/
  data/gold_src/, data/goldens/materialized/, actual_test_results/
  data/perf/
examples/, docs/validation/, dev-docs/
```

These are responsibility boundaries, not a requirement to create empty files.
The initial distribution depends on YIDL and Astichi, not Lifecycle or Undoable.
Use hatch packaging, the existing versioned YIDL golden harness, and a local uv
development source configuration with repository-relative paths. Package all
`.yidl` resources and generated bases in wheels/sdists.

Stage A, build/regeneration: compile modular YIDL sources and inherited concepts
with `compile_yidl_files`; emit the generated DDS/assembly runtime using
`emit_concept_runtime_source`; check in its generated base and provide a
`yidl-dataclass-regenerate-base` check/default and `--write` command. This stage
parses authored template resources once and verifies regeneration determinism.

Stage B, decoration: harvest into immutable typed support dataclasses; normalize
metadata and resolve signatures, dependencies, layout, liveness, method actions
and version policy. Lower validated facts into generated records and collections,
then invoke `build_DataclassModule(...).to_executable_ast()`. Execute the compiled
AST's builder with captured default/factory/callback objects and user namespace
bindings. Do not parse fresh Python snippets, format source into methods, invoke
std method generators, or perform feature-specific AST repair afterward.

Stage C, instance use: specialized generated code uses public/private accesses,
bound callback calls and necessary lazy/pipeline guards. No field metadata
dictionary is consulted on ordinary reads/writes, callback wiring or comparisons.
Compilation caching is not required for the initial release; measure cold and
repeated decoration separately before introducing it.

The pure specialization contract is: normalized immutable shape facts and
precompiled resources determine output structure; arbitrary runtime values are
bound externally, never converted to executable repr text. Callbacks are never
executed by harvesting/generation. Given identical shape/version/resource bytes,
generation produces equivalent AST/source with deterministic names and ordering,
independent of object ids, filesystem locations or callback repr. Generate a
fresh composition per decoration; callback bindings and retained values cannot
leak between classes. Use semantic support classes for field/policy concepts,
not new enums or an emitter switch disguised as a passive tag. Generated YIDL
variant/property facts may use the existing compiler's primitive schema boundary.

Source inspection is a documented `generated_source(cls)` export returning the
materialized source of this class build. Its external bindings use readable
stable names; it does not expose the objects' repr or claim to be a standalone
source file without those bindings. Canonical examples record the binding fixture
beside both readable generated source and observable behavior.

## 10. Required verification and experiment evidence

The next, separately reviewed TDD plan must turn these obligations into observable
red/green steps. This design specifies gates, not an implementation sequence:

1. Regeneration/layering: deterministic bases, packaged shared resource discovery,
   inherited matching, independent neutral fixture and both consuming classes.
   Inspect AST/source: plain writable fields are public slots; no property or
   generic read/write helper; every policy getter/call is field-specialized;
   shared comparison method bodies originate in the common YIDL productions.
2. Versioned differential corpus against std dataclasses on 3.12/3.13/3.14:
   signatures, factory sentinel display, Field/params metadata, kw-only/fences,
   defaults, repr recursion, empty/selected fields, exact classes, tuple versus
   conjunction equality (identity/NaN and observable equality callbacks), all
   ordering/hash actions, inheritance, weakrefs, matching and supported helpers.
   Include ordinary required init=False fields with custom init, suppressed init
   followed by explicit assignment, generated init without a consumer, and dict
   init=False simple-default fallback with an empty instance dictionary and a
   later class-default update. Verify an actual generated factory consuming an
   unavailable provider still diagnoses rather than silently omitting it.
   Pin intentional differences in the matrix, not blanket parity skips.
3. Canonical extension examples pair source with behavioral output: plain,
   converted, const and frozen mutable caches; independent/dependent factories;
   eager and delayed InitVars; class/self providers; lazy comparison/hash/repr;
   included/excluded fields across several instances/classes; local storage;
   copying and serialization. Examples include enough contrasting fields to
   inspect meaningful specialization without hidden fixture knowledge.
4. Narrow failure/mechanics tests: invalid flags/kinds/overrides, metadata adapter
   shapes, unresolved annotations, unbindable callbacks, cycles, self reentry,
   lazy retry/retention cleanup, failed setter atomicity, provider absence,
   forbidden mutation, active copy/pickle, unsupported combinations and exception
   causes. Test disabled YIDL branches by source/AST checks, not only executed
   runtime selections. Apply workspace braced-control-flow/conditional-boundary
   checks to any new or modified C-style/Rust support sources, if any.
5. Real Undoable goldens and full regression: defaults table; each view/type/pin
   boundary; unhashability when enabled; all combinations of logical inclusion,
   value/identity assignment policy and enabled/disabled structural generation.
   Distinct equal values must record under identity policy, identical references
   must skip, and excluded fields must change neither equality nor ordering.
   Verify that equal-valued distinct child-node edges still record replacement
   under value policy and that nested native containers preserve node identity;
   cover hash-container restrictions and unchanged SnapshotNode behavior.
   Add the AcceptOriginal narrow detector case and an integration case with
   staged opaque working values/custom freeze, in both operand directions, for
   legacy/new value-policy spellings with structural generation enabled/disabled.
   Assert callback operand identity and unchanged write/no-write outcomes. Cover
   opaque top-level nonreflexive self equality versus native container identity
   shortcuts, reflected strict-subclass priority, NotImplemented and nonboolean
   callback results, facade-left/opaque-right historical False without an extra
   opaque callback, the reverse direction, exact versus subclass containers,
   nested dict/set shapes and key-lookup exceptions, native-dict versus opaque
   mapping proxies (including escaped input proxies, exact original opaque
   callback operands and forwarding direction), the version-bounded proxy adapter,
   same-node cross-view identity, shared acyclic branches and entered
   cyclic pairs. Require these regressions inside the existing ownership fence.
   Include legacy strings, explicit conflicts, inherited declarations and a
   field-removal generation pair. Keep original experiment results untouched.
6. Install freshly built wheels in isolated environments on each supported
   interpreter. Verify all package resources; run a public-docs-only example and
   the comparison integration without workspace imports. Test wheel/sdist
   regeneration provenance. Record exact Dataclass/shared YIDL/Undoable revisions
   and dependency versions separately from historical reference tuples.
7. Independent design and implementation review, full relevant regressions,
   documentation/API matrix and final reproducible performance evidence.

Canonical success cases are the primary integration oracle; do not duplicate
their assertions in bespoke unit tests. Differential checks are the independent
oracle for the compatible subset. Designed goldens alone do not establish R5.
Use a fixed declarative desk evaluation against the instrument digest in
`DeclarativeEvaluation.md`, with corpus/API revisions, evidence and mode recorded.
Score B.1 as resolution scope and E6 with the field-removal diff; authoring locality
is separately checked. Report projected versus executed correctness/composition
evidence separately. LLM authoring-loop measures remain unscored without their
required harness/calibration inputs.

Benchmark equivalent logical fields on the same machine/interpreter against
stdlib default and slotted dataclasses. Compare plain reads/writes, const/frozen
reads and rejected writes, supplied/default/zero-argument construction,
repr/equality/order/hash and object memory. Independently measure extension
dependent factories, pipeline disabled/enabled, lazy first/cached reads and
cache writes; label operations without a std equivalent. Time generation/decorating
apart from instance work; measure retained-provider and lazy storage overhead as
well as shallow instance and aggregate allocated memory. Record whether a base
dict/weakref is present. Do not time setup or source emission in hot access loops.

Use a versioned harness with calibrated batches, warmups, at least five independent
process runs and repeated samples per case, retaining raw observations, units,
sample counts, medians and variation. Pin exact benchmark definitions, machine,
OS, CPU/power conditions, interpreter build, package tuple and commands. Separate
fresh-process cold decoration from in-process repeated decoration. The reviewed
TDD plan must fix any numeric acceptance/regression thresholds before results;
this design promises correctness and inspectable access paths, not speedup.

The owner records documentation/design/review/plan/implementation/final-validation
timestamps and each intervention/review/remediation. Preserve available actor/stage
token observations and raw attribution; mark missing telemetry unavailable.
Separate actual billed cost from dated API-equivalent estimates, cached-token
treatment and elapsed/active work. No original Undoable timing/cost result is
reused as a Dataclass measurement.

## Reference inspection

The reference inspection used Lifecycle's harvester, generated-base regenerator
and inheritable `lifecycle_*.yidl` resources; YIDL's
`tests/data/yidl/yidl_update_a_dataclasses_split` composition and canonical case;
and Undoable's marker aliases, synthetic Lifecycle harvest, class/view bundle and
RuntimeFacade identity methods. These are evidence for available integration
surfaces, not evidence that the proposed API is implemented.

Version checks used the primary CPython implementations for
[3.12](https://github.com/python/cpython/blob/3.12/Lib/dataclasses.py),
[3.13](https://github.com/python/cpython/blob/3.13/Lib/dataclasses.py), and
[3.14](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py), plus the
[3.14 public documentation](https://docs.python.org/3.14/library/dataclasses.html).
The versioned differential corpus remains necessary for any compatibility claim.

The mapping-proxy boundary uses the documented
[GC referent inspection API](https://docs.python.org/3.14/library/gc.html#gc.get_referents)
and the CPython exact proxy's single-mapping traversal and equality forwarding in
[descrobject.c](https://github.com/python/cpython/blob/3.14/Objects/descrobject.c).
A read-only CPython 3.12.12 probe observed one original dict referent and the
forwarding directions stated above. This inspection supports the proposed bounded
adapter; the three-minor adapter and dispatch regressions remain unexecuted.
