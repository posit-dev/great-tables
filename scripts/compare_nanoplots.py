"""
Compare nanoplot output between a git ref (e.g., `main`) and the working tree.

Thousands of nanoplots are rendered with both versions of great_tables: a grid of direct
`_generate_nanoplot()` calls (every plot type, reference line/area, missing-value option, x values,
expansion, and styling option, plus edge cases) and tables made with `fmt_nanoplot()` from pandas
and polars data. The output of every case (SVG, or the error/warning raised) is compared byte for
byte, so this is meant for checking that a refactor of the nanoplot code doesn't change any output.
The lasting regression tests for nanoplots are the snapshots in `tests/test_nanoplots_snap.py`.

The `--base` ref is extracted into a temporary directory (only the `great_tables` package) and each
version is rendered in its own subprocess. Outputs are written to `--out` (a temporary directory by
default) and never into the repository.

Usage:
    python scripts/compare_nanoplots.py                  # compare against `main`
    python scripts/compare_nanoplots.py --base v0.18.0   # compare against another ref
    python scripts/compare_nanoplots.py --html           # also write a side-by-side HTML page

The exit status is `1` when any case differs.
"""

from __future__ import annotations

import argparse
import difflib
import html
import json
import os
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------------------------
# Rendering (run in a subprocess, with the version of great_tables set by PYTHONPATH)
# ---------------------------------------------------------------------------------------------


def _fmt_kwargs(kw: dict) -> str:
    import math

    def r(v):
        if callable(v):
            return getattr(v, "__name__", "fn")
        if isinstance(v, float) and math.isnan(v):
            return "nan"
        if isinstance(v, list) and len(v) > 8:
            return f"[{', '.join(r(x) for x in v[:6])}, ... ({len(v)} items)]"
        if isinstance(v, list):
            return "[" + ", ".join(r(x) for x in v) + "]"
        return repr(v)

    return ", ".join(f"{k}={r(v)}" for k, v in kw.items())


def render(out_file: Path) -> None:
    """Render every case and write `{case_id: [section, output]}` to `out_file`."""

    import random
    import warnings

    results: dict[str, list[str]] = {}

    def run(section: str, case_id: str, fn) -> None:
        # The values of an invariant scale are jittered, so seed that randomness for each case
        random.seed(12345)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            try:
                out = fn()
            except Exception as e:  # errors are compared as well
                out = f"ERROR {type(e).__name__}: {e}"

        if w:
            out = "".join(f"WARNING {x.category.__name__}: {x.message}\n" for x in w) + out

        assert case_id not in results, f"Duplicate case id: {case_id}"
        results[case_id] = [section, out]

    import great_tables

    print(f"  (great_tables loaded from {Path(great_tables.__file__).parent})")

    _add_cases(run)

    out_file.write_text(json.dumps(results))


