# GT.as_latex()


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


<style>
#ggistlkasm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ggistlkasm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ggistlkasm p { margin: 0; padding: 0; }
 #ggistlkasm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ggistlkasm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ggistlkasm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ggistlkasm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ggistlkasm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ggistlkasm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ggistlkasm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ggistlkasm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ggistlkasm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ggistlkasm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ggistlkasm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ggistlkasm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ggistlkasm .gt_spanner_row { border-bottom-style: hidden; }
 #ggistlkasm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ggistlkasm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ggistlkasm .gt_from_md> :first-child { margin-top: 0; }
 #ggistlkasm .gt_from_md> :last-child { margin-bottom: 0; }
 #ggistlkasm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ggistlkasm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ggistlkasm .gt_indent_1 { text-indent: 5px; }
 #ggistlkasm .gt_indent_2 { text-indent: calc(5px * 2); }
 #ggistlkasm .gt_indent_3 { text-indent: calc(5px * 3); }
 #ggistlkasm .gt_indent_4 { text-indent: calc(5px * 4); }
 #ggistlkasm .gt_indent_5 { text-indent: calc(5px * 5); }
 #ggistlkasm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ggistlkasm .gt_row_group_first td { border-top-width: 2px; }
 #ggistlkasm .gt_row_group_first th { border-top-width: 2px; }
 #ggistlkasm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ggistlkasm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ggistlkasm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ggistlkasm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ggistlkasm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ggistlkasm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ggistlkasm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ggistlkasm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ggistlkasm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ggistlkasm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ggistlkasm .gt_left { text-align: left; }
 #ggistlkasm .gt_center { text-align: center; }
 #ggistlkasm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ggistlkasm .gt_font_normal { font-weight: normal; }
 #ggistlkasm .gt_font_bold { font-weight: bold; }
 #ggistlkasm .gt_font_italic { font-style: italic; }
 #ggistlkasm .gt_super { font-size: 65%; }
 #ggistlkasm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ggistlkasm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ggistlkasm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ggistlkasm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ggistlkasm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ggistlkasm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

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
