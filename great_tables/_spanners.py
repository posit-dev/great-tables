from __future__ import annotations

import itertools

from typing import TYPE_CHECKING, Union, List, Dict, Optional, Any

from ._gt_data import Spanners, SpannerInfo
from ._tbl_data import SelectExpr
from ._locations import resolve_cols_c

if TYPE_CHECKING:
    from ._gt_data import Boxhead
    from ._types import GTSelf


SpannerMatrix = List[Dict[str, Union[str, None]]]


def tab_spanner(
    data: GTSelf,
    label: str,
    columns: SelectExpr = None,
    spanners: Union[list[str], str, None] = None,
    level: Optional[int] = None,
    id: Optional[str] = None,
    gather: bool = True,
    replace: bool = False,
) -> GTSelf:
    """
    Insert a spanner above a selection of column headings.

    This part of the table contains, at a minimum, column labels and, optionally, an unlimited
    number of levels for spanners. A spanner will occupy space over any number of contiguous column
    labels and it will have an associated label and ID value. This method allows for mapping to be
    defined by column names, existing spanner ID values, or a mixture of both.

    The spanners are placed in the order of calling `tab_spanner()` so if a later call uses the same
    columns in its definition (or even a subset) as the first invocation, the second spanner will be
    overlaid atop the first. Options exist for forcibly inserting a spanner underneath others (with
    `level` as space permits) and with `replace`, which allows for full or partial spanner
    replacement.

    Parameters
    ----------
    label : str
        The text to use for the spanner label. We can optionally use the [`md()`](`great_tables.md`)
        and [`html()`](`great_tables.html`) helper functions to style the text as Markdown or to
        retain HTML elements in the text.
    columns : SelectExpr
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    spanners : str | list[str] | None
        The spanners that should be spanned over, should they already be defined. One or more
        spanner ID values (in quotes) can be supplied here. This argument works in tandem with the
        `columns` argument.
    level : Optional[int]
        An explicit level to which the spanner should be placed. If not provided, **Great Tables**
        will choose the level based on the inputs provided within `columns` and `spanners`, placing
        the spanner label where it will fit. The first spanner level (right above the column labels)
        is `0`.
    id : Optional[str]
        The ID for the spanner. When accessing a spanner through the `spanners` argument of
        `tab_spanner()` the `id` value is used as the reference (and not the `label`). If an `id`
        is not explicitly provided here, it will be taken from the `label` value. It is advisable to
        set an explicit `id` value if you plan to access this cell in a later call and the label
        text is complicated (e.g., contains markup, is lengthy, or both). Finally, when providing
        an `id` value you must ensure that it is unique across all ID values set for spanner labels
        (the method will throw an error if `id` isn't unique).
    gather : bool
        An option to move the specified `columns` such that they are unified under the spanner.
        Ordering of the moved-into-place columns will be preserved in all cases. By default, this
        is set to `True`.
    replace : bool
        Should new spanners be allowed to partially or fully replace existing spanners? (This is a
        possibility if setting spanners at an already populated `level`.) By default, this is set to
        `False` and an error will occur if some replacement is attempted.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's create a table using a small portion of the `gtcars` dataset. Over several columns (`hp`,
    `hp_rpm`, `trq`, `trq_rpm`, `mpg_c`, `mpg_h`) we'll use `tab_spanner()` to add a spanner with
    the label `"performance"`. This effectively groups together several columns related to car
    performance under a unifying label.

    ```{python}
    from great_tables import GT
    from great_tables.data import gtcars

    colnames = ["model", "hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
    gtcars_mini = gtcars[colnames].head(10)

    (
        GT(gtcars_mini)
        .tab_spanner(
            label="performance",
            columns=["hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
        )
    )
    ```

    We can also use Markdown formatting for the spanner label. In this example, we'll use
    `gt.md("*Performance*")` to make the label italicized.

    ```{python}
    from great_tables import GT, md
    from great_tables.data import gtcars

    colnames = ["model", "hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
    gtcars_mini = gtcars[colnames].head(10)

    (
        GT(gtcars_mini)
        .tab_spanner(
            label=md("*Performance*"),
            columns=["hp", "hp_rpm", "trq", "trq_rpm", "mpg_c", "mpg_h"]
        )
    )
    ```
    """

    crnt_spanner_ids = [span.spanner_id for span in data._spanners]

    if id is None:
        id = label

    if isinstance(columns, (str, int)):
        columns = [columns]

    if isinstance(spanners, (str, int)):
        spanners = [spanners]

    # validations ----
    if level is not None and level < 0:
        raise ValueError(f"Level may not be negative. Received {level}.")
    if id in crnt_spanner_ids:
        raise ValueError(f"Spanner id {id} already exists.")

    # select columns ----

    if columns is None:
        # TODO: null_means is unimplemented
        raise NotImplementedError("columns must be specified")

    selected_column_names = resolve_cols_c(data=data, expr=columns, null_means="nothing")

    # select spanner ids ----
    # TODO: this supports tidyselect
    # TODO: could we use something like resolve_vector_l
    if spanners is not None:
        assert set(spanners).issubset(set(crnt_spanner_ids))
        spanner_ids = spanners
    else:
        spanner_ids = []

    if not len(selected_column_names) and not len(spanner_ids):
        return data

    # get column names associated with selected spanners ----
    _vars = [span.vars for span in data._spanners if span.spanner_id in spanner_ids]
    spanner_column_names = list({k: True for k in itertools.chain(*_vars)})

    column_names = list({k: True for k in [*selected_column_names, *spanner_column_names]})

    # combine columns names and those from spanners ----

    # get spanner level ----
    if level is None:
        level = data._spanners.next_level(column_names)

    # get spanner units and labels ----
    # TODO: grep units from {{.*}}, may need to switch delimiters
    spanner_units = None
    spanner_pattern = None

    new_span = SpannerInfo(
        spanner_id=id,
        spanner_level=level,
        vars=column_names,
        spanner_units=spanner_units,
        spanner_pattern=spanner_pattern,
        spanner_label=label,
    )

    spanners = data._spanners.append_entry(new_span)

    new_data = data._replace(_spanners=spanners)

    if gather and not len(spanner_ids) and level == 0:
        return cols_move(new_data, columns=column_names, after=column_names[0])

    return new_data


