# Footnotes

Footnotes provide a way to annotate specific cells, columns, or other table parts with additional context without cluttering the main display. **Great Tables** manages footnotes as a system: marks are automatically sequenced, placed consistently, and matched to their explanatory text in the table footer.

Footnotes are best suited for cell-specific or column-specific context that would clutter the main display if placed inline. For information that applies to the entire table, a source note in the footer (via [tab_source_note()](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note)) is usually a better fit because it avoids attaching a mark to any one location. And for systematic column descriptions, such as units or definitions, consider relabeling the column itself so the context is always visible without requiring the reader to look down at the footer.


# A Basic Footnote

Adding a footnote requires two things: the footnote text and a location specifier indicating where the footnote mark should appear. The [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote) method handles both, placing the mark at the targeted location and appending the text to the footer.


``` python
from great_tables import GT, md, loc
from great_tables.data import gibraltar

weather_mini = gibraltar.head(5)[["date", "time", "temp", "humidity", "wind_speed", "pressure"]]

(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Air temperature in degrees Celsius.",
        locations=loc.column_labels(columns="temp")
    )
)
```


<style>
#dcdkcvbpwk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dcdkcvbpwk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dcdkcvbpwk p { margin: 0; padding: 0; }
 #dcdkcvbpwk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dcdkcvbpwk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dcdkcvbpwk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dcdkcvbpwk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dcdkcvbpwk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dcdkcvbpwk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dcdkcvbpwk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dcdkcvbpwk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dcdkcvbpwk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dcdkcvbpwk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dcdkcvbpwk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dcdkcvbpwk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dcdkcvbpwk .gt_spanner_row { border-bottom-style: hidden; }
 #dcdkcvbpwk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dcdkcvbpwk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dcdkcvbpwk .gt_from_md> :first-child { margin-top: 0; }
 #dcdkcvbpwk .gt_from_md> :last-child { margin-bottom: 0; }
 #dcdkcvbpwk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dcdkcvbpwk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dcdkcvbpwk .gt_indent_1 { text-indent: 5px; }
 #dcdkcvbpwk .gt_indent_2 { text-indent: calc(5px * 2); }
 #dcdkcvbpwk .gt_indent_3 { text-indent: calc(5px * 3); }
 #dcdkcvbpwk .gt_indent_4 { text-indent: calc(5px * 4); }
 #dcdkcvbpwk .gt_indent_5 { text-indent: calc(5px * 5); }
 #dcdkcvbpwk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dcdkcvbpwk .gt_row_group_first td { border-top-width: 2px; }
 #dcdkcvbpwk .gt_row_group_first th { border-top-width: 2px; }
 #dcdkcvbpwk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dcdkcvbpwk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dcdkcvbpwk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dcdkcvbpwk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dcdkcvbpwk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dcdkcvbpwk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dcdkcvbpwk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dcdkcvbpwk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dcdkcvbpwk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dcdkcvbpwk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dcdkcvbpwk .gt_left { text-align: left; }
 #dcdkcvbpwk .gt_center { text-align: center; }
 #dcdkcvbpwk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dcdkcvbpwk .gt_font_normal { font-weight: normal; }
 #dcdkcvbpwk .gt_font_bold { font-weight: bold; }
 #dcdkcvbpwk .gt_font_italic { font-style: italic; }
 #dcdkcvbpwk .gt_super { font-size: 65%; }
 #dcdkcvbpwk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dcdkcvbpwk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dcdkcvbpwk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dcdkcvbpwk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dcdkcvbpwk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dcdkcvbpwk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">temp<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">wind_speed</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pressure</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:20</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.77</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Air temperature in degrees Celsius.</td>
</tr>
</tfoot>

</table>


The footnote mark (a superscript number) appears next to the `"temp"` column label, and the corresponding text appears at the bottom of the table.


# Targeting Different Locations

Footnotes can be attached to many different parts of the table. The `locations=` argument accepts any of the `loc` specifiers that support footnotes. Here are some of the most common targets.


## Column Labels

Attaching a footnote to a column label is useful for clarifying units or methodology.


