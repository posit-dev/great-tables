import pytest
from unittest import mock
import pandas as pd
import os

from great_tables import GT

from great_tables._utils_render_latex import (
    get_px_conversion,
    get_units_from_length_string,
    convert_to_px,
    convert_to_pt,
    create_wrap_start_l,
)


@pytest.fixture
def gt_tbl():
    return GT(pd.DataFrame({"x": [1, 2], "y": [4, 5]}), id="test")


def test_get_units_from_length_string():

    assert get_units_from_length_string("12.5pt") == "pt"
    assert get_units_from_length_string("") == "px"


def test_get_px_conversion_val():

    assert get_px_conversion(length="2343.23pt") == 4 / 3
    assert get_px_conversion(length="43.2px") == 1.0


def test_convert_to_px():

    assert convert_to_px("12.5pt") == 17.0
    assert convert_to_px("12.5px") == 12.5


def test_convert_to_pt():

    assert convert_to_pt("16px") == 12.0


@mock.patch.dict(os.environ, {"QUARTO_BIN_PATH": "1"}, clear=True)
def test_create_wrap_start_quarto(gt_tbl: GT):

    assert create_wrap_start_l(gt_tbl) == "\\begin{table}\n"


def test_create_wrap_start_simple_tbl(gt_tbl: GT):

    assert create_wrap_start_l(gt_tbl) == "\\begin{table}[!t]\n"
