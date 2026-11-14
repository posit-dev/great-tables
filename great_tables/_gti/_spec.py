"""The GTI spec: what `<gt-table>` needs to know about a table beyond its static HTML.

The spec is JSON, embedded next to the table, and kept free of Python-only concepts so that other
producers (R gt) can emit it too. Version 1 holds the table's structure and sort ranks:

- `columns`: the body columns, in the order of the body cells (stub columns first), and whether
  readers can sort by each, search it, and resize it, where `controls` lets them (producers that
  leave these out let them); the side a data column is pinned to (`pin`: `"start"`, the stub's,
  or `"end"`), when the table scrolls sideways (pinned columns are next to their side); and
  whether readers can hide a data column (`hideable`), move it (`reorderable`: among the
  reorderable columns next to it, under the same spanners and pinned to the same side), and group
  the rows by it (`groupable`: a data column with ranks, in a table without row groups or summary
  rows); producers that leave these out let them do none of these. And a data column's priority (`priority`: a positive
  integer, or `null`), for a table that drops columns to fit its container: those without one drop
  first (from the last), then those with the highest (from the last, among equals); those with 1
  (and the stub) never do. Producers that leave it out have none. A column's dtype (`dtype`: a short
  name, as Polars prints it, e.g. `"f64"`), shown under its label, and the data rows whose value is
  missing (`missing`, in order: `null`, or NaN in a column of floats), whose cells are tinted;
  producers that leave these out (or give `null`) show neither.
- `query_columns`: the columns left out of the table but kept for querying, in column order: their
  kind, their label's text, and (for a filter on the text they'd show, a facet, or a bool filter)
  each data row's text. A text filter's is what it's matched against: the text the cell would
  show, then (after a newline) what it wouldn't (an image's `alt` text, an SVG's `<title>`); a
  facet's or a bool filter's is its value's label, the text shown with its whitespace collapsed. They have ranks and filters as other columns
  do, but aren't searched or exported. Producers that leave `query_columns` out have none.
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
  in the table's CSS, as smaller row padding), and whether cell text wraps; whether the column
  labels and cells are in a monospaced font (`monospace`); and whether each data row has its
  number (its place in the data, counted from `row_start`, 0 or 1) before its cells
  (`row_numbers`), and the number of rows and columns is above the table (`dimensions`), after
  what the data is (`data_kind`, such as `"Polars DataFrame"`; `null` to say nothing of it).
  Producers that leave these out have none of them (and rows numbered from 1).
- `layout`: how the table fits its space: the most it can take up before its body scrolls
  vertically (a CSS length; `null` to grow with its content), and what it does when it's wider
  than its container (`"scroll"`: scroll sideways with the stub pinned; `null`: as GT's table
  does; `"collapse"`: drop columns by their `priority` until it fits, each row with a button that
  shows those dropped from it, and scroll if it still doesn't), or narrower than `stack_below` px
  (`"stack"`: its rows become cards; `"auto"`: as `"collapse"` if any column has a priority, else
  its rows become cards if it shows no more than six data columns, and it scrolls otherwise). The
  table's own CSS stacks it (so that it's stacked without the runtime), at the width `stack_below`
  gives, which producers keep the same; producers that leave `stack_below` out have 420. The
  runtime drops columns (without it, a `"collapse"` table scrolls).
- `filters`: the columns readers can filter by, in column order, and how: by the text they show
  (`"text"`), a choice of their values (`"facet"`), a range of their numbers (`"range"`), a
  range of their dates, or dates and times (`"date"`; whether they have times is the column's
  `kind`), or one of their booleans (`"bool"`). A facet, range, date or bool filter column has its
  distinct values (`values`), in the order of its `ranks`, so that a data row's value is
  `values[rank]`: as JSON values (numbers, strings, booleans; dates and times as ISO 8601
  strings), with `null` for values JSON can't hold (NaN). Each filter has the data rows whose
  value is missing (`missing`, in order: `null`, or NaN in a column of floats), which an `is_null`
  clause keeps; without it, the runtime has them as the rows without a rank. Producers that leave
  `filters` out have none.
- `profiles`: the table's columns with a profile under their label, in column order: a plot of
  the values in the rows the search and filters keep, with the share of them missing. A
  `"histogram"` (of a column of numbers, dates, or dates and times) has the column's distinct
  values (`values`), as a facet does, which the runtime bins over the column's range; `"top"`
  (bars for its most common values, by the column's `ranks`) has `null`. Each needs the column's
  ranks. Producers that leave `profiles` out have none.
- `view`: how the table is first shown: filtered by a query (as `<gt-table>`'s `filter` property
  takes, or `null`), sorted by columns (as its `sort` property takes), without the hideable
  columns in `hidden` (in column order; producers that leave it out hide none), and with its rows
  grouped by the groupable column `group_by` (or `null`; producers that leave it out group none). The runtime
  applies it without events. Producers that leave `view` out show the table as it is.
- `export`: how readers can export the rows, from the bar: by copying them (`"clipboard"`) or
  downloading them as CSV (`"csv"`), TSV (`"tsv"`) or JSON (`"json"`), and the name of a
  download, without its extension (`filename`). Producers that leave `export` out (or give no
  `formats`) have no export.
- `view_state`: where the reader's view (filters, sort, search, page, page size, hidden columns,
  column order and grouping) is kept, so that it's there when the page is opened again: in the page's URL
  (`url`), and in the browser's storage (`storage`), by a `key` (the table's ID) that names its
  URL parameters; and whether the reader's changes to it can be undone (`undo`). Producers that
  leave `view_state` out (or keep it in neither) don't keep it, and the changes can't be undone.
- `details`: the data rows with details, in order, which readers can show under them (each row's
  button shows and hides them): each row's are the contents of a `<template
  data-gti-details="row">` in the `<gt-table>` element (the HTML of a table, or of text), which the
  runtime shows apart from the page's styles (in a shadow root). Producers that leave `details`
  out have none.
- `link`: the tables on the page this one is linked to (`group`: those with the same group name),
  and the column (`on`) whose values link their rows: each data row's value (`keys`, as JSON
  values, `null` where it's missing, which links the row to none), so that the rows selected in
  one table filter each of the others to those with the same values. The table's name (`name`: its
  title's text, or its ID; or `null`) and the text of the `on` column's label (`label`) are what
  the others say they're filtered by. Producers that leave `link` out (or give `null`) aren't
  linked.
- `colors`: the columns whose fill colors (`data_color()`'s) are made again from the rows the
  search and filters keep, as they were made from every row: each data row colored (`rows`, those
  with a value, in order) and its value (`values`): a number (or `"Infinity"` or `"-Infinity"`,
  which take the ends of the palette), or, for text (`levels`: its distinct values, in the order
  they first come), the index of its value. The fill is the palette's color (`palette`, the colors
  spread evenly from 0 to 1, mixed in CIELAB) at the value's place in the range of the rows' values
  kept (with a `midpoint` in the middle, the range made even around it, if there is one), or at
  the index of its level among those of the rows kept, with `alpha` (hex) after it; and the text
  is black or white, whichever contrasts with it more (by `text`: `"apca"` or `"wcag"`), unless
  `text` is `null`. The rows in `fixed` keep their colors (a later style colors their cells), but
  count for the range. With every row kept, the cells have their colors as the table's HTML gives
  them. Producers that leave `colors` out have none.
- `remote`: for a table whose rows are kept elsewhere (as a widget's, in Python, with
  `i_scale()`), which the runtime asks for a page at a time (from its `source`): how many rows
  the view (as `view` has it) keeps (`count`), and those in `body` (its first page). Its `ranks`
  have every column, but none of the rows, and its columns' and filters' `missing` only some (a
  column's, those in `body`); a facet or bool filter has its values' `labels`, by rank (the
  runtime would read them from the rows). A range or date filter's `values` may be only some of
  its values, in order: its first and last, and for a column of dates and times, any with a time
  other than midnight, or with seconds, that its fields need (as the runtime has them from its
  values). Producers that leave `remote` out have every row.

Data rows are numbered by their position in the input data, as `ranks` are.
"""

