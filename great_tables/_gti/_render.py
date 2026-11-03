from __future__ import annotations

import json
from html import escape
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Literal

from .._gt_data import ColInfoTypeEnum, Options
from ._query import js_trim
from ._settings import settings_of
from ._spec import Spec, build_spec

if TYPE_CHECKING:
    from ..gt import GT

JS_DIR = Path(__file__).parent.parent / "js"

# A compact table's rows' vertical padding, half of GT's default
COMPACT_PADDING = {
    "data_row_padding": "4px",
    "summary_row_padding": "4px",
    "grand_summary_row_padding": "4px",
    "row_group_padding": "4px",
}


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


def render_gti_html(
    gt: GT, runtime: Literal["inline", "none"] = "inline", all_important: bool = False
) -> str:
    """Render a table as a `<gt-table>` element: GT's static HTML, plus its spec.

    With `runtime="inline"`, the runtime's CSS and JS follow the element (they register
    `<gt-table>` only once per page, however often they're included); with `runtime="none"`, the
    page must provide them. With `all_important=True`, the table's CSS (not the runtime's) is
    marked `!important`, as with `as_raw_html()`.
    """
    table_html, spec = render_parts(gt, all_important=all_important)
    spec_json = spec_to_script_json(spec)

    # (The runtime sets these too, but the table shouldn't change when it's hydrated; nor should
    # what's below it, so the control bar's room is kept until it's there)
    attrs = " data-gti-bar" if _has_bar(spec) else ""
    if attrs and _has_tokens(spec):
        attrs += " data-gti-tokens"
    if not spec["display"]["wrap"]:
        attrs += " data-gti-nowrap"
    height = spec["layout"]["height"]
    if height is not None:
        attrs += f' data-gti-scroll style="--gt-i-height: {escape(height)}"'
    html = (
        f"<gt-table{attrs}>\n{table_html}"
        f'<script type="application/json" data-gti-spec>{spec_json}</script>\n'
        "</gt-table>\n"
    )

    if runtime == "inline":
        js, css = _load_runtime()
        html += f"<style>\n{css}</style>\n<script>\n{js}</script>\n"
    elif runtime != "none":
        raise ValueError(f'`runtime=` must be "inline" or "none", not {runtime!r}.')

    return html


def render_parts(gt: GT, all_important: bool = False) -> tuple[str, Spec]:
    """A table's static HTML (its `<div>`) and its spec."""
    settings = settings_of(gt)
    if settings.compact:
        gt = _compact(gt)
    gt = _leave_out(gt, settings.query_only)
    built = gt._build_data(context="html")
    return built._render_as_html(all_important=all_important), build_spec(built)


def _has_bar(spec: Spec) -> bool:
    """Whether the runtime draws a control bar below the table: for a search, filters, pages, or
    an export.

    (Or pages there could be: the page sizes readers can choose from, in the bar's info panel,
    include the table's own. With filters, the bar's info panel says how many rows they leave.)
    """
    controls, pagination = spec["controls"], spec["pagination"]
    sizes = [pagination["page_size"]]
    if pagination["size_select"]:
        sizes += pagination["page_sizes"]
    paged = pagination["enabled"] and spec["nrows"] > min(sizes)
    return controls["bar"] and (
        controls["search"] or bool(spec["filters"]) or bool(spec["export"]["formats"]) or paged
    )


def _has_tokens(spec: Spec) -> bool:
    """Whether the bar starts with a line of tokens: for a view with a filter that's on.

    (A filter is off with blank text, which the runtime trims as JavaScript does.)
    """
    view = spec.get("view")
    clauses = (view["filter"] or {"and": []})["and"] if view is not None else []
    return any(c["op"] != "contains" or js_trim(c["value"]) != "" for c in clauses)


def _leave_out(gt: GT, columns: tuple[str, ...]) -> GT:
    """Hide the columns only for querying, as `cols_hide()` does (their spec has them still).

    This is checked here, as the stub and the row group column may have been set after
    `i_cols_controls()`.
    """
    if not columns:
        return gt
    boxhead = gt._boxhead
    kept = [
        column
        for kind in (ColInfoTypeEnum.stub, ColInfoTypeEnum.row_group)
        for column in boxhead.vars_from_type(kind)
        if column in columns
    ]
    if kept:
        raise ValueError(
            "The stub and the row group column can't be left out of the table, so "
            f"`display=False` can't be set for {', '.join(map(repr, kept))}."
        )
    boxhead = boxhead.set_cols_hidden(list(columns))
    if not boxhead._get_default_columns() and not boxhead._get_stub_columns():
        raise ValueError(
            "A table without a stub can't have every column left out of it with " "`display=False`."
        )
    return gt._replace(_boxhead=boxhead)


def _compact(gt: GT) -> GT:
    """Halve the rows' vertical padding, where the author left it at GT's default."""
    defaults = Options()
    padding = {
        name: value
        for name, value in COMPACT_PADDING.items()
        if getattr(gt._options, name).value == getattr(defaults, name).value
    }
    return gt.tab_options(**padding) if padding else gt
