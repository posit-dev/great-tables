from __future__ import annotations
from decimal import Decimal
from math import floor, log10
from typing import Any, Callable, TypeVar, Union, List, cast, Optional
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
        """
        Set a column format with a formatter function.

        The `fmt()` method provides a way to execute custom formatting functionality with raw data
        values in a way that can consider all output contexts.

        Along with the `columns` and `rows` arguments that provide some precision in targeting data
        cells, the `fns` argument allows you to define one or more functions for manipulating the
        raw data.

        Parameters
        ----------
        fns : Union[FormatFn, FormatFns]
            Either a single formatting function or a named list of functions.

        columns : Union[str, List[str], None]
            The columns to target. Can either be a single column name or a series of column names
            provided in a list.

        rows : Union[int, List[int], None]
            In conjunction with `columns`, we can specify which of their rows should undergo
            formatting. The default is all rows, resulting in all rows in `columns` being formatted.
            Alternatively, we can supply a list of row indices.

        Returns
        -------
        GTData
            The GTData object is returned.
        """

        # If a single function is supplied to `fns` then
        # repackage that into a list as the `default` function
        if isinstance(fns, Callable):
            fns = FormatFns(default=fns)

        columns = _listify(columns, list)

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
    n_sigfig: Optional[int] = None,
    drop_trailing_zeros: bool = False,
    drop_trailing_dec_mark: bool = True,
    use_seps: bool = True,
    # accounting: bool = False,
    scale_by: float = 1,
    # suffixing: bool = False,
    # pattern: str = '{x}'
    sep_mark: str = ",",
    dec_mark: str = ".",
    # force_sign: bool = False,
    # system: str = 'intl',
    # locale: str = None,
) -> GTData:
    """
    Format numeric values.

    With numeric values in a **gt** table, we can perform number-based formatting so that the
    targeted values are rendered with a higher consideration for tabular presentation. Furthermore,
    there is finer control over numeric formatting with the following options:

    - decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice
    of the decimal symbol
    - digit grouping separators: options to enable/disable digit separators and provide a choice of
    separator symbol
    - scaling: we can choose to scale targeted values by a multiplier value
    - large-number suffixing: larger figures (thousands, millions, etc.) can be autoscaled and
    decorated with the appropriate suffixes
    - pattern: option to use a text pattern for decoration of the formatted values
    - locale-based formatting: providing a locale ID will result in number formatting specific to
    the chosen locale

    Parameters
    ----------
    columns : Union[str, List[str], None], optional
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None], optional
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    decimals : int, optional
        The `decimals` values corresponds to the exact number of decimal places to use. A value such
        as `2.34` can, for example, be formatted with `0` decimal places and it would result in
        `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros
        can be removed with `drop_trailing_zeros=True`. If you always need `decimals = 0`, the
        `fmt_integer()` method should be considered.

    n_sigfig : Optional[int], optional
        A option to format numbers to *n* significant figures. By default, this is `None` and thus
        number values will be formatted according to the number of decimal places set via
        `decimals`. If opting to format according to the rules of significant figures, `n_sigfig`
        must be a number greater than or equal to `1`. Any values passed to the `decimals` and
        `drop_trailing_zeros` arguments will be ignored.

    drop_trailing_zeros : bool, optional
        A boolean value that allows for removal of trailing zeros (those redundant zeros after the
        decimal mark).

    drop_trailing_dec_mark : bool, optional
        A boolean value that determines whether decimal marks should always appear even if there are
        no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By
        default trailing decimal marks are not shown.

    scale_by : float, optional
        All numeric values will be multiplied by the `scale_by` value before undergoing formatting.
        Since the `default` value is `1`, no values will be changed unless a different multiplier
        value is supplied.

    sep_mark : str, optional
        The string to use as a separator between groups of digits. For example, using `sep_mark=","`
        with a value of `1000` would result in a formatted value of `"1,000"`. This argument is
        ignored if a `locale` is supplied (i.e., is not `None`).

    dec_mark : str, optional
        The string to be used as the decimal mark. For example, using `dec_mark=","` with the value
        `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a
        `locale` is supplied (i.e., is not `None`).

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    # Generate a function that will operate on single `x` values in
    # the table body
    def fmt_number_fn(
        x: float,
        decimals: int = decimals,
        n_sigfig: Optional[int] = n_sigfig,
        drop_trailing_zeros: bool = drop_trailing_zeros,
        drop_trailing_dec_mark: bool = drop_trailing_dec_mark,
        use_seps: bool = use_seps,  # TODO: not yet implemented
        sep_mark: str = sep_mark,
        dec_mark: str = dec_mark,
        scale_by: float = scale_by,
    ):
        # Scale `x` value by a defined `scale_by` value
        x = x * scale_by

        x_formatted = _value_to_decimal_notation(
            value=x,
            decimals=decimals,
            n_sigfig=n_sigfig,
            drop_trailing_zeros=drop_trailing_zeros,
            drop_trailing_dec_mark=drop_trailing_dec_mark,
            preserve_integer=False,
            use_seps=use_seps,
            sep_mark=sep_mark,
            dec_mark=dec_mark,
        )

        return x_formatted

    FormatsAPI.fmt(self, fns=fmt_number_fn, columns=columns, rows=rows)

    return self


def fmt_integer(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    scale_by: float = 1,
) -> GTData:
    """
    Format values as integers.

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

    Parameters
    ----------
    columns : Union[str, List[str], None], optional
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None], optional
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    scale_by : float, optional
        All numeric values will be multiplied by the `scale_by` value before undergoing formatting.
        Since the `default` value is `1`, no values will be changed unless a different multiplier
        value is supplied.

    Returns
    -------
    GTData
        The GTData object is returned.
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


