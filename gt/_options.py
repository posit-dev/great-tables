from typing import Optional, Union, List, Any


class OptionsInfo:
    parameter: Optional[str]
    scss: Optional[bool]
    category: Optional[str]
    type: Optional[str]
    value: Optional[Union[Any, List[str]]]

    def __init__(
        self,
        parameter: Optional[str] = None,
        scss: Optional[bool] = None,
        category: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[Union[Any, List[str]]] = None,
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
