from __future__ import annotations

import datetime as dt
import re

import numpy as np
import pandas as pd
import pytest

from great_tables import GT, GTI, exibble
from great_tables._gti import build_spec
from great_tables._gti._render import _load_runtime, render_gti_html
from great_tables._gti._spec import FACET_MAX_VALUES

DF = pd.DataFrame({"id": [f"r{i}" for i in range(6)], "y": [10, 20, 30, 40, 50, 60]})


def spec_of(gt: GT) -> dict:
    return build_spec(gt._build_data(context="html"))


def interactive_of(gt: GT) -> dict:
    spec = spec_of(gt)
    return {key: spec[key] for key in ("controls", "pagination", "display", "layout")}


GTI_DEFAULTS = {
    "controls": {
        "sorting": True,
        "search": True,
        "resizing": True,
        "selection": None,
        "bar": True,
    },
    "pagination": {
        "enabled": True,
        "page_size": 10,
        "page_sizes": [10, 25, 50, 100],
        "size_select": True,
        "info": True,
        "type": "jump",
    },
    "display": {"highlight": True, "compact": False, "wrap": True},
    "layout": {"height": None, "responsive": "scroll"},
}


def with_changes(**changes: dict) -> dict:
    return {key: {**value, **changes.get(key, {})} for key, value in GTI_DEFAULTS.items()}


# defaults ----


def test_gti_defaults():
    assert interactive_of(GTI(DF)) == GTI_DEFAULTS


def test_gti_is_a_gt():
    gti = GTI(DF, rowname_col="id", id="t", locale="fr")
    assert isinstance(gti, GT)
    assert gti._options.table_id.value == "t"
    assert gti._locale is not None and gti._locale._locale == "fr"


def test_gt_defaults_are_unchanged():
    # (A `GT` table's spec still comes from its `opt_interactive()` options)
    spec = interactive_of(GT(DF).opt_interactive())
    assert spec["controls"] == {
        "sorting": True,
        "search": False,
        "resizing": False,
        "selection": None,
        "bar": False,
    }
    assert spec["pagination"]["type"] == "numbers"
    assert spec["pagination"]["size_select"] is False
    assert spec["display"]["highlight"] is False


def test_gt_methods_keep_the_class_and_settings():
    gti = GTI(DF).i_search(False).fmt_integer(columns="y").tab_header(title="T").cols_hide("id")
    assert type(gti) is GTI
    assert interactive_of(gti) == with_changes(controls={"search": False})


def test_i_methods_return_new_tables():
    gti = GTI(DF)
    changed = gti.i_search(False)
    assert changed is not gti
    assert interactive_of(gti) == GTI_DEFAULTS


# the i_ methods ----


@pytest.mark.parametrize(
    "method, key", [("i_sorting", "sorting"), ("i_search", "search"), ("i_resizing", "resizing")]
)
def test_i_controls(method: str, key: str):
    assert interactive_of(getattr(GTI(DF), method)(False)) == with_changes(controls={key: False})
    assert interactive_of(
        getattr(GTI(DF).i_sorting(False).i_search(False).i_resizing(False), method)()
    )["controls"][key]


@pytest.mark.parametrize("method", ["i_sorting", "i_search", "i_resizing"])
@pytest.mark.parametrize("value", ["yes", 1, None])
def test_i_controls_take_bools(method: str, value):
    with pytest.raises(TypeError, match="`enabled=` must be `True` or `False`"):
        getattr(GTI(DF), method)(value)


def test_i_pagination():
    gti = GTI(DF).i_pagination(page_size=20, page_sizes=[20, 50])
    assert interactive_of(gti) == with_changes(pagination={"page_size": 20, "page_sizes": [20, 50]})

    off = GTI(DF).i_pagination(False)
    assert interactive_of(off) == with_changes(pagination={"enabled": False})

    no_info = GTI(DF).i_pagination(info=False)
    assert interactive_of(no_info) == with_changes(pagination={"info": False})


@pytest.mark.parametrize("info", ["yes", 1, None])
def test_i_pagination_info_takes_bools(info):
    with pytest.raises(TypeError, match="`info=` must be `True` or `False`"):
        GTI(DF).i_pagination(info=info)


