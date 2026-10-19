from __future__ import annotations

import html as html_lib
import json
import math
import re
import warnings
from pathlib import Path
from typing import TYPE_CHECKING

from ._locations import LocBody, LocColumnLabels
from ._tbl_data import (
    _get_cell,
    _is_numeric_dtype,
    cast_frame_to_string,
    replace_null_frame,
)
from ._text import _process_text
from ._utils import heading_has_subtitle, heading_has_title

if TYPE_CHECKING:
    from ._gt_data import ColInfo
    from .gt import GT


# ---------------------------------------------------------------------------
# Vendored asset loading
# ---------------------------------------------------------------------------


def _load_asset(filename: str) -> str:
    asset_path = Path(__file__).parent / "js" / filename
    return asset_path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def render_as_ihtml(data: GT) -> str:
    """Render a GT object as a self-contained interactive HTML fragment."""
    from ._helpers import random_id

    opts = data._options

    table_id = opts.table_id.value or random_id()
    mount_id = f"gt-ihtml-{table_id}"

    # ------------------------------------------------------------------
    # Run the normal build pipeline so formatting/substitutions apply.
    # ------------------------------------------------------------------
    built = data._build_data(context="html")
    _str_orig = cast_frame_to_string(built._tbl_data)
    tbl_data = replace_null_frame(built._body.body, _str_orig)

    visible_cols = [c for c in built._boxhead._get_default_columns() if c.visible]

    orig_data = built._tbl_data
    numeric_cols: set[str] = {c.var for c in visible_cols if _is_numeric_dtype(orig_data, c.var)}

    if built._summary_rows or built._summary_rows_grand:
        warnings.warn(
            "opt_interactive(): summary_rows() and grand_summary_rows() are not rendered "
            "in interactive mode and have been omitted.",
            stacklevel=3,
        )
    if built._spanners:
        warnings.warn(
            "opt_interactive(): tab_spanner() is not rendered in interactive mode. "
            "Column labels are shown in a flat header row.",
            stacklevel=3,
        )

    # ------------------------------------------------------------------
    # Build rows as a list of dicts — used for width pre-computation and
    # then converted to reactable's columnar format.
    # ------------------------------------------------------------------
    rows_data: list[dict] = []
    orig_numeric_vals: dict[str, list[float | None]] = {c: [] for c in numeric_cols}
    for row_idx, _group_info in built._stub.group_indices_map():
        row: dict = {}
        for col in visible_cols:
            cell_val = _get_cell(tbl_data, row_idx, col.var)
            row[col.var] = str(cell_val) if cell_val is not None else ""
            if col.var in numeric_cols:
                raw = _get_cell(orig_data, row_idx, col.var)
                if raw is None:
                    orig_numeric_vals[col.var].append(None)
                else:
                    v = float(raw)
                    orig_numeric_vals[col.var].append(None if math.isnan(v) else v)
        rows_data.append(row)

    n_rows = len(rows_data)

    # ------------------------------------------------------------------
    # Collect tab_style() / data_color() declarations.
    # ------------------------------------------------------------------
    body_cell_styles = _collect_body_styles(built, visible_cols)
    col_label_styles = _collect_col_label_styles(built, visible_cols)

    # Convert per-cell CSS strings to per-column React style arrays.
    # Build per-column style lookups as JS callback strings.
    # Reactable's style array is indexed by display position (affected by sorting),
    # so we use the {code: "..."} function form with rowInfo.index instead.
    # rowInfo.index is always the original data row index, sort-stable.
    body_style_fns: dict[str, dict] = {}
    for col in visible_cols:
        lookup: dict[str, dict] = {}
        for row_idx in range(n_rows):
            css = body_cell_styles.get(row_idx, {}).get(col.var, "")
            if css:
                react_style = _css_str_to_react_style(css)
                if react_style:
                    lookup[str(row_idx)] = react_style
        if lookup:
            lookup_json = json.dumps(lookup, ensure_ascii=False)
            body_style_fns[col.var] = {
                "code": f"function(rowInfo){{var s={lookup_json};return s[String(rowInfo.index)]||null;}}"
            }

    # ------------------------------------------------------------------
    # Column width pre-computation using monospace character widths.
    # ------------------------------------------------------------------
    font_size_px = 14.0  # monospace data/header cells are rendered at 14px
    char_width_px = font_size_px * 0.60
    cell_pad_px = 20

    col_widths: dict[str, int] = {}
    for col in visible_cols:
        if col.column_width and col.column_width.endswith("px"):
            col_widths[col.var] = int(col.column_width.rstrip("px"))
            continue
        header_px = _html_width_px(_col_label(col), font_size_px, char_width_px)
        max_data_px = max(
            (
                _html_width_px(row.get(col.var, ""), font_size_px, char_width_px)
                for row in rows_data
            ),
            default=0,
        )
        max_px = max(header_px, max_data_px)
        sort_icon_px = 24  # reactable sort arrow occupies header space
        col_widths[col.var] = int(max_px + cell_pad_px + sort_icon_px)

    # ------------------------------------------------------------------
    # Build reactable column definitions.
    # ------------------------------------------------------------------
    # Cells and column labels are HTML (as in the static table), so every column is rendered with
    # `html: True`. The column data, which reactable searches, sorts and filters on, holds the
    # original numbers for numeric columns and each cell's visible text otherwise; the formatted
    # HTML is given separately as `cell` (reactable shows `cell[row.index]`, which follows sorting)
    reactable_cols: list[dict] = []
    columnar_data: dict[str, list] = {}
    for col in visible_cols:
        cells_html = [row.get(col.var, "") for row in rows_data]
        label_html = _col_label(col)
        # reactable uses `name` in the sort and filter aria-labels, so it's the label's text; the
        # label's HTML, when it differs, is given as `header`
        label_text = _html_to_text(_BR_RE.sub(" ", label_html))
        col_def: dict = {
            "id": col.var,
            "name": label_text,
            "minWidth": col_widths[col.var],
            "align": col.column_align or "left",
            "headerAlign": col.column_align or "left",
            "html": True,
        }
        if label_text != label_html:
            col_def["header"] = label_html
        if col.var in numeric_cols:
            col_def["type"] = "numeric"
            col_def["cell"] = cells_html
            columnar_data[col.var] = orig_numeric_vals[col.var]
        else:
            cells_text = [_html_to_text(cell) for cell in cells_html]
            # A cell without markup or entities is shown as is, so `cell` is only needed when
            # some cell's HTML differs from its text
            if cells_text != cells_html:
                col_def["cell"] = cells_html
            columnar_data[col.var] = cells_text
        if col.var in body_style_fns:
            col_def["style"] = body_style_fns[col.var]
        if col.var in col_label_styles:
            col_def["headerStyle"] = _css_str_to_react_style(col_label_styles[col.var])
        reactable_cols.append(col_def)

    # ------------------------------------------------------------------
    # Map GT options to reactable props.
    # ------------------------------------------------------------------
    page_size_vals = opts.ihtml_page_size_values.value or [10, 25, 50, 100]
    height_val = opts.ihtml_height.value

    reactable_props: dict = {
        "data": columnar_data,
        "columns": reactable_cols,
        "searchable": opts.ihtml_use_search.value,
        "filterable": opts.ihtml_use_filters.value,
        "sortable": opts.ihtml_use_sorting.value,
        "pagination": opts.ihtml_use_pagination.value,
        "showPageInfo": opts.ihtml_use_pagination_info.value,
        "defaultPageSize": opts.ihtml_page_size_default.value,
        "showPageSizeOptions": opts.ihtml_use_page_size_select.value,
        "pageSizeOptions": page_size_vals,
        "striped": opts.row_striping_include_table_body.value,
        "highlight": True,
        "compact": opts.ihtml_use_compact_mode.value,
        "nowrap": not opts.ihtml_use_text_wrapping.value,
    }

    if height_val and height_val != "auto":
        reactable_props["height"] = height_val

    pagination_type_map = {
        "numbers": "numbers",
        "simple": "simple",
        "full": "jump",
    }
    reactable_props["paginationType"] = pagination_type_map.get(
        str(opts.ihtml_pagination_type.value), "numbers"
    )

    theme = _build_reactable_theme(built)
    if theme:
        reactable_props["theme"] = theme

    # ------------------------------------------------------------------
    # Build HTML.
    # ------------------------------------------------------------------
    reactable_esm = _load_asset("reactable.esm.js")
    reactable_css = _load_asset("reactable.esm.css")
    theme_css = _build_theme_css(built, mount_id)
    header_html = _build_header_html(built)
    footer_html = _build_footer_html(built)

    props_json = json.dumps(reactable_props, ensure_ascii=True)
    mount_id_json = json.dumps(mount_id)

    html = f"""\
<div id="{mount_id}-container" class="gt-ihtml-container">
{header_html}
<div id="{mount_id}"></div>
{footer_html}
</div>
<style>{reactable_css}</style>
<style>{theme_css}</style>
<script type="importmap">
{{"imports":{{"react":"https://esm.sh/react@18","react-dom":"https://esm.sh/react-dom@18"}}}}
</script>
<script type="module">
{reactable_esm}

const _el = document.getElementById({mount_id_json});
const _props = {props_json};
const _node = requireReact.createElement(Reactable2, _props);
if (requireReactDom.createRoot) {{
  requireReactDom.createRoot(_el).render(_node);
}} else {{
  requireReactDom.render(_node, _el);
}}
</script>
"""
    return html


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _escape_nonascii(s: str) -> str:
    """Escape non-ASCII characters to numeric HTML entities.

    Converts e.g. U+2014 EM DASH to &#8212; so the HTML fragment is safe to embed in pages
    regardless of their declared charset.
    """
    return s.encode("ascii", "xmlcharrefreplace").decode("ascii")