from __future__ import annotations

import datetime as dt
import math
from decimal import Decimal
from typing import TYPE_CHECKING, Any, Literal, Protocol, TypedDict

from .._gt_data import ColInfoTypeEnum
from .._locations import LocBody
from .._styles import CellStyleFill, CellStyleText
from .._tbl_data import (
    ColumnKind,
    PlDataFrame,
    _get_cell,
    _get_column_dtype_name,
    _get_column_kind,
    _get_column_levels,
    _get_column_missing,
    _get_column_ranks,
    _get_column_values,
    cast_frame_to_string,
    get_rows,
    is_na,
    n_rows,
    replace_null_frame,
    to_list,
)
from .._text import _process_text
from .._utils_render_html import _get_header_ids
from ._details import render_details
from ._settings import (
    ExportFormat,
    FilterType,
    PaginationType,
    ProfilePlot,
    SelectionMode,
    Settings,
    settings_of,
)

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
    sortable: bool
    searchable: bool
    resizable: bool
    # The side it's pinned to (in the column order: the stub's, or the other), if it is; the stub
    # always is, at the start
    pin: Literal["start", "end"] | None
    hideable: bool  # whether readers can hide it (a data column)
    reorderable: bool  # whether readers can move it (a data column)
    groupable: bool  # whether readers can group the rows by it (a data column with ranks)
    # (A data column's priority, for a table that drops columns to fit: 1 is never dropped, and
    # higher numbers drop sooner; those without one drop first)
    priority: int | None
    dtype: str | None  # its dtype's short name, shown under its label (`i_inspect()`)
    missing: list[int] | None  # the data rows whose value is missing, tinted (`i_inspect()`)


