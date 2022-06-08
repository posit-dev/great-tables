from typing import Optional, List, Any


class OptionsInfo:
    parameter: Optional[str]
    scss: Optional[bool]
    category: Optional[str]
    type: Optional[str]
    value: Optional[List[Any]]

    def __init__(
        self,
        parameter: Optional[str] = None,
        scss: Optional[bool] = None,
        category: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[List[Any]] = None,
    ):
        self.parameter = parameter
        self.scss = scss
        self.category = category
        self.type = type
        self.value = value


class Options:
    def __init__(self):
        pass


class OptionsAPI:
    _options: Options

    def __init__(self):
        self._options = Options()
