import asyncio
import warnings

import pytest
import polars as pl

from great_tables import GT
from great_tables.shiny import output_gt, render_gt


def test_output_gt_returns_tag():
    tag = output_gt("my_id")
    tag_str = str(tag)
    assert "shiny-html-output" in tag_str
    assert "my_id" in tag_str


def test_output_gt_class_attribute():
    tag = output_gt("my_id")
    assert "shiny-html-output" in str(tag)


def test_output_gt_no_placeholder_no_warning():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        output_gt("my_id")


@pytest.mark.parametrize("placeholder", [True, False])
def test_output_gt_placeholder_deprecated(placeholder: bool):
    with pytest.warns(
        FutureWarning, match="`placeholder` argument of `output_gt\\(\\)` is deprecated"
    ):
        tag = output_gt("my_id", placeholder=placeholder)

    # The argument has no effect on the output
    assert str(tag) == str(output_gt("my_id"))


def test_render_gt_callable():
    # render_gt() with no args returns a decorator
    decorator = render_gt()
    assert callable(decorator)


def test_render_gt_with_fn():
    df = pl.DataFrame({"x": [1, 2, 3]})

    @render_gt
    async def my_table():
        return GT(df)

    assert my_table is not None


def test_gt_transformer_exists():
    # GtTransformer is the output transformer object that wraps the async rendering logic
    from great_tables.shiny import GtTransformer

    assert GtTransformer is not None
