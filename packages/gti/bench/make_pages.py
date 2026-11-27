"""Write the pages the benchmarks (bench/run.mjs) load (into bench/.pages/, which is gitignored).

Each page is one GTI table, as `write_raw_html()` would write it (the runtime inline), so a page
costs what a reader's would. The tables vary in the number of rows, in their cells (plain ones, in 5
or 10 columns, or heavy ones: nanoplots and images), and in whether their rows are split into pages
(of 10) or all on one. Every table can be searched, and filtered on a facet, a range and a date.

There are also pages like the docs' dataset previews (`great_tables.data`): a real dataset, with
the explorer preset, scrolled sideways (`i_responsive("scroll")`) and paged, below a heading and
some text. Each is written three times: on its own; with Bootstrap's CSS (shiny's copy, if shiny
is installed), which stands in for Quarto's, as a big table's styles cost more with Bootstrap's
rules; and also hidden until it's parsed and two frames have been drawn, as great-docs' pages are
(by `theme-init.js`, so the reader doesn't see the theme or the sidebar change).

`bench/.pages/pages.json` lists the pages, with their sizes. With `--quick`, fewer of them.
"""

from __future__ import annotations

import datetime as dt
import gzip
import importlib.resources
import json
import sys
import warnings
from pathlib import Path

import polars as pl

from great_tables import GTI, data
from great_tables._gti import render_gti_html
from great_tables._gti._render import GTISizeWarning, page_html

HERE = Path(__file__).parent
OUT = HERE / ".pages"

ROWS = [500, 1000, 2000, 3000, 5000, 10000, 20000]
# (A nanoplot alone is about 8 KB of HTML)
HEAVY_ROWS = [500, 1000, 2000, 3000]
QUICK_ROWS = [1000, 3000, 10000]
QUICK_HEAVY_ROWS = [1000, 3000]

WORDS = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"]

# A small image, for the heavy tables' image column (which GT embeds, as base64)
DOT = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16">'
    '<circle cx="8" cy="8" r="6" fill="#4a7ab5"/></svg>'
)


# The docs-like pages: a dataset (its first rows, if a number is given), and for each, the columns
# sorted (a number's, a text's) and the text searched for. `sp500-10000` is the preview in the docs
# today; the others are whole datasets
DOCS = [
    ("sp500", 10000, "close", "date", "2010"),
    ("sp500", None, "close", "date", "2010"),
    ("countrypops", None, "population", "country_name", "Ireland"),
    ("nuclides", None, "z", "nuclide", "Fe"),
    ("pizzaplace", None, "price", "name", "hawaiian"),
]
QUICK_DOCS = DOCS[:1]


def bootstrap_css() -> str | None:
    try:
        path = importlib.resources.files("shiny") / "www/shared/bootstrap/bootstrap.min.css"
    except ModuleNotFoundError:
        return None
    return path.read_text(encoding="utf-8") if path.is_file() else None


def frame(rows: int, kind: str) -> pl.DataFrame:
    # Made up but steady: the same table every time, with values in no order
    columns = {
        "name": [f"{WORDS[i % 8]} {WORDS[(i * 7 + 3) % 8]} {i}" for i in range(rows)],
        "group": [WORDS[(i * 3) % 5] for i in range(rows)],
        "value": [((i * 7919) % 10007) / 3.7 for i in range(rows)],
        "date": [dt.date(2020, 1, 1) + dt.timedelta(days=(i * 37) % 1500) for i in range(rows)],
        "count": [(i * 104729) % 1000 for i in range(rows)],
    }
    if kind == "plain10":
        for k in range(5):
            columns[f"x{k}"] = [((i * (k + 3) * 15485863) % 100003) / 10 for i in range(rows)]
    if kind == "heavy":
        columns["trend"] = [[(i * j * 31 + j * 7) % 97 for j in range(12)] for i in range(rows)]
        columns["mark"] = ["dot.svg"] * rows
    return pl.DataFrame(columns)


def table(rows: int, kind: str, paged: bool) -> GTI:
    gti = (
        GTI(frame(rows, kind), id="bench")
        .fmt_number(columns="value", decimals=2)
        .fmt_integer(columns="count")
        .fmt_date(columns="date", date_style="iso")
        .i_cols_filter(columns=["group", "value", "date"])
        .i_pagination(paged)
    )
    if kind == "plain10":
        gti = gti.fmt_number(columns=[f"x{k}" for k in range(5)], decimals=1)
    if kind == "heavy":
        gti = gti.fmt_nanoplot(columns="trend").fmt_image(columns="mark", path=OUT, height=16)
    return gti


