from __future__ import annotations

from typing import Any, List, Optional
from typing_extensions import Self

import tempfile
import copy

from great_tables._gt_data import GTData

# Main gt imports ----
from great_tables._body import body_reassemble
from great_tables._boxhead import cols_align, cols_label
from great_tables._data_color import data_color
from great_tables._formats import (
    fmt,
    fmt_number,
    fmt_percent,
    fmt_integer,
    fmt_scientific,
    fmt_currency,
    fmt_bytes,
    fmt_roman,
    fmt_date,
    fmt_time,
    fmt_datetime,
    fmt_markdown,
    fmt_image,
)
from great_tables._heading import tab_header
from great_tables._helpers import random_id
from great_tables._options import (
    tab_options,
    opt_align_table_header,
    opt_all_caps,
    opt_footnote_marks,
    opt_row_striping,
    opt_vertical_padding,
    opt_horizontal_padding,
    opt_stylize,
)
from great_tables._source_notes import tab_source_note
from great_tables._spanners import (
    tab_spanner,
    cols_move,
    cols_move_to_start,
    cols_move_to_end,
    cols_hide,
    cols_width,
)
from great_tables._stub import reorder_stub_df
from great_tables._stubhead import tab_stubhead
from great_tables._tbl_data import n_rows, _get_cell
from great_tables._utils_render_html import (
    create_heading_component_h,
    create_columns_component_h,
    create_body_component_h,
    create_source_notes_component_h,
    create_footnotes_component_h,
    _get_table_defs,
)
from great_tables._tab_create_modify import tab_style


__all__ = ["GT"]


