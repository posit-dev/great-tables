"""Write the pages the benchmarks (bench/run.mjs) load (into bench/.pages/, which is gitignored).

Each page is one GTI table, as `write_raw_html()` would write it (the runtime inline), so a page
costs what a reader's would. The tables vary in the number of rows, in their cells (plain ones, in 5
or 10 columns, or heavy ones: nanoplots and images), and in whether their rows are split into pages
(of 10) or all on one. Every table can be searched, and filtered on a facet, a range and a date.
`bench/.pages/pages.json` lists the pages, with their sizes. With `--quick`, fewer of them.
"""

from __future__ import annotations

import datetime as dt
import gzip
import json
import sys
from pathlib import Path

import polars as pl

from great_tables import GTI
from great_tables._gti import render_gti_html
from great_tables._gti._render import page_html

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


def spec_of(html: str) -> str:
    start = html.index(">", html.index('<script type="application/json" data-gti-spec')) + 1
    return html[start : html.index("</script>", start)]


def main() -> None:
    quick = "--quick" in sys.argv[1:]
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.html"):
        old.unlink()
    (OUT / "dot.svg").write_text(DOT)

    pages = []
    for kind, counts in [
        ("plain5", QUICK_ROWS if quick else ROWS),
        ("plain10", QUICK_ROWS if quick else ROWS),
        ("heavy", QUICK_HEAVY_ROWS if quick else HEAVY_ROWS),
    ]:
        for rows in counts:
            for paged in [True, False]:
                gti = table(rows, kind, paged)
                html = page_html(render_gti_html(gti))
                name = f"{kind}-{rows}-{'paged' if paged else 'one-page'}.html"
                (OUT / name).write_text(html, encoding="utf-8")
                data = html.encode("utf-8")
                pages.append(
                    {
                        "name": name,
                        "kind": kind,
                        "columns": len(gti._tbl_data.columns),
                        "rows": rows,
                        "paged": paged,
                        "bytes": len(data),
                        "gzip": len(gzip.compress(data)),
                        "spec": len(spec_of(html).encode("utf-8")),
                    }
                )
    (OUT / "pages.json").write_text(json.dumps(pages, indent=1) + "\n")


if __name__ == "__main__":
    main()
