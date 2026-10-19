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
#okvvepuqju table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#okvvepuqju thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#okvvepuqju p { margin: 0; padding: 0; }
 #okvvepuqju .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #okvvepuqju .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #okvvepuqju .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #okvvepuqju .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #okvvepuqju .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #okvvepuqju .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #okvvepuqju .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #okvvepuqju .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #okvvepuqju .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #okvvepuqju .gt_column_spanner_outer:first-child { padding-left: 0; }
 #okvvepuqju .gt_column_spanner_outer:last-child { padding-right: 0; }
 #okvvepuqju .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #okvvepuqju .gt_spanner_row { border-bottom-style: hidden; }
 #okvvepuqju .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #okvvepuqju .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #okvvepuqju .gt_from_md> :first-child { margin-top: 0; }
 #okvvepuqju .gt_from_md> :last-child { margin-bottom: 0; }
 #okvvepuqju .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #okvvepuqju .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #okvvepuqju .gt_indent_1 { text-indent: 5px; }
 #okvvepuqju .gt_indent_2 { text-indent: calc(5px * 2); }
 #okvvepuqju .gt_indent_3 { text-indent: calc(5px * 3); }
 #okvvepuqju .gt_indent_4 { text-indent: calc(5px * 4); }
 #okvvepuqju .gt_indent_5 { text-indent: calc(5px * 5); }
 #okvvepuqju .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #okvvepuqju .gt_row_group_first td { border-top-width: 2px; }
 #okvvepuqju .gt_row_group_first th { border-top-width: 2px; }
 #okvvepuqju .gt_striped { color: #333333; background-color: #F4F4F4; }
 #okvvepuqju .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #okvvepuqju .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #okvvepuqju .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #okvvepuqju .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #okvvepuqju .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #okvvepuqju .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #okvvepuqju .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #okvvepuqju .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #okvvepuqju .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #okvvepuqju .gt_left { text-align: left; }
 #okvvepuqju .gt_center { text-align: center; }
 #okvvepuqju .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #okvvepuqju .gt_font_normal { font-weight: normal; }
 #okvvepuqju .gt_font_bold { font-weight: bold; }
 #okvvepuqju .gt_font_italic { font-style: italic; }
 #okvvepuqju .gt_super { font-size: 65%; }
 #okvvepuqju .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #okvvepuqju .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #okvvepuqju .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #okvvepuqju .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #okvvepuqju .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #okvvepuqju .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
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
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">7.2</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:20</td>
<td class="gt_row gt_right" headers="temp">17.8</td>
<td class="gt_row gt_right" headers="humidity">0.77</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">02:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
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
#obmimjorgz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#obmimjorgz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#obmimjorgz p { margin: 0; padding: 0; }
 #obmimjorgz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #obmimjorgz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #obmimjorgz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #obmimjorgz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #obmimjorgz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #obmimjorgz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #obmimjorgz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #obmimjorgz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #obmimjorgz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #obmimjorgz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #obmimjorgz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #obmimjorgz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #obmimjorgz .gt_spanner_row { border-bottom-style: hidden; }
 #obmimjorgz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #obmimjorgz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #obmimjorgz .gt_from_md> :first-child { margin-top: 0; }
 #obmimjorgz .gt_from_md> :last-child { margin-bottom: 0; }
 #obmimjorgz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #obmimjorgz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #obmimjorgz .gt_indent_1 { text-indent: 5px; }
 #obmimjorgz .gt_indent_2 { text-indent: calc(5px * 2); }
 #obmimjorgz .gt_indent_3 { text-indent: calc(5px * 3); }
 #obmimjorgz .gt_indent_4 { text-indent: calc(5px * 4); }
 #obmimjorgz .gt_indent_5 { text-indent: calc(5px * 5); }
 #obmimjorgz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #obmimjorgz .gt_row_group_first td { border-top-width: 2px; }
 #obmimjorgz .gt_row_group_first th { border-top-width: 2px; }
 #obmimjorgz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #obmimjorgz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #obmimjorgz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #obmimjorgz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #obmimjorgz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #obmimjorgz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #obmimjorgz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #obmimjorgz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #obmimjorgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #obmimjorgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #obmimjorgz .gt_left { text-align: left; }
 #obmimjorgz .gt_center { text-align: center; }
 #obmimjorgz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #obmimjorgz .gt_font_normal { font-weight: normal; }
 #obmimjorgz .gt_font_bold { font-weight: bold; }
 #obmimjorgz .gt_font_italic { font-style: italic; }
 #obmimjorgz .gt_super { font-size: 65%; }
 #obmimjorgz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #obmimjorgz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #obmimjorgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #obmimjorgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #obmimjorgz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #obmimjorgz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
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
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">7.2</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:20</td>
<td class="gt_row gt_right" headers="temp">17.8</td>
<td class="gt_row gt_right" headers="humidity">0.77</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">02:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
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
#webinlxjgw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#webinlxjgw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#webinlxjgw p { margin: 0; padding: 0; }
 #webinlxjgw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #webinlxjgw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #webinlxjgw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #webinlxjgw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #webinlxjgw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #webinlxjgw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #webinlxjgw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #webinlxjgw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #webinlxjgw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #webinlxjgw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #webinlxjgw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #webinlxjgw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #webinlxjgw .gt_spanner_row { border-bottom-style: hidden; }
 #webinlxjgw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #webinlxjgw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #webinlxjgw .gt_from_md> :first-child { margin-top: 0; }
 #webinlxjgw .gt_from_md> :last-child { margin-bottom: 0; }
 #webinlxjgw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #webinlxjgw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #webinlxjgw .gt_indent_1 { text-indent: 5px; }
 #webinlxjgw .gt_indent_2 { text-indent: calc(5px * 2); }
 #webinlxjgw .gt_indent_3 { text-indent: calc(5px * 3); }
 #webinlxjgw .gt_indent_4 { text-indent: calc(5px * 4); }
 #webinlxjgw .gt_indent_5 { text-indent: calc(5px * 5); }
 #webinlxjgw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #webinlxjgw .gt_row_group_first td { border-top-width: 2px; }
 #webinlxjgw .gt_row_group_first th { border-top-width: 2px; }
 #webinlxjgw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #webinlxjgw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #webinlxjgw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #webinlxjgw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #webinlxjgw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #webinlxjgw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #webinlxjgw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #webinlxjgw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #webinlxjgw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #webinlxjgw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #webinlxjgw .gt_left { text-align: left; }
 #webinlxjgw .gt_center { text-align: center; }
 #webinlxjgw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #webinlxjgw .gt_font_normal { font-weight: normal; }
 #webinlxjgw .gt_font_bold { font-weight: bold; }
 #webinlxjgw .gt_font_italic { font-style: italic; }
 #webinlxjgw .gt_super { font-size: 65%; }
 #webinlxjgw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #webinlxjgw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #webinlxjgw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #webinlxjgw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #webinlxjgw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #webinlxjgw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
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
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">7.2</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:20</td>
<td class="gt_row gt_right" headers="temp"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> 17.8</td>
<td class="gt_row gt_right" headers="humidity">0.77</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">02:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
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
#kjptdguciw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kjptdguciw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kjptdguciw p { margin: 0; padding: 0; }
 #kjptdguciw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kjptdguciw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kjptdguciw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kjptdguciw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kjptdguciw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kjptdguciw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kjptdguciw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kjptdguciw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kjptdguciw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kjptdguciw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kjptdguciw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kjptdguciw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kjptdguciw .gt_spanner_row { border-bottom-style: hidden; }
 #kjptdguciw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kjptdguciw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kjptdguciw .gt_from_md> :first-child { margin-top: 0; }
 #kjptdguciw .gt_from_md> :last-child { margin-bottom: 0; }
 #kjptdguciw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kjptdguciw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kjptdguciw .gt_indent_1 { text-indent: 5px; }
 #kjptdguciw .gt_indent_2 { text-indent: calc(5px * 2); }
 #kjptdguciw .gt_indent_3 { text-indent: calc(5px * 3); }
 #kjptdguciw .gt_indent_4 { text-indent: calc(5px * 4); }
 #kjptdguciw .gt_indent_5 { text-indent: calc(5px * 5); }
 #kjptdguciw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kjptdguciw .gt_row_group_first td { border-top-width: 2px; }
 #kjptdguciw .gt_row_group_first th { border-top-width: 2px; }
 #kjptdguciw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kjptdguciw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kjptdguciw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kjptdguciw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kjptdguciw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kjptdguciw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kjptdguciw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kjptdguciw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kjptdguciw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kjptdguciw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kjptdguciw .gt_left { text-align: left; }
 #kjptdguciw .gt_center { text-align: center; }
 #kjptdguciw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kjptdguciw .gt_font_normal { font-weight: normal; }
 #kjptdguciw .gt_font_bold { font-weight: bold; }
 #kjptdguciw .gt_font_italic { font-style: italic; }
 #kjptdguciw .gt_super { font-size: 65%; }
 #kjptdguciw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kjptdguciw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kjptdguciw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kjptdguciw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kjptdguciw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kjptdguciw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
