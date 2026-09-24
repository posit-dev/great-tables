# GT.text_replace()


Perform targeted text replacement with a regex pattern.


Usage

``` python
GT.text_replace(
    pattern,
    replacement,
    locations=None,
)
```


With [text_replace()](GT.text_replace.md#great_tables.GT.text_replace) we can target cells in specific locations and replace text fragments matching a regular expression pattern. This operates on the already-formatted cell content (i.e., after `fmt_*()` methods have been applied).


## Parameters


`pattern: str`  
A regex pattern used to target text fragments in the resolved cells.

`replacement: str`  
The replacement text for any matched text fragments. Backreferences (e.g., `"\\1"`) can be used to refer to capture groups in the pattern.

`locations: Loc | list[Loc] | None = None`  
The cell or set of cells to be associated with the text replacement. Supported locations include [loc.body()](loc.body.md#great_tables.loc.body), [loc.stub()](loc.stub.md#great_tables.loc.stub), [loc.row_groups()](loc.row_groups.md#great_tables.loc.row_groups), and [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels). If `None`, defaults to [loc.body()](loc.body.md#great_tables.loc.body).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Use [text_replace()](GT.text_replace.md#great_tables.GT.text_replace) to add HTML emphasis tags around text in parentheses.


``` python
import pandas as pd
from great_tables import GT, loc

df = pd.DataFrame({"item": ["Column A (details)", "Colum B (info)"], "value": [1, 2]})

(
    GT(df)
    .text_replace(
        pattern=r"\((.+?)\)",
        replacement=r"(<em>\1</em>)",
        locations=loc.body(columns="item"),
    )
)
```


<style>
#zxjejwqzdt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zxjejwqzdt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zxjejwqzdt p { margin: 0; padding: 0; }
 #zxjejwqzdt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zxjejwqzdt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zxjejwqzdt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zxjejwqzdt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zxjejwqzdt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxjejwqzdt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxjejwqzdt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxjejwqzdt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zxjejwqzdt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zxjejwqzdt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zxjejwqzdt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zxjejwqzdt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zxjejwqzdt .gt_spanner_row { border-bottom-style: hidden; }
 #zxjejwqzdt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zxjejwqzdt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zxjejwqzdt .gt_from_md> :first-child { margin-top: 0; }
 #zxjejwqzdt .gt_from_md> :last-child { margin-bottom: 0; }
 #zxjejwqzdt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zxjejwqzdt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zxjejwqzdt .gt_indent_1 { text-indent: 5px; }
 #zxjejwqzdt .gt_indent_2 { text-indent: calc(5px * 2); }
 #zxjejwqzdt .gt_indent_3 { text-indent: calc(5px * 3); }
 #zxjejwqzdt .gt_indent_4 { text-indent: calc(5px * 4); }
 #zxjejwqzdt .gt_indent_5 { text-indent: calc(5px * 5); }
 #zxjejwqzdt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zxjejwqzdt .gt_row_group_first td { border-top-width: 2px; }
 #zxjejwqzdt .gt_row_group_first th { border-top-width: 2px; }
 #zxjejwqzdt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zxjejwqzdt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxjejwqzdt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxjejwqzdt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zxjejwqzdt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxjejwqzdt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxjejwqzdt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zxjejwqzdt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zxjejwqzdt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxjejwqzdt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zxjejwqzdt .gt_left { text-align: left; }
 #zxjejwqzdt .gt_center { text-align: center; }
 #zxjejwqzdt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zxjejwqzdt .gt_font_normal { font-weight: normal; }
 #zxjejwqzdt .gt_font_bold { font-weight: bold; }
 #zxjejwqzdt .gt_font_italic { font-style: italic; }
 #zxjejwqzdt .gt_super { font-size: 65%; }
 #zxjejwqzdt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxjejwqzdt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zxjejwqzdt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxjejwqzdt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zxjejwqzdt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zxjejwqzdt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| item                 | value |
|----------------------|-------|
| Column A (*details*) | 1     |
| Colum B (*info*)     | 2     |


Replace underscores with spaces in the stub (row labels).


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char", "row"]].head(4), rowname_col="row")
    .text_replace(pattern="_", replacement=" ", locations=loc.stub())
)
```


<style>
#gqmagsmjok table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gqmagsmjok thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gqmagsmjok p { margin: 0; padding: 0; }
 #gqmagsmjok .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gqmagsmjok .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gqmagsmjok .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gqmagsmjok .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gqmagsmjok .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gqmagsmjok .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gqmagsmjok .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gqmagsmjok .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gqmagsmjok .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gqmagsmjok .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gqmagsmjok .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gqmagsmjok .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gqmagsmjok .gt_spanner_row { border-bottom-style: hidden; }
 #gqmagsmjok .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gqmagsmjok .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gqmagsmjok .gt_from_md> :first-child { margin-top: 0; }
 #gqmagsmjok .gt_from_md> :last-child { margin-bottom: 0; }
 #gqmagsmjok .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gqmagsmjok .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gqmagsmjok .gt_indent_1 { text-indent: 5px; }
 #gqmagsmjok .gt_indent_2 { text-indent: calc(5px * 2); }
 #gqmagsmjok .gt_indent_3 { text-indent: calc(5px * 3); }
 #gqmagsmjok .gt_indent_4 { text-indent: calc(5px * 4); }
 #gqmagsmjok .gt_indent_5 { text-indent: calc(5px * 5); }
 #gqmagsmjok .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gqmagsmjok .gt_row_group_first td { border-top-width: 2px; }
 #gqmagsmjok .gt_row_group_first th { border-top-width: 2px; }
 #gqmagsmjok .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gqmagsmjok .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gqmagsmjok .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gqmagsmjok .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gqmagsmjok .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gqmagsmjok .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gqmagsmjok .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gqmagsmjok .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gqmagsmjok .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gqmagsmjok .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gqmagsmjok .gt_left { text-align: left; }
 #gqmagsmjok .gt_center { text-align: center; }
 #gqmagsmjok .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gqmagsmjok .gt_font_normal { font-weight: normal; }
 #gqmagsmjok .gt_font_bold { font-weight: bold; }
 #gqmagsmjok .gt_font_italic { font-style: italic; }
 #gqmagsmjok .gt_super { font-size: 65%; }
 #gqmagsmjok .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gqmagsmjok .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gqmagsmjok .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gqmagsmjok .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gqmagsmjok .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gqmagsmjok .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|       | num    | char    |
|-------|--------|---------|
| row 1 | 0.1111 | apricot |
| row 2 | 2.222  | banana  |
| row 3 | 33.33  | coconut |
| row 4 | 444.4  | durian  |
