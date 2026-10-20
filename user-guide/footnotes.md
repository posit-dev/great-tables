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
#xizhqwaiam table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xizhqwaiam thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xizhqwaiam p { margin: 0; padding: 0; }
 #xizhqwaiam .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xizhqwaiam .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xizhqwaiam .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xizhqwaiam .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xizhqwaiam .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xizhqwaiam .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xizhqwaiam .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xizhqwaiam .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xizhqwaiam .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xizhqwaiam .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xizhqwaiam .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xizhqwaiam .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xizhqwaiam .gt_spanner_row { border-bottom-style: hidden; }
 #xizhqwaiam .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xizhqwaiam .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xizhqwaiam .gt_from_md> :first-child { margin-top: 0; }
 #xizhqwaiam .gt_from_md> :last-child { margin-bottom: 0; }
 #xizhqwaiam .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xizhqwaiam .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xizhqwaiam .gt_indent_1 { text-indent: 5px; }
 #xizhqwaiam .gt_indent_2 { text-indent: calc(5px * 2); }
 #xizhqwaiam .gt_indent_3 { text-indent: calc(5px * 3); }
 #xizhqwaiam .gt_indent_4 { text-indent: calc(5px * 4); }
 #xizhqwaiam .gt_indent_5 { text-indent: calc(5px * 5); }
 #xizhqwaiam .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xizhqwaiam .gt_row_group_first td { border-top-width: 2px; }
 #xizhqwaiam .gt_row_group_first th { border-top-width: 2px; }
 #xizhqwaiam .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xizhqwaiam .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xizhqwaiam .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xizhqwaiam .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xizhqwaiam .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xizhqwaiam .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xizhqwaiam .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xizhqwaiam .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xizhqwaiam .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xizhqwaiam .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xizhqwaiam .gt_left { text-align: left; }
 #xizhqwaiam .gt_center { text-align: center; }
 #xizhqwaiam .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xizhqwaiam .gt_font_normal { font-weight: normal; }
 #xizhqwaiam .gt_font_bold { font-weight: bold; }
 #xizhqwaiam .gt_font_italic { font-style: italic; }
 #xizhqwaiam .gt_super { font-size: 65%; }
 #xizhqwaiam .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xizhqwaiam .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xizhqwaiam .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xizhqwaiam .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xizhqwaiam .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xizhqwaiam .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dxztbwdjgf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dxztbwdjgf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dxztbwdjgf p { margin: 0; padding: 0; }
 #dxztbwdjgf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dxztbwdjgf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dxztbwdjgf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dxztbwdjgf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dxztbwdjgf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxztbwdjgf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxztbwdjgf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxztbwdjgf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dxztbwdjgf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dxztbwdjgf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dxztbwdjgf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dxztbwdjgf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dxztbwdjgf .gt_spanner_row { border-bottom-style: hidden; }
 #dxztbwdjgf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dxztbwdjgf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dxztbwdjgf .gt_from_md> :first-child { margin-top: 0; }
 #dxztbwdjgf .gt_from_md> :last-child { margin-bottom: 0; }
 #dxztbwdjgf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dxztbwdjgf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dxztbwdjgf .gt_indent_1 { text-indent: 5px; }
 #dxztbwdjgf .gt_indent_2 { text-indent: calc(5px * 2); }
 #dxztbwdjgf .gt_indent_3 { text-indent: calc(5px * 3); }
 #dxztbwdjgf .gt_indent_4 { text-indent: calc(5px * 4); }
 #dxztbwdjgf .gt_indent_5 { text-indent: calc(5px * 5); }
 #dxztbwdjgf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dxztbwdjgf .gt_row_group_first td { border-top-width: 2px; }
 #dxztbwdjgf .gt_row_group_first th { border-top-width: 2px; }
 #dxztbwdjgf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dxztbwdjgf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxztbwdjgf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxztbwdjgf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dxztbwdjgf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxztbwdjgf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxztbwdjgf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dxztbwdjgf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dxztbwdjgf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxztbwdjgf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxztbwdjgf .gt_left { text-align: left; }
 #dxztbwdjgf .gt_center { text-align: center; }
 #dxztbwdjgf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dxztbwdjgf .gt_font_normal { font-weight: normal; }
 #dxztbwdjgf .gt_font_bold { font-weight: bold; }
 #dxztbwdjgf .gt_font_italic { font-style: italic; }
 #dxztbwdjgf .gt_super { font-size: 65%; }
 #dxztbwdjgf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxztbwdjgf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dxztbwdjgf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxztbwdjgf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxztbwdjgf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dxztbwdjgf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uyzeytrqhk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uyzeytrqhk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uyzeytrqhk p { margin: 0; padding: 0; }
 #uyzeytrqhk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uyzeytrqhk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uyzeytrqhk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uyzeytrqhk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uyzeytrqhk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uyzeytrqhk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uyzeytrqhk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uyzeytrqhk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uyzeytrqhk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uyzeytrqhk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uyzeytrqhk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uyzeytrqhk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uyzeytrqhk .gt_spanner_row { border-bottom-style: hidden; }
 #uyzeytrqhk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uyzeytrqhk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uyzeytrqhk .gt_from_md> :first-child { margin-top: 0; }
 #uyzeytrqhk .gt_from_md> :last-child { margin-bottom: 0; }
 #uyzeytrqhk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uyzeytrqhk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uyzeytrqhk .gt_indent_1 { text-indent: 5px; }
 #uyzeytrqhk .gt_indent_2 { text-indent: calc(5px * 2); }
 #uyzeytrqhk .gt_indent_3 { text-indent: calc(5px * 3); }
 #uyzeytrqhk .gt_indent_4 { text-indent: calc(5px * 4); }
 #uyzeytrqhk .gt_indent_5 { text-indent: calc(5px * 5); }
 #uyzeytrqhk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uyzeytrqhk .gt_row_group_first td { border-top-width: 2px; }
 #uyzeytrqhk .gt_row_group_first th { border-top-width: 2px; }
 #uyzeytrqhk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uyzeytrqhk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uyzeytrqhk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uyzeytrqhk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uyzeytrqhk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uyzeytrqhk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uyzeytrqhk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uyzeytrqhk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uyzeytrqhk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uyzeytrqhk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uyzeytrqhk .gt_left { text-align: left; }
 #uyzeytrqhk .gt_center { text-align: center; }
 #uyzeytrqhk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uyzeytrqhk .gt_font_normal { font-weight: normal; }
 #uyzeytrqhk .gt_font_bold { font-weight: bold; }
 #uyzeytrqhk .gt_font_italic { font-style: italic; }
 #uyzeytrqhk .gt_super { font-size: 65%; }
 #uyzeytrqhk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uyzeytrqhk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uyzeytrqhk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uyzeytrqhk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uyzeytrqhk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uyzeytrqhk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#yydkgvudiv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yydkgvudiv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yydkgvudiv p { margin: 0; padding: 0; }
 #yydkgvudiv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yydkgvudiv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yydkgvudiv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yydkgvudiv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yydkgvudiv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yydkgvudiv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yydkgvudiv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yydkgvudiv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yydkgvudiv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yydkgvudiv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yydkgvudiv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yydkgvudiv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yydkgvudiv .gt_spanner_row { border-bottom-style: hidden; }
 #yydkgvudiv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yydkgvudiv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yydkgvudiv .gt_from_md> :first-child { margin-top: 0; }
 #yydkgvudiv .gt_from_md> :last-child { margin-bottom: 0; }
 #yydkgvudiv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yydkgvudiv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yydkgvudiv .gt_indent_1 { text-indent: 5px; }
 #yydkgvudiv .gt_indent_2 { text-indent: calc(5px * 2); }
 #yydkgvudiv .gt_indent_3 { text-indent: calc(5px * 3); }
 #yydkgvudiv .gt_indent_4 { text-indent: calc(5px * 4); }
 #yydkgvudiv .gt_indent_5 { text-indent: calc(5px * 5); }
 #yydkgvudiv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yydkgvudiv .gt_row_group_first td { border-top-width: 2px; }
 #yydkgvudiv .gt_row_group_first th { border-top-width: 2px; }
 #yydkgvudiv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yydkgvudiv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yydkgvudiv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yydkgvudiv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yydkgvudiv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yydkgvudiv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yydkgvudiv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yydkgvudiv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yydkgvudiv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yydkgvudiv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yydkgvudiv .gt_left { text-align: left; }
 #yydkgvudiv .gt_center { text-align: center; }
 #yydkgvudiv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yydkgvudiv .gt_font_normal { font-weight: normal; }
 #yydkgvudiv .gt_font_bold { font-weight: bold; }
 #yydkgvudiv .gt_font_italic { font-style: italic; }
 #yydkgvudiv .gt_super { font-size: 65%; }
 #yydkgvudiv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yydkgvudiv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yydkgvudiv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yydkgvudiv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yydkgvudiv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yydkgvudiv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gaxtexnccv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gaxtexnccv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gaxtexnccv p { margin: 0; padding: 0; }
 #gaxtexnccv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gaxtexnccv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gaxtexnccv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gaxtexnccv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gaxtexnccv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gaxtexnccv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gaxtexnccv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gaxtexnccv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gaxtexnccv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gaxtexnccv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gaxtexnccv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gaxtexnccv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gaxtexnccv .gt_spanner_row { border-bottom-style: hidden; }
 #gaxtexnccv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gaxtexnccv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gaxtexnccv .gt_from_md> :first-child { margin-top: 0; }
 #gaxtexnccv .gt_from_md> :last-child { margin-bottom: 0; }
 #gaxtexnccv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gaxtexnccv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gaxtexnccv .gt_indent_1 { text-indent: 5px; }
 #gaxtexnccv .gt_indent_2 { text-indent: calc(5px * 2); }
 #gaxtexnccv .gt_indent_3 { text-indent: calc(5px * 3); }
 #gaxtexnccv .gt_indent_4 { text-indent: calc(5px * 4); }
 #gaxtexnccv .gt_indent_5 { text-indent: calc(5px * 5); }
 #gaxtexnccv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gaxtexnccv .gt_row_group_first td { border-top-width: 2px; }
 #gaxtexnccv .gt_row_group_first th { border-top-width: 2px; }
 #gaxtexnccv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gaxtexnccv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gaxtexnccv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gaxtexnccv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gaxtexnccv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gaxtexnccv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gaxtexnccv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gaxtexnccv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gaxtexnccv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gaxtexnccv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gaxtexnccv .gt_left { text-align: left; }
 #gaxtexnccv .gt_center { text-align: center; }
 #gaxtexnccv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gaxtexnccv .gt_font_normal { font-weight: normal; }
 #gaxtexnccv .gt_font_bold { font-weight: bold; }
 #gaxtexnccv .gt_font_italic { font-style: italic; }
 #gaxtexnccv .gt_super { font-size: 65%; }
 #gaxtexnccv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gaxtexnccv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gaxtexnccv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gaxtexnccv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gaxtexnccv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gaxtexnccv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#decrnsgyyr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#decrnsgyyr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#decrnsgyyr p { margin: 0; padding: 0; }
 #decrnsgyyr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #decrnsgyyr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #decrnsgyyr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #decrnsgyyr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #decrnsgyyr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #decrnsgyyr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #decrnsgyyr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #decrnsgyyr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #decrnsgyyr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #decrnsgyyr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #decrnsgyyr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #decrnsgyyr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #decrnsgyyr .gt_spanner_row { border-bottom-style: hidden; }
 #decrnsgyyr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #decrnsgyyr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #decrnsgyyr .gt_from_md> :first-child { margin-top: 0; }
 #decrnsgyyr .gt_from_md> :last-child { margin-bottom: 0; }
 #decrnsgyyr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #decrnsgyyr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #decrnsgyyr .gt_indent_1 { text-indent: 5px; }
 #decrnsgyyr .gt_indent_2 { text-indent: calc(5px * 2); }
 #decrnsgyyr .gt_indent_3 { text-indent: calc(5px * 3); }
 #decrnsgyyr .gt_indent_4 { text-indent: calc(5px * 4); }
 #decrnsgyyr .gt_indent_5 { text-indent: calc(5px * 5); }
 #decrnsgyyr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #decrnsgyyr .gt_row_group_first td { border-top-width: 2px; }
 #decrnsgyyr .gt_row_group_first th { border-top-width: 2px; }
 #decrnsgyyr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #decrnsgyyr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #decrnsgyyr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #decrnsgyyr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #decrnsgyyr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #decrnsgyyr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #decrnsgyyr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #decrnsgyyr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #decrnsgyyr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #decrnsgyyr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #decrnsgyyr .gt_left { text-align: left; }
 #decrnsgyyr .gt_center { text-align: center; }
 #decrnsgyyr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #decrnsgyyr .gt_font_normal { font-weight: normal; }
 #decrnsgyyr .gt_font_bold { font-weight: bold; }
 #decrnsgyyr .gt_font_italic { font-style: italic; }
 #decrnsgyyr .gt_super { font-size: 65%; }
 #decrnsgyyr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #decrnsgyyr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #decrnsgyyr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #decrnsgyyr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #decrnsgyyr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #decrnsgyyr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#aprdcgpdgz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aprdcgpdgz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aprdcgpdgz p { margin: 0; padding: 0; }
 #aprdcgpdgz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aprdcgpdgz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aprdcgpdgz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aprdcgpdgz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aprdcgpdgz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aprdcgpdgz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aprdcgpdgz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aprdcgpdgz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #aprdcgpdgz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aprdcgpdgz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aprdcgpdgz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aprdcgpdgz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aprdcgpdgz .gt_spanner_row { border-bottom-style: hidden; }
 #aprdcgpdgz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aprdcgpdgz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aprdcgpdgz .gt_from_md> :first-child { margin-top: 0; }
 #aprdcgpdgz .gt_from_md> :last-child { margin-bottom: 0; }
 #aprdcgpdgz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aprdcgpdgz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #aprdcgpdgz .gt_indent_1 { text-indent: 5px; }
 #aprdcgpdgz .gt_indent_2 { text-indent: calc(5px * 2); }
 #aprdcgpdgz .gt_indent_3 { text-indent: calc(5px * 3); }
 #aprdcgpdgz .gt_indent_4 { text-indent: calc(5px * 4); }
 #aprdcgpdgz .gt_indent_5 { text-indent: calc(5px * 5); }
 #aprdcgpdgz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #aprdcgpdgz .gt_row_group_first td { border-top-width: 2px; }
 #aprdcgpdgz .gt_row_group_first th { border-top-width: 2px; }
 #aprdcgpdgz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aprdcgpdgz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aprdcgpdgz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aprdcgpdgz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aprdcgpdgz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aprdcgpdgz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aprdcgpdgz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aprdcgpdgz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aprdcgpdgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aprdcgpdgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aprdcgpdgz .gt_left { text-align: left; }
 #aprdcgpdgz .gt_center { text-align: center; }
 #aprdcgpdgz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aprdcgpdgz .gt_font_normal { font-weight: normal; }
 #aprdcgpdgz .gt_font_bold { font-weight: bold; }
 #aprdcgpdgz .gt_font_italic { font-style: italic; }
 #aprdcgpdgz .gt_super { font-size: 65%; }
 #aprdcgpdgz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aprdcgpdgz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aprdcgpdgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aprdcgpdgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aprdcgpdgz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aprdcgpdgz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jwpzuxfoin table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jwpzuxfoin thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jwpzuxfoin p { margin: 0; padding: 0; }
 #jwpzuxfoin .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jwpzuxfoin .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jwpzuxfoin .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jwpzuxfoin .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jwpzuxfoin .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jwpzuxfoin .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jwpzuxfoin .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jwpzuxfoin .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jwpzuxfoin .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jwpzuxfoin .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jwpzuxfoin .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jwpzuxfoin .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jwpzuxfoin .gt_spanner_row { border-bottom-style: hidden; }
 #jwpzuxfoin .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jwpzuxfoin .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jwpzuxfoin .gt_from_md> :first-child { margin-top: 0; }
 #jwpzuxfoin .gt_from_md> :last-child { margin-bottom: 0; }
 #jwpzuxfoin .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jwpzuxfoin .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jwpzuxfoin .gt_indent_1 { text-indent: 5px; }
 #jwpzuxfoin .gt_indent_2 { text-indent: calc(5px * 2); }
 #jwpzuxfoin .gt_indent_3 { text-indent: calc(5px * 3); }
 #jwpzuxfoin .gt_indent_4 { text-indent: calc(5px * 4); }
 #jwpzuxfoin .gt_indent_5 { text-indent: calc(5px * 5); }
 #jwpzuxfoin .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jwpzuxfoin .gt_row_group_first td { border-top-width: 2px; }
 #jwpzuxfoin .gt_row_group_first th { border-top-width: 2px; }
 #jwpzuxfoin .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jwpzuxfoin .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jwpzuxfoin .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jwpzuxfoin .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jwpzuxfoin .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jwpzuxfoin .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jwpzuxfoin .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jwpzuxfoin .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jwpzuxfoin .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jwpzuxfoin .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jwpzuxfoin .gt_left { text-align: left; }
 #jwpzuxfoin .gt_center { text-align: center; }
 #jwpzuxfoin .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jwpzuxfoin .gt_font_normal { font-weight: normal; }
 #jwpzuxfoin .gt_font_bold { font-weight: bold; }
 #jwpzuxfoin .gt_font_italic { font-style: italic; }
 #jwpzuxfoin .gt_super { font-size: 65%; }
 #jwpzuxfoin .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jwpzuxfoin .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jwpzuxfoin .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jwpzuxfoin .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jwpzuxfoin .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jwpzuxfoin .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
