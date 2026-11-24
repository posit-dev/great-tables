"""Interactive tables in a Streamlit app: `st_gti()` shows one, and gives its view, rows and
selection, which `update_gti()` changes.

The table is a component (Streamlit's `st.components.v2`), whose glue (packages/gti/src/streamlit.ts,
run after the runtime) shows the table's element and reports its state, which runs the app's
script again; and each run gives the component its data again: the element, the state Python has
for the table (as last reported, or as `update_gti()` changed it), and for a table whose rows are
Python's (in kernel mode, see `_gti/_kernel.py`), the answers to what it asks for them (a page, or a
facet's counts), which it asks for in its state.

Each table, by its key, is kept in the session's state (`_SESSION_KEY`), with its rendering, so
that a run given the same table (the same object, as `st.cache_resource` gives it) doesn't render
it again, and one given a table rendered the same keeps its view (a table without an id is given
one of its key's, so that it is).
"""

from __future__ import annotations

__all__ = (
    "GTIState",
    "st_gti",
    "update_gti",
)

import hashlib
import json
from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from functools import cache
from typing import TYPE_CHECKING, Any, Literal

try:
    import streamlit as st
    from streamlit.components.v2 import component
except ImportError:
    raise ImportError(
        "The great_tables.streamlit module requires the streamlit package to be installed."
        " Please install it with this command:"
        "\n\n    pip install streamlit"
    )

from ._gti._kernel import KernelEngine, render_table
from ._gti._render import JS_DIR, _load_runtime, render_gti_element
from ._gti._state import (
    author_view,
    check_query_value,
    check_search,
    check_selection,
    check_sort,
    python_rows,
    view_of,
)
from ._render import infer_render_env_defaults
from .gt import GT

if TYPE_CHECKING:
    from ._gti._spec import Spec

# (Where the session's tables are kept, in its state)
_SESSION_KEY = "_great_tables_gti"

# (The component's state, as src/streamlit.ts sets it)
_STATE = "gti"


@cache
def _sources() -> tuple[str, str]:
    # The component's module (the runtime, then the glue, which only uses what the runtime
    # defines) and CSS
    js, css = _load_runtime()
    return js + (JS_DIR / "gti-streamlit.js").read_text(encoding="utf-8"), css


def _component() -> Callable[..., Any]:
    # The component, declared with each run (as Streamlit's runtime, which registers it, may be
    # another one's), not in a shadow root, as the runtime's CSS is the page's
    js, css = _sources()
    return component("great_tables.gti", js=js, css=css, isolate_styles=False)


@dataclass
class _Shown:
    """A table, as last rendered for its key, and what Python has of its state."""

    table: GT
    html: str
    spec: Spec
    engine: KernelEngine | None
    # (Each table rendered has its own, so that what's reported of another is left)
    token: int
    # (The view, rows and selection, as the browser gives them: the rows are `None` where the
    # browser doesn't give them, Python finding them, or where they aren't known yet)
    known: dict[str, Any]
    # (The rows, as Python found them for the view, with the rows in Python)
    found: list[int] | None = None
    # (The id of the state last reported: it's in the component's state, sent again with each ask
    # after it, and taken once, as a change `update_gti()` made since is newer)
    taken: str | None = None
    # (The last change `update_gti()` made, with its number)
    update: dict[str, Any] | None = None
    # (The answers given to the asks in the table's state, by id)
    answers: dict[str, dict[str, Any]] = field(default_factory=dict)


@dataclass
class _Session:
    tables: dict[str, _Shown] = field(default_factory=dict)
    # (The changes `update_gti()` made, for a table's next `st_gti()`)
    pending: dict[str, dict[str, Any]] = field(default_factory=dict)
    tokens: int = 0
    nonces: int = 0


def _session() -> _Session:
    session = st.session_state.get(_SESSION_KEY)
    if not isinstance(session, _Session):
        session = _Session()
        st.session_state[_SESSION_KEY] = session
    return session


