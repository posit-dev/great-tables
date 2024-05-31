import pandas as pd

from great_tables import GT
from great_tables._utils_render_html import create_body_component_h


def assert_rendered_body(snapshot, gt):
    built = gt._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def test_row_group_order(snapshot):
    gt = GT(pd.DataFrame({"g": ["b", "a"], "x": [1, 2], "y": [3, 4]}))

    assert_rendered_body(snapshot, gt)
