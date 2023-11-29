from __future__ import annotations


class StubheadAPI:
    def tab_stubhead(self, label: str):
        """
        Add label text to the stubhead.

        Add a label to the stubhead of a gt table. The stubhead is the lone element that is
        positioned left of the column labels, and above the stub. If a stub does not exist, then
        there is no stubhead (so no change will be made when using this function in that case). We
        have the flexibility to use Markdown formatting for the stubhead label. Furthermore, if the
        table is intended for HTML output, we can use HTML for the stubhead label.

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

        (
            gt.GT(gtcars_mini, rowname_col=\"model\")
            .tab_stubhead(label=\"car\")
        )
        ```
        """

        self._stubhead.stubhead = label

        return self
