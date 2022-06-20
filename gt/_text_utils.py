import commonmark
import re


def _md_html(x: str) -> str:
    str = commonmark.commonmark(x)
    return re.sub(r"^<p>|</p>\n$", "", str)