# =============================================================================
# GT class
# =============================================================================
class GT(
    GTData,
):
    """
    Create a **Great Tables** object.

    The `GT()` class creates the `GT` object when provided with tabular data. Using this class is
    the the first step in a typical **Great Tables** workflow. Once we have this object, we can
    take advantage of numerous methods to get the desired display table for publication.

    There are a few table structuring options we can consider at this stage. We can choose to create
    a table stub containing row labels through the use of the `rowname_col=` argument. Further to
    this, row groups can be created with the `groupname_col=` argument. Both arguments take the name
    of a column in the input table data. Typically, the data in the `groupname_col=` column will
    consist of categorical text whereas the data in the `rowname_col=` column will often contain
    unique labels (perhaps being unique across the entire table or unique only within the different
    row groups).

    Parameters
    ----------
    data
        A DataFrame object.
    rowname_col
        The column name in the input `data=` table to use as row labels to be placed in the table
        stub.
    groupname_col
        The column name in the input `data=` table to use as group labels for generation of row
        groups.
    auto_align
        Optionally have column data be aligned depending on the content contained in each column of
        the input `data=`.
    locale
        An optional locale identifier that can be set as the default locale for all functions that
        take a `locale` argument. Examples include `"en"` for English (United States) and `"fr"`
        for French (France).

    Returns
    -------
    GT
        A GT object is returned.

    Examples
    --------
    Let's use the `exibble` dataset for the next few examples, we'll learn how to make simple
    output tables with the `GT()` class. The most basic thing to do is to just use `GT()` with the
    dataset as the input.

    ```{python}
    from great_tables import GT, exibble

    GT(exibble)
    ```

    This dataset has the `row` and `group` columns. The former contains unique values that are ideal
    for labeling rows, and this often happens in what is called the 'stub' (a reserved area that
    serves to label rows). With the `GT()` class, we can immediately place the contents of the `row`
    column into the stub column. To do this, we use the `rowname_col=` argument with the appropriate
    column name.

    ```{python}
    from great_tables import GT, exibble

    GT(exibble, rowname_col="row")
    ```

    This sets up a table with a stub, the row labels are placed within the stub column, and a
    vertical dividing line has been placed on the right-hand side.

    The `group` column contains categorical values that are ideal for grouping rows. We can use the
    `groupname_col=` argument to place these values into row groups.

    ```{python}
    from great_tables import GT, exibble

    GT(exibble, rowname_col="row", groupname_col="group")
    ```

    By default, values in the body of a table (and their column labels) are automatically aligned.
    The alignment is governed by the types of values in a column. If you'd like to disable this form
    of auto-alignment, the `auto_align=False` option can be taken.

    ```{python}
    from great_tables import GT, exibble

    GT(exibble, rowname_col="row", auto_align=False)
    ```

    What you'll get from that is center-alignment of all table body values and all column labels.
    Note that row labels in the the stub are still left-aligned; and `auto_align=` has no effect on
    alignment within the table stub.

    However which way you generate the initial table object, you can modify it with a huge variety
    of methods to further customize the presentation. Formatting body cells is commonly done with
    the family of formatting methods (e.g., `fmt_number()`, `fmt_date()`, etc.). The package
    supports formatting with internationalization ('i18n' features) and so locale-aware methods
    all come with a `locale=` argument. To avoid having to use that argument repeatedly, the `GT()`
    class has its own `locale=` argument. Setting a locale in that will make it available globally.
    Here's an example of how that works in practice when setting `locale = "fr"` in `GT()` prior to
    using formatting methods:

    ```{python}
    from great_tables import GT, exibble

    (
        GT(exibble, rowname_col="row", locale="fr")
        .fmt_currency(columns="currency")
        .fmt_scientific(columns="num")
        .fmt_date(columns="date", date_style="day_month_year")
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
    cols_align = cols_align
    cols_label = cols_label
    fmt = fmt

    fmt_number = fmt_number
    fmt_integer = fmt_integer
    fmt_percent = fmt_percent
    fmt_scientific = fmt_scientific
    fmt_currency = fmt_currency
    fmt_bytes = fmt_bytes
    fmt_roman = fmt_roman
    fmt_date = fmt_date
    fmt_time = fmt_time
    fmt_datetime = fmt_datetime
    fmt_markdown = fmt_markdown
    fmt_image = fmt_image

    data_color = data_color

    tab_options = tab_options
    opt_align_table_header = opt_align_table_header
    opt_all_caps = opt_all_caps
    opt_footnote_marks = opt_footnote_marks
    opt_row_striping = opt_row_striping
    opt_vertical_padding = opt_vertical_padding
    opt_horizontal_padding = opt_horizontal_padding
    opt_stylize = opt_stylize

    tab_header = tab_header

    tab_spanner = tab_spanner
    tab_source_note = tab_source_note
    cols_move = cols_move
    cols_move_to_start = cols_move_to_start
    cols_move_to_end = cols_move_to_end
    cols_hide = cols_hide
    cols_width = cols_width

    tab_stubhead = tab_stubhead

    tab_style = tab_style

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
        final_body = body_reassemble(built._body, built._row_groups, built._stub, built._boxhead)

        # Reordering of the metadata elements of the table

        final_stub = reorder_stub_df(built._stub, built._row_groups)
        # self = self.reorder_footnotes()
        # self = self.reorder_styles()

        # Transformations of individual cells at supported locations

        # self = self.perform_text_transforms()

        # ...

        return built._replace(_body=final_body, _stub=final_stub)

    def render(self, context: str) -> str:
        html_table = self._build_data(context=context)._render_as_html()
        return html_table

    # =============================================================================
    # HTML Rendering
    # =============================================================================
    def _render_as_html(self) -> str:
        heading_component = create_heading_component_h(data=self)
        column_labels_component = create_columns_component_h(data=self)
        body_component = create_body_component_h(data=self)
        source_notes_component = create_source_notes_component_h(data=self)
        footnotes_component = create_footnotes_component_h(data=self)

        # Get attributes for the table
        table_defs = _get_table_defs(data=self)

        # Determine whether Quarto processing of the table is enabled
        quarto_disable_processing = str(self._options.quarto_disable_processing.value).lower()
        quarto_use_bootstrap = str(self._options.quarto_use_bootstrap.value).lower()

        # If table_defs["table_colgroups"] is None, then we set table_colgroups to an empty string;
        # if present, wrap the value with newlines
        if table_defs["table_colgroups"] is None:
            table_colgroups = ""
        else:
            table_colgroups = f"\n{table_defs['table_colgroups']}\n"

        if table_defs["table_style"] is None:
            table_tag_open = f'<table class="gt_table" data-quarto-disable-processing="{quarto_disable_processing}" data-quarto-bootstrap="{quarto_use_bootstrap}">'
        else:
            table_tag_open = f'<table style="{table_defs["table_style"]}" class="gt_table" data-quarto-disable-processing="{quarto_disable_processing}" data-quarto-bootstrap="{quarto_use_bootstrap}">'

        html_table = f"""{table_tag_open}{table_colgroups}
{heading_component.make_string()}
{column_labels_component}
{body_component}
{source_notes_component}
{footnotes_component}
</table>
"""

        # Obtain the `table_id` value (might be set, might be None)
        table_id = self._options.table_id.value

        if table_id is None:
            id = random_id()
        else:
            id = table_id

        # Compile the SCSS as CSS
        from ._scss import compile_scss

        css = compile_scss(data=self, id=id)

        # Obtain options set for overflow and container dimensions

        container_padding_x = self._options.container_padding_x.value
        container_padding_y = self._options.container_padding_y.value
        container_overflow_x = self._options.container_overflow_x.value
        container_overflow_y = self._options.container_overflow_y.value
        container_width = self._options.container_width.value
        container_height = self._options.container_height.value

        finalized_table = f"""<div id="{id}" style="padding-left:{container_padding_x};padding-right:{container_padding_x};padding-top:{container_padding_y};padding-bottom:{container_padding_y};overflow-x:{container_overflow_x};overflow-y:{container_overflow_y};width:{container_width};height:{container_height};">
