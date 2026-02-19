from __future__ import annotations

import copy
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field, replace
from enum import Enum, auto
from itertools import chain, product
from typing import TYPE_CHECKING, Any, Callable, Literal, Protocol, TypeVar, overload

from typing_extensions import Self, TypeAlias, Union

from ._cols_merge import ColMergeInfo, ColMerges  # noqa: F401 (re-exported)
from ._helpers import GoogleFontImports

# TODO: move this class somewhere else (even gt_data could work)
from ._styles import CellStyle
from ._tbl_data import (
    Agnostic,
    DataFrameLike,
    TblData,
    _get_cell,
    _get_column_dtype,
    _set_cell,
    copy_data,
    create_empty_frame,
    get_column_names,
    is_na,
    n_rows,
    to_list,
    validate_frame,
)
from ._tbl_data_align import (
    ALIGNMENT_MAP,
    classify_dtype_for_alignment,
    is_number_like_column,
)
from ._text import BaseText
from ._utils import OrderedSet

if TYPE_CHECKING:
    from ._helpers import UnitStr
    from ._locations import Loc

T = TypeVar("T")


# Frame Data ----
# this is a reduced form of GTData, with just the DataFrame-like object
class PFrameData(Protocol):
    _tbl_data: TblData | Agnostic


class FramelessData:
    _tbl_data: Agnostic = Agnostic()


# GT Data ----


def _prep_gt(
    data, rowname_col: str | None, groupname_col: str | None, auto_align: bool
) -> tuple[Stub, Boxhead]:
    # this function is similar to Stub._set_cols, except it differs in two ways.
    #   * it supports auto-alignment (an expensive operation)
    #   * it assumes its run on data initialization, whereas _set_cols may be run after

    stub = Stub.from_data(data, rowname_col=rowname_col, groupname_col=groupname_col)
    boxhead = Boxhead(
        data, auto_align=auto_align, rowname_col=rowname_col, groupname_col=groupname_col
    )

    return stub, boxhead


@dataclass(frozen=True)
class GTData:
    _tbl_data: TblData
    _body: Body
    _boxhead: Boxhead
    _stub: Stub
    _spanners: Spanners
    _heading: Heading
    _stubhead: Stubhead
    _summary_rows: SummaryRows
    _summary_rows_grand: SummaryRows
    _source_notes: SourceNotes
    _footnotes: Footnotes
    _styles: Styles
    _locale: Locale | None
    _formats: Formats
    _substitutions: Formats
    _col_merge: ColMerges
    _options: Options
    _google_font_imports: GoogleFontImports = field(default_factory=GoogleFontImports)
    _has_built: bool = False

    def _replace(self, **kwargs: Any) -> Self:
        new_obj = copy.copy(self)

        missing = {k for k in kwargs if k not in new_obj.__dict__}
        if missing:
            raise ValueError(f"Replacements not in data: {missing}")

        new_obj.__dict__.update(kwargs)

        return new_obj

    @classmethod
    def from_data(
        cls,
        data: TblData,
        rowname_col: str | None = None,
        groupname_col: str | None = None,
        auto_align: bool = True,
        id: str | None = None,
        locale: str | None = None,
    ):
        data = validate_frame(data)
        stub, boxhead = _prep_gt(data, rowname_col, groupname_col, auto_align)

        if id is not None:
            options = Options(table_id=OptionsInfo(True, "table", "value", id))
        else:
            options = Options()

        return cls(
            _tbl_data=data,
            _body=Body.from_empty(data),
            _boxhead=boxhead,  # uses get_tbl_data()
            _stub=stub,  # uses get_tbl_data
            _spanners=Spanners([]),
            _heading=Heading(),
            _stubhead=None,
            _summary_rows=SummaryRows(),
            _summary_rows_grand=SummaryRows(_is_grand_summary=True),
            _source_notes=[],
            _footnotes=[],
            _styles=[],
            _locale=Locale(locale),
            _formats=[],
            _substitutions=[],
            _col_merge=[],
            _options=options,
            _google_font_imports=GoogleFontImports(),
        )


class _Sequence(Sequence[T]):
    _d: list[T]

    def __init__(self, data: list[T]):
        self._d = data

    @overload
    def __getitem__(self, ii: int) -> T: ...

    @overload
    def __getitem__(self, ii: slice) -> Self: ...

    @overload
    def __getitem__(self, ii: list[int]) -> Self: ...

    def __getitem__(self, ii: int | slice | list[int]) -> T | Self:
        if isinstance(ii, slice):
            return self.__class__(self._d[ii])
        elif isinstance(ii, list):
            return self.__class__([self._d[el] for el in ii])

        return self._d[ii]

    def __len__(self) -> int:
        return len(self._d)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._d.__repr__()})"

    def __eq__(self, other: Any) -> bool:
        return (type(self) is type(other)) and (self._d == other._d)


# Body ----


# TODO: it seems like this could just be a DataFrameLike object?
# Similar to TblData now being a DataFrame, rather than its own class
# I've left for now, and have just implemented concretes for it in
# _tbl_data.py
class Body:
    body: TblData

    def __init__(self, body: TblData):
        self.body = body

    def render_formats(self, data_tbl: TblData, formats: list[FormatInfo], context: Any):
        for fmt in formats:
            eval_func = getattr(fmt.func, context, fmt.func.default)
            if eval_func is None:
                raise Exception("Internal Error")
            for col, row in fmt.cells.resolve():
                result = eval_func(_get_cell(data_tbl, row, col))
                if isinstance(result, FormatterSkipElement):
                    continue

                # TODO: I think that this is very inefficient with polars, so
                # we could either accumulate results and set them per column, or
                # could always use a pandas DataFrame inside Body?
                new_body = _set_cell(self.body, row, col, result)
                if new_body is not None:
                    # Some backends do not support inplace operations, but return a new dataframe
                    # TODO: Consolidate the behaviour of _set_cell
                    self.body = new_body

        return self

    def copy(self) -> Self:
        return self.__class__(copy_data(self.body))

    @classmethod
    def from_empty(cls, body: DataFrameLike):
        empty_df = create_empty_frame(body)

        return cls(empty_df)


# Boxhead ----
ColumnAlignment: TypeAlias = Literal["left", "center", "right", "justify"]


class ColInfoTypeEnum(Enum):
    default = auto()
    stub = auto()
    row_group = auto()
    hidden = auto()

    # A placeholder column created when there is no table data in the stub,
    # but summary rows need to create one for their labels.  e.g. "mean" to indicate
    # the row is mean summaries
    summary_placeholder = auto()


