from typing import Optional, List
from enum import Enum, auto


class FootnotePlacement(Enum):
    Auto = auto()
    Left = auto()
    Right = auto()


class FootnoteInfo:
    locname: Optional[str]
    grpname: Optional[str]
    colname: Optional[str]
    locnum: Optional[int]
    rownum: Optional[int]
    colnum: Optional[int]
    footnotes: Optional[List[str]]
    placement: Optional[FootnotePlacement]

    # The components of a footnote declaration are:
    # `locname` (empty, str)
    # `grpname` (empty, str)
    # `colname` (empty, str)
    # `locnum` (empty, int)
    # `rownum` (empty, int)
    # `colnum` (empty, int)
    # `footnotes` (empty list, str)
    # `placement` (enum, 3 possible values)

    def __init__(
        self,
        locname: Optional[str] = None,
        grpname: Optional[str] = None,
        colname: Optional[str] = None,
        locnum: Optional[int] = None,
        rownum: Optional[int] = None,
        colnum: Optional[int] = None,
        footnotes: Optional[List[str]] = None,
        placement: Optional[FootnotePlacement] = None,
    ):
        self.locname = locname
        self.grpname = grpname
        self.colname = colname
        self.locnum = locnum
        self.rownum = rownum
        self.colnum = colnum
        self.footnotes = footnotes
        self.placement = placement


class Footnotes:
    def __init__(self):
        pass


class FootnotesAPI:
    _footnotes: Footnotes

    def __init__(self):
        self._footnotes = Footnotes()

    # TODO: create the `tab_footnote()` function
