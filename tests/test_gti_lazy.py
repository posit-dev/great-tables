"""Tables of lazy frames (`GTI(lf)`: a Polars LazyFrame, a DuckDB relation or an Ibis table): made
again from the rows shown, and in kernel mode, their views found with queries of the frame's backend
(great_tables/_gti/_lazy.py).

A lazy table's views are found from its rows' values (as text, for its search), where an eager
table's are found from its cells' text, as the runtime reads them: so the two are compared with
data whose cells show their values as they are. A DuckDB relation's or an Ibis table's eager table
is of its rows as the backend collects them, in their order (by `order_by=`).
"""

from __future__ import annotations

import datetime as dt
import re
import warnings

import narwhals as nw
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

BACKENDS = ["polars", "duckdb", "ibis"]


def lazy_frame(backend: str, data: pl.DataFrame):
    """The data as a lazy frame of the backend."""
    if backend == "polars":
        return data.lazy()
    if backend == "duckdb":
        duckdb = pytest.importorskip("duckdb")
        return duckdb.connect().from_arrow(data.to_arrow())
    ibis = pytest.importorskip("ibis")
    return ibis.memtable(data.to_arrow())


def eager_data(backend: str, data: pl.DataFrame, order_by: str = "char"):
    """The data as the backend collects it, in the order of `order_by=` (but a LazyFrame's)."""
    if backend == "polars":
        return data
    return nw.from_native(lazy_frame(backend, data)).sort(order_by).collect().to_native()


def pair(backend: str, make, data: pl.DataFrame = FRAME, order_by: str = "char"):
    """The tables `make()` makes of the data, eager and lazy (in the backend's order)."""
    lazy = lazy_frame(backend, data)
    order = {} if backend == "polars" else {"order_by": order_by}
    return make(eager_data(backend, data, order_by), {}), make(lazy, order)


QUERY = {"search": "", "hidden": [], "filter": None, "links": [], "sort": []}


def make_gti(data, order=None) -> GTI:
    return (
        GTI(data, id="t", **(order or {}))
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


@pytest.fixture(scope="module", params=BACKENDS)
def both(request) -> tuple[KernelEngine, LazyEngine]:
    return engines(*pair(request.param, make_gti))


def unkind(html: str) -> str:
    """The table's HTML, but for what it says the data is (which a lazy table names as lazy), and
    where its rows' numbers start (from 1 for a database's)."""
    html = re.sub(r'"row_start":[01]', '"row_start":0', html)
    return re.sub(r'"data_kind":(null|"[^"]*")', '"data_kind":null', html)


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


@pytest.mark.parametrize("backend", BACKENDS)
def test_search_folds_as_the_runtime_does(backend):
    data = pl.DataFrame({"w": ["Crème", "ΟΔΟΣ", "οδος", "한국어", "Straße"]})
    eager, lazy = engines(*pair(backend, lambda d, o: GTI(d, **o).i_cols_filter("w"), data, "w"))
    for search in ["ΟΔΟΣ", "οδοσ", "οδος", "creme", "CRÈME", "한국", "국", "STRASSE", "straße"]:
        for query in (
            {**QUERY, "search": search},
            {**QUERY, "filter": contains(eager, "w", search)},
        ):
            assert lazy.rows(query) == eager.rows(query), (search, query)
    assert lazy.rows({**QUERY, "search": "ΟΔΟΣ"}) == lazy.rows({**QUERY, "search": "οδοσ"})
    assert len(lazy.rows({**QUERY, "search": "한국"})) == 1


def contains(engine: KernelEngine, column: str, text: str) -> dict | None:
    return check_query_value(engine.spec, f'{column} contains "{text}"', "q")


@pytest.mark.parametrize("backend", BACKENDS)
def test_search_reads_durations_and_skips_nested_values(backend):
    if backend == "ibis":
        pytest.skip("Ibis can't collect a duration (DuckDB's interval) to PyArrow")
    data = pl.DataFrame({"d": [dt.timedelta(hours=1), None], "l": [[1, 2], [3]]})
    engine = LazyEngine(GTI(lazy_frame(backend, data)))
    # (A duration's text is the backend's)
    hour = {"polars": "1h", "duckdb": "01:00:00", "ibis": "01:00:00"}[backend]
    assert engine.rows({**QUERY, "search": hour}) == ([0] if backend == "polars" else [1])
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


@pytest.mark.parametrize("backend", BACKENDS)
def test_date_filter_has_a_time_and_seconds(backend):
    def values(times):
        frame = lazy_frame(backend, pl.DataFrame({"t": times}))
        [f] = LazyEngine(GTI(frame).i_cols_filter("t", type="date")).spec["filters"]
        return f["values"]

    times = [dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 3, 4, 5, 6)]
    assert values(times) == ["2020-01-01T00:00:00", "2020-01-03T04:05:06"]
    times[2] = dt.datetime(2020, 1, 3, 4, 5)
    assert values(times) == ["2020-01-01T00:00:00", "2020-01-03T04:05:00"]
    times[2] = dt.datetime(2020, 1, 3, 4, 5, 0, 5)
    assert values(times)[-1].startswith("2020-01-03T04:05:00.000005")


# Its pages are the eager table's ----


