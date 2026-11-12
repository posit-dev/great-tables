"""A GTI table as an anywidget (`GTI.i_as_widget()`), whose view and selection Python can read and set.

The widget shows the table's `<gt-table>` element (as `as_raw_html()` has it), and the glue
(packages/gti/src/widget.ts, run after the runtime) keeps the model's state as the browser has it:
the view (`_view`, `None` until the table's shown), the rows the view keeps, in the order shown
(`_rows`), and those selected (`_selection`). Python sets the view's filter, sort and search, and
the selection, which the browser then applies.

The browser is the engine, unless the table's rows are kept in Python (`_kernel`, as
`i_scale()` has it: see `_kernel.py`): then the browser has a page of them at a time, which it
asks for with an "ask" message (as it does a facet's counts), answered with an "answer" message;
and the rows the view keeps are Python's (`_rows` isn't written).
"""

from __future__ import annotations

from collections.abc import Callable
from functools import cache
from typing import TYPE_CHECKING, Any

import anywidget
import traitlets

from .._tbl_data import DataFrameLike, get_column_names, reorder
from ._kernel import KernelEngine, render_table
from ._query import format_query, view_rows
from ._render import JS_DIR, _load_runtime
from ._state import (
    author_view,
    check_query_value,
    check_search,
    check_selection,
    check_sort,
    sort_names,
)

if TYPE_CHECKING:
    from ..gti import GTI
    from ._spec import Spec

__all__ = ["GTIWidget"]


@cache
def _esm() -> str:
    """The widget's module: the runtime, then the glue (which only uses what the runtime defines)."""
    js, _ = _load_runtime()
    return js + (JS_DIR / "gti-widget.js").read_text(encoding="utf-8")


