from __future__ import annotations

from typing import TYPE_CHECKING

from ._gt_data import Heading
from ._text import Text

if TYPE_CHECKING:
    from ._types import GTSelf


def tab_header(
    self: GTSelf,
    title: str | Text,
    subtitle: str | Text | None = None,
    preheader: str | list[str] | None = None,
) -> GTSelf:
    """
    Add a table header.

    We can add a table header to the output table that contains a title and even a subtitle with the
    `tab_header()` method. A table header is an optional table component that is positioned above
    the column labels. We have the flexibility to use Markdown or HTML formatting for the header's
    title and subtitle with the [`md()`](`great_tables.md`) and [`html()`](`great_tables.html`)
    helper functions.

    Parameters
    ----------
    title
        Text to be used in the table title. We can elect to use the [`md()`](`great_tables.md`) and
        [`html()`](`great_tables.html`) helper functions to style the text as Markdown or to retain
        HTML elements in the text.
    subtitle
        Text to be used in the table subtitle. We can elect to use the [`md()`](`great_tables.md`)
        and [`html()`](`great_tables.html`) helper functions to style the text as Markdown or to
        retain HTML elements in the text.
    preheader
        Optional preheader content that is rendered above the table. Can be supplied as a list
        of strings.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's use a small portion of the `gtcars` dataset to create a table. A header part can be added
    to the table with the `tab_header()` method. We'll add a title and the optional subtitle as
    well. With the [`md()`](`great_tables.md`) helper function, we can make sure the Markdown
    formatting is interpreted and transformed.

    ```{python}
    from great_tables import GT, md
    from great_tables.data import gtcars

    gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

    (
        GT(gtcars_mini)
        .tab_header(
            title=md("Data listing from **gtcars**"),
            subtitle=md("`gtcars` is an R dataset")
        )
    )
    ```

    We can alternatively use the [`html()`](`great_tables.html`) helper function to retain HTML
    elements in the text.

    ```{python}
    from great_tables import GT, md, html
    from great_tables.data import gtcars

    gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

    (
        GT(gtcars_mini)
        .tab_header(
            title=md("Data listing <strong>gtcars</strong>"),
            subtitle=html("From <span style='color:red;'>gtcars</span>")
        )
    )
    ```
    """
    return self._replace(_heading=Heading(title=title, subtitle=subtitle, preheader=preheader))
