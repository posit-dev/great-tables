from __future__ import annotations

from typing import Any, List, Optional, cast
from typing_extensions import Self
import pkg_resources

import sass
import re
import copy

from great_tables._gt_data import GTData

# Main gt imports ----
from great_tables import _utils

# Rewrite main gt imports to use relative imports of APIs ----
from great_tables._body import body_reassemble
from great_tables._boxhead import BoxheadAPI
from great_tables._footnotes import FootnotesAPI
from great_tables._formats import (
    FormatsAPI,
    fmt_number,
    fmt_percent,
    fmt_integer,
    fmt_scientific,
    fmt_currency,
    fmt_bytes,
    fmt_roman,
    fmt_date,
    fmt_time,
    fmt_markdown,
)
from great_tables._heading import HeadingAPI
from great_tables._locale import LocaleAPI
from great_tables._options import OptionsAPI
from great_tables._row_groups import RowGroupsAPI
from great_tables._source_notes import tab_source_note
from great_tables._spanners import (
    tab_spanner,
    cols_move,
    cols_move_to_start,
    cols_move_to_end,
    cols_hide,
)
from great_tables._stub import reorder_stub_df
from great_tables._stubhead import StubheadAPI
from great_tables._utils_render_html import (
    create_heading_component_h,
    create_columns_component_h,
    create_body_component_h,
    create_source_notes_component_h,
    create_footnotes_component_h,
)
from great_tables._helpers import random_id


# from ._helpers import random_id
# from ._body import Body
from ._text import StringBuilder, _process_text
from ._utils import _as_css_font_family_attr, _unique_set
from ._tbl_data import n_rows, _get_cell, copy_frame


