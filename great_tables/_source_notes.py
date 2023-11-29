from __future__ import annotations

from ._gt_data import GTData


def tab_source_note(data: GTData, source_note: str) -> GTData:
    """
    Add a source note citation.

    Add a source note to the footer part of the gt table. A source note is useful for citing the
    data included in the table. Several can be added to the footer, simply use the
    `tab_source_note()` method multiple times and they will be inserted in the order provided. We
    can use Markdown formatting for the note, or, if the table is intended for HTML output, we can
    include HTML formatting.

    Parameters
    ----------
    source_note : str
        Text to be used in the source note. We can optionally use the `md()` or `html()` helpers
        to style the text as Markdown or to retain HTML elements in the text.

    Returns
    -------
    GTData
        The GTData object is returned.

    Examples
    --------
    With three columns from the [`gtcars`] dataset, let's create a **gt** table. We can use the
    `tab_source_note()` function to add a source note to the table footer. Here we are citing the
    data source but this function can be used for any text you'd prefer to display in the footer
    component of the table.

    ```{python}
    import great_tables as gt

    gtcars_mini = gt.gtcars[[\"mfr\", \"model\", \"msrp\"]].head(5)

    (
        gt.GT(gtcars_mini, rowname_col=\"model\")
        .tab_source_note(source_note=\"From edmunds.com\")
    )
    ```
    """

    return data._replace(_source_notes=data._source_notes + [source_note])
