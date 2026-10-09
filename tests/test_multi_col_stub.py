from html.parser import HTMLParser
import itertools
import re

import pandas as pd
import polars as pl
import pytest

from great_tables import GT, loc, md, stub, style
from great_tables._locations import resolve_cols_i
from great_tables._utils_render_latex import create_body_component_l, create_columns_component_l
from tests.utils import assert_rendered_body, assert_rendered_columns


DATA = {
    "a": ["A", "A", "A", "B", "B", "C"],
    "b": ["x", "x", "y", "y", "y", "z"],
    "c": ["p", "q", "r", "s", "t", "u"],
    "g": ["G1", "G1", "G1", "G2", "G2", "G2"],
    "n1": [1, 2, 3, 4, 5, 6],
    "n2": [10, 20, 30, 40, 50, 60],
}


class _TableGrid(HTMLParser):
    """Collect the cells (with their rowspan and colspan) of each row in a rendered table."""

    def __init__(self):
        super().__init__()
        self.sections: dict[str, list[list[tuple[int, int]]]] = {}
        self._section = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("thead", "tbody"):
            self._section = self.sections.setdefault(tag, [])
        elif tag == "tr" and self._section is not None:
            self._section.append([])
        elif tag in ("th", "td") and self._section is not None:
            self._section[-1].append(
                (int(attrs.get("rowspan") or 1), int(attrs.get("colspan") or 1))
            )


def assert_consistent_grid(gt: GT, n_cols: int):
    """Assert that every row of the header and body covers exactly `n_cols` columns.

    Cells spanning several rows (rowspan) or columns (colspan) are accounted for, so a mismatch
    between the header and body, or a cell missing from (or added to) a row, is caught.
    """

    parser = _TableGrid()
    parser.feed(gt.as_raw_html())

    for section, rows in parser.sections.items():
        occupied: set[tuple[int, int]] = set()
        for r, cells in enumerate(rows):
            c = 0
            for rowspan, colspan in cells:
                while (r, c) in occupied:
                    c += 1
                for dr, dc in itertools.product(range(rowspan), range(colspan)):
                    occupied.add((r + dr, c + dc))
                c += colspan
            covered = sum(1 for (row, _) in occupied if row == r)
            assert covered == n_cols, f"{section} row {r} covers {covered} of {n_cols} columns"


@pytest.mark.parametrize("frame", [pd.DataFrame, pl.DataFrame])
@pytest.mark.parametrize("stub", [["a", "b"], ["a", "b", "c"]])
@pytest.mark.parametrize("groups", [None, "banner", "column"])
@pytest.mark.parametrize("stubhead", [None, "single", "list"])
@pytest.mark.parametrize("spanners", [0, 2])
@pytest.mark.parametrize("summary", [False, True])
def test_multi_col_stub_grid_is_consistent(frame, stub, groups, stubhead, spanners, summary):
    data = frame(DATA)
    gt = GT(data, rowname_col=stub, groupname_col="g" if groups else None)

    if groups == "column":
        gt = gt.tab_options(row_group_as_column=True)
    if stubhead == "single":
        gt = gt.tab_stubhead("Stub")
    elif stubhead == "list":
        gt = gt.tab_stubhead([f"L{i}" for i in range(len(stub))])
    if spanners:
        gt = gt.tab_spanner("Inner", columns=["n1", "n2"]).tab_spanner("Outer", spanners="Inner")
    if summary:
        fn = (
            pl.col("n1", "n2").sum()
            if isinstance(data, pl.DataFrame)
            else (lambda df: df[["n1", "n2"]].sum())
        )
        gt = gt.grand_summary_rows(fns={"Total": fn})
        if groups:
            gt = gt.summary_rows(fns={"Sum": fn})

    data_cols = [col for col in DATA if col not in stub and not (groups and col == "g")]
    n_cols = len(stub) + len(data_cols) + (groups == "column")

    assert_consistent_grid(gt, n_cols=n_cols)


@pytest.mark.parametrize(
    "transform",
    [
        lambda gt: gt.text_transform(locations=loc.column_labels(), fn=str.upper),
        lambda gt: gt.cols_hide("a"),
        lambda gt: gt.cols_hide("b"),
        lambda gt: gt.cols_hide("a").cols_unhide("a"),
        lambda gt: gt.cols_move_to_start("n2"),
        lambda gt: gt.cols_label(a="Outer").cols_width(cases={"a": "50px"}),
    ],
)
def test_multi_col_stub_grid_after_boxhead_changes(transform):
    gt = transform(GT(pl.DataFrame(DATA).drop("c", "g"), rowname_col=["a", "b"]))
    n_stub_cols = len(gt._boxhead._get_stub_columns())

    assert_consistent_grid(gt, n_cols=n_stub_cols + 2)


