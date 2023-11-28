from __future__ import annotations

import copy
import re

from typing import overload, TypeVar, Optional
from typing_extensions import Self, TypeAlias
from dataclasses import dataclass, field, replace
from ._utils import _str_detect

from ._styles import CellStyle

# Note that we replace with with collections.abc after python 3.8
from typing import Sequence

T = TypeVar("T")


# GT Data ----
from dataclasses import dataclass

__GT = None


@dataclass
class GTData:
    _tbl_data: TblData
    _body: Body
    _boxhead: Boxhead
    _stub: Stub
    _row_groups: RowGroups
    _group_rows: GroupRows
    _spanners: Spanners
    _heading: Heading | None
    _stubhead: Stubhead
    _source_notes: SourceNotes
    _footnotes: Footnotes
    _styles: Styles
    _locale: Locale | None
    _formats: Formats
    _options: Options
    _has_built: bool = False

    def _replace(self, **kwargs) -> Self:
        # TODO: may want to validate that kwargs should be an attribute on GT
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
        locale: str | None = None,
    ):
        stub = Stub(data, rowname_col=rowname_col, groupname_col=groupname_col)
        boxhead = Boxhead(
            data, auto_align=auto_align, rowname_col=rowname_col, groupname_col=groupname_col
        )

        row_groups = stub._to_row_groups()
        group_rows = GroupRows(data, group_key=groupname_col).reorder(row_groups)

        return cls(
            _tbl_data=data,
            _body=Body.from_empty(data),
            _boxhead=boxhead,  # uses get_tbl_data()
            _stub=stub,  # uses get_tbl_data
            _row_groups=row_groups,
            _group_rows=group_rows,
            _spanners=Spanners([]),
            _heading=Heading(),
            _stubhead=None,
            _source_notes=[],
            _footnotes=[],
            _styles=[],
            _locale=Locale(locale),
            _formats=[],
            _options=Options(),
        )


class _Sequence(Sequence[T]):
    _d: list[T]

    def __init__(self, data: list[T]):
        self._d = data

    @overload
    def __getitem__(self, ii: int) -> T:
        ...

    @overload
    def __getitem__(self, ii: slice) -> Self[T]:
        ...

    @overload
    def __getitem__(self, ii: list[int]) -> Self[T]:
        ...

    def __getitem__(self, ii: int | slice | list[int]) -> T | Self[T]:
        if isinstance(ii, slice):
            return self.__class__(self._d[ii])
        elif isinstance(ii, list):
            return self.__class__([self._d[el] for el in ii])

        return self._d[ii]

    def __len__(self):
        return len(self._d)

    def __repr__(self):
        return f"{type(self).__name__}({self._d.__repr__()})"

    def __eq__(self, other: Any) -> bool:
        return (type(self) is type(other)) and (self._d == other._d)


# Body ----
__Body = None

from typing import Union, List, Any
import pandas as pd
from ._tbl_data import DataFrameLike, TblData, _get_cell, _set_cell


# TODO: it seems like this could just be a DataFrameLike object?
# Similar to TblData now being a DataFrame, rather than its own class
# I've left for now, and have just implemented concretes for it in
# _tbl_data.py
class Body:
    body: TblData
    data: Any

    def __init__(self, body: Union[pd.DataFrame, TblData]):
        self.body = body

    def render_formats(self, data_tbl: TblData, formats: List[FormatInfo], context: Context):
        for fmt in formats:
            eval_func = getattr(fmt.func, context, fmt.func.default)
            if eval_func is None:
                raise Exception("Internal Error")
            for col, row in fmt.cells.resolve():
                result = eval_func(_get_cell(data_tbl, row, col))
                # TODO: I think that this is very inefficient with polars, so
                # we could either accumulate results and set them per column, or
                # could always use a pandas DataFrame inside Body?
                _set_cell(self.body, row, col, result)

        return self

    @classmethod
    def from_empty(cls, body: DataFrameLike):
        empty_df = pd.DataFrame(pd.NA, index=body.index, columns=body.columns, dtype="string")

        return cls(empty_df)


# Boxhead ----
__Boxhead = None

from typing import Optional, List
from enum import Enum, auto
import pandas as pd

from ._tbl_data import TblData, get_column_names


class ColumnAlignment(Enum):
    left = auto()
    center = auto()
    right = auto()
    justify = auto()


class ColInfoTypeEnum(Enum):
    default = auto()
    stub = auto()
    row_group = auto()
    hidden = auto()


