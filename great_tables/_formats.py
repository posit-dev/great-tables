from __future__ import annotations
from decimal import Decimal
from typing import Any, Callable, TypeVar, Union, List, cast, Optional
from ._tbl_data import n_rows
from ._gt_data import GTData, FormatFns, FormatFn, FormatInfo
from ._locale import _get_locales_data, _get_default_locales_data, _get_currencies_data
from ._text import _md_html
import re
import pandas as pd
import math

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
    pattern: str = "{x}",
    sep_mark: str = ",",
    dec_mark: str = ".",
    force_sign: bool = False,
    # system: str = "intl",
    locale: Union[str, None] = None,
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
    columns : Union[str, List[str], None]
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None]
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    decimals : int
        The `decimals` values corresponds to the exact number of decimal places to use. A value such
        as `2.34` can, for example, be formatted with `0` decimal places and it would result in
        `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros
        can be removed with `drop_trailing_zeros=True`. If you always need `decimals = 0`, the
        `fmt_integer()` method should be considered.

    n_sigfig : Optional[int]
        A option to format numbers to *n* significant figures. By default, this is `None` and thus
        number values will be formatted according to the number of decimal places set via
        `decimals`. If opting to format according to the rules of significant figures, `n_sigfig`
        must be a number greater than or equal to `1`. Any values passed to the `decimals` and
        `drop_trailing_zeros` arguments will be ignored.

    drop_trailing_zeros : bool
        A boolean value that allows for removal of trailing zeros (those redundant zeros after the
        decimal mark).

    drop_trailing_dec_mark : bool
        A boolean value that determines whether decimal marks should always appear even if there are
        no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By
        default trailing decimal marks are not shown.

    use_seps : bool
        The `use_seps` option allows for the use of digit group separators. The type of digit group
        separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This
        setting is `True` by default.

    scale_by : float
        All numeric values will be multiplied by the `scale_by` value before undergoing formatting.
        Since the `default` value is `1`, no values will be changed unless a different multiplier
        value is supplied.

    pattern : str
        A formatting pattern that allows for decoration of the formatted value. The formatted value
        is represented by the `{x}` (which can be used multiple times, if needed) and all other
        characters will be interpreted as string literals.

    sep_mark : str
        The string to use as a separator between groups of digits. For example, using `sep_mark=","`
        with a value of `1000` would result in a formatted value of `"1,000"`. This argument is
        ignored if a `locale` is supplied (i.e., is not `None`).

    dec_mark : str
        The string to be used as the decimal mark. For example, using `dec_mark=","` with the value
        `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a
        `locale` is supplied (i.e., is not `None`).

    force_sign : bool
        Should the positive sign be shown for positive values (effectively showing a sign for all
        values except zero)? If so, use `True` for this option. The default is `False`, where only
        negative numbers will display a minus sign. This option is disregarded when using accounting
        notation with `accounting = True`.

    locale : str
        An optional locale identifier that can be used for formatting values according the locale's
        rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    # Stop if `locale` does not have a valid value; normalize locale and resolve one
    # that might be set globally
    _validate_locale(locale=locale)
    locale = _normalize_locale(locale=locale)

    # Use locale-based marks if a locale ID is provided
    sep_mark = _get_locale_sep_mark(default=sep_mark, use_seps=use_seps, locale=locale)
    dec_mark = _get_locale_dec_mark(default=dec_mark, locale=locale)

    # Generate a function that will operate on single `x` values in the table body
    def fmt_number_fn(
        x: float,
        decimals: int = decimals,
        n_sigfig: Optional[int] = n_sigfig,
        drop_trailing_zeros: bool = drop_trailing_zeros,
        drop_trailing_dec_mark: bool = drop_trailing_dec_mark,
        use_seps: bool = use_seps,
        scale_by: float = scale_by,
        sep_mark: str = sep_mark,
        dec_mark: str = dec_mark,
        force_sign: bool = force_sign,
    ):
        # Scale `x` value by a defined `scale_by` value
        x = x * scale_by

        # Determine whether the value is positive
        is_negative = _has_negative_value(value=x)

        x_formatted = _value_to_decimal_notation(
            value=x,
            decimals=decimals,
            n_sigfig=n_sigfig,
            drop_trailing_zeros=drop_trailing_zeros,
            drop_trailing_dec_mark=drop_trailing_dec_mark,
            use_seps=use_seps,
            sep_mark=sep_mark,
            dec_mark=dec_mark,
            force_sign=force_sign,
        )

        # Implement minus sign replacement for `x_formatted`
        if is_negative:
            minus_mark = _context_minus_mark()
            x_formatted = _replace_minus(x_formatted, minus_mark=minus_mark)

        # Use a supplied pattern specification to decorate the formatted value
        if pattern != "{x}":
            x_formatted = pattern.replace("{x}", x_formatted)

        return x_formatted

    FormatsAPI.fmt(self, fns=fmt_number_fn, columns=columns, rows=rows)

    return self


def fmt_integer(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    use_seps: bool = True,
    scale_by: float = 1,
    pattern: str = "{x}",
    sep_mark: str = ",",
    force_sign: bool = False,
    locale: Union[str, None] = None,
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
    columns : Union[str, List[str], None]
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None]
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    use_seps : bool
        The `use_seps` option allows for the use of digit group separators. The type of digit group
        separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This
        setting is `True` by default.

    scale_by : float
        All numeric values will be multiplied by the `scale_by` value before undergoing formatting.
        Since the `default` value is `1`, no values will be changed unless a different multiplier
        value is supplied.

    pattern : str
        A formatting pattern that allows for decoration of the formatted value. The formatted value
        is represented by the `{x}` (which can be used multiple times, if needed) and all other
        characters will be interpreted as string literals.

    sep_mark : str
        The string to use as a separator between groups of digits. For example, using `sep_mark=","`
        with a value of `1000` would result in a formatted value of `"1,000"`. This argument is
        ignored if a `locale` is supplied (i.e., is not `None`).

    force_sign : bool
        Should the positive sign be shown for positive values (effectively showing a sign for all
        values except zero)? If so, use `True` for this option. The default is `False`, where only
        negative numbers will display a minus sign. This option is disregarded when using accounting
        notation with `accounting = True`.

    locale : str
        An optional locale identifier that can be used for formatting values according the locale's
        rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    # Stop if `locale` does not have a valid value; normalize locale and resolve one
    # that might be set globally
    _validate_locale(locale=locale)
    locale = _normalize_locale(locale=locale)

    # Use locale-based marks if a locale ID is provided
    sep_mark = _get_locale_sep_mark(default=sep_mark, use_seps=use_seps, locale=locale)

    # Generate a function that will operate on single `x` values in
    # the table body
    def fmt_integer_fn(
        x: float,
        scale_by: float = scale_by,
    ):
        # Scale `x` value by a defined `scale_by` value
        x = x * scale_by

        # Determine whether the value is positive
        is_negative = _has_negative_value(value=x)

        x_formatted = _value_to_decimal_notation(
            value=x,
            decimals=0,
            n_sigfig=None,
            drop_trailing_zeros=False,
            drop_trailing_dec_mark=True,
            use_seps=use_seps,
            sep_mark=sep_mark,
            dec_mark="not used",
            force_sign=force_sign,
        )

        # Implement minus sign replacement for `x_formatted`
        if is_negative:
            minus_mark = _context_minus_mark()
            x_formatted = _replace_minus(x_formatted, minus_mark=minus_mark)

        # Use a supplied pattern specification to decorate the formatted value
        if pattern != "{x}":
            x_formatted = pattern.replace("{x}", x_formatted)

        return x_formatted

    FormatsAPI.fmt(self, fns=fmt_integer_fn, columns=columns, rows=rows)

    return self


