import os
import warnings
from contextlib import contextmanager
from unittest.mock import patch

import pytest

from great_tables import GT, exibble
from great_tables._render import infer_render_env, infer_render_env_defaults
from great_tables._render_checks import RenderWarning, _render_check, _render_check_quarto


@contextmanager
def set_quarto_env():
    import os

    orig = os.environ.get("QUARTO_BIN_PATH", None)

    try:
        os.environ["QUARTO_BIN_PATH"] = "1"
        yield
    finally:
        if orig is not None:
            os.environ["QUARTO_BIN_PATH"] = orig
        else:
            del os.environ["QUARTO_BIN_PATH"]


def test_check_quarto_runs():
    gt = GT(exibble).cols_width({"num": "100px"})

    with set_quarto_env(), pytest.warns(RenderWarning):
        assert infer_render_env() == "quarto"
        gt.render("html")


def test_check_quarto_disable_processing():
    gt = GT(exibble).cols_width({"num": "100px"}).tab_options(quarto_disable_processing=True)

    # assert no warning issued
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        _render_check_quarto(gt)


def test_check_quarto_cols_width():
    gt = GT(exibble).cols_width({"num": "100px"})

    with pytest.warns(RenderWarning):
        _render_check_quarto(gt)


def test_infer_render_env_databricks():
    with patch.dict(os.environ, {"DATABRICKS_RUNTIME_VERSION": "1"}, clear=True):
        assert infer_render_env() == "databricks"


def test_infer_render_env_positron():
    with patch.dict(os.environ, {"POSITRON_VERSION": "1"}, clear=True):
        assert infer_render_env() == "positron"


def test_infer_render_env_vscode():
    with patch.dict(os.environ, {"VSCODE_PID": "123"}, clear=True):
        assert infer_render_env() == "vscode"


def test_infer_render_env_default():
    clean_env = {
        k: v
        for k, v in os.environ.items()
        if k
        not in {"QUARTO_BIN_PATH", "DATABRICKS_RUNTIME_VERSION", "POSITRON_VERSION", "VSCODE_PID"}
    }
    with patch.dict(os.environ, clean_env, clear=True):
        with patch("great_tables._render.IPython", create=True) as mock_ipython:
            mock_ipython.get_ipython.return_value = None
            result = infer_render_env()
    assert result == "default"


def test_infer_render_env_ipython_terminal():
    import sys
    from unittest.mock import MagicMock

    clean_env = {
        k: v
        for k, v in os.environ.items()
        if k
        not in {"QUARTO_BIN_PATH", "DATABRICKS_RUNTIME_VERSION", "POSITRON_VERSION", "VSCODE_PID"}
    }

    mock_shell = MagicMock()
    mock_shell.__class__.__name__ = "TerminalInteractiveShell"
    mock_ipython = MagicMock()
    mock_ipython.get_ipython.return_value = mock_shell

    with patch.dict(os.environ, clean_env, clear=True):
        with patch.dict(sys.modules, {"IPython": mock_ipython}):
            result = infer_render_env()
    assert result == "ipython_terminal"


def test_infer_render_env_defaults_returns_dict():
    result = infer_render_env_defaults()
    assert "make_page" in result
    assert "all_important" in result


def test_render_check_runs_quarto_check():
    gt = GT(exibble).cols_width({"num": "100px"})
    with set_quarto_env(), pytest.warns(RenderWarning):
        _render_check(gt)
