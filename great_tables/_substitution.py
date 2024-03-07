from __future__ import annotations

from ._tbl_data import DataFrameLike, SelectExpr, is_na
from ._gt_data import FormatterSkipElement, FormatInfo
from ._formats import fmt


from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Type, Union, Literal, List

if TYPE_CHECKING:
    from ._types import GTSelf


def _convert_missing(context: Literal["html"], el: str):
    """Convert el to a context specific representation."""

    # TODO: how is context passed? Could use a literal string (e.g. "html") for now?
    # TODO: detect if el has some kind of AsIs feature specified
    # which indicates it should not be converted

    # If a table row has all empty cells, they collapse. So add a single line break.
    # See https://stackoverflow.com/q/2789372/1144523
    if context == "html" and el == "":
        return "<br />"

    return el


def sub_missing(
    self: GTSelf,
    columns: SelectExpr = None,
    rows: Union[int, List[int], None] = None,
    missing_text: str = "---",
) -> GTSelf:
    subber = SubMissing(self._tbl_data, missing_text)
    return fmt(self, fns=subber.to_html, columns=columns, rows=rows)


def sub_zero(
    self: GTSelf,
    columns: SelectExpr = None,
    rows: Union[int, List[int], None] = None,
    zero_text: str = "nil",
) -> GTSelf:
    subber = SubZero(zero_text)
    return fmt(self, fns=subber.to_html, columns=columns, rows=rows)


@dataclass
class SubMissing:
    dispatch_frame: DataFrameLike
    missing_text: str

    def to_html(self, x: Any) -> str | FormatterSkipElement:
        return self.missing_text if is_na(self.dispatch_frame, x) else FormatterSkipElement()


@dataclass
class SubZero:
    zero_text: str

    def to_html(self, x: Any) -> str | FormatterSkipElement:
        return self.zero_text if x == 0 else FormatterSkipElement()