def _value_to_decimal_notation(
    value: Union[int, float],
    decimals: int = 2,
    n_sigfig: Optional[int] = None,
    drop_trailing_zeros: bool = False,
    drop_trailing_dec_mark: bool = True,
    preserve_integer: bool = False,
    use_seps: bool = True,
    sep_mark: str = ",",
    dec_mark: str = ".",
) -> str:
    """
    Decimal notation.

    Returns a string value with the correct precision.

    Parameters
    ----------

    value: Union[int, float]
        The number to be formatted.

    n_sigfig: int
        The number of significant digits

    drop_trailing_zeros : bool
        If True, trailing zeros in the decimal portion will be removed.

    preserve_integer: bool
        If True, all digits will be preserved when returning values that have no decimal component.
    """

    if n_sigfig:
        sig_digits, power, is_neg = _get_number_profile(value, n_sigfig)

        result = ("-" if is_neg else "") + _insert_decimal_mark(
            digits=sig_digits, power=power, dec_mark=dec_mark
        )

        if preserve_integer and not "." in result:
            result = "{:0.0f}".format(value)

    else:
        result = _format_number_fixed_decimals(
            value=value, decimals=decimals, use_seps=use_seps, sep_mark=sep_mark, dec_mark=dec_mark
        )

        # Drop any trailing zeros if option is taken (this purposefully doesn't apply to numbers
        # formatted to a specific number of significant digits)
        if drop_trailing_zeros is True:
            result = result.rstrip("0")

    # Drop the trailing decimal mark if it is present
    if drop_trailing_dec_mark is True:
        result = result.rstrip(dec_mark)

    # Add in a trailing decimal mark under specific circumstances
    if drop_trailing_dec_mark is False and not dec_mark in result:
        result = result + dec_mark

    return result


def _value_to_scientific_notation(
    value: Union[int, float],
    n_sigfig: int,
    exp_style: str,
) -> str:
    """
    Scientific notation.

    Returns a string value with the correct precision and 10s exponent. The `exp_style` text is
    placed between the decimal value and 10s exponent.

    Parameters
    ----------

    value: Union[int, float]
        The number to be formatted.

    n_sigfig: int
        The number of significant digits

    exp_style: str
        The exponent symbol to use.

    drop_trailing_zeros : bool
        If True, trailing zeros in the decimal portion will be removed.
    """

    is_neg, sig_digits, dot_power, ten_power = _get_sci_parts(value, n_sigfig)

    result = (
        ("-" if is_neg else "")
        + _insert_decimal_mark(digits=sig_digits, power=dot_power)
        + exp_style
        + str(ten_power)
    )

    return result


def _value_to_engineering_notation(value: Union[int, float], n_sigfig: int, exp_style: str) -> str:
    """
    Engineering notation.

    Returns a string value with the correct precision and an exponent that is divisible by three.
    The `exp_style` text is placed between the decimal value and the exponent.

    Parameters
    ----------

    value: Union[int, float]
        The number to be formatted.

    n_sigfig: int
        The number of significant digits

    delimiter: str
        The exponent symbol to use.

    drop_trailing_zeros : bool
        If True, trailing zeros in the decimal portion will be removed.
    """

    is_neg, sig_digits, dot_power, ten_power = _get_sci_parts(value, n_sigfig)

    eng_power = int(3 * floor(ten_power / 3))
    eng_dot = dot_power + ten_power - eng_power

    result = (
        ("-" if is_neg else "")
        + _insert_decimal_mark(digits=sig_digits, power=eng_dot)
        + exp_style
        + str(eng_power)
    )

    return result


