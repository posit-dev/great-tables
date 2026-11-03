from __future__ import annotations

import datetime as dt
import re

import numpy as np
import pandas as pd
import polars as pl
import pyarrow as pa
import pytest

from great_tables import GT, GTI, exibble, html
from great_tables._gti._render import _load_runtime, render_gti_html, render_parts
from great_tables._gti._spec import FACET_MAX_VALUES

DF = pd.DataFrame({"id": [f"r{i}" for i in range(6)], "y": [10, 20, 30, 40, 50, 60]})


def spec_of(gt: GT) -> dict:
    # (As the table is rendered, with the columns only for querying left out)
    return render_parts(gt)[1]


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


def controls_of(gt: GT) -> dict:
    return {
        column["id"]: (column["sortable"], column["searchable"], column["resizable"])
        for column in spec_of(gt)["columns"]
    }


def test_i_cols_controls_all_on_by_default():
    gti = GTI(FILTER_DF, rowname_col="id")
    assert set(controls_of(gti).values()) == {(True, True, True)}
    assert (gti._interactive.unsortable, gti._interactive.unsearchable) == ((), ())
    assert gti._interactive.unresizable == ()


def test_i_cols_controls():
    gti = (
        GTI(FILTER_DF[["id", "num", "flag", "few"]], rowname_col="id")
        .i_cols_controls(columns=["num", "few"], sortable=False, searchable=False)
        .i_cols_controls(columns="id", resizable=False)
    )

    # (The stub, when named; others left as they are)
    assert controls_of(gti) == {
        "id": (True, True, False),
        "num": (False, False, True),
        "flag": (True, True, True),
        "few": (False, False, True),
    }


def test_i_cols_controls_replaces_and_restores():
    gti = GTI(FILTER_DF).i_cols_controls(columns=["num", "few"], sortable=False)
    # (`None` leaves a column as it is; `True` puts it back)
    assert gti.i_cols_controls(columns="num", searchable=False)._interactive.unsortable == (
        "num",
        "few",
    )
    assert gti.i_cols_controls(columns="num", sortable=True)._interactive.unsortable == ("few",)
    assert gti.i_cols_controls(sortable=True)._interactive.unsortable == ()
    # (Every column but the stub)
    every = GTI(FILTER_DF, rowname_col="id").i_cols_controls(resizable=False)
    assert "id" not in every._interactive.unresizable
    assert len(every._interactive.unresizable) == len(FILTER_DF.columns) - 1


def test_i_cols_controls_leaves_out_the_row_group_column():
    gti = GTI(FILTER_DF, groupname_col="few").i_cols_controls(["few", "num"], sortable=False)
    assert gti._interactive.unsortable == ("num",)


def test_i_cols_controls_keeps_ranks_of_unsortable_columns():
    # (So that `i_view()` can still sort by them)
    gti = GTI(DF).i_cols_controls(columns="y", sortable=False).i_view(sort="-y")
    spec = spec_of(gti)
    assert "y" in spec["ranks"]
    assert spec["view"]["sort"] == [{"column": "y", "descending": True}]


def test_i_cols_controls_for_summary_labels_only():
    # (The stub column for summary labels has no name to give)
    total = {"Total": lambda df: df[["y"]].sum()}
    spec = spec_of(GTI(DF).grand_summary_rows(fns=total).i_cols_controls(sortable=False))
    assert spec["columns"][0]["id"] is None
    assert spec["columns"][0]["sortable"] is True
    assert [column["sortable"] for column in spec["columns"][1:]] == [False, False]


@pytest.mark.parametrize(
    "name", ["sortable", "searchable", "resizable", "hideable", "reorderable", "display"]
)
@pytest.mark.parametrize("value", [1, "no", 0.0])
def test_i_cols_controls_flags_must_be_bools(name: str, value):
    with pytest.raises(TypeError, match=f"`{name}=` must be `True`, `False`, or `None`"):
        GTI(DF).i_cols_controls(columns="y", **{name: value})