# How great-docs hides a page until it's parsed (`html:not(.theme-loaded)` is in its theme's CSS too)
REVEAL = """\
<style>html:not(.theme-loaded){visibility:hidden}</style>
<script>
document.addEventListener("DOMContentLoaded", () =>
  requestAnimationFrame(() =>
    requestAnimationFrame(() => document.documentElement.classList.add("theme-loaded"))
  )
);
</script>
"""

# The docs pages' variants: their names' ends, their labels, and whether they have Bootstrap's CSS
# and are hidden until parsed
VARIANTS = [
    ("", "", False, False),
    ("-bootstrap", ", Bootstrap", True, False),
    ("-site", ", as on the site", True, True),
]


def docs_page(fragment: str, gti: GTI, title: str, css: bool, hidden: bool) -> str:
    # As a reference page has it: a heading and some text, then the table (in `<main>`, as
    # Bootstrap's containers are)
    body = (
        f'<main class="container">\n<h1>{title}</h1>\n'
        "<p>A dataset's preview, as the docs show it, in a table that can be sorted, searched and "
        "filtered.</p>\n"
        f"{fragment}</main>\n"
    )
    html = page_html(body, gti)
    head = (REVEAL if hidden else "") + (
        '<link rel="stylesheet" href="bootstrap.min.css"/>\n' if css else ""
    )
    return html.replace("</head>", f"{head}</head>", 1)


def spec_of(html: str) -> str:
    start = html.index(">", html.index('<script type="application/json" data-gti-spec')) + 1
    return html[start : html.index("</script>", start)]


def main() -> None:
    quick = "--quick" in sys.argv[1:]
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.html"):
        old.unlink()
    (OUT / "dot.svg").write_text(DOT)
    # (Many of the tables are past the sizes that are warned about, on purpose)
    warnings.simplefilter("ignore", GTISizeWarning)

    pages = []

    def add(name: str, html: str, gti: GTI, **fields) -> None:
        (OUT / name).write_text(html, encoding="utf-8")
        data = html.encode("utf-8")
        pages.append(
            {
                "name": name,
                **fields,
                "columns": len(gti._tbl_data.columns),
                "rows": len(gti._tbl_data),
                "bytes": len(data),
                "gzip": len(gzip.compress(data)),
                "spec": len(spec_of(html).encode("utf-8")),
            }
        )

    for kind, counts in [
        ("plain5", QUICK_ROWS if quick else ROWS),
        ("plain10", QUICK_ROWS if quick else ROWS),
        ("heavy", QUICK_HEAVY_ROWS if quick else HEAVY_ROWS),
    ]:
        for rows in counts:
            for paged in [True, False]:
                gti = table(rows, kind, paged)
                html = page_html(render_gti_html(gti), gti)
                name = f"{kind}-{rows}-{'paged' if paged else 'one-page'}.html"
                add(name, html, gti, kind=kind, paged=paged)

    css = bootstrap_css()
    if css is None:
        print("make_pages.py: no shiny, so no docs pages with Bootstrap's CSS", file=sys.stderr)
    else:
        (OUT / "bootstrap.min.css").write_text(css, encoding="utf-8")
    for dataset, head, number, text, search in QUICK_DOCS if quick else DOCS:
        df = getattr(data.pl, dataset)
        df = df if head is None else df.head(head)
        gti = GTI(df, id="bench", preset="explorer").i_responsive("scroll")
        fragment = render_gti_html(gti)
        title = f"{dataset}-{head}" if head is not None else dataset
        for end, label_end, bootstrap, hidden in VARIANTS[: 3 if css is not None else 1]:
            name = f"docs-{title}{end}.html"
            label = f"{title}{label_end}"
            html = docs_page(fragment, gti, f"data.{dataset}", bootstrap, hidden)
            # (What the actions on the page sort and search for: a docs page has no facet or range
            # filter that is the same on each)
            actions = {"number": number, "text": text, "search": search}
            add(name, html, gti, kind="docs", label=label, paged=True, actions=actions)
    (OUT / "pages.json").write_text(json.dumps(pages, indent=1) + "\n")


if __name__ == "__main__":
    main()
