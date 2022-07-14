from typing import Any, Dict, List, cast

import sass
import re

from gt import (
    _body,
    _boxhead,
    _footnotes,
    _formats,
    _heading,
    _locale,
    _options,
    _row_groups,
    _source_notes,
    _spanners,
    _stub,
    _stubhead,
    _styles,
    _utils,
)

from ._table import Table
from ._tbl_data import TblDataAPI
from ._text import StringBuilder
from ._utils import _as_css_font_family_attr, _unique_set

__all__ = ["GT"]

# Architecture of GT:
# 1. GT class for holding all user specified directives (internally
#    implemented using multiple smaller modules)
# 2. Build step that performs mostly-context-agnostic pre-rendering tasks.
#    State from GT class is transformed into input for the render step.
# 3. Render into final output.

# =============================================================================
# GT class
# =============================================================================
class GT(
    TblDataAPI,
    _body.BodyAPI,
    _boxhead.BoxheadAPI,
    _stub.StubAPI,
    _row_groups.RowGroupsAPI,
    _spanners.SpannersAPI,
    _heading.HeadingAPI,
    _stubhead.StubheadAPI,
    _source_notes.SourceNotesAPI,
    _footnotes.FootnotesAPI,
    _styles.StylesAPI,
    _locale.LocaleAPI,
    _formats.FormatsAPI,
    _options.OptionsAPI,
):
    """
    Create a gt Table object.

    Methods
    -------
        render: Renders and returns the HTML table.

    Examples
    --------
        >>> from gt import *
        >>> x = GT([{"a": 5, "b": 10}, {"a": 15, "b": 20}])
        >>> x
        >>> print(x)
    """

    def __init__(self, data: Any, locale: str = ""):

        TblDataAPI.__init__(self, data)

        _body.BodyAPI.__init__(self)
        _boxhead.BoxheadAPI.__init__(self)
        _stub.StubAPI.__init__(self)
        _row_groups.RowGroupsAPI.__init__(self)
        _spanners.SpannersAPI.__init__(self)
        _heading.HeadingAPI.__init__(self)
        _stubhead.StubheadAPI.__init__(self)
        _source_notes.SourceNotesAPI.__init__(self)
        _footnotes.FootnotesAPI.__init__(self)
        _styles.StylesAPI.__init__(self)
        _locale.LocaleAPI.__init__(self, locale)
        _formats.FormatsAPI.__init__(self)
        _options.OptionsAPI.__init__(self)

        # Table parts
        self._transforms: Dict[str, Any]
        self._summary: Dict[str, Any]
        self._has_built: bool = _has_built_init()
        self._rendered_tbl: str = _rendered_tbl_init()

    def _build_data(self):

        # Building of the table body with cell rendering, merging
        # of cells, and row/column reordering for sake of grouping

        body = Table(self._tbl_data._tbl_data)

        self._body_build(body)
        # self._render_formats()
        # self._migrate_unformatted_to_output()
        # self._perform_col_merge()
        # self._body_reassemble()

        # Reordering of the metadata elements of the table

        # self = self.reorder_stub_df()
        # self = self.reorder_footnotes()
        # self = self.reorder_styles()

        # Transformations of individual cells at supported locations

        # self = self.perform_text_transforms()

        # ...

        return self

    def render(self) -> str:
        self = self._build_data()
        html_table = self._render_as_html()
        return html_table

    # =============================================================================
    # Building
    # =============================================================================

    def _body_build(self, data: Table):
        return self
        # data.cells[(1, 3)].set_cell_value("foo")

    # =============================================================================
    # HTML Rendering
    # =============================================================================
    def _render_as_html(self) -> str:

        heading_component = _create_heading_component(self)
        column_labels_component = _create_column_labels_component(self)
        body_component = _create_body_component(self)
        source_notes_component = _create_source_notes_component(self)
        footnotes_component = _create_footnotes_component(self)

        html_table = f"""<table class=\"gt_table\">
{heading_component}
{column_labels_component}
{body_component}
{source_notes_component}
{footnotes_component}
</table>
"""

        html_table = _compile_scss(data=self, html_table=html_table)

        return html_table


# =============================================================================
# Initialization Functions
# =============================================================================


def _has_built_init() -> bool:
    return False


def _rendered_tbl_init() -> str:
    return ""


# =============================================================================
# Table Structuring Functions
# =============================================================================