``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Relative humidity, as a value between 0 and 1.",
        locations=loc.column_labels(columns="humidity")
    )
)
```


<style>
#jltqohppbx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jltqohppbx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jltqohppbx p { margin: 0; padding: 0; }
 #jltqohppbx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jltqohppbx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jltqohppbx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jltqohppbx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jltqohppbx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jltqohppbx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jltqohppbx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jltqohppbx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jltqohppbx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jltqohppbx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jltqohppbx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jltqohppbx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jltqohppbx .gt_spanner_row { border-bottom-style: hidden; }
 #jltqohppbx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jltqohppbx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jltqohppbx .gt_from_md> :first-child { margin-top: 0; }
 #jltqohppbx .gt_from_md> :last-child { margin-bottom: 0; }
 #jltqohppbx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jltqohppbx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jltqohppbx .gt_indent_1 { text-indent: 5px; }
 #jltqohppbx .gt_indent_2 { text-indent: calc(5px * 2); }
 #jltqohppbx .gt_indent_3 { text-indent: calc(5px * 3); }
 #jltqohppbx .gt_indent_4 { text-indent: calc(5px * 4); }
 #jltqohppbx .gt_indent_5 { text-indent: calc(5px * 5); }
 #jltqohppbx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jltqohppbx .gt_row_group_first td { border-top-width: 2px; }
 #jltqohppbx .gt_row_group_first th { border-top-width: 2px; }
 #jltqohppbx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jltqohppbx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jltqohppbx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jltqohppbx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jltqohppbx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jltqohppbx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jltqohppbx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jltqohppbx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jltqohppbx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jltqohppbx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jltqohppbx .gt_left { text-align: left; }
 #jltqohppbx .gt_center { text-align: center; }
 #jltqohppbx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jltqohppbx .gt_font_normal { font-weight: normal; }
 #jltqohppbx .gt_font_bold { font-weight: bold; }
 #jltqohppbx .gt_font_italic { font-style: italic; }
 #jltqohppbx .gt_super { font-size: 65%; }
 #jltqohppbx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jltqohppbx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jltqohppbx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jltqohppbx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jltqohppbx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jltqohppbx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">temp</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">humidity<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">wind_speed</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pressure</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:20</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.77</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Relative humidity, as a value between 0 and 1.</td>
</tr>
</tfoot>

</table>


## Body Cells

You can annotate specific data cells by targeting them with [loc.body()](../reference/loc.body.md#great_tables.loc.body).


``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Lowest temperature in this sample.",
        locations=loc.body(columns="temp", rows=[2])
    )
)
```


<style>
#gfrshgokli table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gfrshgokli thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gfrshgokli p { margin: 0; padding: 0; }
 #gfrshgokli .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gfrshgokli .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gfrshgokli .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gfrshgokli .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gfrshgokli .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gfrshgokli .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gfrshgokli .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gfrshgokli .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gfrshgokli .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gfrshgokli .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gfrshgokli .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gfrshgokli .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gfrshgokli .gt_spanner_row { border-bottom-style: hidden; }
 #gfrshgokli .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gfrshgokli .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gfrshgokli .gt_from_md> :first-child { margin-top: 0; }
 #gfrshgokli .gt_from_md> :last-child { margin-bottom: 0; }
 #gfrshgokli .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gfrshgokli .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gfrshgokli .gt_indent_1 { text-indent: 5px; }
 #gfrshgokli .gt_indent_2 { text-indent: calc(5px * 2); }
 #gfrshgokli .gt_indent_3 { text-indent: calc(5px * 3); }
 #gfrshgokli .gt_indent_4 { text-indent: calc(5px * 4); }
 #gfrshgokli .gt_indent_5 { text-indent: calc(5px * 5); }
 #gfrshgokli .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gfrshgokli .gt_row_group_first td { border-top-width: 2px; }
 #gfrshgokli .gt_row_group_first th { border-top-width: 2px; }
 #gfrshgokli .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gfrshgokli .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gfrshgokli .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gfrshgokli .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gfrshgokli .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gfrshgokli .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gfrshgokli .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gfrshgokli .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gfrshgokli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gfrshgokli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gfrshgokli .gt_left { text-align: left; }
 #gfrshgokli .gt_center { text-align: center; }
 #gfrshgokli .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gfrshgokli .gt_font_normal { font-weight: normal; }
 #gfrshgokli .gt_font_bold { font-weight: bold; }
 #gfrshgokli .gt_font_italic { font-style: italic; }
 #gfrshgokli .gt_super { font-size: 65%; }
 #gfrshgokli .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gfrshgokli .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gfrshgokli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gfrshgokli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gfrshgokli .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gfrshgokli .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">temp</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">wind_speed</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pressure</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:20</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 17.8</td>
