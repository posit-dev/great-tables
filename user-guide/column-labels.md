# Column Labels

Column labels are the primary way readers identify what data each column contains. Raw DataFrame column names are often abbreviated, inconsistently cased, or full of underscores. Presentation-ready column labels are one of the highest-impact improvements you can make to a table, and they require very little effort.

Beyond simple labels, **Great Tables** lets you group related columns together under spanner labels, reorder columns for clarity, and customize label text with rich formatting. This page walks through each of these capabilities.


# Working with Column Data

The table's **Column Labels** part contains, at a minimum, columns and their *column labels*. The last example had a single column: `population`. Just as in the **Stub**, we can create groupings called *spanner labels* that encompass one or more columns.

To better demonstrate how **Column Labels** work and are displayed, let's use an input data table with more columns. In this case, that input table will be made from [gibraltar](../reference/data.gibraltar.md#great_tables.data.gibraltar), which has weather observations from the Gibraltar Airport Station. We'll keep these of its columns:

- `temp`: the air temperature in degrees Celsius (°C)
- `humidity`: the relative humidity, as a value between `0` and `1`
- `wind_speed`: the wind speed in meters per second (m s<sup>−1</sup>)
- `pressure`: the atmospheric pressure in hectopascals (hPa)
- `date`, `time`: the date and time of the observation

The date and time columns are placed last here, so that we can move them later on.


``` python
from great_tables import GT, html
from great_tables.data import gibraltar

gibraltar_mini = gibraltar.head(10)[["temp", "humidity", "wind_speed", "pressure", "date", "time"]]

gibraltar_mini
```


|     | temp | humidity | wind_speed | pressure | date       | time  |
|-----|------|----------|------------|----------|------------|-------|
| 0   | 18.9 | 0.68     | 6.7        | 1015.2   | 2023-05-01 | 00:20 |
| 1   | 18.9 | 0.73     | 7.2        | 1015.2   | 2023-05-01 | 00:50 |
| 2   | 17.8 | 0.77     | 6.7        | 1014.6   | 2023-05-01 | 01:20 |
| 3   | 18.9 | 0.73     | 6.7        | 1014.6   | 2023-05-01 | 01:50 |
| 4   | 18.9 | 0.68     | 6.7        | 1014.6   | 2023-05-01 | 02:20 |
| 5   | 17.8 | 0.73     | 6.7        | 1014.6   | 2023-05-01 | 02:50 |
| 6   | 17.8 | 0.73     | 7.2        | 1014.6   | 2023-05-01 | 03:20 |
| 7   | 17.8 | 0.73     | 6.3        | 1013.5   | 2023-05-01 | 03:50 |
| 8   | 18.9 | 0.64     | 4.0        | 1014.6   | 2023-05-01 | 04:20 |
| 9   | 18.9 | 0.64     | 3.1        | 1014.6   | 2023-05-01 | 04:50 |


This ten-row subset of the Gibraltar weather dataset has both measurement and time columns, making it a good candidate for organizing with column spanners.


# Adding Column Spanners

Column spanners are most useful when you have a logical grouping of columns and want the reader to grasp the table's structure at a glance. For example, grouping all measurement columns under "Measurement" and all date-related columns under "Time" immediately communicates the two-part nature of the data. Spanners work especially well in wide tables where the column count might otherwise feel overwhelming.

Let's organize the time information under a `Time` *spanner label*, and put the other columns under a `Measurement` *spanner label*. We can do this with the [tab_spanner()](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) method.


``` python
gt_gibraltar = (
    GT(gibraltar_mini)
    .tab_header(
        title="Weather at Gibraltar Airport",
        subtitle="Observations from the early hours of May 1, 2023"
    )
    .tab_spanner(
        label="Time",
        columns=["date", "time"]
    )
    .tab_spanner(
        label="Measurement",
        columns=["temp", "humidity", "wind_speed", "pressure"]
    )
)

gt_gibraltar
```