<style>
{css}
</style>
{html_table}
</div>
        """

        return finalized_table

    def _finalize_html_table(
        style: str, quarto_disable_processing: str, quarto_use_bootstrap: str, *args: Any
    ) -> str:
        from htmltools import tags, HTML, css, TagList

        html_tbl = tags.table(
            data_quarto_disable_processing=quarto_disable_processing,
            data_quarto_bootstrap=quarto_use_bootstrap,
            *args,
            class_="gt_table",
            style=style,
        )

        html_tbl = str(html_tbl)

        return html_tbl


# =============================================================================
# End of GT class
# =============================================================================


# =============================================================================
# Functions that operate on GT objects
# =============================================================================


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


def as_raw_html(gt: GT) -> str:
    """
    Get the HTML content of a GT object.

    Get the HTML content from a GT object as a string. This function is useful for obtaining the
    HTML content of a GT object for use in other contexts.

    Parameters
    ----------
    gt
        A GT object.

    Returns
    -------
    str
        An HTML fragment containing a table.
    """
    gt_built = gt._build_data(context="html")
    html_table = gt_built._render_as_html()
    return html_table


def gtsave(
    gt: GT,
    filename: str,
    path: Optional[str] = None,
    selector: str = "table",
    zoom: int = 2,
    expand: int = 5,
) -> None:
    """
    Save a table as an image file.

    The `gtsave()` function makes it easy to save a table object as an image file. The function
    produces a high-resolution PNG file of the table. The image is created by taking a screenshot of
    the table using a headless Chrome browser. The screenshot is then cropped to only include the
    table element, and the resulting image is saved to the specified file path.

    Parameters
    ----------
    gt
        A GT object.
    filename
        The name of the file to save the image to.
    path
        An optional path to save the image to. If not provided, the image will be saved to the
        current working directory.
    selector
        The HTML element selector to use to select the table. By default, this is set to "table",
        which selects the first table element in the HTML content.
    zoom
        The zoom level to use when taking the screenshot. By default, this is set to 2. Lowering
        this to 1 will result in a smaller image, while increasing it will result in a much larger
        (yet more detailed) image.
    expand
        The number of pixels to expand the screenshot by. By default, this is set to 5. This can be
        increased to capture more of the surrounding area, or decreased to capture less.

    Returns
    -------
    None
        This function does not return anything; it simply saves the image to the specified file
        path.
    """

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from PIL import Image
    from io import BytesIO

    # Get the HTML content from the displayed output
    html_content = as_raw_html(gt)

    # Create a temp directory to store the HTML file
    temp_dir = tempfile.mkdtemp()

    # Create a temp file to store the HTML file; use the .html file extension
    temp_file = tempfile.mkstemp(dir=temp_dir, suffix=".html")

    # Write the HTML content to the temp file
    with open(temp_file[1], "w") as f:
        f.write(html_content)

    # Generate output file path from filename and optional path
    output_path = filename
    if path:
        # If path has a trailing slash, remove it
        if path[-1] == "/":
            path = path[:-1]
        output_path = path + "/" + filename

    # Set up the Chrome webdriver options
    options = webdriver.ChromeOptions()

    # Use headless mode with an extremely large window size
    options.add_argument("--headless")
    options.add_argument("--window-size=6000, 5000")

    # Instantiate a Chrome webdriver with the selected options
    chrome = webdriver.Chrome(options=options)

    # Normalize zoom level
    zoom = zoom - 1

    # Convert the zoom level to a percentage string
    zoom_level = str(zoom * 100) + "%"

    # Get the scaling factor by multiplying the zoom by 2
    scaling_factor = zoom * 2

    # Adjust the expand value by the scaling factor
    expansion_amount = expand * scaling_factor

    # Open the HTML file in the Chrome browser
    chrome.get("file://" + temp_file[1])
    chrome.execute_script(f"document.body.style.zoom = '{zoom_level}'")

    # Get only the chosen element from the page; by default, this is
    # the table element
    element = chrome.find_element(by=By.TAG_NAME, value=selector)

    # Get the location and size of the table element; this will be used
    # to crop the screenshot later
    location = element.location
    size = element.size

    # Get a screenshot of the entire page
    png = chrome.get_screenshot_as_png()

    # Close the Chrome browser
    chrome.quit()

    # Open the screenshot as an image with the PIL library
    image = Image.open(fp=BytesIO(png))

    # Crop the image to only include the table element; the scaling factor
    # of 6 is used to account for the zoom level of 300% set earlier
    left = (location["x"] * scaling_factor) - expansion_amount
    top = (location["y"] * scaling_factor) - expansion_amount
    right = ((location["x"] + size["width"]) * scaling_factor) + expansion_amount
    bottom = ((location["y"] + size["height"]) * scaling_factor) + expansion_amount

    # Save the cropped image to the output path
    image = image.crop((left, top, right, bottom))

    # Save the image to the output path as a PNG file
    image.save(fp=output_path, format="png")
