from typing import Any, Callable, TypeVar, Union, List, cast, Optional, Tuple

from ._base_api import BaseAPI
from ._tbl_data import n_rows

FormatFn = Callable[[Any], str]


class FormatFns:
    html: Optional[FormatFn]
    latex: Optional[FormatFn]
    rtf: Optional[FormatFn]
    default: Optional[FormatFn]

    def __init__(self, **kwargs: FormatFn):
        for format in ["html", "latex", "rtf", "default"]:
            if kwargs.get(format):
                setattr(self, format, kwargs[format])


class CellSubset:
    def __init__(self):
        pass

    def resolve(self) -> List[Tuple[str, int]]:
        raise NotImplementedError("Not implemented")


class CellRectangle(CellSubset):
    cols: List[str]
    rows: List[int]

    def __init__(self, cols: List[str], rows: List[int]):
        self.cols = cols
        self.rows = rows

    def resolve(self):
        return list((col, row) for col in self.cols for row in self.rows)


class FormatInfo:
    func: FormatFns
    cells: CellSubset

    def __init__(self, func: FormatFns, cols: List[str], rows: List[int]):
        self.func = func
        self.cells = CellRectangle(cols, rows)


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

        if rows is None:
            rows = list(range(n_rows(self._get_tbl_data())))
        elif isinstance(rows, int):
            rows = [rows]

        formatter = FormatInfo(fns, columns, rows)
        self._formats.append(formatter)

        return self

    def fmt_number(
        self,
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
        decimals: int = 2,
        # n_sigfig: int = None,
        drop_trailing_zeros: bool = False,
        drop_trailing_dec_mark: bool = True,
        # use_seps: bool = True,
        # accounting: bool = False,
        scale_by: float = 1,
        # suffixing: bool = False,
        # pattern: str = '{x}'
        # sep_mark: str = ',',
        # dec_mark: str = '.',
        # force_sign: bool = False,
        # system: str = 'intl',
        # locale: str = None,
    ):
        # Generate a function that will operate on single `x` values in
        # the table body
        def fmt_number_fn(
            x: float,
            decimals: int = decimals,
            drop_trailing_zeros: bool = drop_trailing_zeros,
            drop_trailing_dec_mark: bool = drop_trailing_dec_mark,
            scale_by: float = scale_by,
        ):
            # Scale `x` value by a defined `scale_by` value
            x = x * scale_by

            # Generate a format specification using `decimals`
            fmt_spec = f".{decimals}f"

            # Get the formatted `x` value
            x_formatted = format(x, fmt_spec)

            # Drop any trailing zeros if option is taken
            if drop_trailing_zeros is True:
                x_formatted = x_formatted.rstrip("0")

            # Drop the trailing decimal mark if it is present
            if drop_trailing_dec_mark is True:
                x_formatted = x_formatted.rstrip(".")

            return x_formatted

        self.fmt(fns=fmt_number_fn, columns=columns, rows=rows)

        return self

    def fmt_integer(
        self,
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
        scale_by: float = 1,
    ):
        # Generate a function that will operate on single `x` values in
        # the table body
        def fmt_integer_fn(
            x: float,
            scale_by: float = scale_by,
        ):
            # Scale `x` value by a defined `scale_by` value
            x = x * scale_by

            x = round(x)

            x_formatted = f"{x}"

            return x_formatted

        self.fmt(fns=fmt_integer_fn, columns=columns, rows=rows)

        return self

    def fmt_scientific(
        self,
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
    ):
        # TODO: Not implemented yet
        return self

    def fmt_engineering(
        self,
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
    ):
        # TODO: Not implemented yet
        return self

    def fmt_percent(
        self,
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
        decimals: int = 2,
        drop_trailing_zeros: bool = False,
        drop_trailing_dec_mark: bool = True,
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
