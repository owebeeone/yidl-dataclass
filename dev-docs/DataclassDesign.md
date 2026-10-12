# YIDL Dataclass detailed design

Status: the semantic design was accepted at
`de7cadd25c1d3fd5deac0d978043284fa130da1c` after both replacement reviewers
reported GO. The active generation boundary now follows the operator-directed
`ScopeCorrection.md` and `ConsumerOnlyGenerationAmendment.md`, accepted at
`382d389172f38e33de8a00af350b1b6b21d46f5b` after fresh dual GO.
Astichi/YIDL changes and compiler P1–P4 are outside scope; the earlier compiler
designs/reports remain historical evidence. This document is an implementation
contract, not an implementation or performance claim; the TDD plan is separate.
The autonomous GO was given at `2026-10-12T03:36:48Z`; stage timestamps and measurements belong in the owner's
experiment ledger.

The controlling brief is `DataclassConcept.md`, `ExperimentProtocol.md`,
`GoldenExamplesAmendment.md`, `DeclarativeEvaluation.md`, and
`DataclassSpec-OperatorAmendment.md`, with the acceptance boundary recorded in
`CurrentProgramCheckpoint.md`. Bounded corrections may exceed two review cycles;
an architectural defect requires redesign. The paused UndoableLeaf proposal is
outside this design.

Component redesign: the write-detection boundary below replaces both the earlier
rebuilt-container projection and the subsequent manual paired traversal. Review
counterexamples exposed operand substitution, dictionary rehashing and tuple
prefix-evaluation defects. Neither approach is retained or extended. This revised
component changes the generated Undoable equality prelude and callback contract,
and both fresh independent design reviews passed before TDD planning. Their
reports and exact acceptance boundary are recorded in the design review result.

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

Own the authoritative neutral asset in Dataclass at
`src/yidl_dataclass/yidl/shared/comparison.yidl`. Dataclass wheels/sdists include
it, and its regenerator reads resources through `importlib.resources`. Undoable
reuses this same asset at build/regeneration time from a pinned candidate
Dataclass wheel, then ships its own self-contained generated base. It has no new
runtime Dataclass dependency or manually maintained comparison source copy.
Section 9 and `ConsumerOnlyGenerationAmendment.md` define the regeneration and
digest boundary. No resources, loaders or semantics are added to either SDK.

`comparison.yidl` exports `ComparisonCore`, defining ordered `ComparisonClass`
and `ComparisonOperand` facts, authored guard/read resources, and equality,
four ordering and optional hash productions. Concrete generation inputs are:

- Class identity/order and selected class-body target surface; requested method
  switches; equality mode (`UseTupleEquality` resolved for the interpreter);
  explicit hash action (generate, None or leave untouched).
- Ordered operands keyed by owner and field identity, inclusion already resolved
  separately for compare and hash; direct left/right structural read paths such
  as `self.price`, `other.price`, and a hash read path.
- A selected compatibility resource. Initial consumers select exact-class
  compatibility. The resource has no dataclass/transaction imports.
- An optional equality-method prelude contribution selected by consumer matching,
  before every self shortcut, compatibility guard and structural operand read.
  Its default is an empty resource. Dataclass selects that empty resource and
  emits no prelude branch, context lookup or context-related import. Undoable's
  adapter selects its own historical-write resource described in Section 8.

Read-path inputs are validated Name/Attribute paths, not arbitrary Python source;
the shared attribute-read resource lowers them using Astichi's `astichi_ref`
external path binding. Consumer extension resources may provide another structural
read expression through inherited authored resources, not consumer-formatted
method strings or runtime getters. Existing SDK source parsing is allowed during
generation; the consumer does not repair or transform the resulting AST.
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

The prelude is a native YIDL extension surface, not post-generation method
wrapping: shared equality productions expose `eq_prelude`, with a default empty
matcher contribution. `undoable_comparison.yidl` overrides that matcher with an
authored `HistoricalWriteIdentityPrelude` resource. The consumer installs the
private scope ContextVar and `RuntimeFacade.__eq__` method object under stable
private names in its exec namespace (or authored builder-function captures).
Existing SDK bindings receive their identifier/path strings, never these runtime
objects. Ordering and hash productions have no such prelude.