def _format_number_fixed_decimals(
    value: Union[int, float, str],
    decimals: int,
    use_seps: bool = True,
    sep_mark: str = ",",
    dec_mark: str = ".",
) -> str:
    # If `number` is a string, cast it into a float
    if isinstance(value, str):
        value = float(value)

    fmt_spec = f".{decimals}f"

    # Get the formatted `x` value
    value = format(value, fmt_spec)

    # Very small or very large numbers can be represented in exponential
    # notation but we don't want that; we need the string value to be fully
    # expanded with zeros so if an 'e' is detected we'll use a helper function
    # to ensure it's back to a number
    if "e" in value or "E" in value:
        value = _expand_exponential_to_full_string(str_number=value)

    # Split number at `.` and obtain the integer and decimal parts
    number_parts = value.split(".")
    integer_part = number_parts[0]
    decimal_part = number_parts[1] if len(number_parts) > 1 else ""

    # Initialize formatted representations of integer and decimal parts
    formatted_integer = ""
    formatted_decimal = dec_mark + decimal_part if decimal_part else ""

    # Insert grouping separators within the integer part
    if use_seps:
        count = 0
        for digit in reversed(integer_part):
            if count and count % 3 == 0:
                formatted_integer = sep_mark + formatted_integer
            formatted_integer = digit + formatted_integer
            count += 1
    else:
        formatted_integer = integer_part

    # Combine the integer and decimal parts
    formatted_number = formatted_integer + formatted_decimal

    return formatted_number


def _expand_exponential_to_full_string(str_number: str) -> str:
    decimal_number = Decimal(str_number)
    formatted_number = "{:f}".format(decimal_number)
    return formatted_number


def _get_number_profile(value: Union[int, float], n_sigfig: int) -> tuple[str, int, bool]:
    """
    Get key components of a number for decimal number formatting.

    Returns a tuple containing: (1) a string value of significant digits, (2) an
    exponent to get the decimal mark to the proper location, and (3) a boolean
    value that's True if the value is less than zero (i.e., negative).
    """
    value = float(value)
    is_neg = value < 0
    value = abs(value)

    if value == 0:
        sig_digits = str(("0" * n_sigfig))
        power = -(1 - n_sigfig)
    else:
        power = -1 * floor(log10(value)) + n_sigfig - 1
        value_power = value * 10.0**power

        if value < 1 and floor(log10(int(round(value_power)))) > floor(log10(int(value_power))):
            power -= 1

        sig_digits = str(int(round(value * 10.0**power)))

    return sig_digits, int(-power), is_neg


def _get_sci_parts(value: Union[int, float], n_sigfig: int) -> tuple[bool, str, int, int]:
    """
    Returns the properties for constructing a number in scientific notation.
    """

    value = float(value)
    sig_digits, power, is_neg = _get_number_profile(value, n_sigfig)

    dot_power = -(n_sigfig - 1)
    ten_power = power + n_sigfig - 1

    return is_neg, sig_digits, dot_power, ten_power


def _insert_decimal_mark(digits: str, power: int, dec_mark: str = ".") -> str:
    """
    Places the decimal mark in the correct location within the digits.

    Should the decimal mark be outside the numeric range, zeros will be added.
    If `drop_trailing_zeros` is True, trailing decimal zeros will be removed.

    Examples:
      _insert_decimal_mark("123",   2, False) => "12300"
      _insert_decimal_mark("123",  -2, False) => "1.23"
      _insert_decimal_mark("123",   3, False) => "0.123"
      _insert_decimal_mark("123",   5, False) => "0.00123"
      _insert_decimal_mark("120",   0, False) => "120."
      _insert_decimal_mark("1200", -2, False) => "12.00"
      _insert_decimal_mark("1200", -2, True ) => "12"
      _insert_decimal_mark("1200", -1, False) => "120.0"
      _insert_decimal_mark("1200", -1, True ) => "120"
    """

    if power > 0:
        out = digits + "0" * power

    elif power < 0:
        power = abs(power)
        n_sigfig = len(digits)

        if power < n_sigfig:
            out = digits[:-power] + dec_mark + digits[-power:]

        else:
            out = "0" + dec_mark + "0" * (power - n_sigfig) + digits

    else:
        out = digits + (dec_mark if digits[-1] == "0" and len(digits) > 1 else "")

    return out


def _listify(
    x: Union[T, List[T], None],
    default: Callable[[], List[T]],
) -> List[T]:
    """
    Convert the input into a list.

    Parameters
    ----------

    x : Union[T, List[T], None]

        The input value to be converted into a list. It can be a single value of type T, a list of
        values of type T, or None.

    default : Callable[[], List[T]]

        A callable that returns a default list when the input value is None.

    Returns
    -------

    List[T]: The converted list.

    Raises:
        None

    Examples:
        _listify(5, lambda: [1, 2, 3])  # Output: [5]
        _listify([1, 2, 3], lambda: [4, 5, 6])  # Output: [1, 2, 3]
        _listify(None, lambda: ['a', 'b', 'c'])  # Output: ['a', 'b', 'c']
    """
    if x is None:
        return default()
    elif not isinstance(x, list):
        return [x]
    else:
        return cast(Any, x)
