from __future__ import annotations

from typing import TYPE_CHECKING

from ._text import Text

if TYPE_CHECKING:
    from ._types import GTSelf


def tab_stubhead(self: GTSelf, label: str | Text) -> GTSelf:
    """
    Add label text to the stubhead.

    Add a label to the stubhead of a table. The stubhead is the lone element that is positioned
    left of the column labels, and above the stub. If a stub does not exist, then there is no
    stubhead (so no change will be made when using this method in that case). We have the
    flexibility to use Markdown formatting for the stubhead label (through use of the
    [`md()`](`great_tables.md`) helper function). Furthermore, we can use HTML for the stubhead
    label so long as we also use the [`html()`](`great_tables.html`) helper function.

    Parameters
    ----------
    label
        The text to be used as the stubhead label. We can optionally use the
        [`md()`](`great_tables.md`) and [`html()`](`great_tables.html`) helper functions to style
        the text as Markdown or to retain HTML elements in the text.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using a small subset of the `gtcars` dataset, we can create a table with row labels. Since
    we have row labels in the stub (via use of `rowname_col="model"` in the `GT()` call) we have
    a stubhead, so, let's add a stubhead label (`"car"`) with the `tab_stubhead()` method to
    describe what's in the stub.

    ```{python}
    from great_tables import GT
    from great_tables.data import gtcars

    gtcars_mini = gtcars[["model", "year", "hp", "trq"]].head(5)

    (
        GT(gtcars_mini, rowname_col="model")
        .tab_stubhead(label="car")
    )
    ```

    We can also use Markdown formatting for the stubhead label. In this example, we'll use
    `md("*Car*")` to make the label italicized.

    ```{python}
    from great_tables import GT, md
    from great_tables.data import gtcars

    (
        GT(gtcars_mini, rowname_col="model")
        .tab_stubhead(label=md("*Car*"))
    )
    ```
    """

    return self._replace(_stubhead=label)