class QueryColumnSpec(TypedDict):
    id: str
    kind: ColumnKind
    label: str  # the text of its label
    texts: list[str] | None  # each data row's, for a text filter, a facet or a bool filter


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


BodyRow = int | GroupHeadingRow | SummaryRow | GrandSummaryRow


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


# (The kinds of data whose rows are numbered from 1, as a database numbers them (`ROW_NUMBER()`):
# a DataFrame's are numbered from 0, as its index is)
NUMBERED_FROM_1 = ("DuckDB relation", "Ibis table")


def row_start_of(settings: Settings) -> int:
    """The first row's number: as `i_inspect()` set it, or as the data numbers its rows."""
    if settings.row_start is not None:
        return settings.row_start
    return 1 if settings.data_kind in NUMBERED_FROM_1 else 0


class DisplaySpec(TypedDict):
    highlight: bool
    compact: bool
    wrap: bool
    monospace: bool
    row_numbers: bool
    row_start: int
    dimensions: bool
    data_kind: str | None


class LayoutSpec(TypedDict):
    height: str | None
    responsive: Literal["scroll", "stack", "collapse", "auto"] | None
    # (The container width, in px, below which a "stack" or "auto" table is stacked)
    stack_below: int | float


class _FilterSpec(TypedDict):
    column: str
    type: Literal["text", "facet", "range", "date", "bool"]
    # A facet, range, date or bool filter column's distinct values, by rank
    values: list[Any] | None
    # The data rows whose value is missing (for an "is_null" clause)
    missing: list[int]


class FilterSpec(_FilterSpec, total=False):
    # A remote table's facet or bool filter's values' labels, by rank
    labels: list[str]


class ProfileSpec(TypedDict):
    column: str
    plot: Literal["histogram", "top"]
    # A histogram's distinct values, by rank (None for "top")
    values: list[Any] | None


class ViewSortSpec(TypedDict):
    column: str
    descending: bool


class ViewSpec(TypedDict):
    filter: dict[str, list[dict[str, Any]]] | None  # a query (see `_query.py`)
    sort: list[ViewSortSpec]
    hidden: list[str]  # the columns hidden, in column order
    group_by: str | None  # the column the rows are grouped by


CodeBackend = Literal["polars", "pandas", "narwhals"]


class CodeColumnSpec(TypedDict):
    # (What the code goes by: a column of strings, of floats, of categories, of dates, of dates
    # and times, or of another type)
    dtype: Literal["string", "float", "categorical", "date", "datetime", "other"]
    nullable: bool  # a pandas nullable dtype, whose comparisons can be missing
    literals: list[str | None] | None  # a facet's values as Python (`None` where it can't be)


