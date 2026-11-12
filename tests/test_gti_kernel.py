"""Kernel mode (`GTI.i_scale()`): a widget's rows kept in Python, which finds them as the runtime
would, and sends the browser a page at a time.

The browser's side (packages/gti/src/widget.ts's `KernelSource`, and a remote `<gt-table>`) is
tested with Vitest.
"""

from __future__ import annotations

import re
import warnings

import pandas as pd
import polars as pl
import pyarrow as pa
import pytest

from great_tables import GT, GTI, loc
from great_tables._gti._kernel import KernelEngine, kernel_reasons
from great_tables._gti._query import view_rows
from great_tables._gti._render import GTIEngineWarning, GTISizeWarning, _build

DATA = {
    "char": ["apricot", "banana", "coconut", "durian", "fig", "grape", "kiwi"],
    "num": [3.0, 1.0, None, 5.0, 1.0, None, 2.0],
    "fctr": ["one", "two", "one", None, "two", "three", "one"],
}

FRAMES = [pd.DataFrame, pl.DataFrame, pa.table]

QUERY = {"search": "", "hidden": [], "filter": None, "links": [], "sort": []}


def make_gti(frame=pl.DataFrame, data=None) -> GTI:
    return (
        GTI(frame(DATA if data is None else data))
        .i_cols_filter("fctr", type="facet")
        .i_cols_filter("num")
        .i_cols_filter("char", type="text")
    )


def make_engine(gti: GTI) -> KernelEngine:
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        return KernelEngine(gti)


def page_query(**parts) -> dict:
    return {**QUERY, "start": 0, "size": 3, **parts}


def body_trs(html: str) -> list[str]:
    body = re.search(r'<tbody class="gt_table_body">\n(.*?)</tbody>', html, re.S)
    assert body is not None
    return [tr.rstrip("\n") for tr in re.split(r"(?m)^(?=  <tr[ >])", body.group(1)) if tr]


@pytest.mark.parametrize("frame", FRAMES)
@pytest.mark.parametrize(
    "filter, sort",
    [
        (None, []),
        (None, ["num"]),
        (None, ["-num"]),
        (None, ["fctr", "-num"]),
        ('fctr in ("one", "two")', ["-char"]),
        ("num > 1", ["num"]),
        ("num is null or fctr is null", []),
        ('char contains "an"', ["-fctr"]),
        ("char matches /^[a-d]/", ["num"]),
    ],
)
def test_rows_are_view_rows(frame, filter, sort):
    gti = make_gti(frame).i_view(filter=filter, sort=sort or None)
    engine = make_engine(gti)
    view = engine.spec["view"]
    query = {**QUERY, "filter": view["filter"], "sort": view["sort"]}
    assert engine.find(query) == view_rows(gti)
    assert engine.rows(query) == sorted(view_rows(gti))


@pytest.mark.parametrize("frame", FRAMES)
def test_search_needs_every_term_in_a_searched_column(frame):
    engine = make_engine(make_gti(frame))
    assert engine.rows({**QUERY, "search": "THREE"}) == [5]
    # (A missing value's cell shows "None")
    assert engine.rows({**QUERY, "search": "one"}) == [0, 2, 3, 5, 6]
    assert engine.rows({**QUERY, "search": "an three"}) == []
    assert engine.rows({**QUERY, "search": "  an two "}) == [1]
    # (Hidden columns aren't searched)
    assert engine.rows({**QUERY, "search": "three", "hidden": ["fctr"]}) == []
    assert engine.rows({**QUERY, "search": "zzz"}) == []


def test_search_reads_footnoted_cells_as_shown():
    gti = make_gti().tab_footnote("A note", locations=loc.body("char", rows=[1]))
    engine = make_engine(gti)
    assert engine.rows({**QUERY, "search": "banana"}) == [1]


def test_search_matches_formatted_text():
    gti = make_gti().fmt_number("num", decimals=2)
    engine = make_engine(gti)
    assert engine.rows({**QUERY, "search": "5.00"}) == [3]


def test_facet_counts_ranks():
    engine = make_engine(make_gti())
    ranks = engine.spec["ranks"]["fctr"]
    counts = dict(map(tuple, engine.facet(QUERY, "fctr")))
    assert counts == {ranks[0]: 3, ranks[1]: 2, ranks[5]: 1, -1: 1}
    with pytest.raises(ValueError, match="no filter"):
        engine.facet(QUERY, "char2")


def test_page_and_clamping():
    engine = make_engine(make_gti())
    page = engine.page(page_query(sort=[{"column": "num", "descending": False}]))
    assert page["count"] == 7 and page["start"] == 0 and page["rows"] == [1, 4, 6]
    assert engine.page(page_query(start=3))["rows"] == [3, 4, 5]
    # (Past the end, the last page)
    last = engine.page(page_query(start=30))
    assert last["start"] == 6 and last["rows"] == [6]
    empty = engine.page(page_query(search="zzz", start=6))
    assert empty == {"count": 0, "start": 0, "rows": [], "html": ""}
    assert engine.page(page_query(size=None))["rows"] == list(range(7))


