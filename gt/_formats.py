from __future__ import annotations

from typing import Any, Callable, TypeVar, Union, List, cast

from ._tbl_data import n_rows
from ._gt_data import GTData, FormatFns, FormatFn, FormatInfo


class FormatsAPI:
    @staticmethod
    def fmt(
        x: GTData,
        fns: Union[FormatFn, FormatFns],
        columns: Union[str, List[str], None] = None,
        rows: Union[int, List[int], None] = None,
    ):
        """Set a column format with a formatter function.

        The `fmt()` method provides a way to execute custom formatting
        functionality with raw data values in a way that can consider all output
        contexts.

        Along with the `columns` and `rows` arguments that provide some precision in
        targeting data cells, the `fns` argument allows you to define one or more
        functions for manipulating the raw data.

        Args:
            fns (list): Either a single formatting function or a named list of
            functions.

        Returns:
            GTData: The GTData object is returned.
        """

        # If a single function is supplied to `fns` then
        # repackage that into a list as the `default` function
        if isinstance(fns, Callable):
            fns = FormatFns(default=fns)

        columns = listify(columns, list)

        if rows is None:
            rows = list(range(n_rows(x._tbl_data)))
        elif isinstance(rows, int):
            rows = [rows]

        formatter = FormatInfo(fns, columns, rows)
        x._formats.append(formatter)

        return x

    # TODO: transition to static methods ----
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


def fmt_integer(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    scale_by: float = 1,
) -> GTData:
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

    FormatsAPI.fmt(self, fns=fmt_integer_fn, columns=columns, rows=rows)

    return self


def fmt_number(
    self: GTData,
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
) -> GTData:
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

    FormatsAPI.fmt(self, fns=fmt_number_fn, columns=columns, rows=rows)

    return self


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
