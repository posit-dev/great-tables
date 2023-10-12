from typing import Optional, List
from enum import Enum, auto
import pandas as pd

from ._base_api import BaseAPI
from ._tbl_data import TblData, get_column_names

from ._utils import _assert_list_is_subset


class ColumnAlignment(Enum):
    Left = auto()
    Center = auto()
    Right = auto()
    Justify = auto()


class ColInfo:
    # TODO: Make var readonly
    var: str
    visible: bool
    column_label: str
    column_align: Optional[ColumnAlignment]
    column_width: Optional[str]

    # The components of the boxhead are:
    # `var` (obtained from column names)
    # `column_label` (obtained from column names)
    # `visible` = True
    # `column_align` = None
    # `column_width` = None

    def __init__(
        self,
        var: str,
        visible: bool = True,
        column_label: Optional[str] = None,
        column_align: Optional[ColumnAlignment] = None,
        column_width: Optional[str] = None,
    ):
        self.var = var
        self.visible = visible
        self.column_label = column_label or var
        self.column_align = column_align
        self.column_width = column_width


class Boxhead:
    _boxhead: List[ColInfo]

    def __init__(self, data: TblData):

        # Obtain the column names from the data and initialize the
        # `_boxhead` from that
        column_names = get_column_names(data)
        self._boxhead = [ColInfo(col) for col in column_names]

    # Get a list of columns
    def _get_columns(self) -> List[str]:
        return [x.var for x in self._boxhead]

    # Get a list of column labels
    def _get_column_labels(self) -> List[str]:
        return [x.column_label for x in self._boxhead]

    # Set column label
    def _set_column_label(self, column: str, label: str):

        for x in self._boxhead:
            if x.var == column:
                x.column_label = label

        return self

    # Get a list of visible columns
    def _get_visible_columns(self) -> List[str]:

        visible_columns = [x.var for x in self._boxhead if x.visible is True]
        return visible_columns

    # Get the number of columns for the visible (not hidden) data; this
    # excludes the number of columns required for the table stub
    def _get_number_of_visible_data_columns(self) -> int:
        return len(self._get_visible_columns())

    # Obtain the number of visible columns in the built table; this should
    # account for the size of the stub in the final, built table
    def _get_effective_number_of_columns(self) -> int:

        n_data_cols = self._get_number_of_visible_data_columns()

        # TODO: Once the stub is defined in the package, we need to account
        # for the width of the stub at build time to fully obtain the number
        # of visible columns in the built table
        # n_data_cols = n_data_cols + len(get_stub_layout(data=data))

        return n_data_cols


class BoxheadAPI(BaseAPI):
    _boxhead: Boxhead

    def __init__(self):
        self._boxhead = Boxhead(self._get_tbl_data())

    def cols_label(self, **kwargs: str):
        """
        Relabel one or more columns.

        Column labels can be modified from their default values (the names of the
        columns from the input table data). When you create a gt table object
        using `gt.GT()`, column names effectively become the column labels. While
        this serves as a good first approximation, column names aren't often
        appealing as column labels in a gt output table. The `cols_label()` method
        provides the flexibility to relabel one or more columns and we even have the
        option to use the `md()` or `html()` helper functions for rendering column
        labels from Markdown or using HTML.

        It's important to note that while columns can be freely relabeled, we
        continue to refer to columns by their original column names. Column names in
        a tibble or data frame must be unique whereas column labels in gt have
        no requirement for uniqueness (which is useful for labeling columns as, say,
        measurement units that may be repeated several times---usually under
        different spanner column labels). Thus, we can still easily distinguish
        between columns in other gt method calls (e.g., in all of the `fmt*()`
        methods) even though we may lose distinguishability in column labels once
        they have been relabeled.

        Returns
        -------
        GT
            Result of the table operation.
        """

        # If nothing is provided, return `data` unchanged
        if len(kwargs) == 0:
            return self

        mod_columns = list(kwargs.keys())
        new_labels = list(kwargs.values())

        # Get the full list of column names for the data
        column_names = self._boxhead._get_columns()

        # Stop function if any of the column names specified are not in `cols_labels`
        # msg: "All column names provided must exist in the input `.data` table."
        _assert_list_is_subset(mod_columns, column_names)

        for i in range(len(kwargs)):
            self._boxhead._set_column_label(column=mod_columns[i], label=new_labels[i])

        return self

    def _print_boxhead(self) -> pd.DataFrame:
        boxhead_list = list(
            zip(
                [x.var for x in self._boxhead._boxhead],
                [x.visible for x in self._boxhead._boxhead],
                [x.column_label for x in self._boxhead._boxhead],
            )
        )
        return pd.DataFrame(boxhead_list, columns=["var", "visible", "column_label"])
