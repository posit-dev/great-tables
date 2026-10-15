from __future__ import annotations

import re
from functools import partial
from typing import Callable, TYPE_CHECKING, Literal

from ._locations import LocBody, LocColumnLabels, resolve_cols_c
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


def cols_label_with(
    self: GTSelf, columns: SelectExpr = None, fn: Callable[[str], str] | None = None
) -> GTSelf:
    """
    Relabel one or more columns using a function.

    The `cols_label_with()` function allows for modification of column labels through a supplied
    function. By default, the function will be invoked on all column labels but this can be limited
    to a subset via the `columns` parameter.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    fn
        A function that accepts a column name as input and returns a label as output.

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
    Let's use a subset of the `sp500` dataset to create a gt table.
    ```{python}
    from great_tables import GT, md
    from great_tables.data import sp500

    gt = GT(sp500.head())
    gt
    ```

    We can pass `str.upper` to the `fn` parameter to convert all column labels to uppercase.
    ```{python}
    gt.cols_label_with(fn=str.upper)
    ```

    One useful use case is using `md()`, provided by **Great Tables**, to format column labels.
    For example, the following code demonstrates how to make the `date` and `adj_close` column labels
    bold using markdown syntax.
    ```{python}
    gt.cols_label_with(["date", "adj_close"], lambda x: md(f"**{x}**"))
    ```

    """
    if fn is None:
        raise ValueError("Must provide the `fn=` parameter to use `cols_label_with()`.")

    # Get the full list of column names for the data
    column_names = self._boxhead._get_columns()

    if isinstance(columns, str):
        columns = [columns]
    if isinstance(columns, list):
        _assert_list_is_subset(
            [col for col in columns if isinstance(col, str)], set_list=column_names
        )
    elif columns is None:
        columns = column_names

    sel_cols = resolve_cols_c(data=self, expr=columns)

    new_cases = {col: fn(col) for col in sel_cols}

    boxhead = self._boxhead._set_column_labels(new_cases)

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
    if isinstance(columns, list):
        _assert_list_is_subset(
            [col for col in columns if isinstance(col, str)], set_list=column_names
        )
    elif columns is None:
        columns = column_names

    sel_cols = resolve_cols_c(data=self, expr=columns, excl_stub=False)

    # Set the alignment for each column
    return self._replace(_boxhead=self._boxhead._set_column_aligns(sel_cols, align=align))


def cols_align_decimal(
    self: GTSelf,
    columns: SelectExpr = None,
    dec_mark: str = ".",
    locale: str | None = None,
) -> GTSelf:
    """
    Align all numeric values in a column along the decimal mark.

    For numeric columns that contain values with more than one decimal place, it can be helpful to
    align them on the decimal mark so they are easier to scan and compare. The
    `cols_align_decimal()` method does this by padding the formatted values with figure spaces
    (which are as wide as a digit) so that the decimal marks line up, and right-aligning the
    columns. This happens after formatting, so it works with values formatted by the `fmt_*()`
    methods, including ones with a `%` or other suffix. Only numeric columns are aligned, any
    other columns that are targeted are left unchanged.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list. If `None`, all numeric columns are targeted.
    dec_mark
        The character used as the decimal mark in the formatted values. This is ignored if a
        `locale` is supplied.
    locale
        An optional locale identifier that can be used to obtain the decimal mark. If not set,
        the locale set in `GT(locale=...)`, if any, is used.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's put some numbers with different numbers of decimal places in a table, format them with
    `fmt_number()` and align them on the decimal mark.

    ```{python}
    import polars as pl
    from great_tables import GT

    df = pl.DataFrame({"num": [1.2, -33.52, 9023.2, -283.527, None, 0.401, 41.0]})

    (
        GT(df)
        .fmt_number(columns="num", decimals=3, drop_trailing_zeros=True)
        .cols_align_decimal()
    )
    ```
    """
    from ._formats import _get_locale_dec_mark, _resolve_locale
    from ._gt_data import TextTransformInfo
    from ._ihtml import _is_numeric_dtype

    locale = _resolve_locale(self, locale=locale)
    dec_mark = _get_locale_dec_mark(default=dec_mark, locale=locale)

    if columns is None:
        columns = self._boxhead._get_columns()

    # Only columns that are numeric in the input data are aligned
    numeric_cols = [
        col
        for col in resolve_cols_c(data=self, expr=columns)
        if _is_numeric_dtype(self._tbl_data, col)
    ]

    if not numeric_cols:
        return self

    res = cols_align(self, align="right", columns=numeric_cols)

    # A `per_column` transform also receives the output context (the padding differs in LaTeX)
    transform = TextTransformInfo(
        loc=LocBody(columns=numeric_cols),
        fn=partial(_align_to_char, align_at=dec_mark),
        per_column=True,
    )
    return res._replace(_transforms=res._transforms + [transform])


