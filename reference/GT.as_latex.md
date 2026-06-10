## GT.as_latex()


Output a GT object as LaTeX


Usage

``` python
GT.as_latex(
    use_longtable=False,
    tbl_pos=None,
)
```


The [as_latex()](GT.as_latex.md#great_tables.GT.as_latex) method outputs a GT object as a LaTeX fragment. This method is useful for when you need to include a table as part of a LaTeX document. The LaTeX fragment contains the table as a string.

> **Warning: Warning**
>
> [as_latex()](GT.as_latex.md#great_tables.GT.as_latex) is still experimental.


## Parameters


`use_longtable: bool = ``False`  
An option to use the `longtable` environment in LaTeX output. This is useful for tables that span multiple pages and don't require precise positioning.

`tbl_pos: str | None = None`  
The position of the table in the LaTeX output when `use_longtable=False`. Valid values for positioning include `"!t"` (top of page), `"!b"` (bottom of the page), `"!h"` (here), `"!p"` (on a separate page), and `"!H"` (exactly here). If a value is not provided then the table will be placed at the top of the page; if in the Quarto render then the table positioning option will be ignored in favor of any setting within the Quarto rendering environment.


## Returns


`str`  
A LaTeX fragment that contains the table.


## Limitations

The [as_latex()](GT.as_latex.md#great_tables.GT.as_latex) method is still experimental and has some limitations. The following functionality that is supported in HTML output tables is not currently supported in LaTeX output tables:

- footnotes (via the [tab_footnote()](GT.tab_footnote.md#great_tables.GT.tab_footnote) method)
- the rendering of the stub and row group labels (via the `=rowname_col` and `=groupname_col` args in the [GT()](GT.md#great_tables.GT) class)
- the use of the [md()](md.md#great_tables.md) helper function to signal conversion of Markdown text
- units notation within the `cols_labels()` and [tab_spanner()](GT.tab_spanner.md#great_tables.GT.tab_spanner) methods
- the [fmt_markdown()](GT.fmt_markdown.md#great_tables.GT.fmt_markdown), [fmt_units()](GT.fmt_units.md#great_tables.GT.fmt_units), [fmt_image()](GT.fmt_image.md#great_tables.GT.fmt_image), and [fmt_nanoplot()](GT.fmt_nanoplot.md#great_tables.GT.fmt_nanoplot) methods
- the [sub_missing()](GT.sub_missing.md#great_tables.GT.sub_missing) and [sub_zero()](GT.sub_zero.md#great_tables.GT.sub_zero) methods
- most options in the [tab_options()](GT.tab_options.md#great_tables.GT.tab_options) method, particularly those that are specific to styling text, borders, or adding fill colors to cells

As development continues, we will work to expand the capabilities of the [as_latex()](GT.as_latex.md#great_tables.GT.as_latex) method to reduce these limitations and more clearly document what is and is not supported.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset to create a new table.


``` python
from great_tables import GT
from great_tables.data import gtcars
import polars as pl

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select(["mfr", "model", "msrp"])
    .head(5)
)

gt_tbl = (
    GT(gtcars_mini)
    .tab_header(
        title="Data Listing from the gtcars Dataset",
        subtitle="Only five rows from the dataset are shown here."
    )
    .fmt_currency(columns="msrp")
)

gt_tbl
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data Listing from the gtcars Dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Only five rows from the dataset are shown here.</th>
</tr>
<tr class="gt_col_headings">
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">$447,000.00</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">$291,744.00</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">$263,553.00</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">$233,509.00</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">$245,400.00</td>
</tr>
</tbody>
</table>


Now we can return the table as string of LaTeX code using the [as_latex()](GT.as_latex.md#great_tables.GT.as_latex) method.


``` python
gt_tbl.as_latex()
```


    '\\begin{table}\n\\caption*{\n{\\large Data Listing from the gtcars Dataset} \\\\\n{\\small Only five rows from the dataset are shown here.}\n} \n\n\\fontsize{12.0pt}{14.4pt}\\selectfont\n\n\\begin{tabular*}{\\linewidth}{@{\\extracolsep{\\fill}}llr}\n\\toprule\nmfr & model & msrp \\\\ \n\\midrule\\addlinespace[2.5pt]\nFord & GT & \\$447,000.00 \\\\\nFerrari & 458 Speciale & \\$291,744.00 \\\\\nFerrari & 458 Spider & \\$263,553.00 \\\\\nFerrari & 458 Italia & \\$233,509.00 \\\\\nFerrari & 488 GTB & \\$245,400.00 \\\\\n\\bottomrule\n\\end{tabular*}\n\n\\end{table}\n'


The LaTeX string contains the code just for the table (it's not a complete LaTeX document). This output can be useful for embedding a GT table in an existing LaTeX document.
