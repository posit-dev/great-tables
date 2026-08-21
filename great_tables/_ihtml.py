from __future__ import annotations

import json
import warnings
from pathlib import Path
from typing import TYPE_CHECKING

from ._locations import LocBody, LocColumnLabels
from ._tbl_data import _get_cell, cast_frame_to_string, replace_null_frame
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
    """Render a GT object as a self-contained interactive HTML table."""
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

    # ------------------------------------------------------------------
    # Visible columns (default columns only; stub excluded in Phase 1)
    # ------------------------------------------------------------------
    visible_cols = [c for c in built._boxhead._get_default_columns() if c.visible]

    if built._summary_rows or built._summary_rows_grand:
        warnings.warn(
            "opt_interactive(): summary_rows() and grand_summary_rows() are not rendered "
            "in interactive mode and have been omitted.",
            stacklevel=3,
        )

    # ------------------------------------------------------------------
    # Build rows data as a list of dicts (one per row).
    # ------------------------------------------------------------------
    rows_data: list[dict] = []
    for row_idx, _group_info in built._stub.group_indices_map():
        row: dict = {}
        for col in visible_cols:
            cell_val = _get_cell(tbl_data, row_idx, col.var)
            row[col.var] = str(cell_val) if cell_val is not None else ""
        rows_data.append(row)

    # ------------------------------------------------------------------
    # Pre-compute column widths from max content length across all rows.
    # Using monospace fonts makes character-to-pixel conversion reliable.
    # ------------------------------------------------------------------
    font_size_px = _parse_px(opts.table_font_size.value, default=16.0)
    char_width_px = font_size_px * 0.60  # monospace: each char ~0.6 em wide
    cell_pad_px = 20  # DataTables default: 10px each side
    sort_icon_px = 26  # room for the sort arrow in headers

    col_widths: dict[str, str] = {}
    for col in visible_cols:
        # User-specified explicit px width always wins.
        if col.column_width and col.column_width.endswith("px"):
            col_widths[col.var] = col.column_width
            continue
        header_chars = len(_col_label(col))
        max_data_chars = max(
            (len(row.get(col.var, "")) for row in rows_data),
            default=0,
        )
        max_chars = max(header_chars, max_data_chars)
        width_px = int(max_chars * char_width_px + cell_pad_px + sort_icon_px)
        col_widths[col.var] = f"{width_px}px"

    # ------------------------------------------------------------------
    # Build column definitions for DataTables.
    # We do NOT include 'title' here — the <thead> we generate owns labels.
    # ------------------------------------------------------------------
    col_defs = []
    for col in visible_cols:
        col_def: dict = {"data": col.var, "width": col_widths[col.var]}
        if not opts.ihtml_use_text_wrapping.value:
            col_def["className"] = "dt-nowrap"
        col_defs.append(col_def)

    # ------------------------------------------------------------------
    # Build <thead>. Spanners are not rendered in interactive mode — DataTables'
    # multi-row header conflicts with its sort-click binding model.
    # ------------------------------------------------------------------
    if built._spanners:
        warnings.warn(
            "opt_interactive(): tab_spanner() is not rendered in interactive mode. "
            "Column labels are shown in a flat header row.",
            stacklevel=3,
        )

    # ------------------------------------------------------------------
    # Collect tab_style() declarations for supported locations.
    # ------------------------------------------------------------------
    body_cell_styles = _collect_body_styles(built, visible_cols)
    col_label_styles = _collect_col_label_styles(built, visible_cols)
    col_idx = {col.var: i for i, col in enumerate(visible_cols)}

    thead_html = _build_thead(built, visible_cols, col_label_styles)

    # ------------------------------------------------------------------
    # Map opt_interactive options to DataTables config.
    # ------------------------------------------------------------------
    pagination_type_map = {
        "numbers": "numbers",
        "simple": "simple",
        "full": "full_numbers",
    }
    dt_pagination_type = pagination_type_map.get(str(opts.ihtml_pagination_type.value), "numbers")

    page_size_vals = opts.ihtml_page_size_values.value or [10, 25, 50, 100]

    height_val = opts.ihtml_height.value
    scroll_y = height_val if height_val and height_val != "auto" else ""

    dt_config: dict = {
        "columns": col_defs,
        "data": rows_data,
        "autoWidth": False,
        "paging": opts.ihtml_use_pagination.value,
        "info": opts.ihtml_use_pagination_info.value,
        "ordering": opts.ihtml_use_sorting.value,
        "searching": opts.ihtml_use_search.value,
        "lengthChange": opts.ihtml_use_page_size_select.value,
        "pageLength": opts.ihtml_page_size_default.value,
        "lengthMenu": page_size_vals,
        "pagingType": dt_pagination_type,
        "scrollY": scroll_y,
        "scrollCollapse": bool(scroll_y),
    }

    # "display" is shorthand for stripe+hover+row-border+order-column.
    # Drop "stripe" so GT's own row_striping options control striping instead.
    base_classes = "hover row-border order-column"
    if opts.ihtml_use_compact_mode.value:
        dt_config["className"] = f"compact {base_classes}"
    else:
        dt_config["className"] = base_classes

    use_filters = opts.ihtml_use_filters.value
    use_highlight = opts.ihtml_use_highlight.value
    use_resizers = opts.ihtml_use_resizers.value

    theme_css = _build_theme_css(built, mount_id)
    header_html = _build_header_html(built)
    footer_html = _build_footer_html(built)

    jquery_js = _load_asset("jquery.slim.min.js")
    dt_js = _load_asset("dataTables.min.js")
    dt_css = _load_asset("dataTables.min.css")

    config_json = json.dumps(dt_config, ensure_ascii=False)

    init_extras = _build_init_extras(
        mount_id=mount_id,
        use_filters=use_filters,
        use_highlight=use_highlight,
        use_resizers=use_resizers,
        body_cell_styles=body_cell_styles,
        col_idx=col_idx,
    )

    html = f"""\
<meta charset="utf-8">
<div id="{mount_id}-container" class="gt-ihtml-container">
{header_html}
<div id="{mount_id}-wrapper">
<table id="{mount_id}" style="width:100%">
{thead_html}
</table>
</div>
{footer_html}
</div>
<style>{dt_css}</style>
<style>{theme_css}</style>
<script>{jquery_js}</script>
<script>{dt_js}</script>
<script>
(function() {{
  var cfg = {config_json};
{init_extras}
  new DataTable(document.getElementById({json.dumps(mount_id)}), cfg);
}})();
</script>
"""
    return html


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _col_label(col: ColInfo) -> str:
    """Return the display label for a column, falling back to the var name."""
    label = col.column_label
    if label is None:
        return col.var
    return str(label)