def hideable_of(gt: GT) -> dict:
    return {column["id"]: column["hideable"] for column in spec_of(gt)["columns"]}


def test_i_cols_controls_hides_none_by_default():
    gti = GTI(PIN_DF, rowname_col="id")
    assert gti._interactive.hideable == ()
    assert set(hideable_of(gti).values()) == {False}
    assert spec_of(gti)["view"]["hidden"] == []


def test_i_cols_controls_hideable():
    gti = GTI(PIN_DF, rowname_col="id").i_cols_controls(["e", "a", "b"], hideable=True)
    assert gti._interactive.hideable == ("e", "a", "b")
    assert hideable_of(gti) == {
        "id": False,
        "a": True,
        "b": True,
        "c": False,
        "d": False,
        "e": True,
    }
    # (`False` takes them back; the others are left as they are)
    assert gti.i_cols_controls("a", hideable=False)._interactive.hideable == ("e", "b")
    assert gti.i_cols_controls("a", sortable=False)._interactive.hideable == ("e", "a", "b")
    every = GTI(PIN_DF, rowname_col="id").i_cols_controls(hideable=True)
    assert every._interactive.hideable == ("a", "b", "c", "d", "e")
    assert every.i_cols_controls(hideable=False)._interactive.hideable == ()


def test_i_cols_controls_hideable_leaves_out_the_stub_and_row_group_column():
    # (Naming the stub does nothing; the row group column can't be named)
    gti = GTI(PIN_DF, rowname_col="id", groupname_col="b").i_cols_controls(
        ["id", "b", "a"], hideable=True
    )
    assert hideable_of(gti) == {"id": False, "a": True, "c": False, "d": False, "e": False}
    # (A column `cols_hide()` hid isn't in the spec)
    assert "a" not in hideable_of(gti.cols_hide("a"))


def reorderable_of(gt: GT) -> dict:
    return {column["id"]: column["reorderable"] for column in spec_of(gt)["columns"]}


def test_i_cols_controls_reorders_none_by_default():
    gti = GTI(PIN_DF, rowname_col="id")
    assert gti._interactive.reorderable == ()
    assert set(reorderable_of(gti).values()) == {False}


def test_i_cols_controls_reorderable():
    gti = GTI(PIN_DF, rowname_col="id").i_cols_controls(["e", "a", "b"], reorderable=True)
    assert gti._interactive.reorderable == ("e", "a", "b")
    assert reorderable_of(gti) == {
        "id": False,
        "a": True,
        "b": True,
        "c": False,
        "d": False,
        "e": True,
    }
    # (`False` takes them back; the others are left as they are, as is `hideable`)
    assert gti.i_cols_controls("a", reorderable=False)._interactive.reorderable == ("e", "b")
    assert gti.i_cols_controls("a", hideable=True)._interactive.reorderable == ("e", "a", "b")
    assert gti._interactive.hideable == ()
    every = GTI(PIN_DF, rowname_col="id").i_cols_controls(reorderable=True)
    assert every._interactive.reorderable == ("a", "b", "c", "d", "e")
    assert every.i_cols_controls(reorderable=False)._interactive.reorderable == ()


def test_i_cols_controls_reorderable_leaves_out_the_stub_and_row_group_column():
    gti = GTI(PIN_DF, rowname_col="id", groupname_col="b").i_cols_controls(
        ["id", "b", "a"], reorderable=True
    )
    assert reorderable_of(gti) == {"id": False, "a": True, "c": False, "d": False, "e": False}


QUERY_DF = pd.DataFrame(
    {
        "id": ["r0", "r1", "r2", "r3"],
        "kind": ["pear", "apple", "pear", None],
        "n": [3, 1, 2, 4],
        "y": [1.5, 2.5, 3.5, 4.5],
    }
)


def query_gti() -> GTI:
    return GTI(QUERY_DF, rowname_col="id").i_cols_controls(["kind", "n"], display=False)