# from ._body import Context


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
    GTData,
    BoxheadAPI,
    RowGroupsAPI,
    HeadingAPI,
    StubheadAPI,
    FootnotesAPI,
    LocaleAPI,
    FormatsAPI,
    OptionsAPI,
):
    """
    Create a **great_tables** object.

    The `GT()` class creates a **great_tables** object when provided with tabular data. Using this
    is the first step in a typical **great_tables** workflow. Once we have this object, we can
    perform numerous transformations before rendering to a display table.

    There are a few data ingest options we can consider at this stage. We can choose to create a
    table stub containing row labels through the use of the `rowname_col` argument. Further to this,
    stub row groups can be created with the `groupname_col` argument. Both arguments take the name
    of a column in the input table data. Typically, the data in the `groupname_col` column will
    consist of categorical text whereas the data in the `rowname_col` column will contain unique
    labels (could be unique across the entire table or unique within the different row groups).

    Parameters
    ----------
    data : Any
        A DataFrame object.
    rowname_col : str | None
        The column name in the input `data` table to use as row labels to be placed in the table
        stub.
    groupname_col : str | None
        The column name in the input `data` table to use as group labels for generation of row
        groups.
    auto_align : bool
        Optionally have column data be aligned depending on the content contained in each column of
        the input `data`.
    locale : str
        An optional locale identifier that can be set as the default locale for all functions that
        take a `locale` argument. Examples include `"en"` for English (United States) and `"fr"`
        for French (France).

    Returns
    -------
    GTData
        A GTData object is returned.

    Examples
    --------
    Let's use the `exibble` dataset for the next few examples, we'll learn how to make simple
    output tables with the `GT()` class. The most basic thing to do is to just use `GT()` with the
    dataset as the input.

    ```{python}
    import great_tables as gt

    gt.GT(gt.exibble)
    ```

    This dataset has the `row` and `group` columns. The former contains unique values that are ideal
    for labeling rows, and this often happens in what is called the 'stub' (a reserved area that
    serves to label rows). With the `GT()` class, we can immediately place the contents of the `row`
    column into the stub column. To do this, we use the `rowname_col` argument with the appropriate
    column name.

    ```{python}
    gt.GT(gt.exibble, rowname_col=\"row\")
    ```

    This sets up a table with a stub, the row labels are placed within the stub column, and a
    vertical dividing line has been placed on the right-hand side.

    The `group` column contains categorical values that are ideal for grouping rows. We can use the
    `groupname_col` argument to place these values into row groups.

    ```{python}
    gt.GT(gt.exibble, rowname_col=\"row\", groupname_col=\"group\")
    ```

    By default, values in the body of a table (and their column labels) are automatically aligned.
    The alignment is governed by the types of values in a column. If you'd like to disable this form
    of auto-alignment, the `auto_align=False` option can be taken.

    ```{python}
    gt.GT(gt.exibble, rowname_col=\"row\", auto_align=False)
    ```

    What you'll get from that is center-alignment of all table body values and all column labels.
    Note that row labels in the the stub are still left-aligned; and `auto_align` has no effect on
    alignment within the table stub.

    However which way you generate the initial table object, you can modify it with a huge variety
    of methods to further customize the presentation. Formatting body cells is commonly done with
    the family of formatting methods (e.g., `fmt_number()`, `fmt_date()`, etc.). The package
    supports formatting with internationalization ('i18n' features) and so locale-aware methods
    all come with a `locale` argument. To avoid having to use that argument repeatedly, the `GT()`
    class has its own `locale` argument. Setting a locale in that will make it available globally.
    Here's an example of how that works in practice when setting `locale = "fr"` in `GT()` prior to
    using formatting methods:

    ```{python}
    (
        gt.GT(gt.exibble, rowname_col=\"row\", locale=\"fr\")
          .fmt_currency(columns=\"currency\")
          .fmt_scientific(columns=\"num\")
          .fmt_date(columns=\"date\", date_style=\"day_month_year\")
    )
    ```

    In this example, the `fmt_currency()`, `fmt_scientific()`, and `fmt_date()` methods understand
    that the locale for this table is `"fr"` (French), so the appropriate formatting for that locale
    is apparent in the `currency`, `num`, and `date` columns.

    """

    def _repr_html_(self):
        return self.render(context="html")

    def __init__(
        self,
        data: Any,
        rowname_col: str | None = None,
        groupname_col: str | None = None,
        auto_align: bool = True,
        locale: str | None = None,
    ):
        # This is a bad idea ----
        gtdata = GTData.from_data(
            data,
            locale=locale,
            rowname_col=rowname_col,
            groupname_col=groupname_col,
            auto_align=auto_align,
        )
        super().__init__(**gtdata.__dict__)

    # TODO: Refactor API methods -----
    fmt_number = fmt_number
    fmt_integer = fmt_integer
    fmt_percent = fmt_percent
    fmt_scientific = fmt_scientific
    fmt_currency = fmt_currency
    fmt_bytes = fmt_bytes
    fmt_roman = fmt_roman
    fmt_date = fmt_date
    fmt_time = fmt_time
    fmt_markdown = fmt_markdown

    tab_spanner = tab_spanner
    tab_source_note = tab_source_note
    cols_move = cols_move
    cols_move_to_start = cols_move_to_start
    cols_move_to_end = cols_move_to_end
    cols_hide = cols_hide

    # -----

    def _get_has_built(self: GT) -> bool:
        return self._has_built

    def _render_formats(self, context: str) -> Self:
        rendered = copy.copy(self)

        # TODO: this body method performs a mutation. Should we make a copy of body?
        rendered._body.render_formats(rendered._tbl_data, rendered._formats, context)
        return rendered

    def _build_data(self, context: str) -> Self:
        # Build the body of the table by generating a dictionary
        # of lists with cells initially set to nan values
        built = self._render_formats(context)
        # built._body = _migrate_unformatted_to_output(body)

        # built._perform_col_merge()
        final_body = body_reassemble(built._body, self._row_groups, self._stub, self._boxhead)

        # Reordering of the metadata elements of the table

        final_stub = reorder_stub_df(self._stub, self._row_groups)
        # self = self.reorder_footnotes()
        # self = self.reorder_styles()

        # Transformations of individual cells at supported locations

        # self = self.perform_text_transforms()

        # ...

        return built._replace(_body=final_body, _stub=final_stub)

    def render(self, context: str) -> str:
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
        heading_component = create_heading_component_h(data=self)
        column_labels_component = create_columns_component_h(data=self)
        body_component = create_body_component_h(data=self)
        source_notes_component = create_source_notes_component_h(data=self)
        footnotes_component = create_footnotes_component_h(data=self)

        # Determine whether Quarto processing of the table is enabled
        quarto_disable_processing = self._options._get_option_value("quarto_disable_processing")
        quarto_use_bootstrap = self._options._get_option_value("quarto_use_bootstrap")
        quarto_disable_processing = str(quarto_disable_processing).lower()
        quarto_use_bootstrap = str(quarto_use_bootstrap).lower()

        html_table = f"""<table class=\"gt_table\" data-quarto-disable-processing="{quarto_disable_processing}" data-quarto-bootstrap="{quarto_use_bootstrap}">
{heading_component.make_string()}
{column_labels_component}
{body_component}
{source_notes_component}
{footnotes_component}
</table>
"""

        # Obtain the `table_id` value (might be set, might be None)
        table_id = self._options._options["table_id"].value

        if table_id is None:
            id = random_id()
        else:
            id = table_id

        # Compile the SCSS as CSS
        css = _compile_scss(data=self, id=id)

        # Obtain options set for overflow and container dimensions

        container_padding_x = self._options._get_option_value("container_padding_x")
        container_padding_y = self._options._get_option_value("container_padding_y")
        container_overflow_x = self._options._get_option_value("container_overflow_x")
        container_overflow_y = self._options._get_option_value("container_overflow_y")
        container_width = self._options._get_option_value("container_width")
        container_height = self._options._get_option_value("container_height")

        finalized_table = f"""<div id="{id}" style="padding-left:{container_padding_x};padding-right:{container_padding_x};padding-top:{container_padding_y};padding-bottom:{container_padding_y};overflow-x:{container_overflow_x};overflow-y:{container_overflow_y};width:{container_width};height:{container_height};">
<style>
{css}
</style>
{html_table}
</div>
        """

        return finalized_table