@dataclass(frozen=True)
class GTIState:
    """
    An interactive table's state in a Streamlit app, as [`st_gti()`](`great_tables.streamlit.st_gti`)
    gives it.

    Attributes
    ----------
    view
        The table's view: a dict with its filters as a query in text (`"query"`), its `"search"`,
        its `"sort"` (columns, with a `-` before those in descending order), its `"page"` and
        `"page_size"`, its `"hidden"` columns and the column its rows are grouped by
        (`"group_by"`).
    rows
        The data rows its search and filters keep (and linked tables' selections), in the order
        shown, on every page, numbered by position in the data (from 0); or `None` until the
        browser has found them (when the app is run again).
    selection
        The data rows selected, in data order.
    """

    view: dict[str, Any]
    rows: list[int] | None
    selection: list[int]

    @property
    def query(self) -> str:
        """The table's filters, as a query in text (`""` without any)."""
        return self.view["query"]

    @property
    def search(self) -> str:
        """The table's search (`""` without one)."""
        return self.view["search"]

    @property
    def sort(self) -> list[str]:
        """The table's sort: its columns, each with a `-` before it if it's in descending order."""
        return self.view["sort"]


def st_gti(
    table: GT,
    *,
    key: str,
    on_change: Literal["rerun", "ignore"] | Callable[[], Any] = "rerun",
) -> GTIState:
    """
    Show an interactive table in a Streamlit app, and get its state.

    The table (a `GTI` table, or a `GT` table with `opt_interactive()`) is shown as a component,
    and its state is given back: its view, the rows the view keeps, and those selected (see
    [`GTIState`](`great_tables.streamlit.GTIState`)). Each change the reader makes to them (a
    search, a filter, a sort, a selection, ...) runs the app again, and the table's state is then
    what the reader made it. [`update_gti()`](`great_tables.streamlit.update_gti`) changes it
    from the app.

    A `GTI` table with more rows than the browser is quick with keeps them in Python instead (see
    [`i_scale()`](`great_tables.GTI.i_scale`)), and sends the browser a page at a time: the
    browser asks for each one (and for a filter's counts) by running the app again, which answers.
    Then the rows its view keeps are found in Python (without linked tables' selections). Such a
    table is best made once, with `st.cache_resource`: a table the app makes again on each run is
    rendered again each time (which, with many rows in a DataFrame, takes a while).

    Parameters
    ----------
    table
        The table to show: a `GTI` table, or a `GT` table with `opt_interactive()`.
    key
        The table's key, unique in the app: the table keeps its view and selection by it (when
        it's made again on each run, but rendered the same), and `update_gti()` changes it.
    on_change
        What a change the reader makes does: run the app again (`"rerun"`, the default); not, so
        that the table's state is only what the app made it (`"ignore"`); or call a function (with
        no arguments), and run the app again. A table whose rows are in Python runs the app again
        for each page all the same.

    Returns
    -------
    GTIState
        The table's state: its view, the rows the view keeps, and those selected. Until it's
        shown, as it's first shown (its rows as Python finds them); once it's shown, as the
        browser last gave it.

    Examples
    --------
    ```python
    import streamlit as st
    from great_tables import GTI, exibble
    from great_tables.streamlit import st_gti

    table = GTI(exibble).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")
    state = st_gti(table, key="table")

    st.write(f"{len(state.rows or [])} rows, filtered by {state.query!r}")
    st.dataframe(exibble.iloc[state.selection])
    ```
    """
    from .gti import GTI

    if not isinstance(table, GT):
        raise TypeError(f"`table` must be a `GTI` or a `GT` table, not {table!r}.")
    if not isinstance(table, GTI) and not table._options.ihtml_active.value:
        raise TypeError(
            "`st_gti()` shows interactive tables (a `GTI` table, or a `GT` table with "
            "`opt_interactive()`); show a static one with `st.html(table.as_raw_html())`."
        )
    if not isinstance(key, str) or key == "":
        raise TypeError(f"`key` must be a nonempty string, not {key!r}.")
    if on_change not in ("rerun", "ignore") and not callable(on_change):
        raise ValueError(f'`on_change` must be "rerun", "ignore" or a function, not {on_change!r}.')

    session = _session()
    shown = _shown(session, key, table)
    asks = _reported(shown, st.session_state.get(key))
    update = session.pending.pop(key, None)
    if update is not None:
        _updated(session, shown, update)

    def changed() -> None:
        # (A change to the table's state the reader made, rather than an ask for its rows)
        if callable(on_change) and _changed(shown, st.session_state.get(key)):
            on_change()

    known = shown.known
    _component()(
        key=key,
        data={
            "html": shown.html,
            "token": shown.token,
            "kernel": shown.engine is not None,
            "nrows": shown.spec["nrows"],
            "report": on_change != "ignore",
            "view": {part: known["view"][part] for part in ("filter", "sort", "search")},
            "selection": known["selection"],
            "known": known,
            "update": shown.update,
            "answers": _answers(shown, asks),
        },
        on_gti_change=changed,
    )
    rows = shown.found if shown.engine is not None else known["rows"]
    return GTIState(
        view=view_of(known["view"]),
        rows=None if rows is None else list(rows),
        selection=list(known["selection"]),
    )


