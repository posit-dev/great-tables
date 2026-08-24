# GT.rm_stubhead()


Remove the stubhead label.


Usage

``` python
GT.rm_stubhead()
```


We can remove the stubhead label (i.e., the label positioned above the table stub) with the [rm_stubhead()](GT.rm_stubhead.md#great_tables.GT.rm_stubhead) method. This is useful when a stubhead label is present but no longer wanted.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, we create a table with a stub and a stubhead label. The label is then removed with the [rm_stubhead()](GT.rm_stubhead.md#great_tables.GT.rm_stubhead) method.


``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["model", "mfr", "msrp"]].head(5)

(
    GT(gtcars_mini, rowname_col="model")
    .tab_stubhead(label="car")
    .rm_stubhead()
)
```


<style>
#kpepofuyvq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kpepofuyvq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kpepofuyvq p { margin: 0; padding: 0; }
 #kpepofuyvq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kpepofuyvq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kpepofuyvq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kpepofuyvq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kpepofuyvq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kpepofuyvq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kpepofuyvq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kpepofuyvq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kpepofuyvq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kpepofuyvq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kpepofuyvq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kpepofuyvq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kpepofuyvq .gt_spanner_row { border-bottom-style: hidden; }
 #kpepofuyvq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kpepofuyvq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kpepofuyvq .gt_from_md> :first-child { margin-top: 0; }
 #kpepofuyvq .gt_from_md> :last-child { margin-bottom: 0; }
 #kpepofuyvq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kpepofuyvq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kpepofuyvq .gt_indent_1 { text-indent: 5px; }
 #kpepofuyvq .gt_indent_2 { text-indent: calc(5px * 2); }
 #kpepofuyvq .gt_indent_3 { text-indent: calc(5px * 3); }
 #kpepofuyvq .gt_indent_4 { text-indent: calc(5px * 4); }
 #kpepofuyvq .gt_indent_5 { text-indent: calc(5px * 5); }
 #kpepofuyvq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kpepofuyvq .gt_row_group_first td { border-top-width: 2px; }
 #kpepofuyvq .gt_row_group_first th { border-top-width: 2px; }
 #kpepofuyvq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kpepofuyvq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kpepofuyvq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kpepofuyvq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kpepofuyvq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kpepofuyvq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kpepofuyvq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kpepofuyvq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kpepofuyvq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kpepofuyvq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kpepofuyvq .gt_left { text-align: left; }
 #kpepofuyvq .gt_center { text-align: center; }
 #kpepofuyvq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kpepofuyvq .gt_font_normal { font-weight: normal; }
 #kpepofuyvq .gt_font_bold { font-weight: bold; }
 #kpepofuyvq .gt_font_italic { font-style: italic; }
 #kpepofuyvq .gt_super { font-size: 65%; }
 #kpepofuyvq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kpepofuyvq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kpepofuyvq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kpepofuyvq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kpepofuyvq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kpepofuyvq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|              | mfr     | msrp     |
|--------------|---------|----------|
| GT           | Ford    | 447000.0 |
| 458 Speciale | Ferrari | 291744.0 |
| 458 Spider   | Ferrari | 263553.0 |
| 458 Italia   | Ferrari | 233509.0 |
| 488 GTB      | Ferrari | 245400.0 |


## See Also

<a href="GT.tab_stubhead.html#great_tables.GT.tab_stubhead" class="gdls-link"><code>tab_stubhead()</code></a> to add a stubhead label to a table.