def cols_move(data: GTSelf, columns: SelectExpr, after: str) -> GTSelf:
    """Move one or more columns.

    On those occasions where you need to move columns this way or that way, we can make use of the
    `cols_move()` method. While it's true that the movement of columns can be done upstream of
    **Great Tables**, it is much easier and less error prone to use the method provided here. The
    movement procedure here takes one or more specified columns (in the `columns` argument) and
    places them to the right of a different column (the `after` argument). The ordering of the
    `columns` to be moved is preserved, as is the ordering of all other columns in the table.

    The columns supplied in `columns` must all exist in the table and none of them can be in the
    `after` argument. The `after` column must also exist and only one column should be provided
    here. If you need to place one more or columns at the beginning of the column series, the
    `cols_move_to_start()` method should be used. Similarly, if those columns to move should be
    placed at the end of the column series then use `cols_move_to_end()`.

    Parameters
    ----------
    columns : SelectExpr
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    after : str
        The column after which the `columns` should be placed. This can be any column name that
        exists in the table.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's use the `countrypops` dataset to create a table. We'll choose to position the `population`
    column after the `country_name` column by using the `cols_move()` method.

    ```{python}
    from great_tables import GT
    from great_tables.data import countrypops

    countrypops_mini = countrypops.loc[countrypops["country_name"] == "Japan"][
        ["country_name", "year", "population"]
    ].tail(5)

    (
        GT(countrypops_mini)
        .cols_move(
            columns="population",
            after="country_name"
        )
    )
    ```
    """

    # If `columns` is a string, convert it to a list
    if isinstance(columns, str):
        columns = [columns]

    sel_cols = resolve_cols_c(data=data, expr=columns)

    sel_after = resolve_cols_c(data=data, expr=[after])

    vars = [col.var for col in data._boxhead]

    if not len(sel_after):
        raise ValueError(f"Column {after} not found in table.")
    elif len(sel_after) > 1:
        raise ValueError(
            f"Only 1 value should be supplied to `after`, recieved argument: {sel_after}"
        )

    if not len(sel_cols):
        raise Exception("No columns selected.")
    elif not all([col in vars for col in sel_cols]):
        raise ValueError("All `columns` must exist and be visible in the input `data` table.")

    moving_columns = [col for col in sel_cols if col not in sel_after]
    other_columns = [col for col in vars if col not in moving_columns]

    indx = other_columns.index(after)
    final_vars = [*other_columns[: indx + 1], *moving_columns, *other_columns[indx + 1 :]]

    new_boxhead = data._boxhead.reorder(final_vars)
    return data._replace(_boxhead=new_boxhead)


