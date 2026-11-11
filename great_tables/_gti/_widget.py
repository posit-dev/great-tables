"""A GTI table as an anywidget (`GTI.i_as_widget()`), whose view and selection Python can read and set.

The browser stays the engine: the widget shows the table's `<gt-table>` element (as
`as_raw_html()` has it), and the glue (packages/gti/src/widget.ts, run after the runtime) keeps
the model's state as the browser has it: the view (`_view`, `None` until the table's shown), the
rows the view keeps, in the order shown (`_rows`), and those selected (`_selection`). Python sets
the view's filter, sort and search, and the selection, which the browser then applies.
"""

from __future__ import annotations

import operator
from collections.abc import Callable
from functools import lru_cache
from typing import TYPE_CHECKING, Any

import anywidget
import traitlets

from .._tbl_data import DataFrameLike, get_column_names, reorder
from ._query import check_query, check_view, format_query, parse_sort, view_rows
from ._render import JS_DIR, _load_runtime, render_gti_element

if TYPE_CHECKING:
    from ..gti import GTI
    from ._spec import Spec

__all__ = ["GTIWidget"]


@lru_cache(maxsize=None)
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

    def __init__(self, gti: GTI) -> None:
        html, spec = render_gti_element(gti)
        super().__init__(_esm=_esm(), _css=_load_runtime()[1], _html=html)
        self._gti = gti
        self._spec: Spec = spec
        # (Whether the browser has given the table's state, which is then its own)
        self._shown = False
        self._callbacks: list[Callable[[GTIWidget], Any]] = []
        self.on_msg(self._on_msg)

    # -----
    # The view

    def _current_view(self) -> dict[str, Any]:
        # The browser's view, or before it has one, the author's
        if self._view is not None:
            return self._view
        spec = self._spec
        pagination = spec["pagination"]
        return {
            "filter": spec["view"]["filter"],
            "sort": spec["view"]["sort"],
            "search": "",
            "page": 1,
            "page_size": pagination["page_size"] if pagination["enabled"] else None,
            "hidden": spec["view"]["hidden"],
            "group_by": spec["view"]["group_by"],
        }

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
        if isinstance(value, str) and value.strip() == "":
            value = None
        try:
            query = check_query(value)
        except ValueError as err:
            raise ValueError(str(err).replace("`filter=`", "`query`")) from None
        spec = self._spec
        kinds = {
            **{column["id"]: column["kind"] for column in spec["columns"]},
            **{column["id"]: column["kind"] for column in spec["query_columns"]},
        }
        check_view(query, (), spec["filters"], spec["ranks"], kinds=kinds)
        self._set_view(filter=query)

    @property
    def search(self) -> str:
        """The table's search (`""` without one). Setting it searches the table's rows."""
        return self._current_view()["search"]

    @search.setter
    def search(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"`search` must be a string, not {value!r}.")
        self._set_view(search=value)

    @property
    def sort(self) -> list[str]:
        """
        The table's sort: its columns, most significant first, each with a `-` before it if it's
        sorted in descending order (e.g., `["-net", "store"]`); `[]` if it isn't sorted.

        Setting it (to a list of them, a column name, or `None`) sorts the table's rows.
        """
        return [
            f"-{key['column']}" if key["descending"] else key["column"]
            for key in self._current_view()["sort"]
        ]

    @sort.setter
    def sort(self, value: str | list[str] | None) -> None:
        keys = parse_sort(value)
        for column, _ in keys:
            if column not in self._spec["ranks"]:
                raise ValueError(
                    f"`sort` can't sort the table by column {column!r}: it isn't one the table "
                    "can be sorted by."
                )
        self._set_view(sort=[{"column": column, "descending": desc} for column, desc in keys])

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
        mode = self._spec["controls"]["selection"]
        nrows = self._spec["nrows"]
        try:
            items = list(rows)
        except TypeError:
            raise TypeError(f"`selection` must be a list of data rows, not {rows!r}.") from None
        checked: set[int] = set()
        for row in items:
            try:
                index = -1 if isinstance(row, bool) else operator.index(row)
            except TypeError:
                index = -1
            if index < 0:
                raise ValueError(
                    f"`selection` must hold data rows (whole numbers, from 0), not {row!r}."
                )
            if index >= nrows:
                raise ValueError(f"`selection` has row {index}, but the table has {nrows} rows.")
            checked.add(index)
        limit = {None: 0, "single": 1}.get(mode, nrows)
        if len(checked) > limit:
            raise ValueError(
                "The table's rows can't be selected: let readers select them with `i_selection()`."
                if mode is None
                else "Only one of the table's rows can be selected (it has `i_selection('single')`)."
            )
        self._selection = sorted(checked)

    @property
    def rows(self) -> list[int]:
        """
        The data rows the table's search and filters keep (and linked tables' selections), in
        the order shown, on every page, numbered by position in the data (from 0).

        They're the browser's. Before the table is shown, they're those its view keeps, as
        Python finds them; once it's shown, a change to the view made from Python is applied by
        the browser after the code making it has run (in a notebook, when the cell is done), and
        until then there are no rows to give (it's an error to ask for them).
        """
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
            sort=[f"-{k['column']}" if k["descending"] else k["column"] for k in view["sort"]],
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
        if isinstance(content, dict) and content.get("type") == "change":
            for callback in list(self._callbacks):
                callback(self)
