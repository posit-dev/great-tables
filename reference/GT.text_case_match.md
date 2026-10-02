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
#ghmqrdeizf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ghmqrdeizf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ghmqrdeizf p { margin: 0; padding: 0; }
 #ghmqrdeizf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ghmqrdeizf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ghmqrdeizf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ghmqrdeizf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ghmqrdeizf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ghmqrdeizf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghmqrdeizf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ghmqrdeizf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ghmqrdeizf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ghmqrdeizf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ghmqrdeizf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ghmqrdeizf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ghmqrdeizf .gt_spanner_row { border-bottom-style: hidden; }
 #ghmqrdeizf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ghmqrdeizf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ghmqrdeizf .gt_from_md> :first-child { margin-top: 0; }
 #ghmqrdeizf .gt_from_md> :last-child { margin-bottom: 0; }
 #ghmqrdeizf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ghmqrdeizf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ghmqrdeizf .gt_indent_1 { text-indent: 5px; }
 #ghmqrdeizf .gt_indent_2 { text-indent: calc(5px * 2); }
 #ghmqrdeizf .gt_indent_3 { text-indent: calc(5px * 3); }
 #ghmqrdeizf .gt_indent_4 { text-indent: calc(5px * 4); }
 #ghmqrdeizf .gt_indent_5 { text-indent: calc(5px * 5); }
 #ghmqrdeizf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ghmqrdeizf .gt_row_group_first td { border-top-width: 2px; }
 #ghmqrdeizf .gt_row_group_first th { border-top-width: 2px; }
 #ghmqrdeizf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ghmqrdeizf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghmqrdeizf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ghmqrdeizf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ghmqrdeizf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghmqrdeizf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ghmqrdeizf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ghmqrdeizf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ghmqrdeizf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghmqrdeizf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ghmqrdeizf .gt_left { text-align: left; }
 #ghmqrdeizf .gt_center { text-align: center; }
 #ghmqrdeizf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ghmqrdeizf .gt_font_normal { font-weight: normal; }
 #ghmqrdeizf .gt_font_bold { font-weight: bold; }
 #ghmqrdeizf .gt_font_italic { font-style: italic; }
 #ghmqrdeizf .gt_super { font-size: 65%; }
 #ghmqrdeizf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghmqrdeizf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ghmqrdeizf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghmqrdeizf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ghmqrdeizf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ghmqrdeizf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#setmbzurnz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#setmbzurnz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#setmbzurnz p { margin: 0; padding: 0; }
 #setmbzurnz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #setmbzurnz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #setmbzurnz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #setmbzurnz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #setmbzurnz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #setmbzurnz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #setmbzurnz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #setmbzurnz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #setmbzurnz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #setmbzurnz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #setmbzurnz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #setmbzurnz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #setmbzurnz .gt_spanner_row { border-bottom-style: hidden; }
 #setmbzurnz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #setmbzurnz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #setmbzurnz .gt_from_md> :first-child { margin-top: 0; }
 #setmbzurnz .gt_from_md> :last-child { margin-bottom: 0; }
 #setmbzurnz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #setmbzurnz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #setmbzurnz .gt_indent_1 { text-indent: 5px; }
 #setmbzurnz .gt_indent_2 { text-indent: calc(5px * 2); }
 #setmbzurnz .gt_indent_3 { text-indent: calc(5px * 3); }
 #setmbzurnz .gt_indent_4 { text-indent: calc(5px * 4); }
 #setmbzurnz .gt_indent_5 { text-indent: calc(5px * 5); }
 #setmbzurnz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #setmbzurnz .gt_row_group_first td { border-top-width: 2px; }
 #setmbzurnz .gt_row_group_first th { border-top-width: 2px; }
 #setmbzurnz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #setmbzurnz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #setmbzurnz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #setmbzurnz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #setmbzurnz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #setmbzurnz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #setmbzurnz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #setmbzurnz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #setmbzurnz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #setmbzurnz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #setmbzurnz .gt_left { text-align: left; }
 #setmbzurnz .gt_center { text-align: center; }
 #setmbzurnz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #setmbzurnz .gt_font_normal { font-weight: normal; }
 #setmbzurnz .gt_font_bold { font-weight: bold; }
 #setmbzurnz .gt_font_italic { font-style: italic; }
 #setmbzurnz .gt_super { font-size: 65%; }
 #setmbzurnz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #setmbzurnz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #setmbzurnz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #setmbzurnz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #setmbzurnz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #setmbzurnz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    |
|--------|---------|
| 0.1111 | apricot |
| 2.222  | b@@a    |
| 33.33  | coconut |
| 444.4  | duri@   |
