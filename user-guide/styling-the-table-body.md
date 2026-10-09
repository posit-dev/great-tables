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
#ivmeaucbft table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ivmeaucbft thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ivmeaucbft p { margin: 0; padding: 0; }
 #ivmeaucbft .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ivmeaucbft .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ivmeaucbft .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ivmeaucbft .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ivmeaucbft .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ivmeaucbft .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ivmeaucbft .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ivmeaucbft .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ivmeaucbft .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ivmeaucbft .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ivmeaucbft .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ivmeaucbft .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ivmeaucbft .gt_spanner_row { border-bottom-style: hidden; }
 #ivmeaucbft .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ivmeaucbft .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ivmeaucbft .gt_from_md> :first-child { margin-top: 0; }
 #ivmeaucbft .gt_from_md> :last-child { margin-bottom: 0; }
 #ivmeaucbft .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ivmeaucbft .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ivmeaucbft .gt_indent_1 { text-indent: 5px; }
 #ivmeaucbft .gt_indent_2 { text-indent: calc(5px * 2); }
 #ivmeaucbft .gt_indent_3 { text-indent: calc(5px * 3); }
 #ivmeaucbft .gt_indent_4 { text-indent: calc(5px * 4); }
 #ivmeaucbft .gt_indent_5 { text-indent: calc(5px * 5); }
 #ivmeaucbft .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ivmeaucbft .gt_row_group_first td { border-top-width: 2px; }
 #ivmeaucbft .gt_row_group_first th { border-top-width: 2px; }
 #ivmeaucbft .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ivmeaucbft .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ivmeaucbft .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ivmeaucbft .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ivmeaucbft .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ivmeaucbft .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ivmeaucbft .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ivmeaucbft .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ivmeaucbft .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ivmeaucbft .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ivmeaucbft .gt_left { text-align: left; }
 #ivmeaucbft .gt_center { text-align: center; }
 #ivmeaucbft .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ivmeaucbft .gt_font_normal { font-weight: normal; }
 #ivmeaucbft .gt_font_bold { font-weight: bold; }
 #ivmeaucbft .gt_font_italic { font-style: italic; }
 #ivmeaucbft .gt_super { font-size: 65%; }
 #ivmeaucbft .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ivmeaucbft .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ivmeaucbft .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ivmeaucbft .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ivmeaucbft .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ivmeaucbft .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ykbfzjlmyz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ykbfzjlmyz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ykbfzjlmyz p { margin: 0; padding: 0; }
 #ykbfzjlmyz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ykbfzjlmyz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ykbfzjlmyz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ykbfzjlmyz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ykbfzjlmyz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ykbfzjlmyz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ykbfzjlmyz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ykbfzjlmyz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ykbfzjlmyz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ykbfzjlmyz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ykbfzjlmyz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ykbfzjlmyz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ykbfzjlmyz .gt_spanner_row { border-bottom-style: hidden; }
 #ykbfzjlmyz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ykbfzjlmyz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ykbfzjlmyz .gt_from_md> :first-child { margin-top: 0; }
 #ykbfzjlmyz .gt_from_md> :last-child { margin-bottom: 0; }
 #ykbfzjlmyz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ykbfzjlmyz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ykbfzjlmyz .gt_indent_1 { text-indent: 5px; }
 #ykbfzjlmyz .gt_indent_2 { text-indent: calc(5px * 2); }
 #ykbfzjlmyz .gt_indent_3 { text-indent: calc(5px * 3); }
 #ykbfzjlmyz .gt_indent_4 { text-indent: calc(5px * 4); }
 #ykbfzjlmyz .gt_indent_5 { text-indent: calc(5px * 5); }
 #ykbfzjlmyz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ykbfzjlmyz .gt_row_group_first td { border-top-width: 2px; }
 #ykbfzjlmyz .gt_row_group_first th { border-top-width: 2px; }
 #ykbfzjlmyz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ykbfzjlmyz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ykbfzjlmyz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ykbfzjlmyz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ykbfzjlmyz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ykbfzjlmyz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ykbfzjlmyz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ykbfzjlmyz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ykbfzjlmyz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ykbfzjlmyz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ykbfzjlmyz .gt_left { text-align: left; }
 #ykbfzjlmyz .gt_center { text-align: center; }
 #ykbfzjlmyz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ykbfzjlmyz .gt_font_normal { font-weight: normal; }
 #ykbfzjlmyz .gt_font_bold { font-weight: bold; }
 #ykbfzjlmyz .gt_font_italic { font-style: italic; }
 #ykbfzjlmyz .gt_super { font-size: 65%; }
 #ykbfzjlmyz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ykbfzjlmyz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ykbfzjlmyz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ykbfzjlmyz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ykbfzjlmyz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ykbfzjlmyz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pceqmtcybq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pceqmtcybq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pceqmtcybq p { margin: 0; padding: 0; }
 #pceqmtcybq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pceqmtcybq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pceqmtcybq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pceqmtcybq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pceqmtcybq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pceqmtcybq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pceqmtcybq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pceqmtcybq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pceqmtcybq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pceqmtcybq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pceqmtcybq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pceqmtcybq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pceqmtcybq .gt_spanner_row { border-bottom-style: hidden; }
 #pceqmtcybq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pceqmtcybq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pceqmtcybq .gt_from_md> :first-child { margin-top: 0; }
 #pceqmtcybq .gt_from_md> :last-child { margin-bottom: 0; }
 #pceqmtcybq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pceqmtcybq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pceqmtcybq .gt_indent_1 { text-indent: 5px; }
 #pceqmtcybq .gt_indent_2 { text-indent: calc(5px * 2); }
 #pceqmtcybq .gt_indent_3 { text-indent: calc(5px * 3); }
 #pceqmtcybq .gt_indent_4 { text-indent: calc(5px * 4); }
 #pceqmtcybq .gt_indent_5 { text-indent: calc(5px * 5); }
 #pceqmtcybq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pceqmtcybq .gt_row_group_first td { border-top-width: 2px; }
 #pceqmtcybq .gt_row_group_first th { border-top-width: 2px; }
 #pceqmtcybq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pceqmtcybq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pceqmtcybq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pceqmtcybq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pceqmtcybq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pceqmtcybq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pceqmtcybq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pceqmtcybq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pceqmtcybq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pceqmtcybq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pceqmtcybq .gt_left { text-align: left; }
 #pceqmtcybq .gt_center { text-align: center; }
 #pceqmtcybq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pceqmtcybq .gt_font_normal { font-weight: normal; }
 #pceqmtcybq .gt_font_bold { font-weight: bold; }
 #pceqmtcybq .gt_font_italic { font-style: italic; }
 #pceqmtcybq .gt_super { font-size: 65%; }
 #pceqmtcybq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pceqmtcybq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pceqmtcybq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pceqmtcybq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pceqmtcybq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pceqmtcybq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ciyahjjpga table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ciyahjjpga thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ciyahjjpga p { margin: 0; padding: 0; }
 #ciyahjjpga .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ciyahjjpga .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ciyahjjpga .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ciyahjjpga .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ciyahjjpga .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ciyahjjpga .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ciyahjjpga .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ciyahjjpga .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ciyahjjpga .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ciyahjjpga .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ciyahjjpga .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ciyahjjpga .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ciyahjjpga .gt_spanner_row { border-bottom-style: hidden; }
 #ciyahjjpga .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ciyahjjpga .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ciyahjjpga .gt_from_md> :first-child { margin-top: 0; }
 #ciyahjjpga .gt_from_md> :last-child { margin-bottom: 0; }
 #ciyahjjpga .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ciyahjjpga .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ciyahjjpga .gt_indent_1 { text-indent: 5px; }
 #ciyahjjpga .gt_indent_2 { text-indent: calc(5px * 2); }
 #ciyahjjpga .gt_indent_3 { text-indent: calc(5px * 3); }
 #ciyahjjpga .gt_indent_4 { text-indent: calc(5px * 4); }
 #ciyahjjpga .gt_indent_5 { text-indent: calc(5px * 5); }
 #ciyahjjpga .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ciyahjjpga .gt_row_group_first td { border-top-width: 2px; }
 #ciyahjjpga .gt_row_group_first th { border-top-width: 2px; }
 #ciyahjjpga .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ciyahjjpga .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ciyahjjpga .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ciyahjjpga .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ciyahjjpga .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ciyahjjpga .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ciyahjjpga .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ciyahjjpga .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ciyahjjpga .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ciyahjjpga .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ciyahjjpga .gt_left { text-align: left; }
 #ciyahjjpga .gt_center { text-align: center; }
 #ciyahjjpga .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ciyahjjpga .gt_font_normal { font-weight: normal; }
 #ciyahjjpga .gt_font_bold { font-weight: bold; }
 #ciyahjjpga .gt_font_italic { font-style: italic; }
 #ciyahjjpga .gt_super { font-size: 65%; }
 #ciyahjjpga .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ciyahjjpga .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ciyahjjpga .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ciyahjjpga .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ciyahjjpga .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ciyahjjpga .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fxanqyqzzt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fxanqyqzzt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fxanqyqzzt p { margin: 0; padding: 0; }
 #fxanqyqzzt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fxanqyqzzt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fxanqyqzzt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fxanqyqzzt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fxanqyqzzt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fxanqyqzzt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fxanqyqzzt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fxanqyqzzt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fxanqyqzzt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fxanqyqzzt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fxanqyqzzt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fxanqyqzzt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fxanqyqzzt .gt_spanner_row { border-bottom-style: hidden; }
 #fxanqyqzzt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fxanqyqzzt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fxanqyqzzt .gt_from_md> :first-child { margin-top: 0; }
 #fxanqyqzzt .gt_from_md> :last-child { margin-bottom: 0; }
 #fxanqyqzzt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fxanqyqzzt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fxanqyqzzt .gt_indent_1 { text-indent: 5px; }
 #fxanqyqzzt .gt_indent_2 { text-indent: calc(5px * 2); }
 #fxanqyqzzt .gt_indent_3 { text-indent: calc(5px * 3); }
 #fxanqyqzzt .gt_indent_4 { text-indent: calc(5px * 4); }
 #fxanqyqzzt .gt_indent_5 { text-indent: calc(5px * 5); }
 #fxanqyqzzt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fxanqyqzzt .gt_row_group_first td { border-top-width: 2px; }
 #fxanqyqzzt .gt_row_group_first th { border-top-width: 2px; }
 #fxanqyqzzt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fxanqyqzzt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fxanqyqzzt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fxanqyqzzt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fxanqyqzzt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fxanqyqzzt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fxanqyqzzt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fxanqyqzzt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fxanqyqzzt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fxanqyqzzt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fxanqyqzzt .gt_left { text-align: left; }
 #fxanqyqzzt .gt_center { text-align: center; }
 #fxanqyqzzt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fxanqyqzzt .gt_font_normal { font-weight: normal; }
 #fxanqyqzzt .gt_font_bold { font-weight: bold; }
 #fxanqyqzzt .gt_font_italic { font-style: italic; }
 #fxanqyqzzt .gt_super { font-size: 65%; }
 #fxanqyqzzt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fxanqyqzzt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fxanqyqzzt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fxanqyqzzt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fxanqyqzzt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fxanqyqzzt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fbbspbherg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fbbspbherg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fbbspbherg p { margin: 0; padding: 0; }
 #fbbspbherg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fbbspbherg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fbbspbherg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fbbspbherg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fbbspbherg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fbbspbherg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fbbspbherg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fbbspbherg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fbbspbherg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fbbspbherg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fbbspbherg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fbbspbherg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fbbspbherg .gt_spanner_row { border-bottom-style: hidden; }
 #fbbspbherg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fbbspbherg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fbbspbherg .gt_from_md> :first-child { margin-top: 0; }
 #fbbspbherg .gt_from_md> :last-child { margin-bottom: 0; }
 #fbbspbherg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fbbspbherg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fbbspbherg .gt_indent_1 { text-indent: 5px; }
 #fbbspbherg .gt_indent_2 { text-indent: calc(5px * 2); }
 #fbbspbherg .gt_indent_3 { text-indent: calc(5px * 3); }
 #fbbspbherg .gt_indent_4 { text-indent: calc(5px * 4); }
 #fbbspbherg .gt_indent_5 { text-indent: calc(5px * 5); }
 #fbbspbherg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fbbspbherg .gt_row_group_first td { border-top-width: 2px; }
 #fbbspbherg .gt_row_group_first th { border-top-width: 2px; }
 #fbbspbherg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fbbspbherg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fbbspbherg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fbbspbherg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fbbspbherg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fbbspbherg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fbbspbherg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fbbspbherg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fbbspbherg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fbbspbherg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fbbspbherg .gt_left { text-align: left; }
 #fbbspbherg .gt_center { text-align: center; }
 #fbbspbherg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fbbspbherg .gt_font_normal { font-weight: normal; }
 #fbbspbherg .gt_font_bold { font-weight: bold; }
 #fbbspbherg .gt_font_italic { font-style: italic; }
 #fbbspbherg .gt_super { font-size: 65%; }
 #fbbspbherg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fbbspbherg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fbbspbherg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fbbspbherg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fbbspbherg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fbbspbherg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hjnaozkqzw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hjnaozkqzw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hjnaozkqzw p { margin: 0; padding: 0; }
 #hjnaozkqzw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hjnaozkqzw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hjnaozkqzw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hjnaozkqzw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hjnaozkqzw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjnaozkqzw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjnaozkqzw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjnaozkqzw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hjnaozkqzw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hjnaozkqzw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hjnaozkqzw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hjnaozkqzw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hjnaozkqzw .gt_spanner_row { border-bottom-style: hidden; }
 #hjnaozkqzw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hjnaozkqzw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hjnaozkqzw .gt_from_md> :first-child { margin-top: 0; }
 #hjnaozkqzw .gt_from_md> :last-child { margin-bottom: 0; }
 #hjnaozkqzw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hjnaozkqzw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hjnaozkqzw .gt_indent_1 { text-indent: 5px; }
 #hjnaozkqzw .gt_indent_2 { text-indent: calc(5px * 2); }
 #hjnaozkqzw .gt_indent_3 { text-indent: calc(5px * 3); }
 #hjnaozkqzw .gt_indent_4 { text-indent: calc(5px * 4); }
 #hjnaozkqzw .gt_indent_5 { text-indent: calc(5px * 5); }
 #hjnaozkqzw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hjnaozkqzw .gt_row_group_first td { border-top-width: 2px; }
 #hjnaozkqzw .gt_row_group_first th { border-top-width: 2px; }
 #hjnaozkqzw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hjnaozkqzw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjnaozkqzw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjnaozkqzw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hjnaozkqzw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjnaozkqzw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjnaozkqzw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hjnaozkqzw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hjnaozkqzw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjnaozkqzw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjnaozkqzw .gt_left { text-align: left; }
 #hjnaozkqzw .gt_center { text-align: center; }
 #hjnaozkqzw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hjnaozkqzw .gt_font_normal { font-weight: normal; }
 #hjnaozkqzw .gt_font_bold { font-weight: bold; }
 #hjnaozkqzw .gt_font_italic { font-style: italic; }
 #hjnaozkqzw .gt_super { font-size: 65%; }
 #hjnaozkqzw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjnaozkqzw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hjnaozkqzw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjnaozkqzw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjnaozkqzw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hjnaozkqzw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cmimefcise table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cmimefcise thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cmimefcise p { margin: 0; padding: 0; }
 #cmimefcise .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cmimefcise .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cmimefcise .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cmimefcise .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cmimefcise .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cmimefcise .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cmimefcise .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cmimefcise .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cmimefcise .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cmimefcise .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cmimefcise .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cmimefcise .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cmimefcise .gt_spanner_row { border-bottom-style: hidden; }
 #cmimefcise .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cmimefcise .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cmimefcise .gt_from_md> :first-child { margin-top: 0; }
 #cmimefcise .gt_from_md> :last-child { margin-bottom: 0; }
 #cmimefcise .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cmimefcise .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cmimefcise .gt_indent_1 { text-indent: 5px; }
 #cmimefcise .gt_indent_2 { text-indent: calc(5px * 2); }
 #cmimefcise .gt_indent_3 { text-indent: calc(5px * 3); }
 #cmimefcise .gt_indent_4 { text-indent: calc(5px * 4); }
 #cmimefcise .gt_indent_5 { text-indent: calc(5px * 5); }
 #cmimefcise .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cmimefcise .gt_row_group_first td { border-top-width: 2px; }
 #cmimefcise .gt_row_group_first th { border-top-width: 2px; }
 #cmimefcise .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cmimefcise .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cmimefcise .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cmimefcise .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cmimefcise .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cmimefcise .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cmimefcise .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cmimefcise .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cmimefcise .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cmimefcise .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cmimefcise .gt_left { text-align: left; }
 #cmimefcise .gt_center { text-align: center; }
 #cmimefcise .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cmimefcise .gt_font_normal { font-weight: normal; }
 #cmimefcise .gt_font_bold { font-weight: bold; }
 #cmimefcise .gt_font_italic { font-style: italic; }
 #cmimefcise .gt_super { font-size: 65%; }
 #cmimefcise .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cmimefcise .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cmimefcise .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cmimefcise .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cmimefcise .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cmimefcise .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#aggvgnrgxw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aggvgnrgxw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aggvgnrgxw p { margin: 0; padding: 0; }
 #aggvgnrgxw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aggvgnrgxw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aggvgnrgxw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aggvgnrgxw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aggvgnrgxw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aggvgnrgxw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aggvgnrgxw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aggvgnrgxw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #aggvgnrgxw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aggvgnrgxw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aggvgnrgxw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aggvgnrgxw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aggvgnrgxw .gt_spanner_row { border-bottom-style: hidden; }
 #aggvgnrgxw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aggvgnrgxw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aggvgnrgxw .gt_from_md> :first-child { margin-top: 0; }
 #aggvgnrgxw .gt_from_md> :last-child { margin-bottom: 0; }
 #aggvgnrgxw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aggvgnrgxw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #aggvgnrgxw .gt_indent_1 { text-indent: 5px; }
 #aggvgnrgxw .gt_indent_2 { text-indent: calc(5px * 2); }
 #aggvgnrgxw .gt_indent_3 { text-indent: calc(5px * 3); }
 #aggvgnrgxw .gt_indent_4 { text-indent: calc(5px * 4); }
 #aggvgnrgxw .gt_indent_5 { text-indent: calc(5px * 5); }
 #aggvgnrgxw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #aggvgnrgxw .gt_row_group_first td { border-top-width: 2px; }
 #aggvgnrgxw .gt_row_group_first th { border-top-width: 2px; }
 #aggvgnrgxw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aggvgnrgxw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aggvgnrgxw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aggvgnrgxw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aggvgnrgxw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aggvgnrgxw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aggvgnrgxw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aggvgnrgxw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aggvgnrgxw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aggvgnrgxw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aggvgnrgxw .gt_left { text-align: left; }
 #aggvgnrgxw .gt_center { text-align: center; }
 #aggvgnrgxw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aggvgnrgxw .gt_font_normal { font-weight: normal; }
 #aggvgnrgxw .gt_font_bold { font-weight: bold; }
 #aggvgnrgxw .gt_font_italic { font-style: italic; }
 #aggvgnrgxw .gt_super { font-size: 65%; }
 #aggvgnrgxw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aggvgnrgxw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aggvgnrgxw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aggvgnrgxw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aggvgnrgxw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aggvgnrgxw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ugzjtcyxqg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ugzjtcyxqg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ugzjtcyxqg p { margin: 0; padding: 0; }
 #ugzjtcyxqg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ugzjtcyxqg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ugzjtcyxqg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ugzjtcyxqg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ugzjtcyxqg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ugzjtcyxqg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ugzjtcyxqg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ugzjtcyxqg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ugzjtcyxqg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ugzjtcyxqg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ugzjtcyxqg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ugzjtcyxqg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ugzjtcyxqg .gt_spanner_row { border-bottom-style: hidden; }
 #ugzjtcyxqg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ugzjtcyxqg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ugzjtcyxqg .gt_from_md> :first-child { margin-top: 0; }
 #ugzjtcyxqg .gt_from_md> :last-child { margin-bottom: 0; }
 #ugzjtcyxqg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ugzjtcyxqg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ugzjtcyxqg .gt_indent_1 { text-indent: 5px; }
 #ugzjtcyxqg .gt_indent_2 { text-indent: calc(5px * 2); }
 #ugzjtcyxqg .gt_indent_3 { text-indent: calc(5px * 3); }
 #ugzjtcyxqg .gt_indent_4 { text-indent: calc(5px * 4); }
 #ugzjtcyxqg .gt_indent_5 { text-indent: calc(5px * 5); }
 #ugzjtcyxqg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ugzjtcyxqg .gt_row_group_first td { border-top-width: 2px; }
 #ugzjtcyxqg .gt_row_group_first th { border-top-width: 2px; }
 #ugzjtcyxqg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ugzjtcyxqg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ugzjtcyxqg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ugzjtcyxqg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ugzjtcyxqg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ugzjtcyxqg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ugzjtcyxqg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ugzjtcyxqg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ugzjtcyxqg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ugzjtcyxqg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ugzjtcyxqg .gt_left { text-align: left; }
 #ugzjtcyxqg .gt_center { text-align: center; }
 #ugzjtcyxqg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ugzjtcyxqg .gt_font_normal { font-weight: normal; }
 #ugzjtcyxqg .gt_font_bold { font-weight: bold; }
 #ugzjtcyxqg .gt_font_italic { font-style: italic; }
 #ugzjtcyxqg .gt_super { font-size: 65%; }
 #ugzjtcyxqg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ugzjtcyxqg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ugzjtcyxqg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ugzjtcyxqg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ugzjtcyxqg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ugzjtcyxqg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zubqkigtij table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zubqkigtij thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zubqkigtij p { margin: 0; padding: 0; }
 #zubqkigtij .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zubqkigtij .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zubqkigtij .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zubqkigtij .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zubqkigtij .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zubqkigtij .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zubqkigtij .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zubqkigtij .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zubqkigtij .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zubqkigtij .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zubqkigtij .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zubqkigtij .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zubqkigtij .gt_spanner_row { border-bottom-style: hidden; }
 #zubqkigtij .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zubqkigtij .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zubqkigtij .gt_from_md> :first-child { margin-top: 0; }
 #zubqkigtij .gt_from_md> :last-child { margin-bottom: 0; }
 #zubqkigtij .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zubqkigtij .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zubqkigtij .gt_indent_1 { text-indent: 5px; }
 #zubqkigtij .gt_indent_2 { text-indent: calc(5px * 2); }
 #zubqkigtij .gt_indent_3 { text-indent: calc(5px * 3); }
 #zubqkigtij .gt_indent_4 { text-indent: calc(5px * 4); }
 #zubqkigtij .gt_indent_5 { text-indent: calc(5px * 5); }
 #zubqkigtij .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zubqkigtij .gt_row_group_first td { border-top-width: 2px; }
 #zubqkigtij .gt_row_group_first th { border-top-width: 2px; }
 #zubqkigtij .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zubqkigtij .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zubqkigtij .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zubqkigtij .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zubqkigtij .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zubqkigtij .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zubqkigtij .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zubqkigtij .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zubqkigtij .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zubqkigtij .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zubqkigtij .gt_left { text-align: left; }
 #zubqkigtij .gt_center { text-align: center; }
 #zubqkigtij .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zubqkigtij .gt_font_normal { font-weight: normal; }
 #zubqkigtij .gt_font_bold { font-weight: bold; }
 #zubqkigtij .gt_font_italic { font-style: italic; }
 #zubqkigtij .gt_super { font-size: 65%; }
 #zubqkigtij .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zubqkigtij .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zubqkigtij .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zubqkigtij .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zubqkigtij .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zubqkigtij .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ffsrsmmkrt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ffsrsmmkrt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ffsrsmmkrt p { margin: 0; padding: 0; }
 #ffsrsmmkrt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ffsrsmmkrt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ffsrsmmkrt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ffsrsmmkrt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ffsrsmmkrt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ffsrsmmkrt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ffsrsmmkrt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ffsrsmmkrt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ffsrsmmkrt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ffsrsmmkrt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ffsrsmmkrt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ffsrsmmkrt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ffsrsmmkrt .gt_spanner_row { border-bottom-style: hidden; }
 #ffsrsmmkrt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ffsrsmmkrt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ffsrsmmkrt .gt_from_md> :first-child { margin-top: 0; }
 #ffsrsmmkrt .gt_from_md> :last-child { margin-bottom: 0; }
 #ffsrsmmkrt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ffsrsmmkrt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ffsrsmmkrt .gt_indent_1 { text-indent: 5px; }
 #ffsrsmmkrt .gt_indent_2 { text-indent: calc(5px * 2); }
 #ffsrsmmkrt .gt_indent_3 { text-indent: calc(5px * 3); }
 #ffsrsmmkrt .gt_indent_4 { text-indent: calc(5px * 4); }
 #ffsrsmmkrt .gt_indent_5 { text-indent: calc(5px * 5); }
 #ffsrsmmkrt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ffsrsmmkrt .gt_row_group_first td { border-top-width: 2px; }
 #ffsrsmmkrt .gt_row_group_first th { border-top-width: 2px; }
 #ffsrsmmkrt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ffsrsmmkrt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ffsrsmmkrt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ffsrsmmkrt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ffsrsmmkrt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ffsrsmmkrt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ffsrsmmkrt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ffsrsmmkrt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ffsrsmmkrt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ffsrsmmkrt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ffsrsmmkrt .gt_left { text-align: left; }
 #ffsrsmmkrt .gt_center { text-align: center; }
 #ffsrsmmkrt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ffsrsmmkrt .gt_font_normal { font-weight: normal; }
 #ffsrsmmkrt .gt_font_bold { font-weight: bold; }
 #ffsrsmmkrt .gt_font_italic { font-style: italic; }
 #ffsrsmmkrt .gt_super { font-size: 65%; }
 #ffsrsmmkrt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ffsrsmmkrt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ffsrsmmkrt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ffsrsmmkrt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ffsrsmmkrt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ffsrsmmkrt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fntnwlslkm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fntnwlslkm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fntnwlslkm p { margin: 0; padding: 0; }
 #fntnwlslkm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fntnwlslkm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fntnwlslkm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fntnwlslkm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fntnwlslkm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fntnwlslkm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fntnwlslkm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fntnwlslkm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fntnwlslkm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fntnwlslkm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fntnwlslkm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fntnwlslkm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fntnwlslkm .gt_spanner_row { border-bottom-style: hidden; }
 #fntnwlslkm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fntnwlslkm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fntnwlslkm .gt_from_md> :first-child { margin-top: 0; }
 #fntnwlslkm .gt_from_md> :last-child { margin-bottom: 0; }
 #fntnwlslkm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fntnwlslkm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fntnwlslkm .gt_indent_1 { text-indent: 5px; }
 #fntnwlslkm .gt_indent_2 { text-indent: calc(5px * 2); }
 #fntnwlslkm .gt_indent_3 { text-indent: calc(5px * 3); }
 #fntnwlslkm .gt_indent_4 { text-indent: calc(5px * 4); }
 #fntnwlslkm .gt_indent_5 { text-indent: calc(5px * 5); }
 #fntnwlslkm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fntnwlslkm .gt_row_group_first td { border-top-width: 2px; }
 #fntnwlslkm .gt_row_group_first th { border-top-width: 2px; }
 #fntnwlslkm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fntnwlslkm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fntnwlslkm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fntnwlslkm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fntnwlslkm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fntnwlslkm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fntnwlslkm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fntnwlslkm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fntnwlslkm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fntnwlslkm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fntnwlslkm .gt_left { text-align: left; }
 #fntnwlslkm .gt_center { text-align: center; }
 #fntnwlslkm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fntnwlslkm .gt_font_normal { font-weight: normal; }
 #fntnwlslkm .gt_font_bold { font-weight: bold; }
 #fntnwlslkm .gt_font_italic { font-style: italic; }
 #fntnwlslkm .gt_super { font-size: 65%; }
 #fntnwlslkm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fntnwlslkm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fntnwlslkm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fntnwlslkm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fntnwlslkm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fntnwlslkm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vrsnadhtod table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vrsnadhtod thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vrsnadhtod p { margin: 0; padding: 0; }
 #vrsnadhtod .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vrsnadhtod .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vrsnadhtod .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vrsnadhtod .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vrsnadhtod .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vrsnadhtod .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vrsnadhtod .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vrsnadhtod .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vrsnadhtod .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vrsnadhtod .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vrsnadhtod .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vrsnadhtod .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vrsnadhtod .gt_spanner_row { border-bottom-style: hidden; }
 #vrsnadhtod .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vrsnadhtod .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vrsnadhtod .gt_from_md> :first-child { margin-top: 0; }
 #vrsnadhtod .gt_from_md> :last-child { margin-bottom: 0; }
 #vrsnadhtod .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vrsnadhtod .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vrsnadhtod .gt_indent_1 { text-indent: 5px; }
 #vrsnadhtod .gt_indent_2 { text-indent: calc(5px * 2); }
 #vrsnadhtod .gt_indent_3 { text-indent: calc(5px * 3); }
 #vrsnadhtod .gt_indent_4 { text-indent: calc(5px * 4); }
 #vrsnadhtod .gt_indent_5 { text-indent: calc(5px * 5); }
 #vrsnadhtod .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vrsnadhtod .gt_row_group_first td { border-top-width: 2px; }
 #vrsnadhtod .gt_row_group_first th { border-top-width: 2px; }
 #vrsnadhtod .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vrsnadhtod .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vrsnadhtod .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vrsnadhtod .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vrsnadhtod .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vrsnadhtod .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vrsnadhtod .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vrsnadhtod .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vrsnadhtod .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vrsnadhtod .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vrsnadhtod .gt_left { text-align: left; }
 #vrsnadhtod .gt_center { text-align: center; }
 #vrsnadhtod .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vrsnadhtod .gt_font_normal { font-weight: normal; }
 #vrsnadhtod .gt_font_bold { font-weight: bold; }
 #vrsnadhtod .gt_font_italic { font-style: italic; }
 #vrsnadhtod .gt_super { font-size: 65%; }
 #vrsnadhtod .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vrsnadhtod .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vrsnadhtod .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vrsnadhtod .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vrsnadhtod .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vrsnadhtod .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="4" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right" style="background-color: orange">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: orange">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">13.255</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">0.44</td>
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
#zspwntxwtq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zspwntxwtq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zspwntxwtq p { margin: 0; padding: 0; }
 #zspwntxwtq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zspwntxwtq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zspwntxwtq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zspwntxwtq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zspwntxwtq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zspwntxwtq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zspwntxwtq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zspwntxwtq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zspwntxwtq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zspwntxwtq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zspwntxwtq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zspwntxwtq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zspwntxwtq .gt_spanner_row { border-bottom-style: hidden; }
 #zspwntxwtq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zspwntxwtq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zspwntxwtq .gt_from_md> :first-child { margin-top: 0; }
 #zspwntxwtq .gt_from_md> :last-child { margin-bottom: 0; }
 #zspwntxwtq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zspwntxwtq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zspwntxwtq .gt_indent_1 { text-indent: 5px; }
 #zspwntxwtq .gt_indent_2 { text-indent: calc(5px * 2); }
 #zspwntxwtq .gt_indent_3 { text-indent: calc(5px * 3); }
 #zspwntxwtq .gt_indent_4 { text-indent: calc(5px * 4); }
 #zspwntxwtq .gt_indent_5 { text-indent: calc(5px * 5); }
 #zspwntxwtq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zspwntxwtq .gt_row_group_first td { border-top-width: 2px; }
 #zspwntxwtq .gt_row_group_first th { border-top-width: 2px; }
 #zspwntxwtq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zspwntxwtq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zspwntxwtq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zspwntxwtq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zspwntxwtq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zspwntxwtq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zspwntxwtq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zspwntxwtq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zspwntxwtq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zspwntxwtq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zspwntxwtq .gt_left { text-align: left; }
 #zspwntxwtq .gt_center { text-align: center; }
 #zspwntxwtq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zspwntxwtq .gt_font_normal { font-weight: normal; }
 #zspwntxwtq .gt_font_bold { font-weight: bold; }
 #zspwntxwtq .gt_font_italic { font-style: italic; }
 #zspwntxwtq .gt_super { font-size: 65%; }
 #zspwntxwtq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zspwntxwtq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zspwntxwtq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zspwntxwtq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zspwntxwtq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zspwntxwtq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="4" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left" style="color: red">NA</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" style="color: red">NA</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">13.255</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right" style="color: red">NA</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">0.44</td>
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
#emkemktooa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#emkemktooa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#emkemktooa p { margin: 0; padding: 0; }
 #emkemktooa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #emkemktooa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #emkemktooa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #emkemktooa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #emkemktooa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #emkemktooa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #emkemktooa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #emkemktooa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #emkemktooa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #emkemktooa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #emkemktooa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #emkemktooa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #emkemktooa .gt_spanner_row { border-bottom-style: hidden; }
 #emkemktooa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #emkemktooa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #emkemktooa .gt_from_md> :first-child { margin-top: 0; }
 #emkemktooa .gt_from_md> :last-child { margin-bottom: 0; }
 #emkemktooa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #emkemktooa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #emkemktooa .gt_indent_1 { text-indent: 5px; }
 #emkemktooa .gt_indent_2 { text-indent: calc(5px * 2); }
 #emkemktooa .gt_indent_3 { text-indent: calc(5px * 3); }
 #emkemktooa .gt_indent_4 { text-indent: calc(5px * 4); }
 #emkemktooa .gt_indent_5 { text-indent: calc(5px * 5); }
 #emkemktooa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #emkemktooa .gt_row_group_first td { border-top-width: 2px; }
 #emkemktooa .gt_row_group_first th { border-top-width: 2px; }
 #emkemktooa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #emkemktooa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #emkemktooa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #emkemktooa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #emkemktooa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #emkemktooa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #emkemktooa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #emkemktooa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #emkemktooa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #emkemktooa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #emkemktooa .gt_left { text-align: left; }
 #emkemktooa .gt_center { text-align: center; }
 #emkemktooa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #emkemktooa .gt_font_normal { font-weight: normal; }
 #emkemktooa .gt_font_bold { font-weight: bold; }
 #emkemktooa .gt_font_italic { font-style: italic; }
 #emkemktooa .gt_super { font-size: 65%; }
 #emkemktooa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #emkemktooa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #emkemktooa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #emkemktooa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #emkemktooa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #emkemktooa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="4" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightgreen">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right" style="background-color: lightgreen">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: lightgreen">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right" style="background-color: lightgreen">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: lightgreen">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right" style="background-color: lightgreen">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right" style="background-color: lightgreen">13.255</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right" style="background-color: lightgreen">0.44</td>
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
#dwyqatcngz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dwyqatcngz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dwyqatcngz p { margin: 0; padding: 0; }
 #dwyqatcngz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dwyqatcngz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dwyqatcngz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dwyqatcngz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dwyqatcngz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dwyqatcngz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dwyqatcngz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dwyqatcngz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dwyqatcngz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dwyqatcngz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dwyqatcngz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dwyqatcngz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dwyqatcngz .gt_spanner_row { border-bottom-style: hidden; }
 #dwyqatcngz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dwyqatcngz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dwyqatcngz .gt_from_md> :first-child { margin-top: 0; }
 #dwyqatcngz .gt_from_md> :last-child { margin-bottom: 0; }
 #dwyqatcngz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dwyqatcngz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dwyqatcngz .gt_indent_1 { text-indent: 5px; }
 #dwyqatcngz .gt_indent_2 { text-indent: calc(5px * 2); }
 #dwyqatcngz .gt_indent_3 { text-indent: calc(5px * 3); }
 #dwyqatcngz .gt_indent_4 { text-indent: calc(5px * 4); }
 #dwyqatcngz .gt_indent_5 { text-indent: calc(5px * 5); }
 #dwyqatcngz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dwyqatcngz .gt_row_group_first td { border-top-width: 2px; }
 #dwyqatcngz .gt_row_group_first th { border-top-width: 2px; }
 #dwyqatcngz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dwyqatcngz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dwyqatcngz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dwyqatcngz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dwyqatcngz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dwyqatcngz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dwyqatcngz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dwyqatcngz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dwyqatcngz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dwyqatcngz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dwyqatcngz .gt_left { text-align: left; }
 #dwyqatcngz .gt_center { text-align: center; }
 #dwyqatcngz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dwyqatcngz .gt_font_normal { font-weight: normal; }
 #dwyqatcngz .gt_font_bold { font-weight: bold; }
 #dwyqatcngz .gt_font_italic { font-style: italic; }
 #dwyqatcngz .gt_super { font-size: 65%; }
 #dwyqatcngz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dwyqatcngz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dwyqatcngz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dwyqatcngz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dwyqatcngz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dwyqatcngz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="4" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left" style="background-color: lightyellow">apricot</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left" style="background-color: lightyellow">banana</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left" style="background-color: lightyellow">coconut</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left" style="background-color: lightyellow">durian</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">13.255</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">0.44</td>
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
#lilbgyuteu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lilbgyuteu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lilbgyuteu p { margin: 0; padding: 0; }
 #lilbgyuteu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lilbgyuteu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lilbgyuteu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lilbgyuteu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lilbgyuteu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lilbgyuteu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lilbgyuteu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lilbgyuteu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lilbgyuteu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lilbgyuteu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lilbgyuteu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lilbgyuteu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lilbgyuteu .gt_spanner_row { border-bottom-style: hidden; }
 #lilbgyuteu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lilbgyuteu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lilbgyuteu .gt_from_md> :first-child { margin-top: 0; }
 #lilbgyuteu .gt_from_md> :last-child { margin-bottom: 0; }
 #lilbgyuteu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lilbgyuteu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lilbgyuteu .gt_indent_1 { text-indent: 5px; }
 #lilbgyuteu .gt_indent_2 { text-indent: calc(5px * 2); }
 #lilbgyuteu .gt_indent_3 { text-indent: calc(5px * 3); }
 #lilbgyuteu .gt_indent_4 { text-indent: calc(5px * 4); }
 #lilbgyuteu .gt_indent_5 { text-indent: calc(5px * 5); }
 #lilbgyuteu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lilbgyuteu .gt_row_group_first td { border-top-width: 2px; }
 #lilbgyuteu .gt_row_group_first th { border-top-width: 2px; }
 #lilbgyuteu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lilbgyuteu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lilbgyuteu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lilbgyuteu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lilbgyuteu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lilbgyuteu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lilbgyuteu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lilbgyuteu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lilbgyuteu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lilbgyuteu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lilbgyuteu .gt_left { text-align: left; }
 #lilbgyuteu .gt_center { text-align: center; }
 #lilbgyuteu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lilbgyuteu .gt_font_normal { font-weight: normal; }
 #lilbgyuteu .gt_font_bold { font-weight: bold; }
 #lilbgyuteu .gt_font_italic { font-style: italic; }
 #lilbgyuteu .gt_super { font-size: 65%; }
 #lilbgyuteu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lilbgyuteu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lilbgyuteu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lilbgyuteu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lilbgyuteu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lilbgyuteu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="4" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightcyan">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: lightcyan">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: lightcyan">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">13.255</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">0.44</td>
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
#pmvhxvgcsl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pmvhxvgcsl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pmvhxvgcsl p { margin: 0; padding: 0; }
 #pmvhxvgcsl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pmvhxvgcsl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pmvhxvgcsl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pmvhxvgcsl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pmvhxvgcsl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pmvhxvgcsl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pmvhxvgcsl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pmvhxvgcsl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pmvhxvgcsl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pmvhxvgcsl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pmvhxvgcsl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pmvhxvgcsl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pmvhxvgcsl .gt_spanner_row { border-bottom-style: hidden; }
 #pmvhxvgcsl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pmvhxvgcsl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pmvhxvgcsl .gt_from_md> :first-child { margin-top: 0; }
 #pmvhxvgcsl .gt_from_md> :last-child { margin-bottom: 0; }
 #pmvhxvgcsl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pmvhxvgcsl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pmvhxvgcsl .gt_indent_1 { text-indent: 5px; }
 #pmvhxvgcsl .gt_indent_2 { text-indent: calc(5px * 2); }
 #pmvhxvgcsl .gt_indent_3 { text-indent: calc(5px * 3); }
 #pmvhxvgcsl .gt_indent_4 { text-indent: calc(5px * 4); }
 #pmvhxvgcsl .gt_indent_5 { text-indent: calc(5px * 5); }
 #pmvhxvgcsl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pmvhxvgcsl .gt_row_group_first td { border-top-width: 2px; }
 #pmvhxvgcsl .gt_row_group_first th { border-top-width: 2px; }
 #pmvhxvgcsl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pmvhxvgcsl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pmvhxvgcsl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pmvhxvgcsl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pmvhxvgcsl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pmvhxvgcsl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pmvhxvgcsl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pmvhxvgcsl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pmvhxvgcsl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pmvhxvgcsl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pmvhxvgcsl .gt_left { text-align: left; }
 #pmvhxvgcsl .gt_center { text-align: center; }
 #pmvhxvgcsl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pmvhxvgcsl .gt_font_normal { font-weight: normal; }
 #pmvhxvgcsl .gt_font_bold { font-weight: bold; }
 #pmvhxvgcsl .gt_font_italic { font-style: italic; }
 #pmvhxvgcsl .gt_super { font-size: 65%; }
 #pmvhxvgcsl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pmvhxvgcsl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pmvhxvgcsl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pmvhxvgcsl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pmvhxvgcsl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pmvhxvgcsl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="4" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightblue; background-color: bisque">0.1111</td>
