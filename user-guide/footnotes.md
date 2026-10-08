# Footnotes

Footnotes provide a way to annotate specific cells, columns, or other table parts with additional context without cluttering the main display. **Great Tables** manages footnotes as a system: marks are automatically sequenced, placed consistently, and matched to their explanatory text in the table footer.

Footnotes are best suited for cell-specific or column-specific context that would clutter the main display if placed inline. For information that applies to the entire table, a source note in the footer (via [tab_source_note()](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note)) is usually a better fit because it avoids attaching a mark to any one location. And for systematic column descriptions, such as units or definitions, consider relabeling the column itself so the context is always visible without requiring the reader to look down at the footer.


# A Basic Footnote

Adding a footnote requires two things: the footnote text and a location specifier indicating where the footnote mark should appear. The [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote) method handles both, placing the mark at the targeted location and appending the text to the footer.


``` python
from great_tables import GT, md, loc
from great_tables.data import airquality

air_mini = airquality.head(5)

(
    GT(air_mini)
    .tab_header(title="New York Air Quality", subtitle="Daily measurements, May 1973")
    .tab_footnote(
        footnote="Measured in parts per billion (ppbV).",
        locations=loc.column_labels(columns="Ozone")
    )
)
```


<style>
#exxgcrxaqc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#exxgcrxaqc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#exxgcrxaqc p { margin: 0; padding: 0; }
 #exxgcrxaqc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #exxgcrxaqc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #exxgcrxaqc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #exxgcrxaqc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #exxgcrxaqc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #exxgcrxaqc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exxgcrxaqc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #exxgcrxaqc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #exxgcrxaqc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #exxgcrxaqc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #exxgcrxaqc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #exxgcrxaqc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #exxgcrxaqc .gt_spanner_row { border-bottom-style: hidden; }
 #exxgcrxaqc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #exxgcrxaqc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #exxgcrxaqc .gt_from_md> :first-child { margin-top: 0; }
 #exxgcrxaqc .gt_from_md> :last-child { margin-bottom: 0; }
 #exxgcrxaqc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #exxgcrxaqc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #exxgcrxaqc .gt_indent_1 { text-indent: 5px; }
 #exxgcrxaqc .gt_indent_2 { text-indent: calc(5px * 2); }
 #exxgcrxaqc .gt_indent_3 { text-indent: calc(5px * 3); }
 #exxgcrxaqc .gt_indent_4 { text-indent: calc(5px * 4); }
 #exxgcrxaqc .gt_indent_5 { text-indent: calc(5px * 5); }
 #exxgcrxaqc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #exxgcrxaqc .gt_row_group_first td { border-top-width: 2px; }
 #exxgcrxaqc .gt_row_group_first th { border-top-width: 2px; }
 #exxgcrxaqc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #exxgcrxaqc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exxgcrxaqc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #exxgcrxaqc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #exxgcrxaqc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exxgcrxaqc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #exxgcrxaqc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #exxgcrxaqc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #exxgcrxaqc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exxgcrxaqc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #exxgcrxaqc .gt_left { text-align: left; }
 #exxgcrxaqc .gt_center { text-align: center; }
 #exxgcrxaqc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #exxgcrxaqc .gt_font_normal { font-weight: normal; }
 #exxgcrxaqc .gt_font_bold { font-weight: bold; }
 #exxgcrxaqc .gt_font_italic { font-style: italic; }
 #exxgcrxaqc .gt_super { font-size: 65%; }
 #exxgcrxaqc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exxgcrxaqc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #exxgcrxaqc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exxgcrxaqc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #exxgcrxaqc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #exxgcrxaqc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">New York Air Quality</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements, May 1973</th>
</tr>
<tr class="gt_col_headings">
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R</th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
</tr>
<tr>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
</tr>
<tr>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
</tr>
<tr>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
</tr>
<tr>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Measured in parts per billion (ppbV).</td>
</tr>
</tfoot>

</table>


The footnote mark (a superscript number) appears next to the `"Ozone"` column label, and the corresponding text appears at the bottom of the table.


# Targeting Different Locations

Footnotes can be attached to many different parts of the table. The `locations=` argument accepts any of the `loc` specifiers that support footnotes. Here are some of the most common targets.


## Column Labels

Attaching a footnote to a column label is useful for clarifying units or methodology.


