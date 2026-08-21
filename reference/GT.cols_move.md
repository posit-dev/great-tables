# GT.cols_move()


Move one or more columns.


Usage

``` python
GT.cols_move(
    columns,
    after,
)
```


On those occasions where you need to move columns this way or that way, we can make use of the [cols_move()](GT.cols_move.md#great_tables.GT.cols_move) method. While it's true that the movement of columns can be done upstream of **Great Tables**, it is much easier and less error prone to use the method provided here. The movement procedure here takes one or more specified columns (in the `columns` argument) and places them to the right of a different column (the `after` argument). The ordering of the `columns` to be moved is preserved, as is the ordering of all other columns in the table.

The columns supplied in `columns` must all exist in the table and none of them can be in the `after` argument. The `after` column must also exist and only one column should be provided here. If you need to place one more or columns at the beginning of the column series, the [cols_move_to_start()](GT.cols_move_to_start.md#great_tables.GT.cols_move_to_start) method should be used. Similarly, if those columns to move should be placed at the end of the column series then use [cols_move_to_end()](GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end).


## Parameters


`columns: SelectExpr`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`after: str`  
The column after which the `columns` should be placed. This can be any column name that exists in the table.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a table. We'll choose to position the `population` column after the `country_name` column by using the [cols_move()](GT.cols_move.md#great_tables.GT.cols_move) method.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Japan"][
    ["country_name", "year", "population"]
].tail(5)

(
    GT(countrypops_mini)
    .cols_move(
        columns="population",
        after="country_name"
    )
)
```


<style>
#xxcusumojw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xxcusumojw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xxcusumojw p { margin: 0; padding: 0; }
 #xxcusumojw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xxcusumojw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xxcusumojw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xxcusumojw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xxcusumojw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xxcusumojw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xxcusumojw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xxcusumojw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xxcusumojw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xxcusumojw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xxcusumojw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xxcusumojw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xxcusumojw .gt_spanner_row { border-bottom-style: hidden; }
 #xxcusumojw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xxcusumojw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xxcusumojw .gt_from_md> :first-child { margin-top: 0; }
 #xxcusumojw .gt_from_md> :last-child { margin-bottom: 0; }
 #xxcusumojw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xxcusumojw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xxcusumojw .gt_indent_1 { text-indent: 5px; }
 #xxcusumojw .gt_indent_2 { text-indent: calc(5px * 2); }
 #xxcusumojw .gt_indent_3 { text-indent: calc(5px * 3); }
 #xxcusumojw .gt_indent_4 { text-indent: calc(5px * 4); }
 #xxcusumojw .gt_indent_5 { text-indent: calc(5px * 5); }
 #xxcusumojw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xxcusumojw .gt_row_group_first td { border-top-width: 2px; }
 #xxcusumojw .gt_row_group_first th { border-top-width: 2px; }
 #xxcusumojw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xxcusumojw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xxcusumojw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xxcusumojw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xxcusumojw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xxcusumojw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xxcusumojw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xxcusumojw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xxcusumojw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xxcusumojw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xxcusumojw .gt_left { text-align: left; }
 #xxcusumojw .gt_center { text-align: center; }
 #xxcusumojw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xxcusumojw .gt_font_normal { font-weight: normal; }
 #xxcusumojw .gt_font_bold { font-weight: bold; }
 #xxcusumojw .gt_font_italic { font-style: italic; }
 #xxcusumojw .gt_super { font-size: 65%; }
 #xxcusumojw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xxcusumojw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xxcusumojw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xxcusumojw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xxcusumojw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xxcusumojw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| country_name | population | year |
|--------------|------------|------|
| Japan        | 126811000  | 2018 |
| Japan        | 126633000  | 2019 |
| Japan        | 126261000  | 2020 |
| Japan        | 125681593  | 2021 |
| Japan        | 125124989  | 2022 |
