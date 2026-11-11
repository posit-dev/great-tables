"""`GTI.i_as_widget()`: the widget's view and selection, as Python reads and sets them.

The browser's side (packages/gti/src/widget.ts) is tested with Vitest, and the two together in
JupyterLab (packages/gti/e2e/hosts.spec.ts).
"""

from __future__ import annotations

import sys

import pandas as pd
import polars as pl
import pyarrow as pa
import pytest

pytest.importorskip("anywidget")

from great_tables import GTI  # noqa: E402
from great_tables._gti._render import JS_DIR, _load_runtime, render_gti_element  # noqa: E402
from great_tables._gti._widget import GTIWidget, _esm  # noqa: E402

DATA = {
    "char": ["apricot", "banana", "coconut", "durian", "fig"],
    "num": [3.0, 1.0, None, 5.0, 2.0],
    "fctr": ["one", "two", "one", "three", "two"],
}

VIEW = {
    "filter": None,
    "sort": [],
    "search": "",
    "page": 1,
    "page_size": None,
    "hidden": [],
    "group_by": None,
}


def make_widget(data=None, selection=None) -> GTIWidget:
    gti = (
        GTI(pd.DataFrame(DATA) if data is None else data)
        .i_cols_filter("fctr", type="facet")
        .i_cols_filter("num")
    )
    return gti.i_selection(selection).i_as_widget()


def show(widget: GTIWidget, **view) -> None:
    """Set the widget's state as the browser gives it, with the rows its view keeps."""
    rows = view.pop("rows")
    selection = view.pop("selection", widget.selection)
    widget.set_state({"_view": {**VIEW, **view}, "_rows": rows, "_selection": selection})


def test_widget_is_made():
    widget = make_widget()
    assert isinstance(widget, GTIWidget)
    assert widget._html.startswith("<gt-table")
    assert "<script>" not in widget._html
    assert widget._view is None and widget._rows is None and widget._selection == []


def test_render_gti_element_gives_spec():
    html, spec = render_gti_element(GTI(pd.DataFrame(DATA)))
    assert html.startswith("<gt-table") and html.endswith("</gt-table>\n")
    assert spec["nrows"] == 5


def test_esm_is_runtime_then_glue():
    js, _ = _load_runtime()
    assert _esm() == js + (JS_DIR / "gti-widget.js").read_text(encoding="utf-8")


def test_state_before_shown_is_authors():
    widget = (
        GTI(pd.DataFrame(DATA))
        .i_cols_filter("fctr", type="facet")
        .i_cols_filter("num")
        .i_view(filter='fctr in ("one", "two")', sort="-num")
        .i_pagination()
        .i_as_widget()
    )
    assert widget.query == 'fctr in ("one", "two")'
    assert widget.sort == ["-num"]
    assert widget.search == ""
    assert widget.selection == []
    # (Row 2's `num` is missing, so it's last)
    assert widget.rows == [0, 4, 1, 2]


def test_rows_before_shown_follow_groups():
    widget = (
        GTI(pd.DataFrame(DATA))
        .i_cols_controls(columns="fctr", groupable=True)
        .i_view(group_by="fctr", sort="char")
        .i_as_widget()
    )
    rows = widget.rows
    groups = [DATA["fctr"][row] for row in rows]
    # (Grouped by `fctr`'s values, in order, the rows sorted within each)
    assert groups == sorted(groups) and len(rows) == 5
    assert [DATA["char"][row] for row in rows if DATA["fctr"][row] == "two"] == ["banana", "fig"]


def test_setters_set_view_and_clear_rows():
    widget = make_widget()
    show(widget, rows=[0, 1, 2, 3, 4], page=2)
    widget.query = 'fctr in ("one")'
    assert widget._view == {
        **VIEW,
        "filter": {"and": [{"col": "fctr", "op": "in", "value": ["one"]}]},
    }
    assert widget._rows is None
    assert widget.query == 'fctr in ("one")'

    widget.query = "  "
    assert widget._view["filter"] is None
    widget.query = {"and": [{"col": "num", "op": "gte", "value": 2}]}
    assert widget.query == "num >= 2"
    widget.query = None
    assert widget.query == ""

    widget.sort = "-num"
    assert widget._view["sort"] == [{"column": "num", "descending": True}]
    widget.sort = ["fctr", "-char"]
    assert widget.sort == ["fctr", "-char"]
    widget.sort = None
    assert widget.sort == []

    widget.search = "an"
    assert widget._view["search"] == "an"


