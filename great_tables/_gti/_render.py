from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Literal

from ._spec import Spec, build_spec

if TYPE_CHECKING:
    from ..gt import GT

JS_DIR = Path(__file__).parent.parent / "js"


@lru_cache(maxsize=None)
def _load_runtime() -> tuple[str, str]:
    """The built `<gt-table>` runtime (see packages/gti): its JS and CSS."""
    js = (JS_DIR / "gti.js").read_text(encoding="utf-8")
    css = (JS_DIR / "gti.css").read_text(encoding="utf-8")
    return js, css


def spec_to_script_json(spec: Spec) -> str:
    """Serialize a spec for a `<script type="application/json">` element.

    `<`, `>` and `&` are escaped (as JSON `\\u` escapes, which only occur inside strings), so a
    value can't close the element (`</script>`) or open a comment.
    """
    text = json.dumps(spec, ensure_ascii=False, allow_nan=False, separators=(",", ":"))
    return text.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


def render_gti_html(gt: GT, runtime: Literal["inline", "none"] = "inline") -> str:
    """Render a table as a `<gt-table>` element: GT's static HTML, plus its spec.

    With `runtime="inline"`, the runtime's CSS and JS follow the element (they register
    `<gt-table>` only once per page, however often they're included); with `runtime="none"`, the
    page must provide them.
    """
    built = gt._build_data(context="html")
    table_html = built._render_as_html()
    spec_json = spec_to_script_json(build_spec(built))

    html = (
        f"<gt-table>\n{table_html}"
        f'<script type="application/json" data-gti-spec>{spec_json}</script>\n'
        "</gt-table>\n"
    )

    if runtime == "inline":
        js, css = _load_runtime()
        html += f"<style>\n{css}</style>\n<script>\n{js}</script>\n"
    elif runtime != "none":
        raise ValueError(f'`runtime=` must be "inline" or "none", not {runtime!r}.')

    return html
