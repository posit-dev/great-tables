import pandas as pd
import polars as pl
import pytest
from great_tables import GT, style, loc, google_font, from_column
from great_tables._locations import LocBody
from great_tables._styles import CellStyleFill
from great_tables._tab_create_modify import tab_style
from polars import selectors as cs


@pytest.fixture
def gt():
    return GT(pd.DataFrame({"x": [1, 2], "y": [4, 5]}))


@pytest.fixture
def gt2():
    return GT(pl.DataFrame({"x": [1, 2], "y": [4, 5]}))


def test_tab_style(gt: GT):
    style = CellStyleFill(color="blue")
    new_gt = tab_style(gt, style, LocBody(["x"], [0]))

    assert len(gt._styles) == 0
    assert len(new_gt._styles) == 1

    assert len(new_gt._styles[0].styles) == 1
    assert new_gt._styles[0].styles[0] is style


def test_tab_style_multiple_columns(gt: GT):
    style = CellStyleFill(color="blue")
    new_gt = tab_style(gt, style, LocBody(["x", "y"], [0]))

    assert len(new_gt._styles) == 2

    assert len(new_gt._styles[0].styles) == 1
    assert new_gt._styles[0].styles[0] is style


def test_tab_style_google_font(gt: GT):
    new_gt = tab_style(
        gt,
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body(columns="x"),
    )

    rendered_html = new_gt.as_raw_html()

    assert rendered_html.find(
        "@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');"
    )
    assert rendered_html.find("font-family: IBM Plex Mono;")


def test_tab_style_font_local(gt: GT):
    new_gt = tab_style(
        gt,
        style=style.text(font="Courier"),
        locations=loc.body(columns="x"),
    )

    rendered_html = new_gt.as_raw_html()

    assert rendered_html.find('<td style="font-family: Courier;" class="gt_row gt_right">1</td>')


def test_tab_style_font_from_column():
    tbl = pl.DataFrame({"x": [1, 2], "font": ["Helvetica", "Courier"]})

    gt_tbl = GT(tbl).tab_style(
        style=style.text(font=from_column(column="font")), locations=loc.body(columns="x")
    )

    rendered_html = gt_tbl.as_raw_html()

    assert rendered_html.find('<td style="font-family: Helvetica;" class="gt_row gt_right">1</td>')
    assert rendered_html.find('<td style="font-family: Courier;" class="gt_row gt_right">2</td>')


def test_tab_style_loc_body_mask(gt2: GT):
    style = CellStyleFill(color="blue")
    new_gt = tab_style(gt2, style, LocBody(mask=cs.numeric().gt(1.5)))

    assert len(gt2._styles) == 0
    assert len(new_gt._styles) == 3

    xy_0y, xy_1x, xy_1y = new_gt._styles

    assert xy_0y.styles[0] is style
    assert xy_1x.styles[0] is style
    assert xy_1y.styles[0] is style

    assert xy_0y.rownum == 0
    assert xy_0y.colname == "y"

    assert xy_1x.rownum == 1
    assert xy_1x.colname == "x"

    assert xy_1y.rownum == 1
    assert xy_1y.colname == "y"


def test_tab_style_loc_body_raises(gt2: GT):
    style = CellStyleFill(color="blue")
    mask = cs.numeric().gt(1.5)
    err_msg = "Cannot specify the `mask` argument along with `columns` or `rows` in `loc.body()`."

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(columns=["x"], mask=mask))
    assert err_msg in exc_info.value.args[0]

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(rows=[0], mask=mask))

    assert err_msg in exc_info.value.args[0]


def test_tab_style_loc_body_mask_not_polars_expression_raises(gt2: GT):
    style = CellStyleFill(color="blue")
    mask = "fake expression"
    err_msg = "Only Polars expressions can be passed to the `mask` argument."

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(mask=mask))
    assert err_msg in exc_info.value.args[0]


def test_tab_style_loc_body_mask_columns_not_inside_raises(gt2: GT):
    style = CellStyleFill(color="blue")
    mask = pl.len()
    err_msg = (
        "The `mask` expression produces extra columns, with names not in the original DataFrame."
    )

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(mask=mask))
    assert err_msg in exc_info.value.args[0]


