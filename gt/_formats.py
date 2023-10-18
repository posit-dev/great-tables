from __future__ import annotations
from typing import Any, Callable, TypeVar, Union, List, cast
from ._tbl_data import n_rows
from ._gt_data import GTData, FormatFns, FormatFn, FormatInfo

T = TypeVar("T")


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

            columns: The columns to target. Can either be a single column name
            or a series of column names provided in a list.

            rows: In conjunction with `columns`, we can specify which of their
            rows should undergo formatting. The default is all rows, resulting
            in all rows in `columns` being formatted. Alternatively, we can
            supply a list of row indices.

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
    """Format numeric values.

    The `fmt()` method provides a way to execute custom formatting
    functionality with raw data values in a way that can consider all output
    contexts.

    Along with the `columns` and `rows` arguments that provide some precision in
    targeting data cells, the `fns` argument allows you to define one or more
    functions for manipulating the raw data.

    Args:
        columns: The columns to target. Can either be a single column name
        or a series of column names provided in a list.

        rows: In conjunction with `columns`, we can specify which of their
        rows should undergo formatting. The default is all rows, resulting
        in all rows in `columns` being formatted. Alternatively, we can
        supply a list of row indices.

        decimals: This corresponds to the exact number of decimal places to use.
        A value such as `2.34` can, for example, be formatted with `0` decimal
        places and it would result in `"2"`. With `4` decimal places, the
        formatted value becomes `"2.3400"`. The trailing zeros can be removed
        with `drop_trailing_zeros=True`. If you always need `decimals = 0`, the
        `fmt_integer()` method should be considered.

        drop_trailing_zeros: A boolean value that allows for removal of trailing
        zeros (those redundant zeros after the decimal mark).

        drop_trailing_dec_mark: A boolean value that determines whether decimal
        marks should always appear even if there are no decimal digits to
        display after formatting (e.g., `23` becomes `23.` if `False`). By
        default trailing decimal marks are not shown.

        scale_by: All numeric values will be multiplied by the `scale_by` value
        before undergoing formatting. Since the `default` value is `1`, no
        values will be changed unless a different multiplier value is supplied.

    Returns:
        GTData: The GTData object is returned.
    """

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


def fmt_integer(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    scale_by: float = 1,
) -> GTData:
    """Format values as integers.

    With numeric values in a gt table, we can perform number-based formatting so
    that the targeted values are always rendered as integer values.

    We can have fine control over integer formatting with the following options:

    - digit grouping separators: options to enable/disable digit separators
    and provide a choice of separator symbol
    - scaling: we can choose to scale targeted values by a multiplier value
    - large-number suffixing: larger figures (thousands, millions, etc.) can
    be autoscaled and decorated with the appropriate suffixes
    - pattern: option to use a text pattern for decoration of the formatted
    values
    - locale-based formatting: providing a locale ID will result in number
    formatting specific to the chosen locale

    Args:
        fns (list): Either a single formatting function or a named list of
        functions.

        columns: The columns to target. Can either be a single column name
        or a series of column names provided in a list.

        rows: In conjunction with `columns`, we can specify which of their
        rows should undergo formatting. The default is all rows, resulting
        in all rows in `columns` being formatted. Alternatively, we can
        supply a list of row indices.

        scale_by: All numeric values will be multiplied by the `scale_by` value
        before undergoing formatting. Since the `default` value is `1`, no
        values will be changed unless a different multiplier value is supplied.

    Returns:
        GTData: The GTData object is returned.
    """

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


def listify(
    x: Union[T, List[T], None],
    default: Callable[[], List[T]],
) -> List[T]:
    """
    Convert the input into a list.

    Args:
        x (Union[T, List[T], None]): The input value to be converted into a
        list. It can be a single value of type T, a list of values of type T,
        or None.

        default (Callable[[], List[T]]): A callable that returns a default list
        when the input value is None.

    Returns:
        List[T]: The converted list.

    Raises:
        None

    Examples:
        listify(5, lambda: [1, 2, 3])  # Output: [5]
        listify([1, 2, 3], lambda: [4, 5, 6])  # Output: [1, 2, 3]
        listify(None, lambda: ['a', 'b', 'c'])  # Output: ['a', 'b', 'c']
    """
    if x is None:
        return default()
    elif not isinstance(x, list):
        return [x]
    else:
        return cast(Any, x)
