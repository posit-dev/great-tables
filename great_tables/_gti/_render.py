from __future__ import annotations

import json
import re
import warnings
from html import escape, unescape
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Literal

from .._gt_data import ColInfoTypeEnum, Options
from .._render_checks import RenderWarning
from .._text import _process_text
from .._utils_render_html import _get_header_ids
from ._details import details_template, leave_out_details_column, render_details
from ._query import js_trim, label_text
from ._settings import settings_of
from ._spec import Spec, build_spec

if TYPE_CHECKING:
    from .._gt_data import GTData
    from ..gt import GT

JS_DIR = Path(__file__).parent.parent / "js"

# A compact table's rows' vertical padding, half of GT's default
COMPACT_PADDING = {
    "data_row_padding": "4px",
    "summary_row_padding": "4px",
    "grand_summary_row_padding": "4px",
    "row_group_padding": "4px",
}

# The most data columns an "auto" table shows and is still stacked (in a narrow container)
STACK_COLUMNS = 6

# What a stacked table's CSS template (gti-stack.css) has for the table's ID and stacking width
STACK_ROOT = "#gt-i-table"
STACK_WIDTH = "(width < 420px)"

# The most data rows, bytes of HTML (the `<gt-table>` element's), and rows shown at once (on a
# page, or all of them, on one) a table has before it's warned about, as it may be slow in the
# browser (see the Phase 1 benchmarks, in packages/gti/bench)
MAX_ROWS = 3_000
MAX_BYTES = 10 * 2**20
MAX_SHOWN = 1_000


class GTISizeWarning(RenderWarning):
    """A warning that an interactive table may be slow in the browser, for its size."""


@lru_cache(maxsize=None)
def _load_runtime() -> tuple[str, str]:
    """The built `<gt-table>` runtime (see packages/gti): its JS and CSS."""
    js = (JS_DIR / "gti.js").read_text(encoding="utf-8")
    css = (JS_DIR / "gti.css").read_text(encoding="utf-8")
    return js, css


@lru_cache(maxsize=None)
def _load_stack_css() -> str:
    """The template of a stacked table's own CSS (see packages/gti/src/stack.css)."""
    return (JS_DIR / "gti-stack.css").read_text(encoding="utf-8")


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
    built = _build(gt)
    table_html = built._render_as_html(all_important=all_important)
    details = render_details(built)
    spec = build_spec(built, details=sorted(details))
    spec_json = spec_to_script_json(spec)

    # (The runtime sets these too, but the table shouldn't change when it's hydrated; nor should
    # what's below it, so the control bar's room is kept until it's there)
    attrs = " data-gti-bar" if _has_bar(spec) else ""
    if attrs and _has_tokens(spec):
        attrs += " data-gti-tokens"
    if not spec["display"]["wrap"]:
        attrs += " data-gti-nowrap"
    height = spec["layout"]["height"]
    responsive = spec["layout"]["responsive"]
    # (An "auto" table whose columns have priorities drops them, rather than being stacked)
    if responsive == "auto" and any(column["priority"] for column in spec["columns"]):
        responsive = "collapse"
    if responsive in ("stack", "auto"):
        attrs += " data-gti-stack"
        # (Until the runtime counts the columns shown, as the reader hides them)
        if responsive == "auto" and _shown_columns(spec) > STACK_COLUMNS:
            attrs += " data-gti-stack-off"
        table_html += f"<style>\n{stack_css(built, spec, table_html)}</style>\n"
    # (Each row's details, inert until the reader opens them, and not shown without the runtime)
    table_html += "".join(details_template(row, html) for row, html in details.items())
    if height is not None:
        attrs += f' data-gti-scroll style="--gt-i-height: {escape(height)}"'
    html = (
        f"<gt-table{attrs}>\n{table_html}"
        f'<script type="application/json" data-gti-spec>{spec_json}</script>\n'
        "</gt-table>\n"
    )
    _warn_size(gt, spec, html)

    if runtime == "inline":
        js, css = _load_runtime()
        html += f"<style>\n{css}</style>\n<script>\n{js}</script>\n"
    elif runtime != "none":
        raise ValueError(f'`runtime=` must be "inline" or "none", not {runtime!r}.')

    return html


