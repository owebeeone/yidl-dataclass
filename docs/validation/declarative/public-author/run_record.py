import datetime
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).parent
label = sys.argv[1]
command = sys.argv[2:]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(command, cwd=root, capture_output=True, text=True)
ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
(root / (label + '.stdout')).write_text(result.stdout)
(root / (label + '.stderr')).write_text(result.stderr)
record = {'label': label, 'command': command, 'cwd': str(root), 'started_utc': started, 'ended_utc': ended, 'exit_code': result.returncode}
(root / (label + '.execution.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
print(result.stdout, end='')
print(result.stderr, end='', file=sys.stderr)
sys.exit(result.returncode)
