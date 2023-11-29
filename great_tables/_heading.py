from __future__ import annotations
from typing import Optional, Union, List
from ._gt_data import GTData, Heading

from copy import copy


class HeadingAPI:
    def tab_header(
        self,
        title: str,
        subtitle: Optional[str] = None,
        preheader: Optional[Union[str, List[str]]] = None,
    ) -> GTData:
        """
        Add a table header.

        We can add a table header to the **gt** table with a title and even a subtitle using the
        `tab_header()` method. A table header is an optional table component that is positioned
        above above the column labels. We have the flexibility to use Markdown or HTML formatting
        for the header's title and subtitle with the `md()` and `html()` helper functions.

        Parameters
        ----------
        title : str
            Text to be used in the table title. We can elect to use the `md()` and `html()` helper
            functions to style the text as Markdown or to retain HTML elements in the text.
        subtitle : str
            Text to be used in the table subtitle. We can elect to use the `md()` and `html()`
            helper functions to style the text as Markdown or to retain HTML elements in the text.
        preheader (str)
            Optional preheader content that is rendered above the table. Can be supplied as a list
            of strings.

        Returns
        -------
        GTData
            The GTData object is returned.

        Examples
        --------
        Let's use a small portion of the `gtcars` dataset to create a table. A header part can be
        added to the table with the `tab_header()` method. We'll add a title and the optional
        subtitle as well. With the `md()` helper function, we can make sure the Markdown formatting
        is interpreted and transformed.

        ```{python}
        import great_tables as gt

        gtcars_mini = gt.gtcars[[\"mfr\", \"model\", \"msrp\"]].head(5)

        (
            gt.GT(gtcars_mini)
            .tab_header(
                title=gt.md(\"Data listing from **gtcars**\"),
                subtitle=gt.md(\"`gtcars` is an R dataset\")
            )
        )
        ```

        We can alternatively use the `html()` helper function to retain HTML elements in the text.

        ```{python}
        (
            gt.GT(gtcars_mini)
            .tab_header(
                title=gt.md("Data listing <strong>gtcars</strong>"),
                subtitle=gt.html("From <span style='color:red;'>gtcars</span>")
            )
        )
        ```
        """
        result = copy(self)
        result._heading = Heading(title=title, subtitle=subtitle, preheader=preheader)

        return result
