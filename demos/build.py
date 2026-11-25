"""
Build the docs' live app demos: `python demos/build.py`

Each app in `demos/` is exported to run in the browser (on Pyodide), in `_demos/`, which the docs
publish as `demos/` (great-docs' `custom_pages`); the widget's notebook is run in JupyterLite. Run
it before `great-docs build`. (Solara's and Flask's apps need a server, so the docs show them only
as the images `demos/posters.mjs` makes.)

The apps install Great Tables from a wheel built from this checkout (in `_demos/wheels/`), so that
they run the code the docs describe, rather than the latest release.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / "demos"
OUT = ROOT / "_demos"

STLITE_VERSION = "1.12.3"
JUPYTERLITE_VERSION = "0.8.7"

# (JupyterLite's settings: the notebook's kernel is started without asking which, as there's one)
JUPYTERLITE_SETTINGS = {"@jupyterlab/notebook-extension:tracker": {"autoStartDefaultKernel": True}}
# (And its own page opens its files, rather than the JupyterLab app, which isn't built)
JUPYTERLITE_CONFIG = {"jupyter-config-data": {"appUrl": "./tree"}}

# (The widget's notebook, in JupyterLite's files; the docs link to `notebooks/?path=` it)
NOTEBOOK = Path("_notebooks", "cars.ipynb")

# (great-docs copies a page with this front matter as it is, rather than putting it in the site)
RAW_PAGE = "---\nlayout: raw\n---\n"

# (The docs' theme, which `<gt-demo>` gives an app's page as `?theme=dark`, as JavaScript)
THEME = 'new URLSearchParams(location.search).get("theme") === "dark" ? "dark" : "light"'

# (JupyterLite's theme is a setting, so the page sets its default, in the config it's started
# with: after `config-utils.js` writes it, and before its app's bundle, which reads it, is run)
JUPYTERLITE_THEME = """
        const themes = { dark: "JupyterLab Dark", light: "JupyterLab Light" };
        const config = document.getElementById("jupyter-config-data");
        const data = JSON.parse(config.textContent);
        const plugin = "@jupyterlab/apputils-extension:themes";
        data.settingsOverrides = {
          ...data.settingsOverrides,
          [plugin]: { ...data.settingsOverrides?.[plugin], theme: themes[THEME] },
        };
        config.textContent = JSON.stringify(data);""".replace("THEME", THEME)

STLITE_PAGE = """\
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@stlite/browser@{version}/build/stlite.css">
</head>
<body>
<div id="root"></div>
<script type="module">
import {{ mount }} from "https://cdn.jsdelivr.net/npm/@stlite/browser@{version}/build/stlite.js";