def fmt_scientific(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    decimals: int = 2,
    n_sigfig: Optional[int] = None,
    drop_trailing_zeros: bool = False,
    drop_trailing_dec_mark: bool = True,
    scale_by: float = 1,
    exp_style: str = "x10n",
    pattern: str = "{x}",
    sep_mark: str = ",",
    dec_mark: str = ".",
    force_sign_m: bool = False,
    force_sign_n: bool = False,
    locale: Union[str, None] = None,
) -> GTData:
    """
    Format values to scientific notation.

    With numeric values in a **gt** table, we can perform formatting so that the targeted values are
    rendered in scientific notation, where extremely large or very small numbers can be expressed in
    a more practical fashion. Here, numbers are written in the form of a mantissa (`m`) and an
    exponent (`n`) with the construction *m* x 10^*n* or *m*E*n*. The mantissa component is a number
    between `1` and `10`. For instance, `2.5 x 10^9` can be used to represent the value
    2,500,000,000 in scientific notation. In a similar way, 0.00000012 can be expressed as
    `1.2 x 10^-7`. Due to its ability to describe numbers more succinctly and its ease of
    calculation, scientific notation is widely employed in scientific and technical domains.

    We have fine control over the formatting task, with the following options:

    - decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice
    of the decimal symbol
    - scaling: we can choose to scale targeted values by a multiplier value
    - pattern: option to use a text pattern for decoration of the formatted values
    - locale-based formatting: providing a locale ID will result in formatting specific to the
    chosen locale

    Parameters
    ----------
    columns : Union[str, List[str], None]
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None]
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    decimals : int
        The `decimals` values corresponds to the exact number of decimal places to use. A value such
        as `2.34` can, for example, be formatted with `0` decimal places and it would result in
        `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros
        can be removed with `drop_trailing_zeros=True`. If you always need `decimals = 0`, the
        `fmt_integer()` method should be considered.

    n_sigfig : Optional[int]
        A option to format numbers to *n* significant figures. By default, this is `None` and thus
        number values will be formatted according to the number of decimal places set via
        `decimals`. If opting to format according to the rules of significant figures, `n_sigfig`
        must be a number greater than or equal to `1`. Any values passed to the `decimals` and
        `drop_trailing_zeros` arguments will be ignored.

    drop_trailing_zeros : bool
        A boolean value that allows for removal of trailing zeros (those redundant zeros after the
        decimal mark).

    drop_trailing_dec_mark : bool
        A boolean value that determines whether decimal marks should always appear even if there are
        no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By
        default trailing decimal marks are not shown.

    scale_by : float
        All numeric values will be multiplied by the `scale_by` value before undergoing formatting.
        Since the `default` value is `1`, no values will be changed unless a different multiplier
        value is supplied.

    exp_style : str
        Style of formatting to use for the scientific notation formatting. By default this is
        `"x10n"` but other options include using a single letter (e.g., `"e"`, `"E"`, etc.), a
        letter followed by a `"1"` to signal a minimum digit width of one, or `"low-ten"` for using
        a stylized `"10"` marker.

    pattern : str
        A formatting pattern that allows for decoration of the formatted value. The formatted value
        is represented by the `{x}` (which can be used multiple times, if needed) and all other
        characters will be interpreted as string literals.

    sep_mark : str
        The string to use as a separator between groups of digits. For example, using `sep_mark=","`
        with a value of `1000` would result in a formatted value of `"1,000"`. This argument is
        ignored if a `locale` is supplied (i.e., is not `None`).

    dec_mark : str
        The string to be used as the decimal mark. For example, using `dec_mark=","` with the value
        `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a
        `locale` is supplied (i.e., is not `None`).

    force_sign_m : bool
        Should the plus sign be shown for positive values of the mantissa (first component)? This
        would effectively show a sign for all values except zero on the first numeric component of
        the notation. If so, use `True` (the default for this is `False`), where only negative
        numbers will display a sign.

    force_sign_n : bool
        Should the plus sign be shown for positive values of the exponent (second component)? This
        would effectively show a sign for all values except zero on the second numeric component of
        the notation. If so, use `True` (the default for this is `False`), where only negative
        numbers will display a sign.

    locale : str
        An optional locale identifier that can be used for formatting values according the locale's
        rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    # Set a default value for `use_seps`; these separators are only used for very
    # large exponent values
    use_seps = True

    # Stop if `locale` does not have a valid value; normalize locale and resolve one
    # that might be set globally
    _validate_locale(locale=locale)
    locale = _normalize_locale(locale=locale)

    # Use locale-based marks if a locale ID is provided
    sep_mark = _get_locale_sep_mark(default=sep_mark, use_seps=use_seps, locale=locale)
    dec_mark = _get_locale_dec_mark(default=dec_mark, locale=locale)

    # Generate a function that will operate on single `x` values in the table body
    def fmt_scientific_fn(
        x: float,
        decimals: int = decimals,
        n_sigfig: Optional[int] = n_sigfig,
        drop_trailing_zeros: bool = drop_trailing_zeros,
        drop_trailing_dec_mark: bool = drop_trailing_dec_mark,
        scale_by: float = scale_by,
        exp_style: str = exp_style,
        sep_mark: str = sep_mark,
        dec_mark: str = dec_mark,
        force_sign_m: bool = force_sign_m,
        force_sign_n: bool = force_sign_n,
    ):
        # Scale `x` value by a defined `scale_by` value
        x = x * scale_by

        # Determine whether the value is positive
        is_positive = _has_positive_value(value=x)

        minus_mark = _context_minus_mark()

        x_sci_notn = _value_to_scientific_notation(
            value=x,
            decimals=decimals,
            n_sigfig=n_sigfig,
            dec_mark=dec_mark,
        )

        sci_parts = x_sci_notn.split("E")

        m_part = sci_parts[0]
        n_part = sci_parts[1]

        # Remove trailing zeros and decimal marks from the `m_part`
        if drop_trailing_zeros:
            m_part = m_part.rstrip("0")
        if drop_trailing_dec_mark:
            m_part = m_part.rstrip(".")

        # Force the positive sign to be present if the `force_sign_m` option is taken
        if is_positive and force_sign_m:
            m_part = "+" + m_part

        if exp_style == "x10n":
            # Define the exponent string based on the `exp_style` that is the default
            # ('x10n'); this is styled as 'x 10^n' instead of using a fixed symbol like 'E'

            # Determine which values don't require the (x 10^n) for scientific formatting
            # since their order would be zero
            small_pos = _has_sci_order_zero(value=x)

            # Force the positive sign to be present if the `force_sign_n` option is taken
            if force_sign_n and not _str_detect(n_part, "-"):
                n_part = "+" + n_part

            # Implement minus sign replacement for `m_part` and `n_part`
            m_part = _replace_minus(m_part, minus_mark=minus_mark)
            n_part = _replace_minus(n_part, minus_mark=minus_mark)

            if small_pos:
                # If the value is small enough to not require the (x 10^n) notation, then
                # the formatted value is based on only the `m_part`
                x_formatted = m_part
            else:
                # Get the set of exponent marks, which are used to decorate the `n_part`
                exp_marks = _context_exp_marks()

                # Create the formatted string based on `exp_marks` and the two `sci_parts`
                x_formatted = m_part + exp_marks[0] + n_part + exp_marks[1]

        else:
            # Define the exponent string based on the `exp_style` that's not the default
            # value of 'x10n'

            exp_str = _context_exp_str(exp_style=exp_style)

            n_min_width = 1 if _str_detect(exp_style, r"^[a-zA-Z]1$") else 2

            # The `n_part` will be extracted here and it must be padded to
            # the defined minimum number of decimal places
            if _str_detect(n_part, "-"):
                n_part = _str_replace(n_part, "-", "")
                n_part = n_part.ljust(n_min_width, "0")
                n_part = "-" + n_part
            else:
                n_part = n_part.ljust(n_min_width, "0")
                if force_sign_n:
                    n_part = "+" + n_part

            # Implement minus sign replacement for `m_part` and `n_part`
            m_part = _replace_minus(m_part, minus_mark=minus_mark)
            n_part = _replace_minus(n_part, minus_mark=minus_mark)

            x_formatted = m_part + exp_str + n_part

        return x_formatted

    FormatsAPI.fmt(self, fns=fmt_scientific_fn, columns=columns, rows=rows)

    return self


def fmt_engineering(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    decimals: int = 2,
    drop_trailing_zeros: bool = False,
    drop_trailing_dec_mark: bool = True,
    scale_by: float = 1,
    exp_style: str = "x10n",
    pattern: str = "{x}",
    sep_mark: str = ",",
    dec_mark: str = ".",
    force_sign_m: bool = False,
    force_sign_n: bool = False,
    locale: Union[str, None] = None,
):
    # TODO: Not implemented yet
    return self


def fmt_percent(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    decimals: int = 2,
    drop_trailing_zeros: bool = False,
    drop_trailing_dec_mark: bool = True,
    scale_values: bool = True,
    use_seps: bool = True,
    # accounting: bool = False,
    pattern: str = "{x}",
    sep_mark: str = ",",
    dec_mark: str = ".",
    force_sign: bool = False,
    placement: str = "right",
    incl_space: bool = False,
    # system: str = "intl",
    locale: Union[str, None] = None,
) -> GTData:
    """
    Format values as a percentage.

    With numeric values in a **gt** table, we can perform percentage-based formatting. It is assumed
    the input numeric values are proportional values and, in this case, the values will be
    automatically multiplied by `100` before decorating with a percent sign (the other case is
    accommodated though setting `scale_values` to `False`). For more control over percentage
    formatting, we can use the following options:

    - percent sign placement: the percent sign can be placed after or before the values and a space
    can be inserted between the symbol and the value.
    - decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice
    of the decimal symbol
    - digit grouping separators: options to enable/disable digit separators and provide a choice of
    separator symbol
    - value scaling toggle: choose to disable automatic value scaling in the situation that values
    are already scaled coming in (and just require the percent symbol)
    - pattern: option to use a text pattern for decoration of the formatted values
    - locale-based formatting: providing a locale ID will result in number formatting specific to
    the chosen locale

    Parameters
    ----------
    columns : Union[str, List[str], None]
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None]
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    decimals : int
        The `decimals` values corresponds to the exact number of decimal places to use. A value such
        as `2.34` can, for example, be formatted with `0` decimal places and it would result in
        `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros
        can be removed with `drop_trailing_zeros=True`. If you always need `decimals = 0`, the
        `fmt_integer()` method should be considered.

    drop_trailing_zeros : bool
        A boolean value that allows for removal of trailing zeros (those redundant zeros after the
        decimal mark).

    drop_trailing_dec_mark : bool
        A boolean value that determines whether decimal marks should always appear even if there are
        no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By
        default trailing decimal marks are not shown.

    scale_values : bool
        Should the values be scaled through multiplication by 100? By default this scaling is
        performed since the expectation is that incoming values are usually proportional. Setting to
        `False` signifies that the values are already scaled and require only the percent sign when
        formatted.

    use_seps : bool
        The `use_seps` option allows for the use of digit group separators. The type of digit group
        separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This
        setting is `True` by default.

    pattern : str
        A formatting pattern that allows for decoration of the formatted value. The formatted value
        is represented by the `{x}` (which can be used multiple times, if needed) and all other
        characters will be interpreted as string literals.

    sep_mark : str
        The string to use as a separator between groups of digits. For example, using `sep_mark=","`
        with a value of `1000` would result in a formatted value of `"1,000"`. This argument is
        ignored if a `locale` is supplied (i.e., is not `None`).

    dec_mark : str
        The string to be used as the decimal mark. For example, using `dec_mark=","` with the value
        `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a
        `locale` is supplied (i.e., is not `None`).

    force_sign : bool
        Should the positive sign be shown for positive values (effectively showing a sign for all
        values except zero)? If so, use `True` for this option. The default is `False`, where only
        negative numbers will display a minus sign. This option is disregarded when using accounting
        notation with `accounting = True`.

    placement : str
        This option governs the placement of the percent sign. This can be either be `"right"` (the
        default) or `"left"`.

    incl_space : bool
        An option for whether to include a space between the value and the percent sign. The default
        is to not introduce a space character.

    locale : str
        An optional locale identifier that can be used for formatting values according the locale's
        rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    # Stop if `locale` does not have a valid value; normalize locale and resolve one
    # that might be set globally
    _validate_locale(locale=locale)
    locale = _normalize_locale(locale=locale)

    # Use locale-based marks if a locale ID is provided
    sep_mark = _get_locale_sep_mark(default=sep_mark, use_seps=use_seps, locale=locale)
    dec_mark = _get_locale_dec_mark(default=dec_mark, locale=locale)

    if scale_values:
        scale_by = 100.0
    else:
        scale_by = 1.0

    # Generate a function that will operate on single `x` values in the table body
    def fmt_percent_fn(
        x: float,
        decimals: int = decimals,
        drop_trailing_zeros: bool = drop_trailing_zeros,
        drop_trailing_dec_mark: bool = drop_trailing_dec_mark,
        use_seps: bool = use_seps,
        scale_by: float = scale_by,
        sep_mark: str = sep_mark,
        dec_mark: str = dec_mark,
        force_sign: bool = force_sign,
        placement: str = placement,
        incl_space: bool = incl_space,
    ):
        # Scale `x` value by a defined `scale_by` value
        x = x * scale_by

        # Determine properties of the value
        is_negative = _has_negative_value(value=x)
        is_positive = _has_positive_value(value=x)

        x_formatted = _value_to_decimal_notation(
            value=x,
            decimals=decimals,
            n_sigfig=None,
            drop_trailing_zeros=drop_trailing_zeros,
            drop_trailing_dec_mark=drop_trailing_dec_mark,
            use_seps=use_seps,
            sep_mark=sep_mark,
            dec_mark=dec_mark,
            force_sign=force_sign,
        )

        # Create a percent pattern for affixing the percent sign
        space_character = " " if incl_space else ""
        percent_pattern = (
            f"{{x}}{space_character}%" if placement == "right" else f"%{space_character}{{x}}"
        )

        if is_negative and placement == "left":
            x_formatted = x_formatted.replace("-", "")
            x_formatted = percent_pattern.replace("{x}", x_formatted)
            x_formatted = "-" + x_formatted
        elif is_positive and force_sign and placement == "left":
            x_formatted = x_formatted.replace("+", "")
            x_formatted = percent_pattern.replace("{x}", x_formatted)
            x_formatted = "+" + x_formatted
        else:
            x_formatted = percent_pattern.replace("{x}", x_formatted)

        # Implement minus sign replacement for `x_formatted`
        if is_negative:
            minus_mark = _context_minus_mark()
            x_formatted = _replace_minus(x_formatted, minus_mark=minus_mark)

        # Use a supplied pattern specification to decorate the formatted value
        if pattern != "{x}":
            x_formatted = pattern.replace("{x}", x_formatted)

        return x_formatted

    FormatsAPI.fmt(self, fns=fmt_percent_fn, columns=columns, rows=rows)

    return self


