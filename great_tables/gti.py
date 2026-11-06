from __future__ import annotations

import math
import numbers
import operator
from dataclasses import replace
from typing import Any, NoReturn

from typing_extensions import Self

from ._gt_data import ColInfoTypeEnum
from ._gti._settings import (
    EXPORT_FORMATS,
    FILTER_TYPES,
    PIN_SIDES,
    RESPONSIVE_MODES,
    SELECTION_MODES,
    ExportFormat,
    FilterType,
    PinSide,
    ResponsiveMode,
    SelectionMode,
    Settings,
)
from ._gti._spec import _has_time_zone
from ._locations import resolve_cols_c
from ._options import _is_height
from ._tbl_data import SelectExpr, _get_column_kind
from .gt import GT

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

    :::{.callout-warning}
    `GTI()` is experimental: its methods, and what they do, may change.
    :::

    Parameters
    ----------
    data
        A DataFrame object.
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

    Returns
    -------
    GTI
        A GTI object is returned.

    Examples
    --------
    Out of the box, a `GTI` table can be sorted by its columns (by clicking their labels), searched,
    and paged through, ten rows at a time, and its columns can be resized.

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

    A `GT` table can be made into a `GTI` table with [`GTI.from_gt()`](`great_tables.GTI.from_gt`).
    """

    def __init__(
        self,
        data: Any,
        rowname_col: str | list[str] | None = None,
        groupname_col: str | None = None,
        auto_align: bool = True,
        id: str | None = None,
        locale: str | None = None,
    ):
        super().__init__(
            data,
            rowname_col=rowname_col,
            groupname_col=groupname_col,
            auto_align=auto_align,
            id=id,
            locale=locale,
        )
        # (Kept apart from the table's options, which are `GT`'s; frozen, as the table is)
        object.__setattr__(self, "_interactive", Settings())

    _interactive: Settings

    @classmethod
    def from_gt(cls, gt: GT) -> GTI:
        """
        Make an interactive table from a `GT` table.

        The new `GTI` table has everything the `GT` table has (its data, formats, styles, and
        options). Readers can do with it what they can with any new `GTI` table, unless
        [`opt_interactive()`](`great_tables.GT.opt_interactive`) was used on the `GT` table: then
        they can do what it set (sorting, searching, and so on), with `GTI`'s page controls.

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
            # (`use_filters=True` filters every column, with GTI's filters)
            filters = gt._options.ihtml_use_filters.value
            settings = replace(
                Settings.from_options(gt._options),
                pagination_type=Settings().pagination_type,
                bar=True,
                filters=tuple((column, "auto") for column in resolve_cols_c(gt, None))
                if filters
                else (),
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

        A column is sorted by clicking (or tapping) its label: once for ascending order, again for
        descending, and a third time to go back to the table's own order. With Shift held, a column
        is added to the sort (and is sorted within the columns before it). Rows are sorted by the
        column's values, not by how they're formatted, and stay in their row groups. The info panel
        (from the (i) button in the control bar) says how the table is sorted, and can put it back
        in its own order. Sorting is on by default; some columns can be left unsortable with
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
        which rows are shown and has the choice of page size. Pagination is on by default, with ten
        rows to a page.

        Parameters
        ----------
        enabled
            Whether the rows are split into pages. Without pagination, all of the rows are shown.
        page_size
            How many rows are on a page, to begin with.
        page_sizes
            The page sizes readers can choose from, in the info panel (as well as `page_size`).
            With `None` (or none at all), readers can't change the page size.
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

    def i_scroll(self, height: str | int | float | None) -> Self:
        """
        Make the table's body scroll, within a height.

        The table takes up no more than `height`, and its body scrolls within it, with the column
        labels (and the table's header) staying in view. By default, a table grows with its rows.

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

    def i_responsive(
        self, mode: ResponsiveMode = "scroll", *, stack_below: int | float = 420
    ) -> Self:
        """
        Set how the table fits a narrow container.

        A table wider than its container scrolls sideways, with its stub (and any pinned columns)
        staying in view (`"scroll"`, the default). Or, in a container narrower than `stack_below`
        pixels (on a phone, say), it can be stacked: each row becomes a card, titled by its stub,
        with each column's label next to its value (labels under a spanner are prefixed with it).
        Row groups become headings between the cards, and summary rows become cards of their own.
        The table is stacked by its CSS alone, so it's stacked before its script runs (or without
        it); once it runs, the column labels are shown above the cards as chips, which readers
        can sort and filter by as with the labels themselves.

        With `"stack"`, the table is stacked in any narrow container; with `"auto"`, only if it
        shows no more than six columns (not counting the stub), so that wider tables scroll. In a
        container as wide as `stack_below` or wider, either is as `"scroll"`.

        Parameters
        ----------
        mode
            How the table fits a narrow container: `"scroll"`, `"stack"`, or `"auto"`.
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
        """
        if mode == "collapse":
            raise ValueError(
                'The "collapse" layout (hiding columns by priority) isn\'t available yet; use '
                '`mode="scroll"`, `"stack"`, or `"auto"`.'
            )
        if mode not in RESPONSIVE_MODES:
            raise ValueError(f'`mode=` must be "scroll", "stack", or "auto", not {mode!r}.')
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
        display: bool | None = None,
    ) -> Self:
        """
        Choose which columns readers can sort by, search, resize, hide, and move, and which are only
        for querying.

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

        Each call sets what it's given for the columns it's given, so that some columns can be
        left out of one thing, and others another; a later call for a column replaces what an
        earlier one set.

        Parameters
        ----------
        columns
            The columns: a column name, a list of them, or a selector (e.g., Polars'
            `cs.numeric()`). With `None` (the default), every column but the stub (which can be
            named). The row group column can't be one of them.
        sortable, searchable, resizable, hideable, reorderable
            Whether readers can sort by the columns, search them, resize them, hide them, and move
            them. With `None` (the default), the columns are left as they are.
        display
            Whether the columns are in the table (`True`), or left out of it and kept only for
            querying (`False`). With `None` (the default), the columns are left as they are.

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
        """
        # (Each setting keeps the columns readers can't do it with (and `query_only`, those not
        # shown), but `hideable` and `reorderable` keep those they can, so they're turned around)
        hide = _optional_flag(hideable, "hideable")
        move = _optional_flag(reorderable, "reorderable")
        flags = {
            "unsortable": _optional_flag(sortable, "sortable"),
            "unsearchable": _optional_flag(searchable, "searchable"),
            "unresizable": _optional_flag(resizable, "resizable"),
            "hideable": None if hide is None else not hide,
            "reorderable": None if move is None else not move,
            "query_only": _optional_flag(display, "display"),
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

    def i_view(
        self,
        filter: str | dict[str, Any] | None = None,
        sort: str | list[str] | None = None,
        hidden: SelectExpr = None,
    ) -> Self:
        """
        Show the table filtered and sorted, as readers first see it.

        The table is first shown with the rows that `filter=` keeps, in the order `sort=` gives
        them, and without the columns `hidden=` hides, which readers can then change (with the
        column filters, sort buttons, and the bar's "Columns" panel) or clear. Rows stay within
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
        """
        # (Imported here, as `_query` is only needed for a view)
        from ._gti._query import check_query, parse_sort

        return self._set_interactive(
            view_filter=check_query(filter),
            view_sort=parse_sort(sort),
            view_hidden=(
                () if hidden is None else tuple(resolve_cols_c(self, hidden, excl_stub=False))
            ),
        )

    def i_view_state(self, url: bool = True, storage: bool = False, undo: bool = True) -> Self:
        """
        Keep the reader's view of the table, for when the page is opened again, and let them undo
        their changes to it.

        The view is the table's filters, sort, search, page, page size, and hidden columns (not
        the rows selected, or the columns' widths). As the reader changes it, it can be kept in
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
        from ._gti import render_gti_html

        if inline_css:
            raise ValueError(
                "A GTI table can't have its CSS inlined (`inline_css=True`): its interactive HTML "
                "needs a <style> block and a script. Use `GT` for a table in an email."
            )

        fragment = render_gti_html(self, all_important=all_important)
        if make_page:
            return (
                '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8"/>\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1"/>\n'
                f"</head>\n<body>\n{fragment}</body>\n</html>\n"
            )
        return fragment

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
            "`i_selection()`, `i_scroll()`, `i_responsive()`, `i_display()`, `i_cols_filter()`, "
            "`i_cols_controls()`, `i_cols_pin()`, `i_view()`, `i_view_state()`, and `i_export()`."
        )


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