class CodeSpec(TypedDict):
    backend: CodeBackend  # the code's library, first: the data's
    columns: dict[str, CodeColumnSpec]  # each column the view can filter or sort by


class ExportSpec(TypedDict):
    formats: list[ExportFormat]
    filename: str  # without its extension
    code: CodeSpec | None  # what the code for the view needs (with the "code" format)


class ViewStateSpec(TypedDict):
    url: bool
    storage: bool
    key: str | None  # the table's ID (needed for either)
    undo: bool


class LinkSpec(TypedDict):
    group: str
    on: str
    name: str | None  # the table's title (its text), or its ID: what the tables it filters say
    label: str  # the text of the `on` column's label (or its name)
    keys: list[Any]  # each data row's `on` value as JSON (`None` where it's missing)


class ColorSpec(TypedDict):
    column: str
    rows: list[int]  # the data rows colored, with a value
    # (Each row's number (or "Infinity" or "-Infinity"), or for text, the index of its level)
    values: list[Any]
    levels: list[str] | None  # text's distinct values, in the order they first come
    palette: list[str]  # as #RRGGBB
    alpha: str  # as hex (or "")
    midpoint: int | float | None
    text: Literal["apca", "wcag"] | None  # how the text is colored, if it is
    fixed: list[int]  # the rows whose cells a later style colors


class RemoteSpec(TypedDict):
    count: int  # the data rows the view keeps
    rows: list[int]  # those in the table's body (its first page), in order


class _Spec(TypedDict):
    version: int
    nrows: int
    columns: list[ColumnSpec]
    query_columns: list[QueryColumnSpec]
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
    profiles: list[ProfileSpec]
    view: ViewSpec
    export: ExportSpec
    view_state: ViewStateSpec
    details: list[int]
    link: LinkSpec | None
    colors: list[ColorSpec]


class Spec(_Spec, total=False):
    remote: RemoteSpec


class FilterRows(Protocol):
    """What a table's filters need of rows that its data doesn't have (a LazyFrame's, whose
    table's data has none: see `_lazy.py`)."""

    nrows: int

    def distinct(self, column: str) -> int:
        """How many distinct values (not missing) a column has."""
        ...

    def values(self, column: str, type: str) -> list[Any]:
        """A filter's values (of a `type` other than "text"), as `FilterSpec` has them: a
        range's or a date filter's may be only some (see `remote`)."""
        ...

    def missing(self, column: str) -> list[int]:
        """The first data row whose value in a column is missing (none, if there isn't one)."""
        ...


