from typing import Any, Dict, List, cast

import sass
import re
import copy

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
    _tbl_data,
)


# from ._helpers import random_id
from ._body import Body
from ._text import StringBuilder
from ._utils import _as_css_font_family_attr, _unique_set

from ._body import Context


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
    _tbl_data.TblDataAPI,
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

    def _repr_html_(self):
        return self.render(context="html")

    def __init__(self, data: Any, locale: str = ""):
        # This init will take the input data (any valid input for the Pandas
        # DataFrame class) and store the resulting DataFrame as `self._tbl_data`
        _tbl_data.TblDataAPI.__init__(self, data)

        _body.BodyAPI.__init__(self, data)
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

    def _render_formats(self, context: Context):
        self._body.render_formats(self._tbl_data, self._formats, context)
        return self

    def _build_data(self, context: Context):
        # Build the body of the table by generating a dictionary
        # of lists with cells initially set to nan values
        self = copy.copy(self)
        self._body = Body(self._body.body._tbl_data)
        self._render_formats(context)

        # body = _migrate_unformatted_to_output(body)

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

    def render(self, context: Context) -> str:
        self = self._build_data(context=context)
        html_table = self._render_as_html()
        return html_table

    # =============================================================================
    # Building
    # =============================================================================

    # def _body_build(self, data: Table):
    #     return self
    #     # data.cells[(1, 3)].set_cell_value("foo")

    # def _migrate_unformatted_to_output(self, body: Dict[Column, Any]):

    #     # Get the dictionary keys from the body as these serve as column names
    #     colnames = body.keys()

    #     for column in colnames:
    #         body[column]

    #     return body

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
{heading_component.make_string()}
{column_labels_component}
{body_component}
{source_notes_component}
{footnotes_component}
</table>
"""

        # Get a string of compiled CSS
        css = _compile_scss(data=self)

        # Obtain the `table_id` value (might be set, might be None)
        table_id = self._options._options["table_id"].value

        # Obtain options set for overflow and container dimensions
        overflow_x = self._options._options["container_overflow_x"].value
        overflow_y = self._options._options["container_overflow_y"].value
        width = self._options._options["container_width"].value
        height = self._options._options["container_height"].value

        if table_id is None:
            id_attr_str = ""
        else:
            id_attr_str = f'id="{table_id}"'

        finalized_table = f"""<div {id_attr_str} style="overflow-x:{overflow_x};overflow-y:{overflow_y};width:{width};height:{height};">
<style>
{css}
</style>
{html_table}
</div>
        """

        return finalized_table


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
    tbl_data = data._body.body

    column_names = data._boxhead._get_visible_columns()

    body_rows: List[str] = []

    for i in range(tbl_data.n_rows()):
        body_cells: List[str] = []

        for name in column_names:
            cell_content: Any = tbl_data._get_cell(i, name)
            cell_str: str = str(cell_content)

            body_cells.append('  <td class="gt_row">' + cell_str + "</td>")

        body_rows.append("<tr>\n" + "\n".join(body_cells) + "\n</tr>")

    all_body_rows = "\n".join(body_rows)

    return f'<tbody class="gt_table_body">\n{all_body_rows}\n</tbody>'


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

    compiled_css = cast(str, sass.compile(string=scss))
    if table_id is not None:
        compiled_css = re.sub(
            r"\.gt_", f"#{table_id} .gt_", compiled_css, 0, re.MULTILINE
        )

    finalized_css = f"""html {{
      {font_family_attr}
}}

{compiled_css}"""

    return finalized_css
