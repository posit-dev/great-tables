"""Interactive tables in a Panel app or notebook: `GTIPane` shows one, and has its view, rows and
selection as parameters, which Python reads, watches and sets.

The pane is a Panel ESM component (`pn.custom.ReactiveESM`), whose module is the runtime, then
the glue (packages/gti/src/panel.ts), which is the widget's (`GTI.i_as_widget()`, see
`_gti/_widget.py`), given a model of its own: the widget's state (`_view`, `_rows`, `_selection`),
kept here as the browser has it (in `_model`), is synced as one parameter each way, `_update`
(the state, as Python changes it, with a count) and `_report` (the reader's changes), as a notebook's Panel has each change
after the first of a message from the browser only once the next one comes. A table whose rows are
kept in Python (see `_gti/_kernel.py`) asks for them with Panel's messages, as the widget does with
its own. Its public parameters (`query`, `search`, `sort`, `selection`, `rows`) are Python's only,
kept in step with the state.
"""

from __future__ import annotations

__all__ = ("GTIPane",)

from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, ClassVar

try:
    import param
    from panel.custom import ReactiveESM
except ImportError:
    raise ImportError(
        "The great_tables.panel module requires the panel package to be installed."
        " Please install it with this command:"
        "\n\n    pip install panel"
    )

from ._gti._kernel import render_table
from ._gti._lazy import eager
from ._gti._query import format_query
from ._gti._render import JS_DIR, _load_runtime, render_gti_element
from ._gti._state import (
    author_view,
    check_query_value,
    check_search,
    check_selection,
    check_sort,
    python_rows,
    sort_names,
)
from ._tbl_data import DataFrameLike, get_column_names, reorder
from .gt import GT

if TYPE_CHECKING:
    from collections.abc import Iterator

    from ._gti._spec import Spec


def _sources() -> tuple[str, str]:
    # The component's module (the runtime, then the glue, which only uses what the runtime
    # defines) and CSS (in the component's shadow root, as Panel's components are each in one)
    js, css = _load_runtime()
    return js + (JS_DIR / "gti-panel.js").read_text(encoding="utf-8"), css


_ESM, _CSS = _sources()


