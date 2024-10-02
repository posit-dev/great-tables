from __future__ import annotations

import tempfile
import time
import warnings
import webbrowser

from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import TYPE_CHECKING, Literal
from typing_extensions import TypeAlias

from ._utils import _try_import

if TYPE_CHECKING:
    # Note that as_raw_html uses methods on the GT class, not just data
    from .gt import GT
    from ._types import GTSelf

    from selenium import webdriver
    from IPython.core.interactiveshell import InteractiveShell


class PatchedHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Patched handler, which does not log requests to stderr"""

    def log_request(self, *args, **kwargs):
        pass


class MISSING:
    """Represent a missing argument (where None has a special meaning)."""


def _create_temp_file_server(fname: Path) -> HTTPServer:
    """Return a HTTPServer, so we can serve a single request (to show the table)."""

    Handler = partial(PatchedHTTPRequestHandler, directory=str(fname.parent))
    server = HTTPServer(("127.0.0.1", 0), Handler)

    return server


def _infer_render_target(ipy: InteractiveShell | None | MISSING = MISSING) -> str:
    # adapted from py-htmltools
    # Note that `ipy` arguments are possible return values of IPython.get_ipython()
    # They are manually passed in from unit tests to validate this function.
    try:
        import IPython  # pyright: ignore[reportUnknownVariableType]
        from IPython.terminal.interactiveshell import TerminalInteractiveShell

        if ipy is MISSING:
            # Note that get_ipython may be None, to indicate no shell in use
            # e.g. if you're in the normal python repl
            ipy = IPython.get_ipython()

        if isinstance(ipy, TerminalInteractiveShell):
            target = "browser"
        elif ipy is None:
            target = "browser"
        else:
            target = "notebook"

    except ImportError:
        target = "browser"

    return target


def show(
    self: GTSelf,
    target: Literal["auto", "notebook", "browser"] = "auto",
):
    """Display the table in a notebook or a web browser.

    Note that this function is often unecessary in a notebook. However, it's sometimes useful for
    manually triggering display within a code cell.

    Parameters
    ----------
    target:
        Where to show the table. If "auto", infer whether the table can be displayed inline (e.g. in
        a notebook), or whether a browser is needed (e.g. in a console).

    Examples
    --------

    The example below when in the Great Tables documentation, should appear on the page.

    ```{python}
    from great_tables import GT, exibble

    GT(exibble.head(2)).show()
    GT(exibble.tail(2)).show()
    ```

    """

    if target == "auto":
        target = _infer_render_target()

    if target == "notebook":
        from IPython.core.display import display_html

        html = self._repr_html_()

        # https://github.com/ipython/ipython/pull/10962
        display_html(  # pyright: ignore[reportUnknownVariableType]
            html, raw=True, metadata={"text/html": {"isolated": True}}
        )
    elif target == "browser":
        html = self.as_raw_html(make_page=True)
        with tempfile.TemporaryDirectory() as tmp_dir:
            f_path = Path(tmp_dir) / "index.html"
            f_path.write_text(html, encoding="utf-8")

            # create a server that closes after 1 request ----
            server = _create_temp_file_server(f_path)
            webbrowser.open(f"http://127.0.0.1:{server.server_port}/{f_path.name}")
            server.handle_request()
    else:
        raise Exception(f"Unknown target display: {target}")


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


class _NoOpDriverCtx:
    """Context manager that no-ops entering a webdriver(options=...) instance."""

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def __call__(self, options):
        # no-op what is otherwise instantiating webdriver with options,
        # since a webdriver instance was already passed on init
        return self

    def __enter__(self):
        return self.driver

    def __exit__(self, *args):
        pass


def save(
    self: GT,
    file: Path | str,
    selector: str = "table",
    scale: float = 1.0,
    expand: int = 5,
    web_driver: WebDrivers | webdriver.Remote = "chrome",
    window_size: tuple[int, int] = (6000, 6000),
    debug_port: None | int = None,
    encoding: str = "utf-8",
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
        The webdriver to use when taking the screenshot. Either a driver name, or webdriver
        instance. By default, uses Google Chrome. Supports `"firefox"` (Mozilla Firefox), `"safari"`
        (Apple Safari), and `"edge"` (Microsoft Edge).

        Specified browser must be installed. Note that if a webdriver instance is passed, options
        that require setting up a webdriver, like debug_port, will not be used.
    window_size
        The size of the browser window to use when laying out the table. This shouldn't be necessary
        to capture a table, but may affect the tables appearance.
    debug_port
        Port number to use for debugging. By default no debugging port is opened.
    encoding
        The encoding used when writing temporary files.
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

    if isinstance(file, Path):
        file = str(file)

    # If there is no file extension, add the .png extension
    if not Path(file).suffix:
        file += ".png"

    # Get the HTML content from the displayed output
    html_content = as_raw_html(self)

    # Set the webdriver and options based on the chosen browser (`web_driver=` argument)
    if isinstance(web_driver, webdriver.Remote):
        wdriver = _NoOpDriverCtx(web_driver)
        wd_options = None

    elif web_driver == "chrome":
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
    else:
        raise ValueError(f"Unsupported web driver: {web_driver}")

    # specify headless flag ----
    if web_driver in {"firefox", "edge"}:
        wd_options.add_argument("--headless")
    elif web_driver == "chrome":
        # Operate all webdrivers in headless mode
        wd_options.add_argument("--headless=new")
    else:
        # note that safari currently doesn't support headless browsing
        pass

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
        with open(f"{tmp_dir}/table.html", "w", encoding=encoding) as temp_file:
            temp_file.write(html_content)

        # Open the HTML file in the headless browser
        headless_browser.set_window_size(*window_size)
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
    crud_factor = 20
    outer_width, outer_height = driver.execute_script(
        "var w = window; return [w.outerWidth - w.innerWidth, w.outerHeight - w.innerHeight]"
    )
    offset_left, offset_top = driver.execute_script(
        "var div = document.body.childNodes[0]; return [div.offsetLeft, div.offsetTop];"
    )
    reported_width = driver.execute_script(
        "var el = document.getElementsByTagName('table')[0]; return el.clientWidth;"
    )
    required_width = (reported_width + offset_left * 2) * scale + crud_factor + outer_width

    # set to our required_width first, in case it changes the height of the table
    driver.set_window_size(required_width, original_size["height"])

    time.sleep(0.05)

    if debug == "width_resize":
        return _dump_debug_screenshot(driver, path)

    # height accounts for top-padding supplied by the browser (doubled to pad top and bottom)
    div_height = driver.execute_script(
        "var div = document.body.childNodes[0]; return div.scrollHeight;"
    )
    required_height = div_height + offset_top * 2 + outer_height

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
        Image.open(fp=BytesIO(el.screenshot_as_png)).save(fp=path)


def _dump_debug_screenshot(driver, path):
    driver.execute_script(
        "document.body.style.border = '3px solid blue'; "
        "document.body.childNodes[0].style.border = '3px solid orange'; "
        "document.getElementsByTagName('table')[0].style.border = '3px solid green'; "
    )
    driver.save_screenshot(path)