<td class="gt_row gt_right">0.77</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Lowest temperature in this sample.</td>
</tr>
</tfoot>

</table>


## The Title or Subtitle

Footnotes on the table header can provide methodological notes or data source context.


``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Data collected at the airport's weather station, 5 m above mean sea level.",
        locations=loc.title()
    )
)
```


<style>
#afqpqrjlny table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#afqpqrjlny thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#afqpqrjlny p { margin: 0; padding: 0; }
 #afqpqrjlny .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #afqpqrjlny .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #afqpqrjlny .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #afqpqrjlny .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #afqpqrjlny .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #afqpqrjlny .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #afqpqrjlny .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #afqpqrjlny .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #afqpqrjlny .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #afqpqrjlny .gt_column_spanner_outer:first-child { padding-left: 0; }
 #afqpqrjlny .gt_column_spanner_outer:last-child { padding-right: 0; }
 #afqpqrjlny .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #afqpqrjlny .gt_spanner_row { border-bottom-style: hidden; }
 #afqpqrjlny .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #afqpqrjlny .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #afqpqrjlny .gt_from_md> :first-child { margin-top: 0; }
 #afqpqrjlny .gt_from_md> :last-child { margin-bottom: 0; }
 #afqpqrjlny .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #afqpqrjlny .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #afqpqrjlny .gt_indent_1 { text-indent: 5px; }
 #afqpqrjlny .gt_indent_2 { text-indent: calc(5px * 2); }
 #afqpqrjlny .gt_indent_3 { text-indent: calc(5px * 3); }
 #afqpqrjlny .gt_indent_4 { text-indent: calc(5px * 4); }
 #afqpqrjlny .gt_indent_5 { text-indent: calc(5px * 5); }
 #afqpqrjlny .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #afqpqrjlny .gt_row_group_first td { border-top-width: 2px; }
 #afqpqrjlny .gt_row_group_first th { border-top-width: 2px; }
 #afqpqrjlny .gt_striped { color: #333333; background-color: #F4F4F4; }
 #afqpqrjlny .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #afqpqrjlny .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #afqpqrjlny .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #afqpqrjlny .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #afqpqrjlny .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #afqpqrjlny .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #afqpqrjlny .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #afqpqrjlny .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #afqpqrjlny .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #afqpqrjlny .gt_left { text-align: left; }
 #afqpqrjlny .gt_center { text-align: center; }
 #afqpqrjlny .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #afqpqrjlny .gt_font_normal { font-weight: normal; }
 #afqpqrjlny .gt_font_bold { font-weight: bold; }
 #afqpqrjlny .gt_font_italic { font-style: italic; }
 #afqpqrjlny .gt_super { font-size: 65%; }
 #afqpqrjlny .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #afqpqrjlny .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #afqpqrjlny .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #afqpqrjlny .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #afqpqrjlny .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #afqpqrjlny .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">temp</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">wind_speed</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pressure</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:20</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.77</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Data collected at the airport's weather station, 5 m above mean sea level.</td>
</tr>
</tfoot>

</table>


# Multiple Footnotes

You can add multiple footnotes to a single table. Each call to [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote) creates a new footnote with its own sequenced mark. The marks are numbered in the order they appear in the table (reading left-to-right, top-to-bottom).


``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Air temperature in degrees Celsius.",
        locations=loc.column_labels(columns="temp")
    )
    .tab_footnote(
        footnote="Atmospheric pressure in hectopascals.",
        locations=loc.column_labels(columns="pressure")
    )
    .tab_footnote(
        footnote="Highest wind speed in this sample.",
        locations=loc.body(columns="wind_speed", rows=[1])
    )
)
```


