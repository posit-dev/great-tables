from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING

from ._spanners import spanners_print_matrix
from ._tbl_data import _get_cell, cast_frame_to_string, replace_null_frame
from ._text import _process_text
from ._utils import heading_has_subtitle, heading_has_title, seq_groups
from ._utils_render_html import _get_spanners_matrix_height

if TYPE_CHECKING:
    from ._gt_data import GroupRowInfo, GTData


def _css_length_to_typst(length: str) -> str:
    """Convert a CSS length string (e.g., '100px', '50%', '2cm') to Typst."""
    length = length.strip()
    if length.endswith("px"):
        # Convert px to pt (Typst uses pt; 1px ≈ 0.75pt)
        val = float(length[:-2])
        return f"{val * 0.75:.1f}pt"
    if length.endswith("%"):
        val = float(length[:-1])
        # Typst supports % for widths but not for text sizes
        return f"{val}%"
    # pt, cm, mm, in, em — Typst supports these directly
    return length


def _css_length_to_typst_text_size(length: str) -> str:
    """Convert a CSS length to Typst text size. Converts % to em.

    Like _css_length_to_typst() but converts percentages to em units since
    Typst's text(size: ...) doesn't accept percentages. em is relative to
    the parent font size, so 125% becomes 1.25em.
    """
    length = length.strip()
    if length.endswith("%"):
        val = float(length[:-1])
        return f"{val / 100:.2f}em"
    return _css_length_to_typst(length)


def _css_weight_to_typst(weight: str) -> str:
    """Convert CSS font-weight to Typst weight string."""
    # Typst accepts: "thin", "extralight", "light", "regular", "medium",
    # "semibold", "bold", "extrabold", "black", or integer 100-900
    if weight == "normal":
        return "regular"
    if weight == "initial" or weight == "inherit":
        return "regular"
    return weight


def _has_stub_column(data: GTData) -> bool:
    """Check if the table has a stub column (explicit or summary-only)."""
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    stub_layout = data._stub._get_stub_layout(
        has_summary_rows=has_summary_rows, options=data._options
    )
    return "rowname" in stub_layout


def _option_border_to_typst(style: str, width: str, color: str) -> str | None:
    """Convert GT border options to Typst stroke syntax. Returns None for style='none'."""
    if style == "none" or style == "hidden":
        return None
    typst_width = _css_length_to_typst(width)
    typst_color = f'rgb("{color}")' if color.startswith("#") else color
    # Typst doesn't support "double" — render as solid with half width
    if style == "double":
        # CSS double border uses the width for the total including gap;
        # approximate as a single solid line at ~1/3 the width
        try:
            val = float(typst_width.replace("pt", ""))
            typst_width = f"{max(val / 3, 0.75):.1f}pt"
        except ValueError:
            pass
    return f"{typst_width} + {typst_color}"


