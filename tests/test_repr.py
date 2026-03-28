import json
import os
from unittest import mock

import pandas as pd
import pytest

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


def _make_quarto_execute_info(tmp_path, pandoc_to):
    """Create a QUARTO_EXECUTE_INFO JSON file mimicking Quarto's execution context."""
    info = {"format": {"pandoc": {"to": pandoc_to}}}
    info_file = tmp_path / "execute-info.json"
    info_file.write_text(json.dumps(info))
    return str(info_file)


def test_repr_html_quarto_typst(gt, tmp_path):
    """When Quarto renders to Typst, _repr_html_ should emit a raw Typst block."""
    import great_tables.quarto as quarto_mod

    info_path = _make_quarto_execute_info(tmp_path, "typst")

    # Reset the cached value so our test file is read
    quarto_mod._quarto_pandoc_to = None

    with mock.patch.dict(
        os.environ,
        {"QUARTO_BIN_PATH": "1", "QUARTO_EXECUTE_INFO": info_path},
        clear=True,
    ):
        assert quarto_mod.is_quarto_typst_render()

        bundle, _ = gt._repr_mimebundle_()
        assert "text/markdown" in bundle
        result = bundle["text/markdown"]
        assert "```{=typst}" in result
        assert "#table(" in result

    # Clean up cache
    quarto_mod._quarto_pandoc_to = None


def test_repr_html_quarto_html(gt, snapshot, tmp_path):
    """When Quarto renders to HTML, _repr_html_ should emit normal HTML."""
    import great_tables.quarto as quarto_mod

    info_path = _make_quarto_execute_info(tmp_path, "html")

    quarto_mod._quarto_pandoc_to = None

    with mock.patch.dict(
        os.environ,
        {"QUARTO_BIN_PATH": "1", "QUARTO_EXECUTE_INFO": info_path},
        clear=True,
    ):
        assert not quarto_mod.is_quarto_typst_render()
        assert_rendered_html_repr(snapshot, gt)

    quarto_mod._quarto_pandoc_to = None