def test_i_cols_controls_display():
    gti = query_gti()
    assert gti._interactive.query_only == ("kind", "n")
    # (`True` puts a column back; `None` leaves it as it is)
    assert gti.i_cols_controls("n", display=True)._interactive.query_only == ("kind",)
    assert gti.i_cols_controls("n", sortable=False)._interactive.query_only == ("kind", "n")
    assert GTI(QUERY_DF)._interactive.query_only == ()


def test_i_cols_controls_display_false_leaves_a_column_out_for_querying():
    gti = query_gti().i_cols_filter(columns="kind").i_cols_filter(columns="n", type="range")
    html, spec = render_parts(gti)
    assert [column["id"] for column in spec["columns"]] == ["id", "y"]
    assert spec["query_columns"] == [
        {
            "id": "kind",
            "kind": "string",
            "label": "kind",
            "texts": ["pear", "apple", "pear", "None"],
        },
        {"id": "n", "kind": "number", "label": "n", "texts": None},
    ]
    # (Its ranks, and its filter, after those of the table's columns)
    assert spec["ranks"]["kind"] == [1, 0, 1, None]
    assert spec["ranks"]["n"] == [2, 0, 1, 3]
    assert [f["column"] for f in spec["filters"]] == ["kind", "n"]
    assert spec["filters"][0] == {"column": "kind", "type": "facet", "values": ["apple", "pear"]}
    # (It isn't in the table)
    assert "pear" not in html
    assert ">kind<" not in html
    assert spec_of(GTI(QUERY_DF))["query_columns"] == []


def test_i_cols_controls_display_false_ships_the_text_cells_would_show():
    gti = (
        query_gti()
        .fmt_integer(columns="n", pattern="{x} <img src='a.png' alt='items'>")
        .fmt(columns="kind", fns=lambda x: f"<b>{x}</b>  fruit")
        .cols_label(kind="<b>The  kind</b>", n="Count")
        .i_cols_filter(columns=["kind", "n"], type="text")
    )
    kind, n = spec_of(gti)["query_columns"]
    assert n["label"] == "Count"
    # (Shown, then what isn't)
    assert n["texts"] == ["3 \nitems", "1 \nitems", "2 \nitems", "4 \nitems"]
    assert kind["label"] == "<b>The kind</b>"
    assert kind["texts"][0] == "pear  fruit"
    # (A facet's, as its labels, with whitespace collapsed)
    facet = spec_of(gti.i_cols_filter(columns="kind", type="facet"))["query_columns"][0]
    assert facet["texts"][0] == "pear fruit"
    # (A label of HTML)
    labelled = spec_of(query_gti().cols_label(kind=html("<em>Fruit</em>  kind")))
    assert labelled["query_columns"][0]["label"] == "Fruit kind"


def test_i_cols_controls_display_false_keeps_a_hidden_column_for_querying():
    gti = GTI(QUERY_DF, rowname_col="id").cols_hide("kind")
    assert spec_of(gti)["query_columns"] == []
    spec = spec_of(gti.i_cols_controls("kind", display=False))
    assert [column["id"] for column in spec["query_columns"]] == ["kind"]
    # (And `display=True` doesn't show it)
    shown = spec_of(gti.i_cols_controls("kind", display=False).i_cols_controls(display=True))
    assert "kind" not in [column["id"] for column in shown["columns"]]


def test_i_cols_controls_display_false_columns_aren_t_hideable_reorderable_or_pinned():
    gti = (
        query_gti()
        .i_cols_controls(hideable=True, reorderable=True)
        .i_cols_pin(columns="n", side="right")
    )
    spec = spec_of(gti)
    assert [column["id"] for column in spec["columns"]] == ["id", "y"]
    assert [column["pin"] for column in spec["columns"]] == [None, None]
    with pytest.raises(ValueError, match="The view can't hide column 'kind'"):
        spec_of(gti.i_view(hidden="kind"))


