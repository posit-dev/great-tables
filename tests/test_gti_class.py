from __future__ import annotations

import re

import numpy as np
import pandas as pd
import pytest

from great_tables import GT, GTI, exibble
from great_tables._gti import build_spec
from great_tables._gti._render import _load_runtime

DF = pd.DataFrame({"id": [f"r{i}" for i in range(6)], "y": [10, 20, 30, 40, 50, 60]})


def spec_of(gt: GT) -> dict:
    return build_spec(gt._build_data(context="html"))


def interactive_of(gt: GT) -> dict:
    spec = spec_of(gt)
    return {key: spec[key] for key in ("controls", "pagination", "display", "layout")}


GTI_DEFAULTS = {
    "controls": {"sorting": True, "search": True, "resizing": True, "selection": None},
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
        f'<gt-table data-gti-scroll style="--gt-i-height: {expected}">'
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
    assert gti.as_raw_html().startswith("<gt-table data-gti-nowrap>")


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
    assert html.startswith("<gt-table>\n")
    assert css in html and js in html


def test_as_raw_html_make_page():
    html = GTI(DF).as_raw_html(make_page=True)
    assert html.startswith('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    assert '<meta name="viewport" content="width=device-width, initial-scale=1"/>' in html
    assert "<body>\n<gt-table>\n" in html
    assert html.endswith("</body>\n</html>\n")


def test_as_raw_html_all_important():
    assert "!important" not in GTI(DF, id="t").as_raw_html().split("<style>\n", 2)[1]
    html = GTI(DF, id="t").as_raw_html(all_important=True)
    assert re.search(r"#t \.gt_row {[^}]*?!important", html)


def test_as_raw_html_inline_css_is_not_available():
    with pytest.raises(ValueError, match="can't have its CSS inlined"):
        GTI(DF).as_raw_html(inline_css=True)


def test_repr_html_is_interactive():
    assert "<gt-table>" in GTI(DF)._repr_html_()


def test_write_raw_html(tmp_path):
    GTI(DF).write_raw_html(tmp_path / "gti.html", make_page=True)
    GT(DF).write_raw_html(tmp_path / "gt.html")

    assert "<gt-table>" in (tmp_path / "gti.html").read_text(encoding="utf-8")
    assert "<gt-table" not in (tmp_path / "gt.html").read_text(encoding="utf-8")


@pytest.mark.parametrize("method", ["save", "gtsave", "as_latex"])
def test_static_output_is_not_available(method: str, tmp_path):
    with pytest.raises(TypeError, match="interactive HTML only"):
        getattr(GTI(DF), method)(tmp_path / "table.png")


def test_opt_interactive_is_not_available():
    with pytest.raises(TypeError, match="`i_` methods"):
        GTI(DF).opt_interactive(use_search=True)


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
