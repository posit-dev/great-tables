from __future__ import annotations
from typing import Union
from typing_extensions import Self
from copy import copy
from ._text import Text


class StubheadAPI:
    def tab_stubhead(self, label: Union[str, Text]) -> Self:
        """
        Add label text to the stubhead.

        Add a label to the stubhead of a table. The stubhead is the lone element that is positioned
        left of the column labels, and above the stub. If a stub does not exist, then there is no
        stubhead (so no change will be made when using this method in that case). We have the
        flexibility to use Markdown formatting for the stubhead label (through use of the `md()`
        helper function). Furthermore, we can use HTML for the stubhead label so long as we also use
        the `html()` helper function.

        Parameters
        ----------
        label : str
            The text to be used as the stubhead label. We can optionally use the `md()` and `html()`
            functions to style the text as Markdown or to retain HTML elements in the text.

        Returns
        -------
        GTData
            The GTData object is returned.

        Examples
        --------
        Using a small subset of the `gtcars` dataset, we can create a table with row labels. Since
        we have row labels in the stub (via use of `rowname_col="model"` in the `GT()` call) we have
        a stubhead, so, let's add a stubhead label (`"car"`) with the `tab_stubhead()` method to
        describe what's in the stub.

        ```{python}
        import great_tables as gt

        gtcars_mini = gt.gtcars[[\"model\", \"year\", \"hp\", \"trq\"]].head(5)

        gt.GT(gtcars_mini, rowname_col=\"model\").tab_stubhead(label=\"car\")
        ```

        We can also use Markdown formatting for the stubhead label. In this example, we'll use
        `md("*Car*")` to make the label italicized.

        ```{python}
        gt.GT(gtcars_mini, rowname_col="model").tab_stubhead(label=gt.md("*Car*"))
        ```
        """

        result = copy(self)

        result._stubhead = label

        return result