def cols_move_to_start(data: GTSelf, columns: SelectExpr) -> GTSelf:
    """Move one or more columns to the start.

    We can easily move set of columns to the beginning of the column series and we only need to
    specify which `columns`. It's possible to do this upstream of **Great Tables**, however, it is
    easier with this method and it presents less possibility for error. The ordering of the
    `columns` that are moved to the start is preserved (same with the ordering of all other columns
    in the table).

    The columns supplied in `columns` must all exist in the table. If you need to place one or
    columns at the end of the column series, the `cols_move_to_end()` method should be used. More
    control is offered with the `cols_move()` method, where columns could be placed after a specific
    column.

    Parameters
    ----------
    columns : SelectExpr
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    For this example, we'll use a portion of the `countrypops` dataset to create a simple table.
    Let's move the `year` column, which is the middle column, to the start of the column series with
    the `cols_move_to_start()` method.

    ```{python}
    from great_tables import GT
    from great_tables.data import countrypops

    countrypops_mini = countrypops.loc[countrypops["country_name"] == "Fiji"][
        ["country_name", "year", "population"]
    ].tail(5)

    GT(countrypops_mini).cols_move_to_start(columns="year")
    ```

    We can also move multiple columns at a time. With the same `countrypops`-based table
    (`countrypops_mini`), let's move both the `year` and `population` columns to the start of the
    column series.

    ```{python}
    GT(countrypops_mini).cols_move_to_start(columns=["year", "population"])
    ```
    """

    # If `columns` is a string, convert it to a list
    if isinstance(columns, str):
        columns = [columns]

    sel_cols = resolve_cols_c(data=data, expr=columns)

    vars = [col.var for col in data._boxhead]

    if not len(sel_cols):
        raise Exception("No columns selected.")
    elif not all([col in vars for col in sel_cols]):
        raise ValueError("All `columns` must exist and be visible in the input `data` table.")

    moving_columns = [col for col in sel_cols]
    other_columns = [col for col in vars if col not in moving_columns]

    final_vars = [*moving_columns, *other_columns]

    new_boxhead = data._boxhead.reorder(final_vars)
    return data._replace(_boxhead=new_boxhead)


def cols_move_to_end(data: GTSelf, columns: SelectExpr) -> GTSelf:
    """Move one or more columns to the end.

    We can easily move set of columns to the beginning of the column series and we only need to
    specify which `columns`. It's possible to do this upstream of **Great Tables**, however, it is
    easier with this method and it presents less possibility for error. The ordering of the
    `columns` that are moved to the end is preserved (same with the ordering of all other columns in
    the table).

    Parameters
    ----------
    columns : SelectExpr
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    For this example, we'll use a portion of the `countrypops` dataset to create a simple table.
    Let's move the `year` column, which is the middle column, to the end of the column series with
    the `cols_move_to_end()` method.

    ```{python}
    from great_tables import GT
    from great_tables.data import countrypops

    countrypops_mini = countrypops.loc[countrypops["country_name"] == "Benin"][
        ["country_name", "year", "population"]
    ].tail(5)

    GT(countrypops_mini).cols_move_to_end(columns="year")
    ```

    We can also move multiple columns at a time. With the same `countrypops`-based table
    (`countrypops_mini`), let's move both the `year` and `country_name` columns to the end of the
    column series.

    ```{python}
    GT(countrypops_mini).cols_move_to_end(columns=["year", "country_name"])
    """

    # If `columns` is a string, convert it to a list
    if isinstance(columns, str):
        columns = [columns]

    sel_cols = resolve_cols_c(data=data, expr=columns)

    vars = [col.var for col in data._boxhead]

    if not len(sel_cols):
        raise Exception("No columns selected.")
    elif not all([col in vars for col in sel_cols]):
        raise ValueError("All `columns` must exist and be visible in the input `data` table.")

    moving_columns = [col for col in sel_cols]
    other_columns = [col for col in vars if col not in moving_columns]

    final_vars = [*other_columns, *moving_columns]

    new_boxhead = data._boxhead.reorder(final_vars)
    return data._replace(_boxhead=new_boxhead)