def _parse_px(value: str | None, default: float = 16.0) -> float:
    """Extract a numeric pixel value from a CSS px string, e.g. '16px' → 16.0."""
    if not value:
        return default
    try:
        return float(str(value).rstrip("px").strip())
    except ValueError:
        return default


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


def _build_thead(
    built: GT,
    visible_cols: list[ColInfo],
    col_label_styles: dict[str, str] | None = None,
) -> str:
    """Build a flat single-row <thead>. Spanners are omitted in interactive mode."""
    col_label_styles = col_label_styles or {}
    cells = []
    for c in visible_cols:
        style_attr = f' style="{col_label_styles[c.var]}"' if c.var in col_label_styles else ""
        cells.append(f"<th{style_attr}>{_col_label(c)}</th>")
    return f"<thead><tr>{''.join(cells)}</tr></thead>"


def _build_header_html(built: GT) -> str:
    if not heading_has_title(built._heading.title):
        return ""

    title = built._heading.title
    subtitle = built._heading.subtitle

    title_str = _process_text(title) if title else ""
    subtitle_str = (
        f'<p class="gt-ihtml-subtitle">{_process_text(subtitle)}</p>'
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
        text = _process_text(sn) if sn else ""
        if text:
            parts.append(f'<p class="gt-ihtml-source-note">{text}</p>')
    if not parts:
        return ""
    return '<div class="gt-ihtml-footer">' + "".join(parts) + "</div>"


def _build_theme_css(built: GT, mount_id: str) -> str:
    opts = built._options
    rules: list[str] = []

    bg = opts.table_background_color.value
    fg = opts.table_font_color.value
    font_size = opts.table_font_size.value
    stripe_color = opts.row_striping_background_color.value
    col_label_bg = opts.column_labels_background_color.value
    col_label_border_bottom = (
        f"{opts.column_labels_border_bottom_width.value} "
        f"{opts.column_labels_border_bottom_style.value} "
        f"{opts.column_labels_border_bottom_color.value}"
    )

    sel = f"#{mount_id}-container"

    # Font family — build a CSS font-family stack from the option list.
    font_names: list[str] = opts.table_font_names.value or []
    if not font_names:
        font_names = ["system-ui", "-apple-system", "sans-serif"]
    css_font_family = ", ".join(f'"{n}"' if " " in n else n for n in font_names)
    rules.append(f"{sel} {{ font-family: {css_font_family}; }}")
    # Monospace font for table cells and column headers — ensures reliable
    # character-based column pre-sizing and prevents per-page width jitter.
    mono_stack = (
        "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "
        '"Liberation Mono", "Courier New", monospace'
    )
    rules.append(
        f"{sel} table.dataTable thead th,"
        f"{sel} table.dataTable tbody td"
        f" {{ font-family: {mono_stack}; }}"
    )

    if bg:
        rules.append(f"{sel} table.dataTable {{ background-color: {bg}; }}")
    if fg:
        rules.append(f"{sel} table.dataTable {{ color: {fg}; }}")
    if font_size:
        rules.append(f"{sel} table.dataTable {{ font-size: {font_size}; }}")
    if col_label_bg:
        rules.append(f"{sel} table.dataTable thead th {{ background-color: {col_label_bg}; }}")
    rules.append(f"{sel} table.dataTable thead th {{ border-bottom: {col_label_border_bottom}; }}")
    if stripe_color and opts.row_striping_include_table_body.value:
        rules.append(
            f"{sel} table.dataTable tbody tr:nth-child(odd) > td,"
            f"{sel} table.dataTable tbody tr:nth-child(odd) > th"
            f" {{ background-color: {stripe_color} !important; }}"
        )

    rules.append(
        f"{sel} .gt-ihtml-header {{ text-align: {opts.heading_align.value}; "
        f"padding: {opts.heading_padding.value}; }}"
    )
    rules.append(
        f"{sel} .gt-ihtml-title {{ font-size: {opts.heading_title_font_size.value}; "
        f"font-weight: {opts.heading_title_font_weight.value}; margin: 0; }}"
    )
    rules.append(
        f"{sel} .gt-ihtml-subtitle {{ font-size: {opts.heading_subtitle_font_size.value}; "
        f"font-weight: {opts.heading_subtitle_font_weight.value}; margin: 0; }}"
    )
    rules.append(
        f"{sel} .gt-ihtml-source-note {{ font-size: {opts.source_notes_font_size.value}; "
        f"padding: {opts.source_notes_padding.value}; margin: 0; }}"
    )
    return "\n".join(rules)


def _build_init_extras(
    mount_id: str,
    use_filters: bool,
    use_highlight: bool,
    use_resizers: bool,
    body_cell_styles: dict[int, dict[str, str]] | None = None,
    col_idx: dict[str, int] | None = None,
) -> str:
    lines: list[str] = []

    if body_cell_styles and col_idx:
        cell_styles_json = json.dumps(
            {str(k): v for k, v in body_cell_styles.items()}, ensure_ascii=False
        )
        col_idx_json = json.dumps(col_idx, ensure_ascii=False)
        lines.append(
            f"  var _cellStyles = {cell_styles_json};\n"
            f"  var _colIdx = {col_idx_json};\n"
            "  cfg.createdRow = function(row, rowData, dataIndex) {\n"
            "    var s = _cellStyles[String(dataIndex)]; if (!s) return;\n"
            "    var cells = row.cells;\n"
            "    for (var col in s) { var i = _colIdx[col]; if (i !== undefined) cells[i].style.cssText += s[col]; }\n"
            "  };"
        )

    if use_filters:
        # Append filter inputs to a new <tr> row using <td> (not <th>) so
        # DataTables does not treat the row as column headers and preserves
        # sort click targets on the real header cells.
        lines.append(
            "  cfg.initComplete = function() {\n"
            "    var api = this.api();\n"
            "    var thead = api.table().header();\n"
            "    var filterRow = document.createElement('tr');\n"
            "    api.columns().every(function() {\n"
            "      var col = this;\n"
            "      var td = document.createElement('td');\n"
            "      var input = document.createElement('input');\n"
            "      input.placeholder = 'Filter...';\n"
            "      input.style.width = '100%';\n"
            "      input.style.boxSizing = 'border-box';\n"
            "      input.addEventListener('input', function() { col.search(this.value).draw(); });\n"
            "      td.appendChild(input);\n"
            "      filterRow.appendChild(td);\n"
            "    });\n"
            "    thead.appendChild(filterRow);\n"
            "  };"
        )

    if use_highlight:
        lines.append(
            f"  document.getElementById({json.dumps(mount_id)}).addEventListener(\n"
            "    'mouseover', function(e) {\n"
            "      var tr = e.target.closest('tr');\n"
            "      if (tr) tr.style.backgroundColor = 'rgba(0,0,0,0.05)';\n"
            "    }\n"
            "  );\n"
            f"  document.getElementById({json.dumps(mount_id)}).addEventListener(\n"
            "    'mouseout', function(e) {\n"
            "      var tr = e.target.closest('tr');\n"
            "      if (tr) tr.style.backgroundColor = '';\n"
            "    }\n"
            "  );"
        )

    if use_resizers:
        lines.append("  cfg.autoWidth = true;")

    return "\n".join(lines)