def test_multi_col_stub_order_kept_after_column_labels_transform():
    gt = GT(pl.DataFrame(DATA).drop("c", "g"), rowname_col=["b", "a"]).text_transform(
        locations=loc.column_labels(), fn=str.upper
    )
    built = gt._build_data("html")

    assert [col.var for col in built._boxhead._get_stub_columns()] == ["b", "a"]


def test_multi_col_stub_unhide_restores_stub_column():
    gt = GT(pl.DataFrame(DATA), rowname_col=["a", "b"]).cols_hide("a").cols_unhide("a")

    assert [col.var for col in gt._boxhead._get_stub_columns()] == ["a", "b"]


def test_multi_col_stub_list_stubhead_with_group_column():
    gt = (
        GT(pl.DataFrame(DATA).drop("c"), rowname_col=["a", "b"], groupname_col="g")
        .tab_options(row_group_as_column=True)
        .tab_stubhead(["Outer", "Inner"])
    )
    thead = gt.as_raw_html().split("<thead")[1].split("</thead>")[0]
    labels = re.findall(r'<th class="gt_col_heading[^>]*>(.*?)</th>', thead, re.S)

    # An empty cell sits above the row group column
    assert [label.strip() for label in labels[:3]] == ["", "Outer", "Inner"]


def test_multi_col_stub_stubhead_labels_can_be_set_before_stub():
    gt = GT(pl.DataFrame(DATA).drop("c", "g")).tab_stubhead(["A", "B"])

    assert_consistent_grid(gt.tab_stub(rowname_col=["a", "b"]), n_cols=4)


def test_multi_col_stub_stale_stubhead_list_raises_on_render():
    gt = (
        GT(pl.DataFrame(DATA), rowname_col=["a", "b"])
        .tab_stubhead(["A", "B"])
        .tab_stub(rowname_col="b")
    )

    with pytest.raises(ValueError, match="given 2 labels but the stub has 1 column"):
        gt.as_raw_html()


@pytest.mark.parametrize(
    "label,match",
    [([], "must not be an empty list"), (["A", 1], "must be a string")],
)
def test_tab_stubhead_invalid_list(label, match):
    with pytest.raises((ValueError, TypeError), match=match):
        GT(pl.DataFrame(DATA), rowname_col=["a", "b"]).tab_stubhead(label)


@pytest.mark.parametrize(
    "rowname_col,match",
    [
        (["zz", "b"], r"not in the table: \['zz'\]"),
        (["b", "b"], r"duplicated column names: \['b'\]"),
        ([], "at least one column name"),
        ([1, "b"], "column name or a list of column names"),
        (1, "column name or a list of column names"),
    ],
)
def test_multi_col_stub_invalid_rowname_col(rowname_col, match):
    with pytest.raises((ValueError, TypeError), match=match):
        GT(pl.DataFrame(DATA), rowname_col=rowname_col)


def test_multi_col_stub_invalid_rowname_col_in_tab_stub():
    with pytest.raises(ValueError, match="not in the table"):
        GT(pl.DataFrame(DATA)).tab_stub(rowname_col=["a", "zz"])


def test_multi_col_stub_tuple_rowname_col():
    gt = GT(pl.DataFrame(DATA), rowname_col=("a", "b"))

    assert [col.var for col in gt._boxhead._get_stub_columns()] == ["a", "b"]


def test_multi_col_stub_all_null_primary_keeps_stub():
    df = pd.DataFrame({"a": ["A", "A", "B"], "c": [None] * 3, "n": [1, 2, 3]})

    assert_consistent_grid(GT(df, rowname_col=["a", "c"]), n_cols=3)


def test_multi_col_stub_summary_label_spans_stub():
    gt = GT(pl.DataFrame(DATA).drop("c", "g"), rowname_col=["a", "b"]).grand_summary_rows(
        fns={"Total": pl.col("n1", "n2").sum()}
    )
    body = gt.as_raw_html().split("<tbody")[1]

    assert body.count(">Total</th>") == 1
    assert re.search(
        r'<th colspan="2" scope="row" class="[^"]*gt_grand_summary_row[^"]*">Total</th>', body
    )


