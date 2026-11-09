"""Write the HTML pages the Playwright tests load (into e2e/.fixtures/, which is gitignored).

The pages use real Great Tables output, so the browser tests always run against what GT emits.
Run by e2e/global-setup.ts; needs great_tables importable (e.g. `pip install -e .` at the repo
root).
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import polars as pl

from great_tables import GT, GTI, exibble, loc, md, style
from great_tables._gti import render_gti_html
from great_tables._gti._query import query_code, view_rows
from great_tables._gti._render import render_parts

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
    table_id: str, groups_as_column: bool = False, height: str = "340px", **options
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
    table_id: str,
    columns: list[str] | None = None,
    selection: str | None = None,
    height: str | None = None,
    **pagination,
) -> str:
    # A GTI table (with GTI's control bar): exibble three times over (24 rows, in two groups),
    # 2 rows to a page (so 12 pages), or with only the columns given; or without pages. Rows can
    # be selected, with `selection`; its body scrolls within `height`, if given, and its view is
    # kept in the URL.
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
    if height is not None:
        gti = gti.i_scroll(height).i_view_state()
    return render_gti_html(gti, runtime="none")


def filter_html(table_id: str, view: str | None = None, **pagination) -> str:
    # A GTI table of exibble three times over (24 rows, in two groups), 5 rows to a page, whose
    # rows can be selected: `num` filtered by a range, `char` by text, and `fctr` by a facet; with
    # the view's filter, as text, if given. It scrolls sideways in a narrow container (rather than
    # being stacked).
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
        .i_responsive("scroll")
    )
    return render_gti_html(gti, runtime="none")


def sheet_html(table_id: str) -> str:
    # The filters' table (24 rows, in two groups, 5 to a page; num filtered by a range, char by
    # text and fctr by a facet), with a search and columns readers can hide, as wide as its
    # container: on a touch screen, its bar folds into the "Filter & sort" sheet's button where
    # it's narrow
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    gti = (
        GTI(
            data[["num", "char", "fctr", "row", "group"]],
            rowname_col="row",
            groupname_col="group",
            id=table_id,
        )
        .i_pagination(page_size=5)
        .i_search()
        .i_cols_filter(columns="num")
        .i_cols_filter(columns="char", type="text")
        .i_cols_filter(columns="fctr", type="facet")
        .i_cols_controls(hideable=True)
        .i_responsive("scroll")
        .tab_options(table_width="100%")
    )
    return render_gti_html(gti, runtime="none")


def date_html(table_id: str) -> str:
    # A GTI table of exibble (8 rows, on one page) as Polars data, with `date` of dates (formatted)
    # and `datetime` of dates and times, each filtered by a date range (as "auto" has them); whose
    # view is kept in the URL
    data = pl.from_pandas(exibble[["row", "date", "datetime", "num"]]).with_columns(
        pl.col("date").str.to_date(), pl.col("datetime").str.to_datetime("%Y-%m-%d %H:%M")
    )
    gti = (
        GTI(data, rowname_col="row", id=table_id)
        .fmt_date(columns="date", date_style="day_m_year")
        .i_pagination(False)
        .i_cols_filter(columns=["date", "datetime"])
        .i_view_state(url=True)
    )
    return render_gti_html(gti, runtime="none")


def bool_html(table_id: str) -> str:
    # A GTI table of exibble (8 rows, on one page) with `big`, whether `num` is over 100 (shown as
    # "yes" or "no"; missing, as "unknown", where `num` is), filtered by a bool filter (as "auto"
    # has it); whose view is kept in the URL
    data = exibble[["row", "num"]].assign(
        big=pd.array([None if pd.isna(x) else x > 100 for x in exibble["num"]], dtype="boolean")
    )
    gti = (
        GTI(data, rowname_col="row", id=table_id)
        .fmt_tf(columns="big", tf_style="yes-no", na_val="unknown")
        .i_pagination(False)
        .i_cols_filter(columns="big")
        .i_view_state(url=True)
    )
    return render_gti_html(gti, runtime="none")


def state_html(table_id: str, url: bool = True, storage: bool = False) -> str:
    # A GTI table of exibble three times over (24 rows), 5 rows to a page, with a search: `num`
    # filtered by a range and `fctr` by a facet, first sorted by `num` (descending); whose view is
    # kept in the URL, or storage, or both (or neither), and can be undone
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    gti = (
        GTI(data[["num", "char", "fctr", "row"]], rowname_col="row", id=table_id)
        .i_pagination(page_size=5)
        .i_cols_filter(columns="num")
        .i_cols_filter(columns="fctr", type="facet")
        .i_view(sort="-num")
        .i_view_state(url=url, storage=storage)
    )
    return render_gti_html(gti, runtime="none")


def controls_html(table_id: str) -> str:
    # A GTI table of exibble (8 rows, on one page) that can't be sorted by `num` (filtered by a
    # range), whose search leaves out `char` (filtered by text), and that can't resize `currency`
    gti = (
        GTI(exibble[["num", "char", "fctr", "currency", "row"]], rowname_col="row", id=table_id)
        .i_pagination(False)
        .i_cols_filter(columns="num")
        .i_cols_filter(columns="char", type="text")
        .i_cols_controls(columns="num", sortable=False)
        .i_cols_controls(columns="char", searchable=False)
        .i_cols_controls(columns="currency", resizable=False)
    )
    return render_gti_html(gti, runtime="none")


def export_html(table_id: str) -> str:
    # A GTI table of exibble three times over (24 rows, in two groups), with a spanner, 5 rows to a
    # page, whose rows can be selected and exported in every format (as "exibble.csv", and so on)
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    gt = sort_gt(table_id, data=data).tab_spanner(label="Numbers", columns=["num", "currency"])
    gti = (
        GTI.from_gt(gt)
        .i_selection("multiple")
        .i_pagination(page_size=5)
        .i_export(["csv", "tsv", "json", "clipboard", "code"], filename="exibble")
    )
    return render_gti_html(gti, runtime="none")


def pin_html(table_id: str, groups_as_column: bool = False, height: str | None = None) -> str:
    # A GTI table of exibble three times over (24 rows, in two groups), on one page, selectable,
    # with every column: char moved to the start and pinned there, and fctr moved to the end and
    # pinned there, under a spanner across its edge (with currency); with group and grand summary
    # rows, a footnote and a source note. Wider than its container.
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    gti = (
        GTI(data, rowname_col="row", groupname_col="group", id=table_id)
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .cols_move_to_start("char")
        .cols_move_to_end("fctr")
        .row_group_order(["grp_b", "grp_a"])
        .opt_row_striping()
        .tab_options(row_group_as_column=groups_as_column)
        .summary_rows(fns={"Total": lambda df: df[["num", "currency"]].sum()})
        .grand_summary_rows(fns={"Max": lambda df: df[["num", "currency"]].max()})
        .tab_spanner(label="Ends", columns=["currency", "fctr"])
        .tab_footnote("A fruit.", locations=loc.body(columns="char", rows=[0]))
        .tab_source_note("Source: great_tables.exibble")
        .i_pagination(enabled=False)
        .i_selection("multiple")
        .i_scroll(height)
        .i_cols_pin("char")
        .i_cols_pin("fctr", side="right")
    )
    return render_gti_html(gti, runtime="none")


def hide_html(table_id: str) -> str:
    # The pinned columns' table (char pinned at the start, fctr at the end, under "Ends" with
    # currency), whose data columns readers can hide, first shown without datetime; with set
    # widths, a search, and CSV export, its view kept in the URL
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    columns = ["char", "num", "date", "time", "datetime", "currency", "fctr"]
    gti = (
        GTI(data, rowname_col="row", groupname_col="group", id=table_id)
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .cols_move_to_start("char")
        .cols_move_to_end("fctr")
        .cols_width({"row": "80px", "num": "140px", **{c: "100px" for c in columns if c != "num"}})
        .row_group_order(["grp_b", "grp_a"])
        .summary_rows(fns={"Total": lambda df: df[["num", "currency"]].sum()})
        .tab_spanner(label="Ends", columns=["currency", "fctr"])
        .i_pagination(enabled=False)
        .i_search()
        .i_export("csv", filename="hide")
        .i_cols_pin("char")
        .i_cols_pin("fctr", side="right")
        .i_cols_controls(columns=columns, hideable=True)
        .i_view(hidden="datetime")
        .i_view_state()
    )
    return render_gti_html(gti, runtime="none")


def reorder_html(table_id: str) -> str:
    # The hiding columns' table, but with currency and fctr both pinned at the end (under "Ends"),
    # its data columns readers can hide and move: char alone (pinned at the start), so it can't
    # move; num, date, time and datetime among themselves; and currency and fctr between them.
    # With set widths, a search, and CSV export, its view kept in the URL, and changes undone
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    columns = ["char", "num", "date", "time", "datetime", "currency", "fctr"]
    gti = (
        GTI(data, rowname_col="row", groupname_col="group", id=table_id)
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .cols_move_to_start("char")
        .cols_move_to_end(["currency", "fctr"])
        .cols_width({"row": "80px", "num": "140px", **{c: "100px" for c in columns if c != "num"}})
        .row_group_order(["grp_b", "grp_a"])
        .summary_rows(fns={"Total": lambda df: df[["num", "currency"]].sum()})
        .tab_spanner(label="Ends", columns=["currency", "fctr"])
        .i_pagination(enabled=False)
        .i_search()
        .i_export("csv", filename="reorder")
        .i_cols_pin("char")
        .i_cols_pin(["currency", "fctr"], side="right")
        .i_cols_controls(columns=columns, hideable=True, reorderable=True)
        .i_view_state(undo=True)
    )
    return render_gti_html(gti, runtime="none")


def stack_html(
    table_id: str, mode: str = "stack", columns: list[str] | None = None, dark: bool = False
) -> str:
    # exibble (8 rows, grp_b then grp_a, each with a summary row, then a grand summary row), with
    # a title, a spanner, a stub, a filter on fctr and selectable rows, 5 to a page: shown as
    # cards in a container narrower than 420px. Its columns can be hidden; with `dark=True`, it's
    # light text on a dark background.
    columns = columns or ["num", "char", "fctr", "currency"]
    gti = (
        GTI(
            exibble[[*columns, "row", "group"]],
            rowname_col="row",
            groupname_col="group",
            id=table_id,
        )
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .row_group_order(["grp_b", "grp_a"])
        .summary_rows(fns={"Total": lambda df: df[["num", "currency"]].sum()})
        .grand_summary_rows(fns={"Max": lambda df: df[["num", "currency"]].max()})
        .tab_header(title="exibble")
        .tab_spanner(label="Numbers", columns=["num", "currency"])
        .i_cols_filter("fctr")
        .i_cols_controls(hideable=True)
        .i_selection()
        .i_pagination(page_size=5, page_sizes=None)
        .i_responsive(mode)  # type: ignore[arg-type]
    )
    if dark:
        gti = gti.tab_options(
            table_background_color="#1e1e1e",
            table_font_color="#eeeeee",
            heading_background_color="#1e1e1e",
            column_labels_background_color="#1e1e1e",
            row_group_background_color="#2a2a2a",
        )
    return render_gti_html(gti, runtime="none")


def collapse_html(
    table_id: str,
    groups_as_column: bool = False,
    height: str | None = None,
    widths: bool = False,
    mode: str = "auto",
) -> str:
    # exibble (8 rows, grp_b then grp_a, each with a summary row), with a spanner over num and
    # currency, a stub, selectable rows, a search, CSV export and columns that can be hidden, 5 to
    # a page: dropping columns to fit a narrow container ("auto", as its columns have priorities).
    # num has priority 1 (never dropped), char 2 and currency 3; fctr and date have none (and go
    # first, from the last). Optionally with groups as a column, a body that scrolls, and widths.
    # In a monospace font, whose letters are as wide on any system, so what's dropped at a width
    # is the same in CI as locally.
    gti = (
        GTI(
            exibble[["num", "currency", "char", "fctr", "date", "row", "group"]],
            rowname_col="row",
            groupname_col="group",
            id=table_id,
        )
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .row_group_order(["grp_b", "grp_a"])
        .summary_rows(fns={"Total": lambda df: df[["num", "currency"]].sum()})
        .tab_spanner(label="Numbers", columns=["num", "currency"])
        .tab_options(row_group_as_column=groups_as_column)
        .opt_table_font(font="monospace", add=False)
        .i_search()
        .i_export("csv", filename="collapse")
        .i_cols_controls(hideable=True)
        .i_selection("multiple")
        .i_pagination(page_size=5, page_sizes=None)
        .i_scroll(height)
        .i_cols_priority("num")
        .i_cols_priority("char", priority=2)
        .i_cols_priority("currency", priority=3)
        .i_responsive(mode)  # type: ignore[arg-type]
    )
    if widths:
        gti = gti.cols_width(
            {"row": "80px", "num": "120px", **{c: "100px" for c in ["currency", "char", "fctr"]}}
        )
    return render_gti_html(gti, runtime="none")


def query_only_gti(table_id: str, filter: str | None = None, sort: str | None = None) -> GTI:
    # Exibble three times over (24 rows, in two groups), on one page, showing num and char; and
    # left out for querying, fctr (as a facet, of its text in capitals), date (as text, by the
    # text of its dates) and currency (as a range), each labelled. With a search, CSV and code
    # export, and the view kept in the URL
    data = pd.concat([exibble] * 3, ignore_index=True)
    data = data.assign(row=[f"row_{i + 1}" for i in range(len(data))])
    gti = (
        GTI(data, rowname_col="row", groupname_col="group", id=table_id)
        .fmt_number(columns="num", decimals=2)
        .fmt_currency(columns="currency")
        .fmt_date(columns="date", date_style="month_day_year")
        .fmt(columns="fctr", fns=lambda x: x.upper())
        .cols_label(fctr="Factor", date="Day", currency="Price")
        .cols_hide(["time", "datetime"])
        .i_pagination(enabled=False)
        .i_search()
        .i_export(["csv", "code"], filename="query-only")
        .i_cols_filter(columns="num")
        .i_cols_filter(columns="fctr", type="facet")
        .i_cols_filter(columns="date", type="text")
        .i_cols_filter(columns="currency", type="range")
        .i_cols_controls(columns=["fctr", "date", "currency"], display=False)
        .i_view_state()
    )
    return gti.i_view(filter=filter, sort=sort)


QUERY_ONLY_VIEWS = [
    ('date contains "may"', None),
    ('fctr in ("one", "five") and currency >= 10', "-currency"),
    (None, "-currency"),
]


def query_only_cases() -> list[dict]:
    # For each view, its filter and sort (as the spec has them), the rows it shows, and its code
    # for each library, as `view_rows()` and `query_code()` have them
    cases = []
    for filter, sort in QUERY_ONLY_VIEWS:
        gti = query_only_gti("q", filter, sort)
        view = render_parts(gti)[1]["view"]
        code = {lib: query_code(gti, lib) for lib in ("polars", "pandas", "narwhals")}
        cases.append(
            {"filter": view["filter"], "sort": view["sort"], "rows": view_rows(gti), "code": code}
        )
    return cases


def code_gti(table_id: str, data, filter: str | None = None, sort: list[str] | None = None) -> GTI:
    # A GTI table of exibble (8 rows, in two groups), with a search: `num` filtered by a range,
    # `char` by text, and `fctr` and `date` by facets; exported as code (and as CSV, and copied)
    gti = (
        GTI(data, rowname_col="row", groupname_col="group", id=table_id)
        .i_search()
        .i_cols_filter(columns="num")
        .i_cols_filter(columns="char", type="text")
        .i_cols_filter(columns=["fctr", "date"], type="facet")
        .i_export(["csv", "clipboard", "code"], filename="exibble")
    )
    return gti.i_view(filter=filter, sort=sort)


# exibble, as pandas data (`fctr` of categories) and as Polars data (`date` of dates)
CODE_DATA = {
    "pandas": exibble[["num", "char", "fctr", "date", "row", "group"]].astype({"fctr": "category"}),
    "polars": pl.from_pandas(exibble[["num", "char", "fctr", "date", "row", "group"]]).with_columns(
        pl.col("date").str.to_date()
    ),
}

# The views the code is of: a filter (as a query's text) and a sort
CODE_VIEWS = [
    (None, None),
    ("num >= 2 and num <= 50000", ["-num"]),
    ('char contains " Ap " and fctr in ("two", "one", null)', ["fctr", "-char"]),
    ('num <= 0.5 and fctr in ("seven")', None),
    (None, ["-num", "char"]),
]
CODE_DATES = ('date in ("2015-02-15", "2015-01-15")', ["date"])


def code_cases() -> dict[str, list[dict]]:
    # For each data, the view's filter and sort (as the spec has them, for the table's `filter`
    # and `sort` properties) and its code for each library, as `query_code()` writes it
    cases: dict[str, list[dict]] = {}
    for name, data in CODE_DATA.items():
        cases[name] = []
        for filter, sort in CODE_VIEWS + ([CODE_DATES] if name == "polars" else []):
            gti = code_gti("k", data, filter, sort)
            view = render_parts(gti)[1]["view"]
            cases[name].append(
                {
                    "filter": view["filter"],
                    "sort": view["sort"],
                    "code": {lib: query_code(gti, lib) for lib in ("polars", "pandas", "narwhals")},
                }
            )
    return cases


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
        # (With rows a whole number of pixels high, whatever the fonts: Firefox rounds separated
        # borders that fall between pixels unlike collapsed ones, drawing 2px lines 1px wide)
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
                head=styles
                + "<style>gt-table :is(th, td) { line-height: 20px !important; }</style>\n",
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
        # without the runtime (added by the test), with text after it; and on one page that
        # scrolls.
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
        # On one page, in a body that scrolls within 300px, its view kept in the URL
        "bar-scroll.html": page(
            bar_html("c", enabled=False, height="300px") + "\n" + runtime_src, head=styles
        ),
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
        # Date filters: of dates, and of dates and times
        "dates.html": page(date_html("dt") + "\n" + runtime_src, head=styles),
        # A bool filter, of a column with a missing value
        "bools.html": page(bool_html("bl") + "\n" + runtime_src, head=styles),
        # View state: two GTI tables on a page, one kept in the URL and storage, one in the URL
        "state.html": page(
            state_html("va", storage=True) + "\n" + state_html("vb") + "\n" + runtime_src,
            head=styles,
        ),
        # Undo: a GTI table whose view isn't kept, but whose changes to it can be undone
        "undo.html": page(state_html("u", url=False) + "\n" + runtime_src, head=styles),
        # Column controls: a GTI table with columns that can't be sorted, searched, or resized
        "controls.html": page(controls_html("cc") + "\n" + runtime_src, head=styles),
        # Pinned columns (at the start and the end), in a container 480px wide: with group
        # headings; with groups shown as a column, in a body that scrolls (in one 640px wide, with
        # room for that column); and right to left
        "pin.html": page(
            '<div style="width: 480px">' + pin_html("pn") + "</div>\n" + runtime_src,
            head=styles,
        ),
        "pin-column.html": page(
            '<div style="width: 640px">'
            + pin_html("pn", groups_as_column=True, height="300px")
            + "</div>\n"
            + runtime_src,
            head=styles,
        ),
        "pin-rtl.html": page(
            '<div dir="rtl" style="width: 480px">' + pin_html("pn") + "</div>\n" + runtime_src,
            head=styles,
        ),
        # Hiding columns: of the pinned columns' table, in a container 480px wide, and right to
        # left; and of a table without a stub, whose last column shown can't be hidden
        "hide.html": page(
            '<div style="width: 480px">' + hide_html("h") + "</div>\n" + runtime_src,
            head=styles,
        ),
        "hide-rtl.html": page(
            '<div dir="rtl" style="width: 480px">' + hide_html("h") + "</div>\n" + runtime_src,
            head=styles,
        ),
        "hide-nostub.html": page(
            render_gti_html(
                GTI(exibble[["num", "char"]], id="hn").i_cols_controls(hideable=True),
                runtime="none",
            )
            + "\n"
            + runtime_src,
            head=styles,
        ),
        # Reordering columns: of a table like the hiding columns' one, in a container 780px wide
        # (with room for its pinned columns), and right to left
        "reorder.html": page(
            '<div style="width: 780px">' + reorder_html("r") + "</div>\n" + runtime_src,
            head=styles,
        ),
        "reorder-rtl.html": page(
            '<div dir="rtl" style="width: 780px">' + reorder_html("r") + "</div>\n" + runtime_src,
            head=styles,
        ),
        # Export: from a GTI table 5 rows to a page, whose rows can be selected
        "export.html": page(export_html("e") + "\n" + runtime_src, head=styles),
        # Export as code: from GTI tables of pandas data and of Polars data, the latter with a
        # view (of the code cases' second)
        "code.html": page(
            render_gti_html(code_gti("k", CODE_DATA["pandas"]), runtime="none")
            + "\n"
            + runtime_src,
            head=styles,
        ),
        "code-polars.html": page(
            render_gti_html(code_gti("k", CODE_DATA["polars"], *CODE_VIEWS[1]), runtime="none")
            + "\n"
            + runtime_src,
            head=styles,
        ),
        # Columns only for querying: in a GTI table that shows two of exibble's columns
        "query-only.html": page(
            render_gti_html(query_only_gti("q"), runtime="none") + "\n" + runtime_src,
            head=styles,
        ),
        # Stacked tables (as cards): in a container 360px wide; in one 800px wide (not stacked);
        # in a page as narrow as a phone's; with light text on a dark background; and "auto"
        # ones, with 7 of exibble's columns (not stacked until enough of them are hidden) and
        # with 3 of them
        **{
            f"stack{suffix}.html": page(
                f'<div style="width: {width}">'
                + stack_html("k", dark=dark)
                + "</div>\n"
                + runtime_src,
                head=styles,
            )
            for suffix, width, dark in [
                ("", "360px", False),
                ("-wide", "800px", False),
                ("-dark", "360px", True),
            ]
        },
        # The "Filter & sort" sheet: in a container 360px wide, and in a page as narrow as a phone's
        "sheet.html": page(
            '<div style="width: 360px">' + sheet_html("fs") + "</div>\n" + runtime_src,
            head=styles,
        ),
        "sheet-phone.html": page(
            sheet_html("fs") + "\n" + runtime_src,
            head='<meta name="viewport" content="width=device-width, initial-scale=1">\n' + styles,
        ),
        "stack-phone.html": page(
            stack_html("k") + "\n" + runtime_src,
            head='<meta name="viewport" content="width=device-width, initial-scale=1">\n' + styles,
        ),
        "stack-auto.html": page(
            '<div style="width: 360px">'
            + stack_html(
                "k",
                mode="auto",
                columns=["num", "char", "fctr", "date", "time", "datetime", "currency"],
            )
            + "</div>\n"
            + runtime_src,
            head=styles,
        ),
        "stack-auto-few.html": page(
            '<div style="width: 360px">'
            + stack_html("k", mode="auto", columns=["num", "fctr", "currency"])
            + "</div>\n"
            + runtime_src,
            head=styles,
        ),
        # Tables that could be stacked, in containers as wide as what's in them (not stacked): an
        # "auto" one in a table's cell; one that's stacked in an inline block; and an "auto" one in
        # an inline block, hidden until it's shown
        **{
            f"stack-fit{suffix}.html": page(
                start
                + stack_html("k", mode=mode, columns=["num", "fctr", "currency"])
                + end
                + runtime_src,
                head=styles,
            )
            for suffix, mode, start, end in [
                ("", "auto", "<table><tr><td>", "</td></tr></table>\n"),
                ("-inline", "stack", '<div style="display: inline-block">', "</div>\n"),
                (
                    "-hidden",
                    "auto",
                    '<div hidden><div style="display: inline-block">',
                    "</div></div>\n",
                ),
            ]
        },
        # Tables that drop columns: in a container 360px wide; in one 1000px wide (none dropped);
        # right to left; with groups as a column, in a body that scrolls; with column widths; one
        # without a stub (of four of exibble's columns, char with priority 1); and one so narrow
        # that it scrolls with only the columns that can't be dropped
        **{
            f"collapse{suffix}.html": page(
                f'<div{attrs} style="width: {width}">'
                + collapse_html("c", **options)
                + "</div>\n"
                + runtime_src,
                head=styles,
            )
            for suffix, attrs, width, options in [
                ("", "", "360px", {}),
                ("-wide", "", "1000px", {}),
                ("-rtl", ' dir="rtl"', "360px", {}),
                ("-column", "", "420px", {"groups_as_column": True, "height": "300px"}),
                ("-widths", "", "360px", {"widths": True}),
                ("-narrow", "", "160px", {}),
            ]
        },
        "collapse-nostub.html": page(
            '<div style="width: 240px">'
            + render_gti_html(
                GTI(exibble[["char", "num", "fctr", "date"]], id="c")
                .opt_table_font(font="monospace", add=False)
                .i_cols_priority("char")
                .i_responsive("collapse"),
                runtime="none",
            )
            + "</div>\n"
            + runtime_src,
            head=styles,
        ),
    }
    for name, html in fixtures.items():
        (OUT / name).write_text(html, encoding="utf-8")
    (OUT / "code-cases.json").write_text(json.dumps(code_cases(), indent=1), encoding="utf-8")
    (OUT / "query-only-cases.json").write_text(
        json.dumps(query_only_cases(), indent=1), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
