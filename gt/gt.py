from typing import List, Dict, Any
from gt import _heading
import pandas as pd


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
class GT(_heading.HeadingAPI):
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

    def __init__(self, data: List[Dict[str, Any]], locale: str = ""):
        _heading.HeadingAPI.__init__(self)

        # The tabular data
        self._tbl_data: List[Dict[str, Any]] = data

        # Table parts
        self._boxhead: Dict[str, Any]
        self._stub_df: Dict[str, Any]
        self._row_groups: Dict[str, Any]
        self._spanners: Dict[str, Any]
        self._stubhead: Dict[str, Any]
        self._source_notes: Dict[str, Any]
        self._footnotes: Dict[str, Any]

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
        columns_component = _create_columns_component(self)
        body_component = _create_body_component(self)
        source_notes_component = _create_source_notes_component(self)
        footnotes_component = _create_footnotes_component(self)

        html_table = f"""
            <table class=\"gt_table\">
            {heading_component}
            {columns_component}
            {body_component}
            {source_notes_component}
            {footnotes_component}
            </table>
        """

        return html_table


# =============================================================================
# Table Structuring Functions
# =============================================================================


# =============================================================================
# Initialization Functions
# =============================================================================


def _heading_init():

    heading = {"title": None, "subtitle": None, "preheader": None}
    return heading


def _locale_init(locale: str) -> str:
    if locale is None:
        locale = "en"
    return locale


def _has_built_init() -> bool:
    return False


def _rendered_tbl_init() -> str:
    return ""


def _create_columns_component(data: GT) -> str:
    return ""


def _create_body_component(data: GT):

    cell_data = data._tbl_data

    column_names = _get_column_names_from_list_dicts(table_input_data=cell_data)

    body_rows: List[str] = []

    for x in cell_data:
        # TODO: Use list comprehension
        body_cells: List[str] = []

        for y in column_names:
            body_cells.append("  <td>" + str(x[y]) + "</td>")

        body_rows.append("<tr>\n" + "\n".join(body_cells) + "\n</tr>")

    return "\n".join(body_rows)


def _create_source_notes_component(data: GT):
    return ""


def _create_footnotes_component(data: GT):
    return ""


def _uniqueify_list(a_list: List[str]) -> List[str]:
    d: Dict[str, bool] = {}
    for x in a_list:
        d[x] = True

    return list(d.keys())


def _get_column_names_from_list_dicts(
    table_input_data: List[Dict[str, Any]]
) -> List[str]:
    keys: List[str] = []
    for d in table_input_data:
        keys.extend(d)
    return _uniqueify_list(keys)