<style>
#anxmvmrdza table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#anxmvmrdza thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#anxmvmrdza p { margin: 0; padding: 0; }
 #anxmvmrdza .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #anxmvmrdza .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #anxmvmrdza .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #anxmvmrdza .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #anxmvmrdza .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #anxmvmrdza .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #anxmvmrdza .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #anxmvmrdza .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #anxmvmrdza .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #anxmvmrdza .gt_column_spanner_outer:first-child { padding-left: 0; }
 #anxmvmrdza .gt_column_spanner_outer:last-child { padding-right: 0; }
 #anxmvmrdza .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #anxmvmrdza .gt_spanner_row { border-bottom-style: hidden; }
 #anxmvmrdza .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #anxmvmrdza .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #anxmvmrdza .gt_from_md> :first-child { margin-top: 0; }
 #anxmvmrdza .gt_from_md> :last-child { margin-bottom: 0; }
 #anxmvmrdza .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #anxmvmrdza .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #anxmvmrdza .gt_indent_1 { text-indent: 5px; }
 #anxmvmrdza .gt_indent_2 { text-indent: calc(5px * 2); }
 #anxmvmrdza .gt_indent_3 { text-indent: calc(5px * 3); }
 #anxmvmrdza .gt_indent_4 { text-indent: calc(5px * 4); }
 #anxmvmrdza .gt_indent_5 { text-indent: calc(5px * 5); }
 #anxmvmrdza .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #anxmvmrdza .gt_row_group_first td { border-top-width: 2px; }
 #anxmvmrdza .gt_row_group_first th { border-top-width: 2px; }
 #anxmvmrdza .gt_striped { color: #333333; background-color: #F4F4F4; }
 #anxmvmrdza .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #anxmvmrdza .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #anxmvmrdza .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #anxmvmrdza .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #anxmvmrdza .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #anxmvmrdza .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #anxmvmrdza .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #anxmvmrdza .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #anxmvmrdza .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #anxmvmrdza .gt_left { text-align: left; }
 #anxmvmrdza .gt_center { text-align: center; }
 #anxmvmrdza .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #anxmvmrdza .gt_font_normal { font-weight: normal; }
 #anxmvmrdza .gt_font_bold { font-weight: bold; }
 #anxmvmrdza .gt_font_italic { font-style: italic; }
 #anxmvmrdza .gt_super { font-size: 65%; }
 #anxmvmrdza .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #anxmvmrdza .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #anxmvmrdza .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #anxmvmrdza .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #anxmvmrdza .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #anxmvmrdza .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">temp<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">wind_speed</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pressure<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">2</span></th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">3</span> 7.2</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:20</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.77</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Air temperature in degrees Celsius.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">2</span> Atmospheric pressure in hectopascals.</td>
</tr>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">3</span> Highest wind speed in this sample.</td>
</tr>
</tfoot>

</table>


Three footnote marks are placed in the table, and three corresponding notes appear in the footer, each with its sequential number.

While you can add many footnotes to a single table, use restraint. More than three or four footnotes can overwhelm the reader and make the footer itself difficult to navigate. If you find yourself adding footnotes to most cells, consider whether the information would be better conveyed through more descriptive column labels, a subtitle, or a separate explanatory paragraph outside the table.


# Footnotes Without a Mark

If you want to include explanatory text in the footer without attaching a mark to any cell, omit the `locations=` argument (or set it to `None`).


