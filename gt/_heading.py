from typing import Optional


class Heading:
    title: Optional[str] = None
    subtitle: Optional[str] = None
    preheader: Optional[str] = None


class HeadingAPI:
    _heading: Heading

    def __init__(self):
        self._heading = Heading()

    def tab_header(
        self,
        title: str,
        subtitle: Optional[str] = None,
        preheader: Optional[str] = None,
    ):
        self._heading.title = title
        self._heading.subtitle = subtitle
        self._heading.preheader = preheader

        return self
