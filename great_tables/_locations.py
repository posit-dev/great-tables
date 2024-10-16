from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from functools import singledispatch
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal, Union

from typing_extensions import TypeAlias

# note that types like Spanners are only used in annotations for concretes of the
# resolve generic, but we need to import at runtime, due to singledispatch looking
# up annotations
from ._gt_data import (
    ColInfoTypeEnum,
    FootnoteInfo,
    FootnotePlacement,
    GTData,
    Spanners,
    StyleInfo,
)
from ._styles import CellStyle
from ._tbl_data import PlDataFrame, PlExpr, eval_select, eval_transform

if TYPE_CHECKING:
    from ._gt_data import TblData
    from ._tbl_data import SelectExpr

# Misc Types ===========================================================================

PlacementOptions: TypeAlias = Literal["auto", "left", "right"]
RowSelectExpr: TypeAlias = 'list[int] | PlExpr | Callable[["TblData"], bool] | None'

# Locations ============================================================================
# TODO: these are called cells_* in gt. I prefixed them with Loc just to keep things
# straight while going through helpers.R, but no strong opinion on naming!


@dataclass
class CellPos:
    """The position of a cell in a DataFrame."""

    column: int
    row: int
    colname: str
    rowname: str | None = None


@dataclass
class Loc:
    """A location."""


@dataclass
class LocHeader(Loc):
    """Target the table header (title and subtitle).

    With `loc.header()`, we can target the table header which contains the title and the subtitle.
    This is useful for applying custom styling with the
    [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a `locations=` argument and
    this class should be used there to perform the targeting.

    Returns
    -------
    LocHeader
        A LocHeader object, which is used for a `locations=` argument if specifying the title of the
        table.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. We will style the entire table header
    (the 'title' and 'subtitle' parts. This can be done by using `locations=loc.header()` within
    [`tab_style()`](`great_tables.GT.tab_style`).

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(gtcars[["mfr", "model", "msrp"]].head(5))
        .tab_header(
            title="Select Cars from the gtcars Dataset",
            subtitle="Only the first five cars are displayed"
        )
        .tab_style(
            style=style.fill(color="lightblue"),
            locations=loc.header()
        )
        .fmt_currency(columns="msrp", decimals=0)
    )
    ```
    """


@dataclass
class LocTitle(Loc):
    """Target the table title.

    With `loc.title()`, we can target the part of table containing the title (within the table
    header). This is useful for applying custom styling with the
    [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a `locations=` argument and
    this class should be used there to perform the targeting.

    Returns
    -------
    LocTitle
        A LocTitle object, which is used for a `locations=` argument if specifying the title of the
        table.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. We will style only the 'title' part
    of the table header (leaving the 'subtitle' part unaffected). This can be done by using
    `locations=loc.title()` within [`tab_style()`](`great_tables.GT.tab_style`).

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(gtcars[["mfr", "model", "msrp"]].head(5))
        .tab_header(
            title="Select Cars from the gtcars Dataset",
            subtitle="Only the first five cars are displayed"
        )
        .tab_style(
            style=style.text(color="blue", size="large", weight="bold"),
            locations=loc.title()
        )
        .fmt_currency(columns="msrp", decimals=0)
    )
    ```
    """


@dataclass
class LocSubTitle(Loc):
    """Target the table subtitle.

    With `loc.subtitle()`, we can target the part of table containing the subtitle (within the table
    header). This is useful for applying custom styling with the
    [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a `locations=` argument and
    this class should be used there to perform the targeting.

    Returns
    -------
    LocSubTitle
        A LocSubTitle object, which is used for a `locations=` argument if specifying the subtitle
        of the table.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. We will style only the 'subtitle'
    part of the table header (leaving the 'title' part unaffected). This can be done by using
    `locations=loc.subtitle()` within [`tab_style()`](`great_tables.GT.tab_style`).

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(gtcars[["mfr", "model", "msrp"]].head(5))
        .tab_header(
            title="Select Cars from the gtcars Dataset",
            subtitle="Only the first five cars are displayed"
        )
        .tab_style(
            style=style.fill(color="lightblue"),
            locations=loc.subtitle()
        )
        .fmt_currency(columns="msrp", decimals=0)
    )
    ```
    """