def _shown(session: _Session, key: str, table: GT) -> _Shown:
    # The table, as rendered for its key: again, unless it's the same table (and kept if it's
    # rendered the same)
    from .gti import GTI

    shown = session.tables.get(key)
    if shown is not None and shown.table is table:
        return shown
    all_important = infer_render_env_defaults()["all_important"]
    # (A table without an id is given one of its key's, so that it's rendered the same each time)
    rendered = table
    if table._options.table_id.value is None:
        rendered = table.with_id(f"gti-{hashlib.sha256(key.encode()).hexdigest()[:12]}")
    engine = None
    if isinstance(rendered, GTI):
        html, spec, engine = render_table(rendered, all_important=all_important)
    else:
        html, spec = render_gti_element(rendered, all_important=all_important)
    # (One rendered the same is the same table, with the rows in Python as they are now)
    if shown is not None and html == shown.html and (engine is None) == (shown.engine is None):
        shown.table = table
        shown.spec = spec
        if engine is not None:
            shown.engine = engine
            _find(shown)
        return shown

    session.tokens += 1
    view = author_view(spec)
    shown = _Shown(
        table=table,
        html=html,
        spec=spec,
        engine=engine,
        token=session.tokens,
        known={"view": view, "rows": None, "selection": []},
    )
    _find(shown)
    session.tables[key] = shown
    return shown


def _find(shown: _Shown) -> None:
    # The rows the known view keeps, as Python finds them: with the rows in Python, always; with
    # them in the browser, where it can (a `GTI` table, without a search), else they're not known
    # until the browser gives them
    from .gti import GTI

    view = shown.known["view"]
    if shown.engine is not None:
        # (A view the table doesn't have keeps none, rather than stopping the app)
        try:
            shown.found = shown.engine.find({**view, "links": []})
        except (TypeError, ValueError):
            shown.found = []
    elif isinstance(shown.table, GTI) and view["search"] == "":
        shown.known["rows"] = python_rows(shown.table, shown.spec, view)
    else:
        shown.known["rows"] = None


def _value(state: Any) -> dict[str, Any] | None:
    # The component's state, as the glue set it (in the session's state, by the table's key)
    if isinstance(state, Mapping):
        value = state.get(_STATE)
        if isinstance(value, Mapping):
            return dict(value)
    return None


def _reported(shown: _Shown, state: Any) -> list[dict[str, Any]]:
    # Take the table's state as the browser last reported it (if it's of this table, and newer
    # than what's known), and give the asks for its rows waiting on an answer
    value = _value(state)
    if value is None or value.get("token") != shown.token:
        return []
    reported = value.get("state")
    if _changed(shown, state):
        shown.taken = value.get("report")
        if isinstance(reported.get("view"), Mapping) and isinstance(
            reported.get("selection"), list
        ):
            rows = reported.get("rows")
            shown.known = {
                "view": {**author_view(shown.spec), **reported["view"]},
                "rows": rows if isinstance(rows, list) else None,
                "selection": reported["selection"],
            }
            if shown.engine is not None:
                _find(shown)
    asks = value.get("asks")
    return [ask for ask in asks if isinstance(ask, dict)] if isinstance(asks, list) else []


def _changed(shown: _Shown, state: Any) -> bool:
    # Whether the browser has reported a state of the table not taken before, other than the one
    # known
    value = _value(state)
    if value is None or value.get("token") != shown.token:
        return False
    reported = value.get("state")
    return (
        isinstance(reported, Mapping)
        and value.get("report") != shown.taken
        and _canonical(reported) != _canonical(shown.known)
    )


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, default=str)