@dataclass
class ColInfo:
    # TODO: Make var readonly
    var: str
    type: ColInfoTypeEnum = ColInfoTypeEnum.default
    column_label: Optional[str] = None
    column_align: Optional[ColumnAlignment] = None
    column_width: Optional[str] = None

    # The components of the boxhead are:
    # `var` (obtained from column names)
    # `column_label` (obtained from column names)
    # `column_align` = None
    # `column_width` = None

    def __post_init__(self):
        if self.column_label is None:
            self.column_label = self.var

    @property
    def visible(self) -> bool:
        return self.type != ColInfoTypeEnum.hidden

    @property
    def defaulted_align(self) -> str:
        return "center" if self.column_align is None else str(self.column_align)


class Boxhead(_Sequence[ColInfo]):
    _d: List[ColInfo]

    def __init__(
        self,
        data: TblData | list[ColInfo],
        auto_align: bool = True,
        rowname_col: Optional[str] = None,
        groupname_col: Optional[str] = None,
    ):
        if isinstance(data, list):
            self._d = data
        else:
            # Obtain the column names from the data and initialize the
            # `_boxhead` from that
            column_names = get_column_names(data)
            self._d = [ColInfo(col) for col in column_names]
        if not isinstance(data, list) and auto_align:
            self.align_from_data(data=data)

        if rowname_col is not None:
            self.set_rowname_col(rowname_col)

        if groupname_col is not None:
            self.set_groupname_col(groupname_col)

    def set_rowname_col(self, rowname_col: str):
        # TODO: validate that rowname_col is in the boxhead
        for ii, col in enumerate(self._d):
            if col.var == rowname_col:
                new_col = replace(col, type=ColInfoTypeEnum.stub)
                self._d[ii] = new_col
            elif col.type == ColInfoTypeEnum.stub:
                new_col = replace(col, type=ColInfoTypeEnum.default)
                self._d[ii] = new_col

    def set_groupname_col(self, groupname_col: str):
        # TODO: validate that groupname_col is in the boxhead
        for ii, col in enumerate(self._d):
            if col.var == groupname_col:
                new_col = replace(col, type=ColInfoTypeEnum.row_group)
                self._d[ii] = new_col
            elif col.type == ColInfoTypeEnum.row_group:
                new_col = replace(col, type=ColInfoTypeEnum.default)
                self._d[ii] = new_col

    def set_col_hidden(self, colname: str):
        # TODO: validate that colname is in the boxhead
        for ii, col in enumerate(self._d):
            if col.var == colname:
                new_col = replace(col, type=ColInfoTypeEnum.hidden)
                self._d[ii] = new_col

    def align_from_data(self, data: TblData):
        """Updates align attribute in entries based on data types."""

        # TODO: validate that data columns and ColInfo list correspond
        if len(get_column_names(data)) != len(self._d):
            raise ValueError("Number of data columns must match length of Boxhead")

        if any(
            col_info.var != col_name for col_info, col_name in zip(self._d, get_column_names(data))
        ):
            raise ValueError("Column names must match between data and Boxhead")

        # Obtain a list of column classes for each of the column names by iterating
        # through each of the columns and obtaining the type of the column from
        # a Pandas DataFrame or a Polars DataFrame
        col_classes = []
        for col in get_column_names(data):
            dtype = data[col].dtype

            if dtype == "object":
                # Check whether all values in 'object' columns are strings that
                # for all intents and purpose are 'number-like'

                import pandas as pd

                col_vals = data[col].to_list()

                # Detect whether all non-NA values in the column are 'number-like'
                # through use of a regular expression
                number_like_matches = []

                for val in col_vals:
                    if isinstance(val, str):
                        number_like_matches.append(re.match("^[0-9 -/:\\.]*$", val))

                # If all values in the column are 'number-like', then set the
                # dtype to 'character-numeric'
                if all(number_like_matches):
                    dtype = "character-numeric"

            col_classes.append(dtype)

        # Get a list of `align` values by translating the column classes
        align = []

        for col_class in col_classes:
            # Ensure that `col_class` is lowercase
            col_class = str(col_class).lower()

            # Translate the column classes to an alignment value of 'left', 'right', or 'center'
            if col_class == "character-numeric":
                align.append("right")
            elif col_class == "object":
                align.append("left")
            elif _str_detect(col_class, "int") or _str_detect(col_class, "float"):
                align.append("right")
            elif _str_detect(col_class, "date"):
                align.append("right")
            elif _str_detect(col_class, "bool"):
                align.append("center")
            elif col_class == "factor":
                align.append("center")
            elif col_class == "list":
                align.append("center")
            else:
                align.append("center")

        # Set the alignment for each column in the boxhead
        for col, alignment in zip(self._d, align):
            col.column_align = alignment

    def vars_from_type(self, type: ColInfoTypeEnum) -> List[str]:
        return [x.var for x in self._d if x.type == type]

    def reorder(self, vars: List[str]) -> Self:
        boxh_vars = [col.var for col in self]
        if set(vars) != set(boxh_vars):
            raise ValueError("Reordering vars must contain all boxhead vars.")

        new_order = [boxh_vars.index(var) for var in vars]

        return self[new_order]

    # Get a list of columns
    def _get_columns(self) -> List[str]:
        return [x.var for x in self._d]

    # Get a list of column labels
    def _get_column_labels(self) -> List[str | None]:
        return [x.column_label for x in self._d]

    # Set column label
    def _set_column_label(self, column: str, label: str):
        for x in self._d:
            if x.var == column:
                x.column_label = label

        return self

    # Set column alignments
    def _set_column_align(self, column: str, align: str):
        for x in self._d:
            if x.var == column:
                x.column_align = ColumnAlignment[align]

        return self

    # Get a list of column widths
    def _get_column_widths(self) -> List[str | None]:
        return [x.column_width for x in self._d]

    # Get a list of visible columns
    def _get_default_columns(self) -> List[ColInfo]:
        default_columns = [x for x in self._d if x.type == ColInfoTypeEnum.default]
        return default_columns

    def _get_stub_column(self) -> Optional[ColInfo]:
        stub_column = [x for x in self._d if x.type == ColInfoTypeEnum.stub]
        if len(stub_column) == 0:
            return None
        return stub_column[0]

    # Get a list of visible column labels
    def _get_default_column_labels(self) -> List[str | None]:
        default_column_labels = [
            x.column_label for x in self._d if x.type == ColInfoTypeEnum.default
        ]
        return default_column_labels

    def _get_default_alignments(self) -> List[str]:
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

        if len(alignment) == 0:
            raise ValueError(f"The `var` used ({var}) doesn't exist in the boxhead.")

        # Convert the single alignment value in the list to a string
        alignment = str(alignment[0])

        return alignment

    # Get the number of columns for the visible (not hidden) data; this
    # excludes the number of columns required for the table stub
    def _get_number_of_visible_data_columns(self) -> int:
        return len(self._get_default_columns())

    # Obtain the number of visible columns in the built table; this should
    # account for the size of the stub in the final, built table
    def _get_effective_number_of_columns(
        self, stub: Stub, row_groups: RowGroups, options: Options
    ) -> int:
        n_data_cols = self._get_number_of_visible_data_columns()

        stub_layout = stub._get_stub_layout(row_groups=row_groups, options=options)
        # Once the stub is defined in the package, we need to account
        # for the width of the stub at build time to fully obtain the number
        # of visible columns in the built table
        n_data_cols = n_data_cols + len(stub_layout)

        return n_data_cols