def create_table_start_typst(data: GTData) -> str:
    """Create the Typst table opening with column specifications and default styling."""

    opts = data._options

    # Check for stub column (includes summary-only stubs)
    has_stub = _has_stub_column(data)

    # Get column alignments
    alignments = data._boxhead._get_default_alignments()

    typst_align_map = {"left": "left", "center": "center", "right": "right"}
    col_aligns = [typst_align_map.get(a, "left") for a in alignments]

    # Prepend stub column alignment
    if has_stub:
        col_aligns = ["left"] + col_aligns

    # Build column sizing from cols_width if set, otherwise auto
    col_widths = data._boxhead._get_column_widths()
    default_cols = data._boxhead._get_default_columns()
    visible_widths = [
        col_widths[i] if i < len(col_widths) else None for i, _ in enumerate(default_cols)
    ]

    if has_stub:
        visible_widths = [None] + visible_widths

    if any(w is not None for w in visible_widths):
        typst_widths = [
            _css_length_to_typst(w) if w is not None else "auto" for w in visible_widths
        ]
        columns_spec = "columns: (" + ", ".join(typst_widths) + ",)"
    else:
        columns_spec = f"columns: {len(col_aligns)}"

    # Build alignment specification
    if len(set(col_aligns)) == 1:
        align_spec = f"align: {col_aligns[0]}"
    else:
        align_spec = "align: (" + ", ".join(col_aligns) + ",)"

    # Cell padding from options
    row_pad = _css_length_to_typst(opts.data_row_padding.value)
    row_pad_h = _css_length_to_typst(opts.data_row_padding_horizontal.value)
    inset_spec = f"inset: (x: {row_pad_h}, y: {row_pad})"

    # Table background color
    table_bg = opts.table_background_color.value
    bg_spec = ""
    if table_bg and table_bg != "#FFFFFF":
        typst_bg = f'rgb("{table_bg}")' if table_bg.startswith("#") else table_bg
        bg_spec = f"\n  fill: {typst_bg},"

    parts = [
        f"#table(\n  {columns_spec},\n  {align_spec},\n  stroke: none,\n  {inset_spec},{bg_spec}"
    ]

    # Row striping (respects row_striping_include_stub)
    # Compute header row count so we can offset the fill function to skip header rows.
    # Header rows: heading (0 or 1) + spanner levels + column labels (0 or 1)
    has_heading = heading_has_title(data._heading.title)
    spanner_levels = _get_spanners_matrix_height(data=data, omit_columns_row=True)
    col_labels_visible = not opts.column_labels_hidden.value
    header_row_count = (1 if has_heading else 0) + spanner_levels + (1 if col_labels_visible else 0)

    striping_opt = opts.row_striping_include_table_body.value
    if striping_opt:
        stripe_color = opts.row_striping_background_color.value
        if stripe_color:
            typst_color = f'rgb("{stripe_color}")' if stripe_color.startswith("#") else stripe_color
        else:
            typst_color = "luma(244)"
        include_stub = opts.row_striping_include_stub.value
        # Offset y by header_row_count so striping starts at the first data row
        if has_stub and not include_stub:
            parts.append(
                f"  fill: (x, y) => if y >= {header_row_count} and calc.odd(y - {header_row_count}) and x > 0 {{ {typst_color} }},"
            )
        else:
            parts.append(
                f"  fill: (_, y) => if y >= {header_row_count} and calc.odd(y - {header_row_count}) {{ {typst_color} }},"
            )

    # Column labels vertical lines
    col_vlines = _option_border_to_typst(
        opts.column_labels_vlines_style.value,
        opts.column_labels_vlines_width.value,
        opts.column_labels_vlines_color.value,
    )

    # Vertical and horizontal lines between cells (override stroke: none)
    vlines = _option_border_to_typst(
        opts.table_body_vlines_style.value,
        opts.table_body_vlines_width.value,
        opts.table_body_vlines_color.value,
    )
    hlines_body = _option_border_to_typst(
        opts.table_body_hlines_style.value,
        opts.table_body_hlines_width.value,
        opts.table_body_hlines_color.value,
    )
    # Column label vlines apply to header; use body vlines as fallback
    effective_vlines = vlines or col_vlines
    if effective_vlines or hlines_body:
        x_stroke = effective_vlines or "none"
        y_stroke = hlines_body or "none"
        parts[0] = parts[0].replace("stroke: none", f"stroke: (x: {x_stroke}, y: {y_stroke})")

    # Top table border
    top_border = _option_border_to_typst(
        opts.table_border_top_style.value,
        opts.table_border_top_width.value,
        opts.table_border_top_color.value,
    )
    if top_border and opts.table_border_top_include.value:
        parts.append(f"  table.hline(stroke: {top_border}),")

    # Left/right table borders
    left_border = _option_border_to_typst(
        opts.table_border_left_style.value,
        opts.table_border_left_width.value,
        opts.table_border_left_color.value,
    )
    right_border = _option_border_to_typst(
        opts.table_border_right_style.value,
        opts.table_border_right_width.value,
        opts.table_border_right_color.value,
    )
    if left_border:
        parts.append(f"  table.vline(x: 0, stroke: {left_border}),")
    if right_border:
        n_cols = len(col_aligns)
        parts.append(f"  table.vline(x: {n_cols}, stroke: {right_border}),")

    return "\n".join(parts)


def create_heading_component_typst(data: GTData, n_cols: int) -> str:
    """Create the Typst heading as table cells that span all columns.

    Returns table.cell rows to be placed inside the #table() before the header,
    so the heading inherits the table's natural width.
    """

    opts = data._options
    title = data._heading.title
    subtitle = data._heading.subtitle

    has_title = heading_has_title(title)

    if not has_title:
        return ""

    title_str = _process_text(title, context="typst")

    # Heading options

    heading_align = opts.heading_align.value or "center"
    title_size = _css_length_to_typst_text_size(opts.heading_title_font_size.value)
    title_weight = opts.heading_title_font_weight.value
    title_text_props = f"size: {title_size}"
    if title_weight and title_weight != "initial":
        title_text_props += f', weight: "{_css_weight_to_typst(title_weight)}"'
    else:
        title_text_props += ', weight: "bold"'

    bg_color = opts.heading_background_color.value
    padding = _css_length_to_typst(opts.heading_padding.value)
    padding_h = _css_length_to_typst(opts.heading_padding_horizontal.value)

    # Use light text color when heading has a background color
    heading_text_fill = ""
    if bg_color:
        font_color_light = opts.table_font_color_light.value or "#FFFFFF"
        heading_text_fill = f', fill: rgb("{font_color_light}")'
        title_text_props += heading_text_fill

    # Build cell properties
    cell_props = [f"colspan: {n_cols}", f"align: {heading_align}"]
    if bg_color:
        typst_bg = f'rgb("{bg_color}")' if bg_color.startswith("#") else bg_color
        cell_props.append(f"fill: {typst_bg}")
    cell_props.append(f"inset: (x: {padding_h}, y: {padding})")

    parts: list[str] = []

    # Title as a table.cell spanning all columns
    title_content = f"#text({title_text_props})[{title_str}]"
    if heading_has_subtitle(subtitle):
        subtitle_str = _process_text(subtitle, context="typst")
        subtitle_size = _css_length_to_typst_text_size(opts.heading_subtitle_font_size.value)
        subtitle_weight = opts.heading_subtitle_font_weight.value
        subtitle_text_props = f"size: {subtitle_size}"
        if subtitle_weight and subtitle_weight != "initial":
            subtitle_text_props += f', weight: "{_css_weight_to_typst(subtitle_weight)}"'
        subtitle_text_props += heading_text_fill
        title_content += f" \\ #text({subtitle_text_props})[{subtitle_str}]"

    parts.append(f"  table.cell({', '.join(cell_props)})[{title_content}],")

    # Heading border bottom
    heading_border = _option_border_to_typst(
        opts.heading_border_bottom_style.value,
        opts.heading_border_bottom_width.value,
        opts.heading_border_bottom_color.value,
    )
    if heading_border:
        parts.append(f"  table.hline(stroke: {heading_border}),")

    return "\n".join(parts)


