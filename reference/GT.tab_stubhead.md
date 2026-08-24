# GT.tab_stubhead()


Add label text to the stubhead.


Usage

``` python
GT.tab_stubhead(label)
```


Add a label to the stubhead of a table. The stubhead is the lone element that is positioned left of the column labels, and above the stub. If a stub does not exist, then there is no stubhead (so no change will be made when using this method in that case). We have the flexibility to use Markdown formatting for the stubhead label (through use of the <a href="md.html#great_tables.md" class="gdls-link"><code>md()</code></a> helper function). Furthermore, we can use HTML for the stubhead label so long as we also use the <a href="html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper function.


## Parameters


`label: str | Text`  
The text to be used as the stubhead label. We can optionally use the <a href="md.html#great_tables.md" class="gdls-link"><code>md()</code></a> and <a href="html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions to style the text as Markdown or to retain HTML elements in the text.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a small subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, we can create a table with row labels. Since we have row labels in the stub (via use of `rowname_col="model"` in the [GT()](GT.md#great_tables.GT) call) we have a stubhead, so, let's add a stubhead label (`"car"`) with the [tab_stubhead()](GT.tab_stubhead.md#great_tables.GT.tab_stubhead) method to describe what's in the stub.


``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["model", "year", "hp", "trq"]].head(5)

(
    GT(gtcars_mini, rowname_col="model")
    .tab_stubhead(label="car")
)
```


<style>
#lvoqvccfpv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lvoqvccfpv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lvoqvccfpv p { margin: 0; padding: 0; }
 #lvoqvccfpv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lvoqvccfpv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lvoqvccfpv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lvoqvccfpv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lvoqvccfpv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lvoqvccfpv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lvoqvccfpv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lvoqvccfpv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lvoqvccfpv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lvoqvccfpv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lvoqvccfpv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lvoqvccfpv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lvoqvccfpv .gt_spanner_row { border-bottom-style: hidden; }
 #lvoqvccfpv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lvoqvccfpv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lvoqvccfpv .gt_from_md> :first-child { margin-top: 0; }
 #lvoqvccfpv .gt_from_md> :last-child { margin-bottom: 0; }
 #lvoqvccfpv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lvoqvccfpv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lvoqvccfpv .gt_indent_1 { text-indent: 5px; }
 #lvoqvccfpv .gt_indent_2 { text-indent: calc(5px * 2); }
 #lvoqvccfpv .gt_indent_3 { text-indent: calc(5px * 3); }
 #lvoqvccfpv .gt_indent_4 { text-indent: calc(5px * 4); }
 #lvoqvccfpv .gt_indent_5 { text-indent: calc(5px * 5); }
 #lvoqvccfpv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lvoqvccfpv .gt_row_group_first td { border-top-width: 2px; }
 #lvoqvccfpv .gt_row_group_first th { border-top-width: 2px; }
 #lvoqvccfpv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lvoqvccfpv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lvoqvccfpv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lvoqvccfpv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lvoqvccfpv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lvoqvccfpv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lvoqvccfpv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lvoqvccfpv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lvoqvccfpv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lvoqvccfpv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lvoqvccfpv .gt_left { text-align: left; }
 #lvoqvccfpv .gt_center { text-align: center; }
 #lvoqvccfpv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lvoqvccfpv .gt_font_normal { font-weight: normal; }
 #lvoqvccfpv .gt_font_bold { font-weight: bold; }
 #lvoqvccfpv .gt_font_italic { font-style: italic; }
 #lvoqvccfpv .gt_super { font-size: 65%; }
 #lvoqvccfpv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lvoqvccfpv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lvoqvccfpv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lvoqvccfpv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lvoqvccfpv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lvoqvccfpv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| car          | year | hp    | trq   |
|--------------|------|-------|-------|
| GT           | 2017 | 647.0 | 550.0 |
| 458 Speciale | 2015 | 597.0 | 398.0 |
| 458 Spider   | 2015 | 562.0 | 398.0 |
| 458 Italia   | 2014 | 562.0 | 398.0 |
| 488 GTB      | 2016 | 661.0 | 561.0 |


We can also use Markdown formatting for the stubhead label. In this example, we'll use `md("*Car*")` to make the label italicized.


``` python
from great_tables import GT, md
from great_tables.data import gtcars

(
    GT(gtcars_mini, rowname_col="model")
    .tab_stubhead(label=md("*Car*"))
)
```


<style>
#kkafbaznuq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kkafbaznuq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kkafbaznuq p { margin: 0; padding: 0; }
 #kkafbaznuq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kkafbaznuq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kkafbaznuq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kkafbaznuq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kkafbaznuq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkafbaznuq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkafbaznuq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkafbaznuq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kkafbaznuq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kkafbaznuq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kkafbaznuq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kkafbaznuq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kkafbaznuq .gt_spanner_row { border-bottom-style: hidden; }
 #kkafbaznuq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kkafbaznuq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kkafbaznuq .gt_from_md> :first-child { margin-top: 0; }
 #kkafbaznuq .gt_from_md> :last-child { margin-bottom: 0; }
 #kkafbaznuq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kkafbaznuq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kkafbaznuq .gt_indent_1 { text-indent: 5px; }
 #kkafbaznuq .gt_indent_2 { text-indent: calc(5px * 2); }
 #kkafbaznuq .gt_indent_3 { text-indent: calc(5px * 3); }
 #kkafbaznuq .gt_indent_4 { text-indent: calc(5px * 4); }
 #kkafbaznuq .gt_indent_5 { text-indent: calc(5px * 5); }
 #kkafbaznuq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kkafbaznuq .gt_row_group_first td { border-top-width: 2px; }
 #kkafbaznuq .gt_row_group_first th { border-top-width: 2px; }
 #kkafbaznuq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kkafbaznuq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkafbaznuq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkafbaznuq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kkafbaznuq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkafbaznuq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkafbaznuq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kkafbaznuq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kkafbaznuq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkafbaznuq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkafbaznuq .gt_left { text-align: left; }
 #kkafbaznuq .gt_center { text-align: center; }
 #kkafbaznuq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kkafbaznuq .gt_font_normal { font-weight: normal; }
 #kkafbaznuq .gt_font_bold { font-weight: bold; }
 #kkafbaznuq .gt_font_italic { font-style: italic; }
 #kkafbaznuq .gt_super { font-size: 65%; }
 #kkafbaznuq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkafbaznuq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kkafbaznuq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkafbaznuq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkafbaznuq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kkafbaznuq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| *Car*        | year | hp    | trq   |
|--------------|------|-------|-------|
| GT           | 2017 | 647.0 | 550.0 |
| 458 Speciale | 2015 | 597.0 | 398.0 |
| 458 Spider   | 2015 | 562.0 | 398.0 |
| 458 Italia   | 2014 | 562.0 | 398.0 |
| 488 GTB      | 2016 | 661.0 | 561.0 |
