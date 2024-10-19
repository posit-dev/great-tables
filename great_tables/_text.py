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


def _md_html(x: str) -> str:
    str = commonmark.commonmark(x)
    return re.sub(r"^<p>|</p>\n$", "", str)


def _md_latex(x: str) -> str:

    # TODO: Implement commonmark to LaTeX conversion (through a different library as
    # commonmark-py does not support it)
    raise NotImplementedError("Markdown to LaTeX conversion is not supported yet")


def _process_text(x: str | Text | None, context: str = "html") -> str:

    from great_tables._helpers import UnitStr

    if x is None:
        return ""

    if context == "html":

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

    elif context == "latex":

        if isinstance(x, Md):
            return _md_latex(x.text)
        elif isinstance(x, Html):
            return x.text
        elif isinstance(x, str):
            return _latex_escape(x)
        elif isinstance(x, Text):
            return x.text
        elif isinstance(x, UnitStr):
            # TODO: this is currently not implemented
            return x.to_latex()
        else:
            raise TypeError(f"Invalid type: {type(x)}")

    else:
        raise ValueError(f"Invalid context: {context}")


def _process_text_id(x: str | Text | None) -> str:
    return _process_text(x)


def _html_escape(x: str) -> str:
    return html.escape(x)


def _latex_escape(text: str) -> str:

    latex_escape_regex = "[\\\\&%$#_{}~^]"
    text = re.sub(latex_escape_regex, lambda match: "\\" + match.group(), text)

    return text