def _add_cases(run) -> None:
    """Add every case with `run(section, case_id, fn)`, where `fn()` returns the output."""

    import itertools
    import math

    import numpy as np
    import pandas as pd
    import polars as pl

    from great_tables import GT, nanoplot_options
    from great_tables._utils_nanoplots import _generate_nanoplot

    NAN = float("nan")
    fmt_kwargs = _fmt_kwargs

    # ---------------------------------------------------------------------------------------------
    # Part A: direct `_generate_nanoplot()` grid
    # ---------------------------------------------------------------------------------------------

    Y_SETS = {
        "mixed": [-5.3, 6.3, -2.3, 0, 2.3, 6.7, 14.2, 0, 2.3, 13.3],
        "pos_int": [1, 5, 3, 8, 2, 9, 4],
        "neg_float": [-1.5, -3.25, -0.5, -7.75, -2.0],
        "with_none": [4, None, 7, 2, None, None, 9, 3],
        "with_nan": [2.5, NAN, 3.5, 1.0, NAN],
        "na_edges": [None, 3, 6, 2, None],
        "invariant": [3, 3, 3, 3],
        "invariant_zero": [0, 0, 0],
        "invariant_neg": [-4.5, -4.5],
        "single": [5],
        "two": [1, 2],
        "large": [12000, 450000, 3_200_000, 1.5e15, 87_654],
        "small": [0.001, 0.005, 0.0002, 0.03, 0.75],
        "mid": [150, 820.5, 999, 101, 333],
        "len25": [((i * 37) % 23) - 8 for i in range(25)],
        "len35": [((i * 13) % 17) * 1.5 for i in range(35)],
        "len45": [((i * 7) % 11) for i in range(45)],
        "len60": [math.sin(i / 4) * 10 for i in range(60)],
        "empty": [],
        "all_none": [None, None],
    }

    REF_CONFIGS = {
        "none": dict(),
        "line0": dict(y_ref_line=0),
        "line_num": dict(y_ref_line=4.25),
        "line_mean": dict(y_ref_line="mean"),
        "line_median": dict(y_ref_line="median"),
        "line_min": dict(y_ref_line="min"),
        "line_max": dict(y_ref_line="max"),
        "line_q1": dict(y_ref_line="q1"),
        "line_q3": dict(y_ref_line="q3"),
        "line_nan": dict(y_ref_line=NAN),
        "line_bad": dict(y_ref_line="bogus"),
        "area_num": dict(y_ref_area=[0.1, 5.3]),
        "area_rev": dict(y_ref_area=[5.3, 0.1]),
        "area_kw": dict(y_ref_area=["min", "median"]),
        "area_q": dict(y_ref_area=["q1", "q3"]),
        "area_mixed": dict(y_ref_area=["max", 0]),
        "area_na": dict(y_ref_area=[None, 3]),
        "area_bad": dict(y_ref_area=["bogus", 3]),
        "both": dict(y_ref_line=0, y_ref_area=[2.3, "max"]),
        "both_kw": dict(y_ref_line="mean", y_ref_area=["q1", "q3"]),
        "both_line_na": dict(y_ref_line=None, y_ref_area=[1, 2]),
    }

    MISSING = ["marker", "gap", "zero", "remove"]
    LINE_TYPES = ["curved", "straight"]
    NA_SETS = {"with_none", "with_nan", "na_edges", "all_none"}

    # A.1: y sets x plot types x reference configs x line types (missing='marker')
    for (yk, y), plot_type, (rk, ref), lt in itertools.product(
        Y_SETS.items(), ["line", "bar"], REF_CONFIGS.items(), LINE_TYPES
    ):
        if plot_type == "bar" and lt == "straight":
            continue
        kw = dict(y_vals=list(y), plot_type=plot_type, data_line_type=lt, **ref)
        run("A1 grid", f"A1|{yk}|{plot_type}|{rk}|{lt}", lambda kw=kw: _generate_nanoplot(**kw))

    # A.2: missing value handling on NA sets
    for (yk, y), plot_type, mv, lt, rk in itertools.product(
        [(k, v) for k, v in Y_SETS.items() if k in NA_SETS],
        ["line", "bar"],
        MISSING,
        LINE_TYPES,
        ["none", "line_num", "area_num", "line_mean"],
    ):
        kw = dict(
            y_vals=list(y),
            plot_type=plot_type,
            missing_vals=mv,
            data_line_type=lt,
            **REF_CONFIGS[rk],
        )
        run(
            "A2 missing",
            f"A2|{yk}|{plot_type}|{mv}|{lt}|{rk}",
            lambda kw=kw: _generate_nanoplot(**kw),
        )

    run("A2 missing", "A2|bad_missing", lambda: _generate_nanoplot([1, 2], missing_vals="bogus"))
    run(
        "A2 missing", "A2|bad_line_type", lambda: _generate_nanoplot([1, 2], data_line_type="bogus")
    )

    # A.3: x values
    X_SETS = {
        "x_basic": ([-5.3, 6.3, -2.3, 0, 2.3], [1.2, 3.4, 4.2, 5.0, 5.8]),
        "x_unsorted": ([1, 4, 2, 8], [10, 2, 7, 4]),
        "x_na": ([1, 4, 2, 8, 3], [1, None, 3, NAN, 5]),
        "x_y_na": ([1, None, 2, 8, 3], [1, 2, 3, 4, 5]),
        "x_invariant": ([2, 3, 4], [1, 1, 1]),
        "x_empty": ([], []),
        "x_all_na": ([1, 2], [None, None]),
        "x_mismatch": ([1, 2, 3], [1, 2]),
        "x_ordinal": ([3, 5, 2], [738000, 738031, 738059]),
    }
    for (xk, (y, x)), plot_type, lt, ek, mv, rk in itertools.product(
        X_SETS.items(),
        ["line", "bar"],
        LINE_TYPES,
        ["none", "expand_x", "expand_both", "expand_x_str"],
        ["marker", "remove", "gap"],
        ["none", "both"],
    ):
        extra = {
            "none": {},
            "expand_x": {"expand_x": [0, 20]},
            "expand_both": {"expand_x": [-5, 15], "expand_y": [-10, 30]},
            "expand_x_str": {"expand_x": ["2020-01-01", "2021-01-01"]},
        }[ek]
        kw = dict(
            y_vals=list(y),
            x_vals=list(x),
            plot_type=plot_type,
            data_line_type=lt,
            missing_vals=mv,
            **extra,
            **REF_CONFIGS[rk],
        )
        run(
            "A3 x values",
            f"A3|{xk}|{plot_type}|{lt}|{ek}|{mv}|{rk}",
            lambda kw=kw: _generate_nanoplot(**kw),
        )

    # A.4: expand_y
    for (yk, y), plot_type, ey, rk in itertools.product(
        [(k, Y_SETS[k]) for k in ["mixed", "pos_int", "invariant", "invariant_zero", "single"]],
        ["line", "bar"],
        [[-20, 30], [0, 5], [100]],
        ["none", "line_mean", "area_num", "both"],
    ):
        kw = dict(y_vals=list(y), plot_type=plot_type, expand_y=ey, **REF_CONFIGS[rk])
        run("A4 expand_y", f"A4|{yk}|{plot_type}|{ey}|{rk}", lambda kw=kw: _generate_nanoplot(**kw))

    # A.5: single values (scalars) on a shared scale
    ALL_SINGLE = {
        "mixed": [-5.3, 6.3, -2.3, 0, 2.3, 6.7, 14.2, 0, 2.3, 13.3],
        "pos": [1, 5, 3, 8, 2],
        "neg": [-1, -5, -3, -8],
        "zeros": [0, 0, 0],
        "with_na": [3, None, 7, NAN, 1],
        "large": [1200, 45000, 3_200_000, 0],
    }
    for (ak, all_vals), plot_type, ref_line, show_ref in itertools.product(
        ALL_SINGLE.items(),
        ["line", "bar"],
        [None, 0, 2.5, 6, "mean", "median", "min", "max", "q1", "q3", NAN],
        [True, False],
    ):
        for y in sorted({v for v in all_vals if v is not None and not math.isnan(v)}) + [3432]:
            kw = dict(
                y_vals=y,
                all_single_y_vals=list(all_vals),
                plot_type=plot_type,
                y_ref_line=ref_line,
                show_reference_line=show_ref,
            )
            run(
                "A5 single values",
                f"A5|{ak}|{plot_type}|{fmt_kwargs({'r': ref_line})}|{show_ref}|{y}",
                lambda kw=kw: _generate_nanoplot(**kw),
            )

    # single values with options that are overridden for single-value plots
    for plot_type, (oi, opts) in itertools.product(
        ["line", "bar"],
        enumerate(
            [
                dict(show_data_points=False, show_data_line=False, show_data_area=True),
                dict(show_vertical_guides=True, show_y_axis_guide=True, show_reference_area=True),
                dict(y_ref_area=[1, 3]),
                dict(currency="EUR", y_ref_line="mean"),
                dict(
                    y_val_fmt_fn=lambda v: f"<{v}>",
                    y_ref_line_fmt_fn=lambda v: f"[{v}]",
                    y_ref_line=1,
                ),
                dict(interactive_data_values=False, y_ref_line="max"),
                dict(
                    data_point_radius=[6],
                    data_point_fill_color=["#00FF00"],
                    data_bar_fill_color=["#0000FF"],
                    data_bar_stroke_color="#111111",
                    data_bar_stroke_width=7,
                    data_line_stroke_color="#222222",
                    data_line_stroke_width=3,
                    reference_line_color="#333333",
                    vertical_guide_stroke_width=9,
                ),
                dict(
                    data_bar_negative_fill_color="#AA0000",
                    data_bar_negative_stroke_color="#BB0000",
                    data_bar_negative_stroke_width=2,
                ),
            ]
        ),
    ):
        for y in [-3, 0, 4]:
            kw = dict(y_vals=y, all_single_y_vals=[-3, 0, 4, 9], plot_type=plot_type, **opts)
            run(
                "A5 single values",
                f"A5opts|{plot_type}|{oi}:{fmt_kwargs(opts)}|{y}",
                lambda kw=kw: _generate_nanoplot(**kw),
            )

    # A.6: styling / visibility options on multi-value plots
    OPTION_SETS = [
        dict(show_data_points=False),
        dict(show_data_line=False),
        dict(show_data_area=False),
        dict(show_reference_line=False),
        dict(show_reference_area=False),
        dict(show_vertical_guides=False),
        dict(show_y_axis_guide=False),
        dict(
            show_data_points=False,
            show_data_line=False,
            show_data_area=False,
            show_reference_line=False,
            show_reference_area=False,
            show_vertical_guides=False,
            show_y_axis_guide=False,
        ),
        dict(interactive_data_values=False),
        dict(interactive_data_values=False, vertical_guide_stroke_color="#00AA00"),
        dict(currency="USD"),
        dict(currency="JPY"),
        dict(y_val_fmt_fn=lambda v: f"v{v}"),
        dict(y_axis_fmt_fn=lambda v: f"a{v}"),
        dict(y_ref_line_fmt_fn=lambda v: f"r{v}"),
        dict(y_val_fmt_fn=lambda v: 5),
        dict(
            data_point_radius=7,
            data_point_stroke_color="#123456",
            data_point_stroke_width=2,
            data_point_fill_color="#654321",
        ),
        dict(data_point_radius=[2, 4, 6, 8, 10]),
        dict(data_point_fill_color=["#F00", "#0F0", "#00F", "#FF0", "#0FF"]),
        dict(data_point_radius=[2, 4]),
        dict(data_line_stroke_color="#ABCDEF", data_line_stroke_width=2),
        dict(data_area_fill_color="#00FF00"),
        dict(data_area_fill_color="blue"),
        dict(
            data_bar_stroke_color=["#1", "#2", "#3", "#4", "#5"],
            data_bar_stroke_width=[1, 2, 3, 4, 5],
            data_bar_fill_color=["#a", "#b", "#c", "#d", "#e"],
        ),
        dict(
            data_bar_negative_stroke_color="#000",
            data_bar_negative_stroke_width=1,
            data_bar_negative_fill_color="#FFF",
        ),
        dict(reference_line_color="#999999", reference_area_fill_color="#888888"),
        dict(vertical_guide_stroke_color="#777777", vertical_guide_stroke_width=3),
        dict(svg_height="3em"),
    ]
    for (yk, y), plot_type, opts, lt in itertools.product(
        [
            ("five", [-2, 5, 0, 3.5, 7]),
            ("five_na", [-2, None, 0, 3.5, 7]),
            ("five_int", [-2, 5, 0, 3, 7]),
        ],
        ["line", "bar"],
        OPTION_SETS,
        LINE_TYPES,
    ):
        if plot_type == "bar" and lt == "straight":
            continue
        kw = dict(
            y_vals=list(y),
            plot_type=plot_type,
            data_line_type=lt,
            y_ref_line="median",
            y_ref_area=[0, 3],
            **opts,
        )
        run(
            "A6 options",
            f"A6|{yk}|{plot_type}|{lt}|{OPTION_SETS.index(opts)}:{fmt_kwargs(opts)}",
            lambda kw=kw: _generate_nanoplot(**kw),
        )

    # A.7: boxplot (internal-only plot type) and other odd inputs
    for y in [[1, 2, 3, 4, 5], [3, 3, 3], [-1, 0, 1]]:
        run(
            "A7 misc",
            f"A7|boxplot|{y}",
            lambda y=y: _generate_nanoplot(y_vals=y, plot_type="boxplot"),
        )
    run("A7 misc", "A7|scalar_boxplot", lambda: _generate_nanoplot(y_vals=4, plot_type="boxplot"))
    run("A7 misc", "A7|int_list_curr", lambda: _generate_nanoplot([1, 20000, 3], currency="GBP"))
    run("A7 misc", "A7|big_curr", lambda: _generate_nanoplot([1, 2e15, 3], currency="USD"))
    run("A7 misc", "A7|neg_big", lambda: _generate_nanoplot([-1e16, 2, 3]))
    run(
        "A7 misc",
        "A7|float_ints",
        lambda: _generate_nanoplot([1.0, 2.0, 3.0], y_ref_line="mean"),
    )
    run("A7 misc", "A7|ref_line_none_kw", lambda: _generate_nanoplot([1, 2, 3], y_ref_line=None))

    EDGE = {
        "scalar_nan": dict(y_vals=NAN, all_single_y_vals=[1, 2, NAN]),
        "scalar_zero_mv": dict(y_vals=2, all_single_y_vals=[1, 2], missing_vals="zero"),
        "scalar_remove_mv": dict(y_vals=2, all_single_y_vals=[1, 2], missing_vals="remove"),
        "scalar_no_all": dict(y_vals=2),
        "scalar_no_all_ref": dict(y_vals=2, y_ref_line="mean"),
        "np_int_scalar": dict(y_vals=np.int64(3), all_single_y_vals=[1, 3]),
        "np_float_scalar": dict(y_vals=np.float64(3.5), all_single_y_vals=[1.0, 3.5]),
        "np_int_list": dict(y_vals=[np.int64(1), np.int64(4), np.int64(2)]),
        "unknown_type": dict(
            y_vals=[1, 5, 2], plot_type="unknown", y_ref_line="mean", y_ref_area=[1, 2]
        ),
        "unknown_type_scalar": dict(y_vals=3, all_single_y_vals=[3], plot_type="unknown"),
        "scalar_x_vals": dict(y_vals=3, x_vals=[1], all_single_y_vals=[3, 4]),
        "scalar_expand_y": dict(y_vals=100, expand_y=[100], all_single_y_vals=[100, 3]),
        "single_list_bar": dict(y_vals=[7], plot_type="bar"),
        "single_list_bar_ref": dict(y_vals=[7], plot_type="bar", y_ref_line=7, y_ref_area=[7, 7]),
        "ref_area_same": dict(y_vals=[1, 2, 3], y_ref_area=[2, 2]),
        "ref_line_out_of_range": dict(y_vals=[1, 2, 3], y_ref_line=50, plot_type="bar"),
        "zero_float_bar": dict(y_vals=[0.0, 1.0, -1.0], plot_type="bar", y_ref_line=0.0),
        "int_float_tie": dict(
            y_vals=[5, 5.0, 2], plot_type="bar", y_ref_line=5.0, y_ref_area=[0, 5]
        ),
        "float_zero_ties": dict(
            y_vals=[0.0, 3, 2], plot_type="bar", y_ref_area=[0, 1], y_ref_line=0
        ),
        "bar_both_pos": dict(y_vals=[3, 5, 4], plot_type="bar", y_ref_line=4, y_ref_area=[3, 5]),
        "x_vals_tuple": dict(y_vals=(1, 2, 3)),
    }
    for k, kw in EDGE.items():
        run("A7 misc", f"A7|edge|{k}", lambda kw=kw: _generate_nanoplot(**kw))
        for mv in ["gap", "zero", "remove"]:
            kw2 = dict(kw, missing_vals=mv)
            run("A7 misc", f"A7|edge|{k}|{mv}", lambda kw2=kw2: _generate_nanoplot(**kw2))

    # ---------------------------------------------------------------------------------------------
    # Part B: GT-level examples through `fmt_nanoplot()`
    # ---------------------------------------------------------------------------------------------

    def gt_html(gt: GT) -> str:
        return gt.as_raw_html()

    STREAMS = {
        "example": [
            "20 23 6 7 37 23 21 4 7 16",
            "2.3 6.8 9.2 2.42 3.5 12.1 5.3 3.6 7.2 3.74",
            "-12 -5 6 3.7 0 8 -7.4",
        ],
        "na": ["1 NA 3 4", "NA 2 NA", "5 6 7 NA"],
        "large": ["12000 45000 230000", "1.2e6 3.4e6 9e5", "0.001 0.02 0.0005"],
        "int_with_comma": ["1,2,3,4", "5, 6, 7", "10 20 30"],
    }

    for (sk, vals), plot_type, autoscale, ref_line, ref_area, mv in itertools.product(
        STREAMS.items(),
        ["line", "bar"],
        [False, True],
        [None, "mean", 5],
        [None, ["q1", "q3"]],
        ["marker", "gap"],
    ):
        if mv == "gap" and sk != "na":
            continue

        def mk(
            vals=vals,
            plot_type=plot_type,
            autoscale=autoscale,
            ref_line=ref_line,
            ref_area=ref_area,
            mv=mv,
        ):
            df = pd.DataFrame({"id": list(range(len(vals))), "v": vals})
            return gt_html(
                GT(df, id="t").fmt_nanoplot(
                    columns="v",
                    plot_type=plot_type,
                    autoscale=autoscale,
                    reference_line=ref_line,
                    reference_area=ref_area,
                    missing_vals=mv,
                )
            )

        run(
            "B1 streams",
            f"B1|{sk}|{plot_type}|{autoscale}|{ref_line}|{ref_area}|{mv}",
            mk,
        )

    # Polars list columns, dicts with x/y, dates
    polars_frames = {
        "list": pl.DataFrame({"v": [[1, 2, 3, 5], [4.5, -1.0, 2.25], [0, 0, 7]]}),
        "list_na": pl.DataFrame({"v": [[1, None, 3, 5], [None, -1, 2], [0, 0, 7]]}),
        "struct_xy": pl.DataFrame(
            {
                "v": [
                    {"x": [1, 2, 4, 8], "y": [5, 3, 6, 2]},
                    {"x": [0.5, 1.5, 3.0, 4.0], "y": [-1, 2, 0, 4]},
                ]
            }
        ),
        "struct_y": pl.DataFrame({"v": [{"y": [5, 3, 6, 2]}, {"y": [1, 9, 2, 8]}]}),
        "struct_dates": pl.DataFrame(
            {
                "v": [
                    {"x": ["2020-01-01", "2020-02-15", "2020-06-30"], "y": [5, 3, 6]},
                    {"x": ["2021-03-01", "2021-03-05", "2021-03-09"], "y": [1, 2, 3]},
                ]
            }
        ),
        "struct_xy_str": pl.DataFrame(
            {"v": [{"x": "1 2 3", "y": "4 5 6"}, {"x": "1 5 9", "y": "6 5 4"}]}
        ),
    }
    for (fk, df), plot_type, autoscale, ref in itertools.product(
        polars_frames.items(),
        ["line", "bar"],
        [False, True],
        [dict(), dict(reference_line="median", reference_area=[0, "max"])],
    ):
        run(
            "B2 polars",
            f"B2|{fk}|{plot_type}|{autoscale}|{fmt_kwargs(ref)}",
            lambda df=df, plot_type=plot_type, autoscale=autoscale, ref=ref: gt_html(
                GT(df, id="t").fmt_nanoplot(
                    columns="v", plot_type=plot_type, autoscale=autoscale, **ref
                )
            ),
        )

    # expand_x / expand_y at the GT level
    for expand in [
        dict(expand_x=[0, 10]),
        dict(expand_y=[-10, 20]),
        dict(expand_x=[0, 10], expand_y=[0, 1]),
    ]:
        run(
            "B2 polars",
            f"B2|expand|{fmt_kwargs(expand)}",
            lambda expand=expand: gt_html(
                GT(polars_frames["struct_xy"], id="t").fmt_nanoplot(columns="v", **expand)
            ),
        )

    # Scalar numeric columns (single-value plots)
    scalar_frames = {
        "pd_float": pd.DataFrame({"v": [-5.3, 6.3, -2.3, 0, 2.3, 6.7]}),
        "pd_int": pd.DataFrame({"v": [10, 200, 3000, 0, -50]}),
        "pd_na": pd.DataFrame({"v": [1.5, None, 3.0, -2.0]}),
        "pl_int": pl.DataFrame({"v": [1, 2, 3, 4]}),
        "pl_na": pl.DataFrame({"v": [1, None, -3, 4]}),
        "pl_zeros": pl.DataFrame({"v": [0, 0, 0]}),
        "pl_uint8": pl.DataFrame({"v": [1, 5, 3]}, schema={"v": pl.UInt8}),
        "pl_int32": pl.DataFrame({"v": [-1, 5, 3]}, schema={"v": pl.Int32}),
        "pl_float32": pl.DataFrame({"v": [-1.5, 5.25, 3.0]}, schema={"v": pl.Float32}),
        "pd_uint": pd.DataFrame({"v": pd.Series([1, 5, 3], dtype="uint16")}),
        "pd_nullable_int": pd.DataFrame({"v": pd.Series([1, None, 3], dtype="Int64")}),
        "pd_float32": pd.DataFrame({"v": pd.Series([1.5, -2.0, 3.0], dtype="float32")}),
        "pd_object_nums": pd.DataFrame({"v": pd.Series([1.5, -2.0, 3.0], dtype="object")}),
    }
    for (fk, df), plot_type, ref_line in itertools.product(
        scalar_frames.items(), ["line", "bar"], [None, "mean", "max", 2, "min"]
    ):
        run(
            "B3 scalars",
            f"B3|{fk}|{plot_type}|{ref_line}",
            lambda df=df, plot_type=plot_type, ref_line=ref_line: gt_html(
                GT(df, id="t").fmt_nanoplot(
                    columns="v", plot_type=plot_type, reference_line=ref_line
                )
            ),
        )

    # Row subsets
    for rows in [None, [0, 2], 1]:
        for plot_type in ["line", "bar"]:
            run(
                "B4 rows",
                f"B4|{rows}|{plot_type}",
                lambda rows=rows, plot_type=plot_type: gt_html(
                    GT(scalar_frames["pd_float"], id="t").fmt_nanoplot(
                        columns="v", plot_type=plot_type, rows=rows, reference_line="mean"
                    )
                ),
            )
            run(
                "B4 rows",
                f"B4stream|{rows}|{plot_type}",
                lambda rows=rows, plot_type=plot_type: gt_html(
                    GT(pd.DataFrame({"v": STREAMS["example"]}), id="t").fmt_nanoplot(
                        columns="v", plot_type=plot_type, rows=rows, autoscale=True
                    )
                ),
            )

    # nanoplot_options() variants at the GT level
    GT_OPTIONS = [
        nanoplot_options(),
        nanoplot_options(data_line_type="straight"),
        nanoplot_options(
            data_point_radius=8,
            data_point_stroke_color="black",
            data_point_stroke_width=2,
            data_point_fill_color="white",
            data_line_type="straight",
            data_line_stroke_color="brown",
            data_line_stroke_width=2,
            data_area_fill_color="orange",
            vertical_guide_stroke_color="green",
        ),
        nanoplot_options(
            data_bar_stroke_color="gray",
            data_bar_stroke_width=2,
            data_bar_fill_color="orange",
            data_bar_negative_stroke_color="blue",
            data_bar_negative_stroke_width=1,
            data_bar_negative_fill_color="lightblue",
        ),
        nanoplot_options(show_data_area=False, show_data_points=False),
        nanoplot_options(show_vertical_guides=False, show_y_axis_guide=False),
        nanoplot_options(interactive_data_values=False),
        nanoplot_options(currency="EUR"),
        nanoplot_options(y_val_fmt_fn=lambda v: f"{v:.1f}%", y_axis_fmt_fn=lambda v: f"{v:.0f}"),
        nanoplot_options(reference_line_color="red", reference_area_fill_color="pink"),
    ]
    for i, opts in enumerate(GT_OPTIONS):
        for plot_type in ["line", "bar"]:
            run(
                "B5 options",
                f"B5|{i}|{plot_type}|stream",
                lambda opts=opts, plot_type=plot_type: gt_html(
                    GT(pd.DataFrame({"v": STREAMS["example"]}), id="t").fmt_nanoplot(
                        columns="v",
                        plot_type=plot_type,
                        reference_line="mean",
                        reference_area=["min", "median"],
                        options=opts,
                    )
                ),
            )
            run(
                "B5 options",
                f"B5|{i}|{plot_type}|scalar",
                lambda opts=opts, plot_type=plot_type: gt_html(
                    GT(scalar_frames["pd_float"], id="t").fmt_nanoplot(
                        columns="v", plot_type=plot_type, reference_line="mean", options=opts
                    )
                ),
            )

    # plot height, multiple nanoplot columns, and guards
    run(
        "B6 misc",
        "B6|two_cols_height",
        lambda: gt_html(
            GT(pd.DataFrame({"a": STREAMS["example"], "b": STREAMS["example"]}), id="t")
            .fmt_nanoplot(columns="a", plot_height="3em")
            .fmt_nanoplot(columns="b", plot_type="bar", plot_height="1em")
        ),
    )
    run(
        "B6 misc",
        "B6|bad_columns",
        lambda: gt_html(GT(pd.DataFrame({"v": ["1 2"]})).fmt_nanoplot(columns=["v"])),
    )
    run(
        "B6 misc",
        "B6|bad_plot_type",
        lambda: gt_html(
            GT(pd.DataFrame({"v": ["1 2"]})).fmt_nanoplot(columns="v", plot_type="boxplot")
        ),
    )
    run(
        "B6 misc",
        "B6|str_y",
        lambda: gt_html(GT(pl.DataFrame({"v": [["a", "b"]]})).fmt_nanoplot(columns="v")),
    )
    run(
        "B6 misc",
        "B6|latex",
        lambda: GT(pd.DataFrame({"v": ["1 2 3"]})).fmt_nanoplot(columns="v").as_latex(),
    )


