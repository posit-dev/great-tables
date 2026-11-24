"""Interactive tables in a marimo notebook: `mo_gti()`.

The browser's changes are given to the element as marimo gives them (`_update()`, with the state
packages/gti/src/widget.ts writes). The two together, with marimo's kernel, are tested in marimo
notebooks (packages/gti/e2e/hosts.spec.ts).
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

import pandas as pd
import pytest

mo = pytest.importorskip("marimo")

import great_tables.marimo as gt_marimo  # noqa: E402
from great_tables import GT, GTI  # noqa: E402
from great_tables._gti._widget import GTIWidget  # noqa: E402
from great_tables.marimo import GTIElement, mo_gti  # noqa: E402

DATA = pd.DataFrame(
    {
        "char": ["apricot", "banana", "coconut", "durian", "fig"],
        "num": [3.0, 1.0, None, 5.0, 2.0],
        "fctr": ["one", "two", "one", "three", "two"],
    }
)

VIEW = {
    "filter": None,
    "sort": [],
    "search": "",
    "page": 1,
    "page_size": None,
    "hidden": [],
    "group_by": None,
}

ONE_TWO = 'fctr in ("one", "two")'


def make_gti(data: pd.DataFrame = DATA) -> GTI:
    return GTI(data).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")


def show(element: GTIElement, **view: Any) -> None:
    # (As marimo gives the element the browser's changes)
    rows = view.pop("rows")
    selection = view.pop("selection", element.selection)
    element._update({"_view": {**VIEW, **view}, "_rows": rows, "_selection": selection})


def state(**parts: Any) -> dict[str, Any]:
    return {"query": "", "search": "", "sort": [], "rows": None, "selection": [], **parts}


def test_element_is_the_tables_widget():
    table = mo_gti(make_gti().i_view(filter='fctr in ("one")', sort="-num"))
    assert isinstance(table, mo.ui.anywidget) and isinstance(table.widget, GTIWidget)
    assert table.widget._html.startswith("<gt-table")
    # (Its value is the table's state, as the author made it, with the rows Python finds)
    assert table.value == state(query='fctr in ("one")', sort=["-num"], rows=[0, 2])


def test_reader_sets_the_value():
    table = mo_gti(make_gti())
    show(table, search="an", rows=[1, 3])
    assert table.value == state(search="an", rows=[1, 3])
    show(
        table,
        search="",
        filter={"and": [{"col": "fctr", "op": "in", "value": ["one", "two"]}]},
        rows=[0, 1, 2, 4],
        selection=[4],
    )
    assert table.value == state(query=ONE_TWO, rows=[0, 1, 2, 4], selection=[4])
    assert table.view(selected=True)["char"].tolist() == ["fig"]
    assert table.view()["char"].tolist() == ["apricot", "banana", "coconut", "fig"]


def test_notebook_sets_the_table(monkeypatch: pytest.MonkeyPatch):
    told: list[str] = []
    monkeypatch.setattr(gt_marimo, "_run_readers", lambda element: told.append("told"))
    table = mo_gti(make_gti())
    show(table, rows=[0, 1, 2, 3, 4])
    # (Set on the widget, which the browser applies, and whose rows it then writes)
    table.query = ONE_TWO
    table.sort = "-num"
    assert table.widget.query == ONE_TWO and table.widget.sort == ["-num"]
    assert table.value["rows"] is None
    # (Its rows, the browser tells marimo of, so marimo needn't be told here; of a selection, it is)
    assert told == []
    table.selection = [0, 4]
    assert table.widget.selection == [0, 4] and told == ["told"]


def test_kernel_mode_rows_are_pythons(monkeypatch: pytest.MonkeyPatch):
    told: list[str] = []
    monkeypatch.setattr(gt_marimo, "_run_readers", lambda element: told.append("told"))
    table = mo_gti(make_gti().i_scale(engine="kernel"))
    assert table.value["rows"] == [0, 1, 2, 3, 4]
    # (Found in Python at once, so marimo is told of each change made here)
    table.query = ONE_TWO
    table.sort = "-num"
    assert table.value == state(query=ONE_TWO, sort=["-num"], rows=[0, 4, 1, 2])
    assert told == ["told", "told"]


def test_readers_are_left_alone_outside_a_kernel():
    # (As when the notebook is run as a script, or the table is used outside marimo)
    table = mo_gti(make_gti().i_scale(engine="kernel"))
    table.sort = "num"
    assert table.value["rows"] == [1, 4, 0, 3, 2]


def test_value_cant_be_set():
    table = mo_gti(make_gti())
    with pytest.raises(RuntimeError, match="set the table's `query`"):
        table.value = {}


def test_copy_is_a_new_widget_with_the_tables_state():
    table = mo_gti(make_gti())
    show(table, sort=[{"column": "num", "descending": True}], rows=[3, 0, 4, 1, 2], selection=[1])
    copy = deepcopy(table)
    assert isinstance(copy, GTIElement)
    assert copy.widget is not table.widget and copy._id != table._id
    assert copy.widget._html == table.widget._html
    assert copy.sort == ["-num"] and copy.selection == [1]


def test_element_in_another():
    # (marimo copies an element put in another, whose value has the copy's)
    tables = mo.ui.array([mo_gti(make_gti())])
    assert tables.value == [state(rows=[0, 1, 2, 3, 4])]
    # (A change to the table is given to the array, as marimo gives it)
    tables._update({"0": {"_view": {**VIEW, "search": "an"}, "_rows": [1, 3], "_selection": []}})
    assert tables.value == [state(search="an", rows=[1, 3])]


def test_opt_interactive_table():
    table = mo_gti(GT(DATA).opt_interactive(use_search=True))
    assert table.widget._html.startswith("<gt-table")
    # (Its rows are the browser's, until it has shown the table)
    assert table.value == state()
    show(table, sort=[{"column": "num", "descending": False}], rows=[1, 4, 0, 3, 2])
    assert table.value == state(sort=["num"], rows=[1, 4, 0, 3, 2])


@pytest.mark.parametrize("table", [GT(DATA), DATA])
def test_needs_an_interactive_table(table: Any):
    with pytest.raises(TypeError, match="interactive tables|`table` must be"):
        mo_gti(table)