@dataclass(frozen=True)
class ColInfo:
    # TODO: Make var readonly
    var: str
    type: ColInfoTypeEnum = ColInfoTypeEnum.default
    column_label: str | BaseText | None = None
    column_align: ColumnAlignment | None = None
    column_width: str | None = None

    # The components of the boxhead are:
    # `var` (obtained from column names)
    # `column_label` (obtained from column names)
    # `column_align` = None
    # `column_width` = None

    def __post_init__(self):
        if self.column_label is None:
            super().__setattr__("column_label", self.var)

    def replace_column_label(self, column_label: str) -> Self:
        return replace(self, column_label=column_label)

    @property
    def visible(self) -> bool:
        return self.type != ColInfoTypeEnum.hidden

    @property
    def is_stub(self) -> bool:
        return self.type in (
            ColInfoTypeEnum.stub,
            ColInfoTypeEnum.row_group,
            ColInfoTypeEnum.summary_placeholder,
        )

    @property
    def defaulted_align(self) -> str:
        return "center" if self.column_align is None else str(self.column_align)


class Boxhead(_Sequence[ColInfo]):
    """Map columns of the input table to their final rendered placement in the boxhead.

    The boxhead is the part of the table that contains the column labels and the stub head. This
    class is responsible for the following:

    - rendered boxhead: column order, labels, alignment, and visibility
    - rendered body: alignment of data values for each column
    - rendered stub: this class records which input column is used for the stub
    """

    _d: list[ColInfo]

    def __new__(
        cls,
        data: TblData | list[ColInfo],
        auto_align: bool = True,
        rowname_col: str | None = None,
        groupname_col: str | None = None,
    ) -> Self:
        obj = super().__new__(cls)

        if isinstance(data, list):
            obj._d = data
        else:
            # Obtain the column names from the data and initialize the
            # `_boxhead` from that
            column_names = get_column_names(data)
            obj._d = [ColInfo(col) for col in column_names]
            obj = obj.set_stub_cols(rowname_col, groupname_col)

        if not isinstance(data, list) and auto_align:
            return obj.align_from_data(data=data)

        return obj

    def __init__(
        self,
        data: TblData | list[ColInfo],
        auto_align: bool = True,
        rowname_col: str | None = None,
        groupname_col: str | None = None,
    ):
        pass

    def __getnewargs__(self):
        return (self._d,)

    def set_stub_cols(self, rowname_col: str | None, groupname_col: str | None) -> Self:
        # Note that None unsets a column
        # TODO: validate that rowname_col is in the boxhead
        if rowname_col is not None and rowname_col == groupname_col:
            raise ValueError(
                "rowname_col and groupname_col may not be set to the same column. "
                f"Received column name: `{rowname_col}`."
            )

        new_cols = []
        stub_or_row_group = (ColInfoTypeEnum.stub, ColInfoTypeEnum.row_group)
        for col in self:
            # either set the col to be the new stub or row_group ----
            # note that this assumes col.var is always a string, so never equals None
            if col.var == rowname_col:
                new_col = replace(col, type=ColInfoTypeEnum.stub)
            elif col.var == groupname_col:
                new_col = replace(col, type=ColInfoTypeEnum.row_group)
            # otherwise, unset the existing stub or row_group ----
            elif col.type in stub_or_row_group:
                new_col = replace(col, type=ColInfoTypeEnum.default)
            else:
                new_col = replace(col)

            new_cols.append(new_col)

        return self.__class__(new_cols)

    def _set_cols_info_type(self, colnames: list[str], colinfo_type: ColInfoTypeEnum) -> Self:
        # TODO: validate that colname is in the boxhead
        res: list[ColInfo] = [
            replace(col, type=colinfo_type) if col.var in colnames else col for col in self._d
        ]
        return self.__class__(res)

    def set_cols_hidden(self, colnames: list[str]) -> Self:
        return self._set_cols_info_type(colnames=colnames, colinfo_type=ColInfoTypeEnum.hidden)

    def set_cols_unhidden(self, colnames: list[str]) -> Self:
        return self._set_cols_info_type(colnames=colnames, colinfo_type=ColInfoTypeEnum.default)

    def align_from_data(self, data: TblData) -> Self:
        """Updates align attribute in entries based on data types."""

        # Validate that data columns and ColInfo list correspond
        if len(get_column_names(data)) != len(self._d):
            raise ValueError("Number of data columns must match length of Boxhead")

        if any(
            col_info.var != col_name for col_info, col_name in zip(self._d, get_column_names(data))
        ):
            raise ValueError("Column names must match between data and Boxhead")

        # Classify each column and map to alignment
        align: list[str] = []
        for col in get_column_names(data):
            classification = classify_dtype_for_alignment(data, col)

            # Special case: string columns with number-like content -> right-align
            # This handles both "object" (pandas 2.x) and "str" (pandas 3.x) dtypes
            if classification == "string":
                dtype = str(_get_column_dtype(data, col)).lower()
                if dtype in ("object", "str") and is_number_like_column(data, col):
                    classification = "numeric"

            align.append(ALIGNMENT_MAP[classification])

        # Set the alignment for each column in the boxhead
        new_cols: list[ColInfo] = [
            replace(col_info, column_align=alignment) for col_info, alignment in zip(self._d, align)
        ]

        return self.__class__(new_cols)

    def vars_from_type(self, type: ColInfoTypeEnum) -> list[str]:
        return [x.var for x in self._d if x.type == type]

    def reorder(self, vars: list[str]) -> Self:
        boxh_vars = [col.var for col in self]
        if set(vars) != set(boxh_vars):
            raise ValueError("Reordering vars must contain all boxhead vars.")

        new_order = [boxh_vars.index(var) for var in vars]

        return self[new_order]

    def final_columns(self, options: Options) -> list[ColInfo]:
        row_group_info = self._get_row_group_column()
        row_group_column = (
            [row_group_info] if row_group_info and options.row_group_as_column.value else []
        )

        stub_info = self._get_stub_column()
        stub_column = [stub_info] if stub_info else []

        default_columns = self._get_default_columns()

        return [*row_group_column, *stub_column, *default_columns]

    # Get a list of columns
    def _get_columns(self) -> list[str]:
        return [x.var for x in self._d]

    # Get a list of column labels
    def _get_column_labels(self) -> list[str | BaseText | None]:
        return [x.column_label for x in self._d]

    # Set column label
    def _set_column_labels(self, col_labels: dict[str, str | BaseText]) -> Self:
        out_cols: list[ColInfo] = [
            replace(x, column_label=col_labels[x.var]) if x.var in col_labels else x
            for x in self._d
        ]

        return self.__class__(out_cols)

    # Set column alignments
    def _set_column_aligns(self, columns: list[str], align: str) -> Self:
        set_cols = set(columns)
        out_cols: list[ColInfo] = [
            replace(x, column_align=align) if x.var in set_cols else x for x in self._d
        ]

        return self.__class__(out_cols)

    # Get a list of all column widths
    def _get_column_widths(self) -> list[str | None]:
        return [x.column_width for x in self._d]

    # Get a list of visible columns
    def _get_default_columns(self) -> list[ColInfo]:
        default_columns = [x for x in self._d if x.type == ColInfoTypeEnum.default]
        return default_columns

    def _get_stub_column(self) -> ColInfo | None:
        stub_column = [x for x in self._d if x.type == ColInfoTypeEnum.stub]
        return None if not stub_column else stub_column[0]

    def _get_row_group_column(self) -> ColInfo | None:
        column = [x for x in self._d if x.type == ColInfoTypeEnum.row_group]
        return None if not column else column[0]

    # Get a list of visible column labels
    def _get_default_column_labels(self) -> list[Union[str, BaseText, None]]:
        default_column_labels = [
            x.column_label for x in self._d if x.type == ColInfoTypeEnum.default
        ]
        return default_column_labels

    def _get_default_alignments(self) -> list[str]:
        # Extract alignment strings to only include 'default'-type columns
        alignments = [str(x.column_align) for x in self._d if x.type == ColInfoTypeEnum.default]
        return alignments

    # Get the alignment for a specific var value
    def _get_boxhead_get_alignment_by_var(self, var: str) -> str:
        # Get the column alignments and also the alignment class names
        boxh = self._d

        # Filter boxh to only include visible columns
        alignment = [x.column_align for x in boxh if x.visible if x.var == var]

        # Check for length of alignment and raise error if not 1
        if len(alignment) != 1:
            raise ValueError("Alignment must be length 1.")

        # Convert the single alignment value in the list to a string
        return str(alignment[0])

    # Get the number of columns for the visible (not hidden) data; this
    # excludes the number of columns required for the table stub
    def _get_number_of_visible_data_columns(self) -> int:
        return len(self._get_default_columns())

    # Obtain the number of visible columns in the built table; this should
    # account for the size of the stub in the final, built table
    def _get_effective_number_of_columns(
        self, stub: Stub, has_summary_rows: bool, options: Options
    ) -> int:
        n_data_cols = self._get_number_of_visible_data_columns()

        stub_layout = stub._get_stub_layout(has_summary_rows=has_summary_rows, options=options)
        # Once the stub is defined in the package, we need to account
        # for the width of the stub at build time to fully obtain the number
        # of visible columns in the built table
        n_data_cols = n_data_cols + len(stub_layout)

        return n_data_cols

    def _set_column_width(self, colname: str, width: str) -> Self:
        colnames = [x.var for x in self._d]

        if colname not in colnames:
            raise ValueError(f"Column name {colname} not found in table.")

        out_cols = [
            replace(x, column_width=width) if xvar == colname else x
            for x, xvar in zip(self._d, colnames)
        ]

        return self.__class__(out_cols)