def create_columns_component_typst(data: GTData) -> str:
    """Create the Typst column headers and spanners with GT-style borders."""

    opts = data._options
    spanner_row_count = _get_spanners_matrix_height(data=data, omit_columns_row=True)

    # Check for stub column (includes summary-only stubs)
    has_stub = _has_stub_column(data)

    # Get column headings
    headings_labels = data._boxhead._get_default_column_labels()
    headings_labels = [_process_text(x, context="typst") for x in headings_labels]

    rows: list[str] = []

    # Build spanner rows if they exist
    if spanner_row_count > 0:
        boxhead = data._boxhead

        spanners, _ = spanners_print_matrix(
            spanners=data._spanners,
            boxhead=boxhead,
            include_hidden=False,
            ids=False,
            omit_columns_row=True,
        )

        for spanners_row in spanners:
            spanners_row = {k: "" if v is None else v for k, v in spanners_row.items()}

            spanner_ids_index = spanners_row.values()
            spanners_rle = seq_groups(seq=spanner_ids_index)

            group_spans = [[x[1]] + [0] * (x[1] - 1) for x in spanners_rle]
            colspans = chain.from_iterable(group_spans)

            level_i_spanners = (
                _process_text(span_label, context="typst") if span_label else None
                for colspan, span_label in zip(colspans, spanners_row.values())
                if colspan > 0
            )

            spanner_cells = []
            spanner_hlines = []
            col_accumulator = 1 if has_stub else 0  # offset for stub column

            for j, level_i_spanner_j in enumerate(level_i_spanners):
                span = group_spans[j][0]
                if level_i_spanner_j is None:
                    # Empty cells for non-spanned columns
                    spanner_cells.extend(["[]"] * span)
                else:
                    spanner_cells.append(
                        f"table.cell(colspan: {span}, align: center)[{level_i_spanner_j}]"
                    )
                    # Track position for partial hline under this spanner
                    spanner_hlines.append(
                        f'  table.hline(start: {col_accumulator}, end: {col_accumulator + span}, stroke: 0.75pt + rgb("#D3D3D3")),'
                    )
                col_accumulator += span

            rows.append("  " + ", ".join(spanner_cells) + ",")
            rows.extend(spanner_hlines)

    # Column label font weight — only bold-wrap if weight is "bold"
    col_label_weight = opts.column_labels_font_weight.value
    use_bold_labels = col_label_weight == "bold"

    # Column labels hidden
    if opts.column_labels_hidden.value:
        return ""

    # Column label text transform
    col_text_transform = opts.column_labels_text_transform.value

    # Build header row with column labels
    header_cells: list[str] = []
    if has_stub:
        header_cells.append("[]")  # blank cell for stub column

    # Column label background color and padding
    col_label_bg = opts.column_labels_background_color.value
    col_label_pad = opts.column_labels_padding.value
    col_label_pad_h = opts.column_labels_padding_horizontal.value
    # Check if padding differs from default data row padding
    has_custom_pad = col_label_pad != "5px" or col_label_pad_h != "5px"

    for label in headings_labels:
        # Apply text transform
        if col_text_transform == "uppercase":
            label = label.upper()
        elif col_text_transform == "lowercase":
            label = label.lower()
        elif col_text_transform == "capitalize":
            label = label.title()

        # Column label font size
        col_label_font_size = opts.column_labels_font_size.value
        if col_label_font_size and col_label_font_size != "100%":
            label = f"#text(size: {_css_length_to_typst_text_size(col_label_font_size)})[{label}]"
        cell_content = f"*{label}*" if use_bold_labels else label
        cell_props: list[str] = []
        if col_label_bg:
            typst_bg = f'rgb("{col_label_bg}")' if col_label_bg.startswith("#") else col_label_bg
            cell_props.append(f"fill: {typst_bg}")
        if has_custom_pad:
            cell_props.append(
                f"inset: (x: {_css_length_to_typst(col_label_pad_h)}, y: {_css_length_to_typst(col_label_pad)})"
            )
        if cell_props:
            header_cells.append(f"table.cell({', '.join(cell_props)})[{cell_content}]")
        else:
            header_cells.append(f"[{cell_content}]")

    rows.append("  " + ", ".join(header_cells) + ",")

    # Column label borders
    col_border_top = _option_border_to_typst(
        opts.column_labels_border_top_style.value,
        opts.column_labels_border_top_width.value,
        opts.column_labels_border_top_color.value,
    )
    col_border_bottom = _option_border_to_typst(
        opts.column_labels_border_bottom_style.value,
        opts.column_labels_border_bottom_width.value,
        opts.column_labels_border_bottom_color.value,
    )
    col_border_lr = _option_border_to_typst(
        opts.column_labels_border_lr_style.value,
        opts.column_labels_border_lr_width.value,
        opts.column_labels_border_lr_color.value,
    )

    # Wrap in table.header() with borders
    header_content = "\n".join(rows)
    result = "  table.header(\n"
    if col_border_top:
        result += f"  table.hline(stroke: {col_border_top}),\n"
    if col_border_lr:
        result += f"  table.vline(x: 0, stroke: {col_border_lr}),\n"
        n_header_cols = len(headings_labels) + (1 if has_stub else 0)
        result += f"  table.vline(x: {n_header_cols}, stroke: {col_border_lr}),\n"
    result += f"{header_content}\n  ),"
    if col_border_bottom:
        result += f"\n  table.hline(stroke: {col_border_bottom}),"
    return result


