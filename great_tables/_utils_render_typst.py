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
        return f"{val}%"
    # pt, cm, mm, in, em — Typst supports these directly
    return length


def _has_stub_column(data: GTData) -> bool:
    """Check if the table has a stub column (explicit or summary-only)."""
    has_summary_rows = bool(data._summary_rows or data._summary_rows_grand)
    stub_layout = data._stub._get_stub_layout(
        has_summary_rows=has_summary_rows, options=data._options
    )
    return "rowname" in stub_layout


def _option_border_to_typst(style: str, width: str, color: str) -> str | None:
    """Convert GT border options to Typst stroke syntax. Returns None for style='none'."""
    if style == "none":
        return None
    typst_width = _css_length_to_typst(width)
    typst_color = f'rgb("{color}")' if color.startswith("#") else color
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

    parts = [f"#table(\n  {columns_spec},\n  {align_spec},\n  stroke: none,\n  {inset_spec},"]

    # Row striping
    striping_opt = opts.row_striping_include_table_body.value
    if striping_opt:
        stripe_color = opts.row_striping_background_color.value
        if stripe_color:
            typst_color = f'rgb("{stripe_color}")' if stripe_color.startswith("#") else stripe_color
        else:
            typst_color = "luma(244)"
        parts.append(f"  fill: (_, y) => if calc.odd(y) {{ {typst_color} }},")

    # Top table border
    top_border = _option_border_to_typst(
        opts.table_border_top_style.value,
        opts.table_border_top_width.value,
        opts.table_border_top_color.value,
    )
    if top_border and opts.table_border_top_include.value:
        parts.append(f"  table.hline(stroke: {top_border}),")

    return "\n".join(parts)


def create_heading_component_typst(data: GTData) -> str:
    """Create the Typst heading (title/subtitle) above the table."""

    title = data._heading.title
    subtitle = data._heading.subtitle

    has_title = heading_has_title(title)

    if not has_title:
        return ""

    title_str = _process_text(title, context="typst")

    parts = [f'#align(center, text(size: 14pt, weight: "bold")[{title_str}])']

    if heading_has_subtitle(subtitle):
        subtitle_str = _process_text(subtitle, context="typst")
        parts.append(f"#align(center, text(size: 10pt)[{subtitle_str}])")

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

    # Build header row with column labels
    header_cells: list[str] = []
    if has_stub:
        header_cells.append("[]")  # blank cell for stub column
    header_cells.extend(f"[*{label}*]" for label in headings_labels)
    rows.append("  " + ", ".join(header_cells) + ",")

    # Column label borders
    col_border_bottom = _option_border_to_typst(
        opts.column_labels_border_bottom_style.value,
        opts.column_labels_border_bottom_width.value,
        opts.column_labels_border_bottom_color.value,
    )

    # Wrap in table.header() with border after
    header_content = "\n".join(rows)
    result = f"  table.header(\n{header_content}\n  ),"
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

    if "text_style" in styles:
        # Inside [...] we're in markup mode, so need # prefix for code expressions
        inner = f"[#text({styles['text_style']})[{content}]]"
    else:
        inner = f"[{content}]"

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
    rows: list[str] = []
    for i, summary_row in enumerate(summary_rows):
        row_index = row_index_offset + i
        cells: list[str] = []

        # Stub column: summary row label
        if has_row_stub:
            stub_styles = _get_grand_summary_cell_styles_typst(
                data, rownum=row_index, colname=None, is_stub=True
            )
            cells.append(_typst_styled_cell(f"*{summary_row.id}*", stub_styles))

        # Data columns
        for colinfo in column_vars:
            cell_value = summary_row.values.get(colinfo.var)
            cell_str = str(cell_value) if cell_value is not None else ""
            cell_styles = _get_grand_summary_cell_styles_typst(
                data, rownum=row_index, colname=colinfo.var, is_stub=False
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

    # Render top-side grand summary rows
    top_g_summary_rows = data._summary_rows_grand.get_summary_rows(side="top")
    if top_g_summary_rows:
        body_rows.extend(
            _create_grand_summary_rows_typst(
                data, top_g_summary_rows, column_vars, has_row_stub, row_index_offset=0
            )
        )
        body_rows.append('  table.hline(stroke: 0.75pt + rgb("#D3D3D3")),')

    ordered_index: list[tuple[int, GroupRowInfo | None]] = data._stub.group_indices_map()

    prev_group_info = None
    stub_col = data._boxhead._get_stub_column()

    for i, group_info in ordered_index:
        # Insert group label row if this is a new group
        if has_groups and group_info is not prev_group_info and group_info is not None:
            group_label = group_info.defaulted_label()
            group_label = _process_text(group_label, context="typst")
            body_rows.append(
                f"  table.cell(colspan: {total_cols}, align: left)" f"[*{group_label}*],"
            )

        prev_group_info = group_info

        body_cells: list[str] = []

        # Add stub (row name) cell if present
        if has_row_stub:
            if stub_col is not None:
                row_label = str(_get_cell(tbl_data, i, stub_col.var))
                body_cells.append(f"[*{row_label}*]")
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

    # Render bottom-side grand summary rows
    bottom_g_summary_rows = data._summary_rows_grand.get_summary_rows(side="bottom")
    if bottom_g_summary_rows:
        body_rows.append('  table.hline(stroke: 0.75pt + rgb("#D3D3D3")),')
        body_rows.extend(
            _create_grand_summary_rows_typst(
                data,
                bottom_g_summary_rows,
                column_vars,
                has_row_stub,
                row_index_offset=len(top_g_summary_rows),
            )
        )

    return "\n".join(body_rows)


def create_footer_component_typst(data: GTData) -> str:
    """Create the Typst footer with source notes."""

    source_notes = data._source_notes

    if len(source_notes) == 0:
        return ""

    source_notes_strs = [_process_text(x, context="typst") for x in source_notes]

    # Render source notes as text block below the table
    notes_lines = [f"#text(size: 8pt)[{note}]" for note in source_notes_strs]

    return "\n".join(notes_lines)


def _render_as_typst(data: GTData) -> str:
    """Render a GTData object as a Typst string."""

    opts = data._options

    # Create heading above the table
    heading_component = create_heading_component_typst(data=data)

    # Create table start with column specs
    table_start = create_table_start_typst(data=data)

    # Create column headers (inside table)
    columns_component = create_columns_component_typst(data=data)

    # Create body rows (inside table)
    body_component = create_body_component_typst(data=data)

    # Create footer (outside table)
    footer_component = create_footer_component_typst(data=data)

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

    # Text color and font size set rules
    font_color = opts.table_font_color.value
    if font_color:
        parts.append(f'#set text(fill: rgb("{font_color}"))')

    table_font_size = opts.table_font_size.value
    if table_font_size and table_font_size != "16px":
        typst_size = _css_length_to_typst(table_font_size)
        parts.append(f"#set text(size: {typst_size})")

    if heading_component:
        parts.append(heading_component)

    # Table body with bottom border
    table_content = f"{table_start}\n{columns_component}\n{body_component}{bottom_hline}\n)"
    parts.append(table_content)

    if footer_component:
        parts.append(footer_component)

    return "\n".join(parts)