def test_multi_col_stub_merges_displayed_values():
    df = pl.DataFrame({"a": [1.001, 1.002, 1.0, 1.0], "b": ["w", "x", "y", "z"], "v": [1, 2, 3, 4]})

    # 1.001 and 1.002 both display as `1.0` and are merged; row 3's 1.0 is shown as `1.000`, so it
    # starts a new run rather than being hidden under the merged cell above
    gt = (
        GT(df, rowname_col=["a", "b"])
        .fmt_number(columns="a", decimals=1)
        .fmt_number(columns="a", rows=[2, 3], decimals=3)
    )
    body = gt.as_raw_html().split("<tbody")[1]
    stub_cells = re.findall(
        r'<th(?: rowspan="(\d+)")? scope="row(?:group)?" class="gt_row gt_left gt_stub">(.*?)</th>',
        body,
    )

    assert stub_cells == [
        ("2", "1.0"),
        ("", "w"),
        ("", "x"),
        ("2", "1.000"),
        ("", "y"),
        ("", "z"),
    ]


def test_multi_col_stub_primary_column_not_merged():
    df = pl.DataFrame({"a": ["A", "A"], "b": ["x", "x"], "v": [1, 2]})
    body = GT(df, rowname_col=["a", "b"]).as_raw_html().split("<tbody")[1]

    assert body.count(">x</th>") == 2


def test_multi_col_stub_footnote_and_indent_on_primary_column_only():
    gt = (
        GT(pl.DataFrame(DATA).drop("c", "g"), rowname_col=["a", "b"])
        .tab_footnote("note", locations=loc.stub(rows=[0]))
        .tab_stub_indent(rows=[0], indent=2)
    )
    first_row = gt.as_raw_html().split("<tbody")[1].split("</tr>")[0]
    outer_cell, primary_cell = re.findall(r"<th[^>]*>.*?</th>", first_row, re.S)

    assert "gt_footnote_marks" not in outer_cell and "gt_indent_2" not in outer_cell
    assert "gt_footnote_marks" in primary_cell and "gt_indent_2" in primary_cell


def test_multi_col_stub_stubhead_footnote_once_and_unique_ids():
    gt = (
        GT(pl.DataFrame(DATA).drop("c", "g"), rowname_col=["a", "b"], id="T")
        .tab_stubhead(["X", "X"])
        .tab_footnote("note", locations=loc.stubhead())
    )
    thead = gt.as_raw_html().split("<thead")[1].split("</thead>")[0]

    assert thead.count('<span class="gt_footnote_marks') == 1
    assert re.findall(r'id="(T-X[^"]*)"', thead) == ["T-X", "T-X-2"]


def test_multi_col_stub_stub_selector_selects_all_levels():
    built = GT(pl.DataFrame(DATA), rowname_col=["b", "a"])._build_data("html")

    assert resolve_cols_i(built, ["stub()"], excl_stub=False) == [("b", 1), ("a", 0)]
    assert resolve_cols_i(built, [stub], excl_stub=False) == [("b", 1), ("a", 0)]
    assert resolve_cols_i(built, [stub(1), "n1"], excl_stub=False) == [("a", 0), ("n1", 4)]

    # Stub selectors are excluded like the stub column names, unless `excl_stub=False`
    assert resolve_cols_i(built, [stub]) == []


def test_multi_col_stub_body_snap(snapshot):
    gt = GT(pl.DataFrame(DATA), rowname_col=["a", "b", "c"], groupname_col="g").summary_rows(
        fns={"Sum": pl.col("n1", "n2").sum()}
    )

    assert_rendered_body(snapshot, gt)


def test_multi_col_stub_row_group_as_column_body_snap(snapshot):
    gt = (
        GT(pl.DataFrame(DATA).drop("c"), rowname_col=["a", "b"], groupname_col="g")
        .tab_options(row_group_as_column=True)
        .grand_summary_rows(fns={"Total": pl.col("n1", "n2").sum()})
    )

    assert_rendered_body(snapshot, gt)


def test_multi_col_stub_list_stubhead_columns_snap(snapshot):
    gt = (
        GT(pl.DataFrame(DATA).drop("c"), rowname_col=["a", "b"], groupname_col="g")
        .tab_options(row_group_as_column=True)
        .tab_stubhead(["Outer", md("**Inner**")])
        .tab_spanner("Values", columns=["n1", "n2"])
    )

    assert_rendered_columns(snapshot, gt)