def _get_cell_styles_typst(data: GTData, rownum: int, colname: str) -> dict[str, str]:
    """Collect Typst style properties for a specific cell from all matching StyleInfo entries."""
    from ._locations import LocBody

    merged: dict[str, str] = {}
    for style_info in data._styles:
        # Match body styles by row and column
        if not isinstance(style_info.locname, LocBody):
            continue
        if style_info.rownum is not None and style_info.rownum != rownum:
            continue
        if style_info.colname is not None and style_info.colname != colname:
            continue
        for cell_style in style_info.styles:
            try:
                merged.update(cell_style._to_typst_style())
            except NotImplementedError:
                pass
    return merged


def _get_grand_summary_cell_styles_typst(
    data: GTData, rownum: int, colname: str | None, is_stub: bool
) -> dict[str, str]:
    """Collect Typst style properties for a grand summary cell."""
    from ._locations import LocGrandSummary, LocGrandSummaryStub

    loc_cls = LocGrandSummaryStub if is_stub else LocGrandSummary
    merged: dict[str, str] = {}
    for style_info in data._styles:
        if not isinstance(style_info.locname, loc_cls):
            continue
        if style_info.rownum is not None and style_info.rownum != rownum:
            continue
        if not is_stub and style_info.colname is not None and style_info.colname != colname:
            continue
        for cell_style in style_info.styles:
            try:
                merged.update(cell_style._to_typst_style())
            except NotImplementedError:
                pass
    return merged


def _typst_styled_cell(content: str, styles: dict[str, str]) -> str:
    """Wrap a cell content string with Typst styling."""
    if not styles:
        return f"[{content}]"

    props: list[str] = []
    if "fill" in styles:
        props.append(f"fill: {styles['fill']}")
    if "stroke" in styles:
        props.append(f"stroke: {styles['stroke']}")
    if "inset" in styles:
        props.append(f"inset: {styles['inset']}")

    # Apply text decorations and transforms as outer wraps
    wrapped_content = content
    if "text_decorate" in styles:
        for deco in styles["text_decorate"].split(","):
            wrapped_content = f"#{deco}[{wrapped_content}]"
    if "text_transform" in styles:
        wrapped_content = f"#{styles['text_transform']}[{wrapped_content}]"

    if "text_style" in styles:
        # Inside [...] we're in markup mode, so need # prefix for code expressions
        inner = f"[#text({styles['text_style']})[{wrapped_content}]]"
    else:
        inner = f"[{wrapped_content}]"

    if props:
        # table.cell(fill: ..., stroke: ...)[content]
        return f"table.cell({', '.join(props)}){inner}"

    if "text_style" in styles:
        # Even without fill/stroke, text styling requires table.cell() wrapper
        # because bare #text() in table args is code context where # is invalid
        return f"table.cell(){inner}"

    return inner


