from math import nan

import numpy as np
import pandas as pd
import polars as pl
import polars.testing
import pytest
from great_tables import GT
from great_tables._gt_data import FormatterSkipElement
from great_tables._substitution import SubMissing, SubZero
from great_tables._tbl_data import DataFrameLike, to_list

params_frames = [pytest.param(pd.DataFrame, id="pandas"), pytest.param(pl.DataFrame, id="polars")]


@pytest.fixture(params=params_frames, scope="function")
def df(request) -> DataFrameLike:
    return request.param({"col1": [None, nan, 0]})


@pytest.fixture(params=params_frames, scope="function")
def df_empty(request) -> DataFrameLike:
    return request.param()


def assert_frame_equal(src: DataFrameLike, target: DataFrameLike):
    if isinstance(src, pd.DataFrame):
        pd.testing.assert_frame_equal(src, target)
    elif isinstance(src, pl.DataFrame):
        pl.testing.assert_frame_equal(src, target)
    else:
        raise NotImplementedError(f"Unsupported data type: {type(src)}")


def assert_series_equals(src, target: list):
    # polars is kind and converts its null type to None, but
    # pandas needs the NA -> None to be done manually.
    fixed = [None if x is pd.NA else x for x in to_list(src)]
    assert fixed == target


@pytest.mark.parametrize("el", [None, nan, np.nan])
def test_sub_missing_el(df_empty: DataFrameLike, el):
    # df just being used as constructor
    assert SubMissing(df_empty, "---").to_html(el) == "---"


def test_sub_missing_el_skip(df_empty: DataFrameLike):
    assert isinstance(SubMissing(df_empty, "---").to_html(0), FormatterSkipElement)


def test_sub_missing_meth(df):
    new_gt = GT(df).sub_missing("col1", missing_text="--")._render_formats("html")
    assert_series_equals(new_gt._body.body["col1"], ["--", "--", None])


@pytest.mark.parametrize("el", [0, 0.0])
def test_sub_zero_el(el):
    assert SubZero("--").to_html(el) == "--"


def test_sub_zero_el_skip():
    assert isinstance(SubZero("--").to_html(1), FormatterSkipElement)


def test_sub_zero_meth(df):
    new_gt = GT(df).sub_zero("col1", zero_text="no")._render_formats("html")
    assert_series_equals(new_gt._body.body["col1"], [None, None, "no"])