# Stub ----


@dataclass(frozen=True)
class RowInfo:
    # TODO: Make `rownum_i` readonly
    rownum_i: int
    group_id: str | None = None
    rowname: str | None = None
    group_label: str | None = None
    built: bool = False

    # The components of the stub are:
    # `rownum_i` (The initial row indices for the table at ingest time)
    # `group_id` = None
    # `rowname` = None
    # `group_label` = None
    # `built` = False


class Stub:
    """Container for row information and labels, along with grouping information.

    This class handles the following:

      * Creating row and grouping information from data.
      * Determining row order for final presentation.

    Note that the order of entries in .group_rows determines final rendering order.
    When .group_rows is empty, the original data order is used.
    """

    # TODO: the rows get reordered at various points, but are never used in rendering?
    # the html rendering uses group_rows to index into the underlying DataFrame

    _d: list[RowInfo]
    rows: list[RowInfo]
    group_rows: GroupRows

    def __init__(self, rows: list[RowInfo], group_rows: GroupRows):
        self.rows = self._d = rows.copy()
        self.group_rows = group_rows

    @classmethod
    def from_data(
        cls, data, rowname_col: str | None = None, groupname_col: str | None = None
    ) -> Self:
        # Obtain a list of row indices from the data and initialize
        # the `_stub` from that
        row_indices = list(range(n_rows(data)))

        if groupname_col is not None:
            group_id = to_list(data[groupname_col])
        else:
            group_id = [None] * n_rows(data)

        if rowname_col is not None:
            row_names = to_list(data[rowname_col])
        else:
            row_names = [None] * n_rows(data)

        # Obtain the column names from the data and initialize the
        # `_stub` from that
        row_info = [RowInfo(*i) for i in zip(row_indices, group_id, row_names)]

        # create groups, and ensure they're ordered by first observed
        group_names = OrderedSet(
            row.group_id for row in row_info if row.group_id is not None
        ).as_list()
        group_rows = GroupRows(data, group_key=groupname_col).reorder(group_names)

        return cls(row_info, group_rows)

    def _set_cols(
        self, data: TblData, boxhead: Boxhead, rowname_col: str | None, groupname_col: str | None
    ) -> tuple[Stub, Boxhead]:
        """Return a new Stub and Boxhead, with updated rowname and groupname columns.

        Note that None unsets a column.
        """

        new_boxhead = boxhead.set_stub_cols(rowname_col, groupname_col)
        new_stub = self.from_data(data, rowname_col, groupname_col)

        return new_stub, new_boxhead

    @property
    def group_ids(self) -> RowGroups:
        return [group.group_id for group in self.group_rows]

    def reorder_rows(self, indices) -> Self:
        new_rows = [self.rows[ii] for ii in indices]

        return self.__class__(new_rows, self.group_rows)

    def order_groups(self, group_order: RowGroups) -> Self:
        # TODO: validate
        return self.__class__(self.rows, self.group_rows.reorder(group_order))

    def update_group_row_labels(self, body: Body, tbl_data: TblData, boxhead: Boxhead) -> Self:
        """Update group row labels using formatted values from the rendered body.

        For each group, the formatted cell value for the first row of the group is
        looked up in `body`. If the cell was not formatted (i.e., it is still NA),
        the original value from `tbl_data` is used instead.

        If no row-group column exists in `boxhead`, the stub is returned unchanged.

        Parameters
        ----------
        body
            The rendered body whose cells may contain formatted values.
        tbl_data
            The original (unformatted) source data.
        boxhead
            The boxhead containing column metadata, used to identify the row-group column.

        Returns
        -------
        Stub
            A new Stub with group labels replaced by formatted values, or the
            original Stub if no row-group column exists.
        """
        rowgroup_var = boxhead._get_row_group_column()
        if rowgroup_var is None:
            return self

        new_group_rows: list[Any] = []

        for group_row in self.group_rows:
            first_index = group_row.indices[0]
            cell_content = _get_cell(body.body, first_index, rowgroup_var.var)

            # When no formatter was applied, the cell is still NA — fall back to
            # the original data value.
            if is_na(tbl_data, cell_content):
                cell_content = _get_cell(tbl_data, first_index, rowgroup_var.var)

            new_group_rows.append(group_row.with_group_label(cell_content))

        return self.__class__(self.rows, GroupRows(new_group_rows))

    def group_indices_map(self) -> list[tuple[int, GroupRowInfo | None]]:
        return self.group_rows.indices_map(len(self.rows))

    def __iter__(self):
        return iter(self.rows)

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, ii: int):
        return self.rows[ii]

    def _get_stub_components(self) -> list[str]:
        stub_components: list[str] = []

        if any(entry.group_id is not None for entry in self.rows):
            stub_components.append("group_id")

        if any(entry.rowname is not None for entry in self.rows):
            stub_components.append("row_id")

        return stub_components

    # Determine whether the table should have row group labels set within a column in the stub
    def _stub_group_names_has_column(self, options: Options) -> bool:
        # If there aren't any row groups then the result is always False
        if len(self.group_ids) < 1:
            return False

        # Given that there are row groups, we need to look at the option `row_group_as_column` to
        # determine whether they populate a column located in the stub; if set as True then that's
        # the return value
        row_group_as_column: Any = options.row_group_as_column.value
        if not isinstance(row_group_as_column, bool):
            raise TypeError(
                "Variable type mismatch. Expected bool, got something entirely different."
            )

        return row_group_as_column

    def _get_stub_layout(self, has_summary_rows: bool, options: Options) -> list[str]:
        # Determine which stub components are potentially present as columns
        stub_rownames_is_column = "row_id" in self._get_stub_components()
        stub_groupnames_is_column = self._stub_group_names_has_column(options=options)

        # Get the potential total number of columns in the table stub
        n_stub_cols = stub_rownames_is_column + stub_groupnames_is_column

        # Resolve the layout of the stub (i.e., the roles of columns if present)
        if n_stub_cols == 0:
            # If summary rows are present, we will use the `rowname` column
            # for the summary row labels
            if has_summary_rows:
                stub_layout = ["rowname"]
            else:
                stub_layout = []

        else:
            stub_layout = [
                label
                for label, condition in (
                    ("group_label", stub_groupnames_is_column),
                    ("rowname", stub_rownames_is_column),
                )
                if condition
            ]

        return stub_layout


