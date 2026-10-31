from __future__ import annotations

import datetime as dt
import json
import math
import re

import pandas as pd
import polars as pl
import pytest

from great_tables import GT, exibble, loc, style
from great_tables._gti import SPEC_VERSION, build_spec, render_gti_html, spec_to_script_json
from great_tables._gti._render import _load_runtime
from great_tables._tbl_data import _get_column_kind, _get_column_ranks
from tests.utils import cast_to_categorical


def spec_of(gt: GT) -> dict:
    return build_spec(gt._build_data(context="html"))


def split_gti_html(html: str) -> tuple[dict, list[str]]:
    """The spec embedded in `render_gti_html()` output, and the `<tr>`s of its table body."""
    spec_text = re.search(r"<script type=\"application/json\" data-gti-spec>(.*?)</script>", html)
    assert spec_text is not None
    tbody = re.search(r'<tbody class="gt_table_body">(.*?)</tbody>', html, re.DOTALL)
    assert tbody is not None
    trs = re.findall(r"<tr[ >].*?</tr>", tbody.group(1), re.DOTALL)
    return json.loads(spec_text.group(1)), trs


# body ----

# Every data row has a unique `id` value ("r0", "r1", ...) shown somewhere in its <tr>
DF = pd.DataFrame(
    {
        "id": [f"r{i}" for i in range(6)],
        "grp": ["b", "a", "b", "c", "a", "b"],
        "x": [1.5, 2.0, None, 4.0, 5.0, 6.0],
        "y": [10, 20, 30, 40, 50, 60],
    }
)

SUM = {"Total": lambda df: df[["x", "y"]].sum()}
MAX = {"Max": lambda df: df[["x", "y"]].max()}


def assert_body_matches_html(gt: GT, row_label: str = "r", first: int = 0) -> list:
    """Check the spec's body row map against the rendered table body, <tr> by <tr>.

    Data row `i` must show the text `{row_label}{first + i}` in one of its cells.
    """
    spec, trs = split_gti_html(render_gti_html(gt, runtime="none"))
    body = spec["body"]
    assert len(body) == len(trs)

    for entry, tr in zip(body, trs):
        ids = [int(n) - first for n in re.findall(rf">{row_label}(\d+)<", tr)]
        if isinstance(entry, int):
            assert ids == [entry], tr
        elif "grand_summary" in entry:
            assert "gt_grand_summary_row" in tr and f">{entry['grand_summary']}<" in tr
            assert ids == []
        elif "summary" in entry:
            assert "gt_summary_row" in tr and f">{entry['summary']}<" in tr
            assert entry["side"] in ("top", "bottom")
            assert ids == []
        else:
            assert "gt_group_heading_row" in tr or "gt_empty_group_heading" in tr
            assert ids == []

    # Each data row is shown exactly once
    assert sorted(e for e in body if isinstance(e, int)) == list(range(spec["nrows"]))
    return body


@pytest.mark.parametrize(
    "gt",
    [
        pytest.param(GT(DF), id="plain"),
        pytest.param(GT(DF, rowname_col="id"), id="stub"),
        pytest.param(GT(DF, groupname_col="grp"), id="groups"),
        pytest.param(GT(DF, rowname_col="id", groupname_col="grp"), id="stub-groups"),
        pytest.param(
            GT(DF, rowname_col="id", groupname_col="grp").tab_options(row_group_as_column=True),
            id="groups-as-column",
        ),
        pytest.param(
            GT(DF, rowname_col="id", groupname_col="grp").summary_rows(fns=SUM, side="bottom"),
            id="summary-bottom",
        ),
        pytest.param(
            GT(DF, rowname_col="id", groupname_col="grp").summary_rows(fns=SUM, side="top"),
            id="summary-top",
        ),
        pytest.param(
            GT(DF, rowname_col="id", groupname_col="grp").summary_rows(fns=SUM, groups=["b"]),
            id="summary-one-group",
        ),
        pytest.param(
            GT(DF, rowname_col="id", groupname_col="grp")
            .tab_options(row_group_as_column=True)
            .summary_rows(fns=SUM),
            id="groups-as-column-summary",
        ),
        pytest.param(
            GT(DF, rowname_col="id").grand_summary_rows(fns={**SUM, **MAX}, side="top"),
            id="grand-top",
        ),
        pytest.param(
            GT(DF, rowname_col="id").grand_summary_rows(fns=MAX, side="bottom"),
            id="grand-bottom",
        ),
        pytest.param(
            GT(DF, rowname_col="id", groupname_col="grp")
            .summary_rows(fns=SUM, side="top")
            .summary_rows(fns=MAX, side="bottom")
            .grand_summary_rows(fns=SUM, side="top")
            .grand_summary_rows(fns=MAX, side="bottom"),
            id="all-summaries",
        ),
        pytest.param(GT(DF, groupname_col="grp").cols_hide("x"), id="hidden-column"),
        pytest.param(GT(DF, rowname_col=["grp", "id"]), id="multi-column-stub"),
        pytest.param(
            GT(DF, rowname_col="id", groupname_col="grp").row_group_order(["c", "a", "b"]),
            id="row-group-order",
        ),
        pytest.param(
            GT(
                DF.assign(grp=["b", None, "b", None, "a", "b"]),
                rowname_col="id",
                groupname_col="grp",
            ).grand_summary_rows(fns=SUM),
            id="null-group",
        ),
    ],
)
def test_body_matches_html(gt: GT):
    assert_body_matches_html(gt)


