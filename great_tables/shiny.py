from __future__ import annotations

__all__ = (
    "output_gt",
    "render_gt",
)

from .gt import GT
from htmltools import Tag, HTML

try:
    from shiny.render.transformer import (
        output_transformer,
        TransformerMetadata,
        ValueFn,
        resolve_value_fn,
    )
    from shiny.ui import output_ui
except ImportError:
    raise ImportError(
        "The great_tables.shiny module requires the shiny package to be installed."
        " Please install it with this command:"
        "\n\n    pip install shiny"
    )

from typing import TYPE_CHECKING, overload

if TYPE_CHECKING:
    from shiny.session._utils import RenderedDeps


def output_gt(id: str, placeholder: bool = False) -> Tag:
    """Output UI for a great_tables table.

    Parameters
    ----------
    id:
        An output id.
    placeholder:
        If ``True``, forward a placeholder attribute onto the Shiny HTML output
        container so an empty box can be shown before the table arrives.
    """
    return output_ui(id, placeholder=placeholder)


@output_transformer(default_ui=output_gt)
async def GtTransformer(_meta: TransformerMetadata, _fn: ValueFn[GT | None]) -> RenderedDeps | None:
    value = await resolve_value_fn(_fn)
    if value is None:
        return None
    elif isinstance(value, GT):
        return _meta.session._process_ui(HTML(value._repr_html_()))

    raise TypeError(f"Expected a great_tables.GT object, got {type(value)}")


@overload
def render_gt() -> GtTransformer.OutputRendererDecorator: ...


@overload
def render_gt(_fn: GtTransformer.ValueFn) -> GtTransformer.OutputRenderer: ...


def render_gt(
    _fn: GtTransformer.ValueFn | None = None,
) -> GtTransformer.OutputRenderer | GtTransformer.OutputRendererDecorator:
    """Render a great_tables table."""

    return GtTransformer(_fn)