@dataclass
class LocStubhead(Loc):
    """Target the stubhead.

    With `loc.stubhead()`, we can target the part of table that resides both at the top of the
    stub and also beside the column header. This is useful for applying custom styling with the
    [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a `locations=` argument and
    this class should be used there to perform the targeting.

    Returns
    -------
    LocStubhead
        A LocStubhead object, which is used for a `locations=` argument if specifying the stubhead
        of the table.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. This table contains a stub (produced
    by setting `rowname_col="model"` in the initial `GT()` call). The stubhead is given a label by
    way of the [`tab_stubhead()`](`great_tables.GT.tab_stubhead`) method and this label can be
    styled by using `locations=loc.stubhead()` within [`tab_style()`](`great_tables.GT.tab_style`).

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(
            gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
            rowname_col="model",
            groupname_col="mfr"
        )
        .tab_stubhead(label="car")
        .tab_style(
            style=style.text(color="red", weight="bold"),
            locations=loc.stubhead()
        )
        .fmt_integer(columns=["hp", "trq"])
        .fmt_currency(columns="msrp", decimals=0)
    )
    ```
    """


@dataclass
class LocStubheadLabel(Loc):
    """Target the stubhead label."""


@dataclass
class LocColumnHeader(Loc):
    """Target column spanners and column labels.

    With `loc.column_header()`, we can target the column header which contains all of the column
    labels and any spanner labels that are present. This is useful for applying custom styling with
    the [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a `locations=` argument
    and this class should be used there to perform the targeting.

    Returns
    -------
    LocColumnHeader
        A LocColumnHeader object, which is used for a `locations=` argument if specifying the column
        header of the table.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. We create spanner labels through
    use of the [`tab_spanner()`](`great_tables.GT.tab_spanner`) method; this gives us a column
    header with a mix of column labels and spanner labels. We will style the entire column header at
    once by using `locations=loc.column_header()` within
    [`tab_style()`](`great_tables.GT.tab_style`).

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5))
        .tab_spanner(
            label="performance",
            columns=["hp", "trq"]
        )
        .tab_spanner(
            label="make and model",
            columns=["mfr", "model"]
        )
        .tab_style(
            style=[
                style.text(color="white", weight="bold"),
                style.fill(color="steelblue")
            ],
            locations=loc.column_header()
        )
        .fmt_integer(columns=["hp", "trq"])
        .fmt_currency(columns="msrp", decimals=0)
    )
    ```
    """


@dataclass
class LocColumnLabels(Loc):
    """Target column labels.

    With `loc.column_labels()`, we can target the cells containing the column labels. This is useful
    for applying custom styling with the [`tab_style()`](`great_tables.GT.tab_style`) method. That
    method has a `locations=` argument and this class should be used there to perform the targeting.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list. If no columns are specified, all columns are targeted.

    Returns
    -------
    LocColumnLabels
        A LocColumnLabels object, which is used for a `locations=` argument if specifying the
        table's column labels.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. We will style all three of the column
    labels by using `locations=loc.column_labels()` within
    [`tab_style()`](`great_tables.GT.tab_style`). Note that no specification of `columns=` is needed
    here because we want to target all columns.

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(gtcars[["mfr", "model", "msrp"]].head(5))
        .tab_style(
            style=style.text(color="blue", size="large", weight="bold"),
            locations=loc.column_labels()
        )
    )
    ```
    """

    columns: SelectExpr = None


