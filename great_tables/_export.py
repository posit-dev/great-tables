from __future__ import annotations
from ._gt_data import GTData
from typing import Optional

import tempfile


def as_raw_html(self: GTData) -> str:
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
    return self._build_data(context="html")._render_as_html()


def save(
    self: GTData,
    filename: str,
    path: Optional[str] = None,
    selector: str = "table",
    zoom: int = 2,
    expand: int = 5,
) -> None:
    """
    Save a table as an image file.

    The `save()` method makes it easy to save a table object as an image file. The function produces
    a high-resolution PNG file of the table. The image is created by taking a screenshot of
    the table using a headless Chrome browser. The screenshot is then cropped to only include the
    table element, and the resulting image is saved to the specified file path.

    Parameters
    ----------
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
    from pathlib import Path

    # Get the HTML content from the displayed output
    html_content = as_raw_html(self=self)

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
        # If path has a trailing slash, remove it; use the Path class to handle this
        path = Path(path)
        if path.is_dir():
            output_path = path / filename
        else:
            path = path.parent
            output_path = path / filename
    else:
        output_path = Path.cwd() / filename

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
