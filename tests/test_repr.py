import pytest
import pandas as pd

from great_tables import GT


@pytest.fixture
def gt():
    return GT(pd.DataFrame({"x": [1, 2], "y": [4, 5]}), id="test")


def assert_rendered_html_repr(snapshot, gt):

    html_repr_output = gt._repr_html_()
    assert snapshot == html_repr_output


def test_repr_html_quarto(gt, snapshot):

    import os

    os.environ["QUARTO_BIN_PATH"] = "1"  # Mock the Quarto environment with a non-empty string

    assert_rendered_html_repr(snapshot, gt)


def test_repr_html_databricks(gt, snapshot):

    import os

    os.environ["DATABRICKS_RUNTIME_VERSION"] = "1"  # Mock the Databricks environment

    assert_rendered_html_repr(snapshot, gt)


def test_repr_html_vscode(gt, snapshot):

    import os

    os.environ["VSCODE_PID"] = "1"  # Mock the VSCode environment

    assert_rendered_html_repr(snapshot, gt)