@dataclass
class LocSpannerLabels(Loc):
    """Target spanner labels.

    With `loc.spanner_labels()`, we can target the cells containing the spanner labels. This is
    useful for applying custom styling with the [`tab_style()`](`great_tables.GT.tab_style`) method.
    That method has a `locations=` argument and this class should be used there to perform the
    targeting.

    Parameters
    ----------
    ids:
        The ID values for the spanner labels to target. A list of one or more ID values is required.

    Returns
    -------
    LocSpannerLabels
        A LocSpannerLabels object, which is used for a `locations=` argument if specifying the
        table's spanner labels.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. We create two spanner labels through
    two separate calls of the [`tab_spanner()`](`great_tables.GT.tab_spanner`) method. In each of
    those, the text supplied to `label=` argument is used as the ID value (though they have to be
    explicitly set via the `id=` argument). We will style only the spanner label having the text
    `"performance"` by using `locations=loc.spanner_labels(ids=["performance"])` within
    [`tab_style()`](`great_tables.GT.tab_style`).

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5))
        .tab_spanner(
            label="performance",
            columns=["hp", "trq"]
        )
        .tab_spanner(
            label="make and model",
            columns=["mfr", "model"]
        )
        .tab_style(
            style=style.text(color="blue", weight="bold"),
            locations=loc.spanner_labels(ids=["performance"])
        )
        .fmt_integer(columns=["hp", "trq"])
        .fmt_currency(columns="msrp", decimals=0)
    )
    ```
    """

    ids: SelectExpr = None


@dataclass
class LocStub(Loc):
    """Target the table stub.

    With `loc.stub()` we can target the cells containing the row labels, which reside in the table
    stub. This is useful for applying custom styling with the
    [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a `locations=` argument and
    this class should be used there to perform the targeting.

    Parameters
    ----------
    rows
        The rows to target within the stub. Can either be a single row name or a series of row names
        provided in a list. If no rows are specified, all rows are targeted.

    Returns
    -------
    LocStub
        A LocStub object, which is used for a `locations=` argument if specifying the table's stub.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. We will style the entire table stub
    (the row labels) by using `locations=loc.stub()` within
    [`tab_style()`](`great_tables.GT.tab_style`).

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(
            gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
            rowname_col="model",
            groupname_col="mfr"
        )
        .tab_stubhead(label="car")
        .tab_style(
            style=[
                style.text(color="crimson", weight="bold"),
                style.fill(color="lightgray")
            ],
            locations=loc.stub()
        )
        .fmt_integer(columns=["hp", "trq"])
        .fmt_currency(columns="msrp", decimals=0)
    )
    ```
    """

    rows: RowSelectExpr = None


@dataclass
class LocRowGroups(Loc):
    """Target row groups.

    With `loc.row_groups()` we can target the cells containing the row group labels, which span
    across the table body. This is useful for applying custom styling with the
    [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a `locations=` argument and
    this class should be used there to perform the targeting.

    Parameters
    ----------
    rows
        The row groups to target. Can either be a single group name or a series of group names
        provided in a list. If no groups are specified, all are targeted.

    Returns
    -------
    LocRowGroups
        A LocRowGroups object, which is used for a `locations=` argument if specifying the table's
        row groups.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. We will style all of the cells
    comprising the row group labels by using `locations=loc.row_groups()` within
    [`tab_style()`](`great_tables.GT.tab_style`).

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(
            gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
            rowname_col="model",
            groupname_col="mfr"
        )
        .tab_stubhead(label="car")
        .tab_style(
            style=[
                style.text(color="crimson", weight="bold"),
                style.fill(color="lightgray")
            ],
            locations=loc.row_groups()
        )
        .fmt_integer(columns=["hp", "trq"])
        .fmt_currency(columns="msrp", decimals=0)
    )
    ```
    """

    rows: RowSelectExpr = None


@dataclass
class LocSummaryLabel(Loc):
    rows: RowSelectExpr = None


