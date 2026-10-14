# Styling the Table Body

Visual styling helps draw attention to important values and makes patterns in your data easier to spot. **Great Tables** provides a flexible system for applying fills, borders, and text styles to cells in the table body. This page covers the fundamentals of cell-level styling, from targeting specific cells to using column values and expressions to drive dynamic styles.

Targeted styling is most effective when used sparingly to draw attention to specific values (outliers, thresholds, or key comparisons). Overusing color and borders can make a table harder to read rather than easier. A good rule of thumb: if everything is highlighted, nothing is. Start with the most important insight you want the reader to take away, and style just enough to guide their eye there.

**Great Tables** can add styles (like color, text properties, and borders) on many different parts of the displayed table. The following set of examples shows how to set styles on the body of table, where the data cells are located.

For the examples on this page, we'll use the included [gibraltar](../reference/data.gibraltar.md#great_tables.data.gibraltar) weather dataset to set up [GT](../reference/GT.md#great_tables.GT) objects for both **Pandas** and **Polars** DataFrames.


``` python
import polars as pl
from great_tables import GT, from_column, style, loc
from great_tables.data import gibraltar

weather_head = gibraltar.head()[["date", "time", "temp", "humidity", "wind_speed", "pressure"]]

gt_weather = GT(weather_head)
gt_pl_weather = GT(pl.from_pandas(weather_head))
```


> **Note: Note**
>
> When using Great Tables with VS Code, the IDE suppresses some forms of table styling displayed in notebooks. For example, border styles might not appear. Use `.show("browser")` to see the styled GT table in a separate browser window.


# Style basics

