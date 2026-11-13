from __future__ import annotations

import copy
import functools
import inspect
import math
import numbers
import operator
import sys
from contextvars import ContextVar
from dataclasses import replace
from typing import TYPE_CHECKING, Any, NoReturn

from typing_extensions import Self

from ._gt_data import ColInfoTypeEnum
from ._gti._settings import (
    DATA_COLOR_MODES,
    ENGINES,
    EXPORT_FORMATS,
    FILTER_TYPES,
    PIN_SIDES,
    PRESETS,
    PROFILE_PLOTS,
    RESPONSIVE_MODES,
    SELECTION_MODES,
    DataColorMode,
    Engine,
    ExportFormat,
    FilterType,
    PinSide,
    Preset,
    ProfilePlot,
    ResponsiveMode,
    SelectionMode,
    Settings,
    settings_of,
)
from ._gti._spec import _has_time_zone
from ._locations import resolve_cols_c
from ._options import _is_height
from ._tbl_data import SelectExpr, _get_column_kind, get_column_names
from .gt import GT

if TYPE_CHECKING:
    from collections.abc import Callable

    from ._gti._lazy import Lazy
    from ._gti._widget import GTIWidget

__all__ = ["GTI"]


class GTI(GT):
    """
    Create an interactive **Great Tables** object.

    The `GTI()` class makes a table that readers can work with in the browser: they can sort it by
    its columns, search it, page through it, resize its columns, and (if allowed) select its rows.
    It's a `GT` table in every other way, so all of `GT`'s methods (formatting, styling, spanners,
    summary rows, and the rest) can be used to make it. What readers can do with it is set by the
    methods beginning with `i_` (e.g., [`i_pagination()`](`great_tables.GTI.i_pagination`) or
    [`i_search()`](`great_tables.GTI.i_search`)), which only `GTI` tables have.

    A `GTI` table is always rendered as interactive HTML: the table's own HTML, made as for a `GT`
    table, inside a `<gt-table>` element that adds the controls. The element needs no other
    libraries, and the table can be read before (or without) its script running. A `GTI` table
    can't be saved as an image or a PDF, or rendered as LaTeX; for those, use a `GT` table.

    To make a published `GT` table browsable (sortable, searchable, filterable, and paged), with the
    options R gt has for that, [`opt_interactive()`](`great_tables.GT.opt_interactive`) may be all
    that's needed; it renders the table with the same engine. `GTI` is for a table that's an
    interface, one readers work with, and [`GTI.from_gt()`](`great_tables.GTI.from_gt`) turns a
    `GT` table into one.

    A table of a lazy frame (a Polars LazyFrame, a DuckDB relation or an Ibis table) is made,
    formatted and styled as any other, but its rows are collected only as they're shown. Shown as
    a widget (with [`i_as_widget()`](`great_tables.GTI.i_as_widget`)) or in a Shiny app (with
    [`render_gt()`](`great_tables.shiny.render_gt`)), a table of more rows than the browser is
    quick with keeps them in Python (see [`i_scale()`](`great_tables.GTI.i_scale`)): each view is
    found with a query on the frame, and only the rows of the page shown are collected, formatted
    and rendered. Anywhere else (or with few rows), all the rows are collected and the table is
    shown as a table of them would be.

    The table is made again from the rows shown, by the same methods: so what depends on every row
    can't be used (`data_color()`, a footnote on the body or the stub, or rows chosen by their
    positions, rather than by an expression or their names in the stub); and a method that looks
    at the rows it's given looks only at the page's (as an expression of a column's mean does, in
    `tab_style()`'s rows, or `cols_align_decimal()`, or a nanoplot's scale). A table with summary
    rows or row groups has all its rows collected. In Python, its search, and its filters'
    "contains" and "matches" clauses, match the rows' values as text (e.g., `1000.5`), not the
    text of their cells (`1,000.50`), and a missing value matches nothing.

    A DuckDB relation's or an Ibis table's rows have no order that's kept from one query to the
    next, so they're shown in the order of their values: sorted by the columns of `order_by=`,
    then by every other column (but those of lists, structs and objects). A Polars LazyFrame's are
    in its own order, unless it's given an `order_by=`. The collected rows, and their data (as
    the widget's `view()` gives it), are of the frame's backend: a Polars DataFrame, for a
    LazyFrame, and a PyArrow table, for DuckDB and Ibis.

    :::{.callout-warning}
    `GTI()` is experimental: its methods, and what they do, may change.
    :::

    Parameters
    ----------
    data
        A DataFrame object, or a lazy frame: a Polars LazyFrame, a DuckDB relation or an Ibis table
        (whose rows are collected as they're shown: see above).
    rowname_col
        The column name in the input `data=` table to use as row labels to be placed in the table
        stub. A list of column names creates a hierarchical stub.
    groupname_col
        The column name in the input `data=` table to use as group labels for generation of row
        groups.
    auto_align
        Optionally have column data be aligned depending on the content contained in each column of
        the input `data=`.
    id
        By default (with `None`) the table ID will be a random, ten-letter string as generated
        through internal use of the `random_id()` function. A custom table ID can be used here by
        providing a string.
    locale
        An optional locale identifier that can be set as the default locale for all functions that
        take a `locale` argument.
    preset
        The settings the table starts with: `"report"` (the default) for a table to be read, with
        the controls above; or `"explorer"` for a look through data, as if made with
        `i_cols_filter()` and `i_cols_profile()` (every column filtered and profiled, as its kind
        suggests), `i_cols_controls(hideable=True, reorderable=True)` (every column can be hidden
        and moved), `i_display(compact=True)`, `i_export("csv")` and `i_inspect()` (row numbers,
        dtypes under the labels, the number of rows and columns, and missing values tinted). The
        stub is left out of these, as those methods leave it out. The `i_` methods change a preset
        as they change any table: each sets all of its feature's settings (so `i_display(wrap=False)`
        on an explorer makes its rows less compact, unless it's given `compact=True` too), and the
        `i_cols_` methods set those of the columns they're given.
    order_by
        For a lazy frame, the columns its rows are in the order of (and numbered by): the rows sort
        by them first, then by the frame's other columns (see above). A column of unique values
        (an ID) is best, which leaves them nothing to sort. Not for a DataFrame (which can be
        sorted first, for the table).

    Returns
    -------
    GTI
        A GTI object is returned.

    Examples
    --------
    Out of the box, a `GTI` table can be sorted by its columns (with the arrows under their labels),
    searched, and paged through, ten rows at a time, and its columns can be resized.

    ```{python}
    from great_tables import GTI
    from great_tables.data import towny

    towny_mini = towny[["name", "status", "csd_type", "population_2021"]]

    GTI(towny_mini, rowname_col="name").fmt_integer(columns="population_2021")
    ```

    The `i_` methods change what readers can do. Here, they get 25 rows to a page and can select
    rows, and the table is compact.

    ```{python}
    (
        GTI(towny_mini, rowname_col="name")
        .fmt_integer(columns="population_2021")
        .i_pagination(page_size=25)
        .i_selection("multiple")
        .i_display(compact=True)
    )
    ```

    With `preset="explorer"`, the table is set up for looking through data: each column can be
    filtered (from the button by its label) and has a profile of its values, with its dtype, the
    rows are numbered and compact, missing values are tinted, and the rows can be downloaded.

    ```{python}
    from great_tables.data import gtcars

    GTI(gtcars[["mfr", "model", "year", "hp", "msrp", "ctry_origin"]], preset="explorer")
    ```

    A `GT` table can be made into a `GTI` table with [`GTI.from_gt()`](`great_tables.GTI.from_gt`).

    A table of a Polars LazyFrame keeps its rows there until they're shown.

    ```python
    import polars as pl
    from great_tables import GTI

    lf = pl.scan_parquet("trips.parquet")

    GTI(lf).fmt_number(columns="fare", decimals=2).i_cols_filter("payment").i_as_widget()
    ```

    And so does a table of a DuckDB relation, in DuckDB, its rows in the order of a column of IDs.

    ```python
    import duckdb

    trips = duckdb.read_parquet("trips.parquet")

    GTI(trips, order_by="trip_id").i_cols_filter("payment").i_as_widget()
    ```
    """

    def __init__(
        self,
        data: Any,
        rowname_col: str | list[str] | None = None,
        groupname_col: str | None = None,
        auto_align: bool = True,
        id: str | None = None,
        locale: str | None = None,
        preset: Preset = "report",
        order_by: str | list[str] | None = None,
    ):
        if preset not in PRESETS:
            raise ValueError(f'`preset=` must be "report" or "explorer", not {preset!r}.')
        init = {
            "rowname_col": rowname_col,
            "groupname_col": groupname_col,
            "auto_align": auto_align,
            "id": id,
            "locale": locale,
        }
        lazy = None
        if _is_lazy_frame(data):
            # (Made over a frame of its columns, without rows, and made again from the rows shown:
            # see `_gti/_lazy.py`)
            from ._gti._lazy import lazy_table

            data, lazy = lazy_table(data, init, order_by)
        elif order_by is not None:
            raise ValueError(
                "`order_by=` orders a lazy frame's rows, and this data isn't one: sort it first."
            )
        super().__init__(data, **init)
        if lazy is not None:
            object.__setattr__(self, "_boxhead", lazy.boxhead)
        object.__setattr__(self, "_lazy", lazy)
        # (Kept apart from the table's options, which are `GT`'s; frozen, as the table is)
        object.__setattr__(self, "_interactive", Settings())
        if preset == "explorer":
            explorer = (
                self.i_cols_filter()
                .i_cols_profile()
                .i_cols_controls(hideable=True, reorderable=True)
                .i_display(compact=True)
                .i_export("csv")
                .i_inspect()
            )
            object.__setattr__(self, "_interactive", explorer._interactive)

    _interactive: Settings
    _lazy: Lazy | None

    @classmethod
    def from_gt(cls, gt: GT) -> GTI:
        """
        Make an interactive table from a `GT` table.

        The new `GTI` table has everything the `GT` table has (its data, formats, styles, and
        options). Readers can do with it what they can with any new `GTI` table, unless
        [`opt_interactive()`](`great_tables.GT.opt_interactive`) was used on the `GT` table: then
        they can do what it set (sorting, searching, filtering, and so on), with `GTI`'s control
        bar, page controls and way of fitting a narrow container.

        Parameters
        ----------
        gt
            A `GT` table.

        Returns
        -------
        GTI
            A new GTI object.

        Examples
        --------
        A table made with `GT()` can become interactive at the end.

        ```{python}
        from great_tables import GT, GTI
        from great_tables.data import towny

        gt_tbl = GT(towny[["name", "population_2021"]]).fmt_integer(columns="population_2021")

        GTI.from_gt(gt_tbl)
        ```
        """
        if isinstance(gt, GTI):
            return gt
        if not isinstance(gt, GT):
            raise TypeError(f"`GTI.from_gt()` needs a `GT` table, not {type(gt).__name__!r}.")

        if gt._options.ihtml_active.value:
            # (With GTI's control bar, page controls and responsive layout)
            settings = replace(
                settings_of(gt),
                pagination_type=Settings().pagination_type,
                bar=True,
                responsive=Settings().responsive,
            )
        else:
            settings = Settings()

        new = cls.__new__(cls)
        new.__dict__.update(gt.__dict__)
        object.__setattr__(new, "_interactive", settings)
        return new

    def _set_interactive(self, **changes: Any) -> Self:
        return self._replace(_interactive=replace(self._interactive, **changes))

    # -----
    # The `i_` methods: each sets all of one feature's settings (those not given go back to their
    # defaults), so that what a table does doesn't depend on the order of the calls (but for the
    # `i_cols_` ones, which set the settings of the columns given, as `fmt_*()` methods do)

    def i_sorting(self, enabled: bool = True) -> Self:
        """
        Let readers sort the table by its columns.

        A column is sorted with the arrows under its label (or by clicking the label itself): once
        for ascending order, again for descending, and a third time to go back to the table's own
        order. With Shift held, a column is added to the sort (and is sorted within the columns
        before it). Rows are sorted by the column's values, not by how they're formatted, and stay
        in their row groups. The info panel (from the (i) button in the control bar) says how the
        table is sorted, and can put it back in its own order. Sorting is on by default; some
        columns can be left unsortable with
        [`i_cols_controls()`](`great_tables.GTI.i_cols_controls`).

        Parameters
        ----------
        enabled
            Whether readers can sort the table.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table that keeps its rows in their order.

        ```{python}
        from great_tables import GTI, exibble

        GTI(exibble[["num", "char", "fctr"]]).i_sorting(False)
        ```
        """
        return self._set_interactive(sorting=_flag(enabled, "enabled"))

    def i_search(self, enabled: bool = True) -> Self:
        """
        Let readers search the table.

        A search shows only the rows with a cell that has the text searched for (as it's shown in
        the table, ignoring case and accents), and highlights the matches. The search is a button
        in the control bar below the table (or the `/` key, from within the table), which opens a
        search field; Esc clears the search, then closes the field. Searching is on by default;
        some columns can be left out of it with
        [`i_cols_controls()`](`great_tables.GTI.i_cols_controls`).

        Parameters
        ----------
        enabled
            Whether readers can search the table.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table without a search.

        ```{python}
        from great_tables import GTI, exibble

        GTI(exibble[["num", "char", "fctr"]]).i_search(False)
        ```
        """
        return self._set_interactive(search=_flag(enabled, "enabled"))

    def i_resizing(self, enabled: bool = True) -> Self:
        """
        Let readers resize the table's columns.

        A column is resized by dragging the handle at the end of its label (or, with the handle
        focused, with the arrow keys); double-clicking the handle sets the column back to its own
        width. Resizing is on by default; some columns can be kept at their width with
        [`i_cols_controls()`](`great_tables.GTI.i_cols_controls`).

        Parameters
        ----------
        enabled
            Whether readers can resize the table's columns.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table with columns of a fixed width.

        ```{python}
        from great_tables import GTI, exibble

        GTI(exibble[["num", "char", "fctr"]]).i_resizing(False)
        ```
        """
        return self._set_interactive(resizing=_flag(enabled, "enabled"))

    def i_pagination(
        self,
        enabled: bool = True,
        *,
        page_size: int = 10,
        page_sizes: list[int] | tuple[int, ...] | None = (10, 25, 50, 100),
        info: bool = True,
    ) -> Self:
        """
        Split the table's rows into pages.

        With pagination, readers see a page of rows at a time, with arrows in the control bar below
        the table to go from page to page (as do the arrow keys, Page Up and Page Down, and Home
        and End, in the bar). Between the arrows is the page and the number of pages, which can be
        clicked to type the page to go to. Each page is as tall as a full one, so the controls stay
        in place. The (i) button at the end of the bar opens the table's info panel, which says
        which rows are shown and has the choice of page size. Readers can also drag the foot of
        the page's rows (the line between the last row and the grand summary rows or footer) down
        or up, for a row more or fewer on each page, from one row to all of them, or focus it and
        use the arrow keys; Enter or a double click on it goes back to `page_size`, as does the
        bar's reset. Pagination is on by default, with ten rows to a page.

        Parameters
        ----------
        enabled
            Whether the rows are split into pages. Without pagination, all of the rows are shown.
        page_size
            How many rows are on a page, to begin with.
        page_sizes
            The page sizes readers can choose from, in the info panel (as well as `page_size`).
            With `None` (or none at all), readers can't change the page size (and there's no
            handle to drag at the foot of the rows).
        info
            Whether the info panel says which rows are shown (as in "21–30 of 215 rows").

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table with 20 rows to a page, which readers can change to 50.

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        GTI(towny[["name", "population_2021"]]).i_pagination(page_size=20, page_sizes=[20, 50])
        ```
        """
        enabled = _flag(enabled, "enabled")
        info = _flag(info, "info")
        page_size = _page_size(page_size, "page_size")
        # (Not `page_sizes or ()`, which a NumPy array can't answer)
        sizes = () if page_sizes is None else tuple(_page_size(s, "page_sizes") for s in page_sizes)
        return self._set_interactive(
            pagination=enabled,
            page_size=page_size,
            page_sizes=sizes,
            page_size_select=bool(sizes),
            page_info=info,
        )

    def i_selection(self, mode: SelectionMode | None = "multiple") -> Self:
        """
        Let readers select the table's rows.

        Rows are selected by clicking them or their checkboxes, in a column before the others. With
        `"single"`, selecting a row clears the one selected before; with `"multiple"`, Shift-click
        selects a range of rows, and a checkbox in the column labels selects every row that matches
        the search. The info panel (from the (i) button in the control bar) says how many rows are
        selected, and can clear the selection. Selection is off by default.

        Parameters
        ----------
        mode
            One of `"multiple"` (several rows), `"single"` (one row at a time), or `None` (no rows
            can be selected).

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table where readers can select one row at a time.

        ```{python}
        from great_tables import GTI, exibble

        GTI(exibble[["num", "char", "fctr"]]).i_selection("single")
        ```
        """
        if mode is not None and mode not in SELECTION_MODES:
            raise ValueError(
                f'`mode=` must be "multiple", "single", or `None` (no selection), not {mode!r}.'
            )
        return self._set_interactive(selection=mode)

    def i_scroll(self, height: str | float | None) -> Self:
        """
        Make the table's body scroll, within a height.

        The table takes up no more than `height`, and its body scrolls within it, with the column
        labels (and the table's header) staying in view. By default, a table grows with its rows.

        With the control bar, readers can drag the foot of the body down or up (or use the arrow
        keys and Page Up and Page Down on it) for a taller or shorter one: from a row's height to
        all of the rows. Double-clicking it (or pressing Enter) puts `height` back, as resetting
        the view does; the height is kept with the view (see
        [`i_view_state()`](`great_tables.GTI.i_view_state`)).

        Parameters
        ----------
        height
            The most the table can take up: a CSS length (e.g., `"400px"` or `"60vh"`) or a number
            of pixels. With `None` (or `"auto"`), the table grows with its rows.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table of all its rows, in a body that scrolls.

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        GTI(towny[["name", "population_2021"]]).i_pagination(False).i_scroll(400)
        ```
        """
        if height is None or height == "auto":
            return self._set_interactive(height=None)
        if not _is_height(height):
            raise ValueError(
                '`height=` must be a CSS length (e.g., "400px" or "60vh"), a number of pixels, or '
                f"`None`, not {height!r}."
            )
        # (A number is of pixels, as with `tab_options()`)
        return self._set_interactive(height=height if isinstance(height, str) else f"{height}px")

    def i_responsive(self, mode: ResponsiveMode = "auto", *, stack_below: float = 420) -> Self:
        """
        Set how the table fits a narrow container.

        A table wider than its container can scroll sideways, with its stub (and any pinned
        columns) staying in view (`"scroll"`). Or, in a container narrower than `stack_below`
        pixels (on a phone, say), it can be stacked (`"stack"`): each row becomes a card, titled by
        its stub, with each column's label next to its value (labels under a spanner are prefixed
        with it). Row groups become headings between the cards, and summary rows become cards of
        their own. The table is stacked by its CSS alone, so it's stacked before its script runs
        (or without it); once it runs, the column labels are shown above the cards as chips, which
        readers can sort and filter by as with the labels themselves.

        Or it can drop columns until it fits (`"collapse"`): those without a priority first (from
        the last), then those with the highest numbers, as
        [`i_cols_priority()`](`great_tables.GTI.i_cols_priority`) set them. Each row then has a
        button by its first cell that shows the columns dropped from it, under it, as labels and
        values. Columns come back as the container widens. A column is never dropped if it has
        priority 1, nor the stub (or the row group column); with only those left, the table
        scrolls. Dropped columns are still searched, filtered and exported, and they're dropped by
        the table's script, so without it the table scrolls.

        With `"auto"` (the default), the table drops columns if any have a priority; otherwise
        it's stacked if it shows no more than six columns (not counting the stub), and scrolls if
        it shows more. With `"stack"` or `"auto"`, a table in a container as wide as `stack_below`
        or wider is as with `"scroll"`. So is one in a container that's only as wide as what's in
        it (a table's cell, or an inline block), once its script runs: before that, such a table
        has no width.

        Whatever the mode, on a touch screen, a control bar narrower than 30em (480 pixels, at 16px text) folds
        its search, its filters as text and its "Columns" button into one "Filter & sort" button,
        which opens a sheet from the foot of the window with all of them, and the table's sort and
        filters. A long press on a column's label opens a sheet for that column (to sort it, filter
        it, or hide it), while a tap still sorts by it.

        Parameters
        ----------
        mode
            How the table fits a narrow container: `"scroll"`, `"stack"`, `"collapse"`, or
            `"auto"`.
        stack_below
            The container width (in pixels) below which the table is stacked, with `"stack"` or
            `"auto"`.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table that's stacked in a container narrower than 420 pixels (narrow the window
        to see its cards).

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        towny_mini = towny[["name", "status", "population_2021", "density_2021"]]

        GTI(towny_mini, rowname_col="name").i_responsive("stack")
        ```

        And a wider one that drops its columns from the last as the window narrows, keeping the
        latest population (narrow the window, then use a row's button to see what it dropped).

        ```{python}
        years = [f"population_{year}" for year in (1996, 2001, 2006, 2011, 2016, 2021)]

        (
            GTI(towny[["name", "status", *years]].head(10), rowname_col="name")
            .fmt_integer(columns=years)
            .i_cols_priority(columns="population_2021")
            .i_responsive("collapse")
        )
        ```
        """
        if mode not in RESPONSIVE_MODES:
            raise ValueError(
                f'`mode=` must be "scroll", "stack", "collapse", or "auto", not {mode!r}.'
            )
        return self._set_interactive(
            responsive=mode, stack_below=_width(stack_below, "stack_below")
        )

    def i_display(
        self, *, highlight: bool = True, compact: bool = False, wrap: bool = True
    ) -> Self:
        """
        Set how the table's rows look.

        Parameters
        ----------
        highlight
            Whether the row under the pointer (or the row tapped, on a touch screen) is highlighted.
        compact
            Whether the rows are compact, with half of their usual padding above and below (where
            it hasn't been set, as with `tab_options(data_row_padding=)`).
        wrap
            Whether the text in cells wraps. Without wrapping, the text is on one line, cut short
            (with an ellipsis) if it doesn't fit.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a compact table, without highlighting.

        ```{python}
        from great_tables import GTI, exibble

        GTI(exibble[["num", "char", "fctr"]]).i_display(highlight=False, compact=True)
        ```
        """
        return self._set_interactive(
            highlight=_flag(highlight, "highlight"),
            compact=_flag(compact, "compact"),
            wrap=_flag(wrap, "wrap"),
        )

    def i_inspect(
        self,
        *,
        row_numbers: bool = True,
        dtypes: bool = True,
        dimensions: bool = True,
        missing: bool = True,
    ) -> Self:
        """
        Show readers what's in the data: its rows' numbers, its columns' dtypes, its size, and where
        its values are missing.

        Row numbers are in a narrow column before the others (with the rows' checkboxes, with
        [`i_selection()`](`great_tables.GTI.i_selection`)), pinned with the stub as the table
        scrolls sideways: each row's is its place in the data, from 1, which stays with it as the
        rows are sorted, filtered and paged. A dtype is under its column's label, as a short name
        (as Polars prints it, for any DataFrame library): `"i64"`, `"f64"`, `"str"`, `"bool"`,
        `"cat"`, `"date"`, `"datetime"`, and so on. The dimensions are above the table: its number
        of rows and columns (those shown, of the stub and the data), and how many of them are
        left as readers search, filter and hide columns ("12 of 47 rows × 6 columns"). A missing
        value (`None`, or NaN in a column of floats) has its cell tinted, whatever the cell shows
        (as [`sub_missing()`](`great_tables.GT.sub_missing`) makes it). None of these are
        searched or exported, and they're all off by default (but in `GTI(preset="explorer")`).

        Like the other `i_` methods (but for the `i_cols_` ones), a call sets all of these: those
        not given are shown.

        Parameters
        ----------
        row_numbers
            Whether each row has its number, in a column before the others.
        dtypes
            Whether each column's dtype is under its label.
        dimensions
            Whether the number of rows and columns is above the table.
        missing
            Whether the cells of missing values are tinted.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table with every one of these: sort it, and the rows keep their numbers.

        ```{python}
        from great_tables import GTI, exibble

        GTI(exibble[["num", "char", "fctr", "date"]]).sub_missing().i_inspect()
        ```

        The row numbers alone:

        ```{python}
        GTI(exibble[["num", "char", "fctr"]]).i_inspect(dtypes=False, dimensions=False, missing=False)
        ```
        """
        return self._set_interactive(
            row_numbers=_flag(row_numbers, "row_numbers"),
            dtypes=_flag(dtypes, "dtypes"),
            dimensions=_flag(dimensions, "dimensions"),
            missing=_flag(missing, "missing"),
        )

    def i_cols_filter(self, columns: SelectExpr = None, type: FilterType | None = "auto") -> Self:
        """
        Let readers filter the table by its columns.

        A filtered column has a filter button in its label, which opens the column's filter. Its
        rows are filtered by the text they show (`"text"`: those with a cell containing what's
        typed, ignoring case and accents, as the search does), by a choice of the column's values
        (`"facet"`: a checklist of them, each with the number of rows that have it, given the
        other filters and the search), by a range of its numbers (`"range"`: at least one value,
        and at most another), by a range of its dates (`"date"`: from one date, to another,
        picked in date fields, or date and time fields for a column with times), or by one of its
        booleans (`"bool"`: any value, true, false, or missing, with the number of rows that have
        each, and their text as the table shows it). The facets, ranges, date ranges and booleans
        go by the column's values, not by how they're formatted. Rows are shown when they
        pass every filter, and the search; the info panel (from the (i) button in the control bar)
        says how many filters there are, and can clear them. The bar also shows the filters that are on, and its <> button opens them as
        text, a query as [`i_view()`](`great_tables.GTI.i_view`) takes it, which readers can edit
        (with suggestions as they type). Filters are off by default.

        Each call sets the filters of the columns it's given, so that some columns can be filtered
        one way, and others another; a later call for a column replaces what an earlier one set.

        Parameters
        ----------
        columns
            The columns to filter by: a column name, a list of them, or a selector (e.g., Polars'
            `cs.numeric()`). With `None` (the default), every column but the stub (which can be
            named). The row group column can't be filtered.
        type
            How the columns are filtered: `"text"`, `"facet"`, `"range"` (for columns of
            numbers), `"date"` (for columns of dates, or dates and times without a time zone), or
            `"bool"` (for columns of booleans), or `"auto"` to choose by the column: a range for
            numbers, a date range for dates, a bool filter for booleans, a facet for categories
            (and text columns with only a few values, each repeated), and text otherwise. With
            `None`, the columns aren't filtered.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table of Ontario's municipalities that can be filtered by status (a facet, as
        there are only a few of them) and population (a range).

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .i_cols_filter(columns=["status", "population_2021"])
        )
        ```

        A column of dates (here, made from the dataset's text) is filtered by a date range, from
        one date to another.

        ```{python}
        import pandas as pd
        from great_tables.data import sp500

        sp500_2015 = sp500[sp500["date"] >= "2015-01-01"].assign(
            date=lambda df: pd.to_datetime(df["date"])
        )

        (
            GTI(sp500_2015[["date", "open", "close"]])
            .fmt_date(columns="date", date_style="month_day_year")
            .fmt_currency(columns=["open", "close"])
            .i_cols_filter(columns="date")
        )
        ```

        A column of booleans (here, whether a nuclide is stable) is filtered by one of its values,
        shown as the table shows them.

        ```{python}
        from great_tables.data import nuclides

        nuclides_mini = nuclides[["nuclide", "z", "n", "is_stable"]].head(20).assign(
            is_stable=lambda df: df["is_stable"] == "TRUE"
        )

        (
            GTI(nuclides_mini)
            .fmt_tf(columns="is_stable", tf_style="yes-no")
            .i_cols_filter(columns="is_stable")
        )
        ```
        """
        if type is not None and type not in FILTER_TYPES:
            raise ValueError(
                '`type=` must be "auto", "text", "facet", "range", "date", "bool", or `None` (no '
                f"filter), not {type!r}."
            )
        selected = resolve_cols_c(self, columns, excl_stub=False)
        for column in selected:
            kind = _get_column_kind(self._tbl_data, column)
            if type == "range" and kind != "number":
                raise ValueError(
                    f"Column {column!r} can't be filtered by a range, which is for columns of "
                    f'numbers (its values are of the {kind!r} kind). Try `type="facet"` or '
                    '`type="text"`.'
                )
            if type == "facet" and kind == "other":
                raise ValueError(
                    f"Column {column!r} can't be filtered by a facet: its values can't be told "
                    'apart and ordered. Try `type="text"`.'
                )
            if type == "date" and kind not in ("date", "datetime"):
                raise ValueError(
                    f"Column {column!r} can't be filtered by a date range, which is for columns "
                    f"of dates, or dates and times (its values are of the {kind!r} kind). Try "
                    '`type="facet"` or `type="text"`, or make its values dates.'
                )
            if type == "bool" and kind != "boolean":
                raise ValueError(
                    f"Column {column!r} can't be filtered by a bool filter, which is for columns "
                    f"of booleans (its values are of the {kind!r} kind). Try "
                    '`type="facet"` or `type="text"`.'
                )
            if type == "date" and kind == "datetime" and _has_time_zone(self._tbl_data, column):
                raise ValueError(
                    f"Column {column!r} can't be filtered by a date range: its dates and times "
                    'have a time zone, which a date range can\'t have yet. Try `type="text"`.'
                )

        filters = dict(self._interactive.filters)
        for column in selected:
            filters.pop(column, None)
            if type is not None:
                filters[column] = type
        return self._set_interactive(filters=tuple(filters.items()))

    def i_cols_controls(
        self,
        columns: SelectExpr = None,
        *,
        sortable: bool | None = None,
        searchable: bool | None = None,
        resizable: bool | None = None,
        hideable: bool | None = None,
        reorderable: bool | None = None,
        groupable: bool | None = None,
        display: bool | None = None,
        data_color: DataColorMode | None = None,
    ) -> Self:
        """
        Choose which columns readers can sort by, search, resize, hide, move, and group the rows by,
        which are only for querying, and whose colors follow the rows kept.

        Where the table lets readers sort it ([`i_sorting()`](`great_tables.GTI.i_sorting`)),
        search it ([`i_search()`](`great_tables.GTI.i_search`)), and resize its columns
        ([`i_resizing()`](`great_tables.GTI.i_resizing`)), they can do so with every column, by
        default. This leaves some columns out: an unsortable column's label has no sort button
        (though the column can still be filtered, and [`i_view()`](`great_tables.GTI.i_view`)
        can still sort by it), the search doesn't look in (or highlight) an unsearchable column's
        cells (though its own filter does), and an unresizable column's label has no handle.

        Readers can't hide any column, by default. Making some hideable puts a "Columns" button in
        the control bar, whose panel has a checkbox for each of them, to hide it or show it again.
        A hidden column's cells are hidden in every row (with a spanner over only hidden columns),
        the search doesn't look in it, and exports leave it out, but a filter on it still keeps
        the rows it keeps. The stub and the row group column can't be hidden (naming them for
        `hideable=` does nothing), and neither can columns
        [`cols_hide()`](`great_tables.GT.cols_hide`) hid, which aren't in the table at all.

        Nor can readers move any column, by default. Making some reorderable lists them in the
        "Columns" panel too, in the order shown, where each can be dragged to another place, or
        moved one place at a time with its arrow buttons (or Alt+↑ and Alt+↓). A column's cells
        move in every row, and exports have the columns in the order shown. A column moves only
        among the reorderable columns next to it with the same spanners over them (and pinned to
        the same side, if pinned): it can't leave its spanner, or pass a column readers can't move.
        The author's order (as [`cols_move()`](`great_tables.GT.cols_move`) and the like set it)
        is the one the table is first shown in, and the one resetting the view goes back to. The
        stub and the row group column can't be moved (naming them for `reorderable=` does
        nothing).

        Nor can readers group the rows by any column, by default. Making some groupable puts a
        "Group rows" button in the control bar, whose panel lists them (and "None"), to group the
        rows by one of them: each of its values gets a heading (with its text, as its first row's
        cell shows it, and the number of rows the search and filters keep), and the rows with it
        come under it, sorted as the table is. The groups are in the order of their values
        (ascending, or descending if the table is sorted by the column so), with the rows missing
        a value last, under "(Missing)". On a page, each group with rows on it has its heading. The
        grouping is part of the view, as [`i_view()`](`great_tables.GTI.i_view`) can set it. A
        column the table can't be sorted by (one of images, say) can't be grouped by, nor can the
        stub (naming them for `groupable=` does nothing), and a table with row groups or summary
        rows can't have any groupable column.

        A column can also be left out of the table but kept for querying, with `display=False`.
        It isn't shown (as with [`cols_hide()`](`great_tables.GT.cols_hide`), and readers can't
        show it), but a filter on it ([`i_cols_filter()`](`great_tables.GTI.i_cols_filter`))
        works, from the query bar, and the table can be sorted by it, as by an unsortable column
        (with [`i_view()`](`great_tables.GTI.i_view`), or by a view kept in the URL). Its filter
        goes by the text its cells would show (a facet lists its values with that text, too). The
        search doesn't look in it, and exports leave it out, but the code copied for the view
        filters and sorts by it. This is also how a column that `cols_hide()` hid can be kept for
        querying. The stub and the row group column can't be left out (naming them for
        `display=False` is an error), and neither can every column of a table without a stub.

        A column's colors from [`data_color()`](`great_tables.GT.data_color`) are made from
        all of its rows, and stay as they are when the rows are searched or filtered, by default
        (`data_color="keep"`). With `data_color="recompute"`, they're made again from the rows the
        search and filters keep (and a linked table's selection, with
        [`i_link()`](`great_tables.GTI.i_link`)), as `data_color()` would make them from those rows
        alone, so that its whole palette is spread over them (the table's first colors come back
        once every row is shown again). Sorting the rows or turning the page doesn't change them.
        Only colors that depend on the rows can change: those `data_color()` made down a column
        (not with `direction="row"`), from a domain it found in the values (not with `domain=`,
        nor from an ordered categorical's levels), and without `fn=`. A missing value keeps its
        `na_color=`, and a cell a later style colors (with `tab_style()`, or another
        `data_color()`) keeps that style's colors.

        Each call sets what it's given for the columns it's given, so that some columns can be
        left out of one thing, and others another; a later call for a column replaces what an
        earlier one set.

        Parameters
        ----------
        columns
            The columns: a column name, a list of them, or a selector (e.g., Polars'
            `cs.numeric()`). With `None` (the default), every column but the stub (which can be
            named). The row group column can't be one of them.
        sortable, searchable, resizable, hideable, reorderable, groupable
            Whether readers can sort by the columns, search them, resize them, hide them, move
            them, and group the rows by them. With `None` (the default), the columns are left as
            they are.
        display
            Whether the columns are in the table (`True`), or left out of it and kept only for
            querying (`False`). With `None` (the default), the columns are left as they are.
        data_color
            Whether the columns' colors from `data_color()` stay as they are when the rows are
            searched or filtered (`"keep"`), or are made again from the rows kept (`"recompute"`).
            With `None` (the default), the columns are left as they are.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table of Ontario's municipalities whose search looks only at their names, and
        that can't be sorted by status.

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .i_cols_controls(columns=["status", "population_2021"], searchable=False)
            .i_cols_controls(columns="status", sortable=False)
        )
        ```

        A wider table whose readers can hide any of its census years, from the "Columns" button
        in the control bar:

        ```{python}
        years = [f"population_{year}" for year in range(1996, 2022, 5)]

        (
            GTI(towny[["name", *years]].head(10), rowname_col="name")
            .fmt_integer(columns=years)
            .i_cols_controls(columns=years, hideable=True)
        )
        ```

        The same years, which readers can put in another order (but not the municipality's status,
        which stays first):

        ```{python}
        (
            GTI(towny[["name", "status", *years]].head(10), rowname_col="name")
            .fmt_integer(columns=years)
            .i_cols_controls(columns=years, reorderable=True)
        )
        ```

        A table whose readers can group the municipalities by their status, from the "Group rows"
        button in the control bar:

        ```{python}
        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .i_cols_controls(columns="status", groupable=True)
        )
        ```

        A table of the municipalities' names and populations that can be filtered by their status,
        which it doesn't show (the filter is in the query bar, from the `<>` button in the control
        bar):

        ```{python}
        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .i_cols_controls(columns="status", display=False)
            .i_cols_filter(columns="status")
            .i_view(filter='status in ("single-tier")')
        )
        ```

        A table whose populations are colored from the rows the search keeps: search for "lake",
        and the darkest blue goes to the most populous of the municipalities named for one
        (Kawartha Lakes), rather than to Toronto.

        ```{python}
        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .data_color(columns="population_2021", palette="Blues")
            .i_cols_controls(columns="population_2021", data_color="recompute")
        )
        ```
        """
        # (Each setting keeps the columns readers can't do it with (and `query_only`, those not
        # shown), but `hideable`, `reorderable` and `groupable` keep those they can, so they're
        # turned around)
        hide = _optional_flag(hideable, "hideable")
        move = _optional_flag(reorderable, "reorderable")
        group = _optional_flag(groupable, "groupable")
        if data_color is not None and data_color not in DATA_COLOR_MODES:
            raise ValueError(
                f'`data_color=` must be "keep", "recompute", or `None`, not {data_color!r}.'
            )
        flags = {
            "unsortable": _optional_flag(sortable, "sortable"),
            "unsearchable": _optional_flag(searchable, "searchable"),
            "unresizable": _optional_flag(resizable, "resizable"),
            "hideable": None if hide is None else not hide,
            "reorderable": None if move is None else not move,
            "groupable": None if group is None else not group,
            "query_only": _optional_flag(display, "display"),
            "recolor": None if data_color is None else data_color == "keep",
        }
        if display is False:
            # (The stub and the row group column are what the rows are known by)
            named = resolve_cols_c(self, columns, excl_stub=False, excl_group=False)
            kept = [
                column
                for kind in (ColInfoTypeEnum.stub, ColInfoTypeEnum.row_group)
                for column in self._boxhead.vars_from_type(kind)
                if column in named
            ]
            if kept:
                raise ValueError(
                    f"The stub and the row group column can't be left out of the table, so "
                    f"`display=False` can't be set for {', '.join(map(repr, kept))}."
                )
        selected = resolve_cols_c(self, columns, excl_stub=False)
        changes: dict[str, Any] = {}
        for name, enabled in flags.items():
            if enabled is None:
                continue
            kept = [column for column in getattr(self._interactive, name) if column not in selected]
            changes[name] = tuple(kept if enabled else [*kept, *selected])
        return self._set_interactive(**changes)

    def i_cols_pin(self, columns: SelectExpr = None, side: PinSide | None = "left") -> Self:
        """
        Pin columns to a side of the table, so they stay in view as it scrolls sideways.

        A table wider than its container scrolls sideways, with its stub (and the row group
        column, if row groups are shown as one) pinned to the left, in view. This pins other
        columns too: to the left, after the stub, or to the right. Pinned columns have to be next
        to their side of the table (with only other columns pinned there between them and it), so
        a column further in has to be moved there first, with
        [`cols_move_to_start()`](`great_tables.GT.cols_move_to_start`) or
        [`cols_move_to_end()`](`great_tables.GT.cols_move_to_end`); this is checked when the
        table is made, after any moves. Hidden columns don't count. A spanner over columns on
        both sides of a pinned edge isn't pinned, and neither is the footer.

        Pinned columns can't take up more than half of the table's container: in a narrower one,
        only the stub stays pinned (until the container is wide enough again).

        The sides are those of the columns' order: the left is the stub's side, and the right is
        the other. A table shown right to left (in a page that's written that way) has its stub on
        the right, and so its columns pinned to the "left" are on the right, by the stub.

        Each call pins (or unpins) the columns it's given, so that some columns can be pinned to
        one side, and others to the other; a later call for a column replaces what an earlier one
        set.

        Parameters
        ----------
        columns
            The columns to pin: a column name, a list of them, or a selector (e.g., Polars'
            `cs.numeric()`). With `None` (the default), every column but the stub. The stub and
            the row group column are always pinned (naming them does nothing).
        side
            The side to pin the columns to: `"left"` (the stub's) or `"right"`. With `None`, the
            columns are unpinned.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a wide table of Ontario's municipalities that keeps each one's status in view, by
        its name, and its latest population at the other side.

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        (
            GTI(towny.drop(columns="website").head(10), rowname_col="name")
            .cols_move_to_end(columns="population_2021")
            .fmt_integer(columns=["population_1996", "population_2021"])
            .i_cols_pin(columns="status")
            .i_cols_pin(columns="population_2021", side="right")
        )
        ```
        """
        if side is not None and side not in PIN_SIDES:
            raise ValueError(
                f'`side=` must be "left", "right", or `None` (unpinned), not {side!r}.'
            )
        selected = resolve_cols_c(self, columns, excl_stub=False)
        pins = dict(self._interactive.pins)
        for column in selected:
            pins.pop(column, None)
            if side is not None:
                pins[column] = side
        return self._set_interactive(pins=tuple(pins.items()))

    def i_cols_priority(self, columns: SelectExpr = None, priority: int | None = 1) -> Self:
        """
        Give columns a priority, for when the table drops columns to fit its container.

        A table that drops columns to fit a narrow container (with
        [`i_responsive("collapse")`](`great_tables.GTI.i_responsive`), or `"auto"`, the default,
        once any column has a priority) drops those without a priority first, from the last; then
        those with the highest numbers (from the last, among those with the same). A column with
        priority 1 is never dropped, and neither are the stub and the row group column. Readers
        can see the columns dropped from a row with the button by its first cell.

        Each call sets (or unsets) the priority of the columns it's given; a later call for a
        column replaces what an earlier one set.

        Parameters
        ----------
        columns
            The columns to give the priority: a column name, a list of them, or a selector (e.g.,
            Polars' `cs.numeric()`). With `None` (the default), every column but the stub. The stub
            and the row group column are never dropped (naming them does nothing).
        priority
            The columns' priority: a positive integer, where 1 (the default) keeps them, and higher
            numbers drop sooner. With `None`, the columns have none, and drop first.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table of Ontario's municipalities that keeps each one's latest population, and
        drops its land area before its status (narrow the window to see them go).

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        (
            GTI(
                towny[["name", "status", "land_area_km2", "population_2021"]].head(10),
                rowname_col="name",
            )
            .fmt_integer(columns="population_2021")
            .i_cols_priority(columns="population_2021")
            .i_cols_priority(columns="status", priority=2)
            .i_cols_priority(columns="land_area_km2", priority=3)
        )
        ```
        """
        if priority is not None:
            priority = _priority(priority)
        selected = resolve_cols_c(self, columns, excl_stub=False)
        priorities = dict(self._interactive.priorities)
        for column in selected:
            priorities.pop(column, None)
            if priority is not None:
                priorities[column] = priority
        return self._set_interactive(priorities=tuple(priorities.items()))

    def i_cols_profile(self, columns: SelectExpr = None, plot: ProfilePlot | None = "auto") -> Self:
        """
        Show how the columns' values are spread, in a small plot under their labels.

        A column's profile is a plot under its label of the values in the rows the table shows:
        a histogram of its numbers or dates (`"histogram"`: how many rows have a value in each of
        up to 20 equal ranges, from the column's lowest value to its highest; or one per value,
        for whole numbers or days a few apart), or bars for its most common values (`"top"`: the
        5 that most rows have, with a bar for the others). Under the plot are the lowest and
        highest values the rows show (for a histogram) or the number of values they have (for the
        others), as the table formats them, and the share of the rows with a missing value.
        Pointing at a bar shows its values and its number of rows. As the reader searches and
        filters the table, the profiles show only the rows that are left (their ranges and
        values stay the same, so that they're easy to compare), but not as the table is sorted,
        or paged. Profiles are off by default, and aren't shown in a table stacked as cards.

        Each call sets the profiles of the columns it's given, so that some columns can have one
        plot, and others another; a later call for a column replaces what an earlier one set.

        Parameters
        ----------
        columns
            The columns to profile: a column name, a list of them, or a selector (e.g., Polars'
            `cs.numeric()`). With `None` (the default), every column but the stub (which can be
            named). The row group column can't be profiled, and neither can a column left out of
            the table.
        plot
            The plot: `"histogram"` (for columns of numbers, dates, or dates and times), or
            `"top"` (the most common values), or `"auto"` to choose by the column: a histogram for
            numbers and dates, and the most common values otherwise. With `None`, the columns
            have no profile.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table of Ontario's municipalities with a profile of their statuses (their most
        common ones) and of their populations (a histogram), which follow the rows a search or a
        filter leaves (try searching for "county").

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        (
            GTI(
                towny[["name", "status", "density_2021", "population_2021"]],
                rowname_col="name",
            )
            .fmt_integer(columns=["density_2021", "population_2021"])
            .i_cols_filter(columns="status")
            .i_cols_profile(columns=["status", "density_2021", "population_2021"])
        )
        ```

        A column of dates (here, made from the dataset's text) has a histogram of them, from its
        first date to its last.

        ```{python}
        import pandas as pd
        from great_tables.data import sp500

        sp500_2015 = sp500[sp500["date"] >= "2015-01-01"].assign(
            date=lambda df: pd.to_datetime(df["date"])
        )

        (
            GTI(sp500_2015[["date", "open", "close", "volume"]])
            .fmt_date(columns="date", date_style="month_day_year")
            .fmt_currency(columns=["open", "close"])
            .fmt_number(columns="volume", compact=True)
            .i_cols_profile()
        )
        ```
        """
        if plot is not None and plot not in PROFILE_PLOTS:
            raise ValueError(
                f'`plot=` must be "auto", "histogram", "top", or `None` (no profile), not {plot!r}.'
            )
        selected = resolve_cols_c(self, columns, excl_stub=False)
        for column in selected:
            kind = _get_column_kind(self._tbl_data, column)
            if plot == "histogram" and kind not in ("number", "date", "datetime"):
                raise ValueError(
                    f"Column {column!r} can't have a histogram, which is for columns of numbers, "
                    f"dates, or dates and times (its values are of the {kind!r} kind). Try "
                    '`plot="top"`.'
                )
            if plot == "top" and kind == "other":
                raise ValueError(
                    f"Column {column!r} can't have its most common values shown: its values "
                    "can't be told apart and ordered."
                )

        profiles = dict(self._interactive.profiles)
        for column in selected:
            profiles.pop(column, None)
            if plot is not None:
                profiles[column] = plot
        return self._set_interactive(profiles=tuple(profiles.items()))

    def i_view(
        self,
        filter: str | dict[str, Any] | None = None,
        sort: str | list[str] | None = None,
        hidden: SelectExpr = None,
        group_by: str | None = None,
    ) -> Self:
        """
        Show the table filtered and sorted, as readers first see it.

        The table is first shown with the rows that `filter=` keeps, in the order `sort=` gives
        them, without the columns `hidden=` hides, and with the rows grouped by the column
        `group_by=` names, which readers can then change (with the column filters, sort buttons,
        and the bar's "Columns" and "Group rows" panels) or clear. Rows stay within
        their row groups, as they do when readers sort the table, and a table whose stub has cells
        merged across rows is shown as it is. Without arguments, the table is shown with all its
        rows and columns, in order (the default).

        Parameters
        ----------
        filter
            The filters, as a query: `{"and": [clauses]}`, where a clause is a dictionary with a
            column (`"col"`), an operation (`"op"`), and a value (`"value"`), and keeps the rows
            that it's true of. A clause's column needs a filter (see
            [`i_cols_filter()`](`great_tables.GTI.i_cols_filter`)) of a type that has its
            operation: `"contains"` for a text filter (the value is the text, matched as readers'
            typing is), or `"matches"` (the value is a regular expression, which has a match in
            the text a cell shows, as it is: with its case and accents), `"in"` for a facet (a
            list of values, with `None` for a missing value), and `"gte"` (at least), `"lte"` (at
            most), `"gt"` (more than) and `"lt"` (less than) for a range (a number) or a date
            filter (a date, as `"2015-06-15"`: for a column of dates and times, its midnight, so
            `"gt"` keeps 09:30 that day). A range or date filter has `"top_n"` and `"bottom_n"`
            too, whose value is a whole number, n, at least 1: they keep the rows with the n
            largest (or smallest) values of all the table's rows, and those tied with the n-th
            (so `{"col": "population_2021", "op": "top_n", "value": 10}` keeps the ten most
            populous, and any tied with the tenth), but not a missing value, NaN or an infinity.
            A `"matches"` pattern is in the part of regular
            expressions' syntax that the browser, Polars, pandas and PyArrow read alike:
            characters (`\\` before punctuation for the character itself), `.`, `^` and `$` (the
            start and end of the text), classes as `[a-z]` and `[^0-9]`, `\\d`, `\\w` and `\\s`
            (ASCII's), groups (`(...)` or `(?:...)`) and `|`, and repeats (`*`, `+`, `?`, and
            `{n,m}`); a pattern starting with `(?i)` ignores case. A clause
            `{"col": ..., "op": "is_null"}`, without a value, keeps the rows whose value is missing
            (`None`, or NaN in a column of floats), in a column with any type of filter. A column
            can have one clause of each operation. With `None` (the default), the rows aren't
            filtered.

            A part of the query can be a group instead of a clause: `{"or": [parts]}` keeps the
            rows that any of its parts keeps, `{"and": [parts]}` those that all of them keep, and
            `{"not": part}` those that its part doesn't keep (a row whose value is missing, which
            a clause doesn't keep, is kept by `"not"`). Groups can be in groups, and a column can
            have one clause of each operation in each `"and"`. The column filters show the
            query's clauses, and the bar below the table shows each group (and each `"is_null"`,
            `"matches"`, `"gt"`, `"lt"`, `"top_n"` and `"bottom_n"` clause), which readers can
            edit as text, or remove.

            The query can be written as text instead: clauses joined by `and`, each a column name
            and then `contains` and a string, `matches` and a pattern between slashes, `in` and
            values in parentheses, `>=`, `<=`, `>` or `<` and a number (or a date in double
            quotes), `top` or `bottom` and a whole number, or `is null` (e.g.,
            `'status in ("single-tier") and population_2021 >= 10000'`, `"name matches /^st\\./i"`,
            `"population_2021 top 10"`, or `"population_2016 is null"`; `is not null` is `not` and `is null`, and so are
            `not in`, `not contains` and `not matches`, as in `'status not in ("city")'`). Strings
            are in double quotes, and values are written as in JSON (`null` for a missing value,
            `true` and `false`). A pattern's flag `i` is its `(?i)`, and a `/` in it is escaped
            (`\\/`) but in a class. A column name that isn't letters, digits and underscores goes in
            backticks (`` `Name of town` ``). Groups are written with `or`, `not` and parentheses,
            `not` binding tighter than `and`, and `and` tighter than `or` (e.g.,
            `'population_2021 >= 10000 and (status in ("lower-tier") or not name contains "ton")'`).
        sort
            The columns to sort by: a column name, or a list of them (the first sorts the rows,
            the next sorts the rows that tie, and so on), each in ascending order, or descending
            with a `-` before its name (e.g., `"-population_2021"`). Missing values are last. The
            columns can be sorted even if readers can't sort them
            ([`i_sorting(False)`](`great_tables.GTI.i_sorting`), or
            [`i_cols_controls(sortable=False)`](`great_tables.GTI.i_cols_controls`)). With `None`
            (the default), the rows keep their order.
        hidden
            The columns to hide, which readers can show again: a column name, a list of them, or a
            selector (e.g., Polars' `cs.numeric()`). Readers have to be able to hide them (see
            [`i_cols_controls(hideable=True)`](`great_tables.GTI.i_cols_controls`)). With `None`
            (the default), none are hidden.
        group_by
            The column to group the rows by, which readers can change: a column name. Readers have
            to be able to group the rows by it (see
            [`i_cols_controls(groupable=True)`](`great_tables.GTI.i_cols_controls`)). With `None`
            (the default), the rows aren't grouped.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table of Ontario's municipalities, first showing the single-tier ones with at
        least 10,000 people, most populous first. Readers can change the filters (or clear them)
        in the column labels or the bar below the table, and the sort with the sort buttons.

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .i_cols_filter(columns=["status", "population_2021"])
            .i_view(
                filter={
                    "and": [
                        {"col": "status", "op": "in", "value": ["single-tier"]},
                        {"col": "population_2021", "op": "gte", "value": 10000},
                    ]
                },
                sort="-population_2021",
            )
        )
        ```

        The same view, with its filter written as text:

        ```{python}
        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .i_cols_filter(columns=["status", "population_2021"])
            .i_view(
                filter='status in ("single-tier") and population_2021 >= 10000',
                sort="-population_2021",
            )
        )
        ```

        The single-tier municipalities with at least 100,000 people, and the lower-tier ones with
        at least 50,000, with an `or` group (which the bar shows, as it isn't one column's
        filter):

        ```{python}
        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .i_cols_filter(columns=["status", "population_2021"])
            .i_view(
                filter=(
                    'status in ("single-tier") and population_2021 >= 100000 '
                    'or status in ("lower-tier") and population_2021 >= 50000'
                ),
                sort="-population_2021",
            )
        )
        ```

        A table first shown with only the latest census year, whose readers can show the others
        from the "Columns" button in the control bar:

        ```{python}
        years = [f"population_{year}" for year in range(1996, 2022, 5)]

        (
            GTI(towny[["name", *years]].head(10), rowname_col="name")
            .fmt_integer(columns=years)
            .i_cols_controls(columns=years, hideable=True)
            .i_view(hidden=years[:-1])
        )
        ```

        A table first shown with the municipalities grouped by their status, most populous first
        in each group, which readers can group otherwise (or not at all) from the "Group rows"
        button in the control bar:

        ```{python}
        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .i_cols_controls(columns="status", groupable=True)
            .i_view(sort="-population_2021", group_by="status")
        )
        ```
        """
        # (Imported here, as `_query` is only needed for a view)
        from ._gti._query import check_query, parse_sort

        if group_by is not None:
            if not isinstance(group_by, str):
                raise TypeError(
                    f"`group_by=` takes a column name (or `None`), not {type(group_by).__name__}."
                )
            if group_by not in resolve_cols_c(self, group_by, excl_stub=False):
                raise ValueError(f"`group_by=` names column {group_by!r}, which the table hasn't.")
        return self._set_interactive(
            view_filter=check_query(filter),
            view_sort=parse_sort(sort),
            view_hidden=(
                () if hidden is None else tuple(resolve_cols_c(self, hidden, excl_stub=False))
            ),
            view_group_by=group_by,
        )

    def i_view_state(self, url: bool = True, storage: bool = False, undo: bool = True) -> Self:
        """
        Keep the reader's view of the table, for when the page is opened again, and let them undo
        their changes to it.

        The view is the table's filters, sort, search, page, page size, hidden columns, and the
        column its rows are grouped by, and the height of a body that scrolls (see [`i_scroll()`](`great_tables.GTI.i_scroll`)) as the
        reader drags it (not the rows selected, or the columns' widths). As the reader changes it, it can be kept in
        the page's URL (`url=`), so that reloading the page, or sharing its link, opens the table
        as it was; and in the browser's storage (`storage=`), so that the reader finds it as they
        left it when they come back to the page. The table's info panel then has a button that
        goes back to the view the table is first shown with (see
        [`i_view()`](`great_tables.GTI.i_view`)), which is also what's kept as no view at all.

        In the URL, the view is in the query string, with each part of it named after the table's
        ID (e.g., `?towny.filter=population_2021+%3E%3D+10000&towny.sort=-population_2021`, the
        filter written as `i_view()` takes it as text), so that tables with different IDs keep
        their own views, and the page's other parameters are left alone. A link that has the view
        of a table opens it with that view, rather than the one in the browser's storage. A part
        of the view the table can't have (say, a filter on a column that has none, after the table
        is changed) is left out, with a warning in the browser's console, and the rest kept.

        With `undo=` (the default), the control bar has buttons that undo and redo the reader's
        changes to the view, as do Ctrl+Z and Ctrl+Y (⌘Z and ⇧⌘Z on a Mac) in the table. Typing a
        search, or changing one filter, a little at a time is one change; going to another page
        isn't one, but is undone with the change after it. Resetting the view is a change too, so
        it can be undone. The changes are kept while the page is open, not with the view.

        The view is kept by the table's ID, so the table needs one: set it with `GTI(id=)` (or
        [`with_id()`](`great_tables.GT.with_id`)). Undo alone (`url=False, storage=False`)
        doesn't need one.

        Parameters
        ----------
        url
            Whether to keep the view in the page's URL (the default).
        storage
            Whether to keep the view in the browser's storage (`localStorage`), for the page.
        undo
            Whether readers can undo and redo their changes to the view (the default).

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table of Ontario's municipalities whose filters, sort, search and page are kept in
        the page's URL as they're changed, so that a link to the page shows what the reader sees;
        the undo and redo buttons in the control bar step back and forth through those changes.

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name", id="towny")
            .fmt_integer(columns="population_2021")
            .i_cols_filter(columns=["status", "population_2021"])
            .i_view_state()
        )
        ```
        """
        return self._set_interactive(
            view_state_url=_flag(url, "url"),
            view_state_storage=_flag(storage, "storage"),
            view_state_undo=_flag(undo, "undo"),
        )

    def i_export(
        self,
        formats: ExportFormat | list[ExportFormat] | tuple[ExportFormat, ...] | None = (
            "csv",
            "clipboard",
        ),
        *,
        filename: str | None = None,
    ) -> Self:
        """
        Let readers export the table's rows.

        An export button in the control bar below the table opens a panel that copies the rows
        (`"clipboard"`) or downloads them as a CSV, TSV or JSON file (`"csv"`, `"tsv"`, `"json"`).
        It exports the rows readers see: every row the search and filters keep (on every page, not
        only the one shown), in the order shown, with the columns' text as the table shows it
        (formatted, without footnote marks). The column labels are the first row, each after its
        spanners' labels (as in "Revenue – gross"), and with row groups, the group's label is a
        column before the others. With [`i_selection()`](`great_tables.GTI.i_selection`), readers
        can export the rows they've selected instead.

        A copy has the rows both as a table, with the cells' styles (for pasting into a document
        or a spreadsheet), and as text, with tabs between the cells; a TSV file has them as that
        text does, with a cell's tabs and line breaks as spaces. In a CSV or TSV file, a cell a
        spreadsheet would read as a formula (one starting with `=`, `+`, `-` or `@`, but not a
        number) starts with a `'`, so that it's read as text. A JSON file has an object for each
        row instead of the labels, with each cell's text under its column's name in the data, and
        the row's group label first, under `"group"` (with a `_` before it if a column has that
        name). Exporting is off by default.

        With `"code"`, readers can also copy code that filters and sorts the table's data (as
        `df`) as their view of it does, for Polars, pandas, or Narwhals (the library of the
        data, at first). The code works on the data's values, so it leaves out the search, and
        a `contains` or `matches` match is of a column's values as text (not of the text the
        table shows; and `contains` ignores case, but not accents); it doesn't keep rows within
        their row groups.

        Parameters
        ----------
        formats
            How readers can export the rows: `"csv"`, `"tsv"`, `"json"`, `"clipboard"`, `"code"`,
            or a list of them (in the order of their buttons in the panel). With `None` (or none
            at all), they can't.
        filename
            The name of the file a download makes (`".csv"`, `".tsv"` or `".json"` is added to
            it). By default, `"table"`.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table of Ontario's municipalities that readers can filter, then download what's
        left as a CSV or JSON file (`towny.csv` or `towny.json`), or copy, or copy the pandas code
        that filters the data as they have.

        ```{python}
        from great_tables import GTI
        from great_tables.data import towny

        (
            GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
            .fmt_integer(columns="population_2021")
            .i_cols_filter(columns=["status", "population_2021"])
            .i_export(["csv", "json", "clipboard", "code"], filename="towny")
        )
        ```
        """
        if formats is None:
            formats = ()
        elif isinstance(formats, str):
            formats = (formats,)
        chosen: list[ExportFormat] = []
        for fmt in formats:
            if fmt not in EXPORT_FORMATS:
                raise ValueError(
                    '`formats=` must be "csv", "tsv", "json", "clipboard", "code", a list of '
                    f"them, or `None` (no export), not one with {fmt!r}."
                )
            if fmt not in chosen:
                chosen.append(fmt)

        if filename is None:
            filename = Settings().export_filename
        if not isinstance(filename, str):
            raise TypeError(f"`filename=` must be a string or `None`, not {filename!r}.")
        # (The extension is added in the browser)
        for extension in (".csv", ".tsv", ".json"):
            if filename.lower().endswith(extension):
                filename = filename[: -len(extension)]
                break
        if filename.strip() == "":
            raise ValueError("`filename=` must name the file, not be empty.")
        return self._set_interactive(export_formats=tuple(chosen), export_filename=filename)

    def i_row_details(self, content: Callable[[dict[str, Any]], Any] | str | None) -> Self:
        """
        Let readers show more about each row, under it.

        Each row with details gets a button (in its first cell) that shows them under the row,
        across the table, and hides them again; on a touch screen, tapping the row does too (with
        [`i_selection()`](`great_tables.GTI.i_selection`), its checkbox selects it then). A row's
        details are a table (a `GT` table, shown as it is on its own) or text (`html()` or `md()`
        text, or a string, shown as it is). They're made from `content=`: a function, which gets
        each row's values and returns the row's details, or the name of a column with each row's
        details in it, which is left out of the table. The info panel (from the (i) button in the
        control bar) has buttons that show and hide the details of every row.

        The function gets a row's values as the data has them (not as they're formatted), as a
        dict of the data's column names to the row's values, with those of the columns the table
        hides (with [`cols_hide()`](`great_tables.GT.cols_hide`)), so they can be what the
        details are made of. With `None` (or, in a column, a missing value or an empty string), a
        row has no details, and no button.

        The details are made as the table is rendered, and are in its HTML, but aren't shown until
        a reader opens them (nor without the table's script running); they aren't searched,
        filtered, or exported. Open details follow their row as the rows are sorted, filtered and
        paged. They're shown apart from the page's styles (in a shadow root), so that a table in
        them looks as it does on its own, in the table's font and text color. Each `GT` table has
        its own CSS, so a table with many of them in its rows' details is a larger page. In a
        table that drops columns to fit a narrow container (see
        [`i_responsive()`](`great_tables.GTI.i_responsive`)), the details are under the columns
        dropped from the row.

        Parameters
        ----------
        content
            A function that takes a row's values (a dict) and returns its details: a `GT` table
            (not an interactive one), `html()` or `md()` text, a string, or `None` (no details).
            Or the name of a column with each row's details in it. With `None`, the rows have no
            details.

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here's a table of cars, each with a sentence about its engine under it, made from columns
        that the table hides.

        ```{python}
        from great_tables import GTI, md
        from great_tables.data import gtcars

        cars = gtcars[["mfr", "model", "year", "trim", "hp", "hp_rpm", "trq", "msrp"]].head(10)


        def engine(row):
            return md(
                f"The **{row['trim']}** makes {row['hp']:.0f} hp at {row['hp_rpm']:,.0f} rpm, "
                f"and {row['trq']:.0f} lb-ft of torque."
            )


        (
            GTI(cars, rowname_col="model")
            .cols_hide(columns=["trim", "hp", "hp_rpm", "trq"])
            .fmt_currency(columns="msrp", decimals=0)
            .i_row_details(engine)
        )
        ```

        A row's details can be a table of their own. Here, each of Ontario's ten largest
        municipalities has a table of its population at each census.

        ```{python}
        import pandas as pd
        from great_tables import GT
        from great_tables.data import towny

        years = [1996, 2001, 2006, 2011, 2016, 2021]
        counts = [f"population_{year}" for year in years]
        largest = towny.nlargest(10, "population_2021")[["name", "status", *counts]]


        def populations(row):
            census = pd.DataFrame({"census": years, "population": [row[c] for c in counts]})
            return (
                GT(census)
                .cols_label(census="Census", population="Population")
                .fmt_integer(columns="population")
            )


        (
            GTI(largest, rowname_col="name")
            .cols_hide(columns=counts[:-1])
            .fmt_integer(columns="population_2021")
            .i_row_details(populations)
        )
        ```
        """
        if not (content is None or isinstance(content, str) or callable(content)):
            raise TypeError(
                "`content=` must be a function that makes a row's details, the name of a column "
                f"with them, or `None` (no details), not {content!r}."
            )
        if isinstance(content, str) and content not in get_column_names(self._tbl_data):
            raise ValueError(f"`content=` names a column the data doesn't have: {content!r}.")
        return self._set_interactive(row_details=content)

    def i_link(self, group: str | None, on: str | None = None) -> Self:
        """
        Link the table to others on the page, so that the rows selected in one filter the others.

        Tables with the same `group=` are linked by their `on=` column, which each of them has in
        its data (it can be a hidden one). When a reader selects rows in one of them (which
        [`i_selection()`](`great_tables.GTI.i_selection`) lets them do), each of the others
        shows only its rows whose value in that column is one of the selected rows' values;
        clearing the selection shows them all again. A row with a missing value in the column
        isn't linked to any. A table whose rows can't be selected is only filtered, and tables
        whose rows can be filter each other (but not themselves). The tables link in the browser,
        without a server: in a Quarto document, a notebook (but not across the frames some show
        each cell's output in, as Colab does), or an HTML page with the tables in it.

        A table filtered by another's selection says so in its control bar, with a token
        ("Selected in Makes: Ferrari, Lamborghini") that shows the rows again (until the
        selection changes), and in its info panel. The tables are named after their titles (see
        [`tab_header()`](`great_tables.GT.tab_header`)), or else their IDs. The filter is on top
        of the table's own search and filters, and isn't part of its view: it isn't kept with the
        view (see [`i_view_state()`](`great_tables.GTI.i_view_state`)), undone, or in the code
        an export copies.

        Parameters
        ----------
        group
            The name of the tables' group: tables with the same one are linked. With `None`, the
            table isn't linked.
        on
            The column of the table's data whose values link its rows to those of the others in
            the group (each of which has a column of that name).

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        Here are two tables of cars, one of their makes and one of the cars themselves, linked
        by the make. Select some makes in the first, and the second shows only their cars.

        ```{python}
        from great_tables import GTI
        from great_tables.data import gtcars

        cars = gtcars[["mfr", "model", "year", "hp", "msrp"]]
        makes = cars.groupby("mfr", as_index=False).agg(models=("model", "count"))

        (
            GTI(makes, rowname_col="mfr")
            .tab_header(title="Makes")
            .i_selection("multiple")
            .i_link("cars", on="mfr")
        )
        ```

        ```{python}
        (
            GTI(cars, rowname_col="model")
            .tab_header(title="Cars")
            .fmt_integer(columns=["year", "hp"], use_seps=False)
            .fmt_currency(columns="msrp", decimals=0)
            .i_link("cars", on="mfr")
        )
        ```
        """
        if group is None:
            return self._set_interactive(link_group=None, link_on=None)
        if not isinstance(group, str):
            raise TypeError(f"`group=` must be a string, or `None` (not linked), not {group!r}.")
        if group.strip() == "":
            raise ValueError("`group=` must name the tables' group, not be empty.")
        if on is None:
            raise ValueError(
                "`on=` must name the column whose values link the table's rows to those of the "
                f"other tables in the {group!r} group."
            )
        if not isinstance(on, str):
            raise TypeError(f"`on=` must be the name of a column, not {on!r}.")
        if on not in get_column_names(self._tbl_data):
            raise ValueError(f"`on=` names a column the data doesn't have: {on!r}.")
        return self._set_interactive(link_group=group, link_on=on)

    def i_scale(self, engine: Engine = "auto") -> Self:
        """
        Set where the rows of the table, shown as a widget or in a Shiny app, are searched,
        filtered and sorted.

        A table shown in the browser has all of its rows there, which does all of this: quick for
        a table of a few thousand rows, but slow to load (and to sort) with many more. Shown as a
        widget (with [`i_as_widget()`](`great_tables.GTI.i_as_widget`)), or in a Shiny app (with
        [`render_gt()`](`great_tables.shiny.render_gt`)), a table can keep its rows in Python
        instead (in the notebook's kernel, or on the app's server), which searches, filters and
        sorts them (with [Narwhals](https://narwhals-dev.github.io/narwhals/), on the data's own
        library), and sends the browser the page it shows, one at a time: so the table loads as
        quickly with a million rows as with a few.

        In the kernel, a table always has pages (as [`i_pagination()`](`great_tables.GTI.i_pagination`)
        sets them up), and its readers can't group its rows by a column, see its columns'
        profiles, see rows' details, or export the rows themselves (they can copy the code that
        filters and sorts the data as the view does, if the table has the `"code"` format); nor
        do its `data_color()` colors change with the rows kept, or does it filter linked tables
        (see [`i_link()`](`great_tables.GTI.i_link`)). A table with row groups, summary rows, or a
        stub of more than one column is shown in the browser, as anywhere else, and so is a table
        that isn't shown as a widget or in a Shiny app.

        A table of a lazy frame (a Polars LazyFrame, a DuckDB relation or an Ibis table) keeps its
        rows in the frame, and has only the page shown collected (see [`GTI()`](`great_tables.GTI`)).

        Parameters
        ----------
        engine
            Where the rows are searched, filtered and sorted: in Python, if the table is shown as a
            widget or in a Shiny app and has more rows than the browser is quick with (more than
            3,000, or more than 10 MB of HTML), and in the browser otherwise (`"auto"`, the
            default); in the browser (`"browser"`); or in Python, if the table is shown as a widget
            or in a Shiny app (`"kernel"`).

        Returns
        -------
        GTI
            The GTI object is returned.

        Examples
        --------
        This table of a million rows is shown a page at a time, from Python.

        ```python
        import numpy as np
        import polars as pl
        from great_tables import GTI

        rng = np.random.default_rng(1)
        df = pl.DataFrame({"x": rng.normal(size=1_000_000), "n": rng.integers(0, 100, 1_000_000)})

        GTI(df).fmt_number(columns="x").i_cols_filter().i_scale(engine="kernel").i_as_widget()
        ```
        """
        if engine not in ENGINES:
            raise ValueError(f'`engine=` must be "auto", "browser", or "kernel", not {engine!r}.')
        return self._set_interactive(engine=engine)

    def i_as_widget(self) -> GTIWidget:
        """
        Show the table as a widget, whose view and selection can be read and set from Python.

        The widget (an [anywidget](https://anywidget.dev)) shows the table as it's shown anywhere
        else, in a notebook in Jupyter, VS Code or Colab, or in marimo (as
        `mo.ui.anywidget(widget)`), and keeps Python up to date with what the reader does with
        it: the rows its search and filters keep, in the order shown, and those selected. Python
        can change the table's filters, sort, search and selection, too, and the table shows the
        change. The table works in the browser, as without a widget: Python is told what it does.

        The widget has these, to read and set:

        - `query`: the filters, as a query in text (as the query box has it, e.g.
          `'category in ("Tools") and margin > 0.2'`), or `""` without any; set it to a query (in
          text, or as [`i_view()`](`great_tables.GTI.i_view`)'s `filter=` takes it), or to `""`.
        - `search`: the search, or `""`.
        - `sort`: the columns the rows are sorted by, most significant first, with a `-` before
          each one sorted in descending order (e.g., `["-net", "store"]`).
        - `selection`: the data rows selected (numbered by position in the data, from 0), in data
          order, as far as [`i_selection()`](`great_tables.GTI.i_selection`) lets readers select
          them.

        And these, to read:

        - `rows`: the data rows the search and filters keep (and linked tables' selections; see
          [`i_link()`](`great_tables.GTI.i_link`)), in the order shown, on every page.
        - `view()`: the table's data with those rows, as a DataFrame of the data's library (with
          all its columns); `view(selected=True)` has the rows selected.

        And `on_change(callback)` has `callback` called, with the widget, after each change the
        reader makes (`on_change(callback, remove=True)` stops it).

        The rows are the browser's: a change made from Python is applied by the browser once the
        code making it has run, so in a notebook, `rows` and `view()` have it in the next cell (in
        the same cell, they raise an error). Before the widget is shown, they're those of the
        table's view (see [`i_view()`](`great_tables.GTI.i_view`)), as Python finds them.

        A table with more rows than the browser is quick with keeps them in Python instead (see
        [`i_scale()`](`great_tables.GTI.i_scale`)), which sends the browser a page at a time:
        then the rows are Python's, and `rows` and `view()` have a change at once.

        The widget needs the `anywidget` package (`pip install anywidget`, or
        `pip install great_tables[widget]`).

        Returns
        -------
        GTIWidget
            The widget, which shows the table when it's a cell's output (or with `display()`).

        Examples
        --------
        Here the reader can filter the cars by their make and select some; Python gets them.

        ```python
        from great_tables import GTI
        from great_tables.data import gtcars

        cars = gtcars[["mfr", "model", "year", "hp", "msrp"]]

        widget = (
            GTI(cars, rowname_col="model")
            .i_cols_filter(columns="mfr", type="facet")
            .i_selection("multiple")
            .i_as_widget()
        )
        widget
        ```

        In a later cell, after filtering and selecting:

        ```python
        widget.query           # 'mfr in ("Ferrari", "Lamborghini")'
        widget.view()          # those makes' cars, as a pandas DataFrame
        widget.view(selected=True)
        ```

        And from Python, the table shows the cars with the most power first:

        ```python
        widget.sort = "-hp"
        ```
        """
        try:
            from ._gti._widget import GTIWidget
        except ImportError as err:
            if err.name not in ("anywidget", "traitlets", "ipywidgets"):
                raise
            raise ImportError(
                "`i_as_widget()` needs the anywidget package: install it with "
                "`pip install anywidget` (or `pip install great_tables[widget]`)."
            ) from err
        return GTIWidget(self)

    # -----
    # A `GTI` table is only ever interactive HTML

    def as_raw_html(
        self,
        inline_css: bool = False,
        make_page: bool = False,
        all_important: bool = False,
    ) -> str:
        """
        Get the HTML of a GTI table.

        The HTML is a `<gt-table>` element (the table's own HTML, and what it needs to be
        interactive), followed by the element's CSS and JavaScript.

        Parameters
        ----------
        inline_css
            Not available for a GTI table, whose interactive HTML needs its CSS in a `<style>`
            block (and its script, which email clients don't run).
        make_page
            If `True`, the table will be wrapped in a complete HTML page with proper `<html>`,
            `<head>`, and `<body>` tags.
        all_important
            If `True`, the table's CSS declarations are marked with `!important` to ensure they
            take precedence over other styles that might be present in the document.

        Returns
        -------
        str
            An HTML string containing the table.
        """
        from ._gti import page_html, render_gti_html

        if inline_css:
            raise ValueError(
                "A GTI table can't have its CSS inlined (`inline_css=True`): its interactive HTML "
                "needs a <style> block and a script. Use `GT` for a table in an email."
            )

        fragment = render_gti_html(self, all_important=all_important)
        return page_html(fragment) if make_page else fragment

    def save(self, *args: Any, **kwargs: Any) -> NoReturn:
        """Not available for a GTI table, which is interactive HTML only."""
        raise TypeError(_static_only("save()"))

    def gtsave(self, *args: Any, **kwargs: Any) -> NoReturn:
        """Not available for a GTI table, which is interactive HTML only."""
        raise TypeError(_static_only("gtsave()"))

    def as_latex(self, *args: Any, **kwargs: Any) -> NoReturn:
        """Not available for a GTI table, which is interactive HTML only."""
        raise TypeError(_static_only("as_latex()"))

    def opt_interactive(self, *args: Any, **kwargs: Any) -> NoReturn:
        """Not available for a GTI table, which has its own `i_` methods."""
        raise TypeError(
            "`opt_interactive()` is for `GT` tables. A GTI table is set up with its `i_` methods "
            "instead: `i_sorting()`, `i_search()`, `i_resizing()`, `i_pagination()`, "
            "`i_selection()`, `i_scroll()`, `i_responsive()`, `i_display()`, `i_inspect()`, "
            "`i_cols_filter()`, "
            "`i_cols_controls()`, `i_cols_pin()`, `i_cols_priority()`, `i_cols_profile()`, "
            "`i_view()`, `i_view_state()`, `i_export()`, `i_row_details()`, and `i_link()` "
            "(and shown as a widget with `i_as_widget()`, set up with `i_scale()`)."
        )