@dataclass
class LocBody(Loc):
    # TODO: these can be tidyselectors
    """Target data cells in the table body.

    With `loc.body()`, we can target the data cells in the table body. This is useful for applying
    custom styling with the [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a
    `locations=` argument and this class should be used there to perform the targeting.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    rows
        The rows to target. Can either be a single row name or a series of row names provided in a
        list.

    Returns
    -------
    LocBody
        A LocBody object, which is used for a `locations=` argument if specifying the table body.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. We will style all of the body cells
    by using `locations=loc.body()` within [`tab_style()`](`great_tables.GT.tab_style`).

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(
            gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
            rowname_col="model",
            groupname_col="mfr"
        )
        .tab_stubhead(label="car")
        .tab_style(
            style=[
                style.text(color="darkblue", weight="bold"),
                style.fill(color="gainsboro")
            ],
            locations=loc.body()
        )
        .fmt_integer(columns=["hp", "trq"])
        .fmt_currency(columns="msrp", decimals=0)
    )
    ```
    """

    columns: SelectExpr = None
    rows: RowSelectExpr = None


@dataclass
class LocSummary(Loc):
    # TODO: these can be tidyselectors
    columns: SelectExpr = None
    rows: RowSelectExpr = None


@dataclass
class LocFooter(Loc):
    """Target the table footer.

    With `loc.footer()` we can target the table's footer, which currently contains the source notes
    (and may contain a 'footnotes' location in the future). This is useful when applying custom
    styling with the [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a
    `locations=` argument and this class should be used there to perform the targeting. The 'footer'
    location is generated by [`tab_source_note()`](`great_tables.GT.tab_source_note`).

    Returns
    -------
    LocFooter
        A `LocFooter` object, which is used for a `locations=` argument if specifying the footer of
        the table.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. Add a source note (with
    [`tab_source_note()`](`great_tables.GT.tab_source_note`) and style this footer section inside of
    [`tab_style()`](`great_tables.GT.tab_style`) with `locations=loc.footer()`.

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(gtcars[["mfr", "model", "msrp"]].head(5))
        .tab_source_note(source_note="From edmunds.com")
        .tab_style(
            style=style.text(color="blue", size="small", weight="bold"),
            locations=loc.footer()
        )
    )
    ```
    """


@dataclass
class LocFootnotes(Loc):
    """Target the footnotes."""


@dataclass
class LocSourceNotes(Loc):
    """Target the source notes.

    With `loc.source_notes()`, we can target the source notes in the table. This is useful when
    applying custom with the [`tab_style()`](`great_tables.GT.tab_style`) method. That method has a
    `locations=` argument and this class should be used there to perform the targeting. The
    'source_notes' location is generated by
    [`tab_source_note()`](`great_tables.GT.tab_source_note`).

    Returns
    -------
    LocSourceNotes
        A `LocSourceNotes` object, which is used for a `locations=` argument if specifying the
        source notes.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset in a new table. Add a source note (with
    [`tab_source_note()`](`great_tables.GT.tab_source_note`) and style the source notes section
    inside [`tab_style()`](`great_tables.GT.tab_style`) with `locations=loc.source_notes()`.

    ```{python}
    from great_tables import GT, style, loc
    from great_tables.data import gtcars

    (
        GT(gtcars[["mfr", "model", "msrp"]].head(5))
        .tab_source_note(source_note="From edmunds.com")
        .tab_style(
            style=style.text(color="blue", size="small", weight="bold"),
            locations=loc.source_notes()
        )
    )
    ```
    """


# Utils ================================================================================
# Note that there are three kinds of functions below:
#   * resolve_vector_* functions are largely for selecting from spanner names.
#   * resolve_rows_* are for resolving locations for styles. These can select by name,
#     or a predicate.
#   * resolve_cols_* functions select columns using tidyselect.


def resolve_vector_i(expr: list[str], candidates: list[str], item_label: str) -> list[int]:
    """Return list of indices for candidates, selected by expr."""

    mask = resolve_vector_l(expr, candidates, item_label)
    return [ii for ii, val in enumerate(mask) if val]


def resolve_vector_l(expr: list[str], candidates: list[str], item_label: str) -> list[bool]:
    """Return list of logical index for candidates, selected by expr."""

    if not (isinstance(expr, list) and all(isinstance(x, str) for x in expr)):
        raise NotImplementedError("Selecting entries currently requires a list of strings.")

    set_expr = set(expr)
    if missing := (set_expr - set(candidates)):
        raise ValueError(f"Cannot find these entries: {missing}")

    return [candidate in set_expr for candidate in candidates]


