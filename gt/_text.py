from typing import Union

import commonmark
import re


class Text:
    def __init__(self, text: str, type: str):
        self.text: str = text
        self.type: str = type


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

    def append(self, *args: str):
        self.pieces.extend(args)

    def prepend(self, *args: str):
        self.pieces[0:0] = args


def _md_html(x: str) -> str:
    str = commonmark.commonmark(x)
    return re.sub(r"^<p>|</p>\n$", "", str)


def _process_text(x: Union[Text, str]) -> str:

    if isinstance(x, str):
        text = x
        type = "plaintext"
    else:
        text = x.text
        type = x.type

    if type == "markdown":
        x_out = _md_html(text)
    if type == "html":
        x_out = text
    else:
        # TODO: Perform HTML escaping
        x_out = text

    return x_out
