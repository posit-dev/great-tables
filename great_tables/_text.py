from __future__ import annotations

import html
import re
from dataclasses import dataclass
from typing import Literal, Union

import commonmark


@dataclass
class Text:
    text: str


class Md(Text):
    """Markdown text"""


class Html(Text):
    """HTML text"""


class StringBuilder:
    pieces: list[Union[str, "StringBuilder"]]

    def __init__(self, *args: Union[str, "StringBuilder"]):
        self.pieces = list(args)

    def _collect(self, lst: list[str]):
        for piece in self.pieces:
            if isinstance(piece, str):
                lst.append(piece)
            else:
                piece._collect(lst)

    def make_string(self) -> str:
        lst = []
        self._collect(lst)
        return "".join(lst)

    def append(self, *args: str) -> None:
        self.pieces.extend(args)

    def prepend(self, *args: str) -> None:
        self.pieces[0:0] = args


def _md_html(x: str) -> str:
    str = commonmark.commonmark(x)
    return re.sub(r"^<p>|</p>\n$", "", str)


def _process_text(x: str | Text | None) -> str:
    from great_tables._helpers import UnitStr

    if x is None:
        return ""

    if isinstance(x, Md):
        return _md_html(x.text)
    elif isinstance(x, Html):
        return x.text
    elif isinstance(x, str):
        return _html_escape(x)
    elif isinstance(x, Text):
        return x.text
    elif isinstance(x, UnitStr):
        return x.to_html()
    else:
        raise TypeError(f"Invalid type: {type(x)}")


def _process_text_id(x: str | Text | None) -> str:
    return _process_text(x)


def _html_escape(x: str) -> str:
    return html.escape(x)
