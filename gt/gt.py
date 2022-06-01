from typing import List, Dict, Any
from gt import (
    _tbl_data,
    _boxhead,
    _stub,
    _row_groups,
    _heading,
    _stubhead,
    _source_notes,
    _footnotes,
)

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
    _boxhead.BoxheadAPI,
    _stub.StubAPI,
    _row_groups.RowGroupsAPI,
    _heading.HeadingAPI,
    _stubhead.StubheadAPI,
    _source_notes.SourceNotesAPI,
    _footnotes.FootnotesAPI,
):
    """
    Create a gt Table object
    Methods:
    --------
        render: Returns the HTML table.

    Examples:
    ---------
        >>> from gt import *
        >>> x = GT([{"a": 5, "b": 10}, {"a": 15, "b": 20}])
        >>> x
        >>> print(x)
    """

    def __init__(self, data: Any, locale: str = ""):

        _tbl_data.TblDataAPI.__init__(self, data)
        _boxhead.BoxheadAPI.__init__(self, data)
        _stub.StubAPI.__init__(self, data)
        _row_groups.RowGroupsAPI.__init__(self)
        _heading.HeadingAPI.__init__(self)
        _stubhead.StubheadAPI.__init__(self)
        _source_notes.SourceNotesAPI.__init__(self)
        _footnotes.FootnotesAPI.__init__(self)

        # Table parts
        self._spanners: Dict[str, Any]

        self._formats: Dict[str, Any]
        self._styles: Dict[str, Any]
        self._summary: Dict[str, Any]
        self._options: Dict[str, Any]
        self._transforms: Dict[str, Any]
        self._locale: str = _locale_init(locale)
        self._has_built: bool = _has_built_init()
        self._rendered_tbl: str = _rendered_tbl_init()

    def render(self) -> str:
        self = self._build_data()
        html_table = self._render_as_html()
        return html_table

    def _build_data(self):
        return self

    # =============================================================================
    # HTML Rendering
    # =============================================================================
    def _render_as_html(self) -> str:

        heading_component = self._heading.create_heading_component()
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

        return html_table


# =============================================================================
# Initialization Functions
# =============================================================================


def _locale_init(locale: str) -> str:
    if locale is None:
        locale = "en"
    return locale


def _has_built_init() -> bool:
    return False


def _rendered_tbl_init() -> str:
    return ""


# =============================================================================
# Table Structuring Functions
# =============================================================================


def _create_column_labels_component(data: GT) -> str:

    tbl_data = data._tbl_data

    column_names = tbl_data.columns

    th_cells = "".join([f"  <th>{x}</th>\n" for x in column_names])

    column_names_str = f"<tr>\n{th_cells}</tr>"

    return column_names_str


def _create_body_component(data: GT):

    tbl_data = data._tbl_data

    column_names = tbl_data.columns

    body_rows: List[str] = []

    for i in range(tbl_data.rows):

        body_cells: List[str] = []

        for name in column_names:

            cell_content: Any = tbl_data.get_cell(i, name)
            cell_str: str = str(cell_content)

            body_cells.append("  <td>" + cell_str + "</td>")

        body_rows.append("<tr>\n" + "\n".join(body_cells) + "\n</tr>")

    return "\n".join(body_rows)


def _create_source_notes_component(data: GT):
    return ""


def _create_footnotes_component(data: GT):
    return ""
