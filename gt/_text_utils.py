import commonmark


def md_html(x: str) -> str:
    return commonmark.commonmark(x)
