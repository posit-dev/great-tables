from __future__ import annotations

from dataclasses import replace
from typing import TYPE_CHECKING, Literal, Union

from ._gt_data import Stub
from ._locations import RowSelectExpr, resolve_rows_i

if TYPE_CHECKING:
    from ._types import GTSelf


def tab_stub_indent(
    self: GTSelf,
    rows: RowSelectExpr,
    indent: Union[int, Literal["increase", "decrease"]] = "increase",
) -> GTSelf:
    """
    Control indentation of row labels in the stub.

    Indentation of row labels is an effective way to establish visual hierarchy in a table stub.
    `tab_stub_indent()` allows for fine-grained control over row label indentation in the stub.
    You can use an explicit integer indentation level (between `0` and `5`), or use a keyword
    directive: `"increase"` (the default) or `"decrease"`.

    Parameters
    ----------
    rows
        The rows to target for the indentation change. We can supply a list of row indices, a
        single row index integer, or a callable that takes the table data and returns a boolean
        Series. When targeting rows by name, provide a list of row label strings.
    indent
        An indentation directive or explicit integer level. The keyword `"increase"` (the default)
        increments the indentation level by `1`; `"decrease"` decrements it by `1`. The minimum
        indentation level is `0` (no indentation) and the maximum is `5`. An integer value
        directly sets the indentation level (clamped to the `0`–`5` range).

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's use a subset of the `exibble` dataset to create a gt table with row groups and row
    labels. We'll use `tab_stub_indent()` to add indentation to all the row labels in the stub.

    ```{python}
    from great_tables import GT
    from great_tables.data import exibble

    exibble_mini = exibble[["num", "char", "row", "group"]].head(8)

    (
        GT(exibble_mini, rowname_col="row", groupname_col="group")
        .tab_stub_indent(rows=True, indent=2)
    )
    ```

    Here's a more advanced example using the `constants` dataset. We filter for three groups of
    physical constants and rename the sub-entries to start with `"..."` so it's clear they belong
    to a parent constant. Then `tab_stub_indent()` targets those sub-rows (via a Polars expression)
    and indents them by 4 levels.

    ```{python}
    from great_tables import GT, stub
    from great_tables.data import constants
    import polars as pl

    constants_mini = (
        pl.from_pandas(constants)
        .select(["name", "value", "uncert", "units"])
        .filter(
            pl.col("name").str.starts_with("atomic mass constant")
            | pl.col("name").str.starts_with("Rydberg constant")
            | pl.col("name").str.starts_with("Bohr magneton")
        )
        .with_columns(
            name=pl.when(
                pl.col("name").str.contains("constant ")
                | pl.col("name").str.contains("magneton ")
            )
            .then(pl.col("name").str.replace(r".*?(?:constant |magneton )", "..."))
            .otherwise(pl.col("name"))
        )
    )

    (
        GT(constants_mini, rowname_col="name")
        .tab_stubhead(label="Physical Constant")
        .tab_stub_indent(
            rows=pl.col("name").str.starts_with("..."),
            indent=4,
        )
        .fmt_scientific(columns=["value", "uncert"])
        .fmt_units(columns="units")
        .cols_label(value="Value", uncert="Uncertainty", units="Units")
        .cols_width(cases={stub: "250px", "value": "150px", "uncert": "150px", "units": "80px"})
    )
    ```
    """

    row_res = resolve_rows_i(self, rows)
    row_positions = [ii for _, ii in row_res]

    if isinstance(indent, str):
        position_set = set(row_positions)
        new_rows = []
        for ii, row in enumerate(self._stub.rows):
            if ii in position_set:
                if indent == "increase":
                    new_indent = min(5, row.indent + 1)
                else:  # "decrease"
                    new_indent = max(0, row.indent - 1)
                new_rows.append(replace(row, indent=new_indent))
            else:
                new_rows.append(row)
        new_stub = Stub(new_rows, self._stub.group_rows)
    else:
        indent_val = max(0, min(5, int(indent)))
        new_stub = self._stub.set_row_indent(row_positions, indent_val)

    return self._replace(_stub=new_stub)
