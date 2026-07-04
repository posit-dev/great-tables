from __future__ import annotations

import math
import random
from typing import Any, Callable

from ._tbl_data import Agnostic, NpInteger, is_na
from ._utils import _flatten_list, _match_arg

REFERENCE_LINE_KEYWORDS = ["mean", "median", "min", "max", "q1", "q3"]


def _is_na(x: Any) -> bool:
    return is_na(Agnostic(), x)


def _map_is_na(x: list[Any]) -> list[bool]:
    # TODO: all([]) returns True. Let's double check all places
    # in the code that call all() with this function. Do they work as intended?
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


# This determines whether an entire list of values are integer-like; this skips
# over missing values and returns a single boolean
def _is_integerlike(val_list: list[Any]) -> bool:
    """
    Determine whether an entire list of values are integer-like; this skips
    over missing values and returns a single boolean.
    """

    # If the list is empty, return False
    if not val_list:
        return False

    return all((isinstance(val, (int, NpInteger)) or _is_na(val)) for val in val_list)


def _any_na_in_list(x: list[Any]) -> bool:
    """
    Determine whether a list of values contains any missing values.
    """

    return any(_is_na(val) for val in x)


def _check_any_na_in_list(x: list[int | float]) -> None:
    """
    Check whether a list of values contains any missing values; if so, raise an error.
    """

    if _any_na_in_list(x):
        raise ValueError("The list of values cannot contain missing values.")


# Remove missing values from a list of values
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


def calc_ref_value(val_or_calc: int | float | str, data) -> int | float | str:
    if _val_is_numeric(val_or_calc):
        return val_or_calc
    elif _val_is_str(val_or_calc) and val_or_calc in REFERENCE_LINE_KEYWORDS:
        return _generate_ref_line_from_keyword(vals=data, keyword=val_or_calc)

    raise ValueError(f"Unsupported nanoplot area value: {val_or_calc}")


def _apply_custom_number_format(
    val: int | float,
    fn: Callable[..., str] | None,
) -> str | None:
    if fn is None:
        return None

    if callable(fn):
        res = fn(val)

        if not isinstance(res, str):
            raise ValueError("The result of the formatting function must be a single string value.")

        return res

    return None


def _get_number_format_profile(val: int | float) -> tuple[bool, int | None, int, bool]:
    abs_val = abs(val)

    if abs_val < 0.01:
        return True, None, 2, False

    if abs_val < 1:
        return True, None, 2, False

    if abs_val < 100:
        return True, None, 3, False

    if abs_val < 1000:
        return True, None, 3, False

    if abs_val < 10000:
        return False, 2, 3, True

    if abs_val < 100000:
        return False, 1, 3, True

    if abs_val < 1000000:
        return False, 0, 3, True

    if abs_val < 1e15:
        return False, 1, 3, True

    return False, None, 2, False


def _format_number_default(
    val: int | float,
    currency: str | None,
    as_integer: bool,
    use_subunits: bool,
    decimals: int | None,
    n_sigfig: int,
    compact: bool,
) -> str:
    from great_tables.vals import fmt_currency, fmt_integer, fmt_number, fmt_scientific

    if currency is not None:
        if abs(val) >= 1e15:
            val_formatted = fmt_currency(
                1e15,
                currency=currency,
                use_subunits=False,
                decimals=0,
            )

            return f">{val_formatted}"

        return fmt_currency(
            val,
            currency=currency,
            use_subunits=use_subunits,
            decimals=decimals,
        )

    if abs(val) < 0.01 or abs(val) >= 1e15:
        return fmt_scientific(
            val,
            exp_style="E",
            n_sigfig=n_sigfig,
            decimals=1,
        )

    if as_integer and -100 < val < 100:
        return fmt_integer(val)

    return fmt_number(
        val,
        n_sigfig=n_sigfig,
        decimals=1,
        compact=compact,
    )


def _format_number_compactly(
    val: int | float,
    currency: str | None = None,
    as_integer: bool = False,
    fn: Callable[..., str] | None = None,
) -> str:
    """
    Format a single numeric value compactly, using a currency if provided.
    """

    custom_format = _apply_custom_number_format(val=val, fn=fn)
    if custom_format is not None:
        return custom_format

    if _is_na(val):
        return "NA"

    if val == 0:
        return "0"

    use_subunits, decimals, n_sigfig, compact = _get_number_format_profile(val)

    val_formatted = _format_number_default(
        val=val,
        currency=currency,
        as_integer=as_integer,
        use_subunits=use_subunits,
        decimals=decimals,
        n_sigfig=n_sigfig,
        compact=compact,
    )

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


def _get_extreme_value(
    *args: int | float,
    stat: str = "max",
) -> int | float:
    """
    Get either the maximum or minimum value from a list of numeric values.
    """

    # Ensure that `stat` is either 'max' or 'min'
    _match_arg(stat, lst=["max", "min"])

    # Remove any None values from the `args` list
    args = [val for val in args if val is not None]

    # Flatten the `args` list which may contain lists and scalar values
    val_list = _flatten_list(args)

    # Remove missing values from the `val_list`
    val_list = _remove_na_from_list(val_list)

    # Remove None values from the `val_list`
    val_list = [val for val in val_list if val is not None]

    if stat == "max":
        extreme_val = max(val_list)
    else:
        extreme_val = min(val_list)

    return extreme_val


def _generate_ref_line_from_keyword(vals: list[int | float], keyword: str) -> int | float:
    """
    Generate a value for a reference line from a valid keyword.
    """

    _match_arg(
        x=keyword,
        lst=REFERENCE_LINE_KEYWORDS,
    )

    _check_any_na_in_list(vals)

    # Remove missing values from the `vals` list
    vals = [val for val in vals if not _is_na(val)]

    if keyword == "mean":
        ref_line = _gt_mean(vals)
    elif keyword == "median":
        ref_line = _gt_median(vals)
    elif keyword == "min":
        ref_line = _gt_min(vals)
    elif keyword == "max":
        ref_line = _gt_max(vals)
    elif keyword == "first":
        ref_line = _gt_first(vals)
    elif keyword == "last":
        ref_line = _gt_last(vals)
    elif keyword == "q1":
        ref_line = _gt_q1(vals)
    else:
        ref_line = _gt_q3(vals)

    return ref_line


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


# TODO: example nanoplot showing when jitter vals might be applied
# Looks like it's on the x-axis:
# GT(pd.DataFrame({'x': [{"x": [1, 1, 1], "y": [2, 3, 4]}]})).fmt_nanoplot("x")
def _jitter_vals(x: list[int | float], amount: float) -> list[int | float]:
    """
    Jitter a list of numeric values by a small amount.
    """

    return [val + random.uniform(-amount, amount) for val in x]


