from typing import Optional, List, Union, Any, Dict, Callable
import pandas as pd
import numpy as np
from great_tables._utils import _match_arg
from great_tables.vals import fmt_currency, fmt_scientific, fmt_integer, fmt_number

REFERENCE_LINE_KEYWORDS = ["mean", "median", "min", "max", "q1", "q3"]


def _val_is_numeric(x: Any) -> bool:

    # If a list then signal a failure
    if isinstance(x, list):
        ValueError("The input cannot be a list. It must be a single value.")

    return isinstance(x, (int, float))


def _val_is_str(x: Any) -> bool:

    # If a list then signal a failure
    if isinstance(x, list):
        ValueError("The input cannot be a list. It must be a single value.")

    return isinstance(x, (str))


def _val_is_missing(x: Any) -> bool:
    return pd.isna(x)


# This determines whether an entire list of values are integer-like; this skips
# over missing values and returns a single boolean
def _is_integerlike(val_list: list) -> bool:
    return all((isinstance(val, (int, np.integer)) or _val_is_missing(val)) for val in val_list)


def _any_na_in_list(x: List[Union[int, float]]) -> bool:
    return any(_val_is_missing(val) for val in x)


def _check_any_na_in_list(x: List[Union[int, float]]) -> None:
    if _any_na_in_list(x):
        raise ValueError("The list of values cannot contain missing values.")

    return None


# Remove missing values from a list of values
def _remove_na_from_list(x: List[Union[int, float]]) -> List[Union[int, float]]:
    return [val for val in x if not _val_is_missing(val)]


def _normalize_option_list(option_list: Union[Any, List[Any]], num_y_vals: int) -> List[Any]:

    # If `option_list` is a single value, then make it a list
    if not isinstance(option_list, list):
        option_list = [option_list]

    if len(option_list) != 1 and len(option_list) != num_y_vals:
        raise ValueError("Every option must have either length 1 or `length(y_vals)`.")

    if len(option_list) == 1:
        option_list = [option_list[0]] * num_y_vals

    return option_list


def _format_number_compactly(
    val, currency: Optional[str] = None, as_integer: bool = False, fn: Any = None
) -> str:

    if fn is not None and isinstance(fn, Callable):
        return fn(val)

    if _val_is_missing(val):
        return "NA"

    if val == 0:
        return "0"

    if abs(val) < 0.01:

        use_subunits = True
        decimals = None

        n_sigfig = 2
        compact = False

    elif abs(val) < 1:

        use_subunits = True
        decimals = None

        n_sigfig = 2
        compact = False

    elif abs(val) < 100:

        use_subunits = True
        decimals = None

        n_sigfig = 3
        compact = False

    elif abs(val) < 1000:

        use_subunits = True
        decimals = None

        n_sigfig = 3
        compact = False

    elif abs(val) < 10000:

        use_subunits = False
        decimals = 2

        n_sigfig = 3
        compact = True

    elif abs(val) < 100000:

        use_subunits = False
        decimals = 1

        n_sigfig = 3
        compact = True

    elif abs(val) < 1000000:

        use_subunits = False
        decimals = 0

        n_sigfig = 3
        compact = True

    elif abs(val) < 1e15:

        use_subunits = False
        decimals = 1

        n_sigfig = 3
        compact = True

    else:

        use_subunits = False
        decimals = None
        n_sigfig = 2
        compact = False

    # Format value accordingly

    if currency is not None:

        if abs(val) >= 1e15:

            val_formatted = fmt_currency(
                1e15,
                currency=currency,
                use_subunits=False,
                decimals=0,
                # compact=True,
                # output="html"
            )

            val_formatted = f">{val_formatted}"

        else:

            val_formatted = fmt_currency(
                val,
                currency=currency,
                use_subunits=use_subunits,
                decimals=decimals,
                # compact=compact,
                # output="html"
            )

    else:

        if abs(val) < 0.01 or abs(val) >= 1e15:

            val_formatted = fmt_scientific(
                val,
                exp_style="E",
                n_sigfig=n_sigfig,
                decimals=1,
                # output="html"
            )

        else:

            if as_integer and val > -100 and val < 100:

                val_formatted = fmt_integer(
                    val,
                    # output="html"
                )

            else:

                val_formatted = fmt_number(
                    val,
                    n_sigfig=n_sigfig,
                    decimals=1,
                    compact=compact,
                    # output="html"
                )

    return val_formatted[0]


#
# Collection of general functions to calculate the mean, min, max, median,
# and other statistical measures from a list of values; the list should not
# be expected to contain any missing values so we won't guard against them here
#