def test_i_cols_controls_display_false_columns_can_be_filtered_and_sorted_by():
    gti = query_gti().i_cols_filter(columns="kind").i_view(filter='kind in ("pear")', sort="-n")
    assert spec_of(gti)["view"]["filter"] == {
        "and": [{"col": "kind", "op": "in", "value": ["pear"]}]
    }
    assert spec_of(gti)["view"]["sort"] == [{"column": "n", "descending": True}]


@pytest.mark.parametrize("column", ["id", "g"])
def test_i_cols_controls_display_false_leaves_in_the_stub_and_row_group_column(column: str):
    df = QUERY_DF.assign(g=["a", "a", "b", "b"])
    with pytest.raises(ValueError, match=f"can't be set for '{column}'"):
        GTI(df, rowname_col="id", groupname_col="g").i_cols_controls([column, "y"], display=False)
    # (Nor when they're set after)
    gti = GTI(df).i_cols_controls(column, display=False)
    with pytest.raises(ValueError, match=f"can't be set for '{column}'"):
        render_parts(gti.tab_stub(rowname_col="id", groupname_col="g"))


def test_i_cols_controls_display_false_leaves_in_a_column():
    with pytest.raises(ValueError, match="every column left out"):
        render_parts(GTI(QUERY_DF).i_cols_controls(display=False))
    # (With a stub, the stub is left)
    spec = spec_of(GTI(QUERY_DF, rowname_col="id").i_cols_controls(display=False))
    assert [column["id"] for column in spec["columns"]] == ["id"]


def test_i_view_hides_columns():
    gti = GTI(PIN_DF, rowname_col="id").i_cols_controls(["a", "b", "c"], hideable=True)
    # (In column order, once each, in the spec)
    view = gti.i_view(hidden=["c", "a", "c"])
    assert view._interactive.view_hidden == ("c", "a", "c")
    assert spec_of(view)["view"] == {"filter": None, "sort": [], "hidden": ["a", "c"]}
    assert spec_of(gti.i_view(hidden="b"))["view"]["hidden"] == ["b"]
    # (What's not given goes back to its default)
    assert view.i_view(sort="a")._interactive.view_hidden == ()


@pytest.mark.parametrize("column", ["d", "id"])
def test_i_view_hides_only_columns_readers_can_hide(column: str):
    gti = GTI(PIN_DF, rowname_col="id").i_cols_controls(["a", "b"], hideable=True)
    with pytest.raises(ValueError, match=f"The view can't hide column '{column}'"):
        spec_of(gti.i_view(hidden=["a", column]))


def pins_of(gt: GT) -> dict:
    return {column["id"]: column["pin"] for column in spec_of(gt)["columns"]}


PIN_DF = pd.DataFrame({name: [1, 2] for name in ["id", "a", "b", "c", "d", "e"]})


def test_i_cols_pin_none_by_default():
    gti = GTI(PIN_DF, rowname_col="id")
    assert gti._interactive.pins == ()
    assert set(pins_of(gti).values()) == {None}


def test_i_cols_pin():
    gti = GTI(PIN_DF, rowname_col="id").i_cols_pin(["a", "b"]).i_cols_pin("e", side="right")
    assert gti._interactive.pins == (("a", "left"), ("b", "left"), ("e", "right"))
    # (As the start and end of the column order, in the spec)
    assert pins_of(gti) == {
        "id": None,
        "a": "start",
        "b": "start",
        "c": None,
        "d": None,
        "e": "end",
    }


def test_i_cols_pin_replaces_and_unpins():
    gti = GTI(PIN_DF).i_cols_pin(["id", "a"]).i_cols_pin("a", side="right")
    assert gti._interactive.pins == (("id", "left"), ("a", "right"))
    assert gti.i_cols_pin("a", side=None)._interactive.pins == (("id", "left"),)
    assert gti.i_cols_pin(side=None)._interactive.pins == ()
    # (Every column but the stub)
    every = GTI(PIN_DF, rowname_col="id").i_cols_pin(side="right")
    assert [column for column, _ in every._interactive.pins] == ["a", "b", "c", "d", "e"]
    assert set(pins_of(every).values()) == {None, "end"}