# Stub ----
__Stub = None

from ._tbl_data import TblData, n_rows


@dataclass
class RowInfo:
    # TODO: Make `rownum_i` readonly
    rownum_i: int
    group_id: Optional[str] = None
    rowname: Optional[str] = None
    group_label: Optional[str] = None
    built: bool = False

    # The components of the stub are:
    # `rownum_i` (The initial row indices for the table at ingest time)
    # `group_id` = None
    # `rowname` = None
    # `group_label` = None
    # `built` = False


class Stub(_Sequence[RowInfo]):
    _d: list[RowInfo]

    def __init__(
        self, data: TblData | list[RowInfo], rowname_col: str = None, groupname_col: str = None
    ):
        if isinstance(data, list):
            self._d = list(data)

        else:
            # Obtain a list of row indices from the data and initialize
            # the `_stub` from that
            row_indices = list(range(n_rows(data)))

            if groupname_col is not None:
                group_id = data[groupname_col].tolist()
            else:
                group_id = [None] * n_rows(data)

            if rowname_col is not None:
                row_names = data[rowname_col].tolist()
            else:
                row_names = [None] * n_rows(data)

            # Obtain the column names from the data and initialize the
            # `_stub` from that
            self._d = [RowInfo(*i) for i in zip(row_indices, group_id, row_names)]

    def _to_row_groups(self) -> RowGroups:
        # get unique group_ids, using dict as an ordered set
        group_ids = list({row.group_id: True for row in self if row.group_id is not None})

        return group_ids

    def _get_stub_components(self) -> list[str]:
        stub_components: list[str] = []

        if any(entry.group_id is not None for entry in self):
            stub_components.append("group_id")

        if any(entry.rowname is not None for entry in self):
            stub_components.append("row_id")

        return stub_components

    # Determine whether the table should have row group labels set within a column in the stub
    def _stub_group_names_has_column(self, row_groups: RowGroups, options: Options) -> bool:
        # If there aren't any row groups then the result is always False
        if len(row_groups) < 1:
            return False

        # Given that there are row groups, we need to look at the option `row_group_as_column` to
        # determine whether they populate a column located in the stub; if set as True then that's
        # the return value
        row_group_as_column = options._get_option_value(option="row_group_as_column")

        row_group_as_column: Any
        if not isinstance(row_group_as_column, bool):
            raise TypeError(
                "Variable type mismatch. Expected bool, got something entirely different."
            )

        return row_group_as_column

    def _get_stub_layout(self, row_groups: RowGroups, options: Options) -> List[str]:
        # Determine which stub components are potentially present as columns
        stub_rownames_is_column = "row_id" in self._get_stub_components()
        stub_groupnames_is_column = self._stub_group_names_has_column(
            row_groups=row_groups, options=options
        )

        # Get the potential total number of columns in the table stub
        n_stub_cols = stub_rownames_is_column + stub_groupnames_is_column

        # Resolve the layout of the stub (i.e., the roles of columns if present)
        if n_stub_cols == 0:
            # TODO: If summary rows are present, we will use the `rowname` column
            # # for the summary row labels
            # if _summary_exists(data=data):
            #     stub_layout = ["rowname"]
            # else:
            #     stub_layout = []

            stub_layout = []

        else:
            stub_layout = [
                label
                for label, condition in [
                    ("group_label", stub_groupnames_is_column),
                    ("rowname", stub_rownames_is_column),
                ]
                if condition
            ]

        return stub_layout