def page_html(fragment: str) -> str:
    """A whole page, with a table's HTML (as `render_gti_html()` makes it) as its body."""
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8"/>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1"/>\n'
        f"</head>\n<body>\n{fragment}</body>\n</html>\n"
    )


def _warn_size(gt: GT, spec: Spec, html: str) -> None:
    """Warn if the table may be slow in the browser: with more data rows than `MAX_ROWS` or more
    bytes of HTML (its `<gt-table>` element's) than `MAX_BYTES`, as it's slow to load, or with
    more rows shown at once than `MAX_SHOWN`, as each is laid out again when the rows are sorted,
    searched or filtered.
    """
    from ..gti import GTI

    nrows, pagination = spec["nrows"], spec["pagination"]
    shown = min(nrows, pagination["page_size"]) if pagination["enabled"] else nrows
    size = len(html.encode("utf-8"))

    reasons: list[str] = []
    if nrows > MAX_ROWS:
        reasons.append(f"has {nrows:,} rows (more than {MAX_ROWS:,})")
    if size > MAX_BYTES:
        reasons.append(f"has {size / 2**20:.1f} MB of HTML (more than {MAX_BYTES / 2**20:g} MB)")
    if shown > MAX_SHOWN:
        if pagination["enabled"]:
            shows = f"shows {shown:,} rows on a page"
        else:
            shows = "shows them all" if nrows > MAX_ROWS else f"shows all {nrows:,} rows"
            shows += " on one page"
        reasons.append(f"{shows} (more than {MAX_SHOWN:,})")
    if not reasons:
        return

    reason = reasons[-1] if len(reasons) == 1 else f"{', '.join(reasons[:-1])}, and {reasons[-1]}"
    message = (
        f"This interactive table may be slow in the browser, especially on phones: it {reason}."
    )
    if nrows > MAX_ROWS or size > MAX_BYTES:
        message += (
            " It's quicker to load with fewer rows, or fewer columns (or less in them), e.g., by "
            "filtering the data first."
        )
    if shown > MAX_SHOWN:
        if isinstance(gt, GTI):
            how = "`i_pagination()`"
            if pagination["enabled"]:
                how = f"a smaller `page_size=` in {how}"
        elif pagination["enabled"]:
            how = "a smaller `page_size_default=` in `opt_interactive()`"
        else:
            how = "`opt_interactive(use_pagination=True)`"
        message += (
            f" Sorting, searching and filtering are quicker with fewer rows on a page ({how})."
        )
    # (For the caller of `render_gti_html()`)
    warnings.warn(message, GTISizeWarning, stacklevel=3)


def render_parts(gt: GT, all_important: bool = False) -> tuple[str, Spec]:
    """A table's static HTML (its `<div>`) and its spec."""
    built = _build(gt)
    return built._render_as_html(all_important=all_important), build_spec(built)


def _build(gt: GT) -> GTData:
    settings = settings_of(gt)
    if settings.compact:
        gt = _compact(gt)
    gt = _leave_out(gt, settings.query_only)
    gt = leave_out_details_column(gt)
    return gt._build_data(context="html")


