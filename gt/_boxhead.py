from __future__ import annotations

from typing import Optional, List
from enum import Enum, auto
import pandas as pd

from ._base_api import BaseAPI
from ._tbl_data import TblData, get_column_names

from ._utils import _assert_list_is_subset



class BoxheadAPI(BaseAPI):
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