def test_setters_check_values():
    widget = make_widget()
    with pytest.raises(ValueError, match="`query`"):
        widget.query = "fctr in ("
    with pytest.raises(ValueError, match="nope"):
        widget.query = 'nope in ("a")'
    with pytest.raises(ValueError, match="nope"):
        widget.sort = "nope"
    with pytest.raises(TypeError, match="`search`"):
        widget.search = 3  # type: ignore[assignment]


def test_selection_is_checked():
    widget = make_widget(selection="multiple")
    widget.selection = [3, 1, 3]
    assert widget.selection == [1, 3]
    assert widget._selection == [1, 3]
    widget.selection = []
    assert widget.selection == []
    for bad in ([-1], [1.5], [True], ["1"]):
        with pytest.raises(ValueError, match="whole numbers"):
            widget.selection = bad
    with pytest.raises(ValueError, match="has 5 rows"):
        widget.selection = [5]
    with pytest.raises(TypeError, match="list of data rows"):
        widget.selection = 3

    single = make_widget(selection="single")
    single.selection = [2]
    with pytest.raises(ValueError, match="Only one"):
        single.selection = [1, 2]

    none = make_widget()
    with pytest.raises(ValueError, match="i_selection"):
        none.selection = [1]


def test_rows_are_browsers_once_shown():
    widget = make_widget()
    show(widget, rows=[1, 3], search="an")
    assert widget.rows == [1, 3]
    assert widget.search == "an"
    widget.search = ""
    with pytest.raises(RuntimeError, match="another cell"):
        widget.rows
    show(widget, rows=[0, 1, 2, 3, 4])
    assert widget.rows == [0, 1, 2, 3, 4]


def test_rows_with_search_before_shown():
    widget = make_widget()
    widget.search = "an"
    with pytest.raises(RuntimeError, match="before it's shown with a search"):
        widget.rows


def chars(frame) -> list[str]:
    if isinstance(frame, pa.Table):
        return frame.column("char").to_pylist()
    return list(frame["char"])


@pytest.mark.parametrize(
    "frame",
    [pd.DataFrame, pl.DataFrame, pa.table],
    ids=["pandas", "polars", "pyarrow"],
)
def test_view_gives_frame(frame):
    widget = make_widget(frame(DATA), selection="multiple")
    show(widget, rows=[3, 1], selection=[0, 4])
    viewed = widget.view()
    assert isinstance(viewed, type(frame(DATA)))
    assert chars(viewed) == ["durian", "banana"]
    assert chars(widget.view(selected=True)) == ["apricot", "fig"]
    with pytest.raises(TypeError, match="`selected=`"):
        widget.view(selected="yes")  # type: ignore[arg-type]


def test_on_change_calls_back():
    widget = make_widget()
    calls = []

    def callback(w):
        calls.append(w)

    widget.on_change(callback)
    widget.on_change(callback)
    widget._on_msg(widget, {"type": "change"}, [])
    widget._on_msg(widget, {"type": "other"}, [])
    assert calls == [widget]
    widget.on_change(callback, remove=True)
    widget.on_change(callback, remove=True)
    widget._on_msg(widget, {"type": "change"}, [])
    assert calls == [widget]
    with pytest.raises(TypeError, match="callable"):
        widget.on_change(3)  # type: ignore[arg-type]


def test_needs_anywidget(monkeypatch):
    monkeypatch.setitem(sys.modules, "anywidget", None)
    monkeypatch.delitem(sys.modules, "great_tables._gti._widget")
    with pytest.raises(ImportError, match="pip install anywidget"):
        GTI(pd.DataFrame(DATA)).i_as_widget()
