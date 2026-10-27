"""Release checks run by Gearu against an isolated candidate checkout."""

from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PROJECT = tomllib.loads((ROOT / "pyproject.toml").read_text())
MINORS = tuple(PROJECT["tool"]["yidl"]["test-matrix"]["python"])
ENGINES = ("python", "native-rust")


def run(command, *, cwd=ROOT, engine=None):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("PYTHONPATH", None)
    if engine:
        env["ASTICHI_LOWER_ENGINE"] = engine
    print("Running:", " ".join(map(str, command)), flush=True)
    subprocess.run(command, cwd=cwd, env=env, check=True)


def uv_python(minor, package):
    return [
        "uv", "run", "--no-project", "--no-sources", "--python", minor,
        "--with", package, "python",
    ]


def source_checks(minor):
    python = uv_python(minor, str(ROOT) + "[dev]")
    for engine in ENGINES:
        run(python + ["-c", BACKEND_CHECK], engine=engine)
        run(python + ["-m", "pytest", "-q", "-p", "no:cacheprovider"], engine=engine)
        run(python + ["-m", "yidl_dataclass.regenerate_dataclass_base"], engine=engine)


BACKEND_CHECK = """
import os
from astichi.lower_engine import select_effective_lower_engine
state = select_effective_lower_engine().snapshot()
assert state['selected_engine'] == os.environ['ASTICHI_LOWER_ENGINE'], state
assert state['fallback_scope'] is None, state
print(state)
"""

INSTALLED_CHECK = BACKEND_CHECK + """
from importlib.metadata import version
from pathlib import Path
import runpy
import sys
import yidl_dataclass
package = Path(yidl_dataclass.__file__).resolve().parent
assert not package.is_relative_to(Path(sys.argv[2]).resolve()), package
assert version('yidl-dataclass') == sys.argv[1]
for example in ('first_use.py', 'runtime_freeze.py'):
    runpy.run_path(str(package / 'documentation' / 'examples' / example), run_name='__main__')
from yidl_dataclass.regenerate_dataclass_base import main
sys.argv = ['yidl-dataclass-regenerate-base']
assert main() == 0, 'installed regeneration differs from packaged base'
"""


def artifact_checks():
    expected = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"]
    with tempfile.TemporaryDirectory(prefix="dataclass-release-") as directory:
        temporary = Path(directory)
        output = temporary / "dist"
        run([sys.executable, "-m", "build", "--outdir", str(output)])
        artifacts = sorted(output.iterdir())
        assert len(artifacts) == 2, artifacts
        run([sys.executable, "-m", "twine", "check", "--strict", *map(str, artifacts)])
        for artifact in artifacts:
            for minor in MINORS:
                for engine in ENGINES:
                    run(
                        uv_python(minor, str(artifact))
                        + ["-c", INSTALLED_CHECK, expected, str(ROOT)],
                        cwd=temporary,
                        engine=engine,
                    )


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=len(MINORS)) as pool:
        list(pool.map(source_checks, MINORS))
    artifact_checks()
