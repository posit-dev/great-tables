from __future__ import annotations

import itertools

from dataclasses import dataclass
from functools import singledispatch
from typing import TYPE_CHECKING, Literal, List, Callable, Union
from typing_extensions import TypeAlias

# note that types like Spanners are only used in annotations for concretes of the
# resolve generic, but we need to import at runtime, due to singledispatch looking
# up annotations
from ._gt_data import GTData, FootnoteInfo, Spanners, ColInfoTypeEnum, StyleInfo, FootnotePlacement
from ._tbl_data import eval_select, eval_transform, PlExpr, PlDataFrame
from ._styles import CellStyle


if TYPE_CHECKING:
    from ._gt_data import TblData
    from ._tbl_data import SelectExpr

# Misc Types ===========================================================================

PlacementOptions: TypeAlias = Literal["auto", "left", "right"]
RowSelectExpr: TypeAlias = Union[List[int], PlExpr, Callable[["TblData"], bool], None]

# Locations ============================================================================
# TODO: these are called cells_* in gt. I prefixed them with Loc just to keep things
# straight while going through helpers.R, but no strong opinion on naming!


@dataclass
class CellPos:
    """The position of a cell in a DataFrame."""

    column: int
    row: int
    colname: str


@dataclass
class Loc:
    """A location."""


@dataclass
class LocTitle(Loc):
    """A location for targeting the table title and subtitle."""

    groups: Literal["title", "subtitle"]


@dataclass
class LocStubhead(Loc):
    groups: Literal["stubhead"] = "stubhead"


@dataclass
class LocColumnSpanners(Loc):
    """A location for column spanners."""

    # TODO: these can also be tidy selectors
    ids: list[str]


@dataclass
class LocColumnLabels(Loc):
    # TODO: these can be tidyselectors
    columns: list[str]


@dataclass
class LocRowGroups(Loc):
    # TODO: these can be tidyselectors
    groups: list[str]


@dataclass
class LocStub(Loc):
    # TODO: these can be tidyselectors
    # TODO: can this take integers?
    rows: list[str]


@dataclass
class LocBody(Loc):
    # TODO: these can be tidyselectors
    """A location specification for targeting data cells in the table body.

    The `loc.body()` class is used to target the data cells in the table body. The class can be used
    to apply custom styling with the `tab_style()` method. That method has a `locations` argument
    and this class should be used there to perform the targeting.

    Parameters
    ----------
    columns : SelectExpr
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    rows : list[str | int]
        The rows to target. Can either be a single row name or a series of row names provided in a
        list.

    Returns
    -------
    LocBody
        A LocBody object, which is used for a `locations` argument if specifying the table body.
    """
    columns: SelectExpr = None
    rows: RowSelectExpr = None


@dataclass
class LocSummary(Loc):
    # TODO: these can be tidyselectors
    groups: list[str]
    columns: list[str]
    rows: list[str]


@dataclass
class LocGrandSummary(Loc):
    # TODO: these can be tidyselectors
    columns: list[str]
    rows: list[str]


@dataclass
class LocStubSummary(Loc):
    # TODO: these can be tidyselectors
    groups: list[str]
    rows: list[str]


@dataclass
class LocStubGrandSummary(Loc):
    rows: list[str]


@dataclass
class LocFootnotes(Loc):
    groups: Literal["footnotes"] = "footnotes"


