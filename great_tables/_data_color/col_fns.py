"""Color-mapping function factories for use with `data_color(fn=...)`.

These are modeled on the `col_numeric()`, `col_bin()`, and `col_factor()` functions from the R
**scales** package. Each one returns a function that takes a list of values and returns a list of
colors of the same length.
"""

from __future__ import annotations

from bisect import bisect_left, bisect_right
from math import isinf, isnan
from typing import Any, Callable

from .base import (
    _html_color,
    _midpoint_stops,
    _rescale_stops,
    _resolve_palette,
    _validate_midpoint,
)
from .palettes import GradientPalette

ColorFn = Callable[[list[Any]], "list[str | None]"]


def col_numeric(
    palette: str | list[str] | None = None,
    domain: list[int] | list[float] | None = None,
    midpoint: int | float | None = None,
    stops: list[int | float | str] | None = None,
    na_color: str | None = None,
    reverse: bool = False,
    truncate: bool = False,
) -> ColorFn:
    """
    Create a color-mapping function for continuous numeric values.

    The `col_numeric()` helper returns a function that linearly maps numeric values onto a color
    palette (interpolating between the palette's colors). The returned function is designed to be
    passed to the `fn=` argument of [`data_color()`](`great_tables.GT.data_color`), but it can be
    called on any list of values.

    Parameters
    ----------
    palette
        The colors to interpolate between. This can be a list of colors (as hexadecimal values or
        color names) or the name of a ColorBrewer or viridis palette (see
        [`data_color()`](`great_tables.GT.data_color`) for the available names). If `None`, then a
        default palette will be used.
    domain
        The range of values to map onto the palette, given as `[min, max]`. Values outside of this
        range receive the missing-value color (unless `truncate=True`). If `None`, then the domain
        is taken from the range of the (non-missing) values supplied to the returned function each
        time it is called (or, with `midpoint=`, a range made symmetric around the midpoint). This
        can't be used together with `stops=`.
    midpoint
        A value that receives the color at the center of the palette. If `domain=` is `None`, then
        the domain is made symmetric around the midpoint, reaching as far as the value furthest
        from it. If `domain=` is supplied, then each side of the midpoint is scaled separately to
        its end of the domain (and the midpoint must lie within the domain). This works in the same
        way as the `midpoint=` argument of [`data_color()`](`great_tables.GT.data_color`) and
        can't be used together with `stops=`.
    stops
        A list giving the value at which each palette color is reached, with one entry per color
        in the palette (after any ColorBrewer or viridis palette name is expanded). Colors are
        interpolated between neighboring stops. Each stop can be either a number (a data value) or
        a percentage string from `"0%"` to `"100%"` (a position within the range of the values
        supplied to the returned function, extended to include any numeric stops). For example,
        `stops=["0%", 0, "100%"]` pins the lowest value, zero, and the highest value, whatever the
        range of the values. Stops must be in non-decreasing order once resolved. A repeated stop
        creates a sharp change between two colors, with a value exactly at that stop taking the
        later color. The outermost stops act as the domain, so values beyond them receive the
        missing-value color (unless `truncate=True`).
    na_color
        The color to use for missing values and values outside of the domain. If `None`, then the
        returned function gives `None` for those values, which lets `data_color()` apply its own
        `na_color=` color.
    reverse
        Should the order of the palette colors be reversed? This doesn't affect `stops=`, which
        apply to the colors in their reversed order.
    truncate
        If `True`, then values outside of the domain (or the outermost `stops=`) are treated as the
        nearest end of it, so they receive the first or last color of the palette. If `False` (the
        default), then they receive the missing-value color.

    Returns
    -------
    Callable[[list[Any]], list[str | None]]
        A function that takes a list of numeric values and returns a list of hexadecimal colors.

    Examples
    --------
    A diverging palette with a domain centered on zero colors negative values increasingly red and
    positive values increasingly green, the further they are from zero:

    ```{python}
    import pandas as pd
    from great_tables import GT, col_numeric

    df = pd.DataFrame(
        {
            "region": ["North", "South", "East", "West", "Central"],
            "change": [12.5, -8.1, 0.0, 3.2, -1.0],
        }
    )

    GT(df).data_color(
        columns="change",
        fn=col_numeric(palette=["#D7191C", "white", "#1A9641"], domain=[-15, 15]),
    )
    ```

    Rather than fixing the domain, we can give a `midpoint=`. The domain is then made symmetric
    around the midpoint, reaching as far as the value furthest from it:

    ```{python}
    GT(df).data_color(
        columns="change",
        fn=col_numeric(palette=["#D7191C", "white", "#1A9641"], midpoint=0),
    )
    ```

    With `stops=`, every palette color can be pinned to a value. Stops can be data values or
    percentages of the way through the range of values. Here, the lowest value is fully red, zero
    is white, and the highest value is fully green, so each side uses its full range of colors:

    ```{python}
    GT(df).data_color(
        columns="change",
        fn=col_numeric(palette=["#D7191C", "white", "#1A9641"], stops=["0%", 0, "100%"]),
    )
    ```

    Repeating a stop makes a sharp change in color at that value. Here, values below zero are
    shades of orange and values from zero up are shades of purple:

    ```{python}
    GT(df).data_color(
        columns="change",
        fn=col_numeric(
            palette=["#E66101", "#FDB863", "#B2ABD2", "#5E3C99"],
            stops=["0%", 0, 0, "100%"],
        ),
    )
    ```

    With a narrower domain, `truncate=True` saturates the colors of values beyond its limits rather
    than leaving them uncolored. Here, anything above `5` is fully green and anything below `-5`
    is fully red:

    ```{python}
    GT(df).data_color(
        columns="change",
        fn=col_numeric(palette=["#D7191C", "white", "#1A9641"], domain=[-5, 5], truncate=True),
    )
    ```
    """

    colors = _resolve_palette(palette=palette, reverse=reverse)
    na_color = _resolve_na_color(na_color)

    if domain is not None:
        _validate_numeric_domain(domain)

    if stops is not None:
        if domain is not None or midpoint is not None:
            raise ValueError("`stops=` can't be used together with `domain=` or `midpoint=`.")

        _validate_stops(stops, n_colors=len(colors))

    if midpoint is not None:
        _validate_midpoint(midpoint, domain=domain)

    def color_fn(vals: list[Any]) -> list[str | None]:
        vals = list(vals)
        _validate_numeric_vals(vals, fn_name="col_numeric")

        present = [x for x in vals if not _is_missing(x)]

        if midpoint is not None or stops is not None:
            if not present:
                return [na_color] * len(vals)

            present_vals = [None if _is_missing(x) else x for x in vals]

            if midpoint is not None:
                knots, positions = _midpoint_stops(midpoint, domain=domain, vals=present_vals)
            else:
                knots = _resolve_stops(stops, vals=present)
                n = len(knots)
                positions = [i / max(n - 1, 1) for i in range(n)]

            scaled = _rescale_stops(
                present_vals, stops=knots, positions=positions, truncate=truncate
            )

            return _scaled_to_colors(scaled, colors=colors, na_color=na_color)

        if domain is not None:
            domain_min, domain_max = domain
        elif present:
            domain_min, domain_max = min(present), max(present)
        else:
            return [na_color] * len(vals)

        domain_range = domain_max - domain_min

        scaled: list[float | None] = []
        for x in vals:
            if not _is_missing(x) and truncate:
                x = min(max(x, domain_min), domain_max)

            if _is_missing(x) or x < domain_min or x > domain_max:
                scaled.append(None)
            elif domain_range == 0:
                scaled.append(0.0)
            else:
                scaled.append((x - domain_min) / domain_range)

        return _scaled_to_colors(scaled, colors=colors, na_color=na_color)

    return color_fn