At regeneration, source maps use stable logical keys:
`shared/comparison.yidl`, `dataclass/<filename>.yidl`, and
`undoable/<filename>.yidl`. Consumer imports refer to
`../shared/comparison.yidl`. The Dataclass regenerator loads its own authoritative
resource; the Undoable regenerator loads that resource from the pinned Dataclass
wheel into the same logical source map. Record its SHA256, candidate version and
all local resource digests beside each generated base. The existing YIDL emitter
embeds the selected resource/matcher source into that base, so decoration needs
only the consumer and its existing SDK dependencies. No runtime cross-package
resource lookup occurs in Undoable. Regeneration requires the declared build
dependency and verifies its resource digest; changing the authority requires
regeneration of both bases. Ordinary Undoable wheel/sdist builds can use the
checked-in base; an sdist regeneration check installs the pinned build dependency
and reproduces it. See the amendment for the SDK-unchanged sharing gate.

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

There is one explicit contextual exception to structural equality: during the
synchronous value-write comparison scope below, generated Undoable equality uses
historical node-state identity, including calls originating inside opaque user
equality callbacks. Outside an active scope it uses the structural rules above.
This dynamic rule is part of the documented comparison API, not a claimed
invisible optimization. It also applies to other generated Undoable models whose
equality is invoked in that same active context. Dataclass equality is unaffected.

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

Preserve transaction node identity while leaving Python in charge of equality.
The existing value-write callback remains native `bool(old == value)` on the
original operands, inside the existing manager `_call` comparison ownership
fence. Enter a private historical-write scope around that expression only. The
identity-write branch remains exactly `old is value` inside its existing fence,
without a new scope or equality callback. Do not change field inclusion, current
read selection, write staging or either marker's effective assignment policy.

Own the scope in `src/yidl_undoable/write_comparison_context.py`. Its private
module-level `_historical_write_scope: ContextVar[_HistoricalWriteScope | None]`
defaults to None. `_historical_write_equal(old, value)` is the private synchronous
scope-and-native-expression function used by the manager. A scope
marker is a small slotted support dataclass with only mutable `active: bool`; it
contains no manager, node, operands, parent marker or context token. Each invocation
allocates a fresh marker initially active, sets the ContextVar and holds the
returned token in its synchronous stack frame. The scoped function then evaluates
`bool(old == value)` exactly once. In finally, set this marker's active flag to
False first, then reset the ContextVar with that token in the setting context.
Cleanup runs on success, comparison/truth-conversion failure and BaseException.
Do not use the 3.14-only token context-manager shorthand; the same explicit
set/try/finally/reset sequence applies to all supported minors.

The manager invokes the scoped function from its existing `_call` callback,
keeping scope setup, native equality, result truth conversion and scope teardown
inside the original ownership fence. The existing comparison diagnostic and
callback-depth/ownership checks remain in force. Scope creation and teardown
perform no model reads, freeze/thaw calls or additional equality. Operand
acquisition stays where it is in the current write path. Exceptions and their
existing notes/ownership faults propagate through that fence. The scope does not
permit same-manager mutation or authorize concurrent manager operations.

The adapter-selected YIDL equality prelude is precisely:

1. Read the private ContextVar into a method local.
2. If its value is non-None and that marker is active, immediately return
   `RuntimeFacade.__eq__(self, other)` using the bound historical method object.
3. Otherwise continue into the shared generated structural equality body.

The prelude executes before the version-dependent self-identity shortcut and
exact-class guard. Thus active write comparison uses the original RuntimeFacade
state identity across default/current/working views and against opaque operands,
including its False result against a nonfacade. Python still decides which
operand's rich-comparison method to invoke, reflected strict-subclass priority,
NotImplemented handling, descriptor behavior and truth conversion. A user-owned
subclass equality method is not replaced: native dispatch still invokes it, and
calls it makes to a generated Undoable equality method obey the same active
scope. No method is monkey-patched and no special-method dispatcher is emulated.
Structural classes remain `__hash__=None` in every context; the prelude does not
make them hashable. Generated ordering remains structural in every context and
has no scope branch. Read-only data SnapshotNode equality remains unchanged.