def _create_grand_summary_rows_typst(
    data: GTData,
    summary_rows: list,
    column_vars: list,
    has_row_stub: bool,
    row_index_offset: int,
) -> list[str]:
    """Render grand summary rows as Typst table cells."""
    opts = data._options
    gs_bg = opts.grand_summary_row_background_color.value
    gs_text_transform = opts.grand_summary_row_text_transform.value
    gs_padding = opts.grand_summary_row_padding.value
    gs_padding_h = opts.grand_summary_row_padding_horizontal.value
    has_custom_gs_pad = gs_padding != "8px" or gs_padding_h != "5px"
    rows: list[str] = []
    for i, summary_row in enumerate(summary_rows):
        row_index = row_index_offset + i
        cells: list[str] = []

        # Stub column: summary row label
        if has_row_stub:
            stub_styles = _get_grand_summary_cell_styles_typst(
                data, rownum=row_index, colname=None, is_stub=True
            )
            if gs_bg and "fill" not in stub_styles:
                typst_bg = f'rgb("{gs_bg}")' if gs_bg.startswith("#") else gs_bg
                stub_styles["fill"] = typst_bg
            if has_custom_gs_pad:
                stub_styles["inset"] = (
                    f"(x: {_css_length_to_typst(gs_padding_h)}, y: {_css_length_to_typst(gs_padding)})"
                )
            label = summary_row.id
            if gs_text_transform == "uppercase":
                label = label.upper()
            cells.append(_typst_styled_cell(f"*{label}*", stub_styles))

        # Data columns
        for colinfo in column_vars:
            cell_value = summary_row.values.get(colinfo.var)
            cell_str = str(cell_value) if cell_value is not None else ""
            cell_styles = _get_grand_summary_cell_styles_typst(
                data, rownum=row_index, colname=colinfo.var, is_stub=False
            )
            if gs_bg and "fill" not in cell_styles:
                typst_bg = f'rgb("{gs_bg}")' if gs_bg.startswith("#") else gs_bg
                cell_styles["fill"] = typst_bg
            if has_custom_gs_pad:
                cell_styles["inset"] = (
                    f"(x: {_css_length_to_typst(gs_padding_h)}, y: {_css_length_to_typst(gs_padding)})"
                )
            cells.append(_typst_styled_cell(cell_str, cell_styles))

        rows.append("  " + ", ".join(cells) + ",")
    return rows