def _col_label(col: ColInfo) -> str:
    """Get a column label as HTML (a plain string is escaped; `md()`/`html()` are processed)."""
    label = col.column_label
    if label is None:
        label = col.var
    return _process_text(label, context="html")


_BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
_SVG_RE = re.compile(r"<svg\b.*?</svg>", re.IGNORECASE | re.DOTALL)
_IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
_TAG_RE = re.compile(r"<[^>]+>")


def _html_to_text(html_str: str) -> str:
    """Get the visible text of a cell's HTML: no markup (or inline SVG), entities unescaped."""
    return html_lib.unescape(_TAG_RE.sub("", _SVG_RE.sub("", html_str)))


def _html_width_px(html_str: str, font_size_px: float, char_width_px: float) -> float:
    """Estimate the width of a cell's (or label's) HTML when rendered, in px.

    Each line (lines are split at `<br>`) is as wide as its visible text, plus each image or
    inline SVG in it; markup and entities (e.g., `&nbsp;`) aren't counted as characters.
    """
    width_px = 0.0
    for line in _BR_RE.split(html_str):
        graphics = _SVG_RE.findall(line) + _IMG_RE.findall(line)
        graphics_px = sum(_graphic_width_px(tag, font_size_px) for tag in graphics)
        width_px = max(width_px, len(_html_to_text(line)) * char_width_px + graphics_px)
    return width_px


