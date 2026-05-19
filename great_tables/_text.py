from __future__ import annotations

import html
import re
from dataclasses import dataclass
from typing import Callable

import commonmark


class BaseText:
    """Abstract base class for text elements"""

    def to_html(self) -> str:
        raise NotImplementedError("Method not implemented")

    def to_latex(self) -> str:
        raise NotImplementedError("Method not implemented")


@dataclass
class Text(BaseText):
    """As-is text"""

    text: str

    def to_html(self) -> str:
        return self.text

    def to_latex(self) -> str:
        return self.text


class Md(Text):
    """Markdown text"""

    def to_html(self) -> str:
        return _md_html(self.text)

    def to_latex(self) -> str:
        return _md_latex(self.text)


class Html(Text):
    """HTML text"""

    def to_html(self) -> str:
        if "{{" in self.text and "}}" in self.text:
            from great_tables._helpers import UnitStr

            unit_str = UnitStr.from_str(self.text)
            return unit_str.to_html()
        return self.text

    def to_latex(self) -> str:
        from ._utils_render_latex import _not_implemented

        _not_implemented(
            "Using the `html()` helper function won't convert HTML to LaTeX. Escaping HTML string instead."
        )

        return _latex_escape(self.text)


def _md_html(x: str) -> str:
    if "{{" in x and "}}" in x:
        from great_tables._helpers import UnitStr

        unit_str = UnitStr.from_str(x)
        processed_text = unit_str.to_html()
    else:
        processed_text = x

    str_result = commonmark.commonmark(processed_text)
    if str_result is None:
        return processed_text
    return re.sub(r"^<p>|</p>\n$", "", str_result)


def _md_latex(x: str) -> str:
    # TODO: Implement commonmark to LaTeX conversion (through a different library as
    # commonmark-py does not support it)
    raise NotImplementedError("Markdown to LaTeX conversion is not supported yet")


def _process_text(x: str | BaseText | None, context: str = "html") -> str:
    if x is None:
        return ""

    escape_fn = _html_escape if context == "html" else _latex_escape

    if isinstance(x, str):
        return escape_fn(x)

    elif isinstance(x, BaseText):
        return x.to_html() if context == "html" else x.to_latex()

    raise TypeError(f"Invalid type: {type(x)}")


def _process_text_id(x: str | BaseText | None) -> str:
    return _process_text(x).replace(" ", "-")


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
    Apply a function to segments of a string that are unmatched by a regex pattern.

    This function splits a string based on a regex pattern to a list of strings, and invokes the
    supplied function (in `func=`) to those list elements that *do not* match the pattern (i.e.,
    the matched components are untouched). Finally, the processed list of text fragments is then
    joined back into a single .

    Parameters
    ----------
    string
        The string to process.
    pattern
        The regex pattern used for splitting the input string.
    func
        The function applied to elements that do not match the pattern.

    Returns
    -------
    str
        A processed string.
    """

    # Split the string by the pattern
    split_result = re.split(pattern, string)

    # Apply the function to elements that do not match the pattern
    processed_list = (func(part) if not re.match(pattern, part) else part for part in split_result)

    # Recombine the list elements to obtain a selectively processed string
    combined_str = "".join(processed_list)

    return combined_str
