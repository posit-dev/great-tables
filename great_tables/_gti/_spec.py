"""The GTI spec: what `<gt-table>` needs to know about a table beyond its static HTML.

The spec is JSON, embedded next to the table, and kept free of Python-only concepts so that other
producers (R gt) can emit it too. Version 1 holds the table's structure and sort ranks:

- `columns`: the body columns, in the order of the body cells (stub columns first)
- `spanners`: the column spanners, with the visible columns under each
- `stub`: the stub columns, and whether row groups are shown as a column of the stub
- `groups`: the row groups, in display order, with their data rows
- `body`: one entry per `<tr>` of the table body, in order: a data row's index (an integer), or an
  object for a group heading, a summary row, or a grand summary row
- `ranks`: per sortable column, each data row's dense sort rank (`null` for a missing value)
- `striping`: whether the stub and body cells of alternate data rows are striped (`gt_striped`),
  so that striping can be redone when rows are reordered or hidden
- `controls`: which controls the reader gets: sort buttons in the column labels, a search box,
  handles for resizing columns, and whether rows can be selected (one at a time, or several); and
  whether the search and page controls are in one bar below the table (`bar`, GTI's), rather than
  a search box above the table and page controls below it (as `pagination.type` says). Producers
  that leave `bar` out get the latter.
- `pagination`: whether rows are split into pages, how many to a page, and the page controls
- `display`: how body rows look: highlighted under the pointer (or when tapped), compact (already
  in the table's CSS, as smaller row padding), and whether cell text wraps
- `layout`: how the table fits its space: the most it can take up before its body scrolls
  vertically (a CSS length; `null` to grow with its content), and what it does when it's wider
  than its container (`"scroll"`: scroll sideways with the stub pinned; `null`: as GT's table does)
- `filters`: the columns readers can filter by, in column order, and how: by the text they show
  (`"text"`), a choice of their values (`"facet"`), or a range of their numbers (`"range"`). A
  facet or range column has its distinct values (`values`), in the order of its `ranks`, so that
  a data row's value is `values[rank]`: as JSON values (numbers, strings, booleans; dates and
  times as ISO 8601 strings), with `null` for values JSON can't hold (NaN). Producers that leave
  `filters` out have none.

Data rows are numbered by their position in the input data, as `ranks` are.
"""

from __future__ import annotations

import datetime as dt
import math
from decimal import Decimal
from typing import TYPE_CHECKING, Any, Literal, TypedDict, Union

from .._tbl_data import (
    ColumnKind,
    _get_column_kind,
    _get_column_ranks,
    _get_column_values,
    n_rows,
)
from .._utils_render_html import _get_header_ids
from ._settings import FilterType, PaginationType, SelectionMode, settings_of

if TYPE_CHECKING:
    from .._gt_data import GTData

SPEC_VERSION = 1

# An "auto" filter on a column of text is a facet when the column has at most this many distinct
# values (and each is in two rows, on average)
FACET_MAX_VALUES = 20


class ColumnSpec(TypedDict):
    id: str | None  # None for the stub column GT adds to hold summary row labels
    role: Literal["stub", "data"]
    kind: ColumnKind
    align: str | None
    header: str | None  # the id of the column's label cell, if it has one


class SpannerSpec(TypedDict):
    id: str
    level: int
    columns: list[str]
    header: str | None


class StubSpec(TypedDict):
    columns: list[str]
    groups_as_column: bool


class GroupSpec(TypedDict):
    id: str | None
    rows: list[int]


class GroupHeadingRow(TypedDict):
    group: str | None


class SummaryRow(TypedDict):
    summary: str
    group: str | None
    side: Literal["top", "bottom"]


class GrandSummaryRow(TypedDict):
    grand_summary: str
    side: Literal["top", "bottom"]


BodyRow = Union[int, GroupHeadingRow, SummaryRow, GrandSummaryRow]


class StripingSpec(TypedDict):
    stub: bool
    body: bool


class ControlsSpec(TypedDict):
    sorting: bool
    search: bool
    resizing: bool
    selection: SelectionMode | None
    bar: bool


class PaginationSpec(TypedDict):
    enabled: bool
    page_size: int
    page_sizes: list[int]
    size_select: bool
    info: bool
    type: PaginationType


class DisplaySpec(TypedDict):
    highlight: bool
    compact: bool
    wrap: bool