# Row groups ----
__RowGroups = None

RowGroups: TypeAlias = List[str]

# Group rows ----
__GroupRows = None


@dataclass
class GroupRowInfo:
    group_id: str
    group_label: str | None = None
    indices: list[int] = field(default_factory=lambda: [])
    # row_start: int | None = None
    # row_end: int | None = None
    has_summary_rows: bool = False
    summary_row_side: str | None = None

    def defaulted_label(self) -> str:
        """Return a group label that has been defaulted."""
        label = self.group_label if self.group_label is not None else self.group_id
        return label


class MISSING_GROUP:
    """Represent a category of all missing group levels in data."""


class GroupRows(_Sequence[GroupRowInfo]):
    _d: list[GroupRowInfo]

    def __init__(self, data: list[GroupRowInfo] | DataFrameLike, group_key: Optional[str] = None):
        if isinstance(data, list):
            self._d = data

        elif group_key is None:
            self._d = []

        # otherwise, instantiate from a table of data
        else:
            from ._tbl_data import group_splits

            self._d = []
            for grp_key, ind in group_splits(data, group_key=group_key).items():
                self._d.append(GroupRowInfo(grp_key, indices=ind))

    def reorder(self, group_ids: list[str | MISSING_GROUP]) -> Self:
        # TODO: validate all group_ids are in data
        non_missing = [g for g in group_ids if not isinstance(g, MISSING_GROUP)]
        crnt_order = {grp.group_id: ii for ii, grp in enumerate(self)}

        set_gids = set(group_ids)
        missing_groups = [grp.group_id for grp in self if grp.group_id not in set_gids]
        reordered = [
            *[self[crnt_order[g]] for g in non_missing],
            *[self[crnt_order[g]] for g in missing_groups],
        ]

        return self.__class__(reordered)

    def indices_map(self) -> dict[int, str]:
        list_dicts = [{ind: info.defaulted_label() for ind in info.indices} for info in self]
        final = {}

        for entry in list_dicts:
            key, value = list(entry.items())[0]
            final.update({key: value})

        return final


# Spanners ----
__Spanners = None
import pandas as pd


@dataclass
class SpannerInfo:
    spanner_id: str
    spanner_level: int
    spanner_label: str | None = None
    spanner_units: str | None = None
    spanner_pattern: str | None = None
    vars: list[str] = field(default_factory=lambda: [])
    built: Optional[str] = None

    def built_label(self) -> str:
        """Return a list of spanner labels that have been built."""
        label = self.built if self.built is not None else self.spanner_label
        if label is None:
            raise ValueError("Spanner label must be a string and not None.")
        return label


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
            s.spanner_level for s in self if any(v in column_names for v in s.vars)
        ]

        return max(overlapping_levels, default=-1) + 1

    def append_entry(self, span: SpannerInfo) -> Self:
        return self.__class__(self._d + [span])


# Heading ---
__Heading = None

from typing import Optional, Union, List


class Heading:
    title: Optional[str] = None
    subtitle: Optional[str] = None
    preheader: Optional[Union[str, List[str]]] = None


# Stubhead ----
__Stubhead = None

from typing import Optional

Stubhead: TypeAlias = Optional[str]


# Sourcenotes ----
__Sourcenotes = None

from typing import List


SourceNotes = List[str]

# Footnotes ----
__Footnotes = None

from typing import Optional, List
from enum import Enum, auto


class FootnotePlacement(Enum):
    left = auto()
    right = auto()
    auto = auto()


@dataclass
class FootnoteInfo:
    locname: Optional[str] = None
    grpname: Optional[str] = None
    colname: Optional[str] = None
    locnum: Optional[int] = None
    rownum: Optional[int] = None
    colnum: Optional[int] = None
    footnotes: Optional[List[str]] = None
    placement: Optional[FootnotePlacement] = None


