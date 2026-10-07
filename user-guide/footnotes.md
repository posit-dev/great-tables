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
#muhryzkmgw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#muhryzkmgw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#muhryzkmgw p { margin: 0; padding: 0; }
 #muhryzkmgw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #muhryzkmgw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #muhryzkmgw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #muhryzkmgw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #muhryzkmgw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muhryzkmgw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muhryzkmgw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muhryzkmgw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #muhryzkmgw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #muhryzkmgw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #muhryzkmgw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #muhryzkmgw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #muhryzkmgw .gt_spanner_row { border-bottom-style: hidden; }
 #muhryzkmgw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #muhryzkmgw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #muhryzkmgw .gt_from_md> :first-child { margin-top: 0; }
 #muhryzkmgw .gt_from_md> :last-child { margin-bottom: 0; }
 #muhryzkmgw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #muhryzkmgw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #muhryzkmgw .gt_indent_1 { text-indent: 5px; }
 #muhryzkmgw .gt_indent_2 { text-indent: calc(5px * 2); }
 #muhryzkmgw .gt_indent_3 { text-indent: calc(5px * 3); }
 #muhryzkmgw .gt_indent_4 { text-indent: calc(5px * 4); }
 #muhryzkmgw .gt_indent_5 { text-indent: calc(5px * 5); }
 #muhryzkmgw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #muhryzkmgw .gt_row_group_first td { border-top-width: 2px; }
 #muhryzkmgw .gt_row_group_first th { border-top-width: 2px; }
 #muhryzkmgw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #muhryzkmgw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muhryzkmgw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muhryzkmgw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #muhryzkmgw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muhryzkmgw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muhryzkmgw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #muhryzkmgw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #muhryzkmgw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muhryzkmgw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muhryzkmgw .gt_left { text-align: left; }
 #muhryzkmgw .gt_center { text-align: center; }
 #muhryzkmgw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #muhryzkmgw .gt_font_normal { font-weight: normal; }
 #muhryzkmgw .gt_font_bold { font-weight: bold; }
 #muhryzkmgw .gt_font_italic { font-style: italic; }
 #muhryzkmgw .gt_super { font-size: 65%; }
 #muhryzkmgw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muhryzkmgw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #muhryzkmgw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muhryzkmgw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muhryzkmgw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #muhryzkmgw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#btihpyslgi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#btihpyslgi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#btihpyslgi p { margin: 0; padding: 0; }
 #btihpyslgi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #btihpyslgi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #btihpyslgi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #btihpyslgi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #btihpyslgi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #btihpyslgi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #btihpyslgi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #btihpyslgi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #btihpyslgi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #btihpyslgi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #btihpyslgi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #btihpyslgi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #btihpyslgi .gt_spanner_row { border-bottom-style: hidden; }
 #btihpyslgi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #btihpyslgi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #btihpyslgi .gt_from_md> :first-child { margin-top: 0; }
 #btihpyslgi .gt_from_md> :last-child { margin-bottom: 0; }
 #btihpyslgi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #btihpyslgi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #btihpyslgi .gt_indent_1 { text-indent: 5px; }
 #btihpyslgi .gt_indent_2 { text-indent: calc(5px * 2); }
 #btihpyslgi .gt_indent_3 { text-indent: calc(5px * 3); }
 #btihpyslgi .gt_indent_4 { text-indent: calc(5px * 4); }
 #btihpyslgi .gt_indent_5 { text-indent: calc(5px * 5); }
 #btihpyslgi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #btihpyslgi .gt_row_group_first td { border-top-width: 2px; }
 #btihpyslgi .gt_row_group_first th { border-top-width: 2px; }
 #btihpyslgi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #btihpyslgi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #btihpyslgi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #btihpyslgi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #btihpyslgi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #btihpyslgi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #btihpyslgi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #btihpyslgi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #btihpyslgi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #btihpyslgi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #btihpyslgi .gt_left { text-align: left; }
 #btihpyslgi .gt_center { text-align: center; }
 #btihpyslgi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #btihpyslgi .gt_font_normal { font-weight: normal; }
 #btihpyslgi .gt_font_bold { font-weight: bold; }
 #btihpyslgi .gt_font_italic { font-style: italic; }
 #btihpyslgi .gt_super { font-size: 65%; }
 #btihpyslgi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #btihpyslgi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #btihpyslgi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #btihpyslgi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #btihpyslgi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #btihpyslgi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#scrkarwxzd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#scrkarwxzd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#scrkarwxzd p { margin: 0; padding: 0; }
 #scrkarwxzd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #scrkarwxzd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #scrkarwxzd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #scrkarwxzd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #scrkarwxzd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #scrkarwxzd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #scrkarwxzd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #scrkarwxzd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #scrkarwxzd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #scrkarwxzd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #scrkarwxzd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #scrkarwxzd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #scrkarwxzd .gt_spanner_row { border-bottom-style: hidden; }
 #scrkarwxzd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #scrkarwxzd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #scrkarwxzd .gt_from_md> :first-child { margin-top: 0; }
 #scrkarwxzd .gt_from_md> :last-child { margin-bottom: 0; }
 #scrkarwxzd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #scrkarwxzd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #scrkarwxzd .gt_indent_1 { text-indent: 5px; }
 #scrkarwxzd .gt_indent_2 { text-indent: calc(5px * 2); }
 #scrkarwxzd .gt_indent_3 { text-indent: calc(5px * 3); }
 #scrkarwxzd .gt_indent_4 { text-indent: calc(5px * 4); }
 #scrkarwxzd .gt_indent_5 { text-indent: calc(5px * 5); }
 #scrkarwxzd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #scrkarwxzd .gt_row_group_first td { border-top-width: 2px; }
 #scrkarwxzd .gt_row_group_first th { border-top-width: 2px; }
 #scrkarwxzd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #scrkarwxzd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #scrkarwxzd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #scrkarwxzd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #scrkarwxzd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #scrkarwxzd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #scrkarwxzd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #scrkarwxzd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #scrkarwxzd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #scrkarwxzd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #scrkarwxzd .gt_left { text-align: left; }
 #scrkarwxzd .gt_center { text-align: center; }
 #scrkarwxzd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #scrkarwxzd .gt_font_normal { font-weight: normal; }
 #scrkarwxzd .gt_font_bold { font-weight: bold; }
 #scrkarwxzd .gt_font_italic { font-style: italic; }
 #scrkarwxzd .gt_super { font-size: 65%; }
 #scrkarwxzd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #scrkarwxzd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #scrkarwxzd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #scrkarwxzd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #scrkarwxzd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #scrkarwxzd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pihrterpxs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pihrterpxs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pihrterpxs p { margin: 0; padding: 0; }
 #pihrterpxs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pihrterpxs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pihrterpxs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pihrterpxs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pihrterpxs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pihrterpxs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pihrterpxs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pihrterpxs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pihrterpxs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pihrterpxs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pihrterpxs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pihrterpxs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pihrterpxs .gt_spanner_row { border-bottom-style: hidden; }
 #pihrterpxs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pihrterpxs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pihrterpxs .gt_from_md> :first-child { margin-top: 0; }
 #pihrterpxs .gt_from_md> :last-child { margin-bottom: 0; }
 #pihrterpxs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pihrterpxs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pihrterpxs .gt_indent_1 { text-indent: 5px; }
 #pihrterpxs .gt_indent_2 { text-indent: calc(5px * 2); }
 #pihrterpxs .gt_indent_3 { text-indent: calc(5px * 3); }
 #pihrterpxs .gt_indent_4 { text-indent: calc(5px * 4); }
 #pihrterpxs .gt_indent_5 { text-indent: calc(5px * 5); }
 #pihrterpxs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pihrterpxs .gt_row_group_first td { border-top-width: 2px; }
 #pihrterpxs .gt_row_group_first th { border-top-width: 2px; }
 #pihrterpxs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pihrterpxs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pihrterpxs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pihrterpxs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pihrterpxs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pihrterpxs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pihrterpxs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pihrterpxs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pihrterpxs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pihrterpxs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pihrterpxs .gt_left { text-align: left; }
 #pihrterpxs .gt_center { text-align: center; }
 #pihrterpxs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pihrterpxs .gt_font_normal { font-weight: normal; }
 #pihrterpxs .gt_font_bold { font-weight: bold; }
 #pihrterpxs .gt_font_italic { font-style: italic; }
 #pihrterpxs .gt_super { font-size: 65%; }
 #pihrterpxs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pihrterpxs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pihrterpxs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pihrterpxs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pihrterpxs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pihrterpxs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wcoxreazwe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wcoxreazwe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wcoxreazwe p { margin: 0; padding: 0; }
 #wcoxreazwe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wcoxreazwe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wcoxreazwe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wcoxreazwe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wcoxreazwe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wcoxreazwe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wcoxreazwe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wcoxreazwe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wcoxreazwe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wcoxreazwe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wcoxreazwe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wcoxreazwe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wcoxreazwe .gt_spanner_row { border-bottom-style: hidden; }
 #wcoxreazwe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wcoxreazwe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wcoxreazwe .gt_from_md> :first-child { margin-top: 0; }
 #wcoxreazwe .gt_from_md> :last-child { margin-bottom: 0; }
 #wcoxreazwe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wcoxreazwe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wcoxreazwe .gt_indent_1 { text-indent: 5px; }
 #wcoxreazwe .gt_indent_2 { text-indent: calc(5px * 2); }
 #wcoxreazwe .gt_indent_3 { text-indent: calc(5px * 3); }
 #wcoxreazwe .gt_indent_4 { text-indent: calc(5px * 4); }
 #wcoxreazwe .gt_indent_5 { text-indent: calc(5px * 5); }
 #wcoxreazwe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wcoxreazwe .gt_row_group_first td { border-top-width: 2px; }
 #wcoxreazwe .gt_row_group_first th { border-top-width: 2px; }
 #wcoxreazwe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wcoxreazwe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wcoxreazwe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wcoxreazwe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wcoxreazwe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wcoxreazwe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wcoxreazwe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wcoxreazwe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wcoxreazwe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wcoxreazwe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wcoxreazwe .gt_left { text-align: left; }
 #wcoxreazwe .gt_center { text-align: center; }
 #wcoxreazwe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wcoxreazwe .gt_font_normal { font-weight: normal; }
 #wcoxreazwe .gt_font_bold { font-weight: bold; }
 #wcoxreazwe .gt_font_italic { font-style: italic; }
 #wcoxreazwe .gt_super { font-size: 65%; }
 #wcoxreazwe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wcoxreazwe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wcoxreazwe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wcoxreazwe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wcoxreazwe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wcoxreazwe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dqfieaeflb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dqfieaeflb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dqfieaeflb p { margin: 0; padding: 0; }
 #dqfieaeflb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dqfieaeflb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dqfieaeflb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dqfieaeflb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dqfieaeflb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dqfieaeflb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dqfieaeflb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dqfieaeflb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dqfieaeflb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dqfieaeflb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dqfieaeflb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dqfieaeflb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dqfieaeflb .gt_spanner_row { border-bottom-style: hidden; }
 #dqfieaeflb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dqfieaeflb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dqfieaeflb .gt_from_md> :first-child { margin-top: 0; }
 #dqfieaeflb .gt_from_md> :last-child { margin-bottom: 0; }
 #dqfieaeflb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dqfieaeflb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dqfieaeflb .gt_indent_1 { text-indent: 5px; }
 #dqfieaeflb .gt_indent_2 { text-indent: calc(5px * 2); }
 #dqfieaeflb .gt_indent_3 { text-indent: calc(5px * 3); }
 #dqfieaeflb .gt_indent_4 { text-indent: calc(5px * 4); }
 #dqfieaeflb .gt_indent_5 { text-indent: calc(5px * 5); }
 #dqfieaeflb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dqfieaeflb .gt_row_group_first td { border-top-width: 2px; }
 #dqfieaeflb .gt_row_group_first th { border-top-width: 2px; }
 #dqfieaeflb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dqfieaeflb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dqfieaeflb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dqfieaeflb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dqfieaeflb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dqfieaeflb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dqfieaeflb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dqfieaeflb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dqfieaeflb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dqfieaeflb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dqfieaeflb .gt_left { text-align: left; }
 #dqfieaeflb .gt_center { text-align: center; }
 #dqfieaeflb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dqfieaeflb .gt_font_normal { font-weight: normal; }
 #dqfieaeflb .gt_font_bold { font-weight: bold; }
 #dqfieaeflb .gt_font_italic { font-style: italic; }
 #dqfieaeflb .gt_super { font-size: 65%; }
 #dqfieaeflb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dqfieaeflb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dqfieaeflb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dqfieaeflb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dqfieaeflb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dqfieaeflb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#yvbjuhpuzz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yvbjuhpuzz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yvbjuhpuzz p { margin: 0; padding: 0; }
 #yvbjuhpuzz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yvbjuhpuzz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yvbjuhpuzz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yvbjuhpuzz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yvbjuhpuzz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yvbjuhpuzz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yvbjuhpuzz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yvbjuhpuzz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yvbjuhpuzz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yvbjuhpuzz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yvbjuhpuzz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yvbjuhpuzz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yvbjuhpuzz .gt_spanner_row { border-bottom-style: hidden; }
 #yvbjuhpuzz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yvbjuhpuzz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yvbjuhpuzz .gt_from_md> :first-child { margin-top: 0; }
 #yvbjuhpuzz .gt_from_md> :last-child { margin-bottom: 0; }
 #yvbjuhpuzz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yvbjuhpuzz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yvbjuhpuzz .gt_indent_1 { text-indent: 5px; }
 #yvbjuhpuzz .gt_indent_2 { text-indent: calc(5px * 2); }
 #yvbjuhpuzz .gt_indent_3 { text-indent: calc(5px * 3); }
 #yvbjuhpuzz .gt_indent_4 { text-indent: calc(5px * 4); }
 #yvbjuhpuzz .gt_indent_5 { text-indent: calc(5px * 5); }
 #yvbjuhpuzz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yvbjuhpuzz .gt_row_group_first td { border-top-width: 2px; }
 #yvbjuhpuzz .gt_row_group_first th { border-top-width: 2px; }
 #yvbjuhpuzz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yvbjuhpuzz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yvbjuhpuzz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yvbjuhpuzz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yvbjuhpuzz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yvbjuhpuzz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yvbjuhpuzz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yvbjuhpuzz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yvbjuhpuzz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yvbjuhpuzz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yvbjuhpuzz .gt_left { text-align: left; }
 #yvbjuhpuzz .gt_center { text-align: center; }
 #yvbjuhpuzz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yvbjuhpuzz .gt_font_normal { font-weight: normal; }
 #yvbjuhpuzz .gt_font_bold { font-weight: bold; }
 #yvbjuhpuzz .gt_font_italic { font-style: italic; }
 #yvbjuhpuzz .gt_super { font-size: 65%; }
 #yvbjuhpuzz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yvbjuhpuzz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yvbjuhpuzz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yvbjuhpuzz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yvbjuhpuzz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yvbjuhpuzz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ussqczrkzu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ussqczrkzu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ussqczrkzu p { margin: 0; padding: 0; }
 #ussqczrkzu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ussqczrkzu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ussqczrkzu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ussqczrkzu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ussqczrkzu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ussqczrkzu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ussqczrkzu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ussqczrkzu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ussqczrkzu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ussqczrkzu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ussqczrkzu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ussqczrkzu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ussqczrkzu .gt_spanner_row { border-bottom-style: hidden; }
 #ussqczrkzu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ussqczrkzu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ussqczrkzu .gt_from_md> :first-child { margin-top: 0; }
 #ussqczrkzu .gt_from_md> :last-child { margin-bottom: 0; }
 #ussqczrkzu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ussqczrkzu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ussqczrkzu .gt_indent_1 { text-indent: 5px; }
 #ussqczrkzu .gt_indent_2 { text-indent: calc(5px * 2); }
 #ussqczrkzu .gt_indent_3 { text-indent: calc(5px * 3); }
 #ussqczrkzu .gt_indent_4 { text-indent: calc(5px * 4); }
 #ussqczrkzu .gt_indent_5 { text-indent: calc(5px * 5); }
 #ussqczrkzu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ussqczrkzu .gt_row_group_first td { border-top-width: 2px; }
 #ussqczrkzu .gt_row_group_first th { border-top-width: 2px; }
 #ussqczrkzu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ussqczrkzu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ussqczrkzu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ussqczrkzu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ussqczrkzu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ussqczrkzu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ussqczrkzu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ussqczrkzu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ussqczrkzu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ussqczrkzu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ussqczrkzu .gt_left { text-align: left; }
 #ussqczrkzu .gt_center { text-align: center; }
 #ussqczrkzu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ussqczrkzu .gt_font_normal { font-weight: normal; }
 #ussqczrkzu .gt_font_bold { font-weight: bold; }
 #ussqczrkzu .gt_font_italic { font-style: italic; }
 #ussqczrkzu .gt_super { font-size: 65%; }
 #ussqczrkzu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ussqczrkzu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ussqczrkzu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ussqczrkzu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ussqczrkzu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ussqczrkzu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
