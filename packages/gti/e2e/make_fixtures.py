"""Write the HTML pages the Playwright tests load (into e2e/.fixtures/, which is gitignored).

The pages use real Great Tables output, so the browser tests always run against what GT emits.
Run by e2e/global-setup.ts; needs great_tables importable (e.g. `pip install -e .` at the repo
root).
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from great_tables import GT, GTI, exibble, loc, md, style
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


def display_html(table_id: str, groups_as_column: bool = False, **options) -> str:
    # The table to sort, on one page, with a filled cell in row 0 and a long value in row 2 (in a
    # narrow column, with the column widths set).
    data = exibble.assign(
        char=exibble["char"].replace("coconut", "a coconut, cracked open at noon")
    )
    gt = sort_gt(table_id, groups_as_column, data=data)
    gt = gt.tab_style(style.fill("lightblue"), loc.body(columns="currency", rows=[0]))
    gt = gt.cols_width({"char": "90px"})
    gt = gt.opt_interactive(use_pagination=False, **options)
    return render_gti_html(gt, runtime="none")


def resize_html(table_id: str, groups_as_column: bool = False) -> str:
    # The table to sort, searchable, 3 rows to a page, with a spanner and resize handles.
    gt = sort_gt(table_id, groups_as_column).tab_spanner(
        label="Numbers", columns=["num", "currency"]
    )
    gt = gt.opt_interactive(use_search=True, use_resizers=True, page_size_default=3)
    return render_gti_html(gt, runtime="none")


def select_html(
    table_id: str, mode: str = "multiple", groups_as_column: bool = False, **options
) -> str:
    # The table to sort, with a title and a source note, and rows to select.
    gt = (
        sort_gt(table_id, groups_as_column)
        .tab_header(title="exibble")
        .tab_source_note("Source: great_tables.exibble")
    )
    gt = gt.opt_interactive(selection_mode=mode, **options)
    return render_gti_html(gt, runtime="none")


def scroll_html(
    table_id: str, groups_as_column: bool = False, height: str = "300px", **options
) -> str:
    # exibble three times over (24 rows, in two groups), with a title, a spanner, group and
    # grand summary rows, a footnote and a source note, in a body that scrolls.
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    gt = (
        sort_gt(table_id, groups_as_column, data=data)
        .tab_header(title="exibble", subtitle="Three times over")
        .tab_spanner(label="Numbers", columns=["num", "currency"])
        .tab_footnote("A fruit.", locations=loc.body(columns="char", rows=[0]))
        .tab_source_note("Source: great_tables.exibble")
    )
    gt = gt.opt_interactive(height=height, **options)
    return render_gti_html(gt, runtime="none")


def wide_html(
    table_id: str, groups_as_column: bool = False, height: str = "auto", **options
) -> str:
    # exibble three times over (24 rows, in two groups) with every column, striped, with a title,
    # a spanner, group and grand summary rows, a footnote and a source note: wider than a phone.
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    gt = (
        GT(data, rowname_col="row", groupname_col="group", id=table_id)
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .row_group_order(["grp_b", "grp_a"])
        .opt_row_striping()
        .tab_options(row_group_as_column=groups_as_column)
        .summary_rows(fns={"Total": lambda df: df[["num", "currency"]].sum()})
        .grand_summary_rows(fns={"Max": lambda df: df[["num", "currency"]].max()})
        .tab_header(title="exibble", subtitle="Three times over")
        .tab_spanner(label="Numbers", columns=["num", "currency"])
        .tab_footnote("A fruit.", locations=loc.body(columns="char", rows=[0]))
        .tab_source_note("Source: great_tables.exibble")
    )
    gt = gt.opt_interactive(height=height, use_pagination=False, **options)
    return render_gti_html(gt, runtime="none")


def pad_html(table_id: str, **options) -> str:
    # exibble without its groups (8 rows), striped, selectable and searchable, 5 rows to a page
    # (or 10, which fits every row), so that the last page is short.
    gt = (
        GT(exibble.drop(columns="group"), rowname_col="row", id=table_id)
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .opt_row_striping()
        .tab_source_note("Source: great_tables.exibble")
    )
    gt = gt.opt_interactive(
        selection_mode="multiple",
        use_search=True,
        use_page_size_select=True,
        page_size_values=[5, 10],
        page_size_default=5,
        **options,
    )
    return render_gti_html(gt, runtime="none")


def bar_html(
    table_id: str, columns: list[str] | None = None, selection: str | None = None, **pagination
) -> str:
    # A GTI table (with GTI's control bar): exibble three times over (24 rows, in two groups),
    # 2 rows to a page (so 12 pages), or with only the columns given; or without pages. Rows can
    # be selected, with `selection`.
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    if columns is None:
        gti = GTI.from_gt(sort_gt(table_id, data=data))
    else:
        gti = GTI(data[columns], id=table_id)
    gti = gti.i_selection(selection)
    if pagination.get("enabled", True):
        gti = gti.i_pagination(**{"page_size": 2, **pagination})
    else:
        gti = gti.i_pagination(False)
    return render_gti_html(gti, runtime="none")


def filter_html(table_id: str, view: str | None = None, **pagination) -> str:
    # A GTI table of exibble three times over (24 rows, in two groups), 5 rows to a page, whose
    # rows can be selected: `num` filtered by a range, `char` by text, and `fctr` by a facet; with
    # the view's filter, as text, if given.
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    gti = (
        GTI(
            data[["num", "char", "fctr", "row", "group"]],
            rowname_col="row",
            groupname_col="group",
            id=table_id,
        )
        .i_selection("multiple")
        .i_pagination(page_size=5, **pagination)
        .i_cols_filter(columns="num")
        .i_cols_filter(columns="char", type="text")
        .i_cols_filter(columns="fctr", type="facet")
        .i_view(filter=view)
    )
    return render_gti_html(gti, runtime="none")


TOKENS_VIEW = 'num >= 1000 and char contains "a" and fctr in ("two", "seven", "one", "eight")'


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
        # Tables with highlighted rows (with group headings, or groups shown as a column); as they
        # are, compact, and without text wrapping.
        "display.html": page(display_html("d") + "\n" + runtime_src, head=styles),
        "display-highlight.html": page(
            display_html("d", use_highlight=True) + "\n" + runtime_src, head=styles
        ),
        "display-highlight-column.html": page(
            display_html("d", groups_as_column=True, use_highlight=True) + "\n" + runtime_src,
            head=styles,
        ),
        "display-compact.html": page(
            display_html("d", use_compact_mode=True) + "\n" + runtime_src, head=styles
        ),
        "display-nowrap.html": page(
            display_html("d", use_text_wrapping=False) + "\n" + runtime_src, head=styles
        ),
        # Tables with resizable columns: with a spanner (and groups shown as a column), and
        # without text wrapping, with column widths set by the author.
        "resize.html": page(resize_html("r") + "\n" + runtime_src, head=styles),
        "resize-column.html": page(
            resize_html("r", groups_as_column=True) + "\n" + runtime_src, head=styles
        ),
        "resize-nowrap.html": page(
            display_html("d", use_text_wrapping=False, use_resizers=True) + "\n" + runtime_src,
            head=styles,
        ),
        # Tables with rows to select: several, searchable, 3 rows to a page, highlighted; one at a
        # time, on one page; and several, with groups shown as a column and resizable columns.
        "select.html": page(
            select_html("x", use_search=True, page_size_default=3, use_highlight=True)
            + "\n"
            + runtime_src,
            head=styles,
        ),
        "select-single.html": page(
            select_html("x", mode="single", use_pagination=False) + "\n" + runtime_src,
            head=styles,
        ),
        "select-column.html": page(
            select_html("x", groups_as_column=True, use_pagination=False, use_resizers=True)
            + "\n"
            + runtime_src,
            head=styles,
        ),
        # Tables whose body scrolls: on one page, selectable, with a search box; with groups shown
        # as a column; 10 rows to a page, with resizable columns and no text wrapping.
        "scroll.html": page(
            scroll_html("v", use_pagination=False, use_search=True, selection_mode="multiple")
            + "\n"
            + runtime_src,
            head=styles,
        ),
        "scroll-column.html": page(
            scroll_html("v", groups_as_column=True, use_pagination=False) + "\n" + runtime_src,
            head=styles,
        ),
        "scroll-pages.html": page(
            scroll_html(
                "v",
                height="200px",
                page_size_default=10,
                use_resizers=True,
                use_text_wrapping=False,
            )
            + "\n"
            + runtime_src,
            head=styles,
        ),
        # The same tables (selectable, with groups shown as headings or as a column) as GT draws
        # them, and with a body that scrolls, taller than they are: their borders should match.
        **{
            f"scroll-borders{suffix}.html": page(
                "\n".join(
                    scroll_html(
                        table_id,
                        groups_as_column=bool(suffix),
                        height=height,
                        use_pagination=False,
                        selection_mode="multiple",
                    )
                    for table_id, height in [("b1", "auto"), ("b2", "5000px")]
                )
                + "\n"
                + runtime_src,
                head=styles,
            )
            for suffix in ["", "-column"]
        },
        # Tables wider than their container (360px): selectable, with a search box; with groups
        # shown as a column, in a body that scrolls; and in a page as narrow as a phone's.
        "wide.html": page(
            '<div style="width: 360px">'
            + wide_html("w", selection_mode="multiple", use_search=True)
            + "</div>\n"
            + runtime_src,
            head=styles,
        ),
        "wide-column.html": page(
            '<div style="width: 360px">'
            + wide_html("w", groups_as_column=True, height="300px", selection_mode="multiple")
            + "</div>\n"
            + runtime_src,
            head=styles,
        ),
        "wide-phone.html": page(
            wide_html("w") + "\n" + runtime_src,
            head='<meta name="viewport" content="width=device-width, initial-scale=1">\n' + styles,
        ),
        # The same tables (selectable, with groups shown as headings or as a column) as GT draws
        # them, in a container they fit in, and in one they don't: their borders should match.
        **{
            f"wide-borders{suffix}.html": page(
                "\n".join(
                    f'<div style="width: {width}">'
                    + wide_html(table_id, groups_as_column=bool(suffix), selection_mode="multiple")
                    + "</div>"
                    for table_id, width in [("b1", "min-content"), ("b2", "360px")]
                )
                + "\n"
                + runtime_src,
                head=styles,
            )
            for suffix in ["", "-column"]
        },
        # A table whose last page is short: as GT draws it, and wider than its container (300px).
        "pad.html": page(pad_html("pd") + "\n" + runtime_src, head=styles),
        "pad-wide.html": page(
            '<div style="width: 300px">' + pad_html("pd") + "</div>\n" + runtime_src,
            head=styles,
        ),
        # GTI tables, with the control bar: 12 pages and a search; as narrow as one column; in a
        # container 300px wide; on one page, which the bar sticks to the bottom of the view of;
        # and without the runtime (added by the test), with text after it.
        "bar.html": page(bar_html("c") + "\n" + runtime_src, head=styles),
        "bar-narrow.html": page(bar_html("c", columns=["char"]) + "\n" + runtime_src, head=styles),
        "bar-container.html": page(
            '<div style="width: 300px">' + bar_html("c") + "</div>\n" + runtime_src, head=styles
        ),
        "bar-sticky.html": page(
            bar_html("c", enabled=False) + '\n<div style="height: 1500px"></div>\n' + runtime_src,
            head=styles,
        ),
        "bar-late.html": page(bar_html("c") + '\n<p id="after">After the table</p>', head=styles),
        # The info panel: of a GTI table whose rows can be selected, with page sizes of 2 and 5
        # (below room for the panel above it); and of one in a container 300px wide
        "info.html": page(
            '<div style="height: 400px"></div>\n'
            + bar_html("c", selection="multiple", page_sizes=[5])
            + "\n"
            + runtime_src,
            head=styles,
        ),
        "info-container.html": page(
            '<div style="width: 300px">'
            + bar_html("c", selection="multiple")
            + "</div>\n"
            + runtime_src,
            head=styles,
        ),
        # Filters: on a GTI table 5 rows to a page; and on one in a container 300px wide
        "filters.html": page(filter_html("f") + "\n" + runtime_src, head=styles),
        "filters-container.html": page(
            '<div style="width: 300px">' + filter_html("f") + "</div>\n" + runtime_src,
            head=styles,
        ),
        # Filter tokens: of a view filtered by every column (3 rows); in a container 300px wide;
        # and without the runtime (added by the test), with text after it.
        "tokens.html": page(filter_html("f", view=TOKENS_VIEW) + "\n" + runtime_src, head=styles),
        "tokens-container.html": page(
            '<div style="width: 300px">'
            + filter_html("f", view=TOKENS_VIEW)
            + "</div>\n"
            + runtime_src,
            head=styles,
        ),
        "tokens-late.html": page(
            filter_html("f", view=TOKENS_VIEW) + '\n<p id="after">After the table</p>', head=styles
        ),
    }
    for name, html in fixtures.items():
        (OUT / name).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