@pytest.mark.parametrize("page_sizes", [None, [], ()])
def test_i_pagination_without_size_choice(page_sizes):
    gti = GTI(DF).i_pagination(page_size=25, page_sizes=page_sizes)
    assert interactive_of(gti)["pagination"] == {
        **GTI_DEFAULTS["pagination"],
        "page_size": 25,
        "page_sizes": [],
        "size_select": False,
    }


def test_i_pagination_takes_numpy_ints():
    gti = GTI(DF).i_pagination(page_size=np.int64(5), page_sizes=np.array([5, 10]))
    pagination = interactive_of(gti)["pagination"]
    assert pagination["page_size"] == 5 and type(pagination["page_size"]) is int
    assert pagination["page_sizes"] == [5, 10]


@pytest.mark.parametrize("page_size", [0, -1, 2.5, True, "10", None])
def test_i_pagination_page_size_must_be_a_whole_number(page_size):
    with pytest.raises(ValueError, match="`page_size=` must be a whole number"):
        GTI(DF).i_pagination(page_size=page_size)


@pytest.mark.parametrize("page_sizes", [[10, 0], [10, 2.5], [False]])
def test_i_pagination_page_sizes_must_be_whole_numbers(page_sizes):
    with pytest.raises(ValueError, match="`page_sizes=` must be a whole number"):
        GTI(DF).i_pagination(page_sizes=page_sizes)


def test_i_methods_set_all_of_a_features_settings():
    # (What's not given goes back to its default, rather than staying as set before)
    gti = GTI(DF).i_pagination(page_size=25, page_sizes=None).i_pagination()
    assert interactive_of(gti) == GTI_DEFAULTS

    gti = GTI(DF).i_display(highlight=False, compact=True).i_display(wrap=False)
    assert interactive_of(gti) == with_changes(display={"wrap": False})


@pytest.mark.parametrize("mode", ["single", "multiple"])
def test_i_selection(mode: str):
    assert interactive_of(GTI(DF).i_selection(mode)) == with_changes(controls={"selection": mode})


def test_i_selection_default_and_off():
    assert interactive_of(GTI(DF).i_selection())["controls"]["selection"] == "multiple"
    assert interactive_of(GTI(DF).i_selection().i_selection(None)) == GTI_DEFAULTS


@pytest.mark.parametrize("mode", ["all", "Multiple", True])
def test_i_selection_mode_must_be_known(mode):
    with pytest.raises(ValueError, match='`mode=` must be "multiple", "single", or `None`'):
        GTI(DF).i_selection(mode)


@pytest.mark.parametrize(
    "height, expected",
    [
        ("400px", "400px"),
        ("min(60vh, 600px)", "min(60vh, 600px)"),
        (400, "400px"),
        (250.5, "250.5px"),
    ],
)
def test_i_scroll(height, expected: str):
    gti = GTI(DF).i_scroll(height)
    assert interactive_of(gti) == with_changes(layout={"height": expected})
    assert gti.as_raw_html().startswith(
        f'<gt-table data-gti-bar data-gti-scroll style="--gt-i-height: {expected}">'
    )


@pytest.mark.parametrize("height", [None, "auto"])
def test_i_scroll_off(height):
    assert interactive_of(GTI(DF).i_scroll(400).i_scroll(height)) == GTI_DEFAULTS


@pytest.mark.parametrize("height", ["400", "-5px", "red", "", "400px;color:red", True, -1])
def test_i_scroll_height_must_be_a_length(height):
    with pytest.raises(ValueError, match="`height=` must be a CSS length"):
        GTI(DF).i_scroll(height)


def test_i_display():
    gti = GTI(DF).i_display(highlight=False, compact=True, wrap=False)
    assert interactive_of(gti) == with_changes(
        display={"highlight": False, "compact": True, "wrap": False}
    )
    assert gti.as_raw_html().startswith("<gt-table data-gti-bar data-gti-nowrap>")


def test_i_display_compact_halves_row_padding():
    def row_padding(gt: GT) -> str:
        rule = re.search(r"#t \.gt_row {[^}]*?padding-top: ([^;]+);", gt.as_raw_html())
        assert rule is not None
        return rule.group(1)

    assert row_padding(GTI(DF, id="t")) == "8px"
    assert row_padding(GTI(DF, id="t").i_display(compact=True)) == "4px"


@pytest.mark.parametrize("option", ["highlight", "compact", "wrap"])
def test_i_display_takes_bools(option: str):
    with pytest.raises(TypeError, match=f"`{option}=` must be `True` or `False`"):
        GTI(DF).i_display(**{option: "yes"})