def _css_length_px(tag: str, prop: str, font_size_px: float) -> float | None:
    """Get the `width` or `height` of a tag (from its style or attribute) in px, if px or em."""
    match = re.search(
        rf"(?<![\w-]){prop}\s*[:=]\s*[\"']?([\d.]+)\s*(px|em)?(?![\w%])", tag, re.IGNORECASE
    )
    if match is None:
        return None
    value = float(match.group(1))
    return value * font_size_px if match.group(2) == "em" else value


def _graphic_width_px(tag: str, font_size_px: float) -> float:
    """Estimate the width of an `<img>` or inline `<svg>`, in px.

    The width is the tag's own `width`, if set; otherwise its `height` (2em if not set, the
    `fmt_image()` default) times the `viewBox` aspect ratio, or square if that isn't known.
    """
    opening_tag = tag[: tag.find(">") + 1]
    width = _css_length_px(opening_tag, "width", font_size_px)
    if width is not None:
        return width
    height = _css_length_px(opening_tag, "height", font_size_px) or 2 * font_size_px
    view_box = re.search(
        r'viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)', opening_tag
    )
    if view_box is not None and float(view_box.group(2)) > 0:
        return height * float(view_box.group(1)) / float(view_box.group(2))
    return height


def _parse_px(value: str | None, default: float = 16.0) -> float:
    if not value:
        return default
    try:
        return float(str(value).rstrip("px").strip())
    except ValueError:
        return default