def create_body_component_typst(data: GTData) -> str:
    """Create the Typst table body rows."""

    _str_orig_data = cast_frame_to_string(data._tbl_data)
    tbl_data = replace_null_frame(data._body.body, _str_orig_data)

    column_vars = data._boxhead._get_default_columns()
    n_data_cols = len(column_vars)

    # Check for stub and group features
    has_row_stub = _has_stub_column(data)
    has_groups = len(data._stub.group_ids) > 0

    # Total columns including stub
    total_cols = n_data_cols + (1 if has_row_stub else 0)

    body_rows: list[str] = []
    opts = data._options

    # Grand summary border (used for top and bottom separators)
    gs_border_early = _option_border_to_typst(
        opts.grand_summary_row_border_style.value,
        opts.grand_summary_row_border_width.value,
        opts.grand_summary_row_border_color.value,
    )
    gs_hline_early = gs_border_early or '0.75pt + rgb("#D3D3D3")'

    # Render top-side grand summary rows
    top_g_summary_rows = data._summary_rows_grand.get_summary_rows(side="top")
    if top_g_summary_rows:
        body_rows.extend(
            _create_grand_summary_rows_typst(
                data, top_g_summary_rows, column_vars, has_row_stub, row_index_offset=0
            )
        )
        body_rows.append(f"  table.hline(stroke: {gs_hline_early}),")

    ordered_index: list[tuple[int, GroupRowInfo | None]] = data._stub.group_indices_map()

    prev_group_info = None
    stub_col = data._boxhead._get_stub_column()

    # Row group styling options
    rg_bg = opts.row_group_background_color.value
    rg_weight = opts.row_group_font_weight.value
    rg_use_bold = rg_weight == "bold" or rg_weight == "initial"  # default is bold-like
    rg_font_size = opts.row_group_font_size.value
    rg_text_transform = opts.row_group_text_transform.value
    rg_padding = opts.row_group_padding.value
    rg_padding_h = opts.row_group_padding_horizontal.value

    # Row group border options
    rg_border_top = _option_border_to_typst(
        opts.row_group_border_top_style.value,
        opts.row_group_border_top_width.value,
        opts.row_group_border_top_color.value,
    )
    rg_border_bottom = _option_border_to_typst(
        opts.row_group_border_bottom_style.value,
        opts.row_group_border_bottom_width.value,
        opts.row_group_border_bottom_color.value,
    )
    rg_border_left = _option_border_to_typst(
        opts.row_group_border_left_style.value,
        opts.row_group_border_left_width.value,
        opts.row_group_border_left_color.value,
    )
    rg_border_right = _option_border_to_typst(
        opts.row_group_border_right_style.value,
        opts.row_group_border_right_width.value,
        opts.row_group_border_right_color.value,
    )

    # row_group_as_column
    _rg_as_column = opts.row_group_as_column.value  # noqa: F841

    # Stub styling options
    stub_bg = opts.stub_background_color.value
    stub_weight = opts.stub_font_weight.value
    stub_use_bold = stub_weight == "bold" or stub_weight == "initial"
    stub_font_size = opts.stub_font_size.value
    stub_text_transform = opts.stub_text_transform.value
    stub_border = _option_border_to_typst(
        opts.stub_border_style.value,
        opts.stub_border_width.value,
        opts.stub_border_color.value,
    )
    # row_striping_include_stub is handled in create_table_start_typst

    # Stub row group styling (used when row_group_as_column=True, not yet implemented)
    _stub_rg_bg = opts.stub_row_group_background_color.value  # noqa: F841
    _stub_rg_font_size = opts.stub_row_group_font_size.value  # noqa: F841
    _stub_rg_weight = opts.stub_row_group_font_weight.value  # noqa: F841
    _stub_rg_text_transform = opts.stub_row_group_text_transform.value  # noqa: F841
    _stub_rg_border = _option_border_to_typst(  # noqa: F841
        opts.stub_row_group_border_style.value,
        opts.stub_row_group_border_width.value,
        opts.stub_row_group_border_color.value,
    )

    # Table body borders
    body_border_top = _option_border_to_typst(
        opts.table_body_border_top_style.value,
        opts.table_body_border_top_width.value,
        opts.table_body_border_top_color.value,
    )
    body_border_bottom = _option_border_to_typst(
        opts.table_body_border_bottom_style.value,
        opts.table_body_border_bottom_width.value,
        opts.table_body_border_bottom_color.value,
    )

    if body_border_top:
        body_rows.append(f"  table.hline(stroke: {body_border_top}),")

    for i, group_info in ordered_index:
        # Insert group label row if this is a new group
        if has_groups and group_info is not prev_group_info and group_info is not None:
            group_label = group_info.defaulted_label()
            group_label = _process_text(group_label, context="typst")
            # Apply text transform
            if rg_text_transform == "uppercase":
                group_label = group_label.upper()
            elif rg_text_transform == "lowercase":
                group_label = group_label.lower()
            elif rg_text_transform == "capitalize":
                group_label = group_label.title()
            label_content = f"*{group_label}*" if rg_use_bold else group_label
            # Wrap in text() if custom font size
            if rg_font_size and rg_font_size != "100%":
                label_content = (
                    f"#text(size: {_css_length_to_typst_text_size(rg_font_size)})[{label_content}]"
                )
            cell_props = [f"colspan: {total_cols}", "align: left"]
            if rg_bg:
                typst_bg = f'rgb("{rg_bg}")' if rg_bg.startswith("#") else rg_bg
                cell_props.append(f"fill: {typst_bg}")
            has_custom_rg_pad = rg_padding != "8px" or rg_padding_h != "5px"
            if has_custom_rg_pad:
                cell_props.append(
                    f"inset: (x: {_css_length_to_typst(rg_padding_h)}, y: {_css_length_to_typst(rg_padding)})"
                )
            # Row group stroke (left/right applied to the cell itself)
            rg_stroke_parts: list[str] = []
            if rg_border_left:
                rg_stroke_parts.append(f"left: {rg_border_left}")
            if rg_border_right:
                rg_stroke_parts.append(f"right: {rg_border_right}")
            if rg_stroke_parts:
                cell_props.append(f"stroke: ({', '.join(rg_stroke_parts)})")
            if rg_border_top:
                body_rows.append(f"  table.hline(stroke: {rg_border_top}),")
            body_rows.append(f"  table.cell({', '.join(cell_props)})[{label_content}],")
            if rg_border_bottom:
                body_rows.append(f"  table.hline(stroke: {rg_border_bottom}),")

        prev_group_info = group_info

        body_cells: list[str] = []

        # Add stub (row name) cell if present
        if has_row_stub:
            if stub_col is not None:
                row_label = str(_get_cell(tbl_data, i, stub_col.var))
                # Apply text transform
                if stub_text_transform == "uppercase":
                    row_label = row_label.upper()
                elif stub_text_transform == "lowercase":
                    row_label = row_label.lower()
                elif stub_text_transform == "capitalize":
                    row_label = row_label.title()
                label_content = f"*{row_label}*" if stub_use_bold else row_label
                # Apply font size
                if stub_font_size and stub_font_size != "100%":
                    label_content = f"#text(size: {_css_length_to_typst_text_size(stub_font_size)})[{label_content}]"
                stub_cell_props: list[str] = []
                if stub_bg:
                    typst_bg = f'rgb("{stub_bg}")' if stub_bg.startswith("#") else stub_bg
                    stub_cell_props.append(f"fill: {typst_bg}")
                if stub_border:
                    stub_cell_props.append(f"stroke: (right: {stub_border})")
                if stub_cell_props:
                    body_cells.append(f"table.cell({', '.join(stub_cell_props)})[{label_content}]")
                else:
                    body_cells.append(f"[{label_content}]")
            else:
                # Summary-only stub: emit empty cell for data rows
                body_cells.append("[]")

        for colinfo in column_vars:
            cell_content = _get_cell(tbl_data, i, colinfo.var)
            cell_str: str = str(cell_content)

            # Get styles for this cell
            cell_styles = _get_cell_styles_typst(data, rownum=i, colname=colinfo.var)
            body_cells.append(_typst_styled_cell(cell_str, cell_styles))

        body_rows.append("  " + ", ".join(body_cells) + ",")

    # Grand summary border
    gs_border = _option_border_to_typst(
        opts.grand_summary_row_border_style.value,
        opts.grand_summary_row_border_width.value,
        opts.grand_summary_row_border_color.value,
    )
    gs_hline = gs_border or '0.75pt + rgb("#D3D3D3")'

    # Render bottom-side grand summary rows
    bottom_g_summary_rows = data._summary_rows_grand.get_summary_rows(side="bottom")
    if bottom_g_summary_rows:
        # Grand summary border replaces body_border_bottom
        body_rows.append(f"  table.hline(stroke: {gs_hline}),")
        body_rows.extend(
            _create_grand_summary_rows_typst(
                data,
                bottom_g_summary_rows,
                column_vars,
                has_row_stub,
                row_index_offset=len(top_g_summary_rows),
            )
        )
    elif body_border_bottom:
        body_rows.append(f"  table.hline(stroke: {body_border_bottom}),")

    return "\n".join(body_rows)


