from typing import Any, Callable, TypeVar, TypedDict, Union, List, cast
from typing_extensions import NotRequired

from ._base_api import BaseAPI

# TODO: when htmltools is used, we may want to support multiple output types
#       like Markdown or Tag objects with dependencies as some examples
FormatFn = Callable[[Any], str]


class FormatFns(TypedDict):
    html: NotRequired[FormatFn]
    latex: NotRequired[FormatFn]
    rtf: NotRequired[FormatFn]
    default: NotRequired[FormatFn]

    # TODO: Could we use something other than TypedDict so
    # this becomes possible? Maybe dataclasses?
    # def __call__(self, context: str, x: Any) -> str:
    #     if self has context:
    #         return self[context](x)
    #     elif self has "default":
    #         return self["default"](x)


class FormatInfo:
    func: FormatFns
    cols: List[str]
    rows: List[int]

    def __init__(self, func: FormatFns, cols: List[str], rows: List[int]):
        self.func = func
        self.cols = cols
        self.rows = rows


# TODO: this will contain private methods for formatting cell values to strings
class Formats:
    def __init__(self):
        pass


class FormatsAPI(BaseAPI):
    _formats: List[FormatInfo]

    def __init__(self):
        self._formats = []

    def fmt(
        self,
        fns: Union[FormatFn, FormatFns],
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
    ):

        # If a single function is supplied to `fns` then
        # repackage that into a list as the `default` function
        if isinstance(fns, Callable):
            fns = FormatFns(default=fns)

        columns = listify(columns, List[str])

        # if columns is None:
        #     columns = self._data.columns
        # elif isinstance(columns, str):
        #     columns = [columns]

        if rows is None:
            rows = list(range(self._get_tbl_data().n_rows()))
        elif isinstance(rows, int):
            rows = [rows]

        formatter = FormatInfo(fns, columns, rows)

        self._formats.append(formatter)

        return self

    def fmt_number(
        self,
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
        decimals=2,
    ):
        # TODO: Not implemented yet
        return self

    def fmt_integer(
        self,
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
    ):
        # TODO: Not implemented yet
        return self

    # TODO: add `fmt_scientific()`
    # TODO: add `fmt_engineering()`

    def fmt_percent(
        self,
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
        decimals=2,
    ):
        # TODO: Not implemented yet
        return self

    # TODO: add `fmt_partsper()`
    # TODO: add `fmt_fraction()`
    # TODO: add `fmt_currency()`
    # TODO: add `fmt_roman()`
    # TODO: add `fmt_bytes()`
    # TODO: add `fmt_date()`
    # TODO: add `fmt_time()`
    # TODO: add `fmt_datetime()`
    # TODO: add `fmt_duration()`
    # TODO: add `fmt_markdown()`
    # TODO: add `fmt_passthrough()`


T = TypeVar("T")


def listify(
    x: Union[T, List[T], None],
    default: Callable[[], List[T]],
) -> List[T]:
    if x is None:
        return default()
    elif not isinstance(x, list):
        return [x]
    else:
        return cast(Any, x)