``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(footnote="All observations are from Gibraltar Airport, May 2023.")
)
```


<style>
#vvfvqasbpr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vvfvqasbpr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vvfvqasbpr p { margin: 0; padding: 0; }
 #vvfvqasbpr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vvfvqasbpr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vvfvqasbpr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vvfvqasbpr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vvfvqasbpr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vvfvqasbpr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vvfvqasbpr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vvfvqasbpr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vvfvqasbpr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vvfvqasbpr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vvfvqasbpr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vvfvqasbpr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vvfvqasbpr .gt_spanner_row { border-bottom-style: hidden; }
 #vvfvqasbpr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vvfvqasbpr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vvfvqasbpr .gt_from_md> :first-child { margin-top: 0; }
 #vvfvqasbpr .gt_from_md> :last-child { margin-bottom: 0; }
 #vvfvqasbpr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vvfvqasbpr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vvfvqasbpr .gt_indent_1 { text-indent: 5px; }
 #vvfvqasbpr .gt_indent_2 { text-indent: calc(5px * 2); }
 #vvfvqasbpr .gt_indent_3 { text-indent: calc(5px * 3); }
 #vvfvqasbpr .gt_indent_4 { text-indent: calc(5px * 4); }
 #vvfvqasbpr .gt_indent_5 { text-indent: calc(5px * 5); }
 #vvfvqasbpr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vvfvqasbpr .gt_row_group_first td { border-top-width: 2px; }
 #vvfvqasbpr .gt_row_group_first th { border-top-width: 2px; }
 #vvfvqasbpr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vvfvqasbpr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vvfvqasbpr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vvfvqasbpr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vvfvqasbpr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vvfvqasbpr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vvfvqasbpr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vvfvqasbpr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vvfvqasbpr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vvfvqasbpr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vvfvqasbpr .gt_left { text-align: left; }
 #vvfvqasbpr .gt_center { text-align: center; }
 #vvfvqasbpr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vvfvqasbpr .gt_font_normal { font-weight: normal; }
 #vvfvqasbpr .gt_font_bold { font-weight: bold; }
 #vvfvqasbpr .gt_font_italic { font-style: italic; }
 #vvfvqasbpr .gt_super { font-size: 65%; }
 #vvfvqasbpr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vvfvqasbpr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vvfvqasbpr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vvfvqasbpr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vvfvqasbpr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vvfvqasbpr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">temp</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">wind_speed</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pressure</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:20</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.77</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote">All observations are from Gibraltar Airport, May 2023.</td>
</tr>
</tfoot>

</table>


This is useful for general notes that apply to the entire table rather than to a specific cell or label. Markless footnotes work well for disclaimers, methodological notes, or data-source attributions that apply broadly rather than to any single cell. Because they carry no superscript mark, they read as supplementary context for the table as a whole.


# Controlling Mark Placement

The `placement=` argument determines where the footnote mark appears relative to the cell content. The options are `"auto"` (the default), `"left"`, and `"right"`.


``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote="Wind speed in meters per second.",
        locations=loc.column_labels(columns="wind_speed"),
        placement="left"
    )
)
```


<style>
#qwmvnbjjwz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qwmvnbjjwz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qwmvnbjjwz p { margin: 0; padding: 0; }
 #qwmvnbjjwz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qwmvnbjjwz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qwmvnbjjwz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qwmvnbjjwz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qwmvnbjjwz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qwmvnbjjwz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwmvnbjjwz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qwmvnbjjwz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qwmvnbjjwz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qwmvnbjjwz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qwmvnbjjwz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qwmvnbjjwz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qwmvnbjjwz .gt_spanner_row { border-bottom-style: hidden; }
 #qwmvnbjjwz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qwmvnbjjwz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qwmvnbjjwz .gt_from_md> :first-child { margin-top: 0; }
 #qwmvnbjjwz .gt_from_md> :last-child { margin-bottom: 0; }
 #qwmvnbjjwz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qwmvnbjjwz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qwmvnbjjwz .gt_indent_1 { text-indent: 5px; }
 #qwmvnbjjwz .gt_indent_2 { text-indent: calc(5px * 2); }
 #qwmvnbjjwz .gt_indent_3 { text-indent: calc(5px * 3); }
 #qwmvnbjjwz .gt_indent_4 { text-indent: calc(5px * 4); }
 #qwmvnbjjwz .gt_indent_5 { text-indent: calc(5px * 5); }
 #qwmvnbjjwz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qwmvnbjjwz .gt_row_group_first td { border-top-width: 2px; }
 #qwmvnbjjwz .gt_row_group_first th { border-top-width: 2px; }
 #qwmvnbjjwz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qwmvnbjjwz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwmvnbjjwz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qwmvnbjjwz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qwmvnbjjwz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwmvnbjjwz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qwmvnbjjwz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qwmvnbjjwz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qwmvnbjjwz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwmvnbjjwz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qwmvnbjjwz .gt_left { text-align: left; }
 #qwmvnbjjwz .gt_center { text-align: center; }
 #qwmvnbjjwz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qwmvnbjjwz .gt_font_normal { font-weight: normal; }
 #qwmvnbjjwz .gt_font_bold { font-weight: bold; }
 #qwmvnbjjwz .gt_font_italic { font-style: italic; }
 #qwmvnbjjwz .gt_super { font-size: 65%; }
 #qwmvnbjjwz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwmvnbjjwz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qwmvnbjjwz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwmvnbjjwz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qwmvnbjjwz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qwmvnbjjwz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">temp</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> wind_speed</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pressure</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:20</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.77</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Wind speed in meters per second.</td>
