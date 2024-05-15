from __future__ import annotations

import tempfile
import time
import warnings

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

DebugDumpOptions: TypeAlias = Literal["zoom", "width_resize", "final_resize"]


def save(
    self: GT,
    file: str,
    selector: str = "table",
    scale: float = 1.0,
    expand: int = 5,
    web_driver: WebDrivers = "chrome",
    window_size: tuple[int, int] = (6000, 6000),
    debug_port: None | int = None,
    _debug_dump: DebugDumpOptions | None = None,
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
    _debug_dump
        Whether the saved image should be a big browser window, with key elements outlined. This is
        helpful for debugging this function's resizing, cropping heuristics. This is an internal
        parameter and subject to change.

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

    # specify headless flag ----
    # note that safari currently doesn't support headless browsing
    if web_driver == "firefox":
        wd_options.add_argument("--headless")
    else:
        # Operate all webdrivers in headless mode
        wd_options.add_argument("--headless=new")

    if debug_port:
        if web_driver == "chrome":
            wd_options.add_argument(f"--remote-debugging-port={debug_port}")
        elif web_driver == "firefox":
            # TODO: not sure how to connect to this session on firefox?
            wd_options.add_argument(f"--start-debugger-server {debug_port}")
        else:
            warnings.warn("debug_port argument only supported on chrome and firefox")
            debug_port = None

    # run browser ----
    with (
        tempfile.TemporaryDirectory() as tmp_dir,
        wdriver(options=wd_options) as headless_browser,
    ):

        # Write the HTML content to the temp file
        with open(f"{tmp_dir}/table.html", "w") as temp_file:
            temp_file.write(html_content)

        # Open the HTML file in the headless browser
        headless_browser.set_window_size(window_size[0], window_size[1])
        headless_browser.get("file://" + temp_file.name)

        _save_screenshot(headless_browser, scale, file, debug=_debug_dump)

        if debug_port:
            input(
                f"Currently debugging on port {debug_port}.\n\n"
                "If you are using Chrome, enter chrome://inspect to preview the headless browser."
                "Other browsers may have different ways to preview headless browser sessions.\n\n"
                "Press enter to continue."
            )


def _save_screenshot(
    driver: webdriver.Chrome, scale, path: str, debug: DebugDumpOptions | None
) -> None:
    from io import BytesIO
    from selenium.webdriver.common.by import By

    # Based on: https://stackoverflow.com/a/52572919/
    # In some headless browsers, element position and width do not always reflect
    # css transforms like zoom.
    #
    # This approach works on the following assumptions:
    #   * Zoomed table width cannot always be obtained directly, but is its clientWidth * scale
    #   * Zoomed table height is obtained by the height of the div wrapping it
    #   * A sleep may be necessary before the final screen capture
    #
    # I can't say for sure whether the final sleep is needed. Only that it seems like
    # on CI with firefox sometimes the final screencapture is wider than necessary.

    original_size = driver.get_window_size()

    # set table zoom ----
    driver.execute_script(
        "var el = document.getElementsByTagName('table')[0]; "
        f"el.style.zoom = '{scale}'; "
        "el.parentNode.style.display='none'; "
        "el.parentNode.style.display='';"
    )

    if debug == "zoom":
        return _dump_debug_screenshot(driver, path)

    # get table width and height, resizing window as we go ----

    # the window can be bigger than the table, but smaller risks pushing text
    # onto new lines. this pads width and height for a little slack.
    # note that this is mostly to account for body, div padding, and table borders.
    crud_factor = 100

    offset_left, offset_top = driver.execute_script(
        "var div = document.body.childNodes[0]; return [div.offsetLeft, div.offsetTop];"
    )
    reported_width = driver.execute_script(
        "var el = document.getElementsByTagName('table')[0]; return el.clientWidth;"
    )
    required_width = (reported_width + offset_left * 2 + crud_factor) * scale

    # set to our required_width first, in case it changes the height of the table
    driver.set_window_size(required_width, original_size["height"])

    if debug == "width_resize":
        return _dump_debug_screenshot(driver, path)

    # height accounts for top-padding supplied by the browser (doubled to pad top and bottom)
    div_height = driver.execute_script(
        "var div = document.body.childNodes[0]; return div.scrollHeight;"
    )
    required_height = div_height + crud_factor + offset_top * 2

    # final resize window and capture image ----
    driver.set_window_size(required_width, required_height)

    if debug == "final_resize":
        return _dump_debug_screenshot(driver, path)

    el = driver.find_element(by=By.TAG_NAME, value="body")

    time.sleep(0.05)

    if path.endswith(".png"):
        el.screenshot(path)
    else:
        _try_import(name="PIL", pip_install_line="pip install pillow")

        from PIL import Image

        # convert to other formats (e.g. pdf, bmp) using PIL
        with tempfile.TemporaryDirectory() as tmp_dir:
            fname = f"{tmp_dir}/image.png"
            el.screenshot(fname)

            with open(fname, "rb") as f:
                Image.open(fp=BytesIO(f)).save(fp=path)


def _dump_debug_screenshot(driver, path):
    driver.execute_script(
        "document.body.style.border = '5px solid blue'; "
        "document.body.childNodes[0].style.border = '5px solid orange'; "
        "document.getElementsByTagName('table')[0].style.border = '5px solid green'; "
    )
    driver.save_screenshot(path)