def col_bin(
    palette: str | list[str] | None = None,
    domain: list[int] | list[float] | None = None,
    bins: int | list[int] | list[float] = 7,
    na_color: str | None = None,
    right: bool = False,
    reverse: bool = False,
    truncate: bool = False,
) -> ColorFn:
    """
    Create a color-mapping function for numeric values cut into bins.

    The `col_bin()` helper returns a function that divides numeric values into bins and gives
    every value in a bin the same color. The bin colors are spaced evenly along the palette. The
    returned function is designed to be passed to the `fn=` argument of
    [`data_color()`](`great_tables.GT.data_color`), but it can be called on any list of values.

    Parameters
    ----------
    palette
        The colors to use. This can be a list of colors (as hexadecimal values or color names) or
        the name of a ColorBrewer or viridis palette (see
        [`data_color()`](`great_tables.GT.data_color`) for the available names). If `None`, then a
        default palette will be used.
    domain
        The range of values to divide into bins, given as `[min, max]`. This is only used when
        `bins=` is an integer. If `None`, then the domain is taken from the range of the
        (non-missing) values supplied to the returned function each time it is called.
    bins
        Either the number of equal-width bins to cut the domain into, or a list of two or more bin
        boundaries (e.g., `[0, 10, 50, 100]`). Values outside of the outermost boundaries receive
        the missing-value color (unless `truncate=True`).
    na_color
        The color to use for missing values and values outside of the bins. If `None`, then the
        returned function gives `None` for those values, which lets `data_color()` apply its own
        `na_color=` color.
    right
        Should the bins be closed on the right (and open on the left)? By default, bins include
        their lower boundary but not their upper one (the last bin includes both). With
        `right=True`, bins include their upper boundary but not their lower one (the first bin
        includes both).
    reverse
        Should the order of the palette colors be reversed?
    truncate
        If `True`, then values below the lowest boundary are placed in the first bin and values
        above the highest boundary are placed in the last bin. If `False` (the default), then they
        receive the missing-value color.

    Returns
    -------
    Callable[[list[Any]], list[str | None]]
        A function that takes a list of numeric values and returns a list of hexadecimal colors.

    Examples
    --------
    Let's color the `currency` column of the `exibble` dataset in three bins with explicit
    boundaries:

    ```{python}
    from great_tables import GT, col_bin
    from great_tables.data import exibble

    GT(exibble[["currency", "char"]]).data_color(
        columns="currency",
        fn=col_bin(palette="Blues", bins=[0, 10, 1000, 100000]),
        na_color="lightgray",
    )
    ```
    """

    colors = _resolve_palette(palette=palette, reverse=reverse)
    na_color = _resolve_na_color(na_color)

    if domain is not None:
        _validate_numeric_domain(domain)

    if isinstance(bins, int):
        if bins < 1:
            raise ValueError(f"`bins=` must be at least 1 when given as an integer, not {bins}.")
        fixed_breaks = None
    else:
        fixed_breaks = sorted(bins)
        if len(fixed_breaks) < 2:
            raise ValueError("`bins=` must contain at least two boundaries when given as a list.")

    def color_fn(vals: list[Any]) -> list[str | None]:
        vals = list(vals)
        _validate_numeric_vals(vals, fn_name="col_bin")

        if fixed_breaks is not None:
            breaks = fixed_breaks
        else:
            present = [x for x in vals if not _is_missing(x)]

            if domain is not None:
                domain_min, domain_max = domain
            elif present:
                domain_min, domain_max = min(present), max(present)
            else:
                return [na_color] * len(vals)

            assert isinstance(bins, int)
            step = (domain_max - domain_min) / bins
            breaks = [domain_min + step * i for i in range(bins)] + [domain_max]

        n_bins = len(breaks) - 1
        lower, upper = breaks[0], breaks[-1]

        scaled: list[float | None] = []
        for x in vals:
            if not _is_missing(x) and truncate:
                x = min(max(x, lower), upper)

            if _is_missing(x) or x < lower or x > upper:
                scaled.append(None)
                continue

            if right:
                idx = max(bisect_left(breaks, x) - 1, 0)
            else:
                idx = min(bisect_right(breaks, x) - 1, n_bins - 1)

            scaled.append(idx / (n_bins - 1) if n_bins > 1 else 0.0)

        return _scaled_to_colors(scaled, colors=colors, na_color=na_color)

    return color_fn


