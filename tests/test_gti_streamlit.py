"""Interactive tables in a Streamlit app: `st_gti()` and `update_gti()`.

The apps are run with Streamlit's `AppTest`, the browser's reports (as packages/gti/src/streamlit.ts
makes them) set in the component's state, as the browser sets it, and what the component's given
read from its element. The two together are tested in a Streamlit app
(packages/gti/e2e/hosts.spec.ts).
"""

from __future__ import annotations

import json
from typing import Any

import pytest

pytest.importorskip("streamlit")

from streamlit.testing.v1 import AppTest  # noqa: E402

from great_tables.streamlit import _SESSION_KEY  # noqa: E402

FILTER = {"and": [{"col": "fctr", "op": "in", "value": ["one", "two"]}]}


def app(kind: str = "gti", on_change: str = "rerun") -> None:
    # (An app showing a table, and its state, with buttons that change it with `update_gti()`)
    import json

    import pandas as pd
    import streamlit as st

    from great_tables import GT, GTI
    from great_tables.streamlit import st_gti, update_gti

    data = pd.DataFrame(
        {
            "char": ["apricot", "banana", "coconut", "durian", "fig"],
            "num": [3.0, 1.0, None, 5.0, 2.0],
            "fctr": ["one", "two", "one", "three", "two"],
        }
    )
    st.session_state.setdefault("changes", 0)

    def changed():
        st.session_state.changes += 1

    st.button(
        "Update",
        key="update",
        on_click=update_gti,
        args=("table",),
        kwargs={"query": 'fctr in ("one", "two")', "sort": "-num", "selection": [0]},
    )
    st.button("Search", key="search", on_click=update_gti, args=("table",), kwargs={"search": "an"})
    if kind == "gti":
        table = GTI(data).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")
    elif kind == "gti_id":
        table = GTI(data, id="mine").i_selection("multiple")
    elif kind == "gt":
        table = GT(data).opt_interactive(use_search=True)
    else:
        big = pd.DataFrame(
            {"n": range(50), "kind": ["odd" if i % 2 else "even" for i in range(50)]}
        )
        table = GTI(big).i_cols_filter(columns="kind", type="facet").i_scale(engine="kernel")
    state = st_gti(table, key="table", on_change=changed if on_change == "callable" else on_change)
    st.text(json.dumps([state.query, state.search, state.sort, state.rows, state.selection]))


def run(**kwargs: Any) -> AppTest:
    at = AppTest.from_function(app, kwargs=kwargs, default_timeout=30).run()
    assert not at.exception
    return at


def state(at: AppTest) -> list[Any]:
    return json.loads(at.text[0].value)


def data(at: AppTest) -> dict[str, Any]:
    # What the component's given (by the last run)
    return json.loads(at.get("bidi_component")[0].proto.json)


def shown(at: AppTest) -> Any:
    return at.session_state[_SESSION_KEY].tables["table"]


def report(at: AppTest, id: str, asks: list[dict[str, Any]] | None = None, **parts: Any) -> AppTest:
    # The browser's report of the table's state (its known one, with these parts), and its asks,
    # in the component's state, then the run it makes
    known = shown(at).known
    reported = {
        "view": {**known["view"], **parts.pop("view", {})},
        "rows": parts.pop("rows", known["rows"]),
        "selection": parts.pop("selection", known["selection"]),
    }
    at.session_state["table"] = {
        "gti": {"token": shown(at).token, "report": id, "state": reported, "asks": asks or []}
    }
    at.run()
    assert not at.exception
    return at


def test_st_gti_first_state():
    at = run()
    assert state(at) == ["", "", [], [0, 1, 2, 3, 4], []]
    given = data(at)
    assert given["html"].startswith("<gt-table")
    assert given["kernel"] is False
    assert given["nrows"] == 5
    assert given["report"] is True
    assert given["view"] == {"filter": None, "sort": [], "search": ""}
    assert given["update"] is None


