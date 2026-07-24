## GT.cols_hide()


Hide one or more columns.


Usage

``` python
GT.cols_hide(columns)
```


The [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) method allows us to hide one or more columns from appearing in the final output table. While it's possible and often desirable to omit columns from the input table data before introduction to the [GT()](GT.md#great_tables.GT) class, there can be cases where the data in certain columns is useful (as a column reference during formatting of other columns) but the final display of those columns is not necessary.


## Parameters


`columns: SelectExpr`  
The columns to hide in the output display table. Can either be a single column name or a series of column names provided in a list.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

For this example, we'll use a portion of the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a simple table. Let's hide the `year` column with the [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) method.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Benin"][
    ["country_name", "year", "population"]
].tail(5)

GT(countrypops_mini).cols_hide(columns="year")
```


<style>
#zmjcxkjhcb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zmjcxkjhcb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zmjcxkjhcb p { margin: 0; padding: 0; }
 #zmjcxkjhcb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zmjcxkjhcb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zmjcxkjhcb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zmjcxkjhcb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zmjcxkjhcb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zmjcxkjhcb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zmjcxkjhcb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zmjcxkjhcb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zmjcxkjhcb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zmjcxkjhcb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zmjcxkjhcb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zmjcxkjhcb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zmjcxkjhcb .gt_spanner_row { border-bottom-style: hidden; }
 #zmjcxkjhcb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zmjcxkjhcb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zmjcxkjhcb .gt_from_md> :first-child { margin-top: 0; }
 #zmjcxkjhcb .gt_from_md> :last-child { margin-bottom: 0; }
 #zmjcxkjhcb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zmjcxkjhcb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zmjcxkjhcb .gt_indent_1 { text-indent: 5px; }
 #zmjcxkjhcb .gt_indent_2 { text-indent: calc(5px * 2); }
 #zmjcxkjhcb .gt_indent_3 { text-indent: calc(5px * 3); }
 #zmjcxkjhcb .gt_indent_4 { text-indent: calc(5px * 4); }
 #zmjcxkjhcb .gt_indent_5 { text-indent: calc(5px * 5); }
 #zmjcxkjhcb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zmjcxkjhcb .gt_row_group_first td { border-top-width: 2px; }
 #zmjcxkjhcb .gt_row_group_first th { border-top-width: 2px; }
 #zmjcxkjhcb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zmjcxkjhcb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zmjcxkjhcb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zmjcxkjhcb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zmjcxkjhcb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zmjcxkjhcb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zmjcxkjhcb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zmjcxkjhcb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zmjcxkjhcb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zmjcxkjhcb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zmjcxkjhcb .gt_left { text-align: left; }
 #zmjcxkjhcb .gt_center { text-align: center; }
 #zmjcxkjhcb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zmjcxkjhcb .gt_font_normal { font-weight: normal; }
 #zmjcxkjhcb .gt_font_bold { font-weight: bold; }
 #zmjcxkjhcb .gt_font_italic { font-style: italic; }
 #zmjcxkjhcb .gt_super { font-size: 65%; }
 #zmjcxkjhcb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zmjcxkjhcb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zmjcxkjhcb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zmjcxkjhcb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zmjcxkjhcb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zmjcxkjhcb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| country_name | population |
|--------------|------------|
| Benin        | 11940683   |
| Benin        | 12290444   |
| Benin        | 12643123   |
| Benin        | 12996895   |
| Benin        | 13352864   |


## Details

The hiding of columns is internally a rendering directive, so, all columns that are 'hidden' are still accessible and useful in any expression provided to a `rows` argument. Furthermore, the [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) method (as with many of the methods available in **Great Tables**) can be placed anywhere in a chain of calls (acting as a promise to hide columns when the timing is right). However there's perhaps greater readability when placing this call closer to the end of such a chain. The [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) method quietly changes the visible state of a column and doesn't yield warnings when changing the state of already-invisible columns.
