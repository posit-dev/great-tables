# GT.cols_align()


Set the alignment of one or more columns.


Usage

``` python
GT.cols_align(
    align="left",
    columns=None,
)
```


The [cols_align()](GT.cols_align.md#great_tables.GT.cols_align) method sets the alignment of one or more columns. The `align` argument can be set to one of `"left"`, `"center"`, or `"right"` and the `columns` argument can be used to specify which columns to apply the alignment to. If `columns` is not specified, the alignment is applied to all columns.


## Parameters


`align: str = ``"left"`  
The alignment to apply. Must be one of `"left"`, `"center"`, or `"right"`.

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. If `None`, the alignment is applied to all columns.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [countrypops](data.countrypops.md#great_tables.data.countrypops) to create a small table. We can change the alignment of the `population` column with [cols_align()](GT.cols_align.md#great_tables.GT.cols_align). In this example, the column label and body cells of `population` will be aligned to the left.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "San Marino"][
    ["country_name", "year", "population"]
].tail(5)

(
    GT(countrypops_mini, rowname_col="year", groupname_col="country_name")
    .cols_align(align="left", columns="population")
)
```


<style>
#tjfgcllnam table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tjfgcllnam thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tjfgcllnam p { margin: 0; padding: 0; }
 #tjfgcllnam .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tjfgcllnam .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tjfgcllnam .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tjfgcllnam .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tjfgcllnam .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tjfgcllnam .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tjfgcllnam .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tjfgcllnam .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tjfgcllnam .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tjfgcllnam .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tjfgcllnam .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tjfgcllnam .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tjfgcllnam .gt_spanner_row { border-bottom-style: hidden; }
 #tjfgcllnam .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tjfgcllnam .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tjfgcllnam .gt_from_md> :first-child { margin-top: 0; }
 #tjfgcllnam .gt_from_md> :last-child { margin-bottom: 0; }
 #tjfgcllnam .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tjfgcllnam .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tjfgcllnam .gt_indent_1 { text-indent: 5px; }
 #tjfgcllnam .gt_indent_2 { text-indent: calc(5px * 2); }
 #tjfgcllnam .gt_indent_3 { text-indent: calc(5px * 3); }
 #tjfgcllnam .gt_indent_4 { text-indent: calc(5px * 4); }
 #tjfgcllnam .gt_indent_5 { text-indent: calc(5px * 5); }
 #tjfgcllnam .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tjfgcllnam .gt_row_group_first td { border-top-width: 2px; }
 #tjfgcllnam .gt_row_group_first th { border-top-width: 2px; }
 #tjfgcllnam .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tjfgcllnam .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tjfgcllnam .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tjfgcllnam .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tjfgcllnam .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tjfgcllnam .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tjfgcllnam .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tjfgcllnam .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tjfgcllnam .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tjfgcllnam .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tjfgcllnam .gt_left { text-align: left; }
 #tjfgcllnam .gt_center { text-align: center; }
 #tjfgcllnam .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tjfgcllnam .gt_font_normal { font-weight: normal; }
 #tjfgcllnam .gt_font_bold { font-weight: bold; }
 #tjfgcllnam .gt_font_italic { font-style: italic; }
 #tjfgcllnam .gt_super { font-size: 65%; }
 #tjfgcllnam .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tjfgcllnam .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tjfgcllnam .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tjfgcllnam .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tjfgcllnam .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tjfgcllnam .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="population" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">population</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">San Marino</th>
</tr>

<tr>
<th class="gt_row gt_left gt_stub">2018</th>
<td class="gt_row gt_left">34156</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">2019</th>
<td class="gt_row gt_left">34178</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">2020</th>
<td class="gt_row gt_left">34007</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">2021</th>
<td class="gt_row gt_left">33745</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">2022</th>
<td class="gt_row gt_left">33660</td>
</tr>
</tbody>
</table>
