"""Interactive tables in a Panel app: `GTIPane`.

The browser's changes (as packages/gti/src/panel.ts reports them, which are the widget's) are set
on the pane's report, as Panel sets it, and the asks of a table whose rows are in Python
given to its message handler. The two together are tested in Panel apps
(packages/gti/e2e/hosts.spec.ts).
"""

from __future__ import annotations

from typing import Any

import pandas as pd
import pytest

pytest.importorskip("panel")

from great_tables import GT, GTI  # noqa: E402
from great_tables._gti._state import author_view  # noqa: E402
from great_tables.panel import GTIPane  # noqa: E402

DATA = pd.DataFrame(
    {
        "char": ["apricot", "banana", "coconut", "durian", "fig"],
        "num": [3.0, 1.0, None, 5.0, 2.0],
        "fctr": ["one", "two", "one", "three", "two"],
    }
)

FILTER = {"and": [{"col": "fctr", "op": "in", "value": ["one", "two"]}]}

QUERY = {"search": "", "hidden": [], "filter": None, "links": [], "sort": []}


def make_gti() -> GTI:
    return GTI(DATA).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")


def state(pane: GTIPane) -> list[Any]:
    return [pane.query, pane.search, pane.sort, pane.rows, pane.selection]


def report(pane: GTIPane, **changes: Any) -> None:
    # (As the browser reports the reader's changes)
    pane._report = {**changes, "n": pane._report.get("n", 0) + 1, "from": "view"}


def sent(pane: GTIPane) -> dict[str, Any]:
    # (The state the browser's sent, as it is once it's had each change)
    return pane._model


def big_pane() -> GTIPane:
    big = pd.DataFrame({"n": range(50), "kind": ["odd" if i % 2 else "even" for i in range(50)]})
    return GTIPane(GTI(big).i_cols_filter(columns="kind", type="facet").i_scale(engine="kernel"))


def test_pane_starts_with_the_authors_view():
    pane = GTIPane(make_gti().i_view(filter='fctr in ("one")', sort="-num"))
    assert state(pane) == ['fctr in ("one")', "", ["-num"], [0, 2], []]
    assert pane._update["_view"]["filter"] == {
        "and": [{"col": "fctr", "op": "in", "value": ["one"]}]
    }
    assert pane._update["n"] == 0 and pane._update["_selection"] == []
    assert pane._html.startswith("<gt-table") and not pane._kernel and pane._nrows == 5
    # (Without a `</`, which would end the script a notebook has it in)
    assert "</" not in pane._html and "<\x00/script>" in pane._html


def test_pane_takes_the_browsers_changes():
    pane = GTIPane(make_gti())
    seen = []
    pane.param.watch(lambda event: seen.append(event.name), ["rows", "search", "selection"])
    pane.param.watch(lambda event: seen.append(event.name), ["_update"])
    view = {**sent(pane)["_view"], "search": "an", "sort": [{"column": "char", "descending": True}]}
    report(pane, _view=view, _rows=[3, 1])
    assert state(pane) == ["", "an", ["-char"], [3, 1], []]
    report(pane, _selection=[3])
    assert pane.selection == [3]
    assert set(seen) == {"rows", "search", "selection"}
    # (Nothing's sent back to the browser, but the state's kept for a view made from now on)
    assert sent(pane) == {"_view": view, "_rows": [3, 1], "_selection": [3]}
    assert pane._update == {**sent(pane), "n": 0}


def test_pane_sets_the_view_and_selection():
    pane = GTIPane(make_gti())
    pane.param.update(query='fctr in ("one", "two")', sort=["-num"], selection=[0])
    view = {
        **author_view(pane._spec),
        "filter": FILTER,
        "sort": [{"column": "num", "descending": True}],
    }
    assert sent(pane) == {"_view": view, "_rows": None, "_selection": [0]}
    # (The state sent with each change, with a count: the view's, then the selection's)
    assert pane._update == {"_view": view, "_rows": None, "_selection": [0], "n": 2}
    # (Before it's shown, its rows are those Python finds)
    assert state(pane) == ['fctr in ("one", "two")', "", ["-num"], [0, 4, 1, 2], [0]]
    pane.search = "an"
    assert pane._update["_view"]["search"] == "an" and pane._update["_view"]["page"] == 1
    # (Which Python can't find with a search)
    assert pane.rows is None


def test_pane_rows_are_the_browsers_once_shown():
    pane = GTIPane(make_gti())
    pane.get_root()
    pane.sort = ["char"]
    assert sent(pane)["_rows"] is None and pane.rows is None
    report(pane, _rows=[0, 1, 2, 3, 4])
    assert pane.rows == [0, 1, 2, 3, 4]


