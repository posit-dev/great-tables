# GT.opt_footnote_spec()


Option to modify the formatting of footnote marks.


Usage

``` python
GT.opt_footnote_spec(
    spec_ref=None,
    spec_ftr=None,
)
```


Control how footnote marks are styled in two independent contexts: inline references next to cell content (`spec_ref`) and marks in the footer listing (`spec_ftr`). Each takes a compact DSL string composed of formatting codes.

The spec DSL codes are:

- `"^"`: superscript
- `"b"`: bold
- `"i"`: italic
- `"()"` or `"(x)"`: parentheses around the mark
- `"[]"` or `"[x]"`: square brackets around the mark
- `"."`: trailing period
- `"x"`: optional placeholder for readability (ignored in parsing)


## Parameters


`spec_ref: str | None = None`  
A spec string controlling the formatting of inline reference marks (marks that appear next to cell content). If `None`, the current setting is unchanged. The default value in the options system is `"^i"` (superscript + italic).

`spec_ftr: str | None = None`  
A spec string controlling the formatting of footer marks (marks that appear in the footnote listing at the bottom of the table). If `None`, the current setting is unchanged. The default value in the options system is `"^i"` (superscript + italic).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's create a table with footnotes to demonstrate the spec DSL. We'll use superscript bold marks for inline references and superscript italic marks in the footer (the default).


``` python
from great_tables import GT, loc
import pandas as pd

df = pd.DataFrame({"city": ["Paris", "London", "Tokyo"], "pop_m": [2.1, 8.8, 13.9]})

(
    GT(df)
    .tab_header(title="Major Cities")
    .tab_footnote("2023 estimate", locations=loc.body(columns="pop_m", rows=[0, 1, 2]))
    .tab_footnote("Metropolitan area", locations=loc.column_labels(columns="pop_m"))
    .opt_footnote_spec(spec_ref="^b", spec_ftr="^i")
)
```


<style>
#eocqreqexx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eocqreqexx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eocqreqexx p { margin: 0; padding: 0; }
 #eocqreqexx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eocqreqexx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eocqreqexx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eocqreqexx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eocqreqexx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eocqreqexx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eocqreqexx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eocqreqexx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eocqreqexx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eocqreqexx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eocqreqexx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eocqreqexx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eocqreqexx .gt_spanner_row { border-bottom-style: hidden; }
 #eocqreqexx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eocqreqexx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eocqreqexx .gt_from_md> :first-child { margin-top: 0; }
 #eocqreqexx .gt_from_md> :last-child { margin-bottom: 0; }
 #eocqreqexx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eocqreqexx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eocqreqexx .gt_indent_1 { text-indent: 5px; }
 #eocqreqexx .gt_indent_2 { text-indent: calc(5px * 2); }
 #eocqreqexx .gt_indent_3 { text-indent: calc(5px * 3); }
 #eocqreqexx .gt_indent_4 { text-indent: calc(5px * 4); }
 #eocqreqexx .gt_indent_5 { text-indent: calc(5px * 5); }
 #eocqreqexx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eocqreqexx .gt_row_group_first td { border-top-width: 2px; }
 #eocqreqexx .gt_row_group_first th { border-top-width: 2px; }
 #eocqreqexx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eocqreqexx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eocqreqexx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eocqreqexx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eocqreqexx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eocqreqexx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eocqreqexx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eocqreqexx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eocqreqexx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eocqreqexx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eocqreqexx .gt_left { text-align: left; }
 #eocqreqexx .gt_center { text-align: center; }
 #eocqreqexx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eocqreqexx .gt_font_normal { font-weight: normal; }
 #eocqreqexx .gt_font_bold { font-weight: bold; }
 #eocqreqexx .gt_font_italic { font-style: italic; }
 #eocqreqexx .gt_super { font-size: 65%; }
 #eocqreqexx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eocqreqexx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eocqreqexx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eocqreqexx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eocqreqexx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eocqreqexx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_title gt_font_normal">Major Cities</th>
