"""Interactive tables in a Shiny app: `render_gt()`'s inputs and `update_gti()`.

The browser's side (packages/gti/src/shiny.ts) is tested with Vitest, and the two together in a
Shiny app (packages/gti/e2e/hosts.spec.ts).
"""

from __future__ import annotations

import asyncio
import json

import pandas as pd
import pytest

pytest.importorskip("shiny")

from shiny import App, ui  # noqa: E402
from shiny._connection import MockConnection  # noqa: E402
from shiny.input_handler import input_handlers  # noqa: E402
from shiny.session import session_context  # noqa: E402
from shiny.session._session import AppSession  # noqa: E402

from great_tables import GT, GTI  # noqa: E402
from great_tables._gti._state import (  # noqa: E402
    author_view,
    check_query_value,
    check_selection,
    check_sort,
    sort_names,
    view_of,
)
from great_tables._gti._render import render_gti_html_spec  # noqa: E402
from great_tables.shiny import MESSAGE, VIEW_TYPE, _SPECS, render_gt, update_gti  # noqa: E402

DATA = pd.DataFrame(
    {
        "char": ["apricot", "banana", "coconut", "durian", "fig"],
        "num": [3.0, 1.0, None, 5.0, 2.0],
        "fctr": ["one", "two", "one", "three", "two"],
    }
)

FILTER = {"and": [{"col": "fctr", "op": "in", "value": ["one", "two"]}]}


class Connection(MockConnection):
    """A connection that keeps the messages the server sends."""

    def __init__(self):
        super().__init__()
        self.sent: list[dict] = []

    async def send(self, message: str) -> None:
        self.sent.append(json.loads(message))


@pytest.fixture
def session():
    return AppSession(App(ui.page_fluid(), None), "session", Connection())


def custom(session: AppSession) -> list[dict]:
    """The custom messages sent so far, once the session's outputs are."""
    asyncio.run(session._flushed_callbacks.invoke())
    return [message["custom"] for message in session._conn.sent if "custom" in message]


def make_gti(selection=None) -> GTI:
    return GTI(DATA).i_cols_filter("fctr", type="facet").i_cols_filter("num").i_selection(selection)


def render(session, table, id: str = "table") -> dict:
    @render_gt
    def renderer():
        return table

    renderer._set_output_metadata(output_id=id)

    async def run():
        with session_context(session):
            return await renderer.render()

    return asyncio.run(run())


# The view, as Python reads it ----


def test_view_of_reads_query_and_sort():
    view = {
        "filter": FILTER,
        "sort": [{"column": "num", "descending": True}, {"column": "char", "descending": False}],
        "search": "an",
        "page": 2,
        "page_size": 10,
        "hidden": ["char"],
        "group_by": "fctr",
    }
    assert view_of(view) == {
        "query": 'fctr in ("one", "two")',
        "search": "an",
        "sort": ["-num", "char"],
        "page": 2,
        "page_size": 10,
        "hidden": ["char"],
        "group_by": "fctr",
    }
    assert view_of({}) == {
        "query": "",
        "search": "",
        "sort": [],
        "page": 1,
        "page_size": None,
        "hidden": [],
        "group_by": None,
    }


def test_sort_names():
    keys = [{"column": "a", "descending": True}, {"column": "b", "descending": False}]
    assert sort_names(keys) == ["-a", "b"]


def test_view_input_handler_is_registered(session):
    handler = input_handlers[VIEW_TYPE]
    assert handler({"filter": FILTER, "sort": []}, "table_view", session)["query"] == (
        'fctr in ("one", "two")'
    )


def test_author_view_is_first_view():
    _, spec = render_gti_html_spec(make_gti().i_view(sort="-num").i_pagination(page_size=2))
    view = author_view(spec)
    assert view["sort"] == [{"column": "num", "descending": True}]
    assert view["page"] == 1 and view["page_size"] == 2 and view["search"] == ""


# The checks, with or without a table's spec ----


def test_checks_without_spec_check_only_values():
    assert check_query_value(None, 'nope in ("a")', "`query=`") == {
        "and": [{"col": "nope", "op": "in", "value": ["a"]}]
    }
    assert check_sort(None, "-nope", "`sort=`") == [{"column": "nope", "descending": True}]
    assert check_selection(None, [9, 2, 9], "`selection=`") == [2, 9]
    with pytest.raises(ValueError, match="`query=`"):
        check_query_value(None, "fctr in (", "`query=`")
    with pytest.raises(TypeError, match="list of data rows"):
        check_selection(None, "1", "`selection=`")


