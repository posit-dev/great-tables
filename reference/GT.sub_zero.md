# GT.sub_zero()


Substitute zero values in the table body.


Usage

``` python
GT.sub_zero(
    columns=None,
    rows=None,
    zero_text="nil",
)
```


Wherever there is numerical data that are zero in value, replacement text may be better for explanatory purposes. The [sub_zero()](GT.sub_zero.md#great_tables.GT.sub_zero) function allows for this replacement through its `zero_text=` argument.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should be scanned for zeros. The default is all rows, resulting in all rows in all targeted columns being considered for this substitution. Alternatively, we can supply a list of row indices.

`zero_text: str = ``"nil"`  
The text to be used in place of zero values in the rendered table. We can optionally use the <a href="md.html#great_tables.md" class="gdls-link"><code>md()</code></a> or <a href="html.html#great_tables.html" class="gdls-link"><code>html()</code></a> functions to style the text as Markdown or to retain HTML elements in the text.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's generate a simple table that contains an assortment of values that could potentially undergo some substitution via the [sub_zero()](GT.sub_zero.md#great_tables.GT.sub_zero) method (i.e., there are two `0` values). The ordering of the <a href="GT.fmt_scientific.html#great_tables.GT.fmt_scientific" class="gdls-link"><code>fmt_scientific()</code></a> and [sub_zero()](GT.sub_zero.md#great_tables.GT.sub_zero) calls in the example below doesn't affect the final result since any `sub_*()` method won't interfere with the formatting of the table.


``` python
from great_tables import GT
import polars as pl

single_vals_df = pl.DataFrame(
    {
        "i": range(1, 8),
        "numbers": [2.75, 0, -3.2, 8, 1e-10, 0, 2.6e9]
    }
)

GT(single_vals_df).fmt_scientific(columns="numbers").sub_zero()
```


<style>
#fvmokauazp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fvmokauazp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fvmokauazp p { margin: 0; padding: 0; }
 #fvmokauazp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fvmokauazp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fvmokauazp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fvmokauazp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fvmokauazp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fvmokauazp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fvmokauazp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fvmokauazp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fvmokauazp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fvmokauazp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fvmokauazp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fvmokauazp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fvmokauazp .gt_spanner_row { border-bottom-style: hidden; }
 #fvmokauazp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fvmokauazp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fvmokauazp .gt_from_md> :first-child { margin-top: 0; }
 #fvmokauazp .gt_from_md> :last-child { margin-bottom: 0; }
 #fvmokauazp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fvmokauazp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fvmokauazp .gt_indent_1 { text-indent: 5px; }
 #fvmokauazp .gt_indent_2 { text-indent: calc(5px * 2); }
 #fvmokauazp .gt_indent_3 { text-indent: calc(5px * 3); }
 #fvmokauazp .gt_indent_4 { text-indent: calc(5px * 4); }
 #fvmokauazp .gt_indent_5 { text-indent: calc(5px * 5); }
 #fvmokauazp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fvmokauazp .gt_row_group_first td { border-top-width: 2px; }
 #fvmokauazp .gt_row_group_first th { border-top-width: 2px; }
 #fvmokauazp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fvmokauazp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fvmokauazp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fvmokauazp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fvmokauazp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fvmokauazp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fvmokauazp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fvmokauazp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fvmokauazp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fvmokauazp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fvmokauazp .gt_left { text-align: left; }
 #fvmokauazp .gt_center { text-align: center; }
 #fvmokauazp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fvmokauazp .gt_font_normal { font-weight: normal; }
 #fvmokauazp .gt_font_bold { font-weight: bold; }
 #fvmokauazp .gt_font_italic { font-style: italic; }
 #fvmokauazp .gt_super { font-size: 65%; }
 #fvmokauazp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fvmokauazp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fvmokauazp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fvmokauazp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fvmokauazp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fvmokauazp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| i   | numbers                 |
|-----|-------------------------|
| 1   | 2.75                    |
| 2   | nil                     |
| 3   | −3.20                   |
| 4   | 8.00                    |
| 5   | 1.00 × 10<sup>−10</sup> |
| 6   | nil                     |
| 7   | 2.60 × 10<sup>9</sup>   |
