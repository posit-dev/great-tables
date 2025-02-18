import warnings

import pytest

from contextlib import contextmanager
from great_tables import GT, exibble
from great_tables._render import infer_render_env
from great_tables._render_checks import RenderWarning, _render_check_quarto


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