def cols_hide(data: GTSelf, columns: SelectExpr) -> GTSelf:
    """Hide one or more columns.

    The `cols_hide()` method allows us to hide one or more columns from appearing in the final
    output table. While it's possible and often desirable to omit columns from the input table data
    before introduction to the `GT()` class, there can be cases where the data in certain columns is
    useful (as a column reference during formatting of other columns) but the final display of those
    columns is not necessary.

    Parameters
    ----------
    columns : SelectExpr
        The columns to hide in the output display table. Can either be a single column name or a
        series of column names provided in a list.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Details
    -------
    The hiding of columns is internally a rendering directive, so, all columns that are 'hidden' are
    still accessible and useful in any expression provided to a `rows` argument. Furthermore, the
    `cols_hide()` method (as with many of the methods available in **Great Tables**) can be placed
    anywhere in a chain of calls (acting as a promise to hide columns when the timing is right).
    However there's perhaps greater readability when placing this call closer to the end of such a
    chain. The `cols_hide()` method quietly changes the visible state of a column and doesn't yield
    warnings when changing the state of already-invisible columns.
    """

    # If `columns` is a string, convert it to a list
    if isinstance(columns, str):
        columns = [columns]

    sel_cols = resolve_cols_c(data=data, expr=columns)

    vars = [col.var for col in data._boxhead]

    if not len(sel_cols):
        raise Exception("No columns selected.")
    elif not all([col in vars for col in columns]):
        raise ValueError("All `columns` must exist and be visible in the input `data` table.")

    # New boxhead with hidden columns
    new_boxhead = data._boxhead.set_cols_hidden(sel_cols)

    return data._replace(_boxhead=new_boxhead)


def spanners_print_matrix(
    spanners: Spanners,
    boxhead: Boxhead,
    include_hidden: bool = False,
    ids: bool = False,
    omit_columns_row: bool = False,
) -> tuple[SpannerMatrix, list[str]]:
    if include_hidden:
        vars = [row.var for row in boxhead if not row.is_stub]
    else:
        vars = [row.var for row in boxhead if not row.is_stub and row.visible]

    if not spanners:
        return empty_spanner_matrix(vars=vars, omit_columns_row=omit_columns_row)

    # Modify `spanners_tbl` such that:
    # (1) only visible vars are included in the `vars` column
    # (2) entries with no vars (after step 1) are removed, and
    # (3) `spanner_level` values have all gaps removed, being compressed
    #     down to start at 1 (e.g., 7, 5, 3, 1 -> 4, 3, 2, 1)
    _vars = [set(span.vars) & set(vars) for span in spanners]
    _lvls = sorted({span.spanner_level for span in spanners})

    non_empty_spans = [span for crnt_vars, span in zip(_vars, spanners) if len(crnt_vars)]
    new_levels = [_lvls.index(span.spanner_level) for span in non_empty_spans]

    crnt_spans = Spanners(non_empty_spans).relevel(new_levels)

    if not crnt_spans:
        return empty_spanner_matrix(vars=vars, omit_columns_row=omit_columns_row)

    spanner_height = len(_lvls)
    # TODO: span.built can be None. When does it get set?
    spanner_reprs = [span.spanner_id if ids else span.built_label() for span in crnt_spans]

    # Create a matrix with dimension spanner_height x vars (e.g. presented columns)
    label_matrix: SpannerMatrix = [
        {var_name: None for var_name in vars} for _ in range(spanner_height)
    ]

    for span_ii, span in enumerate(crnt_spans):
        for var in span.vars:
            # This if clause skips spanned columns that are not in the
            # boxhead vars we are planning to use (e.g. not in the visible ones
            # or in the stub).
            if var in label_matrix[span.spanner_level]:
                label_matrix[span.spanner_level][var] = spanner_reprs[span_ii]

    # reverse order , so if you were to print it out, level 0 would appear on the bottom
    label_matrix.reverse()

    # add column names to matrix
    if not omit_columns_row:
        label_matrix.append({var: var for var in vars})

    return label_matrix, vars