# filters ----

# Columns of each kind: numbers, booleans, a category, text with few values (each repeated) and
# with many, and values that can't be sorted
FILTER_DF = pd.DataFrame(
    {
        "id": [f"r{i}" for i in range(6)],
        "num": [3.5, 1.0, None, 3.5, 2.0, 1.0],
        "flag": [True, False, True, True, False, True],
        "cat": pd.Categorical(["lo", "hi", "lo", None, "hi", "lo"], categories=["lo", "hi"]),
        "few": ["b", "a", "b", "a", "b", "b"],
        "many": ["u", "v", "w", "x", "y", "z"],
        "mixed": [1, "a", 2.0, 1, "a", 2.0],
    }
)


def filters_of(gt: GT) -> list[dict]:
    return spec_of(gt)["filters"]


def test_i_cols_filter_off_by_default():
    assert filters_of(GTI(FILTER_DF)) == []
    assert GTI(FILTER_DF)._interactive.filters == ()


def test_i_cols_filter_auto():
    gti = GTI(FILTER_DF, rowname_col="id").i_cols_filter()

    # (Every column but the stub, in column order, with the facets' and ranges' values in rank
    # order)
    assert filters_of(gti) == [
        {"column": "num", "type": "range", "values": [1.0, 2.0, 3.5]},
        {"column": "flag", "type": "facet", "values": [False, True]},
        {"column": "cat", "type": "facet", "values": ["lo", "hi"]},
        {"column": "few", "type": "facet", "values": ["a", "b"]},
        {"column": "many", "type": "text", "values": None},
        {"column": "mixed", "type": "text", "values": None},
    ]


@pytest.mark.parametrize(
    "distinct, expected", [(FACET_MAX_VALUES, "facet"), (FACET_MAX_VALUES + 1, "text")]
)
def test_i_cols_filter_auto_facets_text_with_few_values(distinct: int, expected: str):
    df = pd.DataFrame({"x": [f"v{i:02}" for i in range(distinct)] * 2})
    assert filters_of(GTI(df).i_cols_filter())[0]["type"] == expected


def test_i_cols_filter_types():
    gti = (
        GTI(FILTER_DF, rowname_col="id")
        .i_cols_filter(columns="num", type="facet")
        .i_cols_filter(columns=["few", "flag"], type="text")
        .i_cols_filter(columns="id")
    )

    assert gti._interactive.filters == (
        ("num", "facet"),
        ("few", "text"),
        ("flag", "text"),
        ("id", "auto"),
    )
    # (The stub, when named; in column order)
    assert filters_of(gti) == [
        {"column": "id", "type": "text", "values": None},
        {"column": "num", "type": "facet", "values": [1.0, 2.0, 3.5]},
        {"column": "flag", "type": "text", "values": None},
        {"column": "few", "type": "text", "values": None},
    ]


def test_i_cols_filter_replaces_and_removes():
    gti = GTI(FILTER_DF).i_cols_filter(columns=["num", "few"], type="text")
    assert gti.i_cols_filter(columns="num", type="range")._interactive.filters == (
        ("few", "text"),
        ("num", "range"),
    )
    assert gti.i_cols_filter(columns="few", type=None)._interactive.filters == (("num", "text"),)
    assert gti.i_cols_filter(type=None)._interactive.filters == ()


def test_i_cols_filter_leaves_out_the_row_group_column():
    gti = GTI(FILTER_DF, groupname_col="few").i_cols_filter(columns=["few", "num"])
    assert [f["column"] for f in filters_of(gti)] == ["num"]


@pytest.mark.parametrize("type", ["Range", "number", True, ""])
def test_i_cols_filter_type_must_be_known(type):
    with pytest.raises(ValueError, match='`type=` must be "auto", "text", "facet", "range"'):
        GTI(FILTER_DF).i_cols_filter(columns="num", type=type)


@pytest.mark.parametrize("column", ["few", "flag", "cat"])
def test_i_cols_filter_range_needs_numbers(column: str):
    with pytest.raises(ValueError, match=f"Column '{column}' can't be filtered by a range"):
        GTI(FILTER_DF).i_cols_filter(columns=column, type="range")


