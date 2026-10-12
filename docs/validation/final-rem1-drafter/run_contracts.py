"""Run canonical behavior before golden refresh, exposing product failures directly."""
import runpy
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'tests'))
for name in sys.argv[1:]:
    runpy.run_path(str(ROOT/'tests/data/gold_src'/name))['render_case']()
    print(name+': PASS')
