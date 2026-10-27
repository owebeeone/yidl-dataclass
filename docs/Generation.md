# Generation, source inspection and distributions

The consumer uses published Astichi 1.1.3 and YIDL 0.1.2. Authored modules live in
`yidl_dataclass/yidl`: core layout/constructor, comparison adapter, factories,
providers, pipelines, policies, lazy initialization/retention, copy and runtime-freeze support.
Inheritance and matching select only the field-specific contributions needed by
a declaration. The generated user class is plain Python; std dataclass method
generators do not produce its behavior.

Ordinary writable fields have public slots and direct operations. Policy fields
have individual private backing storage and generated bodies. The public property
is assigned from captured builtin property plus its field-specific getter/setter/
deleter functions. This is equivalent descriptor construction to @property and
@field.setter; separated public decorator contributions scoped identifiers
inconsistently on the original Python backend. There is no additional runtime
field access dispatcher. Private builtin captures also protect valid user names
such as property/type/Exception from accidental shadowing.

`generated_source(Model)` exposes the actual generated composition as readable
inspection source. It references a consumer-installed capture namespace and is
not a standalone model module. Defaults, factories/converters/validators and
callable argument defaults remain application objects in that namespace; existing
SDK name/path bindings refer to them. Objects are not supplied to literal SDK
bindings, serialized or repr-ed into source. Fresh decoration owns fresh captures;
shared resource compilation/caches do not share live user values or final classes.

YIDL/Astichi composition is the generation architecture. It does not imply wholly
Rust backend execution or parser-free decoration. Existing source templates may
compile/cache during generation. Both explicit original SDK selections,
`ASTICHI_LOWER_ENGINE=python` and `ASTICHI_LOWER_ENGINE=native-rust`, are verified.
No handwritten dynamic method-source generator or consumer AST repair is used.

Run `python -m yidl_dataclass.regenerate_dataclass_base` from an installed wheel to
check its base against packaged resources; `--write` is for intentional consumer
source maintenance. Stable logical source names make regeneration independent of
checkout/install paths. The wheel and sdist include all authored resources,
compiled Python base, regeneration code and py.typed, plus public documentation
and the introductory example. Rebuilding the wheel from the sdist requires the
same fixed SDK wheels and the build tool, not SDK source/rebuilds.

`yidl/shared/comparison.yidl` is a neutral, reusable native YIDL module. Dataclass
and independently authored consumers inherit its actual equality/order/hash
productions and override read/prelude matching as needed. The Undoable consumer
loads the pinned authoritative Dataclass wheel resource at regeneration time,
checks version and SHA256, and embeds generated resources/provenance in its own
base. It has no hand-maintained shared copy or Dataclass runtime dependency.

Undoable defaults eq=False/order=False. Its logical field compare is boolean,
while managed write_compare=value/identity is separate; legacy compare strings
retain write meaning. Enabled default/current/working views compare selected
exposed values with exact-class guards and are unhashable. During historical
value-write detection only, native bool(old == value) runs on original operands
within its existing ownership fence; an expiring ContextVar marker makes generated
facade equality use historical state identity for that callback scope. Normal
structural equality resumes outside it. Dataclass comparison has no such prelude.
See the Undoable public API for its separate transaction/view contracts.

Gearu owns release preparation, isolated verification, versioning and tagging;
see `RELEASE.md` and `gearu.toml`. Release publishing uses `.github/workflows/publish.yml` and the PyPI trusted
publisher for `owebeeone/yidl-dataclass`. Only a published GitHub release invokes
the upload job; ordinary pushes, pull requests and manual runs perform checks.
The tag must equal `v` followed by the version in `pyproject.toml`. The workflow
tests both lowering backends on CPython 3.12–3.15, builds wheel/sdist artifacts,
checks their metadata and runs installed-wheel examples and regeneration outside
the checkout. OIDC permission is limited to the publish job. The configured
publisher does not require a named GitHub environment or a stored PyPI token.
Packaging and correctness evidence is separate from performance measurements
and independent review; source shape alone proves no speed/memory claim.