An opaque callback comparing two generated facade handles while evaluating a
write now intentionally receives historical identity behavior, matching the
pre-structural-generation engine. This applies even if it calls equality directly
rather than letting a native container call it. Its original input operands and
its own callback implementation are preserved. The earlier proposed exception
letting such callbacks observe new structural equality during write detection is
withdrawn: it contradicted preservation of the old value-write boundary. Explicit
ordering inside an opaque callback remains the new requested ordering behavior;
this component does not claim historical parity for newly opted-in operators or
arbitrary user callback changes.

Nested synchronous scopes allocate independent markers. Inner teardown closes
its own marker and resets its token to restore the enclosing marker; subsequent
parent-context equality remains historical until the outer scope closes. A
copied context holds the marker object by reference. Closing it before token
reset means an escaped copied context/task sees a closed marker and returns to
normal structural equality when it later invokes a generated method. A copy of
an inner scope does not resurrect the outer marker after the inner closes; only
the original context's token reset restores that outer scope. Closed markers can
remain in copied contexts but contain no manager/node data and never reactivate.
There is no global class mutation, global active boolean, thread-local fallback,
parent-marker chain or global context/operand registry.

A copied context deliberately run while its captured marker is active sees the
historical rule. Explicit empty contexts see the ordinary structural rule.
Thread inheritance defaults vary by interpreter/build; do not assume a new
thread is empty, and test explicit `Context()` versus explicit `copy_context()`
execution. Async task context copying follows the same marker-lifetime rule;
comparison remains synchronous and does not await. A concurrent invocation that
has already read an active marker can finish its identity branch after closure;
there is no atomic cutover for in-flight calls or new concurrency guarantee for
Undoable managers. Later prelude checks after closure must see the closed marker.
No scope state enters model storage, schemas or history.

Native equality keeps native dictionary cached-hash lookup and collision order,
tuple/list prefix evaluation, element identity shortcuts, proxy forwarding and
opaque operands. There is no traversal, recursive dispatcher, rehashing lookup,
rebuilt payload, proxy unwrapping, GC adapter, ctypes/C-layout access or hash-mode
switching in this design. Do not introduce a preliminary normalization/inspection
pass to "help" the native expression. Cycles retain native equality outcomes
(including identity shortcuts and possible RecursionError) at this boundary;
existing managed read/freeze/graph cycle diagnostics remain at their existing
boundaries. No new detector promises a uniform cycle exception.

For AcceptOriginal, let `inner = [child_facade]` and let the opaque callback accept
only `other is inner`. Native comparison of `(AcceptOriginal(inner),)` against
`(inner,)`, and the reverse direction, passes that same original inner list to
the callback and does not walk/rebuild it. A separate native comparison of
containers holding equal-valued distinct nodes reaches their generated equality
prelude and observes state identity, recording replacement. Scope setup adds its
own overhead and the prelude adds a context lookup to enabled Undoable equality;
measure both. Dataclass method code and ordinary field access incur no scope cost.

The implementation corpus must check this boundary against native expressions
and the pre-integration Undoable write path, rather than another hand-authored
container comparator. The following is the required component matrix:

| Scenario | Required evidence |
| --- | --- |
| Dictionaries with opaque keys | Shared keys and distinct equal keys; constant-hash counters, post-construction raising hashes, deliberate collisions and key-equality exceptions; zero additional hash callbacks from comparison relative to native equality; preserve key/value callback order and early exit |
| Tuple versus list lengths | Unequal lengths with common-prefix True, False, raising and observable truth-returning comparators, both directions; tuple prefix effects and contrasting list early rejection; identical nonreflexive elements retain native identity shortcuts |
| Proxies and opaque boundaries | Dict/proxy, proxy/dict and proxy/proxy; escaped proxies and custom mapping-backed proxies; original callback argument identity and native forwarding direction; AcceptOriginal with the exact original inner list in both directions |
| Facade leaves and user callbacks | Distinct equal-valued nodes, same-node cross-view/pinned handles, nested native containers; opaque equality directly comparing handles observes historical identity; native reflected/subclass priority, NotImplemented and nonboolean result truth conversion; nonfacade comparison keeps historical False when the facade slot runs |
| Scope recovery | Success, equality error, truth-conversion error, BaseException and ownership fault; marker is closed and ContextVar restored on every exit; next ordinary generated equality is structural; mutation remains rejected by the existing ownership fence |
| Nested/captured contexts | Nested scopes and cross-manager callbacks restore outer scope; copies captured at outer/inner depths observe closed markers after their own scope ends; explicit empty and copied thread contexts, async tasks running before/after closure; document concurrent in-flight sampling rather than assert atomic cutover |
| Hash/order and cycles | Structural handles remain unhashable inside/outside scope; ordering remains structural; native cyclic equality success/error remains native, with existing read/freeze/graph cycle checks still enforced where applicable |
| Generated source and cost | Undoable prelude precedes all structural guards/reads; Dataclass generated eq has no prelude/context import; native expression receives unchanged operands; benchmark ordinary enabled Undoable eq and value-write scoping separately |

Run the dictionary/tuple/proxy/opaque working-value scenarios through managed
fields with the existing custom freeze/thaw extension, not only through a scope
unit probe. Across supported minors cover legacy `compare="value"|"identity"`
and new boolean-compare/write_compare declarations, generation enabled/disabled,
and logical inclusion true/false where eligible. Value policy must preserve the
native callback/write decision; identity policy must remain `old is value` with
no equality callback or newly created scope. Include a comparisons-disabled
parent whose managed values contain comparisons-enabled child nodes: scoping
belongs to value-write detection regardless of the parent's structural options.
Keep source inspection, narrow
failure tests and canonical integration evidence distinct, without duplicating
the same successful scenario in bespoke tests.

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
    shared/comparison.yidl
tests/
  data/gold_src/, data/goldens/materialized/, actual_test_results/
  data/perf/