</tr>
<tr class="gt_col_headings">
<th id="city" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">city</th>
<th id="pop_m" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pop_m<span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:bold;line-height:0;">1</span></th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Paris</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:bold;line-height:0;">2</span> 2.1</td>
</tr>
<tr>
<td class="gt_row gt_left">London</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:bold;line-height:0;">2</span> 8.8</td>
</tr>
<tr>
<td class="gt_row gt_left">Tokyo</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:bold;line-height:0;">2</span> 13.9</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="2" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Metropolitan area</td>
</tr>
<tr class="gt_footnotes">
<td colspan="2" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">2</span> 2023 estimate</td>
</tr>
</tfoot>

</table>


Use parenthesized marks at baseline (no superscript) in both the inline references and the footer listing.


``` python
(
    GT(df)
    .tab_header(title="Major Cities")
    .tab_footnote("2023 estimate", locations=loc.body(columns="pop_m", rows=[0, 1, 2]))
    .tab_footnote("Metropolitan area", locations=loc.column_labels(columns="pop_m"))
    .opt_footnote_spec(spec_ref="(x)", spec_ftr="(x)")
)
```


<style>
#dlbdfuvtck table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dlbdfuvtck thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dlbdfuvtck p { margin: 0; padding: 0; }
 #dlbdfuvtck .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dlbdfuvtck .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dlbdfuvtck .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dlbdfuvtck .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dlbdfuvtck .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dlbdfuvtck .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dlbdfuvtck .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dlbdfuvtck .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dlbdfuvtck .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dlbdfuvtck .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dlbdfuvtck .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dlbdfuvtck .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dlbdfuvtck .gt_spanner_row { border-bottom-style: hidden; }
 #dlbdfuvtck .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dlbdfuvtck .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dlbdfuvtck .gt_from_md> :first-child { margin-top: 0; }
 #dlbdfuvtck .gt_from_md> :last-child { margin-bottom: 0; }
 #dlbdfuvtck .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dlbdfuvtck .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dlbdfuvtck .gt_indent_1 { text-indent: 5px; }
 #dlbdfuvtck .gt_indent_2 { text-indent: calc(5px * 2); }
 #dlbdfuvtck .gt_indent_3 { text-indent: calc(5px * 3); }
 #dlbdfuvtck .gt_indent_4 { text-indent: calc(5px * 4); }
 #dlbdfuvtck .gt_indent_5 { text-indent: calc(5px * 5); }
 #dlbdfuvtck .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dlbdfuvtck .gt_row_group_first td { border-top-width: 2px; }
 #dlbdfuvtck .gt_row_group_first th { border-top-width: 2px; }
 #dlbdfuvtck .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dlbdfuvtck .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dlbdfuvtck .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dlbdfuvtck .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dlbdfuvtck .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dlbdfuvtck .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dlbdfuvtck .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dlbdfuvtck .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dlbdfuvtck .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dlbdfuvtck .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dlbdfuvtck .gt_left { text-align: left; }
 #dlbdfuvtck .gt_center { text-align: center; }
 #dlbdfuvtck .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dlbdfuvtck .gt_font_normal { font-weight: normal; }
 #dlbdfuvtck .gt_font_bold { font-weight: bold; }
 #dlbdfuvtck .gt_font_italic { font-style: italic; }
 #dlbdfuvtck .gt_super { font-size: 65%; }
 #dlbdfuvtck .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dlbdfuvtck .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dlbdfuvtck .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dlbdfuvtck .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dlbdfuvtck .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dlbdfuvtck .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_title gt_font_normal">Major Cities</th>
</tr>
<tr class="gt_col_headings">
<th id="city" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">city</th>
<th id="pop_m" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pop_m<span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:normal;vertical-align:baseline;font-size:100%;">(1)</span></th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Paris</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:normal;vertical-align:baseline;font-size:100%;">(2)</span> 2.1</td>
</tr>
<tr>
<td class="gt_row gt_left">London</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:normal;vertical-align:baseline;font-size:100%;">(2)</span> 8.8</td>
</tr>
<tr>
<td class="gt_row gt_left">Tokyo</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:normal;vertical-align:baseline;font-size:100%;">(2)</span> 13.9</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="2" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:normal;vertical-align:baseline;font-size:100%;">(1)</span> Metropolitan area</td>
</tr>
<tr class="gt_footnotes">
<td colspan="2" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:normal;vertical-align:baseline;font-size:100%;">(2)</span> 2023 estimate</td>
</tr>
</tfoot>

