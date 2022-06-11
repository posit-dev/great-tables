from typing import Optional, Union, List


class Heading:
    title: Optional[str] = None
    subtitle: Optional[str] = None
    preheader: Optional[str] = None


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
        Add a table header

        Parameters
        ----------
        title,subtitle
            Text to be used in the table title and, optionally, for
            the table subtitle. We can elect to use the `md()` and `html()`
            helper functions to style the text as Markdown or to retain HTML
            elements in the text.
        preheader
            Optional preheader content that is rendered above the table. Can
            be supplied as a list of strings.

        Examples:
        ---------
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
