from __future__ import annotations

import pandas as pd
from typing import Optional
from ._gt_data import GTData

from ._utils import _assert_list_is_subset


class BoxheadAPI:
    def cols_label(self, **kwargs: str):
        """
        Relabel one or more columns.

        Column labels can be modified from their default values (the names of the columns from the
        input table data). When you create a table object using `gt.GT()`, column names effectively
        become the column labels. While this serves as a good first approximation, column names
        aren't often appealing as column labels in an output table. The `cols_label()` method
        provides the flexibility to relabel one or more columns and we even have the option to use
        the `md()` or `html()` helpers for rendering column labels from Markdown or using HTML.

        It's important to note that while columns can be freely relabeled, we continue to refer to
        columns by their names for targeting purposes. Column names in the input data table must be
        unique whereas column labels in **great_tables** have no requirement for uniqueness (which
        is useful for labeling columns as, say, measurement units that may be repeated several
        times---usually under different spanner labels). Thus, we can still easily distinguish
        between columns in other method calls (e.g., in all of the `fmt*()` methods) even though we
        may lose distinguishability in column labels once they have been relabeled.

        Parameters
        ----------
        columns : Union[str, List[str], None]
            The columns to target. Can either be a single column name or a series of column names
            provided in a list.

        **kwargs : str
            The column names and new labels. The column names are provided as keyword arguments
            and the new labels are provided as the values for those keyword arguments. For example,
            `cols_label(col1="Column 1", col2="Column 2")` would relabel columns `col1`
            and `col2` with the labels `"Column 1"` and `"Column 2"`, respectively.

        Returns
        -------
        GTData
            The GTData object is returned.
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

    def cols_align(self, align: str = "left", columns: Optional[str] = None):
        """
        Set the alignment of one or more columns.

        The `cols_align()` method sets the alignment of one or more columns. The `align` argument
        can be set to one of `"left"`, `"center"`, or `"right"` and the `columns` argument can be
        used to specify which columns to apply the alignment to. If `columns` is not specified, the
        alignment is applied to all columns.

        Parameters
        ----------
        columns : Union[str, List[str], None]
            The columns to target. Can either be a single column name or a series of column names
            provided in a list.

        align : str
            The alignment to apply. Must be one of `"left"`, `"center"`, or `"right"`.

        Returns
        -------
        GTData
            The GTData object is returned.
        """

        # Get the full list of column names for the data
        column_names = self._boxhead._get_columns()

        # Stop function if any of the column names specified are not in `cols_labels`
        # msg: "All column names provided must exist in the input `.data` table."
        if columns is not None:
            _assert_list_is_subset(columns, column_names)

        if columns is None:
            columns = column_names

        for column in columns:
            self._boxhead._set_column_align(column=column, align=align)

        return self

    def _print_boxhead(self) -> pd.DataFrame:
        boxhead_list = list(
            zip(
                [x.var for x in self._boxhead],
                [x.visible for x in self._boxhead],
                [x.column_label for x in self._boxhead],
            )
        )
        return pd.DataFrame(boxhead_list, columns=["var", "visible", "column_label"])