examples/, docs/validation/, dev-docs/
```

These are responsibility boundaries, not a requirement to create empty files.
The initial distribution depends on YIDL and Astichi, not Lifecycle or Undoable.
Use hatch packaging and the existing versioned YIDL golden harness. Candidate
Dataclass build/runtime environments lock original `astichi==1.1.3` and
`yidl==0.1.0`; no SDK candidate versions or editable overrides to the preserved
SDK prototype are permitted. Any local consumer development references use
repository-relative paths. Package all `.yidl` resources and generated bases in
wheels/sdists. Original-SDK three-minor validation remains required.

Stage A, build/regeneration: compile modular YIDL sources and inherited concepts
with `compile_yidl_files`; emit the generated DDS/assembly runtime using
`emit_concept_runtime_source`; check in its generated base and provide a
`yidl-dataclass-regenerate-base` check/default and `--write` command. This stage
parses authored YIDL sources and verifies regeneration determinism. The emitted
base contains source-based SDK resource wrappers; their existing
`MatcherGeneratedValue.to_generator()` compiles lazily and caches that template
within the wrapper. This is ordinary supported source generation, not an artifact
restore protocol or a zero-parser guarantee.

Stage B, decoration: harvest into immutable typed support dataclasses; normalize
metadata and resolve signatures, dependencies, layout, liveness, method actions
and version policy. Lower validated facts into generated records and collections,
then invoke `build_DataclassModule(...).to_executable_ast()`. Execute the compiled
AST in a fresh consumer exec namespace containing default/factory/callback
objects under deterministic private names and the required user namespace values.
Generated methods reference those names; SDK external/ref bindings receive only
their validated name/path strings or supported literals, never arbitrary Python
objects. For example, capture the factory as `_y_dc_factory_0` in that namespace
and bind the authored factory reference to the string `_y_dc_factory_0`. An
authored builder function may instead receive ordinary Python arguments and
retain captures in closures. No object serialization, executable repr or callback
execution is involved. The Undoable ContextVar/identity method follows the same
consumer capture route. Use existing external/identifier/ref bindings, holes and matcher-selected
contributions. `self.astichi_ref(external=field_name)` specializes to direct
attribute reads; the existing transparent `._` assignment form specializes stores.
Generation may parse/cache authored resources and use SDK literal/import/edge
value facilities. Do not handwrite a dynamic method-source emitter, interpolate
per-field method snippets, invoke std method generators, or repair the AST.
Native YIDL composition names this resource/matcher composition; it does not
promise wholly Rust-owned execution or require selecting a Rust backend.

Stage C, instance use: specialized generated code uses public/private accesses,
bound callback calls and necessary lazy/pipeline guards. No field metadata
dictionary is consulted on ordinary reads/writes, callback wiring or comparisons.
Keep the SDK's existing resource compilation cache. Generate fresh class builds
and external bindings; do not cache model values or final classes. Additional
consumer caching is not required; measure cold and repeated decoration separately.

The pure specialization contract is: normalized immutable shape facts and
authored resources determine output structure; arbitrary runtime values remain
in the consumer namespace or authored builder-function captures described above,
never SDK-bound objects or executable repr text. Callbacks are never
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

The TDD plan turns these obligations into observable red/green steps. This design specifies gates, not an implementation sequence:

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
   runtime selections. Workspace braced-control-flow/conditional-boundary checks
   still apply to any authorized C-style consumer work; SDK/Rust support
   edits are outside this experiment.
5. Real Undoable goldens and full regression: defaults table; each view/type/pin
   boundary; unhashability when enabled; all combinations of logical inclusion,
   value/identity assignment policy and enabled/disabled structural generation.
   Distinct equal values must record under identity policy, identical references
   must skip, and excluded fields must change neither equality nor ordering.
   Verify that equal-valued distinct child-node edges still record replacement
   under value policy and that nested native containers preserve node identity;
   cover hash-container restrictions and unchanged SnapshotNode behavior.
   Fulfill Section 8's native-comparison/context matrix, including inherited
   operand-substitution, dictionary-hash and tuple-prefix counterexamples. Test
   scope/prelude composition and callbacks inside the existing ownership fence;
   do not substitute a manually emulated native-equality oracle. Public docs
   must state the contextual historical equality rule and unchanged unhashability.
   Include legacy strings, explicit conflicts, inherited declarations and a
   field-removal generation pair. Keep original experiment results untouched.
6. Install freshly built wheels in isolated environments on each supported
   interpreter. Verify all package resources; run a public-docs-only example and
   the comparison integration without workspace imports. Test wheel/sdist
   regeneration provenance and build-only comparison reuse without a runtime
   Dataclass dependency in Undoable. Record exact Dataclass/Undoable revisions
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
Separately benchmark the new Undoable equality prelude outside write scope and
native value-write equality inside scope against the pre-integration engine;
record marker allocation, context set/reset and lookup overhead. These integration
measurements remain separate from Dataclass-versus-stdlib results.

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

The redesigned boundary uses the public
[ContextVar/context API](https://docs.python.org/3.14/library/contextvars.html),
with explicit set/reset on all supported minors. Read-only in-memory probes on
CPython 3.12.12, with bytecode writes disabled, observed native dictionary equality
adding no key-hash calls after preparation (including a key rejecting later
hashing), unequal-length tuple prefix callback execution versus list early length
rejection, original AcceptOriginal list arguments in both directions, and native
proxy comparisons without an explicit rehashing lookup. Separate ContextVar
primitive probes observed nested restoration, marker closure after an exception,
closed markers in copied contexts and an explicitly copied thread context, and
an async task seeing its copied marker closed after synchronous scope teardown.
These are observations of Python primitives, not tests of generated Undoable
preludes, manager integration, performance or the complete three-minor matrix.
The required implementation corpus and two fresh reviews remain outstanding.
