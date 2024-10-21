from __future__ import annotations

import html
import re
from dataclasses import dataclass
from typing import Literal, Union, Callable

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


def escape_pattern_str_latex(pattern_str: str) -> str:

    pattern = r"(\{[x0-9]+\})"

    return process_string(pattern_str, pattern, _latex_escape)


def process_string(string: str, pattern: str, func: Callable[[str], str]) -> str:
    """
    Process a string selectively based on a pattern.

    This function splits a string based on a pattern and applies a function to elements that do not
    match the pattern. The processed elements are then recombined to obtain a selectively processed
    string.

    Args:
        string (str): The string to process.
        pattern (str): The pattern to split the string by.
        func (Callable[[str], str]): The function applied to elements that do not match the pattern.

    Returns:
        str: The selectively processed string.
    """

    # Split the string by the pattern
    split_result = re.split(pattern, string)

    # Apply the function to elements that do not match the pattern
    processed_list = [func(part) if not re.match(pattern, part) else part for part in split_result]

    # Recombine the list elements to obtain a selectively processed string
    combined_str = "".join(processed_list)

    return combined_str