Footnotes: TypeAlias = List[FootnoteInfo]

# Styles ----
__Styles = None

from typing import List, Optional


@dataclass
class StyleInfo:
    locname: str
    locnum: int
    grpname: Optional[str] = None
    colname: Optional[str] = None
    rownum: Optional[int] = None
    colnum: Optional[int] = None
    styles: Optional[List[CellStyle]] = field(default_factory=list)


Styles: TypeAlias = List[StyleInfo]

# Locale ----
__Locale = None

from typing import Optional


class Locale:
    locale: Optional[str]

    def __init__(self, locale: Optional[str]):
        self._locale: Union[str, None] = locale


# Formats ----
__Formats = None

from typing import Any, Callable, TypeVar, Union, List, Optional, Tuple

from ._tbl_data import n_rows

FormatFn = Callable[[Any], str]


class FormatFns:
    html: Optional[FormatFn]
    latex: Optional[FormatFn]
    rtf: Optional[FormatFn]
    default: Optional[FormatFn]

    def __init__(self, **kwargs: FormatFn):
        for format in ["html", "latex", "rtf", "default"]:
            if kwargs.get(format):
                setattr(self, format, kwargs[format])


class CellSubset:
    def __init__(self):
        pass

    def resolve(self) -> List[Tuple[str, int]]:
        raise NotImplementedError("Not implemented")


class CellRectangle(CellSubset):
    cols: List[str]
    rows: List[int]

    def __init__(self, cols: List[str], rows: List[int]):
        self.cols = cols
        self.rows = rows

    def resolve(self):
        return list((col, row) for col in self.cols for row in self.rows)


class FormatInfo:
    func: FormatFns
    cells: CellSubset

    def __init__(self, func: FormatFns, cols: List[str], rows: List[int]):
        self.func = func
        self.cells = CellRectangle(cols, rows)


# TODO: this will contain private methods for formatting cell values to strings
# class Formats:
#     def __init__(self):
#         pass
Formats = list

# Tbl Data ----
from ._tbl_data import TblData


# Options ----
__Options = None

from typing import Optional, Union, List, Any, cast
from great_tables import _utils

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


class OptionsInfo:
    parameter: str
    scss: Optional[bool]
    category: Optional[str]
    type: Optional[str]
    value: Optional[Union[Any, List[str]]]

    def __init__(
        self,
        parameter: str,
        scss: Optional[bool] = None,
        category: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[Union[Any, List[str]]] = None,
    ):
        self.parameter = parameter
        self.scss = scss
        self.category = category
        self.type = type
        self.value = value