def test_body_order_and_groups():
    gt = (
        GT(DF, rowname_col="id", groupname_col="grp")
        .row_group_order(["c", "a", "b"])
        .summary_rows(fns=SUM, side="top")
        .grand_summary_rows(fns=MAX)
    )
    body = assert_body_matches_html(gt)
    total = {"summary": "Total", "side": "top"}

    assert body == [
        {"group": "c"},
        {**total, "group": "c"},
        3,
        {"group": "a"},
        {**total, "group": "a"},
        1,
        4,
        {"group": "b"},
        {**total, "group": "b"},
        0,
        2,
        5,
        {"grand_summary": "Max", "side": "bottom"},
    ]
    assert spec_of(gt)["groups"] == [
        {"id": "c", "rows": [3]},
        {"id": "a", "rows": [1, 4]},
        {"id": "b", "rows": [0, 2, 5]},
    ]


def test_body_groups_as_column_has_no_headings():
    gt = GT(DF, rowname_col="id", groupname_col="grp").tab_options(row_group_as_column=True)
    spec = spec_of(gt)

    assert spec["stub"]["groups_as_column"] is True
    assert all(isinstance(entry, int) for entry in spec["body"])


def test_body_null_group():
    gt = GT(
        DF.assign(grp=["b", None, "b", None, "a", "b"]), rowname_col="id", groupname_col="grp"
    ).grand_summary_rows(fns=SUM)
    body = assert_body_matches_html(gt)
    structural = [entry for entry in body if not isinstance(entry, int)]

    # A grand summary row isn't mistaken for a summary of the null group
    assert {"group": None} in structural
    assert {"grand_summary": "Total", "side": "bottom"} in structural
    assert {"id": None, "rows": [1, 3]} in spec_of(gt)["groups"]


def test_body_row_indices_are_python_ints():
    # pandas gives numpy integers, which `json` can't serialize
    spec = spec_of(GT(DF, groupname_col="grp"))

    assert all(type(entry) is int for entry in spec["body"] if not isinstance(entry, dict))
    assert all(type(i) is int for group in spec["groups"] for i in group["rows"])


# columns, spanners, stub ----


def test_spec_columns_spanners_and_stub():
    gt = (
        GT(DF, rowname_col="id", groupname_col="grp", id="t")
        .tab_stubhead(label="ID")
        .tab_spanner(label="Values", columns=["x", "y"])
        .cols_align(align="center", columns="y")
    )
    spec = spec_of(gt)

    assert spec["version"] == SPEC_VERSION
    assert spec["nrows"] == 6
    assert [(c["id"], c["role"], c["kind"], c["align"]) for c in spec["columns"]] == [
        ("id", "stub", "string", "left"),
        ("x", "data", "number", "right"),
        ("y", "data", "number", "center"),
    ]
    assert [c["header"] for c in spec["columns"]] == ["t-ID", "t-x", "t-y"]
    assert spec["spanners"] == [
        {"id": "Values", "level": 0, "columns": ["x", "y"], "header": "t-Values"}
    ]
    assert spec["stub"] == {"columns": ["id"], "groups_as_column": False}