def empty_spanner_matrix(
    vars: list[str], omit_columns_row: bool
) -> tuple[SpannerMatrix, list[str]]:
    if omit_columns_row:
        return [], vars

    return [{var: var for var in vars}], vars


def seq_groups(seq: list[str]):
    # TODO: 0-length sequence
    if len(seq) == 0:
        raise StopIteration
    elif len(seq) == 1:
        yield seq[0], 1
    else:
        crnt_ttl = 1
        for crnt_el, next_el in zip(seq[:-1], seq[1:]):
            if is_equal(crnt_el, next_el):
                crnt_ttl += 1
            else:
                yield crnt_el, crnt_ttl
                crnt_ttl = 1

        # final step has same elements, so we need to yield one last time
        if is_equal(crnt_el, next_el):
            yield crnt_el, crnt_ttl
        else:
            yield next_el, 1


def is_equal(x: Any, y: Any) -> bool:
    return x is not None and x == y


def cols_width(data: GTSelf, cases: Dict[str, str]) -> GTSelf:
    """Set the widths of columns.

    Manual specifications of column widths can be performed using the `cols_width()` method. We
    choose which columns get specific widths. This can be in units of pixels or as percentages.
    Width assignments are supplied inside of a dictionary where columns are the keys and the
    corresponding width is the value.

    Parameters
    ----------
    cases : Dict[str, str]
        A dictionary where the keys are column names and the values are the widths. Widths can be
        specified in pixels (e.g., `"50px"`) or as percentages (e.g., `"20%"`).

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's use select columns from the `exibble` dataset to create a new table. We can specify the
    widths of columns with `cols_width()`. This is done by specifying the exact widths for table
    columns in a dictionary. In this example, we'll set the width of the `num` column to `"150px"`,
    the `char` column to `"100px"`, the `date` column to `"300px"`. All other columns won't be
    affected (their widths will be automatically set by their content).

    ```{python}
    from great_tables import GT, exibble

    exibble_mini = exibble[["num", "char", "date", "datetime", "row"]].head(5)

    (
        GT(exibble_mini)
        .cols_width(
            cases={
                "num": "150px",
                "char": "100px",
                "date": "300px"
            }
        )
    )
    ```

    We can also specify the widths of columns as percentages. In this example, we'll set the width
    of the `num` column to `"20%"`, the `char` column to `"10%"`, and the `date` column to `"30%"`.
    Note that the percentages are relative and don't need to sum to 100%.

    ```{python}
    (
        GT(exibble_mini)
        .cols_width(
            cases={
                "num": "20%",
                "char": "10%",
                "date": "30%"
            }
        )
    )
    ```

    We can also mix and match pixel and percentage widths. In this example, we'll set the width of
    the `num` column to `"150px"`, the `char` column to `"10%"`, and the `date` column to `"30%"`.

    ```{python}
    (
        GT(exibble_mini)
        .cols_width(
            cases={
                "num": "150px",
                "char": "10%",
                "date": "30%"
            }
        )
    )
    ```

    If we set the width of all columns, the table will be forced to use the specified widths (i.e.,
    a column width less than the content width will be honored). In this next example, we'll set
    widths for all columns. This is a good way to ensure that the widths you specify are fully
    respected (and not overridden by automatic width calculations).

    ```{python}
    (
        GT(exibble_mini)
        .cols_width(
            cases={
                "num": "30px",
                "char": "100px",
                "date": "100px",
                "datetime": "200px",
                "row": "50px"
            }
        )
    )
    ```

    Notice that in the above example, the `num` column is very small (only `30px`) and the content
    overflows. When not specifying the width of all columns, the table will automatically adjust the
    column widths based on the content (and you wouldn't get the overflowing behavior seen in the
    previous example).
    """

    curr_boxhead = data._boxhead

    for col, width in cases.items():
        curr_boxhead = curr_boxhead._set_column_width(col, width)

    return data._replace(_boxhead=curr_boxhead)
