"""Write the sources the host tests (hosts.spec.ts) give to each host (into e2e/.fixtures/hosts/).

Each host shows the same three tables, from cells it runs itself: a `GTI` table, a `GT` table made
interactive with `opt_interactive()`, and a static `GT` table. The hosts are Jupyter (a notebook,
for nbconvert and JupyterLab, with a kernel spec of this Python's own), Quarto (a document),
Shiny (an app), marimo (an app), and VS Code (a page showing the tables' output as its notebooks
do, in a sandboxed frame). Run by e2e/global-setup.ts.
"""

from __future__ import annotations

import html
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / ".fixtures" / "hosts"

SETUP = 'from great_tables import GT, GTI, exibble\n\nsmall = exibble[["num", "char", "fctr"]]'

TABLES = [
    'GTI(small).tab_header("One").i_cols_filter(columns="fctr", type="facet")',
    'GT(small, id="two").tab_header("Two").opt_interactive(use_search=True, use_filters=True)',
    'GT(small.head(2)).tab_header("Three")',
]


def notebook() -> str:
    cells = [
        {
            "cell_type": "code",
            "execution_count": None,
            "id": f"cell-{i}",
            "metadata": {},
            "outputs": [],
            "source": source,
        }
        for i, source in enumerate([SETUP, *TABLES])
    ]
    kernel = {"display_name": "Python 3", "language": "python", "name": "python3"}
    return json.dumps(
        {
            "cells": cells,
            "metadata": {"kernelspec": kernel, "language_info": {"name": "python"}},
            "nbformat": 4,
            "nbformat_minor": 5,
        },
        indent=1,
    )


def kernel_spec() -> str:
    # (This Python's, whatever the user's own kernels are)
    argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
    return json.dumps({"argv": argv, "display_name": "Python 3", "language": "python"})


def quarto_doc() -> str:
    cells = "\n\n".join(f"```{{python}}\n{source}\n```" for source in [SETUP, *TABLES])
    return f"---\ntitle: Hosts\njupyter: python3\n---\n\n{cells}\n"


# (The first two re-rendered as the input changes: as `render_gt()` and as `ui.HTML()`)
SHINY_APP = f"""\
from shiny import App, render, ui

from great_tables.shiny import output_gt, render_gt

{SETUP}

app_ui = ui.page_fluid(
    ui.input_select("rows", "Rows", ["all", "head"]),
    output_gt("one"),
    ui.output_ui("two"),
    ui.HTML({TABLES[2]}.as_raw_html()),
)


def server(input, output, session):
    def rows():
        return small if input.rows() == "all" else small.head(4)

    @render_gt
    def one():
        return {TABLES[0].replace("small", "rows()", 1)}

    @render.ui
    def two():
        return ui.HTML({TABLES[1].replace("small", "rows()", 1)}.as_raw_html())


app = App(app_ui, server)
"""

# (The tables as cells' outputs, and the second also as `mo.Html()`)
MARIMO_APP = f"""\
import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    {SETUP.replace(chr(10), chr(10) + "    ")}
    return GT, GTI, mo, small


@app.cell
def _(GTI, small):
    {TABLES[0]}
    return


@app.cell
def _(GT, small):
    {TABLES[1]}
    return


@app.cell
def _(GT, small):
    {TABLES[2]}
    return


@app.cell
def _(GT, mo, small):
    mo.Html({TABLES[1].replace('id="two"', 'id="html"')}.as_raw_html())
    return


if __name__ == "__main__":
    app.run()
"""


def vscode_page() -> str:
    # The tables' output in VS Code (whose notebooks have their CSS marked `!important`), shown
    # as its notebooks show HTML output: set as an element's HTML, with each script then made
    # again (as one set as HTML doesn't run). They're shown again, as when the cells are run
    # again, by `show()`. The frame is sandboxed more strictly than VS Code's (it's not of the
    # same origin as anything, so its storage throws), and the first table keeps its view there.
    namespace: dict[str, object] = {}
    exec(SETUP, namespace)  # noqa: S102 (runs the fixture's own setup code)
    sources = [TABLES[0] + '.with_id("one").i_view_state(storage=True)', *TABLES[1:]]
    os.environ["VSCODE_PID"] = "1"
    try:
        outputs = [eval(source, namespace)._repr_html_() for source in sources]
    finally:
        del os.environ["VSCODE_PID"]
    outputs_json = json.dumps(outputs).replace("</", "<\\/")
    frame = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8"/>\n</head>\n<body>\n'
        '<div id="outputs"></div>\n<script>\n'
        f"const outputs = {outputs_json};\n"
        "function show() {\n"
        '  const root = document.getElementById("outputs");\n'
        "  root.replaceChildren();\n"
        "  for (const output of outputs) {\n"
        '    const el = document.createElement("div");\n'
        "    el.innerHTML = output;\n"
        "    root.append(el);\n"
        '    for (const old of el.querySelectorAll("script")) {\n'
        '      const script = document.createElement("script");\n'
        "      for (const { name, value } of old.attributes) {\n"
        "        script.setAttribute(name, value);\n"
        "      }\n"
        "      script.text = old.text;\n"
        "      old.replaceWith(script);\n"
        "    }\n"
        "  }\n"
        "}\n"
        "show();\n"
        "</script>\n</body>\n</html>\n"
    )
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8"/>\n</head>\n<body>\n'
        '<iframe sandbox="allow-scripts" style="width: 1000px; height: 1200px; border: 0" '
        f'srcdoc="{html.escape(frame)}"></iframe>\n</body>\n</html>\n'
    )


def main() -> None:
    (OUT / "jupyter" / "kernels" / "python3").mkdir(parents=True, exist_ok=True)
    files = {
        "notebook.ipynb": notebook(),
        "jupyter/kernels/python3/kernel.json": kernel_spec(),
        "doc.qmd": quarto_doc(),
        "shiny_app.py": SHINY_APP,
        "marimo_app.py": MARIMO_APP,
        "vscode.html": vscode_page(),
    }
    for name, text in files.items():
        (OUT / name).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