def resolve_cols_c(
    data: GTData,
    expr: SelectExpr,
    strict: bool = True,
    excl_stub: bool = True,
    excl_group: bool = True,
    null_means: Literal["everything", "nothing"] = "everything",
) -> list[str]:
    """Return a list of column names, selected by expr."""
    selected = resolve_cols_i(
        data=data,
        expr=expr,
        strict=strict,
        excl_stub=excl_stub,
        excl_group=excl_group,
        null_means=null_means,
    )
    return [name_pos[0] for name_pos in selected]


def resolve_cols_i(
    data: GTData | TblData,
    expr: SelectExpr,
    strict: bool = True,
    excl_stub: bool = True,
    excl_group: bool = True,
    null_means: Literal["everything", "nothing"] = "everything",
) -> list[tuple[str, int]]:
    """Return a tuple of (column name, position) pairs, selected by expr."""

    if isinstance(data, GTData):
        stub_var = data._boxhead.vars_from_type(ColInfoTypeEnum.stub)
        group_var = data._boxhead.vars_from_type(ColInfoTypeEnum.row_group)

        # TODO: special handling of "stub()"
        if isinstance(expr, list) and any(isinstance(x, str) and x == "stub()" for x in expr):
            if len(stub_var):
                return [(stub_var[0], 1)]

            return []

        # If expr is None, we want to select everything or nothing depending on
        # the value of `null_means`
        if expr is None:
            if null_means == "everything":
                cols_excl = [*(stub_var if excl_stub else []), *(group_var if excl_group else [])]

                return [
                    (col, ii)
                    for ii, col in enumerate(data._tbl_data.columns)
                    if col not in cols_excl
                ]

            else:
                return []

        if not excl_stub:
            # In most cases we would want to exclude the column that
            # represents the stub but that isn't always the case (e.g.,
            # when considering the stub for column sizing); the `excl_stub`
            # argument will determine whether the stub column is obtained
            # for exclusion or not (if FALSE, we get NULL which removes the
            # stub, if present, from `cols_excl`)
            stub_var = None

        if not excl_group:
            # The columns that represent the group rows are usually
            # always excluded but in certain cases (i.e., `rows_add()`)
            # we may want to include this column
            _group_vars = data._boxhead.vars_from_type(ColInfoTypeEnum.row_group)
            group_var = _group_vars[0] if len(_group_vars) else None
        else:
            group_var = None

        cols_excl = [stub_var, group_var]

        tbl_data = data._tbl_data
    else:
        # I am not sure if this gets used in the R program, but it's
        # convenient for testing
        tbl_data = data
        cols_excl = []

    selected = eval_select(tbl_data, expr, strict)
    return [name_pos for name_pos in selected if name_pos[0] not in cols_excl]


# resolving rows ----