def test_tab_style_loc_body_mask_rows_not_equal_raises(gt2: GT):
    style = CellStyleFill(color="blue")
    mask = pl.len().alias("x")
    err_msg = "The DataFrame length after applying `mask` differs from the original."

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(mask=mask))
    assert err_msg in exc_info.value.args[0]


# =============================================================================
# text_transform tests
# =============================================================================


# =============================================================================
# tab_style_body tests
# =============================================================================


def test_tab_style_body_values():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    new_gt = GT(df).tab_style_body(style=style.fill(color="orange"), values=[2, 5])
    assert len(new_gt._styles) == 2
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 1) in styled_cells
    assert ("y", 1) in styled_cells


def test_tab_style_body_pattern():
    df = pd.DataFrame({"name": ["alice", "bob", "anna"], "score": [1, 2, 3]})
    new_gt = GT(df).tab_style_body(style=style.fill(color="green"), pattern="^a")
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("name", 0) in styled_cells  # alice
    assert ("name", 2) in styled_cells  # anna
    assert ("score", 0) not in styled_cells  # "1" doesn't match "^a"


def test_tab_style_body_fn():
    df = pd.DataFrame({"x": [10, 20, 30], "y": [40, 50, 60]})
    new_gt = GT(df).tab_style_body(
        style=style.fill(color="pink"),
        fn=lambda val: val >= 30,
    )
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 2) in styled_cells  # 30
    assert ("y", 0) in styled_cells  # 40
    assert ("y", 1) in styled_cells  # 50
    assert ("y", 2) in styled_cells  # 60
    assert ("x", 0) not in styled_cells  # 10


def test_tab_style_body_fn_precedence_over_values():
    df = pd.DataFrame({"x": [1, 2, 3]})
    new_gt = GT(df).tab_style_body(
        style=style.fill(color="red"),
        values=[1],
        fn=lambda val: val == 3,
    )
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 2) in styled_cells  # fn matched 3
    assert ("x", 0) not in styled_cells  # values=[1] ignored


def test_tab_style_body_pattern_precedence_over_values():
    df = pd.DataFrame({"x": ["apple", "banana", "avocado"]})
    new_gt = GT(df).tab_style_body(
        style=style.fill(color="red"),
        values=["banana"],
        pattern="^a",
    )
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 0) in styled_cells  # apple matches ^a
    assert ("x", 2) in styled_cells  # avocado matches ^a
    assert ("x", 1) not in styled_cells  # banana doesn't match ^a


def test_tab_style_body_columns_filter():
    df = pd.DataFrame({"x": [1, 2], "y": [1, 2]})
    new_gt = GT(df).tab_style_body(style=style.fill(color="blue"), values=[1], columns="x")
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 0) in styled_cells
    assert ("y", 0) not in styled_cells  # y column excluded


def test_tab_style_body_rows_filter():
    df = pd.DataFrame({"x": [1, 1, 1]})
    new_gt = GT(df).tab_style_body(style=style.fill(color="blue"), values=[1], rows=[0, 2])
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 0) in styled_cells
    assert ("x", 2) in styled_cells
    assert ("x", 1) not in styled_cells  # row 1 excluded


def test_tab_style_body_targets_row():
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    new_gt = GT(df).tab_style_body(style=style.fill(color="blue"), values=[1], targets="row")
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 0) in styled_cells
    assert ("y", 0) in styled_cells  # entire row 0 styled
    assert ("x", 1) not in styled_cells
    assert ("y", 1) not in styled_cells


def test_tab_style_body_targets_column():
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    new_gt = GT(df).tab_style_body(style=style.fill(color="blue"), values=[1], targets="column")
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 0) in styled_cells
    assert ("x", 1) in styled_cells  # entire column x styled
    assert ("y", 0) not in styled_cells
    assert ("y", 1) not in styled_cells


def test_tab_style_body_targets_combined():
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    new_gt = GT(df).tab_style_body(
        style=style.fill(color="blue"), values=[1], targets=["row", "column"]
    )
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    # row 0 and column x should all be styled
    assert ("x", 0) in styled_cells
    assert ("y", 0) in styled_cells  # row expansion
    assert ("x", 1) in styled_cells  # column expansion