@pytest.mark.parametrize(
    "name, value, message",
    [
        ("query", "nope in (1)", "nope"),
        ("sort", ["nope"], "nope"),
        ("selection", [99], "`selection`"),
    ],
)
def test_pane_puts_back_what_cant_be_set(name: str, value: Any, message: str):
    pane = GTIPane(make_gti())
    model = dict(sent(pane))
    with pytest.raises((TypeError, ValueError), match=message):
        setattr(pane, name, value)
    assert state(pane) == ["", "", [], [0, 1, 2, 3, 4], []]
    assert sent(pane) == model and pane._update["n"] == 0


def test_pane_gives_its_data():
    pane = GTIPane(make_gti())
    pane.param.update(sort=["-num"], selection=[1, 3])
    assert list(pane.data()["char"]) == ["durian", "apricot", "fig", "banana", "coconut"]
    assert list(pane.data(selected=True)["char"]) == ["banana", "durian"]
    pane.search = "an"
    with pytest.raises(RuntimeError, match="aren't known"):
        pane.data()
    with pytest.raises(TypeError, match="`selected=`"):
        pane.data(selected=1)  # type: ignore[arg-type]


def test_pane_of_an_opt_interactive_table():
    pane = GTIPane(GT(DATA).opt_interactive(use_search=True, use_filters=True))
    assert "<gt-table" in pane._html and pane._engine is None
    # (Its rows are the browser's)
    assert pane.rows is None
    pane.sort = ["-num"]
    assert pane._update["_view"]["sort"] == [{"column": "num", "descending": True}]
    assert pane.rows is None
    report(pane, _rows=[3, 0])
    assert list(pane.data()["char"]) == ["durian", "apricot"]


@pytest.mark.parametrize("table", [GT(DATA), DATA])
def test_pane_needs_an_interactive_table(table: Any):
    with pytest.raises(TypeError, match="`table`|interactive"):
        GTIPane(table)


def test_pane_in_kernel_mode():
    pane = big_pane()
    assert pane._kernel and pane._nrows == 50 and pane._engine is not None
    assert len(pane.rows) == 50
    pane.param.update(query='kind in ("odd")', sort=["-n"])
    assert pane.rows[:3] == [49, 47, 45]
    # (Even once shown, and with the browser's search)
    pane.get_root()
    report(pane, _view={**sent(pane)["_view"], "search": "33"})
    assert pane.rows == [33] and pane.search == "33"
    assert list(pane.data()["n"]) == [33]


def test_pane_answers_the_browsers_asks():
    pane = big_pane()
    sent: list[Any] = []
    pane._send_msg = sent.append  # type: ignore[method-assign]
    query = {**QUERY, "start": 10, "size": 10}
    pane._handle_msg({"type": "ask", "id": "v:1", "kind": "page", "query": query})
    assert sent[-1]["id"] == "v:1" and sent[-1]["answer"]["rows"] == list(range(10, 20))
    pane._handle_msg({"type": "ask", "id": "v:2", "kind": "facet", "query": QUERY, "column": "x"})
    assert sent[-1]["id"] == "v:2" and "no filter" in sent[-1]["error"]
    # (And nothing else)
    pane._handle_msg({"type": "change"})
    pane._handle_msg("ask")
    assert len(sent) == 2


def test_pane_in_browser_mode_ignores_asks():
    pane = GTIPane(make_gti())
    sent: list[Any] = []
    pane._send_msg = sent.append  # type: ignore[method-assign]
    pane._handle_msg({"type": "ask", "id": "v:1", "kind": "page", "query": QUERY})
    assert sent == []


def test_pane_shown_again_starts_with_its_state():
    pane = GTIPane(make_gti())
    first = pane.get_root()
    view = {**sent(pane)["_view"], "search": "an"}
    report(pane, _view=view, _rows=[1, 3], _selection=[3])
    # (Which isn't sent to the view there is)
    assert first.data._update["_selection"] == []
    pane.sort = ["-num"]
    model = pane.get_root()
    shown = {**view, "sort": [{"column": "num", "descending": True}]}
    assert model.data._update == {"_view": shown, "_rows": None, "_selection": [3], "n": 1}


def test_pane_keeps_the_public_parameters_in_python():
    pane = GTIPane(make_gti())
    model = pane.get_root()
    names = set(model.data.properties())
    assert {"_html", "_update", "_report", "_kernel", "_nrows"} <= names
    assert not names & {"query", "search", "sort", "rows", "selection"}