# fmt: off
class Options:
    def __init__(self):
        self._options: dict[str, OptionsInfo] = dict(
           (v.parameter, v) for v in [
            #           parameter                            scss    category            type        value
            OptionsInfo("table_id",                          False,  "table",            "value",    None),
            OptionsInfo("table_caption",                     False,  "table",            "value",    None),
            OptionsInfo("table_width",                        True,  "table",            "px",       "auto"),
            OptionsInfo("table_layout",                       True,  "table",            "value",    "fixed"),
            OptionsInfo("table_margin_left",                  True,  "table",            "px",       "auto"),
            OptionsInfo("table_margin_right",                 True,  "table",            "px",       "auto"),
            OptionsInfo("table_background_color",             True,  "table",            "value",    "#FFFFFF"),
            OptionsInfo("table_additional_css",              False,  "table",            "values",   None),
            OptionsInfo("table_font_names",                  False,  "table",            "values",   default_fonts_list),
            OptionsInfo("table_font_size",                    True,  "table",            "px",       "16px"),
            OptionsInfo("table_font_weight",                  True,  "table",            "value",    "normal"),
            OptionsInfo("table_font_style",                   True,  "table",            "value",    "normal"),
            OptionsInfo("table_font_color",                   True,  "table",            "value",    "#333333"),
            OptionsInfo("table_font_color_light",             True,  "table",            "value",    "#FFFFFF"),
            OptionsInfo("table_border_top_include",          False,  "table",            "boolean",  True),
            OptionsInfo("table_border_top_style",             True,  "table",            "value",    "solid"),
            OptionsInfo("table_border_top_width",             True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_top_color",             True,  "table",            "value",    "#A8A8A8"),
            OptionsInfo("table_border_right_style",           True,  "table",            "value",    "none"),
            OptionsInfo("table_border_right_width",           True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_right_color",           True,  "table",            "value",    "#D3D3D3"),
            OptionsInfo("table_border_bottom_include",       False,  "table",            "boolean",  True),
            OptionsInfo("table_border_bottom_style",          True,  "table",            "value",    "solid"),
            OptionsInfo("table_border_bottom_width",          True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_bottom_color",          True,  "table",            "value",    "#A8A8A8"),
            OptionsInfo("table_border_left_style",            True,  "table",            "value",    "none"),
            OptionsInfo("table_border_left_width",            True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_left_color",            True,  "table",            "value",    "#D3D3D3"),
            OptionsInfo("heading_background_color",           True,  "heading",          "value",    None),
            OptionsInfo("heading_align",                      True,  "heading",          "value",    "center"),
            OptionsInfo("heading_title_font_size",            True,  "heading",          "px",       "125%"),
            OptionsInfo("heading_title_font_weight",          True,  "heading",          "value",    "initial"),
            OptionsInfo("heading_subtitle_font_size",         True,  "heading",          "px",       "85%"),
            OptionsInfo("heading_subtitle_font_weight",       True,  "heading",          "value",    "initial"),
            OptionsInfo("heading_padding",                    True,  "heading",          "px",       "4px"),
            OptionsInfo("heading_padding_horizontal",         True,  "heading",          "px",       "5px"),
            OptionsInfo("heading_border_bottom_style",        True,  "heading",          "value",    "solid"),
            OptionsInfo("heading_border_bottom_width",        True,  "heading",          "px",       "2px"),
            OptionsInfo("heading_border_bottom_color",        True,  "heading",          "value",    "#D3D3D3"),
            OptionsInfo("heading_border_lr_style",            True,  "heading",          "value",    "none"),
            OptionsInfo("heading_border_lr_width",            True,  "heading",          "px",       "1px"),
            OptionsInfo("heading_border_lr_color",            True,  "heading",          "value",    "#D3D3D3"),
            OptionsInfo("column_labels_background_color",     True,  "column_labels",    "value",    None),
            OptionsInfo("column_labels_font_size",            True,  "column_labels",    "px",       "100%"),
            OptionsInfo("column_labels_font_weight",          True,  "column_labels",    "value",    "normal"),
            OptionsInfo("column_labels_text_transform",       True,  "column_labels",    "value",    "inherit"),
            OptionsInfo("column_labels_padding",              True,  "column_labels",    "px",       "5px"),
            OptionsInfo("column_labels_padding_horizontal",   True,  "column_labels",    "px",       "5px"),
            OptionsInfo("column_labels_vlines_style",         True,  "table_body",       "value",    "none"),
            OptionsInfo("column_labels_vlines_width",         True,  "table_body",       "px",       "1px"),
            OptionsInfo("column_labels_vlines_color",         True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("column_labels_border_top_style",     True,  "column_labels",    "value",    "solid"),
            OptionsInfo("column_labels_border_top_width",     True,  "column_labels",    "px",       "2px"),
            OptionsInfo("column_labels_border_top_color",     True,  "column_labels",    "value",    "#D3D3D3"),
            OptionsInfo("column_labels_border_bottom_style",  True,  "column_labels",    "value",    "solid"),
            OptionsInfo("column_labels_border_bottom_width",  True,  "column_labels",    "px",       "2px"),
            OptionsInfo("column_labels_border_bottom_color",  True,  "column_labels",    "value",    "#D3D3D3"),
            OptionsInfo("column_labels_border_lr_style",      True,  "column_labels",    "value",    "none"),
            OptionsInfo("column_labels_border_lr_width",      True,  "column_labels",    "px",       "1px"),
            OptionsInfo("column_labels_border_lr_color",      True,  "column_labels",    "value",    "#D3D3D3"),
            OptionsInfo("column_labels_hidden",              False,  "column_labels",    "boolean",  False),
            OptionsInfo("row_group_background_color",         True,  "row_group",        "value",    None),
            OptionsInfo("row_group_font_size",                True,  "row_group",        "px",       "100%"),
            OptionsInfo("row_group_font_weight",              True,  "row_group",        "value",    "initial"),
            OptionsInfo("row_group_text_transform",           True,  "row_group",        "value",    "inherit"),
            OptionsInfo("row_group_padding",                  True,  "row_group",        "px",       "8px"),
            OptionsInfo("row_group_padding_horizontal",       True,  "row_group",        "px",       "5px"),
            OptionsInfo("row_group_border_top_style",         True,  "row_group",        "value",    "solid"),
            OptionsInfo("row_group_border_top_width",         True,  "row_group",        "px",       "2px"),
            OptionsInfo("row_group_border_top_color",         True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_border_right_style",       True,  "row_group",        "value",    "none"),
            OptionsInfo("row_group_border_right_width",       True,  "row_group",        "px",       "1px"),
            OptionsInfo("row_group_border_right_color",       True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_border_bottom_style",      True,  "row_group",        "value",    "solid"),
            OptionsInfo("row_group_border_bottom_width",      True,  "row_group",        "px",       "2px"),
            OptionsInfo("row_group_border_bottom_color",      True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_border_left_style",        True,  "row_group",        "value",    "none"),
            OptionsInfo("row_group_border_left_width",        True,  "row_group",        "px",       "1px"),
            OptionsInfo("row_group_border_left_color",        True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_default_label",           False,  "row_group",        "value",    None),
            OptionsInfo("row_group_as_column",               False,  "row_group",        "boolean",  False),
            OptionsInfo("table_body_hlines_style",            True,  "table_body",       "value",    "solid"),
            OptionsInfo("table_body_hlines_width",            True,  "table_body",       "px",       "1px"),
            OptionsInfo("table_body_hlines_color",            True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("table_body_vlines_style",            True,  "table_body",       "value",    "none"),
            OptionsInfo("table_body_vlines_width",            True,  "table_body",       "px",       "1px"),
            OptionsInfo("table_body_vlines_color",            True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("table_body_border_top_style",        True,  "table_body",       "value",    "solid"),
            OptionsInfo("table_body_border_top_width",        True,  "table_body",       "px",       "2px"),
            OptionsInfo("table_body_border_top_color",        True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("table_body_border_bottom_style",     True,  "table_body",       "value",    "solid"),
            OptionsInfo("table_body_border_bottom_width",     True,  "table_body",       "px",       "2px"),
            OptionsInfo("table_body_border_bottom_color",     True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("data_row_padding",                   True,  "data_row",         "px",       "8px"),
            OptionsInfo("data_row_padding_horizontal",        True,  "data_row",         "px",       "5px"),
            OptionsInfo("stub_background_color",              True,  "stub",             "value",    None),
            OptionsInfo("stub_font_size",                     True,  "stub",             "px",       "100%"),
            OptionsInfo("stub_font_weight",                   True,  "stub",             "value",    "initial"),
            OptionsInfo("stub_text_transform",                True,  "stub",             "value",    "inherit"),
            OptionsInfo("stub_border_style",                  True,  "stub",             "value",    "solid"),
            OptionsInfo("stub_border_width",                  True,  "stub",             "px",       "2px"),
            OptionsInfo("stub_border_color",                  True,  "stub",             "value",    "#D3D3D3"),
            OptionsInfo("stub_row_group_background_color",    True,  "stub",             "value",    None),
            OptionsInfo("stub_row_group_font_size",           True,  "stub",             "px",       "100%"),
            OptionsInfo("stub_row_group_font_weight",         True,  "stub",             "value",    "initial"),
            OptionsInfo("stub_row_group_text_transform",      True,  "stub",             "value",    "inherit"),
            OptionsInfo("stub_row_group_border_style",        True,  "stub",             "value",    "solid"),
            OptionsInfo("stub_row_group_border_width",        True,  "stub",             "px",       "2px"),
            OptionsInfo("stub_row_group_border_color",        True,  "stub",             "value",    "#D3D3D3"),
            OptionsInfo("summary_row_padding",                True,  "summary_row",      "px",       "8px"),
            OptionsInfo("summary_row_padding_horizontal",     True,  "summary_row",      "px",       "5px"),
            OptionsInfo("summary_row_background_color",       True,  "summary_row",      "value",    None),
            OptionsInfo("summary_row_text_transform",         True,  "summary_row",      "value",    "inherit"),
            OptionsInfo("summary_row_border_style",           True,  "summary_row",      "value",    "solid"),
            OptionsInfo("summary_row_border_width",           True,  "summary_row",      "px",       "2px"),
            OptionsInfo("summary_row_border_color",           True,  "summary_row",      "value",    "#D3D3D3"),
            OptionsInfo("grand_summary_row_padding",          True,  "grand_summary_row", "px",      "8px"),
            OptionsInfo("grand_summary_row_padding_horizontal",True, "grand_summary_row", "px",      "5px"),
            OptionsInfo("grand_summary_row_background_color", True,  "grand_summary_row", "value",   None),
            OptionsInfo("grand_summary_row_text_transform",   True,  "grand_summary_row", "value",   "inherit"),
            OptionsInfo("grand_summary_row_border_style",     True,  "grand_summary_row", "value",   "double"),
            OptionsInfo("grand_summary_row_border_width",     True,  "grand_summary_row", "px",      "6px"),
            OptionsInfo("grand_summary_row_border_color",     True,  "grand_summary_row", "value",   "#D3D3D3"),
            OptionsInfo("footnotes_font_size",                True,  "footnotes",        "px",       "90%"),
            OptionsInfo("footnotes_padding",                  True,  "footnotes",        "px",       "4px"),
            OptionsInfo("footnotes_padding_horizontal",       True,  "footnotes",        "px",       "5px"),
            OptionsInfo("footnotes_background_color",         True,  "footnotes",        "value",    None),
            OptionsInfo("footnotes_margin",                   True,  "footnotes",        "px",       "0px"),
            OptionsInfo("footnotes_border_bottom_style",      True,  "footnotes",        "value",    "none"),
            OptionsInfo("footnotes_border_bottom_width",      True,  "footnotes",        "px",       "2px"),
            OptionsInfo("footnotes_border_bottom_color",      True,  "footnotes",        "value",    "#D3D3D3"),
            OptionsInfo("footnotes_border_lr_style",          True,  "footnotes",        "value",    "none"),
            OptionsInfo("footnotes_border_lr_width",          True,  "footnotes",        "px",       "2px"),
            OptionsInfo("footnotes_border_lr_color",          True,  "footnotes",        "value",    "#D3D3D3"),
            OptionsInfo("footnotes_marks" ,                  False,  "footnotes",        "values",   "numbers"),
            OptionsInfo("footnotes_multiline",               False,  "footnotes",        "boolean",  True),
            OptionsInfo("footnotes_sep",                     False,  "footnotes",        "value",    " "),
            OptionsInfo("source_notes_padding",               True,  "source_notes",     "px",       "4px"),
            OptionsInfo("source_notes_padding_horizontal",    True,  "source_notes",     "px",       "5px"),
            OptionsInfo("source_notes_background_color",      True,  "source_notes",     "value",    None),
            OptionsInfo("source_notes_font_size",             True,  "source_notes",     "px",       "90%"),
            OptionsInfo("source_notes_border_bottom_style",   True,  "source_notes",     "value",    "none"),
            OptionsInfo("source_notes_border_bottom_width",   True,  "source_notes",     "px",       "2px"),
            OptionsInfo("source_notes_border_bottom_color",   True,  "source_notes",     "value",    "#D3D3D3"),
            OptionsInfo("source_notes_border_lr_style",       True,  "source_notes",     "value",    "none"),
            OptionsInfo("source_notes_border_lr_width",       True,  "source_notes",     "px",       "2px"),
            OptionsInfo("source_notes_border_lr_color",       True,  "source_notes",     "value",    "#D3D3D3"),
            OptionsInfo("source_notes_multiline",            False,  "source_notes",     "boolean",  True),
            OptionsInfo("source_notes_sep",                  False,  "source_notes",     "value",    " "),
            OptionsInfo("row_striping_background_color",      True,  "row",              "value",    "rgba(128,128,128,0.05)"),
            OptionsInfo("row_striping_include_stub",         False,  "row",              "boolean",  False),
            OptionsInfo("row_striping_include_table_body",   False,  "row",              "boolean",  False),
            OptionsInfo("container_width",                   False,  "container",        "px",       "auto"),
            OptionsInfo("container_height",                  False,  "container",        "px",       "auto"),
            OptionsInfo("container_padding_x",               False,  "container",        "px",       "0px"),
            OptionsInfo("container_padding_y",               False,  "container",        "px",       "10px"),
            OptionsInfo("container_overflow_x",              False,  "container",        "overflow", "auto"),
            OptionsInfo("container_overflow_y",              False,  "container",        "overflow", "auto"),
            OptionsInfo("page_orientation",                  False,  "page",             "value",    "portrait"),
            OptionsInfo("page_numbering",                    False,  "page",             "boolean",  False),
            OptionsInfo("page_header_use_tbl_headings",      False,  "page",             "boolean",  False),
            OptionsInfo("page_footer_use_tbl_notes",         False,  "page",             "boolean",  False),
            OptionsInfo("page_width",                        False,  "page",             "value",    "8.5in"),
            OptionsInfo("page_height",                       False,  "page",             "value",    "11.0in"),
            OptionsInfo("page_margin_left",                  False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_right",                 False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_top",                   False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_bottom",                False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_header_height",                False,  "page",             "value",    "0.5in"),
            OptionsInfo("page_footer_height",                False,  "page",             "value",    "0.5in"),
            OptionsInfo("quarto_disable_processing",         False,  "quarto",           "logical",  False),
            OptionsInfo("quarto_use_bootstrap",              False,  "quarto",           "logical",  False),
        ])
# fmt: on

    def _get_all_options_keys(self) -> List[Union[str, None]]:
        return [x.parameter for x in self._options.values()]

    def __getattr__(self, __name: str) -> OptionsInfo:
        return self._options[__name]
        # use this like
        #
        # options = Options()
        # options.foo.value = "bar"
        # print(options.foo.type)

    #def _get_option_type(self, option: str) -> Union[Any, List[str]]:
    #    return self._options[option].type

    def _get_option_value(self, option: str) -> Union[Any, List[str]]:
        return self._options[option].value

    def _set_option_value(self, option: str, value: Any):
       self._options[option].value = value
       return self