def test_i_cols_pin_leaves_out_the_stub_and_row_group_column():
    # (They're always pinned, at the start)
    gti = GTI(PIN_DF, rowname_col="id").i_cols_pin(["id", "a"], side="right")
    assert pins_of(gti.cols_move_to_end("a")) == {
        "id": None,
        "b": None,
        "c": None,
        "d": None,
        "e": None,
        "a": "end",
    }
    grouped = GTI(PIN_DF, groupname_col="b").i_cols_pin(["b", "id"])
    assert grouped._interactive.pins == (("id", "left"),)


def test_i_cols_pin_checks_columns_are_next_to_their_side():
    gti = GTI(PIN_DF, rowname_col="id").i_cols_pin(["a", "c"])
    with pytest.raises(ValueError, match=r"Column 'c' can't be pinned to the left") as error:
        spec_of(gti)
    assert "('b') would have to be pinned too" in str(error.value)
    assert "`cols_move_to_start()`" in str(error.value)

    right = GTI(PIN_DF, rowname_col="id").i_cols_pin(["b", "e"], side="right")
    with pytest.raises(ValueError, match=r"Column 'b' can't be pinned to the right") as error:
        spec_of(right)
    assert "('c', 'd') would have to be pinned too" in str(error.value)
    assert "`cols_move_to_end()`" in str(error.value)

    # (Checked once the columns are in their places: moving them there is enough)
    assert pins_of(gti.cols_move_to_start("c"))["c"] == "start"
    assert pins_of(right.cols_move_to_end("b"))["b"] == "end"


def test_i_cols_pin_skips_hidden_columns():
    gti = GTI(PIN_DF, rowname_col="id").i_cols_pin(["a", "c"]).cols_hide("b")
    assert pins_of(gti) == {"id": None, "a": "start", "c": "start", "d": None, "e": None}
    # (A pinned column that's hidden isn't in the spec)
    hidden = GTI(PIN_DF).i_cols_pin(["id", "c"]).cols_hide(["a", "c"])
    assert pins_of(hidden) == {"id": "start", "b": None, "d": None, "e": None}


@pytest.mark.parametrize("side", ["start", "LEFT", True])
def test_i_cols_pin_side_must_be_a_side(side):
    with pytest.raises(ValueError, match='`side=` must be "left", "right", or `None`'):
        GTI(PIN_DF).i_cols_pin("a", side=side)


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
        "hidden": [],
    }
    # (What's not given goes back to its default)
    assert gti.i_view(sort="id")._interactive.view_filter is None
    assert spec_of(gti.i_view())["view"] == {"filter": None, "sort": [], "hidden": []}


def test_i_view_takes_a_query_as_text():
    gti = GTI(FILTER_DF).i_cols_filter(columns=["few", "num"])
    text = gti.i_view(filter='few in ("a") and num >= 1.5')
    query = {
        "and": [
            {"col": "few", "op": "in", "value": ["a"]},
            {"col": "num", "op": "gte", "value": 1.5},
        ]
    }
    assert spec_of(text) == spec_of(gti.i_view(filter=query))
    assert gti.i_view(filter=" ")._interactive.view_filter is None
    with pytest.raises(ValueError, match=r"can't be read as a query: expected a number, at char"):
        gti.i_view(filter="num >= x")


def test_i_view_keeps_room_for_the_filter_tokens():
    gti = GTI(FILTER_DF).i_cols_filter(columns=["few", "id"])
    assert gt_table_tag(gti.i_view(filter='few in ("a")')) == (
        "<gt-table data-gti-bar data-gti-tokens>"
    )
    # (Not for no filter, or one that's off)
    assert gt_table_tag(gti.i_view(sort="few")) == "<gt-table data-gti-bar>"
    assert gt_table_tag(gti.i_view(filter='id contains " \\u00a0"')) == "<gt-table data-gti-bar>"