def test_tab_style_body_extents_stub():
    from great_tables import exibble

    new_gt = GT(exibble, rowname_col="row", groupname_col="group").tab_style_body(
        style=style.fill(color="coral"),
        values=[49.95],
        targets="row",
        extents=["body", "stub"],
    )
    html = new_gt.as_raw_html()
    assert "coral" in html


def test_tab_style_body_no_match():
    df = pd.DataFrame({"x": [1, 2, 3]})
    gt_obj = GT(df)
    new_gt = gt_obj.tab_style_body(style=style.fill(color="red"), values=[999])
    assert len(new_gt._styles) == 0


def test_tab_style_body_no_matching_arg_raises():
    df = pd.DataFrame({"x": [1]})
    with pytest.raises(ValueError, match="At least one of"):
        GT(df).tab_style_body(style=style.fill(color="red"))


def test_tab_style_body_fn_exception_skips():
    df = pd.DataFrame({"x": [1, "text", 3]})
    new_gt = GT(df).tab_style_body(
        style=style.fill(color="blue"),
        fn=lambda val: val > 2,
    )
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 2) in styled_cells  # 3 > 2
    assert ("x", 1) not in styled_cells  # "text" > 2 raises, skipped


def test_tab_style_body_pattern_none_skipped():
    df = pd.DataFrame({"x": [None, "hello", None]})
    new_gt = GT(df).tab_style_body(style=style.fill(color="blue"), pattern="hello")
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 1) in styled_cells
    assert ("x", 0) not in styled_cells
    assert ("x", 2) not in styled_cells


def test_tab_style_body_polars():
    df = pl.DataFrame({"x": [10, 20, 30], "y": [1, 2, 3]})
    new_gt = GT(df).tab_style_body(
        style=style.fill(color="yellow"),
        fn=lambda val: val >= 20,
    )
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 1) in styled_cells  # 20
    assert ("x", 2) in styled_cells  # 30
    assert ("y", 2) not in styled_cells  # 3 < 20


def test_tab_style_body_multiple_styles():
    df = pd.DataFrame({"x": [1, 2]})
    new_gt = GT(df).tab_style_body(
        style=[style.fill(color="red"), style.text(color="white")],
        values=[1],
    )
    assert len(new_gt._styles) == 1
    assert len(new_gt._styles[0].styles) == 2


def test_tab_style_body_renders_html():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    html = GT(df).tab_style_body(style=style.fill(color="orange"), values=[2]).as_raw_html()
    assert "orange" in html


def test_tab_style_body_nan_normalized_to_none_fn():
    df = pd.DataFrame({"x": [1.0, None, 3.0], "y": ["a", None, "c"]})
    new_gt = GT(df).tab_style_body(style=style.fill(color="red"), fn=lambda x: x is None)
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 1) in styled_cells  # NaN normalized to None
    assert ("y", 1) in styled_cells  # actual None
    assert len(styled_cells) == 2


def test_tab_style_body_nan_normalized_to_none_values():
    df = pd.DataFrame({"x": [1.0, None, 3.0]})
    new_gt = GT(df).tab_style_body(style=style.fill(color="red"), values=[None])
    styled_cells = {(s.colname, s.rownum) for s in new_gt._styles}
    assert ("x", 1) in styled_cells
    assert len(styled_cells) == 1


# =============================================================================
# text_transform tests
# =============================================================================


def test_text_transform_basic(gt: GT):
    new_gt = gt.text_transform(locations=loc.body(columns="x"), fn=lambda x: f"[{x}]")
    html = new_gt.as_raw_html()
    assert "[1]" in html
    assert "[2]" in html


def test_text_transform_formatted_cells():
    df = pd.DataFrame({"val": [1.234, 5.678]})
    html = (
        GT(df)
        .fmt_number(columns="val", decimals=1)
        .text_transform(locations=loc.body(columns="val"), fn=lambda x: f"({x})")
        .as_raw_html()
    )
    assert "(1.2)" in html
    assert "(5.7)" in html


def test_text_transform_row_selection():
    df = pd.DataFrame({"name": ["alice", "bob", "charlie"]})
    html = (
        GT(df)
        .text_transform(locations=loc.body(columns="name", rows=[0, 2]), fn=str.upper)
        .as_raw_html()
    )
    assert "ALICE" in html
    assert "bob" in html
    assert "CHARLIE" in html