def col_factor(
    palette: str | list[str] | None = None,
    domain: list[Any] | None = None,
    na_color: str | None = None,
    reverse: bool = False,
) -> ColorFn:
    """
    Create a color-mapping function for categorical values.

    The `col_factor()` helper returns a function that gives each distinct value (or level) its own
    color. If the palette has at least as many colors as there are levels, then the levels take
    the palette colors in order; otherwise, colors are interpolated along the palette. The returned
    function is designed to be passed to the `fn=` argument of
    [`data_color()`](`great_tables.GT.data_color`), but it can be called on any list of values.

    Parameters
    ----------
    palette
        The colors to use. This can be a list of colors (as hexadecimal values or color names) or
        the name of a ColorBrewer or viridis palette (see
        [`data_color()`](`great_tables.GT.data_color`) for the available names). If `None`, then a
        default palette will be used.
    domain
        The levels to map to colors, in order. Values that aren't in the domain receive the
        missing-value color. If `None`, then the levels are the distinct (non-missing) values
        supplied to the returned function each time it is called, in their order of appearance.
    na_color
        The color to use for missing values and values not in the domain. If `None`, then the
        returned function gives `None` for those values, which lets `data_color()` apply its own
        `na_color=` color.
    reverse
        Should the order of the palette colors be reversed?

    Returns
    -------
    Callable[[list[Any]], list[str | None]]
        A function that takes a list of values and returns a list of hexadecimal colors.

    Examples
    --------
    Setting the `domain=` fixes the color of each level, no matter which levels are present in the
    column or in what order they appear:

    ```{python}
    import pandas as pd
    from great_tables import GT, col_factor

    df = pd.DataFrame(
        {
            "ticket": [101, 102, 103, 104, 105],
            "priority": ["low", "high", "medium", "high", "urgent"],
        }
    )

    GT(df).data_color(
        columns="priority",
        fn=col_factor(
            palette=["#FEF0D9", "#FDCC8A", "#FC8D59"],
            domain=["low", "medium", "high"],
            na_color="#D7301F",
        ),
    )
    ```
    """

    colors = _resolve_palette(palette=palette, reverse=reverse)
    na_color = _resolve_na_color(na_color)

    def color_fn(vals: list[Any]) -> list[str | None]:
        vals = list(vals)

        if domain is not None:
            levels = list(domain)
        else:
            levels: list[Any] = []
            for x in vals:
                if not _is_missing(x) and x not in levels:
                    levels.append(x)

        n_levels = len(levels)

        if n_levels == 0:
            return [na_color] * len(vals)

        level_colors = _sample_palette(colors[:n_levels], n=n_levels)
        lookup = dict(zip(levels, level_colors))

        return [na_color if _is_missing(x) else lookup.get(x, na_color) for x in vals]

    return color_fn


