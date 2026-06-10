# Exporting and Saving Tables

Once you have built a table, you need to get it into its final destination. That might be a notebook cell, a standalone HTML file, a LaTeX document, or an image file for inclusion in a report or presentation. **Great Tables** provides several export methods to cover these use cases, each with options to control the output format.


# Displaying Tables

In most notebook environments (Jupyter, Quarto, Marimo), simply placing a [GT](../reference/GT.md#great_tables.GT) object as the last expression in a cell will render the table automatically. However, you can also use the [show()](../reference/GT.show.md#great_tables.GT.show) method for explicit control over where the table is displayed.


``` python
from great_tables import GT
from great_tables.data import exibble

gt_tbl = (
    GT(exibble.head(3)[["num", "char", "currency"]])
    .tab_header(title="Example Table", subtitle="A small demonstration")
    .fmt_currency(columns="currency")
    .fmt_number(columns="num", decimals=2)
)

gt_tbl.show()
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Example Table</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">A small demonstration</th>
</tr>
<tr class="gt_col_headings">
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
</tbody>
</table>


The `target=` argument controls the display destination. The available options are:

- `"auto"` (the default): displays inline in a notebook if possible, otherwise opens a browser window.
- `"notebook"`: forces inline notebook display.
- `"browser"`: opens the table in your default web browser. This is particularly useful when working in the console or when you want to see the full styled output that some IDEs may suppress.

``` python
# Open in a browser window (useful when running from a script or console)
gt_tbl.show(target="browser")
```


# Getting HTML as a String

The [as_raw_html()](../reference/GT.as_raw_html.md#great_tables.GT.as_raw_html) method returns the table as an HTML string. This is useful for embedding tables in web applications, email templates, or custom HTML documents.


``` python
html_str = gt_tbl.as_raw_html()

# Show the first 200 characters to see the structure
print(html_str[:200])
```


    <div id="clqwtspiuc" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
    <style>
    #clqwtspiuc table {
              font


The method accepts several arguments that control the output format.


## Inline CSS for Email

Email clients typically strip `<style>` blocks, so you need inline CSS for the table to render correctly. Set `inline_css=True` to move all styles into [style](../reference/style.text.md#great_tables.style.text.style) attributes.

``` python
email_html = gt_tbl.as_raw_html(inline_css=True)
```


## Complete HTML Page

If you need a self-contained HTML document (with `<html>`, `<head>`, and `<body>` tags), set `make_page=True`.

``` python
full_page = gt_tbl.as_raw_html(make_page=True)
```


## Writing HTML to a File

The [write_raw_html()](../reference/GT.write_raw_html.md#great_tables.GT.write_raw_html) method is a convenience wrapper that writes the HTML output directly to a file.

``` python
gt_tbl.write_raw_html("my_table.html")
```


# LaTeX Output

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

> **Note: Note**
>
> LaTeX output is still experimental. Not all table features (such as certain styling options) are fully supported in the LaTeX renderer.


# Saving as an Image

The [gtsave()](../reference/GT.gtsave.md#great_tables.GT.gtsave) method renders your table as a high-quality image file. It supports PNG, JPEG, WebP, and PDF formats. Under the hood, it uses the `nokap` package to drive a headless Chrome browser for pixel-perfect rendering.

``` python
gt_tbl.gtsave("my_table.png")
```

The output format is determined by the file extension. Here are some common formats:

- `.png` for lossless raster images (great for reports and presentations)
- `.pdf` for vector output (ideal for print and LaTeX inclusion)
- `.jpeg` or `.jpg` for compressed raster images
- `.webp` for efficient web-optimized images


## Controlling Image Quality

The `zoom=` argument controls the resolution of raster outputs. The default value of `2.0` produces retina-quality images. Increase it for even higher resolution, or decrease it for smaller file sizes.

``` python
# High-resolution image for print
gt_tbl.gtsave("high_res.png", zoom=4.0)

# Standard resolution for web
gt_tbl.gtsave("standard.png", zoom=1.0)
```


## Padding Around the Table

The `expand=` argument adds padding (in pixels) around the captured table element. You can provide a single integer for uniform padding or a tuple of four values for `(top, right, bottom, left)`.

``` python
# Uniform padding
gt_tbl.gtsave("padded.png", expand=20)

# Asymmetric padding
gt_tbl.gtsave("asymmetric.png", expand=(10, 20, 10, 20))
```


## Viewport Dimensions

The `vwidth=` and `vheight=` arguments set the virtual viewport size. This can affect how responsive table layouts are rendered.

``` python
gt_tbl.gtsave("wide_viewport.png", vwidth=1200)
```


## Rendering Delay

Some tables with custom fonts or dynamic content may need a short delay after page load before the screenshot is taken. The `delay=` argument (in seconds) controls this wait time.

``` python
gt_tbl.gtsave("with_delay.png", delay=0.5)
```

> **Note: Note**
>
> The [gtsave()](../reference/GT.gtsave.md#great_tables.GT.gtsave) method requires the `nokap` package and a Chrome or Chromium browser to be installed on your system.


# Choosing the Right Export Method

The following table summarizes when to use each export approach:


``` python
import polars as pl

export_df = pl.DataFrame({
    "Method": ["show()", "as_raw_html()", "as_latex()", "gtsave()"],
    "Use Case": [
        "Interactive display in notebooks or browser",
        "Embedding in web apps, emails, or HTML docs",
        "Inclusion in LaTeX/PDF documents",
        "Static image files for reports and slides",
    ],
    "Output": ["Rendered display", "HTML string", "LaTeX string", "PNG/PDF/JPEG/WebP file"],
})

GT(export_df)
```


| Method | Use Case | Output |
|----|----|----|
| show() | Interactive display in notebooks or browser | Rendered display |
| as_raw_html() | Embedding in web apps, emails, or HTML docs | HTML string |
| as_latex() | Inclusion in LaTeX/PDF documents | LaTeX string |
| gtsave() | Static image files for reports and slides | PNG/PDF/JPEG/WebP file |


Each export method preserves the styling, formatting, and structural components you have built into your table. Choose the method that matches your final output medium, and your carefully crafted table will look great wherever it lands.
