# GT.tab_stubhead()


Add label text to the stubhead.


Usage

``` python
GT.tab_stubhead(label)
```


Add a label to the stubhead of a table. The stubhead is the lone element that is positioned left of the column labels, and above the stub. If a stub does not exist, then there is no stubhead (so no change will be made when using this method in that case). We have the flexibility to use Markdown formatting for the stubhead label (through use of the <a href="../reference/md.html#great_tables.md" class="gdls-link"><code>md()</code></a> helper function). Furthermore, we can use HTML for the stubhead label so long as we also use the <a href="../reference/html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper function.


## Parameters


`label: str | Text | list[str | Text]`  
The text to be used as the stubhead label. We can optionally use the <a href="../reference/md.html#great_tables.md" class="gdls-link"><code>md()</code></a> and <a href="../reference/html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions to style the text as Markdown or to retain HTML elements in the text. With a hierarchical stub (where `rowname_col=` is a list of columns), a single label spans all of the stub columns; alternatively, a list of labels can be provided, one per stub column (outermost first).


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
#ipttxzdhjm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ipttxzdhjm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ipttxzdhjm p { margin: 0; padding: 0; }
 #ipttxzdhjm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ipttxzdhjm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ipttxzdhjm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ipttxzdhjm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ipttxzdhjm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ipttxzdhjm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ipttxzdhjm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ipttxzdhjm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ipttxzdhjm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ipttxzdhjm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ipttxzdhjm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ipttxzdhjm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ipttxzdhjm .gt_spanner_row { border-bottom-style: hidden; }
 #ipttxzdhjm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ipttxzdhjm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ipttxzdhjm .gt_from_md> :first-child { margin-top: 0; }
 #ipttxzdhjm .gt_from_md> :last-child { margin-bottom: 0; }
 #ipttxzdhjm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ipttxzdhjm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ipttxzdhjm .gt_indent_1 { text-indent: 5px; }
 #ipttxzdhjm .gt_indent_2 { text-indent: calc(5px * 2); }
 #ipttxzdhjm .gt_indent_3 { text-indent: calc(5px * 3); }
 #ipttxzdhjm .gt_indent_4 { text-indent: calc(5px * 4); }
 #ipttxzdhjm .gt_indent_5 { text-indent: calc(5px * 5); }
 #ipttxzdhjm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ipttxzdhjm .gt_row_group_first td { border-top-width: 2px; }
 #ipttxzdhjm .gt_row_group_first th { border-top-width: 2px; }
 #ipttxzdhjm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ipttxzdhjm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ipttxzdhjm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ipttxzdhjm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ipttxzdhjm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ipttxzdhjm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ipttxzdhjm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ipttxzdhjm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ipttxzdhjm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ipttxzdhjm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ipttxzdhjm .gt_left { text-align: left; }
 #ipttxzdhjm .gt_center { text-align: center; }
 #ipttxzdhjm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ipttxzdhjm .gt_font_normal { font-weight: normal; }
 #ipttxzdhjm .gt_font_bold { font-weight: bold; }
 #ipttxzdhjm .gt_font_italic { font-style: italic; }
 #ipttxzdhjm .gt_super { font-size: 65%; }
 #ipttxzdhjm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ipttxzdhjm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ipttxzdhjm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ipttxzdhjm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ipttxzdhjm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ipttxzdhjm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gkqrtvcudd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gkqrtvcudd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gkqrtvcudd p { margin: 0; padding: 0; }
 #gkqrtvcudd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gkqrtvcudd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gkqrtvcudd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gkqrtvcudd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gkqrtvcudd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gkqrtvcudd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gkqrtvcudd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gkqrtvcudd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gkqrtvcudd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gkqrtvcudd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gkqrtvcudd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gkqrtvcudd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gkqrtvcudd .gt_spanner_row { border-bottom-style: hidden; }
 #gkqrtvcudd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gkqrtvcudd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gkqrtvcudd .gt_from_md> :first-child { margin-top: 0; }
 #gkqrtvcudd .gt_from_md> :last-child { margin-bottom: 0; }
 #gkqrtvcudd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gkqrtvcudd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gkqrtvcudd .gt_indent_1 { text-indent: 5px; }
 #gkqrtvcudd .gt_indent_2 { text-indent: calc(5px * 2); }
 #gkqrtvcudd .gt_indent_3 { text-indent: calc(5px * 3); }
 #gkqrtvcudd .gt_indent_4 { text-indent: calc(5px * 4); }
 #gkqrtvcudd .gt_indent_5 { text-indent: calc(5px * 5); }
 #gkqrtvcudd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gkqrtvcudd .gt_row_group_first td { border-top-width: 2px; }
 #gkqrtvcudd .gt_row_group_first th { border-top-width: 2px; }
 #gkqrtvcudd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gkqrtvcudd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gkqrtvcudd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gkqrtvcudd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gkqrtvcudd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gkqrtvcudd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gkqrtvcudd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gkqrtvcudd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gkqrtvcudd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gkqrtvcudd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gkqrtvcudd .gt_left { text-align: left; }
 #gkqrtvcudd .gt_center { text-align: center; }
 #gkqrtvcudd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gkqrtvcudd .gt_font_normal { font-weight: normal; }
 #gkqrtvcudd .gt_font_bold { font-weight: bold; }
 #gkqrtvcudd .gt_font_italic { font-style: italic; }
 #gkqrtvcudd .gt_super { font-size: 65%; }
 #gkqrtvcudd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gkqrtvcudd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gkqrtvcudd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gkqrtvcudd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gkqrtvcudd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gkqrtvcudd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| *Car*        | year | hp    | trq   |
|--------------|------|-------|-------|
| GT           | 2017 | 647.0 | 550.0 |
| 458 Speciale | 2015 | 597.0 | 398.0 |
| 458 Spider   | 2015 | 562.0 | 398.0 |
| 458 Italia   | 2014 | 562.0 | 398.0 |
| 488 GTB      | 2016 | 661.0 | 561.0 |