def build_spec(
    data: GTData, details: list[int] | None = None, rows: FilterRows | None = None
) -> Spec:
    """Make the spec of a built table (`GT._build_data(context="html")`): with the data rows
    that have details (as `render_details()` has them, which makes them, if they're not given).

    (With `rows`, the table's rows aren't in its data, which has none: the spec has their count,
    and its filters are theirs, but it's otherwise as for a table without rows.)
    """

    boxhead = data._boxhead
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    stub_layout = data._stub._get_stub_layout(
        has_summary_rows=has_summary_rows, options=data._options, boxhead=boxhead
    )
    header_ids = _get_header_ids(data)
    tbl_data = data._tbl_data
    # (A `GTI`'s own settings, or those `opt_interactive()` set)
    settings = settings_of(data)
    pins = dict(settings.pins)
    priorities = dict(settings.priorities)

    def column_spec(
        id: str | None,
        role: Literal["stub", "data"],
        kind: ColumnKind,
        align: str | None,
        header: str | None,
    ) -> ColumnSpec:
        side = pins.get(id) if role == "data" and id is not None else None
        return ColumnSpec(
            id=id,
            role=role,
            kind=kind,
            align=align,
            header=header,
            sortable=id not in settings.unsortable,
            searchable=id not in settings.unsearchable,
            resizable=id not in settings.unresizable,
            pin=None if side is None else "start" if side == "left" else "end",
            hideable=role == "data" and id in settings.hideable,
            reorderable=role == "data" and id in settings.reorderable,
            # (Set once the ranks are known)
            groupable=False,
            priority=priorities.get(id) if role == "data" and id is not None else None,
            dtype=_get_column_dtype_name(tbl_data, id)
            if settings.dtypes and id is not None
            else None,
            missing=_get_column_missing(tbl_data, id)
            if settings.missing and id is not None
            else None,
        )

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
                    column_spec(
                        id=info.var,
                        role="stub",
                        kind=_get_column_kind(tbl_data, info.var),
                        align=info.column_align,
                        header=stubhead[i] if stubhead else None,
                    )
                )
        else:
            columns.append(
                column_spec(id=None, role="stub", kind="other", align="left", header=None)
            )

    for info in default_columns:
        columns.append(
            column_spec(
                id=info.var,
                role="data",
                kind=_get_column_kind(tbl_data, info.var),
                align=info.column_align,
                header=header_ids.columns.get(info.var),
            )
        )

    _check_pins([column for column in columns if column["role"] == "data"])

    # The columns only for querying (`_leave_out()` in `_render.py` hid them)
    query_infos = [
        info
        for info in boxhead
        if info.type == ColInfoTypeEnum.hidden and info.var in settings.query_only
    ]
    kinds = {info.var: _get_column_kind(tbl_data, info.var) for info in query_infos}

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
    for var, kind in [*((column["id"], column["kind"]) for column in columns), *kinds.items()]:
        if var is not None and kind != "other":
            column_ranks = _get_column_ranks(tbl_data, var)
            if column_ranks is not None:
                ranks[var] = column_ranks

    # (Grouping goes by a column's ranks, and regroups the body's rows, which a table's own row
    # groups and summary rows would have to be kept with)
    for column in columns:
        column["groupable"] = (
            column["role"] == "data"
            and column["id"] in settings.groupable
            and column["id"] in ranks
        )
    if any(column["groupable"] for column in columns) and (
        data._stub.group_ids or has_summary_rows
    ):
        raise ValueError(
            "Readers can't group the rows of a table with row groups or summary rows, so "
            "`i_cols_controls(groupable=True)` can't be set for this one."
        )

    groups_as_column = "group_label" in stub_layout
    data_rows = n_rows(tbl_data)
    nrows = data_rows if rows is None else rows.nrows

    chosen = dict(settings.filters)
    filters: list[FilterSpec] = []
    # (The table's columns, then those only for querying)
    for var, kind in [*((column["id"], column["kind"]) for column in columns), *kinds.items()]:
        if var is None or var not in chosen:
            continue
        column_ranks = ranks.get(var)
        zoned = kind == "datetime" and _has_time_zone(tbl_data, var)
        distinct = None
        if rows is not None and kind == "string" and column_ranks is not None:
            distinct = rows.distinct(var) if chosen[var] == "auto" else None
        filter_type = _filter_type(chosen[var], kind, column_ranks, nrows, zoned, distinct)
        values = None
        if filter_type != "text":
            if rows is None:
                values = _filter_values(tbl_data, var, column_ranks or [])
            else:
                values = rows.values(var, filter_type)
        missing = _get_column_missing(tbl_data, var) if rows is None else rows.missing(var)
        filters.append(FilterSpec(column=var, type=filter_type, values=values, missing=missing))

    plots = dict(settings.profiles)
    profiles: list[ProfileSpec] = []
    # (The table's columns with a label, under which a profile goes, and ranks, which it counts)
    for column in columns:
        var, kind = column["id"], column["kind"]
        if var not in plots or column["header"] is None or var not in ranks:
            continue
        plot = _profile_plot(plots[var], kind)
        if plot is not None:
            values = _filter_values(tbl_data, var, ranks[var]) if plot == "histogram" else None
            profiles.append(ProfileSpec(column=var, plot=plot, values=values))

    # (Imported here, as `_query` imports from this module)
    from ._query import check_view, code_spec, label_text, match_text

    query_columns: list[QueryColumnSpec] = []
    if query_infos:
        types = {f["column"]: f["type"] for f in filters}
        # (The cells' HTML, as the body has it)
        body = replace_null_frame(data._body.body, cast_frame_to_string(tbl_data))
        for info in query_infos:
            texts = None
            if types.get(info.var) in ("text", "facet", "bool"):
                cells = [str(_get_cell(body, row, info.var)) for row in range(data_rows)]
                texts = [
                    match_text(cell) if types[info.var] == "text" else label_text(cell)
                    for cell in cells
                ]
            query_columns.append(
                QueryColumnSpec(
                    id=info.var,
                    kind=kinds[info.var],
                    label=label_text(str(_process_text(info.column_label))) or info.var,
                    texts=texts,
                )
            )

    hideable = [column["id"] for column in columns if column["hideable"] and column["id"]]
    groupable = [column["id"] for column in columns if column["groupable"] and column["id"]]
    all_kinds = {**{c["id"]: c["kind"] for c in columns}, **kinds}
    view = check_view(
        settings.view_filter,
        settings.view_sort,
        filters,
        ranks,
        settings.view_hidden,
        hideable,
        all_kinds,
        settings.view_group_by,
        groupable,
    )
    code = None
    if "code" in settings.export_formats:
        code = code_spec(tbl_data, all_kinds, filters, ranks)
    if details is None:
        details = sorted(render_details(data))
    key = data._options.table_id.value
    if (settings.view_state_url or settings.view_state_storage) and not key:
        raise ValueError(
            "`i_view_state()` keeps the reader's view by the table's ID, and this table has none. "
            'Give it one with `GTI(id=)` (e.g., `GTI(df, id="towny")`) or `with_id()`.'
        )
    link = None
    if settings.link_group is not None and settings.link_on is not None:
        on = settings.link_on
        keys = [_json_value(value) for value in _get_column_values(tbl_data, on)]
        # (A missing value links a row to none, whatever JSON would make of it: pandas' `NaT`)
        for row in _get_column_missing(tbl_data, on):
            keys[row] = None
        title = data._heading.title
        name = label_text(str(_process_text(title))) if title else ""
        info = next((info for info in boxhead if info.var == on), None)
        label = label_text(str(_process_text(info.column_label))) if info is not None else ""
        link = LinkSpec(
            group=settings.link_group,
            on=on,
            name=name or key or None,
            label=label or on,
            keys=keys,
        )

    return Spec(
        version=SPEC_VERSION,
        nrows=nrows,
        columns=columns,
        query_columns=query_columns,
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
            highlight=settings.highlight,
            compact=settings.compact,
            wrap=settings.wrap,
            monospace=settings.monospace,
            row_numbers=settings.row_numbers,
            row_start=row_start_of(settings),
            dimensions=settings.dimensions,
            data_kind=settings.data_kind,
        ),
        layout=LayoutSpec(
            height=settings.height,
            responsive=settings.responsive,
            stack_below=settings.stack_below,
        ),
        filters=filters,
        profiles=profiles,
        view=view,
        export=ExportSpec(
            formats=list(settings.export_formats), filename=settings.export_filename, code=code
        ),
        view_state=ViewStateSpec(
            url=settings.view_state_url,
            storage=settings.view_state_storage,
            key=key,
            undo=settings.view_state_undo,
        ),
        details=details,
        link=link,
        colors=_color_specs(
            data,
            [c["id"] for c in columns if c["role"] == "data" and c["id"] in settings.recolor],
        ),
    )