# A `GTI` table of a LazyFrame keeps the calls of `GT`'s methods that made it (but not of those
# they call), to make it again from the rows shown
_RECORDING: ContextVar[bool] = ContextVar("_RECORDING", default=False)

# (Those whose results aren't tables, or that render it, which are of all of its rows)
_NOT_RECORDED = {"show", "write_raw_html", "render"}


def _recorded(name: str, method: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(method)
    def call(self: GT, *args: Any, **kwargs: Any) -> Any:
        lazy = self.__dict__.get("_lazy")
        if lazy is None:
            return method(self, *args, **kwargs)
        from ._gti._lazy import UNRUN, check_call

        check_call(name, method, args, kwargs)
        if _RECORDING.get():
            return self if name in UNRUN else method(self, *args, **kwargs)
        token = _RECORDING.set(True)
        try:
            result = self if name in UNRUN else method(self, *args, **kwargs)
        finally:
            _RECORDING.reset(token)
        result = copy.copy(result)
        object.__setattr__(result, "_lazy", lazy.called(name, args, kwargs))
        return result

    return call


def _collected(method: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(method)
    def call(self: GT, *args: Any, **kwargs: Any) -> Any:
        from ._gti._lazy import eager

        return method(eager(self), *args, **kwargs)

    return call


for _name, _method in list(vars(GT).items()):
    if _name.startswith("_") or not inspect.isfunction(_method) or _name in vars(GTI):
        continue
    if _name == "render":
        setattr(GTI, _name, _collected(_method))
    elif _name not in _NOT_RECORDED:
        setattr(GTI, _name, _recorded(_name, _method))
del _name, _method


# The lazy frames a table can be of (see `_gti/_lazy.py`): each one's module and class
_LAZY_FRAMES = [
    ("polars", "LazyFrame"),
    ("duckdb", "DuckDBPyRelation"),
    ("ibis.expr.types", "Table"),
]


def _is_lazy_frame(data: Any) -> bool:
    # (Of a module that's imported, which it is if there's data of it)
    for module, name in _LAZY_FRAMES:
        kind = getattr(sys.modules.get(module), name, None)
        if isinstance(kind, type) and isinstance(data, kind):
            return True
    return False


def _static_only(method: str) -> str:
    return (
        f"`{method}` isn't available for a GTI table, which is interactive HTML only. Use "
        "`write_raw_html()` to save it as an HTML file, or `GT` for static output."
    )


def _flag(value: object, name: str) -> bool:
    if not isinstance(value, bool):
        raise TypeError(f"`{name}=` must be `True` or `False`, not {value!r}.")
    return value


def _optional_flag(value: object, name: str) -> bool | None:
    if not (value is None or isinstance(value, bool)):
        raise TypeError(f"`{name}=` must be `True`, `False`, or `None`, not {value!r}.")
    return value


def _width(value: Any, name: str) -> int | float:
    # (A positive number of pixels, e.g. NumPy's, but not a bool; kept whole where it is)
    if isinstance(value, numbers.Real) and not isinstance(value, bool):
        width = float(value)
        if math.isfinite(width) and width > 0:
            return int(width) if width.is_integer() else width
    raise ValueError(f"`{name}=` must be a positive number of pixels, not {value!r}.")


def _page_size(value: Any, name: str) -> int:
    # (Any integer, e.g. NumPy's, but not a bool or a float)
    if not isinstance(value, bool):
        try:
            size = operator.index(value)
        except TypeError:
            size = 0
        if size >= 1:
            return size
    raise ValueError(f"`{name}=` must be a whole number of rows (at least 1), not {value!r}.")


def _priority(value: Any) -> int:
    # (Any integer, e.g. NumPy's, but not a bool or a float)
    if not isinstance(value, bool):
        try:
            priority = operator.index(value)
        except TypeError:
            priority = 0
        if priority >= 1:
            return priority
    raise ValueError(
        f"`priority=` must be a positive integer, or `None` (no priority), not {value!r}."
    )