class GTIWidget(anywidget.AnyWidget):
    """
    A GTI table as a widget, whose view and selection can be read and set from Python.

    Made by [`GTI.i_as_widget()`](`great_tables.GTI.i_as_widget`), which has the details.
    """

    _esm = traitlets.Unicode().tag(sync=True)
    _css = traitlets.Unicode().tag(sync=True)
    _html = traitlets.Unicode().tag(sync=True)
    _view = traitlets.Dict(allow_none=True, default_value=None).tag(sync=True)
    _rows = traitlets.List(allow_none=True, default_value=None).tag(sync=True)
    _selection = traitlets.List().tag(sync=True)
    # (Whether the table's rows are kept in Python, and how many there are)
    _kernel = traitlets.Bool(False).tag(sync=True)
    _nrows = traitlets.Int(0).tag(sync=True)

    def __init__(self, gti: GTI) -> None:
        html, spec, engine = render_table(gti)
        super().__init__(
            _esm=_esm(),
            _css=_load_runtime()[1],
            _html=html,
            _kernel=engine is not None,
            _nrows=spec["nrows"],
        )
        self._gti = gti
        # (With the rows in Python, its spec has every row's, as the browser's would)
        self._spec: Spec = spec
        self._engine = engine
        # (Whether the browser has given the table's state, which is then its own)
        self._shown = False
        self._callbacks: list[Callable[[GTIWidget], Any]] = []
        self.on_msg(self._on_msg)

    # -----
    # The view

    def _current_view(self) -> dict[str, Any]:
        # The browser's view, or before it has one, the author's
        return self._view if self._view is not None else author_view(self._spec)

    def _set_view(self, **parts: Any) -> None:
        view = {**self._current_view(), **parts, "page": 1}
        # (In one message, so that the browser's rows, written once it's applied the view, come
        # after it)
        with self.hold_sync():
            self._view = view
            self._rows = None

    @property
    def query(self) -> str:
        """
        The table's filters, as a query in text (as the query box has it), or `""` without any.

        Setting it (to a query in text, or as [`i_view()`](`great_tables.GTI.i_view`)'s `filter=`
        takes it, or to `None` or `""` for none) filters the table's rows, and shows the first page.
        """
        return format_query(self._current_view()["filter"])

    @query.setter
    def query(self, value: str | dict[str, Any] | None) -> None:
        self._set_view(filter=check_query_value(self._spec, value, "`query`"))

    @property
    def search(self) -> str:
        """The table's search (`""` without one). Setting it searches the table's rows."""
        return self._current_view()["search"]

    @search.setter
    def search(self, value: str) -> None:
        self._set_view(search=check_search(value, "`search`"))

    @property
    def sort(self) -> list[str]:
        """
        The table's sort: its columns, most significant first, each with a `-` before it if it's
        sorted in descending order (e.g., `["-net", "store"]`); `[]` if it isn't sorted.

        Setting it (to a list of them, a column name, or `None`) sorts the table's rows.
        """
        return sort_names(self._current_view()["sort"])

    @sort.setter
    def sort(self, value: str | list[str] | None) -> None:
        self._set_view(sort=check_sort(self._spec, value, "`sort`"))

    # -----
    # Rows

    @property
    def selection(self) -> list[int]:
        """
        The data rows selected (numbered by position in the data, from 0), in data order.

        Setting it (to a list of them) selects those rows, and only those, as far as the table
        lets readers select rows (see [`i_selection()`](`great_tables.GTI.i_selection`)).
        """
        return list(self._selection)

    @selection.setter
    def selection(self, rows: Any) -> None:
        self._selection = check_selection(self._spec, rows, "`selection`")

    @property
    def rows(self) -> list[int]:
        """
        The data rows the table's search and filters keep (and linked tables' selections), in
        the order shown, on every page, numbered by position in the data (from 0).

        They're the browser's. Before the table is shown, they're those its view keeps, as
        Python finds them; once it's shown, a change to the view made from Python is applied by
        the browser after the code making it has run (in a notebook, when the cell is done), and
        until then there are no rows to give (it's an error to ask for them). With the rows kept
        in Python (see [`i_scale()`](`great_tables.GTI.i_scale`)), they're Python's, at once.
        """
        if self._engine is not None:
            view = self._current_view()
            return list(self._engine.find({**view, "links": []}))
        if self._rows is not None:
            return list(self._rows)
        if self._shown:
            raise RuntimeError(
                "The table hasn't shown the change to its view yet: the browser applies it after "
                "the code making it has run (in a notebook, ask for the rows in another cell)."
            )
        view = self._current_view()
        if view["search"] != "":
            raise RuntimeError(
                "The table's rows can't be found before it's shown with a search: show the "
                "table first (or set `search` after)."
            )
        return self._python_rows(view)

    def _python_rows(self, view: dict[str, Any]) -> list[int]:
        # The rows the view keeps, as Python finds them (with `view_rows()`), and grouped as the
        # runtime groups them: by the group column's values (descending if sorted so), the rows
        # missing one last
        gti = self._gti.i_view(
            filter=view["filter"],
            sort=sort_names(view["sort"]),
            hidden=view["hidden"] or None,
            group_by=view["group_by"],
        )
        rows = view_rows(gti)
        column = view["group_by"]
        if column is not None:
            ranks = self._spec["ranks"][column]
            descending = any(k["column"] == column and k["descending"] for k in view["sort"])

            def key(row: int) -> tuple[bool, int]:
                rank = ranks[row]
                return (rank is None, 0 if rank is None else (-rank if descending else rank))

            rows.sort(key=key)
        return rows

    def view(self, selected: bool = False) -> DataFrameLike:
        """
        The table's data, with the rows its view keeps, in the order shown (see `rows`), or with
        `selected=True`, the rows selected (in data order): a DataFrame of the data's library,
        with all of its columns.
        """
        if not isinstance(selected, bool):
            raise TypeError(f"`selected=` must be `True` or `False`, not {selected!r}.")
        data = self._gti._tbl_data
        rows = self.selection if selected else self.rows
        return reorder(data, rows, get_column_names(data))

    # -----
    # Changes

    def on_change(self, callback: Callable[[GTIWidget], Any], remove: bool = False) -> None:
        """
        Call `callback` (with the widget) after each change the reader makes to the table's view
        or selection, or to the rows it keeps, once Python has it; or with `remove=True`, don't.
        """
        if not callable(callback):
            raise TypeError(f"`callback` must be callable, not {callback!r}.")
        if remove:
            if callback in self._callbacks:
                self._callbacks.remove(callback)
        elif callback not in self._callbacks:
            self._callbacks.append(callback)

    @traitlets.observe("_rows")
    def _rows_changed(self, change: dict[str, Any]) -> None:
        if change["new"] is not None:
            self._shown = True

    def _on_msg(self, _: Any, content: Any, buffers: Any) -> None:
        if not isinstance(content, dict):
            return
        if content.get("type") == "change":
            for callback in list(self._callbacks):
                callback(self)
        elif content.get("type") == "ask" and self._engine is not None:
            self._answer(self._engine, content)

    def _answer(self, engine: KernelEngine, ask: dict[str, Any]) -> None:
        # (An error is the browser's to show, as it shows a source's)
        try:
            answer = engine.answer(ask)
        except Exception as err:  # noqa: BLE001
            self.send({"type": "answer", "id": ask.get("id"), "error": str(err)})
        else:
            self.send({"type": "answer", "id": ask.get("id"), "answer": answer})
