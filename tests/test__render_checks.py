import warnings

import pytest

from great_tables import GT, exibble
from great_tables._render_checks import RenderWarning, _render_check_quarto


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
