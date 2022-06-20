from typing import Union

import commonmark
import re

from ._helpers import Text


def _md_html(x: str) -> str:
    str = commonmark.commonmark(x)
    return re.sub(r"^<p>|</p>\n$", "", str)


def _process_text(x: Union[Text, str]) -> str:

    if isinstance(x, str):
        text = x
        type = "plaintext"
    else:
        text = x.text  # type: ignore
        type = x.type  # type: ignore

    if type == "markdown":
        x_out = _md_html(text)  # type: ignore
    else:
        x_out = text

    return x_out