def fmt_currency(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    currency: Optional[int] = None,
    use_subunits: bool = True,
    decimals: Optional[int] = None,
    drop_trailing_dec_mark: bool = True,
    use_seps: bool = True,
    # accounting: bool = False,
    scale_by: float = 1,
    # suffixing: bool = False,
    pattern: str = "{x}",
    sep_mark: str = ",",
    dec_mark: str = ".",
    force_sign: bool = False,
    placement: str = "left",
    incl_space: bool = False,
    # system: str = "intl",
    locale: Union[str, None] = None,
) -> GTData:
    """
    Format values as currencies.

    With numeric values in a **gt** table, we can perform currency-based formatting with the
    `fmt_currency()` method. This supports both automatic formatting with a three-letter currency
    code. We have fine control over the conversion from numeric values to currency values, where we
    could take advantage of the following options:

    - the currency: providing a currency code or common currency name will procure the correct
    currency symbol and number of currency subunits
    - currency symbol placement: the currency symbol can be placed before or after the values
    - decimals/subunits: choice of the number of decimal places, and a choice of the decimal symbol,
    and an option on whether to include or exclude the currency subunits (the decimal portion)
    - digit grouping separators: options to enable/disable digit separators and provide a choice of
    separator symbol
    - scaling: we can choose to scale targeted values by a multiplier value
    - pattern: option to use a text pattern for decoration of the formatted currency values
    - locale-based formatting: providing a locale ID will result in currency formatting specific to
    the chosen locale; it will also retrieve the locale's currency if none is explicitly given

    Parameters
    ----------
    columns : Union[str, List[str], None]
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None]
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    currency : Union[str, None]
        The currency to use for the numeric value. This input can be supplied as a 3-letter currency
        code (e.g., `"USD"` for U.S. Dollars, `"EUR"` for the Euro currency).

    use_subunits: bool
        An option for whether the subunits portion of a currency value should be displayed. For
        example, with an input value of `273.81`, the default formatting will produce `"$273.81"`.
        Removing the subunits (with `use_subunits = False`) will give us `"$273"`.

    decimals : int
        The `decimals` values corresponds to the exact number of decimal places to use. This value
        is optional as a currency has an intrinsic number of decimal places (i.e., the subunits).
        A value such as `2.34` can, for example, be formatted with `0` decimal places and if the
        currency used is `"USD"` it would result in `"$2"`. With `4` decimal places, the formatted
        value becomes `"$2.3400"`.

    drop_trailing_dec_mark : bool
        A boolean value that determines whether decimal marks should always appear even if there are
        no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By
        default trailing decimal marks are not shown.

    use_seps : bool
        The `use_seps` option allows for the use of digit group separators. The type of digit group
        separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This
        setting is `True` by default.

    scale_by : float
        All numeric values will be multiplied by the `scale_by` value before undergoing formatting.
        Since the `default` value is `1`, no values will be changed unless a different multiplier
        value is supplied.

    pattern : str
        A formatting pattern that allows for decoration of the formatted value. The formatted value
        is represented by the `{x}` (which can be used multiple times, if needed) and all other
        characters will be interpreted as string literals.

    sep_mark : str
        The string to use as a separator between groups of digits. For example, using `sep_mark=","`
        with a value of `1000` would result in a formatted value of `"1,000"`. This argument is
        ignored if a `locale` is supplied (i.e., is not `None`).

    dec_mark : str
        The string to be used as the decimal mark. For example, using `dec_mark=","` with the value
        `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a
        `locale` is supplied (i.e., is not `None`).

    force_sign : bool
        Should the positive sign be shown for positive values (effectively showing a sign for all
        values except zero)? If so, use `True` for this option. The default is `False`, where only
        negative numbers will display a minus sign. This option is disregarded when using accounting
        notation with `accounting = True`.

    placement : str
        The placement of the currency symbol. This can be either be `"left"` (as in `"$450"`) or
        `"right"` (which yields `"450$"`).

    incl_space : bool
        An option for whether to include a space between the value and the currency symbol. The
        default is to not introduce a space character.

    locale : str
        An optional locale identifier that can be used for formatting values according the locale's
        rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    # Stop if `locale` does not have a valid value; normalize locale and resolve one
    # that might be set globally
    _validate_locale(locale=locale)
    locale = _normalize_locale(locale=locale)

    # Use locale-based marks if a locale ID is provided
    sep_mark = _get_locale_sep_mark(default=sep_mark, use_seps=use_seps, locale=locale)
    dec_mark = _get_locale_dec_mark(default=dec_mark, locale=locale)

    # Resolve the currency either from direct input in `currency` or through a locale
    if currency is None:
        # If not providing a `currency` code, we can obtain the currency code from the locale
        currency_resolved = _get_locale_currency_code(locale=locale)
    else:
        # Cast the `currency` value to a string
        currency_resolved = str(currency)
        # Stop if `currency_resolved` does not have a valid value
        _validate_currency(currency=currency_resolved)

    # Get the number of decimal places for the currency; this takes into account whether
    # the currency uses subunits or not and whether decimals are explicitly set
    decimals = _get_currency_decimals(
        currency=currency_resolved, decimals=decimals, use_subunits=use_subunits
    )

    # Generate a function that will operate on single `x` values in the table body
    def fmt_currency_fn(
        x: float,
        currency: str = currency_resolved,
        decimals: int = decimals,
        drop_trailing_dec_mark: bool = drop_trailing_dec_mark,
        use_seps: bool = use_seps,
        scale_by: float = scale_by,
        sep_mark: str = sep_mark,
        dec_mark: str = dec_mark,
        force_sign: bool = force_sign,
        placement: str = placement,
        incl_space: bool = incl_space,
    ):
        # Scale `x` value by a defined `scale_by` value
        x = x * scale_by

        # Determine properties of the value
        is_negative = _has_negative_value(value=x)
        is_positive = _has_positive_value(value=x)

        # Get the currency symbol on the basis of a valid currency code
        currency_symbol = _get_currency_str(currency=currency)

        # Format the value to decimal notation; this is done before the currency symbol is
        # affixed to the value
        x_formatted = _value_to_decimal_notation(
            value=x,
            decimals=decimals,
            n_sigfig=None,
            drop_trailing_zeros=False,
            drop_trailing_dec_mark=drop_trailing_dec_mark,
            use_seps=use_seps,
            sep_mark=sep_mark,
            dec_mark=dec_mark,
            force_sign=force_sign,
        )

        # Create a currency pattern for affixing the currency symbol
        space_character = " " if incl_space else ""
        currency_pattern = (
            f"{{x}}{space_character}{currency_symbol}"
            if placement == "right"
            else f"{currency_symbol}{space_character}{{x}}"
        )

        if is_negative and placement == "left":
            x_formatted = x_formatted.replace("-", "")
            x_formatted = currency_pattern.replace("{x}", x_formatted)
            x_formatted = "-" + x_formatted
        elif is_positive and force_sign and placement == "left":
            x_formatted = x_formatted.replace("+", "")
            x_formatted = currency_pattern.replace("{x}", x_formatted)
            x_formatted = "+" + x_formatted
        else:
            x_formatted = currency_pattern.replace("{x}", x_formatted)

        # Implement minus sign replacement for `x_formatted`
        if is_negative:
            minus_mark = _context_minus_mark()
            x_formatted = _replace_minus(x_formatted, minus_mark=minus_mark)

        # Use a supplied pattern specification to decorate the formatted value
        if pattern != "{x}":
            x_formatted = pattern.replace("{x}", x_formatted)

        return x_formatted

    FormatsAPI.fmt(self, fns=fmt_currency_fn, columns=columns, rows=rows)

    return self


def fmt_bytes(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    standard: str = "decimal",
    decimals: int = 1,
    n_sigfig: Optional[int] = None,
    drop_trailing_zeros: bool = True,
    drop_trailing_dec_mark: bool = True,
    use_seps: bool = True,
    pattern: str = "{x}",
    sep_mark: str = ",",
    dec_mark: str = ".",
    force_sign: bool = False,
    incl_space: bool = True,
    locale: Union[str, None] = None,
) -> GTData:
    """
    Format values as bytes.

    With numeric values in a table, we can transform those to values of bytes with human readable
    units. The `fmt_bytes()` method allows for the formatting of byte sizes to either of two common
    representations: (1) with decimal units (powers of 1000, examples being `"kB"` and `"MB"`), and
    (2) with binary units (powers of 1024, examples being `"KiB"` and `"MiB"`). It is assumed the
    input numeric values represent the number of bytes and automatic truncation of values will
    occur. The numeric values will be scaled to be in the range of 1 to <1000 and then decorated
    with the correct unit symbol according to the standard chosen. For more control over the
    formatting of byte sizes, we can use the following options:

    - decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice
    of the decimal symbol
    - digit grouping separators: options to enable/disable digit separators and provide a choice of
    separator symbol
    - pattern: option to use a text pattern for decoration of the formatted values
    - locale-based formatting: providing a locale ID will result in number formatting specific to
    the chosen locale

    Parameters
    ----------
    columns : Union[str, List[str], None]
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None]
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    standard: str
        The form of expressing large byte sizes is divided between: (1) decimal units (powers of
        1000; e.g., `"kB"` and `"MB"`), and (2) binary units (powers of 1024; e.g., `"KiB"` and
        `"MiB"`). The default is to use decimal units with the `"decimal"` option. The alternative
        is to use binary units with the `"binary"` option.

    decimals : int
        This corresponds to the exact number of decimal places to use. A value such as `2.34` can,
        for example, be formatted with `0` decimal places and it would result in `"2"`. With `4`
        decimal places, the formatted value becomes `"2.3400"`. The trailing zeros can be removed
        with `drop_trailing_zeros=True`.

    drop_trailing_zeros : bool
        A boolean value that allows for removal of trailing zeros (those redundant zeros after the
        decimal mark).

    drop_trailing_dec_mark : bool
        A boolean value that determines whether decimal marks should always appear even if there are
        no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By
        default trailing decimal marks are not shown.

    use_seps : bool
        The `use_seps` option allows for the use of digit group separators. The type of digit group
        separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This
        setting is `True` by default.

    pattern : str
        A formatting pattern that allows for decoration of the formatted value. The formatted value
        is represented by the `{x}` (which can be used multiple times, if needed) and all other
        characters will be interpreted as string literals.

    sep_mark : str
        The string to use as a separator between groups of digits. For example, using `sep_mark=","`
        with a value of `1000` would result in a formatted value of `"1,000"`. This argument is
        ignored if a `locale` is supplied (i.e., is not `None`).

    dec_mark : str
        The string to be used as the decimal mark. For example, using `dec_mark=","` with the value
        `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a
        `locale` is supplied (i.e., is not `None`).

    force_sign : bool
        Should the positive sign be shown for positive values (effectively showing a sign for all
        values except zero)? If so, use `True` for this option. The default is `False`, where only
        negative numbers will display a minus sign. This option is disregarded when using accounting
        notation with `accounting = True`.

    incl_space : bool
        An option for whether to include a space between the value and the currency symbol. The
        default is to not introduce a space character.

    locale : str
        An optional locale identifier that can be used for formatting values according the locale's
        rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    # Stop if `locale` does not have a valid value; normalize locale and resolve one
    # that might be set globally
    _validate_locale(locale=locale)
    locale = _normalize_locale(locale=locale)

    # Use locale-based marks if a locale ID is provided
    sep_mark = _get_locale_sep_mark(default=sep_mark, use_seps=use_seps, locale=locale)
    dec_mark = _get_locale_dec_mark(default=dec_mark, locale=locale)

    # Stop if `n_sigfig` does not have a valid value
    if n_sigfig is not None:
        _validate_n_sigfig(n_sigfig=n_sigfig)

    # Get the `base` value and the `byte_units` list based on the `standard` value
    if standard == "decimal":
        # This is the 'decimal' standard (the default)
        base = 1000
        byte_units = ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    else:
        # This is the 'binary' standard
        base = 1024
        byte_units = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]

    # Generate a function that will operate on single `x` values in the table body
    def fmt_bytes_fn(
        x: float,
        base: int = base,
        byte_units: str = byte_units,
        decimals: int = decimals,
        n_sigfig: Optional[int] = n_sigfig,
        drop_trailing_zeros: bool = drop_trailing_zeros,
        drop_trailing_dec_mark: bool = drop_trailing_dec_mark,
        use_seps: bool = use_seps,
        sep_mark: str = sep_mark,
        dec_mark: str = dec_mark,
        force_sign: bool = force_sign,
        incl_space: bool = incl_space,
    ):
        # Truncate all byte values by casting to an integer; this is done because bytes
        # are always whole numbers
        x = int(x)

        # Determine properties of the value
        is_negative = _has_negative_value(value=x)
        is_positive = _has_positive_value(value=x)

        # Determine the power index for the value
        if x == 0:
            # If the value is zero, then the power index is 1; otherwise, we'd get
            # an error when trying to calculate the log of zero
            num_power_idx = 1
        else:
            # Otherwise, we can calculate the power index by taking the log of the value
            # and dividing by the log of the base; we add 1 to the result to account for
            # the fact that the power index is 1-based (i.e., the first element in the
            # `byte_units` list is at index 0) --- the final statement ensures that the
            # power index is always at least 1
            num_power_idx = math.floor(math.log(abs(x), base)) + 1
            num_power_idx = max(1, min(len(byte_units), num_power_idx))

        # The `units_str` is obtained by indexing the `byte_units` list with the `num_power_idx`
        # value; this is the string that will be affixed to the formatted value
        units_str = byte_units[num_power_idx - 1]

        # Scale `x` value by a defined `base` value, this is done by dividing by the
        # `base` value raised to the power index minus 1 (we subtract 1 because the
        # power index is 1-based)
        x = x / base ** (num_power_idx - 1)

        # Format the value to decimal notation; this is done before the `byte_units` text
        # is affixed to the value
        x_formatted = _value_to_decimal_notation(
            value=x,
            decimals=decimals,
            n_sigfig=n_sigfig,
            drop_trailing_zeros=drop_trailing_zeros,
            drop_trailing_dec_mark=drop_trailing_dec_mark,
            use_seps=use_seps,
            sep_mark=sep_mark,
            dec_mark=dec_mark,
            force_sign=force_sign,
        )

        # Create a `bytes_pattern` object for affixing the `units_str`, which is the
        # string that represents the byte units
        space_character = " " if incl_space else ""
        bytes_pattern = f"{{x}}{space_character}{units_str}"

        x_formatted = bytes_pattern.replace("{x}", x_formatted)

        # Implement minus sign replacement for `x_formatted`
        if is_negative:
            minus_mark = _context_minus_mark()
            x_formatted = _replace_minus(x_formatted, minus_mark=minus_mark)

        # Use a supplied pattern specification to decorate the formatted value
        if pattern != "{x}":
            x_formatted = pattern.replace("{x}", x_formatted)

        return x_formatted

    FormatsAPI.fmt(self, fns=fmt_bytes_fn, columns=columns, rows=rows)

    return self


def fmt_roman(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
    case: str = "upper",
    pattern: str = "{x}",
):
    """
    Format values as Roman numerals.

    With numeric values in a **gt** table we can transform those to Roman numerals, rounding values
    as necessary.

    Parameters
    ----------
    columns : Union[str, List[str], None]
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None]
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    case : str
        Should Roman numerals should be rendered as uppercase (`"upper"`) or lowercase (`"lower"`)
        letters? By default, this is set to `"upper"`.

    pattern : str
        A formatting pattern that allows for decoration of the formatted value. The formatted value
        is represented by the `{x}` (which can be used multiple times, if needed) and all other
        characters will be interpreted as string literals.

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    # Check that the `case` value is valid and only consists of the string 'upper' or 'lower'
    _validate_case(case=case)

    # Generate a function that will operate on single `x` values in the table body
    def fmt_roman_fn(
        x: float,
        case: str = case,
    ):
        # Get the absolute value of `x` so that negative values are handled
        x = abs(x)

        # Round x to 0 digits with the R-H-U method of rounding (for reproducibility purposes)
        x = _round_rhu(x, 0)

        # Determine if `x` is in the range of 1 to 3899 and if it is zero
        x_is_in_range = x > 0 and x < 3900
        x_is_zero = x == 0

        if not x_is_in_range and not x_is_zero:
            # We cannot format a 'large' integer to roman numerals, so we return a string
            # that indicates this
            return "ex terminis"
        elif x_is_zero:
            # Zero is a special case and is handled separately with the character 'N'
            # which stands for 'nulla' (i.e., 'nothing')
            x_formatted = "N"
        else:
            # All other values are formatted with the `_as_roman()` utility function
            x_formatted = _as_roman(x)

        # Transform the case of the formatted value
        if case == "upper":
            pass
        else:
            x_formatted = x_formatted.lower()

        # Use a supplied pattern specification to decorate the formatted value
        if pattern != "{x}":
            x_formatted = pattern.replace("{x}", x_formatted)

        return x_formatted

    FormatsAPI.fmt(self, fns=fmt_roman_fn, columns=columns, rows=rows)

    return self


def fmt_markdown(
    self: GTData,
    columns: Union[str, List[str], None] = None,
    rows: Union[int, List[int], None] = None,
) -> GTData:
    """
    Format Markdown text.

    Any Markdown-formatted text in the incoming cells will be transformed during render when using
    the `fmt_markdown()` method.

    Parameters
    ----------
    columns : Union[str, List[str], None]
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.

    rows : Union[int, List[int], None]
        In conjunction with `columns`, we can specify which of their rows should undergo formatting.
        The default is all rows, resulting in all rows in `columns` being formatted. Alternatively,
        we can supply a list of row indices.

    Returns
    -------
    GTData
        The GTData object is returned.
    """

    # Generate a function that will operate on single `x` values in the table body
    def fmt_markdown_fn(x: Any) -> str:
        x_str: str = str(x)

        x_formatted = _md_html(x_str)

        return x_formatted

    FormatsAPI.fmt(self, fns=fmt_markdown_fn, columns=columns, rows=rows)

    return self


def _value_to_decimal_notation(
    value: Union[int, float],
    decimals: int = 2,
    n_sigfig: Optional[int] = None,
    drop_trailing_zeros: bool = False,
    drop_trailing_dec_mark: bool = True,
    use_seps: bool = True,
    sep_mark: str = ",",
    dec_mark: str = ".",
    force_sign: bool = False,
) -> str:
    """
    Decimal notation.

    Returns a string value with the correct precision or fixed number of decimal places (with
    optional formatting of the decimal part).
    """

    is_positive = value > 0

    if n_sigfig:
        # If there is a value provided to `n_sigfig` then number formatting proceeds through the
        # significant digits pathway, which ignores `decimals` and any removal of trailing zero values
        # in the decimal portion of the value
        result = _format_number_n_sigfig(
            value=value,
            n_sigfig=n_sigfig,
            use_seps=use_seps,
            sep_mark=sep_mark,
            dec_mark=dec_mark,
            preserve_integer=False,
        )

    else:
        # If there is nothing provided to `n_sigfig` then the conventional decimal number formatting
        # pathway is taken; this formats to a specific number of decimal places and removal of
        # trailing zero values can be undertaken
        result = _format_number_fixed_decimals(
            value=value,
            decimals=decimals,
            drop_trailing_zeros=drop_trailing_zeros,
            use_seps=use_seps,
            sep_mark=sep_mark,
            dec_mark=dec_mark,
        )

    # Drop the trailing decimal mark if it is present
    if drop_trailing_dec_mark is True:
        result = result.rstrip(dec_mark)

    # Add in a trailing decimal mark under specific circumstances
    if drop_trailing_dec_mark is False and not dec_mark in result:
        result = result + dec_mark

    # Force the positive sign to be present if the `force_sign` option is taken
    if is_positive and force_sign:
        result = "+" + result

    return result


def _value_to_scientific_notation(
    value: Union[int, float],
    decimals: int = 2,
    n_sigfig: Optional[int] = None,
    dec_mark: str = ".",
) -> str:
    """
    Scientific notation.

    Returns a string value with the correct precision and 10s exponent. An 'E' is placed between
    the decimal value and 10s exponent.
    """

    # Transform value of `decimals` to `n_sigfig`
    if n_sigfig:
        pass
    else:
        n_sigfig = decimals + 1

    is_negative, sig_digits, dot_power, ten_power = _get_sci_parts(value, n_sigfig)

    result = (
        ("-" if is_negative else "")
        + _insert_decimal_mark(digits=sig_digits, power=dot_power, dec_mark=dec_mark)
        + "E"
        + str(ten_power)
    )

    return result


def _value_to_engineering_notation(value: Union[int, float], n_sigfig: int, exp_style: str) -> str:
    """
    Engineering notation.

    Returns a string value with the correct precision and an exponent that is divisible by three.
    The `exp_style` text is placed between the decimal value and the exponent.
    """

    is_negative, sig_digits, dot_power, ten_power = _get_sci_parts(value, n_sigfig)

    eng_power = int(3 * math.floor(ten_power / 3))
    eng_dot = dot_power + ten_power - eng_power

    result = (
        ("-" if is_negative else "")
        + _insert_decimal_mark(digits=sig_digits, power=eng_dot)
        + exp_style
        + str(eng_power)
    )

    return result


def _format_number_n_sigfig(
    value: Union[int, float],
    n_sigfig: int,
    use_seps: bool = True,
    sep_mark: str = ",",
    dec_mark: str = ".",
    preserve_integer: bool = False,
) -> str:
    sig_digits, power, is_negative = _get_number_profile(value, n_sigfig)

    formatted_value = ("-" if is_negative else "") + _insert_decimal_mark(
        digits=sig_digits, power=power, dec_mark="."
    )

    # Get integer and decimal parts
    # Split number at `.` and obtain the integer and decimal parts
    number_parts = formatted_value.split(".")
    integer_part = number_parts[0]
    decimal_part = number_parts[1] if len(number_parts) > 1 else ""

    # Initialize formatted representations of integer and decimal parts
    formatted_integer = ""
    formatted_decimal = dec_mark + decimal_part if decimal_part else ""

    if preserve_integer and not "." in formatted_value:
        formatted_value = "{:0.0f}".format(value)

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
    result = formatted_integer + formatted_decimal

    return result


def _format_number_fixed_decimals(
    value: Union[int, float],
    decimals: int,
    drop_trailing_zeros: bool = False,
    use_seps: bool = True,
    sep_mark: str = ",",
    dec_mark: str = ".",
) -> str:
    # If `number` is a string, cast it into a float
    if isinstance(value, str):
        value = float(value)

    is_negative = value < 0

    fmt_spec = f".{decimals}f"

    # Get the formatted `x` value
    value_str = format(value, fmt_spec)

    # Very small or very large numbers can be represented in exponential
    # notation but we don't want that; we need the string value to be fully
    # expanded with zeros so if an 'e' is detected we'll use a helper function
    # to ensure it's back to a number
    if "e" in value_str or "E" in value_str:
        value_str = _expand_exponential_to_full_string(str_number=value_str)

    # Split number at `.` and obtain the integer and decimal parts
    number_parts = value_str.split(".")
    integer_part = number_parts[0].lstrip("-")
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

    # Add back the negative sign if the number is negative
    if is_negative:
        formatted_integer = "-" + formatted_integer

    # Combine the integer and decimal parts
    result = formatted_integer + formatted_decimal

    # Drop any trailing zeros if option is taken (this purposefully doesn't apply to numbers
    # formatted to a specific number of significant digits)
    if drop_trailing_zeros is True:
        result = result.rstrip("0")

    return result


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
    is_negative = value < 0
    value = abs(value)

    if value == 0:
        sig_digits = str(("0" * n_sigfig))
        power = -(1 - n_sigfig)
    else:
        power = -1 * math.floor(math.log10(value)) + n_sigfig - 1
        value_power = value * 10.0**power

        if value < 1 and math.floor(math.log10(int(round(value_power)))) > math.floor(
            math.log10(int(value_power))
        ):
            power -= 1

        sig_digits = str(int(round(value * 10.0**power)))

    return sig_digits, int(-power), is_negative


def _get_sci_parts(value: Union[int, float], n_sigfig: int) -> tuple[bool, str, int, int]:
    """
    Returns the properties for constructing a number in scientific notation.
    """

    value = float(value)
    sig_digits, power, is_negative = _get_number_profile(value, n_sigfig)

    dot_power = -(n_sigfig - 1)
    ten_power = power + n_sigfig - 1

    return is_negative, sig_digits, dot_power, ten_power


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


def _has_negative_value(value: Union[int, float]) -> bool:
    return value < 0


def _has_positive_value(value: Union[int, float]) -> bool:
    return value > 0


def _has_zero_value(value: Union[int, float]) -> bool:
    return value == 0


def _has_sci_order_zero(value: Union[int, float]) -> bool:
    return (value >= 1 and value < 10) or (value <= -1 and value > -10) or value == 0


def _context_exp_marks() -> List[str]:
    return [" \u00D7 10<sup style='font-size: 65%;'>", "</sup>"]


def _context_exp_str(exp_style: str) -> str:
    if exp_style == "low-ten":
        # For the 'low-ten' style, use a specialized `exp_str` string value
        exp_str = "<sub style='font-size: 65%;'>10</sub>"

    elif _str_detect(exp_style, "^[a-zA-Z]{1}1?$"):
        # If there is a single letter (or a letter and a '1') then
        # use that letter as the `exp_str` value
        exp_str = exp_style[0]

    else:
        # Use `E` if none of the above conditions are met
        exp_str = "E"

    return exp_str


def _context_minus_mark() -> str:
    return "\u2212"


def _replace_minus(string: str, minus_mark: str) -> str:
    return _str_replace(string, "-", minus_mark)


def _str_replace(string: str, pattern: str, replace: str):
    return string.replace(pattern, replace)


def _str_detect(string: str, pattern: str):
    return re.match(pattern, string)


def _filter_pd_df_to_row(pd_df: pd.DataFrame, column: str, filter_expr: str) -> pd.DataFrame:
    filtered_pd_df = pd_df[pd_df[column] == filter_expr]
    if len(filtered_pd_df) != 1:
        raise Exception(
            "Internal Error, the filtered table doesn't result in a table of exactly one row."
        )
    return filtered_pd_df


def _get_locale_sep_mark(default: str, use_seps: bool, locale: Union[str, None] = None) -> str:
    # If `use_seps` is False, then force `sep_mark` to be an empty string
    if not use_seps:
        return ""

    # If `locale` is NULL then return the default `sep_mark`
    if locale is None:
        return default

    # Get the correct `group` value from the locales lookup table
    pd_df_row = _filter_pd_df_to_row(pd_df=_get_locales_data(), column="locale", filter_expr=locale)

    # Obtain a single cell value from the single row in `pd_df_row` that is below
    # the column named 'group'; this could potentially be of any type but we expect
    # it to be a string (and we'll check for that here)
    sep_mark: Any
    sep_mark = pd_df_row.iloc[0]["group"]
    if not isinstance(sep_mark, str):
        raise TypeError(f"Variable type mismatch. Expected str, got {type(sep_mark)}.")

    # Replace any `""` or "\u00a0" with `" "` since an empty string actually
    # signifies a space character, and, we want to normalize to a simple space
    sep_mark = " " if sep_mark == "" or sep_mark == "\u00a0" else sep_mark

    return sep_mark


def _get_locale_dec_mark(default: str, locale: Union[str, None] = None) -> str:
    # If `locale` is NULL then return the default `dec_mark`
    if locale is None:
        return default

    # Get the correct `decimal` value row from the locales lookup table
    pd_df_row = _filter_pd_df_to_row(pd_df=_get_locales_data(), column="locale", filter_expr=locale)

    # Obtain a single cell value from the single row in `pd_df_row` that is below
    # the column named 'decimal'; this could potentially be of any type but we expect
    # it to be a string (and we'll check for that here)
    dec_mark: Any
    dec_mark = pd_df_row.iloc[0]["decimal"]
    if not isinstance(dec_mark, str):
        raise TypeError(f"Variable type mismatch. Expected str, got {type(dec_mark)}.")

    return dec_mark


def _get_locales_list() -> List[str]:
    """
    Returns a list of locales as strings.

    Raises:
        TypeError: If the first element of the locale list is not a string.
    """

    # Get the 'locales' dataset and obtain from that a list of locales
    locales = _get_locales_data()
    locale_list = locales["locale"].tolist()

    # Ensure that `locale_list` is of the type 'str'
    locale_list: Any
    if not isinstance(locale_list[0], str):
        raise TypeError("Variable type mismatch. Expected str, got something entirely different.")
    return locale_list


def _get_default_locales_list() -> List[str]:
    """
    Returns a list of default locales.

    The function retrieves the default locales data and extracts the default locale list.
    It ensures that the list is of type 'str' and raises a TypeError if not.

    Returns:
        A list of default locales as strings.
    """

    # Get the 'default locales' dataset and obtain from that a list of default locales
    default_locales = _get_default_locales_data()
    default_locale_list = default_locales["default_locale"].tolist()

    # Ensure that `default_locale_list` is of the type 'str'
    default_locale_list: Any
    if not isinstance(default_locale_list[0], str):
        raise TypeError("Variable type mismatch. Expected str, got something entirely different.")

    return default_locale_list


def _validate_locale(locale: Union[str, None] = None) -> None:
    """
    Validates the given locale string against a list of supported locales.

    Args:
        locale (str or None): The locale string to validate. If None, the function returns without
        doing anything.

    Raises:
        ValueError: If the supplied `locale` is not available in the list of supported locales.
    """

    # If `locale` is None then return without doing anything (nothing to validate)
    if locale is None:
        return

    locales_list = _get_locales_list()
    default_locales_list = _get_default_locales_list()

    # Replace any underscores with hyphens
    supplied_locale = _str_replace(locale, "_", "-")

    # Stop if the `locale` provided isn't a valid one
    if supplied_locale not in locales_list and supplied_locale not in default_locales_list:
        raise ValueError("The supplied `locale` is not available in the list of supported locales.")

    return


def _normalize_locale(locale: Union[str, None] = None) -> Union[str, None]:
    """
    Normalize the given locale string by replacing any underscores with hyphens and resolving any default locales into their base names.

    Args:
        locale (str or None): The locale string to normalize. If None, returns None.

    Returns:
        str or None: The normalized locale string, or None if the input was None.

    Raises:
        TypeError: If the resolved locale is not of type 'str'.
    """

    # If `locale` is None then return None (we don't need to normalize anything here)
    if locale is None:
        return None

    # Replace any underscores with hyphens
    supplied_locale = _str_replace(locale, "_", "-")

    # Resolve any default locales into their base names (e.g., 'en-US' -> 'en')
    if supplied_locale in _get_default_locales_list():
        default_locales = _get_default_locales_data()
        resolved_locale = default_locales[
            default_locales["default_locale"] == supplied_locale
        ].iloc[0]["base_locale"]

        # Ensure that `resolved_locale` is of the type 'str'
        resolved_locale: Any
        if not isinstance(resolved_locale, str):
            raise TypeError(
                "Variable type mismatch. Expected str, got something entirely different."
            )
    else:
        resolved_locale = supplied_locale

    return resolved_locale


def _get_locale_currency_code(locale: Union[str, None] = None) -> str:
    """
    Given a locale, returns the corresponding currency code. If no locale is provided,
    returns the currency code for the United States ('USD').

    Args:
        locale (str or None): A string representing the locale for which to retrieve the
            currency code. If None, the currency code for the United States ('USD') is returned.

    Returns:
        str: A string representing the currency code for the specified locale.

    Raises:
        TypeError: If the currency code is not a string.

    """

    # If `locale` is None then return `"USD"`
    if locale is None:
        return "USD"

    # Get the correct 'locale' value row from the `__x_locales` lookup table
    pd_df_row = _filter_pd_df_to_row(pd_df=_get_locales_data(), column="locale", filter_expr=locale)

    # Extract the 'currency_code' cell value from this 1-row DataFrame
    currency_code = pd_df_row.iloc[0]["currency_code"]

    # Ensure that `currency_code` is of the type 'str'
    currency_code: Any
    if not isinstance(currency_code, str):
        raise TypeError("Variable type mismatch. Expected str, got something entirely different.")

    # If the field isn't populated, we'll obtain an empty string; in such a case we fall
    # back to using the 'USD' currency code
    if currency_code == "":
        currency_code = "USD"

    return currency_code


def _get_currency_str(currency: str) -> str:
    """
    Given a currency code, returns the corresponding currency symbol as a string.

    Args:
        currency (str): The currency code to look up.

    Returns:
        str: The currency symbol corresponding to the given currency code.

    Raises:
        TypeError: If the currency symbol is not of type 'str'.
    """

    # Get the correct 'curr_code' value row from the `__x_currencies` lookup table
    pd_df_row = _filter_pd_df_to_row(
        pd_df=_get_currencies_data(), column="curr_code", filter_expr=currency
    )

    # Extract the 'symbol' cell value from this 1-row DataFrame
    currency_str = pd_df_row.iloc[0]["symbol"]

    # Ensure that `currency_str` is of the type 'str'
    currency_str: Any
    if not isinstance(currency_str, str):
        raise TypeError("Variable type mismatch. Expected str, got something entirely different.")

    return currency_str


def _validate_currency(currency: str) -> None:
    """
    Validates if the provided currency is available in the list of supported currencies.

    Args:
    - currency (str): The currency code to validate

    Raises:
    - ValueError: If the `currency` provided isn't a valid one

    Returns:
    - None
    """

    # Get the currencies data
    currencies = _get_currencies_data()

    # Get the `curr_code` column from currencies DataFrame as a list
    curr_code_list: List[str] = currencies["curr_code"].tolist()

    # Stop if the `currency` provided isn't a valid one
    if currency not in curr_code_list:
        raise ValueError(
            "The supplied `currency` is not available in the list of supported currencies."
        )

    return


def _get_currency_decimals(currency: str, decimals: Optional[int], use_subunits: bool) -> int:
    """
    Returns the number of decimal places to use for a given currency.

    If `decimals` is not None, it is returned. Otherwise, if `use_subunits` is True,
    the number of decimal places is determined by the currency's exponent. Otherwise,
    the number of decimal places is 0.

    Args:
        currency (str): The currency code.
        decimals (Optional[int]): The number of decimal places to use, if specified.
        use_subunits (bool): Whether to use subunits for the currency.

    Returns:
        int: The number of decimal places to use.
    """

    # If `decimals` is not None, return it
    if decimals is not None:
        return decimals

    # If `decimals` is None, then we need to determine the number of decimal places
    if decimals is None and use_subunits:
        # Get the number of decimal places from the currency's exponent
        decimals = _get_currency_exponent(currency=currency)
    elif decimals is None and not use_subunits:
        # If `use_subunits` is False, then the number of decimal places is 0
        decimals = 0

    # Assert that `decimals` is not None and then return it
    assert decimals is not None
    return decimals


def _get_currency_exponent(currency: str) -> int:
    """
    Given a currency code, returns the exponent associated with that` currency.
    If the currency code is not found, returns 2 as a default value.

    Args:
        currency (str): The currency code to look up.

    Returns:
        int: The exponent associated with the currency code.
    """
    currencies = _get_currencies_data()

    # get the curr_code column from currencies df as a list
    curr_code_list: List[str] = currencies["curr_code"].tolist()

    if currency in curr_code_list:
        exponent = currencies[currencies["curr_code"] == currency].iloc[0]["exponent"]

        # Cast exponent variable as an integer value (it is a str currently)
        exponent = int(exponent)

        # Ensure that `exponent` is of the type 'int'
        exponent: Any
        if not isinstance(exponent, int):
            raise TypeError(
                "Variable type mismatch. Expected int, got something entirely different."
            )
    else:
        exponent = 2

    return exponent


def _validate_n_sigfig(n_sigfig: int) -> None:
    """
    Validates the input for the number of significant figures.

    Args:
        n_sigfig (int): The number of significant figures to validate.

    Raises:
        ValueError: If the length of `n_sigfig` is not 1, or if the value is `None` or less than 1.
        TypeError: If the input for `n_sigfig` is not an integer.

    Returns:
        None
    """

    if len(str(n_sigfig)) != 1:
        raise ValueError("The length of `n_sigfig` must be 1.")
    if n_sigfig is None:
        raise ValueError("The value for `n_sigfig` must not be `None`.")
    if not isinstance(n_sigfig, int):
        raise TypeError("Any input for `n_sigfig` must be an integer.")
    if n_sigfig < 1:
        raise ValueError("The value for `n_sigfig` must be greater than or equal to `1`.")

    return


def _round_rhu(x, digits=0):
    """
    Rounds a number using the 'Round-Half-Up' (R-H-U) algorithm.

    Args:
        x (float): The number to round.
        digits (int): The number of digits to round to.

    Returns:
        float: The rounded number.
    """

    # Multiply the number by 10^digits to move the decimal point to the right
    z = x * 10**digits

    # Add 0.5 + 2.220446049250313e-16 to the number to ensure that the number is rounded up
    z += 0.5 + math.sqrt(2.220446049250313e-16)

    # Truncate the number to remove the decimal places
    z = math.trunc(z)

    # Divide the number by 10^digits to move the decimal point back to the original position
    z /= 10**digits

    return z


def _as_roman(x: int) -> str:
    """
    Converts an integer to a Roman numeral string.

    Args:
        x (int): The integer to convert.

    Returns:
        str: The Roman numeral string representation of the integer.
    """

    roman_key_value_list = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    out = ""
    while x > 0:
        for i, r in roman_key_value_list:
            while x >= i:
                out += r
                x -= i
    return out


def _validate_case(case=str):
    """
    Validates the case argument for the `fmt_roman()` method.

    Args:
        case (str): The case argument to validate.

    Raises:
        ValueError: If the case argument is not 'upper' or 'lower'.
    """
    if case not in ["upper", "lower"]:
        raise ValueError(f"The `case` argument must be either 'upper' or 'lower' (not '{case}').")

    return
