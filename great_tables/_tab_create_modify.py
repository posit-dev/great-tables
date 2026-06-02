from __future__ import annotations

import re
from typing import TYPE_CHECKING, Callable, Literal

from ._gt_data import TextTransformInfo
from ._helpers import GoogleFont
from ._locations import Loc, set_style
from ._styles import CellStyle

if TYPE_CHECKING:
    from ._types import GTSelf


def tab_style(
    self: GTSelf, style: CellStyle | list[CellStyle], locations: Loc | list[Loc]
) -> GTSelf:
    """Add custom style to one or more cells

    With the `tab_style()` method we can target specific cells and apply styles to them. We do this
    with the combination of the `style` and `location` arguments. The `style` argument requires use
    of styling classes (e.g., `style.fill(color="red")`) and the `location` argument needs to be an
    expression of the cells we want to target using location targeting classes (e.g.,
    `loc.body(columns=<column_name>)`). With the available suite of styling classes, here are some
    of the styles we can apply:

    - the background color of the cell (`style.fill()`'s `color`)
    - the cell's text color, font, and size (`style.text()`'s `color`, `font`, and `size`)
    - the text style (`style.text()`'s `style`), enabling the use of italics or oblique text.
    - the text weight (`style.text()`'s `weight`), allowing the use of thin to bold text (the degree
    of choice is greater with variable fonts)
    - the alignment of text (`style.text()`'s `align`)
    - cell borders with the `style.borders()` class

    Parameters
    ----------
    style
        The styles to use for the cells at the targeted `locations`. The `style.text()`,
        `style.fill()`, and `style.borders()` classes can be used here to more easily generate valid
        styles.
    locations
        The cell or set of cells to be associated with the style. The `loc.body()` class can be used
        here to easily target body cell locations.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's use a small subset of the `exibble` dataset to demonstrate how to use `tab_style()` to
    target specific cells and apply styles to them. We'll start by creating the `exibble_sm` table
    (a subset of the `exibble` table) and then use `tab_style()` to apply a light cyan background
    color to the cells in the `num` column for the first two rows of the table. We'll then apply a
    larger font size to the cells in the `fctr` column for the last four rows of the table.

    ```{python}
    from great_tables import GT, style, loc, exibble

    exibble_sm = exibble[["num", "fctr", "row", "group"]]

    (
        GT(exibble_sm, rowname_col="row", groupname_col="group")
        .tab_style(
            style=style.fill(color="lightcyan"),
            locations=loc.body(columns="num", rows=["row_1", "row_2"]),
        )
        .tab_style(
            style=style.text(size="22px"),
            locations=loc.body(columns=["fctr"], rows=[4, 5, 6, 7]),
        )
    )
    ```

    Let's use `exibble` once again to create a simple, two-column output table (keeping only the
    `num` and `currency` columns). With the `tab_style()` method (called thrice), we'll add style to
    the values already formatted by `fmt_number()` and `fmt_currency()`. In the `style` argument of
    the first two `tab_style()` call, we can define multiple types of styling with the
    `style.fill()` and `style.text()` classes (enclosing these in a list). The cells to be targeted
    for styling require the use of `loc.body()`, which is used here with different columns being
    targeted. For the final `tab_style()` call, we demonstrate the use of `style.borders()` class
    as the `style` argument, which is employed in conjunction with `loc.body()` to locate the row to
    be styled.

    ```{python}
    from great_tables import GT, style, loc, exibble

    (
        GT(exibble[["num", "currency"]])
        .fmt_number(columns="num", decimals=1)
        .fmt_currency(columns="currency")
        .tab_style(
            style=[
                style.fill(color="lightcyan"),
                style.text(weight="bold")
            ],
            locations=loc.body(columns="num")
        )
        .tab_style(
            style=[
                style.fill(color="#F9E3D6"),
                style.text(style="italic")
            ],
            locations=loc.body(columns="currency")
        )
        .tab_style(
            style=style.borders(sides=["top", "bottom"], weight='2px', color="red"),
            locations=loc.body(rows=[4])
        )
    )
    ```
    """

    if not isinstance(style, list):
        style = [style]

    if not isinstance(locations, list):
        locations = [locations]

    new_data = self

    # Intercept `font` in CellStyleText to capture Google Fonts and:
    # 1. transform dictionary to string (with Google Font name)
    # 2. add Google Font import statement
    if any(isinstance(s, CellStyle) for s in style):
        for s in style:
            if (
                isinstance(s, CellStyle)
                and hasattr(s, "font")
                and s.font is not None
                and isinstance(s.font, GoogleFont)
            ):
                # Obtain font name and import statement as local variables
                font_name = s.font.get_font_name()
                font_import_stmt = s.font.make_import_stmt()

                # Replace GoogleFont class with font name
                s.font = font_name

                # Add the Google Font import statement to the internal font imports
                new_data = new_data._replace(
                    _google_font_imports=new_data._google_font_imports.add(font_import_stmt)
                )

    for loc in locations:
        new_data = set_style(loc, new_data, style)

    return new_data


