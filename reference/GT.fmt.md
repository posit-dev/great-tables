# GT.fmt()


Set a column format with a formatter function.


Usage

``` python
GT.fmt(
    fns,
    columns=None,
    rows=None,
    is_substitution=False,
)
```


The [fmt()](GT.fmt.md#great_tables.GT.fmt) method provides a way to execute custom formatting functionality with raw data values in a way that can consider all output contexts.

Along with the `columns` and `rows` arguments that provide some precision in targeting data cells, the `fns` argument allows you to define a function for manipulating the raw data.


## Parameters


`fns: FormatFn`  
A formatting function to apply to the targeted cells.

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in `columns` being formatted. Alternatively, we can supply a list of row indices.

`is_substitution: bool = ``False`  
Whether the formatter is a substitution. Substitutions are run last, after other formatters.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a table. With the [fmt()](GT.fmt.md#great_tables.GT.fmt) method, we'll add a prefix `^` and a suffix `$` to the `row` and `group` columns.


``` python
from great_tables import GT, exibble

(
    GT(exibble)
    .fmt(lambda x: f"^{x}$", columns=["row", "group"])
)
```


<style>
#lmudizzecr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lmudizzecr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lmudizzecr p { margin: 0; padding: 0; }
 #lmudizzecr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lmudizzecr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lmudizzecr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lmudizzecr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lmudizzecr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lmudizzecr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lmudizzecr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lmudizzecr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lmudizzecr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lmudizzecr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lmudizzecr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lmudizzecr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lmudizzecr .gt_spanner_row { border-bottom-style: hidden; }
 #lmudizzecr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lmudizzecr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lmudizzecr .gt_from_md> :first-child { margin-top: 0; }
 #lmudizzecr .gt_from_md> :last-child { margin-bottom: 0; }
 #lmudizzecr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lmudizzecr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lmudizzecr .gt_indent_1 { text-indent: 5px; }
 #lmudizzecr .gt_indent_2 { text-indent: calc(5px * 2); }
 #lmudizzecr .gt_indent_3 { text-indent: calc(5px * 3); }
 #lmudizzecr .gt_indent_4 { text-indent: calc(5px * 4); }
 #lmudizzecr .gt_indent_5 { text-indent: calc(5px * 5); }
 #lmudizzecr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lmudizzecr .gt_row_group_first td { border-top-width: 2px; }
 #lmudizzecr .gt_row_group_first th { border-top-width: 2px; }
 #lmudizzecr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lmudizzecr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lmudizzecr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lmudizzecr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lmudizzecr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lmudizzecr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lmudizzecr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lmudizzecr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lmudizzecr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lmudizzecr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lmudizzecr .gt_left { text-align: left; }
 #lmudizzecr .gt_center { text-align: center; }
 #lmudizzecr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lmudizzecr .gt_font_normal { font-weight: normal; }
 #lmudizzecr .gt_font_bold { font-weight: bold; }
 #lmudizzecr .gt_font_italic { font-style: italic; }
 #lmudizzecr .gt_super { font-size: 65%; }
 #lmudizzecr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lmudizzecr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lmudizzecr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lmudizzecr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lmudizzecr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lmudizzecr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | ^row_1\$ | ^grp_a\$ |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | ^row_2\$ | ^grp_a\$ |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | ^row_3\$ | ^grp_a\$ |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | ^row_4\$ | ^grp_a\$ |
| 5550.0 |  | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | ^row_5\$ | ^grp_b\$ |
|  | fig | six | 2015-06-15 |  | 2018-06-06 16:11 | 13.255 | ^row_6\$ | ^grp_b\$ |
| 777000.0 | grapefruit | seven |  | 19:10 | 2018-07-07 05:22 |  | ^row_7\$ | ^grp_b\$ |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 |  | 0.44 | ^row_8\$ | ^grp_b\$ |
