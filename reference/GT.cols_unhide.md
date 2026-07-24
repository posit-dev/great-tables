## GT.cols_unhide()


Unhide one or more columns.


Usage

``` python
GT.cols_unhide(columns)
```


The [cols_unhide()](GT.cols_unhide.md#great_tables.GT.cols_unhide) method allows us to unhide one or more columns from appearing in the final output table. This may be important in cases where the user obtains a [GT](GT.md#great_tables.GT) instance with hidden columns and there is motivation to reveal one or more of those.


## Parameters


`columns: SelectExpr`  
The columns to unhide in the output display table. Can either be a single column name or a series of column names provided in a list.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

For this example, we'll use a portion of the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a simple table. We'll hide the `year` column using [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) and then unhide it with [cols_unhide()](GT.cols_unhide.md#great_tables.GT.cols_unhide), ensuring that the `year` column remains visible in the table.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Benin"][
    ["country_name", "year", "population"]
].tail(5)

GT(countrypops_mini).cols_hide(columns="year").cols_unhide(columns="year")
```


<style>
#zfoyhoozfw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zfoyhoozfw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zfoyhoozfw p { margin: 0; padding: 0; }
 #zfoyhoozfw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zfoyhoozfw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zfoyhoozfw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zfoyhoozfw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zfoyhoozfw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zfoyhoozfw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zfoyhoozfw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zfoyhoozfw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zfoyhoozfw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zfoyhoozfw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zfoyhoozfw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zfoyhoozfw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zfoyhoozfw .gt_spanner_row { border-bottom-style: hidden; }
 #zfoyhoozfw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zfoyhoozfw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zfoyhoozfw .gt_from_md> :first-child { margin-top: 0; }
 #zfoyhoozfw .gt_from_md> :last-child { margin-bottom: 0; }
 #zfoyhoozfw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zfoyhoozfw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zfoyhoozfw .gt_indent_1 { text-indent: 5px; }
 #zfoyhoozfw .gt_indent_2 { text-indent: calc(5px * 2); }
 #zfoyhoozfw .gt_indent_3 { text-indent: calc(5px * 3); }
 #zfoyhoozfw .gt_indent_4 { text-indent: calc(5px * 4); }
 #zfoyhoozfw .gt_indent_5 { text-indent: calc(5px * 5); }
 #zfoyhoozfw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zfoyhoozfw .gt_row_group_first td { border-top-width: 2px; }
 #zfoyhoozfw .gt_row_group_first th { border-top-width: 2px; }
 #zfoyhoozfw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zfoyhoozfw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zfoyhoozfw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zfoyhoozfw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zfoyhoozfw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zfoyhoozfw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zfoyhoozfw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zfoyhoozfw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zfoyhoozfw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zfoyhoozfw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zfoyhoozfw .gt_left { text-align: left; }
 #zfoyhoozfw .gt_center { text-align: center; }
 #zfoyhoozfw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zfoyhoozfw .gt_font_normal { font-weight: normal; }
 #zfoyhoozfw .gt_font_bold { font-weight: bold; }
 #zfoyhoozfw .gt_font_italic { font-style: italic; }
 #zfoyhoozfw .gt_super { font-size: 65%; }
 #zfoyhoozfw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zfoyhoozfw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zfoyhoozfw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zfoyhoozfw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zfoyhoozfw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zfoyhoozfw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| country_name | year | population |
|--------------|------|------------|
| Benin        | 2018 | 11940683   |
| Benin        | 2019 | 12290444   |
| Benin        | 2020 | 12643123   |
| Benin        | 2021 | 12996895   |
| Benin        | 2022 | 13352864   |