def test_i_cols_filter_keeps_room_for_the_bar():
    gti = GTI(DF).i_search(False)
    assert gt_table_tag(gti) == "<gt-table>"
    assert gt_table_tag(gti.i_cols_filter(columns="y")) == "<gt-table data-gti-bar>"


# export ----


def test_export_is_off_by_default():
    assert spec_of(GTI(DF))["export"] == {"formats": [], "filename": "table", "code": None}
    assert spec_of(GTI.from_gt(GT(DF).opt_interactive()))["export"]["formats"] == []


def test_i_export_sets_the_formats_and_filename():
    gti = GTI(DF).i_export()
    assert spec_of(gti)["export"] == {
        "formats": ["csv", "clipboard"],
        "filename": "table",
        "code": None,
    }
    # (In the order given, once each)
    assert spec_of(gti.i_export(["clipboard", "csv", "clipboard"]))["export"]["formats"] == [
        "clipboard",
        "csv",
    ]
    assert spec_of(gti.i_export("csv", filename="towny"))["export"] == {
        "formats": ["csv"],
        "filename": "towny",
        "code": None,
    }
    # (Without the extension, which the runtime adds)
    assert gti.i_export(filename="Towny 2021.CSV")._interactive.export_filename == "Towny 2021"
    # (What's not given goes back to its default)
    assert gti.i_export(filename="x").i_export()._interactive.export_filename == "table"


def test_i_export_turns_off():
    gti = GTI(DF).i_export()
    assert spec_of(gti.i_export(None))["export"]["formats"] == []
    assert spec_of(gti.i_export([]))["export"]["formats"] == []


def test_i_export_checks_its_arguments():
    with pytest.raises(ValueError, match='`formats=` must be "csv", "clipboard", "code"'):
        GTI(DF).i_export("xlsx")
    with pytest.raises(ValueError, match="not one with 'json'"):
        GTI(DF).i_export(["csv", "json"])
    with pytest.raises(TypeError, match="`filename=` must be a string"):
        GTI(DF).i_export(filename=1)  # type: ignore[arg-type]
    for empty in ["", " ", ".csv"]:
        with pytest.raises(ValueError, match="`filename=` must name the file"):
            GTI(DF).i_export(filename=empty)


def test_i_export_code_has_what_the_code_needs():
    gti = GTI(DF).i_cols_filter(columns="id", type="facet").i_export(["csv", "code"])
    export = spec_of(gti)["export"]
    assert export["formats"] == ["csv", "code"]
    # (For the columns the view can filter or sort by: a facet's values as Python)
    code = export["code"]
    assert code["backend"] == "pandas"
    assert list(code["columns"]) == ["id", "y"]
    assert code["columns"]["id"]["dtype"] == "string"
    assert code["columns"]["id"]["literals"] == ['"r0"', '"r1"', '"r2"', '"r3"', '"r4"', '"r5"']
    assert code["columns"]["y"] == {"dtype": "other", "nullable": False, "literals": None}


def test_i_export_code_is_for_the_data_library():
    data = {"x": [1.5, 0.0, None], "c": ["a", "b", "a"]}
    for frame, backend in [
        (pl.DataFrame(data, schema_overrides={"c": pl.Categorical}), "polars"),
        (pd.DataFrame(data).astype({"c": "category"}), "pandas"),
        (pa.table(data).set_column(1, "c", pa.array(data["c"]).dictionary_encode()), "narwhals"),
    ]:
        gti = GTI(frame).i_cols_filter(type="facet").i_export("code")
        code = spec_of(gti)["export"]["code"]
        assert code["backend"] == backend
        assert code["columns"]["x"] == {
            "dtype": "float",
            "nullable": False,
            "literals": ["0.0", "1.5"],
        }
        assert code["columns"]["c"] == {
            "dtype": "categorical",
            "nullable": False,
            "literals": ['"a"', '"b"'],
        }