def test_checks_with_spec():
    _, spec = render_gti_html_spec(make_gti("single"))
    with pytest.raises(ValueError, match="nope"):
        check_query_value(spec, 'nope in ("a")', "`query=`")
    with pytest.raises(ValueError, match="`sort=` can't sort the table by column 'nope'"):
        check_sort(spec, "nope", "`sort=`")
    with pytest.raises(ValueError, match="has 5 rows"):
        check_selection(spec, [5], "`selection=`")
    with pytest.raises(ValueError, match="Only one"):
        check_selection(spec, [1, 2], "`selection=`")


# render_gt() ----


@pytest.mark.parametrize(
    "table",
    [make_gti(), GT(DATA).opt_interactive()],
    ids=["GTI", "GT-opt_interactive"],
)
def test_render_gt_gives_glue_and_keeps_spec(session, table):
    rendered = render(session, table)
    assert [dep["name"] for dep in rendered["deps"]] == ["great-tables-gti-shiny"]
    assert "<gt-table" in rendered["html"]
    assert _SPECS[session]["table"]["nrows"] == 5


def test_render_gt_in_module_keeps_spec_by_namespaced_id(session):
    render(session.make_scope("mod"), make_gti())
    assert list(_SPECS[session]) == ["mod-table"]


def test_render_gt_static_table_has_no_glue(session):
    rendered = render(session, GT(DATA))
    assert rendered["deps"] == []
    assert "<gt-table" not in rendered["html"]
    assert session not in _SPECS


# update_gti() ----


def test_update_gti_sends_after_flush(session):
    render(session, make_gti("multiple"))
    with session_context(session):
        update_gti(
            "table", query='fctr in ("one", "two")', search="an", sort="-num", selection=[3, 0]
        )
    # (Nothing's sent until the session's outputs are)
    assert session._conn.sent == []
    assert custom(session) == [
        {
            MESSAGE: {
                "id": "table",
                "view": {
                    "filter": FILTER,
                    "search": "an",
                    "sort": [{"column": "num", "descending": True}],
                },
                "selection": [0, 3],
            }
        }
    ]
    # (Sent once)
    assert len(custom(session)) == 1


def test_update_gti_sends_only_whats_given(session):
    with session_context(session):
        update_gti("table", search="")
        update_gti("table", sort=[], query="")
    assert custom(session) == [
        {MESSAGE: {"id": "table", "view": {"search": ""}}},
        {MESSAGE: {"id": "table", "view": {"sort": [], "filter": None}}},
    ]


def test_update_gti_with_nothing_sends_nothing(session):
    with session_context(session):
        update_gti("table")
    assert custom(session) == []


def test_update_gti_in_module_uses_namespaced_id(session):
    scope = session.make_scope("mod")
    with session_context(scope):
        update_gti("table", selection=[1])
    assert custom(session) == [{MESSAGE: {"id": "mod-table", "selection": [1]}}]


def test_update_gti_takes_session(session):
    update_gti("table", search="an", session=session)
    assert custom(session) == [{MESSAGE: {"id": "table", "view": {"search": "an"}}}]


def test_update_gti_checks_against_rendered_table(session):
    render(session, make_gti())
    with session_context(session):
        with pytest.raises(ValueError, match="nope"):
            update_gti("table", query='nope in ("a")')
        with pytest.raises(ValueError, match="`sort=`"):
            update_gti("table", sort="nope")
        with pytest.raises(ValueError, match="i_selection"):
            update_gti("table", selection=[1])
        with pytest.raises(TypeError, match="`search=`"):
            update_gti("table", search=3)  # type: ignore[arg-type]
    assert custom(session) == []


def test_update_gti_without_rendered_table_checks_values(session):
    with session_context(session):
        # (Its columns aren't known, but the query must still be one)
        update_gti("other", sort="nope", selection=[7])
        with pytest.raises(ValueError, match="`query=`"):
            update_gti("other", query="fctr in (")
        with pytest.raises(ValueError, match="whole numbers"):
            update_gti("other", selection=[-1])
    assert custom(session) == [
        {
            MESSAGE: {
                "id": "other",
                "view": {"sort": [{"column": "nope", "descending": False}]},
                "selection": [7],
            }
        }
    ]


def test_update_gti_needs_session():
    with pytest.raises(RuntimeError):
        update_gti("table", search="an")