def stack_css(data: GTData, spec: Spec, table_html: str) -> str:
    """A stacked table's own CSS: the template, for the table's ID (that of GT's `<div>`, in its
    static HTML) and stacking width, and each column's label for its cells, under its spanners.

    The labels go by the cells' `headers` (a table without column labels has none), and by the
    column labels' IDs for the spanners, which the column labels have as chips.
    """
    found = re.match(r'<div id="([^"]*)"', table_html)
    if found is None:
        raise ValueError("The table's HTML doesn't start with its `<div>`, with an ID.")
    root = "#" + _css_id(unescape(found.group(1)))
    template = _load_stack_css()
    css = template.replace(STACK_WIDTH, f"(width < {spec['layout']['stack_below']}px)")
    css = css.replace(STACK_ROOT, root)

    header_ids = _get_header_ids(data)
    spanner_labels = {
        header_ids.spanners[span.spanner_id]: _label(span.spanner_label)
        for span in data._spanners
        if span.spanner_id in header_ids.spanners
    }
    rules = []
    for info in data._boxhead._get_default_columns():
        header = header_ids.columns.get(info.var)
        if header is None:
            continue
        spanners = [spanner_labels.get(id, "") for id in header_ids.column_spanners[info.var]]
        prefix = "".join(f"{label} · " for label in spanners if label)
        label = prefix + (_label(info.column_label) or info.var)
        rules.append(
            f"{root} [headers~={_css_string(header)}]{{--gt-i-label:{_css_string(label)}}}"
        )
        if prefix:
            rules.append(
                f"{root} th[id={_css_string(header)}]{{--gt-i-spanner:{_css_string(prefix)}}}"
            )
    return css + "".join(f"{rule}\n" for rule in rules)


def _label(label: object) -> str:
    return label_text(str(_process_text(label)))  # type: ignore[arg-type]


def _shown_columns(spec: Spec) -> int:
    """The data columns the table shows at first (not the stub, nor those its view hides)."""
    view = spec.get("view")
    hidden = set(view.get("hidden", [])) if view is not None else set()
    return sum(1 for c in spec["columns"] if c["role"] == "data" and c["id"] not in hidden)


def _css_id(ident: str) -> str:
    """An identifier escaped for CSS, as `CSS.escape()` does (and `<` too, which can't be in a
    `<style>` element's text as it is)."""
    out = []
    for i, char in enumerate(ident):
        code = ord(char)
        if code == 0:
            out.append("\ufffd")
        elif (
            0x01 <= code <= 0x1F
            or code == 0x7F
            or (i == 0 and char.isdigit() and char.isascii())
            or (i == 1 and char.isdigit() and char.isascii() and ident[0] == "-")
            or char == "<"
        ):
            out.append(f"\\{code:x} ")
        elif i == 0 and char == "-" and len(ident) == 1:
            out.append("\\-")
        elif code >= 0x80 or char in "-_" or (char.isascii() and char.isalnum()):
            out.append(char)
        else:
            out.append(f"\\{char}")
    return "".join(out)


def _css_string(text: str) -> str:
    """A CSS string, quoted: backslashes, quotes, control characters (and line breaks) and `<`
    (which can't be in a `<style>` element's text as it is) are escaped."""
    out = []
    for char in text:
        code = ord(char)
        if char in '\\"':
            out.append(f"\\{char}")
        elif code < 0x20 or code == 0x7F or char == "<":
            out.append(f"\\{code:x} ")
        else:
            out.append(char)
    return '"' + "".join(out) + '"'


def _has_bar(spec: Spec) -> bool:
    """Whether the runtime draws a control bar below the table: for a search, filters, pages, an
    export, rows' details (whose buttons opening and closing them all are in its info panel), or a
    link to other tables (whose selections filter it, as its tokens and info panel say).

    (Or pages there could be: the page sizes readers can choose from, in the bar's info panel,
    include the table's own. With filters, the bar's info panel says how many rows they leave.)
    """
    controls, pagination = spec["controls"], spec["pagination"]
    sizes = [pagination["page_size"]]
    if pagination["size_select"]:
        sizes += pagination["page_sizes"]
    paged = pagination["enabled"] and spec["nrows"] > min(sizes)
    return controls["bar"] and (
        controls["search"]
        or bool(spec["filters"])
        or bool(spec["export"]["formats"])
        or paged
        or bool(spec["details"])
        or spec.get("link") is not None
    )


def _has_tokens(spec: Spec) -> bool:
    """Whether the bar starts with a line of tokens: for a view with a filter that's on, or a
    group of its query's.

    (A filter is off with blank text, which the runtime trims as JavaScript does.)
    """
    view = spec.get("view")
    items = (view["filter"] or {"and": []})["and"] if view is not None else []
    return any("col" not in c or c["op"] != "contains" or js_trim(c["value"]) != "" for c in items)


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
            "A table without a stub can't have every column left out of it with `display=False`."
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