# =============================================================================
# End of GT class
# =============================================================================


# =============================================================================
# as_raw_html()
# =============================================================================


def as_raw_html(gt: GT) -> str:
    """
    Returns the GTData object as raw HTML.

    Args:
        gt (GT): The GTData object to convert to raw HTML.
        context (str): The context in which to build the output.

    Returns:
        str: The GTData object as raw HTML.
    """
    gt_built = gt._build_data(context="html")
    html_table = gt_built._render_as_html()
    return html_table


# =============================================================================
# GT Getter/Setter Functions
# =============================================================================


def _set_has_built(gt: GT, value: bool) -> GT:
    gt._has_built = value
    return gt


def _get_column_labels(gt: GT, context: str) -> List[str]:
    gt_built = gt._build_data(context=context)
    column_labels = [x.column_label for x in gt_built._boxhead]
    return column_labels


def _get_column_of_values(gt: GT, column_name: str, context: str) -> List[str]:
    gt_built = gt._build_data(context=context)
    tbl_data = gt_built._body.body
    cell_values: List[str] = []

    for i in range(n_rows(tbl_data)):
        cell_content: Any = _get_cell(tbl_data, i, column_name)
        cell_str: str = str(cell_content)
        cell_values.append(cell_str)

    return cell_values


# =============================================================================
# Table Structuring Functions
# =============================================================================


def _compile_scss(data: GT, id: Optional[str]) -> str:
    # Obtain the SCSS options dictionary
    gt_options_dict = data._options._options

    # Get collection of parameters that pertain to SCSS
    scss_params = [
        f"${x.parameter}: {x.value};"
        for x in gt_options_dict.values()
        if x.scss is True and x.value is not None
    ]
    scss_params_str = "\n".join(scss_params) + "\n"

    # Determine whether the table has an ID
    has_id = id is not None

    # Obtain the `table_id` value (might be set, might be None)
    # table_id = data._options._get_option_value(option="table_id")

    # TODO: need to implement a function to normalize color (`html_color()`)

    # Get the unique list of fonts from `gt_options_dict`
    font_list = _unique_set(gt_options_dict["table_font_names"].value)

    # Generate a `font-family` string
    if font_list is not None:
        font_family_attr = _as_css_font_family_attr(fonts=font_list)
    else:
        font_family_attr = ""

    gt_table_open_str = f"#{id} table" if has_id else ".gt_table"

    gt_table_class_str = f"""{gt_table_open_str} {{
          {font_family_attr}
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }}"""

    gt_styles_default_file = open(
        pkg_resources.resource_filename("great_tables", "css/gt_styles_default.scss")
    )

    gt_styles_default = gt_styles_default_file.read()
    gt_styles_default = re.sub(r"\s+", " ", gt_styles_default, 0, re.MULTILINE)
    gt_styles_default = re.sub(r"}", "}\n", gt_styles_default, 0, re.MULTILINE)

    gt_colors_file = open(pkg_resources.resource_filename("great_tables", "css/gt_colors.scss"))

    gt_colors = gt_colors_file.read()

    scss = scss_params_str + gt_colors + gt_styles_default

    compiled_css = cast(str, sass.compile(string=scss))

    if has_id:
        compiled_css = re.sub(r"\.gt_", f"#{id} .gt_", compiled_css, 0, re.MULTILINE)
        compiled_css = re.sub(r"thead", f"#{id} thead", compiled_css, 0, re.MULTILINE)
        compiled_css = re.sub(r"p ", f"#{id} p ", compiled_css, 0, re.MULTILINE)

    finalized_css = f"{gt_table_class_str}\n\n{compiled_css}"

    return finalized_css