class GTIPane(ReactiveESM):
    """
    An interactive table in a Panel app or notebook, whose view and selection are parameters.

    The table (a `GTI` table, or a `GT` table with `opt_interactive()`) is shown as a Panel
    component, and its state is in its parameters: `query`, `search` and `sort` (its view),
    `rows` (the rows the view keeps) and `selection` (the rows selected). Each change the reader
    makes to them sets them, so that they can be watched (with `pn.bind()`, `param.depends()` or
    `.param.watch()`) like any other Panel parameter; and setting `query`, `search`, `sort` or
    `selection` changes the table, as if the reader had.

    A `GTI` table with more rows than the browser is quick with keeps them in Python instead (see
    [`i_scale()`](`great_tables.GTI.i_scale`)), and sends the browser a page at a time. Then
    `rows` is found in Python (without linked tables' selections).

    Parameters
    ----------
    table
        The table to show: a `GTI` table, or a `GT` table with `opt_interactive()`.
    **params
        Panel's parameters of a component (e.g., `margin=`, `visible=`).

    Examples
    --------
    ```python
    import panel as pn
    from great_tables import GTI, exibble
    from great_tables.panel import GTIPane

    pn.extension()

    table = GTIPane(
        GTI(exibble).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")
    )


    def selected(selection):
        return exibble.iloc[selection]


    pn.Column(table, pn.bind(selected, table.param.selection)).servable()
    ```
    """

    query = param.String(
        default="",
        doc="The table's filters, as a query in text (as the query box has it), or `''` without any.",
    )
    search = param.String(default="", doc="The table's search (`''` without one).")
    sort = param.List(
        default=[],
        item_type=str,
        doc=(
            "The table's sort: its columns, most significant first, each with a `-` before it if "
            "it's sorted in descending order."
        ),
    )
    selection = param.List(
        default=[],
        item_type=int,
        doc="The data rows selected (numbered by position in the data, from 0), in data order.",
    )
    rows = param.List(
        default=None,
        allow_None=True,
        constant=True,
        doc=(
            "The data rows the table's search and filters keep, in the order shown, on every "
            "page (numbered by position in the data, from 0); `None` until they're known."
        ),
    )

    # (Synced with the browser: the table, and the changes to its state, each way)
    _html = param.String(default="")
    _update = param.Dict(default={})
    _report = param.Dict(default={})
    _kernel = param.Boolean(default=False)
    _nrows = param.Integer(default=0)

    # (The public parameters are Python's only)
    _rename: ClassVar[dict[str, str | None]] = dict.fromkeys(
        ["query", "search", "sort", "selection", "rows"]
    )

    _esm = _ESM
    _stylesheets: ClassVar[list[str]] = [_CSS]

    def __init__(self, table: GT, **params: Any) -> None:
        from .gti import GTI

        if not isinstance(table, GT):
            raise TypeError(f"`table` must be a `GTI` or a `GT` table, not {table!r}.")
        if not isinstance(table, GTI) and not table._options.ihtml_active.value:
            raise TypeError(
                "`GTIPane` shows interactive tables (a `GTI` table, or a `GT` table with "
                "`opt_interactive()`); show a static one with `pn.pane.HTML(table.as_raw_html())`."
            )
        if isinstance(table, GTI):
            html, spec, engine = render_table(table)
        else:
            (html, spec), engine = render_gti_element(table), None
        # (Set before the parameters, which are checked against it)
        self._table = table
        self._spec: Spec = spec
        self._engine = engine
        self._syncing = False
        view = author_view(spec)
        # (The widget's state, as the browser has it, or will once it's sent)
        self._model: dict[str, Any] = {"_view": view, "_rows": None, "_selection": []}
        super().__init__(
            # (Without a `</` in it, as a notebook has the parameters in a script, as they are:
            # src/panel.ts puts them back)
            _html=html.replace("</", "<\x00/"),
            _update={**self._model, "n": 0},
            _kernel=engine is not None,
            _nrows=spec["nrows"],
            **params,
        )
        with self._sync():
            self._take_view(view)
            self._take_rows(None)
        self.param.watch(self._view_changed, ["query", "search", "sort"])
        self.param.watch(self._selection_changed, ["selection"])
        self.param.watch(self._reported, ["_report"])

    @contextmanager
    def _sync(self) -> Iterator[None]:
        # (While the parameters are set from one another, which isn't a change to make)
        syncing, self._syncing = self._syncing, True
        try:
            yield
        finally:
            self._syncing = syncing

    # -----
    # From the browser

    def _take_view(self, view: dict[str, Any]) -> None:
        self.param.update(
            query=format_query(view["filter"]),
            search=view["search"],
            sort=sort_names(view["sort"]),
        )

    def _take_rows(self, rows: list[int] | None) -> None:
        # (The browser's, or with the rows in Python, Python's; or before the browser has any,
        # those Python finds, where it can)
        view = self._model["_view"]
        if self._engine is not None:
            try:
                rows = list(self._engine.find({**view, "links": []}))
            except (TypeError, ValueError):
                rows = []
        elif rows is None and view["search"] == "" and not self._shown():
            from .gti import GTI

            if isinstance(self._table, GTI):
                rows = python_rows(self._table, self._spec, view)
        with param.edit_constant(self):
            self.rows = None if rows is None else list(rows)

    def _shown(self) -> bool:
        return bool(self._models)

    def _reported(self, event: param.parameterized.Event) -> None:
        report = event.new if isinstance(event.new, dict) else {}
        changes = {name: report[name] for name in self._model if name in report}
        self._model.update(changes)
        # (Which a view made from now on starts with, as when the pane's shown again; but isn't
        # sent to the views there are, which have it, or have another view's report)
        with param.discard_events(self):
            self._update = {**self._model, "n": self._update["n"]}
        with self._sync():
            if "_view" in changes and changes["_view"] is not None:
                self._take_view(changes["_view"])
            if "_selection" in changes:
                self.selection = list(changes["_selection"])
            if changes.keys() & {"_view", "_rows"}:
                self._take_rows(self._model["_rows"])

    def _send(self, **changes: Any) -> None:
        # (The whole state, with a count, so that it's a change, if it's the same as the last)
        self._model.update(changes)
        self._update = {**self._model, "n": self._update["n"] + 1}

    # -----
    # From Python

    def _view_changed(self, *events: param.parameterized.Event) -> None:
        if self._syncing:
            return
        parts: dict[str, Any] = {}
        try:
            for event in events:
                if event.name == "query":
                    parts["filter"] = check_query_value(self._spec, event.new, "`query`")
                elif event.name == "search":
                    parts["search"] = check_search(event.new, "`search`")
                else:
                    parts["sort"] = check_sort(self._spec, event.new, "`sort`")
        except (TypeError, ValueError):
            # (What can't be set is put back)
            with self._sync():
                self.param.update({event.name: event.old for event in events})
            raise
        view = {**self._model["_view"], **parts, "page": 1}
        with self._sync():
            # (The browser's rows, sent once it's applied the view, come after it)
            self._send(_view=view, _rows=None)
            self._take_view(view)
            self._take_rows(None)

    def _selection_changed(self, event: param.parameterized.Event) -> None:
        if self._syncing:
            return
        try:
            selection = check_selection(self._spec, event.new, "`selection`")
        except (TypeError, ValueError):
            with self._sync():
                self.selection = event.old
            raise
        with self._sync():
            self._send(_selection=selection)
            self.selection = selection

    # -----
    # The rows

    def data(self, selected: bool = False) -> DataFrameLike:
        """
        The table's data, with the rows its view keeps, in the order shown (see `rows`), or with
        `selected=True`, the rows selected (in data order): a DataFrame of the data's library,
        with all of its columns.
        """
        if not isinstance(selected, bool):
            raise TypeError(f"`selected=` must be `True` or `False`, not {selected!r}.")
        rows = self.selection if selected else self.rows
        if rows is None:
            raise RuntimeError(
                "The table's rows aren't known yet: the browser finds them once it's shown."
            )
        if self._engine is not None:
            return self._engine.data(rows)
        data = eager(self._table)._tbl_data
        return reorder(data, rows, get_column_names(data))

    def _handle_msg(self, data: Any) -> None:
        # An ask for rows (a page, or a facet's counts), from the browser, with the rows in Python
        # (an error is the browser's to show, as it shows a source's)
        if not isinstance(data, dict) or data.get("type") != "ask" or self._engine is None:
            return
        try:
            answer = self._engine.answer(data)
        except Exception as err:  # noqa: BLE001
            self._send_msg({"type": "answer", "id": data.get("id"), "error": str(err)})
        else:
            self._send_msg({"type": "answer", "id": data.get("id"), "answer": answer})