def test_multi_col_stub_latex_body_blanks_repeated_outer_values():
    gt = GT(pl.DataFrame(DATA).drop("c", "g"), rowname_col=["a", "b"])
    rows = create_body_component_l(gt._build_data("latex")).splitlines()

    assert rows == [
        "A & x & 1 & 10 \\\\",
        " & x & 2 & 20 \\\\",
        " & y & 3 & 30 \\\\",
        "B & y & 4 & 40 \\\\",
        " & y & 5 & 50 \\\\",
        "C & z & 6 & 60 \\\\",
    ]


def test_multi_col_stub_latex_list_stubhead_and_summary():
    gt = (
        GT(pl.DataFrame(DATA).drop("c"), rowname_col=["a", "b"], groupname_col="g")
        .tab_options(row_group_as_column=True)
        .tab_stubhead(["Outer", "Inner"])
        .grand_summary_rows(fns={"Total": pl.col("n1", "n2").sum()})
    )
    built = gt._build_data("latex")

    assert create_columns_component_l(built).splitlines()[1] == "  & Outer & Inner & n1 & n2 \\\\ "
    assert create_body_component_l(built).splitlines()[-1] == (
        "\\multicolumn{3}{l}{Total} & 21 & 210 \\\\"
    )
    assert "lll|rr}" in gt.as_latex()


def test_multi_col_stub_text_transform_stub_polars():
    gt = GT(pl.DataFrame(DATA).drop("c", "g"), rowname_col=["a", "b"]).text_transform(
        locations=loc.stub(), fn=str.lower
    )
    body = gt.as_raw_html().split("<tbody")[1]

    assert ">a</th>" in body and ">x</th>" in body and ">A</th>" not in body


CARS = {
    "mfr": ["Ford", "Ferrari", "Ferrari", "BMW"],
    "model": ["GT", "458", "FF", "M4"],
    "hp": [647, 562, 652, 425],
}


def _stub_cells(gt: GT) -> list[list[tuple[bool, str]]]:
    """Return each body row's stub cells as (is styled, text with footnote marks as `^n`)."""

    body = gt.as_raw_html().split("<tbody")[1].split("</tbody>")[0]
    rows = []
    for tr in body.split("<tr")[1:]:
        cells = re.findall(r"<th([^>]*)>(.*?)</th>", tr, re.S)
        rows.append(
            [
                ("style=" in attrs, re.sub(r"<span[^>]*>(.*?)</span>", r"^\1", text).strip())
                for attrs, text in cells
            ]
        )
    return rows


@pytest.mark.parametrize(
    "location,styled",
    [
        # Row names are matched against the targeted column's values
        (loc.stub(rows="Ferrari", columns="mfr"), {"Ferrari"}),
        # A row inside a merged run targets the merged cell
        (loc.stub(rows=[2], columns="mfr"), {"Ferrari"}),
        (loc.stub(rows=[2], columns="model"), {"FF"}),
        (loc.stub(rows=pl.col("hp") > 600, columns="model"), {"GT", "FF"}),
        (loc.stub(rows=["Ford", "BMW"], columns=["mfr"]), {"Ford", "BMW"}),
        (loc.stub(rows=[0], columns=["mfr", "model"]), {"Ford", "GT"}),
        # Without `columns=`, every stub column of the row is targeted
        (loc.stub(rows=[0]), {"Ford", "GT"}),
    ],
)
def test_loc_stub_columns_styles(location, styled):
    gt = GT(pl.DataFrame(CARS), rowname_col=["mfr", "model"]).tab_style(
        style=style.fill(color="gray"), locations=location
    )
    cells = [cell for row in _stub_cells(gt) for cell in row]

    assert {text for is_styled, text in cells if is_styled} == styled


def test_loc_stub_columns_footnotes():
    gt = (
        GT(pl.DataFrame(CARS), rowname_col=["mfr", "model"], id="T")
        .tab_footnote("Italian", locations=loc.stub(rows="Ferrari", columns="mfr"))
        .tab_footnote("Fastest", locations=loc.stub(rows="FF", columns="model"))
        .tab_footnote("First", locations=loc.stub(rows=[0]))
    )

    # The merged Ferrari cell is marked once; marks follow the visual order of the cells
    assert [[text for _, text in row] for row in _stub_cells(gt)] == [
        ["Ford", "GT^1"],
        ["Ferrari^2", "458"],
        ["FF^3"],
        ["BMW", "M4"],
    ]