@pytest.mark.parametrize("backend", BACKENDS)
@pytest.mark.parametrize("rowname_col", [None, "char"])
def test_pages_are_the_eager_tables(backend, rowname_col):
    def make(data, order):
        return (
            GTI(data, rowname_col=rowname_col, id="t", **order)
            .fmt_number("num", decimals=1)
            .tab_style(style.fill("red"), loc.body(columns="int", rows=["kiwi", "fig"]))
            .tab_header("Fruit")
            .i_inspect()
            .i_cols_filter("fctr", type="facet")
            .i_pagination(page_size=3)
            .i_view(sort="-num")
        )

    eager, lazy = engines(*pair(backend, make))
    for start in (0, 3, 6):
        query = page_query(sort=[{"column": "num", "descending": True}], start=start)
        assert lazy.page(query) == eager.page(query)
    (lazy_html, lazy_spec), (eager_html, eager_spec) = lazy.render(), eager.render()
    assert unkind(lazy_html) == unkind(eager_html)
    kindless = {"data_kind": None, "row_start": 0}
    assert {**lazy_spec, "display": {**lazy_spec["display"], **kindless}} == {
        **eager_spec,
        "display": {**eager_spec["display"], **kindless},
    }


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


@pytest.mark.parametrize("backend", BACKENDS)
def test_view_rows_and_code_are_the_eager_tables(backend):
    eager, lazy = (table.i_view(filter="num > 1", sort="-int") for table in pair(backend, make_gti))
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


# Its rows' order ----


def test_relations_rows_are_numbered_by_their_columns():
    duckdb = pytest.importorskip("duckdb")
    # (A relation sorted with ties, whose rows' order DuckDB doesn't keep from query to query)
    rel = duckdb.sql("select i % 7 as v, i from range(300000) r(i) order by v")
    engine = LazyEngine(GTI(rel).i_scale("kernel"))
    assert engine.data(list(range(3)))["i"].to_pylist() == [0, 7, 14]
    assert engine.data([299999, 1])["i"].to_pylist() == [299998, 7]
    # (By `order_by=`'s columns, then the others)
    engine = LazyEngine(GTI(rel, order_by="i").i_cols_filter("v").i_scale("kernel"))
    assert engine.data([0, 1, 299999])["i"].to_pylist() == [0, 1, 299999]
    rows = engine.rows(
        {**QUERY, "filter": check_query_value(engine.spec, "v >= 3 and v <= 3", "q")}
    )
    assert rows[:3] == [3, 10, 17] and len(rows) == 42857


def test_lazyframes_rows_are_in_its_order_or_order_by():
    lf = pl.LazyFrame({"n": [3, 1, 2], "t": ["c", "a", "b"]})
    assert collected(GTI(lf))._tbl_data["n"].to_list() == [3, 1, 2]
    assert collected(GTI(lf, order_by="t"))._tbl_data["n"].to_list() == [1, 2, 3]


def test_ibis_table_of_another_backend_is_queried_there():
    ibis = pytest.importorskip("ibis")
    con = ibis.sqlite.connect()
    data = pl.DataFrame({"w": ["Crème", "Apple", "BANANA"], "n": [1, 2, 3]})
    # (Made from a memtable: sqlglot 30.31 breaks Ibis's SQLite `create_table()` of PyArrow data)
    table = con.create_table("w", ibis.memtable(data.to_arrow()))
    engine = LazyEngine(GTI(table).i_scale("kernel"))
    # (Numbered as they sort, by `w`; its text lowercased, but its accents kept)
    assert engine.rows({**QUERY, "search": "banana"}) == [1]
    assert engine.rows({**QUERY, "search": "creme"}) == []
    assert engine.page(page_query(start=1, size=2))["rows"] == [1, 2]


def test_order_by_is_checked():
    with pytest.raises(ValueError, match="doesn't have"):
        GTI(FRAME.lazy(), order_by="nope")
    with pytest.raises(ValueError, match="isn't one"):
        GTI(FRAME, order_by="char")
    duckdb = pytest.importorskip("duckdb")
    with pytest.raises(ValueError, match="give an `order_by=`"):
        GTI(duckdb.sql("select [1, 2] as l"))


# Where it's shown ----


def test_browser_table_is_collected():
    lazy = make_gti(FRAME.lazy()).fmt_number("num", decimals=1)
    eager = make_gti(FRAME).fmt_number("num", decimals=1)
    assert unkind(lazy.as_raw_html()) == unkind(eager.as_raw_html())
    # (But it still says it's a LazyFrame)
    assert '"data_kind":"Polars LazyFrame"' in lazy.as_raw_html()


@pytest.mark.parametrize("backend", ["duckdb", "ibis"])
def test_browser_table_of_a_relation_is_collected_in_order(backend):
    eager, lazy = pair(backend, lambda d, o: make_gti(d, o).fmt_number("num", decimals=1))
    assert unkind(lazy.as_raw_html()) == unkind(eager.as_raw_html())
    assert type(collected(lazy)._tbl_data).__name__ == "Table"


def test_large_browser_table_warns_it_was_collected():
    big = pl.LazyFrame({"n": range(4000)})
    with pytest.warns(GTISizeWarning, match="collected from its lazy frame"):
        GTI(big).as_raw_html()


def test_summary_rows_are_made_from_every_row():
    gti = GTI(FRAME.lazy(), id="t").grand_summary_rows(fns={"Total": pl.col("int").sum()})
    eager = GTI(FRAME, id="t").grand_summary_rows(fns={"Total": pl.col("int").sum()})
    assert unkind(gti.as_raw_html()) == unkind(eager.as_raw_html())
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


def test_widget_of_a_relation_views_its_rows():
    duckdb = pytest.importorskip("duckdb")
    rel = duckdb.connect().from_arrow(FRAME.to_arrow())
    widget = make_gti(rel, {"order_by": "char"}).i_selection("multiple").i_scale("kernel")
    widget = widget.i_as_widget()
    widget.query = 'fctr in ("one")'
    widget.sort = "-int"
    # (Numbered as they sort by `char`: "Banana", "apricot", "coconut", ...)
    assert widget.view()["char"].to_pylist() == ["apricot", "kiwi", "coconut"]
    widget.selection = [0]
    assert widget.view(selected=True)["char"].to_pylist() == ["Banana"]


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
