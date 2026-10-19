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
#otrbmwcmiq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#otrbmwcmiq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#otrbmwcmiq p { margin: 0; padding: 0; }
 #otrbmwcmiq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #otrbmwcmiq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #otrbmwcmiq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #otrbmwcmiq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #otrbmwcmiq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #otrbmwcmiq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #otrbmwcmiq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #otrbmwcmiq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #otrbmwcmiq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #otrbmwcmiq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #otrbmwcmiq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #otrbmwcmiq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #otrbmwcmiq .gt_spanner_row { border-bottom-style: hidden; }
 #otrbmwcmiq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #otrbmwcmiq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #otrbmwcmiq .gt_from_md> :first-child { margin-top: 0; }
 #otrbmwcmiq .gt_from_md> :last-child { margin-bottom: 0; }
 #otrbmwcmiq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #otrbmwcmiq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #otrbmwcmiq .gt_indent_1 { text-indent: 5px; }
 #otrbmwcmiq .gt_indent_2 { text-indent: calc(5px * 2); }
 #otrbmwcmiq .gt_indent_3 { text-indent: calc(5px * 3); }
 #otrbmwcmiq .gt_indent_4 { text-indent: calc(5px * 4); }
 #otrbmwcmiq .gt_indent_5 { text-indent: calc(5px * 5); }
 #otrbmwcmiq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #otrbmwcmiq .gt_row_group_first td { border-top-width: 2px; }
 #otrbmwcmiq .gt_row_group_first th { border-top-width: 2px; }
 #otrbmwcmiq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #otrbmwcmiq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #otrbmwcmiq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #otrbmwcmiq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #otrbmwcmiq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #otrbmwcmiq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #otrbmwcmiq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #otrbmwcmiq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #otrbmwcmiq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #otrbmwcmiq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #otrbmwcmiq .gt_left { text-align: left; }
 #otrbmwcmiq .gt_center { text-align: center; }
 #otrbmwcmiq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #otrbmwcmiq .gt_font_normal { font-weight: normal; }
 #otrbmwcmiq .gt_font_bold { font-weight: bold; }
 #otrbmwcmiq .gt_font_italic { font-style: italic; }
 #otrbmwcmiq .gt_super { font-size: 65%; }
 #otrbmwcmiq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #otrbmwcmiq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #otrbmwcmiq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #otrbmwcmiq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #otrbmwcmiq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #otrbmwcmiq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#khmkdpegpe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#khmkdpegpe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#khmkdpegpe p { margin: 0; padding: 0; }
 #khmkdpegpe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #khmkdpegpe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #khmkdpegpe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #khmkdpegpe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #khmkdpegpe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khmkdpegpe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khmkdpegpe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khmkdpegpe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #khmkdpegpe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #khmkdpegpe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #khmkdpegpe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #khmkdpegpe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #khmkdpegpe .gt_spanner_row { border-bottom-style: hidden; }
 #khmkdpegpe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #khmkdpegpe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #khmkdpegpe .gt_from_md> :first-child { margin-top: 0; }
 #khmkdpegpe .gt_from_md> :last-child { margin-bottom: 0; }
 #khmkdpegpe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #khmkdpegpe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #khmkdpegpe .gt_indent_1 { text-indent: 5px; }
 #khmkdpegpe .gt_indent_2 { text-indent: calc(5px * 2); }
 #khmkdpegpe .gt_indent_3 { text-indent: calc(5px * 3); }
 #khmkdpegpe .gt_indent_4 { text-indent: calc(5px * 4); }
 #khmkdpegpe .gt_indent_5 { text-indent: calc(5px * 5); }
 #khmkdpegpe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #khmkdpegpe .gt_row_group_first td { border-top-width: 2px; }
 #khmkdpegpe .gt_row_group_first th { border-top-width: 2px; }
 #khmkdpegpe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #khmkdpegpe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khmkdpegpe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khmkdpegpe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #khmkdpegpe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khmkdpegpe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khmkdpegpe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #khmkdpegpe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #khmkdpegpe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khmkdpegpe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khmkdpegpe .gt_left { text-align: left; }
 #khmkdpegpe .gt_center { text-align: center; }
 #khmkdpegpe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #khmkdpegpe .gt_font_normal { font-weight: normal; }
 #khmkdpegpe .gt_font_bold { font-weight: bold; }
 #khmkdpegpe .gt_font_italic { font-style: italic; }
 #khmkdpegpe .gt_super { font-size: 65%; }
 #khmkdpegpe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khmkdpegpe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #khmkdpegpe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khmkdpegpe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khmkdpegpe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #khmkdpegpe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jyjfetbfhg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jyjfetbfhg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jyjfetbfhg p { margin: 0; padding: 0; }
 #jyjfetbfhg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jyjfetbfhg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jyjfetbfhg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jyjfetbfhg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jyjfetbfhg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jyjfetbfhg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jyjfetbfhg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jyjfetbfhg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jyjfetbfhg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jyjfetbfhg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jyjfetbfhg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jyjfetbfhg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jyjfetbfhg .gt_spanner_row { border-bottom-style: hidden; }
 #jyjfetbfhg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jyjfetbfhg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jyjfetbfhg .gt_from_md> :first-child { margin-top: 0; }
 #jyjfetbfhg .gt_from_md> :last-child { margin-bottom: 0; }
 #jyjfetbfhg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jyjfetbfhg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jyjfetbfhg .gt_indent_1 { text-indent: 5px; }
 #jyjfetbfhg .gt_indent_2 { text-indent: calc(5px * 2); }
 #jyjfetbfhg .gt_indent_3 { text-indent: calc(5px * 3); }
 #jyjfetbfhg .gt_indent_4 { text-indent: calc(5px * 4); }
 #jyjfetbfhg .gt_indent_5 { text-indent: calc(5px * 5); }
 #jyjfetbfhg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jyjfetbfhg .gt_row_group_first td { border-top-width: 2px; }
 #jyjfetbfhg .gt_row_group_first th { border-top-width: 2px; }
 #jyjfetbfhg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jyjfetbfhg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jyjfetbfhg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jyjfetbfhg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jyjfetbfhg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jyjfetbfhg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jyjfetbfhg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jyjfetbfhg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jyjfetbfhg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jyjfetbfhg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jyjfetbfhg .gt_left { text-align: left; }
 #jyjfetbfhg .gt_center { text-align: center; }
 #jyjfetbfhg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jyjfetbfhg .gt_font_normal { font-weight: normal; }
 #jyjfetbfhg .gt_font_bold { font-weight: bold; }
 #jyjfetbfhg .gt_font_italic { font-style: italic; }
 #jyjfetbfhg .gt_super { font-size: 65%; }
 #jyjfetbfhg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jyjfetbfhg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jyjfetbfhg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jyjfetbfhg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jyjfetbfhg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jyjfetbfhg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jndnanyvki table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jndnanyvki thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jndnanyvki p { margin: 0; padding: 0; }
 #jndnanyvki .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jndnanyvki .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jndnanyvki .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jndnanyvki .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jndnanyvki .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jndnanyvki .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jndnanyvki .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jndnanyvki .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jndnanyvki .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jndnanyvki .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jndnanyvki .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jndnanyvki .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jndnanyvki .gt_spanner_row { border-bottom-style: hidden; }
 #jndnanyvki .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jndnanyvki .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jndnanyvki .gt_from_md> :first-child { margin-top: 0; }
 #jndnanyvki .gt_from_md> :last-child { margin-bottom: 0; }
 #jndnanyvki .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jndnanyvki .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jndnanyvki .gt_indent_1 { text-indent: 5px; }
 #jndnanyvki .gt_indent_2 { text-indent: calc(5px * 2); }
 #jndnanyvki .gt_indent_3 { text-indent: calc(5px * 3); }
 #jndnanyvki .gt_indent_4 { text-indent: calc(5px * 4); }
 #jndnanyvki .gt_indent_5 { text-indent: calc(5px * 5); }
 #jndnanyvki .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jndnanyvki .gt_row_group_first td { border-top-width: 2px; }
 #jndnanyvki .gt_row_group_first th { border-top-width: 2px; }
 #jndnanyvki .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jndnanyvki .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jndnanyvki .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jndnanyvki .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jndnanyvki .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jndnanyvki .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jndnanyvki .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jndnanyvki .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jndnanyvki .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jndnanyvki .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jndnanyvki .gt_left { text-align: left; }
 #jndnanyvki .gt_center { text-align: center; }
 #jndnanyvki .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jndnanyvki .gt_font_normal { font-weight: normal; }
 #jndnanyvki .gt_font_bold { font-weight: bold; }
 #jndnanyvki .gt_font_italic { font-style: italic; }
 #jndnanyvki .gt_super { font-size: 65%; }
 #jndnanyvki .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jndnanyvki .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jndnanyvki .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jndnanyvki .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jndnanyvki .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jndnanyvki .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cehyfarmph table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cehyfarmph thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cehyfarmph p { margin: 0; padding: 0; }
 #cehyfarmph .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cehyfarmph .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cehyfarmph .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cehyfarmph .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cehyfarmph .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cehyfarmph .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cehyfarmph .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cehyfarmph .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cehyfarmph .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cehyfarmph .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cehyfarmph .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cehyfarmph .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cehyfarmph .gt_spanner_row { border-bottom-style: hidden; }
 #cehyfarmph .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cehyfarmph .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cehyfarmph .gt_from_md> :first-child { margin-top: 0; }
 #cehyfarmph .gt_from_md> :last-child { margin-bottom: 0; }
 #cehyfarmph .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cehyfarmph .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cehyfarmph .gt_indent_1 { text-indent: 5px; }
 #cehyfarmph .gt_indent_2 { text-indent: calc(5px * 2); }
 #cehyfarmph .gt_indent_3 { text-indent: calc(5px * 3); }
 #cehyfarmph .gt_indent_4 { text-indent: calc(5px * 4); }
 #cehyfarmph .gt_indent_5 { text-indent: calc(5px * 5); }
 #cehyfarmph .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cehyfarmph .gt_row_group_first td { border-top-width: 2px; }
 #cehyfarmph .gt_row_group_first th { border-top-width: 2px; }
 #cehyfarmph .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cehyfarmph .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cehyfarmph .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cehyfarmph .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cehyfarmph .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cehyfarmph .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cehyfarmph .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cehyfarmph .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cehyfarmph .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cehyfarmph .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cehyfarmph .gt_left { text-align: left; }
 #cehyfarmph .gt_center { text-align: center; }
 #cehyfarmph .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cehyfarmph .gt_font_normal { font-weight: normal; }
 #cehyfarmph .gt_font_bold { font-weight: bold; }
 #cehyfarmph .gt_font_italic { font-style: italic; }
 #cehyfarmph .gt_super { font-size: 65%; }
 #cehyfarmph .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cehyfarmph .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cehyfarmph .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cehyfarmph .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cehyfarmph .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cehyfarmph .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xsucansmqg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xsucansmqg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xsucansmqg p { margin: 0; padding: 0; }
 #xsucansmqg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xsucansmqg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xsucansmqg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xsucansmqg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xsucansmqg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xsucansmqg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xsucansmqg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xsucansmqg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xsucansmqg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xsucansmqg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xsucansmqg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xsucansmqg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xsucansmqg .gt_spanner_row { border-bottom-style: hidden; }
 #xsucansmqg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xsucansmqg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xsucansmqg .gt_from_md> :first-child { margin-top: 0; }
 #xsucansmqg .gt_from_md> :last-child { margin-bottom: 0; }
 #xsucansmqg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xsucansmqg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xsucansmqg .gt_indent_1 { text-indent: 5px; }
 #xsucansmqg .gt_indent_2 { text-indent: calc(5px * 2); }
 #xsucansmqg .gt_indent_3 { text-indent: calc(5px * 3); }
 #xsucansmqg .gt_indent_4 { text-indent: calc(5px * 4); }
 #xsucansmqg .gt_indent_5 { text-indent: calc(5px * 5); }
 #xsucansmqg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xsucansmqg .gt_row_group_first td { border-top-width: 2px; }
 #xsucansmqg .gt_row_group_first th { border-top-width: 2px; }
 #xsucansmqg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xsucansmqg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xsucansmqg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xsucansmqg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xsucansmqg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xsucansmqg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xsucansmqg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xsucansmqg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xsucansmqg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xsucansmqg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xsucansmqg .gt_left { text-align: left; }
 #xsucansmqg .gt_center { text-align: center; }
 #xsucansmqg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xsucansmqg .gt_font_normal { font-weight: normal; }
 #xsucansmqg .gt_font_bold { font-weight: bold; }
 #xsucansmqg .gt_font_italic { font-style: italic; }
 #xsucansmqg .gt_super { font-size: 65%; }
 #xsucansmqg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xsucansmqg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xsucansmqg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xsucansmqg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xsucansmqg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xsucansmqg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hpdyhulhgj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hpdyhulhgj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hpdyhulhgj p { margin: 0; padding: 0; }
 #hpdyhulhgj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hpdyhulhgj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hpdyhulhgj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hpdyhulhgj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hpdyhulhgj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hpdyhulhgj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hpdyhulhgj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hpdyhulhgj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hpdyhulhgj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hpdyhulhgj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hpdyhulhgj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hpdyhulhgj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hpdyhulhgj .gt_spanner_row { border-bottom-style: hidden; }
 #hpdyhulhgj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hpdyhulhgj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hpdyhulhgj .gt_from_md> :first-child { margin-top: 0; }
 #hpdyhulhgj .gt_from_md> :last-child { margin-bottom: 0; }
 #hpdyhulhgj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hpdyhulhgj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hpdyhulhgj .gt_indent_1 { text-indent: 5px; }
 #hpdyhulhgj .gt_indent_2 { text-indent: calc(5px * 2); }
 #hpdyhulhgj .gt_indent_3 { text-indent: calc(5px * 3); }
 #hpdyhulhgj .gt_indent_4 { text-indent: calc(5px * 4); }
 #hpdyhulhgj .gt_indent_5 { text-indent: calc(5px * 5); }
 #hpdyhulhgj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hpdyhulhgj .gt_row_group_first td { border-top-width: 2px; }
 #hpdyhulhgj .gt_row_group_first th { border-top-width: 2px; }
 #hpdyhulhgj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hpdyhulhgj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hpdyhulhgj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hpdyhulhgj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hpdyhulhgj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hpdyhulhgj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hpdyhulhgj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hpdyhulhgj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hpdyhulhgj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hpdyhulhgj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hpdyhulhgj .gt_left { text-align: left; }
 #hpdyhulhgj .gt_center { text-align: center; }
 #hpdyhulhgj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hpdyhulhgj .gt_font_normal { font-weight: normal; }
 #hpdyhulhgj .gt_font_bold { font-weight: bold; }
 #hpdyhulhgj .gt_font_italic { font-style: italic; }
 #hpdyhulhgj .gt_super { font-size: 65%; }
 #hpdyhulhgj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hpdyhulhgj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hpdyhulhgj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hpdyhulhgj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hpdyhulhgj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hpdyhulhgj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tvhknzivlg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tvhknzivlg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tvhknzivlg p { margin: 0; padding: 0; }
 #tvhknzivlg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tvhknzivlg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tvhknzivlg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tvhknzivlg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tvhknzivlg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tvhknzivlg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tvhknzivlg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tvhknzivlg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tvhknzivlg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tvhknzivlg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tvhknzivlg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tvhknzivlg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tvhknzivlg .gt_spanner_row { border-bottom-style: hidden; }
 #tvhknzivlg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tvhknzivlg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tvhknzivlg .gt_from_md> :first-child { margin-top: 0; }
 #tvhknzivlg .gt_from_md> :last-child { margin-bottom: 0; }
 #tvhknzivlg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tvhknzivlg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tvhknzivlg .gt_indent_1 { text-indent: 5px; }
 #tvhknzivlg .gt_indent_2 { text-indent: calc(5px * 2); }
 #tvhknzivlg .gt_indent_3 { text-indent: calc(5px * 3); }
 #tvhknzivlg .gt_indent_4 { text-indent: calc(5px * 4); }
 #tvhknzivlg .gt_indent_5 { text-indent: calc(5px * 5); }
 #tvhknzivlg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tvhknzivlg .gt_row_group_first td { border-top-width: 2px; }
 #tvhknzivlg .gt_row_group_first th { border-top-width: 2px; }
 #tvhknzivlg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tvhknzivlg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tvhknzivlg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tvhknzivlg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tvhknzivlg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tvhknzivlg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tvhknzivlg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tvhknzivlg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tvhknzivlg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tvhknzivlg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tvhknzivlg .gt_left { text-align: left; }
 #tvhknzivlg .gt_center { text-align: center; }
 #tvhknzivlg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tvhknzivlg .gt_font_normal { font-weight: normal; }
 #tvhknzivlg .gt_font_bold { font-weight: bold; }
 #tvhknzivlg .gt_font_italic { font-style: italic; }
 #tvhknzivlg .gt_super { font-size: 65%; }
 #tvhknzivlg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tvhknzivlg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tvhknzivlg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tvhknzivlg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tvhknzivlg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tvhknzivlg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