``` python
(
    GT(air_mini)
    .tab_header(title="New York Air Quality", subtitle="Daily measurements, May 1973")
    .tab_footnote(
        footnote="Solar radiation in Langleys (cal/cm²), measured 08:00-noon.",
        locations=loc.column_labels(columns="Solar_R")
    )
)
```


<style>
#bhmvwndqyj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bhmvwndqyj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bhmvwndqyj p { margin: 0; padding: 0; }
 #bhmvwndqyj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bhmvwndqyj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bhmvwndqyj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bhmvwndqyj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bhmvwndqyj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhmvwndqyj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhmvwndqyj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhmvwndqyj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bhmvwndqyj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bhmvwndqyj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bhmvwndqyj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bhmvwndqyj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bhmvwndqyj .gt_spanner_row { border-bottom-style: hidden; }
 #bhmvwndqyj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bhmvwndqyj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bhmvwndqyj .gt_from_md> :first-child { margin-top: 0; }
 #bhmvwndqyj .gt_from_md> :last-child { margin-bottom: 0; }
 #bhmvwndqyj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bhmvwndqyj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bhmvwndqyj .gt_indent_1 { text-indent: 5px; }
 #bhmvwndqyj .gt_indent_2 { text-indent: calc(5px * 2); }
 #bhmvwndqyj .gt_indent_3 { text-indent: calc(5px * 3); }
 #bhmvwndqyj .gt_indent_4 { text-indent: calc(5px * 4); }
 #bhmvwndqyj .gt_indent_5 { text-indent: calc(5px * 5); }
 #bhmvwndqyj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bhmvwndqyj .gt_row_group_first td { border-top-width: 2px; }
 #bhmvwndqyj .gt_row_group_first th { border-top-width: 2px; }
 #bhmvwndqyj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bhmvwndqyj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhmvwndqyj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhmvwndqyj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bhmvwndqyj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhmvwndqyj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhmvwndqyj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bhmvwndqyj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bhmvwndqyj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhmvwndqyj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhmvwndqyj .gt_left { text-align: left; }
 #bhmvwndqyj .gt_center { text-align: center; }
 #bhmvwndqyj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bhmvwndqyj .gt_font_normal { font-weight: normal; }
 #bhmvwndqyj .gt_font_bold { font-weight: bold; }
 #bhmvwndqyj .gt_font_italic { font-style: italic; }
 #bhmvwndqyj .gt_super { font-size: 65%; }
 #bhmvwndqyj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhmvwndqyj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bhmvwndqyj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhmvwndqyj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhmvwndqyj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bhmvwndqyj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">New York Air Quality</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements, May 1973</th>
</tr>
<tr class="gt_col_headings">
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
</tr>
<tr>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
</tr>
<tr>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
</tr>
<tr>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
</tr>
<tr>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Solar radiation in Langleys (cal/cm²), measured 08:00-noon.</td>
</tr>
</tfoot>

</table>


## Body Cells

