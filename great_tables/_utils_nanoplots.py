from __future__ import annotations

import math
import random
import warnings
import zlib
from collections.abc import Callable
from dataclasses import dataclass, fields, replace
from typing import Any

from ._tbl_data import Agnostic, NpInteger, is_na
from ._utils import _flatten_list, _match_arg


def _is_na(x: Any) -> bool:
    return is_na(Agnostic(), x)


def _map_is_na(x: list[Any]) -> list[bool]:
    return [is_na(Agnostic(), val) for val in x]


def _val_is_numeric(x: Any) -> bool:
    """
    Determine whether a scalar value is numeric (i.e., either an integer or a float).
    """

    # If a list then signal a failure
    if isinstance(x, list):
        raise ValueError("The input cannot be a list. It must be a single value.")

    return isinstance(x, (int, float))


def _val_is_str(x: Any) -> bool:
    """
    Determine whether a scalar value is a string.
    """

    # If a list then signal a failure
    if isinstance(x, list):
        raise ValueError("The input cannot be a list. It must be a single value.")

    return isinstance(x, (str))


def _is_integerlike(val_list: list[Any]) -> bool:
    """
    Determine whether an entire list of values are integer-like; this skips
    over missing values and returns a single boolean.
    """

    # If the list is empty, return False
    if not val_list:
        return False

    return all((isinstance(val, (int, NpInteger)) or _is_na(val)) for val in val_list)


def _remove_na_from_list(x: list[int | float]) -> list[int | float]:
    """
    Remove missing values from a list of values.
    """

    return [val for val in x if not _is_na(val)]


def _normalize_option_list(option_list: Any | list[Any], num_y_vals: int) -> list[Any]:
    """
    Normalize an option list to have the same length as the number of `y` values.
    """

    # If `option_list` is a single value, then make it a list
    if not isinstance(option_list, list):
        option_list = [option_list]

    if len(option_list) != 1 and len(option_list) != num_y_vals:
        raise ValueError("Every option must have either length 1 or `length(y_vals)`.")

    if len(option_list) == 1:
        option_list = [option_list[0]] * num_y_vals

    return option_list


def calc_ref_value(val_or_calc: float | str, data) -> int | float | str:
    if _val_is_numeric(val_or_calc):
        return val_or_calc
    elif _val_is_str(val_or_calc) and val_or_calc in REFERENCE_LINE_KEYWORDS:
        return _generate_ref_line_from_keyword(vals=data, keyword=val_or_calc)

    raise ValueError(f"Unsupported nanoplot area value: {val_or_calc}")


# Settings for `_format_number_compactly()` by magnitude of the value: each entry holds the
# (exclusive) upper bound of `abs(val)` and the `use_subunits=`, `decimals=`, `n_sigfig=`, and
# `compact=` settings; values at or above the last bound use `_COMPACT_FMT_LARGE`
_CompactFmt = tuple[bool, int | None, int, bool]

_COMPACT_FMT_SETTINGS: list[tuple[float, _CompactFmt]] = [
    (1, (True, None, 2, False)),
    (1000, (True, None, 3, False)),
    (10000, (False, 2, 3, True)),
    (100000, (False, 1, 3, True)),
    (1000000, (False, 0, 3, True)),
    (1e15, (False, 1, 3, True)),
]
_COMPACT_FMT_LARGE: _CompactFmt = (False, None, 2, False)


def _get_compact_fmt_settings(val: float, currency: str | None) -> tuple[float, _CompactFmt, bool]:
    """
    Get the value to format compactly, its settings, and whether it's at or above 1e15.

    The settings are chosen from the value as it will be displayed: a value that rounds up to
    the upper bound of its magnitude range (e.g., `999.6` with three significant figures shows
    as `1,000`) is replaced by the bound and uses the settings of the next range, so it's
    formatted exactly like the bound itself (`1.00K`).
    """

    from great_tables._formats import _get_currency_decimals, _rounds_up_to

    i = next(
        (i for i, (bound, _) in enumerate(_COMPACT_FMT_SETTINGS) if abs(val) < bound),
        len(_COMPACT_FMT_SETTINGS),
    )

    while i < len(_COMPACT_FMT_SETTINGS):
        bound, (use_subunits, decimals, n_sigfig, compact) = _COMPACT_FMT_SETTINGS[i]

        # Compact values are rounded after scaling to their suffix (K, M, B, T)
        scale = 1000 ** min(4, math.floor(math.log(abs(val), 1000))) if compact else 1
        scale = max(1, scale)

        # The currency path rounds to a number of decimals, the number path to `n_sigfig=`
        if currency is not None:
            rounding = dict(
                decimals=_get_currency_decimals(currency, decimals, use_subunits), n_sigfig=None
            )
        else:
            rounding = dict(decimals=0, n_sigfig=n_sigfig)

        if not _rounds_up_to(val / scale, threshold=bound / scale, **rounding):
            return val, _COMPACT_FMT_SETTINGS[i][1], False

        val = math.copysign(bound, val)
        i += 1

    return val, _COMPACT_FMT_LARGE, True


def _format_number_compactly(
    val: float,
    currency: str | None = None,
    as_integer: bool = False,
    fn: Callable[..., str] | None = None,
) -> str:
    """
    Format a single numeric value compactly, using a currency if provided.
    """

    from great_tables.vals import fmt_currency, fmt_integer, fmt_number, fmt_scientific

    if fn is not None and isinstance(fn, Callable):
        res = fn(val)

        # Check whether the result is a single string value; if not, raise an error
        if not isinstance(res, str):
            raise ValueError("The result of the formatting function must be a single string value.")

        return res

    if _is_na(val):
        return "NA"

    if val == 0:
        return "0"

    val, (use_subunits, decimals, n_sigfig, compact), is_large = _get_compact_fmt_settings(
        val, currency=currency
    )

    if currency is not None:
        if is_large:
            # Values this large are shown as a bound (`>$1Q`, or `<−$1Q` for negative values)
            val_formatted = fmt_currency(
                math.copysign(1e15, val),
                currency=currency,
                use_subunits=False,
                decimals=0,
                compact=True,
            )
            return (">" if val > 0 else "<") + val_formatted[0]

        val_formatted = fmt_currency(
            val, currency=currency, use_subunits=use_subunits, decimals=decimals, compact=compact
        )

    elif abs(val) < 0.01 or is_large:
        val_formatted = fmt_scientific(val, exp_style="E", n_sigfig=n_sigfig, decimals=1)

    elif as_integer and -100 < val < 100:
        val_formatted = fmt_integer(val)

    else:
        val_formatted = fmt_number(val, n_sigfig=n_sigfig, decimals=1, compact=compact)

    return val_formatted[0]


#
# Collection of general functions to calculate the mean, min, max, median,
# and other statistical measures from a list of values; the list should not
# be expected to contain any missing values so we won't guard against them here
#


def _gt_mean(x: list[int | float]) -> float:
    """
    Calculate the mean of a list of values.
    """

    return sum(x) / len(x)


def _gt_min(x: list[int | float]) -> int | float:
    """
    Calculate the minimum value from a list of values.
    """
    return min(x)


def _gt_max(x: list[int | float]) -> int | float:
    """
    Calculate the maximum value from a list of values.
    """
    return max(x)


