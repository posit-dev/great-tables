import html
import re
from dataclasses import dataclass
from typing import Literal, Union

import commonmark


@dataclass
class Text:
    text: str
    type: Literal["from_markdown", "html"]


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
    if x is None:
        return ""

    if isinstance(x, str):
        text = x
        type = "plaintext"
    else:
        text = x.text
        type = x.type

    if type == "from_markdown":
        x_out = _md_html(text)
    elif type == "html":
        x_out = text
    else:
        x_out = _html_escape(text)

    return x_out


def _process_text_id(x: str | Text | None) -> str:
    return _process_text(x)


def _html_escape(x: str) -> str:
    return html.escape(x)