def test_loc_stub_columns_footnote_order_outer_level_first():
    gt = (
        GT(pl.DataFrame(CARS), rowname_col=["mfr", "model"], id="T")
        .tab_footnote("On the model", locations=loc.stub(rows=[0], columns="model"))
        .tab_footnote("On the make", locations=loc.stub(rows=[0], columns="mfr"))
    )

    assert _stub_cells(gt)[0] == [(False, "Ford^1"), (False, "GT^2")]


def test_loc_stub_columns_text_transform():
    gt = GT(pl.DataFrame(CARS), rowname_col=["mfr", "model"]).text_transform(
        locations=loc.stub(columns="mfr"), fn=str.upper
    )

    assert [[text for _, text in row] for row in _stub_cells(gt)][:2] == [
        ["FORD", "GT"],
        ["FERRARI", "458"],
    ]


def test_loc_stub_columns_must_be_stub_columns():
    with pytest.raises(ValueError, match=r"must refer to stub columns \(\['mfr', 'model'\]\)"):
        GT(pl.DataFrame(CARS), rowname_col=["mfr", "model"]).tab_style(
            style=style.fill(color="gray"), locations=loc.stub(columns="hp")
        )


def test_loc_stub_columns_single_column_stub():
    gt = GT(pl.DataFrame(CARS), rowname_col="model").tab_style(
        style=style.fill(color="gray"), locations=loc.stub(rows="FF", columns="model")
    )

    assert [is_styled for row in _stub_cells(gt) for is_styled, _ in row] == [
        False,
        False,
        True,
        False,
    ]


def test_loc_stub_columns_merged_cell_style_applied_once():
    gt = GT(pl.DataFrame(CARS), rowname_col=["mfr", "model"]).tab_style(
        style=style.fill(color="gray"), locations=loc.stub(rows="Ferrari", columns="mfr")
    )

    assert re.findall(r'<th style="([^"]*)"[^>]*>Ferrari', gt.as_raw_html()) == [
        "background-color: gray;"
    ]


def _col_widths(gt: GT) -> list[str | None]:
    built = gt._build_data("html")
    stub_and_data = [*built._boxhead._get_stub_columns(), *built._boxhead._get_default_columns()]
    return [col.column_width for col in stub_and_data]


@pytest.mark.parametrize(
    "cases,widths",
    [
        ({stub(1): "70px", stub(2): "200px"}, ["200px", "70px", None, None]),
        # `stub(n)` overrides `stub`, and a named column overrides both
        ({stub: "100px", stub(1): "250px"}, ["100px", "250px", None, None]),
        ({stub(1): "250px", "model": "90px"}, [None, "90px", None, None]),
        ({stub: "100px", stub(2): "120px", "hp": "50px"}, ["120px", "100px", "50px", None]),
    ],
)
def test_cols_width_stub_level(cases, widths):
    gt = GT(pl.DataFrame(CARS).with_columns(year=2020), rowname_col=["mfr", "model"])

    assert _col_widths(gt.cols_width(cases=cases)) == widths


def test_cols_width_stub_level_single_column_stub():
    gt = GT(pl.DataFrame(CARS), rowname_col="model").cols_width(cases={stub(1): "150px"})

    assert _col_widths(gt) == ["150px", None, None]


@pytest.mark.parametrize("rowname_col,n", [(["mfr", "model"], 3), (None, 1)])
def test_cols_width_stub_level_out_of_range(rowname_col, n):
    gt = GT(pl.DataFrame(CARS), rowname_col=rowname_col)
    n_stub_cols = len(rowname_col or [])

    with pytest.raises(ValueError, match=rf"stub level {n} .* has {n_stub_cols} column"):
        gt.cols_width(cases={stub(n): "100px"})


@pytest.mark.parametrize("n", [0, -1, 1.5, True, "1"])
def test_stub_level_must_be_positive_integer(n):
    with pytest.raises(ValueError, match="positive integer"):
        stub(n)


def test_stub_level_sentinel():
    assert stub() is stub
    assert repr(stub(2)) == "stub(2)"
    assert stub(2) == stub(2) and stub(2) != stub(1) and stub(1) != stub
    assert len({stub, stub(1), stub(1), stub(2)}) == 3

    with pytest.raises(TypeError, match="can't be called"):
        stub(1)(2)