def _is_missing(x: Any) -> bool:
    if x is None:
        return True

    if isinstance(x, float):
        return isnan(x)

    # Cover pandas' `NA` and `NaT` without needing to import pandas
    return type(x).__name__ in ("NAType", "NaTType")


def _resolve_na_color(na_color: str | None) -> str | None:
    return None if na_color is None else _html_color(colors=[na_color])[0]


def _validate_numeric_domain(domain: list[int] | list[float]) -> None:
    if len(domain) != 2:
        raise ValueError(f"`domain=` must be a list of two values ([min, max]), not {domain!r}.")

    if domain[0] > domain[1]:
        raise ValueError(f"The first value in `domain=` must not exceed the second: {domain!r}.")


def _parse_percent_stop(stop: str) -> float | None:
    """Return the percentage in a stop like `"25%"` (or `None` if it isn't a valid percentage)."""

    text = stop.strip()

    if not text.endswith("%"):
        return None

    try:
        pct = float(text[:-1])
    except ValueError:
        return None

    return pct if 0 <= pct <= 100 else None


def _validate_stops(stops: list[int | float | str], n_colors: int) -> None:
    if len(stops) != n_colors:
        raise ValueError(
            f"`stops=` must have one value per palette color ({n_colors}), but has {len(stops)}."
        )

    numbers: list[float] = []
    percents: list[float] = []

    for stop in stops:
        if isinstance(stop, str):
            pct = _parse_percent_stop(stop)

            if pct is None:
                raise ValueError(
                    f"A string in `stops=` must be a percentage from '0%' to '100%', not {stop!r}."
                )

            percents.append(pct)

        elif (
            isinstance(stop, bool)
            or not isinstance(stop, (int, float))
            or isinf(stop)
            or isnan(stop)
        ):
            raise ValueError(
                f"Each value in `stops=` must be a finite number or a percentage string, not {stop!r}."
            )

        else:
            numbers.append(stop)

    for kind, seq in (("numbers", numbers), ("percentages", percents)):
        if any(a > b for a, b in zip(seq, seq[1:])):
            raise ValueError(f"The {kind} in `stops=` must be in non-decreasing order: {stops!r}.")


def _resolve_stops(stops: list[int | float | str], vals: list[float]) -> list[float]:
    """
    Resolve `stops=` to data values.

    Percentage stops are positions within the range spanning both the (non-missing) values in
    `vals=` and the numeric stops.
    """

    numbers = [stop for stop in stops if not isinstance(stop, str)]
    lo, hi = min(vals + numbers), max(vals + numbers)

    resolved = [
        lo + _parse_percent_stop(stop) / 100 * (hi - lo) if isinstance(stop, str) else stop  # type: ignore[operator]
        for stop in stops
    ]

    if any(a > b for a, b in zip(resolved, resolved[1:])):
        raise ValueError(
            f"The values in `stops=` must be in non-decreasing order once percentages are resolved "
            f"(against a range of [{lo!r}, {hi!r}]), but {stops!r} resolved to {resolved!r}."
        )

    return resolved


def _validate_numeric_vals(vals: list[Any], fn_name: str) -> None:
    for x in vals:
        if _is_missing(x):
            continue

        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError(
                f"The function created by `{fn_name}()` requires numeric values, but received a "
                f"value of type {type(x).__name__} ({x!r})."
            )

        if isinf(x):
            raise ValueError(f"The function created by `{fn_name}()` can't map infinite values.")


def _sample_palette(colors: list[str], n: int) -> list[str]:
    """Return `n` colors spaced evenly along a palette (interpolating where necessary)."""

    if len(colors) == 1 or n == 1:
        return [colors[0]] * n

    if len(colors) == n:
        return list(colors)

    positions = [i / (n - 1) for i in range(n)]
    return [color.upper() for color in GradientPalette(colors=colors)(positions)]  # type: ignore


def _scaled_to_colors(
    scaled: list[float | None], colors: list[str], na_color: str | None
) -> list[str | None]:
    """Map values in the range [0, 1] (or `None`) to colors along a palette."""

    if len(colors) == 1:
        return [na_color if x is None else colors[0] for x in scaled]

    mapped = GradientPalette(colors=colors)(scaled)  # type: ignore[arg-type]

    return [na_color if x is None else x.upper() for x in mapped]
