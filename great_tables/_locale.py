from __future__ import annotations
from typing import Optional


class Locale:
    locale: Optional[str]

    def __init__(self, locale: str | None = ""):
        if locale is None or locale == "":
            locale = "en"
        self._locale = locale


class LocaleAPI:
    pass