def text_transform(self: GTSelf, locations: Loc | list[Loc], fn: Callable[[str], str]) -> GTSelf:
    """Apply a custom text transformation to cells at specified locations.

    With the `text_transform()` method we can target specific cells and apply a text
    transformation function to their already-formatted content. This is useful for modifying the
    rendered text of cells after all formatting (via `fmt_*()` methods) has been applied.

    Parameters
    ----------
    locations
        The cell or set of cells to be associated with the text transformation. Supported
        locations include `loc.body()`, `loc.stub()`, `loc.row_groups()`, and
        `loc.column_labels()`.
    fn
        A function that takes a cell's text content as a string and returns the transformed
        string.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's use the `exibble` dataset to demonstrate `text_transform()`. We'll format the `num`
    column and then apply a text transformation to wrap the values in parentheses.

    ```{python}
    from great_tables import GT, loc, exibble

    (
        GT(exibble[["num", "char"]].head(4))
        .fmt_number(columns="num", decimals=1)
        .text_transform(
            locations=loc.body(columns="num"),
            fn=lambda x: f"({x})",
        )
    )
    ```

    Using `text_transform()` we can also convert specific cells to uppercase. Here we target only
    the first two rows of the `char` column.

    ```{python}
    from great_tables import GT, loc, exibble

    (
        GT(exibble[["num", "char"]].head(4))
        .text_transform(
            locations=loc.body(columns="char", rows=[0, 1]),
            fn=lambda x: x.upper(),
        )
    )
    ```

    Multiple locations can be targeted at once by passing a list. In this example, we add a
    prefix to all cells in both the `num` and `char` columns.

    ```{python}
    from great_tables import GT, loc, exibble

    (
        GT(exibble[["num", "char"]].head(4))
        .fmt_number(columns="num", decimals=2)
        .text_transform(
            locations=[loc.body(columns="num"), loc.body(columns="char")],
            fn=lambda x: f"~ {x}",
        )
    )
    ```
    """

    if not isinstance(locations, list):
        locations = [locations]

    new_transforms = [TextTransformInfo(loc=loc, fn=fn) for loc in locations]

    return self._replace(_transforms=self._transforms + new_transforms)


def text_replace(
    self: GTSelf,
    pattern: str,
    replacement: str,
    locations: Loc | list[Loc] | None = None,
) -> GTSelf:
    """Perform targeted text replacement with a regex pattern.

    With `text_replace()` we can target cells in specific locations and replace text fragments
    matching a regular expression pattern. This operates on the already-formatted cell content
    (i.e., after `fmt_*()` methods have been applied).

    Parameters
    ----------
    pattern
        A regex pattern used to target text fragments in the resolved cells.
    replacement
        The replacement text for any matched text fragments. Backreferences (e.g., `"\\\\1"`)
        can be used to refer to capture groups in the pattern.
    locations
        The cell or set of cells to be associated with the text replacement. Supported locations
        include `loc.body()`, `loc.stub()`, `loc.row_groups()`, and `loc.column_labels()`. If
        `None`, defaults to `loc.body()`.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that
        we can facilitate method chaining.

    Examples
    --------
    Use `text_replace()` to add HTML emphasis tags around text in parentheses.

    ```{python}
    import pandas as pd
    from great_tables import GT, loc

    df = pd.DataFrame({"item": ["Column A (details)", "Colum B (info)"], "value": [1, 2]})

    (
        GT(df)
        .text_replace(
            pattern=r"\\((.+?)\\)",
            replacement=r"(<em>\\1</em>)",
            locations=loc.body(columns="item"),
        )
    )
    ```

    Replace underscores with spaces in the stub (row labels).

    ```{python}
    from great_tables import GT, loc, exibble

    (
        GT(exibble[["num", "char", "row"]].head(4), rowname_col="row")
        .text_replace(pattern="_", replacement=" ", locations=loc.stub())
    )
    ```
    """
    from ._locations import LocBody

    if locations is None:
        locations = LocBody()

    def _replace_fn(x: str) -> str:
        return re.sub(pattern, replacement, x)

    return text_transform(self, locations=locations, fn=_replace_fn)