def _updated(session: _Session, shown: _Shown, update: dict[str, Any]) -> None:
    # A change `update_gti()` made: known at once (with the first page), and set on the table
    # once, by its number
    session.nonces += 1
    shown.update = {"nonce": session.nonces, **update}
    view = {**shown.known["view"], **update.get("view", {})}
    if "view" in update:
        view["page"] = 1
    selection = update.get("selection", shown.known["selection"])
    # (A selection alone keeps the rows)
    shown.known = {"view": view, "rows": shown.known["rows"], "selection": selection}
    if "view" in update:
        _find(shown)


def _answers(shown: _Shown, asks: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    # The answers to the asks for the table's rows waiting on one (each answered once), as the
    # glue takes them (an error is the browser's to log, as it does a source's)
    if shown.engine is None:
        return {}
    answers: dict[str, dict[str, Any]] = {}
    for ask in asks:
        id = ask.get("id")
        if not isinstance(id, str):
            continue
        if id not in shown.answers:
            try:
                shown.answers[id] = {"answer": shown.engine.answer(ask)}
            except Exception as err:  # noqa: BLE001
                shown.answers[id] = {"error": str(err)}
        answers[id] = shown.answers[id]
    # (Those no longer asked for aren't kept)
    shown.answers = dict(answers)
    return answers


def update_gti(
    key: str,
    *,
    query: str | dict[str, Any] | None = None,
    search: str | None = None,
    sort: str | list[str] | None = None,
    selection: list[int] | None = None,
) -> None:
    """
    Change an interactive table's view or selection, from a Streamlit app.

    The table (shown with [`st_gti()`](`great_tables.streamlit.st_gti`), with the same `key`) is
    filtered, searched, sorted, and has its rows selected, as if the reader had done it (so that a
    change to its filters, search or sort shows its first page). What isn't given (or is `None`)
    is left as it is. It's changed by the table's next `st_gti()`: so call `update_gti()` before
    it, as in a widget's callback (`on_click=` or `on_change=`), which is run before the app; one
    called after it is the next run's.

    Parameters
    ----------
    key
        The table's key.
    query
        The table's filters: a query in text (as the query box has it), or as
        [`i_view()`](`great_tables.GTI.i_view`)'s `filter=` takes it; `""` for none.
    search
        The table's search; `""` for none.
    sort
        The columns to sort the table by, most significant first, each with a `-` before it to
        sort it in descending order (e.g., `["-net", "store"]`), or one column; `[]` to leave it
        unsorted.
    selection
        The data rows to select (numbered by position in the data, from 0), and only those; `[]`
        for none. The table must let readers select rows (with
        [`i_selection()`](`great_tables.GTI.i_selection`)).

    Examples
    --------
    ```python
    import streamlit as st
    from great_tables import GTI, exibble
    from great_tables.streamlit import st_gti, update_gti

    st.button(
        "Largest first",
        on_click=update_gti,
        args=("table",),
        kwargs={"query": 'fctr in ("one", "two")', "sort": "-num"},
    )
    state = st_gti(GTI(exibble).i_cols_filter(columns="fctr", type="facet"), key="table")
    st.write(f"{len(state.rows or [])} rows, filtered by {state.query!r}")
    ```
    """
    if not isinstance(key, str) or key == "":
        raise TypeError(f"`key` must be a nonempty string, not {key!r}.")
    session = _session()
    # (Checked against the table as last rendered, if it has been)
    shown = session.tables.get(key)
    spec = shown.spec if shown is not None else None

    view: dict[str, Any] = {}
    if query is not None:
        view["filter"] = check_query_value(spec, query, "`query=`")
    if search is not None:
        view["search"] = check_search(search, "`search=`")
    if sort is not None:
        view["sort"] = check_sort(spec, sort, "`sort=`")
    update: dict[str, Any] = {}
    if view:
        update["view"] = view
    if selection is not None:
        update["selection"] = check_selection(spec, selection, "`selection=`")
    if not update:
        return
    # (Merged with one made before, the later's parts winning)
    before = session.pending.get(key, {})
    merged = {**before, **update}
    if "view" in before and "view" in update:
        merged["view"] = {**before["view"], **update["view"]}
    session.pending[key] = merged