def _gt_median(x: list[int | float]) -> int | float:
    """
    Calculate the median of a list of values.
    """
    x.sort()
    n = len(x)
    if n % 2 == 0:
        return (x[n // 2 - 1] + x[n // 2]) / 2
    else:
        return x[n // 2]


def _gt_first(x: list[int | float]) -> int | float:
    """
    Get the first value from a list of values.
    """
    return x[0]


def _gt_last(x: list[int | float]) -> int | float:
    """
    Get the last value from a list of values.
    """
    return x[-1]


def _gt_quantile(x: list[int | float], q: float) -> int | float:
    """
    Calculate the quantile of a list of values.
    """
    x.sort()
    n = len(x)
    return x[int(n * q)]


def _gt_q1(x: list[int | float]) -> float:
    """
    Calculate the first quartile of a list of values.
    """
    return _gt_quantile(x, 0.25)


def _gt_q3(x: list[int | float]) -> float:
    """
    Calculate the third quartile of a list of values.
    """
    return _gt_quantile(x, 0.75)


# The keywords that can be used for a reference line (or for the bounds of a reference area),
# mapped to the functions computing their values
_REFERENCE_LINE_FNS: dict[str, Callable[[list[int | float]], int | float]] = {
    "mean": _gt_mean,
    "median": _gt_median,
    "min": _gt_min,
    "max": _gt_max,
    "q1": _gt_q1,
    "q3": _gt_q3,
}

REFERENCE_LINE_KEYWORDS = list(_REFERENCE_LINE_FNS)


def _get_extreme_value(
    *args: float | list[int | float] | None,
    stat: str = "max",
) -> int | float:
    """
    Get either the maximum or minimum value from a collection of numeric values and lists of
    numeric values; `None` and missing values are ignored.
    """

    # Ensure that `stat` is either 'max' or 'min'
    _match_arg(stat, lst=["max", "min"])

    val_list = _flatten_list([val for val in args if val is not None])
    val_list = [val for val in _remove_na_from_list(val_list) if val is not None]

    return max(val_list) if stat == "max" else min(val_list)


def _generate_ref_line_from_keyword(vals: list[int | float], keyword: str) -> int | float:
    """
    Generate a value for a reference line from a valid keyword (one of `REFERENCE_LINE_KEYWORDS`)
    using the non-missing values in `vals`.
    """

    _match_arg(x=keyword, lst=REFERENCE_LINE_KEYWORDS)

    # This is a new list, so `vals` isn't changed by the functions that sort in place
    non_missing_vals = _remove_na_from_list(vals)

    if not non_missing_vals:
        raise ValueError(
            f"A reference line of `{keyword}` needs at least one value that isn't missing."
        )

    return _REFERENCE_LINE_FNS[keyword](non_missing_vals)


def _normalize_vals(x: list[int] | list[float] | list[int | float]) -> list[float | None]:
    """
    Normalize a list of numeric values to be between 0 and 1. Account for missing values.
    """

    x_missing = [i for i, val in enumerate(x) if _is_na(val)]
    mean_x: float = sum(val for val in x if not _is_na(val)) / sum(
        1 for val in x if not _is_na(val)
    )
    x: list[float] = [mean_x if _is_na(val) else val for val in x]
    min_attr: float = min(x)
    max_attr: float = max(x)
    xmin: list[float] = [val - min_attr for val in x]
    xover_diff: list[float] = [x / (max_attr - min_attr) for x in xmin]
    return [None if i in x_missing else val for i, val in enumerate(xover_diff)]


def _jitter_vals(x: list[int | float], amount: float) -> list[int | float]:
    """
    Jitter a list of numeric values by a small amount.
    """

    return [val + random.uniform(-amount, amount) for val in x]


def _normalize_to_dict(
    **kwargs: float | list[int | float] | None,
) -> dict[str, list[float | None]]:
    """
    Normalize a collection of numeric values to be between 0 and 1. Account for missing values.
    This only accepts values (scalar or list) associated with keyword arguments. A dictionary
    is returned with the same keys but the values are normalized lists. This is done so that
    any disparate collection of normalized values are distinguishable by their original keys.

    All values (lists are flattened, scalars treated as length-1) are pooled together before
    normalization, so that every returned value is scaled relative to the global min/max across
    all inputs. Keyword arguments with a `None` value are left out of the normalization and out of
    the returned dictionary.

    Examples
    --------
    ```{python}
    # Case 1: line/area plot - y values with zero line and expand_y bounds
    _normalize_to_dict(vals=[5, 10, 15, 20], zero=0, expand_y=[0, 25])
    # {'vals': [0.2, 0.4, 0.6, 0.8], 'zero': [0.0], 'expand_y': [0.0, 1.0]}

    # Case 2: line plot - y values with a reference line
    _normalize_to_dict(vals=[5, 10, 15, 20], ref_line=12, zero=0, expand_y=[0, 25])
    # {'vals': [0.2, 0.4, 0.6, 0.8], 'ref_line': [0.48], 'zero': [0.0], 'expand_y': [0.0, 1.0]}

    # Case 3: line plot - y values with a reference area (band between two bounds)
    _normalize_to_dict(vals=[5, 10, 15, 20], ref_area_l=8, ref_area_u=17, zero=0, expand_y=[0, 25])
    # {'vals': [0.2, 0.4, 0.6, 0.8], 'ref_area_l': [0.32], 'ref_area_u': [0.68],
    #  'zero': [0.0], 'expand_y': [0.0, 1.0]}

    # Case 4: line plot - x values with expand_x bounds
    _normalize_to_dict(vals=[1, 2, 3, 4], expand_x=[0, 5])
    # {'vals': [0.2, 0.4, 0.6, 0.8], 'expand_x': [0.0, 1.0]}

    # Case 5: bar plot - single value normalized against all row values with zero baseline
    _normalize_to_dict(val=[15], all_vals=[5, 10, 15, 20, -5], zero=0)
    # {'val': [0.8], 'all_vals': [0.4, 0.6, 0.8, 1.0, 0.0], 'zero': [0.2]}
    ```
    """

    # Ensure that at least two values are provided
    if len(kwargs) < 2:
        raise ValueError("At least two values must be provided.")

    args = {key: val for key, val in kwargs.items() if val is not None}

    # Pool all values together (a scalar counts as a single value)
    arg_lens = [len(val) if type(val) is list else 1 for val in args.values()]
    all_vals = _flatten_list(list(args.values()))

    # If all values are the same, then jitter the values
    if len(set(all_vals)) == 1:
        all_vals = _jitter_vals(all_vals, 0.1)

    normalized_vals = _normalize_vals(all_vals)

    # Split the normalized values back into the original structure of `args`
    normalized = {}
    start = 0
    for key, arg_len in zip(args, arg_lens):
        normalized[key] = normalized_vals[start : start + arg_len]
        start += arg_len

    return normalized


def _is_whole_number(x: float) -> bool:
    return float(x).is_integer()


def _is_intlike(n: Any, scaled_by: float = 1e17) -> bool:
    """
    https://stackoverflow.com/a/71373152
    """
    import numbers
    from decimal import Decimal

    if isinstance(n, str):
        try:
            # Replacement of minus sign (U+2212) with hyphen (necessary in some locales)
            n = float(n.replace("−", "-"))
        except ValueError:
            return False
    elif isinstance(n, Decimal):
        n = float(n)
    return (
        isinstance(n, numbers.Real)
        and not math.isnan(n)
        and ((n * scaled_by - int(n) * scaled_by) == 0)
    )


def _get_n_intlike(nums: list[Any]) -> int:
    return len([n for n in nums if _is_intlike(n)])


def _remove_exponent(n: str | float) -> str:
    """
    https://docs.python.org/3/library/decimal.html#decimal-faq
    """
    from decimal import Decimal, InvalidOperation

    if isinstance(n, str):
        # Replacement of minus sign (U+2212) with hyphen (necessary in some locales)
        n = n.replace("−", "-")

    # TODO: note that in the nanoplot code, this function only runs when
    # GT believes everything is an integer. However, _format_number_compactly
    # may have run on each value and formatted them compactly (e.g. 7045 to "704K")
    # The InvalidOperation catch prevents errors on compact numbers, but is a
    # hacky patch. We need to consolidate the processing steps run for value
    # formatting.
    try:
        d = Decimal(n)
        if d == d.to_integral():
            x = d.quantize(Decimal(1))
        else:
            x = d.normalize()
        return str(int(x))
    except InvalidOperation:
        return str(n)


# ---------------------------------------------------------------------------------------------
# Nanoplot options
# ---------------------------------------------------------------------------------------------

# Options that can be given per data point (as a list with one value per `y` value)
_PER_POINT_OPTIONS = (
    "data_point_radius",
    "data_point_stroke_color",
    "data_point_stroke_width",
    "data_point_fill_color",
    "data_bar_stroke_color",
    "data_bar_stroke_width",
    "data_bar_fill_color",
)


@dataclass(frozen=True)
class _NanoplotOptions:
    """The styling and layer options of a nanoplot (see `nanoplot_options()`).

    The options in `_PER_POINT_OPTIONS` can be a single value or a list with one value per data
    point; `per_point()` turns all of them into lists."""

    data_point_radius: int | list[int] = 10
    data_point_stroke_color: str | list[str] = "#FFFFFF"
    data_point_stroke_width: int | list[int] = 4
    data_point_fill_color: str | list[str] = "#FF0000"
    data_line_stroke_color: str = "#4682B4"
    data_line_stroke_width: int = 8
    data_area_fill_color: str = "#FF0000"
    data_bar_stroke_color: str | list[str] = "#3290CC"
    data_bar_stroke_width: int | list[int] = 4
    data_bar_fill_color: str | list[str] = "#3FB5FF"
    data_bar_negative_stroke_color: str = "#CC3243"
    data_bar_negative_stroke_width: int = 4
    data_bar_negative_fill_color: str = "#D75A68"
    reference_line_color: str = "#75A8B0"
    reference_area_fill_color: str = "#A6E6F2"
    vertical_guide_stroke_color: str = "#911EB4"
    vertical_guide_stroke_width: int = 12
    show_data_points: bool = True
    show_data_line: bool = True
    show_data_area: bool = True
    show_reference_line: bool = True
    show_reference_area: bool = True
    show_vertical_guides: bool = True
    show_y_axis_guide: bool = True
    interactive_data_values: bool = True
    currency: str | None = None
    y_val_fmt_fn: Callable[..., str] | None = None
    y_axis_fmt_fn: Callable[..., str] | None = None
    y_ref_line_fmt_fn: Callable[..., str] | None = None

    def per_point(self, num_y_vals: int) -> _NanoplotOptions:
        """Expand each option in `_PER_POINT_OPTIONS` to a list of length `num_y_vals`."""

        return replace(
            self,
            **{
                name: _normalize_option_list(getattr(self, name), num_y_vals=num_y_vals)
                for name in _PER_POINT_OPTIONS
            },
        )

    def hide_layers(self) -> _NanoplotOptions:
        """Turn off every optional layer (all `show_*` options)."""

        return replace(self, **{f.name: False for f in fields(self) if f.name.startswith("show_")})

    def format(self, val: float, as_integer: bool, fn: Callable[..., str] | None) -> str:
        """Format a value for display with the `currency` option and the formatting function `fn`
        (e.g., `y_val_fmt_fn`)."""

        return _format_number_compactly(val, currency=self.currency, as_integer=as_integer, fn=fn)


# ---------------------------------------------------------------------------------------------
# Canvas
# ---------------------------------------------------------------------------------------------

# Safe zones around the data area, on the left/right and on the top/bottom
_SAFE_X_D = 50
_SAFE_Y_D = 15

# Height of the data area, and of the whole plot (in SVG units)
_DATA_Y_HEIGHT = 100
_BOTTOM_Y = _SAFE_Y_D + _DATA_Y_HEIGHT + _SAFE_Y_D

# Width of the data area when the data points aren't evenly spaced (i.e., for plots with `x`
# values, single-value plots, and box plots)
_FIXED_DATA_X_WIDTH = 600

_ZERO_LINE_STROKE_COLOR = "#BFBFBF"
_ZERO_LINE_STROKE_WIDTH = 4

# Bars for `0` values are drawn as a thin gray line
_ZERO_BAR_COLOR = "#808080"
_ZERO_BAR_STROKE_WIDTH = 4


def _point_spacing(num_y_vals: int) -> int:
    """The horizontal distance between evenly spaced data points, which shrinks as the number of
    points grows."""

    for max_num_y_vals, spacing in ((20, 50), (30, 40), (40, 30), (50, 25)):
        if num_y_vals <= max_num_y_vals:
            return spacing

    return 20


@dataclass(frozen=True)
class _Canvas:
    """The horizontal extent of a nanoplot, in SVG units.

    `x_d` is the distance between evenly spaced data points, and is `None` when the points aren't
    evenly spaced."""

    data_x_width: int
    x_d: int | None = None

    @classmethod
    def create(cls, num_y_vals: int, evenly_spaced: bool) -> _Canvas:
        if not evenly_spaced:
            return cls(data_x_width=_FIXED_DATA_X_WIDTH)

        x_d = _point_spacing(num_y_vals)

        return cls(data_x_width=num_y_vals * x_d, x_d=x_d)

    @property
    def viewbox(self) -> str:
        return f"0 0 {_SAFE_X_D + self.data_x_width + _SAFE_X_D} {_BOTTOM_Y}"

    def x_pos(self, proportion: float) -> float:
        """Map a proportion of the data area's width to an `x` position."""
        return (self.data_x_width * proportion) + _SAFE_X_D


def _y_pos(proportion: float) -> float:
    """Map a proportion of the data area's height (from the bottom) to a `y` position."""
    return _SAFE_Y_D + ((1 - proportion) * _DATA_Y_HEIGHT)


# ---------------------------------------------------------------------------------------------
# Input data
# ---------------------------------------------------------------------------------------------


def _has_no_data(vals: Any) -> bool:
    """Whether `vals` is a missing value, or a list without any non-missing values."""

    if isinstance(vals, float):
        return _is_na(vals)

    return isinstance(vals, list) and (len(vals) == 0 or all(_map_is_na(vals)))


def _drop_missing_x_vals(
    x_vals: list[int | float], y_vals: list[int | float]
) -> tuple[list[int | float], list[int | float]]:
    """Remove the positions with a missing `x` value from both `x_vals` and `y_vals`."""

    keep = [not _is_na(val) for val in x_vals]

    return (
        [x for x, k in zip(x_vals, keep) if k],
        [y for y, k in zip(y_vals, keep) if k],
    )


def _handle_missing_y_vals(
    y_vals: list[int | float], x_vals: list[int | float] | None, missing_vals: str
) -> tuple[list[int | float], list[int | float] | None]:
    """Replace missing `y` values with `0` (`missing_vals="zero"`) or remove them along with their
    `x` values (`missing_vals="remove"`); other `missing_vals` options keep them."""

    if missing_vals == "zero":
        y_vals = [0 if _is_na(val) else val for val in y_vals]

    elif missing_vals == "remove":
        keep = [not _is_na(val) for val in y_vals]
        y_vals = [y for y, k in zip(y_vals, keep) if k]

        if x_vals is not None:
            x_vals = [x for x, k in zip(x_vals, keep) if k]

    return y_vals, x_vals


def _prepare_vals(
    y_vals: Any, x_vals: list[int | float] | None, missing_vals: str
) -> tuple[Any, list[int | float] | None] | None:
    """Clean up the `y` and `x` values (as directed by `missing_vals`); `None` is returned when there
    is nothing to plot."""

    if _has_no_data(y_vals):
        return None

    if x_vals is not None:
        if _has_no_data(x_vals):
            return None

        num_y_vals = len(y_vals) if type(y_vals) is list else 1

        if len(x_vals) != num_y_vals:
            raise ValueError(
                f"""The number of `x` and `y` values must match.
                The `x` value length is: {len(x_vals)}
                The `y` value length is: {num_y_vals}
                """
            )

        x_vals, y_vals = _drop_missing_x_vals(x_vals, y_vals)

    return _handle_missing_y_vals(y_vals, x_vals, missing_vals)


# ---------------------------------------------------------------------------------------------
# Nanoplot spec (for plots of one or more data points)
# ---------------------------------------------------------------------------------------------


def _resolve_ref_line(ref_line: float | str, y_vals: list[int | float]) -> int | float | str:
    """Compute the value of a reference line given as a keyword (e.g., `"mean"`); other values are
    returned as is."""

    if _val_is_str(ref_line) and ref_line in REFERENCE_LINE_KEYWORDS:
        return _generate_ref_line_from_keyword(vals=y_vals, keyword=ref_line)

    return ref_line


def _is_complete_ref_area(ref_area: list[Any] | None) -> bool:
    return ref_area is not None and not (_is_na(ref_area[0]) or _is_na(ref_area[1]))


def _expand_invariant_y(
    y_vals: list[int | float], expand_y: list[int | float] | None
) -> list[int | float] | None:
    """Without `expand_y`, give `y` values that are all the same a range to be centered in."""

    y_max = _get_extreme_value(y_vals, stat="max")
    y_min = _get_extreme_value(y_vals, stat="min")

    if y_min != y_max or expand_y is not None:
        return expand_y

    expand_y_dist = 5 if y_min == 0 else (y_min / 10) * 2

    return [y_min - expand_y_dist, y_min + expand_y_dist]


@dataclass(frozen=True)
class _YScale:
    """The `y` values of a nanoplot together with its reference line, reference area, and zero
    line, all on a common scale.

    `y_proportions` are proportions of the data area's height (`None` for a missing value) and the
    other `*_y` fields are `y` positions; fields of layers that aren't drawn are `None`. `y_min`
    and `y_max` are the bounds labeled on the *y*-axis guide."""

    y_proportions: list[float | None]
    y_min: int | float
    y_max: int | float
    ref_line: int | float | None = None
    ref_line_y: float | None = None
    ref_area_y_l: float | None = None
    ref_area_y_u: float | None = None
    zero_y: float | None = None

    @classmethod
    def resolve(
        cls,
        y_vals: list[int | float],
        ref_line: float | str | None,
        ref_area: list[int | float | str] | None,
        expand_y: list[int | float] | None,
        include_zero: bool,
    ) -> _YScale:
        """Compute the scale from the `y` values, an optional reference line and reference area
        (either can be a keyword such as `"mean"`), the `expand_y` bounds, and (if `include_zero`)
        the zero line."""

        if ref_line is not None:
            ref_line = _resolve_ref_line(ref_line, y_vals)

        area_l = area_u = None
        if ref_area is not None:
            area_l, area_u = sorted([calc_ref_value(val, y_vals) for val in ref_area[:2]])

        zero = 0 if include_zero else None

        # TODO: the zero line is left out of the y-axis bounds when there are both a reference
        # line and a reference area (but not otherwise), which is likely unintended
        axis_zero = None if ref_line is not None and area_l is not None else zero
        axis_vals = (y_vals, ref_line, area_l, area_u, expand_y, axis_zero)

        y_max = _get_extreme_value(*axis_vals, stat="max")
        y_min = _get_extreme_value(*axis_vals, stat="min")

        proportions = _normalize_to_dict(
            vals=y_vals,
            ref_line=ref_line,
            ref_area_l=area_l,
            ref_area_u=area_u,
            zero=zero,
            expand_y=expand_y,
        )

        def y_of(key: str) -> float | None:
            return _y_pos(proportions[key][0]) if key in proportions else None

        return cls(
            y_proportions=proportions["vals"],
            y_min=y_min,
            y_max=y_max,
            ref_line=ref_line,
            ref_line_y=y_of("ref_line"),
            ref_area_y_l=y_of("ref_area_l"),
            ref_area_y_u=y_of("ref_area_u"),
            zero_y=y_of("zero"),
        )


def _x_proportions(
    x_vals: list[int | float] | None,
    expand_x: list[int | float] | None,
    num_y_vals: int,
    plot_type: str,
) -> list[float]:
    """Scale the `x` values (only used for line plots) to proportions of the data area's width;
    without them, the data points are evenly spaced."""

    if plot_type != "line" or x_vals is None:
        return [i / (num_y_vals - 1) if num_y_vals > 1 else 0 for i in range(num_y_vals)]

    if isinstance(expand_x, str) or (
        isinstance(expand_x, list) and any(isinstance(item, str) for item in expand_x)
    ):
        # TODO: support date strings by converting them to numeric values (as for `x` values)
        raise NotImplementedError("Currently, passing expand_x as a string is unsupported.")

    return _normalize_to_dict(vals=x_vals, expand_x=expand_x)["vals"]


@dataclass(frozen=True)
class _NanoplotSpec:
    """The data, scale, and options of a nanoplot with one or more data points, which is drawn by
    the `_render_*()` functions.

    Data point positions are in SVG units, where a missing `y` value has a `y` position of `None`.
    The `opts` have their per-point options expanded to one value per data point, and the layers
    that can't be drawn (e.g., a reference line without a value) turned off."""

    plot_type: str
    data_line_type: str
    missing_vals: str
    y_vals: list[int | float]
    y_vals_integerlike: bool
    canvas: _Canvas
    scale: _YScale
    x_points: tuple[float, ...]
    y_points: tuple[float | None, ...]
    opts: _NanoplotOptions

    @classmethod
    def from_inputs(
        cls,
        y_vals: list[int | float],
        x_vals: list[int | float] | None,
        *,
        plot_type: str,
        data_line_type: str,
        missing_vals: str,
        y_ref_line: float | str | None,
        y_ref_area: list[int | float | str] | None,
        expand_x: list[int | float] | None,
        expand_y: list[int | float] | None,
        opts: _NanoplotOptions,
    ) -> _NanoplotSpec:
        # TODO: box plots are not drawn yet, so all of their layers are turned off
        if plot_type == "boxplot":
            opts = opts.hide_layers()

        y_vals_integerlike = _is_integerlike(val_list=y_vals)
        expand_y = _expand_invariant_y(y_vals, expand_y)

        opts = replace(
            opts,
            show_reference_line=not _is_na(y_ref_line) and opts.show_reference_line,
            show_reference_area=_is_complete_ref_area(y_ref_area) and opts.show_reference_area,
        )

        canvas = _Canvas.create(
            len(y_vals), evenly_spaced=x_vals is None and plot_type != "boxplot"
        )

        scale = _YScale.resolve(
            y_vals,
            ref_line=y_ref_line if opts.show_reference_line else None,
            ref_area=y_ref_area if opts.show_reference_area else None,
            expand_y=expand_y,
            include_zero=plot_type in ("bar", "boxplot"),
        )

        x_proportions = _x_proportions(x_vals, expand_x, len(y_vals), plot_type)

        return cls(
            plot_type=plot_type,
            data_line_type=data_line_type,
            missing_vals=missing_vals,
            y_vals=y_vals,
            y_vals_integerlike=y_vals_integerlike,
            canvas=canvas,
            scale=scale,
            x_points=tuple(canvas.x_pos(p) for p in x_proportions),
            y_points=tuple(None if p is None else _y_pos(p) for p in scale.y_proportions),
            opts=opts.per_point(len(y_vals)),
        )

    @property
    def segments(self) -> list[slice]:
        """The runs of consecutive non-missing data points; lines and areas are broken (gapped)
        wherever a missing value occurs."""

        runs: list[slice] = []
        start = None

        for i, y in enumerate(self.y_points):
            if y is not None and start is None:
                start = i
            elif y is None and start is not None:
                runs.append(slice(start, i))
                start = None

        if start is not None:
            runs.append(slice(start, len(self.y_points)))

        return runs

    @property
    def y_vals_all_intlike(self) -> bool:
        """Whether every `y` value is integer-like (in which case labels lose any exponent)."""
        return len(self.y_vals) == _get_n_intlike(self.y_vals)


# ---------------------------------------------------------------------------------------------
# SVG elements
# ---------------------------------------------------------------------------------------------


def _svg_tag(name: str, attrs: dict[str, Any], content: str = "") -> str:
    """An SVG element with the attributes in `attrs` (in order) and the inner `content`."""

    attr_str = " ".join(f'{key}="{val}"' for key, val in attrs.items())

    return f"<{name} {attr_str}>{content}</{name}>"


def _hidden_text_tag(x: float, y: float, label: str, **attrs: Any) -> str:
    """A text label that is transparent until the nanoplot's style rules reveal it (e.g., on hover);
    any `attrs` (e.g., `text_anchor="end"`) are added at the end."""

    extra = {key.replace("_", "-"): val for key, val in attrs.items()}

    return _svg_tag(
        "text",
        {"x": x, "y": y, "fill": "transparent", "stroke": "transparent", "font-size": "30px"}
        | extra,
        label,
    )


def _missing_marker_tag(x: float, radius: float, stroke_width: int, fill: str) -> str:
    """A circle denoting a missing value, placed at the vertical middle of the data area."""

    return _svg_tag(
        "circle",
        {
            "cx": x,
            "cy": _SAFE_Y_D + (_DATA_Y_HEIGHT / 2),
            "r": radius + (radius / 2),
            "stroke": "red",
            "stroke-width": stroke_width,
            "fill": fill,
        },
    )


def _curved_path_d(xs: tuple[float, ...], ys: tuple[float, ...], x_d: int) -> str:
    """The path data of a smooth curve through the points, made of cubic Bézier segments whose
    control points are offset horizontally by half of the point spacing `x_d`."""

    commands = [f"M {xs[0]},{ys[0]}"]

    for j in range(1, len(xs)):
        commands.append(
            f"C {xs[j - 1] + x_d / 2},{ys[j - 1]} {xs[j] - x_d / 2},{ys[j]} {xs[j]},{ys[j]}"
        )

    return " ".join(commands)


def _polyline_points(xs: tuple[float, ...], ys: tuple[float, ...]) -> str:
    return " ".join(f"{x},{y}" for x, y in zip(xs, ys))


def _bar_style(val: float, i: int, opts: _NanoplotOptions) -> tuple[str, int, str]:
    """The stroke color, stroke width, and fill color of the bar for the `i`-th value `val` (with
    `opts` expanded per point); negative values and zero get their own styles."""

    if val < 0:
        return (
            opts.data_bar_negative_stroke_color,
            opts.data_bar_negative_stroke_width,
            opts.data_bar_negative_fill_color,
        )

    if val > 0:
        return (
            opts.data_bar_stroke_color[i],
            opts.data_bar_stroke_width[i],
            opts.data_bar_fill_color[i],
        )

    return _ZERO_BAR_COLOR, _ZERO_BAR_STROKE_WIDTH, _ZERO_BAR_COLOR


def _area_pattern_id(fill_color: str) -> str:
    # All nanoplots end up in the same HTML document, so the pattern id has to differ
    # between fill colors. Otherwise every area uses the first pattern with that id.
    return f"area_pattern_{zlib.crc32(str(fill_color).encode()):08x}"


def _nanoplot_svg_defs(data_area_fill_color: str) -> str:
    """The `<defs>` of a nanoplot: the pattern of diagonal lines that fills data areas."""

    return (
        f"<defs>"
        f'<pattern id="{_area_pattern_id(data_area_fill_color)}" width="8" height="8" '
        f'patternUnits="userSpaceOnUse">'
        f'<path class="pattern-line" d="M 0,8 l 8,-8 M -1,1 l 4,-4 M 6,10 l 4,-4" stroke="'
        f"{data_area_fill_color}"
        f'" stroke-width="1.5" stroke-linecap="round" shape-rendering="geometricPrecision">'
        f"</path>"
        f"</pattern>"
        f"</defs>"
    )


def _nanoplot_svg_style(
    interactive_data_values: bool, vertical_guide_stroke_color: str
) -> tuple[str, str]:
    """Generate the `<style>` tag for a nanoplot, along with the class that scopes it.

    Styles inside an inline SVG apply to the whole page, so every rule is prefixed with a class
    that is set on the nanoplot's `<svg>` element. The class is derived from the rules themselves,
    so nanoplots with the same styling share a class while differently-styled nanoplots (e.g., in
    another table on the same page) can't affect each other."""

    text_shown = "stroke: white; fill: #212427;"

    rules = [
        "text { font-family: ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, "
        "'DejaVu Sans Mono', monospace; stroke-width: 0.15em; paint-order: stroke; "
        "stroke-linejoin: round; cursor: default; }",
    ]

    if interactive_data_values:
        # Values, guides, and the reference line are highlighted when hovered over
        rules += [
            f".vert-line:hover rect {{ fill: {vertical_guide_stroke_color}; fill-opacity: 40%; "
            "stroke: #FFFFFF60; color: red; }",
            f".vert-line:hover text {{ {text_shown} }}",
            f".horizontal-line:hover text {{ {text_shown} }}",
            ".ref-line:hover rect { stroke: #FFFFFF60; }",
            ".ref-line:hover line { stroke: #FF0000; }",
            f".ref-line:hover text {{ {text_shown} }}",
            ".y-axis-line:hover rect { fill: #EDEDED; fill-opacity: 60%; stroke: #FFFFFF60; "
            "color: red; }",
            ".y-axis-line:hover text { stroke: white; stroke-width: 0.20em; fill: #1A1C1F; }",
        ]
    else:
        # Values are always shown, so the hover highlights of the guides and the reference line
        # are left out (they would otherwise be shown all at once)
        rules += [
            f".vert-line text {{ {text_shown} }}",
            f".horizontal-line text {{ {text_shown} }}",
            f".ref-line text {{ {text_shown} }}",
            ".y-axis-line rect { fill: #EDEDED; fill-opacity: 60%; }",
            ".y-axis-line text { stroke: white; stroke-width: 0.20em; fill: #1A1C1F; }",
        ]

    scope_class = f"gt-nanoplot-{zlib.crc32(''.join(rules).encode()):08x}"

    svg_style = "<style> " + " ".join(f".{scope_class} {rule}" for rule in rules) + " </style>"

    return scope_class, svg_style


def _construct_nanoplot_svg(
    viewbox: str, svg_height: str, opts: _NanoplotOptions, layers: list[str]
) -> str:
    """Wrap the SVG elements of a nanoplot's `layers` (from bottom to top) in an `<svg>` element."""

    svg_class, svg_style = _nanoplot_svg_style(
        interactive_data_values=opts.interactive_data_values,
        vertical_guide_stroke_color=opts.vertical_guide_stroke_color,
    )

    svg_defs = _nanoplot_svg_defs(opts.data_area_fill_color)

    return (
        f'<div><svg class="{svg_class}" role="img" viewBox="{viewbox}" '
        f'style="height: {svg_height}; margin-left: auto; margin-right: auto; font-size: inherit; '
        f'overflow: visible; vertical-align: middle; position:relative;">'
        f"{svg_defs}{svg_style}{''.join(layers)}</svg></div>"
    )


# ---------------------------------------------------------------------------------------------
# Layers of a nanoplot with one or more data points (each is empty when not drawn)
# ---------------------------------------------------------------------------------------------


def _render_ref_area(spec: _NanoplotSpec) -> str:
    if not spec.opts.show_reference_area:
        return ""

    x_first, x_last = spec.x_points[0], spec.x_points[-1]
    y_l, y_u = spec.scale.ref_area_y_l, spec.scale.ref_area_y_u

    return _svg_tag(
        "path",
        {
            "d": f"M{x_first},{y_u},{x_last},{y_u},{x_last},{y_l},{x_first},{y_l}Z",
            "stroke": "transparent",
            "stroke-width": "2",
            "fill": spec.opts.reference_area_fill_color,
            "fill-opacity": "0.8",
        },
    )


def _render_data_area(spec: _NanoplotSpec) -> str:
    if spec.plot_type != "line" or not spec.opts.show_data_area:
        return ""

    # The area extends below the data area by the radius of the data points
    bottom = _BOTTOM_Y - _SAFE_Y_D + spec.opts.data_point_radius[0]
    pattern_id = _area_pattern_id(spec.opts.data_area_fill_color)

    tags = []
    for segment in spec.segments:
        xs, ys = spec.x_points[segment], spec.y_points[segment]

        d = f"M {_polyline_points(xs, ys)} {xs[-1]},{bottom} {xs[0]},{bottom} Z"

        tags.append(
            _svg_tag(
                "path",
                {
                    "class": "area-closed",
                    "d": d,
                    "stroke": "transparent",
                    "stroke-width": "2",
                    "fill": f"url(#{pattern_id})",
                    "fill-opacity": "0.7",
                },
            )
        )

    return " ".join(tags)


def _render_data_line(spec: _NanoplotSpec) -> str:
    if spec.plot_type != "line" or not spec.opts.show_data_line:
        return ""

    stroke = {
        "stroke": spec.opts.data_line_stroke_color,
        "stroke-width": spec.opts.data_line_stroke_width,
        "fill": "none",
    }

    tags = []
    for segment in spec.segments:
        xs, ys = spec.x_points[segment], spec.y_points[segment]

        if spec.data_line_type == "curved":
            tags.append(_svg_tag("path", {"d": _curved_path_d(xs, ys, spec.canvas.x_d)} | stroke))
        else:
            tags.append(_svg_tag("polyline", {"points": _polyline_points(xs, ys)} | stroke))

    return ("\n" if spec.data_line_type == "curved" else "").join(tags)


def _render_zero_line(spec: _NanoplotSpec) -> str:
    if spec.plot_type != "bar":
        return ""

    return _svg_tag(
        "line",
        {
            "x1": spec.x_points[0] - 27.5,
            "y1": spec.scale.zero_y,
            "x2": spec.x_points[-1] + 27.5,
            "y2": spec.scale.zero_y,
            "stroke": _ZERO_LINE_STROKE_COLOR,
            "stroke-width": _ZERO_LINE_STROKE_WIDTH,
        },
    )


def _render_bars(spec: _NanoplotSpec) -> str:
    if spec.plot_type != "bar":
        return ""

    x_d = spec.canvas.x_d
    if x_d is None:
        raise NotImplementedError("Bar plots with `x` values are not supported.")

    opts, zero_y = spec.opts, spec.scale.zero_y

    tags = []
    for i, (x, y, val) in enumerate(zip(spec.x_points, spec.y_points, spec.y_vals)):
        if y is None:
            if spec.missing_vals == "marker":
                tags.append(
                    _missing_marker_tag(
                        x, opts.data_point_radius[i], opts.data_bar_stroke_width[i], "transparent"
                    )
                )
            continue

        if val < 0:
            rect_y, height = zero_y, y - zero_y
        elif val > 0:
            rect_y, height = y, zero_y - y
        else:
            rect_y, height = zero_y - 1, 2

        stroke, stroke_width, fill = _bar_style(val, i, opts)

        tags.append(
            _svg_tag(
                "rect",
                {
                    "x": x - (x_d - 10) / 2,
                    "y": rect_y,
                    "width": x_d - 10,
                    "height": height,
                    "stroke": stroke,
                    "stroke-width": stroke_width,
                    "fill": fill,
                },
            )
        )

    return "".join(tags)


def _render_ref_line(spec: _NanoplotSpec) -> str:
    if not spec.opts.show_reference_line:
        return ""

    ref_line, y = spec.scale.ref_line, spec.scale.ref_line_y
    x_first, width = spec.x_points[0], spec.canvas.data_x_width

    label = spec.opts.format(
        ref_line,
        as_integer=spec.y_vals_integerlike and _is_whole_number(ref_line),
        fn=spec.opts.y_ref_line_fmt_fn,
    )

    hover_target = _svg_tag(
        "rect",
        {
            "x": x_first - 10,
            "y": y - 10,
            "width": width + 20,
            "height": "20",
            "stroke": "transparent",
            "stroke-width": "1",
            "fill": "transparent",
        },
    )

    line = _svg_tag(
        "line",
        {
            "class": "ref-line",
            "x1": x_first,
            "y1": y,
            "x2": width + _SAFE_X_D,
            "y2": y,
            "stroke": spec.opts.reference_line_color,
            "stroke-width": 1,
            "stroke-dasharray": "4 3",
            "transform": "",
            "stroke-linecap": "round",
            "vector-effect": "non-scaling-stroke",
        },
    )

    text = _hidden_text_tag(width + _SAFE_X_D + 10, y + 10, label)

    return f'<g class="ref-line">{hover_target}{line}{text}</g>'


def _render_data_points(spec: _NanoplotSpec) -> str:
    if spec.plot_type != "line" or not spec.opts.show_data_points:
        return ""

    opts = spec.opts

    tags = []
    for i, (x, y) in enumerate(zip(spec.x_points, spec.y_points)):
        if y is None:
            if spec.missing_vals == "marker":
                tags.append(
                    _missing_marker_tag(
                        x, opts.data_point_radius[i], opts.data_point_stroke_width[i], "white"
                    )
                )
            continue

        tags.append(
            _svg_tag(
                "circle",
                {
                    "cx": x,
                    "cy": y,
                    "r": opts.data_point_radius[i],
                    "stroke": opts.data_point_stroke_color[i],
                    "stroke-width": opts.data_point_stroke_width[i],
                    "fill": opts.data_point_fill_color[i],
                },
            )
        )

    return "".join(tags)


def _render_y_axis_guide(spec: _NanoplotSpec) -> str:
    if not spec.opts.show_y_axis_guide:
        return ""

    y_min, y_max = spec.scale.y_min, spec.scale.y_max
    as_integer = _is_integerlike(val_list=[y_max]) and _is_integerlike(val_list=[y_min])

    max_label = spec.opts.format(y_max, as_integer=as_integer, fn=spec.opts.y_axis_fmt_fn)
    min_label = spec.opts.format(y_min, as_integer=as_integer, fn=spec.opts.y_axis_fmt_fn)

    if spec.y_vals_all_intlike:
        max_label = _remove_exponent(max_label)
        min_label = _remove_exponent(min_label)

    hover_target = _svg_tag(
        "rect",
        {
            "x": 0,
            "y": 0,
            "width": _SAFE_X_D + 15,
            "height": _BOTTOM_Y,
            "stroke": "transparent",
            "stroke-width": "0",
            "fill": "transparent",
        },
    )

    def axis_text(y: float, label: str) -> str:
        attrs = {"x": 0, "y": y, "fill": "transparent", "stroke": "transparent", "font-size": "25"}
        return _svg_tag("text", attrs, label)

    max_text = axis_text(_SAFE_Y_D + _DATA_Y_HEIGHT / 25, max_label)
    min_text = axis_text(_BOTTOM_Y - _DATA_Y_HEIGHT / 25, min_label)

    return f'<g class="y-axis-line">{hover_target}{max_text}{min_text}</g>'


def _render_vertical_guides(spec: _NanoplotSpec) -> str:
    if not spec.opts.show_vertical_guides:
        return ""

    opts = spec.opts

    tags = []
    for x, val in zip(spec.x_points, spec.y_vals):
        if opts.interactive_data_values:
            # A hover target, highlighted by the nanoplot's style rules
            guide = _svg_tag(
                "rect",
                {
                    "x": x - 10,
                    "y": 0,
                    "width": "20",
                    "height": _BOTTOM_Y,
                    "stroke": "transparent",
                    "stroke-width": opts.vertical_guide_stroke_width,
                    "fill": "transparent",
                },
            )
        else:
            # With all values always shown, each guide is a thin, dim line
            guide = _svg_tag(
                "line",
                {
                    "x1": x,
                    "y1": 0,
                    "x2": x,
                    "y2": _BOTTOM_Y,
                    "stroke": opts.vertical_guide_stroke_color,
                    "stroke-opacity": "0.25",
                    "stroke-width": "1",
                    "vector-effect": "non-scaling-stroke",
                },
            )

        label = opts.format(val, as_integer=spec.y_vals_integerlike, fn=opts.y_val_fmt_fn)

        x_text = x + 10
        if label == "NA":
            x_text = x_text + 2

        if spec.y_vals_all_intlike:
            label = _remove_exponent(label)

        text = _hidden_text_tag(x_text, _SAFE_Y_D + 5, label)

        tags.append(f'<g class="vert-line">{guide}{text}</g>')

    return "".join(tags)


def _render_layers(spec: _NanoplotSpec) -> list[str]:
    """The layers of the nanoplot, from bottom to top."""

    return [
        _render_ref_area(spec),
        _render_data_area(spec),
        _render_data_line(spec),
        _render_zero_line(spec),
        _render_bars(spec),
        _render_ref_line(spec),
        _render_data_points(spec),
        _render_y_axis_guide(spec),
        _render_vertical_guides(spec),
    ]


# ---------------------------------------------------------------------------------------------
# Single-value nanoplots (a horizontal bar or line per row, on a scale shared by all rows)
# ---------------------------------------------------------------------------------------------


def _single_value_proportions(
    y_val: float,
    all_vals: list[int] | list[float] | list[int | float],
    ref_line: float | None = None,
) -> tuple[float, float, float | None]:
    """Scale a single `y` value, the zero line and an optional reference line to the common
    scale shared by the single-value plots of all rows."""

    if all(val == 0 for val in all_vals) and not ref_line:
        # Handle case where all values across rows (and the reference line) are `0`
        return 0.5, 0.5, None if ref_line is None else 0.5

    scale = {"val": [y_val], "all_vals": all_vals, "zero": 0}
    if ref_line is not None:
        scale["ref_line"] = ref_line

    proportions = _normalize_to_dict(**scale)

    return (
        proportions["val"][0],
        proportions["zero"][0],
        None if ref_line is None else proportions["ref_line"][0],
    )


def _single_value_ref_line_tags(
    x: float, y1: float, y2: float, stroke: str, label: str, label_on_left: bool = False
) -> str:
    """Vertical reference line for single-value (horizontal) bar and line plots.

    The label is placed to the left of the line when `label_on_left=True`, which keeps it within
    the plot when the line is close to the right edge."""

    text_position = f'x="{x - 10}" text-anchor="end"' if label_on_left else f'x="{x + 10}"'

    return (
        f'<g class="ref-line"><rect x="{x - 10}" y="{y1}" width="20" height="{y2 - y1}" '
        'stroke="transparent" stroke-width="1" fill="transparent"></rect>'
        f'<line class="ref-line" x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{stroke}" '
        'stroke-width="1" stroke-dasharray="4 3" stroke-linecap="round" '
        'vector-effect="non-scaling-stroke"></line>'
        f'<text {text_position} y="{y1 - 10}" fill="transparent" stroke="transparent" '
        f'font-size="30px">{label}</text></g>'
    )


def _single_value_label_tag(
    y_val: float, label: str, zero_x: float, all_vals: list[int | float], zero_offset: int
) -> str:
    """The value label of a single-value plot, beside the zero line on the side of the bar or line.

    A `0` value is labeled on the right of the zero line (at `zero_offset`) unless all values are
    negative."""

    if y_val > 0:
        return _hidden_text_tag(zero_x + 10, _SAFE_Y_D + 10, label)

    if y_val < 0:
        return _hidden_text_tag(zero_x - 10, _SAFE_Y_D + 10, label, text_anchor="end")

    if all(val == 0 for val in all_vals):
        x, anchor = zero_x + 10, "start"
    elif all(val < 0 for val in all_vals):
        x, anchor = zero_x - 10, "end"
    else:
        x, anchor = zero_x + zero_offset, "start"

    return _hidden_text_tag(x, _BOTTOM_Y / 2 + 10, label, text_anchor=anchor)


def _single_value_bar_tag(
    y_val: float, val_x: float, zero_x: float, thickness: float, opts: _NanoplotOptions
) -> str:
    """A horizontal bar from the zero line to the value."""

    if y_val < 0:
        rect_x, width = val_x, zero_x - val_x
    elif y_val > 0:
        rect_x, width = zero_x, val_x - zero_x
    else:
        rect_x, width = zero_x - 2.5, 5

    stroke, stroke_width, fill = _bar_style(y_val, 0, opts)

    return _svg_tag(
        "rect",
        {
            "x": rect_x,
            "y": _BOTTOM_Y / 2 - thickness / 2,
            "width": width,
            "height": thickness,
            "stroke": stroke,
            "stroke-width": stroke_width,
            "fill": fill,
        },
    )


def _single_value_line_tags(
    y_val: float, val_x: float, zero_x: float, opts: _NanoplotOptions
) -> tuple[str, str]:
    """A horizontal line from the zero line to the value, and the data point at its end."""

    x1, x2 = (zero_x, val_x) if y_val > 0 else (val_x, zero_x)
    point_x = x1 if y_val < 0 else x2

    line = _svg_tag(
        "line",
        {
            "x1": x1,
            "y1": _BOTTOM_Y / 2,
            "x2": x2,
            "y2": _BOTTOM_Y / 2,
            "stroke": opts.data_line_stroke_color,
            "stroke-width": opts.data_line_stroke_width,
        },
    )

    point = _svg_tag(
        "circle",
        {
            "cx": point_x,
            "cy": _BOTTOM_Y / 2,
            "r": opts.data_point_radius[0],
            "stroke": opts.data_point_stroke_color[0],
            "stroke-width": opts.data_point_stroke_width[0],
            "fill": opts.data_point_fill_color[0],
        },
    )

    return line, point


def _single_value_guide_tag(label_tag: str, thickness: float, opts: _NanoplotOptions) -> str:
    """The value label of a single-value plot, together with the hover target revealing it."""

    hover_target = _svg_tag(
        "rect",
        {
            "x": "0",
            "y": _BOTTOM_Y / 2 - thickness / 2,
            "width": _FIXED_DATA_X_WIDTH,
            "height": thickness,
            "stroke": "transparent",
            "stroke-width": opts.vertical_guide_stroke_width,
            "fill": "transparent",
        },
    )

    return f'<g class="horizontal-line">{hover_target}{label_tag}</g>'


def _single_value_layers(
    y_val: float,
    all_vals: list[int | float],
    y_ref_line: float | str | None,
    plot_type: str,
    opts: _NanoplotOptions,
) -> list[str]:
    """The layers of a single-value bar or line plot (from bottom to top). The values of all rows
    in `all_vals` share a scale, and so a `y_ref_line` keyword (e.g., `"mean"`) is computed from
    them (leaving out any missing values)."""

    ref_value = None
    if opts.show_reference_line and not _is_na(y_ref_line):
        ref_value = calc_ref_value(y_ref_line, [val for val in all_vals if not _is_na(val)])

    y_vals_integerlike = _is_integerlike(val_list=[y_val])
    opts = opts.per_point(1)

    thickness = opts.data_point_radius[0] * 4
    y1, y2 = (_BOTTOM_Y / 2) - (thickness * 1.5), (_BOTTOM_Y / 2) + (thickness * 1.5)

    val_p, zero_p, ref_p = _single_value_proportions(y_val, all_vals, ref_value)
    val_x, zero_x = val_p * _FIXED_DATA_X_WIDTH, zero_p * _FIXED_DATA_X_WIDTH

    label = opts.format(y_val, as_integer=y_vals_integerlike, fn=opts.y_val_fmt_fn)
    label_tag = _single_value_label_tag(
        y_val, label, zero_x, all_vals, zero_offset=10 if plot_type == "bar" else 15
    )
    guide = _single_value_guide_tag(label_tag, thickness, opts)

    zero_line = _svg_tag(
        "line",
        {
            "x1": zero_x,
            "y1": y1,
            "x2": zero_x,
            "y2": y2,
            "stroke": _ZERO_LINE_STROKE_COLOR,
            "stroke-width": _ZERO_LINE_STROKE_WIDTH,
        },
    )

    ref_line = ""
    if ref_p is not None:
        ref_label = opts.format(
            ref_value,
            as_integer=y_vals_integerlike and _is_whole_number(ref_value),
            fn=opts.y_ref_line_fmt_fn,
        )
        ref_line = _single_value_ref_line_tags(
            ref_p * _FIXED_DATA_X_WIDTH,
            y1,
            y2,
            stroke=opts.reference_line_color,
            label=ref_label,
            label_on_left=ref_p > 0.5,
        )

    if plot_type == "bar":
        bar = _single_value_bar_tag(y_val, val_x, zero_x, thickness, opts)
        return [zero_line, bar + guide, ref_line]

    line, point = _single_value_line_tags(y_val, val_x, zero_x, opts)
    return [line + guide, zero_line, ref_line, point]


# ---------------------------------------------------------------------------------------------
# Nanoplot generation
# ---------------------------------------------------------------------------------------------


def _generate_nanoplot(
    y_vals: list[int] | list[float] | list[int | float] | float,
    y_ref_line: float | str | None = None,
    y_ref_area: list[int | float | str] | None = None,
    x_vals: list[int | float] | None = None,
    expand_x: list[int] | list[float] | list[int | float] | None = None,
    expand_y: list[int] | list[float] | list[int | float] | None = None,
    missing_vals: str = "marker",
    all_single_y_vals: list[int] | list[float] | list[int | float] | None = None,
    plot_type: str = "line",
    data_line_type: str = "curved",
    svg_height: str = "2em",
    **options: Any,
) -> str:
    """
    Generate a nanoplot SVG.

    A list of `y_vals` gives a plot of one or more data points, while a single (scalar) `y_vals`
    value gives a horizontal bar or line on the scale shared with all rows' values in
    `all_single_y_vals`. The `options` are the styling and layer options of `_NanoplotOptions`
    (as returned by `nanoplot_options()`). An empty string is returned if there is nothing to plot.
    """

    _match_arg(x=missing_vals, lst=["marker", "gap", "zero", "remove"])
    _match_arg(x=data_line_type, lst=["curved", "straight"])

    opts = _NanoplotOptions(**options)

    # A curved data line is interpolated from evenly spaced x positions, so it cannot
    # be drawn once `x_vals` set the positions; fall back to a straight line and say so
    if x_vals is not None and data_line_type == "curved":
        warnings.warn(
            "A curved data line is not supported when `x_vals` is supplied; "
            "using `data_line_type='straight'` instead."
        )
        data_line_type = "straight"

    vals = _prepare_vals(y_vals, x_vals, missing_vals)

    if vals is None:
        return ""

    y_vals, x_vals = vals

    if isinstance(y_vals, (int, float)) and plot_type in ("line", "bar"):
        layers = _single_value_layers(y_vals, all_single_y_vals, y_ref_line, plot_type, opts)

        # The viewbox leaves out the safe zones so that bars and lines span the whole width
        viewbox = f"0 0 {_FIXED_DATA_X_WIDTH} {_BOTTOM_Y}"

        return _construct_nanoplot_svg(viewbox, svg_height, opts, layers)

    spec = _NanoplotSpec.from_inputs(
        y_vals,
        x_vals,
        plot_type=plot_type,
        data_line_type=data_line_type,
        missing_vals=missing_vals,
        y_ref_line=y_ref_line,
        y_ref_area=y_ref_area,
        expand_x=expand_x,
        expand_y=expand_y,
        opts=opts,
    )

    return _construct_nanoplot_svg(spec.canvas.viewbox, svg_height, opts, _render_layers(spec))