# Row groups ----
RowGroups: TypeAlias = list[str]

# Group rows ----


@dataclass(frozen=True)
class GroupRowInfo:
    group_id: str
    group_label: str | None = None
    indices: list[int] = field(default_factory=list)
    # row_start: int | None = None
    # row_end: int | None = None
    # has_summary_rows: bool = False  # TODO: remove
    summary_row_side: str | None = None

    def defaulted_label(self) -> str:
        """Return a group label that has been defaulted."""
        label = self.group_label if self.group_label is not None else self.group_id
        return label

    def with_group_label(self, label: str | None) -> Self:
        """Return a copy of the object with the specified group label."""
        return replace(self, group_label=label)


class MISSING_GROUP:
    """Represent a category of all missing group levels in data."""


class GroupRows(_Sequence[GroupRowInfo]):
    _d: list[GroupRowInfo]

    def __init__(self, data: list[GroupRowInfo] | DataFrameLike, group_key: str | None = None):
        if isinstance(data, list):
            self._d = data

        elif group_key is None:
            self._d = []

        # otherwise, instantiate from a table of data
        else:
            from ._tbl_data import group_splits

            self._d = [
                GroupRowInfo(group_id, indices=ind)
                for group_id, ind in group_splits(data, group_key=group_key).items()
            ]

    def reorder(self, group_ids: list[str | MISSING_GROUP]) -> Self:
        # TODO: validate all group_ids are in data
        non_missing = (g for g in group_ids if not isinstance(g, MISSING_GROUP))
        crnt_order = {grp.group_id: ii for ii, grp in enumerate(self)}

        set_gids = set(group_ids)
        missing_groups = (grp.group_id for grp in self if grp.group_id not in set_gids)
        reordered = [self[crnt_order[g]] for g in chain(non_missing, missing_groups)]

        return self.__class__(reordered)

    def indices_map(self, n: int) -> list[tuple[int, GroupRowInfo | None]]:
        """Return pairs of row index, group label for all rows in data.

        Note that when no groupings exist, n is used to return from range(n).
        In this case, None is used to indicate there is no grouping. This is
        distinct from MISSING_GROUP (which may currently be unused?).

        """
        return (
            [(ii, None) for ii in range(n)]
            if not self._d
            else [(ind, info) for info in self for ind in info.indices]
        )


# Spanners ----


@dataclass(frozen=True)
class SpannerInfo:
    spanner_id: str
    spanner_level: int
    spanner_label: str | BaseText | UnitStr | None = None
    spanner_units: str | None = None
    spanner_pattern: str | None = None
    vars: list[str] = field(default_factory=list)
    built: str | None = None

    def built_label(self) -> str | BaseText | UnitStr:
        """Return a list of spanner labels that have been built."""
        label = self.built if self.built is not None else self.spanner_label
        if label is None:
            raise ValueError("Spanner label must be a string and not None.")
        return label

    def drop_var(self, name: str) -> Self:
        new_vars = [entry for entry in self.vars if entry != name]

        if len(new_vars) == len(self.vars):
            return self

        return replace(self, vars=new_vars)


class Spanners(_Sequence[SpannerInfo]):
    _d: list[SpannerInfo]

    @classmethod
    def from_ids(cls, ids: list[str]):
        """Construct an object from a list of spanner_ids"""

        return cls([SpannerInfo(id, ii) for ii, id in enumerate(ids)])

    def relevel(self, levels: list[int]) -> Self:
        if len(levels) != len(self):
            raise ValueError(
                "New levels must be same length as spanners."
                f" Received {len(levels)}, but have {len(self)} spanners."
            )

        new_spans = [replace(span, spanner_level=lvl) for span, lvl in zip(self, levels)]
        return self.__class__(new_spans)

    def next_level(self, column_names: list[str]) -> int:
        """Return the next available spanner level.

        Spanners whose columns do not overlap are put on the same level.
        """

        if not len(self):
            return 0

        overlapping_levels = [
            span.spanner_level for span in self if any(v in column_names for v in span.vars)
        ]

        return max(overlapping_levels, default=-1) + 1

    def append_entry(self, span: SpannerInfo) -> Self:
        return self.__class__(self._d + [span])

    def remove_column(self, column: str) -> Self:
        return self.__class__([span.drop_var(column) for span in self])