def create_footer_component_typst(data: GTData, n_cols: int) -> str:
    """Create the Typst footer as table.cell rows inside the table.

    Returns table.cell(colspan: N) entries for source notes, placed inside the
    #table() after body rows. This way the footer inherits the table's width
    and an explicit fill prevents table-level striping from leaking in.
    """

    opts = data._options
    source_notes = data._source_notes

    if len(source_notes) == 0:
        return ""

    source_notes_strs = [_process_text(x, context="typst") for x in source_notes]

    # Source notes options
    sn_font_size = _css_length_to_typst_text_size(opts.source_notes_font_size.value)
    sn_bg = opts.source_notes_background_color.value
    sn_multiline = opts.source_notes_multiline.value
    sn_sep = opts.source_notes_sep.value or " "
    sn_padding = _css_length_to_typst(opts.source_notes_padding.value)
    sn_pad_h = _css_length_to_typst(opts.source_notes_padding_horizontal.value)

    if sn_multiline:
        notes_parts = [f"#text(size: {sn_font_size})[{note}]" for note in source_notes_strs]
        notes_content = r" \ ".join(notes_parts)
    else:
        joined = sn_sep.join(source_notes_strs)
        notes_content = f"#text(size: {sn_font_size})[{joined}]"

    # Build table.cell properties
    cell_props = [f"colspan: {n_cols}", "align: left"]

    # Always set fill to prevent table-level striping from leaking into footer
    if sn_bg:
        typst_bg = f'rgb("{sn_bg}")' if sn_bg.startswith("#") else sn_bg
    else:
        tbl_bg = opts.table_background_color.value or "#FFFFFF"
        typst_bg = f'rgb("{tbl_bg}")' if tbl_bg.startswith("#") else tbl_bg
    cell_props.append(f"fill: {typst_bg}")

    cell_props.append(f"inset: (x: {sn_pad_h}, y: {sn_padding})")

    # Borders via stroke on the cell
    sn_border_bottom = _option_border_to_typst(
        opts.source_notes_border_bottom_style.value,
        opts.source_notes_border_bottom_width.value,
        opts.source_notes_border_bottom_color.value,
    )
    sn_border_lr = _option_border_to_typst(
        opts.source_notes_border_lr_style.value,
        opts.source_notes_border_lr_width.value,
        opts.source_notes_border_lr_color.value,
    )
    stroke_parts: list[str] = []
    if sn_border_bottom:
        stroke_parts.append(f"bottom: {sn_border_bottom}")
    if sn_border_lr:
        stroke_parts.append(f"left: {sn_border_lr}")
        stroke_parts.append(f"right: {sn_border_lr}")
    if stroke_parts:
        cell_props.append(f"stroke: ({', '.join(stroke_parts)})")

    return f"  table.cell({', '.join(cell_props)})[{notes_content}],"


