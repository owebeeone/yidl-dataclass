import datetime
import json
import pathlib
import shlex

root = pathlib.Path(__file__).parent
started = datetime.datetime.fromisoformat('2026-10-12T15:02:38+00:00')
ended = datetime.datetime.now(datetime.timezone.utc)
metadata = {
    'actual_author_start_utc': started.isoformat(),
    'actual_author_end_utc': ended.isoformat(),
    'author_elapsed_seconds': (ended - started).total_seconds(),
    'original_go_utc_as_dispatched': '03:36:48Z',
    'immutable_consumer_revision_as_dispatched': '446dc1ee5d9cbe9d2b4c485bb2675eaddbdc138f',
    'wheel_sha256': '50e7a1b17f68de56d88441ee47df8d2b0a4377981dd236e591d2a8eff8ff5f1b',
    'billing_metadata': 'Unavailable to author; not zero. Captured separately by owner.',
    'final_programs': ['card1_attempt02.py', 'card2_attempt01.py', 'card3_attempt01.py',
                       'card4_with_cache_attempt02.py', 'card4_without_cache_attempt02.py'],
    'card_program_executions': 8,
    'card_failed_executions': 3,
    'required_clarification': None,
    'implementation_verdict': 'Not performed in author phase',
}
(root / 'author-metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
parts = [
    '# Dataclass cold public authoring record\n',
    'This is an uncalibrated first-day public-author observation. It is not an overall declarativity score or an implementation review/verdict. The author stops after this record awaiting a separate final Code review task.\n',
    '## Scope and cold boundary\n',
    'Deliverables: four runnable public-API cards, saved first sources and every repair, exact execution evidence, immutable wheel/documentation checks, and this standalone record. Only this external author directory was written. No repository, installed package, dependency or Git changes were made. Dataclass was the installed immutable product; Astichi 1.1.3 and YIDL 0.1.0 were reference/runtime dependencies. Undoable was unnecessary and not inspected.\n',
    'Before authoring, AGENTS_GWZ.md and the dispatched author brief were read. The sole product documentation read was the installed README.md, docs/API.md, docs/Generation.md, and examples/first_use.py, reproduced below in the documentation-read stdout and copied under public-docs/. Public callable signatures, public package origins, public performance-counter metadata, standard field helpers, __slots__, and public field descriptors were inspected. No implementation source, callable bodies, private attributes, private documentation, designs/plans, tests/goldens, oracle snapshots, or other-agent reports were read. No agents were spawned and no drafter hints were requested.\n',
    '## Timing and identity\n',
    '```json\n' + json.dumps(metadata, indent=2) + '\n```\n',
    'The consumer revision is dispatch provenance; no Git inspection was performed. The wheel archive bytes and the four installed documentation files were hashed at the start and end and remained identical. Public package origins were under the isolated interpreter sys.prefix. python -I excluded the author directory, sibling checkouts and PYTHONPATH from import resolution.\n',
    '## First-day outcomes and author decisions\n',
    '| Card | Final program | Result |\n| --- | --- | --- |\n'
    '| 1 | card1_attempt02.py | quantity 2.8→2, unit price 5, readonly total 10; writable cache replacement and entry mutation excluded from equality/hash; hidden locale; first/cached receipt; replacement quantity 3 and total 15; public inspection all exercised. |\n'
    '| 2 | card2_attempt01.py | Nullable None preservation and 4.8→4 conversion work at construction and assignment; explicit converter=None preserves float values despite class convert=True. |\n'
    '| 3 | card3_attempt01.py | Inherited order value/mode/extra, required keyword-only override, inherited public slot descriptor reuse, and zero-argument super all work. |\n'
    '| 4 | both card4_*_attempt02.py | Removing only the cache declaration leaves frozen=True/order=True unchanged. Both types independently retain identical equality, inequality, ordering and hash outcomes. |\n',
    'Initial author choices: use a frozen quote, const(init=False) for the dependent total, named InitVar/lazy providers for locale and receipt, and an ordinary mutable cache explicitly excluded from comparison/hash/repr. The cache explicitly disables inferred conversion because dict is not an inferred constructor type. Receipt is excluded from comparison/hash/repr to keep logical comparisons and presentation from incidentally causing its lazy evaluation; readonly comes from frozen=True. Replacement omits the defaulted locale intentionally to demonstrate the documented reinitialization provider behavior.\n',
    'The child overrides the base mode field from a defaulted keyword-only field to a required keyword-only field while retaining its ordinary writable storage shape. Card 4 enables order as well as frozen equality/hash and keeps those options unchanged. No handwritten model implementation substitutes for generated behavior.\n',
    'Three failed executions were preserved. Card 1 had an author expectation error about replacement: its ordinary init=True cache should be carried to the new constructor, not rebuilt. Both Card 4 first executions completed their requested model assertions and printed successful logical outcomes, then failed the author counter assertion because decoration happened outside its collection window. Repairs did not change class options or relax any requested behavior. See exact rationales and source versions below. No required clarification remained.\n',
    '## Backend evidence\n',
    'All product executions set ASTICHI_LOWER_ENGINE=native-rust on the exact isolated CPython 3.12 interpreter. The public probe reported 32 native-only batch requests out of 32 engine requests. Final cards reported respectively 270/270, 100/100, 105/105, 106/106 and 88/88 native-only/engine requests. Their runtime assertions require positive native-only counts, equality with all counted engine requests, and zero fallback-labelled counter values. No fallback was observed on these selected lowering requests. This does not claim wholly Rust program execution or a speed/memory advantage; ordinary Python runtime and other SDK work remain visible in the counters.\n',
    '## Preserved source manifests\n',
]
for name in ['first-attempt-manifest.json', 'repair-attempt-manifest.json', 'repairs.json', 'card4-declaration-removal.json', 'end-check.json']:
    parts.append('### ' + name + '\n\n```json\n' + (root / name).read_text() + '```\n')
parts.append('## Every authored card source\n')
for path in sorted(root.glob('card*_attempt*.py')):
    parts.append('### ' + path.name + '\n\n```python\n' + path.read_text() + '```\n')
parts.append('## Supporting scripts\n')
for name in ['run_record.py', 'read_public_docs.py', 'inspect_public_surface.py', 'backend_public_signatures.py', 'backend_probe.py', 'end_check.py']:
    parts.append('### ' + name + '\n\n```python\n' + (root / name).read_text() + '```\n')
parts.append('## Every captured execution\n')
executions = [json.loads(path.read_text()) for path in root.glob('*.execution.json')]
for execution in sorted(executions, key=lambda value: (value['started_utc'], value['label'])):
    label = execution['label']
    parts.append('### ' + label + '\n\n```json\n' + json.dumps(execution, indent=2) + '\n```\n')
    parts.append('Exact shell rendering of captured argument vector:\n\n```sh\n' + shlex.join(execution['command']) + '\n```\n')
    parts.append('stdout:\n\n```text\n' + (root / (label + '.stdout')).read_text() + '```\n')
    parts.append('stderr (empty block means empty stderr):\n\n```text\n' + (root / (label + '.stderr')).read_text() + '```\n')
parts.append('## Artifact inventory\n\n')
parts.append('\n'.join('- ' + str(path.relative_to(root)) for path in sorted(root.rglob('*')) if path.is_file()) + '\n')
parts.append('\nThe standalone record is AUTHORING_RECORD.md. All raw .execution.json/.stdout/.stderr files and exact first/repaired source files remain beside it. No product defect or implementation verdict is inferred from the author corrections.\n')
(root / 'AUTHORING_RECORD.md').write_text('\n'.join(parts))
print(json.dumps(metadata, indent=2))
print('record:', root / 'AUTHORING_RECORD.md')
print('record_bytes:', (root / 'AUTHORING_RECORD.md').stat().st_size)
