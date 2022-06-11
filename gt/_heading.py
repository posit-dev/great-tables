from typing import Optional, Union, List


class Heading:
    title: Optional[str] = None
    subtitle: Optional[str] = None
    preheader: Optional[Union[str, List[str]]] = None


class HeadingAPI:
    _heading: Heading

    def __init__(self):
        self._heading = Heading()

    def tab_header(
        self,
        title: str,
        subtitle: Optional[str] = None,
        preheader: Optional[Union[str, List[str]]] = None,
    ):
        """
        Add a table header.

        We can add a table header to the **gt** table with a title and even a
        subtitle. A table header is an optional table part that is positioned above
        the column labels. We have the flexibility to use Markdown formatting for the
        header's title and subtitle. Furthermore, if the table is intended for HTML
        output, we can use HTML in either of the title or subtitle.

        Parameters
        ----------
        title (str), subtitle (str)
            Text to be used in the table title and, optionally, for
            the table subtitle. We can elect to use the `md()` and `html()`
            helper functions to style the text as Markdown or to retain HTML
            elements in the text.
        preheader (str)
            Optional preheader content that is rendered above the table. Can
            be supplied as a list of strings.

        Returns
        -------
        GT
            Result of the table operation.

        Examples
        --------
            >>> from gt import *
            >>> x = GT([{"a": 5, "b": 10}, {"a": 15, "b": 20
            >>>     .tab_header(title="Title", subtitle="Subtitle")
            >>> x
            >>> print(x)
        """
        self._heading.title = title
        self._heading.subtitle = subtitle
        self._heading.preheader = preheader

        return self