<style>
#dnznxudwed table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dnznxudwed thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dnznxudwed p { margin: 0; padding: 0; }
 #dnznxudwed .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dnznxudwed .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dnznxudwed .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dnznxudwed .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dnznxudwed .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dnznxudwed .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnznxudwed .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dnznxudwed .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dnznxudwed .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dnznxudwed .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dnznxudwed .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dnznxudwed .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dnznxudwed .gt_spanner_row { border-bottom-style: hidden; }
 #dnznxudwed .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dnznxudwed .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dnznxudwed .gt_from_md> :first-child { margin-top: 0; }
 #dnznxudwed .gt_from_md> :last-child { margin-bottom: 0; }
 #dnznxudwed .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dnznxudwed .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dnznxudwed .gt_indent_1 { text-indent: 5px; }
 #dnznxudwed .gt_indent_2 { text-indent: calc(5px * 2); }
 #dnznxudwed .gt_indent_3 { text-indent: calc(5px * 3); }
 #dnznxudwed .gt_indent_4 { text-indent: calc(5px * 4); }
 #dnznxudwed .gt_indent_5 { text-indent: calc(5px * 5); }
 #dnznxudwed .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dnznxudwed .gt_row_group_first td { border-top-width: 2px; }
 #dnznxudwed .gt_row_group_first th { border-top-width: 2px; }
 #dnznxudwed .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dnznxudwed .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnznxudwed .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dnznxudwed .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dnznxudwed .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnznxudwed .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dnznxudwed .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dnznxudwed .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dnznxudwed .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnznxudwed .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dnznxudwed .gt_left { text-align: left; }
 #dnznxudwed .gt_center { text-align: center; }
 #dnznxudwed .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dnznxudwed .gt_font_normal { font-weight: normal; }
 #dnznxudwed .gt_font_bold { font-weight: bold; }
 #dnznxudwed .gt_font_italic { font-style: italic; }
 #dnznxudwed .gt_super { font-size: 65%; }
 #dnznxudwed .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnznxudwed .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dnznxudwed .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnznxudwed .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dnznxudwed .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dnznxudwed .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations from the early hours of May 1, 2023</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="4" id="Measurement" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Measurement</th>
<th colspan="2" id="Time" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Time</th>
</tr>
<tr class="gt_col_headings">
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">temp</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">wind_speed</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">pressure</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1015.2</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:20</td>
</tr>
<tr>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1015.2</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">00:50</td>
</tr>
<tr>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.77</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:20</td>
</tr>
<tr>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">01:50</td>
</tr>
<tr>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.68</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:20</td>
</tr>
<tr>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:50</td>
</tr>
<tr>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1014.6</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">03:20</td>
</tr>
<tr>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.3</td>
<td class="gt_row gt_right">1013.5</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">03:50</td>
</tr>
<tr>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.64</td>
<td class="gt_row gt_right">4.0</td>
<td class="gt_row gt_right">1014.6</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">04:20</td>
</tr>
<tr>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.64</td>
<td class="gt_row gt_right">3.1</td>
<td class="gt_row gt_right">1014.6</td>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">04:50</td>
</tr>
</tbody>
</table>


# Moving and Relabeling Columns

We can do two more things to make this presentable:

