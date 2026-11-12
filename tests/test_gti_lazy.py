"""Tables of Polars LazyFrames (`GTI(lf)`): made again from the rows shown, and in kernel mode,
their views found with Polars queries (great_tables/_gti/_lazy.py).

A lazy table's views are found from its rows' values (as text, for its search), where an eager
table's are found from its cells' text, as the runtime reads them: so the two are compared with
data whose cells show their values as they are.
"""

from __future__ import annotations

import datetime as dt
import re
import warnings

import polars as pl
import pytest

from great_tables import GTI, loc, style
from great_tables._gti._kernel import KernelEngine, render_table
from great_tables._gti._lazy import LazyEngine, collected, lazy_of
from great_tables._gti._query import query_code, view_rows
from great_tables._gti._render import GTIEngineWarning, GTISizeWarning
from great_tables._gti._state import check_query_value

DATA = {
    "char": ["apricot", "Banana", "coconut", "durian", "fig", "grape", "kiwi", "Éclair"],
    "num": [3.0, 1.0, None, 5.0, 1.0, float("nan"), 2.0, -1.5],
    "int": [3, 1, None, 5, 1, 7, 2, 0],
    "fctr": ["one", "two", "one", None, "two", "three", "one", "two"],
    "flag": [True, False, None, True, True, False, True, False],
    "day": [dt.date(2020, 1, i) for i in (3, 1, 2, 5, 4, 8, 7, 6)],
    "cat": pl.Series(["x", "y", "x", "z", None, "y", "x", "z"], dtype=pl.Categorical),
}

FRAME = pl.DataFrame(DATA, strict=False)

QUERY = {"search": "", "hidden": [], "filter": None, "links": [], "sort": []}


def make_gti(data) -> GTI:
    return (
        GTI(data, id="t")
        .i_cols_filter("fctr", type="facet")
        .i_cols_filter("num")
        .i_cols_filter("int")
        .i_cols_filter("char", type="text")
        .i_cols_filter("flag")
        .i_cols_filter("day")
        .i_cols_filter("cat", type="facet")
    )


def engines(eager: GTI, lazy: GTI) -> tuple[KernelEngine, LazyEngine]:
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        return KernelEngine(eager), LazyEngine(lazy)


@pytest.fixture(scope="module")
def both() -> tuple[KernelEngine, LazyEngine]:
    return engines(make_gti(FRAME), make_gti(FRAME.lazy()))


def page_query(**parts) -> dict:
    return {**QUERY, "start": 0, "size": 3, **parts}


# A lazy table finds the rows an eager one does ----


@pytest.mark.parametrize(
    "filter",
    [
        None,
        'fctr in ("one", "two")',
        "num > 1",
        "num is null or fctr is null",
        'char contains "an"',
        'char contains "ecl"',
        "char matches /^[a-d]/",
        "int >= 2",
        "flag in (true)",
        'day > "2020-01-04"',
        'cat in ("x")',
        "num top 3",
        "int bottom 2",
        "not (num > 1)",
    ],
)
@pytest.mark.parametrize(
    "sort",
    [
        [],
        ["num"],
        ["-num"],
        ["fctr", "-int"],
        ["char"],
        ["-cat"],
        ["flag"],
        ["-day"],
    ],
)
def test_rows_are_the_eager_tables(both, filter, sort):
    eager, lazy = both
    keys = [{"column": key.lstrip("-"), "descending": key.startswith("-")} for key in sort]
    query = {**QUERY, "filter": check_query_value(eager.spec, filter, "q"), "sort": keys}
    assert lazy.find(query) == eager.find(query)
    assert lazy.rows(query) == eager.rows(query)


@pytest.mark.parametrize("search", ["an", "AN", "1", "2020", "true", "x", "ecl", "-1.5", "an two"])
def test_search_finds_the_eager_tables_rows(both, search):
    eager, lazy = both
    query = {**QUERY, "search": search}
    assert lazy.rows(query) == eager.rows(query)


def test_search_matches_values_not_cells_text():
    gti = GTI(FRAME.lazy()).fmt_number("num", decimals=2).sub_missing(missing_text="gone")
    engine = LazyEngine(gti)
    # (The value, as text, not the cell's)
    assert engine.rows({**QUERY, "search": "5.0"}) == [3]
    assert engine.rows({**QUERY, "search": "5.00"}) == []
    # (A missing value has no text)
    assert engine.rows({**QUERY, "search": "gone"}) == []
    assert engine.rows({**QUERY, "search": "none"}) == []
    # (Nor hidden columns)
    assert engine.rows({**QUERY, "search": "three", "hidden": ["fctr"]}) == []


def test_search_folds_as_the_runtime_does():
    data = pl.DataFrame({"w": ["ΟΔΟΣ", "οδος", "Crème"]})
    eager, lazy = engines(GTI(data), GTI(data.lazy()))
    for search in ["ΟΔΟΣ", "οδοσ", "οδος", "creme", "CRÈME"]:
        query = {**QUERY, "search": search}
        assert lazy.rows(query) == eager.rows(query)
    assert lazy.rows({**QUERY, "search": "ΟΔΟΣ"}) == [0]