class LayoutSpec(TypedDict):
    height: str | None
    responsive: Literal["scroll"] | None


class FilterSpec(TypedDict):
    column: str
    type: Literal["text", "facet", "range"]
    values: list[Any] | None  # a facet or range column's distinct values, by rank


class Spec(TypedDict):
    version: int
    nrows: int
    columns: list[ColumnSpec]
    spanners: list[SpannerSpec]
    stub: StubSpec
    groups: list[GroupSpec]
    body: list[BodyRow]
    ranks: dict[str, list[int | None]]
    striping: StripingSpec
    controls: ControlsSpec
    pagination: PaginationSpec
    display: DisplaySpec
    layout: LayoutSpec
    filters: list[FilterSpec]


def build_spec(data: GTData) -> Spec:
    """Make the spec of a built table (`GT._build_data(context="html")`)."""

    boxhead = data._boxhead
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    stub_layout = data._stub._get_stub_layout(
        has_summary_rows=has_summary_rows, options=data._options, boxhead=boxhead
    )
    header_ids = _get_header_ids(data)
    tbl_data = data._tbl_data

    stub_columns = boxhead._get_stub_columns()
    default_columns = boxhead._get_default_columns()

    # The body cells, as `create_body_component_h()` lays them out
    columns: list[ColumnSpec] = []
    if "rowname" in stub_layout:
        if stub_columns:
            # A hierarchical stub's levels each have a stubhead label, if there are as many
            stubhead = header_ids.stubhead if len(header_ids.stubhead) == len(stub_columns) else []
            for i, info in enumerate(stub_columns):
                columns.append(
                    ColumnSpec(
                        id=info.var,
                        role="stub",
                        kind=_get_column_kind(tbl_data, info.var),
                        align=info.column_align,
                        header=stubhead[i] if stubhead else None,
                    )
                )
        else:
            columns.append(
                ColumnSpec(id=None, role="stub", kind="other", align="left", header=None)
            )

    for info in default_columns:
        columns.append(
            ColumnSpec(
                id=info.var,
                role="data",
                kind=_get_column_kind(tbl_data, info.var),
                align=info.column_align,
                header=header_ids.columns.get(info.var),
            )
        )

    visible = {info.var for info in default_columns}
    spanners: list[SpannerSpec] = []
    for span in data._spanners:
        span_columns = [var for var in span.vars if var in visible]
        if span_columns:
            spanners.append(
                SpannerSpec(
                    id=span.spanner_id,
                    level=span.spanner_level,
                    columns=span_columns,
                    header=header_ids.spanners.get(span.spanner_id),
                )
            )

    ranks: dict[str, list[int | None]] = {}
    for column in columns:
        if column["id"] is not None and column["kind"] != "other":
            column_ranks = _get_column_ranks(tbl_data, column["id"])
            if column_ranks is not None:
                ranks[column["id"]] = column_ranks

    groups_as_column = "group_label" in stub_layout
    # (A `GTI`'s own settings, or those `opt_interactive()` set)
    settings = settings_of(data)
    nrows = n_rows(tbl_data)

    chosen = dict(settings.filters)
    filters: list[FilterSpec] = []
    for column in columns:
        var = column["id"]
        if var is None or var not in chosen:
            continue
        column_ranks = ranks.get(var)
        filter_type = _filter_type(chosen[var], column["kind"], column_ranks, nrows)
        values = None
        if filter_type != "text":
            values = _filter_values(tbl_data, var, column_ranks or [])
        filters.append(FilterSpec(column=var, type=filter_type, values=values))

    return Spec(
        version=SPEC_VERSION,
        nrows=nrows,
        columns=columns,
        spanners=spanners,
        stub=StubSpec(
            columns=[info.var for info in stub_columns], groups_as_column=groups_as_column
        ),
        groups=[
            GroupSpec(id=_group_key(group.group_id), rows=[int(i) for i in group.indices])
            for group in data._stub.group_rows
        ],
        body=_body_rows(data, groups_as_column=groups_as_column),
        ranks=ranks,
        striping=StripingSpec(
            stub=bool(data._options.row_striping_include_stub.value),
            body=bool(data._options.row_striping_include_table_body.value),
        ),
        controls=ControlsSpec(
            sorting=settings.sorting,
            search=settings.search,
            resizing=settings.resizing,
            selection=settings.selection,
            bar=settings.bar,
        ),
        pagination=PaginationSpec(
            enabled=settings.pagination,
            page_size=settings.page_size,
            page_sizes=list(settings.page_sizes),
            size_select=settings.page_size_select,
            info=settings.page_info,
            type=settings.pagination_type,
        ),
        display=DisplaySpec(
            highlight=settings.highlight, compact=settings.compact, wrap=settings.wrap
        ),
        # (Responsive layouts are GTI's own, and "scroll" is the only one so far)
        layout=LayoutSpec(height=settings.height, responsive="scroll"),
        filters=filters,
    )


