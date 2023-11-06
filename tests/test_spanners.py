from great_tables._spanners import spanners_print_matrix, empty_spanner_matrix
from great_tables._gt_data import Spanners, SpannerInfo, Boxhead, ColInfo


# TODO: test arguments


def test_spanners_print_matrix():
    spanners = Spanners(
        [
            SpannerInfo(spanner_id="a", spanner_level=0, vars=["col1"], built="A"),
            SpannerInfo(spanner_id="b", spanner_level=1, vars=["col2"], built="B"),
        ]
    )

    boxhead = Boxhead(
        [
            ColInfo(var="col1"),
            ColInfo(var="col2"),
            ColInfo(var="col3"),
        ]
    )

    mat, vars = spanners_print_matrix(spanners, boxhead)
    assert vars == ["col1", "col2", "col3"]
    assert mat == [
        {"col1": None, "col2": "B", "col3": None},
        {"col1": "A", "col2": None, "col3": None},
        {"col1": "col1", "col2": "col2", "col3": "col3"},
    ]


def test_empty_spanner_matrix():
    mat, vars = empty_spanner_matrix(["a", "b"], omit_columns_row=False)

    assert vars == ["a", "b"]
    assert mat == [{"a": "a", "b": "b"}]


def test_empty_spanner_matrix_arg_omit_columns_row():
    mat, vars = empty_spanner_matrix(["a", "b"], omit_columns_row=False)

    assert vars == ["a", "b"]
    assert mat == []
