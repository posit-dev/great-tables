# GT


Create a **Great Tables** object.


Usage

``` python
GT(
    data,
    rowname_col=None,
    groupname_col=None,
    auto_align=True,
    id=None,
    locale=None,
)
```


The [GT()](GT.md#great_tables.GT) class creates the [GT](GT.md#great_tables.GT) object when provided with tabular data. Using this class is the the first step in a typical **Great Tables** workflow. Once we have this object, we can take advantage of numerous methods to get the desired display table for publication.

There are a few table structuring options we can consider at this stage. We can choose to create a table stub containing row labels through the use of the `rowname_col=` argument. Further to this, row groups can be created with the `groupname_col=` argument. Both arguments take the name of a column in the input table data. Typically, the data in the `groupname_col=` column will consist of categorical text whereas the data in the `rowname_col=` column will often contain unique labels (perhaps being unique across the entire table or unique only within the different row groups).


## Parameters


`data: Any`  
A DataFrame object.

`rowname_col: str | list[str] | None = None`  
The column name in the input `data=` table to use as row labels to be placed in the table stub. A list of column names creates a hierarchical stub, where the last column holds the row labels and the columns before it are outer levels (outermost first); repeated values in the outer levels are merged across adjacent rows.

`groupname_col: str | None = None`  
The column name in the input `data=` table to use as group labels for generation of row groups.

`auto_align: bool = ``True`  
Optionally have column data be aligned depending on the content contained in each column of the input `data=`.

`id: str | None = None`  
By default (with `None`) the table ID will be a random, ten-letter string as generated through internal use of the `random_id()` function. A custom table ID can be used here by providing a string.

`locale: str | None = None`  
An optional locale identifier that can be set as the default locale for all functions that take a `locale` argument. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`GT`  
A GT object is returned.


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset for the next few examples, we'll learn how to make simple output tables with the [GT()](GT.md#great_tables.GT) class. The most basic thing to do is to just use [GT()](GT.md#great_tables.GT) with the dataset as the input.


``` python
from great_tables import GT, exibble

GT(exibble)
```


<style>
#jolzywconq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jolzywconq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jolzywconq p { margin: 0; padding: 0; }
 #jolzywconq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jolzywconq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jolzywconq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jolzywconq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jolzywconq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jolzywconq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jolzywconq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jolzywconq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jolzywconq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jolzywconq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jolzywconq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jolzywconq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jolzywconq .gt_spanner_row { border-bottom-style: hidden; }
 #jolzywconq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jolzywconq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jolzywconq .gt_from_md> :first-child { margin-top: 0; }
 #jolzywconq .gt_from_md> :last-child { margin-bottom: 0; }
 #jolzywconq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jolzywconq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jolzywconq .gt_indent_1 { text-indent: 5px; }
 #jolzywconq .gt_indent_2 { text-indent: calc(5px * 2); }
 #jolzywconq .gt_indent_3 { text-indent: calc(5px * 3); }
 #jolzywconq .gt_indent_4 { text-indent: calc(5px * 4); }
 #jolzywconq .gt_indent_5 { text-indent: calc(5px * 5); }
 #jolzywconq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jolzywconq .gt_row_group_first td { border-top-width: 2px; }
 #jolzywconq .gt_row_group_first th { border-top-width: 2px; }
 #jolzywconq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jolzywconq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jolzywconq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jolzywconq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jolzywconq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jolzywconq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jolzywconq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jolzywconq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jolzywconq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jolzywconq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jolzywconq .gt_left { text-align: left; }
 #jolzywconq .gt_center { text-align: center; }
 #jolzywconq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jolzywconq .gt_font_normal { font-weight: normal; }
 #jolzywconq .gt_font_bold { font-weight: bold; }
 #jolzywconq .gt_font_italic { font-style: italic; }
 #jolzywconq .gt_super { font-size: 65%; }
 #jolzywconq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jolzywconq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jolzywconq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jolzywconq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jolzywconq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jolzywconq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


This dataset has the `row` and `group` columns. The former contains unique values that are ideal for labeling rows, and this often happens in what is called the 'stub' (a reserved area that serves to label rows). With the [GT()](GT.md#great_tables.GT) class, we can immediately place the contents of the `row` column into the stub column. To do this, we use the `rowname_col=` argument with the appropriate column name.


``` python
from great_tables import GT, exibble

GT(exibble, rowname_col="row")
```


<style>
#yrzxntkphh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yrzxntkphh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yrzxntkphh p { margin: 0; padding: 0; }
 #yrzxntkphh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yrzxntkphh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yrzxntkphh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yrzxntkphh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yrzxntkphh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yrzxntkphh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yrzxntkphh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yrzxntkphh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yrzxntkphh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yrzxntkphh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yrzxntkphh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yrzxntkphh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yrzxntkphh .gt_spanner_row { border-bottom-style: hidden; }
 #yrzxntkphh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yrzxntkphh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yrzxntkphh .gt_from_md> :first-child { margin-top: 0; }
 #yrzxntkphh .gt_from_md> :last-child { margin-bottom: 0; }
 #yrzxntkphh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yrzxntkphh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yrzxntkphh .gt_indent_1 { text-indent: 5px; }
 #yrzxntkphh .gt_indent_2 { text-indent: calc(5px * 2); }
 #yrzxntkphh .gt_indent_3 { text-indent: calc(5px * 3); }
 #yrzxntkphh .gt_indent_4 { text-indent: calc(5px * 4); }
 #yrzxntkphh .gt_indent_5 { text-indent: calc(5px * 5); }
 #yrzxntkphh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yrzxntkphh .gt_row_group_first td { border-top-width: 2px; }
 #yrzxntkphh .gt_row_group_first th { border-top-width: 2px; }
 #yrzxntkphh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yrzxntkphh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yrzxntkphh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yrzxntkphh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yrzxntkphh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yrzxntkphh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yrzxntkphh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yrzxntkphh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yrzxntkphh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yrzxntkphh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yrzxntkphh .gt_left { text-align: left; }
 #yrzxntkphh .gt_center { text-align: center; }
 #yrzxntkphh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yrzxntkphh .gt_font_normal { font-weight: normal; }
 #yrzxntkphh .gt_font_bold { font-weight: bold; }
 #yrzxntkphh .gt_font_italic { font-style: italic; }
 #yrzxntkphh .gt_super { font-size: 65%; }
 #yrzxntkphh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yrzxntkphh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yrzxntkphh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yrzxntkphh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yrzxntkphh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yrzxntkphh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | num | char | fctr | date | time | datetime | currency | group |
|----|----|----|----|----|----|----|----|----|
| row_1 | 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | grp_a |
| row_2 | 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | grp_a |
| row_3 | 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | grp_a |
| row_4 | 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | grp_a |
| row_5 | 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | grp_b |
| row_6 | None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | grp_b |
| row_7 | 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | grp_b |
| row_8 | 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | grp_b |


This sets up a table with a stub, the row labels are placed within the stub column, and a vertical dividing line has been placed on the right-hand side.

The `group` column contains categorical values that are ideal for grouping rows. We can use the `groupname_col=` argument to place these values into row groups.


``` python
from great_tables import GT, exibble

GT(exibble, rowname_col="row", groupname_col="group")
```


<style>
#tamijtcpoo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tamijtcpoo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tamijtcpoo p { margin: 0; padding: 0; }
 #tamijtcpoo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tamijtcpoo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tamijtcpoo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tamijtcpoo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tamijtcpoo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tamijtcpoo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tamijtcpoo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tamijtcpoo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tamijtcpoo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tamijtcpoo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tamijtcpoo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tamijtcpoo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tamijtcpoo .gt_spanner_row { border-bottom-style: hidden; }
 #tamijtcpoo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tamijtcpoo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tamijtcpoo .gt_from_md> :first-child { margin-top: 0; }
 #tamijtcpoo .gt_from_md> :last-child { margin-bottom: 0; }
 #tamijtcpoo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tamijtcpoo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tamijtcpoo .gt_indent_1 { text-indent: 5px; }
 #tamijtcpoo .gt_indent_2 { text-indent: calc(5px * 2); }
 #tamijtcpoo .gt_indent_3 { text-indent: calc(5px * 3); }
 #tamijtcpoo .gt_indent_4 { text-indent: calc(5px * 4); }
 #tamijtcpoo .gt_indent_5 { text-indent: calc(5px * 5); }
 #tamijtcpoo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tamijtcpoo .gt_row_group_first td { border-top-width: 2px; }
 #tamijtcpoo .gt_row_group_first th { border-top-width: 2px; }
 #tamijtcpoo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tamijtcpoo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tamijtcpoo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tamijtcpoo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tamijtcpoo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tamijtcpoo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tamijtcpoo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tamijtcpoo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tamijtcpoo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tamijtcpoo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tamijtcpoo .gt_left { text-align: left; }
 #tamijtcpoo .gt_center { text-align: center; }
 #tamijtcpoo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tamijtcpoo .gt_font_normal { font-weight: normal; }
 #tamijtcpoo .gt_font_bold { font-weight: bold; }
 #tamijtcpoo .gt_font_italic { font-style: italic; }
 #tamijtcpoo .gt_super { font-size: 65%; }
 #tamijtcpoo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tamijtcpoo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tamijtcpoo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tamijtcpoo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tamijtcpoo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tamijtcpoo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_left">six</td>
<td class="gt_row gt_right">2015-06-15</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">2018-06-06 16:11</td>
<td class="gt_row gt_right">13.255</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_left">seven</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">19:10</td>
<td class="gt_row gt_right">2018-07-07 05:22</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_left">eight</td>
<td class="gt_row gt_right">2015-08-15</td>
<td class="gt_row gt_right">20:20</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">0.44</td>
</tr>
</tbody>
</table>


By default, values in the body of a table (and their column labels) are automatically aligned. The alignment is governed by the types of values in a column. If you'd like to disable this form of auto-alignment, the `auto_align=False` option can be taken.


``` python
from great_tables import GT, exibble

GT(exibble, rowname_col="row", auto_align=False)
```


<style>
#ridkrllksk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ridkrllksk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ridkrllksk p { margin: 0; padding: 0; }
 #ridkrllksk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ridkrllksk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ridkrllksk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ridkrllksk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ridkrllksk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ridkrllksk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ridkrllksk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ridkrllksk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ridkrllksk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ridkrllksk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ridkrllksk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ridkrllksk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ridkrllksk .gt_spanner_row { border-bottom-style: hidden; }
 #ridkrllksk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ridkrllksk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ridkrllksk .gt_from_md> :first-child { margin-top: 0; }
 #ridkrllksk .gt_from_md> :last-child { margin-bottom: 0; }
 #ridkrllksk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ridkrllksk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ridkrllksk .gt_indent_1 { text-indent: 5px; }
 #ridkrllksk .gt_indent_2 { text-indent: calc(5px * 2); }
 #ridkrllksk .gt_indent_3 { text-indent: calc(5px * 3); }
 #ridkrllksk .gt_indent_4 { text-indent: calc(5px * 4); }
 #ridkrllksk .gt_indent_5 { text-indent: calc(5px * 5); }
 #ridkrllksk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ridkrllksk .gt_row_group_first td { border-top-width: 2px; }
 #ridkrllksk .gt_row_group_first th { border-top-width: 2px; }
 #ridkrllksk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ridkrllksk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ridkrllksk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ridkrllksk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ridkrllksk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ridkrllksk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ridkrllksk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ridkrllksk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ridkrllksk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ridkrllksk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ridkrllksk .gt_left { text-align: left; }
 #ridkrllksk .gt_center { text-align: center; }
 #ridkrllksk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ridkrllksk .gt_font_normal { font-weight: normal; }
 #ridkrllksk .gt_font_bold { font-weight: bold; }
 #ridkrllksk .gt_font_italic { font-style: italic; }
 #ridkrllksk .gt_super { font-size: 65%; }
 #ridkrllksk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ridkrllksk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ridkrllksk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ridkrllksk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ridkrllksk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ridkrllksk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | num | char | fctr | date | time | datetime | currency | group |
|----|----|----|----|----|----|----|----|----|
| row_1 | 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | grp_a |
| row_2 | 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | grp_a |
| row_3 | 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | grp_a |
| row_4 | 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | grp_a |
| row_5 | 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | grp_b |
| row_6 | None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | grp_b |
| row_7 | 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | grp_b |
| row_8 | 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | grp_b |


What you'll get from that is center-alignment of all table body values and all column labels. Note that row labels in the the stub are still left-aligned; and `auto_align=` has no effect on alignment within the table stub.

However which way you generate the initial table object, you can modify it with a huge variety of methods to further customize the presentation. Formatting body cells is commonly done with the family of formatting methods (e.g., `fmt_number()`, `fmt_date()`, etc.). The package supports formatting with internationalization ('i18n' features) and so locale-aware methods all come with a `locale=` argument. To avoid having to use that argument repeatedly, the [GT()](GT.md#great_tables.GT) class has its own `locale=` argument. Setting a locale in that will make it available globally. Here's an example of how that works in practice when setting `locale = "fr"` in [GT()](GT.md#great_tables.GT) prior to using formatting methods:


``` python
from great_tables import GT, exibble

(
    GT(exibble, rowname_col="row", locale="fr")
    .fmt_currency(columns="currency")
    .fmt_scientific(columns="num")
    .fmt_date(columns="date", date_style="day_month_year")
)
```


<style>
#ebmgyqdnfi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ebmgyqdnfi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ebmgyqdnfi p { margin: 0; padding: 0; }
 #ebmgyqdnfi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ebmgyqdnfi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ebmgyqdnfi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ebmgyqdnfi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ebmgyqdnfi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ebmgyqdnfi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ebmgyqdnfi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ebmgyqdnfi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ebmgyqdnfi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ebmgyqdnfi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ebmgyqdnfi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ebmgyqdnfi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ebmgyqdnfi .gt_spanner_row { border-bottom-style: hidden; }
 #ebmgyqdnfi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ebmgyqdnfi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ebmgyqdnfi .gt_from_md> :first-child { margin-top: 0; }
 #ebmgyqdnfi .gt_from_md> :last-child { margin-bottom: 0; }
 #ebmgyqdnfi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ebmgyqdnfi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ebmgyqdnfi .gt_indent_1 { text-indent: 5px; }
 #ebmgyqdnfi .gt_indent_2 { text-indent: calc(5px * 2); }
 #ebmgyqdnfi .gt_indent_3 { text-indent: calc(5px * 3); }
 #ebmgyqdnfi .gt_indent_4 { text-indent: calc(5px * 4); }
 #ebmgyqdnfi .gt_indent_5 { text-indent: calc(5px * 5); }
 #ebmgyqdnfi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ebmgyqdnfi .gt_row_group_first td { border-top-width: 2px; }
 #ebmgyqdnfi .gt_row_group_first th { border-top-width: 2px; }
 #ebmgyqdnfi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ebmgyqdnfi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ebmgyqdnfi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ebmgyqdnfi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ebmgyqdnfi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ebmgyqdnfi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ebmgyqdnfi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ebmgyqdnfi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ebmgyqdnfi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ebmgyqdnfi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ebmgyqdnfi .gt_left { text-align: left; }
 #ebmgyqdnfi .gt_center { text-align: center; }
 #ebmgyqdnfi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ebmgyqdnfi .gt_font_normal { font-weight: normal; }
 #ebmgyqdnfi .gt_font_bold { font-weight: bold; }
 #ebmgyqdnfi .gt_font_italic { font-style: italic; }
 #ebmgyqdnfi .gt_super { font-size: 65%; }
 #ebmgyqdnfi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ebmgyqdnfi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ebmgyqdnfi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ebmgyqdnfi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ebmgyqdnfi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ebmgyqdnfi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | num | char | fctr | date | time | datetime | currency | group |
|----|----|----|----|----|----|----|----|----|
| row_1 | 1,11 × 10<sup>−1</sup> | apricot | one | 15 janvier 2015 | 13:35 | 2018-01-01 02:22 | €49,95 | grp_a |
| row_2 | 2,22 | banana | two | 15 février 2015 | 14:40 | 2018-02-02 14:33 | €17,95 | grp_a |
| row_3 | 3,33 × 10<sup>1</sup> | coconut | three | 15 mars 2015 | 15:45 | 2018-03-03 03:44 | €1,39 | grp_a |
| row_4 | 4,44 × 10<sup>2</sup> | durian | four | 15 avril 2015 | 16:50 | 2018-04-04 15:55 | €65 100,00 | grp_a |
| row_5 | 5,55 × 10<sup>3</sup> | None | five | 15 mai 2015 | 17:55 | 2018-05-05 04:00 | €1 325,81 | grp_b |
| row_6 | None | fig | six | 15 juin 2015 | None | 2018-06-06 16:11 | €13,26 | grp_b |
| row_7 | 7,77 × 10<sup>5</sup> | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | grp_b |
| row_8 | 8,88 × 10<sup>6</sup> | honeydew | eight | 15 août 2015 | 20:20 | None | €0,44 | grp_b |


In this example, the `fmt_currency()`, `fmt_scientific()`, and `fmt_date()` methods understand that the locale for this table is `"fr"` (French), so the appropriate formatting for that locale is apparent in the `currency`, `num`, and `date` columns.