def test_text_transform_multiple_locations():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    html = (
        GT(df)
        .text_transform(
            locations=[loc.body(columns="a"), loc.body(columns="b")],
            fn=lambda x: f"*{x}*",
        )
        .as_raw_html()
    )
    assert "*1*" in html
    assert "*2*" in html
    assert "*3*" in html
    assert "*4*" in html


def test_text_transform_polars():
    df = pl.DataFrame({"x": ["hello", "world"]})
    html = GT(df).text_transform(locations=loc.body(columns="x"), fn=str.upper).as_raw_html()
    assert "HELLO" in html
    assert "WORLD" in html


def test_text_transform_skips_na():
    df = pd.DataFrame({"x": [1.0, None, 3.0]})
    html = (
        GT(df).text_transform(locations=loc.body(columns="x"), fn=lambda x: f"[{x}]").as_raw_html()
    )
    assert "[1.0]" in html
    assert "[3.0]" in html


def test_text_transform_chaining():
    df = pd.DataFrame({"x": ["hello"]})
    html = (
        GT(df)
        .text_transform(locations=loc.body(columns="x"), fn=str.upper)
        .text_transform(locations=loc.body(columns="x"), fn=lambda x: f"({x})")
        .as_raw_html()
    )
    assert "(HELLO)" in html


def test_text_transform_latex():
    df = pd.DataFrame({"x": [1, 2]})
    latex = (
        GT(df)
        .fmt_number(columns="x", decimals=0)
        .text_transform(locations=loc.body(columns="x"), fn=lambda x: f"[{x}]")
        .as_latex()
    )
    assert "[1]" in latex
    assert "[2]" in latex


def test_text_transform_loc_stub():
    from great_tables import exibble

    html = (
        GT(exibble[["num", "char", "row"]].head(3), rowname_col="row")
        .text_transform(locations=loc.stub(), fn=str.upper)
        .as_raw_html()
    )
    assert "ROW_1" in html
    assert "ROW_2" in html
    assert "ROW_3" in html


def test_text_transform_loc_stub_with_rows():
    from great_tables import exibble

    html = (
        GT(exibble[["num", "char", "row"]].head(3), rowname_col="row")
        .text_transform(locations=loc.stub(rows=[0]), fn=str.upper)
        .as_raw_html()
    )
    assert "ROW_1" in html
    assert "row_2" in html


def test_text_transform_loc_column_labels():
    df = pd.DataFrame({"first_name": ["Alice"], "score": [95]})
    html = GT(df).text_transform(locations=loc.column_labels(), fn=str.upper).as_raw_html()
    assert "FIRST_NAME" in html
    assert "SCORE" in html


def test_text_transform_loc_column_labels_specific():
    df = pd.DataFrame({"name": ["Alice"], "score": [95]})
    html = (
        GT(df)
        .text_transform(locations=loc.column_labels(columns="name"), fn=str.upper)
        .as_raw_html()
    )
    assert "NAME" in html
    assert "score" in html


def test_text_transform_loc_row_groups():
    from great_tables import exibble

    html = (
        GT(
            exibble[["num", "char", "row", "group"]].head(6),
            rowname_col="row",
            groupname_col="group",
        )
        .text_transform(locations=loc.row_groups(), fn=str.upper)
        .as_raw_html()
    )
    assert "GRP_A" in html
    assert "GRP_B" in html


# =============================================================================
# text_replace tests
# =============================================================================


def test_text_replace_basic():
    df = pd.DataFrame({"x": ["hello_world", "foo_bar"]})
    html = (
        GT(df)
        .text_replace(pattern="_", replacement=" ", locations=loc.body(columns="x"))
        .as_raw_html()
    )
    assert "hello world" in html
    assert "foo bar" in html


def test_text_replace_regex():
    df = pd.DataFrame({"x": ["item (detail)", "thing (info)"]})
    html = (
        GT(df)
        .text_replace(
            pattern=r"\((.+?)\)",
            replacement=r"[\1]",
            locations=loc.body(columns="x"),
        )
        .as_raw_html()
    )
    assert "[detail]" in html
    assert "[info]" in html


