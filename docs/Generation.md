# Generation, source inspection and distributions

YIDL Dataclass generates Python methods specialized for a declaration. Inspect
those methods when you need to understand a model's constructor, field access or
comparison behavior. Most application code only needs the public declarations
and helpers from `yidl_dataclass`.

## Inspect generated source

```python
from yidl_dataclass import dataclass, generated_source

@dataclass
class Point:
    x: int
    y: int

source = generated_source(Point)
assert isinstance(source, str)
assert "__init__" in source
```

`generated_source(Model)` returns readable inspection source for the actual
composition. It refers to a consumer-installed capture namespace and is not a
standalone model module. Defaults, factories, converters, validators and callable
argument defaults remain captured application objects. They are not serialized or
represented as source literals. Fresh decoration owns fresh captures; shared
resource compilation does not share final classes or live user values.

## Field-specific behavior

Ordinary writable fields use public slots and direct operations. Fields requiring
read-only access, pipelines, lazy evaluation or runtime freezing use specialized
storage and generated accessors. Public properties are assembled from their
field-specific getter/setter/deleter functions. There is no general field access
dispatcher on the ordinary path. Builtin captures protect application field names
such as `property`, `type` and `Exception` from accidental shadowing.

Authored YIDL resources cover core layout and initialization, comparison,
factories/providers, pipelines, policies, lazy state/retention, copying and runtime
freezing. The generated user class is plain Python; stdlib dataclass method
generators do not produce its behavior. Source shape does not establish a speed
or memory advantage.

## Dependencies and backend selection

The consumer depends on published Astichi 1.1.3 and YIDL 0.1.2. On qualified
platform/version combinations with the required published wheels, no SDK source
checkout or rebuild is needed. See the
[platform/backend boundary](GettingStarted.md#platform-and-backend-boundary):
Astichi 1.1.3 has no Windows CPython 3.15 wheel and that source-build combination
has not been qualified. These backend selections are available within their
qualified platform/version combinations:

```sh
ASTICHI_LOWER_ENGINE=python python examples/first_use.py
ASTICHI_LOWER_ENGINE=native-rust python examples/first_use.py
```

YIDL/Astichi composition does not imply wholly Rust execution or parser-free
decoration. Source templates may compile/cache during generation. No handwritten
dynamic method-source generator or consumer AST repair is used.

## Check packaged resources

From an installed wheel, run:

```sh
python -m yidl_dataclass.regenerate_dataclass_base
```

The default operation checks the generated base against the authored resources.
`--write` is for intentional source maintenance, described in
[contributing](../CONTRIBUTING.md). Stable logical source names keep this check
independent of checkout/install paths.

The wheel and sdist include authored resources, the compiled Python base,
regeneration code and `py.typed`, plus the README, API/generation guides and
packaged introductory/runtime-freeze examples. The complete progressive guide
set is available on this site and in the repository; the package inclusion list
is controlled separately. Where the required published SDK wheels are available,
rebuilding from an sdist uses those fixed wheels and the build tool, without
rebuilding SDKs. This does not qualify a Windows CPython 3.15 SDK source build;
see the platform/backend boundary above.

## Shared resources and release checks

`yidl/shared/comparison.yidl` is a neutral reusable resource owned by this
package. Independent consumers can inherit its equality/order/hash productions
and adapt their field reads. Undoable consumes a pinned authoritative wheel
resource at regeneration time and has no Dataclass runtime dependency. Its
transaction/view behavior is a separate API.

Release preparation belongs to Gearu; see [RELEASE.md](../RELEASE.md).
The package workflow tests supported CPython 3.12–3.15 and both backends, checks
wheel/sdist metadata, and runs installed-wheel examples and regeneration outside
the checkout. Registry publication is limited to the release workflow. The
[documentation workflow](../.github/workflows/docs.yml) independently verifies
examples, builds this site and checks its local links, search and exclusions.
