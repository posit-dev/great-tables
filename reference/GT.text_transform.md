# GT.text_transform()


Apply a custom text transformation to cells at specified locations.


Usage

``` python
GT.text_transform(
    locations,
    fn,
)
```


With the [text_transform()](GT.text_transform.md#great_tables.GT.text_transform) method we can target specific cells and apply a text transformation function to their already-formatted content. This is useful for modifying the rendered text of cells after all formatting (via `fmt_*()` methods) has been applied.


## Parameters


`locations: Loc | list[Loc]`  
The cell or set of cells to be associated with the text transformation. Supported locations include [loc.body()](loc.body.md#great_tables.loc.body), [loc.stub()](loc.stub.md#great_tables.loc.stub), [loc.row_groups()](loc.row_groups.md#great_tables.loc.row_groups), and [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels).

`fn: Callable[[str], str]`  
A function that takes a cell's text content as a string and returns the transformed string.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to demonstrate [text_transform()](GT.text_transform.md#great_tables.GT.text_transform). We'll format the `num` column and then apply a text transformation to wrap the values in parentheses.


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char"]].head(4))
    .fmt_number(columns="num", decimals=1)
    .text_transform(
        locations=loc.body(columns="num"),
        fn=lambda x: f"({x})",
    )
)
```


<style>
#ixhxhzndeq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ixhxhzndeq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ixhxhzndeq p { margin: 0; padding: 0; }
 #ixhxhzndeq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ixhxhzndeq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ixhxhzndeq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ixhxhzndeq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ixhxhzndeq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ixhxhzndeq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixhxhzndeq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ixhxhzndeq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ixhxhzndeq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ixhxhzndeq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ixhxhzndeq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ixhxhzndeq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ixhxhzndeq .gt_spanner_row { border-bottom-style: hidden; }
 #ixhxhzndeq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ixhxhzndeq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ixhxhzndeq .gt_from_md> :first-child { margin-top: 0; }
 #ixhxhzndeq .gt_from_md> :last-child { margin-bottom: 0; }
 #ixhxhzndeq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ixhxhzndeq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ixhxhzndeq .gt_indent_1 { text-indent: 5px; }
 #ixhxhzndeq .gt_indent_2 { text-indent: calc(5px * 2); }
 #ixhxhzndeq .gt_indent_3 { text-indent: calc(5px * 3); }
 #ixhxhzndeq .gt_indent_4 { text-indent: calc(5px * 4); }
 #ixhxhzndeq .gt_indent_5 { text-indent: calc(5px * 5); }
 #ixhxhzndeq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ixhxhzndeq .gt_row_group_first td { border-top-width: 2px; }
 #ixhxhzndeq .gt_row_group_first th { border-top-width: 2px; }
 #ixhxhzndeq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ixhxhzndeq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixhxhzndeq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ixhxhzndeq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ixhxhzndeq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ixhxhzndeq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ixhxhzndeq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ixhxhzndeq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ixhxhzndeq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixhxhzndeq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ixhxhzndeq .gt_left { text-align: left; }
 #ixhxhzndeq .gt_center { text-align: center; }
 #ixhxhzndeq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ixhxhzndeq .gt_font_normal { font-weight: normal; }
 #ixhxhzndeq .gt_font_bold { font-weight: bold; }
 #ixhxhzndeq .gt_font_italic { font-style: italic; }
 #ixhxhzndeq .gt_super { font-size: 65%; }
 #ixhxhzndeq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixhxhzndeq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ixhxhzndeq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ixhxhzndeq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ixhxhzndeq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ixhxhzndeq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num     | char    |
|---------|---------|
| (0.1)   | apricot |
| (2.2)   | banana  |
| (33.3)  | coconut |
| (444.4) | durian  |


Using [text_transform()](GT.text_transform.md#great_tables.GT.text_transform) we can also convert specific cells to uppercase. Here we target only the first two rows of the `char` column.


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char"]].head(4))
    .text_transform(
        locations=loc.body(columns="char", rows=[0, 1]),
        fn=lambda x: x.upper(),
    )
)
```


<style>
#tcagbegjih table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tcagbegjih thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tcagbegjih p { margin: 0; padding: 0; }
 #tcagbegjih .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tcagbegjih .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tcagbegjih .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tcagbegjih .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tcagbegjih .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tcagbegjih .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tcagbegjih .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tcagbegjih .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tcagbegjih .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tcagbegjih .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tcagbegjih .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tcagbegjih .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tcagbegjih .gt_spanner_row { border-bottom-style: hidden; }
 #tcagbegjih .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tcagbegjih .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tcagbegjih .gt_from_md> :first-child { margin-top: 0; }
 #tcagbegjih .gt_from_md> :last-child { margin-bottom: 0; }
 #tcagbegjih .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tcagbegjih .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tcagbegjih .gt_indent_1 { text-indent: 5px; }
 #tcagbegjih .gt_indent_2 { text-indent: calc(5px * 2); }
 #tcagbegjih .gt_indent_3 { text-indent: calc(5px * 3); }
 #tcagbegjih .gt_indent_4 { text-indent: calc(5px * 4); }
 #tcagbegjih .gt_indent_5 { text-indent: calc(5px * 5); }
 #tcagbegjih .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tcagbegjih .gt_row_group_first td { border-top-width: 2px; }
 #tcagbegjih .gt_row_group_first th { border-top-width: 2px; }
 #tcagbegjih .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tcagbegjih .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tcagbegjih .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tcagbegjih .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tcagbegjih .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tcagbegjih .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tcagbegjih .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tcagbegjih .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tcagbegjih .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tcagbegjih .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tcagbegjih .gt_left { text-align: left; }
 #tcagbegjih .gt_center { text-align: center; }
 #tcagbegjih .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tcagbegjih .gt_font_normal { font-weight: normal; }
 #tcagbegjih .gt_font_bold { font-weight: bold; }
 #tcagbegjih .gt_font_italic { font-style: italic; }
 #tcagbegjih .gt_super { font-size: 65%; }
 #tcagbegjih .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tcagbegjih .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tcagbegjih .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tcagbegjih .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tcagbegjih .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tcagbegjih .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    |
|--------|---------|
| 0.1111 | APRICOT |
| 2.222  | BANANA  |
| 33.33  | coconut |
| 444.4  | durian  |


Multiple locations can be targeted at once by passing a list. In this example, we add a prefix to all cells in both the `num` and `char` columns.


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char"]].head(4))
    .fmt_number(columns="num", decimals=2)
    .text_transform(
        locations=[loc.body(columns="num"), loc.body(columns="char")],
        fn=lambda x: f"~ {x}",
    )
)
```


<style>
#vbiujprggz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vbiujprggz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vbiujprggz p { margin: 0; padding: 0; }
 #vbiujprggz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vbiujprggz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vbiujprggz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vbiujprggz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vbiujprggz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vbiujprggz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vbiujprggz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vbiujprggz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vbiujprggz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vbiujprggz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vbiujprggz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vbiujprggz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vbiujprggz .gt_spanner_row { border-bottom-style: hidden; }
 #vbiujprggz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vbiujprggz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vbiujprggz .gt_from_md> :first-child { margin-top: 0; }
 #vbiujprggz .gt_from_md> :last-child { margin-bottom: 0; }
 #vbiujprggz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vbiujprggz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vbiujprggz .gt_indent_1 { text-indent: 5px; }
 #vbiujprggz .gt_indent_2 { text-indent: calc(5px * 2); }
 #vbiujprggz .gt_indent_3 { text-indent: calc(5px * 3); }
 #vbiujprggz .gt_indent_4 { text-indent: calc(5px * 4); }
 #vbiujprggz .gt_indent_5 { text-indent: calc(5px * 5); }
 #vbiujprggz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vbiujprggz .gt_row_group_first td { border-top-width: 2px; }
 #vbiujprggz .gt_row_group_first th { border-top-width: 2px; }
 #vbiujprggz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vbiujprggz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vbiujprggz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vbiujprggz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vbiujprggz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vbiujprggz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vbiujprggz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vbiujprggz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vbiujprggz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vbiujprggz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vbiujprggz .gt_left { text-align: left; }
 #vbiujprggz .gt_center { text-align: center; }
 #vbiujprggz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vbiujprggz .gt_font_normal { font-weight: normal; }
 #vbiujprggz .gt_font_bold { font-weight: bold; }
 #vbiujprggz .gt_font_italic { font-style: italic; }
 #vbiujprggz .gt_super { font-size: 65%; }
 #vbiujprggz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vbiujprggz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vbiujprggz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vbiujprggz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vbiujprggz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vbiujprggz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num      | char      |
|----------|-----------|
| ~ 0.11   | ~ apricot |
| ~ 2.22   | ~ banana  |
| ~ 33.33  | ~ coconut |
| ~ 444.40 | ~ durian  |
