# GT.text_case_match()


Perform text replacements with a switch-like approach.


Usage

``` python
GT.text_case_match(
    *cases,
    default=None,
    replace="all",
    locations=None,
)
```


With [text_case_match()](GT.text_case_match.md#great_tables.GT.text_case_match) we can supply a sequence of matching cases in the form of `(old_text, new_text)` tuples. Each tuple's first element specifies text to match (either a single string or a list of strings) and the second element provides the replacement. By default, the matching is performed on the entire cell text (`replace="all"`); use `replace="partial"` for substring matching and replacement.


## Parameters


`*cases: tuple[str | list[str], str]`  
One or more tuples of the form `(old_text, new_text)` where `old_text` is a string or list of strings to match, and `new_text` is the replacement string.

`default: str | None = None`  
The replacement text to use when cell values aren't matched by any of the supplied cases. If `None` (the default), unmatched cells are left unchanged.

`replace: Literal[``"all", `<span class="st">`"partial"``]`</span>` = ``"all"`  
The method for text replacement. Use `"all"` (the default) to match and replace the entire cell text, or `"partial"` to match and replace substrings within the cell text.

`locations: Loc | list[Loc] | None = None`  
The cell or set of cells to be associated with the text replacement. Supported locations include [loc.body()](loc.body.md#great_tables.loc.body), [loc.stub()](loc.stub.md#great_tables.loc.stub), [loc.row_groups()](loc.row_groups.md#great_tables.loc.row_groups), and [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels). If `None`, defaults to [loc.body()](loc.body.md#great_tables.loc.body).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Replace specific cell values in the `char` column with different text.


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char"]].head(4))
    .text_case_match(
        ("apricot", "APRICOT"),
        (["banana", "coconut"], "tropical fruit"),
        default="other",
        locations=loc.body(columns="char"),
    )
)
```


<style>
#umqbgegpae table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#umqbgegpae thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#umqbgegpae p { margin: 0; padding: 0; }
 #umqbgegpae .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #umqbgegpae .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #umqbgegpae .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #umqbgegpae .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #umqbgegpae .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #umqbgegpae .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #umqbgegpae .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #umqbgegpae .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #umqbgegpae .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #umqbgegpae .gt_column_spanner_outer:first-child { padding-left: 0; }
 #umqbgegpae .gt_column_spanner_outer:last-child { padding-right: 0; }
 #umqbgegpae .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #umqbgegpae .gt_spanner_row { border-bottom-style: hidden; }
 #umqbgegpae .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #umqbgegpae .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #umqbgegpae .gt_from_md> :first-child { margin-top: 0; }
 #umqbgegpae .gt_from_md> :last-child { margin-bottom: 0; }
 #umqbgegpae .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #umqbgegpae .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #umqbgegpae .gt_indent_1 { text-indent: 5px; }
 #umqbgegpae .gt_indent_2 { text-indent: calc(5px * 2); }
 #umqbgegpae .gt_indent_3 { text-indent: calc(5px * 3); }
 #umqbgegpae .gt_indent_4 { text-indent: calc(5px * 4); }
 #umqbgegpae .gt_indent_5 { text-indent: calc(5px * 5); }
 #umqbgegpae .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #umqbgegpae .gt_row_group_first td { border-top-width: 2px; }
 #umqbgegpae .gt_row_group_first th { border-top-width: 2px; }
 #umqbgegpae .gt_striped { color: #333333; background-color: #F4F4F4; }
 #umqbgegpae .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #umqbgegpae .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #umqbgegpae .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #umqbgegpae .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #umqbgegpae .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #umqbgegpae .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #umqbgegpae .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #umqbgegpae .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #umqbgegpae .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #umqbgegpae .gt_left { text-align: left; }
 #umqbgegpae .gt_center { text-align: center; }
 #umqbgegpae .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #umqbgegpae .gt_font_normal { font-weight: normal; }
 #umqbgegpae .gt_font_bold { font-weight: bold; }
 #umqbgegpae .gt_font_italic { font-style: italic; }
 #umqbgegpae .gt_super { font-size: 65%; }
 #umqbgegpae .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #umqbgegpae .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #umqbgegpae .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #umqbgegpae .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #umqbgegpae .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #umqbgegpae .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char           |
|--------|----------------|
| 0.1111 | APRICOT        |
| 2.222  | tropical fruit |
| 33.33  | tropical fruit |
| 444.4  | other          |


Use `replace="partial"` to perform substring replacements.


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char"]].head(4))
    .text_case_match(
        ("an", "@"),
        replace="partial",
        locations=loc.body(columns="char"),
    )
)
```


<style>
#xyvqyagyru table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xyvqyagyru thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xyvqyagyru p { margin: 0; padding: 0; }
 #xyvqyagyru .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xyvqyagyru .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xyvqyagyru .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xyvqyagyru .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xyvqyagyru .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xyvqyagyru .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xyvqyagyru .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xyvqyagyru .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xyvqyagyru .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xyvqyagyru .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xyvqyagyru .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xyvqyagyru .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xyvqyagyru .gt_spanner_row { border-bottom-style: hidden; }
 #xyvqyagyru .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xyvqyagyru .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xyvqyagyru .gt_from_md> :first-child { margin-top: 0; }
 #xyvqyagyru .gt_from_md> :last-child { margin-bottom: 0; }
 #xyvqyagyru .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xyvqyagyru .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xyvqyagyru .gt_indent_1 { text-indent: 5px; }
 #xyvqyagyru .gt_indent_2 { text-indent: calc(5px * 2); }
 #xyvqyagyru .gt_indent_3 { text-indent: calc(5px * 3); }
 #xyvqyagyru .gt_indent_4 { text-indent: calc(5px * 4); }
 #xyvqyagyru .gt_indent_5 { text-indent: calc(5px * 5); }
 #xyvqyagyru .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xyvqyagyru .gt_row_group_first td { border-top-width: 2px; }
 #xyvqyagyru .gt_row_group_first th { border-top-width: 2px; }
 #xyvqyagyru .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xyvqyagyru .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xyvqyagyru .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xyvqyagyru .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xyvqyagyru .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xyvqyagyru .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xyvqyagyru .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xyvqyagyru .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xyvqyagyru .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xyvqyagyru .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xyvqyagyru .gt_left { text-align: left; }
 #xyvqyagyru .gt_center { text-align: center; }
 #xyvqyagyru .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xyvqyagyru .gt_font_normal { font-weight: normal; }
 #xyvqyagyru .gt_font_bold { font-weight: bold; }
 #xyvqyagyru .gt_font_italic { font-style: italic; }
 #xyvqyagyru .gt_super { font-size: 65%; }
 #xyvqyagyru .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xyvqyagyru .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xyvqyagyru .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xyvqyagyru .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xyvqyagyru .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xyvqyagyru .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    |
|--------|---------|
| 0.1111 | apricot |
| 2.222  | b@@a    |
| 33.33  | coconut |
| 444.4  | duri@   |
