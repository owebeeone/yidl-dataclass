# Reference-only SDK observations during consumer Stage A

These observations do not authorize SDK edits or become optional SDK prerequisites.
They describe resource integration choices on original installed Astichi 1.1.3 /
YIDL 0.1.0; product generation remains within existing APIs.

| Observation/evidence | Impact and disposition |
| --- | --- |
| Global `astichi_ref` in a parameter annotation emitted an unlowered call; `a01-green-attempt-green.log` records the resulting NameError, and subsequent emitted source inspection located the annotation | Consumer integration error, not a claimed SDK defect. Existing identifier marker/bindings generate the correct captured Name. Nonblocking after authored resource correction; no SDK improvement required |
| An `astichi_pass` expression used as an assignment target yielded Load context; `a02-green-attempt-green.log` records builtin AST compile rejection | Consumer used the wrong assignment form. An ordinary authored identifier target plus existing identifier binding preserves Store context. No AST mutation or SDK improvement required |
| A zero-argument/empty-store constructor and disabled slot/init facilities lacked explicit contributions; `a03-red.log` records selected-native assembly rejection | Consumer assembly was incomplete. Empty parameter and statement resources/matchers provide supported contributions; the canonical corpus passes. No fallback, SDK change or narrowing of public storage semantics |

Direct field reads/stores still use existing attribute-path specialization.
Source-based generation and cache reuse are permitted by the operator boundary;
these facts do not revive precompiled-resource or Rust-restoration requirements.
