from __future__ import annotations

import tempfile
from typing import TYPE_CHECKING, Literal

from typing_extensions import TypeAlias

from ._utils import _try_import

if TYPE_CHECKING:
    # Note that as_raw_html uses methods on the GT class, not just data
    from .gt import GT

    from selenium import webdriver


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

    Examples:
    ------
    Let's use the `row` column of `exibble` dataset to create a table. With the `as_raw_html()`
    method, we're able to output the HTML content.

    ```{python}
    from great_tables import GT, exibble

    GT(exibble[["row"]]).as_raw_html()
    ```

    """
    built_table = self._build_data(context="html")

    html_table = built_table._render_as_html(
        make_page=make_page,
        all_important=all_important,
    )

    return html_table


# Create a list of all selenium webdrivers
WebDrivers: TypeAlias = Literal[
    "chrome",
    "firefox",
    "safari",
    "edge",
]


def save(
    self: GT,
    file: str,
    selector: str = "table",
    scale: float = 1.0,
    expand: int = 5,
    web_driver: WebDrivers = "chrome",
    window_size: tuple[int, int] = (6000, 6000),
    debug_port: None | int = None,
) -> None:
    """
    Produce a high-resolution image file or PDF of the table.

    The output file is created by taking a screenshot of the table using a headless browser.

    Parameters
    ----------
    file
        The name of the file to save the image to. Accepts names ending with .png, .bmp, and other
        image extensions. Also accepts the extension .pdf.
    selector
        (NOT IMPLEMENTED) The HTML element name used to select table. Defaults to the whole table.
    scale
        The scaling factor that will be used when generating the image.  Lower values decrease
        resolution. A scale of 2 is equivalent to doubling the width of the table in pixels. Note
        that higher resolution results in larger file sizes.
    expand
        (NOT IMPLEMENTED) The number of pixels to expand the screenshot by.  This can be
        increased to capture more of the surrounding area, or decreased to capture less.
    web_driver
        The webdriver to use when taking the screenshot. By default, uses Google Chrome. Supports
        `"firefox"` (Mozilla Firefox), `"safari"` (Apple Safari), and `"edge"` (Microsoft Edge).
        Specified browser must be installed.
    window_size
        The size of the browser window to use when laying out the table. This shouldn't be necessary
        to capture a table, but may affect the tables appearance.
    debug_port
        Port number to use for debugging. By default no debugging port is opened.

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
    _try_import(name="PIL", pip_install_line="pip install pillow")
    _try_import(name="selenium", pip_install_line="pip install selenium")

    from selenium import webdriver

    if selector != "table":
        raise NotImplementedError("Currently, only selector='table' is supported.")

    # Get the file extension from the file name
    file_extension = file.split(".")[-1]

    # If there is no file extension, add the .png extension
    if len(file_extension) == len(file):
        file += ".png"

    # Get the HTML content from the displayed output
    html_content = as_raw_html(self)

    # Create a temp directory to store the HTML file
    temp_dir = tempfile.mkdtemp()

    # Set the webdriver and options based on the chosen browser (`web_driver=` argument)
    if web_driver == "chrome":
        wdriver = webdriver.Chrome
        wd_options = webdriver.ChromeOptions()
    elif web_driver == "safari":
        wdriver = webdriver.Safari
        wd_options = webdriver.SafariOptions()
    elif web_driver == "firefox":
        wdriver = webdriver.Firefox
        wd_options = webdriver.FirefoxOptions()
    elif web_driver == "edge":
        wdriver = webdriver.Edge
        wd_options = webdriver.EdgeOptions()

    # All webdrivers except for 'Firefox' can operate in headless mode; they all accept window size
    # options are separate width and height arguments
    if web_driver != "firefox":
        wd_options.add_argument(str("--headless"))

    if debug_port:
        wd_options.add_argument(f"--remote-debugging-port={debug_port}")

    with (
        tempfile.NamedTemporaryFile(suffix=".html", dir=temp_dir) as temp_file,
        wdriver(options=wd_options) as headless_browser,
    ):

        # Write the HTML content to the temp file
        with open(temp_file.name, "w") as fp:
            fp.write(html_content)

        # Open the HTML file in the headless browser
        headless_browser.set_window_size(window_size[0], window_size[1])
        headless_browser.get("file://" + temp_file.name)

        _save_screenshot(headless_browser, scale, file)

        if debug_port:
            input(
                f"Currently debugging on port {debug_port}.\n\n"
                "If you are using Chrome, enter chrome://inspect to preview the headless browser."
                "Other browsers may have different ways to preview headless browser sessions.\n\n"
                "Press enter to continue."
            )


def _save_screenshot(driver: webdriver.Chrome, scale, path: str) -> None:
    from PIL import Image
    from io import BytesIO
    from selenium.webdriver.common.by import By

    # Based on: https://stackoverflow.com/a/52572919/
    # In some headless browsers, element position and width do not always reflect
    # css transforms like zoom.
    #
    # This approach works on the following assumptions:
    #   * Zoomed table width cannot always be obtained directly, but is clientWidth * scale
    #   * Zoomed table height is accurately obtained by body scrollHeight

    original_size = driver.get_window_size()

    # set table zoom ----
    driver.execute_script(
        f"var el = document.getElementsByTagName('table')[0]; el.style.zoom = '{scale}';"
    )

    # get table width and height ----
    reported_width = driver.execute_script(
        "return document.getElementsByTagName('table')[0].clientWidth"
    )

    required_width = reported_width * scale
    required_height = driver.execute_script("return document.body.scrollHeight")

    # resize window and capture image ----
    driver.set_window_size(required_width, required_height)
    el = driver.find_element(by=By.TAG_NAME, value="body")

    if path.endswith(".png"):
        el.screenshot(path)
    else:
        png = driver.get_screenshot_as_png()
        Image.open(fp=BytesIO(png)).save(fp=path)

    # set window back to original size ----
    driver.set_window_size(original_size["width"], original_size["height"])
