# YIDL Dataclass concept

Status: discussion requirements captured on 2026-10-12 (Australia/Sydney).
This is a starting specification, not an accepted implementation design.

## Standard behavior and metadata

Aim for close compatibility with Python dataclasses, including constructors,
defaults/factories, representation, equality, ordering, hashing, inheritance,
frozen behavior, slots, keyword-only fields and pattern matching. Preserve field
and decorator settings in class metadata shaped like `__dataclass_fields__` and
`__dataclass_params__`; instance values live in the class's instance attributes or
slots. Standard `field()` parameters should be supported as closely as possible.

Consider compatibility with field inspection and copy-with-changes operations
such as `dataclasses.replace`, and with other standard helpers. Exact interoperability
is an objective to investigate, not an established guarantee. The operator
explicitly replaces the standard post-init initialization mechanism with named
factory dependencies; this intentional difference must be documented.

## Single generated class

Store fields and generate behavior on one class. No separate facades, transaction
manager or externally stored state are needed. Follow Lifecycle's specialization
approach: generate direct field accesses and factory arguments where practical,
using private backing slots for policies that need generated properties.

Slots are the default. An ordinary read-write field must be a public slot, with
normal Python attribute access and no generated property, name-based helper,
per-field dictionary lookup or generic runtime dispatch in its access path.
This changes the standard decorator's default; the detailed design must decide
whether an explicit nonslotted option remains supported for compatibility.

For constant, frozen, lazy or other fields needing access behavior, generate
field-specific properties and, where applicable, property setters over private
backing slots. Read-only properties must reject public replacement and deletion;
the exact exception contract needs to be specified. Constructor/internal lazy
writes use the permitted backing storage directly.

Resolve field names, provider wiring, policy selection and other information known
at generation time during generation. Generate direct field and factory accesses,
with straight-line code wherever semantics permit. Retain necessary runtime work,
such as actual conversion/validation callbacks, lazy initialization checks and
failure guards. Shared generation helpers are acceptable; generic runtime
accessor dispatch is not the default design. A field with assignment conversion
or validation may require a property and must be benchmarked separately from an
ordinary read-write slot.

## Reusable comparison generation

Keep generators for field-by-field equality and ordering in a separate YIDL file
or module that can be composed into other generated class families. The goal is
to reuse this facility in YIDL Lifecycle and YIDL Undoable, rather than coupling
the comparison templates to dataclass storage or decorator machinery.

The consuming generator supplies the ordered comparison fields and generated
expressions for reading each operand's field values. Dataclass composition uses
its selected fields and specialized access paths; Lifecycle or Undoable can
supply their own access expressions and explicitly chosen view semantics. Resolve
this adaptation during generation, without adding generic runtime field lookup.

For dataclasses, retain the agreed standard comparison semantics and field
exclusion flags. Reuse must not silently compare private caches, initialization
providers, transaction metadata or different state views. Consumer-specific type
compatibility and field selection rules belong in the explicit generation
contract. The detailed design should identify which related generation pieces,
such as hashing, can share this boundary while preserving equality/hash consistency.

Use YIDL Undoable as the second consuming generator to demonstrate actual reuse,
with canonical generated output and behavior checks. Plan an extension of its
decorator with dataclass-style `eq` and `order` options, and applicable per-field
comparison selection. Dataclass fields use the standard boolean `compare` flag.
Undoable already has `managed(compare="value"|"identity")` for transaction write
detection; it must retain that independent meaning. Do not overload or reinterpret
the shared Lifecycle marker's setting.

For Undoable, provide `compare_fields` on the decorator as a mapping from field
names to boolean inclusion overrides. It selects fields for generated equality
and ordering only. Eligible ordinary, const, static/lazy, managed and binding
fields default to included. Initialization-only providers, class variables,
transient fields and local storage are excluded; reject attempts to include them,
unknown names and nonboolean overrides at decoration. The adapter supplies this
logical selection separately from the managed assignment policy to the shared
comparison generator. No change to Lifecycle's existing marker API is required.

The Undoable generation defaults are `eq=False, order=False`; these differ from
the standard dataclass equality default to preserve existing node-identity
equality and hashing. Disabling structural generation preserves that behavior.
Bare and empty-parentheses decoration have identical effective defaults.

| Undoable decoration | Requested generation/result |
| --- | --- |
| `@undoable` | Existing identity equality/hash; no generated ordering |
| `@undoable()` | Same as bare decoration |
| `@undoable(eq=False, order=False)` | Same disabled-generation behavior |
| `@undoable(eq=True)` | Field equality; no generated ordering |
| `@undoable(eq=True, order=True)` | Field equality and ordering |
| `@undoable(order=True)` | Reject: omitted `eq` defaults to false |
| `@undoable(eq=False, order=True)` | Reject incompatible options |

For example, the following proposed API independently expresses an identity
assignment policy and exclusion from logical comparison:

```python
@undoable(eq=True, order=True, compare_fields={"cache": False})
class Model:
    value: int = managed(default=0)
    cache: tuple[str, ...] = managed(default=(), compare="identity")
```

This is a design requirement, not currently implemented syntax. Both transaction
policies must remain unchanged with structural comparisons enabled or disabled.
Require tests of all combinations of value/identity assignment policy and
included/excluded logical fields: distinct equal values record a replacement
under identity policy, the same reference skips, and excluded fields affect
neither generated equality nor ordering. Keep the two metadata controls separate.

The Undoable adapter must explicitly define which values its default, current
and working facades compare, cross-view/type compatibility and hash behavior for
values that change as history moves. This amendment authorizes planning that
integration, not an immediate runtime edit during requirements discussion.
Lifecycle remains a prospective consumer of the same module.

## Factories and initialization providers

Factory parameter names identify field providers. Parameters receive instance
values, including explicit constructor inputs and defaults. Resolve dependencies
in their required order. Ordinary functions and lambdas both work. Preserve the
useful class-provider and opt-in instance-provider concepts from Lifecycle/Undoable.

An initialization-only variable is distinct from constructor-parameter inclusion.
It may be a parameter, or may be produced from a default/factory without appearing
in the signature. Several field factories may depend on its value. It is not an
ordinary exposed instance field.

Eager-only initialization variables can remain constructor locals. A variable
needed by a later lazy factory must be retained privately on the instance, without
becoming part of normal field access, representation, equality or serialization.
Its declaration may remain in initialization metadata. Retention/cleanup and copying
of these private providers require an explicit design rule.

## Conversion and validation

Provide optional field conversion and validation, plus an optional default
conversion policy. Example: an integer field can opt into converting a supplied
float with the integer converter. The proposed pipeline converts, validates and
only then installs or provides the value to dependent factories. Input values and
factory results need a coherent policy. Exact converter/validator signatures,
type-derived defaults, diagnostics and assignment-time behavior remain to be settled.

## Constants and frozen overrides

An explicit constant field is read-only after construction. A frozen class can
make ordinary fields effectively constant by default while allowing explicitly
nominated mutable fields, such as caches. Constructor writes remain permitted.

A proposed tri-state field mutability option inherits the class default when
unspecified, permits writes when explicitly mutable and requests read-only behavior
when explicitly nonmutable. Exact spelling and precedence remain design decisions.
Cache fields should be excluded from equality/ordering and hashing, and optionally
representation. Standard comparison flags cover both equality and ordering.
Define reference replacement separately from mutable contents; freezing need not
recursively freeze stored objects.

## Lazy values in frozen classes

On first access, compute, convert and validate, then cache the successful result
privately. Subsequent reads return that cached value. A frozen/publicly read-only
lazy field permits its internal first initialization but forbids public replacement
or deletion unless an explicit mutable policy allows them.

Failure leaves the target unset for retry. A lazy field participating in comparison
or hashing materializes when those operations access it. Private initialization
providers must remain available to the delayed factory. Recursion, dependency
cycles, callback behavior and hash stability require detailed rules and tests.

## Field families and scope

Provide ordinary fields, constants, lazy fields, initialization-only providers,
class variables and local storage for per-instance caches or management data.
Aim to recognize the standard `ClassVar` and `InitVar` annotations alongside any
convenience declarations. Local storage should default to exclusion from logical
equality, ordering and hashing; inspection, representation, copying and
serialization rules still need to be specified.

Conversion, validation and named factory dependencies are options on applicable
field kinds rather than additional kinds. Transactional fields and transaction
managers are outside this single-state dataclass's scope.

Pydantic is a useful reference for validation, conversion, diagnostics and schema
features, but its complete model framework is not a requirement. Additional
features such as whole-object validation, aliases, JSON serialization and JSON
Schema generation remain candidates, not agreed scope. Its data-aware factories
already support dependencies through a mapping of earlier validated fields;
the proposed named-parameter dependency resolution must be assessed on its own
contract rather than described as an absent Pydantic capability.

## Experiment approach

This is a second experiment in producing a working library from the agreed brief
with as little operator intervention as possible. Use reviewed design, a separate
TDD plan, autonomous implementation and recorded time, token observations,
estimated cost and quality evidence, as in the Undoable experiment. Measure both
correctness and performance against standard Python dataclasses, including a
slotted baseline. Detailed measurement and evidence requirements are in
[Experiment protocol](ExperimentProtocol.md).

This document records the requested brief. Documentation preparation, the design
start and the autonomous implementation start must have separate timestamps; do
not retroactively count member creation as the implementation start.

## Reference evidence

- [Python dataclasses documentation](https://docs.python.org/3.14/library/dataclasses.html)
- [CPython dataclasses implementation](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py)
- [Pydantic field and factory documentation](https://docs.pydantic.dev/latest/concepts/fields/)

Python versions, helper interoperability, the precise public marker API, frozen
inheritance, private-provider copying, and lazy-field inclusion policies remain
open. Formal review should distinguish required behavior from these unresolved
choices before implementation.
