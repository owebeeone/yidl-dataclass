"""Audit stopped consumer tuple, real attempts, effective sanitation and matrices."""
import hashlib
import json
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[3]
EVIDENCE=Path(__file__).parent
RAW=Path(tempfile.gettempdir())/'yidl-dataclass-final-rem1-drafter-raw'
EXTERNAL=Path((Path(tempfile.gettempdir())/'yidl-dataclass-final-rem1-pointer.txt').read_text())


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    records=[json.loads(line) for line in (EVIDENCE/'increments.jsonl').read_text().splitlines()]
    corrections=[json.loads(line) for line in (EVIDENCE/'sanitation-corrections.jsonl').read_text().splitlines()]
    corrected={}
    for correction in corrections:corrected.setdefault(correction['path'],[]).append(correction)
    reference_count=0;raw_hashes=set();junit_paths=set()
    for row in records:
        assert row['phase']!='green' or row['exit_code']==0
        for artifact in row['artifacts']:
            reference_count+=1
            raw=RAW/(artifact['raw_sha256']+'.raw')
            assert digest(raw)==artifact['raw_sha256']
            raw_hashes.add(artifact['raw_sha256'])
            expected=artifact['sha256']
            if artifact['path'] in corrected:
                for correction in corrected[artifact['path']]:
                    assert correction['prior_sanitized_sha256']==expected
                    assert correction['original_raw_sha256']==artifact['raw_sha256']
                    assert digest(RAW/(expected+'.sanitized-before-correction'))==expected
                    expected=correction['sha256']
            path=ROOT/artifact['path']
            assert digest(path)==expected,(artifact['path'],'evidence hash')
            if path.name.endswith('.junit.xml'):
                ET.parse(path);junit_paths.add(artifact['path'])
    red={row['increment']:row for row in records if row['phase']=='red'}
    for name in ('rem1-data-names','rem1-data-protocol','rem1-inherited-slots','rem1-undoable-captures'):
        assert red[name]['exit_code']==1
    index={(row['increment'],row['phase']):row for row in records}
    matrix=[]
    for minor in ('312','313','314'):
        for backend in ('native-rust','python'):
            for member in ('dataclass','undoable'):
                source=f'rem1-source-{member}-{minor}-{backend}'
                if member=='dataclass' and backend=='python':source+='-restored'
                installed=f'rem1-installed-{member}-{minor}-{backend}-'+('v2' if member=='dataclass' else 'v3')
                for label in (source,installed):assert index[label,'verification']['exit_code']==0,label
                xml=EVIDENCE/(installed+'-verification.junit.xml')
                suites=ET.parse(xml).getroot().findall('testsuite')
                counts={key:sum(int(suite.get(key,'0')) for suite in suites) for key in ('tests','failures','errors','skipped')}
                assert counts['failures']==counts['errors']==0
                assert counts['tests']==(205 if member=='dataclass' else 349)
                matrix.append({'member':member,'minor':minor,'backend':backend,'path':xml.relative_to(ROOT).as_posix(),'counts':counts})
            absent=f'rem1-installed-undoable-{minor}-{backend}-v3-without-authority'
            assert index[absent,'verification']['exit_code']==0
            xml=EVIDENCE/(absent+'-verification.junit.xml')
            suites=ET.parse(xml).getroot().findall('testsuite')
            assert sum(int(s.get('tests','0')) for s in suites)==342
            assert sum(int(s.get('errors','0'))+int(s.get('failures','0')) for s in suites)==0
            for mode in ('smoke','provenance'):assert index[f'rem1-{mode}-{minor}-{backend}','verification']['exit_code']==0
    artifact_rows={}
    for member in ('dataclass','undoable'):
        rows=json.loads((EVIDENCE/(member+'-artifacts.json')).read_text())
        for row in rows:assert digest(EXTERNAL/(member+'-final')/row['file'])==row['sha256']
        artifact_rows[member]=rows
    definition=ROOT/'docs/validation/stage-h2-preparation/definition.json'
    assert digest(definition)=='279995dee0f0a5088030714a4e9935bf51d139d1f92fad20a2b8af566fa3c29b'
    frozen=json.loads(definition.read_text())['source_sha256']
    for name,value in frozen.items():assert digest(ROOT/'tests/data/perf'/name)==value
    changes=json.loads((EVIDENCE/'changed-distribution-paths.json').read_text())
    members={'dataclass':ROOT,'undoable':ROOT.parent/'yidl_undoable'}
    for member,paths in changes.items():
        for name in paths:
            text=(members[member]/name).read_text()
            assert not re.search(r'/(?:Users|Volumes|opt/homebrew|private/var|var/folders)/',text),name
    for path in EVIDENCE.iterdir():
        if path.is_file():assert not re.search(r'/(?:Users|Volumes|opt/homebrew|private/var|var/folders)/',path.read_text()),path.name
    report={'increments':len(records),'artifact_references':reference_count,'distinct_raw_hashes':len(raw_hashes),'junit_files':len(junit_paths),'explicit_sanitation_corrections':len(corrections),'final_installed_matrix':matrix,'all_six_no_authority_pass':True,'all_six_regeneration_public_smokes_pass':True,'frozen_h2_source_hashes':len(frozen),'frozen_h2_definition_sha256':digest(definition),'consumer_artifacts':artifact_rows,'owned_distribution_paths':{member:len(paths) for member,paths in changes.items()},'result':'PASS','limits':'Historical H2 measurements retain their old artifact tuple; no timings performed and no numerical parity claim.'}
    (EVIDENCE/'qa.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    changes['dataclass']+=sorted(path.relative_to(ROOT).as_posix() for path in EVIDENCE.iterdir() if path.is_file() and path.name!='owned-manifest.json')
    manifest={'scope':'Final remediation round1 sole-drafter changed consumer/public/test paths and evidence only; owner and paused files excluded.','files':{member:[{'path':name,'bytes':(members[member]/name).stat().st_size,'sha256':digest(members[member]/name)} for name in sorted(set(paths))] for member,paths in changes.items()},'consumer_artifacts':artifact_rows,'raw_archive':'external:yidl-dataclass-final-rem1-drafter-raw','h2_definition_sha256':digest(definition)}
    (EVIDENCE/'owned-manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'result':report['result'],'increments':len(records),'junit_files':len(junit_paths),'artifact_references':reference_count,'distinct_raw_hashes':len(raw_hashes),'owned_manifest_sha256':digest(EVIDENCE/'owned-manifest.json'),'qa_sha256':digest(EVIDENCE/'qa.json')},sort_keys=True))


if __name__=='__main__':main()