def _render_as_typst(data: GTData) -> str:
    """Render a GTData object as a Typst string."""

    opts = data._options

    # Create table start with column specs
    table_start = create_table_start_typst(data=data)

    # Compute total column count for heading colspan
    has_stub = _has_stub_column(data)
    n_data_cols = len(data._boxhead._get_default_columns())
    n_cols = n_data_cols + (1 if has_stub else 0)

    # Create heading as table cells (inside table, before header)
    heading_component = create_heading_component_typst(data=data, n_cols=n_cols)

    # Create column headers (inside table)
    columns_component = create_columns_component_typst(data=data)

    # Create body rows (inside table)
    body_component = create_body_component_typst(data=data)

    # Create footer as table.cell rows (inside table, after body)
    footer_component = create_footer_component_typst(data=data, n_cols=n_cols)

    # Bottom table border (inside table, at the end)
    bottom_border = _option_border_to_typst(
        opts.table_border_bottom_style.value,
        opts.table_border_bottom_width.value,
        opts.table_border_bottom_color.value,
    )
    bottom_hline = ""
    if bottom_border and opts.table_border_bottom_include.value:
        bottom_hline = f"\n  table.hline(stroke: {bottom_border}),"

    # Assemble the table
    parts: list[str] = []

    # Text set rules (font color, size, weight, style, family)
    text_props: list[str] = []
    font_color = opts.table_font_color.value
    if font_color:
        text_props.append(f'fill: rgb("{font_color}")')

    table_font_size = opts.table_font_size.value
    if table_font_size and table_font_size != "16px":
        text_props.append(f"size: {_css_length_to_typst(table_font_size)}")

    table_font_weight = opts.table_font_weight.value
    if table_font_weight and table_font_weight != "normal":
        text_props.append(f'weight: "{_css_weight_to_typst(table_font_weight)}"')

    table_font_style = opts.table_font_style.value
    if table_font_style and table_font_style != "normal":
        text_props.append(f'style: "{table_font_style}"')

    # Typst font stack: filter out CSS-only names that Typst can't resolve,
    # but keep generic families (sans-serif, serif, monospace) which Typst supports.
    _css_only_fonts = {"-apple-system", "BlinkMacSystemFont"}

    table_font_names = opts.table_font_names.value
    if table_font_names:
        typst_fonts = [f for f in table_font_names if f not in _css_only_fonts]
        if typst_fonts:
            font_list = ", ".join(f'"{f}"' for f in typst_fonts)
            parts.append(f"#set text(font: ({font_list},))")
    # If table_font_names is empty/None, don't emit #set text(font:) —
    # this lets the table inherit the document's font settings

    if text_props:
        parts.append(f"#set text({', '.join(text_props)})")

    # table_font_color_light is used by data_color for auto-contrast text,
    # not directly in the renderer — it's consumed by _data_color/base.py
    _font_color_light = opts.table_font_color_light.value  # noqa: F841

    # Table width and margins
    table_width = opts.table_width.value
    table_margin_left = opts.table_margin_left.value
    table_margin_right = opts.table_margin_right.value

    # Assemble table: heading cells go inside table.header() so they repeat on page breaks.
    # The columns_component already wraps content in table.header(...), so inject heading there.
    if heading_component and columns_component:
        # Insert heading cells at the start of table.header()
        columns_component = columns_component.replace(
            "  table.header(\n", f"  table.header(\n{heading_component}\n", 1
        )
    elif heading_component:
        # No column headers (hidden), wrap heading in its own table.header()
        columns_component = f"  table.header(\n{heading_component}\n  ),"

    # Footer goes inside the table (as table.cell rows) before the bottom border
    footer_section = f"\n{footer_component}" if footer_component else ""
    table_content = (
        f"{table_start}\n{columns_component}\n" f"{body_component}{footer_section}{bottom_hline}\n)"
    )

    # Wrap in block if table_width or margins are set
    block_props: list[str] = []
    if table_width and table_width != "auto":
        block_props.append(f"width: {_css_length_to_typst(table_width)}")
    if table_margin_left and table_margin_left != "auto":
        block_props.append(f"inset: (left: {_css_length_to_typst(table_margin_left)})")
    if table_margin_right and table_margin_right != "auto":
        if table_margin_left and table_margin_left != "auto":
            block_props[-1] = (
                f"inset: (left: {_css_length_to_typst(table_margin_left)}, "
                f"right: {_css_length_to_typst(table_margin_right)})"
            )
        else:
            block_props.append(f"inset: (right: {_css_length_to_typst(table_margin_right)})")
    if block_props:
        table_content = f"#block({', '.join(block_props)})[\n{table_content}\n]"

    parts.append(table_content)

    return "\n".join(parts)
