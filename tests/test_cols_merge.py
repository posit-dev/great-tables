import pandas as pd
import pytest
from great_tables import GT
from great_tables._gt_data import ColMergeInfo


@pytest.fixture
def simple_df():
    return pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})


@pytest.fixture
def missing_df():
    return pd.DataFrame(
        {
            "number": ["Three", "Four", "Five"],
            "val1": [10, 20, 30],
            "val2": [15.0, 25.0, None],
            "val3": [5.0, None, None],
        }
    )


def test_cols_merge_basic(simple_df: pd.DataFrame):
    gt = GT(simple_df).cols_merge(columns=["a", "b"])

    # Check that merge was registered
    assert len(gt._col_merge) == 1
    assert gt._col_merge[0].vars == ["a", "b"]
    assert gt._col_merge[0].pattern == "{1} {2}"
    assert gt._col_merge[0].type == "merge"

    # Check rendered output
    html = gt.as_raw_html()
    assert "1 4" in html
    assert "2 5" in html
    assert "3 6" in html


def test_cols_merge_custom_pattern(simple_df: pd.DataFrame):
    gt = GT(simple_df).cols_merge(columns=["a", "b"], pattern="{1}—{2}")

    assert gt._col_merge[0].pattern == "{1}—{2}"

    # Check rendered output with em dash
    html = gt.as_raw_html()
    assert "1—4" in html
    assert "2—5" in html
    assert "3—6" in html


def test_cols_merge_three_columns(simple_df: pd.DataFrame):
    gt = GT(simple_df).cols_merge(columns=["a", "b", "c"])

    assert gt._col_merge[0].vars == ["a", "b", "c"]
    assert gt._col_merge[0].pattern == "{1} {2} {3}"

    # Check rendered output with three columns
    html = gt.as_raw_html()
    assert "1 4 7" in html
    assert "2 5 8" in html
    assert "3 6 9" in html


def test_cols_merge_subset_of_columns(simple_df: pd.DataFrame):
    # Provide three columns but only use first two in the pattern
    gt1 = GT(simple_df).cols_merge(columns=["a", "b", "c"], pattern="{1} {2}")

    html1 = gt1.as_raw_html()
    assert "1 4" in html1
    assert "2 5" in html1
    assert "3 6" in html1

    # Provide three columns but only use first and third in the pattern
    gt2 = GT(simple_df).cols_merge(columns=["a", "b", "c"], pattern="{1} {3}")

    html2 = gt2.as_raw_html()
    assert "1 7" in html2
    assert "2 8" in html2
    assert "3 9" in html2

    # Provide three columns but only use the third in the pattern
    gt3 = GT(simple_df).cols_merge(columns=["a", "b", "c"], pattern="Value: {3}")

    html3 = gt3.as_raw_html()
    assert "Value: 7" in html3
    assert "Value: 8" in html3
    assert "Value: 9" in html3


def test_cols_merge_hiding_default(simple_df: pd.DataFrame):
    gt = GT(simple_df).cols_merge(columns=["a", "b", "c"])

    built = gt._build_data(context="html")

    # Check visibility in boxhead
    col_a = [col for col in built._boxhead if col.var == "a"][0]
    col_b = [col for col in built._boxhead if col.var == "b"][0]
    col_c = [col for col in built._boxhead if col.var == "c"][0]

    assert col_a.visible
    assert not col_b.visible
    assert not col_c.visible


def test_cols_merge_hiding_false(simple_df: pd.DataFrame):
    gt = GT(simple_df).cols_merge(columns=["a", "b"], hide_columns=False)

    built = gt._build_data(context="html")

    col_a = [col for col in built._boxhead if col.var == "a"][0]
    col_b = [col for col in built._boxhead if col.var == "b"][0]

    assert col_a.visible
    assert col_b.visible


def test_cols_merge_specific_rows(simple_df: pd.DataFrame):
    gt = GT(simple_df).cols_merge(columns=["a", "b"], rows=[0, 2], pattern="{1}-{2}")

    assert gt._col_merge[0].rows == [0, 2]

    html = gt.as_raw_html()

    # Check that only rows 0 and 2 are merged
    assert "1-4" in html  # Row 0
    assert "2-5" not in html  # Row 1 (not merged)
    assert "3-6" in html  # Row 2