def _css_str_to_react_style(css: str) -> dict:
    """Convert a CSS declaration string to a React-style camelCase dict.

    e.g. 'background-color: yellow; font-weight: bold;' ->
         {'backgroundColor': 'yellow', 'fontWeight': 'bold'}
    """
    result: dict = {}
    for decl in css.split(";"):
        decl = decl.strip()
        if not decl:
            continue
        # Strip !important — React doesn't accept it in style objects
        decl = decl.replace("!important", "").strip()
        if ":" not in decl:
            continue
        prop, _, value = decl.partition(":")
        prop = prop.strip()
        value = value.strip()
        if not prop or not value:
            continue
        parts = prop.split("-")
        camel = parts[0] + "".join(p.capitalize() for p in parts[1:])
        result[camel] = value
    return result


def _collect_body_styles(built: GT, visible_cols: list[ColInfo]) -> dict[int, dict[str, str]]:
    """Return {rownum: {colname: css}} for all tab_style(loc.body()) declarations."""
    col_vars = {c.var for c in visible_cols}
    result: dict[int, dict[str, str]] = {}
    for si in built._styles:
        if not isinstance(si.locname, LocBody):
            continue
        if si.rownum is None or si.colname not in col_vars:
            continue
        css = "".join(s._to_html_style() for s in si.styles)
        if css:
            row_entry = result.setdefault(si.rownum, {})
            row_entry[si.colname] = row_entry.get(si.colname, "") + css
    return result


def _collect_col_label_styles(built: GT, visible_cols: list[ColInfo]) -> dict[str, str]:
    """Return {colname: css} for all tab_style(loc.column_labels()) declarations."""
    col_vars = {c.var for c in visible_cols}
    result: dict[str, str] = {}
    for si in built._styles:
        if not isinstance(si.locname, LocColumnLabels):
            continue
        if si.colname not in col_vars:
            continue
        css = "".join(s._to_html_style() for s in si.styles)
        if css:
            result[si.colname] = result.get(si.colname, "") + css
    return result


def _build_reactable_theme(built: GT) -> dict:
    """Build a reactable theme object from GT options."""
    opts = built._options
    theme: dict = {}

    bg = opts.table_background_color.value
    fg = opts.table_font_color.value
    stripe_color = opts.row_striping_background_color.value

    if bg:
        theme["backgroundColor"] = bg
    if fg:
        theme["color"] = fg
    if stripe_color and opts.row_striping_include_table_body.value:
        theme["stripedColor"] = stripe_color

    # Font family
    font_names: list[str] = opts.table_font_names.value or []
    if not font_names:
        font_names = ["system-ui", "-apple-system", "sans-serif"]
    css_font_family = ", ".join(f'"{n}"' if " " in n else n for n in font_names)

    font_size = opts.table_font_size.value
    table_style: dict = {"fontFamily": css_font_family}
    if font_size:
        table_style["fontSize"] = font_size
    theme["style"] = table_style

    # Monospace for data cells and headers at a slightly smaller size
    mono_stack = (
        "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "
        '"Liberation Mono", "Courier New", monospace'
    )
    theme["tableBodyStyle"] = {"fontFamily": mono_stack, "fontSize": "14px"}
    theme["headerStyle"] = {"fontFamily": mono_stack, "fontSize": "14px"}

    # Column label background/border from GT options
    col_label_bg = opts.column_labels_background_color.value
    if col_label_bg:
        theme["headerStyle"]["backgroundColor"] = col_label_bg

    return theme if theme else {}


