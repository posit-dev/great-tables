"""Write the HTML pages the Playwright tests load (into e2e/.fixtures/, which is gitignored).

The pages use real Great Tables output, so the browser tests always run against what GT emits.
Run by e2e/global-setup.ts; needs great_tables importable (e.g. `pip install -e .` at the repo
root).
"""

from __future__ import annotations

from pathlib import Path

from great_tables import GT, exibble, loc, md
from great_tables._gti import render_gti_html

HERE = Path(__file__).parent
OUT = HERE / ".fixtures"
JS_DIR = HERE.parent.parent.parent / "great_tables" / "js"


def gt_html(table_id: str) -> str:
    # Groups shown out of data order, with group and grand summary rows, so that body rows and
    # data rows don't line up.
    gt = (
        GT(exibble, rowname_col="row", groupname_col="group", id=table_id)
        .tab_header(title="exibble", subtitle=md("A *small* table"))
        .tab_spanner(label="Numbers", columns=["num", "currency"])
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .row_group_order(["grp_b", "grp_a"])
        .summary_rows(fns={"Total": lambda df: df[["num", "currency"]].sum()}, side="top")
        .grand_summary_rows(fns={"Max": lambda df: df[["num", "currency"]].max()})
        .tab_source_note("Source: great_tables.exibble")
    )
    return render_gti_html(gt, runtime="none")


def sort_gt(
    table_id: str, groups_as_column: bool = False, summaries: bool = True, data=exibble
) -> GT:
    # Groups out of data order, each with a summary row, striped, with missing values to sort.
    gt = (
        GT(
            data[["num", "char", "currency", "row", "group"]],
            rowname_col="row",
            groupname_col="group",
            id=table_id,
        )
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .row_group_order(["grp_b", "grp_a"])
        .opt_row_striping()
        .tab_options(row_group_as_column=groups_as_column)
    )
    if summaries:
        gt = gt.summary_rows(fns={"Total": lambda df: df[["num", "currency"]].sum()})
        gt = gt.grand_summary_rows(fns={"Max": lambda df: df[["num", "currency"]].max()})
    return gt


def sort_html(table_id: str, groups_as_column: bool = False, summaries: bool = True) -> str:
    return render_gti_html(sort_gt(table_id, groups_as_column, summaries), runtime="none")


def search_html(table_id: str, groups_as_column: bool = False) -> str:
    # The table to sort, with a search box, an accented value and a footnote mark in a cell.
    data = exibble.assign(char=exibble["char"].replace("durian", "Crème brûlée"))
    gt = sort_gt(table_id, groups_as_column, data=data)
    gt = gt.tab_footnote("A fruit.", locations=loc.body(columns="char", rows=[0]))
    return render_gti_html(gt.opt_interactive(use_search=True), runtime="none")


def pages_html(
    table_id: str, groups_as_column: bool = False, widths: bool = False, **options
) -> str:
    # The table to sort, searchable, 3 rows to a page, so that groups run across pages.
    gt = sort_gt(table_id, groups_as_column)
    if widths:
        gt = gt.cols_width({"char": "180px"})
    gt = gt.opt_interactive(use_search=True, page_size_default=3, **options)
    return render_gti_html(gt, runtime="none")


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
        # Tables to sort, with group headings or with groups shown as a column.
        "sort.html": page(sort_html("s") + "\n" + runtime_src, head=styles),
        "sort-column.html": page(
            sort_html("s", groups_as_column=True) + "\n" + runtime_src, head=styles
        ),
        "sort-column-bare.html": page(
            sort_html("s", groups_as_column=True, summaries=False) + "\n" + runtime_src,
            head=styles,
        ),
        # Tables to search, likewise.
        "search.html": page(search_html("q") + "\n" + runtime_src, head=styles),
        "search-column.html": page(
            search_html("q", groups_as_column=True) + "\n" + runtime_src, head=styles
        ),
        # Tables to page: with a page size select; with groups shown as a column; with a page
        # input; with column widths set by the author.
        "pages.html": page(
            pages_html("p", use_page_size_select=True, page_size_values=[3, 5])
            + "\n"
            + runtime_src,
            head=styles,
        ),
        "pages-column.html": page(
            pages_html("p", groups_as_column=True) + "\n" + runtime_src, head=styles
        ),
        "pages-jump.html": page(
            pages_html("p", pagination_type="jump") + "\n" + runtime_src, head=styles
        ),
        "pages-widths.html": page(pages_html("p", widths=True) + "\n" + runtime_src, head=styles),
    }
    for name, html in fixtures.items():
        (OUT / name).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