// (By its full URL, as stlite's worker would find a relative one from its own)
const wheel = new URL("../wheels/{wheel}", location.href).href;
mount(
  {{
    requirements: [wheel, "pandas"],
    entrypoint: "app.py",
    files: {{ "app.py": {source} }},
    streamlitConfig: {{ "theme.base": {theme} }},
  }},
  document.getElementById("root"),
);
</script>
</body>
</html>
"""


def main() -> None:
    shutil.rmtree(OUT, ignore_errors=True)
    wheel = build_wheel()
    build_streamlit(wheel)
    build_panel(wheel)
    build_marimo(wheel)
    build_widget(wheel)

    for page in OUT.rglob("*.html"):
        page.write_text(RAW_PAGE + page.read_text(encoding="utf-8"), encoding="utf-8")


def build_wheel() -> str:
    wheels = OUT / "wheels"
    run("uv", "build", "--wheel", "--out-dir", wheels, cwd=ROOT)
    for path in wheels.iterdir():
        if path.suffix != ".whl":
            path.unlink()
    (wheel,) = wheels.glob("great_tables-*.whl")
    return wheel.name


def build_streamlit(wheel: str) -> None:
    source = (DEMOS / "streamlit" / "app.py").read_text(encoding="utf-8")
    page = STLITE_PAGE.format(
        title="Great Tables in a Streamlit app",
        version=STLITE_VERSION,
        wheel=wheel,
        source=json.dumps(source).replace("</", "<\\/"),
        theme=THEME,
    )
    (OUT / "streamlit").mkdir()
    (OUT / "streamlit" / "index.html").write_text(page, encoding="utf-8")


def build_panel(wheel: str) -> None:
    out = OUT / "panel"
    # (Panel packs the wheel with the app, in `app.resources.zip`)
    run(
        sys.executable,
        "-m",
        "panel",
        "convert",
        DEMOS / "panel" / "app.py",
        "--to",
        "pyodide-worker",
        "--out",
        out,
        "--title",
        "Great Tables in a Panel app",
        "--requirements",
        OUT / "wheels" / wheel,
        "pandas",
    )
    (out / "app.html").rename(out / "index.html")


def build_marimo(wheel: str) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        # marimo bundles a wheel given by a path in the notebook's dependencies (beside it)
        shutil.copy(OUT / "wheels" / wheel, tmp)
        notebook = Path(tmp) / "cars.py"
        source = (DEMOS / "marimo" / "cars.py").read_text(encoding="utf-8")
        source, n = re.subn(
            r'"great-tables\[marimo\]"', f'"great-tables @ ./{wheel}", "anywidget"', source
        )
        assert n == 1, "The notebook's dependencies should list great-tables[marimo]"
        notebook.write_text(source, encoding="utf-8")
        run(
            sys.executable,
            "-m",
            "marimo",
            "export",
            "html-wasm",
            notebook,
            "--output",
            OUT / "marimo",
            "--mode",
            "run",
            "--force",
        )
    # (marimo writes instructions for AI assistants that edit the notebook, which isn't edited
    # here, and its static files have a test run's results)
    (OUT / "marimo" / "CLAUDE.md").unlink(missing_ok=True)
    shutil.rmtree(OUT / "marimo" / "test-results", ignore_errors=True)

    # (The page's theme, which is in the config it's mounted with, is the docs')
    page = OUT / "marimo" / "index.html"
    html, n = re.subn(
        r'"theme": "(?:light|dark|system)"', f'"theme": {THEME}', page.read_text(encoding="utf-8")
    )
    assert n == 1, "marimo's export should set its theme once"
    page.write_text(html, encoding="utf-8")


def build_widget(wheel: str) -> None:
    # (JupyterLite, run in an environment of its own, from which it takes the extensions the
    # widget needs: anywidget's, and the ipywidgets manager. The kernel's `%pip install` takes
    # Great Tables from the wheel, which is served with the notebook, before PyPI's.)
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "overrides.json").write_text(
            json.dumps(JUPYTERLITE_SETTINGS), encoding="utf-8"
        )
        (Path(tmp) / "jupyter-lite.json").write_text(
            json.dumps(JUPYTERLITE_CONFIG), encoding="utf-8"
        )
        # (In a folder whose name starts with `_`, which Quarto doesn't render, as it would a
        # notebook elsewhere in the site)
        contents = Path(tmp) / "contents" / NOTEBOOK.parent
        contents.mkdir(parents=True)
        shutil.copy(DEMOS / "widget" / "cars.ipynb", contents / NOTEBOOK.name)
        run(
            "uv",
            "tool",
            "run",
            "--from",
            f"jupyterlite-core=={JUPYTERLITE_VERSION}",
            "--with",
            f"jupyterlite-pyodide-kernel=={JUPYTERLITE_VERSION}",
            "--with",
            "jupyter-server",
            "--with",
            "anywidget",
            "--with",
            "jupyterlab-widgets",
            "jupyter-lite",
            "build",
            "--contents",
            Path(tmp) / "contents",
            "--piplite-wheels",
            OUT / "wheels" / wheel,
            "--apps",
            "notebooks",
            "--apps",
            "tree",
            "--no-sourcemaps",
            "--output-dir",
            OUT / "widget",
            cwd=Path(tmp),
        )
    # (Its settings as notebooks, which it reads with those in `jupyter-lite.json`, are empty, and
    # Quarto would render them)
    for settings in (OUT / "widget").rglob("jupyter-lite.ipynb"):
        settings.unlink()

    for app in ("notebooks", "tree"):
        page = OUT / "widget" / app / "index.html"
        html, n = re.subn(
            r"await import\(\s*'[^']*config-utils\.js[^']*'\s*\);",
            lambda found: found[0] + JUPYTERLITE_THEME,
            page.read_text(encoding="utf-8"),
        )
        assert n == 1, f"JupyterLite's {app} page should load its config once"
        page.write_text(html, encoding="utf-8")


def run(*args: str | Path, cwd: Path | None = None) -> None:
    subprocess.run([str(arg) for arg in args], cwd=cwd, check=True)


if __name__ == "__main__":
    main()