# ---------------------------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------------------------


def _summarize(out: str) -> str:
    """A short description of an output: the error raised, or whether it's an SVG or empty."""

    if "ERROR " in out:
        return out.strip().split("\n")[-1][:90]

    return "SVG" if out else "(empty string)"


def _show_diff(case_id: str, a: str, b: str) -> None:
    print(f"\n=== {case_id}")

    if "<svg" not in a or "<svg" not in b:
        print(f"  - {a[-300:]!r}\n  + {b[-300:]!r}")
        return

    matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in matcher.get_opcodes()[:6]:
        if op != "equal":
            print(
                f"  {op}:\n  - {a[max(0, i1 - 60) : i2 + 20]!r}\n  + {b[max(0, j1 - 60) : j2 + 20]!r}"
            )


def compare(base: dict, new: dict, max_shown: int) -> list[str]:
    """Print a summary of the differences between `base` and `new`; return the changed case ids."""

    missing = sorted(set(base) - set(new))
    extra = sorted(set(new) - set(base))
    changed = [k for k in base if k in new and base[k][1] != new[k][1]]

    print(f"{len(base)} cases: {len(base) - len(changed) - len(missing)} identical, ", end="")
    print(f"{len(changed)} changed, {len(missing)} missing, {len(extra)} new")

    if not changed:
        return changed

    print("\nChanged cases by section:")
    for section, n in Counter(base[k][0] for k in changed).most_common():
        print(f"  {n:5d}  {section}")

    print("\nChanged cases by kind of change (base => new):")
    kinds = Counter((_summarize(base[k][1]), _summarize(new[k][1])) for k in changed)
    for (a, b), n in kinds.most_common():
        print(f"  {n:5d}  {a}\n         => {b}")

    for k in changed[:max_shown]:
        _show_diff(k, base[k][1], new[k][1])

    return changed


