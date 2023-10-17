from __future__ import annotations
from typing import Optional


class Stubhead:
    stubhead: Optional[str]

    def __init__(self):
        pass


class StubheadAPI:
    def tab_stubhead(self, label: str):
        """
        Add label text to the stubhead.

        Add a label to the stubhead of a gt table. The stubhead is the lone
        element that is positioned left of the column labels, and above the stub. If
        a stub does not exist, then there is no stubhead (so no change will be made
        when using this function in that case). We have the flexibility to use
        Markdown formatting for the stubhead label. Furthermore, if the table is
        intended for HTML output, we can use HTML for the stubhead label.

        Parameters
        ----------
        label (str)
            The text to be used as the stubhead label. We can optionally use the `md()`
            and `html()` functions to style the text as Markdown or to retain HTML
            elements in the text.

        Returns
        -------
        GT
            Result of the table operation.

        Examples
        --------
            >>> from gt import *
            >>> x = GT([{"a": 5, "b": 10}, {"a": 15, "b": 20}])
            >>>     .tab_stubhead(label="The Stubhead Label")
            >>> x
            >>> print(x)
        """

        self._stubhead.stubhead = label

        return self