def _create_heading_component(data: GT) -> StringBuilder:

    result = StringBuilder()

    # If there is no title or heading component, then return an empty string
    if _utils.heading_has_title(title=data._heading.title) is False:
        return result

    title = data._heading.title
    subtitle_defined = _utils.heading_has_subtitle(subtitle=data._heading.subtitle)

    # Get the effective number of columns, which is number of columns
    # that will finally be rendered accounting for the stub layout
    n_cols_total = data._boxhead._get_effective_number_of_columns()

    result.append(
        f"""  <tr>
    <th colspan="{n_cols_total}" class="gt_heading gt_title gt_font_normal">{title}
  </tr>"""
    )

    if subtitle_defined:

        subtitle = data._heading.subtitle

        subtitle_row = f"""  <tr>
    <th colspan="{n_cols_total}" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">{subtitle}
  </tr>"""
        result.append(f"\n{subtitle_row}")

    return StringBuilder('<thead class="gt_header">', result, "</thead>")


def _create_column_labels_component(data: GT) -> str:

    column_names = data._boxhead._get_column_labels()

    th_cells = "".join([f"  <th>{x}</th>\n" for x in column_names])

    column_names_str = f"<tr>\n{th_cells}</tr>"

    return column_names_str


def _create_body_component(data: GT):

    tbl_data = data._tbl_data

    column_names = tbl_data.get_column_names()

    body_rows: List[str] = []

    for i in range(tbl_data.n_rows()):

        body_cells: List[str] = []

        for name in column_names:

            cell_content: Any = tbl_data._get_cell(i, name)
            cell_str: str = str(cell_content)

            body_cells.append("  <td>" + cell_str + "</td>")

        body_rows.append("<tr>\n" + "\n".join(body_cells) + "\n</tr>")

    return "\n".join(body_rows)


def _create_source_notes_component(data: GT) -> str:

    source_notes = data._source_notes.source_notes

    # If there are no source notes, then return an empty string
    if source_notes == []:
        return ""

    # Obtain the `multiline` and `separator` options from `_options`
    multiline = data._options.source_notes_multiline.value
    separator = cast(str, data._options.source_notes_sep.value)

    # Get the effective number of columns, which is number of columns
    # that will finally be rendered accounting for the stub layout
    n_cols_total = data._boxhead._get_effective_number_of_columns()

    # Handle the multiline source notes case (each note takes up one line)
    if multiline:

        # Create the source notes component as a series of `<tr><td>` (one per
        # source note) inside of a `<tfoot>`

        source_notes_tr: List[str] = []

        for note in source_notes:
            source_notes_tr.append(
                f"""
  <tr>
    <td class="gt_sourcenote" colspan="{n_cols_total}">{note}</td>
  </tr>
"""
            )

        source_notes_joined = "\n".join(source_notes_tr)

        source_notes_component = f"""  <tfoot class="gt_sourcenotes">
  {source_notes_joined}
</tfoot>"""

        return source_notes_component

    # TODO: Perform HTML escaping on the separator text and
    # transform space characters to non-breaking spaces

    # Create the source notes component as a single `<tr><td>` inside
    # of a `<tfoot>`

    source_notes_str_joined = separator.join(source_notes)

    source_notes_component = f"""<tfoot>
  <tr class="gt_sourcenotes">
    <td class="gt_sourcenote" colspan="{n_cols_total}">
      <div style="padding-bottom:2px;">{source_notes_str_joined}</div>
    </td>
  </tr>
</tfoot>
    """

    return source_notes_component


def _create_footnotes_component(data: GT):
    return ""


# TODO: Port the SCSS compilation routine from the R implementation here
def _compile_scss(data: GT) -> str:

    # Obtain the SCSS options dictionary
    gt_options_dict = data._options._options

    # Get collection of parameters that pertain to SCSS
    scss_params = [
        f"${x.parameter}: {x.value};"
        for x in gt_options_dict.values()
        if x.scss is True and x.value is not None
    ]
    scss_params_str = "\n".join(scss_params) + "\n"

    # Obtain the `table_id` value (might be set, might be None)
    table_id = gt_options_dict["table_id"].value

    has_id = table_id is not None

    # TODO: need to implement a function to normalize color (`html_color()`)

    # Get the unique list of fonts from `gt_options_dict`
    font_list = _unique_set(gt_options_dict["table_font_names"].value)

    # Generate a `font-family` string
    if font_list is not None:
        font_family_attr = _as_css_font_family_attr(fonts=font_list)
    else:
        font_family_attr = ""

    gt_styles_default_file = open("gt/css/gt_styles_default.scss")
    gt_styles_default = gt_styles_default_file.read()
    gt_styles_default = re.sub(r"\s+", " ", gt_styles_default, 0, re.MULTILINE)
    gt_styles_default = re.sub(r"}", "}\n", gt_styles_default, 0, re.MULTILINE)

    gt_colors_file = open("gt/css/gt_colors.scss")
    gt_colors = gt_colors_file.read()

    scss = scss_params_str + gt_colors + gt_styles_default
    compiled_sass = cast(str, sass.compile(string=scss))

    return compiled_sass