@pytest.mark.parametrize(
    "parts, message",
    [
        ({"start": -1}, "`start`"),
        ({"start": 1.5}, "`start`"),
        ({"size": 0}, "`size`"),
        ({"size": True}, "`size`"),
        ({"search": 1}, "`search`"),
        ({"hidden": "num"}, "`hidden`"),
        ({"sort": [{"column": "zzz"}]}, "`sort`"),
        ({"filter": "nope ("}, "`filter`"),
    ],
)
def test_page_checks_query(parts, message):
    engine = make_engine(make_gti())
    with pytest.raises((ValueError, TypeError), match=message):
        engine.page(page_query(**parts))


def test_page_needs_object():
    with pytest.raises(TypeError, match="object"):
        make_engine(make_gti()).find("all")


@pytest.mark.parametrize("rowname_col", [None, "char"])
def test_page_html_is_the_tables_rows(rowname_col):
    gti = GTI(pl.DataFrame(DATA), rowname_col=rowname_col).fmt_number("num", decimals=1)
    engine = make_engine(gti)
    full = body_trs(_build(gti)._render_as_html())
    page = engine.page(page_query(sort=[{"column": "num", "descending": True}]))
    assert page["rows"] == [3, 0, 6]
    assert body_trs(f'<tbody class="gt_table_body">\n{page["html"]}</tbody>') == [
        full[row] for row in page["rows"]
    ]


def test_page_html_tints_missing_values():
    gti = make_gti().i_inspect()
    engine = make_engine(gti)
    trs = body_trs(
        f'<tbody class="gt_table_body">\n{engine.page(page_query(start=3))["html"]}</tbody>'
    )
    tinted = [[cell for cell in tr.split("\n") if "gt-i-missing" in cell] for tr in trs]
    assert [len(cells) for cells in tinted] == [1, 0, 1]
    assert 'headers="fctr"' in tinted[0][0] and 'headers="num"' in tinted[2][0]


def test_render_gives_the_first_page_and_a_remote_spec():
    gti = make_gti().i_pagination(page_size=2).i_view(sort="-num").i_inspect()
    engine = make_engine(gti)
    html, spec = engine.render()
    assert spec["remote"] == {"count": 7, "rows": [3, 0]}
    assert spec["body"] == [3, 0]
    assert spec["nrows"] == 7
    assert spec["ranks"] == {column: [] for column in engine.spec["ranks"]}
    assert spec["pagination"]["enabled"]
    assert len(body_trs(html)) == 2
    # (Only the page's missing values, and a filter's first)
    missing = {c["id"]: c["missing"] for c in spec["columns"]}
    assert missing == {"char": [], "num": [], "fctr": [3]}
    fctr = next(f for f in spec["filters"] if f["column"] == "fctr")
    assert fctr["missing"] == [3]
    assert fctr["labels"] == ["one", "three", "two"]
    assert "labels" not in next(f for f in spec["filters"] if f["column"] == "num")
    # (The engine's own spec has every row's)
    assert len(engine.spec["ranks"]["num"]) == 7


def test_render_filters_the_first_page():
    gti = make_gti().i_pagination(page_size=2).i_view(filter='fctr in ("two")')
    _, spec = make_engine(gti).render()
    assert spec["remote"] == {"count": 2, "rows": [1, 4]}


def test_labels_are_the_cells_text():
    gti = make_gti().fmt(lambda x: f"<b>{str(x).upper()}</b>", columns="fctr")
    _, spec = make_engine(gti).render()
    fctr = next(f for f in spec["filters"] if f["column"] == "fctr")
    assert fctr["labels"] == ["ONE", "THREE", "TWO"]


def test_dropped_features_are_warned_about():
    gti = (
        make_gti()
        .i_pagination(enabled=False)
        .i_export(["csv", "code"])
        .i_row_details("char")
        .i_cols_profile("num")
    )
    with pytest.warns(GTIEngineWarning, match="can't have every row on one page") as record:
        engine = KernelEngine(gti)
    message = str(record[0].message)
    assert "rows' details" in message and "profiles" in message and "'csv'" in message
    _, spec = engine.render()
    assert spec["export"]["formats"] == ["code"]
    assert spec["details"] == [] and spec["profiles"] == [] and spec["pagination"]["enabled"]


@pytest.mark.parametrize(
    "gti, reason",
    [
        (GTI(pl.DataFrame(DATA), groupname_col="fctr"), "row groups"),
        (
            GTI(pd.DataFrame(DATA), rowname_col="char").grand_summary_rows(
                fns={"Total": lambda df: df[["num"]].sum()}
            ),
            "summary rows",
        ),
    ],
)
def test_kernel_reasons(gti, reason):
    assert reason in kernel_reasons(_build(gti))