def test_i_cols_filter_facet_needs_comparable_values():
    with pytest.raises(ValueError, match="Column 'mixed' can't be filtered by a facet"):
        GTI(FILTER_DF).i_cols_filter(columns="mixed", type="facet")
    # (But by text)
    gti = GTI(FILTER_DF).i_cols_filter(columns="mixed", type="text")
    assert filters_of(gti) == [{"column": "mixed", "type": "text", "values": None}]


def test_i_cols_filter_unsortable_facet_is_text():
    # (A facet goes by the column's ranks, which a column the backend can't sort lacks: naive and
    # aware datetimes can't be compared)
    df = pd.DataFrame(
        {"x": [dt.datetime(2024, 1, 1), dt.datetime(2024, 1, 2, tzinfo=dt.timezone.utc)]}
    )
    gti = GTI(df).i_cols_filter(columns="x", type="facet")
    assert filters_of(gti) == [{"column": "x", "type": "text", "values": None}]


def test_i_cols_filter_values_are_json():
    df = pd.DataFrame(
        {
            "n": np.array([2, 1, 2], dtype="int32"),
            "d": [dt.date(2024, 5, 1), dt.date(2023, 1, 2), None],
            "f": [0.5, float("nan"), 0.25],
        }
    )
    gti = GTI(df).i_cols_filter(type="facet")
    assert [f["values"] for f in filters_of(gti)] == [
        [1, 2],
        ["2023-01-02", "2024-05-01"],
        [0.25, 0.5],
    ]
    assert all(type(value) is int for value in filters_of(gti)[0]["values"])


def test_i_view_sets_the_whole_view():
    query = {"and": [{"col": "few", "op": "in", "value": ["a"]}]}
    gti = GTI(FILTER_DF).i_cols_filter(columns="few").i_view(filter=query, sort="-num")
    assert gti._interactive.view_filter == query
    assert gti._interactive.view_sort == (("num", True),)
    assert spec_of(gti)["view"] == {
        "filter": query,
        "sort": [{"column": "num", "descending": True}],
    }
    # (What's not given goes back to its default)
    assert gti.i_view(sort="id")._interactive.view_filter is None
    assert spec_of(gti.i_view())["view"] == {"filter": None, "sort": []}


def test_i_cols_filter_keeps_room_for_the_bar():
    gti = GTI(DF).i_search(False)
    assert gt_table_tag(gti) == "<gt-table>"
    assert gt_table_tag(gti.i_cols_filter(columns="y")) == "<gt-table data-gti-bar>"


# the control bar ----


def gt_table_tag(gt: GT) -> str:
    return gt.as_raw_html().split("\n", 1)[0]


def test_control_bar_room_is_kept_for_a_search_or_pages():
    many = pd.DataFrame({"y": range(11)})
    assert gt_table_tag(GTI(DF)) == "<gt-table data-gti-bar>"
    assert gt_table_tag(GTI(many).i_search(False)) == "<gt-table data-gti-bar>"
    # (Not for one page, or none)
    assert gt_table_tag(GTI(DF).i_search(False)) == "<gt-table>"
    assert gt_table_tag(GTI(many).i_search(False).i_pagination(False)) == "<gt-table>"
    no_choice = GTI(many).i_search(False).i_pagination(page_size=11, page_sizes=None)
    assert gt_table_tag(no_choice) == "<gt-table>"
    # (But for a page size readers can choose, in the bar's info panel, that makes pages)
    assert gt_table_tag(GTI(many).i_search(False).i_pagination(page_size=11)) == (
        "<gt-table data-gti-bar>"
    )
    few = GTI(many).i_search(False).i_pagination(page_size=11, page_sizes=[11, 50])
    assert gt_table_tag(few) == "<gt-table>"


def test_opt_interactive_tables_have_no_control_bar():
    gt = GT(pd.DataFrame({"y": range(11)})).opt_interactive(use_search=True)
    assert spec_of(gt)["controls"]["bar"] is False
    assert render_gti_html(gt, runtime="none").startswith("<gt-table>\n")


# from_gt ----


def test_from_gt():
    gt = GT(DF, rowname_col="id", id="t").fmt_integer(columns="y").tab_header(title="Title")
    gti = GTI.from_gt(gt)

    assert type(gti) is GTI
    assert interactive_of(gti) == GTI_DEFAULTS
    # (With the GT table's everything else, which is unchanged)
    assert gti._options is gt._options and gti._formats is gt._formats
    assert type(gt) is GT and not hasattr(gt, "_interactive")
    assert 'id="t"' in gti.as_raw_html() and "Title" in gti.as_raw_html()


