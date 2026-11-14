"""Interactive tables in a marimo notebook or app: `mo_gti()` shows one as a UI element, whose
value is the table's view, rows and selection, so that the cells that read it run again with each
change the reader makes.

The element is marimo's for an anywidget (`mo.ui.anywidget`), of the table's widget
(`GTI.i_as_widget()`, see `_gti/_widget.py`): marimo keeps the widget's state as the browser has
it, runs the cells that read the element again when the browser changes it, and passes on the
widget's messages, with which a table whose rows are kept in Python asks for them. The element
has the widget's own (`query`, `rows`, `view()`, ...), and a value of the parts an app reads,
rather than all of the widget's state (which has the table's HTML).
"""

from __future__ import annotations

__all__ = (
    "GTIElement",
    "mo_gti",
)

from typing import TYPE_CHECKING, Any

try:
    import marimo as mo
except ImportError:
    raise ImportError(
        "The great_tables.marimo module requires the marimo package to be installed."
        " Please install it with this command:"
        "\n\n    pip install marimo"
    )

from ._gti._widget import GTIWidget
from .gt import GT

if TYPE_CHECKING:
    from ._tbl_data import DataFrameLike


class GTIElement(mo.ui.anywidget):
    """
    An interactive table as a marimo UI element, made by
    [`mo_gti()`](`great_tables.marimo.mo_gti`), which has the details.

    Attributes
    ----------
    value
        The table's state: a dict with its `"query"`, `"search"` and `"sort"`, the data `"rows"`
        its view keeps (in the order shown; `None` while they aren't known), and the rows in its
        `"selection"`.
    widget
        The table's widget (see [`i_as_widget()`](`great_tables.GTI.i_as_widget`)), whose
        `query`, `search`, `sort` and `selection` the element has too, to read and set, with its
        `rows`, `view()` and `on_change()`.
    """

    widget: GTIWidget

    @property
    def value(self) -> dict[str, Any]:
        """The table's view, the rows it keeps, and those selected."""
        return self._state()

    def _convert_value(self, value: Any) -> dict[str, Any]:
        # (What marimo keeps of a change from the browser, which sets the widget's state, as the
        # value an element made of this one has, e.g. `mo.ui.array()`'s)
        super()._convert_value(value)
        return self._state()

    def _state(self) -> dict[str, Any]:
        widget = self.widget
        try:
            rows: list[int] | None = widget.rows
        except RuntimeError:
            # (Not known yet: the browser finds them)
            rows = None
        return {
            "query": widget.query,
            "search": widget.search,
            "sort": widget.sort,
            "rows": rows,
            "selection": widget.selection,
        }

    @value.setter
    def value(self, value: Any) -> None:
        del value
        raise RuntimeError(
            "Setting the value of a UI element isn't allowed: set the table's `query`, `search`, "
            "`sort` or `selection` instead."
        )

    def view(self, selected: bool = False) -> DataFrameLike:
        """The table's data with the rows its view keeps (or those selected), as a DataFrame of
        the data's library."""
        return self.widget.view(selected=selected)

    def __setattr__(self, name: str, value: Any) -> None:
        # (Set on the widget, as marimo's element does)
        super().__setattr__(name, value)
        # The cells that read the element run again when the browser tells marimo of a change, as
        # it does with the rows a view set from Python leaves; it has nothing to tell of a
        # selection, or of a view whose rows are Python's, so marimo is told here
        if (
            name in _SETTABLE
            and self._initialized
            and (name == "selection" or self.widget._engine is not None)
        ):
            _run_readers(self)

    def __deepcopy__(self, memo: Any) -> GTIElement:
        # (As marimo copies an element put in another, e.g. `mo.ui.array()`: a widget can't be
        # copied, so the copy is a new one of the table, with its state as it is now)
        widget = self.widget
        rendered = (widget._html, widget._spec, widget._engine)
        state = {"_view": widget._view, "_selection": widget._selection}
        return GTIElement(GTIWidget(widget._gti, rendered, state))


# (What's set on the element that changes the table)
_SETTABLE = ("query", "search", "sort", "selection")


def _run_readers(element: GTIElement) -> None:
    # Have marimo run the cells that read the element once the code changing it has run (as a
    # change from the browser does), unless it's the element's own cell, after which they run
    # anyway. This is marimo's own machinery (as its code mode uses it), so it's left alone if
    # it isn't there, as when the notebook is run as a script.
    try:
        from marimo._runtime.commands import UpdateUIElementCommand
        from marimo._runtime.context import get_context
        from marimo._runtime.context.kernel_context import KernelRuntimeContext

        ctx = get_context()
        if not isinstance(ctx, KernelRuntimeContext):
            return
        if ctx.cell_id == ctx.ui_element_registry.get_cell(element._id):
            return
        # (An empty update, which changes nothing of the widget's state)
        ctx._kernel.enqueue_control_request(
            UpdateUIElementCommand(object_ids=[element._id], values=[{}])
        )
    except Exception:  # noqa: BLE001
        return


def mo_gti(table: GT) -> GTIElement:
    """
    Show an interactive table in marimo, as a UI element whose value is the table's state.

    The table (a `GTI` table, or a `GT` table with `opt_interactive()`) is shown as a widget (see
    [`i_as_widget()`](`great_tables.GTI.i_as_widget`)), made a UI element, as marimo's own are:
    assigned to a variable (and shown as a cell's output), the cells that read it run again with
    each change the reader makes (a search, a filter, a sort, a selection, ...). Its `value` is
    the table's `"query"`, `"search"` and `"sort"`, the data `"rows"` its view keeps, and the rows
    in its `"selection"`. The element has the widget's `query`, `search`, `sort` and `selection`,
    too, which change the table when they're set (as in a button's `on_click=`), and `rows`,
    `view()` (the table's data with those rows; `view(selected=True)`, the rows selected) and
    `on_change()`.

    The rows are the browser's: a change made from Python is applied by the browser after the cell
    making it has run, and the cells that read the element then run again. A `GT` table's rows,
    and a `GTI` table's with a search, are known once the browser has shown the table (until
    then, `value["rows"]` is `None`).

    A `GTI` table with more rows than the browser is quick with keeps them in Python instead (see
    [`i_scale()`](`great_tables.GTI.i_scale`)), and sends the browser a page at a time. Then the
    rows the view keeps are found in Python (without linked tables' selections), and the cells
    that read the element run again for each page.

    Parameters
    ----------
    table
        The table to show: a `GTI` table, or a `GT` table with `opt_interactive()`.

    Returns
    -------
    GTIElement
        The table, as a UI element.

    Examples
    --------
    In one cell, make the table, and show it:

    ```python
    import marimo as mo
    from great_tables import GTI, exibble
    from great_tables.marimo import mo_gti

    table = mo_gti(
        GTI(exibble).i_cols_filter(columns="fctr", type="facet").i_selection("multiple")
    )
    table
    ```

    And in another, use what the reader does with it:

    ```python
    mo.vstack([
        mo.md(f"{len(table.value['rows'] or [])} rows, filtered by {table.value['query']!r}"),
        table.view(selected=True),
    ])
    ```
    """
    from .gti import GTI

    if not isinstance(table, GT):
        raise TypeError(f"`table` must be a `GTI` or a `GT` table, not {table!r}.")
    if not isinstance(table, GTI) and not table._options.ihtml_active.value:
        raise TypeError(
            "`mo_gti()` shows interactive tables (a `GTI` table, or a `GT` table with "
            "`opt_interactive()`); show a static one as it is, as a cell's output."
        )
    return GTIElement(GTIWidget(table))
