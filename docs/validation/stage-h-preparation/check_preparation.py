"""Read-only frozen preparation/evidence audit; never samples benchmark cases."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = Path(__file__).parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def main():
    definition = json.loads((EVIDENCE / 'definition.json').read_text())
    source = {p.name: digest(p) for p in sorted((ROOT / 'tests/data/perf').glob('*.py'))}
    assert source == definition['source_sha256']
    spec = importlib.util.spec_from_file_location('audit_validation', ROOT / 'tests/data/perf/validation.py')
    validation = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validation)
    inventory = validation.validate_definition(definition)
    for minor in ('312', '313', '314'):
        local = json.loads((EVIDENCE / f'definition-final-{minor}.json').read_text())
        setup = json.loads((EVIDENCE / f'setup-final-{minor}.json').read_text())
        label = '3.' + minor[-2:]
        assert local['source_sha256'] == source
        assert setup['provenance']['source_sha256'] == source
        assert local['provenance'] == setup['provenance'] == definition['minor_provenance'][label]
        assert len(setup['checked']) == 84
        cold = [json.loads(line) for line in (EVIDENCE / f'h20-cold-setup-{minor}-verification.log').read_text().splitlines() if line.startswith('{')]
        assert len(cold) == 6 and all(row['selected_backend'] == 'native-rust' for row in cold)
        xml = ET.parse(EVIDENCE / f'h19-mechanics-{minor}-verification.junit.xml').getroot()
        assert sum(int(suite.get('tests', 0)) for suite in xml.iter('testsuite')) == 49
        assert sum(int(suite.get('failures', 0)) + int(suite.get('errors', 0)) for suite in xml.iter('testsuite')) == 0
    raw_root = Path(tempfile.gettempdir()) / 'yidl-dataclass-stage-h-preparation-raw'
    corrections = {row['path']: row for row in json.loads((EVIDENCE / 'sanitization-corrections.json').read_text())}
    rows = [json.loads(line) for line in (EVIDENCE / 'increments.jsonl').read_text().splitlines()]
    refs = 0
    for row in rows:
        if row['phase'] == 'green':
            assert row['exit_code'] == 0
        if row['phase'] == 'red':
            assert row['exit_code'] != 0
        for artifact in row['artifacts']:
            path = ROOT / artifact['path']
            current = corrections.get(artifact['path'], {})
            expected = current.get('sha256', artifact['sha256'])
            if current:
                assert artifact['sha256'] in (current['sha256'], current['prior_sanitized_sha256'])
                assert digest(raw_root / (current['prior_sanitized_archive_sha256'] + '.raw')) == current['prior_sanitized_sha256']
            assert digest(path) == expected
            assert digest(raw_root / (artifact['raw_sha256'] + '.raw')) == artifact['raw_sha256']
            refs += 1
    xmls = list(EVIDENCE.glob('*.xml'))
    for path in xmls:
        ET.parse(path)
        assert all(suite.get('hostname') in (None, '[host]') for suite in ET.parse(path).getroot().iter('testsuite'))
    for path in [*(ROOT / 'tests/data/perf').glob('*.py'), *(ROOT / 'tests/data/perf').glob('*.md'), *EVIDENCE.rglob('*')]:
        if path.is_file():
            # Source expression is assembled to avoid storing prohibited prefixes.
            prefixes = tuple('/' + part + '/' for part in ('Users', 'Volumes', 'private', 'var', 'dev'))
            assert not any(prefix in path.read_text() for prefix in prefixes), path.relative_to(ROOT)
    tuple_ = definition['artifact_tuple']
    product_files = 0
    for row in tuple_['consumers'].values():
        for relative, sha in row['package_hashes'].items():
            if relative.startswith('yidl_dataclass/'):
                source_path = ROOT / 'src' / relative
                if not source_path.exists():
                    source_path = ROOT / relative.removeprefix('yidl_dataclass/documentation/')
                assert digest(source_path) == sha
                product_files += 1
    assert product_files > 0
    result = {'scope': 'H preparation only; no timed benchmark samples', 'definition_sha256': canonical(definition), 'definition_file_sha256': digest(EVIDENCE / 'definition.json'), 'source_files': len(source), **inventory, 'increments': len(rows), 'artifact_references': refs, 'junit_files': len(xmls), 'sanitization_corrections': len(corrections), 'untimed_setup_checks_per_minor': 84, 'cold_setup_checks': 18, 'mechanics_per_minor': 49, 'unchanged_dataclass_package_files': product_files, 'raw_archive': 'external:yidl-dataclass-stage-h-preparation-raw', 'success': True}
    (EVIDENCE / 'qa.json').write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