def test_cols_merge_multiple_operations(simple_df: pd.DataFrame):
    gt = (
        GT(simple_df)
        .cols_merge(columns=["a", "b"], pattern="{1}+{2}")
        .cols_merge(columns=["a", "c"], pattern="{1}*{2}")
    )

    assert len(gt._col_merge) == 2
    assert gt._col_merge[0].pattern == "{1}+{2}"
    assert gt._col_merge[1].pattern == "{1}*{2}"

    html = gt.as_raw_html()

    # Check that the second merge uses the result of the first merge
    assert "1+4*7" in html
    assert "2+5*8" in html
    assert "3+6*9" in html


def test_cols_merge_with_missing_values(missing_df: pd.DataFrame):
    gt = GT(missing_df).cols_merge(columns=["val1", "val2"], pattern="{1}<< ({2})>>")

    html = gt.as_raw_html()
    assert "10 (15.0)" in html or "10.0 (15.0)" in html
    assert "20 (25.0)" in html or "20.0 (25.0)" in html
    assert "30<" in html or "30.0<" in html  # The '<' is part of the closing tag (missing val2)


def test_cols_merge_nested_conditionals(missing_df: pd.DataFrame):
    gt = GT(missing_df).cols_merge(
        columns=["val1", "val2", "val3"], pattern="{1}<< ({2}-<<{3}>>)>>"
    )

    html = gt.as_raw_html()

    assert "10 (15.0-5.0)" in html or "10.0 (15.0-5.0)" in html
    assert "20 (25.0-)" in html or "20.0 (25.0-)" in html
    assert "30<" in html or "30.0<" in html


def test_cols_merge_minimum_columns_error(simple_df: pd.DataFrame):
    with pytest.raises(ValueError, match="At least two columns"):
        GT(simple_df).cols_merge(columns=["a"])


def test_cols_merge_invalid_pattern_reference(simple_df: pd.DataFrame):
    gt = GT(simple_df).cols_merge(columns=["a", "b"], pattern="{1} {2} {3}")

    with pytest.raises(ValueError, match="Pattern references column"):
        gt._repr_html_()


def test_cols_merge_zero_based_index_error(simple_df: pd.DataFrame):
    gt = GT(simple_df).cols_merge(columns=["a", "b"], pattern="{0}-{1}")

    # Should raise error because pattern uses 1-based indexing, not 0-based
    with pytest.raises(ValueError, match="column indexing starts at"):
        gt._repr_html_()


def test_cols_merge_preserves_formatting(simple_df: pd.DataFrame):
    gt = (
        GT(simple_df)
        .fmt_number(columns="a", decimals=3)
        .cols_merge(columns=["a", "b"], pattern="{1}+{2}")
    )

    html = gt.as_raw_html()

    assert "1.000+4" in html
    assert "2.000+5" in html
    assert "3.000+6" in html


def test_col_merge_info_creation():
    info = ColMergeInfo(vars=["a", "b"], rows=[0, 1, 2], type="merge", pattern="{1} {2}")

    assert info.vars == ["a", "b"]
    assert info.rows == [0, 1, 2]
    assert info.type == "merge"
    assert info.pattern == "{1} {2}"


def test_col_merge_info_pattern_optional():
    info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern=None)

    assert info.pattern is None


def test_cols_merge_with_sub_missing(missing_df: pd.DataFrame):
    # calling sub_missing() before cols_merge()
    gt_1 = (
        GT(missing_df)
        .sub_missing(columns=["val2", "val3"], missing_text="--")
        .cols_merge(columns=["val1", "val2", "val3"], pattern="{1}<< to {2}<< to {3}>>>>")
    )

    # calling sub_missing() after cols_merge()
    gt_2 = (
        GT(missing_df)
        .cols_merge(columns=["val1", "val2", "val3"], pattern="{1}<< to {2}<< to {3}>>>>")
        .sub_missing(columns=["val2", "val3"], missing_text="--")
    )

    # From both approaches, we should get the same output
    html_1 = gt_1.as_raw_html()
    html_2 = gt_2.as_raw_html()

    # Row 0: All values are present (none are missing values)
    assert "10 to 15.0 to 5.0" in html_1
    assert "10 to 15.0 to 5.0" in html_2

    # Row 1: val3 was None, but sub_missing() replaced it with "--" so that "--"
    # should be included (it's treated as a non-missing value because of sub_missing())
    assert "20 to 25.0 to --" in html_1
    assert "20 to 25.0 to --" in html_2

    # Row 2: val2 and val3 were None, both replaced with "--" by sub_missing() so both of
    # the "--" values should be included in the output
    assert "30 to -- to --" in html_1
    assert "30 to -- to --" in html_2
