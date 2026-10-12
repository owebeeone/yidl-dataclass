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
Slots configuration and default settings must be reconciled with compatibility goals.

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

## Experiment approach

The proposed follow-on experiment would use reviewed design, a separate TDD plan,
autonomous implementation and recorded time, token observations, estimated cost
and quality evidence, as in the Undoable experiment. Differential tests against
the standard library should establish retained behavior on supported Python
versions; extension tests should establish intentional differences. Benchmarks
should measure construction, field access and comparisons without assuming speed.
Creating this member does not start that implementation experiment.

## Reference evidence

- [Python dataclasses documentation](https://docs.python.org/3.14/library/dataclasses.html)
- [CPython dataclasses implementation](https://github.com/python/cpython/blob/3.14/Lib/dataclasses.py)

Python versions, helper interoperability, the precise public marker API, frozen
inheritance, private-provider copying, and lazy-field inclusion policies remain
open. Formal review should distinguish required behavior from these unresolved
choices before implementation.