def _normalize_to_dict(**kwargs: list[int | float]) -> dict[str, list[int | float]]:
    """
    Normalize a collection of numeric values to be between 0 and 1. Account for missing values.
    This only accepts values (scalar or list) associated with keyword arguments. A dictionary
    is returned with the same keys but the values are normalized lists. This is done so that
    any disparate collection of normalized values are distinguishable by their original keys.

    All values (lists are flattened, scalars treated as length-1) are pooled together before
    normalization, so that every returned value is scaled relative to the global min/max across
    all inputs. None-valued kwargs are excluded from the normalization pool.

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

    # Get args as a dictionary
    args = kwargs.copy()

    # Extract the values from the dictionary as a list
    all_vals = list(args.values())
    all_keys = list(args.keys())

    # Remove any None values from the `all_vals` list
    all_vals = [val for val in all_vals if val is not None]

    # Get the length of each arg in the args dictionary (if single value, length is 1; if
    # a list, length is the length of the list)
    arg_lens = [len(val) if type(val) is list else 1 for val in all_vals]

    # Flatten the `all_vals` list which may contain lists and scalar values
    all_vals = _flatten_list(all_vals)

    # If all values are the same, then jitter the values
    if len(set(all_vals)) == 1:
        all_vals = _jitter_vals(all_vals, 0.1)

    # Get the normalized values across the collection of all values
    normalized_vals = _normalize_vals(all_vals)

    # Use the `arg_lens` list to put the sequence of normalized values back into
    # the original structure of args; do this with iteration
    for i in range(len(arg_lens)):
        normalized_vals_i = normalized_vals[0 : arg_lens[i]]

        # Assign these values back to the original args dictionary at the ith key
        args[all_keys[i]] = normalized_vals_i

        # Remove the first n elements from `normalized_vals` and assign the result
        normalized_vals = normalized_vals[arg_lens[i] :]

    return args


def _construct_nanoplot_svg(
    viewbox: str,
    svg_height: str,
    svg_defs: str,
    svg_style: str,
    show_data_points: bool,
    show_data_line: bool,
    show_data_area: bool,
    show_reference_line: bool,
    show_reference_area: bool,
    show_vertical_guides: bool,
    show_y_axis_guide: bool,
    ref_area_tags: str | None = None,
    area_path_tags: str | None = None,
    data_path_tags: str | None = None,
    zero_line_tags: str | None = None,
    bar_tags: str | None = None,
    ref_line_tags: str | None = None,
    circle_tags: str | None = None,
    g_y_axis_tags: str | None = None,
    g_guide_tags: str | None = None,
) -> str:
    """
    Construct an SVG nanoplot from a collection of SVG tags.
    """

    # For the optional strings, transform None to an empty string
    ref_area_tags = "" if ref_area_tags is None or show_reference_area is False else ref_area_tags
    area_path_tags = "" if area_path_tags is None or show_data_area is False else area_path_tags
    data_path_tags = "" if data_path_tags is None or show_data_line is False else data_path_tags
    zero_line_tags = "" if zero_line_tags is None else zero_line_tags
    bar_tags = "" if bar_tags is None else bar_tags
    ref_line_tags = "" if ref_line_tags is None or show_reference_line is False else ref_line_tags
    circle_tags = "" if circle_tags is None or show_data_points is False else circle_tags
    g_y_axis_tags = "" if g_y_axis_tags is None or show_y_axis_guide is False else g_y_axis_tags
    g_guide_tags = "" if g_guide_tags is None or show_vertical_guides is False else g_guide_tags

    return f'<div><svg role="img" viewBox="{viewbox}" style="height: {svg_height}; margin-left: auto; margin-right: auto; font-size: inherit; overflow: visible; vertical-align: middle; position:relative;">{svg_defs}{svg_style}{ref_area_tags}{area_path_tags}{data_path_tags}{zero_line_tags}{bar_tags}{ref_line_tags}{circle_tags}{g_y_axis_tags}{g_guide_tags}</svg></div>'


def _generate_nanoplot(*args: Any, **kwargs: Any) -> str:
    return _generate_nanoplot_impl(*args, **kwargs)


def _generate_nanoplot_impl(
    y_vals: list[int] | list[float] | list[int | float],
    y_ref_line: str | None = None,
    y_ref_area: str | None = None,
    x_vals: list[int | float] | None = None,
    expand_x: list[int] | list[float] | list[int | float] | None = None,
    expand_y: list[int] | list[float] | list[int | float] | None = None,
    missing_vals: str = "marker",
    all_y_vals: list[int] | list[float] | list[int | float] | None = None,
    all_single_y_vals: list[int] | list[float] | list[int | float] | None = None,
    plot_type: str = "line",
    data_line_type: str = "curved",
    currency: str | None = None,
    y_val_fmt_fn: Callable[..., str] | None = None,
    y_axis_fmt_fn: Callable[..., str] | None = None,
    y_ref_line_fmt_fn: Callable[..., str] | None = None,
    data_point_radius: int | list[int] = 10,
    data_point_stroke_color: str | list[str] = "#FFFFFF",
    data_point_stroke_width: int | list[int] = 4,
    data_point_fill_color: str | list[str] = "#FF0000",
    data_line_stroke_color: str = "#4682B4",
    data_line_stroke_width: int = 8,
    data_area_fill_color: str = "#FF0000",
    data_bar_stroke_color: str | list[str] = "#3290CC",
    data_bar_stroke_width: int | list[int] = 4,
    data_bar_fill_color: str | list[str] = "#3FB5FF",
    data_bar_negative_stroke_color: str = "#CC3243",
    data_bar_negative_stroke_width: int = 4,
    data_bar_negative_fill_color: str = "#D75A68",
    reference_line_color: str = "#75A8B0",
    reference_area_fill_color: str = "#A6E6F2",
    vertical_guide_stroke_color: str = "#911EB4",
    vertical_guide_stroke_width: int = 12,
    show_data_points: bool = True,
    show_data_line: bool = True,
    show_data_area: bool = True,
    show_reference_line: bool = True,
    show_reference_area: bool = True,
    show_vertical_guides: bool = True,
    show_y_axis_guide: bool = True,
    interactive_data_values: bool = True,
    svg_height: str = "2em",
) -> str:
    return _generate_nanoplot_impl(
        y_vals=y_vals,
        y_ref_line=y_ref_line,
        y_ref_area=y_ref_area,
        x_vals=x_vals,
        expand_x=expand_x,
        expand_y=expand_y,
        missing_vals=missing_vals,
        all_y_vals=all_y_vals,
        all_single_y_vals=all_single_y_vals,
        plot_type=plot_type,
        data_line_type=data_line_type,
        currency=currency,
        y_val_fmt_fn=y_val_fmt_fn,
        y_axis_fmt_fn=y_axis_fmt_fn,
        y_ref_line_fmt_fn=y_ref_line_fmt_fn,
        data_point_radius=data_point_radius,
        data_point_stroke_color=data_point_stroke_color,
        data_point_stroke_width=data_point_stroke_width,
        data_point_fill_color=data_point_fill_color,
        data_line_stroke_color=data_line_stroke_color,
        data_line_stroke_width=data_line_stroke_width,
        data_area_fill_color=data_area_fill_color,
        data_bar_stroke_color=data_bar_stroke_color,
        data_bar_stroke_width=data_bar_stroke_width,
        data_bar_fill_color=data_bar_fill_color,
        data_bar_negative_stroke_color=data_bar_negative_stroke_color,
        data_bar_negative_stroke_width=data_bar_negative_stroke_width,
        data_bar_negative_fill_color=data_bar_negative_fill_color,
        reference_line_color=reference_line_color,
        reference_area_fill_color=reference_area_fill_color,
        vertical_guide_stroke_color=vertical_guide_stroke_color,
        vertical_guide_stroke_width=vertical_guide_stroke_width,
        show_data_points=show_data_points,
        show_data_line=show_data_line,
        show_data_area=show_data_area,
        show_reference_line=show_reference_line,
        show_reference_area=show_reference_area,
        show_vertical_guides=show_vertical_guides,
        show_y_axis_guide=show_y_axis_guide,
        interactive_data_values=interactive_data_values,
        svg_height=svg_height,
    )


# pylint: disable=too-many-statements
def _generate_nanoplot_impl(
    y_vals: list[int] | list[float] | list[int | float],
    y_ref_line: str | None = None,
    y_ref_area: str | None = None,
    x_vals: list[int | float] | None = None,
    expand_x: list[int] | list[float] | list[int | float] | None = None,
    expand_y: list[int] | list[float] | list[int | float] | None = None,
    missing_vals: str = "marker",
    all_y_vals: list[int] | list[float] | list[int | float] | None = None,
    all_single_y_vals: list[int] | list[float] | list[int | float] | None = None,
    plot_type: str = "line",
    data_line_type: str = "curved",
    currency: str | None = None,
    y_val_fmt_fn: Callable[..., str] | None = None,
    y_axis_fmt_fn: Callable[..., str] | None = None,
    y_ref_line_fmt_fn: Callable[..., str] | None = None,
    data_point_radius: int | list[int] = 10,
    data_point_stroke_color: str | list[str] = "#FFFFFF",
    data_point_stroke_width: int | list[int] = 4,
    data_point_fill_color: str | list[str] = "#FF0000",
    data_line_stroke_color: str = "#4682B4",
    data_line_stroke_width: int = 8,
    data_area_fill_color: str = "#FF0000",
    data_bar_stroke_color: str | list[str] = "#3290CC",
    data_bar_stroke_width: int | list[int] = 4,
    data_bar_fill_color: str | list[str] = "#3FB5FF",
    data_bar_negative_stroke_color: str = "#CC3243",
    data_bar_negative_stroke_width: int = 4,
    data_bar_negative_fill_color: str = "#D75A68",
    reference_line_color: str = "#75A8B0",
    reference_area_fill_color: str = "#A6E6F2",
    vertical_guide_stroke_color: str = "#911EB4",
    vertical_guide_stroke_width: int = 12,
    show_data_points: bool = True,
    show_data_line: bool = True,
    show_data_area: bool = True,
    show_reference_line: bool = True,
    show_reference_area: bool = True,
    show_vertical_guides: bool = True,
    show_y_axis_guide: bool = True,
    interactive_data_values: bool = True,
    svg_height: str = "2em",
) -> str:
    """
    Generate a nanoplot SVG from a collection of parameters.
    """
    state: dict[str, Any] = {
        "y_vals": y_vals,
        "y_ref_line": y_ref_line,
        "y_ref_area": y_ref_area,
        "x_vals": x_vals,
        "expand_x": expand_x,
        "expand_y": expand_y,
        "missing_vals": missing_vals,
        "all_y_vals": all_y_vals,
        "all_single_y_vals": all_single_y_vals,
        "plot_type": plot_type,
        "data_line_type": data_line_type,
        "currency": currency,
        "y_val_fmt_fn": y_val_fmt_fn,
        "y_axis_fmt_fn": y_axis_fmt_fn,
        "y_ref_line_fmt_fn": y_ref_line_fmt_fn,
        "data_point_radius": data_point_radius,
        "data_point_stroke_color": data_point_stroke_color,
        "data_point_stroke_width": data_point_stroke_width,
        "data_point_fill_color": data_point_fill_color,
        "data_line_stroke_color": data_line_stroke_color,
        "data_line_stroke_width": data_line_stroke_width,
        "data_area_fill_color": data_area_fill_color,
        "data_bar_stroke_color": data_bar_stroke_color,
        "data_bar_stroke_width": data_bar_stroke_width,
        "data_bar_fill_color": data_bar_fill_color,
        "data_bar_negative_stroke_color": data_bar_negative_stroke_color,
        "data_bar_negative_stroke_width": data_bar_negative_stroke_width,
        "data_bar_negative_fill_color": data_bar_negative_fill_color,
        "reference_line_color": reference_line_color,
        "reference_area_fill_color": reference_area_fill_color,
        "vertical_guide_stroke_color": vertical_guide_stroke_color,
        "vertical_guide_stroke_width": vertical_guide_stroke_width,
        "show_data_points": show_data_points,
        "show_data_line": show_data_line,
        "show_data_area": show_data_area,
        "show_reference_line": show_reference_line,
        "show_reference_area": show_reference_area,
        "show_vertical_guides": show_vertical_guides,
        "show_y_axis_guide": show_y_axis_guide,
        "interactive_data_values": interactive_data_values,
        "svg_height": svg_height,
        "ref_area_tags": None,
        "area_path_tags": None,
        "data_path_tags": None,
        "zero_line_tags": None,
        "bar_tags": None,
        "ref_line_tags": None,
        "circle_tags": None,
        "g_y_axis_tags": None,
        "g_guide_tags": None,
        "boxplot_tags": None,
        "single_horizontal_plot": False,
        "zero_line_stroke_color": "#BFBFBF",
        "zero_line_stroke_width": 4,
    }

    if not _prepare_nanoplot_state(state):
        return ""

    _resolve_nanoplot_scales_and_geometry(state)
    _build_nanoplot_data_series(state)
    _build_nanoplot_plot_specific_tags(state)
    _build_nanoplot_reference_tags(state)
    _build_nanoplot_axis_tags(state)
    _build_nanoplot_area_tags(state)

    svg_defs = (
        f"<defs>"
        f'<pattern id="area_pattern" width="8" height="8" patternUnits="userSpaceOnUse">'
        f'<path class="pattern-line" d="M 0,8 l 8,-8 M -1,1 l 4,-4 M 6,10 l 4,-4" stroke="'
        f"{state['data_area_fill_color']}"
        f'" stroke-width="1.5" stroke-linecap="round" shape-rendering="geometricPrecision">'
        f"</path>"
        f"</pattern>"
        f"</defs>"
    )
    svg_style = _build_nanoplot_svg_style(state)

    return _construct_nanoplot_svg(
        viewbox=state["viewbox"],
        svg_height=state["svg_height"],
        svg_defs=svg_defs,
        svg_style=svg_style,
        show_data_points=state["show_data_points"],
        show_data_line=state["show_data_line"],
        show_data_area=state["show_data_area"],
        show_reference_line=state["show_reference_line"],
        show_reference_area=state["show_reference_area"],
        show_vertical_guides=state["show_vertical_guides"],
        show_y_axis_guide=state["show_y_axis_guide"],
        ref_area_tags=state["ref_area_tags"],
        area_path_tags=state["area_path_tags"],
        data_path_tags=state["data_path_tags"],
        zero_line_tags=state["zero_line_tags"],
        bar_tags=state["bar_tags"],
        ref_line_tags=state["ref_line_tags"],
        circle_tags=state["circle_tags"],
        g_y_axis_tags=state["g_y_axis_tags"],
        g_guide_tags=state["g_guide_tags"],
    )


def _prepare_nanoplot_state(state: dict[str, Any]) -> bool:
    _match_arg(x=state["missing_vals"], lst=["marker", "gap", "zero", "remove"])
    _match_arg(x=state["data_line_type"], lst=["curved", "straight"])

    state["zero_line_considered"] = state["plot_type"] in ("bar", "boxplot")

    if isinstance(state["y_vals"], list) and len(state["y_vals"]) == 0:
        return False
    if isinstance(state["y_vals"], list) and all(_map_is_na(state["y_vals"])):
        return False

    state["num_y_vals"] = len(state["y_vals"]) if type(state["y_vals"]) is list else 1

    if state["x_vals"] is not None:
        if len(state["x_vals"]) == 0:
            return False
        if all(_map_is_na(state["x_vals"])):
            return False
        num_x_vals = len(state["x_vals"])
        if num_x_vals != state["num_y_vals"]:
            raise ValueError(
                f"""The number of `x` and `y` values must match.
                The `x` value length is: {num_x_vals}
                The `y` value length is: {state['num_y_vals']}
                """
            )
        if any(_map_is_na(state["x_vals"])):
            x_vals_non_missing = [not _is_na(val) for val in state["x_vals"]]
            state["x_vals"] = [x for x, keep in zip(state["x_vals"], x_vals_non_missing) if keep]
            state["y_vals"] = [y for y, keep in zip(state["y_vals"], x_vals_non_missing) if keep]
        state["data_line_type"] = "straight"

    if state["missing_vals"] == "zero":
        state["y_vals"] = [0 if _is_na(val) else val for val in state["y_vals"]]
    if state["missing_vals"] == "remove":
        non_na_mask = [not _is_na(val) for val in state["y_vals"]]
        state["y_vals"] = [v for v, keep in zip(state["y_vals"], non_na_mask) if keep]
        if state["x_vals"] is not None:
            state["x_vals"] = [v for v, keep in zip(state["x_vals"], non_na_mask) if keep]

    state["num_y_vals"] = len(state["y_vals"]) if isinstance(state["y_vals"], list) else 1

    if isinstance(state["y_vals"], (int, float)) and state["plot_type"] in ("line", "bar"):
        state["single_horizontal_plot"] = True
        state["show_data_points"] = True
        state["show_data_line"] = True
        state["show_data_area"] = False
        state["show_reference_line"] = False
        state["show_reference_area"] = False
        state["show_vertical_guides"] = False
        state["show_y_axis_guide"] = False
        state["y_vals"] = [state["y_vals"]]

    if state["plot_type"] == "boxplot":
        state["show_data_points"] = False
        state["show_data_line"] = False
        state["show_data_area"] = False
        state["show_reference_line"] = False
        state["show_reference_area"] = False
        state["show_vertical_guides"] = False
        state["show_y_axis_guide"] = False

    state["y_vals_integerlike"] = _is_integerlike(val_list=state["y_vals"])
    return True


def _resolve_nanoplot_scales_and_geometry(state: dict[str, Any]) -> None:
    _resolve_nanoplot_reference_state(state)
    _resolve_nanoplot_x_state(state)
    _resolve_nanoplot_dimensions(state)


def _resolve_nanoplot_reference_state(state: dict[str, Any]) -> None:
    y_vals = state["y_vals"]
    y_scale_max = _get_extreme_value(y_vals, stat="max")
    y_scale_min = _get_extreme_value(y_vals, stat="min")

    if y_scale_min == y_scale_max and state["expand_y"] is None:
        expand_y_dist = 5 if y_scale_min == 0 else (y_scale_min / 10) * 2
        state["expand_y"] = [y_scale_min - expand_y_dist, y_scale_min + expand_y_dist]

    if _is_na(state["y_ref_line"]):
        state["show_reference_line"] = False

    if state["y_ref_area"] is None:
        state["show_reference_area"] = False
    elif _is_na(state["y_ref_area"][0]) or _is_na(state["y_ref_area"][1]):
        state["show_reference_area"] = False

    if state["show_reference_line"] and state["show_reference_area"]:
        if state["y_ref_line"] is not None and _val_is_str(state["y_ref_line"]) and state["y_ref_line"] in REFERENCE_LINE_KEYWORDS:
            state["y_ref_line"] = _generate_ref_line_from_keyword(vals=y_vals, keyword=state["y_ref_line"])

        y_ref_area_line_1 = calc_ref_value(state["y_ref_area"][0], y_vals)
        y_ref_area_line_2 = calc_ref_value(state["y_ref_area"][1], y_vals)
        y_ref_area_l, y_ref_area_u = sorted([y_ref_area_line_1, y_ref_area_line_2])

        state["y_scale_max"] = _get_extreme_value(y_vals, state["y_ref_line"], y_ref_area_l, y_ref_area_u, state["expand_y"], stat="max")
        state["y_scale_min"] = _get_extreme_value(y_vals, state["y_ref_line"], y_ref_area_l, y_ref_area_u, state["expand_y"], stat="min")

        y_proportions_list = _normalize_to_dict(
            vals=y_vals,
            ref_line=state["y_ref_line"],
            ref_area_l=y_ref_area_l,
            ref_area_u=y_ref_area_u,
            zero=0 if state["zero_line_considered"] else None,
            expand_y=state["expand_y"],
        )
        state["y_proportions"] = y_proportions_list["vals"]
        state["y_proportion_ref_line"] = y_proportions_list["ref_line"][0]
        state["y_proportions_ref_area_l"] = y_proportions_list["ref_area_l"][0]
        state["y_proportions_ref_area_u"] = y_proportions_list["ref_area_u"][0]
        state["data_y_ref_line"] = state["safe_y_d"] + ((1 - state["y_proportion_ref_line"]) * state["data_y_height"])
        state["data_y_ref_area_l"] = state["safe_y_d"] + ((1 - state["y_proportions_ref_area_l"]) * state["data_y_height"])
        state["data_y_ref_area_u"] = state["safe_y_d"] + ((1 - state["y_proportions_ref_area_u"]) * state["data_y_height"])
    elif state["show_reference_line"]:
        if state["y_ref_line"] is not None and _val_is_str(state["y_ref_line"]) and state["y_ref_line"] in REFERENCE_LINE_KEYWORDS:
            state["y_ref_line"] = _generate_ref_line_from_keyword(vals=y_vals, keyword=state["y_ref_line"])

        args = [y_vals, state["y_ref_line"], state["expand_y"]] + ([0] if state["zero_line_considered"] else [])
        state["y_scale_max"] = _get_extreme_value(*args, stat="max")
        state["y_scale_min"] = _get_extreme_value(*args, stat="min")

        y_proportions_list = _normalize_to_dict(
            vals=y_vals,
            ref_line=state["y_ref_line"],
            zero=0 if state["zero_line_considered"] else None,
            expand_y=state["expand_y"],
        )
        state["y_proportions"] = y_proportions_list["vals"]
        state["y_proportion_ref_line"] = y_proportions_list["ref_line"][0]
        state["data_y_ref_line"] = state["safe_y_d"] + ((1 - state["y_proportion_ref_line"]) * state["data_y_height"])
    elif state["show_reference_area"]:
        y_ref_area_line_1 = calc_ref_value(state["y_ref_area"][0], y_vals)
        y_ref_area_line_2 = calc_ref_value(state["y_ref_area"][1], y_vals)
        y_ref_area_l, y_ref_area_u = sorted([y_ref_area_line_1, y_ref_area_line_2])

        args = [y_vals, y_ref_area_l, y_ref_area_u, state["expand_y"]] + ([0] if state["zero_line_considered"] else [])
        state["y_scale_max"] = _get_extreme_value(*args, stat="max")
        state["y_scale_min"] = _get_extreme_value(*args, stat="min")

        y_proportions_list = _normalize_to_dict(
            vals=y_vals,
            ref_area_l=y_ref_area_l,
            ref_area_u=y_ref_area_u,
            zero=0 if state["zero_line_considered"] else None,
            expand_y=state["expand_y"],
        )
        state["y_proportions"] = y_proportions_list["vals"]
        state["y_proportions_ref_area_l"] = y_proportions_list["ref_area_l"][0]
        state["y_proportions_ref_area_u"] = y_proportions_list["ref_area_u"][0]
        state["data_y_ref_area_l"] = state["safe_y_d"] + ((1 - state["y_proportions_ref_area_l"]) * state["data_y_height"])
        state["data_y_ref_area_u"] = state["safe_y_d"] + ((1 - state["y_proportions_ref_area_u"]) * state["data_y_height"])
    else:
        args = [y_vals, state["expand_y"]] + ([0] if state["zero_line_considered"] else [])
        state["y_scale_max"] = _get_extreme_value(*args, stat="max")
        state["y_scale_min"] = _get_extreme_value(*args, stat="min")

        y_proportions_list = _normalize_to_dict(
            vals=y_vals,
            zero=0 if state["zero_line_considered"] else None,
            expand_y=state["expand_y"],
        )
        state["y_proportions"] = y_proportions_list["vals"]

    if state["zero_line_considered"]:
        state["y_proportions_zero"] = y_proportions_list["zero"][0]
        state["data_y0_point"] = state["safe_y_d"] + ((1 - state["y_proportions_zero"]) * state["data_y_height"])


def _resolve_nanoplot_x_state(state: dict[str, Any]) -> None:
    if state["plot_type"] == "line" and state["x_vals"] is not None:
        if isinstance(state["expand_x"], str) or (
            isinstance(state["expand_x"], list) and any(isinstance(item, str) for item in state["expand_x"])
        ):
            raise NotImplementedError("Currently, passing expand_x as a string is unsupported.")
        state["x_proportions"] = _normalize_to_dict(vals=state["x_vals"], expand_x=state["expand_x"])["vals"]
    else:
        state["x_proportions"] = [i / (state["num_y_vals"] - 1) if state["num_y_vals"] > 1 else 0 for i in range(state["num_y_vals"])]


def _resolve_nanoplot_dimensions(state: dict[str, Any]) -> None:
    if state["x_vals"] is not None or state["single_horizontal_plot"] or state["plot_type"] == "boxplot":
        state["data_x_width"] = 600
        state["x_d"] = 50
    else:
        if state["num_y_vals"] <= 20:
            state["x_d"] = 50
        elif state["num_y_vals"] <= 30:
            state["x_d"] = 40
        elif state["num_y_vals"] <= 40:
            state["x_d"] = 30
        elif state["num_y_vals"] <= 50:
            state["x_d"] = 25
        else:
            state["x_d"] = 20
        state["data_x_width"] = state["num_y_vals"] * state["x_d"]

    state["left_x"] = 0
    state["top_y"] = 0
    state["safe_y_d"] = 15
    state["safe_x_d"] = 50
    state["data_y_height"] = 100
    state["bottom_y"] = state["safe_y_d"] + state["data_y_height"] + state["safe_y_d"]
    state["right_x"] = state["safe_x_d"] + state["data_x_width"] + state["safe_x_d"]
    state["viewbox"] = f"{state['left_x']} {state['top_y']} {state['right_x']} {state['bottom_y']}"


def _build_nanoplot_data_series(state: dict[str, Any]) -> None:
    state["data_y_points"] = tuple(
        None if y_p is None else state["safe_y_d"] + ((1 - y_p) * state["data_y_height"]) for y_p in state["y_proportions"]
    )
    state["data_x_points"] = tuple((state["data_x_width"] * x_p) + state["safe_x_d"] for x_p in state["x_proportions"])

    state["data_point_radius"] = _normalize_option_list(option_list=state["data_point_radius"], num_y_vals=state["num_y_vals"])
    state["data_point_stroke_color"] = _normalize_option_list(option_list=state["data_point_stroke_color"], num_y_vals=state["num_y_vals"])
    state["data_point_stroke_width"] = _normalize_option_list(option_list=state["data_point_stroke_width"], num_y_vals=state["num_y_vals"])
    state["data_point_fill_color"] = _normalize_option_list(option_list=state["data_point_fill_color"], num_y_vals=state["num_y_vals"])
    state["data_bar_stroke_color"] = _normalize_option_list(option_list=state["data_bar_stroke_color"], num_y_vals=state["num_y_vals"])
    state["data_bar_stroke_width"] = _normalize_option_list(option_list=state["data_bar_stroke_width"], num_y_vals=state["num_y_vals"])
    state["data_bar_fill_color"] = _normalize_option_list(option_list=state["data_bar_fill_color"], num_y_vals=state["num_y_vals"])

    start_data_y_points: list[int] = []
    end_data_y_points: list[int] = []
    in_segment = False
    for idx, val in enumerate(state["data_y_points"]):
        if val is not None:
            if not in_segment:
                start_data_y_points.append(idx)
                in_segment = True
        elif in_segment:
            end_data_y_points.append(idx)
            in_segment = False
    if in_segment:
        end_data_y_points.append(len(state["data_y_points"]))

    state["start_data_y_points"] = start_data_y_points
    state["end_data_y_points"] = end_data_y_points
    state["n_segments"] = len(start_data_y_points)


def _build_nanoplot_plot_specific_tags(state: dict[str, Any]) -> None:
    if state["plot_type"] == "line":
        _build_nanoplot_line_tags(state)
        _build_nanoplot_single_horizontal_line_tags(state)
    elif state["plot_type"] == "bar":
        _build_nanoplot_vertical_bar_tags(state)
        _build_nanoplot_single_horizontal_bar_tags(state)


def _build_nanoplot_line_tags(state: dict[str, Any]) -> None:
    if state["show_data_line"] and state["data_line_type"] == "curved":
        data_path_tags = []
        for i in range(state["n_segments"]):
            curve_x = state["data_x_points"][state["start_data_y_points"][i] : state["end_data_y_points"][i]]
            curve_y = state["data_y_points"][state["start_data_y_points"][i] : state["end_data_y_points"][i]]
            curved_path_string = [f"M {curve_x[0]},{curve_y[0]}"]
            for j in range(1, len(curve_x)):
                point_b1 = f"{curve_x[j - 1] + state['x_d'] / 2},{curve_y[j - 1]}"
                point_b2 = f"{curve_x[j] - state['x_d'] / 2},{curve_y[j]}"
                point_i = f"{curve_x[j]},{curve_y[j]}"
                curved_path_string.append(f"C {point_b1} {point_b2} {point_i}")
            data_path_tags.append(
                f'<path d="{" ".join(curved_path_string)}" stroke="{state["data_line_stroke_color"]}" stroke-width="{state["data_line_stroke_width"]}" fill="none"></path>'
            )
        state["data_path_tags"] = "\n".join(data_path_tags)

    if state["show_data_line"] and state["data_line_type"] == "straight":
        data_path_tags = []
        for i in range(state["n_segments"]):
            line_x = state["data_x_points"][state["start_data_y_points"][i] : state["end_data_y_points"][i]]
            line_y = state["data_y_points"][state["start_data_y_points"][i] : state["end_data_y_points"][i]]
            line_xy = " ".join((f"{x},{y}" for x, y in zip(line_x, line_y)))
            data_path_tags.append(
                f'<polyline points="{line_xy}" stroke="{state["data_line_stroke_color"]}" stroke-width="{state["data_line_stroke_width"]}" fill="none"></polyline>'
            )
        state["data_path_tags"] = "".join(data_path_tags)

    if state["show_data_points"]:
        circle_strings = []
        for i, (data_x_point_i, data_y_point_i) in enumerate(zip(state["data_x_points"], state["data_y_points"])):
            data_point_radius_i = state["data_point_radius"][i]
            data_point_stroke_color_i = state["data_point_stroke_color"][i]
            data_point_stroke_width_i = state["data_point_stroke_width"][i]
            data_point_fill_color_i = state["data_point_fill_color"][i]
            if data_y_point_i is None:
                if state["missing_vals"] == "marker":
                    circle_strings.append(
                        f'<circle cx="{data_x_point_i}" cy="{state["safe_y_d"] + (state["data_y_height"] / 2)}" r="{data_point_radius_i + (data_point_radius_i / 2)}" stroke="red" stroke-width="{data_point_stroke_width_i}" fill="white"></circle>'
                    )
                continue
            circle_strings.append(
                f'<circle cx="{data_x_point_i}" cy="{data_y_point_i}" r="{data_point_radius_i}" stroke="{data_point_stroke_color_i}" stroke-width="{data_point_stroke_width_i}" fill="{data_point_fill_color_i}"></circle>'
            )
        state["circle_tags"] = "".join(circle_strings)


def _build_nanoplot_vertical_bar_tags(state: dict[str, Any]) -> None:
    if state["single_horizontal_plot"]:
        return

    bar_strings = []
    for i, (data_x_point_i, data_y_point_i) in enumerate(zip(state["data_x_points"], state["data_y_points"])):
        data_point_radius_i = state["data_point_radius"][i]
        data_bar_stroke_color_i = state["data_bar_stroke_color"][i]
        data_bar_stroke_width_i = state["data_bar_stroke_width"][i]
        data_bar_fill_color_i = state["data_bar_fill_color"][i]

        if data_y_point_i is None:
            if state["missing_vals"] == "marker":
                bar_strings.append(
                    f'<circle cx="{data_x_point_i}" cy="{state["safe_y_d"] + (state["data_y_height"] / 2)}" r="{data_point_radius_i + (data_point_radius_i / 2)}" stroke="red" stroke-width="{data_bar_stroke_width_i}" fill="transparent"></circle>'
                )
            continue

        if state["y_vals"][i] < 0:
            y_value_i = state["data_y0_point"]
            y_height = data_y_point_i - state["data_y0_point"]
            data_bar_stroke_color_i = state["data_bar_negative_stroke_color"]
            data_bar_stroke_width_i = state["data_bar_negative_stroke_width"]
            data_bar_fill_color_i = state["data_bar_negative_fill_color"]
        elif state["y_vals"][i] > 0:
            y_value_i = data_y_point_i
            y_height = state["data_y0_point"] - data_y_point_i
        else:
            y_value_i = state["data_y0_point"] - 1
            y_height = 2
            data_bar_stroke_color_i = "#808080"
            data_bar_stroke_width_i = 4
            data_bar_fill_color_i = "#808080"

        bar_strings.append(
            f'<rect x="{data_x_point_i - (state["x_d"] - 10) / 2}" y="{y_value_i}" width="{state["x_d"] - 10}" height="{y_height}" stroke="{data_bar_stroke_color_i}" stroke-width="{data_bar_stroke_width_i}" fill="{data_bar_fill_color_i}"></rect>'
        )

    state["bar_tags"] = "".join(bar_strings)
    if state["plot_type"] == "bar" and state["single_horizontal_plot"] is False:
        state["zero_line_tags"] = f'<line x1="{state["data_x_points"][0] - 27.5}" y1="{state["data_y0_point"]}" x2="{state["data_x_points"][-1] + 27.5}" y2="{state["data_y0_point"]}" stroke="{state["zero_line_stroke_color"]}" stroke-width="{state["zero_line_stroke_width"]}"></line>'


def _build_nanoplot_single_horizontal_bar_tags(state: dict[str, Any]) -> None:
    if not (state["plot_type"] == "bar" and state["single_horizontal_plot"]):
        return

    bar_thickness = state["data_point_radius"][0] * 4
    if all(val == 0 for val in state["all_single_y_vals"]):
        y_proportion = 0.5
        y_proportion_zero = 0.5
    else:
        y_proportions_list = _normalize_to_dict(val=state["y_vals"], all_vals=state["all_single_y_vals"], zero=0)
        y_proportion = y_proportions_list["val"][0]
        y_proportion_zero = y_proportions_list["zero"][0]

    y0_width = y_proportion_zero * state["data_x_width"]
    y_width = y_proportion * state["data_x_width"]

    if state["y_vals"][0] < 0:
        data_bar_stroke_color = state["data_bar_negative_stroke_color"]
        data_bar_stroke_width = state["data_bar_negative_stroke_width"]
        data_bar_fill_color = state["data_bar_negative_fill_color"]
        rect_x = y_width
        rect_width = y0_width - y_width
    elif state["y_vals"][0] > 0:
        data_bar_stroke_color = state["data_bar_stroke_color"][0]
        data_bar_stroke_width = state["data_bar_stroke_width"][0]
        data_bar_fill_color = state["data_bar_fill_color"][0]
        rect_x = y0_width
        rect_width = y_width - y0_width
    else:
        data_bar_stroke_color = "#808080"
        data_bar_stroke_width = 4
        data_bar_fill_color = "#808080"
        rect_x = y0_width - 2.5
        rect_width = 5

    y_value = _format_number_compactly(val=state["y_vals"][0], currency=state["currency"], as_integer=state["y_vals_integerlike"], fn=state["y_val_fmt_fn"])
    rect_strings = f'<rect x="0" y="{state["bottom_y"] / 2 - bar_thickness / 2}" width="600" height="{bar_thickness}" stroke="transparent" stroke-width="{state["vertical_guide_stroke_width"]}" fill="transparent"></rect>'

    if state["y_vals"][0] > 0:
        text_strings = f'<text x="{y0_width + 10}" y="{state["safe_y_d"] + 10}" fill="transparent" stroke="transparent" font-size="30px">{y_value}</text>'
    elif state["y_vals"][0] < 0:
        text_strings = f'<text x="{y0_width - 10}" y="{state["safe_y_d"] + 10}" fill="transparent" stroke="transparent" font-size="30px" text-anchor="end">{y_value}</text>'
    else:
        if all(val == 0 for val in state["all_single_y_vals"]):
            text_anchor = "start"
            x_position_text = y0_width + 10
        elif all(val < 0 for val in state["all_single_y_vals"]):
            text_anchor = "end"
            x_position_text = y0_width - 10
        else:
            text_anchor = "start"
            x_position_text = y0_width + 10
        text_strings = f'<text x="{x_position_text}" y="{state["bottom_y"] / 2 + 10}" fill="transparent" stroke="transparent" font-size="30px" text-anchor="{text_anchor}">{y_value}</text>'

    state["g_guide_tags"] = f'<g class="horizontal-line">{rect_strings}{text_strings}</g>'
    state["bar_tags"] = f'<rect x="{rect_x}" y="{state["bottom_y"] / 2 - bar_thickness / 2}" width="{rect_width}" height="{bar_thickness}" stroke="{data_bar_stroke_color}" stroke-width="{data_bar_stroke_width}" fill="{data_bar_fill_color}"></rect>{state["g_guide_tags"]}'
    state["zero_line_tags"] = f'<line x1="{y0_width}" y1="{(state["bottom_y"] / 2) - (bar_thickness * 1.5)}" x2="{y0_width}" y2="{(state["bottom_y"] / 2) + (bar_thickness * 1.5)}" stroke="{state["zero_line_stroke_color"]}" stroke-width="{state["zero_line_stroke_width"]}"></line>'
    state["viewbox"] = f"{state['left_x']} {state['top_y']} {state['data_x_width']} {state['bottom_y']}"


def _build_nanoplot_single_horizontal_line_tags(state: dict[str, Any]) -> None:
    if not (state["plot_type"] == "line" and state["single_horizontal_plot"]):
        return

    data_point_radius_i = state["data_point_radius"][0]
    data_point_stroke_color_i = state["data_point_stroke_color"][0]
    data_point_stroke_width_i = state["data_point_stroke_width"][0]
    data_point_fill_color_i = state["data_point_fill_color"][0]
    bar_thickness = state["data_point_radius"][0] * 4

    if all(val == 0 for val in state["all_single_y_vals"]):
        y_proportion = 0.5
        y_proportion_zero = 0.5
    else:
        y_proportions_list = _normalize_to_dict(val=state["y_vals"], all_vals=state["all_single_y_vals"], zero=0)
        y_proportion = y_proportions_list["val"][0]
        y_proportion_zero = y_proportions_list["zero"][0]

    y0_width = y_proportion_zero * state["data_x_width"]
    y_width = y_proportion * state["data_x_width"]

    if state["y_vals"][0] < 0:
        x1_val = y_width
        x2_val = y0_width
        circle_x_val = x1_val
    elif state["y_vals"][0] > 0:
        x1_val = y0_width
        x2_val = y_width
        circle_x_val = x2_val
    else:
        x1_val = y_width
        x2_val = y0_width
        circle_x_val = x2_val

    y_value = _format_number_compactly(val=state["y_vals"][0], currency=state["currency"], as_integer=state["y_vals_integerlike"], fn=state["y_val_fmt_fn"])
    rect_strings = f'<rect x="0" y="{state["bottom_y"] / 2 - bar_thickness / 2}" width="600" height="{bar_thickness}" stroke="transparent" stroke-width="{state["vertical_guide_stroke_width"]}" fill="transparent"></rect>'

    if state["y_vals"][0] > 0:
        text_strings = f'<text x="{y0_width + 10}" y="{state["safe_y_d"] + 10}" fill="transparent" stroke="transparent" font-size="30px">{y_value}</text>'
    elif state["y_vals"][0] < 0:
        text_strings = f'<text x="{y0_width - 10}" y="{state["safe_y_d"] + 10}" fill="transparent" stroke="transparent" font-size="30px" text-anchor="end">{y_value}</text>'
    else:
        if all(val == 0 for val in state["all_single_y_vals"]):
            text_anchor = "start"
            x_position_text = y0_width + 10
        elif all(val < 0 for val in state["all_single_y_vals"]):
            text_anchor = "end"
            x_position_text = y0_width - 10
        else:
            text_anchor = "start"
            x_position_text = y0_width + 15
        text_strings = f'<text x="{x_position_text}" y="{state["bottom_y"] / 2 + 10}" fill="transparent" stroke="transparent" font-size="30px" text-anchor="{text_anchor}">{y_value}</text>'

    state["g_guide_tags"] = f'<g class="horizontal-line">{rect_strings}{text_strings}</g>'
    state["data_path_tags"] = f'<line x1="{x1_val}" y1="{state["bottom_y"] / 2}" x2="{x2_val}" y2="{state["bottom_y"] / 2}" stroke="{state["data_line_stroke_color"]}" stroke-width="{state["data_line_stroke_width"]}"></line>{state["g_guide_tags"]}'
    state["circle_tags"] = f'<circle cx="{circle_x_val}" cy="{state["bottom_y"] / 2}" r="{data_point_radius_i}" stroke="{data_point_stroke_color_i}" stroke-width="{data_point_stroke_width_i}" fill="{data_point_fill_color_i}"></circle>'
    state["zero_line_tags"] = f'<line x1="{y0_width}" y1="{(state["bottom_y"] / 2) - (bar_thickness * 1.5)}" x2="{y0_width}" y2="{(state["bottom_y"] / 2) + (bar_thickness * 1.5)}" stroke="{state["zero_line_stroke_color"]}" stroke-width="{state["zero_line_stroke_width"]}"></line>'
    state["viewbox"] = f"{state['left_x']} {state['top_y']} {state['data_x_width']} {state['bottom_y']}"


def _build_nanoplot_reference_tags(state: dict[str, Any]) -> None:
    if state["show_reference_line"]:
        y_ref_line = _format_number_compactly(
            val=state["y_ref_line"], currency=state["currency"], as_integer=state["y_vals_integerlike"], fn=state["y_ref_line_fmt_fn"]
        )
        state["ref_line_tags"] = (
            f'<g class="ref-line"><rect x="{state["data_x_points"][0] - 10}" y="{state["data_y_ref_line"] - 10}" width="{state["data_x_width"] + 20}" height="20" stroke="transparent" stroke-width="1" fill="transparent"></rect><line class="ref-line" x1="{state["data_x_points"][0]}" y1="{state["data_y_ref_line"]}" x2="{state["data_x_width"] + state["safe_x_d"]}" y2="{state["data_y_ref_line"]}" stroke="{state["reference_line_color"]}" stroke-width="1" stroke-dasharray="4 3" transform="" stroke-linecap="round" vector-effect="non-scaling-stroke"></line><text x="{state["data_x_width"] + state["safe_x_d"] + 10}" y="{state["data_y_ref_line"] + 10}" fill="transparent" stroke="transparent" font-size="30px">{y_ref_line}</text></g>'
        )

    if state["show_reference_area"]:
        p_ul = f"{state['data_x_points'][0]},{state['data_y_ref_area_u']}"
        p_ur = f"{state['data_x_points'][-1]},{state['data_y_ref_area_u']}"
        p_lr = f"{state['data_x_points'][-1]},{state['data_y_ref_area_l']}"
        p_ll = f"{state['data_x_points'][0]},{state['data_y_ref_area_l']}"
        ref_area_path = f"M{p_ul},{p_ur},{p_lr},{p_ll}Z"
        state["ref_area_tags"] = f'<path d="{ref_area_path}" stroke="transparent" stroke-width="2" fill="{state["reference_area_fill_color"]}" fill-opacity="0.8"></path>'


def _build_nanoplot_axis_tags(state: dict[str, Any]) -> None:
    if state["show_y_axis_guide"]:
        is_all_intify_y_axis = len(state["y_vals"]) == _get_n_intlike(state["y_vals"])
        rect_tag = f'<rect x="{state["left_x"]}" y="{state["top_y"]}" width="{state["safe_x_d"] + 15}" height="{state["bottom_y"]}" stroke="transparent" stroke-width="0" fill="transparent"></rect>'
        y_axis_guide_vals_integerlike = _is_integerlike(val_list=[state["y_scale_max"]]) and _is_integerlike(val_list=[state["y_scale_min"]])
        y_value_max_label = _format_number_compactly(val=state["y_scale_max"], currency=state["currency"], as_integer=y_axis_guide_vals_integerlike, fn=state["y_axis_fmt_fn"])
        y_value_min_label = _format_number_compactly(val=state["y_scale_min"], currency=state["currency"], as_integer=y_axis_guide_vals_integerlike, fn=state["y_axis_fmt_fn"])
        if is_all_intify_y_axis:
            y_value_max_label = _remove_exponent(y_value_max_label)
            y_value_min_label = _remove_exponent(y_value_min_label)
        text_strings_min = f'<text x="{state["left_x"]}" y="{state["safe_y_d"] + state["data_y_height"] + state["safe_y_d"] - state["data_y_height"] / 25}" fill="transparent" stroke="transparent" font-size="25">{y_value_min_label}</text>'
        text_strings_max = f'<text x="{state["left_x"]}" y="{state["safe_y_d"] + state["data_y_height"] / 25}" fill="transparent" stroke="transparent" font-size="25">{y_value_max_label}</text>'
        state["g_y_axis_tags"] = f'<g class="y-axis-line">{rect_tag}{text_strings_max}{text_strings_min}</g>'

    if state["show_vertical_guides"]:
        is_all_intify_v_guides = len(state["y_vals"]) == _get_n_intlike(state["y_vals"])
        g_guide_strings = []
        for i, (data_x_point_i, y_val_i) in enumerate(zip(state["data_x_points"], state["y_vals"])):
            rect_strings_i = f'<rect x="{data_x_point_i - 10}" y="{state["top_y"]}" width="20" height="{state["bottom_y"]}" stroke="transparent" stroke-width="{state["vertical_guide_stroke_width"]}" fill="transparent"></rect>'
            y_value_i = _format_number_compactly(val=y_val_i, currency=state["currency"], as_integer=state["y_vals_integerlike"], fn=state["y_val_fmt_fn"])
            x_text = data_x_point_i + 10
            if y_value_i == "NA":
                x_text = x_text + 2
            if is_all_intify_v_guides:
                y_value_i = _remove_exponent(y_value_i)
            text_strings_i = f'<text x="{x_text}" y="{state["safe_y_d"] + 5}" fill="transparent" stroke="transparent" font-size="30px">{y_value_i}</text>'
            g_guide_strings.append(f'<g class="vert-line">{rect_strings_i}{text_strings_i}</g>')
        state["g_guide_tags"] = "".join(g_guide_strings)


def _build_nanoplot_area_tags(state: dict[str, Any]) -> None:
    if state["plot_type"] == "line" and state["show_data_area"]:
        area_path_tags = []
        for i in range(state["n_segments"]):
            area_x = state["data_x_points"][state["start_data_y_points"][i] : state["end_data_y_points"][i]]
            area_y = state["data_y_points"][state["start_data_y_points"][i] : state["end_data_y_points"][i]]
            area_path_string = [f"{area_x[j]},{area_y[j]}" for j in range(0, len(area_x))]
            area_path_i = f"M {' '.join(area_path_string)} {area_x[-1]},{state['bottom_y'] - state['safe_y_d'] + state['data_point_radius'][0]} {area_x[0]},{state['bottom_y'] - state['safe_y_d'] + state['data_point_radius'][0]} Z"
            area_path_tags.append(f'<path class="area-closed" d="{area_path_i}" stroke="transparent" stroke-width="2" fill="url(#area_pattern)" fill-opacity="0.7"></path>')
        state["area_path_tags"] = " ".join(area_path_tags)


def _build_nanoplot_svg_style(state: dict[str, Any]) -> str:
    hover_param = ":hover" if state["interactive_data_values"] else ""
    return (
        f"<style> text {{ font-family: ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace; stroke-width: 0.15em; paint-order: stroke; stroke-linejoin: round; cursor: default; }} "
        f".vert-line{hover_param} rect {{ fill: {state['vertical_guide_stroke_color']}; fill-opacity: 40%; stroke: #FFFFFF60; color: red; }} "
        f".vert-line{hover_param} text {{ stroke: white; fill: #212427; }} "
        f".horizontal-line{hover_param} text {{stroke: white; fill: #212427; }} "
        f".ref-line{hover_param} rect {{ stroke: #FFFFFF60; }} "
        f".ref-line{hover_param} line {{ stroke: #FF0000; }} "
        f".ref-line{hover_param} text {{ stroke: white; fill: #212427; }} "
        f".y-axis-line{hover_param} rect {{ fill: #EDEDED; fill-opacity: 60%; stroke: #FFFFFF60; color: red; }} "
        f".y-axis-line{hover_param} text {{ stroke: white; stroke-width: 0.20em; fill: #1A1C1F; }} "
        f"</style>"
    )


def _build_nanoplot_line_path_tags(
    plot_type: str,
    show_data_line: bool,
    data_line_type: str,
    n_segments: int,
    start_data_y_points: list[int],
    end_data_y_points: list[int],
    data_x_points: tuple[float, ...],
    data_y_points: tuple[int | float | None, ...],
    x_d: int | None,
    data_line_stroke_color: str,
    data_line_stroke_width: int,
) -> str | None:
    if plot_type != "line" or not show_data_line:
        return None

    if data_line_type == "curved":
        data_path_tags = []

        for i in range(n_segments):
            curve_x = data_x_points[start_data_y_points[i] : end_data_y_points[i]]
            curve_y = data_y_points[start_data_y_points[i] : end_data_y_points[i]]

            curved_path_string = [f"M {curve_x[0]},{curve_y[0]}"]

            for j in range(1, len(curve_x)):
                point_b1 = f"{curve_x[j - 1] + x_d / 2},{curve_y[j - 1]}"
                point_b2 = f"{curve_x[j] - x_d / 2},{curve_y[j]}"
                point_i = f"{curve_x[j]},{curve_y[j]}"

                curved_path_string.append(f"C {point_b1} {point_b2} {point_i}")

            curved_path_string_i = " ".join(curved_path_string)
            data_path_tags.append(
                f'<path d="{curved_path_string_i}" stroke="{data_line_stroke_color}" stroke-width="{data_line_stroke_width}" fill="none"></path>'
            )

        return "\n".join(data_path_tags)

    data_path_tags = []
    for i in range(n_segments):
        line_x = data_x_points[start_data_y_points[i] : end_data_y_points[i]]
        line_y = data_y_points[start_data_y_points[i] : end_data_y_points[i]]

        line_xy = " ".join((f"{x},{y}" for x, y in zip(line_x, line_y)))
        data_path_tags.append(
            f'<polyline points="{line_xy}" stroke="{data_line_stroke_color}" stroke-width="{data_line_stroke_width}" fill="none"></polyline>'
        )

    return "".join(data_path_tags)


def _build_nanoplot_point_tags(
    plot_type: str,
    show_data_points: bool,
    data_x_points: tuple[float, ...],
    data_y_points: tuple[int | float | None, ...],
    data_point_radius: list[int],
    data_point_stroke_color: list[str],
    data_point_stroke_width: list[int],
    data_point_fill_color: list[str],
    missing_vals: str,
    safe_y_d: int,
    data_y_height: int,
) -> str | None:
    if plot_type != "line" or not show_data_points:
        return None

    circle_strings = []

    for i, (data_x_point_i, data_y_point_i) in enumerate(zip(data_x_points, data_y_points)):
        data_point_radius_i = data_point_radius[i]
        data_point_stroke_color_i = data_point_stroke_color[i]
        data_point_stroke_width_i = data_point_stroke_width[i]
        data_point_fill_color_i = data_point_fill_color[i]

        if data_y_point_i is None:
            if missing_vals == "marker":
                circle_strings_i = f'<circle cx="{data_x_point_i}" cy="{safe_y_d + (data_y_height / 2)}" r="{data_point_radius_i + (data_point_radius_i / 2)}" stroke="red" stroke-width="{data_point_stroke_width_i}" fill="white"></circle>'
            else:
                continue
        else:
            circle_strings_i = f'<circle cx="{data_x_point_i}" cy="{data_y_point_i}" r="{data_point_radius_i}" stroke="{data_point_stroke_color_i}" stroke-width="{data_point_stroke_width_i}" fill="{data_point_fill_color_i}"></circle>'

        circle_strings.append(circle_strings_i)

    return "".join(circle_strings)


def _build_nanoplot_bar_tags(
    plot_type: str,
    single_horizontal_plot: bool,
    data_x_points: tuple[float, ...],
    data_y_points: tuple[int | float | None, ...],
    data_point_radius: list[int],
    data_bar_stroke_color: list[str],
    data_bar_stroke_width: list[int],
    data_bar_fill_color: list[str],
    missing_vals: str,
    x_d: int | None,
    y_vals: list[int] | list[float] | list[int | float],
    data_y0_point: float | None,
    data_bar_negative_stroke_color: str,
    data_bar_negative_stroke_width: int,
    data_bar_negative_fill_color: str,
    safe_y_d: int,
    data_y_height: int,
) -> str | None:
    if plot_type != "bar" or single_horizontal_plot:
        return None

    bar_strings = []

    for i, (data_x_point_i, data_y_point_i) in enumerate(zip(data_x_points, data_y_points)):
        data_point_radius_i = data_point_radius[i]
        data_bar_stroke_color_i = data_bar_stroke_color[i]
        data_bar_stroke_width_i = data_bar_stroke_width[i]
        data_bar_fill_color_i = data_bar_fill_color[i]

        if data_y_point_i is None:
            if missing_vals == "marker":
                bar_strings_i = f'<circle cx="{data_x_point_i}" cy="{safe_y_d + (data_y_height / 2)}" r="{data_point_radius_i + (data_point_radius_i / 2)}" stroke="red" stroke-width="{data_bar_stroke_width_i}" fill="transparent"></circle>'
            else:
                continue
        else:
            if y_vals[i] < 0:
                y_value_i = data_y_point_i
                y_height = data_y_point_i - data_y0_point
                data_bar_stroke_color_i = data_bar_negative_stroke_color
                data_bar_stroke_width_i = data_bar_negative_stroke_width
                data_bar_fill_color_i = data_bar_negative_fill_color
            elif y_vals[i] > 0:
                y_value_i = data_y_point_i
                y_height = data_y0_point - data_y_point_i
            else:
                y_value_i = data_y0_point - 1
                y_height = 2
                data_bar_stroke_color_i = "#808080"
                data_bar_stroke_width_i = 4
                data_bar_fill_color_i = "#808080"

            bar_strings_i = f'<rect x="{data_x_point_i - (x_d - 10) / 2}" y="{y_value_i}" width="{x_d - 10}" height="{y_height}" stroke="{data_bar_stroke_color_i}" stroke-width="{data_bar_stroke_width_i}" fill="{data_bar_fill_color_i}"></rect>'

        bar_strings.append(bar_strings_i)

    return "".join(bar_strings)


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


def _remove_exponent(n: "str | int | float") -> str:
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