</tr>
</tfoot>

</table>


With `placement="left"`, the footnote mark appears before the cell text rather than after it.


# Using Markdown in Footnotes

Footnote text supports Markdown formatting through the [md()](../reference/md.md#great_tables.md) helper function. This lets you include emphasis, links, or other inline formatting in your footnotes.


``` python
(
    GT(weather_mini)
    .tab_header(title="Weather at Gibraltar Airport", subtitle="Observations on May 1, 2023")
    .tab_footnote(
        footnote=md("Observations from the *Gibraltar Airport Station* (GIB)."),
        locations=loc.title()
    )
)
```


<style>
#unyzyuygmc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#unyzyuygmc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#unyzyuygmc p { margin: 0; padding: 0; }
 #unyzyuygmc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #unyzyuygmc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #unyzyuygmc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #unyzyuygmc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #unyzyuygmc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #unyzyuygmc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #unyzyuygmc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #unyzyuygmc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #unyzyuygmc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #unyzyuygmc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #unyzyuygmc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #unyzyuygmc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #unyzyuygmc .gt_spanner_row { border-bottom-style: hidden; }
 #unyzyuygmc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #unyzyuygmc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #unyzyuygmc .gt_from_md> :first-child { margin-top: 0; }
 #unyzyuygmc .gt_from_md> :last-child { margin-bottom: 0; }
 #unyzyuygmc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #unyzyuygmc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #unyzyuygmc .gt_indent_1 { text-indent: 5px; }
 #unyzyuygmc .gt_indent_2 { text-indent: calc(5px * 2); }
 #unyzyuygmc .gt_indent_3 { text-indent: calc(5px * 3); }
 #unyzyuygmc .gt_indent_4 { text-indent: calc(5px * 4); }
 #unyzyuygmc .gt_indent_5 { text-indent: calc(5px * 5); }
 #unyzyuygmc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #unyzyuygmc .gt_row_group_first td { border-top-width: 2px; }
 #unyzyuygmc .gt_row_group_first th { border-top-width: 2px; }
 #unyzyuygmc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #unyzyuygmc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #unyzyuygmc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #unyzyuygmc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #unyzyuygmc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #unyzyuygmc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #unyzyuygmc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #unyzyuygmc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #unyzyuygmc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #unyzyuygmc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #unyzyuygmc .gt_left { text-align: left; }
 #unyzyuygmc .gt_center { text-align: center; }
 #unyzyuygmc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #unyzyuygmc .gt_font_normal { font-weight: normal; }
 #unyzyuygmc .gt_font_bold { font-weight: bold; }
 #unyzyuygmc .gt_font_italic { font-style: italic; }
 #unyzyuygmc .gt_super { font-size: 65%; }
 #unyzyuygmc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #unyzyuygmc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #unyzyuygmc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #unyzyuygmc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #unyzyuygmc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #unyzyuygmc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">temp</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">wind_speed</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pressure</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:20</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.77</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Observations from the <em>Gibraltar Airport Station</em> (GIB).</td>
</tr>
</tfoot>

</table>


Footnotes are a subtle but important tool for building informative tables. They let you add precision and context where it matters most, keeping the main table body clean while ensuring readers have access to the details they need. The automatic sequencing and placement system means you can focus on content rather than managing mark numbers manually.
