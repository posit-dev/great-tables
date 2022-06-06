from typing import List, Optional


class StyleInfo:
    locname: Optional[str]
    grpname: Optional[str]
    colname: Optional[str]
    locnum: Optional[int]
    rownum: Optional[int]
    colnum: Optional[int]
    styles: Optional[List[str]]

    # The components of a style declaration are:
    # `locname` (empty, str)
    # `grpname` (empty, str)
    # `colname` (empty, str)
    # `locnum` (empty, int)
    # `rownum` (empty, int)
    # `colnum` (empty, int)
    # `styles` (empty list, str)

    def __init__(
        self,
        locname: Optional[str] = None,
        grpname: Optional[str] = None,
        colname: Optional[str] = None,
        locnum: Optional[int] = None,
        rownum: Optional[int] = None,
        colnum: Optional[int] = None,
        styles: Optional[List[str]] = None,
    ):
        self.locname = locname
        self.grpname = grpname
        self.colname = colname
        self.locnum = locnum
        self.rownum = rownum
        self.colnum = colnum
        self.styles = styles


class Styles:
    def __init__(self):
        pass


class StylesAPI:
    _styles: Styles

    def __init__(self):
        self._styles = Styles()