def test_i_export_code_has_python_values():
    frame = pd.DataFrame(
        {
            "n": pd.array([1, None, 3], dtype="Int64"),
            "d": [dt.date(2020, 1, 2), None, dt.date(2020, 1, 2)],
            "t": [dt.datetime(2020, 1, 2, 3, 4), dt.datetime(2021, 1, 1), None],
            "s": ["it's", 'say "hi"', "é"],
            "b": [True, False, True],
            "td": pd.to_timedelta([1, 2, 3], unit="D"),
        }
    )
    gti = GTI(frame).i_cols_filter(columns="n", type="range")
    gti = gti.i_cols_filter(columns=["d", "t", "s", "b", "td"], type="facet").i_export("code")
    columns = spec_of(gti)["export"]["code"]["columns"]
    assert columns["n"] == {"dtype": "other", "nullable": True, "literals": None}
    assert columns["d"]["literals"] == ["datetime.date(2020, 1, 2)"]
    assert columns["t"]["literals"] == [
        "datetime.datetime(2020, 1, 2, 3, 4)",
        "datetime.datetime(2021, 1, 1, 0, 0)",
    ]
    assert columns["s"]["literals"] == ['"it\'s"', '"say \\"hi\\""', '"é"']
    assert columns["b"]["literals"] == ["False", "True"]
    # (Durations, which the code can't have yet)
    assert columns["td"]["literals"] == [None, None, None]


# view state ----


def test_view_state_is_off_by_default():
    assert spec_of(GTI(DF))["view_state"] == {
        "url": False,
        "storage": False,
        "key": None,
        "undo": False,
    }
    assert spec_of(GTI.from_gt(GT(DF, id="t").opt_interactive()))["view_state"] == {
        "url": False,
        "storage": False,
        "key": "t",
        "undo": False,
    }


def test_i_view_state_keeps_the_view_by_the_table_id():
    gti = GTI(DF, id="towny").i_view_state()
    assert spec_of(gti)["view_state"] == {
        "url": True,
        "storage": False,
        "key": "towny",
        "undo": True,
    }
    assert spec_of(gti.i_view_state(url=False, storage=True, undo=False))["view_state"] == {
        "url": False,
        "storage": True,
        "key": "towny",
        "undo": False,
    }
    # (Set with `with_id()`, before or after)
    assert spec_of(GTI(DF).i_view_state().with_id("t"))["view_state"]["key"] == "t"
    # (And turned off)
    assert spec_of(gti.i_view_state(url=False))["view_state"]["url"] is False


def test_i_view_state_needs_a_table_id():
    gti = GTI(DF).i_view_state(url=False, storage=True)
    with pytest.raises(
        ValueError, match=r"`i_view_state\(\)` keeps the reader's view by the table's ID"
    ):
        spec_of(gti)
    with pytest.raises(ValueError, match=r"Give it one with `GTI\(id=\)`"):
        gti.as_raw_html()
    # (Not when it's off, or for undo alone)
    assert (
        spec_of(gti.i_view_state(url=False, storage=False, undo=False))["view_state"]["key"] is None
    )
    assert spec_of(GTI(DF).i_view_state(url=False))["view_state"] == {
        "url": False,
        "storage": False,
        "key": None,
        "undo": True,
    }


def test_i_view_state_checks_its_arguments():
    with pytest.raises(TypeError, match="`url=` must be `True` or `False`"):
        GTI(DF).i_view_state(url="yes")  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="`storage=` must be `True` or `False`"):
        GTI(DF).i_view_state(storage=1)  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="`undo=` must be `True` or `False`"):
        GTI(DF).i_view_state(undo=None)  # type: ignore[arg-type]


def test_i_export_keeps_room_for_the_bar():
    gti = GTI(DF).i_search(False)
    assert gt_table_tag(gti.i_export()) == "<gt-table data-gti-bar>"
    assert gt_table_tag(gti.i_export(None)) == "<gt-table>"


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