def test_spec_headers_are_ids_in_the_table():
    gt = (
        GT(DF, rowname_col="id")
        .tab_stubhead(label="ID")
        .tab_spanner(label="Values", columns=["x", "y"])
    )
    html = render_gti_html(gt, runtime="none")
    spec, _ = split_gti_html(html)
    headers = [c["header"] for c in spec["columns"]] + [s["header"] for s in spec["spanners"]]

    for header in headers:
        assert header is not None and f'id="{header}"' in html


def test_spec_hidden_columns_are_left_out():
    spec = spec_of(GT(DF).cols_hide(["grp", "y"]))

    assert [c["id"] for c in spec["columns"]] == ["id", "x"]
    assert set(spec["ranks"]) == {"id", "x"}


def test_spec_stub_for_summary_labels_only():
    # Summary rows need a stub column for their labels, even without a `rowname_col`
    spec = spec_of(GT(DF).grand_summary_rows(fns=SUM))
    first = spec["columns"][0]

    assert first == {"id": None, "role": "stub", "kind": "other", "align": "left", "header": None}
    assert spec["stub"]["columns"] == []
    assert None not in spec["ranks"]


def test_spec_multi_column_stub():
    spec = spec_of(GT(DF, rowname_col=["grp", "id"]))

    assert spec["stub"]["columns"] == ["grp", "id"]
    assert [(c["id"], c["role"]) for c in spec["columns"]][:2] == [("grp", "stub"), ("id", "stub")]


def test_spec_ranks_skip_unsortable_columns():
    df = pd.DataFrame({"ok": [2, 1], "mixed": [1, "a"], "obj": [{"a": 1}, {"b": 2}]})
    spec = spec_of(GT(df))

    assert spec["ranks"] == {"ok": [1, 0]}


def test_spec_with_exibble():
    gt = GT(exibble, rowname_col="row", groupname_col="group").tab_style(
        style.fill("red"), loc.body(columns="num")
    )
    spec = spec_of(gt)

    assert spec["nrows"] == len(exibble)
    assert {c["id"]: c["kind"] for c in spec["columns"]} == {
        "row": "string",
        "num": "number",
        "char": "string",
        "fctr": "string",
        "date": "string",
        "time": "string",
        "datetime": "string",
        "currency": "number",
    }
    assert_body_matches_html(gt, row_label="row_", first=1)


def test_spec_stub_without_stubhead_has_no_header():
    spec = spec_of(GT(DF, rowname_col="id"))

    assert spec["columns"][0]["id"] == "id"
    assert spec["columns"][0]["header"] is None


# ranks ----

NAN = float("nan")


def ranks_of(frame_constructor, values, **cast) -> list[int | None] | None:
    df = frame_constructor({"x": values})
    if cast:
        df = cast_to_categorical(df, "x", **cast)
    return _get_column_ranks(df, "x")


def is_pandas(frame_constructor) -> bool:
    return frame_constructor.__name__.startswith("pandas_")


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([3, 1, 3, 2, -5], [3, 1, 3, 2, 0], id="ints"),
        pytest.param([2.5, None, -1.0, 2.5, 0.0], [2, None, 0, 2, 1], id="floats-null"),
        pytest.param(["b", None, "a", "b", "C"], [2, None, 1, 2, 0], id="strings"),
        pytest.param([True, False, True], [1, 0, 1], id="booleans"),
        pytest.param(
            [dt.date(2024, 1, 2), dt.date(2023, 5, 1), None, dt.date(2024, 1, 2)],
            [1, 0, None, 1],
            id="dates",
        ),
        pytest.param(
            [dt.datetime(2024, 1, 1, 12), dt.datetime(2024, 1, 1, 9), dt.datetime(2025, 1, 1)],
            [1, 0, 2],
            id="datetimes",
        ),
        pytest.param([None, 2.0, None], [None, 0, None], id="mostly-null"),
    ],
)
def test_ranks(frame_constructor, values, expected):
    assert ranks_of(frame_constructor, values) == expected


def test_ranks_empty():
    assert _get_column_ranks(pd.DataFrame({"x": pd.Series([], dtype="int64")}), "x") == []
    assert _get_column_ranks(pl.DataFrame({"x": pl.Series([], dtype=pl.Int64)}), "x") == []


