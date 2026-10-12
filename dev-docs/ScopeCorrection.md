# Dataclass scope correction

Status: operator-directed correction; SDK implementation is stopped.

The operator clarified that the task is the YIDL Dataclass implementation and
its YIDL resources, with no scope to modify Astichi or YIDL SDKs. The owner had
introduced parser-free whole-template restoration and strict Rust-owned lowering
as implementation prerequisites. Those were stronger requirements than the
requested direct slots and specialized generated field access. The owner should
have tested the existing generation route before widening the work.

`PrecompiledResourcesDesign.md`, `PrecompiledResourcesImplementation.md` and
`NativeLoweringAddendum.md` are now historical records of that detour. Their
review results establish only the scoped technical judgments stated there;
they do not override the operator's project boundary. P1–P4 are removed from
the active Dataclass prerequisite sequence. Keep all elapsed time and usage in
the experiment ledger, including the detour, failed attempts and scope correction.

YIDL SDK source remains unchanged at
`9d374f88445c426a56d5dd1f96fad112d1ec5417`. Its proposed precompiled-resource
policy, constructors, structural dynamic values and evaluation changes were not
implemented. No shared comparison resource was added to its library.

Astichi P1 was committed at `4a62b093498dae7b6d346306eae23e5925aaa004` over
baseline `1c47f781d3804130fdd61cbee07a3b2e4529158a`. P2 is uncommitted and
partial; its latest statement-splice source does not compile. A separate backup
preserves 222 files, the cumulative tracked patch, prototype binaries and a
verified P1 Git bundle. Backup manifest SHA256:
`c00fa2bc4c9be7edca98b1fb859111e9377f334325900f1edb2aa4149865ce15`.
The current SDK tree was left intact for inspection. No source restoration,
publication or deletion is claimed by this record.

Original installed Astichi 1.1.3 / YIDL 0.1.0 pass the focused probe recorded in
`docs/validation/baseline/original-sdk-results.json`: existing YIDL assembly
generates slots, equality and frozen hashing; existing `astichi_ref` binding
specializes direct attribute access; resource wrappers already cache compilation.
Both backend selections pass. This is core feasibility, not full Dataclass
parity, ordering, extensions, benchmarks or wholly Rust-owned generation.

The next consumer design correction must use existing source-based resources and
SDK APIs. Preserve direct slots, specialized straight-line accessors, field-local
policies, modular YIDL composition, real metadata/helpers and the requested TDD,
goldens, independent reviews and measurements. Source compilation during
generation is permitted; no new SDK artifact APIs or capabilities are required.
Reusable comparison resources must reside in a consumer repository rather than
being added to YIDL. Complete that boundary correction before product code resumes.
