from __future__ import annotations

from dataclasses import dataclass, fields
from functools import singledispatch
from typing import TYPE_CHECKING, Literal, get_origin, get_type_hints

# note that types like Spanners are only used in annotations for concretes of the
# resolve generic, but we need to import at runtime, due to singledispatch looking
# up annotations
from ._gt_data import GTData, Spanners, ColInfoTypeEnum
from ._tbl_data import eval_select


if TYPE_CHECKING:
    from ._gt_data import TblData


# Locations ============================================================================
# TODO: these are called cells_* in gt. I prefixed them with Loc just to keep things
# straight while going through helpers.R, but no strong opinion on naming!


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
    columns: list[str]
    rows: list[str]


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
    expr: list[str],
    data: GTData,
    strict: bool = True,
    excl_stub: bool = True,
    excl_group: bool = True,
    null_means: Literal["everything", "nothing"] = "everything",
) -> list[str]:
    selected = resolve_cols_i(expr, data, strict, excl_stub, excl_group, null_means)
    return [name_pos[0] for name_pos in selected]


def resolve_cols_i(
    expr: list[str],
    data: GTData,
    strict: bool = True,
    excl_stub: bool = True,
    excl_group: bool = True,
    null_means: Literal["everything", "nothing"] = "everything",
) -> list[tuple[str, int]]:
    """Return a tuple of (column name, position) pairs, selected by expr."""

    if isinstance(data, GTData):
        stub_var = data._boxhead.vars_from_type(ColInfoTypeEnum.stub)

        # TODO: special handling of "stub()"
        if "stub()" in expr:
            if len(stub_var):
                return [(stub_var[0], 1)]

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
        # TODO: is this path used? In the R program, cols_excl isn't set, so it seems
        # like it must not get used.
        tbl_data = data._tbl_data
        cols_excl = []

    selected = eval_select(tbl_data, expr, strict)
    return [name_pos for name_pos in selected if name_pos[0] not in cols_excl]


# Resolve generic ======================================================================


@singledispatch
def resolve(loc: Loc, *args, **kwargs) -> Loc:
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