def _filter_type(
    chosen: FilterType, kind: ColumnKind, ranks: list[int | None] | None, nrows: int
) -> Literal["text", "facet", "range"]:
    """How a column is filtered: as chosen, or (for "auto") as its kind and values suggest."""
    # (Facets and ranges go by the column's ranks, which a column the backend can't sort lacks)
    if ranks is None or chosen == "text":
        return "text"
    if chosen != "auto":
        return chosen
    if kind == "number":
        return "range"
    if kind in ("boolean", "category"):
        return "facet"
    if kind == "string":
        distinct = max((rank for rank in ranks if rank is not None), default=-1) + 1
        if distinct <= FACET_MAX_VALUES and distinct * 2 <= nrows:
            return "facet"
    return "text"


def _filter_values(data: Any, column: str, ranks: list[int | None]) -> list[Any]:
    """A column's distinct values, in the order of their ranks, as JSON values."""
    distinct = max((rank for rank in ranks if rank is not None), default=-1) + 1
    values: list[Any] = [None] * distinct
    seen = [False] * distinct
    for value, rank in zip(_get_column_values(data, column), ranks):
        if rank is not None and not seen[rank]:
            seen[rank] = True
            values[rank] = _json_value(value)
    return values


def _json_value(value: Any) -> Any:
    """A data value as JSON can hold it: NaN and infinities as `None`, dates as ISO 8601 text."""
    # (NumPy's booleans and numbers, as Python's)
    if getattr(getattr(value, "dtype", None), "kind", None) in ("b", "i", "u", "f"):
        value = value.item()
    if value is None or isinstance(value, (bool, int, str)):
        return value
    if isinstance(value, (float, Decimal)):
        number = float(value)
        return number if math.isfinite(number) else None
    if isinstance(value, (dt.date, dt.time)):
        return value.isoformat()
    return str(value)


def _body_rows(data: GTData, groups_as_column: bool) -> list[BodyRow]:
    """What each `<tr>` of the table body is, in the order `create_body_component_h()` makes them."""

    rows: list[BodyRow] = []

    def summary_rows(group: Any, side: Literal["top", "bottom"]) -> list[BodyRow]:
        if not data._summary_rows:
            return []
        found = data._summary_rows.get_summary_rows(group_id=group, side=side)
        return [SummaryRow(summary=row.id, group=_group_key(group), side=side) for row in found]

    def grand_summary_rows(side: Literal["top", "bottom"]) -> list[BodyRow]:
        found = data._summary_rows_grand.get_summary_rows(side=side)
        return [GrandSummaryRow(grand_summary=row.id, side=side) for row in found]

    rows.extend(grand_summary_rows("top"))

    has_groups = len(data._stub.group_ids) > 0
    ordered_index = data._stub.group_indices_map()
    prev_group = None

    for j, (i, group) in enumerate(ordered_index):
        if has_groups and group is not None and group is not prev_group:
            if not groups_as_column:
                rows.append(GroupHeadingRow(group=_group_key(group.group_id)))
            rows.extend(summary_rows(group.group_id, "top"))

        # (indices can be numpy integers, which `json` can't serialize)
        rows.append(int(i))
        prev_group = group

        is_last_in_group = j == len(ordered_index) - 1 or ordered_index[j + 1][1] is not group
        if has_groups and group is not None and is_last_in_group:
            rows.extend(summary_rows(group.group_id, "bottom"))

    rows.extend(grand_summary_rows("bottom"))
    return rows


def _group_key(group_id: Any) -> str | None:
    # Group ids are usually strings, but a `groupname_col` can hold any values
    return None if group_id is None else str(group_id)
