# GT.gtsave()

Save a GT table to a file (PNG, JPEG, WebP, PDF, SVG, Word, Excel, PowerPoint, RTF, or Typst).

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_export.py#L733-L879)

``` python
GT.gtsave(
    file,
    selector="table",
    expand=5,
    zoom=2.0,
    delay=0.2,
    vwidth=992,
    vheight=744,
)
```

The [gtsave()](../reference/GT.gtsave.md#great_tables.GT.gtsave) method renders the table to an image or PDF using a headless Chrome browser via the `nokap` package. This provides a reliable way to produce high-resolution image files of tables without requiring Selenium or Playwright. Chrome or Chromium must be installed on the system for these formats.

The other formats (SVG, Word, Excel, PowerPoint, RTF, and Typst) are written by [gridwell](https://github.com/rich-iannone/gridwell) from the table's gridwell IR (see `GT.as_gridwell()`), with no browser needed. Install gridwell with `pip install "great_tables[gridwell]"`. SVG output is experimental in gridwell, and its styling may change between gridwell releases.

## Parameters

`file: Path | str`  
The file path to write the output to. The format is determined by the file extension: `.png`, `.jpg`/`.jpeg`, `.webp` for images; `.pdf` for PDF; and, with gridwell, `.svg` for SVG, `.docx` for Word, `.xlsx` for Excel, `.pptx` for PowerPoint, `.rtf` for RTF, and `.typ` for Typst. If no extension is provided, `.png` is assumed. The other arguments apply to images and PDF only.

`selector: str = "table"`  
A CSS selector targeting the element to capture. Defaults to `"table"`, which captures just the table element with tight bounds.

`expand: int | tuple[int, int, int, int] = 5`  
Padding (in pixels) to add around the captured element. A single integer applies equal padding on all sides. A 4-tuple specifies `(top, right, bottom, left)` padding individually. Defaults to `5`.

`zoom: float = 2.0`  
The scale factor for raster image output. Higher values produce higher resolution images. For example, `zoom=2` produces a retina-quality (2x) image. Defaults to `2.0`. Ignored for PDF output.

`delay: float = 0.2`  
Seconds to wait after page load before capturing. This is useful for ensuring that any web fonts or dynamic content have fully rendered. Defaults to `0.2`.

`vwidth: int = 992`  
Viewport width in pixels. This controls the layout width of the page and may affect how the table is rendered (e.g., responsive layouts). Defaults to `992`.

`vheight: int = 744`  
Viewport height in pixels. Defaults to `744`.

## Returns

`GT`  
The GT object is returned (the same object the method is called on), facilitating method chaining.

## Examples

Using a small subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset, let's create a table and save it to a PNG file.

``` python
from great_tables import GT, data
from great_tables.data import gtcars
import polars as pl

gtcars_mini = (
    data.pl.gtcars
    .select(["mfr", "model", "msrp"])
    .head(5)
)

(
    GT(gtcars_mini)
    .tab_header(title="Some Cars from gtcars")
    .fmt_currency(columns="msrp")
    .gtsave("my_table.png")
)
```

Save a table as a high-resolution retina image with extra padding.

``` python
(
    GT(gtcars_mini)
    .fmt_currency(columns="msrp")
    .gtsave("my_table.png", zoom=3, expand=20)
)
```

Save a table as a PDF.

``` python
(
    GT(gtcars_mini)
    .fmt_currency(columns="msrp")
    .gtsave("my_table.pdf")
)
```

With gridwell installed, save the same table as SVG, or as a Word document.

``` python
GT(gtcars_mini).fmt_currency(columns="msrp").gtsave("my_table.svg")
GT(gtcars_mini).fmt_currency(columns="msrp").gtsave("my_table.docx")
```
