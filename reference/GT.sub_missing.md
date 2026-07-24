## GT.sub_missing()


Substitute missing values in the table body.


Usage

``` python
GT.sub_missing(
    columns=None,
    rows=None,
    missing_text=None,
)
```


Wherever there is missing data (i.e., `None` values) customizable content may present better than the standard representation of missing values that would otherwise appear. The [sub_missing()](GT.sub_missing.md#great_tables.GT.sub_missing) method allows for this replacement through its `missing_text=` argument. And by not supplying anything to `missing_text=`, an em dash will serve as a default indicator of missingness.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should be scanned for missing values. The default is all rows, resulting in all rows in all targeted columns being considered for this substitution. Alternatively, we can supply a list of row indices.

`missing_text: str | Text | None = None`  
The text to be used in place of missing values in the rendered table. We can optionally use the <a href="md.html#great_tables.md" class="gdls-link"><code>md()</code></a> or <a href="html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions to style the text as Markdown or to retain HTML elements in the text.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [exibble](data.exibble.md#great_tables.data.exibble) dataset, let's create a new table. The missing values in two selections of columns will be given different variations of replacement text (across two separate calls of [sub_missing()](GT.sub_missing.md#great_tables.GT.sub_missing)).


``` python
from great_tables import GT, md, html, exibble
import polars as pl
import polars.selectors as cs

exibble_mini = pl.from_pandas(exibble).drop("row", "group", "fctr").slice(4, 8)

(
    GT(exibble_mini)
    .sub_missing(
        columns=["num", "char"],
        missing_text="missing"
    )
    .sub_missing(
        columns=cs.contains(("date", "time")) | cs.by_name("currency"),
        missing_text="nothing"
    )
)
```


<style>
#nvddsfpuhi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nvddsfpuhi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nvddsfpuhi p { margin: 0; padding: 0; }
 #nvddsfpuhi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nvddsfpuhi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nvddsfpuhi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nvddsfpuhi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nvddsfpuhi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nvddsfpuhi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvddsfpuhi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nvddsfpuhi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nvddsfpuhi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nvddsfpuhi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nvddsfpuhi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nvddsfpuhi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nvddsfpuhi .gt_spanner_row { border-bottom-style: hidden; }
 #nvddsfpuhi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nvddsfpuhi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nvddsfpuhi .gt_from_md> :first-child { margin-top: 0; }
 #nvddsfpuhi .gt_from_md> :last-child { margin-bottom: 0; }
 #nvddsfpuhi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nvddsfpuhi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nvddsfpuhi .gt_indent_1 { text-indent: 5px; }
 #nvddsfpuhi .gt_indent_2 { text-indent: calc(5px * 2); }
 #nvddsfpuhi .gt_indent_3 { text-indent: calc(5px * 3); }
 #nvddsfpuhi .gt_indent_4 { text-indent: calc(5px * 4); }
 #nvddsfpuhi .gt_indent_5 { text-indent: calc(5px * 5); }
 #nvddsfpuhi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nvddsfpuhi .gt_row_group_first td { border-top-width: 2px; }
 #nvddsfpuhi .gt_row_group_first th { border-top-width: 2px; }
 #nvddsfpuhi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nvddsfpuhi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvddsfpuhi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nvddsfpuhi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nvddsfpuhi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvddsfpuhi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nvddsfpuhi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nvddsfpuhi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nvddsfpuhi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvddsfpuhi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nvddsfpuhi .gt_left { text-align: left; }
 #nvddsfpuhi .gt_center { text-align: center; }
 #nvddsfpuhi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nvddsfpuhi .gt_font_normal { font-weight: normal; }
 #nvddsfpuhi .gt_font_bold { font-weight: bold; }
 #nvddsfpuhi .gt_font_italic { font-style: italic; }
 #nvddsfpuhi .gt_super { font-size: 65%; }
 #nvddsfpuhi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvddsfpuhi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nvddsfpuhi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvddsfpuhi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nvddsfpuhi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nvddsfpuhi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num       | char       | date       | time    | datetime         | currency |
|-----------|------------|------------|---------|------------------|----------|
| 5550.0    | missing    | 2015-05-15 | 17:55   | 2018-05-05 04:00 | 1325.81  |
| missing   | fig        | 2015-06-15 | nothing | 2018-06-06 16:11 | 13.255   |
| 777000.0  | grapefruit | nothing    | 19:10   | 2018-07-07 05:22 | nothing  |
| 8880000.0 | honeydew   | 2015-08-15 | 20:20   | nothing          | 0.44     |