def test_search_reads_durations_and_skips_nested_values():
    data = pl.DataFrame({"d": [dt.timedelta(hours=1), None], "l": [[1, 2], [3]]})
    engine = LazyEngine(GTI(data.lazy()))
    assert engine.rows({**QUERY, "search": "1h"}) == [0]
    assert engine.rows({**QUERY, "search": "3"}) == []


@pytest.mark.parametrize("column", ["fctr", "flag", "cat"])
def test_facet_counts_are_the_eager_tables(both, column):
    eager, lazy = both
    query = {**QUERY, "filter": check_query_value(eager.spec, "int > 0", "q")}
    assert sorted(lazy.facet(query, column)) == sorted(eager.facet(query, column))
    with pytest.raises(ValueError, match="no filter"):
        lazy.facet(QUERY, "char2")


def test_filters_have_their_values(both):
    eager, lazy = both
    filters = {f["column"]: f for f in lazy.spec["filters"]}
    for f in eager.spec["filters"]:
        if f["type"] in ("facet", "bool"):
            assert filters[f["column"]] == f
    # (A range's or a date's, its first and last)
    assert filters["num"]["values"] == [-1.5, 5.0]
    assert filters["day"]["values"] == ["2020-01-01", "2020-01-08"]
    assert filters["num"]["missing"] == [2]


def test_date_filter_has_a_time_and_seconds():
    times = [dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 3, 4, 5, 6)]
    engine = LazyEngine(GTI(pl.LazyFrame({"t": times})).i_cols_filter("t", type="date"))
    [f] = engine.spec["filters"]
    assert f["values"] == ["2020-01-01T00:00:00", "2020-01-03T04:05:06"]
    times[2] = dt.datetime(2020, 1, 3, 4, 5)
    engine = LazyEngine(GTI(pl.LazyFrame({"t": times})).i_cols_filter("t", type="date"))
    assert engine.spec["filters"][0]["values"] == ["2020-01-01T00:00:00", "2020-01-03T04:05:00"]


# Its pages are the eager table's ----


@pytest.mark.parametrize("rowname_col", [None, "char"])
def test_pages_are_the_eager_tables(rowname_col):
    def make(data):
        return (
            GTI(data, rowname_col=rowname_col, id="t")
            .fmt_number("num", decimals=1)
            .tab_style(style.fill("red"), loc.body(columns="int", rows=pl.col("int") > 2))
            .tab_header("Fruit")
            .i_inspect()
            .i_cols_filter("fctr", type="facet")
            .i_pagination(page_size=3)
            .i_view(sort="-num")
        )

    eager, lazy = engines(make(FRAME), make(FRAME.lazy()))
    for start in (0, 3, 6):
        query = page_query(sort=[{"column": "num", "descending": True}], start=start)
        assert lazy.page(query) == eager.page(query)
    assert lazy.render() == eager.render()


def test_page_is_made_from_its_rows_only():
    calls = []

    def upper(x):
        calls.append(x)
        return x.upper()

    gti = GTI(FRAME.lazy()).fmt(upper, columns="char").i_pagination(page_size=2).i_scale("kernel")
    html, _, engine = render_table(gti)
    assert isinstance(engine, LazyEngine) and '"remote":{"count":8,"rows":[0,1]}' in html
    assert calls == ["apricot", "Banana"]
    assert "COCONUT" in engine.page(page_query(start=2, size=1))["html"]


def test_labels_are_the_cells_text():
    gti = make_gti(FRAME.lazy()).fmt(lambda x: f"<b>{str(x).upper()}</b>", columns="fctr")
    _, spec = LazyEngine(gti).render()
    fctr = next(f for f in spec["filters"] if f["column"] == "fctr")
    assert fctr["labels"] == ["ONE", "THREE", "TWO"]


def test_view_rows_and_code_are_the_eager_tables():
    eager = make_gti(FRAME).i_view(filter="num > 1", sort="-int")
    lazy = make_gti(FRAME.lazy()).i_view(filter="num > 1", sort="-int")
    assert view_rows(lazy) == view_rows(eager)
    assert query_code(lazy) == query_code(eager)


# Made again from the calls that made it ----


def test_methods_keep_the_frame_and_their_calls():
    lf = FRAME.lazy()
    gti = GTI(lf).fmt_number("num").pipe(lambda t: t.cols_label(num="Number")).i_search(False)
    lazy = lazy_of(gti)
    assert lazy is not None and lazy.frame is lf
    # (Not those `pipe()` makes, which it makes again)
    assert [name for name, _, _ in lazy.calls] == ["fmt_number", "pipe"]
    assert gti._tbl_data.height == 0
    assert lazy_of(GTI(FRAME)) is None


