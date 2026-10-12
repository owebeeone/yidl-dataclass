# P2 owner inspection

This is working-tree discovery, not a settled acceptance report or canonical
TDD RED. The sole drafter owns regression tests and remediation.

## Raw native metadata table correspondence

Observed UTC: 2026-10-12T08:14:19.511386+00:00

Using Astichi local sources, Python 3.12.12 and explicit Python compilation of
`astichi_bind_external(value)\nvalue` with origin `templates/raw.py`, copy the
result's package snapshot and append `unused-owner-probe` separately to its
`string_table` and `ast_path_table`.

Both calls to `artifacts.native_bridge.validate_package_correspondence` accepted
the changed package. Direct Rust `register_template_artifact`, supplied the same
syntax and origin after `ensure_current_native_surface_bundle` in a fresh engine,
also accepted both variants. Each temporary engine was closed in `finally`.
No shared engine or source files were mutated by these probes.

The validation computes a complete normalized signature but compares only
selected sections, records and locator counts. Public loading compares the whole
package signature; this raw ABI path does not. The accepted complete-package
correspondence and pre-registration validation contract requires an owning-layer
negative regression and rejection without partial registration. The drafter was
notified with the reproducer; no closure is claimed here.

The first inspection invocation lacked the local `src` import path and failed
with `ModuleNotFoundError`. That was setup-only, not behavioral RED. Corrected
source-path inspection and the subsequent direct Rust probe produced the invalid
acceptance observations above.