You can annotate specific data cells by targeting them with [loc.body()](../reference/loc.body.md#great_tables.loc.body).


``` python
(
    GT(air_mini)
    .tab_header(title="New York Air Quality", subtitle="Daily measurements, May 1973")
    .tab_footnote(
        footnote="Highest temperature in this sample.",
        locations=loc.body(columns="Temp", rows=[0])
    )
)
```


<style>
#farhmlhzvl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#farhmlhzvl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#farhmlhzvl p { margin: 0; padding: 0; }
 #farhmlhzvl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #farhmlhzvl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #farhmlhzvl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #farhmlhzvl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #farhmlhzvl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #farhmlhzvl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #farhmlhzvl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #farhmlhzvl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #farhmlhzvl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #farhmlhzvl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #farhmlhzvl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #farhmlhzvl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #farhmlhzvl .gt_spanner_row { border-bottom-style: hidden; }
 #farhmlhzvl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #farhmlhzvl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #farhmlhzvl .gt_from_md> :first-child { margin-top: 0; }
 #farhmlhzvl .gt_from_md> :last-child { margin-bottom: 0; }
 #farhmlhzvl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #farhmlhzvl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #farhmlhzvl .gt_indent_1 { text-indent: 5px; }
 #farhmlhzvl .gt_indent_2 { text-indent: calc(5px * 2); }
 #farhmlhzvl .gt_indent_3 { text-indent: calc(5px * 3); }
 #farhmlhzvl .gt_indent_4 { text-indent: calc(5px * 4); }
 #farhmlhzvl .gt_indent_5 { text-indent: calc(5px * 5); }
 #farhmlhzvl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #farhmlhzvl .gt_row_group_first td { border-top-width: 2px; }
 #farhmlhzvl .gt_row_group_first th { border-top-width: 2px; }
 #farhmlhzvl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #farhmlhzvl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #farhmlhzvl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #farhmlhzvl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #farhmlhzvl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #farhmlhzvl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #farhmlhzvl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #farhmlhzvl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #farhmlhzvl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #farhmlhzvl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #farhmlhzvl .gt_left { text-align: left; }
 #farhmlhzvl .gt_center { text-align: center; }
 #farhmlhzvl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #farhmlhzvl .gt_font_normal { font-weight: normal; }
 #farhmlhzvl .gt_font_bold { font-weight: bold; }
 #farhmlhzvl .gt_font_italic { font-style: italic; }
 #farhmlhzvl .gt_super { font-size: 65%; }
 #farhmlhzvl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #farhmlhzvl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #farhmlhzvl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #farhmlhzvl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #farhmlhzvl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #farhmlhzvl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">New York Air Quality</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements, May 1973</th>
</tr>
<tr class="gt_col_headings">
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R</th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 67</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
</tr>
<tr>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
</tr>
<tr>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
</tr>
<tr>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
</tr>
<tr>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Highest temperature in this sample.</td>
</tr>
</tfoot>

</table>


## The Title or Subtitle

Footnotes on the table header can provide methodological notes or data source context.


``` python
(
    GT(air_mini)
    .tab_header(title="New York Air Quality", subtitle="Daily measurements, May 1973")
    .tab_footnote(
        footnote="Data collected at a monitoring station in midtown Manhattan.",
        locations=loc.title()
    )
)
```


<style>
#oxouujombu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oxouujombu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oxouujombu p { margin: 0; padding: 0; }
 #oxouujombu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oxouujombu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oxouujombu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oxouujombu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oxouujombu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oxouujombu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxouujombu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oxouujombu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oxouujombu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oxouujombu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oxouujombu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oxouujombu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oxouujombu .gt_spanner_row { border-bottom-style: hidden; }
 #oxouujombu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oxouujombu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oxouujombu .gt_from_md> :first-child { margin-top: 0; }
 #oxouujombu .gt_from_md> :last-child { margin-bottom: 0; }
 #oxouujombu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oxouujombu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oxouujombu .gt_indent_1 { text-indent: 5px; }
 #oxouujombu .gt_indent_2 { text-indent: calc(5px * 2); }
 #oxouujombu .gt_indent_3 { text-indent: calc(5px * 3); }
 #oxouujombu .gt_indent_4 { text-indent: calc(5px * 4); }
 #oxouujombu .gt_indent_5 { text-indent: calc(5px * 5); }
 #oxouujombu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oxouujombu .gt_row_group_first td { border-top-width: 2px; }
 #oxouujombu .gt_row_group_first th { border-top-width: 2px; }
 #oxouujombu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oxouujombu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxouujombu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oxouujombu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oxouujombu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxouujombu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oxouujombu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oxouujombu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oxouujombu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxouujombu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oxouujombu .gt_left { text-align: left; }
 #oxouujombu .gt_center { text-align: center; }
 #oxouujombu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oxouujombu .gt_font_normal { font-weight: normal; }
 #oxouujombu .gt_font_bold { font-weight: bold; }
 #oxouujombu .gt_font_italic { font-style: italic; }
 #oxouujombu .gt_super { font-size: 65%; }
 #oxouujombu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxouujombu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oxouujombu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxouujombu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oxouujombu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oxouujombu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">New York Air Quality<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements, May 1973</th>
</tr>
<tr class="gt_col_headings">
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R</th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
</tr>
<tr>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
</tr>
<tr>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
</tr>
<tr>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
</tr>
<tr>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Data collected at a monitoring station in midtown Manhattan.</td>
</tr>
</tfoot>

</table>


# Multiple Footnotes

You can add multiple footnotes to a single table. Each call to [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote) creates a new footnote with its own sequenced mark. The marks are numbered in the order they appear in the table (reading left-to-right, top-to-bottom).


``` python
(
    GT(air_mini)
    .tab_header(title="New York Air Quality", subtitle="Daily measurements, May 1973")
    .tab_footnote(
        footnote="Mean ozone concentration, 13:00-15:00.",
        locations=loc.column_labels(columns="Ozone")
    )
    .tab_footnote(
        footnote="Maximum daily temperature in degrees Fahrenheit.",
        locations=loc.column_labels(columns="Temp")
    )
    .tab_footnote(
        footnote="Measurement device was recalibrated on this day.",
        locations=loc.body(columns="Ozone", rows=[2])
    )
)
```


<style>
#xzuwwoebnc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xzuwwoebnc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xzuwwoebnc p { margin: 0; padding: 0; }
 #xzuwwoebnc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xzuwwoebnc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xzuwwoebnc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xzuwwoebnc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xzuwwoebnc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xzuwwoebnc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xzuwwoebnc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xzuwwoebnc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xzuwwoebnc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xzuwwoebnc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xzuwwoebnc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xzuwwoebnc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xzuwwoebnc .gt_spanner_row { border-bottom-style: hidden; }
 #xzuwwoebnc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xzuwwoebnc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xzuwwoebnc .gt_from_md> :first-child { margin-top: 0; }
 #xzuwwoebnc .gt_from_md> :last-child { margin-bottom: 0; }
 #xzuwwoebnc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xzuwwoebnc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xzuwwoebnc .gt_indent_1 { text-indent: 5px; }
 #xzuwwoebnc .gt_indent_2 { text-indent: calc(5px * 2); }
 #xzuwwoebnc .gt_indent_3 { text-indent: calc(5px * 3); }
 #xzuwwoebnc .gt_indent_4 { text-indent: calc(5px * 4); }
 #xzuwwoebnc .gt_indent_5 { text-indent: calc(5px * 5); }
 #xzuwwoebnc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xzuwwoebnc .gt_row_group_first td { border-top-width: 2px; }
 #xzuwwoebnc .gt_row_group_first th { border-top-width: 2px; }
 #xzuwwoebnc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xzuwwoebnc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xzuwwoebnc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xzuwwoebnc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xzuwwoebnc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xzuwwoebnc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xzuwwoebnc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xzuwwoebnc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xzuwwoebnc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xzuwwoebnc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xzuwwoebnc .gt_left { text-align: left; }
 #xzuwwoebnc .gt_center { text-align: center; }
 #xzuwwoebnc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xzuwwoebnc .gt_font_normal { font-weight: normal; }
 #xzuwwoebnc .gt_font_bold { font-weight: bold; }
 #xzuwwoebnc .gt_font_italic { font-style: italic; }
 #xzuwwoebnc .gt_super { font-size: 65%; }
 #xzuwwoebnc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xzuwwoebnc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xzuwwoebnc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xzuwwoebnc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xzuwwoebnc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xzuwwoebnc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">New York Air Quality</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements, May 1973</th>
</tr>
<tr class="gt_col_headings">
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R</th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">2</span></th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
</tr>
<tr>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
</tr>
<tr>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">3</span> 12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
</tr>
<tr>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
</tr>
<tr>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Mean ozone concentration, 13:00-15:00.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">2</span> Maximum daily temperature in degrees Fahrenheit.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">3</span> Measurement device was recalibrated on this day.</td>
</tr>
</tfoot>

</table>


Three footnote marks are placed in the table, and three corresponding notes appear in the footer, each with its sequential number.

While you can add many footnotes to a single table, use restraint. More than three or four footnotes can overwhelm the reader and make the footer itself difficult to navigate. If you find yourself adding footnotes to most cells, consider whether the information would be better conveyed through more descriptive column labels, a subtitle, or a separate explanatory paragraph outside the table.


# Footnotes Without a Mark

If you want to include explanatory text in the footer without attaching a mark to any cell, omit the `locations=` argument (or set it to `None`).


``` python
(
    GT(air_mini)
    .tab_header(title="New York Air Quality", subtitle="Daily measurements, May 1973")
    .tab_footnote(footnote="All measurements taken in New York City, 1973.")
)
```


<style>
#hnfnxtujua table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hnfnxtujua thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hnfnxtujua p { margin: 0; padding: 0; }
 #hnfnxtujua .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hnfnxtujua .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hnfnxtujua .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hnfnxtujua .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hnfnxtujua .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hnfnxtujua .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hnfnxtujua .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hnfnxtujua .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hnfnxtujua .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hnfnxtujua .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hnfnxtujua .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hnfnxtujua .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hnfnxtujua .gt_spanner_row { border-bottom-style: hidden; }
 #hnfnxtujua .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hnfnxtujua .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hnfnxtujua .gt_from_md> :first-child { margin-top: 0; }
 #hnfnxtujua .gt_from_md> :last-child { margin-bottom: 0; }
 #hnfnxtujua .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hnfnxtujua .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hnfnxtujua .gt_indent_1 { text-indent: 5px; }
 #hnfnxtujua .gt_indent_2 { text-indent: calc(5px * 2); }
 #hnfnxtujua .gt_indent_3 { text-indent: calc(5px * 3); }
 #hnfnxtujua .gt_indent_4 { text-indent: calc(5px * 4); }
 #hnfnxtujua .gt_indent_5 { text-indent: calc(5px * 5); }
 #hnfnxtujua .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hnfnxtujua .gt_row_group_first td { border-top-width: 2px; }
 #hnfnxtujua .gt_row_group_first th { border-top-width: 2px; }
 #hnfnxtujua .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hnfnxtujua .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hnfnxtujua .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hnfnxtujua .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hnfnxtujua .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hnfnxtujua .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hnfnxtujua .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hnfnxtujua .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hnfnxtujua .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hnfnxtujua .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hnfnxtujua .gt_left { text-align: left; }
 #hnfnxtujua .gt_center { text-align: center; }
 #hnfnxtujua .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hnfnxtujua .gt_font_normal { font-weight: normal; }
 #hnfnxtujua .gt_font_bold { font-weight: bold; }
 #hnfnxtujua .gt_font_italic { font-style: italic; }
 #hnfnxtujua .gt_super { font-size: 65%; }
 #hnfnxtujua .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hnfnxtujua .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hnfnxtujua .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hnfnxtujua .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hnfnxtujua .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hnfnxtujua .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">New York Air Quality</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements, May 1973</th>
</tr>
<tr class="gt_col_headings">
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R</th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
</tr>
<tr>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
</tr>
<tr>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
</tr>
<tr>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
</tr>
<tr>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote">All measurements taken in New York City, 1973.</td>
</tr>
</tfoot>

</table>


This is useful for general notes that apply to the entire table rather than to a specific cell or label. Markless footnotes work well for disclaimers, methodological notes, or data-source attributions that apply broadly rather than to any single cell. Because they carry no superscript mark, they read as supplementary context for the table as a whole.


# Controlling Mark Placement

The `placement=` argument determines where the footnote mark appears relative to the cell content. The options are `"auto"` (the default), `"left"`, and `"right"`.


``` python
(
    GT(air_mini)
    .tab_header(title="New York Air Quality", subtitle="Daily measurements, May 1973")
    .tab_footnote(
        footnote="Measured at ground level.",
        locations=loc.column_labels(columns="Ozone"),
        placement="left"
    )
)
```


<style>
#eexdcywdha table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eexdcywdha thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eexdcywdha p { margin: 0; padding: 0; }
 #eexdcywdha .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eexdcywdha .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eexdcywdha .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eexdcywdha .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eexdcywdha .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eexdcywdha .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eexdcywdha .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eexdcywdha .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eexdcywdha .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eexdcywdha .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eexdcywdha .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eexdcywdha .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eexdcywdha .gt_spanner_row { border-bottom-style: hidden; }
 #eexdcywdha .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eexdcywdha .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eexdcywdha .gt_from_md> :first-child { margin-top: 0; }
 #eexdcywdha .gt_from_md> :last-child { margin-bottom: 0; }
 #eexdcywdha .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eexdcywdha .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eexdcywdha .gt_indent_1 { text-indent: 5px; }
 #eexdcywdha .gt_indent_2 { text-indent: calc(5px * 2); }
 #eexdcywdha .gt_indent_3 { text-indent: calc(5px * 3); }
 #eexdcywdha .gt_indent_4 { text-indent: calc(5px * 4); }
 #eexdcywdha .gt_indent_5 { text-indent: calc(5px * 5); }
 #eexdcywdha .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eexdcywdha .gt_row_group_first td { border-top-width: 2px; }
 #eexdcywdha .gt_row_group_first th { border-top-width: 2px; }
 #eexdcywdha .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eexdcywdha .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eexdcywdha .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eexdcywdha .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eexdcywdha .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eexdcywdha .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eexdcywdha .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eexdcywdha .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eexdcywdha .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eexdcywdha .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eexdcywdha .gt_left { text-align: left; }
 #eexdcywdha .gt_center { text-align: center; }
 #eexdcywdha .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eexdcywdha .gt_font_normal { font-weight: normal; }
 #eexdcywdha .gt_font_bold { font-weight: bold; }
 #eexdcywdha .gt_font_italic { font-style: italic; }
 #eexdcywdha .gt_super { font-size: 65%; }
 #eexdcywdha .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eexdcywdha .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eexdcywdha .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eexdcywdha .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eexdcywdha .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eexdcywdha .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">New York Air Quality</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements, May 1973</th>
</tr>
<tr class="gt_col_headings">
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Ozone</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R</th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
</tr>
<tr>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
</tr>
<tr>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
</tr>
<tr>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
</tr>
<tr>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Measured at ground level.</td>
</tr>
</tfoot>

</table>


With `placement="left"`, the footnote mark appears before the cell text rather than after it.


# Using Markdown in Footnotes

Footnote text supports Markdown formatting through the [md()](../reference/md.md#great_tables.md) helper function. This lets you include emphasis, links, or other inline formatting in your footnotes.


``` python
(
    GT(air_mini)
    .tab_header(title="New York Air Quality", subtitle="Daily measurements, May 1973")
    .tab_footnote(
        footnote=md("Source: *Interactive Data Analysis* (McNeil, 1977)."),
        locations=loc.title()
    )
)
```


<style>
#rzpwrgrhyo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rzpwrgrhyo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rzpwrgrhyo p { margin: 0; padding: 0; }
 #rzpwrgrhyo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rzpwrgrhyo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rzpwrgrhyo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rzpwrgrhyo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rzpwrgrhyo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rzpwrgrhyo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rzpwrgrhyo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rzpwrgrhyo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rzpwrgrhyo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rzpwrgrhyo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rzpwrgrhyo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rzpwrgrhyo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rzpwrgrhyo .gt_spanner_row { border-bottom-style: hidden; }
 #rzpwrgrhyo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rzpwrgrhyo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rzpwrgrhyo .gt_from_md> :first-child { margin-top: 0; }
 #rzpwrgrhyo .gt_from_md> :last-child { margin-bottom: 0; }
 #rzpwrgrhyo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rzpwrgrhyo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rzpwrgrhyo .gt_indent_1 { text-indent: 5px; }
 #rzpwrgrhyo .gt_indent_2 { text-indent: calc(5px * 2); }
 #rzpwrgrhyo .gt_indent_3 { text-indent: calc(5px * 3); }
 #rzpwrgrhyo .gt_indent_4 { text-indent: calc(5px * 4); }
 #rzpwrgrhyo .gt_indent_5 { text-indent: calc(5px * 5); }
 #rzpwrgrhyo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rzpwrgrhyo .gt_row_group_first td { border-top-width: 2px; }
 #rzpwrgrhyo .gt_row_group_first th { border-top-width: 2px; }
 #rzpwrgrhyo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rzpwrgrhyo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rzpwrgrhyo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rzpwrgrhyo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rzpwrgrhyo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rzpwrgrhyo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rzpwrgrhyo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rzpwrgrhyo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rzpwrgrhyo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rzpwrgrhyo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rzpwrgrhyo .gt_left { text-align: left; }
 #rzpwrgrhyo .gt_center { text-align: center; }
 #rzpwrgrhyo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rzpwrgrhyo .gt_font_normal { font-weight: normal; }
 #rzpwrgrhyo .gt_font_bold { font-weight: bold; }
 #rzpwrgrhyo .gt_font_italic { font-style: italic; }
 #rzpwrgrhyo .gt_super { font-size: 65%; }
 #rzpwrgrhyo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rzpwrgrhyo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rzpwrgrhyo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rzpwrgrhyo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rzpwrgrhyo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rzpwrgrhyo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">New York Air Quality<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements, May 1973</th>
</tr>
<tr class="gt_col_headings">
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R</th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
</tr>
<tr>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
</tr>
<tr>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
</tr>
<tr>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
</tr>
<tr>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Source: <em>Interactive Data Analysis</em> (McNeil, 1977).</td>
</tr>
</tfoot>

</table>


Footnotes are a subtle but important tool for building informative tables. They let you add precision and context where it matters most, keeping the main table body clean while ensuring readers have access to the details they need. The automatic sequencing and placement system means you can focus on content rather than managing mark numbers manually.
