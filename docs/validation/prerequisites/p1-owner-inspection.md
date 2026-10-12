# Independent P1 inspection observations

These are owner probes against the evolving implementation, not a settled-tree
acceptance gate or replacement for owning-layer TDD records.

1. The drafter-only test environment did not expose the package to an external
   script. The owner used the established workspace development environment;
   that setup failure is not behavioral RED.
2. The initial source-compile tripwire also blocked a normal static module import.
   The corrected probe allows only compilation whose bytes exactly match the
   real absolute Python module file; it continues to block fresh fragments.
   This probe correction is not a product defect.
3. The corrected probe observed successful parser-free load/bind/keep/materialize,
   independent states, and rejection of three malformed AST field/context shapes.
   It then failed on an invalid Name identifier. The drafter independently
   recorded its narrow RED/GREEN correction in Astichi's P1 evidence.
4. A follow-up capture passed while the drafter was still making changes. Its
   initially selected `before-fix` filename does not establish pre-fix execution;
   the append-only index explicitly corrects that label. The correctly named
   `p1-owner-probe-working-tree.txt` contains that same actual successful output.

The owner repeats the checks after the drafter stops at the checkpoint and records
its exact tuple separately. Native behavior remains outside P1's Python-only gate.
