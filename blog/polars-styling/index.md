# Great Tables: The Polars DataFrame Styler of Your Dreams

Analyzing data with polars is a no-brainer in python. It provides an intuitive, expressive interface to data. When it comes to reports, it's trivial to plug polars into plotting libraries like seaborn, plotly, and plotnine.

However, there are fewer options for styling tables for presentation. You could convert from polars to pandas, and use the [built-in pandas DataFrame styler](https://pandas.pydata.org/docs/user_guide/style.html), but this has one major limitation: you can't use polars expressions.

As it turns out, polars expressions make styling tables very straightforward. The same polars code that you would use to select or filter combines with Great Tables to highlight, circle, or bolden text.

In this post, I'll show how Great Tables uses polars expressions to make delightful tables, like the one below.


Code

``` python
import polars as pl
import polars.selectors as cs

from great_tables import GT, md, html, style, loc
from great_tables.data import airquality

airquality_mini = airquality.head(10).assign(Year = 1973)
pl_airquality = pl.DataFrame(airquality_mini).select(
    "Year", "Month", "Day", "Ozone", "Solar_R", "Wind", "Temp"
)
gt_air = GT(pl_airquality)

(
    gt_air

    # Table header ----
    .tab_header(
        title = "New York Air Quality Measurements",
        subtitle = "Daily measurements in New York City (May 1-10, 1973)"
    )

    # Table column spanners ----
    .tab_spanner(
        label = "Time",
        columns = ["Year", "Month", "Day"]
    )
    .tab_spanner(
        label = "Measurement",
        columns = ["Ozone", "Solar_R", "Wind", "Temp"]
    )
    .cols_label(
        Ozone = html("Ozone,<br>ppbV"),
        Solar_R = html("Solar R.,<br>cal/m<sup>2</sup>"),
        Wind = html("Wind,<br>mph"),
        Temp = html("Temp,<br>°F")
    )

    # Table styles ----
    .tab_style(
        style.fill("lightyellow"),
        loc.body(
            columns = cs.all(),
            rows = pl.col("Wind") == pl.col("Wind").max()
        )
    )
    .tab_style(
        style.text(weight = "bold"),
        loc.body("Wind", pl.col("Wind") == pl.col("Wind").max())
    )
)
```


<style>
#bhbelunqwz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bhbelunqwz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bhbelunqwz p { margin: 0; padding: 0; }
 #bhbelunqwz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bhbelunqwz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bhbelunqwz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bhbelunqwz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bhbelunqwz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhbelunqwz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhbelunqwz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bhbelunqwz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bhbelunqwz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bhbelunqwz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bhbelunqwz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bhbelunqwz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bhbelunqwz .gt_spanner_row { border-bottom-style: hidden; }
 #bhbelunqwz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bhbelunqwz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bhbelunqwz .gt_from_md> :first-child { margin-top: 0; }
 #bhbelunqwz .gt_from_md> :last-child { margin-bottom: 0; }
 #bhbelunqwz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bhbelunqwz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bhbelunqwz .gt_indent_1 { text-indent: 5px; }
 #bhbelunqwz .gt_indent_2 { text-indent: calc(5px * 2); }
 #bhbelunqwz .gt_indent_3 { text-indent: calc(5px * 3); }
 #bhbelunqwz .gt_indent_4 { text-indent: calc(5px * 4); }
 #bhbelunqwz .gt_indent_5 { text-indent: calc(5px * 5); }
 #bhbelunqwz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bhbelunqwz .gt_row_group_first td { border-top-width: 2px; }
 #bhbelunqwz .gt_row_group_first th { border-top-width: 2px; }
 #bhbelunqwz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bhbelunqwz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhbelunqwz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhbelunqwz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bhbelunqwz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bhbelunqwz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bhbelunqwz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bhbelunqwz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bhbelunqwz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhbelunqwz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhbelunqwz .gt_left { text-align: left; }
 #bhbelunqwz .gt_center { text-align: center; }
 #bhbelunqwz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bhbelunqwz .gt_font_normal { font-weight: normal; }
 #bhbelunqwz .gt_font_bold { font-weight: bold; }
 #bhbelunqwz .gt_font_italic { font-style: italic; }
 #bhbelunqwz .gt_super { font-size: 65%; }
 #bhbelunqwz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhbelunqwz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bhbelunqwz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bhbelunqwz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bhbelunqwz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bhbelunqwz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" style="width:100%;" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">New York Air Quality Measurements</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements in New York City (May 1-10, 1973)</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="3" id="Time" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Time</th>
<th colspan="4" id="Measurement" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Measurement</th>
</tr>
<tr class="gt_col_headings">
<th id="Year" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Year</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone,<br />
ppbV</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar R.,<br />
cal/m<sup>2</sup></th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind,<br />
mph</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp,<br />
°F</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">6</td>
<td class="gt_row gt_right">28.0</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.9</td>
<td class="gt_row gt_right">66</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">7</td>
<td class="gt_row gt_right">23.0</td>
<td class="gt_row gt_right">299.0</td>
<td class="gt_row gt_right">8.6</td>
<td class="gt_row gt_right">65</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right">19.0</td>
<td class="gt_row gt_right">99.0</td>
<td class="gt_row gt_right">13.8</td>
<td class="gt_row gt_right">59</td>
</tr>
<tr>
<td class="gt_row gt_right" style="background-color: lightyellow">1973</td>
<td class="gt_row gt_right" style="background-color: lightyellow">5</td>
<td class="gt_row gt_right" style="background-color: lightyellow">9</td>
<td class="gt_row gt_right" style="background-color: lightyellow">8.0</td>
<td class="gt_row gt_right" style="background-color: lightyellow">19.0</td>
<td class="gt_row gt_right" style="background-color: lightyellow; font-weight: bold">20.1</td>
<td class="gt_row gt_right" style="background-color: lightyellow">61</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">10</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">194.0</td>
<td class="gt_row gt_right">8.6</td>
<td class="gt_row gt_right">69</td>
</tr>
</tbody>
</table>


# The parts of a presentation-ready table

Our example table customized three main parts:

- **Title and subtitle**: User friendly titles and subtitles, describing the data.
- **Column spanners**: Group related columns together with a custom label.
- **Styles**: Highlight rows, columns, or individual cells of data.

This is marked below.


<img src="./table-preview.png" class="img-fluid" />


Let's walk through each piece in order to produce the table below.


# Creating GT object

First, we'll import the necessary libraries, and do a tiny bit of data processing.


``` python
import polars as pl
import polars.selectors as cs

from great_tables import GT
from great_tables.data import airquality

# Note that we'll use the first 5 rows as we build up our code
airquality_mini = airquality.head(5).assign(Year = 1973)
pl_airquality = pl.DataFrame(airquality_mini).select(
    "Year", "Month", "Day", "Ozone", "Solar_R", "Wind", "Temp"
)

pl_airquality
```


shape: (5, 7)

| Year | Month | Day | Ozone | Solar_R | Wind | Temp |
|------|-------|-----|-------|---------|------|------|
| i64  | i64   | i64 | f64   | f64     | f64  | i64  |
| 1973 | 5     | 1   | 41.0  | 190.0   | 7.4  | 67   |
| 1973 | 5     | 2   | 36.0  | 118.0   | 8.0  | 72   |
| 1973 | 5     | 3   | 12.0  | 149.0   | 12.6 | 74   |
| 1973 | 5     | 4   | 18.0  | 313.0   | 11.5 | 62   |
| 1973 | 5     | 5   | null  | null    | 14.3 | 56   |


The default polars output above is really helpful for data analysis! By passing it to the [GT](../../reference/GT.md#great_tables.GT) constructor, we can start getting it ready for presentation.


``` python
gt_air = GT(pl_airquality)

gt_air
```


<style>
#mnhldnvkjn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mnhldnvkjn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mnhldnvkjn p { margin: 0; padding: 0; }
 #mnhldnvkjn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mnhldnvkjn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mnhldnvkjn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mnhldnvkjn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mnhldnvkjn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mnhldnvkjn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mnhldnvkjn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mnhldnvkjn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mnhldnvkjn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mnhldnvkjn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mnhldnvkjn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mnhldnvkjn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mnhldnvkjn .gt_spanner_row { border-bottom-style: hidden; }
 #mnhldnvkjn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mnhldnvkjn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mnhldnvkjn .gt_from_md> :first-child { margin-top: 0; }
 #mnhldnvkjn .gt_from_md> :last-child { margin-bottom: 0; }
 #mnhldnvkjn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mnhldnvkjn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mnhldnvkjn .gt_indent_1 { text-indent: 5px; }
 #mnhldnvkjn .gt_indent_2 { text-indent: calc(5px * 2); }
 #mnhldnvkjn .gt_indent_3 { text-indent: calc(5px * 3); }
 #mnhldnvkjn .gt_indent_4 { text-indent: calc(5px * 4); }
 #mnhldnvkjn .gt_indent_5 { text-indent: calc(5px * 5); }
 #mnhldnvkjn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mnhldnvkjn .gt_row_group_first td { border-top-width: 2px; }
 #mnhldnvkjn .gt_row_group_first th { border-top-width: 2px; }
 #mnhldnvkjn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mnhldnvkjn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mnhldnvkjn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mnhldnvkjn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mnhldnvkjn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mnhldnvkjn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mnhldnvkjn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mnhldnvkjn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mnhldnvkjn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mnhldnvkjn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mnhldnvkjn .gt_left { text-align: left; }
 #mnhldnvkjn .gt_center { text-align: center; }
 #mnhldnvkjn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mnhldnvkjn .gt_font_normal { font-weight: normal; }
 #mnhldnvkjn .gt_font_bold { font-weight: bold; }
 #mnhldnvkjn .gt_font_italic { font-style: italic; }
 #mnhldnvkjn .gt_super { font-size: 65%; }
 #mnhldnvkjn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mnhldnvkjn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mnhldnvkjn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mnhldnvkjn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mnhldnvkjn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mnhldnvkjn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Year | Month | Day | Ozone | Solar_R | Wind | Temp |
|------|-------|-----|-------|---------|------|------|
| 1973 | 5     | 1   | 41.0  | 190.0   | 7.4  | 67   |
| 1973 | 5     | 2   | 36.0  | 118.0   | 8.0  | 72   |
| 1973 | 5     | 3   | 12.0  | 149.0   | 12.6 | 74   |
| 1973 | 5     | 4   | 18.0  | 313.0   | 11.5 | 62   |
| 1973 | 5     | 5   | None  | None    | 14.3 | 56   |


In the next section I'll show setting a title, and then go on to more exciting stuff like styling the body and creating column spanners.


# Set title and subtitle

The simplest method in gt is [GT.tab_header()](../../reference/GT.tab_header.md#great_tables.GT.tab_header), which lets you add a title and subtitle.


``` python
(
    gt_air

    # Table header ----
    .tab_header(
        title = "New York Air Quality Measurements",
        subtitle = "Daily measurements in New York City (May 1-10, 1973)"
    )
)
```


<style>
#rwmeunhuja table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rwmeunhuja thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rwmeunhuja p { margin: 0; padding: 0; }
 #rwmeunhuja .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rwmeunhuja .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rwmeunhuja .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rwmeunhuja .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rwmeunhuja .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rwmeunhuja .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rwmeunhuja .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rwmeunhuja .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rwmeunhuja .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rwmeunhuja .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rwmeunhuja .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rwmeunhuja .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rwmeunhuja .gt_spanner_row { border-bottom-style: hidden; }
 #rwmeunhuja .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rwmeunhuja .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rwmeunhuja .gt_from_md> :first-child { margin-top: 0; }
 #rwmeunhuja .gt_from_md> :last-child { margin-bottom: 0; }
 #rwmeunhuja .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rwmeunhuja .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rwmeunhuja .gt_indent_1 { text-indent: 5px; }
 #rwmeunhuja .gt_indent_2 { text-indent: calc(5px * 2); }
 #rwmeunhuja .gt_indent_3 { text-indent: calc(5px * 3); }
 #rwmeunhuja .gt_indent_4 { text-indent: calc(5px * 4); }
 #rwmeunhuja .gt_indent_5 { text-indent: calc(5px * 5); }
 #rwmeunhuja .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rwmeunhuja .gt_row_group_first td { border-top-width: 2px; }
 #rwmeunhuja .gt_row_group_first th { border-top-width: 2px; }
 #rwmeunhuja .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rwmeunhuja .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rwmeunhuja .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rwmeunhuja .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rwmeunhuja .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rwmeunhuja .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rwmeunhuja .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rwmeunhuja .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rwmeunhuja .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rwmeunhuja .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rwmeunhuja .gt_left { text-align: left; }
 #rwmeunhuja .gt_center { text-align: center; }
 #rwmeunhuja .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rwmeunhuja .gt_font_normal { font-weight: normal; }
 #rwmeunhuja .gt_font_bold { font-weight: bold; }
 #rwmeunhuja .gt_font_italic { font-style: italic; }
 #rwmeunhuja .gt_super { font-size: 65%; }
 #rwmeunhuja .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rwmeunhuja .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rwmeunhuja .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rwmeunhuja .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rwmeunhuja .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rwmeunhuja .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">New York Air Quality Measurements</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements in New York City (May 1-10, 1973)</th>
</tr>
<tr class="gt_col_headings">
<th id="Year" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Year</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R</th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
</tr>
</tbody>
</table>


Just like with plots, tables need titles so people know what they're about!


# Set body styles

The `.tab_style()` method sets styles--like fill color, or text properties--on different parts of the table. Let's use it twice with a polars expression. First to highlight the row corresponding to the max Wind value, and then to bold that value.


``` python
from great_tables import style, loc

is_max_wind = pl.col("Wind") == pl.col("Wind").max()

(
    gt_air

    # Table styles ----
    .tab_style(
        style.fill("lightyellow"),
        loc.body(
            columns = cs.all(),
            rows = is_max_wind
        )
    )
    .tab_style(
        style.text(weight = "bold"),
        loc.body("Wind", is_max_wind)
    )
)
```


<style>
#qtbfddzhro table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qtbfddzhro thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qtbfddzhro p { margin: 0; padding: 0; }
 #qtbfddzhro .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qtbfddzhro .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qtbfddzhro .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qtbfddzhro .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qtbfddzhro .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qtbfddzhro .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qtbfddzhro .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qtbfddzhro .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qtbfddzhro .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qtbfddzhro .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qtbfddzhro .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qtbfddzhro .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qtbfddzhro .gt_spanner_row { border-bottom-style: hidden; }
 #qtbfddzhro .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qtbfddzhro .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qtbfddzhro .gt_from_md> :first-child { margin-top: 0; }
 #qtbfddzhro .gt_from_md> :last-child { margin-bottom: 0; }
 #qtbfddzhro .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qtbfddzhro .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qtbfddzhro .gt_indent_1 { text-indent: 5px; }
 #qtbfddzhro .gt_indent_2 { text-indent: calc(5px * 2); }
 #qtbfddzhro .gt_indent_3 { text-indent: calc(5px * 3); }
 #qtbfddzhro .gt_indent_4 { text-indent: calc(5px * 4); }
 #qtbfddzhro .gt_indent_5 { text-indent: calc(5px * 5); }
 #qtbfddzhro .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qtbfddzhro .gt_row_group_first td { border-top-width: 2px; }
 #qtbfddzhro .gt_row_group_first th { border-top-width: 2px; }
 #qtbfddzhro .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qtbfddzhro .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qtbfddzhro .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qtbfddzhro .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qtbfddzhro .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qtbfddzhro .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qtbfddzhro .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qtbfddzhro .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qtbfddzhro .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qtbfddzhro .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qtbfddzhro .gt_left { text-align: left; }
 #qtbfddzhro .gt_center { text-align: center; }
 #qtbfddzhro .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qtbfddzhro .gt_font_normal { font-weight: normal; }
 #qtbfddzhro .gt_font_bold { font-weight: bold; }
 #qtbfddzhro .gt_font_italic { font-style: italic; }
 #qtbfddzhro .gt_super { font-size: 65%; }
 #qtbfddzhro .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qtbfddzhro .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qtbfddzhro .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qtbfddzhro .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qtbfddzhro .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qtbfddzhro .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Year | Month | Day | Ozone | Solar_R | Wind | Temp |
|------|-------|-----|-------|---------|------|------|
| 1973 | 5     | 1   | 41.0  | 190.0   | 7.4  | 67   |
| 1973 | 5     | 2   | 36.0  | 118.0   | 8.0  | 72   |
| 1973 | 5     | 3   | 12.0  | 149.0   | 12.6 | 74   |
| 1973 | 5     | 4   | 18.0  | 313.0   | 11.5 | 62   |
| 1973 | 5     | 5   | None  | None    | 14.3 | 56   |


Note two important pieces:

- Functions like [style.fill()](../../reference/style.fill.md#great_tables.style.fill) indicate **what** style to set.
- Functions like [loc.body()](../../reference/loc.body.md#great_tables.loc.body) indicate **where** to apply the style. Its `columns=` and `rows=` parameters let you target specific parts of the table body (using polars expressions).

Currently, Great Tables only supports styling the table body. In the (very near) future, other `loc.*` functions will allow styling other parts of the table (e.g. the title, column labels, etc..).

For more details on styles, see [Styling the Table Body](../../user-guide/styling-the-table-body.md) in the User Guide.


# Set column spanners

The last piece to set in the table is the column spanners, which are made up of two things:

- Labels describing groups of columns (e.g. Time, Measurement).
- More readable labels for columns themselves.

Use [GT.tab_spanner()](../../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) to set labels on groups of columns.


``` python
time_cols = ["Year", "Month", "Day"]

gt_with_spanners = (
    gt_air

    # Table column spanners ----
    .tab_spanner(
        label="Time",
        columns=time_cols
    )
    .tab_spanner(
        label="Measurement",
        columns=cs.exclude(time_cols)
    )
)

gt_with_spanners
```


<style>
#jaencubrwl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jaencubrwl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jaencubrwl p { margin: 0; padding: 0; }
 #jaencubrwl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jaencubrwl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jaencubrwl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jaencubrwl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jaencubrwl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jaencubrwl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jaencubrwl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jaencubrwl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jaencubrwl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jaencubrwl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jaencubrwl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jaencubrwl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jaencubrwl .gt_spanner_row { border-bottom-style: hidden; }
 #jaencubrwl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jaencubrwl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jaencubrwl .gt_from_md> :first-child { margin-top: 0; }
 #jaencubrwl .gt_from_md> :last-child { margin-bottom: 0; }
 #jaencubrwl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jaencubrwl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jaencubrwl .gt_indent_1 { text-indent: 5px; }
 #jaencubrwl .gt_indent_2 { text-indent: calc(5px * 2); }
 #jaencubrwl .gt_indent_3 { text-indent: calc(5px * 3); }
 #jaencubrwl .gt_indent_4 { text-indent: calc(5px * 4); }
 #jaencubrwl .gt_indent_5 { text-indent: calc(5px * 5); }
 #jaencubrwl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jaencubrwl .gt_row_group_first td { border-top-width: 2px; }
 #jaencubrwl .gt_row_group_first th { border-top-width: 2px; }
 #jaencubrwl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jaencubrwl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jaencubrwl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jaencubrwl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jaencubrwl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jaencubrwl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jaencubrwl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jaencubrwl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jaencubrwl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jaencubrwl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jaencubrwl .gt_left { text-align: left; }
 #jaencubrwl .gt_center { text-align: center; }
 #jaencubrwl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jaencubrwl .gt_font_normal { font-weight: normal; }
 #jaencubrwl .gt_font_bold { font-weight: bold; }
 #jaencubrwl .gt_font_italic { font-style: italic; }
 #jaencubrwl .gt_super { font-size: 65%; }
 #jaencubrwl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jaencubrwl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jaencubrwl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jaencubrwl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jaencubrwl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jaencubrwl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="3" id="Time" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Time</th>
<th colspan="4" id="Measurement" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Measurement</th>
</tr>
<tr class="gt_col_headings">
<th id="Year" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Year</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar_R</th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
</tr>
</tbody>
</table>


Notice that there are now labels for "Time" and "Measurement" sitting above the column names. This is useful for emphasizing columns that share something in common.

Use `GT.cols_labels()` with [html()](../../reference/html.md#great_tables.html) to create human-friendly labels (e.g. convert things like `cal_m_2` to `cal/m`<sup>`2`</sup>).


``` python
from great_tables import html

(
    gt_with_spanners
    .cols_label(
        Ozone = html("Ozone,<br>ppbV"),
        Solar_R = html("Solar R.,<br>cal/m<sup>2</sup>"),
        Wind = html("Wind,<br>mph"),
        Temp = html("Temp,<br>°F")
    )
)
```


<style>
#ptshrwpvoc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ptshrwpvoc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ptshrwpvoc p { margin: 0; padding: 0; }
 #ptshrwpvoc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ptshrwpvoc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ptshrwpvoc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ptshrwpvoc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ptshrwpvoc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ptshrwpvoc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ptshrwpvoc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ptshrwpvoc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ptshrwpvoc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ptshrwpvoc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ptshrwpvoc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ptshrwpvoc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ptshrwpvoc .gt_spanner_row { border-bottom-style: hidden; }
 #ptshrwpvoc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ptshrwpvoc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ptshrwpvoc .gt_from_md> :first-child { margin-top: 0; }
 #ptshrwpvoc .gt_from_md> :last-child { margin-bottom: 0; }
 #ptshrwpvoc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ptshrwpvoc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ptshrwpvoc .gt_indent_1 { text-indent: 5px; }
 #ptshrwpvoc .gt_indent_2 { text-indent: calc(5px * 2); }
 #ptshrwpvoc .gt_indent_3 { text-indent: calc(5px * 3); }
 #ptshrwpvoc .gt_indent_4 { text-indent: calc(5px * 4); }
 #ptshrwpvoc .gt_indent_5 { text-indent: calc(5px * 5); }
 #ptshrwpvoc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ptshrwpvoc .gt_row_group_first td { border-top-width: 2px; }
 #ptshrwpvoc .gt_row_group_first th { border-top-width: 2px; }
 #ptshrwpvoc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ptshrwpvoc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ptshrwpvoc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ptshrwpvoc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ptshrwpvoc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ptshrwpvoc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ptshrwpvoc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ptshrwpvoc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ptshrwpvoc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ptshrwpvoc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ptshrwpvoc .gt_left { text-align: left; }
 #ptshrwpvoc .gt_center { text-align: center; }
 #ptshrwpvoc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ptshrwpvoc .gt_font_normal { font-weight: normal; }
 #ptshrwpvoc .gt_font_bold { font-weight: bold; }
 #ptshrwpvoc .gt_font_italic { font-style: italic; }
 #ptshrwpvoc .gt_super { font-size: 65%; }
 #ptshrwpvoc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ptshrwpvoc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ptshrwpvoc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ptshrwpvoc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ptshrwpvoc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ptshrwpvoc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" style="width:100%;" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="3" id="Time" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Time</th>
<th colspan="4" id="Measurement" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Measurement</th>
</tr>
<tr class="gt_col_headings">
<th id="Year" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Year</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone,<br />
ppbV</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar R.,<br />
cal/m<sup>2</sup></th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind,<br />
mph</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp,<br />
°F</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
</tr>
</tbody>
</table>


This is helpful because labels are often in a funky format (e.g. `cal_m_2`) because they're easier to work with programmatically, so need to be cleaned up for presentation.

See the [Column Labels](../../user-guide/column-labels.md) page of the guide for more details.


# Putting it all together

Finally, we'll combine everything from the sections above into a single block of code, and use a few more rows of data.


Code

``` python
import polars as pl
import polars.selectors as cs

from great_tables import GT, md, html, style, loc
from great_tables.data import airquality

airquality_mini = airquality.head(10).assign(Year = 1973)
pl_airquality = pl.DataFrame(airquality_mini).select(
    "Year", "Month", "Day", "Ozone", "Solar_R", "Wind", "Temp"
)
gt_air = GT(pl_airquality)

(
    gt_air

    # Table header ----
    .tab_header(
        title = "New York Air Quality Measurements",
        subtitle = "Daily measurements in New York City (May 1-10, 1973)"
    )

    # Table column spanners ----
    .tab_spanner(
        label = "Time",
        columns = ["Year", "Month", "Day"]
    )
    .tab_spanner(
        label = "Measurement",
        columns = ["Ozone", "Solar_R", "Wind", "Temp"]
    )
    .cols_label(
        Ozone = html("Ozone,<br>ppbV"),
        Solar_R = html("Solar R.,<br>cal/m<sup>2</sup>"),
        Wind = html("Wind,<br>mph"),
        Temp = html("Temp,<br>°F")
    )

    # Table styles ----
    .tab_style(
        style.fill("lightyellow"),
        loc.body(
            columns = cs.all(),
            rows = pl.col("Wind") == pl.col("Wind").max()
        )
    )
    .tab_style(
        style.text(weight = "bold"),
        loc.body("Wind", pl.col("Wind") == pl.col("Wind").max())
    )
)
```


<style>
#dffoifouak table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dffoifouak thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dffoifouak p { margin: 0; padding: 0; }
 #dffoifouak .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dffoifouak .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dffoifouak .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dffoifouak .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dffoifouak .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dffoifouak .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dffoifouak .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dffoifouak .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dffoifouak .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dffoifouak .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dffoifouak .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dffoifouak .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dffoifouak .gt_spanner_row { border-bottom-style: hidden; }
 #dffoifouak .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dffoifouak .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dffoifouak .gt_from_md> :first-child { margin-top: 0; }
 #dffoifouak .gt_from_md> :last-child { margin-bottom: 0; }
 #dffoifouak .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dffoifouak .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dffoifouak .gt_indent_1 { text-indent: 5px; }
 #dffoifouak .gt_indent_2 { text-indent: calc(5px * 2); }
 #dffoifouak .gt_indent_3 { text-indent: calc(5px * 3); }
 #dffoifouak .gt_indent_4 { text-indent: calc(5px * 4); }
 #dffoifouak .gt_indent_5 { text-indent: calc(5px * 5); }
 #dffoifouak .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dffoifouak .gt_row_group_first td { border-top-width: 2px; }
 #dffoifouak .gt_row_group_first th { border-top-width: 2px; }
 #dffoifouak .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dffoifouak .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dffoifouak .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dffoifouak .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dffoifouak .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dffoifouak .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dffoifouak .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dffoifouak .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dffoifouak .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dffoifouak .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dffoifouak .gt_left { text-align: left; }
 #dffoifouak .gt_center { text-align: center; }
 #dffoifouak .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dffoifouak .gt_font_normal { font-weight: normal; }
 #dffoifouak .gt_font_bold { font-weight: bold; }
 #dffoifouak .gt_font_italic { font-style: italic; }
 #dffoifouak .gt_super { font-size: 65%; }
 #dffoifouak .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dffoifouak .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dffoifouak .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dffoifouak .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dffoifouak .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dffoifouak .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" style="width:100%;" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">New York Air Quality Measurements</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements in New York City (May 1-10, 1973)</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="3" id="Time" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Time</th>
<th colspan="4" id="Measurement" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Measurement</th>
</tr>
<tr class="gt_col_headings">
<th id="Year" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Year</th>
<th id="Month" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Month</th>
<th id="Day" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Day</th>
<th id="Ozone" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Ozone,<br />
ppbV</th>
<th id="Solar_R" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Solar R.,<br />
cal/m<sup>2</sup></th>
<th id="Wind" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind,<br />
mph</th>
<th id="Temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp,<br />
°F</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">41.0</td>
<td class="gt_row gt_right">190.0</td>
<td class="gt_row gt_right">7.4</td>
<td class="gt_row gt_right">67</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">36.0</td>
<td class="gt_row gt_right">118.0</td>
<td class="gt_row gt_right">8.0</td>
<td class="gt_row gt_right">72</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">12.0</td>
<td class="gt_row gt_right">149.0</td>
<td class="gt_row gt_right">12.6</td>
<td class="gt_row gt_right">74</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">18.0</td>
<td class="gt_row gt_right">313.0</td>
<td class="gt_row gt_right">11.5</td>
<td class="gt_row gt_right">62</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.3</td>
<td class="gt_row gt_right">56</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">6</td>
<td class="gt_row gt_right">28.0</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">14.9</td>
<td class="gt_row gt_right">66</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">7</td>
<td class="gt_row gt_right">23.0</td>
<td class="gt_row gt_right">299.0</td>
<td class="gt_row gt_right">8.6</td>
<td class="gt_row gt_right">65</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right">19.0</td>
<td class="gt_row gt_right">99.0</td>
<td class="gt_row gt_right">13.8</td>
<td class="gt_row gt_right">59</td>
</tr>
<tr>
<td class="gt_row gt_right" style="background-color: lightyellow">1973</td>
<td class="gt_row gt_right" style="background-color: lightyellow">5</td>
<td class="gt_row gt_right" style="background-color: lightyellow">9</td>
<td class="gt_row gt_right" style="background-color: lightyellow">8.0</td>
<td class="gt_row gt_right" style="background-color: lightyellow">19.0</td>
<td class="gt_row gt_right" style="background-color: lightyellow; font-weight: bold">20.1</td>
<td class="gt_row gt_right" style="background-color: lightyellow">61</td>
</tr>
<tr>
<td class="gt_row gt_right">1973</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">10</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">194.0</td>
<td class="gt_row gt_right">8.6</td>
<td class="gt_row gt_right">69</td>
</tr>
</tbody>
</table>


Not too bad!

Table styling is a surprisingly deep topic, and we've only scratched the surface on what Great Tables can do. A big one not covered here is the many [column formatting methods](../../user-guide/formatting-values.md), like [GT.fmt_currency()](../../reference/GT.fmt_currency.md#great_tables.GT.fmt_currency).

Thoughtfully styled tables tell viewers that you care as much about communicating the table, as much as the data wrangling behind it. Working with polars has been an absolute dream, and we're excited to explore different ways it and Great Tables make for easy table styling!