def test_kernel_reasons_none():
    assert kernel_reasons(_build(make_gti())) == []


@pytest.mark.parametrize("engine", ["gpu", None, 1])
def test_i_scale_checks_engine(engine):
    with pytest.raises(ValueError, match="`engine=`"):
        GTI(pl.DataFrame(DATA)).i_scale(engine)


def test_kernel_outside_a_widget_warns():
    with pytest.warns(GTIEngineWarning, match="only when it's shown as a widget"):
        make_gti().i_scale("kernel").as_raw_html()


def test_size_warning_suggests_kernel():
    big = {"n": list(range(4000))}
    with pytest.warns(GTISizeWarning, match="i_scale"):
        GTI(pl.DataFrame(big)).as_raw_html()
    # (Not for a table that can't keep its rows in Python, nor for GT's)
    grouped = {**big, "g": ["a", "b"] * 2000}
    for gt in (
        GTI(pl.DataFrame(grouped), groupname_col="g"),
        GT(pl.DataFrame(big)).opt_interactive(),
    ):
        with pytest.warns(GTISizeWarning) as record:
            gt.as_raw_html()
        assert all("i_scale" not in str(r.message) for r in record)


# -----
# The widget

anywidget = pytest.importorskip("anywidget")


def make_widget(gti: GTI):
    widget = gti.i_as_widget()
    sent: list = []
    widget.send = sent.append
    return widget, sent


def ask(widget, sent, **content):
    widget._on_msg(None, {"type": "ask", "id": "v:1", **content}, [])
    assert sent[-1]["id"] == "v:1" and sent[-1]["type"] == "answer"
    return sent[-1]


def test_widget_in_kernel_mode():
    widget, sent = make_widget(make_gti().i_scale("kernel").i_pagination(page_size=2))
    assert widget._kernel and widget._nrows == 7
    assert widget._engine is not None
    # (Its spec, for checking views, is every row's)
    assert len(widget._spec["ranks"]["num"]) == 7
    assert '"remote":{"count":7,"rows":[0,1]}' in widget._html

    answer = ask(widget, sent, kind="page", query=page_query(start=2, size=2))["answer"]
    assert answer["rows"] == [2, 3] and answer["count"] == 7 and answer["html"].count("<tr") == 2
    assert ask(widget, sent, kind="rows", query={**QUERY, "search": "two"})["answer"] == [1, 4]
    facet = ask(widget, sent, kind="facet", query=QUERY, column="fctr")["answer"]
    assert sum(count for _, count in facet) == 7


def test_widget_answers_errors():
    widget, sent = make_widget(make_gti().i_scale("kernel"))
    assert "no filter" in ask(widget, sent, kind="facet", query=QUERY, column="char2")["error"]
    assert "`start`" in ask(widget, sent, kind="page", query=page_query(start=-2))["error"]
    assert "no answer" in ask(widget, sent, kind="nope", query=QUERY)["error"]


def test_widget_in_browser_mode_ignores_asks():
    widget, sent = make_widget(make_gti())
    assert not widget._kernel and widget._engine is None
    widget._on_msg(None, {"type": "ask", "id": "v:1", "kind": "page", "query": QUERY}, [])
    assert sent == []


def test_widget_rows_are_pythons_at_once():
    widget, _ = make_widget(make_gti().i_scale("kernel"))
    widget.query = 'fctr in ("one")'
    widget.sort = "-char"
    assert widget.rows == [6, 2, 0]
    # (Even once shown, and with a search)
    widget.set_state({"_view": {**widget._current_view(), "search": "coco"}})
    assert widget.rows == [2]
    assert list(widget.view()["char"]) == ["coconut"]


def test_auto_is_kernel_for_many_rows():
    many = {"n": list(range(4000)), "t": ["x"] * 4000}
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        widget = GTI(pl.DataFrame(many)).i_as_widget()
        few = GTI(pl.DataFrame(DATA)).i_as_widget()
    assert widget._kernel and widget._nrows == 4000
    assert not few._kernel


def test_auto_with_row_groups_stays_in_the_browser():
    many = {"n": list(range(4000)), "g": ["a", "b"] * 2000}
    with pytest.warns(GTISizeWarning):
        widget = GTI(pl.DataFrame(many), groupname_col="g").i_as_widget()
    assert not widget._kernel


def test_kernel_with_row_groups_warns_and_stays_in_the_browser():
    gti = GTI(pl.DataFrame(DATA), groupname_col="fctr").i_scale("kernel")
    with pytest.warns(GTIEngineWarning, match="row groups") as record:
        widget = gti.i_as_widget()
    assert not widget._kernel
    assert record[0].filename == __file__


def test_browser_widget_doesnt_warn_about_kernel():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        widget = make_gti().i_scale("browser").i_as_widget()
    assert not widget._kernel
