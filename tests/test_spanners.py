import pytest

from great_tables._spanners import spanners_print_matrix, empty_spanner_matrix
from great_tables._gt_data import Spanners, SpannerInfo, Boxhead, ColInfo, ColInfoTypeEnum


@pytest.fixture
def spanners():
    return Spanners(
        [
            SpannerInfo(spanner_id="a", spanner_level=0, vars=["col1"], built="A"),
            SpannerInfo(spanner_id="b", spanner_level=1, vars=["col2"], built="B"),
        ]
    )


@pytest.fixture
def boxhead():
    return Boxhead(
        [
            ColInfo(var="col1"),
            ColInfo(var="col2"),
            ColInfo(var="col3"),
            ColInfo(var="col4", type=ColInfoTypeEnum.hidden),
        ]
    )


def test_spanners_print_matrix(spanners, boxhead):
    mat, vars = spanners_print_matrix(spanners, boxhead)
    assert vars == ["col1", "col2", "col3"]
    assert mat == [
        {"col1": None, "col2": "B", "col3": None},
        {"col1": "A", "col2": None, "col3": None},
        {"col1": "col1", "col2": "col2", "col3": "col3"},
    ]


def test_spanners_print_matrix_arg_omit_columns_row(spanners, boxhead):
    mat, vars = spanners_print_matrix(spanners, boxhead, omit_columns_row=True)
    assert vars == ["col1", "col2", "col3"]
    assert mat == [
        {"col1": None, "col2": "B", "col3": None},
        {"col1": "A", "col2": None, "col3": None},
    ]


def test_spanners_print_matrix_arg_include_hidden(spanners, boxhead):
    mat, vars = spanners_print_matrix(spanners, boxhead, include_hidden=True)
    assert vars == ["col1", "col2", "col3", "col4"]
    assert mat == [
        {"col1": None, "col2": "B", "col3": None, "col4": None},
        {"col1": "A", "col2": None, "col3": None, "col4": None},
        {"col1": "col1", "col2": "col2", "col3": "col3", "col4": "col4"},
    ]


def test_empty_spanner_matrix():
    mat, vars = empty_spanner_matrix(["a", "b"], omit_columns_row=False)

    assert vars == ["a", "b"]
    assert mat == [{"a": "a", "b": "b"}]


def test_empty_spanner_matrix_arg_omit_columns_row():
    mat, vars = empty_spanner_matrix(["a", "b"], omit_columns_row=True)

    assert vars == ["a", "b"]
    assert mat == []