def write_page(base: dict, new: dict, changed: list[str], every: int, path: Path) -> None:
    """Write an HTML page showing the changed cases, and a sample of the identical ones, side by
    side."""

    identical_svgs = [k for k in base if k in new and k not in changed and "<svg" in base[k][1]]

    def cell(out: str) -> str:
        return out if "<svg" in out else f"<pre>{html.escape(out[-400:]) or '(empty string)'}</pre>"

    rows = []
    for title, keys in [
        (f"Changed cases ({len(changed)})", changed),
        (
            f"Sample of identical cases (every {every}th of {len(identical_svgs)})",
            identical_svgs[::every],
        ),
    ]:
        rows.append(f"<tr><th colspan=3><h2>{html.escape(title)}</h2></th></tr>")
        rows += [
            f"<tr><td class=id>{html.escape(k)}</td><td>{cell(base[k][1])}</td>"
            f"<td>{cell(new[k][1])}</td></tr>"
            for k in keys
        ]

    path.write_text(
        "<!doctype html><html><head><meta charset='utf-8'><title>Nanoplot comparison</title>"
        "<style>body{font-family:sans-serif;font-size:13px} table{border-collapse:collapse} "
        "td,th{border:1px solid #ddd;padding:4px;vertical-align:middle} td{width:330px} "
        "td.id{width:260px;font-size:10px;word-break:break-all;color:#444} "
        "pre{white-space:pre-wrap;font-size:10px;color:#a00;margin:0} td table{font-size:10px}"
        "</style></head><body><h1>Nanoplot comparison: base vs. working tree</h1>"
        f"<p>{len(base)} cases; {len(changed)} changed.</p>"
        f"<table><tr><th>case</th><th>base</th><th>working tree</th></tr>{''.join(rows)}</table>"
        "</body></html>"
    )