def test_collected_is_kept_and_has_the_tables_settings():
    gti = GTI(FRAME.lazy()).fmt_number("num")
    table = collected(gti)
    assert table._tbl_data.height == 8 and lazy_of(table) is None
    assert collected(gti)._tbl_data is table._tbl_data
    searchless = collected(gti.i_search(False))
    assert searchless._tbl_data is table._tbl_data
    assert not searchless._interactive.search


def test_text_that_looks_like_numbers_is_aligned_by_every_row():
    data = pl.LazyFrame({"n": ["1", "2", None], "t": ["1", "a", "2"]})
    gti = GTI(data)
    assert [info.column_align for info in gti._boxhead] == ["right", "left"]
    assert [info.column_align for info in collected(gti)._boxhead] == ["right", "left"]


@pytest.mark.parametrize(
    "make, message",
    [
        (lambda t: t.data_color("num"), "data_color"),
        (lambda t: t.pipe(lambda t: t.data_color("num")), "data_color"),
        (lambda t: t.tab_footnote("A note", loc.body("num", rows=pl.col("num") > 1)), "footnote"),
        (lambda t: t.tab_footnote("A note", [loc.title(), loc.stub()]), "footnote"),
        (lambda t: t.tab_style(style.fill("red"), loc.body("num", rows=[1])), "positions"),
    ],
)
def test_methods_needing_every_row_raise(make, message):
    with pytest.raises(ValueError, match=message):
        make(GTI(FRAME.lazy()).tab_header("Fruit"))


def test_footnotes_elsewhere_are_kept():
    gti = GTI(FRAME.lazy(), id="t").tab_footnote("A note", loc.column_labels("num"))
    assert "A note" in gti.as_raw_html()


# Where it's shown ----


def test_browser_table_is_collected():
    lazy = make_gti(FRAME.lazy()).fmt_number("num", decimals=1)
    eager = make_gti(FRAME).fmt_number("num", decimals=1)
    assert lazy.as_raw_html() == eager.as_raw_html()


def test_large_browser_table_warns_it_was_collected():
    big = pl.LazyFrame({"n": range(4000)})
    with pytest.warns(GTISizeWarning, match="collected from its LazyFrame"):
        GTI(big).as_raw_html()


def test_summary_rows_are_made_from_every_row():
    gti = GTI(FRAME.lazy(), id="t").grand_summary_rows(fns={"Total": pl.col("int").sum()})
    eager = GTI(FRAME, id="t").grand_summary_rows(fns={"Total": pl.col("int").sum()})
    assert gti.as_raw_html() == eager.as_raw_html()
    with pytest.warns(GTIEngineWarning, match="summary rows"):
        _, _, engine = render_table(gti.i_scale("kernel"))
    assert engine is None


def test_row_groups_stay_in_the_browser():
    gti = GTI(FRAME.lazy(), groupname_col="fctr").i_scale("kernel")
    with pytest.warns(GTIEngineWarning, match="row groups"):
        _, spec, engine = render_table(gti)
    assert engine is None and spec["nrows"] == 8


# As a widget ----

anywidget = pytest.importorskip("anywidget")


def test_auto_widget_collects_few_rows_and_keeps_many_in_python():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        few = GTI(FRAME.lazy()).i_as_widget()
        many = GTI(pl.LazyFrame({"n": range(4000), "t": ["x"] * 4000})).i_as_widget()
    assert not few._kernel and few.view().height == 8
    assert many._kernel and many._nrows == 4000
    assert isinstance(many._engine, LazyEngine)


def test_widget_finds_and_views_rows():
    widget = make_gti(FRAME.lazy()).i_selection("multiple").i_scale("kernel").i_as_widget()
    widget.query = 'fctr in ("one")'
    widget.sort = "-char"
    assert widget.rows == [6, 2, 0]
    assert widget.view()["char"].to_list() == ["kiwi", "coconut", "apricot"]
    widget.selection = [7, 1]
    assert widget.view(selected=True)["char"].to_list() == ["Banana", "Éclair"]
    with pytest.raises(ValueError, match="has 8 rows"):
        widget.selection = [8]


def test_widget_dropped_features_warning_is_the_callers():
    gti = GTI(FRAME.lazy()).i_cols_profile("num").i_scale("kernel")
    with pytest.warns(GTIEngineWarning, match="profiles") as record:
        gti.i_as_widget()
    assert record[0].filename == __file__


def test_widget_answers_pages():
    widget = GTI(FRAME.lazy()).i_pagination(page_size=2).i_scale("kernel").i_as_widget()
    sent: list = []
    widget.send = sent.append
    assert '"remote":{"count":8,"rows":[0,1]}' in widget._html
    query = page_query(start=6, size=2)
    widget._on_msg(None, {"type": "ask", "id": "v:1", "kind": "page", "query": query}, [])
    answer = sent[-1]["answer"]
    assert answer["rows"] == [6, 7]
    assert re.findall(r'headers="char"[^>]*>([^<]*)<', answer["html"]) == ["kiwi", "Éclair"]