def _gt_mean(x: List[Union[int, float]]) -> float:
    return sum(x) / len(x)


def _gt_min(x: List[Union[int, float]]) -> Union[int, float]:
    return min(x)


def _gt_max(x: List[Union[int, float]]) -> Union[int, float]:
    return max(x)


def _gt_median(x: List[Union[int, float]]) -> float:
    x.sort()
    n = len(x)
    if n % 2 == 0:
        return (x[n // 2 - 1] + x[n // 2]) / 2
    else:
        return x[n // 2]


def _gt_first(x: List[Union[int, float]]) -> Union[int, float]:
    return x[0]


def _gt_last(x: List[Union[int, float]]) -> Union[int, float]:
    return x[-1]


def _gt_quantile(x: List[Union[int, float]], q: float) -> float:
    x.sort()
    n = len(x)
    return x[int(n * q)]


def _gt_q1(x: List[Union[int, float]]) -> float:
    return _gt_quantile(x, 0.25)


def _gt_q3(x: List[Union[int, float]]) -> float:
    return _gt_quantile(x, 0.75)


def _flatten_list(x) -> List[Any]:

    flat_list = []

    # Iterate through the outer list
    for element in x:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


# Function to get either the max or min value from a list of values
def _get_extreme_value(
    *args,
    stat: str = "max",
):
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


def _generate_ref_line_from_keyword(vals: List[Union[int, float]], keyword: str) -> float:

    _match_arg(
        x=keyword,
        lst=REFERENCE_LINE_KEYWORDS,
    )

    _check_any_na_in_list(vals)

    # Remove missing values from the `vals` list
    vals = [val for val in vals if not _val_is_missing(val)]

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


def _normalize_vals(
    x: Union[List[Union[int, float]], List[int], List[float]]
) -> List[Union[int, float]]:
    x_missing = [i for i, val in enumerate(x) if pd.isna(val)]
    mean_x = np.mean([val for val in x if not pd.isna(val)])
    x = [mean_x if pd.isna(val) else val for val in x]
    x = np.array(x)
    min_attr = np.min(x, axis=0)
    max_attr = np.max(x, axis=0)
    x = x - min_attr
    x = x / (max_attr - min_attr)
    x = x.tolist()
    x = [np.nan if i in x_missing else val for i, val in enumerate(x)]
    return x


def _jitter_vals(x: List[Union[int, float]], amount: float) -> List[Union[int, float]]:
    return [val + np.random.uniform(-amount, amount) for val in x]


def _normalize_to_dict(**kwargs) -> Dict[str, List[Union[int, float]]]:

    # Ensure that at least two values are provided
    if len(kwargs) < 2:
        raise ValueError("At least two values must be provided.")

    # Get args as a dictionary
    args = dict(kwargs)

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
    ref_area_tags: Optional[str] = None,
    area_path_tags: Optional[str] = None,
    data_path_tags: Optional[str] = None,
    ref_line_tags: Optional[str] = None,
    circle_tags: Optional[str] = None,
    g_y_axis_tags: Optional[str] = None,
    g_guide_tags: Optional[str] = None,
) -> str:

    # For the optional strings, transform None to an empty string
    ref_area_tags = "" if ref_area_tags is None else ref_area_tags
    area_path_tags = "" if area_path_tags is None else area_path_tags
    data_path_tags = "" if data_path_tags is None else data_path_tags
    ref_line_tags = "" if ref_line_tags is None else ref_line_tags
    circle_tags = "" if circle_tags is None else circle_tags
    g_y_axis_tags = "" if g_y_axis_tags is None else g_y_axis_tags
    g_guide_tags = "" if g_guide_tags is None else g_guide_tags

    # FIXME: remove the style attribute on the surrounding div
    return f'<div style="width:500px;height:200px"><svg role="img" "viewBox="{viewbox} "style=height:{svg_height};margin-left:auto;margin-right:auto;font-size:inherit;overflow:visible;vertical-align:middle;position:relative;">{svg_defs}{svg_style}{ref_area_tags}{area_path_tags}{data_path_tags}{ref_line_tags}{circle_tags}{g_y_axis_tags}{g_guide_tags}</svg></div>'


def _generate_nanoplot(
    y_vals: str,
    y_ref_line: Optional[str] = None,
    y_ref_area: Optional[str] = None,
    x_vals: Optional[str] = None,
    expand_x: Optional[str] = None,
    expand_y: Optional[str] = None,
    missing_vals: str = "gap",
    all_y_vals: Optional[str] = None,
    all_single_y_vals: Optional[str] = None,
    plot_type: str = "line",
    line_type: str = "curved",
    currency: Optional[str] = None,
    y_val_fmt_fn: Optional[str] = None,
    y_axis_fmt_fn: Optional[str] = None,
    y_ref_line_fmt_fn: Optional[str] = None,
    data_point_radius: int = 10,
    data_point_stroke_color: str = "#FFFFFF",
    data_point_stroke_width: int = 4,
    data_point_fill_color: str = "#FF0000",
    data_line_stroke_color: str = "#4682B4",
    data_line_stroke_width: int = 8,
    data_area_fill_color: str = "#FF0000",
    data_bar_stroke_color: str = "#3290CC",
    data_bar_stroke_width: int = 4,
    data_bar_fill_color: str = "#3FB5FF",
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
    show_ref_line: bool = True,
    show_ref_area: bool = True,
    show_vertical_guides: bool = True,
    show_y_axis_guide: bool = True,
    interactive_data_values: bool = True,
    svg_height: str = "2em",
) -> str:

    # Ensure that arguments are matched
    _match_arg(
        x=missing_vals,
        lst=["gap", "marker", "zero", "remove"],
    )
    _match_arg(
        x=line_type,
        lst=["curved", "straight"],
    )

    # Initialize several local `*_tags` variables with `None`
    ref_area_tags = None
    area_path_tags = None
    data_path_tags = None
    zero_line_tags = None
    bar_tags = None
    boxplot_tags = None
    ref_line_tags = None
    circle_tags = None
    g_y_axis_tags = None
    g_guide_tags = None

    # Initialize the `single_horizontal_bar` variable with `False`
    single_horizontal_bar = False

    # If the number of `y` values is zero or if all consist of NA values,
    # return an empty string
    if len(y_vals) == 0:
        return ""

    # If all `y` values are NA, return an empty string
    # TODO: Do this with the `pd_na()` function
    if all(pd.isna(y_vals)):
        return ""

    # Get the number of data points for `y`
    num_y_vals = len(y_vals)

    # Handle case where `x_vals` exists (i.e., is not `NULL`)
    if x_vals is not None:

        # If the number of `x` values is zero or an empty string,
        # return an empty string
        if len(x_vals) == 0:
            return ""
        if all(pd.isna(x_vals)):
            return ""

        # Get the number of data points for `x`
        num_x_vals = len(x_vals)

        # Ensure that, if there are `x` values, the number of `x`
        # and `y` values matches
        if num_x_vals != num_y_vals:
            raise ValueError(
                f"""The number of `x` and `y` values must match.
                The `x` value length is: {num_x_vals}
                The `y` value length is: {num_y_vals}
                """
            )

        # Handle missing values in `x_vals` through removal (i.e., missing
        # values in `x_vals` means removal of positional values from both
        # `x_vals` and `y_vals`)
        if any(pd.isna(x_vals)):
            # Determine which values from `x_vals` are non-missing values
            x_vals_non_missing = ~pd.isna(x_vals)

            # Retain only `x_vals_non_missing` from `x_vals` and `y_vals`
            x_vals = x_vals[x_vals_non_missing]
            y_vals = y_vals[x_vals_non_missing]

        # If `x` values are present, we cannot use a curved line so
        # we'll force the use of the 'straight' line type
        line_type = "straight"

    # For the `missing_vals` options of 'zero' or 'remove', either replace NAs
    # with `0` or remove NAs entirely
    if missing_vals == "zero":
        y_vals = y_vals.fillna(0)

    # If `missing_vals` is 'remove', remove NAs from `y_vals`
    if missing_vals == "remove":
        y_vals = y_vals.dropna()

        if x_vals is not None:
            # Remove the corresponding `x` values for the removed `y` values
            x_vals = x_vals[y_vals.index]

    # Determine the total number of `y` values available
    num_y_vals = len(y_vals)

    # If the number of y_vals is `1` and we requested a 'bar' plot, then
    # reset several parameters
    if num_y_vals == 1 and plot_type == "bar":

        single_horizontal_bar = True
        show_data_points = False
        show_data_line = False
        show_data_area = False
        show_ref_line = False
        show_ref_area = False
        show_vertical_guides = False
        show_y_axis_guide = False

    # If this is a boxplot, set several parameters
    if plot_type == "boxplot":

        show_data_points = False
        show_data_line = False
        show_data_area = False
        show_ref_line = False
        show_ref_area = False
        show_vertical_guides = False
        show_y_axis_guide = False

    # Find out whether the collection of non-NA `y` values are all integer-like
    y_vals_integerlike = _is_integerlike(val_list=y_vals)

    # Get the max and min of the `y` scale from the `y` data values
    y_scale_max = _get_extreme_value(y_vals, stat="max")
    y_scale_min = _get_extreme_value(y_vals, stat="min")

    # Handle cases where collection of `y_vals` is invariant
    if y_scale_min == y_scale_max and expand_y is None:

        if y_scale_min == 0:
            expand_y_dist = 5
        else:
            expand_y_dist = (y_scale_min / 10) * 2

        # Expand the `y` scale, centering around the `y_scale_min` value
        expand_y = [y_scale_min - expand_y_dist, y_scale_min + expand_y_dist]

    # Ensure that a reference line or reference area isn't shown if None or
    # any of its directives is missing
    if y_ref_line is None or (y_ref_line is not None and pd.isna(y_ref_line)):
        show_ref_line = False

    if y_ref_area is None:
        show_ref_area = False

    if y_ref_area is not None and (pd.isna(y_ref_area[0]) or pd.isna(y_ref_area[1])):
        show_ref_area = False

    # Determine the width of the data plot area; for plots where `x_vals`
    # are available, we'll use a fixed width of `500` (px), and for plots
    # where `x_vals` aren't present, we'll adjust the final width based
    # on the fixed interval between data points (this is dependent on the
    # number of data points)
    if x_vals is not None or single_horizontal_bar or plot_type == "boxplot":
        data_x_width = 600
    else:
        # Obtain a sensible, fixed interval between data points in px
        if num_y_vals <= 20:
            x_d = 50
        elif num_y_vals <= 30:
            x_d = 40
        elif num_y_vals <= 40:
            x_d = 30
        elif num_y_vals <= 50:
            x_d = 25
        else:
            x_d = 20

        data_x_width = num_y_vals * x_d

    # Define the top-left of the plot area
    left_x = 0
    top_y = 0

    # Define the safe zone distance from top/bottom and left/right edges
    safe_y_d = 15
    safe_x_d = 50

    # Define the height of the plot area that bounds the data points
    data_y_height = 100

    # Determine the bottom-right of the plot area based on the quantity of data
    bottom_y = safe_y_d + data_y_height + safe_y_d
    right_x = safe_x_d + data_x_width + safe_x_d

    viewbox = f"{left_x} {top_y} {right_x} {bottom_y}"

    #
    # If there is a reference line and/or reference area, the values for these
    # need to be generated and integrated in the `normalize_y_vals()` operation
    # so that there are normalized values in relation to the data points
    #

    if plot_type == "line":

        if show_ref_line and show_ref_area:

            # Case where there is both a reference line and a reference area

            #
            # Resolve the reference line
            #

            if (
                y_ref_line is not None
                and _val_is_str(y_ref_line)
                and y_ref_line in REFERENCE_LINE_KEYWORDS
            ):
                y_ref_line = _generate_ref_line_from_keyword(vals=y_vals, keyword=y_ref_line)

            #
            # Resolve the reference area
            #

            if y_ref_area is not None:
                y_ref_area_1 = y_ref_area[0]
                y_ref_area_2 = y_ref_area[1]

                if _val_is_numeric(y_ref_area_1):
                    y_ref_area_line_1 = y_ref_area_1

                if _val_is_numeric(y_ref_area_2):
                    y_ref_area_line_2 = y_ref_area_2

                if _val_is_str(y_ref_area_1) and y_ref_area_1 in REFERENCE_LINE_KEYWORDS:
                    y_ref_area_line_1 = _generate_ref_line_from_keyword(
                        vals=y_vals, keyword=y_ref_area_1
                    )

                if _val_is_str(y_ref_area_2) and y_ref_area_2 in REFERENCE_LINE_KEYWORDS:
                    y_ref_area_line_2 = _generate_ref_line_from_keyword(
                        vals=y_vals, keyword=y_ref_area_2
                    )

                y_ref_area_lines_sorted = sorted([y_ref_area_line_1, y_ref_area_line_2])
                y_ref_area_l = y_ref_area_lines_sorted[0]
                y_ref_area_u = y_ref_area_lines_sorted[1]

            # Recompute the `y` scale min and max values
            y_scale_max = _get_extreme_value(
                y_vals, y_ref_line, y_ref_area_l, y_ref_area_u, expand_y, stat="max"
            )
            y_scale_min = _get_extreme_value(
                y_vals, y_ref_line, y_ref_area_l, y_ref_area_u, expand_y, stat="min"
            )

            # Scale to proportional values
            y_proportions_list = _normalize_to_dict(
                vals=y_vals,
                ref_line=y_ref_line,
                ref_area_l=y_ref_area_l,
                ref_area_u=y_ref_area_u,
                expand_y=expand_y,
            )

            y_proportions = y_proportions_list["vals"]
            y_proportion_ref_line = y_proportions_list["ref_line"][0]
            y_proportions_ref_area_l = y_proportions_list["ref_area_l"][0]
            y_proportions_ref_area_u = y_proportions_list["ref_area_u"][0]

            # Scale reference line and reference area boundaries
            data_y_ref_line = safe_y_d + ((1 - y_proportion_ref_line) * data_y_height)
            data_y_ref_area_l = safe_y_d + ((1 - y_proportions_ref_area_l) * data_y_height)
            data_y_ref_area_u = safe_y_d + ((1 - y_proportions_ref_area_u) * data_y_height)

        elif show_ref_line:

            # Case where there is a reference line
            if (
                y_ref_line is not None
                and _val_is_str(y_ref_line)
                and y_ref_line in REFERENCE_LINE_KEYWORDS
            ):
                y_ref_line = _generate_ref_line_from_keyword(vals=y_vals, keyword=y_ref_line)

            # Recompute the `y` scale min and max values
            y_scale_max = _get_extreme_value(y_vals, y_ref_line, expand_y, stat="max")
            y_scale_min = _get_extreme_value(y_vals, y_ref_line, expand_y, stat="min")

            # Scale to proportional values
            y_proportions_list = _normalize_to_dict(
                vals=y_vals, ref_line=y_ref_line, expand_y=expand_y
            )

            y_proportions = y_proportions_list["vals"]
            y_proportion_ref_line = y_proportions_list["ref_line"][0]

            # Scale the reference line
            data_y_ref_line = safe_y_d + ((1 - y_proportion_ref_line) * data_y_height)

        elif show_ref_area:

            # Case where there is a reference area
            if y_ref_area is not None:

                # TODO: Validate input for `y_ref_area`

                y_ref_area_1 = y_ref_area[0]
                y_ref_area_2 = y_ref_area[1]

                if _val_is_numeric(y_ref_area_1):
                    y_ref_area_line_1 = y_ref_area_1
                if _val_is_numeric(y_ref_area_2):
                    y_ref_area_line_2 = y_ref_area_2

                if _val_is_str(y_ref_area_1) and y_ref_area_1 in REFERENCE_LINE_KEYWORDS:
                    y_ref_area_line_1 = _generate_ref_line_from_keyword(
                        vals=y_vals, keyword=y_ref_area_1
                    )

                if _val_is_str(y_ref_area_2) and y_ref_area_2 in REFERENCE_LINE_KEYWORDS:
                    y_ref_area_line_2 = _generate_ref_line_from_keyword(
                        vals=y_vals, keyword=y_ref_area_2
                    )

                y_ref_area_lines_sorted = sorted([y_ref_area_line_1, y_ref_area_line_2])
                y_ref_area_l = y_ref_area_lines_sorted[0]
                y_ref_area_u = y_ref_area_lines_sorted[1]

            # Recompute the `y` scale min and max values
            y_scale_max = _get_extreme_value(
                y_vals, y_ref_area_l, y_ref_area_u, expand_y, stat="max"
            )
            y_scale_min = _get_extreme_value(
                y_vals, y_ref_area_l, y_ref_area_u, expand_y, stat="min"
            )

            # Scale to proportional values
            y_proportions_list = _normalize_to_dict(
                vals=y_vals, ref_area_l=y_ref_area_l, ref_area_u=y_ref_area_u, expand_y=expand_y
            )

            y_proportions = y_proportions_list["vals"]
            y_proportions_ref_area_l = y_proportions_list["ref_area_l"]
            y_proportions_ref_area_u = y_proportions_list["ref_area_u"]

            # Scale reference area boundaries
            data_y_ref_area_l = safe_y_d + ((1 - y_proportions_ref_area_l[0]) * data_y_height)
            data_y_ref_area_u = safe_y_d + ((1 - y_proportions_ref_area_u[0]) * data_y_height)

        else:

            # Case where there is no reference line or reference area

            # Recompute the `y` scale min and max values
            y_scale_max = _get_extreme_value(y_vals, expand_y, stat="max")
            y_scale_min = _get_extreme_value(y_vals, expand_y, stat="min")

            # Scale to proportional values
            y_proportions_list = _normalize_to_dict(vals=y_vals, expand_y=expand_y)

            y_proportions = y_proportions_list["vals"]

    if plot_type == "bar" or plot_type == "boxplot":
        pass

    # If x values are present then normalize them between [0, 1]; if
    # there are no x values, generate equally-spaced x values according
    # to the number of y values
    if plot_type == "line" and x_vals is not None:
        pass
    else:
        x_proportions = np.linspace(0, 1, num_y_vals)

    # Create normalized (and inverted for SVG) data `x` and `y` values
    for i in range(len(y_proportions)):
        y_proportions[i] = safe_y_d + ((1 - y_proportions[i]) * data_y_height)

    for i in range(len(x_proportions)):
        x_proportions[i] = (data_x_width * x_proportions[i]) + safe_x_d

    data_y_points = y_proportions
    data_x_points = x_proportions

    #
    # Ensure that certain options have their lengths checked and
    # expanded to length `num_y_vals`
    #

    data_point_radius = _normalize_option_list(option_list=data_point_radius, num_y_vals=num_y_vals)
    data_point_stroke_color = _normalize_option_list(
        option_list=data_point_stroke_color, num_y_vals=num_y_vals
    )
    data_point_stroke_width = _normalize_option_list(
        option_list=data_point_stroke_width, num_y_vals=num_y_vals
    )
    data_point_fill_color = _normalize_option_list(
        option_list=data_point_fill_color, num_y_vals=num_y_vals
    )
    data_bar_stroke_color = _normalize_option_list(
        option_list=data_bar_stroke_color, num_y_vals=num_y_vals
    )
    data_bar_stroke_width = _normalize_option_list(
        option_list=data_bar_stroke_width, num_y_vals=num_y_vals
    )
    data_bar_fill_color = _normalize_option_list(
        option_list=data_bar_fill_color, num_y_vals=num_y_vals
    )

    #
    # Generate data segments by defining `start` and `end` vectors (these
    # are guaranteed to be of the same length); these the segments of data
    # they receive line segments and adjoining areas
    #

    # Use run-length encoding to determine the segments of data

    # rle_data_y_points = pd.Series(data_y_points).diff().ne(0).cumsum()

    # end_data_y_points = np.cumsum(rle_data_y_points.lengths)

    # start_data_y_points = end_data_y_points - rle_data_y_points.lengths + 1

    start_data_y_points = [0]
    end_data_y_points = [len(data_y_points)]
    n_segments = 1

    #
    # Generate a curved data line
    #

    if plot_type == "line" and show_data_line and line_type == "curved":

        data_path_tags = []

        for i in range(n_segments):

            curve_x = data_x_points[start_data_y_points[i] : end_data_y_points[i]]
            curve_y = data_y_points[start_data_y_points[i] : end_data_y_points[i]]

            curved_path_string = [f"M {curve_x[0]},{curve_y[0]}"]

            for j in range(1, len(curve_x)):

                point_b1 = f"{curve_x[j - 1] + x_d / 2},{curve_y[j - 1]}"
                point_b2 = f"{curve_x[j] - x_d / 2},{curve_y[j]}"
                point_i = f"{curve_x[j]},{curve_y[j]}"

                path_string_j = f"C {point_b1} {point_b2} {point_i}"

                curved_path_string.append(path_string_j)

            curved_path_string_i = " ".join(curved_path_string)

            data_path_tags_i = f'<path d="{curved_path_string_i}" stroke="{data_line_stroke_color}" stroke-width="{data_line_stroke_width}" fill="none"></path>'

            data_path_tags.append(data_path_tags_i)

        data_path_tags = "\n".join(data_path_tags)

    if plot_type == "line" and show_data_line and line_type == "straight":

        data_path_tags = []

        for i in range(n_segments):

            line_x = data_x_points[start_data_y_points[i] : end_data_y_points[i]]
            line_y = data_y_points[start_data_y_points[i] : end_data_y_points[i]]

            line_xy = " ".join([f"{x},{y}" for x, y in zip(line_x, line_y)])

            data_path_tags_i = f'<polyline points="{line_xy}" stroke="{data_line_stroke_color}" stroke-width="{data_line_stroke_width}" fill="none"></polyline>'

            data_path_tags.append(data_path_tags_i)

        data_path_tags = "".join(data_path_tags)

    #
    # Generate data points
    #

    if plot_type == "line" and show_data_points:

        circle_strings = []

        for i, _ in enumerate(data_x_points):

            data_point_radius_i = data_point_radius[i]
            data_point_stroke_color_i = data_point_stroke_color[i]
            data_point_stroke_width_i = data_point_stroke_width[i]
            data_point_fill_color_i = data_point_fill_color[i]

            if data_y_points[i] is None:

                if missing_vals == "marker":

                    # Create a symbol that should denote that a missing value is present
                    circle_strings_i = f'<circle cx="{data_x_points[i]}" cy="{safe_y_d + (data_y_height / 2)}" r="{data_point_radius_i + (data_point_radius_i / 2)}" stroke="red" stroke-width="{data_point_stroke_width_i}" fill="white"></circle>'

                else:
                    continue

            else:
                circle_strings_i = f'<circle cx="{data_x_points[i]}" cy="{data_y_points[i]}" r="{data_point_radius_i}" stroke="{data_point_stroke_color_i}" stroke-width="{data_point_stroke_width_i}" fill="{data_point_fill_color_i}"></circle>'

            circle_strings.append(circle_strings_i)

        circle_tags = "".join(circle_strings)

    #
    # Generate data bars
    #

    if plot_type == "bar" and single_horizontal_bar is False:
        pass

    #
    # Generate single horizontal data bars
    #

    if plot_type == "bar" and single_horizontal_bar:
        pass

    #
    # Generate box plots
    #

    if plot_type == "boxplot":
        pass

    #
    # Generate zero line for bar plots
    #

    if plot_type == "bar" and single_horizontal_bar is False:
        pass

    #
    # Generate reference line
    #

    if show_ref_line:

        stroke = reference_line_color
        stroke_width = 1
        stroke_dasharray = "4 3"
        transform = ""
        stroke_linecap = "round"
        vector_effect = "non-scaling-stroke"

        y_ref_line = _format_number_compactly(
            val=y_ref_line, currency=currency, as_integer=y_vals_integerlike, fn=y_ref_line_fmt_fn
        )

        ref_line_tags = f'<g class="ref-line"><rect x="{data_x_points[0] - 10}" y="{data_y_ref_line - 10}" width="{data_x_width + 20}" height="20" stroke="transparent" stroke-width="1" fill="transparent"></rect><line class="ref-line" x1="{data_x_points[0]}" y1="{data_y_ref_line}" x2="{data_x_width + safe_x_d}" y2="{data_y_ref_line}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-dasharray="{stroke_dasharray}" transform="{transform}" stroke-linecap="{stroke_linecap}" vector-effect="{vector_effect}"></line><text x="{data_x_width + safe_x_d + 10}" y="{data_y_ref_line + 10}" fill="transparent" stroke="transparent" font-size="30px">{y_ref_line}</text></g>'

    #
    # Generate reference area
    #

    if show_ref_area:

        fill = reference_area_fill_color

        p_ul = f"{data_x_points[0]},{data_y_ref_area_u}"
        p_ur = f"{data_x_points[-1]},{data_y_ref_area_u}"
        p_lr = f"{data_x_points[-1]},{data_y_ref_area_l}"
        p_ll = f"{data_x_points[0]},{data_y_ref_area_l}"

        ref_area_path = f"M{p_ul},{p_ur},{p_lr},{p_ll}Z"

        ref_area_tags = f'<path d="{ref_area_path}" stroke="transparent" stroke-width="2" fill="{fill}" fill-opacity="0.8"></path>'

    #
    # Generate y-axis guide
    #

    if show_y_axis_guide:

        rect_tag = f'<rect x="{left_x}" y="{top_y}" width="{safe_x_d + 15}" height="{bottom_y}" stroke="transparent" stroke-width="0" fill="transparent"></rect>'

        if _is_integerlike(val_list=[y_scale_max]) and _is_integerlike(val_list=[y_scale_min]):
            y_axis_guide_vals_integerlike = True
        else:
            y_axis_guide_vals_integerlike = False

        y_value_max_label = _format_number_compactly(
            val=y_scale_max,
            currency=currency,
            as_integer=y_axis_guide_vals_integerlike,
            fn=y_axis_fmt_fn,
        )

        y_value_min_label = _format_number_compactly(
            val=y_scale_min,
            currency=currency,
            as_integer=y_axis_guide_vals_integerlike,
            fn=y_axis_fmt_fn,
        )

        text_strings_min = f'<text x="{left_x}" y="{safe_y_d + data_y_height + safe_y_d - data_y_height / 25}" fill="transparent" stroke="transparent" font-size="25">{y_value_min_label}</text>'

        text_strings_max = f'<text x="{left_x}" y="{safe_y_d + data_y_height / 25}" fill="transparent" stroke="transparent" font-size="25">{y_value_max_label}</text>'

        g_y_axis_tags = f'<g class="y-axis-line">{rect_tag}{text_strings_max}{text_strings_min}</g>'

    #
    # Generate vertical data point guidelines
    #

    if show_vertical_guides:

        g_guide_strings = []

        for i, _ in enumerate(data_x_points):

            rect_strings_i = f'<rect x="{data_x_points[i] - 10}" y="{top_y}" width="20" height="{bottom_y}" stroke="transparent" stroke-width="{vertical_guide_stroke_width}" fill="transparent"></rect>'

            y_value_i = _format_number_compactly(
                val=y_vals[i], currency=currency, as_integer=y_vals_integerlike, fn=y_val_fmt_fn
            )

            x_text = data_x_points[i] + 10

            if y_value_i == "NA":
                x_text = x_text + 2

            text_strings_i = f'<text x="{x_text}" y="{safe_y_d + 5}" fill="transparent" stroke="transparent" font-size="30px">{y_value_i}</text>'

            g_guide_strings_i = f'<g class="vert-line">{rect_strings_i}{text_strings_i}</g>'

            g_guide_strings.append(g_guide_strings_i)

        g_guide_tags = "".join(g_guide_strings)

    #
    # Generate background with repeating line pattern
    #

    svg_defs = (
        f"<defs>"
        f'<pattern id="area_pattern" width="8" height="8" patternUnits="userSpaceOnUse">'
        f'<path class="pattern-line" d="M 0,8 l 8,-8 M -1,1 l 4,-4 M 6,10 l 4,-4" stroke="'
        f"{data_area_fill_color}"
        f'" stroke-width="1.5" stroke-linecap="round" shape-rendering="geometricPrecision">'
        f"</pattern>"
        f"</defs>"
    )

    if plot_type == "line" and show_data_area:

        area_path_tags = []

        for i in range(n_segments):

            area_x = data_x_points[start_data_y_points[i] : end_data_y_points[i]]
            area_y = data_y_points[start_data_y_points[i] : end_data_y_points[i]]

            area_path_string = []

            for j in range(1, len(area_x)):

                area_path_j = f"{area_x[j]},{area_y[j]}"
                area_path_string.append(area_path_j)

            area_path_i = f"M {' '.join(area_path_string)} {area_x[-1]},{bottom_y - safe_y_d + data_point_radius[0]} {area_x[0]},{bottom_y - safe_y_d + data_point_radius[0]} Z"

            area_path_tag_i = f'<path class="area-closed" d="{area_path_i}" stroke="transparent" stroke-width="2" fill="url(#area_pattern)" fill-opacity="0.7"></path>'

            area_path_tags.append(area_path_tag_i)

        area_path_tags = " ".join(area_path_tags)

    #
    # Generate style tag for vertical guidelines and y-axis
    #

    hover_param = ":hover" if interactive_data_values else ""

    svg_style = (
        f"<style> text {{ font-family: ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace; stroke-width: 0.15em; paint-order: stroke; stroke-linejoin: round; cursor: default; }} "
        f".vert-line{hover_param} rect {{ fill: {vertical_guide_stroke_color}; fill-opacity: 40%; stroke: #FFFFFF60; color: red; }} "
        f".vert-line{hover_param} text {{ stroke: white; fill: #212427; }} "
        f".horizontal-line{hover_param} text {{stroke: white; fill: #212427; }} "
        f".ref-line{hover_param} rect {{ stroke: #FFFFFF60; }} "
        f".ref-line{hover_param} line {{ stroke: #FF0000; }} "
        f".ref-line{hover_param} text {{ stroke: white; fill: #212427; }} "
        f".y-axis-line{hover_param} rect {{ fill: #EDEDED; fill-opacity: 60%; stroke: #FFFFFF60; color: red; }} "
        f".y-axis-line{hover_param} text {{ stroke: white; stroke-width: 0.20em; fill: #1A1C1F; }} "
        f"</style>"
    )

    nanoplot_svg = _construct_nanoplot_svg(
        viewbox=viewbox,
        svg_height=svg_height,
        svg_defs=svg_defs,
        svg_style=svg_style,
        ref_area_tags=ref_area_tags,
        area_path_tags=area_path_tags,
        data_path_tags=data_path_tags,
        ref_line_tags=ref_line_tags,
        circle_tags=circle_tags,
        g_y_axis_tags=g_y_axis_tags,
        g_guide_tags=g_guide_tags,
    )

    print(nanoplot_svg)

    return nanoplot_svg
