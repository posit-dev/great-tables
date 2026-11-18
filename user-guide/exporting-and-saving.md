# Exporting and Saving Tables

Once you have built a table, you need to get it into its final destination. That might be a notebook cell, a standalone HTML file, a LaTeX document, or an image file for inclusion in a report or presentation. **Great Tables** provides several export methods to cover these use cases, each with options to control the output format.

The general principle is: build your table once, export it many ways. The same [GT](../reference/GT.md#great_tables.GT) object can be displayed interactively, saved as HTML, rendered as LaTeX, or captured as an image. This means you don't need to maintain separate table-building code for different output formats. Your single chain of formatting, styling, and structural methods produces the canonical table, and the export step simply serializes it for the target medium.

## Displaying Tables

In most notebook environments (Jupyter, Quarto, marimo), simply placing a [GT](../reference/GT.md#great_tables.GT) object as the last expression in a cell will render the table automatically. However, you can also use the [show()](../reference/GT.show.md#great_tables.GT.show) method for explicit control over where the table is displayed.

``` python
from great_tables import GT, data

gt_tbl = (
    GT(data.pl.exibble.head(3).select("num", "char", "currency"))
    .tab_header(title="Example Table", subtitle="A small demonstration")
    .fmt_currency(columns="currency")
    .fmt_number(columns="num", decimals=2)
)

gt_tbl.show()
```

| Example Table         |         |          |
|-----------------------|---------|----------|
| A small demonstration |         |          |
| num                   | char    | currency |
| 0.11                  | apricot | \$49.95  |
| 2.22                  | banana  | \$17.95  |
| 33.33                 | coconut | \$1.39   |

The `target=` argument controls the display destination. The available options are:

- `"auto"` (the default): displays inline in a notebook if possible, otherwise opens a browser window.
- `"notebook"`: forces inline notebook display.
- `"browser"`: opens the table in your default web browser. This is particularly useful when working in the console or when you want to see the full styled output that some IDEs may suppress.

``` python
# Open in a browser window (useful when running from a script or console)
gt_tbl.show(target="browser")
```

## Getting HTML as a String

The [as_raw_html()](../reference/GT.as_raw_html.md#great_tables.GT.as_raw_html) method returns the table as an HTML string. This is useful for embedding tables in web applications, email templates, or custom HTML documents. Body cells that have not been processed by a `fmt_*()` method are automatically HTML-escaped to prevent cross-site scripting (XSS) when rendering untrusted data. See the [Formatting Values](formatting-values.md) page for details on how to include raw HTML in cells using [html()](../reference/html.md#great_tables.md) and [fmt()](../reference/GT.fmt.md#great_tables.GT.fmt).

``` python
html_str = gt_tbl.as_raw_html()

# Show the first 200 characters to see the structure
print(html_str[:200])
```

    <div id="erkdslgqwb" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
    <style>
    #erkdslgqwb table {
              font

The method accepts several arguments that control the output format.

### Inline CSS for Email

Email clients typically strip `<style>` blocks, so you need inline CSS for the table to render correctly. Set `inline_css=True` to move all styles into `style` attributes.

``` python
email_html = gt_tbl.as_raw_html(inline_css=True)
```

With inline CSS, your table will render correctly in Gmail, Outlook, and other email clients that strip external stylesheets.

This matters because most email clients aggressively strip `<style>` blocks and external CSS references for security reasons. Without inline CSS, your carefully styled table will appear as plain, unstyled HTML in the recipient's inbox. If you are sharing tables via email (whether through automated reports or one-off sends), `inline_css=True` is almost always what you want.

### Complete HTML Page

If you need a self-contained HTML document (with `<html>`, `<head>`, and `<body>` tags), set `make_page=True`.

``` python
full_page = gt_tbl.as_raw_html(make_page=True)
```

This wraps the table in a complete HTML document that can be opened directly in any browser without additional scaffolding.

### Writing HTML to a File

The [write_raw_html()](../reference/GT.write_raw_html.md#great_tables.GT.write_raw_html) method is a convenience wrapper that writes the HTML output directly to a file (with UTF-8 encoding by default).

``` python
gt_tbl.write_raw_html("my_table.html")
```

It takes the same `inline_css=` and `make_page=` options as [as_raw_html()](../reference/GT.as_raw_html.md#great_tables.GT.as_raw_html), so the file can hold an email-ready fragment or a complete page.

## LaTeX Output

For inclusion in LaTeX documents, the [as_latex()](../reference/GT.as_latex.md#great_tables.GT.as_latex) method generates a LaTeX fragment containing the table.

``` python
latex_str = gt_tbl.as_latex()
print(latex_str)
```

    \begin{table}
    \caption*{
    {\large Example Table} \\
    {\small A small demonstration}
    } 

    \fontsize{12.0pt}{14.4pt}\selectfont

    \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}rlr}
    \toprule
    num & char & currency \\ 
    \midrule\addlinespace[2.5pt]
    0.11 & apricot & \$49.95 \\
    2.22 & banana & \$17.95 \\
    33.33 & coconut & \$1.39 \\
    \bottomrule
    \end{tabular*}

    \end{table}

The output uses a `tabular` environment by default. For tables that span multiple pages, you can switch to the `longtable` environment.

``` python
long_latex = gt_tbl.as_latex(use_longtable=True)
```

The `tbl_pos=` argument controls the float placement when not using `longtable`. Valid options include `"!t"` (top), `"!b"` (bottom), `"!h"` (here), and `"!H"` (exactly here, requires the `float` package).

``` python
positioned_latex = gt_tbl.as_latex(tbl_pos="!h")
```

> **Note**
>
> LaTeX output is still experimental. Not all table features (such as certain styling options) are fully supported in the LaTeX renderer; the *Limitations* section of [as_latex()](../reference/GT.as_latex.md#great_tables.GT.as_latex) lists them.

The LaTeX fragment relies on a few LaTeX packages, so load them in your document's preamble: `booktabs` is always needed, `longtable` is needed with `use_longtable=True`, and `hyperref` is needed for links from [fmt_url()](../reference/GT.fmt_url.md#great_tables.GT.fmt_url) or [fmt_email()](../reference/GT.fmt_email.md#great_tables.GT.fmt_email). Adding `anyfontsize` lets a font size set with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) be used exactly:

``` latex
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{hyperref}
\usepackage{anyfontsize}
```

LaTeX output is the bridge between **Great Tables** and the world of academic publishing and typesetting. If you are writing papers in LaTeX or producing PDF reports via Quarto, this method lets you bring your Python-built tables into that workflow without manual conversion. You get the convenience of building tables programmatically in Python with the typographic quality of LaTeX's table rendering.

## Saving as an Image

The [gtsave()](../reference/GT.gtsave.md#great_tables.GT.gtsave) method renders your table as a high-quality image file. It supports PNG, JPEG, WebP, and PDF formats. Under the hood, it uses the `nokap` package to drive a headless Chrome browser for pixel-perfect rendering.

``` python
gt_tbl.gtsave("my_table.png")
```

The output format is determined by the file extension (a file name without one is saved as PNG). The supported formats are:

- `.png` for lossless raster images (great for reports and presentations)
- `.pdf` for vector output (ideal for print and LaTeX inclusion)
- `.jpeg` or `.jpg` for compressed raster images
- `.webp` for efficient web-optimized images

### Controlling Image Quality

The `zoom=` argument controls the resolution of raster outputs. The default value of `2.0` produces retina-quality images. Increase it for even higher resolution, or decrease it for smaller file sizes.

``` python
# High-resolution image for print
gt_tbl.gtsave("high_res.png", zoom=4.0)

# Standard resolution for web
gt_tbl.gtsave("standard.png", zoom=1.0)
```

A `zoom=4.0` value produces an image with twice the resolution of the default, which is ideal for print materials where crisp text is essential. The `zoom=` setting doesn't apply to PDF output, which is already vector-based.

### Padding Around the Table

The `expand=` argument adds padding (in pixels) around the captured table element (the default is `5`). You can provide a single integer for uniform padding or a tuple of four values for `(top, right, bottom, left)`.

``` python
# Uniform padding
gt_tbl.gtsave("padded.png", expand=20)

# Asymmetric padding
gt_tbl.gtsave("asymmetric.png", expand=(10, 20, 10, 20))
```

Adding padding is especially useful when the saved image will be placed on a colored background or inside a slide layout where the table edge needs breathing room.

### Viewport Dimensions

The `vwidth=` and `vheight=` arguments set the virtual viewport size. This can affect how responsive table layouts are rendered (the defaults are `992` and `744` pixels).

``` python
gt_tbl.gtsave("wide_viewport.png", vwidth=1200)
```

A wider viewport can prevent the table from wrapping or truncating columns, while a narrower one can test how the table responds to constrained width.

### Rendering Delay

Some tables with custom fonts or dynamic content may need a short delay after page load before the screenshot is taken. The `delay=` argument (in seconds, defaulting to `0.2`) controls this wait time.

``` python
gt_tbl.gtsave("with_delay.png", delay=0.5)
```

> **Note**
>
> For images and PDF, the [gtsave()](../reference/GT.gtsave.md#great_tables.GT.gtsave) method requires the `nokap` package and a Chrome or Chromium browser to be installed on your system.

## Saving as SVG, Word, Excel, and More

The [gtsave()](../reference/GT.gtsave.md#great_tables.GT.gtsave) method also saves a table as SVG, a Word document, an Excel workbook, a PowerPoint presentation, RTF, or Typst. These files are written by [gridwell](https://github.com/rich-iannone/gridwell), which draws the same table, with its formatting and styles, in each format's own terms (as far as each format allows), with no browser involved. Install it with the `gridwell` extra:

``` bash
pip install "great_tables[gridwell]"
```

Then choose the format by the file extension, just as with images:

``` python
gt_tbl.gtsave("my_table.svg")   # SVG
gt_tbl.gtsave("my_table.docx")  # Word
gt_tbl.gtsave("my_table.xlsx")  # Excel
gt_tbl.gtsave("my_table.pptx")  # PowerPoint
gt_tbl.gtsave("my_table.rtf")   # RTF
gt_tbl.gtsave("my_table.typ")   # Typst
```

The image options (`zoom=`, `expand=`, and the rest) don't apply to these formats. In an Excel workbook, each cell holds the number, date, or boolean behind its formatted text, so the values can still be summed and sorted. SVG output is experimental in gridwell for now: it is valid and has every cell, but its styling may change between gridwell releases.

## Choosing the Right Export Method

The following table summarizes when to use each export approach:

``` python
import polars as pl

export_df = pl.DataFrame({
    "Method": ["show()", "as_raw_html()", "as_latex()", "gtsave()", "gtsave() with gridwell"],
    "Use Case": [
        "Interactive display in notebooks or browser",
        "Embedding in web apps, emails, or HTML docs",
        "Inclusion in LaTeX/PDF documents",
        "Static image files for reports and slides",
        "Office documents, vector graphics, and Typst",
    ],
    "Output": [
        "Rendered display",
        "HTML string",
        "LaTeX string",
        "PNG/PDF/JPEG/WebP file",
        "SVG/DOCX/XLSX/PPTX/RTF/Typst file",
    ],
})

GT(export_df)
```

| Method | Use Case | Output |
|----|----|----|
| show() | Interactive display in notebooks or browser | Rendered display |
| as_raw_html() | Embedding in web apps, emails, or HTML docs | HTML string |
| as_latex() | Inclusion in LaTeX/PDF documents | LaTeX string |
| gtsave() | Static image files for reports and slides | PNG/PDF/JPEG/WebP file |
| gtsave() with gridwell | Office documents, vector graphics, and Typst | SVG/DOCX/XLSX/PPTX/RTF/Typst file |

Each export method preserves the styling, formatting, and structural components you have built into your table. Choose the method that matches your final output medium, and your carefully crafted table will look great wherever it lands.