def test_st_gti_gt_table_rows_not_known():
    # (A GT table's rows aren't Python's to find)
    at = run(kind="gt")
    assert state(at) == ["", "", [], None, []]
    at = report(at, "a", view={"search": "an"}, rows=[1, 3])
    assert state(at) == ["", "an", [], [1, 3], []]


def test_st_gti_takes_report():
    at = run()
    at = report(at, "a", view={"search": "an"}, rows=[1, 3], selection=[1])
    assert state(at) == ["", "an", [], [1, 3], [1]]
    assert data(at)["known"]["selection"] == [1]


def test_st_gti_keeps_view_of_table_made_again():
    # (The table's made again on each run, and rendered the same, with an id of its key's)
    at = run()
    token = shown(at).token
    at = report(at, "a", view={"search": "an"}, rows=[1, 3])
    at.run()
    assert shown(at).token == token
    assert state(at) == ["", "an", [], [1, 3], []]
    assert 'id="gti-' in data(at)["html"]


def test_st_gti_keeps_kernel_table_made_again():
    # (With the rows in Python as they are now)
    at = run(kind="kernel")
    table = shown(at)
    engine = table.engine
    at.run()
    assert shown(at) is table
    assert table.engine is not engine


def test_st_gti_table_own_id():
    at = run(kind="gti_id")
    assert 'id="mine"' in data(at)["html"]


def test_st_gti_ignores_other_tables_report():
    at = run()
    at.session_state["table"] = {
        "gti": {"token": shown(at).token + 1, "report": "a", "state": {}, "asks": []}
    }
    at.run()
    assert state(at) == ["", "", [], [0, 1, 2, 3, 4], []]


def test_st_gti_takes_report_once():
    # (The report, sent again with an ask after `update_gti()`, doesn't undo its change)
    at = run()
    at = report(at, "a", view={"search": "an"}, rows=[1, 3])
    at.button(key="update").click().run()
    assert state(at) == ['fctr in ("one", "two")', "an", ["-num"], None, [0]]
    view = {**shown(at).known["view"], "filter": None, "sort": [], "search": "an"}
    value = {"view": view, "rows": [1, 3], "selection": []}
    ask = {"id": "x:1", "kind": "page"}
    at.session_state["table"] = {
        "gti": {"token": shown(at).token, "report": "a", "state": value, "asks": [ask]}
    }
    at.run()
    assert state(at) == ['fctr in ("one", "two")', "an", ["-num"], None, [0]]

    # (But a new report, of the same state as before, is taken)
    at = report(
        at, "b", view={"filter": None, "sort": [], "search": "an"}, rows=[1, 3], selection=[]
    )
    assert state(at) == ["", "an", [], [1, 3], []]


def test_update_gti():
    at = run()
    at.button(key="update").click().run()
    assert state(at) == ['fctr in ("one", "two")', "", ["-num"], [0, 4, 1, 2], [0]]
    update = data(at)["update"]
    assert update["view"] == {"filter": FILTER, "sort": [{"column": "num", "descending": True}]}
    assert update["selection"] == [0]
    nonce = update["nonce"]

    # (The change is given once more, by the same number, until there's another)
    at.run()
    assert data(at)["update"]["nonce"] == nonce
    at.button(key="search").click().run()
    assert data(at)["update"] == {"nonce": nonce + 1, "view": {"search": "an"}}
    # (The rows a search keeps are the browser's to find)
    assert state(at)[3] is None


def test_update_gti_kernel_finds_rows():
    at = run(kind="kernel")
    assert state(at)[3] == list(range(50))
    at.button(key="search").click().run()
    assert state(at)[1:4] == ["an", [], []]


