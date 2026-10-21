# Exporting and Saving Tables

Once you have built a table, you need to get it into its final destination. That might be a notebook cell, a standalone HTML file, a LaTeX document, or an image file for inclusion in a report or presentation. **Great Tables** provides several export methods to cover these use cases, each with options to control the output format.

The general principle is: build your table once, export it many ways. The same [GT](../reference/GT.md#great_tables.GT) object can be displayed interactively, saved as HTML, rendered as LaTeX, or captured as an image. This means you don't need to maintain separate table-building code for different output formats. Your single chain of formatting, styling, and structural methods produces the canonical table, and the export step simply serializes it for the target medium.


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


<style>
#gbtfujueds table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gbtfujueds thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gbtfujueds p { margin: 0; padding: 0; }
 #gbtfujueds .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gbtfujueds .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gbtfujueds .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gbtfujueds .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gbtfujueds .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gbtfujueds .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gbtfujueds .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gbtfujueds .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gbtfujueds .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gbtfujueds .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gbtfujueds .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gbtfujueds .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gbtfujueds .gt_spanner_row { border-bottom-style: hidden; }
 #gbtfujueds .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gbtfujueds .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gbtfujueds .gt_from_md> :first-child { margin-top: 0; }
 #gbtfujueds .gt_from_md> :last-child { margin-bottom: 0; }
 #gbtfujueds .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gbtfujueds .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gbtfujueds .gt_indent_1 { text-indent: 5px; }
 #gbtfujueds .gt_indent_2 { text-indent: calc(5px * 2); }
 #gbtfujueds .gt_indent_3 { text-indent: calc(5px * 3); }
 #gbtfujueds .gt_indent_4 { text-indent: calc(5px * 4); }
 #gbtfujueds .gt_indent_5 { text-indent: calc(5px * 5); }
 #gbtfujueds .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gbtfujueds .gt_row_group_first td { border-top-width: 2px; }
 #gbtfujueds .gt_row_group_first th { border-top-width: 2px; }
 #gbtfujueds .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gbtfujueds .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gbtfujueds .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gbtfujueds .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gbtfujueds .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gbtfujueds .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gbtfujueds .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gbtfujueds .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gbtfujueds .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gbtfujueds .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gbtfujueds .gt_left { text-align: left; }
 #gbtfujueds .gt_center { text-align: center; }
 #gbtfujueds .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gbtfujueds .gt_font_normal { font-weight: normal; }
 #gbtfujueds .gt_font_bold { font-weight: bold; }
 #gbtfujueds .gt_font_italic { font-style: italic; }
 #gbtfujueds .gt_super { font-size: 65%; }
 #gbtfujueds .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gbtfujueds .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gbtfujueds .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gbtfujueds .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gbtfujueds .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gbtfujueds .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Example Table</th>
</tr>
<tr class="gt_heading">
<th colspan="3" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">A small demonstration</th>
</tr>
<tr class="gt_col_headings">
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right" headers="num">0.11</td>
<td class="gt_row gt_left" headers="char">apricot</td>
<td class="gt_row gt_right" headers="currency">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="num">2.22</td>
<td class="gt_row gt_left" headers="char">banana</td>
<td class="gt_row gt_right" headers="currency">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="num">33.33</td>
<td class="gt_row gt_left" headers="char">coconut</td>
<td class="gt_row gt_right" headers="currency">$1.39</td>
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

The [as_raw_html()](../reference/GT.as_raw_html.md#great_tables.GT.as_raw_html) method returns the table as an HTML string. This is useful for embedding tables in web applications, email templates, or custom HTML documents. Body cells that have not been processed by a `fmt_*()` method are automatically HTML-escaped to prevent cross-site scripting (XSS) when rendering untrusted data. See the [Formatting Values](formatting-values.md) guide for details on how to include raw HTML in cells using [html()](../reference/html.md#great_tables.html) and [fmt()](../reference/GT.fmt.md#great_tables.GT.fmt).


``` python
html_str = gt_tbl.as_raw_html()

# Show the first 200 characters to see the structure
print(html_str[:200])
```


    <div id="ttckpaggst" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
    <style>
    #ttckpaggst table {
              font


The method accepts several arguments that control the output format.


## Inline CSS for Email

Email clients typically strip `<style>` blocks, so you need inline CSS for the table to render correctly. Set `inline_css=True` to move all styles into `style` attributes.

``` python
email_html = gt_tbl.as_raw_html(inline_css=True)
```

With inline CSS, your table will render correctly in Gmail, Outlook, and other email clients that strip external stylesheets.

This matters because most email clients aggressively strip `<style>` blocks and external CSS references for security reasons. Without inline CSS, your carefully styled table will appear as plain, unstyled HTML in the recipient's inbox. If you are sharing tables via email (whether through automated reports or one-off sends), `inline_css=True` is almost always what you want.


## Complete HTML Page

If you need a self-contained HTML document (with `<html>`, `<head>`, and `<body>` tags), set `make_page=True`.

``` python
full_page = gt_tbl.as_raw_html(make_page=True)
```

This wraps the table in a complete HTML document that can be opened directly in any browser without additional scaffolding.


## Writing HTML to a File

The [write_raw_html()](../reference/GT.write_raw_html.md#great_tables.GT.write_raw_html) method is a convenience wrapper that writes the HTML output directly to a file.

``` python
gt_tbl.write_raw_html("my_table.html")
```

The file is written with the same options available on [as_raw_html()](../reference/GT.as_raw_html.md#great_tables.GT.as_raw_html) (such as `inline_css=` and `make_page=`), passed through as keyword arguments.


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
> LaTeX output is still experimental. Not all table features (such as certain styling options) are fully supported in the LaTeX renderer; the *Limitations* section of [as_latex()](../reference/GT.as_latex.md#great_tables.GT.as_latex) lists them.

The LaTeX fragment relies on a few LaTeX packages, so load them in your document's preamble: `booktabs` is always needed, `longtable` is needed with `use_longtable=True`, and `hyperref` is needed for links from [fmt_url()](../reference/GT.fmt_url.md#great_tables.GT.fmt_url) or [fmt_email()](../reference/GT.fmt_email.md#great_tables.GT.fmt_email). Adding `anyfontsize` lets a font size set with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) be used exactly:

``` latex
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{hyperref}
\usepackage{anyfontsize}
```

LaTeX output is the bridge between Great Tables and the world of academic publishing and typesetting. If you are writing papers in LaTeX or producing PDF reports via Quarto, this method lets you bring your Python-built tables into that workflow without manual conversion. You get the convenience of building tables programmatically in Python with the typographic quality of LaTeX's table rendering.


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

A `zoom=4.0` value produces an image four times the default resolution, which is ideal for print materials where crisp text is essential.


## Padding Around the Table

The `expand=` argument adds padding (in pixels) around the captured table element. You can provide a single integer for uniform padding or a tuple of four values for `(top, right, bottom, left)`.

``` python
# Uniform padding
gt_tbl.gtsave("padded.png", expand=20)

# Asymmetric padding
gt_tbl.gtsave("asymmetric.png", expand=(10, 20, 10, 20))
```

Adding padding is especially useful when the saved image will be placed on a colored background or inside a slide layout where the table edge needs breathing room.


## Viewport Dimensions

The `vwidth=` and `vheight=` arguments set the virtual viewport size. This can affect how responsive table layouts are rendered.

``` python
gt_tbl.gtsave("wide_viewport.png", vwidth=1200)
```

A wider viewport can prevent the table from wrapping or truncating columns, while a narrower one can test how the table responds to constrained width.


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


<style>
#mjsekgnkiq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mjsekgnkiq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mjsekgnkiq p { margin: 0; padding: 0; }
 #mjsekgnkiq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mjsekgnkiq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mjsekgnkiq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mjsekgnkiq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mjsekgnkiq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mjsekgnkiq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mjsekgnkiq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mjsekgnkiq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mjsekgnkiq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mjsekgnkiq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mjsekgnkiq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mjsekgnkiq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mjsekgnkiq .gt_spanner_row { border-bottom-style: hidden; }
 #mjsekgnkiq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mjsekgnkiq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mjsekgnkiq .gt_from_md> :first-child { margin-top: 0; }
 #mjsekgnkiq .gt_from_md> :last-child { margin-bottom: 0; }
 #mjsekgnkiq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mjsekgnkiq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mjsekgnkiq .gt_indent_1 { text-indent: 5px; }
 #mjsekgnkiq .gt_indent_2 { text-indent: calc(5px * 2); }
 #mjsekgnkiq .gt_indent_3 { text-indent: calc(5px * 3); }
 #mjsekgnkiq .gt_indent_4 { text-indent: calc(5px * 4); }
 #mjsekgnkiq .gt_indent_5 { text-indent: calc(5px * 5); }
 #mjsekgnkiq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mjsekgnkiq .gt_row_group_first td { border-top-width: 2px; }
 #mjsekgnkiq .gt_row_group_first th { border-top-width: 2px; }
 #mjsekgnkiq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mjsekgnkiq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mjsekgnkiq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mjsekgnkiq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mjsekgnkiq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mjsekgnkiq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mjsekgnkiq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mjsekgnkiq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mjsekgnkiq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mjsekgnkiq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mjsekgnkiq .gt_left { text-align: left; }
 #mjsekgnkiq .gt_center { text-align: center; }
 #mjsekgnkiq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mjsekgnkiq .gt_font_normal { font-weight: normal; }
 #mjsekgnkiq .gt_font_bold { font-weight: bold; }
 #mjsekgnkiq .gt_font_italic { font-style: italic; }
 #mjsekgnkiq .gt_super { font-size: 65%; }
 #mjsekgnkiq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mjsekgnkiq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mjsekgnkiq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mjsekgnkiq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mjsekgnkiq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mjsekgnkiq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Method | Use Case | Output |
|----|----|----|
| show() | Interactive display in notebooks or browser | Rendered display |
| as_raw_html() | Embedding in web apps, emails, or HTML docs | HTML string |
| as_latex() | Inclusion in LaTeX/PDF documents | LaTeX string |
| gtsave() | Static image files for reports and slides | PNG/PDF/JPEG/WebP file |


Each export method preserves the styling, formatting, and structural components you have built into your table. Choose the method that matches your final output medium, and your carefully crafted table will look great wherever it lands.
