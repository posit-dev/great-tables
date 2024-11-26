import pytest
from unittest import mock
import pandas as pd
import os

from great_tables import GT
from great_tables._render import infer_render_env


@pytest.fixture
def gt():
    return GT(pd.DataFrame({"x": [1, 2], "y": [4, 5]}), id="test")


def assert_rendered_html_repr(snapshot, gt):
    html_repr_output = gt._repr_html_()
    assert snapshot == html_repr_output


@mock.patch.dict(os.environ, {"QUARTO_BIN_PATH": "1"}, clear=True)
def test_repr_html_quarto(gt, snapshot):
    assert infer_render_env() == "quarto"

    assert_rendered_html_repr(snapshot, gt)


@mock.patch.dict(os.environ, {"DATABRICKS_RUNTIME_VERSION": "1"}, clear=True)
def test_repr_html_databricks(gt, snapshot):
    assert infer_render_env() == "databricks"

    assert_rendered_html_repr(snapshot, gt)


@mock.patch.dict(os.environ, {"VSCODE_PID": "1"}, clear=True)
def test_repr_html_vscode(gt, snapshot):
    assert infer_render_env() == "vscode"

    assert_rendered_html_repr(snapshot, gt)


@mock.patch.dict(os.environ, {"POSITRON_VERSION": "1"}, clear=True)
def test_repr_html_positron(gt, snapshot):
    assert infer_render_env() == "positron"

    assert_rendered_html_repr(snapshot, gt)


def test_repr_html_default(gt, snapshot):
    assert infer_render_env() == "default"

    assert_rendered_html_repr(snapshot, gt)