def _color_specs(data: GTData, recolored: list[str]) -> list[ColorSpec]:
    """How the colors of `data_color()` calls are made again from the rows kept, for the columns
    in `recolored` (shown in the table)."""
    tbl_data = data._tbl_data
    styles = data._styles
    specs: list[ColorSpec] = []
    for info in data._data_colors:
        columns = [column for column in info.columns if column in recolored]
        # (The call's last style, after which a style of the same cell wins; gone if `tab_stub()`
        # made its column the row group column)
        place = next((i for i, style in enumerate(styles) if style is info.last), None)
        if not columns or place is None:
            continue
        later = {
            (style.colname, style.rownum)
            for style in styles[place + 1 :]
            if isinstance(style.locname, LocBody)
            and any(
                isinstance(cell_style, CellStyleFill)
                or (isinstance(cell_style, CellStyleText) and cell_style.color is not None)
                for cell_style in style.styles
            )
        }
        for column in columns:
            # (As `_map_data_colors()` reads them)
            column_vals = to_list(get_rows(tbl_data[column], indexes=info.rows))
            column_vals = [float(x) if isinstance(x, Decimal) else x for x in column_vals]
            present = [(row, x) for row, x in zip(info.rows, column_vals) if not is_na(tbl_data, x)]
            if not present:
                continue
            levels: list[str] | None = None
            if all(isinstance(x, (int, float)) for _, x in present):
                values: list[Any] = [
                    ("Infinity" if x > 0 else "-Infinity")
                    if isinstance(x, float) and math.isinf(x)
                    else _json_value(x)
                    for _, x in present
                ]
            elif all(isinstance(x, str) for _, x in present):
                # (An ordered categorical's levels are its domain, whatever the rows)
                if _get_column_levels(tbl_data, column):
                    continue
                levels = list(dict.fromkeys(x for _, x in present))
                index = {level: i for i, level in enumerate(levels)}
                values = [index[x] for _, x in present]
            else:
                continue
            rows = [row for row, _ in present]
            specs.append(
                ColorSpec(
                    column=column,
                    rows=rows,
                    values=values,
                    levels=levels,
                    palette=info.palette,
                    alpha=info.alpha,
                    midpoint=info.midpoint,
                    text=info.contrast_algo,
                    fixed=[row for row in rows if (column, row) in later],
                )
            )
    return specs