def test_text_replace_default_location():
    df = pd.DataFrame({"x": ["aaa", "bbb"]})
    html = GT(df).text_replace(pattern="a", replacement="z").as_raw_html()
    assert "zzz" in html


def test_text_replace_stub():
    from great_tables import exibble

    html = (
        GT(exibble[["num", "char", "row"]].head(3), rowname_col="row")
        .text_replace(pattern="_", replacement=" ", locations=loc.stub())
        .as_raw_html()
    )
    assert "row 1" in html
    assert "row 2" in html


# =============================================================================
# text_case_match tests
# =============================================================================


def test_text_case_match_all():
    from great_tables import exibble

    html = (
        GT(exibble[["char"]].head(4))
        .text_case_match(
            ("apricot", "APRICOT"),
            (["banana", "coconut"], "tropical"),
            default="other",
            locations=loc.body(columns="char"),
        )
        .as_raw_html()
    )
    assert "APRICOT" in html
    assert "tropical" in html
    assert "other" in html


def test_text_case_match_no_default():
    df = pd.DataFrame({"x": ["cat", "dog", "bird"]})
    html = (
        GT(df)
        .text_case_match(
            ("cat", "CAT"),
            locations=loc.body(columns="x"),
        )
        .as_raw_html()
    )
    assert "CAT" in html
    assert "dog" in html  # unchanged
    assert "bird" in html  # unchanged


def test_text_case_match_partial():
    from great_tables import exibble

    html = (
        GT(exibble[["char"]].head(4))
        .text_case_match(
            ("an", "@"),
            replace="partial",
            locations=loc.body(columns="char"),
        )
        .as_raw_html()
    )
    # banana -> b@@a (two "an" replacements)
    assert "b@@a" in html


def test_text_case_match_default_location():
    df = pd.DataFrame({"x": ["yes", "no"]})
    html = GT(df).text_case_match(("yes", "YES")).as_raw_html()
    assert "YES" in html
    assert "no" in html


# =============================================================================
# text_case_when tests
# =============================================================================


def test_text_case_when_basic():
    df = pd.DataFrame({"score": [95, 72, 88, 61]})
    html = (
        GT(df)
        .fmt_number(columns="score", decimals=0)
        .text_case_when(
            (lambda x: int(x) >= 90, "A"),
            (lambda x: int(x) >= 80, "B"),
            (lambda x: int(x) >= 70, "C"),
            default="F",
            locations=loc.body(columns="score"),
        )
        .as_raw_html()
    )
    assert ">A<" in html
    assert ">B<" in html
    assert ">C<" in html
    assert ">F<" in html


def test_text_case_when_no_default():
    df = pd.DataFrame({"x": ["apple", "banana", "cherry"]})
    html = (
        GT(df)
        .text_case_when(
            (lambda x: x.startswith("a"), "MATCHED"),
            locations=loc.body(columns="x"),
        )
        .as_raw_html()
    )
    assert "MATCHED" in html
    assert "banana" in html  # unchanged
    assert "cherry" in html  # unchanged


def test_text_case_when_default_location():
    df = pd.DataFrame({"x": ["yes", "no"]})
    html = GT(df).text_case_when((lambda x: x == "yes", "YES"), default="NO").as_raw_html()
    assert "YES" in html
    assert "NO" in html


def test_text_case_when_first_match_wins():
    df = pd.DataFrame({"x": ["hello"]})
    html = (
        GT(df)
        .text_case_when(
            (lambda x: len(x) > 3, "FIRST"),
            (lambda x: len(x) > 2, "SECOND"),
            locations=loc.body(columns="x"),
        )
        .as_raw_html()
    )
    assert "FIRST" in html
    assert "SECOND" not in html


def test_text_case_match_with_default_no_match():
    # `return default` when no match is found but default is set
    df = pd.DataFrame({"x": ["cat", "dog"]})
    html = (
        GT(df)
        .text_case_match(
            ("bird", "BIRD"),
            default="OTHER",
            locations=loc.body(columns="x"),
        )
        .as_raw_html()
    )

    assert "OTHER" in html
    assert "cat" not in html
    assert "dog" not in html