We use the [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) method in combination with [loc.body()](../reference/loc.body.md#great_tables.loc.body) to set styles on cells of data in the table body. For example, the table-making code below applies a yellow background color to specific cells.


``` python
gt_weather.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(columns="temp", rows=[1, 2])
)
```


<style>
#siiadlwlvy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#siiadlwlvy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#siiadlwlvy p { margin: 0; padding: 0; }
 #siiadlwlvy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #siiadlwlvy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #siiadlwlvy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #siiadlwlvy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #siiadlwlvy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #siiadlwlvy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #siiadlwlvy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #siiadlwlvy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #siiadlwlvy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #siiadlwlvy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #siiadlwlvy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #siiadlwlvy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #siiadlwlvy .gt_spanner_row { border-bottom-style: hidden; }
 #siiadlwlvy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #siiadlwlvy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #siiadlwlvy .gt_from_md> :first-child { margin-top: 0; }
 #siiadlwlvy .gt_from_md> :last-child { margin-bottom: 0; }
 #siiadlwlvy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #siiadlwlvy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #siiadlwlvy .gt_indent_1 { text-indent: 5px; }
 #siiadlwlvy .gt_indent_2 { text-indent: calc(5px * 2); }
 #siiadlwlvy .gt_indent_3 { text-indent: calc(5px * 3); }
 #siiadlwlvy .gt_indent_4 { text-indent: calc(5px * 4); }
 #siiadlwlvy .gt_indent_5 { text-indent: calc(5px * 5); }
 #siiadlwlvy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #siiadlwlvy .gt_row_group_first td { border-top-width: 2px; }
 #siiadlwlvy .gt_row_group_first th { border-top-width: 2px; }
 #siiadlwlvy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #siiadlwlvy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #siiadlwlvy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #siiadlwlvy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #siiadlwlvy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #siiadlwlvy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #siiadlwlvy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #siiadlwlvy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #siiadlwlvy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #siiadlwlvy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #siiadlwlvy .gt_left { text-align: left; }
 #siiadlwlvy .gt_center { text-align: center; }
 #siiadlwlvy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #siiadlwlvy .gt_font_normal { font-weight: normal; }
 #siiadlwlvy .gt_font_bold { font-weight: bold; }
 #siiadlwlvy .gt_font_italic { font-style: italic; }
 #siiadlwlvy .gt_super { font-size: 65%; }
 #siiadlwlvy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #siiadlwlvy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #siiadlwlvy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #siiadlwlvy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #siiadlwlvy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #siiadlwlvy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


There are two important arguments to [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style): `style=` and `locations=`. We are calling a specific function for each of these:

- [style.fill()](../reference/style.fill.md#great_tables.style.fill): the type of style to apply. In this case the *fill* (or background color).
- [loc.body()](../reference/loc.body.md#great_tables.loc.body): the area we want to style. In this case, it's the table body with specific columns and rows specified.

In addition to [style.fill()](../reference/style.fill.md#great_tables.style.fill), several other styling functions exist. We'll look at styling borders and text in the following sections.


## Customizing Borders

Let's use [style.borders()](../reference/style.borders.md#great_tables.style.borders) to place borders around targeted cells. In this next example, the table has a red dashed border above two rows.


``` python
gt_weather.tab_style(
    style=style.borders(sides="top", color="red", style="dashed", weight="3px"),
    locations=loc.body(rows=[1, 2])
)
```


<style>
#ankirkcdlx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ankirkcdlx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ankirkcdlx p { margin: 0; padding: 0; }
 #ankirkcdlx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ankirkcdlx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ankirkcdlx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ankirkcdlx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ankirkcdlx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ankirkcdlx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ankirkcdlx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ankirkcdlx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ankirkcdlx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ankirkcdlx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ankirkcdlx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ankirkcdlx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ankirkcdlx .gt_spanner_row { border-bottom-style: hidden; }
 #ankirkcdlx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ankirkcdlx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ankirkcdlx .gt_from_md> :first-child { margin-top: 0; }
 #ankirkcdlx .gt_from_md> :last-child { margin-bottom: 0; }
 #ankirkcdlx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ankirkcdlx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ankirkcdlx .gt_indent_1 { text-indent: 5px; }
 #ankirkcdlx .gt_indent_2 { text-indent: calc(5px * 2); }
 #ankirkcdlx .gt_indent_3 { text-indent: calc(5px * 3); }
 #ankirkcdlx .gt_indent_4 { text-indent: calc(5px * 4); }
 #ankirkcdlx .gt_indent_5 { text-indent: calc(5px * 5); }
 #ankirkcdlx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ankirkcdlx .gt_row_group_first td { border-top-width: 2px; }
 #ankirkcdlx .gt_row_group_first th { border-top-width: 2px; }
 #ankirkcdlx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ankirkcdlx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ankirkcdlx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ankirkcdlx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ankirkcdlx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ankirkcdlx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ankirkcdlx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ankirkcdlx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ankirkcdlx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ankirkcdlx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ankirkcdlx .gt_left { text-align: left; }
 #ankirkcdlx .gt_center { text-align: center; }
 #ankirkcdlx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ankirkcdlx .gt_font_normal { font-weight: normal; }
 #ankirkcdlx .gt_font_bold { font-weight: bold; }
 #ankirkcdlx .gt_font_italic { font-style: italic; }
 #ankirkcdlx .gt_super { font-size: 65%; }
 #ankirkcdlx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ankirkcdlx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ankirkcdlx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ankirkcdlx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ankirkcdlx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ankirkcdlx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


The red dashed border appears above rows 1 and 2, providing a visual separator. You can control the side (`"top"`, `"bottom"`, `"left"`, `"right"`), color, style, and weight of the border.


## Customizing Text

We can style text with by using the [style.text()](../reference/style.text.md#great_tables.style.text) function. This gives us many customization possibilities for any text we target. For example, the `humidity` column below has green, bolded text in a custom font.


``` python
gt_weather.tab_style(
    style=style.text(color="green", font="Times New Roman", weight="bold"),
    locations=loc.body(columns="humidity")
)
```


<style>
#abcjdwapsl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#abcjdwapsl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#abcjdwapsl p { margin: 0; padding: 0; }
 #abcjdwapsl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #abcjdwapsl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #abcjdwapsl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #abcjdwapsl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #abcjdwapsl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #abcjdwapsl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #abcjdwapsl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #abcjdwapsl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #abcjdwapsl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #abcjdwapsl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #abcjdwapsl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #abcjdwapsl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #abcjdwapsl .gt_spanner_row { border-bottom-style: hidden; }
 #abcjdwapsl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #abcjdwapsl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #abcjdwapsl .gt_from_md> :first-child { margin-top: 0; }
 #abcjdwapsl .gt_from_md> :last-child { margin-bottom: 0; }
 #abcjdwapsl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #abcjdwapsl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #abcjdwapsl .gt_indent_1 { text-indent: 5px; }
 #abcjdwapsl .gt_indent_2 { text-indent: calc(5px * 2); }
 #abcjdwapsl .gt_indent_3 { text-indent: calc(5px * 3); }
 #abcjdwapsl .gt_indent_4 { text-indent: calc(5px * 4); }
 #abcjdwapsl .gt_indent_5 { text-indent: calc(5px * 5); }
 #abcjdwapsl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #abcjdwapsl .gt_row_group_first td { border-top-width: 2px; }
 #abcjdwapsl .gt_row_group_first th { border-top-width: 2px; }
 #abcjdwapsl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #abcjdwapsl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #abcjdwapsl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #abcjdwapsl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #abcjdwapsl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #abcjdwapsl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #abcjdwapsl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #abcjdwapsl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #abcjdwapsl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #abcjdwapsl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #abcjdwapsl .gt_left { text-align: left; }
 #abcjdwapsl .gt_center { text-align: center; }
 #abcjdwapsl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #abcjdwapsl .gt_font_normal { font-weight: normal; }
 #abcjdwapsl .gt_font_bold { font-weight: bold; }
 #abcjdwapsl .gt_font_italic { font-style: italic; }
 #abcjdwapsl .gt_super { font-size: 65%; }
 #abcjdwapsl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #abcjdwapsl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #abcjdwapsl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #abcjdwapsl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #abcjdwapsl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #abcjdwapsl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


The `humidity` column text appears in green, bold, and in the Times New Roman font. The [style.text()](../reference/style.text.md#great_tables.style.text) function supports additional options like `size=`, `style=` (italic), and `decorate=` (underline, line-through).


# Column-based Styles

In addition to setting styles to specific values (e.g., a `"yellow"` background fill), you can also use parameter values from table columns to specify styles. The way to do this is to use the [from_column()](../reference/from_column.md#great_tables.from_column) helper function to access those values.

Column-based styling is powerful because it lets the data itself drive the visual presentation. Instead of manually specifying which cells to highlight, you define a rule and let it apply automatically. This is especially valuable for tables that are regenerated with updated data, since the styling adapts without any code changes.


``` python
df = pl.DataFrame({"x": [1, 2], "background": ["lightyellow", "lightblue"]})

(
    GT(df)
    .tab_style(
        style=style.fill(color=from_column(column="background")),
        locations=loc.body(columns="x")
    )
)
```


<style>
#owbgbtwlfo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#owbgbtwlfo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#owbgbtwlfo p { margin: 0; padding: 0; }
 #owbgbtwlfo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #owbgbtwlfo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #owbgbtwlfo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #owbgbtwlfo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #owbgbtwlfo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #owbgbtwlfo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #owbgbtwlfo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #owbgbtwlfo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #owbgbtwlfo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #owbgbtwlfo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #owbgbtwlfo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #owbgbtwlfo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #owbgbtwlfo .gt_spanner_row { border-bottom-style: hidden; }
 #owbgbtwlfo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #owbgbtwlfo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #owbgbtwlfo .gt_from_md> :first-child { margin-top: 0; }
 #owbgbtwlfo .gt_from_md> :last-child { margin-bottom: 0; }
 #owbgbtwlfo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #owbgbtwlfo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #owbgbtwlfo .gt_indent_1 { text-indent: 5px; }
 #owbgbtwlfo .gt_indent_2 { text-indent: calc(5px * 2); }
 #owbgbtwlfo .gt_indent_3 { text-indent: calc(5px * 3); }
 #owbgbtwlfo .gt_indent_4 { text-indent: calc(5px * 4); }
 #owbgbtwlfo .gt_indent_5 { text-indent: calc(5px * 5); }
 #owbgbtwlfo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #owbgbtwlfo .gt_row_group_first td { border-top-width: 2px; }
 #owbgbtwlfo .gt_row_group_first th { border-top-width: 2px; }
 #owbgbtwlfo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #owbgbtwlfo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #owbgbtwlfo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #owbgbtwlfo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #owbgbtwlfo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #owbgbtwlfo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #owbgbtwlfo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #owbgbtwlfo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #owbgbtwlfo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #owbgbtwlfo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #owbgbtwlfo .gt_left { text-align: left; }
 #owbgbtwlfo .gt_center { text-align: center; }
 #owbgbtwlfo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #owbgbtwlfo .gt_font_normal { font-weight: normal; }
 #owbgbtwlfo .gt_font_bold { font-weight: bold; }
 #owbgbtwlfo .gt_font_italic { font-style: italic; }
 #owbgbtwlfo .gt_super { font-size: 65%; }
 #owbgbtwlfo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #owbgbtwlfo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #owbgbtwlfo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #owbgbtwlfo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #owbgbtwlfo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #owbgbtwlfo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| x   | background  |
|-----|-------------|
| 1   | lightyellow |
| 2   | lightblue   |


Notice that in the code above, we used values from the `background` column to specify the fill color for each styled row.

In the next few sections, we'll first show how this combines nicely with the [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide) method, then, we'll demonstrate how to use **Polars** expressions to do everything much more simply.


## Combining Styling with [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide)

One common approach is to specify a style from a column, and then hide that column in the final output. For example, we can add a background column to our [gibraltar](../reference/data.gibraltar.md#great_tables.data.gibraltar) data:


``` python
color_map = {
    True: "lightyellow",
    False: "lightblue"
}

with_color = weather_head.assign(
    background=(weather_head["temp"] > 18.5).replace(color_map)
)

with_color
```


|     | date       | time  | temp | humidity | wind_speed | pressure | background  |
|-----|------------|-------|------|----------|------------|----------|-------------|
| 0   | 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   | lightyellow |
| 1   | 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   | lightyellow |
| 2   | 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   | lightblue   |
| 3   | 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   | lightyellow |
| 4   | 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   | lightyellow |


Notice that the dataset now has a `background` column set to either `"lightyellow"` or `"lightblue"`, depending on whether `temp` is above `18.5`.

We can then use this `background` column to set the fill color of certain body cells, and then hide the `background` column since we don't need that in our finalized display table:


``` python
(
    GT(with_color)
    .tab_style(
        style=style.fill(color=from_column(column="background")),
        locations=loc.body(columns="temp")
    )
    .cols_hide(columns="background")
)
```


<style>
#tgsqrnygui table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tgsqrnygui thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tgsqrnygui p { margin: 0; padding: 0; }
 #tgsqrnygui .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tgsqrnygui .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tgsqrnygui .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tgsqrnygui .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tgsqrnygui .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tgsqrnygui .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgsqrnygui .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tgsqrnygui .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tgsqrnygui .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tgsqrnygui .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tgsqrnygui .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tgsqrnygui .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tgsqrnygui .gt_spanner_row { border-bottom-style: hidden; }
 #tgsqrnygui .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tgsqrnygui .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tgsqrnygui .gt_from_md> :first-child { margin-top: 0; }
 #tgsqrnygui .gt_from_md> :last-child { margin-bottom: 0; }
 #tgsqrnygui .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tgsqrnygui .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tgsqrnygui .gt_indent_1 { text-indent: 5px; }
 #tgsqrnygui .gt_indent_2 { text-indent: calc(5px * 2); }
 #tgsqrnygui .gt_indent_3 { text-indent: calc(5px * 3); }
 #tgsqrnygui .gt_indent_4 { text-indent: calc(5px * 4); }
 #tgsqrnygui .gt_indent_5 { text-indent: calc(5px * 5); }
 #tgsqrnygui .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tgsqrnygui .gt_row_group_first td { border-top-width: 2px; }
 #tgsqrnygui .gt_row_group_first th { border-top-width: 2px; }
 #tgsqrnygui .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tgsqrnygui .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgsqrnygui .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tgsqrnygui .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tgsqrnygui .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgsqrnygui .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tgsqrnygui .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tgsqrnygui .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tgsqrnygui .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgsqrnygui .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tgsqrnygui .gt_left { text-align: left; }
 #tgsqrnygui .gt_center { text-align: center; }
 #tgsqrnygui .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tgsqrnygui .gt_font_normal { font-weight: normal; }
 #tgsqrnygui .gt_font_bold { font-weight: bold; }
 #tgsqrnygui .gt_font_italic { font-style: italic; }
 #tgsqrnygui .gt_super { font-size: 65%; }
 #tgsqrnygui .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgsqrnygui .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tgsqrnygui .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgsqrnygui .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tgsqrnygui .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tgsqrnygui .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


Note the two methods used above:

- [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style): uses [from_column()](../reference/from_column.md#great_tables.from_column) to set the color using the values of the `background` column.
- [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide): prevents the `background` column from being displayed in the output.


## Using **Polars** expressions

Styles can also be specified using **Polars** expressions. For example, the code below uses the `temp` column to set color to `"lightyellow"` or `"lightblue"`.


``` python
# A Polars expression defines color based on `temp`
temp_color = (
    pl.when(pl.col("temp") > 18.5)
    .then(pl.lit("lightyellow"))
    .otherwise(pl.lit("lightblue"))
)

gt_pl_weather.tab_style(
    style=style.fill(color=temp_color),
    locations=loc.body("temp")
)
```


<style>
#nlqzpwevou table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nlqzpwevou thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nlqzpwevou p { margin: 0; padding: 0; }
 #nlqzpwevou .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nlqzpwevou .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nlqzpwevou .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nlqzpwevou .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nlqzpwevou .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nlqzpwevou .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nlqzpwevou .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nlqzpwevou .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nlqzpwevou .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nlqzpwevou .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nlqzpwevou .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nlqzpwevou .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nlqzpwevou .gt_spanner_row { border-bottom-style: hidden; }
 #nlqzpwevou .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nlqzpwevou .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nlqzpwevou .gt_from_md> :first-child { margin-top: 0; }
 #nlqzpwevou .gt_from_md> :last-child { margin-bottom: 0; }
 #nlqzpwevou .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nlqzpwevou .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nlqzpwevou .gt_indent_1 { text-indent: 5px; }
 #nlqzpwevou .gt_indent_2 { text-indent: calc(5px * 2); }
 #nlqzpwevou .gt_indent_3 { text-indent: calc(5px * 3); }
 #nlqzpwevou .gt_indent_4 { text-indent: calc(5px * 4); }
 #nlqzpwevou .gt_indent_5 { text-indent: calc(5px * 5); }
 #nlqzpwevou .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nlqzpwevou .gt_row_group_first td { border-top-width: 2px; }
 #nlqzpwevou .gt_row_group_first th { border-top-width: 2px; }
 #nlqzpwevou .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nlqzpwevou .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nlqzpwevou .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nlqzpwevou .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nlqzpwevou .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nlqzpwevou .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nlqzpwevou .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nlqzpwevou .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nlqzpwevou .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nlqzpwevou .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nlqzpwevou .gt_left { text-align: left; }
 #nlqzpwevou .gt_center { text-align: center; }
 #nlqzpwevou .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nlqzpwevou .gt_font_normal { font-weight: normal; }
 #nlqzpwevou .gt_font_bold { font-weight: bold; }
 #nlqzpwevou .gt_font_italic { font-style: italic; }
 #nlqzpwevou .gt_super { font-size: 65%; }
 #nlqzpwevou .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nlqzpwevou .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nlqzpwevou .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nlqzpwevou .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nlqzpwevou .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nlqzpwevou .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


The Polars expression evaluates per row and produces a color string for each cell. This approach avoids creating and hiding an extra column, keeping the code concise.

Each of the three approaches ([from_column()](../reference/from_column.md#great_tables.from_column) with [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide), Polars expressions, and functions) has its strengths. Polars expressions are the most concise for Polars DataFrames and keep the styling logic self-contained. The [from_column()](../reference/from_column.md#great_tables.from_column) approach works with both Pandas and Polars backends but requires an extra column. Functions are the most flexible option for Pandas workflows. Choose whichever matches your data library and preference.


## Using functions

You can also use a function, that takes the DataFrame and returns a Series with a style value for each row.

This is shown below on a pandas DataFrame.


``` python
def map_color(df):
    return (df["temp"] > 18.5).map(
        {True: "lightyellow", False: "lightblue"}
    )

gt_weather.tab_style(
    style=style.fill(
        color=map_color),
    locations=loc.body("temp")
)
```


<style>
#vekmxvdjfh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vekmxvdjfh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vekmxvdjfh p { margin: 0; padding: 0; }
 #vekmxvdjfh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vekmxvdjfh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vekmxvdjfh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vekmxvdjfh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vekmxvdjfh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vekmxvdjfh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vekmxvdjfh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vekmxvdjfh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vekmxvdjfh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vekmxvdjfh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vekmxvdjfh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vekmxvdjfh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vekmxvdjfh .gt_spanner_row { border-bottom-style: hidden; }
 #vekmxvdjfh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vekmxvdjfh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vekmxvdjfh .gt_from_md> :first-child { margin-top: 0; }
 #vekmxvdjfh .gt_from_md> :last-child { margin-bottom: 0; }
 #vekmxvdjfh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vekmxvdjfh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vekmxvdjfh .gt_indent_1 { text-indent: 5px; }
 #vekmxvdjfh .gt_indent_2 { text-indent: calc(5px * 2); }
 #vekmxvdjfh .gt_indent_3 { text-indent: calc(5px * 3); }
 #vekmxvdjfh .gt_indent_4 { text-indent: calc(5px * 4); }
 #vekmxvdjfh .gt_indent_5 { text-indent: calc(5px * 5); }
 #vekmxvdjfh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vekmxvdjfh .gt_row_group_first td { border-top-width: 2px; }
 #vekmxvdjfh .gt_row_group_first th { border-top-width: 2px; }
 #vekmxvdjfh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vekmxvdjfh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vekmxvdjfh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vekmxvdjfh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vekmxvdjfh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vekmxvdjfh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vekmxvdjfh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vekmxvdjfh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vekmxvdjfh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vekmxvdjfh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vekmxvdjfh .gt_left { text-align: left; }
 #vekmxvdjfh .gt_center { text-align: center; }
 #vekmxvdjfh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vekmxvdjfh .gt_font_normal { font-weight: normal; }
 #vekmxvdjfh .gt_font_bold { font-weight: bold; }
 #vekmxvdjfh .gt_font_italic { font-style: italic; }
 #vekmxvdjfh .gt_super { font-size: 65%; }
 #vekmxvdjfh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vekmxvdjfh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vekmxvdjfh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vekmxvdjfh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vekmxvdjfh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vekmxvdjfh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


The function receives the full DataFrame and returns a Series of color values aligned with the rows. This pattern works well with Pandas when you want to derive styles from data logic without Polars expressions.


# Specifying columns and rows


## Using polars selectors

If you are using **Polars**, you can use column selectors and expressions for selecting specific columns and rows:


``` python
import polars.selectors as cs

gt_pl_weather.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(
        columns=cs.starts_with("Te"),
        rows=pl.col("temp") > 18.5
    )
)
```


<style>
#bmthtvusev table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bmthtvusev thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bmthtvusev p { margin: 0; padding: 0; }
 #bmthtvusev .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bmthtvusev .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bmthtvusev .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bmthtvusev .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bmthtvusev .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bmthtvusev .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bmthtvusev .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bmthtvusev .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bmthtvusev .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bmthtvusev .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bmthtvusev .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bmthtvusev .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bmthtvusev .gt_spanner_row { border-bottom-style: hidden; }
 #bmthtvusev .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bmthtvusev .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bmthtvusev .gt_from_md> :first-child { margin-top: 0; }
 #bmthtvusev .gt_from_md> :last-child { margin-bottom: 0; }
 #bmthtvusev .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bmthtvusev .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bmthtvusev .gt_indent_1 { text-indent: 5px; }
 #bmthtvusev .gt_indent_2 { text-indent: calc(5px * 2); }
 #bmthtvusev .gt_indent_3 { text-indent: calc(5px * 3); }
 #bmthtvusev .gt_indent_4 { text-indent: calc(5px * 4); }
 #bmthtvusev .gt_indent_5 { text-indent: calc(5px * 5); }
 #bmthtvusev .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bmthtvusev .gt_row_group_first td { border-top-width: 2px; }
 #bmthtvusev .gt_row_group_first th { border-top-width: 2px; }
 #bmthtvusev .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bmthtvusev .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bmthtvusev .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bmthtvusev .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bmthtvusev .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bmthtvusev .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bmthtvusev .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bmthtvusev .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bmthtvusev .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bmthtvusev .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bmthtvusev .gt_left { text-align: left; }
 #bmthtvusev .gt_center { text-align: center; }
 #bmthtvusev .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bmthtvusev .gt_font_normal { font-weight: normal; }
 #bmthtvusev .gt_font_bold { font-weight: bold; }
 #bmthtvusev .gt_font_italic { font-style: italic; }
 #bmthtvusev .gt_super { font-size: 65%; }
 #bmthtvusev .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bmthtvusev .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bmthtvusev .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bmthtvusev .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bmthtvusev .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bmthtvusev .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


See [Column Selection](column-selection.md) for details on selecting columns.


## Using a function

For tools like **pandas**, you can use a function (or lambda) to select rows. The function should take a DataFrame, and output a boolean Series.


``` python
gt_weather.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(
        columns=lambda col_name: col_name.startswith("Te"),
        rows=lambda D: D["temp"] > 18.5,
    )
)
```


<style>
#rtbwjmvrad table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rtbwjmvrad thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rtbwjmvrad p { margin: 0; padding: 0; }
 #rtbwjmvrad .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rtbwjmvrad .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rtbwjmvrad .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rtbwjmvrad .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rtbwjmvrad .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rtbwjmvrad .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rtbwjmvrad .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rtbwjmvrad .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rtbwjmvrad .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rtbwjmvrad .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rtbwjmvrad .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rtbwjmvrad .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rtbwjmvrad .gt_spanner_row { border-bottom-style: hidden; }
 #rtbwjmvrad .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rtbwjmvrad .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rtbwjmvrad .gt_from_md> :first-child { margin-top: 0; }
 #rtbwjmvrad .gt_from_md> :last-child { margin-bottom: 0; }
 #rtbwjmvrad .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rtbwjmvrad .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rtbwjmvrad .gt_indent_1 { text-indent: 5px; }
 #rtbwjmvrad .gt_indent_2 { text-indent: calc(5px * 2); }
 #rtbwjmvrad .gt_indent_3 { text-indent: calc(5px * 3); }
 #rtbwjmvrad .gt_indent_4 { text-indent: calc(5px * 4); }
 #rtbwjmvrad .gt_indent_5 { text-indent: calc(5px * 5); }
 #rtbwjmvrad .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rtbwjmvrad .gt_row_group_first td { border-top-width: 2px; }
 #rtbwjmvrad .gt_row_group_first th { border-top-width: 2px; }
 #rtbwjmvrad .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rtbwjmvrad .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rtbwjmvrad .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rtbwjmvrad .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rtbwjmvrad .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rtbwjmvrad .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rtbwjmvrad .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rtbwjmvrad .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rtbwjmvrad .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rtbwjmvrad .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rtbwjmvrad .gt_left { text-align: left; }
 #rtbwjmvrad .gt_center { text-align: center; }
 #rtbwjmvrad .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rtbwjmvrad .gt_font_normal { font-weight: normal; }
 #rtbwjmvrad .gt_font_bold { font-weight: bold; }
 #rtbwjmvrad .gt_font_italic { font-style: italic; }
 #rtbwjmvrad .gt_super { font-size: 65%; }
 #rtbwjmvrad .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rtbwjmvrad .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rtbwjmvrad .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rtbwjmvrad .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rtbwjmvrad .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rtbwjmvrad .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


The function-based row selection gives you full flexibility: any callable that takes a DataFrame and returns a boolean Series can serve as a row filter.


# Multiple styles and locations

We can use a list within `style=` to apply multiple styles at once. For example, the code below sets fill and border styles on the same set of body cells.


``` python
gt_weather.tab_style(
    style=[style.fill(color="yellow"), style.borders(sides="all")],
    locations=loc.body(columns="temp", rows=[1, 2]),
)
```


<style>
#bvptwjvqfc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bvptwjvqfc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bvptwjvqfc p { margin: 0; padding: 0; }
 #bvptwjvqfc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bvptwjvqfc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bvptwjvqfc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bvptwjvqfc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bvptwjvqfc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bvptwjvqfc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bvptwjvqfc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bvptwjvqfc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bvptwjvqfc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bvptwjvqfc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bvptwjvqfc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bvptwjvqfc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bvptwjvqfc .gt_spanner_row { border-bottom-style: hidden; }
 #bvptwjvqfc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bvptwjvqfc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bvptwjvqfc .gt_from_md> :first-child { margin-top: 0; }
 #bvptwjvqfc .gt_from_md> :last-child { margin-bottom: 0; }
 #bvptwjvqfc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bvptwjvqfc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bvptwjvqfc .gt_indent_1 { text-indent: 5px; }
 #bvptwjvqfc .gt_indent_2 { text-indent: calc(5px * 2); }
 #bvptwjvqfc .gt_indent_3 { text-indent: calc(5px * 3); }
 #bvptwjvqfc .gt_indent_4 { text-indent: calc(5px * 4); }
 #bvptwjvqfc .gt_indent_5 { text-indent: calc(5px * 5); }
 #bvptwjvqfc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bvptwjvqfc .gt_row_group_first td { border-top-width: 2px; }
 #bvptwjvqfc .gt_row_group_first th { border-top-width: 2px; }
 #bvptwjvqfc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bvptwjvqfc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bvptwjvqfc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bvptwjvqfc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bvptwjvqfc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bvptwjvqfc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bvptwjvqfc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bvptwjvqfc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bvptwjvqfc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bvptwjvqfc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bvptwjvqfc .gt_left { text-align: left; }
 #bvptwjvqfc .gt_center { text-align: center; }
 #bvptwjvqfc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bvptwjvqfc .gt_font_normal { font-weight: normal; }
 #bvptwjvqfc .gt_font_bold { font-weight: bold; }
 #bvptwjvqfc .gt_font_italic { font-style: italic; }
 #bvptwjvqfc .gt_super { font-size: 65%; }
 #bvptwjvqfc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bvptwjvqfc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bvptwjvqfc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bvptwjvqfc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bvptwjvqfc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bvptwjvqfc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


Note that you can also pass a list to `locations=`!


``` python
gt_weather.tab_style(
    style=style.fill(color="yellow"),
    locations=[
        loc.body(columns="temp", rows=[1, 2]),
        loc.body(columns="wind_speed", rows=[0])
    ]
)
```


<style>
#enmszthxuh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#enmszthxuh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#enmszthxuh p { margin: 0; padding: 0; }
 #enmszthxuh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #enmszthxuh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #enmszthxuh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #enmszthxuh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #enmszthxuh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #enmszthxuh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #enmszthxuh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #enmszthxuh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #enmszthxuh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #enmszthxuh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #enmszthxuh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #enmszthxuh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #enmszthxuh .gt_spanner_row { border-bottom-style: hidden; }
 #enmszthxuh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #enmszthxuh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #enmszthxuh .gt_from_md> :first-child { margin-top: 0; }
 #enmszthxuh .gt_from_md> :last-child { margin-bottom: 0; }
 #enmszthxuh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #enmszthxuh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #enmszthxuh .gt_indent_1 { text-indent: 5px; }
 #enmszthxuh .gt_indent_2 { text-indent: calc(5px * 2); }
 #enmszthxuh .gt_indent_3 { text-indent: calc(5px * 3); }
 #enmszthxuh .gt_indent_4 { text-indent: calc(5px * 4); }
 #enmszthxuh .gt_indent_5 { text-indent: calc(5px * 5); }
 #enmszthxuh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #enmszthxuh .gt_row_group_first td { border-top-width: 2px; }
 #enmszthxuh .gt_row_group_first th { border-top-width: 2px; }
 #enmszthxuh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #enmszthxuh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #enmszthxuh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #enmszthxuh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #enmszthxuh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #enmszthxuh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #enmszthxuh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #enmszthxuh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #enmszthxuh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #enmszthxuh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #enmszthxuh .gt_left { text-align: left; }
 #enmszthxuh .gt_center { text-align: center; }
 #enmszthxuh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #enmszthxuh .gt_font_normal { font-weight: normal; }
 #enmszthxuh .gt_font_bold { font-weight: bold; }
 #enmszthxuh .gt_font_italic { font-style: italic; }
 #enmszthxuh .gt_super { font-size: 65%; }
 #enmszthxuh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #enmszthxuh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #enmszthxuh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #enmszthxuh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #enmszthxuh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #enmszthxuh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


You can also combine **Polars** selectors with a row filtering expression, in order to select a combination of columns and rows.


``` python
import polars.selectors as cs

gt_pl_weather.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(
        columns=cs.exclude(["date", "time"]),
        rows=pl.col("temp") == pl.col("temp").max()
    )
)
```


<style>
#zcyjzvwarv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zcyjzvwarv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zcyjzvwarv p { margin: 0; padding: 0; }
 #zcyjzvwarv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zcyjzvwarv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zcyjzvwarv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zcyjzvwarv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zcyjzvwarv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zcyjzvwarv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zcyjzvwarv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zcyjzvwarv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zcyjzvwarv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zcyjzvwarv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zcyjzvwarv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zcyjzvwarv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zcyjzvwarv .gt_spanner_row { border-bottom-style: hidden; }
 #zcyjzvwarv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zcyjzvwarv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zcyjzvwarv .gt_from_md> :first-child { margin-top: 0; }
 #zcyjzvwarv .gt_from_md> :last-child { margin-bottom: 0; }
 #zcyjzvwarv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zcyjzvwarv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zcyjzvwarv .gt_indent_1 { text-indent: 5px; }
 #zcyjzvwarv .gt_indent_2 { text-indent: calc(5px * 2); }
 #zcyjzvwarv .gt_indent_3 { text-indent: calc(5px * 3); }
 #zcyjzvwarv .gt_indent_4 { text-indent: calc(5px * 4); }
 #zcyjzvwarv .gt_indent_5 { text-indent: calc(5px * 5); }
 #zcyjzvwarv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zcyjzvwarv .gt_row_group_first td { border-top-width: 2px; }
 #zcyjzvwarv .gt_row_group_first th { border-top-width: 2px; }
 #zcyjzvwarv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zcyjzvwarv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zcyjzvwarv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zcyjzvwarv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zcyjzvwarv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zcyjzvwarv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zcyjzvwarv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zcyjzvwarv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zcyjzvwarv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zcyjzvwarv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zcyjzvwarv .gt_left { text-align: left; }
 #zcyjzvwarv .gt_center { text-align: center; }
 #zcyjzvwarv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zcyjzvwarv .gt_font_normal { font-weight: normal; }
 #zcyjzvwarv .gt_font_bold { font-weight: bold; }
 #zcyjzvwarv .gt_font_italic { font-style: italic; }
 #zcyjzvwarv .gt_super { font-size: 65%; }
 #zcyjzvwarv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zcyjzvwarv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zcyjzvwarv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zcyjzvwarv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zcyjzvwarv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zcyjzvwarv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


Lastly, you can use **Polars** selectors or expressions to conditionally select rows on a per-column basis.


``` python
import polars.selectors as cs

gt_pl_weather.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(mask=cs.numeric().eq(cs.numeric().max())),
)
```


<style>
#sfzvbzduht table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sfzvbzduht thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sfzvbzduht p { margin: 0; padding: 0; }
 #sfzvbzduht .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sfzvbzduht .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sfzvbzduht .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sfzvbzduht .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sfzvbzduht .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sfzvbzduht .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sfzvbzduht .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sfzvbzduht .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sfzvbzduht .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sfzvbzduht .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sfzvbzduht .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sfzvbzduht .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sfzvbzduht .gt_spanner_row { border-bottom-style: hidden; }
 #sfzvbzduht .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sfzvbzduht .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sfzvbzduht .gt_from_md> :first-child { margin-top: 0; }
 #sfzvbzduht .gt_from_md> :last-child { margin-bottom: 0; }
 #sfzvbzduht .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sfzvbzduht .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sfzvbzduht .gt_indent_1 { text-indent: 5px; }
 #sfzvbzduht .gt_indent_2 { text-indent: calc(5px * 2); }
 #sfzvbzduht .gt_indent_3 { text-indent: calc(5px * 3); }
 #sfzvbzduht .gt_indent_4 { text-indent: calc(5px * 4); }
 #sfzvbzduht .gt_indent_5 { text-indent: calc(5px * 5); }
 #sfzvbzduht .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sfzvbzduht .gt_row_group_first td { border-top-width: 2px; }
 #sfzvbzduht .gt_row_group_first th { border-top-width: 2px; }
 #sfzvbzduht .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sfzvbzduht .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sfzvbzduht .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sfzvbzduht .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sfzvbzduht .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sfzvbzduht .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sfzvbzduht .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sfzvbzduht .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sfzvbzduht .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sfzvbzduht .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sfzvbzduht .gt_left { text-align: left; }
 #sfzvbzduht .gt_center { text-align: center; }
 #sfzvbzduht .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sfzvbzduht .gt_font_normal { font-weight: normal; }
 #sfzvbzduht .gt_font_bold { font-weight: bold; }
 #sfzvbzduht .gt_font_italic { font-style: italic; }
 #sfzvbzduht .gt_super { font-size: 65%; }
 #sfzvbzduht .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sfzvbzduht .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sfzvbzduht .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sfzvbzduht .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sfzvbzduht .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sfzvbzduht .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time  | temp | humidity | wind_speed | pressure |
|------------|-------|------|----------|------------|----------|
| 2023-05-01 | 00:20 | 18.9 | 0.68     | 6.7        | 1015.2   |
| 2023-05-01 | 00:50 | 18.9 | 0.73     | 7.2        | 1015.2   |
| 2023-05-01 | 01:20 | 17.8 | 0.77     | 6.7        | 1014.6   |
| 2023-05-01 | 01:50 | 18.9 | 0.73     | 6.7        | 1014.6   |
| 2023-05-01 | 02:20 | 18.9 | 0.68     | 6.7        | 1014.6   |


The `mask=` argument applies row/column logic jointly, highlighting only the cells where a column's value equals its own maximum (here, among the numeric columns). This is a powerful way to perform per-column conditional formatting in a single statement.


# Value-driven styling with [tab_style_body()](../reference/GT.tab_style_body.md#great_tables.GT.tab_style_body)

While [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) targets cells by their *position* (specific rows and columns), [tab_style_body()](../reference/GT.tab_style_body.md#great_tables.GT.tab_style_body) targets cells by their *values*. This is useful when you want to style cells that meet a condition without having to figure out which rows and columns contain those values ahead of time.

Three matching strategies are available, in order of precedence:

1.  `fn=`: a predicate function that receives each cell's value and returns `True` or `False`
2.  `pattern=`: a regex matched against the string representation of each cell
3.  `values=`: a list of exact values to match


## Highlighting specific values

The simplest use case involves passing a list of values, where any cell containing one of those values gets styled.


``` python
from great_tables import style, exibble

(
    GT(exibble[["num", "char", "currency", "row", "group"]], rowname_col="row", groupname_col="group")
    .tab_style_body(
        style=style.fill(color="orange"),
        values=[49.95, 33.33],
    )
)
```


<style>
#emgkzzaipw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#emgkzzaipw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#emgkzzaipw p { margin: 0; padding: 0; }
 #emgkzzaipw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #emgkzzaipw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #emgkzzaipw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #emgkzzaipw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #emgkzzaipw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #emgkzzaipw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #emgkzzaipw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #emgkzzaipw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #emgkzzaipw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #emgkzzaipw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #emgkzzaipw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #emgkzzaipw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #emgkzzaipw .gt_spanner_row { border-bottom-style: hidden; }
 #emgkzzaipw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #emgkzzaipw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #emgkzzaipw .gt_from_md> :first-child { margin-top: 0; }
 #emgkzzaipw .gt_from_md> :last-child { margin-bottom: 0; }
 #emgkzzaipw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #emgkzzaipw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #emgkzzaipw .gt_indent_1 { text-indent: 5px; }
 #emgkzzaipw .gt_indent_2 { text-indent: calc(5px * 2); }
 #emgkzzaipw .gt_indent_3 { text-indent: calc(5px * 3); }
 #emgkzzaipw .gt_indent_4 { text-indent: calc(5px * 4); }
 #emgkzzaipw .gt_indent_5 { text-indent: calc(5px * 5); }
 #emgkzzaipw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #emgkzzaipw .gt_row_group_first td { border-top-width: 2px; }
 #emgkzzaipw .gt_row_group_first th { border-top-width: 2px; }
 #emgkzzaipw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #emgkzzaipw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #emgkzzaipw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #emgkzzaipw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #emgkzzaipw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #emgkzzaipw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #emgkzzaipw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #emgkzzaipw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #emgkzzaipw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #emgkzzaipw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #emgkzzaipw .gt_left { text-align: left; }
 #emgkzzaipw .gt_center { text-align: center; }
 #emgkzzaipw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #emgkzzaipw .gt_font_normal { font-weight: normal; }
 #emgkzzaipw .gt_font_bold { font-weight: bold; }
 #emgkzzaipw .gt_font_italic { font-style: italic; }
 #emgkzzaipw .gt_super { font-size: 65%; }
 #emgkzzaipw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #emgkzzaipw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #emgkzzaipw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #emgkzzaipw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #emgkzzaipw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #emgkzzaipw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" style="background-color: orange" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: orange" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


## Using a predicate function

For more flexibility, pass a function to `fn=`. The function receives the raw cell value and should return `True` to apply the style. Missing values (`NaN` in Pandas) are normalized to `None` before being passed to your function, so `x is None` works reliably.


``` python
(
    GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
    )
    .tab_style_body(
        style=style.text(color="red"),
        fn=lambda x: x is None,
    )
    .sub_missing(missing_text="NA")
)
```


<style>
#undzdqocrc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#undzdqocrc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#undzdqocrc p { margin: 0; padding: 0; }
 #undzdqocrc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #undzdqocrc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #undzdqocrc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #undzdqocrc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #undzdqocrc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #undzdqocrc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #undzdqocrc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #undzdqocrc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #undzdqocrc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #undzdqocrc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #undzdqocrc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #undzdqocrc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #undzdqocrc .gt_spanner_row { border-bottom-style: hidden; }
 #undzdqocrc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #undzdqocrc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #undzdqocrc .gt_from_md> :first-child { margin-top: 0; }
 #undzdqocrc .gt_from_md> :last-child { margin-bottom: 0; }
 #undzdqocrc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #undzdqocrc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #undzdqocrc .gt_indent_1 { text-indent: 5px; }
 #undzdqocrc .gt_indent_2 { text-indent: calc(5px * 2); }
 #undzdqocrc .gt_indent_3 { text-indent: calc(5px * 3); }
 #undzdqocrc .gt_indent_4 { text-indent: calc(5px * 4); }
 #undzdqocrc .gt_indent_5 { text-indent: calc(5px * 5); }
 #undzdqocrc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #undzdqocrc .gt_row_group_first td { border-top-width: 2px; }
 #undzdqocrc .gt_row_group_first th { border-top-width: 2px; }
 #undzdqocrc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #undzdqocrc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #undzdqocrc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #undzdqocrc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #undzdqocrc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #undzdqocrc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #undzdqocrc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #undzdqocrc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #undzdqocrc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #undzdqocrc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #undzdqocrc .gt_left { text-align: left; }
 #undzdqocrc .gt_center { text-align: center; }
 #undzdqocrc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #undzdqocrc .gt_font_normal { font-weight: normal; }
 #undzdqocrc .gt_font_bold { font-weight: bold; }
 #undzdqocrc .gt_font_italic { font-style: italic; }
 #undzdqocrc .gt_super { font-size: 65%; }
 #undzdqocrc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #undzdqocrc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #undzdqocrc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #undzdqocrc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #undzdqocrc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #undzdqocrc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" style="color: red" headers="grp_b stub-5 char">NA</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" style="color: red" headers="grp_b stub-6 num">NA</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" style="color: red" headers="grp_b stub-7 currency">NA</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


The predicate function is the most flexible option. Here we style all numeric cells with a value under 50:


``` python
(
    GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
    )
    .tab_style_body(
        style=style.fill(color="lightgreen"),
        fn=lambda x: x >= 0 and x < 50,
    )
)
```


<style>
#xhcbvhvwtq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xhcbvhvwtq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xhcbvhvwtq p { margin: 0; padding: 0; }
 #xhcbvhvwtq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xhcbvhvwtq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xhcbvhvwtq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xhcbvhvwtq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xhcbvhvwtq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xhcbvhvwtq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xhcbvhvwtq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xhcbvhvwtq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xhcbvhvwtq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xhcbvhvwtq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xhcbvhvwtq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xhcbvhvwtq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xhcbvhvwtq .gt_spanner_row { border-bottom-style: hidden; }
 #xhcbvhvwtq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xhcbvhvwtq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xhcbvhvwtq .gt_from_md> :first-child { margin-top: 0; }
 #xhcbvhvwtq .gt_from_md> :last-child { margin-bottom: 0; }
 #xhcbvhvwtq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xhcbvhvwtq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xhcbvhvwtq .gt_indent_1 { text-indent: 5px; }
 #xhcbvhvwtq .gt_indent_2 { text-indent: calc(5px * 2); }
 #xhcbvhvwtq .gt_indent_3 { text-indent: calc(5px * 3); }
 #xhcbvhvwtq .gt_indent_4 { text-indent: calc(5px * 4); }
 #xhcbvhvwtq .gt_indent_5 { text-indent: calc(5px * 5); }
 #xhcbvhvwtq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xhcbvhvwtq .gt_row_group_first td { border-top-width: 2px; }
 #xhcbvhvwtq .gt_row_group_first th { border-top-width: 2px; }
 #xhcbvhvwtq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xhcbvhvwtq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xhcbvhvwtq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xhcbvhvwtq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xhcbvhvwtq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xhcbvhvwtq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xhcbvhvwtq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xhcbvhvwtq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xhcbvhvwtq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xhcbvhvwtq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xhcbvhvwtq .gt_left { text-align: left; }
 #xhcbvhvwtq .gt_center { text-align: center; }
 #xhcbvhvwtq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xhcbvhvwtq .gt_font_normal { font-weight: normal; }
 #xhcbvhvwtq .gt_font_bold { font-weight: bold; }
 #xhcbvhvwtq .gt_font_italic { font-style: italic; }
 #xhcbvhvwtq .gt_super { font-size: 65%; }
 #xhcbvhvwtq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xhcbvhvwtq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xhcbvhvwtq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xhcbvhvwtq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xhcbvhvwtq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xhcbvhvwtq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightgreen" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" style="background-color: lightgreen" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: lightgreen" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" style="background-color: lightgreen" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: lightgreen" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" style="background-color: lightgreen" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" style="background-color: lightgreen" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" style="background-color: lightgreen" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


If the function raises an exception for a cell (e.g., comparing a string with `>=`), that cell is silently skipped.


## Using a regex pattern

The `pattern=` argument matches against the string representation of each cell. `None` values are skipped.


``` python
(
    GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
    )
    .tab_style_body(
        style=style.fill(color="lightyellow"),
        pattern="^[a-d]",
    )
)
```


<style>
#cvplzhqsrg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cvplzhqsrg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cvplzhqsrg p { margin: 0; padding: 0; }
 #cvplzhqsrg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cvplzhqsrg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cvplzhqsrg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cvplzhqsrg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cvplzhqsrg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cvplzhqsrg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvplzhqsrg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cvplzhqsrg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cvplzhqsrg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cvplzhqsrg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cvplzhqsrg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cvplzhqsrg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cvplzhqsrg .gt_spanner_row { border-bottom-style: hidden; }
 #cvplzhqsrg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cvplzhqsrg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cvplzhqsrg .gt_from_md> :first-child { margin-top: 0; }
 #cvplzhqsrg .gt_from_md> :last-child { margin-bottom: 0; }
 #cvplzhqsrg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cvplzhqsrg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cvplzhqsrg .gt_indent_1 { text-indent: 5px; }
 #cvplzhqsrg .gt_indent_2 { text-indent: calc(5px * 2); }
 #cvplzhqsrg .gt_indent_3 { text-indent: calc(5px * 3); }
 #cvplzhqsrg .gt_indent_4 { text-indent: calc(5px * 4); }
 #cvplzhqsrg .gt_indent_5 { text-indent: calc(5px * 5); }
 #cvplzhqsrg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cvplzhqsrg .gt_row_group_first td { border-top-width: 2px; }
 #cvplzhqsrg .gt_row_group_first th { border-top-width: 2px; }
 #cvplzhqsrg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cvplzhqsrg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvplzhqsrg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cvplzhqsrg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cvplzhqsrg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cvplzhqsrg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cvplzhqsrg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cvplzhqsrg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cvplzhqsrg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvplzhqsrg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cvplzhqsrg .gt_left { text-align: left; }
 #cvplzhqsrg .gt_center { text-align: center; }
 #cvplzhqsrg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cvplzhqsrg .gt_font_normal { font-weight: normal; }
 #cvplzhqsrg .gt_font_bold { font-weight: bold; }
 #cvplzhqsrg .gt_font_italic { font-style: italic; }
 #cvplzhqsrg .gt_super { font-size: 65%; }
 #cvplzhqsrg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvplzhqsrg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cvplzhqsrg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cvplzhqsrg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cvplzhqsrg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cvplzhqsrg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" style="background-color: lightyellow" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" style="background-color: lightyellow" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" style="background-color: lightyellow" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" style="background-color: lightyellow" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


## Scoping with `columns=` and `rows=`

You can restrict which cells are considered for matching by providing `columns=` and `rows=`, exactly as you would with [loc.body()](../reference/loc.body.md#great_tables.loc.body).


``` python
(
    GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
    )
    .tab_style_body(
        style=style.fill(color="lightcyan"),
        fn=lambda x: x >= 0 and x < 50,
        columns="num",
    )
)
```


<style>
#ksgtbhlsyo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ksgtbhlsyo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ksgtbhlsyo p { margin: 0; padding: 0; }
 #ksgtbhlsyo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ksgtbhlsyo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ksgtbhlsyo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ksgtbhlsyo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ksgtbhlsyo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ksgtbhlsyo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksgtbhlsyo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ksgtbhlsyo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ksgtbhlsyo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ksgtbhlsyo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ksgtbhlsyo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ksgtbhlsyo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ksgtbhlsyo .gt_spanner_row { border-bottom-style: hidden; }
 #ksgtbhlsyo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ksgtbhlsyo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ksgtbhlsyo .gt_from_md> :first-child { margin-top: 0; }
 #ksgtbhlsyo .gt_from_md> :last-child { margin-bottom: 0; }
 #ksgtbhlsyo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ksgtbhlsyo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ksgtbhlsyo .gt_indent_1 { text-indent: 5px; }
 #ksgtbhlsyo .gt_indent_2 { text-indent: calc(5px * 2); }
 #ksgtbhlsyo .gt_indent_3 { text-indent: calc(5px * 3); }
 #ksgtbhlsyo .gt_indent_4 { text-indent: calc(5px * 4); }
 #ksgtbhlsyo .gt_indent_5 { text-indent: calc(5px * 5); }
 #ksgtbhlsyo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ksgtbhlsyo .gt_row_group_first td { border-top-width: 2px; }
 #ksgtbhlsyo .gt_row_group_first th { border-top-width: 2px; }
 #ksgtbhlsyo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ksgtbhlsyo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksgtbhlsyo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ksgtbhlsyo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ksgtbhlsyo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksgtbhlsyo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ksgtbhlsyo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ksgtbhlsyo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ksgtbhlsyo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksgtbhlsyo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ksgtbhlsyo .gt_left { text-align: left; }
 #ksgtbhlsyo .gt_center { text-align: center; }
 #ksgtbhlsyo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ksgtbhlsyo .gt_font_normal { font-weight: normal; }
 #ksgtbhlsyo .gt_font_bold { font-weight: bold; }
 #ksgtbhlsyo .gt_font_italic { font-style: italic; }
 #ksgtbhlsyo .gt_super { font-size: 65%; }
 #ksgtbhlsyo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksgtbhlsyo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ksgtbhlsyo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksgtbhlsyo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ksgtbhlsyo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ksgtbhlsyo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightcyan" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: lightcyan" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: lightcyan" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


## Expanding matches with `targets=`

By default, only the matched cell itself is styled (`targets="cell"`). You can expand the styling to entire rows or columns that contain a match:

- `targets="row"`: style the full row of each match
- `targets="column"`: style the full column of each match
- `targets=["row", "column"]`: both


``` python
(
    GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
    )
    .tab_style_body(
        style=style.fill(color="lightblue"),
        values=[49.95],
        targets="row",
    )
    .tab_style_body(
        style=style.fill(color="bisque"),
        values=[33.33],
        targets="column",
    )
)
```


<style>
#vtpjxlexdh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vtpjxlexdh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vtpjxlexdh p { margin: 0; padding: 0; }
 #vtpjxlexdh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vtpjxlexdh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vtpjxlexdh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vtpjxlexdh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vtpjxlexdh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vtpjxlexdh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vtpjxlexdh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vtpjxlexdh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vtpjxlexdh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vtpjxlexdh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vtpjxlexdh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vtpjxlexdh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vtpjxlexdh .gt_spanner_row { border-bottom-style: hidden; }
 #vtpjxlexdh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vtpjxlexdh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vtpjxlexdh .gt_from_md> :first-child { margin-top: 0; }
 #vtpjxlexdh .gt_from_md> :last-child { margin-bottom: 0; }
 #vtpjxlexdh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vtpjxlexdh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vtpjxlexdh .gt_indent_1 { text-indent: 5px; }
 #vtpjxlexdh .gt_indent_2 { text-indent: calc(5px * 2); }
 #vtpjxlexdh .gt_indent_3 { text-indent: calc(5px * 3); }
 #vtpjxlexdh .gt_indent_4 { text-indent: calc(5px * 4); }
 #vtpjxlexdh .gt_indent_5 { text-indent: calc(5px * 5); }
 #vtpjxlexdh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vtpjxlexdh .gt_row_group_first td { border-top-width: 2px; }
 #vtpjxlexdh .gt_row_group_first th { border-top-width: 2px; }
 #vtpjxlexdh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vtpjxlexdh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vtpjxlexdh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vtpjxlexdh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vtpjxlexdh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vtpjxlexdh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vtpjxlexdh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vtpjxlexdh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vtpjxlexdh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vtpjxlexdh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vtpjxlexdh .gt_left { text-align: left; }
 #vtpjxlexdh .gt_center { text-align: center; }
 #vtpjxlexdh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vtpjxlexdh .gt_font_normal { font-weight: normal; }
 #vtpjxlexdh .gt_font_bold { font-weight: bold; }
 #vtpjxlexdh .gt_font_italic { font-style: italic; }
 #vtpjxlexdh .gt_super { font-size: 65%; }
 #vtpjxlexdh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vtpjxlexdh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vtpjxlexdh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vtpjxlexdh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vtpjxlexdh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vtpjxlexdh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightblue; background-color: bisque" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" style="background-color: lightblue" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" style="background-color: lightblue" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: bisque" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: bisque" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" style="background-color: bisque" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" style="background-color: bisque" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" style="background-color: bisque" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" style="background-color: bisque" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" style="background-color: bisque" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


## Projecting into the stub with `extents=`

When your table has a stub (row labels), you can extend the styling into it with `extents=["body", "stub"]`. This is especially useful with `targets="row"` to highlight an entire row including its label.


``` python
(
    GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
    )
    .tab_style_body(
        style=style.fill(color="lightblue"),
        values=[49.95],
        targets="row",
        extents=["body", "stub"],
    )
)
```


<style>
#jxeifbihza table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jxeifbihza thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jxeifbihza p { margin: 0; padding: 0; }
 #jxeifbihza .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jxeifbihza .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jxeifbihza .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jxeifbihza .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jxeifbihza .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jxeifbihza .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jxeifbihza .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jxeifbihza .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jxeifbihza .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jxeifbihza .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jxeifbihza .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jxeifbihza .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jxeifbihza .gt_spanner_row { border-bottom-style: hidden; }
 #jxeifbihza .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jxeifbihza .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jxeifbihza .gt_from_md> :first-child { margin-top: 0; }
 #jxeifbihza .gt_from_md> :last-child { margin-bottom: 0; }
 #jxeifbihza .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jxeifbihza .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jxeifbihza .gt_indent_1 { text-indent: 5px; }
 #jxeifbihza .gt_indent_2 { text-indent: calc(5px * 2); }
 #jxeifbihza .gt_indent_3 { text-indent: calc(5px * 3); }
 #jxeifbihza .gt_indent_4 { text-indent: calc(5px * 4); }
 #jxeifbihza .gt_indent_5 { text-indent: calc(5px * 5); }
 #jxeifbihza .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jxeifbihza .gt_row_group_first td { border-top-width: 2px; }
 #jxeifbihza .gt_row_group_first th { border-top-width: 2px; }
 #jxeifbihza .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jxeifbihza .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jxeifbihza .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jxeifbihza .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jxeifbihza .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jxeifbihza .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jxeifbihza .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jxeifbihza .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jxeifbihza .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jxeifbihza .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jxeifbihza .gt_left { text-align: left; }
 #jxeifbihza .gt_center { text-align: center; }
 #jxeifbihza .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jxeifbihza .gt_font_normal { font-weight: normal; }
 #jxeifbihza .gt_font_bold { font-weight: bold; }
 #jxeifbihza .gt_font_italic { font-style: italic; }
 #jxeifbihza .gt_super { font-size: 65%; }
 #jxeifbihza .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jxeifbihza .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jxeifbihza .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jxeifbihza .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jxeifbihza .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jxeifbihza .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" style="background-color: lightblue" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightblue" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" style="background-color: lightblue" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_right" style="background-color: lightblue" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody>
</table>


# Learning more

The combination of [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style), [tab_style_body()](../reference/GT.tab_style_body.md#great_tables.GT.tab_style_body), location specifiers, and the various style functions gives you precise control over the visual presentation of your table body. Whether you are highlighting outliers, applying conditional formatting, or using column-driven styles, these tools let you communicate data insights through visual cues that complement the numeric values themselves.

For further reference, consult the API documentation:

- API Docs:
  - [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style)
  - [tab_style_body()](../reference/GT.tab_style_body.md#great_tables.GT.tab_style_body)
  - [`style.*` and `loc.*` functions](../reference/index.md#location-targeting-and-styling-classes)
  - [from_column()](../reference/from_column.md#great_tables.from_column)