def test_update_gti_checks():
    from great_tables.streamlit import update_gti

    at = run()
    session = at.session_state[_SESSION_KEY]
    import streamlit as st

    st.session_state[_SESSION_KEY] = session
    try:
        with pytest.raises(ValueError, match="can't sort the table by column 'nope'"):
            update_gti("table", sort="nope")
        with pytest.raises(ValueError, match="has row 9"):
            update_gti("table", selection=[9])
        with pytest.raises(TypeError, match="`search=` must be a string"):
            update_gti("table", search=1)
        with pytest.raises(TypeError, match="`key` must be a nonempty string"):
            update_gti("")
        # (Merged with the change made before, the later's parts winning)
        update_gti("table", search="an", sort="num")
        update_gti("table", sort="-num")
        assert session.pending["table"] == {
            "view": {"search": "an", "sort": [{"column": "num", "descending": True}]}
        }
    finally:
        del st.session_state[_SESSION_KEY]


def test_st_gti_kernel_answers_asks():
    at = run(kind="kernel")
    assert data(at)["kernel"] is True
    query = {"search": "", "hidden": [], "filter": None, "links": [], "sort": [], "start": 10}
    ask = {"id": "v:1", "kind": "page", "query": {**query, "size": 5}}
    at = report(at, "a", asks=[ask, {"id": "v:2", "kind": "nope"}])
    answers = data(at)["answers"]
    assert answers["v:1"]["answer"]["rows"] == list(range(10, 15))
    assert "error" in answers["v:2"]
    # (Each is answered once, and those no longer asked aren't kept)
    assert set(shown(at).answers) == {"v:1", "v:2"}
    at = report(at, "a", asks=[ask])
    assert set(data(at)["answers"]) == {"v:1"}
    assert set(shown(at).answers) == {"v:1"}


def test_st_gti_kernel_finds_reported_view():
    at = run(kind="kernel")
    at = report(at, "a", view={"filter": {"and": [{"col": "kind", "op": "in", "value": ["odd"]}]}})
    assert state(at)[3] == list(range(1, 50, 2))
    # (Nor a view it can't have)
    at = report(at, "b", view={"filter": {"and": [{"col": "nope", "op": "in", "value": [1]}]}})
    assert state(at)[3] == []


def test_st_gti_on_change():
    # (`AppTest` doesn't call the component's callback, so this is what it calls `on_change` for:
    # a report not taken before, of a state other than the one known)
    from great_tables.streamlit import _changed

    at = run(on_change="callable")
    assert at.session_state["changes"] == 0
    table = shown(at)
    known = table.known

    def value(report: str, token: int = table.token, **parts: Any) -> dict[str, Any]:
        return {"gti": {"token": token, "report": report, "state": {**known, **parts}}}

    assert _changed(table, value("a", selection=[2]))
    assert not _changed(table, value("a"))
    assert not _changed(table, value("a", token=table.token + 1, selection=[2]))
    assert not _changed(table, None)
    at = report(at, "a", selection=[2])
    assert state(at)[4] == [2]
    assert not _changed(table, value("a", selection=[3]))
    assert _changed(table, value("b", selection=[3]))


def test_st_gti_ignore():
    at = run(on_change="ignore")
    assert data(at)["report"] is False


@pytest.mark.parametrize(
    "kwargs, error, match",
    [
        ({"table": 1}, TypeError, "`table` must be a `GTI` or a `GT` table"),
        ({"static": True}, TypeError, "show a static one with `st.html"),
        ({"key": ""}, TypeError, "`key` must be a nonempty string"),
        ({"on_change": "now"}, ValueError, "`on_change` must be"),
    ],
)
def test_st_gti_checks(kwargs: dict[str, Any], error: type[Exception], match: str):
    def bad(table=None, static=False, key="table", on_change="rerun"):
        import pandas as pd

        from great_tables import GT, GTI
        from great_tables.streamlit import st_gti

        data = pd.DataFrame({"x": [1, 2]})
        if table is None:
            table = GT(data) if static else GTI(data)
        st_gti(table, key=key, on_change=on_change)

    at = AppTest.from_function(bad, kwargs=kwargs, default_timeout=30).run()
    assert len(at.exception) == 1
    assert at.exception[0].proto.type == error.__name__
    assert match in at.exception[0].message