FIGURE_SPACE = "\u2007"
NO_BREAK_SPACE = "\u00a0"


def _align_to_char(values: list[str], align_at: str = ".", context: str = "html") -> list[str]:
    """Pad the formatted values of a column with figure spaces so that they line up on
    `align_at`. This follows `align_to_char()` in the R gt package.

    In LaTeX, the padding is written with `\\hphantom{}` (Unicode spaces such as the figure space
    aren't available in pdfLaTeX), and the values' escape sequences (e.g., `\\%`) are measured as
    the single character they print.
    """

    if context == "latex":
        return _align_to_char_latex(values, align_at=align_at)

    def _can_align(value: str) -> bool:
        return value != "NA" and (align_at in value or re.search(r"[0-9]", value) is not None)

    idx = [i for i, value in enumerate(values) if _can_align(value)]
    if not idx:
        return list(values)

    to_align = [values[i] for i in idx]

    lhs: list[str] = []
    rhs: list[str] = []
    for value in to_align:
        pieces = value.split(align_at)
        # Drop the empty piece left by a trailing decimal mark (e.g. "41.")
        if len(pieces) > 1 and pieces[-1] == "":
            pieces = pieces[:-1]
        lhs.append(pieces[0])
        rhs.append(align_at.join(pieces[1:]))

    max_lhs = max(len(x) for x in lhs)
    max_rhs = max(len(x) for x in rhs)
    lhs_pieces = [FIGURE_SPACE * (max_lhs - len(x)) + x for x in lhs]
    rhs_pieces = [x + FIGURE_SPACE * (max_rhs - len(x)) for x in rhs]

    # A suffix after the integer part of a value without a decimal mark (e.g. "41%" or "(41)") is
    # moved after the decimal mark, where it takes the place of padding
    for i, lhs_piece in enumerate(lhs_pieces):
        suffix = re.search(r"[^0-9]+$", lhs_piece)
        if suffix:
            extracted = suffix.group(0)
            lhs_pieces[i] = lhs_piece.replace(extracted, "")
            rhs_pieces[i] = re.sub(
                re.escape(FIGURE_SPACE * len(extracted)) + "$", "", extracted + rhs_pieces[i]
            )

    aligned = [left + align_at + right for left, right in zip(lhs_pieces, rhs_pieces)]
    has_parens = [re.search(r"\(.+?\)", x) is not None for x in aligned]
    no_dec_mark = [len(r) == 0 and align_at not in v for r, v in zip(rhs, to_align)]

    if any(align_at in value for value in to_align):
        # Values without a decimal mark get a space in its place
        aligned = [
            x.replace(align_at, " ", 1) if no_mark else x
            for x, no_mark in zip(aligned, no_dec_mark)
        ]
        aligned = [x + NO_BREAK_SPACE if parens else x for x, parens in zip(aligned, has_parens)]
    else:
        aligned = [
            x.replace(align_at, "", 1) if no_mark else x for x, no_mark in zip(aligned, no_dec_mark)
        ]
        aligned = [x if parens else x + NO_BREAK_SPACE for x, parens in zip(aligned, has_parens)]

    out = list(values)
    for i, x in zip(idx, aligned):
        out[i] = x
    return out


# A placeholder for the space that takes the place of a missing decimal mark in LaTeX, so that it
# can be written as a phantom decimal mark (a space isn't as wide)
_MISSING_MARK = "\ue0ff"


def _align_to_char_latex(values: list[str], align_at: str) -> list[str]:
    """`_align_to_char()` for LaTeX output (see there)."""

    from ._text import _latex_escape

    # Each escape sequence (e.g., `\%`, `\textless{}`) prints a single character, so it's
    # replaced by a single placeholder character while the values are aligned
    sequences: list[str] = []

    def encode(value: str) -> str:
        def placeholder(match: re.Match[str]) -> str:
            if match.group(0) not in sequences:
                sequences.append(match.group(0))
            return chr(0xE000 + sequences.index(match.group(0)))

        return re.sub(r"\\(?:[a-zA-Z]+(?:\{\})?|.)", placeholder, value)

    def decode(value: str) -> str:
        for k, sequence in enumerate(sequences):
            value = value.replace(chr(0xE000 + k), sequence)
        return value

    encoded = [encode(value) for value in values]
    aligned = _align_to_char(encoded, align_at=align_at)

    # Mark the spaces that replaced a missing decimal mark (the only spaces added by alignment)
    aligned = [
        x if x == e else x.replace(" ", _MISSING_MARK) if " " not in e else x
        for x, e in zip(aligned, encoded)
    ]

    phantom_mark = f"\\hphantom{{{_latex_escape(align_at)}}}"
    return [
        decode(
            x.replace(FIGURE_SPACE, "\\hphantom{0}")
            .replace(NO_BREAK_SPACE, "~")
            .replace(_MISSING_MARK, phantom_mark)
        )
        for x in aligned
    ]


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