def test_from_gt_with_opt_interactive():
    gt = GT(DF).opt_interactive(
        use_search=True,
        use_highlight=True,
        use_page_size_select=True,
        page_size_default=25,
        pagination_type="full",
        selection_mode="single",
    )
    gti = GTI.from_gt(gt)

    # What `opt_interactive()` set, with GTI's page controls
    assert interactive_of(gti) == with_changes(
        controls={"resizing": False, "selection": "single"},
        pagination={"page_size": 25},
    )


def test_from_gt_with_use_filters():
    gt = GT(FILTER_DF[["id", "num", "few"]], rowname_col="id").opt_interactive(use_filters=True)
    # (A GT table's own filters are reactable's, which `<gt-table>` doesn't have)
    assert filters_of(gt) == []
    assert GTI.from_gt(gt)._interactive.filters == (("num", "auto"), ("few", "auto"))
    assert [f["type"] for f in filters_of(GTI.from_gt(gt))] == ["range", "facet"]
    assert GTI.from_gt(gt.opt_interactive())._interactive.filters == ()


def test_from_gt_of_a_gti():
    gti = GTI(DF).i_search(False)
    assert GTI.from_gt(gti) is gti


def test_from_gt_needs_a_gt():
    with pytest.raises(TypeError, match="needs a `GT` table"):
        GTI.from_gt(DF)  # type: ignore[arg-type]


# output ----


def test_as_raw_html_is_interactive():
    html = GTI(DF).as_raw_html()
    js, css = _load_runtime()
    assert html.startswith("<gt-table data-gti-bar>\n")
    assert css in html and js in html


def test_as_raw_html_make_page():
    html = GTI(DF).as_raw_html(make_page=True)
    assert html.startswith('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    assert '<meta name="viewport" content="width=device-width, initial-scale=1"/>' in html
    assert "<body>\n<gt-table data-gti-bar>\n" in html
    assert html.endswith("</body>\n</html>\n")


def test_as_raw_html_all_important():
    assert "!important" not in GTI(DF, id="t").as_raw_html().split("<style>\n", 2)[1]
    html = GTI(DF, id="t").as_raw_html(all_important=True)
    assert re.search(r"#t \.gt_row {[^}]*?!important", html)


def test_as_raw_html_inline_css_is_not_available():
    with pytest.raises(ValueError, match="can't have its CSS inlined"):
        GTI(DF).as_raw_html(inline_css=True)


def test_repr_html_is_interactive():
    assert "<gt-table data-gti-bar>" in GTI(DF)._repr_html_()


def test_write_raw_html(tmp_path):
    GTI(DF).write_raw_html(tmp_path / "gti.html", make_page=True)
    GT(DF).write_raw_html(tmp_path / "gt.html")

    assert "<gt-table data-gti-bar>" in (tmp_path / "gti.html").read_text(encoding="utf-8")
    assert "<gt-table" not in (tmp_path / "gt.html").read_text(encoding="utf-8")


@pytest.mark.parametrize("method", ["save", "gtsave", "as_latex"])
def test_static_output_is_not_available(method: str, tmp_path):
    with pytest.raises(TypeError, match="interactive HTML only"):
        getattr(GTI(DF), method)(tmp_path / "table.png")


def test_opt_interactive_is_not_available():
    with pytest.raises(TypeError, match="`i_` methods") as info:
        GTI(DF).opt_interactive(use_search=True)
    # (Naming every one)
    for name in [name for name in dir(GTI) if name.startswith("i_")]:
        assert f"`{name}()`" in str(info.value)


# GT and the i_ methods ----


def test_gt_has_no_i_methods():
    gt = GT(exibble)
    with pytest.raises(AttributeError, match=r"`i_search\(\)` is a method of interactive tables"):
        gt.i_search()
    assert not hasattr(gt, "i_pagination")


def test_gt_other_attributes_are_missing_as_usual():
    gt = GT(exibble)
    for name in ["i_serch", "tab_hedaer"]:
        with pytest.raises(AttributeError, match=f"'GT' object has no attribute '{name}'") as info:
            getattr(gt, name)
        # (So that Python can suggest a name that's close)
        assert info.value.name == name and info.value.obj is gt
