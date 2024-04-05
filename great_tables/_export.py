from __future__ import annotations
from ._gt_data import GTData
from ._utils import _try_import
from typing import Optional, TYPE_CHECKING

import tempfile

if TYPE_CHECKING:
    # Note that as_raw_html uses methods on the GT class, not just data
    from .gt import GT


def as_raw_html(
    self: GT,
    make_page: bool = False,
    all_important: bool = False,
) -> str:
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
    built_table = self._build_data(context="html")

    html_table = built_table._render_as_html(
        make_page=make_page,
        all_important=all_important,
    )

    return html_table


def save(
    self: GTData,
    file: str,
    selector: str = "table",
    scale: float = 1.0,
    expand: int = 5,
    window_size: tuple[int, int] = (6000, 6000),
) -> None:
    """
    Save a table as an image file or a PDF document.

    The `save()` method makes it easy to save a table object as an image file. The function produces
    a high-resolution image file or PDF of the table. The output file is create by first taking a
    screenshot of the table using a headless Chrome browser. Then, the screenshot is then cropped to
    only include the table element. Finally, and the resulting image is saved to the specified file
    path in the format specified (via the file extension).

    Parameters
    ----------
    file
        The name of the file to save the image to. Accepts names ending with .png, .bmp, and other
        image extensions. Also accepts the extension .pdf.
    selector
        The HTML element selector to use to select the table. By default, this is set to "table",
        which selects the first table element in the HTML content.
    scale
        The scaling factor that will be used when generating the image. By default, this is set to a
        value of `1.0`. Lowering this will result in a smaller image, whereas increasing it will
        result in a much higher-resolution image. This can be considered a quality setting, yet it
        also affects the file size. The default value of `1.0` is a good balance between file size
        and quality.
    expand
        The number of pixels to expand the screenshot by. By default, this is set to 5. This can be
        increased to capture more of the surrounding area, or decreased to capture less.
    window_size
        The size of the window to use when taking the screenshot. This is a tuple of two integers,
        representing the width and height of the window. By default, this is set to `(6000, 6000)`,
        a large size that should be sufficient for most tables. If the table is larger than this
        (and this will be obvious once inspecting the image file) you can increase the appropriate
        values of the tuple. If the table is very small, then a reduction in these these values will
        result in a speed gain during image capture. Please note that the window size is *not* the
        same as the final image size. The table will be captured at the same size as it is displayed
        in the headless browser, and the window size is used to ensure that the entire table is
        visible in the screen capture before the cropping process occurs.

    Returns
    -------
    None
        This function does not return anything; it simply saves the image to the specified file
        path.

    Details
    -------
    We create the output file based on the HTML version of the table.

    This process is facilitated by two libraries:

    - `selenium`, which is used to control the Chrome browser and take a screenshot of the table.
    - `PIL`, which is used to crop the screenshot to only include the table element of the page.

    Both of these packages needs to be installed before attempting to save any table as an image
    file. The `selenium` package also requires the Chrome browser to be installed on the system.

    A pip-based reinstallation of **Great Tables** through the following command will install these
    required packages:

    ```bash
    pip install great_tables[extra]
    ```

    """

    # Import the required packages
    _try_import(name="selenium", pip_install_line="pip install selenium")
    _try_import(name="PIL", pip_install_line="pip install pillow")

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from PIL import Image
    from io import BytesIO
    from pathlib import Path

    Image.MAX_IMAGE_PIXELS = None

    # Get the file extension from the file name
    file_extension = file.split(".")[-1]

    # If there is no file extension, add the .png extension
    if len(file_extension) == len(file):
        file += ".png"

    # Get the HTML content from the displayed output
    html_content = as_raw_html(self=self)

    # Create a temp directory to store the HTML file
    temp_dir = tempfile.mkdtemp()

    # Set up the Chrome webdriver options
    options = webdriver.ChromeOptions()

    # Use headless mode with an extremely large window size
    options.add_argument("--headless")

    # Set the window size (x by y) to a large value to ensure the entire table
    # is visible in the screenshot; this is settable via the `window_size=` argument
    options.add_argument(f"--window-size={window_size[0]},{window_size[1]}")

    with (
        tempfile.NamedTemporaryFile(suffix=".html", dir=temp_dir) as temp_file,
        webdriver.Chrome(options=options) as chrome,
    ):

        # Write the HTML content to the temp file
        with open(temp_file.name, "w") as fp:
            fp.write(html_content)

        # Convert the scale value to a percentage string used by the
        # Chrome browser for zooming
        zoom_level = str(scale * 100) + "%"

        # Get the scaling factor by multiplying `scale` by 2
        scaling_factor = scale * 2

        # Adjust the expand value by the scaling factor
        expansion_amount = expand * scaling_factor

        # Open the HTML file in the Chrome browser
        chrome.get("file://" + temp_file.name)
        chrome.execute_script(f"document.body.style.zoom = '{zoom_level}'")

        # Get only the chosen element from the page; by default, this is the table element
        element = chrome.find_element(by=By.TAG_NAME, value=selector)

        # Get the location and size of the table element; this will be used
        # to crop the screenshot later
        location = element.location
        size = element.size

        # Get a screenshot of the entire page as a PNG image
        png = chrome.get_screenshot_as_png()

    # Open the screenshot as an image with the PIL library; since the screenshot will be large
    # (due to the large window size), we use the BytesIO class to handle the large image data
    image = Image.open(fp=BytesIO(png))

    # Crop the image to only include the table element; the scaling factor
    # of 6 is used to account for the zoom level of 300% set earlier
    left = (location["x"] * scaling_factor) - expansion_amount
    top = (location["y"] * scaling_factor) - expansion_amount
    right = ((location["x"] + size["width"]) * scaling_factor) + expansion_amount
    bottom = ((location["y"] + size["height"]) * scaling_factor) + expansion_amount

    # Save the cropped image to the output path
    image = image.crop((left, top, right, bottom))

    # Save the image to the output path in the specified format
    image.save(fp=file)
