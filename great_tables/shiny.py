from __future__ import annotations

__all__ = (
    "output_gt",
    "render_gt",
)

from great_tables import GT
from shiny.render.transformer import (
    output_transformer,
    TransformerMetadata,
    ValueFn,
    resolve_value_fn,
)
from shiny.session._utils import RenderedDeps
from shiny._namespaces import resolve_id

from htmltools import Tag, div, HTML


def output_gt(id: str, placeholder: bool = False) -> Tag:
    """Output UI for a great_tables table."""
    return div({"class": "shiny-html-output"}, id=resolve_id(id))


@output_transformer(default_ui=output_gt)
async def GtTransformer(_meta: TransformerMetadata, _fn: ValueFn[GT | None]) -> RenderedDeps | None:
    value = await resolve_value_fn(_fn)
    if value is None:
        return None
    elif isinstance(value, GT):
        return _meta.session._process_ui(HTML(value._repr_html_()))

    raise TypeError(f"Expected a great_tables.GT object, got {type(value)}")


@overload
def render_gt() -> GtTransformer.OutputRendererDecorator:
    ...

@overload
def render_gt(_fn: GtTransformer.ValueFn) -> GtTransformer.OutputRenderer:
    ...

def render_gt(
    _fn: GtTransformer.ValueFn | None = None,
) -> GtTransformer.OutputRenderer | GtTransformer.OutputRendererDecorator:
    """Render a great_tables table."""

    return GtTransformer(_fn)