# Heading ---


@dataclass(frozen=True)
class Heading:
    title: str | BaseText | None = None
    subtitle: str | BaseText | None = None
    preheader: str | list[str] | None = None


# Stubhead ----
Stubhead: TypeAlias = "str | None"


# Sourcenotes ----
SourceNotes = list[str]

# Footnotes ----


class FootnotePlacement(Enum):
    left = auto()
    right = auto()
    auto = auto()


@dataclass(frozen=True)
class FootnoteInfo:
    locname: Loc | None = None
    grpname: str | None = None
    colname: str | None = None
    locnum: int | None = None
    rownum: int | None = None
    colnum: int | None = None
    footnotes: list[str] | None = None
    placement: FootnotePlacement | None = None


Footnotes: TypeAlias = list[FootnoteInfo]

# Styles ----


@dataclass(frozen=True)
class StyleInfo:
    locname: Loc
    grpname: str | None = None
    colname: str | None = None
    rownum: int | None = None
    colnum: int | None = None
    styles: list[CellStyle] = field(default_factory=list)


Styles: TypeAlias = list[StyleInfo]

# Locale ----


class Locale:
    locale: str | None

    def __init__(self, locale: str | None):
        self._locale: str | None = locale


# Formats ----


class FormatterSkipElement:
    """Represent that nothing should be saved for a formatted value."""


FormatFn = Callable[[Any], "str | FormatterSkipElement"]


class FormatFns:
    html: FormatFn | None
    latex: FormatFn | None
    rtf: FormatFn | None
    default: FormatFn | None

    def __init__(self, **kwargs: FormatFn):
        for format in ("html", "latex", "rtf", "default"):
            if fmt := kwargs.get(format):
                setattr(self, format, fmt)


class CellSubset:
    def resolve(self) -> list[tuple[str, int]]:
        raise NotImplementedError("Not implemented")


class CellRectangle(CellSubset):
    cols: list[str]
    rows: list[int]

    def __init__(self, cols: list[str], rows: list[int]):
        self.cols = cols
        self.rows = rows

    def resolve(self) -> list[tuple[str, int]]:
        return list(product(self.cols, self.rows))


class FormatInfo:
    """Contains functions for formatting in different contexts, and columns and rows to apply to.

    Note that format functions apply to individual values.
    """

    func: FormatFns
    cells: CellSubset

    def __init__(self, func: FormatFns, cols: list[str], rows: list[int]):
        self.func = func
        self.cells = CellRectangle(cols, rows)


# TODO: this will contain private methods for formatting cell values to strings
# class Formats:
#     def __init__(self):
#         pass
Formats = list


# Column Merge ----
# ColMergeInfo and ColMerges are defined in _cols_merge.py but re-exported here

# Summary Rows ---

# This can't conflict with actual group ids since we have a
# separate data structure for grand summary row infos


@dataclass(frozen=True)
class SummaryRowInfo:
    """Information about a single summary row"""

    id: str
    label: str  # For now, label and id are identical
    # The motivation for values as a dict is to ensure cols_* functions don't have to consider
    # the implications on existing SummaryRowInfo objects
    values: dict[str, Any]  # TODO: consider datatype, series?
    side: Literal["top", "bottom"]  # TODO: consider enum


# TODO: refactor into a collection/dataclass wrapping the list part
#       put most of the methods for filtering, adding, replacing there.
#       Make immutable to avoid potential bugs.
class SummaryRows(Mapping[str, list[SummaryRowInfo]]):
    """A sequence of summary rows

    The following structures should always be true about summary rows:
        - The id is also the label (often the same as the function name)
        - There is at most 1 row for each group and id pairing
        - If a summary row is added and no row exists for that group and id, add it
        - If a summary row is added and a row exists for that group and id pairing,
            then replace all cells (in values) that are numeric in the new version
    """

    _d: dict[str, list[SummaryRowInfo]]
    _is_grand_summary: bool

    LIST_CLS = list
    GRAND_SUMMARY_KEY = "grand"

    def __init__(
        self,
        entries: dict[str, list[SummaryRowInfo]] | None = None,
        _is_grand_summary: bool = False,
    ):
        if entries is None:
            self._d = {}
        else:
            self._d = entries
        self._is_grand_summary = _is_grand_summary

    def __bool__(self) -> bool:
        """Return True if there are any summary rows, False otherwise."""
        return len(self._d) > 0

    def __getitem__(self, key: str | None) -> list[SummaryRowInfo]:
        if self._is_grand_summary:
            key = SummaryRows.GRAND_SUMMARY_KEY

        if not key:
            raise KeyError("Summary row group key must not be None for group summary rows.")

        if key not in self._d:
            raise KeyError(f"Group '{key}' not found in summary rows.")

        return self.LIST_CLS(self._d[key])

    def define(self, **kwargs: list[SummaryRowInfo]) -> Self:
        """Define multiple summary row groups at once, replacing any existing groups."""

        new_d = dict(self._d)
        for group_id, summary_rows in kwargs.items():
            new_d[group_id] = summary_rows

        return self.__class__(new_d, _is_grand_summary=self._is_grand_summary)

    def add_summary_row(self, summary_row: SummaryRowInfo, group_id: str | None = None) -> Self:
        """Add a summary row following the merging rules in the class docstring."""

        # TODO: group_id can be None for grand summary configuration, but can't be none
        # for regular summary configuration (a bit double barrelled).
        if self._is_grand_summary and group_id is None:
            group_id = SummaryRows.GRAND_SUMMARY_KEY
        elif group_id is None:
            raise TypeError("group_id must be provided for group summary rows.")

        existing_group = self.get(group_id)

        if not existing_group:
            return self.define(**{group_id: [summary_row]})

        else:
            existing_index = next(
                (ii for ii, crnt_row in enumerate(existing_group) if crnt_row.id == summary_row.id),
                None,
            )

            new_rows = self.LIST_CLS(existing_group)

            if existing_index is None:
                # No existing row for this group and id, add it
                new_rows.append(summary_row)
            else:
                # Replace existing row, but merge numeric values from new version
                existing_row = new_rows[existing_index]

                # Start with existing values
                merged_values = existing_row.values.copy()

                # Replace with numeric values from new row
                for key, new_value in summary_row.values.items():
                    merged_values[key] = new_value

                # Create merged row with new row's properties but merged values
                merged_row = SummaryRowInfo(
                    id=summary_row.id,
                    label=summary_row.label,
                    values=merged_values,
                    # Setting this to existing row instead of summary_row means original
                    # side is fixed by whatever side is first assigned to this row
                    side=existing_row.side,
                )

                new_rows[existing_index] = merged_row

        return self.define(**{group_id: new_rows})

    def get_summary_rows(
        self, group_id: str | None = None, side: str | None = None
    ) -> list[SummaryRowInfo]:
        """Get list of summary rows for that group. If side is None, do not filter by side.
        Sorts result with 'top' side first, then 'bottom'."""

        result: list[SummaryRowInfo] = []

        if self._is_grand_summary:
            group_id = SummaryRows.GRAND_SUMMARY_KEY
        elif group_id is None:
            raise TypeError("group_id must be provided for group summary rows.")

        summary_row_group = self.get(group_id)

        if summary_row_group:
            for summary_row in summary_row_group:
                if side is None or summary_row.side == side:
                    result.append(summary_row)

        # Sort: 'top' first, then 'bottom'
        result.sort(key=lambda r: 0 if r.side == "top" else 1)  # TODO: modify if enum for side
        return result

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError


# Options ----

default_fonts_list = [
    "-apple-system",
    "BlinkMacSystemFont",
    "Segoe UI",
    "Roboto",
    "Oxygen",
    "Ubuntu",
    "Cantarell",
    "Helvetica Neue",
    "Fira Sans",
    "Droid Sans",
    "Arial",
    "sans-serif",
]


@dataclass(frozen=True)
class OptionsInfo:
    scss: bool
    category: str
    type: str
    value: Any


@dataclass(frozen=True)
class Options:
    table_id: OptionsInfo = OptionsInfo(False, "table", "value", None)
    table_caption: OptionsInfo = OptionsInfo(False, "table", "value", None)
    table_width: OptionsInfo = OptionsInfo(True, "table", "px", "auto")
    table_layout: OptionsInfo = OptionsInfo(True, "table", "value", "fixed")
    table_margin_left: OptionsInfo = OptionsInfo(True, "table", "px", "auto")
    table_margin_right: OptionsInfo = OptionsInfo(True, "table", "px", "auto")
    table_background_color: OptionsInfo = OptionsInfo(True, "table", "value", "#FFFFFF")
    table_additional_css: OptionsInfo = OptionsInfo(False, "table", "values", [])
    table_font_names: OptionsInfo = OptionsInfo(False, "table", "values", default_fonts_list)
    table_font_size: OptionsInfo = OptionsInfo(True, "table", "px", "16px")
    table_font_weight: OptionsInfo = OptionsInfo(True, "table", "value", "normal")
    table_font_style: OptionsInfo = OptionsInfo(True, "table", "value", "normal")
    table_font_color: OptionsInfo = OptionsInfo(True, "table", "value", "#333333")
    table_font_color_light: OptionsInfo = OptionsInfo(True, "table", "value", "#FFFFFF")
    table_border_top_include: OptionsInfo = OptionsInfo(False, "table", "boolean", True)
    table_border_top_style: OptionsInfo = OptionsInfo(True, "table", "value", "solid")
    table_border_top_width: OptionsInfo = OptionsInfo(True, "table", "px", "2px")
    table_border_top_color: OptionsInfo = OptionsInfo(True, "table", "value", "#A8A8A8")
    table_border_right_style: OptionsInfo = OptionsInfo(True, "table", "value", "none")
    table_border_right_width: OptionsInfo = OptionsInfo(True, "table", "px", "2px")
    table_border_right_color: OptionsInfo = OptionsInfo(True, "table", "value", "#D3D3D3")
    table_border_bottom_include: OptionsInfo = OptionsInfo(False, "table", "boolean", True)
    table_border_bottom_style: OptionsInfo = OptionsInfo(True, "table", "value", "solid")
    table_border_bottom_width: OptionsInfo = OptionsInfo(True, "table", "px", "2px")
    table_border_bottom_color: OptionsInfo = OptionsInfo(True, "table", "value", "#A8A8A8")
    table_border_left_style: OptionsInfo = OptionsInfo(True, "table", "value", "none")
    table_border_left_width: OptionsInfo = OptionsInfo(True, "table", "px", "2px")
    table_border_left_color: OptionsInfo = OptionsInfo(True, "table", "value", "#D3D3D3")
    heading_background_color: OptionsInfo = OptionsInfo(True, "heading", "value", None)
    heading_align: OptionsInfo = OptionsInfo(True, "heading", "value", "center")
    heading_title_font_size: OptionsInfo = OptionsInfo(True, "heading", "px", "125%")
    heading_title_font_weight: OptionsInfo = OptionsInfo(True, "heading", "value", "initial")
    heading_subtitle_font_size: OptionsInfo = OptionsInfo(True, "heading", "px", "85%")
    heading_subtitle_font_weight: OptionsInfo = OptionsInfo(True, "heading", "value", "initial")
    heading_padding: OptionsInfo = OptionsInfo(True, "heading", "px", "4px")
    heading_padding_horizontal: OptionsInfo = OptionsInfo(True, "heading", "px", "5px")
    heading_border_bottom_style: OptionsInfo = OptionsInfo(True, "heading", "value", "solid")
    heading_border_bottom_width: OptionsInfo = OptionsInfo(True, "heading", "px", "2px")
    heading_border_bottom_color: OptionsInfo = OptionsInfo(True, "heading", "value", "#D3D3D3")
    heading_border_lr_style: OptionsInfo = OptionsInfo(True, "heading", "value", "none")
    heading_border_lr_width: OptionsInfo = OptionsInfo(True, "heading", "px", "1px")
    heading_border_lr_color: OptionsInfo = OptionsInfo(True, "heading", "value", "#D3D3D3")
    column_labels_background_color: OptionsInfo = OptionsInfo(True, "column_labels", "value", None)
    column_labels_font_size: OptionsInfo = OptionsInfo(True, "column_labels", "px", "100%")
    column_labels_font_weight: OptionsInfo = OptionsInfo(True, "column_labels", "value", "normal")
    column_labels_text_transform: OptionsInfo = OptionsInfo(
        True, "column_labels", "value", "inherit"
    )
    column_labels_padding: OptionsInfo = OptionsInfo(True, "column_labels", "px", "5px")
    column_labels_padding_horizontal: OptionsInfo = OptionsInfo(True, "column_labels", "px", "5px")
    column_labels_vlines_style: OptionsInfo = OptionsInfo(True, "table_body", "value", "none")
    column_labels_vlines_width: OptionsInfo = OptionsInfo(True, "table_body", "px", "1px")
    column_labels_vlines_color: OptionsInfo = OptionsInfo(True, "table_body", "value", "#D3D3D3")
    column_labels_border_top_style: OptionsInfo = OptionsInfo(
        True, "column_labels", "value", "solid"
    )
    column_labels_border_top_width: OptionsInfo = OptionsInfo(True, "column_labels", "px", "2px")
    column_labels_border_top_color: OptionsInfo = OptionsInfo(
        True, "column_labels", "value", "#D3D3D3"
    )
    column_labels_border_bottom_style: OptionsInfo = OptionsInfo(
        True, "column_labels", "value", "solid"
    )
    column_labels_border_bottom_width: OptionsInfo = OptionsInfo(True, "column_labels", "px", "2px")
    column_labels_border_bottom_color: OptionsInfo = OptionsInfo(
        True, "column_labels", "value", "#D3D3D3"
    )
    column_labels_border_lr_style: OptionsInfo = OptionsInfo(True, "column_labels", "value", "none")
    column_labels_border_lr_width: OptionsInfo = OptionsInfo(True, "column_labels", "px", "1px")
    column_labels_border_lr_color: OptionsInfo = OptionsInfo(
        True, "column_labels", "value", "#D3D3D3"
    )
    column_labels_hidden: OptionsInfo = OptionsInfo(False, "column_labels", "boolean", False)
    row_group_background_color: OptionsInfo = OptionsInfo(True, "row_group", "value", None)
    row_group_font_size: OptionsInfo = OptionsInfo(True, "row_group", "px", "100%")
    row_group_font_weight: OptionsInfo = OptionsInfo(True, "row_group", "value", "initial")
    row_group_text_transform: OptionsInfo = OptionsInfo(True, "row_group", "value", "inherit")
    row_group_padding: OptionsInfo = OptionsInfo(True, "row_group", "px", "8px")
    row_group_padding_horizontal: OptionsInfo = OptionsInfo(True, "row_group", "px", "5px")
    row_group_border_top_style: OptionsInfo = OptionsInfo(True, "row_group", "value", "solid")
    row_group_border_top_width: OptionsInfo = OptionsInfo(True, "row_group", "px", "2px")
    row_group_border_top_color: OptionsInfo = OptionsInfo(True, "row_group", "value", "#D3D3D3")
    row_group_border_right_style: OptionsInfo = OptionsInfo(True, "row_group", "value", "none")
    row_group_border_right_width: OptionsInfo = OptionsInfo(True, "row_group", "px", "1px")
    row_group_border_right_color: OptionsInfo = OptionsInfo(True, "row_group", "value", "#D3D3D3")
    row_group_border_bottom_style: OptionsInfo = OptionsInfo(True, "row_group", "value", "solid")
    row_group_border_bottom_width: OptionsInfo = OptionsInfo(True, "row_group", "px", "2px")
    row_group_border_bottom_color: OptionsInfo = OptionsInfo(True, "row_group", "value", "#D3D3D3")
    row_group_border_left_style: OptionsInfo = OptionsInfo(True, "row_group", "value", "none")
    row_group_border_left_width: OptionsInfo = OptionsInfo(True, "row_group", "px", "1px")
    row_group_border_left_color: OptionsInfo = OptionsInfo(True, "row_group", "value", "#D3D3D3")
    # row_group_default_label: OptionsInfo = OptionsInfo(False, "row_group", "value", None)
    row_group_as_column: OptionsInfo = OptionsInfo(False, "row_group", "boolean", False)
    table_body_hlines_style: OptionsInfo = OptionsInfo(True, "table_body", "value", "solid")
    table_body_hlines_width: OptionsInfo = OptionsInfo(True, "table_body", "px", "1px")
    table_body_hlines_color: OptionsInfo = OptionsInfo(True, "table_body", "value", "#D3D3D3")
    table_body_vlines_style: OptionsInfo = OptionsInfo(True, "table_body", "value", "none")
    table_body_vlines_width: OptionsInfo = OptionsInfo(True, "table_body", "px", "1px")
    table_body_vlines_color: OptionsInfo = OptionsInfo(True, "table_body", "value", "#D3D3D3")
    table_body_border_top_style: OptionsInfo = OptionsInfo(True, "table_body", "value", "solid")
    table_body_border_top_width: OptionsInfo = OptionsInfo(True, "table_body", "px", "2px")
    table_body_border_top_color: OptionsInfo = OptionsInfo(True, "table_body", "value", "#D3D3D3")
    table_body_border_bottom_style: OptionsInfo = OptionsInfo(True, "table_body", "value", "solid")
    table_body_border_bottom_width: OptionsInfo = OptionsInfo(True, "table_body", "px", "2px")
    table_body_border_bottom_color: OptionsInfo = OptionsInfo(
        True, "table_body", "value", "#D3D3D3"
    )
    data_row_padding: OptionsInfo = OptionsInfo(True, "data_row", "px", "8px")
    data_row_padding_horizontal: OptionsInfo = OptionsInfo(True, "data_row", "px", "5px")
    stub_background_color: OptionsInfo = OptionsInfo(True, "stub", "value", None)
    stub_font_size: OptionsInfo = OptionsInfo(True, "stub", "px", "100%")
    stub_font_weight: OptionsInfo = OptionsInfo(True, "stub", "value", "initial")
    stub_text_transform: OptionsInfo = OptionsInfo(True, "stub", "value", "inherit")
    stub_border_style: OptionsInfo = OptionsInfo(True, "stub", "value", "solid")
    stub_border_width: OptionsInfo = OptionsInfo(True, "stub", "px", "2px")
    stub_border_color: OptionsInfo = OptionsInfo(True, "stub", "value", "#D3D3D3")
    stub_row_group_background_color: OptionsInfo = OptionsInfo(True, "stub", "value", None)
    stub_row_group_font_size: OptionsInfo = OptionsInfo(True, "stub", "px", "100%")
    stub_row_group_font_weight: OptionsInfo = OptionsInfo(True, "stub", "value", "initial")
    stub_row_group_text_transform: OptionsInfo = OptionsInfo(True, "stub", "value", "inherit")
    stub_row_group_border_style: OptionsInfo = OptionsInfo(True, "stub", "value", "solid")
    stub_row_group_border_width: OptionsInfo = OptionsInfo(True, "stub", "px", "2px")
    stub_row_group_border_color: OptionsInfo = OptionsInfo(True, "stub", "value", "#D3D3D3")
    # summary_row_padding: OptionsInfo = OptionsInfo(True, "summary_row", "px", "8px")
    # summary_row_padding_horizontal: OptionsInfo = OptionsInfo(True, "summary_row", "px", "5px")
    # summary_row_background_color: OptionsInfo = OptionsInfo(True, "summary_row", "value", None)
    # summary_row_text_transform: OptionsInfo = OptionsInfo(True, "summary_row", "value", "inherit")
    # summary_row_border_style: OptionsInfo = OptionsInfo(True, "summary_row", "value", "solid")
    # summary_row_border_width: OptionsInfo = OptionsInfo(True, "summary_row", "px", "2px")
    # summary_row_border_color: OptionsInfo = OptionsInfo(True, "summary_row", "value", "#D3D3D3")
    grand_summary_row_padding: OptionsInfo = OptionsInfo(True, "grand_summary_row", "px", "8px")
    grand_summary_row_padding_horizontal: OptionsInfo = OptionsInfo(
        True, "grand_summary_row", "px", "5px"
    )
    grand_summary_row_background_color: OptionsInfo = OptionsInfo(
        True, "grand_summary_row", "value", None
    )
    grand_summary_row_text_transform: OptionsInfo = OptionsInfo(
        True, "grand_summary_row", "value", "inherit"
    )
    grand_summary_row_border_style: OptionsInfo = OptionsInfo(
        True, "grand_summary_row", "value", "double"
    )
    grand_summary_row_border_width: OptionsInfo = OptionsInfo(
        True, "grand_summary_row", "px", "6px"
    )
    grand_summary_row_border_color: OptionsInfo = OptionsInfo(
        True, "grand_summary_row", "value", "#D3D3D3"
    )
    # footnotes_font_size: OptionsInfo = OptionsInfo(True, "footnotes", "px", "90%")
    # footnotes_padding: OptionsInfo = OptionsInfo(True, "footnotes", "px", "4px")
    # footnotes_padding_horizontal: OptionsInfo = OptionsInfo(True, "footnotes", "px", "5px")
    # footnotes_background_color: OptionsInfo = OptionsInfo(True, "footnotes", "value", None)
    # footnotes_margin: OptionsInfo = OptionsInfo(True, "footnotes", "px", "0px")
    # footnotes_border_bottom_style: OptionsInfo = OptionsInfo(True, "footnotes", "value", "none")
    # footnotes_border_bottom_width: OptionsInfo = OptionsInfo(True, "footnotes", "px", "2px")
    # footnotes_border_bottom_color: OptionsInfo = OptionsInfo(True, "footnotes", "value", "#D3D3D3")
    # footnotes_border_lr_style: OptionsInfo = OptionsInfo(True, "footnotes", "value", "none")
    # footnotes_border_lr_width: OptionsInfo = OptionsInfo(True, "footnotes", "px", "2px")
    # footnotes_border_lr_color: OptionsInfo = OptionsInfo(True, "footnotes", "value", "#D3D3D3")
    # footnotes_marks: OptionsInfo = OptionsInfo(False, "footnotes", "values", "numbers")
    # footnotes_multiline: OptionsInfo = OptionsInfo(False, "footnotes", "boolean", True)
    # footnotes_sep: OptionsInfo = OptionsInfo(False, "footnotes", "value", " ")
    source_notes_padding: OptionsInfo = OptionsInfo(True, "source_notes", "px", "4px")
    source_notes_padding_horizontal: OptionsInfo = OptionsInfo(True, "source_notes", "px", "5px")
    source_notes_background_color: OptionsInfo = OptionsInfo(True, "source_notes", "value", None)
    source_notes_font_size: OptionsInfo = OptionsInfo(True, "source_notes", "px", "90%")
    source_notes_border_bottom_style: OptionsInfo = OptionsInfo(
        True, "source_notes", "value", "none"
    )
    source_notes_border_bottom_width: OptionsInfo = OptionsInfo(True, "source_notes", "px", "2px")
    source_notes_border_bottom_color: OptionsInfo = OptionsInfo(
        True, "source_notes", "value", "#D3D3D3"
    )
    source_notes_border_lr_style: OptionsInfo = OptionsInfo(True, "source_notes", "value", "none")
    source_notes_border_lr_width: OptionsInfo = OptionsInfo(True, "source_notes", "px", "2px")
    source_notes_border_lr_color: OptionsInfo = OptionsInfo(
        True, "source_notes", "value", "#D3D3D3"
    )
    source_notes_multiline: OptionsInfo = OptionsInfo(False, "source_notes", "boolean", True)
    source_notes_sep: OptionsInfo = OptionsInfo(False, "source_notes", "value", " ")
    row_striping_background_color: OptionsInfo = OptionsInfo(True, "row", "value", "#F4F4F4")
    row_striping_include_stub: OptionsInfo = OptionsInfo(False, "row", "boolean", False)
    row_striping_include_table_body: OptionsInfo = OptionsInfo(False, "row", "boolean", False)
    container_width: OptionsInfo = OptionsInfo(False, "container", "px", "auto")
    container_height: OptionsInfo = OptionsInfo(False, "container", "px", "auto")
    container_padding_x: OptionsInfo = OptionsInfo(False, "container", "px", "0px")
    container_padding_y: OptionsInfo = OptionsInfo(False, "container", "px", "10px")
    container_overflow_x: OptionsInfo = OptionsInfo(False, "container", "overflow", "auto")
    container_overflow_y: OptionsInfo = OptionsInfo(False, "container", "overflow", "auto")
    # page_orientation: OptionsInfo = OptionsInfo(False, "page", "value", "portrait")
    # page_numbering: OptionsInfo = OptionsInfo(False, "page", "boolean", False)
    # page_header_use_tbl_headings: OptionsInfo = OptionsInfo(False, "page", "boolean", False)
    # page_footer_use_tbl_notes: OptionsInfo = OptionsInfo(False, "page", "boolean", False)
    # page_width: OptionsInfo = OptionsInfo(False, "page", "value", "8.5in")
    # page_height: OptionsInfo = OptionsInfo(False, "page", "value", "11.0in")
    # page_margin_left: OptionsInfo = OptionsInfo(False, "page", "value", "1.0in")
    # page_margin_right: OptionsInfo = OptionsInfo(False, "page", "value", "1.0in")
    # page_margin_top: OptionsInfo = OptionsInfo(False, "page", "value", "1.0in")
    # page_margin_bottom: OptionsInfo = OptionsInfo(False, "page", "value", "1.0in")
    # page_header_height: OptionsInfo = OptionsInfo(False, "page", "value", "0.5in")
    # page_footer_height: OptionsInfo = OptionsInfo(False, "page", "value", "0.5in")
    quarto_disable_processing: OptionsInfo = OptionsInfo(False, "quarto", "logical", False)
    quarto_use_bootstrap: OptionsInfo = OptionsInfo(False, "quarto", "logical", False)

    def __getitem__(self, k: str) -> Any:
        return getattr(self, k).value

    def _get_all_options_keys(self) -> list[str | None]:
        return [x.parameter for x in self._options.values()]

    # def _get_option_type(self, option: str) -> Any | list[str]:
    #    return self._options[option].type

    def _set_option_value(self, option: str, value: Any):
        old_info = getattr(self, option)
        new_info = replace(old_info, value=value)

        return replace(self, **{option: new_info})