<td class="gt_row gt_left" style="background-color: lightblue">apricot</td>
<td class="gt_row gt_right" style="background-color: lightblue">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: bisque">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" style="background-color: bisque">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" style="background-color: bisque">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" style="background-color: bisque">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" style="background-color: bisque">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">13.255</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" style="background-color: bisque">777000.0</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" style="background-color: bisque">8880000.0</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">0.44</td>
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
#ipbmigdwnu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ipbmigdwnu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ipbmigdwnu p { margin: 0; padding: 0; }
 #ipbmigdwnu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ipbmigdwnu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ipbmigdwnu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ipbmigdwnu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ipbmigdwnu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ipbmigdwnu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ipbmigdwnu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ipbmigdwnu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ipbmigdwnu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ipbmigdwnu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ipbmigdwnu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ipbmigdwnu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ipbmigdwnu .gt_spanner_row { border-bottom-style: hidden; }
 #ipbmigdwnu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ipbmigdwnu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ipbmigdwnu .gt_from_md> :first-child { margin-top: 0; }
 #ipbmigdwnu .gt_from_md> :last-child { margin-bottom: 0; }
 #ipbmigdwnu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ipbmigdwnu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ipbmigdwnu .gt_indent_1 { text-indent: 5px; }
 #ipbmigdwnu .gt_indent_2 { text-indent: calc(5px * 2); }
 #ipbmigdwnu .gt_indent_3 { text-indent: calc(5px * 3); }
 #ipbmigdwnu .gt_indent_4 { text-indent: calc(5px * 4); }
 #ipbmigdwnu .gt_indent_5 { text-indent: calc(5px * 5); }
 #ipbmigdwnu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ipbmigdwnu .gt_row_group_first td { border-top-width: 2px; }
 #ipbmigdwnu .gt_row_group_first th { border-top-width: 2px; }
 #ipbmigdwnu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ipbmigdwnu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ipbmigdwnu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ipbmigdwnu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ipbmigdwnu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ipbmigdwnu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ipbmigdwnu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ipbmigdwnu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ipbmigdwnu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ipbmigdwnu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ipbmigdwnu .gt_left { text-align: left; }
 #ipbmigdwnu .gt_center { text-align: center; }
 #ipbmigdwnu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ipbmigdwnu .gt_font_normal { font-weight: normal; }
 #ipbmigdwnu .gt_font_bold { font-weight: bold; }
 #ipbmigdwnu .gt_font_italic { font-style: italic; }
 #ipbmigdwnu .gt_super { font-size: 65%; }
 #ipbmigdwnu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ipbmigdwnu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ipbmigdwnu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ipbmigdwnu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ipbmigdwnu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ipbmigdwnu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="4" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" style="background-color: lightblue" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightblue">0.1111</td>
<td class="gt_row gt_left" style="background-color: lightblue">apricot</td>
<td class="gt_row gt_right" style="background-color: lightblue">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">13.255</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">0.44</td>
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
