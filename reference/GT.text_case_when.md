# GT.text_case_when()


Perform text replacements using a case-when approach.


Usage

``` python
GT.text_case_when(
    *cases,
    default=None,
    locations=None,
)
```


With [text_case_when()](GT.text_case_when.md#great_tables.GT.text_case_when) we supply a sequence of cases as `(predicate, replacement)` tuples. Each predicate is a function that takes the cell text (as a string) and returns `True` or `False`. The first predicate that returns `True` determines the replacement text. This is analogous to a series of if/elif statements applied to each cell.


## Parameters


`*cases: tuple[Callable[[str], bool], str]`  
One or more tuples of the form `(predicate_fn, new_text)` where `predicate_fn` is a callable that accepts a string and returns a boolean, and `new_text` is the replacement string to use when the predicate is `True`.

`default: str | None = None`  
The replacement text to use when no predicate matches. If `None` (the default), unmatched cells are left unchanged.

`locations: Loc | list[Loc] | None = None`  
The cell or set of cells to be associated with the text replacement. Supported locations include [loc.body()](loc.body.md#great_tables.loc.body), [loc.stub()](loc.stub.md#great_tables.loc.stub), [loc.row_groups()](loc.row_groups.md#great_tables.loc.row_groups), and [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels). If `None`, defaults to [loc.body()](loc.body.md#great_tables.loc.body).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Conditionally replace cell values based on their content.


``` python
import pandas as pd
from great_tables import GT, loc

df = pd.DataFrame({"score": [95, 72, 88, 61, 100]})

(
    GT(df)
    .fmt_number(columns="score", decimals=0)
    .text_case_when(
        (lambda x: int(x) >= 90, "A"),
        (lambda x: int(x) >= 80, "B"),
        (lambda x: int(x) >= 70, "C"),
        default="F",
        locations=loc.body(columns="score"),
    )
)
```


<style>
#lfdkzgggfq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lfdkzgggfq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lfdkzgggfq p { margin: 0; padding: 0; }
 #lfdkzgggfq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lfdkzgggfq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lfdkzgggfq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lfdkzgggfq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lfdkzgggfq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lfdkzgggfq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lfdkzgggfq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lfdkzgggfq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lfdkzgggfq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lfdkzgggfq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lfdkzgggfq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lfdkzgggfq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lfdkzgggfq .gt_spanner_row { border-bottom-style: hidden; }
 #lfdkzgggfq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lfdkzgggfq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lfdkzgggfq .gt_from_md> :first-child { margin-top: 0; }
 #lfdkzgggfq .gt_from_md> :last-child { margin-bottom: 0; }
 #lfdkzgggfq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lfdkzgggfq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lfdkzgggfq .gt_indent_1 { text-indent: 5px; }
 #lfdkzgggfq .gt_indent_2 { text-indent: calc(5px * 2); }
 #lfdkzgggfq .gt_indent_3 { text-indent: calc(5px * 3); }
 #lfdkzgggfq .gt_indent_4 { text-indent: calc(5px * 4); }
 #lfdkzgggfq .gt_indent_5 { text-indent: calc(5px * 5); }
 #lfdkzgggfq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lfdkzgggfq .gt_row_group_first td { border-top-width: 2px; }
 #lfdkzgggfq .gt_row_group_first th { border-top-width: 2px; }
 #lfdkzgggfq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lfdkzgggfq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lfdkzgggfq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lfdkzgggfq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lfdkzgggfq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lfdkzgggfq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lfdkzgggfq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lfdkzgggfq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lfdkzgggfq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lfdkzgggfq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lfdkzgggfq .gt_left { text-align: left; }
 #lfdkzgggfq .gt_center { text-align: center; }
 #lfdkzgggfq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lfdkzgggfq .gt_font_normal { font-weight: normal; }
 #lfdkzgggfq .gt_font_bold { font-weight: bold; }
 #lfdkzgggfq .gt_font_italic { font-style: italic; }
 #lfdkzgggfq .gt_super { font-size: 65%; }
 #lfdkzgggfq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lfdkzgggfq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lfdkzgggfq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lfdkzgggfq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lfdkzgggfq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lfdkzgggfq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| score |
|-------|
| A     |
| C     |
| B     |
| F     |
| A     |


Use string methods in predicates to match patterns.


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char"]].head(4))
    .text_case_when(
        (lambda x: x.startswith("a"), "Starts with A"),
        (lambda x: len(x) > 6, "Long text"),
        default="other",
        locations=loc.body(columns="char"),
    )
)
```


<style>
#cfjajbvchs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cfjajbvchs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cfjajbvchs p { margin: 0; padding: 0; }
 #cfjajbvchs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cfjajbvchs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cfjajbvchs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cfjajbvchs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cfjajbvchs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cfjajbvchs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cfjajbvchs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cfjajbvchs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cfjajbvchs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cfjajbvchs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cfjajbvchs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cfjajbvchs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cfjajbvchs .gt_spanner_row { border-bottom-style: hidden; }
 #cfjajbvchs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cfjajbvchs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cfjajbvchs .gt_from_md> :first-child { margin-top: 0; }
 #cfjajbvchs .gt_from_md> :last-child { margin-bottom: 0; }
 #cfjajbvchs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cfjajbvchs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cfjajbvchs .gt_indent_1 { text-indent: 5px; }
 #cfjajbvchs .gt_indent_2 { text-indent: calc(5px * 2); }
 #cfjajbvchs .gt_indent_3 { text-indent: calc(5px * 3); }
 #cfjajbvchs .gt_indent_4 { text-indent: calc(5px * 4); }
 #cfjajbvchs .gt_indent_5 { text-indent: calc(5px * 5); }
 #cfjajbvchs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cfjajbvchs .gt_row_group_first td { border-top-width: 2px; }
 #cfjajbvchs .gt_row_group_first th { border-top-width: 2px; }
 #cfjajbvchs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cfjajbvchs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cfjajbvchs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cfjajbvchs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cfjajbvchs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cfjajbvchs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cfjajbvchs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cfjajbvchs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cfjajbvchs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cfjajbvchs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cfjajbvchs .gt_left { text-align: left; }
 #cfjajbvchs .gt_center { text-align: center; }
 #cfjajbvchs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cfjajbvchs .gt_font_normal { font-weight: normal; }
 #cfjajbvchs .gt_font_bold { font-weight: bold; }
 #cfjajbvchs .gt_font_italic { font-style: italic; }
 #cfjajbvchs .gt_super { font-size: 65%; }
 #cfjajbvchs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cfjajbvchs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cfjajbvchs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cfjajbvchs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cfjajbvchs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cfjajbvchs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char          |
|--------|---------------|
| 0.1111 | Starts with A |
| 2.222  | other         |
| 33.33  | Long text     |
| 444.4  | other         |
