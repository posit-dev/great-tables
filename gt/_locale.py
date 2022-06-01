from typing import Optional


class Locale:
    locale: Optional[str]

    def __init__(self, locale: str = ""):
        if locale is None or locale == "":
            locale = "en"
        self._locale = locale


class LocaleAPI:
    _locale: Locale

    def __init__(self, locale: str = ""):
        self._locale = Locale(locale)