- move the `Time` columns to the beginning of the series (using [cols_move_to_start()](../reference/GT.cols_move_to_start.md#great_tables.GT.cols_move_to_start))
- customize the column labels so that they are more descriptive (using [cols_label()](../reference/GT.cols_label.md#great_tables.GT.cols_label))

Let's do both of these things in the next example:


``` python
(
    gt_gibraltar
    .cols_move_to_start(columns=["date", "time"])
    .cols_label(
        date="Date",
        time="Time",
        temp=html("Temp,<br>°C"),
        humidity="Humidity",
        wind_speed=html("Wind,<br>m s<sup>−1</sup>"),
        pressure=html("Pressure,<br>hPa")
    )
)
```


<style>
#bfzridhbue table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bfzridhbue thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bfzridhbue p { margin: 0; padding: 0; }
 #bfzridhbue .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bfzridhbue .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bfzridhbue .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bfzridhbue .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bfzridhbue .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bfzridhbue .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bfzridhbue .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bfzridhbue .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bfzridhbue .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bfzridhbue .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bfzridhbue .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bfzridhbue .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bfzridhbue .gt_spanner_row { border-bottom-style: hidden; }
 #bfzridhbue .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bfzridhbue .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bfzridhbue .gt_from_md> :first-child { margin-top: 0; }
 #bfzridhbue .gt_from_md> :last-child { margin-bottom: 0; }
 #bfzridhbue .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bfzridhbue .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bfzridhbue .gt_indent_1 { text-indent: 5px; }
 #bfzridhbue .gt_indent_2 { text-indent: calc(5px * 2); }
 #bfzridhbue .gt_indent_3 { text-indent: calc(5px * 3); }
 #bfzridhbue .gt_indent_4 { text-indent: calc(5px * 4); }
 #bfzridhbue .gt_indent_5 { text-indent: calc(5px * 5); }
 #bfzridhbue .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bfzridhbue .gt_row_group_first td { border-top-width: 2px; }
 #bfzridhbue .gt_row_group_first th { border-top-width: 2px; }
 #bfzridhbue .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bfzridhbue .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bfzridhbue .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bfzridhbue .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bfzridhbue .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bfzridhbue .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bfzridhbue .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bfzridhbue .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bfzridhbue .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bfzridhbue .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bfzridhbue .gt_left { text-align: left; }
 #bfzridhbue .gt_center { text-align: center; }
 #bfzridhbue .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bfzridhbue .gt_font_normal { font-weight: normal; }
 #bfzridhbue .gt_font_bold { font-weight: bold; }
 #bfzridhbue .gt_font_italic { font-style: italic; }
 #bfzridhbue .gt_super { font-size: 65%; }
 #bfzridhbue .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bfzridhbue .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bfzridhbue .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bfzridhbue .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bfzridhbue .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bfzridhbue .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" style="width:100%;" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations from the early hours of May 1, 2023</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="2" id="Time" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Time</th>
<th colspan="4" id="Measurement" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Measurement</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp,<br />
°C</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind,<br />
m s<sup>−1</sup></th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Pressure,<br />
hPa</th>
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
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">02:50</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.7</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">03:20</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">7.2</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">03:50</td>
<td class="gt_row gt_right">17.8</td>
<td class="gt_row gt_right">0.73</td>
<td class="gt_row gt_right">6.3</td>
<td class="gt_row gt_right">1013.5</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">04:20</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.64</td>
<td class="gt_row gt_right">4.0</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right">2023-05-01</td>
<td class="gt_row gt_right">04:50</td>
<td class="gt_row gt_right">18.9</td>
<td class="gt_row gt_right">0.64</td>
<td class="gt_row gt_right">3.1</td>
<td class="gt_row gt_right">1014.6</td>
</tr>
</tbody>
</table>


Column order matters because readers scan left to right. Placing the most important or identifying columns first improves usability. In many tables, time or context columns work well on the left, with measurements and results on the right. This mirrors how people naturally ask questions about data: "when and where" before "what happened."

Note that even though columns were moved using [cols_move_to_start()](../reference/GT.cols_move_to_start.md#great_tables.GT.cols_move_to_start), the *spanner column labels* still spanned above the correct *column labels*. There are a number of methods on [GT](../reference/GT.md#great_tables.GT) to move columns, including [cols_move()](../reference/GT.cols_move.md#great_tables.GT.cols_move), [cols_move_to_end()](../reference/GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end). And there's even a method to hide columns: [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide).

Multiple columns can be renamed in a single use of [cols_label()](../reference/GT.cols_label.md#great_tables.GT.cols_label). Further to this, the helper functions [md()](../reference/md.md#great_tables.md) and [html()](../reference/html.md#great_tables.html) can be used to create column labels with additional styling. In the above example, we provided column labels as HTML so that we can insert linebreaks with `<br>`, insert a superscripted `−1` (with `<sup>−1</sup>`), and insert a degree symbol as an HTML entity (`°`).


# Targeting Columns for `columns=`

In the above examples, we selected columns to span or move using a list of column names (as strings). However, **Great Tables** supports a wide range of ways to select columns.

For example, you can use a lambda function:


``` python
(
    GT(gibraltar_mini)
    .cols_move_to_start(columns=lambda colname: colname.startswith("wind"))
)
```


<style>
#kkwvuqwfcf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kkwvuqwfcf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kkwvuqwfcf p { margin: 0; padding: 0; }
 #kkwvuqwfcf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kkwvuqwfcf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kkwvuqwfcf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kkwvuqwfcf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kkwvuqwfcf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkwvuqwfcf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkwvuqwfcf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkwvuqwfcf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kkwvuqwfcf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kkwvuqwfcf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kkwvuqwfcf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kkwvuqwfcf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kkwvuqwfcf .gt_spanner_row { border-bottom-style: hidden; }
 #kkwvuqwfcf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kkwvuqwfcf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kkwvuqwfcf .gt_from_md> :first-child { margin-top: 0; }
 #kkwvuqwfcf .gt_from_md> :last-child { margin-bottom: 0; }
 #kkwvuqwfcf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kkwvuqwfcf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kkwvuqwfcf .gt_indent_1 { text-indent: 5px; }
 #kkwvuqwfcf .gt_indent_2 { text-indent: calc(5px * 2); }
 #kkwvuqwfcf .gt_indent_3 { text-indent: calc(5px * 3); }
 #kkwvuqwfcf .gt_indent_4 { text-indent: calc(5px * 4); }
 #kkwvuqwfcf .gt_indent_5 { text-indent: calc(5px * 5); }
 #kkwvuqwfcf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kkwvuqwfcf .gt_row_group_first td { border-top-width: 2px; }
 #kkwvuqwfcf .gt_row_group_first th { border-top-width: 2px; }
 #kkwvuqwfcf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kkwvuqwfcf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkwvuqwfcf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkwvuqwfcf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kkwvuqwfcf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkwvuqwfcf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkwvuqwfcf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kkwvuqwfcf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kkwvuqwfcf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkwvuqwfcf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkwvuqwfcf .gt_left { text-align: left; }
 #kkwvuqwfcf .gt_center { text-align: center; }
 #kkwvuqwfcf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kkwvuqwfcf .gt_font_normal { font-weight: normal; }
 #kkwvuqwfcf .gt_font_bold { font-weight: bold; }
 #kkwvuqwfcf .gt_font_italic { font-style: italic; }
 #kkwvuqwfcf .gt_super { font-size: 65%; }
 #kkwvuqwfcf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkwvuqwfcf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kkwvuqwfcf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkwvuqwfcf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkwvuqwfcf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kkwvuqwfcf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| wind_speed | temp | humidity | pressure | date       | time  |
|------------|------|----------|----------|------------|-------|
| 6.7        | 18.9 | 0.68     | 1015.2   | 2023-05-01 | 00:20 |
| 7.2        | 18.9 | 0.73     | 1015.2   | 2023-05-01 | 00:50 |
| 6.7        | 17.8 | 0.77     | 1014.6   | 2023-05-01 | 01:20 |
| 6.7        | 18.9 | 0.73     | 1014.6   | 2023-05-01 | 01:50 |
| 6.7        | 18.9 | 0.68     | 1014.6   | 2023-05-01 | 02:20 |
| 6.7        | 17.8 | 0.73     | 1014.6   | 2023-05-01 | 02:50 |
| 7.2        | 17.8 | 0.73     | 1014.6   | 2023-05-01 | 03:20 |
| 6.3        | 17.8 | 0.73     | 1013.5   | 2023-05-01 | 03:50 |
| 4.0        | 18.9 | 0.64     | 1014.6   | 2023-05-01 | 04:20 |
| 3.1        | 18.9 | 0.64     | 1014.6   | 2023-05-01 | 04:50 |


Inputs like strings, integers, and polars selectors are also supported. For more information, see [Column Selection](column-selection.md).

Between spanners, relabeling, and reordering, you have full control over how your column labels communicate the structure of your data. These tools let you transform raw DataFrame column names into polished, informative headers that guide readers through the table.