def resolve_rows_i(
    data: GTData | list[str],
    expr: RowSelectExpr = None,
    null_means: Literal["everything", "nothing"] = "everything",
    row_name_attr: Literal["rowname", "group_id"] = "rowname",
) -> list[tuple[str, int]]:
    """Return matching row numbers, based on expr

    Note that this function needs to handle 2 important cases:
      * tidyselect: everything()
      * filter-like: _.cyl == 4

    Unlike tidyselect::eval_select, this function returns names in
    the order they appear in the data (rather than ordered by selectors).
    """

    if isinstance(expr, (str, int)):
        expr: list[str | int] = [expr]

    if isinstance(data, GTData):
        row_names = [getattr(row, row_name_attr) for row in data._stub]
    else:
        row_names = data

    if expr is None:
        if null_means == "everything":
            return [(name, ii) for ii, name in enumerate(row_names)]
        else:
            return []

    elif isinstance(expr, list):
        # TODO: manually doing row selection here for now
        target_names = set(x for x in expr if isinstance(x, str))
        target_pos = set(
            indx if indx >= 0 else len(row_names) + indx for indx in expr if isinstance(indx, int)
        )

        selected = [
            (name, ii)
            for ii, name in enumerate(row_names)
            if (name in target_names or ii in target_pos)
        ]
        return selected

    elif isinstance(expr, PlExpr):
        # TODO: decide later on the name supplied to `name`
        # with_row_index supercedes with_row_count
        frame: PlDataFrame = data._tbl_data
        meth_row_number = getattr(frame, "with_row_index", None)
        if not meth_row_number:
            meth_row_number = frame.with_row_count

        result = meth_row_number(name="__row_number__").filter(expr)
        return [(row_names[ii], ii) for ii in result["__row_number__"]]

    elif callable(expr):
        res: "list[bool]" = eval_transform(data._tbl_data, expr)
        if not all(map(lambda x: isinstance(x, bool), res)):
            raise ValueError(
                "If you select rows using a callable, it must take a DataFrame, "
                "and return a boolean Series."
            )
        return [(row_names[ii], ii) for ii, val in enumerate(res) if val]

    # TODO: identify filter-like selectors using some backend check
    # e.g. if it's a siuba expression vs tidyselect expression, etc..
    # TODO: how would this be handled with something like polars? May need a predicate
    # function, similar in spirit to where()?
    raise NotImplementedError(
        "Currently, rows can only be selected using these approaches:\n\n"
        "  * a list of integers\n"
        "  * a polars expression\n"
        "  * a callable that takes a DataFrame and returns a boolean Series"
    )


# Resolve generic ======================================================================


@singledispatch
def resolve(loc: Loc, *args: Any, **kwargs: Any) -> Loc | list[CellPos]:
    """Return a copy of location with lookups resolved (e.g. tidyselect on columns)."""
    raise NotImplementedError(f"Unsupported location type: {type(loc)}")


@resolve.register
def _(loc: LocSpannerLabels, spanners: Spanners) -> LocSpannerLabels:
    # unique labels (with order preserved)
    spanner_ids = [span.spanner_id for span in spanners]

    resolved_spanners_idx = resolve_vector_i(loc.ids, spanner_ids, item_label="spanner")
    resolved_spanners = [spanner_ids[idx] for idx in resolved_spanners_idx]

    # Create a list object
    return LocSpannerLabels(ids=resolved_spanners)


@resolve.register
def _(loc: LocColumnLabels, data: GTData) -> list[tuple[str, int]]:
    name_pos = resolve_cols_i(data=data, expr=loc.columns)
    return name_pos


@resolve.register
def _(loc: LocRowGroups, data: GTData) -> set[int]:
    # TODO: what are the rules for matching row groups?
    # TODO: resolve_rows_i will match a list expr to row names (not group names)
    group_pos = set(name for name, _ in resolve_rows_i(data, loc.rows, row_name_attr="group_id"))
    return group_pos


@resolve.register
def _(loc: LocStub, data: GTData) -> set[int]:
    # TODO: what are the rules for matching row groups?
    rows = resolve_rows_i(data=data, expr=loc.rows)
    cell_pos = set(row[1] for row in rows)
    return cell_pos


@resolve.register
def _(loc: LocBody, data: GTData) -> list[CellPos]:
    cols = resolve_cols_i(data=data, expr=loc.columns)
    rows = resolve_rows_i(data=data, expr=loc.rows)

    # TODO: dplyr arranges by `Var1`, and does distinct (since you can tidyselect the same
    # thing multiple times
    cell_pos = [
        CellPos(col[1], row[1], colname=col[0]) for col, row in itertools.product(cols, rows)
    ]

    return cell_pos


# Style generic ========================================================================


# LocHeader
# LocTitle
# LocSubTitle
# LocStubhead
# LocStubheadLabel
# LocColumnLabels
# LocColumnLabel
# LocSpannerLabel
# LocStub
# LocRowGroupLabel
# LocRowLabel
# LocSummaryLabel
# LocBody
# LocSummary
# LocFooter
# LocFootnotes
# LocSourceNotes


@singledispatch
def set_style(loc: Loc, data: GTData, style: list[str]) -> GTData:
    """Set style for location."""
    raise NotImplementedError(f"Unsupported location type: {type(loc)}")