</tr>
<tr class="gt_heading">
<th colspan="6" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
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
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">7.2</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:20</td>
<td class="gt_row gt_right" headers="temp">17.8</td>
<td class="gt_row gt_right" headers="humidity">0.77</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">02:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
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
#bbpisaidsg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bbpisaidsg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bbpisaidsg p { margin: 0; padding: 0; }
 #bbpisaidsg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bbpisaidsg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bbpisaidsg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bbpisaidsg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bbpisaidsg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bbpisaidsg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bbpisaidsg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bbpisaidsg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bbpisaidsg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bbpisaidsg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bbpisaidsg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bbpisaidsg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bbpisaidsg .gt_spanner_row { border-bottom-style: hidden; }
 #bbpisaidsg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bbpisaidsg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bbpisaidsg .gt_from_md> :first-child { margin-top: 0; }
 #bbpisaidsg .gt_from_md> :last-child { margin-bottom: 0; }
 #bbpisaidsg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bbpisaidsg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bbpisaidsg .gt_indent_1 { text-indent: 5px; }
 #bbpisaidsg .gt_indent_2 { text-indent: calc(5px * 2); }
 #bbpisaidsg .gt_indent_3 { text-indent: calc(5px * 3); }
 #bbpisaidsg .gt_indent_4 { text-indent: calc(5px * 4); }
 #bbpisaidsg .gt_indent_5 { text-indent: calc(5px * 5); }
 #bbpisaidsg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bbpisaidsg .gt_row_group_first td { border-top-width: 2px; }
 #bbpisaidsg .gt_row_group_first th { border-top-width: 2px; }
 #bbpisaidsg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bbpisaidsg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bbpisaidsg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bbpisaidsg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bbpisaidsg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bbpisaidsg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bbpisaidsg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bbpisaidsg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bbpisaidsg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bbpisaidsg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bbpisaidsg .gt_left { text-align: left; }
 #bbpisaidsg .gt_center { text-align: center; }
 #bbpisaidsg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bbpisaidsg .gt_font_normal { font-weight: normal; }
 #bbpisaidsg .gt_font_bold { font-weight: bold; }
 #bbpisaidsg .gt_font_italic { font-style: italic; }
 #bbpisaidsg .gt_super { font-size: 65%; }
 #bbpisaidsg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bbpisaidsg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bbpisaidsg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bbpisaidsg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bbpisaidsg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bbpisaidsg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
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
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">3</span> 7.2</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:20</td>
<td class="gt_row gt_right" headers="temp">17.8</td>
<td class="gt_row gt_right" headers="humidity">0.77</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">02:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
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
#xxbjebabfn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xxbjebabfn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xxbjebabfn p { margin: 0; padding: 0; }
 #xxbjebabfn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xxbjebabfn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xxbjebabfn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xxbjebabfn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xxbjebabfn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xxbjebabfn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xxbjebabfn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xxbjebabfn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xxbjebabfn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xxbjebabfn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xxbjebabfn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xxbjebabfn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xxbjebabfn .gt_spanner_row { border-bottom-style: hidden; }
 #xxbjebabfn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xxbjebabfn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xxbjebabfn .gt_from_md> :first-child { margin-top: 0; }
 #xxbjebabfn .gt_from_md> :last-child { margin-bottom: 0; }
 #xxbjebabfn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xxbjebabfn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xxbjebabfn .gt_indent_1 { text-indent: 5px; }
 #xxbjebabfn .gt_indent_2 { text-indent: calc(5px * 2); }
 #xxbjebabfn .gt_indent_3 { text-indent: calc(5px * 3); }
 #xxbjebabfn .gt_indent_4 { text-indent: calc(5px * 4); }
 #xxbjebabfn .gt_indent_5 { text-indent: calc(5px * 5); }
 #xxbjebabfn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xxbjebabfn .gt_row_group_first td { border-top-width: 2px; }
 #xxbjebabfn .gt_row_group_first th { border-top-width: 2px; }
 #xxbjebabfn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xxbjebabfn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xxbjebabfn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xxbjebabfn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xxbjebabfn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xxbjebabfn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xxbjebabfn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xxbjebabfn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xxbjebabfn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xxbjebabfn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xxbjebabfn .gt_left { text-align: left; }
 #xxbjebabfn .gt_center { text-align: center; }
 #xxbjebabfn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xxbjebabfn .gt_font_normal { font-weight: normal; }
 #xxbjebabfn .gt_font_bold { font-weight: bold; }
 #xxbjebabfn .gt_font_italic { font-style: italic; }
 #xxbjebabfn .gt_super { font-size: 65%; }
 #xxbjebabfn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xxbjebabfn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xxbjebabfn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xxbjebabfn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xxbjebabfn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xxbjebabfn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
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
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">7.2</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:20</td>
<td class="gt_row gt_right" headers="temp">17.8</td>
<td class="gt_row gt_right" headers="humidity">0.77</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">02:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
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
#dhjdttrmcm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dhjdttrmcm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dhjdttrmcm p { margin: 0; padding: 0; }
 #dhjdttrmcm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dhjdttrmcm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dhjdttrmcm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dhjdttrmcm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dhjdttrmcm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dhjdttrmcm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dhjdttrmcm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dhjdttrmcm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dhjdttrmcm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dhjdttrmcm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dhjdttrmcm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dhjdttrmcm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dhjdttrmcm .gt_spanner_row { border-bottom-style: hidden; }
 #dhjdttrmcm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dhjdttrmcm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dhjdttrmcm .gt_from_md> :first-child { margin-top: 0; }
 #dhjdttrmcm .gt_from_md> :last-child { margin-bottom: 0; }
 #dhjdttrmcm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dhjdttrmcm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dhjdttrmcm .gt_indent_1 { text-indent: 5px; }
 #dhjdttrmcm .gt_indent_2 { text-indent: calc(5px * 2); }
 #dhjdttrmcm .gt_indent_3 { text-indent: calc(5px * 3); }
 #dhjdttrmcm .gt_indent_4 { text-indent: calc(5px * 4); }
 #dhjdttrmcm .gt_indent_5 { text-indent: calc(5px * 5); }
 #dhjdttrmcm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dhjdttrmcm .gt_row_group_first td { border-top-width: 2px; }
 #dhjdttrmcm .gt_row_group_first th { border-top-width: 2px; }
 #dhjdttrmcm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dhjdttrmcm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dhjdttrmcm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dhjdttrmcm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dhjdttrmcm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dhjdttrmcm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dhjdttrmcm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dhjdttrmcm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dhjdttrmcm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dhjdttrmcm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dhjdttrmcm .gt_left { text-align: left; }
 #dhjdttrmcm .gt_center { text-align: center; }
 #dhjdttrmcm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dhjdttrmcm .gt_font_normal { font-weight: normal; }
 #dhjdttrmcm .gt_font_bold { font-weight: bold; }
 #dhjdttrmcm .gt_font_italic { font-style: italic; }
 #dhjdttrmcm .gt_super { font-size: 65%; }
 #dhjdttrmcm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dhjdttrmcm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dhjdttrmcm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dhjdttrmcm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dhjdttrmcm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dhjdttrmcm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
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
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">7.2</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:20</td>
<td class="gt_row gt_right" headers="temp">17.8</td>
<td class="gt_row gt_right" headers="humidity">0.77</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">02:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
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
#hamitutpzx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hamitutpzx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hamitutpzx p { margin: 0; padding: 0; }
 #hamitutpzx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hamitutpzx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hamitutpzx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hamitutpzx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hamitutpzx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hamitutpzx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hamitutpzx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hamitutpzx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hamitutpzx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hamitutpzx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hamitutpzx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hamitutpzx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hamitutpzx .gt_spanner_row { border-bottom-style: hidden; }
 #hamitutpzx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hamitutpzx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hamitutpzx .gt_from_md> :first-child { margin-top: 0; }
 #hamitutpzx .gt_from_md> :last-child { margin-bottom: 0; }
 #hamitutpzx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hamitutpzx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hamitutpzx .gt_indent_1 { text-indent: 5px; }
 #hamitutpzx .gt_indent_2 { text-indent: calc(5px * 2); }
 #hamitutpzx .gt_indent_3 { text-indent: calc(5px * 3); }
 #hamitutpzx .gt_indent_4 { text-indent: calc(5px * 4); }
 #hamitutpzx .gt_indent_5 { text-indent: calc(5px * 5); }
 #hamitutpzx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hamitutpzx .gt_row_group_first td { border-top-width: 2px; }
 #hamitutpzx .gt_row_group_first th { border-top-width: 2px; }
 #hamitutpzx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hamitutpzx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hamitutpzx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hamitutpzx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hamitutpzx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hamitutpzx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hamitutpzx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hamitutpzx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hamitutpzx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hamitutpzx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hamitutpzx .gt_left { text-align: left; }
 #hamitutpzx .gt_center { text-align: center; }
 #hamitutpzx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hamitutpzx .gt_font_normal { font-weight: normal; }
 #hamitutpzx .gt_font_bold { font-weight: bold; }
 #hamitutpzx .gt_font_italic { font-style: italic; }
 #hamitutpzx .gt_super { font-size: 65%; }
 #hamitutpzx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hamitutpzx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hamitutpzx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hamitutpzx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hamitutpzx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hamitutpzx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span></th>
</tr>
<tr class="gt_heading">
<th colspan="6" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations on May 1, 2023</th>
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
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">00:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">7.2</td>
<td class="gt_row gt_right" headers="pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:20</td>
<td class="gt_row gt_right" headers="temp">17.8</td>
<td class="gt_row gt_right" headers="humidity">0.77</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">01:50</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.73</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="date">2023-05-01</td>
<td class="gt_row gt_right" headers="time">02:20</td>
<td class="gt_row gt_right" headers="temp">18.9</td>
<td class="gt_row gt_right" headers="humidity">0.68</td>
<td class="gt_row gt_right" headers="wind_speed">6.7</td>
<td class="gt_row gt_right" headers="pressure">1014.6</td>
</tr>
</tbody><tfoot>
<tr class="gt_footnotes">
<td colspan="6" class="gt_footnote"><span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;line-height:0;">1</span> Observations from the <em>Gibraltar Airport Station</em> (GIB).</td>
</tr>
</tfoot>

</table>


Footnotes are a subtle but important tool for building informative tables. They let you add precision and context where it matters most, keeping the main table body clean while ensuring readers have access to the details they need. The automatic sequencing and placement system means you can focus on content rather than managing mark numbers manually.