# ---------------------------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------------------------


def _render_version(package_dir: Path, out_file: Path) -> dict:
    env = {**os.environ, "PYTHONPATH": str(package_dir)}

    subprocess.run(
        [sys.executable, __file__, "--render", str(out_file)],
        env=env,
        cwd=out_file.parent,
        check=True,
    )

    return json.loads(out_file.read_text())


def _extract_ref(ref: str, dest: Path) -> None:
    archive = subprocess.run(
        ["git", "archive", ref, "great_tables"], cwd=REPO_ROOT, check=True, capture_output=True
    )
    subprocess.run(["tar", "-x", "-C", str(dest)], input=archive.stdout, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0].strip())
    parser.add_argument("--base", default="main", help="git ref to compare against (default: main)")
    parser.add_argument("--out", type=Path, help="output directory (default: a temporary one)")
    parser.add_argument("--html", action="store_true", help="also write a side-by-side HTML page")
    parser.add_argument(
        "--every", type=int, default=15, help="sample rate of identical cases in the page"
    )
    parser.add_argument(
        "--show", type=int, default=8, help="number of changed cases to show diffs for"
    )
    parser.add_argument("--render", type=Path, help=argparse.SUPPRESS)  # used by the subprocesses
    args = parser.parse_args()

    if args.render:
        render(args.render)
        return 0

    out_dir = args.out or Path(tempfile.mkdtemp(prefix="compare_nanoplots_"))
    out_dir.mkdir(parents=True, exist_ok=True)

    base_pkg = out_dir / "base_pkg"
    base_pkg.mkdir(exist_ok=True)
    _extract_ref(args.base, base_pkg)

    print(f"Rendering with great_tables from `{args.base}`...", flush=True)
    base = _render_version(base_pkg, out_dir / "base.json")

    print("Rendering with great_tables from the working tree...", flush=True)
    new = _render_version(REPO_ROOT, out_dir / "new.json")

    print()
    changed = compare(base, new, max_shown=args.show)

    if args.html:
        page = out_dir / "comparison.html"
        write_page(base, new, changed, args.every, page)
        print(f"\nSide-by-side page: {page}")

    print(f"Outputs are in {out_dir}")

    return 1 if changed or set(base) != set(new) else 0


if __name__ == "__main__":
    sys.exit(main())