@set_style.register(LocHeader)
@set_style.register(LocTitle)
@set_style.register(LocSubTitle)
@set_style.register(LocStubhead)
@set_style.register(LocStubheadLabel)
@set_style.register(LocColumnHeader)
@set_style.register(LocFooter)
@set_style.register(LocSourceNotes)
def _(
    loc: (
        LocHeader
        | LocTitle
        | LocSubTitle
        | LocStubhead
        | LocStubheadLabel
        | LocColumnHeader
        | LocFooter
        | LocSourceNotes
    ),
    data: GTData,
    style: list[CellStyle],
) -> GTData:
    # validate ----
    for entry in style:
        entry._raise_if_requires_data(loc)

    return data._replace(_styles=data._styles + [StyleInfo(locname=loc, styles=style)])


@set_style.register
def _(loc: LocColumnLabels, data: GTData, style: list[CellStyle]) -> GTData:
    selected = resolve(loc, data)

    # evaluate any column expressions in styles
    styles = [entry._evaluate_expressions(data._tbl_data) for entry in style]

    all_info: list[StyleInfo] = []
    for name, pos in selected:
        crnt_info = StyleInfo(
            locname=loc,
            colname=name,
            styles=styles,
        )
        all_info.append(crnt_info)
    return data._replace(_styles=data._styles + all_info)


@set_style.register
def _(loc: LocSpannerLabels, data: GTData, style: list[CellStyle]) -> GTData:
    # validate ----
    for entry in style:
        entry._raise_if_requires_data(loc)
    # TODO resolve

    new_loc = resolve(loc, data._spanners)
    return data._replace(
        _styles=data._styles + [StyleInfo(locname=new_loc, grpname=new_loc.ids, styles=style)]
    )


@set_style.register
def _(loc: LocRowGroups, data: GTData, style: list[CellStyle]) -> GTData:
    # validate ----
    for entry in style:
        entry._raise_if_requires_data(loc)

    row_groups = resolve(loc, data)
    return data._replace(
        _styles=data._styles + [StyleInfo(locname=loc, grpname=row_groups, styles=style)]
    )


@set_style.register
def _(loc: LocStub, data: GTData, style: list[CellStyle]) -> GTData:
    # validate ----
    for entry in style:
        entry._raise_if_requires_data(loc)
    # TODO resolve
    cells = resolve(loc, data)

    new_styles = [StyleInfo(locname=loc, rownum=rownum, styles=style) for rownum in cells]
    return data._replace(_styles=data._styles + new_styles)


@set_style.register
def _(loc: LocBody, data: GTData, style: list[CellStyle]) -> GTData:
    positions: list[CellPos] = resolve(loc, data)

    # evaluate any column expressions in styles
    style_ready = [entry._evaluate_expressions(data._tbl_data) for entry in style]

    all_info: list[StyleInfo] = []
    for col_pos in positions:
        row_styles = [entry._from_row(data._tbl_data, col_pos.row) for entry in style_ready]
        crnt_info = StyleInfo(
            locname=loc, colname=col_pos.colname, rownum=col_pos.row, styles=row_styles
        )
        all_info.append(crnt_info)

    return data._replace(_styles=data._styles + all_info)


# Set footnote generic =================================================================


@singledispatch
def set_footnote(loc: Loc, data: GTData, footnote: str, placement: PlacementOptions) -> GTData:
    """Set footnote for location."""
    raise NotImplementedError(f"Unsupported location type: {type(loc)}")


@set_footnote.register(type(None))
def _(loc: None, data: GTData, footnote: str, placement: PlacementOptions) -> GTData:
    place = FootnotePlacement[placement]
    info = FootnoteInfo(locname="none", footnotes=[footnote], placement=place)

    return data._replace(_footnotes=data._footnotes + [info])


@set_footnote.register
def _(loc: LocTitle, data: GTData, footnote: str, placement: PlacementOptions) -> GTData:
    raise NotImplementedError()
