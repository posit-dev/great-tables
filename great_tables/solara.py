"""Interactive tables in a Solara app: `GTITable` shows one, whose view and selection are the app's
values (or reactive variables), set by each change the reader makes, and changing the table when
the app sets them.

The table is a widget (`GTI.i_as_widget()`, see `_gti/_widget.py`), which Solara shows as it is,
as it shows any ipywidget: its glue (packages/gti/src/widget.ts) keeps the widget's state as the
browser has it, and a table whose rows are kept in Python asks for them with the widget's messages.
The component keeps one widget while it's given the same table (or one rendered the same, as a
table made again on each render is), so that the reader's view is kept, and it sets the widget
from its values, and its values from the widget.
"""

from __future__ import annotations

__all__ = ("GTITable",)

import uuid
from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, TypeVar

try:
    import solara
except ImportError:
    raise ImportError(
        "The great_tables.solara module requires the solara package to be installed."
        " Please install it with this command:"
        "\n\n    pip install solara"
    )
from reacton.core import get_render_context

from ._gti._state import (
    author_view,
    check_query_value,
    check_search,
    check_selection,
    check_sort,
)
from ._gti._widget import GTIWidget, render_widget_table
from .gt import GT

if TYPE_CHECKING:
    from ._gti._spec import Spec

T = TypeVar("T")

# (A value, or a reactive variable with one; `None` for the table's own)
_Value = T | solara.Reactive[T] | None

# (The widget's state the app has, in this order: the view's parts, then the selection)
_PARTS = ("query", "search", "sort", "selection")


@dataclass
class _Shown:
    """The table last given, and the widget showing it."""

    table: GT
    widget: GTIWidget


@solara.component
def GTITable(
    table: GT,
    query: _Value[str] = None,
    search: _Value[str] = None,
    sort: _Value[list[str]] = None,
    selection: _Value[list[int]] = None,
    on_query: Callable[[str], None] | None = None,
    on_search: Callable[[str], None] | None = None,
    on_sort: Callable[[list[str]], None] | None = None,
    on_selection: Callable[[list[int]], None] | None = None,
    on_rows: Callable[[list[int]], None] | None = None,
) -> solara.Element:
    """
    An interactive table in a Solara app, whose view and selection are the app's to read and set.

    The table (a `GTI` table, or a `GT` table with `opt_interactive()`) is shown as a widget (see
    [`i_as_widget()`](`great_tables.GTI.i_as_widget`)), and its state is in the component's
    values, as with Solara's own components: `query`, `search` and `sort` (its view), and
    `selection` (the rows selected). Each can be a value with a callback (`on_query=`, ...) or a
    reactive variable (`solara.reactive()`, `solara.use_reactive()`), which each change the reader
    makes sets; and when the app changes it, the table changes, as if the reader had. One left as
    `None` (as are all of them by default) starts as the table has it, and is then set. The rows
    the view keeps are given to `on_rows=`.

    A `GTI` table with more rows than the browser is quick with keeps them in Python instead (see
    [`i_scale()`](`great_tables.GTI.i_scale`)), and sends the browser a page at a time. Then the
    rows the view keeps are found in Python (without linked tables' selections). Such a table is
    best made once (at the module's top level, or with `solara.use_memo()`): a table made again on
    each render is rendered again each time (which, with many rows, takes a while), though the
    reader's view is kept if it's rendered the same.

    Parameters
    ----------
    table
        The table to show: a `GTI` table, or a `GT` table with `opt_interactive()`.
    query
        The table's filters, as a query in text (as the query box has it), or as
        [`i_view()`](`great_tables.GTI.i_view`)'s `filter=` takes it; `""` for none. It's set to
        a query in text.
    search
        The table's search; `""` for none.
    sort
        The columns the table is sorted by, most significant first, each with a `-` before it if
        it's sorted in descending order (e.g., `["-net", "store"]`); `[]` if it isn't sorted.
    selection
        The data rows selected (numbered by position in the data, from 0), in data order; `[]` for
        none. Setting it needs a table that lets readers select rows (see
        [`i_selection()`](`great_tables.GTI.i_selection`)).
    on_query, on_search, on_sort, on_selection
        Called with the new value, after each change to it (by the reader, or by the app).
    on_rows
        Called with the data rows the table's search and filters keep (and linked tables'
        selections), in the order shown, on every page (numbered by position in the data, from 0),
        whenever they change: first when they're known (before the table is shown, if Python can
        find them; a `GT` table's, and one with a search, once the browser has).

    Returns
    -------
    solara.Element
        The table.

    Examples
    --------
    ```python
    import solara
    from great_tables import GTI, exibble
    from great_tables.solara import GTITable

    table = GTI(exibble).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")
    query = solara.reactive("")
    selection = solara.reactive([])


    @solara.component
    def Page():
        solara.Button("One and two", on_click=lambda: query.set('fctr in ("one", "two")'))
        GTITable(table, query=query, selection=selection)
        solara.DataFrame(exibble.iloc[selection.value])
    ```
    """
    from .gti import GTI

    if not isinstance(table, GT):
        raise TypeError(f"`table` must be a `GTI` or a `GT` table, not {table!r}.")
    if not isinstance(table, GTI) and not table._options.ihtml_active.value:
        raise TypeError(
            "`GTITable` shows interactive tables (a `GTI` table, or a `GT` table with "
            "`opt_interactive()`); show a static one with `solara.HTML(unsafe_innerHTML=...)`."
        )

    values = {
        "query": solara.use_reactive(query, on_query),
        "search": solara.use_reactive(search, on_search),
        "sort": solara.use_reactive(sort, on_sort),
        "selection": solara.use_reactive(selection, on_selection),
    }
    # (A table without an id is given one of the component's, so that it's rendered the same each
    # time it's made again)
    id = solara.use_memo(lambda: f"gti-{uuid.uuid4().hex[:12]}", [])
    shown = solara.use_ref(None)
    widget = _widget(shown, table, id, values)
    context = get_render_context()

    # (What the widget's observer reads: as of the latest render)
    latest = solara.use_ref((values, on_rows))
    latest.current = (values, on_rows)
    # (Whether the app's values are being set on the widget, which reports each part as it's set,
    # and the widget they were last set on)
    syncing = solara.use_ref(False)
    applied = solara.use_ref(None)
    # (The rows last given to `on_rows`)
    reported = solara.use_ref(None)

    def report_rows() -> None:
        rows = _rows(widget)
        callback = latest.current[1]
        if rows is not None and rows != reported.current:
            reported.current = rows
            if callback is not None:
                callback(rows)

    def watch() -> Callable[[], None]:
        def changed(change: dict[str, Any]) -> None:
            # (In one render, after all the values are set: a render after one of them would set
            # the others' old values on the widget)
            with context:
                if not syncing.current:
                    _take(widget, latest.current[0])
                report_rows()

        names = ["_view", "_rows", "_selection"]
        widget.observe(changed, names=names)
        reported.current = None
        report_rows()
        return lambda: widget.unobserve(changed, names=names)

    def apply() -> None:
        # (A widget made for another table, which the values may not apply to, takes what it can)
        replaced = applied.current is not None and applied.current is not widget
        applied.current = widget
        syncing.current = True
        try:
            _apply(widget, values, replaced)
        finally:
            syncing.current = False
        _take(widget, values)

    solara.use_effect(watch, [widget])
    solara.use_effect(apply, [widget, *(values[part].value for part in _PARTS)])
    # (A widget no longer shown is closed)
    solara.use_effect(lambda: widget.close, [widget])
    return solara.Div(children=[widget])


