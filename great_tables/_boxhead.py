from __future__ import annotations

import pandas as pd
from typing import Optional, Any
from ._gt_data import GTData

from ._utils import _assert_list_is_subset


class BoxheadAPI:
    def cols_label(self, **kwargs: Any) -> GTData:
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
        **kwargs : str
            The column names and new labels. The column names are provided as keyword arguments
            and the new labels are provided as the values for those keyword arguments. For example,
            `cols_label(col1="Column 1", col2="Column 2")` would relabel columns `col1`
            and `col2` with the labels `"Column 1"` and `"Column 2"`, respectively.

        Returns
        -------
        GTData
            The GTData object is returned.

        Examples
        --------
        Let's use a portion of the `countrypops` dataset to create a table. We can relabel all the
        table's columns with the `cols_label()` method to improve its presentation. In this simple
        case we are supplying the name of the column as the key, and the label text as the value.

        ```{python}
        import great_tables as gt

        countrypops_mini = gt.countrypops.loc[gt.countrypops[\"country_name\"] == \"Uganda\"][
            [\"country_name\", \"year\", \"population\"]
        ].tail(5)

        (
            gt.GT(countrypops_mini)
            .cols_label(
                country_name=\"Name\",
                year=\"Year\",
                population=\"Population\"
            )
        )
        ```

        We can also use Markdown formatting for the column labels. In this example, we'll use
        `gt.md("*Population*")` to make the label italicized.

        ```{python}
        (
            gt.GT(countrypops_mini)
            .cols_label(
                country_name=\"Name\",
                year=\"Year\",
                population=gt.md(\"*Population*\")
            )
        )
        ```
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
        _assert_list_is_subset(mod_columns, set_list=column_names)

        for i in range(len(kwargs)):
            self._boxhead._set_column_label(column=mod_columns[i], label=new_labels[i])

        return self

    def cols_align(self, align: str = "left", columns: Optional[str] = None) -> GTData:
        """
        Set the alignment of one or more columns.

        The `cols_align()` method sets the alignment of one or more columns. The `align` argument
        can be set to one of `"left"`, `"center"`, or `"right"` and the `columns` argument can be
        used to specify which columns to apply the alignment to. If `columns` is not specified, the
        alignment is applied to all columns.

        Parameters
        ----------
        align : str
            The alignment to apply. Must be one of `"left"`, `"center"`, or `"right"`.
        columns : Union[str, List[str], None]
            The columns to target. Can either be a single column name or a series of column names
            provided in a list. If `None`, the alignment is applied to all columns.

        Returns
        -------
        GTData
            The GTData object is returned.

        Examples
        --------
        Let's use the `countrypops` to create a small table. We can change the alignment of the
        `population` column with `cols_align()`. In this example, the column label and body cells of
        `population` will be aligned to the left.

        ```{python}
        import great_tables as gt

        countrypops_mini = gt.countrypops.loc[gt.countrypops[\"country_name\"] == \"San Marino\"][
            [\"country_name\", \"year\", \"population\"]
        ].tail(5)

        (
            gt.GT(countrypops_mini, rowname_col=\"year\", groupname_col=\"country_name\")
            .cols_align(align=\"left\", columns=\"population\")
        )
        ```

        """

        # Throw if `align` is not one of the three allowed values
        if align not in ["left", "center", "right"]:
            raise ValueError("Align must be one of 'left', 'center', or 'right'.")

        # Get the full list of column names for the data
        column_names = self._boxhead._get_columns()

        # Upgrade `columns` to a list if `columns` is a string and not None
        if isinstance(columns, str):
            columns = [columns]
            _assert_list_is_subset(columns, set_list=column_names)
        elif columns is None:
            columns = column_names

        # Set the alignment for each column
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
