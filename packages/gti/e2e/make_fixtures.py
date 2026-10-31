"""Write the HTML pages the Playwright tests load (into e2e/.fixtures/, which is gitignored).

The pages use real Great Tables output, so the browser tests always run against what GT emits.
Run by e2e/global-setup.ts; needs great_tables importable (e.g. `pip install -e .` at the repo
root).
"""

from __future__ import annotations

from pathlib import Path

from great_tables import GT, exibble, md

HERE = Path(__file__).parent
OUT = HERE / ".fixtures"
JS_DIR = HERE.parent.parent.parent / "great_tables" / "js"


def gt_html(table_id: str) -> str:
    gt = (
        GT(exibble, rowname_col="row", groupname_col="group", id=table_id)
        .tab_header(title="exibble", subtitle=md("A *small* table"))
        .tab_spanner(label="Numbers", columns=["num", "currency"])
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .tab_source_note("Source: great_tables.exibble")
    )
    return f"<gt-table>{gt.as_raw_html()}</gt-table>"


def page(body: str, head: str = "") -> str:
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        f"<title>GTI fixture</title>\n{head}</head>\n<body>\n{body}\n</body>\n</html>\n"
    )


def main() -> None:
    OUT.mkdir(exist_ok=True)
    runtime_src = '<script src="../../../../great_tables/js/gti.js"></script>\n'
    styles = '<link rel="stylesheet" href="../../../../great_tables/js/gti.css">\n'
    inline_runtime = f"<script>{(JS_DIR / 'gti.js').read_text()}</script>"

    fixtures = {
        # The usual case: the runtime follows the table it hydrates.
        "after.html": page(gt_html("t1") + "\n" + runtime_src, head=styles),
        # The runtime loads first, so tables are hydrated once the document is parsed.
        "head.html": page(gt_html("t1"), head=styles + runtime_src),
        # Two outputs that each inline the runtime (as notebooks do); the second must be a no-op.
        "twice.html": page(
            "\n".join([gt_html("t1"), inline_runtime, gt_html("t2"), inline_runtime]),
            head=styles,
        ),
    }
    for name, html in fixtures.items():
        (OUT / name).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
