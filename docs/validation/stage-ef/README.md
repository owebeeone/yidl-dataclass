# Dataclass affected E/F verification

The Dataclass product and authoritative shared comparison resource are unchanged
from owner-verified D commit `23833598e4c7e78d073f20cf152c731fa5bb7bbe`.
Undoable consumes the pinned D wheel's shared resource at regeneration time;
normal Undoable decoration does not import Dataclass. The shared authority SHA256
is `2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef`.

Six recorded original-SDK source/regeneration/neutral-composition targets each
passed eight tests (14 deliberately deselected) across Python 3.12–3.14 and both
explicit native-rust/Python selections. These are affected verification targets,
not a new full Dataclass matrix or a product RED. The independently verified D
full matrix remains the baseline. Original SDKs/Lifecycle were not edited/built.

`increments.jsonl` preserves actual commands, backend, runtime, elapsed times and
raw/sanitized hashes. Original bytes are content-addressed externally at
`external:yidl-dataclass-stage-ef-raw`. `check_evidence.py` checks hashes/JUnit,
unchanged D source/tests, text hygiene and freezes this owning inventory. No new
performance claim is made. G/H and final Code/State review remain outstanding;
prior TDD/scope/process deviations remain disclosed in historical evidence.