@dataclass
class LocSourceNotes(Loc):
    # This dataclass in R has a `groups` field, which is a literal value.
    # In python, we can use an isinstance check to determine we're seeing an
    # instance of this class
    groups: Literal["source_notes"] = "source_notes"


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
    if set_expr - set(candidates):
        missing = set_expr - set(candidates)
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
        if isinstance(expr, list) and "stub()" in expr:
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
) -> list[tuple[str, int]]:
    """Return matching row numbers, based on expr

    Note that this function needs to handle 2 important cases:
      * tidyselect: everything()
      * filter-like: _.cyl == 4

    Unlike tidyselect::eval_select, this function returns names in
    the order they appear in the data (rather than ordered by selectors).
    """

    if isinstance(expr, (str, int)):
        expr: List["str | int"] = [expr]

    if isinstance(data, GTData):
        if expr is None:
            if null_means == "everything":
                return [(row.rowname, ii) for ii, row in enumerate(data._stub)]
            else:
                return []

        row_names = [row.rowname for row in data._stub]
    else:
        row_names = data

    if isinstance(expr, list):
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
def resolve(loc: Loc, *args, **kwargs) -> "Loc | List[CellPos]":
    """Return a copy of location with lookups resolved (e.g. tidyselect on columns)."""
    raise NotImplementedError(f"Unsupported location type: {type(loc)}")


@resolve.register
def _(loc: LocColumnSpanners, spanners: Spanners) -> LocColumnSpanners:
    # unique labels (with order preserved)
    spanner_ids = [span.spanner_id for span in spanners]

    resolved_spanners_idx = resolve_vector_i(loc.ids, spanner_ids, item_label="spanner")
    resolved_spanners = [spanner_ids[idx] for idx in resolved_spanners_idx]

    # Create a list object
    return LocColumnSpanners(ids=resolved_spanners)


@resolve.register
def _(loc: LocBody, data: GTData) -> List[CellPos]:
    cols = resolve_cols_i(data=data, expr=loc.columns)
    rows = resolve_rows_i(data=data, expr=loc.rows)

    # TODO: dplyr arranges by `Var1`, and does distinct (since you can tidyselect the same
    # thing multiple times
    cell_pos = [
        CellPos(col[1], row[1], colname=col[0]) for col, row in itertools.product(cols, rows)
    ]

    return cell_pos


# Style generic ========================================================================


@singledispatch
def set_style(loc: Loc, data: GTData, style: List[str]) -> GTData:
    """Set style for location."""
    raise NotImplementedError(f"Unsupported location type: {type(loc)}")


@set_style.register
def _(loc: LocTitle, data: GTData, style: List[CellStyle]) -> GTData:
    # validate ----
    for entry in style:
        entry._raise_if_requires_data(loc)

    # set ----
    if loc.groups == "title":
        info = StyleInfo(locname="title", locnum=1, styles=style)
    elif loc.groups == "subtitle":
        info = StyleInfo(locname="subtitle", locnum=2, styles=style)
    else:
        raise ValueError(f"Unknown title group: {loc.groups}")

    return data._styles.append(info)


@set_style.register
def _(loc: LocBody, data: GTData, style: List[CellStyle]) -> GTData:
    positions: List[CellPos] = resolve(loc, data)

    # evaluate any column expressions in styles
    style_ready = [entry._evaluate_expressions(data._tbl_data) for entry in style]

    all_info: list[StyleInfo] = []
    for col_pos in positions:
        row_styles = [entry._from_row(data._tbl_data, col_pos.row) for entry in style_ready]
        crnt_info = StyleInfo(
            locname="data", locnum=5, colname=col_pos.colname, rownum=col_pos.row, styles=row_styles
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
    info = FootnoteInfo(locname="none", locnum=0, footnotes=[footnote], placement=place)

    return data._replace(_footnotes=data._footnotes + [info])


@set_footnote.register
def _(loc: LocTitle, data: GTData, footnote: str, placement: PlacementOptions) -> GTData:
    # TODO: note that footnote here is annotated as a string, but I think that in R it
    # can be a list of strings.
    place = FootnotePlacement[placement]
    if loc.groups == "title":
        info = FootnoteInfo(locname="title", locnum=1, footnotes=[footnote], placement=place)
    elif loc.groups == "subtitle":
        info = FootnoteInfo(locname="subtitle", locnum=2, footnotes=[footnote], placement=place)
    else:
        raise ValueError(f"Unknown title group: {loc.groups}")

    return data._replace(_footnotes=data._footnotes + [info])
