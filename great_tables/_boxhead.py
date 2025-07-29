from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from ._locations import LocColumnLabels, resolve_cols_c
from ._styles import CellStyleCss
from ._tbl_data import SelectExpr
from ._text import BaseText
from ._utils import _assert_list_is_subset

if TYPE_CHECKING:
    from ._types import GTSelf


def cols_label(
    self: GTSelf, cases: dict[str, str | BaseText] | None = None, **kwargs: str | BaseText
) -> GTSelf:
    """
    Relabel one or more columns.

    There are three important pieces to labelling:

    * Each argument has the form: {name in data} = {new label}.
    * Multiple columns may be given the same label.
    * Labels may use curly braces to apply special formatting, called unit notation.
      For example, "area ({{ft^2}})" would appear as "area (ft²)".

    See [`define_units()`](`great_tables.define_units`) for details on unit notation.

    Parameters
    ----------
    cases
        A dictionary where the keys are column names and the values are the labels. Labels may use
        [`md()`](`great_tables.md`) or [`html()`](`great_tables.html`) helpers for formatting.

    **kwargs
        Keyword arguments to specify column labels. Each keyword corresponds to a column name, with
        its value indicating the new label.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Notes
    -----
    GT always selects columns using their name in the underlying data. This means that a column's
    label is purely for final presentation.

    Examples
    --------

    The example below relabels columns from the `countrypops` data to start with uppercase.

    ```{python}
    from great_tables import GT
    from great_tables.data import countrypops

    countrypops_mini = countrypops.loc[countrypops["country_name"] == "Uganda"][
        ["country_name", "year", "population"]
    ].tail(5)

    (
        GT(countrypops_mini)
        .cols_label(
            country_name="Country Name",
            year="Year",
            population="Population"
        )
    )
    ```

    Note that we supplied the name of the column as the key, and the new label as the value.

    We can also use Markdown formatting for the column labels. In this example, we'll use
    `md("*Population*")` to make the label italicized.

    ```{python}
    from great_tables import GT, md
    from great_tables.data import countrypops

    (
        GT(countrypops_mini)
        .cols_label(
            country_name="Name",
            year="Year",
            population=md("*Population*")
        )
    )
    ```

    We can also use unit notation to format the column labels. In this example, we'll use
    `{{cm^3 molecules^-1 s^-1}}` for part of the label for the `OH_k298` column.

    ```{python}
    from great_tables import GT
    from great_tables.data import reactions
    import polars as pl

    reactions_mini = (
        pl.from_pandas(reactions)
        .filter(pl.col("cmpd_type") == "mercaptan")
        .select(["cmpd_name", "OH_k298"])
    )

    (
        GT(reactions_mini)
        .fmt_scientific("OH_k298")
        .sub_missing()
        .cols_label(
            cmpd_name="Compound Name",
            OH_k298="OH, {{cm^3 molecules^-1 s^-1}}",
        )
    )
    ```
    """
    from great_tables._helpers import UnitStr

    cases = cases if cases is not None else {}
    new_cases = cases | kwargs

    # If nothing is provided, return `data` unchanged
    if not new_cases:
        return self

    # Get the full list of column names for the data
    column_names = self._boxhead._get_columns()
    mod_columns = list(new_cases.keys())

    # Stop function if any of the column names specified are not in `cols_labels`
    # msg: "All column names provided must exist in the input `.data` table."
    _assert_list_is_subset(mod_columns, set_list=column_names)

    # Handle units syntax in labels (e.g., "Density ({{ppl / mi^2}})")
    new_kwargs: dict[str, UnitStr | str | BaseText] = {}

    for k, v in new_cases.items():
        if isinstance(v, str):
            unitstr_v = UnitStr.from_str(v)

            if len(unitstr_v.units_str) == 1 and isinstance(unitstr_v.units_str[0], str):
                new_kwargs[k] = unitstr_v.units_str[0]
            else:
                new_kwargs[k] = unitstr_v

        elif isinstance(v, BaseText):
            new_kwargs[k] = v

        else:
            raise ValueError(
                "Column labels must be strings or BaseText objects. Use `md()` or `html()` for formatting."
            )

    boxhead = self._boxhead._set_column_labels(new_kwargs)

    return self._replace(_boxhead=boxhead)