def text_case_match(
    self: GTSelf,
    *cases: tuple[str | list[str], str],
    default: str | None = None,
    replace: Literal["all", "partial"] = "all",
    locations: Loc | list[Loc] | None = None,
) -> GTSelf:
    """Perform text replacements with a switch-like approach.

    With `text_case_match()` we can supply a sequence of matching cases in the form of
    `(old_text, new_text)` tuples. Each tuple's first element specifies text to match (either a
    single string or a list of strings) and the second element provides the replacement. By
    default, the matching is performed on the entire cell text (`replace="all"`); use
    `replace="partial"` for substring matching and replacement.

    Parameters
    ----------
    *cases
        One or more tuples of the form `(old_text, new_text)` where `old_text` is a string or
        list of strings to match, and `new_text` is the replacement string.
    default
        The replacement text to use when cell values aren't matched by any of the supplied
        cases. If `None` (the default), unmatched cells are left unchanged.
    replace
        The method for text replacement. Use `"all"` (the default) to match and replace the
        entire cell text, or `"partial"` to match and replace substrings within the cell text.
    locations
        The cell or set of cells to be associated with the text replacement. Supported locations
        include `loc.body()`, `loc.stub()`, `loc.row_groups()`, and `loc.column_labels()`. If
        `None`, defaults to `loc.body()`.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that
        we can facilitate method chaining.

    Examples
    --------
    Replace specific cell values in the `char` column with different text.

    ```{python}
    from great_tables import GT, loc, exibble

    (
        GT(exibble[["num", "char"]].head(4))
        .text_case_match(
            ("apricot", "APRICOT"),
            (["banana", "coconut"], "tropical fruit"),
            default="other",
            locations=loc.body(columns="char"),
        )
    )
    ```

    Use `replace="partial"` to perform substring replacements.

    ```{python}
    from great_tables import GT, loc, exibble

    (
        GT(exibble[["num", "char"]].head(4))
        .text_case_match(
            ("an", "@"),
            replace="partial",
            locations=loc.body(columns="char"),
        )
    )
    ```
    """
    from ._locations import LocBody

    if locations is None:
        locations = LocBody()

    # Build the mapping from all old_text values to their replacement
    match_map: list[tuple[list[str], str]] = []
    for old_text, new_text in cases:
        if isinstance(old_text, str):
            old_text = [old_text]
        match_map.append((old_text, new_text))

    if replace == "all":

        def _match_fn(x: str) -> str:
            for old_values, new_text in match_map:
                if x in old_values:
                    return new_text
            return default if default is not None else x

    else:  # partial

        def _match_fn(x: str) -> str:
            result = x
            for old_values, new_text in match_map:
                for old_val in old_values:
                    result = result.replace(old_val, new_text)
            if result == x and default is not None:
                return default
            return result

    return text_transform(self, locations=locations, fn=_match_fn)


def text_case_when(
    self: GTSelf,
    *cases: tuple[Callable[[str], bool], str],
    default: str | None = None,
    locations: Loc | list[Loc] | None = None,
) -> GTSelf:
    """Perform text replacements using a case-when approach.

    With `text_case_when()` we supply a sequence of cases as `(predicate, replacement)` tuples.
    Each predicate is a function that takes the cell text (as a string) and returns `True` or
    `False`. The first predicate that returns `True` determines the replacement text. This is
    analogous to a series of if/elif statements applied to each cell.

    Parameters
    ----------
    *cases
        One or more tuples of the form `(predicate_fn, new_text)` where `predicate_fn` is a
        callable that accepts a string and returns a boolean, and `new_text` is the replacement
        string to use when the predicate is `True`.
    default
        The replacement text to use when no predicate matches. If `None` (the default),
        unmatched cells are left unchanged.
    locations
        The cell or set of cells to be associated with the text replacement. Supported locations
        include `loc.body()`, `loc.stub()`, `loc.row_groups()`, and `loc.column_labels()`. If
        `None`, defaults to `loc.body()`.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that
        we can facilitate method chaining.

    Examples
    --------
    Conditionally replace cell values based on their content.

    ```{python}
    import pandas as pd
    from great_tables import GT, loc

    df = pd.DataFrame({"score": [95, 72, 88, 61, 100]})

    (
        GT(df)
        .fmt_number(columns="score", decimals=0)
        .text_case_when(
            (lambda x: int(x) >= 90, "A"),
            (lambda x: int(x) >= 80, "B"),
            (lambda x: int(x) >= 70, "C"),
            default="F",
            locations=loc.body(columns="score"),
        )
    )
    ```

    Use string methods in predicates to match patterns.

    ```{python}
    from great_tables import GT, loc, exibble

    (
        GT(exibble[["num", "char"]].head(4))
        .text_case_when(
            (lambda x: x.startswith("a"), "Starts with A"),
            (lambda x: len(x) > 6, "Long text"),
            default="other",
            locations=loc.body(columns="char"),
        )
    )
    ```
    """
    from ._locations import LocBody

    if locations is None:
        locations = LocBody()

    def _case_when_fn(x: str) -> str:
        for predicate, new_text in cases:
            if predicate(x):
                return new_text
        return default if default is not None else x

    return text_transform(self, locations=locations, fn=_case_when_fn)
