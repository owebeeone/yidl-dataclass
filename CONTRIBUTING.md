# Contributing

Keep changes in the component that owns them. Application documentation and
examples live in this repository; Astichi, YIDL, Lifecycle and Undoable are
separate dependencies or reference projects. A documentation task does not
authorize changing their code or this package's public behavior.

Read `AGENTS.md` and the workspace instructions before editing. Record intended
outcomes, permitted components and reference-only dependencies before implementation.
For releases, follow [RELEASE.md](RELEASE.md) and Gearu rather than publishing
from a checkout.

## Work on public documentation

Public pages live in `docs/` and their explicit navigation is in `mkdocs.yml`.
Keep `docs/API.md` and `docs/Generation.md` URLs stable. Put complete runnable
programs in `examples/`; readers should be able to run them after installing the
published package, without SDK source trees. Guide Python blocks execute in page
order with a fresh namespace for each page. Reference signatures are descriptive,
not runnable examples.

Use the stdlib dataclasses documentation as a benchmark for the level of detail:
explain defaults, constraints, accepted combinations, callback arguments, side
effects and failures. Keep learner introductions focused on what readers can do.
Implementation experiments and review history belong in `dev-docs/`, and existing
validation evidence stays in `docs/validation/`. Neither directory is published
as site content or copied into the search index.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r docs-requirements.txt
python -m pip install .
ASTICHI_LOWER_ENGINE=python python dev-docs/documentation/verify_examples.py
python -m mkdocs build --strict
python dev-docs/documentation/check_site.py build/docs-site
```

The verifier uses the installed package. Run it after installing the intended
published version when reviewing published behavior; `python -m pip install .`
is the workflow's separate checkout-install check. It does not add `src` to the
import path. Guide blocks and standalone examples have separate namespaces.
Generated evidence goes to `build/docs-example-evidence.json`, outside the public
site. The site checker verifies local links/anchors/assets, the repository base
path, search presence, source/evidence exclusions and machine-path leaks.

`python -m mkdocs serve` previews the site locally. A hook rewrites valid links
from public pages to repository files such as examples and contributor guides,
so those files are not copied into the site. Use paths relative to the repository
that owns the file. Do not commit generated site output or absolute machine paths.

The docs-only workflow builds on pull requests and relevant pushes. Deployment
runs only for `owebeeone/yidl-dataclass`, on `main`, outside pull requests, after
all documentation checks pass. Its Pages/OIDC permissions are confined to the
deploy job; package publication stays in `.github/workflows/publish.yml`.
Changing Pages settings, publishing a package or pushing branches/tags requires
the corresponding user authorization. Local verification does not deploy anything.

## Work on implementation

Install the supported fixed SDK wheels and the package's development extras in
an isolated environment. The normal checks are:

```sh
python -m pytest -q
python -m yidl_dataclass.regenerate_dataclass_base
```

The regeneration command checks by default. Use `--write` only for an intentional
authored-resource change and inspect generated differences. Do not hand-edit the
generated base to substitute for an authored YIDL change. Keep field policies
local to declarations and preserve hidden-provider/copy/freeze contracts.

Prefer canonical fixture/golden/integration coverage for successful end-to-end
behavior and narrow tests for parsing, diagnostics and edge failures. Avoid
duplicating the same success assertions in bespoke tests. Run checks appropriate
to the change; library/package release checks and supported-version/backend
matrices are specified by the repository's release process.

Control-flow bodies in C-style languages require braces, and conditional
compilation must have explicit enclosing boundaries. Inspect disabled platform
branches with syntax-aware source checks where applicable. Treat attributes and
owning scopes as part of a moved/deleted declaration. Record broader migrations
or out-of-scope findings separately instead of implying they were completed.