def cols_align(self: GTSelf, align: str = "left", columns: SelectExpr = None) -> GTSelf:
    """
    Set the alignment of one or more columns.

    The `cols_align()` method sets the alignment of one or more columns. The `align` argument
    can be set to one of `"left"`, `"center"`, or `"right"` and the `columns` argument can be
    used to specify which columns to apply the alignment to. If `columns` is not specified, the
    alignment is applied to all columns.

    Parameters
    ----------
    align
        The alignment to apply. Must be one of `"left"`, `"center"`, or `"right"`.
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list. If `None`, the alignment is applied to all columns.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's use the `countrypops` to create a small table. We can change the alignment of the
    `population` column with `cols_align()`. In this example, the column label and body cells of
    `population` will be aligned to the left.

    ```{python}
    from great_tables import GT
    from great_tables.data import countrypops

    countrypops_mini = countrypops.loc[countrypops["country_name"] == "San Marino"][
        ["country_name", "year", "population"]
    ].tail(5)

    (
        GT(countrypops_mini, rowname_col="year", groupname_col="country_name")
        .cols_align(align="left", columns="population")
    )
    ```

    """

    # Throw if `align` is not one of the three allowed values
    if align not in ("left", "center", "right"):
        raise ValueError("Align must be one of 'left', 'center', or 'right'.")

    # Get the full list of column names for the data
    column_names = self._boxhead._get_columns()

    # Upgrade `columns` to a list if `columns` is a string and not None
    if isinstance(columns, str):
        columns = [columns]
        _assert_list_is_subset(columns, set_list=column_names)
    elif columns is None:
        columns = column_names

    sel_cols = resolve_cols_c(data=self, expr=columns)

    # Set the alignment for each column
    return self._replace(_boxhead=self._boxhead._set_column_aligns(sel_cols, align=align))


def cols_label_rotate(
    self: GTSelf,
    columns: SelectExpr = None,
    dir: Literal["sideways-lr", "sideways-rl", "vertical-lr"] = "sideways-lr",
    align: Literal["left", "center", "right"] | None = None,
    padding: int = 8,
) -> GTSelf:
    """
    Rotate the column label for one or more columns.

    The `cols_label_rotate()` method sets the orientation of the column label text to make it flow
    vertically. The `dir` argument can be set to one of `"sideways-lr"`, `"sideways-rl"`, or
    `"vertical-lr"`, and the `columns` argument can be used to specify which columns to apply the
    alignment to. If `columns` is not specified, the alignment is applied to all columns.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list. If `None`, the alignment is applied to all columns.
    dir
        A string that gives the direction of the text. Options: `"sideways-lr"`, `"sideways-rl"`,
        `"vertical-lr"`. See note for information on text layout.
    align
        The alignment to apply. Must be one of `"left"`, `"center"`, `"right"`, or `"none"`. If text
        is laid out vertically, this affects alignment along the vertical axis.
    padding
        The vertical padding to apply to the column labels.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    The example below rotates column labels such that the text is set to the left.

    ```{python}
    from great_tables import GT, style, loc, exibble

    exibble_sm = exibble[["num", "fctr", "row", "group"]]

    (
        GT(exibble_sm, rowname_col="row", groupname_col="group")
        .cols_label_rotate(columns=["num", "fctr"])
    )
    ```

    Other styles you provide won't override the column label rotation directives. Here we set the
    text to the right.

    ```{python}
    (
        GT(exibble_sm, rowname_col="row", groupname_col="group")
        .cols_label_rotate(columns=["num", "fctr"], dir="vertical-lr")
        .tab_style(style=style.text(weight="bold"), locations=loc.column_labels(["fctr"]))
    )
    ```

    Labels that are restricted by the height of the stub head will wrap horizontally.

    ```{python}
    (
        GT(exibble_sm, rowname_col="row", groupname_col="group")
        .cols_label({"fctr": "A longer description of the values in the column below"})
        .cols_label_rotate(columns=["num", "fctr"], dir="sideways-lr")
        .tab_style(
            style=[style.text(weight="bold"), style.css(rule="height: 200px;")],
            locations=loc.column_labels(["fctr"])
        )
    )
    ```

    Note
    --------
    The `dir` parameter uses the following keywords to alter the direction of the column label text.

    ##### `"sideways-lr"`

    For ltr scripts, content flows vertically from bottom to top. For rtl scripts, content flows
    vertically from top to bottom. Characters are set sideways toward the left. Overflow lines are
    appended to the right.

    ##### `"sideways-rl"`

    For ltr scripts, content flows vertically from top to bottom. For rtl scripts, content flows
    vertically from bottom to top. Characters are set sideways toward the right. Overflow lines are
    appended to the left.

    ##### `"vertical-lr"`

    Identical to `"sideways-rl"`, but overflow lines are appended to the right.

    """
    # Throw if `align` is not one of the four allowed values
    if align not in (None, "left", "center", "right"):
        raise ValueError("Align must be one of `None`, 'left', 'center', or 'right'.")

    # Throw if `dir` is not one of the three allowed values
    if dir not in ("sideways-lr", "sideways-rl", "vertical-lr"):
        raise ValueError("Dir must be one of 'sideways-lr', 'sideways-rl', or 'vertical-lr'.")

    # If user doesn't set an align value then align to the bottom, which is left in the case of
    # "sideways-lr" and right in all other cases
    if not align:
        if dir == "sideways-lr":
            align = "left"
        else:
            align = "right"

    res = self.tab_style(
        style=CellStyleCss(
            f"writing-mode: {dir}; vertical-align: middle; text-align: {align}; padding: {padding}px 0px;"
        ),
        locations=LocColumnLabels(columns=columns),
    )
    return res