</table>


Use superscript bold marks inline with bracketed marks and a trailing period in the footer.


``` python
(
    GT(df)
    .tab_header(title="Major Cities")
    .tab_footnote("2023 estimate", locations=loc.body(columns="pop_m", rows=[0, 1, 2]))
    .tab_footnote("Metropolitan area", locations=loc.column_labels(columns="pop_m"))
    .opt_footnote_spec(spec_ref="^b", spec_ftr="[x].")
)
```


<style>
#edkwqexcoi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#edkwqexcoi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#edkwqexcoi p { margin: 0; padding: 0; }
 #edkwqexcoi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #edkwqexcoi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #edkwqexcoi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #edkwqexcoi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #edkwqexcoi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #edkwqexcoi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #edkwqexcoi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #edkwqexcoi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #edkwqexcoi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #edkwqexcoi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #edkwqexcoi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #edkwqexcoi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #edkwqexcoi .gt_spanner_row { border-bottom-style: hidden; }
 #edkwqexcoi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #edkwqexcoi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #edkwqexcoi .gt_from_md> :first-child { margin-top: 0; }
 #edkwqexcoi .gt_from_md> :last-child { margin-bottom: 0; }
 #edkwqexcoi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #edkwqexcoi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #edkwqexcoi .gt_indent_1 { text-indent: 5px; }
 #edkwqexcoi .gt_indent_2 { text-indent: calc(5px * 2); }
 #edkwqexcoi .gt_indent_3 { text-indent: calc(5px * 3); }
 #edkwqexcoi .gt_indent_4 { text-indent: calc(5px * 4); }
 #edkwqexcoi .gt_indent_5 { text-indent: calc(5px * 5); }
 #edkwqexcoi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #edkwqexcoi .gt_row_group_first td { border-top-width: 2px; }
 #edkwqexcoi .gt_row_group_first th { border-top-width: 2px; }
 #edkwqexcoi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #edkwqexcoi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #edkwqexcoi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #edkwqexcoi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #edkwqexcoi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #edkwqexcoi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #edkwqexcoi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #edkwqexcoi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #edkwqexcoi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edkwqexcoi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #edkwqexcoi .gt_left { text-align: left; }
 #edkwqexcoi .gt_center { text-align: center; }
 #edkwqexcoi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #edkwqexcoi .gt_font_normal { font-weight: normal; }
 #edkwqexcoi .gt_font_bold { font-weight: bold; }
 #edkwqexcoi .gt_font_italic { font-style: italic; }
 #edkwqexcoi .gt_super { font-size: 65%; }
 #edkwqexcoi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edkwqexcoi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #edkwqexcoi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edkwqexcoi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #edkwqexcoi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #edkwqexcoi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_title gt_font_normal">Major Cities</th>
</tr>
<tr class="gt_col_headings">
<th id="city" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">city</th>
<th id="pop_m" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pop_m<span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:bold;line-height:0;">1</span></th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Paris</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:bold;line-height:0;">2</span> 2.1</td>
</tr>
<tr>
<td class="gt_row gt_left">London</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:bold;line-height:0;">2</span> 8.8</td>
</tr>
<tr>
<td class="gt_row gt_left">Tokyo</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:bold;line-height:0;">2</span> 13.9</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="2" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:normal;vertical-align:baseline;font-size:100%;">[1].</span> Metropolitan area</td>
</tr>
<tr class="gt_footnotes">
<td colspan="2" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:normal;font-weight:normal;vertical-align:baseline;font-size:100%;">[2].</span> 2023 estimate</td>
</tr>
</tfoot>

</table>