def _build_header_html(built: GT) -> str:
    if not heading_has_title(built._heading.title):
        return ""

    title = built._heading.title
    subtitle = built._heading.subtitle

    title_str = _escape_nonascii(_process_text(title)) if title else ""
    subtitle_str = (
        f'<p class="gt-ihtml-subtitle">{_escape_nonascii(_process_text(subtitle))}</p>'
        if heading_has_subtitle(built._heading.subtitle)
        else ""
    )

    return (
        f'<div class="gt-ihtml-header">'
        f'<p class="gt-ihtml-title">{title_str}</p>'
        f"{subtitle_str}"
        f"</div>"
    )


def _build_footer_html(built: GT) -> str:
    parts: list[str] = []
    for sn in built._source_notes:
        text = _escape_nonascii(_process_text(sn)) if sn else ""
        if text:
            parts.append(f'<p class="gt-ihtml-source-note">{text}</p>')
    if not parts:
        return ""
    return '<div class="gt-ihtml-footer">' + "".join(parts) + "</div>"


def _build_theme_css(built: GT, mount_id: str) -> str:
    """CSS for GT wrapper elements (header, footer). Table styling uses reactable theme."""
    opts = built._options
    rules: list[str] = []
    sel = f"#{mount_id}-container"

    font_names: list[str] = opts.table_font_names.value or []
    if not font_names:
        font_names = ["system-ui", "-apple-system", "sans-serif"]
    css_font_family = ", ".join(f'"{n}"' if " " in n else n for n in font_names)

    font_size = opts.table_font_size.value or "16px"
    rules.append(
        f"{sel} {{ display: block; width: 100%; font-size: {font_size}; margin: 10px 0; }}"
    )

    border_top = (
        f"{opts.table_border_top_width.value} "
        f"{opts.table_border_top_style.value} "
        f"{opts.table_border_top_color.value}"
    )
    border_bottom = (
        f"{opts.heading_border_bottom_width.value} "
        f"{opts.heading_border_bottom_style.value} "
        f"{opts.heading_border_bottom_color.value}"
    )
    body_border_bottom = (
        f"{opts.column_labels_border_top_width.value} "
        f"{opts.column_labels_border_top_style.value} "
        f"{opts.column_labels_border_top_color.value}"
    )
    h_pad = opts.heading_padding_horizontal.value
    rules.append(
        f"{sel} .gt-ihtml-header {{ display: block; width: 100%; "
        f"text-align: {opts.heading_align.value}; "
        f"padding: 10px {h_pad} 8px {h_pad}; "
        f"border-top: {border_top}; "
        f"border-bottom: {border_bottom}; }}"
    )
    rules.append(f"{sel} .rt-tbody {{ border-bottom: {body_border_bottom}; }}")
    if heading_has_title(built._heading.title):
        rules.append(f"{sel} .rt-search {{ margin-top: 8px; }}")
    rules.append(
        f"{sel} .gt-ihtml-title {{ font-family: {css_font_family}; "
        f"font-size: 1.5em; "
        f"font-weight: {opts.heading_title_font_weight.value}; margin: 0; }}"
    )
    rules.append(
        f"{sel} .gt-ihtml-subtitle {{ font-family: {css_font_family}; "
        f"font-size: 1.05em; "
        f"font-weight: {opts.heading_subtitle_font_weight.value}; margin: 0; }}"
    )
    rules.append(
        f"{sel} .gt-ihtml-source-note {{ font-family: {css_font_family}; "
        f"font-size: {opts.source_notes_font_size.value}; "
        f"padding: {opts.source_notes_padding.value}; margin: 0; }}"
    )
    return "\n".join(rules)