def _check_pins(columns: list[ColumnSpec]) -> None:
    # Pinned columns stay in view by the side they're pinned to, so they have to be next to it,
    # with only pinned columns (on that side) between them and it
    for side, name, move, order in [
        ("start", "left", "cols_move_to_start", columns),
        ("end", "right", "cols_move_to_end", columns[::-1]),
    ]:
        edge = 0
        while edge < len(order) and order[edge]["pin"] == side:
            edge += 1
        stray = next((column for column in order[edge:] if column["pin"] == side), None)
        if stray is not None:
            between = [column["id"] for column in order[edge : order.index(stray)]]
            if side == "end":
                between.reverse()
            raise ValueError(
                f"Column {stray['id']!r} can't be pinned to the {name}, since it isn't next to "
                f"that side of the table: the columns between them "
                f"({', '.join(map(repr, between))}) would have to be pinned too. Pin them with "
                f"`i_cols_pin()` as well, or move the column there with `{move}()`."
            )


def _filter_type(
    chosen: FilterType,
    kind: ColumnKind,
    ranks: list[int | None] | None,
    nrows: int,
    zoned: bool = False,
    distinct: int | None = None,
) -> Literal["text", "facet", "range", "date", "bool"]:
    """How a column is filtered: as chosen, or (for "auto") as its kind and values suggest.

    (A column of dates and times with a time zone, `zoned`, can't have a date filter yet. A
    column of text has `distinct` values, if they aren't counted from its ranks.)
    """
    # (Facets, ranges, date and bool filters go by the column's ranks, which a column the backend
    # can't sort lacks)
    if ranks is None or chosen == "text":
        return "text"
    if chosen != "auto":
        return chosen
    if kind == "number":
        return "range"
    if kind in ("date", "datetime") and not zoned:
        return "date"
    if kind == "boolean":
        return "bool"
    if kind == "category":
        return "facet"
    if kind == "string":
        if distinct is None:
            distinct = max((rank for rank in ranks if rank is not None), default=-1) + 1
        if distinct <= FACET_MAX_VALUES and distinct * 2 <= nrows:
            return "facet"
    return "text"


def _profile_plot(chosen: ProfilePlot, kind: ColumnKind) -> Literal["histogram", "top"] | None:
    """A column's profile plot: as chosen, or (for "auto") as its kind suggests; none for a
    histogram of a column that isn't of numbers or dates (`i_cols_profile()` checks)."""
    histogram = kind in ("number", "date", "datetime")
    if chosen == "auto":
        return "histogram" if histogram else "top"
    return None if chosen == "histogram" and not histogram else chosen


def _has_time_zone(data: Any, column: str) -> bool:
    """Whether a column of dates and times has any with a time zone."""
    if isinstance(data, PlDataFrame):
        # (As its dtype has it: so too without rows)
        return getattr(data.schema[column], "time_zone", None) is not None
    return any(
        getattr(value, "tzinfo", None) is not None for value in _get_column_values(data, column)
    )


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