def test_ranks_nan(frame_constructor):
    ranks = ranks_of(frame_constructor, [1.0, NAN, 0.0, NAN, None])

    if is_pandas(frame_constructor):
        # pandas counts NaN as missing
        assert ranks == [1, None, 0, None, None]
    else:
        # Polars and PyArrow sort NaN after all numbers
        assert ranks == [1, 2, 0, 2, None]


def test_ranks_ordered_categorical(frame_constructor):
    # Levels are in order of first appearance: lo, hi, mid
    ranks = ranks_of(frame_constructor, ["lo", "hi", None, "mid", "hi"], ordered=True)

    assert ranks == [0, 1, None, 2, 1]


def test_ranks_unordered_categorical(frame_constructor):
    ranks = ranks_of(frame_constructor, ["lo", "hi", None, "mid", "hi"], ordered=False)

    if is_pandas(frame_constructor):
        # pandas sorts by category order, even when the categories are unordered
        assert ranks == [0, 1, None, 2, 1]
    else:
        assert ranks == [1, 0, None, 2, 0]


def test_ranks_follow_the_backend_sort(frame_constructor):
    values = [5.0, None, -2.0, 5.0, 3.25, None, -2.0, 0.0]
    ranks = ranks_of(frame_constructor, values)
    assert ranks is not None

    # Sorting rows by (rank, row) gives the data sorted, missing values last
    order = sorted(range(len(values)), key=lambda i: (ranks[i] is None, ranks[i] or 0, i))
    assert [values[i] for i in order] == [-2.0, -2.0, 0.0, 3.25, 5.0, 5.0, None, None]
    # Dense: 0, 1, ... with no gaps
    assert sorted({r for r in ranks if r is not None}) == list(range(4))


def test_ranks_ignore_the_pandas_index():
    df = pd.DataFrame({"x": [3, 1, 2]}, index=[10, 5, 7])

    assert _get_column_ranks(df, "x") == [2, 0, 1]


def test_ranks_unsortable():
    assert _get_column_ranks(pd.DataFrame({"x": [1, "a", 2.0]}), "x") is None
    assert _get_column_ranks(pl.DataFrame({"x": [object(), object()]}), "x") is None


def test_column_kinds(frame_constructor):
    df = frame_constructor(
        {
            "num": [1.5, None],
            "int": [1, 2],
            "str": ["a", None],
            "bool": [True, False],
            "date": [dt.date(2024, 1, 1), None],
            "datetime": [dt.datetime(2024, 1, 1), None],
            "time": [dt.time(12, 30), None],
            "duration": [dt.timedelta(days=1), None],
        }
    )
    expected = {
        "num": "number",
        "int": "number",
        "str": "string",
        "bool": "boolean",
        "date": "date",
        "datetime": "datetime",
        "time": "time",
        "duration": "duration",
    }
    assert {column: _get_column_kind(df, column) for column in expected} == expected


def test_column_kind_categorical(frame_constructor):
    df = cast_to_categorical(frame_constructor({"x": ["a", "b"]}), "x", ordered=False)

    assert _get_column_kind(df, "x") == "category"


# rendering ----


def test_spec_json_escapes_markup():
    spec = spec_of(GT(pd.DataFrame({"</script><!--&": [1]})))
    text = spec_to_script_json(spec)

    assert "<" not in text and ">" not in text and "&" not in text
    assert json.loads(text) == spec


def test_spec_json_has_no_nan():
    df = pd.DataFrame({"x": [NAN, 1.0]})
    text = spec_to_script_json(spec_of(GT(pl.from_pandas(df, nan_to_null=False))))

    assert "NaN" not in text
    assert not any(isinstance(v, float) and math.isnan(v) for v in json.loads(text)["ranks"]["x"])


def test_render_wraps_gt_html():
    gt = GT(exibble, id="t").tab_header(title="A title")
    html = render_gti_html(gt, runtime="none")

    assert html.startswith("<gt-table>\n")
    assert html.endswith("</gt-table>\n")
    assert gt.as_raw_html() in html
    assert html.count("data-gti-spec") == 1


def test_render_runtime_inline():
    js, css = _load_runtime()
    gt = GT(exibble, id="t")
    inline = render_gti_html(gt)
    none = render_gti_html(gt, runtime="none")

    assert inline.startswith(none)
    assert js in inline and css in inline
    assert js not in none and css not in none


def test_render_runtime_invalid():
    with pytest.raises(ValueError, match="runtime="):
        render_gti_html(GT(exibble), runtime="cdn")  # type: ignore[arg-type]