def _widget(shown: Any, table: GT, id: str, values: dict[str, solara.Reactive[Any]]) -> GTIWidget:
    # The widget showing the table: the last one, if it's the same table, or one rendered the
    # same (which then has the new table, as its rows may have changed); or a new one, with the
    # app's values from the start (as the browser may report its first state before it has a
    # change made after; one for another table taking those that apply to it)
    current: _Shown | None = shown.current
    if current is not None and current.table is table:
        return current.widget
    if table._options.table_id.value is None:
        table_with_id = table.with_id(id)
    else:
        table_with_id = table
    rendered = render_widget_table(table_with_id)
    html, spec, engine = rendered
    if (
        current is not None
        and html == current.widget._html
        and (engine is not None) == current.widget._kernel
    ):
        widget = current.widget
        widget._gti, widget._spec, widget._engine = table_with_id, spec, engine
    else:
        state = _start(spec, values, replaced=current is not None)
        widget = GTIWidget(table_with_id, rendered, state)
    shown.current = _Shown(table=table, widget=widget)
    return widget


def _start(spec: Spec, values: dict[str, solara.Reactive[Any]], replaced: bool) -> dict[str, Any]:
    # A new widget's first view and selection: the table's own, with the app's values
    view = author_view(spec)
    selection: list[int] = []
    checks = {
        "query": ("filter", lambda value: check_query_value(spec, value, "`query`")),
        "search": ("search", lambda value: check_search(value, "`search`")),
        "sort": ("sort", lambda value: check_sort(spec, value, "`sort`")),
    }
    for part in _PARTS:
        value = values[part].value
        if value is None:
            continue
        try:
            if part == "selection":
                selection = check_selection(spec, value, "`selection`")
            else:
                key, check = checks[part]
                view[key] = check(value)
        except (TypeError, ValueError):
            if not replaced:
                raise
    return {"_view": view, "_selection": selection}


def _apply(widget: GTIWidget, values: dict[str, solara.Reactive[Any]], replaced: bool) -> None:
    # Set the app's values on the widget, where they differ from its own (those that are `None`
    # are the widget's to give); with `replaced`, those that don't apply to it are dropped
    with widget.hold_sync():
        for part in _PARTS:
            value = values[part].value
            if value is None or value == getattr(widget, part):
                continue
            try:
                setattr(widget, part, value)
            except (TypeError, ValueError):
                if not replaced:
                    raise


def _take(widget: GTIWidget, values: dict[str, solara.Reactive[Any]]) -> None:
    # Set the app's values from the widget, where they differ from its own
    for part in _PARTS:
        value = getattr(widget, part)
        if values[part].value != value:
            values[part].set(value)


def _rows(widget: GTIWidget) -> list[int] | None:
    # The rows the widget's view keeps, or `None` while they aren't known
    try:
        return widget.rows
    except RuntimeError:
        return None
