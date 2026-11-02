from __future__ import annotations

import operator
from dataclasses import replace
from typing import Any, NoReturn

from typing_extensions import Self

from ._gti._settings import SELECTION_MODES, Settings, SelectionMode
from ._options import _is_height
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
            settings = replace(
                Settings.from_options(gt._options), pagination_type=Settings().pagination_type
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
    # defaults), so that what a table does doesn't depend on the order of the calls

    def i_sorting(self, enabled: bool = True) -> Self:
        """
        Let readers sort the table by its columns.

        A column is sorted by clicking (or tapping) its label: once for ascending order, again for
        descending, and a third time to go back to the table's own order. With Shift held, a column
        is added to the sort (and is sorted within the columns before it). Rows are sorted by the
        column's values, not by how they're formatted, and stay in their row groups. Sorting is on
        by default.

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
        the table, ignoring case and accents), and highlights the matches. Searching is on by
        default.

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
        width. Resizing is on by default.

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
    ) -> Self:
        """
        Split the table's rows into pages.

        With pagination, readers see a page of rows at a time, with controls below the table to go
        from page to page. Each page is as tall as a full one, so the controls stay in place.
        Pagination is on by default, with ten rows to a page.

        Parameters
        ----------
        enabled
            Whether the rows are split into pages. Without pagination, all of the rows are shown.
        page_size
            How many rows are on a page, to begin with.
        page_sizes
            The page sizes readers can choose from. With `None` (or none at all), readers can't
            change the page size.

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
        page_size = _page_size(page_size, "page_size")
        # (Not `page_sizes or ()`, which a NumPy array can't answer)
        sizes = () if page_sizes is None else tuple(_page_size(s, "page_sizes") for s in page_sizes)
        return self._set_interactive(
            pagination=enabled,
            page_size=page_size,
            page_sizes=sizes,
            page_size_select=bool(sizes),
        )

    def i_selection(self, mode: SelectionMode | None = "multiple") -> Self:
        """
        Let readers select the table's rows.

        Rows are selected by clicking them or their checkboxes, in a column before the others. With
        `"single"`, selecting a row clears the one selected before; with `"multiple"`, Shift-click
        selects a range of rows, and a checkbox in the column labels selects every row that matches
        the search. Selection is off by default.

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
            "`i_selection()`, `i_scroll()`, and `i_display()`."
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
