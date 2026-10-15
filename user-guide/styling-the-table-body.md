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
#wcurklakda table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wcurklakda thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wcurklakda p { margin: 0; padding: 0; }
 #wcurklakda .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wcurklakda .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wcurklakda .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wcurklakda .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wcurklakda .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wcurklakda .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wcurklakda .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wcurklakda .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wcurklakda .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wcurklakda .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wcurklakda .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wcurklakda .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wcurklakda .gt_spanner_row { border-bottom-style: hidden; }
 #wcurklakda .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wcurklakda .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wcurklakda .gt_from_md> :first-child { margin-top: 0; }
 #wcurklakda .gt_from_md> :last-child { margin-bottom: 0; }
 #wcurklakda .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wcurklakda .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wcurklakda .gt_indent_1 { text-indent: 5px; }
 #wcurklakda .gt_indent_2 { text-indent: calc(5px * 2); }
 #wcurklakda .gt_indent_3 { text-indent: calc(5px * 3); }
 #wcurklakda .gt_indent_4 { text-indent: calc(5px * 4); }
 #wcurklakda .gt_indent_5 { text-indent: calc(5px * 5); }
 #wcurklakda .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wcurklakda .gt_row_group_first td { border-top-width: 2px; }
 #wcurklakda .gt_row_group_first th { border-top-width: 2px; }
 #wcurklakda .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wcurklakda .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wcurklakda .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wcurklakda .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wcurklakda .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wcurklakda .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wcurklakda .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wcurklakda .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wcurklakda .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wcurklakda .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wcurklakda .gt_left { text-align: left; }
 #wcurklakda .gt_center { text-align: center; }
 #wcurklakda .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wcurklakda .gt_font_normal { font-weight: normal; }
 #wcurklakda .gt_font_bold { font-weight: bold; }
 #wcurklakda .gt_font_italic { font-style: italic; }
 #wcurklakda .gt_super { font-size: 65%; }
 #wcurklakda .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wcurklakda .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wcurklakda .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wcurklakda .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wcurklakda .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wcurklakda .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#yyzlnfwlji table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yyzlnfwlji thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yyzlnfwlji p { margin: 0; padding: 0; }
 #yyzlnfwlji .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yyzlnfwlji .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yyzlnfwlji .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yyzlnfwlji .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yyzlnfwlji .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yyzlnfwlji .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yyzlnfwlji .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yyzlnfwlji .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yyzlnfwlji .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yyzlnfwlji .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yyzlnfwlji .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yyzlnfwlji .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yyzlnfwlji .gt_spanner_row { border-bottom-style: hidden; }
 #yyzlnfwlji .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yyzlnfwlji .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yyzlnfwlji .gt_from_md> :first-child { margin-top: 0; }
 #yyzlnfwlji .gt_from_md> :last-child { margin-bottom: 0; }
 #yyzlnfwlji .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yyzlnfwlji .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yyzlnfwlji .gt_indent_1 { text-indent: 5px; }
 #yyzlnfwlji .gt_indent_2 { text-indent: calc(5px * 2); }
 #yyzlnfwlji .gt_indent_3 { text-indent: calc(5px * 3); }
 #yyzlnfwlji .gt_indent_4 { text-indent: calc(5px * 4); }
 #yyzlnfwlji .gt_indent_5 { text-indent: calc(5px * 5); }
 #yyzlnfwlji .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yyzlnfwlji .gt_row_group_first td { border-top-width: 2px; }
 #yyzlnfwlji .gt_row_group_first th { border-top-width: 2px; }
 #yyzlnfwlji .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yyzlnfwlji .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yyzlnfwlji .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yyzlnfwlji .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yyzlnfwlji .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yyzlnfwlji .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yyzlnfwlji .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yyzlnfwlji .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yyzlnfwlji .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yyzlnfwlji .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yyzlnfwlji .gt_left { text-align: left; }
 #yyzlnfwlji .gt_center { text-align: center; }
 #yyzlnfwlji .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yyzlnfwlji .gt_font_normal { font-weight: normal; }
 #yyzlnfwlji .gt_font_bold { font-weight: bold; }
 #yyzlnfwlji .gt_font_italic { font-style: italic; }
 #yyzlnfwlji .gt_super { font-size: 65%; }
 #yyzlnfwlji .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yyzlnfwlji .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yyzlnfwlji .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yyzlnfwlji .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yyzlnfwlji .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yyzlnfwlji .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ynmtspnjyl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ynmtspnjyl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ynmtspnjyl p { margin: 0; padding: 0; }
 #ynmtspnjyl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ynmtspnjyl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ynmtspnjyl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ynmtspnjyl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ynmtspnjyl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ynmtspnjyl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ynmtspnjyl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ynmtspnjyl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ynmtspnjyl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ynmtspnjyl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ynmtspnjyl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ynmtspnjyl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ynmtspnjyl .gt_spanner_row { border-bottom-style: hidden; }
 #ynmtspnjyl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ynmtspnjyl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ynmtspnjyl .gt_from_md> :first-child { margin-top: 0; }
 #ynmtspnjyl .gt_from_md> :last-child { margin-bottom: 0; }
 #ynmtspnjyl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ynmtspnjyl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ynmtspnjyl .gt_indent_1 { text-indent: 5px; }
 #ynmtspnjyl .gt_indent_2 { text-indent: calc(5px * 2); }
 #ynmtspnjyl .gt_indent_3 { text-indent: calc(5px * 3); }
 #ynmtspnjyl .gt_indent_4 { text-indent: calc(5px * 4); }
 #ynmtspnjyl .gt_indent_5 { text-indent: calc(5px * 5); }
 #ynmtspnjyl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ynmtspnjyl .gt_row_group_first td { border-top-width: 2px; }
 #ynmtspnjyl .gt_row_group_first th { border-top-width: 2px; }
 #ynmtspnjyl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ynmtspnjyl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ynmtspnjyl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ynmtspnjyl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ynmtspnjyl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ynmtspnjyl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ynmtspnjyl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ynmtspnjyl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ynmtspnjyl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ynmtspnjyl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ynmtspnjyl .gt_left { text-align: left; }
 #ynmtspnjyl .gt_center { text-align: center; }
 #ynmtspnjyl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ynmtspnjyl .gt_font_normal { font-weight: normal; }
 #ynmtspnjyl .gt_font_bold { font-weight: bold; }
 #ynmtspnjyl .gt_font_italic { font-style: italic; }
 #ynmtspnjyl .gt_super { font-size: 65%; }
 #ynmtspnjyl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ynmtspnjyl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ynmtspnjyl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ynmtspnjyl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ynmtspnjyl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ynmtspnjyl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hebigplrbh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hebigplrbh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hebigplrbh p { margin: 0; padding: 0; }
 #hebigplrbh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hebigplrbh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hebigplrbh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hebigplrbh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hebigplrbh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hebigplrbh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hebigplrbh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hebigplrbh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hebigplrbh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hebigplrbh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hebigplrbh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hebigplrbh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hebigplrbh .gt_spanner_row { border-bottom-style: hidden; }
 #hebigplrbh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hebigplrbh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hebigplrbh .gt_from_md> :first-child { margin-top: 0; }
 #hebigplrbh .gt_from_md> :last-child { margin-bottom: 0; }
 #hebigplrbh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hebigplrbh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hebigplrbh .gt_indent_1 { text-indent: 5px; }
 #hebigplrbh .gt_indent_2 { text-indent: calc(5px * 2); }
 #hebigplrbh .gt_indent_3 { text-indent: calc(5px * 3); }
 #hebigplrbh .gt_indent_4 { text-indent: calc(5px * 4); }
 #hebigplrbh .gt_indent_5 { text-indent: calc(5px * 5); }
 #hebigplrbh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hebigplrbh .gt_row_group_first td { border-top-width: 2px; }
 #hebigplrbh .gt_row_group_first th { border-top-width: 2px; }
 #hebigplrbh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hebigplrbh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hebigplrbh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hebigplrbh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hebigplrbh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hebigplrbh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hebigplrbh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hebigplrbh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hebigplrbh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hebigplrbh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hebigplrbh .gt_left { text-align: left; }
 #hebigplrbh .gt_center { text-align: center; }
 #hebigplrbh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hebigplrbh .gt_font_normal { font-weight: normal; }
 #hebigplrbh .gt_font_bold { font-weight: bold; }
 #hebigplrbh .gt_font_italic { font-style: italic; }
 #hebigplrbh .gt_super { font-size: 65%; }
 #hebigplrbh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hebigplrbh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hebigplrbh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hebigplrbh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hebigplrbh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hebigplrbh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#atqrorysbt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#atqrorysbt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#atqrorysbt p { margin: 0; padding: 0; }
 #atqrorysbt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #atqrorysbt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #atqrorysbt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #atqrorysbt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #atqrorysbt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #atqrorysbt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #atqrorysbt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #atqrorysbt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #atqrorysbt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #atqrorysbt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #atqrorysbt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #atqrorysbt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #atqrorysbt .gt_spanner_row { border-bottom-style: hidden; }
 #atqrorysbt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #atqrorysbt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #atqrorysbt .gt_from_md> :first-child { margin-top: 0; }
 #atqrorysbt .gt_from_md> :last-child { margin-bottom: 0; }
 #atqrorysbt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #atqrorysbt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #atqrorysbt .gt_indent_1 { text-indent: 5px; }
 #atqrorysbt .gt_indent_2 { text-indent: calc(5px * 2); }
 #atqrorysbt .gt_indent_3 { text-indent: calc(5px * 3); }
 #atqrorysbt .gt_indent_4 { text-indent: calc(5px * 4); }
 #atqrorysbt .gt_indent_5 { text-indent: calc(5px * 5); }
 #atqrorysbt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #atqrorysbt .gt_row_group_first td { border-top-width: 2px; }
 #atqrorysbt .gt_row_group_first th { border-top-width: 2px; }
 #atqrorysbt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #atqrorysbt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #atqrorysbt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #atqrorysbt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #atqrorysbt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #atqrorysbt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #atqrorysbt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #atqrorysbt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #atqrorysbt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #atqrorysbt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #atqrorysbt .gt_left { text-align: left; }
 #atqrorysbt .gt_center { text-align: center; }
 #atqrorysbt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #atqrorysbt .gt_font_normal { font-weight: normal; }
 #atqrorysbt .gt_font_bold { font-weight: bold; }
 #atqrorysbt .gt_font_italic { font-style: italic; }
 #atqrorysbt .gt_super { font-size: 65%; }
 #atqrorysbt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #atqrorysbt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #atqrorysbt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #atqrorysbt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #atqrorysbt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #atqrorysbt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#glmksjghgz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#glmksjghgz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#glmksjghgz p { margin: 0; padding: 0; }
 #glmksjghgz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #glmksjghgz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #glmksjghgz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #glmksjghgz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #glmksjghgz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #glmksjghgz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #glmksjghgz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #glmksjghgz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #glmksjghgz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #glmksjghgz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #glmksjghgz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #glmksjghgz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #glmksjghgz .gt_spanner_row { border-bottom-style: hidden; }
 #glmksjghgz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #glmksjghgz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #glmksjghgz .gt_from_md> :first-child { margin-top: 0; }
 #glmksjghgz .gt_from_md> :last-child { margin-bottom: 0; }
 #glmksjghgz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #glmksjghgz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #glmksjghgz .gt_indent_1 { text-indent: 5px; }
 #glmksjghgz .gt_indent_2 { text-indent: calc(5px * 2); }
 #glmksjghgz .gt_indent_3 { text-indent: calc(5px * 3); }
 #glmksjghgz .gt_indent_4 { text-indent: calc(5px * 4); }
 #glmksjghgz .gt_indent_5 { text-indent: calc(5px * 5); }
 #glmksjghgz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #glmksjghgz .gt_row_group_first td { border-top-width: 2px; }
 #glmksjghgz .gt_row_group_first th { border-top-width: 2px; }
 #glmksjghgz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #glmksjghgz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #glmksjghgz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #glmksjghgz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #glmksjghgz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #glmksjghgz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #glmksjghgz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #glmksjghgz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #glmksjghgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #glmksjghgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #glmksjghgz .gt_left { text-align: left; }
 #glmksjghgz .gt_center { text-align: center; }
 #glmksjghgz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #glmksjghgz .gt_font_normal { font-weight: normal; }
 #glmksjghgz .gt_font_bold { font-weight: bold; }
 #glmksjghgz .gt_font_italic { font-style: italic; }
 #glmksjghgz .gt_super { font-size: 65%; }
 #glmksjghgz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #glmksjghgz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #glmksjghgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #glmksjghgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #glmksjghgz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #glmksjghgz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fmkjsphndq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fmkjsphndq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fmkjsphndq p { margin: 0; padding: 0; }
 #fmkjsphndq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fmkjsphndq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fmkjsphndq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fmkjsphndq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fmkjsphndq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fmkjsphndq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fmkjsphndq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fmkjsphndq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fmkjsphndq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fmkjsphndq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fmkjsphndq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fmkjsphndq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fmkjsphndq .gt_spanner_row { border-bottom-style: hidden; }
 #fmkjsphndq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fmkjsphndq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fmkjsphndq .gt_from_md> :first-child { margin-top: 0; }
 #fmkjsphndq .gt_from_md> :last-child { margin-bottom: 0; }
 #fmkjsphndq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fmkjsphndq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fmkjsphndq .gt_indent_1 { text-indent: 5px; }
 #fmkjsphndq .gt_indent_2 { text-indent: calc(5px * 2); }
 #fmkjsphndq .gt_indent_3 { text-indent: calc(5px * 3); }
 #fmkjsphndq .gt_indent_4 { text-indent: calc(5px * 4); }
 #fmkjsphndq .gt_indent_5 { text-indent: calc(5px * 5); }
 #fmkjsphndq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fmkjsphndq .gt_row_group_first td { border-top-width: 2px; }
 #fmkjsphndq .gt_row_group_first th { border-top-width: 2px; }
 #fmkjsphndq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fmkjsphndq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fmkjsphndq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fmkjsphndq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fmkjsphndq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fmkjsphndq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fmkjsphndq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fmkjsphndq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fmkjsphndq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fmkjsphndq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fmkjsphndq .gt_left { text-align: left; }
 #fmkjsphndq .gt_center { text-align: center; }
 #fmkjsphndq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fmkjsphndq .gt_font_normal { font-weight: normal; }
 #fmkjsphndq .gt_font_bold { font-weight: bold; }
 #fmkjsphndq .gt_font_italic { font-style: italic; }
 #fmkjsphndq .gt_super { font-size: 65%; }
 #fmkjsphndq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fmkjsphndq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fmkjsphndq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fmkjsphndq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fmkjsphndq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fmkjsphndq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qgcgtpgdxp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qgcgtpgdxp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qgcgtpgdxp p { margin: 0; padding: 0; }
 #qgcgtpgdxp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qgcgtpgdxp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qgcgtpgdxp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qgcgtpgdxp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qgcgtpgdxp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qgcgtpgdxp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgcgtpgdxp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qgcgtpgdxp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qgcgtpgdxp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qgcgtpgdxp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qgcgtpgdxp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qgcgtpgdxp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qgcgtpgdxp .gt_spanner_row { border-bottom-style: hidden; }
 #qgcgtpgdxp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qgcgtpgdxp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qgcgtpgdxp .gt_from_md> :first-child { margin-top: 0; }
 #qgcgtpgdxp .gt_from_md> :last-child { margin-bottom: 0; }
 #qgcgtpgdxp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qgcgtpgdxp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qgcgtpgdxp .gt_indent_1 { text-indent: 5px; }
 #qgcgtpgdxp .gt_indent_2 { text-indent: calc(5px * 2); }
 #qgcgtpgdxp .gt_indent_3 { text-indent: calc(5px * 3); }
 #qgcgtpgdxp .gt_indent_4 { text-indent: calc(5px * 4); }
 #qgcgtpgdxp .gt_indent_5 { text-indent: calc(5px * 5); }
 #qgcgtpgdxp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qgcgtpgdxp .gt_row_group_first td { border-top-width: 2px; }
 #qgcgtpgdxp .gt_row_group_first th { border-top-width: 2px; }
 #qgcgtpgdxp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qgcgtpgdxp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgcgtpgdxp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qgcgtpgdxp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qgcgtpgdxp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qgcgtpgdxp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qgcgtpgdxp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qgcgtpgdxp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qgcgtpgdxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgcgtpgdxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qgcgtpgdxp .gt_left { text-align: left; }
 #qgcgtpgdxp .gt_center { text-align: center; }
 #qgcgtpgdxp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qgcgtpgdxp .gt_font_normal { font-weight: normal; }
 #qgcgtpgdxp .gt_font_bold { font-weight: bold; }
 #qgcgtpgdxp .gt_font_italic { font-style: italic; }
 #qgcgtpgdxp .gt_super { font-size: 65%; }
 #qgcgtpgdxp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgcgtpgdxp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qgcgtpgdxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qgcgtpgdxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qgcgtpgdxp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qgcgtpgdxp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ilzbkoxbmb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ilzbkoxbmb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ilzbkoxbmb p { margin: 0; padding: 0; }
 #ilzbkoxbmb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ilzbkoxbmb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ilzbkoxbmb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ilzbkoxbmb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ilzbkoxbmb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ilzbkoxbmb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ilzbkoxbmb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ilzbkoxbmb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ilzbkoxbmb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ilzbkoxbmb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ilzbkoxbmb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ilzbkoxbmb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ilzbkoxbmb .gt_spanner_row { border-bottom-style: hidden; }
 #ilzbkoxbmb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ilzbkoxbmb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ilzbkoxbmb .gt_from_md> :first-child { margin-top: 0; }
 #ilzbkoxbmb .gt_from_md> :last-child { margin-bottom: 0; }
 #ilzbkoxbmb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ilzbkoxbmb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ilzbkoxbmb .gt_indent_1 { text-indent: 5px; }
 #ilzbkoxbmb .gt_indent_2 { text-indent: calc(5px * 2); }
 #ilzbkoxbmb .gt_indent_3 { text-indent: calc(5px * 3); }
 #ilzbkoxbmb .gt_indent_4 { text-indent: calc(5px * 4); }
 #ilzbkoxbmb .gt_indent_5 { text-indent: calc(5px * 5); }
 #ilzbkoxbmb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ilzbkoxbmb .gt_row_group_first td { border-top-width: 2px; }
 #ilzbkoxbmb .gt_row_group_first th { border-top-width: 2px; }
 #ilzbkoxbmb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ilzbkoxbmb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ilzbkoxbmb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ilzbkoxbmb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ilzbkoxbmb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ilzbkoxbmb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ilzbkoxbmb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ilzbkoxbmb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ilzbkoxbmb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ilzbkoxbmb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ilzbkoxbmb .gt_left { text-align: left; }
 #ilzbkoxbmb .gt_center { text-align: center; }
 #ilzbkoxbmb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ilzbkoxbmb .gt_font_normal { font-weight: normal; }
 #ilzbkoxbmb .gt_font_bold { font-weight: bold; }
 #ilzbkoxbmb .gt_font_italic { font-style: italic; }
 #ilzbkoxbmb .gt_super { font-size: 65%; }
 #ilzbkoxbmb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ilzbkoxbmb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ilzbkoxbmb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ilzbkoxbmb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ilzbkoxbmb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ilzbkoxbmb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#oavcuxzplt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oavcuxzplt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oavcuxzplt p { margin: 0; padding: 0; }
 #oavcuxzplt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oavcuxzplt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oavcuxzplt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oavcuxzplt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oavcuxzplt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oavcuxzplt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oavcuxzplt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oavcuxzplt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oavcuxzplt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oavcuxzplt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oavcuxzplt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oavcuxzplt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oavcuxzplt .gt_spanner_row { border-bottom-style: hidden; }
 #oavcuxzplt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oavcuxzplt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oavcuxzplt .gt_from_md> :first-child { margin-top: 0; }
 #oavcuxzplt .gt_from_md> :last-child { margin-bottom: 0; }
 #oavcuxzplt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oavcuxzplt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oavcuxzplt .gt_indent_1 { text-indent: 5px; }
 #oavcuxzplt .gt_indent_2 { text-indent: calc(5px * 2); }
 #oavcuxzplt .gt_indent_3 { text-indent: calc(5px * 3); }
 #oavcuxzplt .gt_indent_4 { text-indent: calc(5px * 4); }
 #oavcuxzplt .gt_indent_5 { text-indent: calc(5px * 5); }
 #oavcuxzplt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oavcuxzplt .gt_row_group_first td { border-top-width: 2px; }
 #oavcuxzplt .gt_row_group_first th { border-top-width: 2px; }
 #oavcuxzplt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oavcuxzplt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oavcuxzplt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oavcuxzplt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oavcuxzplt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oavcuxzplt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oavcuxzplt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oavcuxzplt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oavcuxzplt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oavcuxzplt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oavcuxzplt .gt_left { text-align: left; }
 #oavcuxzplt .gt_center { text-align: center; }
 #oavcuxzplt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oavcuxzplt .gt_font_normal { font-weight: normal; }
 #oavcuxzplt .gt_font_bold { font-weight: bold; }
 #oavcuxzplt .gt_font_italic { font-style: italic; }
 #oavcuxzplt .gt_super { font-size: 65%; }
 #oavcuxzplt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oavcuxzplt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oavcuxzplt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oavcuxzplt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oavcuxzplt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oavcuxzplt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#suefwkjlto table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#suefwkjlto thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#suefwkjlto p { margin: 0; padding: 0; }
 #suefwkjlto .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #suefwkjlto .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #suefwkjlto .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #suefwkjlto .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #suefwkjlto .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #suefwkjlto .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #suefwkjlto .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #suefwkjlto .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #suefwkjlto .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #suefwkjlto .gt_column_spanner_outer:first-child { padding-left: 0; }
 #suefwkjlto .gt_column_spanner_outer:last-child { padding-right: 0; }
 #suefwkjlto .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #suefwkjlto .gt_spanner_row { border-bottom-style: hidden; }
 #suefwkjlto .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #suefwkjlto .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #suefwkjlto .gt_from_md> :first-child { margin-top: 0; }
 #suefwkjlto .gt_from_md> :last-child { margin-bottom: 0; }
 #suefwkjlto .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #suefwkjlto .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #suefwkjlto .gt_indent_1 { text-indent: 5px; }
 #suefwkjlto .gt_indent_2 { text-indent: calc(5px * 2); }
 #suefwkjlto .gt_indent_3 { text-indent: calc(5px * 3); }
 #suefwkjlto .gt_indent_4 { text-indent: calc(5px * 4); }
 #suefwkjlto .gt_indent_5 { text-indent: calc(5px * 5); }
 #suefwkjlto .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #suefwkjlto .gt_row_group_first td { border-top-width: 2px; }
 #suefwkjlto .gt_row_group_first th { border-top-width: 2px; }
 #suefwkjlto .gt_striped { color: #333333; background-color: #F4F4F4; }
 #suefwkjlto .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #suefwkjlto .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #suefwkjlto .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #suefwkjlto .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #suefwkjlto .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #suefwkjlto .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #suefwkjlto .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #suefwkjlto .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #suefwkjlto .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #suefwkjlto .gt_left { text-align: left; }
 #suefwkjlto .gt_center { text-align: center; }
 #suefwkjlto .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #suefwkjlto .gt_font_normal { font-weight: normal; }
 #suefwkjlto .gt_font_bold { font-weight: bold; }
 #suefwkjlto .gt_font_italic { font-style: italic; }
 #suefwkjlto .gt_super { font-size: 65%; }
 #suefwkjlto .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #suefwkjlto .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #suefwkjlto .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #suefwkjlto .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #suefwkjlto .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #suefwkjlto .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jhvuiqhwdh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jhvuiqhwdh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jhvuiqhwdh p { margin: 0; padding: 0; }
 #jhvuiqhwdh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jhvuiqhwdh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jhvuiqhwdh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jhvuiqhwdh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jhvuiqhwdh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jhvuiqhwdh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jhvuiqhwdh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jhvuiqhwdh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jhvuiqhwdh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jhvuiqhwdh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jhvuiqhwdh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jhvuiqhwdh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jhvuiqhwdh .gt_spanner_row { border-bottom-style: hidden; }
 #jhvuiqhwdh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jhvuiqhwdh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jhvuiqhwdh .gt_from_md> :first-child { margin-top: 0; }
 #jhvuiqhwdh .gt_from_md> :last-child { margin-bottom: 0; }
 #jhvuiqhwdh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jhvuiqhwdh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jhvuiqhwdh .gt_indent_1 { text-indent: 5px; }
 #jhvuiqhwdh .gt_indent_2 { text-indent: calc(5px * 2); }
 #jhvuiqhwdh .gt_indent_3 { text-indent: calc(5px * 3); }
 #jhvuiqhwdh .gt_indent_4 { text-indent: calc(5px * 4); }
 #jhvuiqhwdh .gt_indent_5 { text-indent: calc(5px * 5); }
 #jhvuiqhwdh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jhvuiqhwdh .gt_row_group_first td { border-top-width: 2px; }
 #jhvuiqhwdh .gt_row_group_first th { border-top-width: 2px; }
 #jhvuiqhwdh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jhvuiqhwdh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jhvuiqhwdh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jhvuiqhwdh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jhvuiqhwdh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jhvuiqhwdh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jhvuiqhwdh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jhvuiqhwdh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jhvuiqhwdh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jhvuiqhwdh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jhvuiqhwdh .gt_left { text-align: left; }
 #jhvuiqhwdh .gt_center { text-align: center; }
 #jhvuiqhwdh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jhvuiqhwdh .gt_font_normal { font-weight: normal; }
 #jhvuiqhwdh .gt_font_bold { font-weight: bold; }
 #jhvuiqhwdh .gt_font_italic { font-style: italic; }
 #jhvuiqhwdh .gt_super { font-size: 65%; }
 #jhvuiqhwdh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jhvuiqhwdh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jhvuiqhwdh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jhvuiqhwdh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jhvuiqhwdh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jhvuiqhwdh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#plfitlkjvu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#plfitlkjvu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#plfitlkjvu p { margin: 0; padding: 0; }
 #plfitlkjvu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #plfitlkjvu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #plfitlkjvu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #plfitlkjvu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #plfitlkjvu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #plfitlkjvu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #plfitlkjvu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #plfitlkjvu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #plfitlkjvu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #plfitlkjvu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #plfitlkjvu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #plfitlkjvu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #plfitlkjvu .gt_spanner_row { border-bottom-style: hidden; }
 #plfitlkjvu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #plfitlkjvu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #plfitlkjvu .gt_from_md> :first-child { margin-top: 0; }
 #plfitlkjvu .gt_from_md> :last-child { margin-bottom: 0; }
 #plfitlkjvu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #plfitlkjvu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #plfitlkjvu .gt_indent_1 { text-indent: 5px; }
 #plfitlkjvu .gt_indent_2 { text-indent: calc(5px * 2); }
 #plfitlkjvu .gt_indent_3 { text-indent: calc(5px * 3); }
 #plfitlkjvu .gt_indent_4 { text-indent: calc(5px * 4); }
 #plfitlkjvu .gt_indent_5 { text-indent: calc(5px * 5); }
 #plfitlkjvu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #plfitlkjvu .gt_row_group_first td { border-top-width: 2px; }
 #plfitlkjvu .gt_row_group_first th { border-top-width: 2px; }
 #plfitlkjvu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #plfitlkjvu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #plfitlkjvu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #plfitlkjvu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #plfitlkjvu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #plfitlkjvu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #plfitlkjvu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #plfitlkjvu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #plfitlkjvu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #plfitlkjvu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #plfitlkjvu .gt_left { text-align: left; }
 #plfitlkjvu .gt_center { text-align: center; }
 #plfitlkjvu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #plfitlkjvu .gt_font_normal { font-weight: normal; }
 #plfitlkjvu .gt_font_bold { font-weight: bold; }
 #plfitlkjvu .gt_font_italic { font-style: italic; }
 #plfitlkjvu .gt_super { font-size: 65%; }
 #plfitlkjvu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #plfitlkjvu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #plfitlkjvu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #plfitlkjvu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #plfitlkjvu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #plfitlkjvu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qeqcsdkqra table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qeqcsdkqra thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qeqcsdkqra p { margin: 0; padding: 0; }
 #qeqcsdkqra .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qeqcsdkqra .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qeqcsdkqra .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qeqcsdkqra .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qeqcsdkqra .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qeqcsdkqra .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeqcsdkqra .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qeqcsdkqra .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qeqcsdkqra .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qeqcsdkqra .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qeqcsdkqra .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qeqcsdkqra .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qeqcsdkqra .gt_spanner_row { border-bottom-style: hidden; }
 #qeqcsdkqra .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qeqcsdkqra .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qeqcsdkqra .gt_from_md> :first-child { margin-top: 0; }
 #qeqcsdkqra .gt_from_md> :last-child { margin-bottom: 0; }
 #qeqcsdkqra .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qeqcsdkqra .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qeqcsdkqra .gt_indent_1 { text-indent: 5px; }
 #qeqcsdkqra .gt_indent_2 { text-indent: calc(5px * 2); }
 #qeqcsdkqra .gt_indent_3 { text-indent: calc(5px * 3); }
 #qeqcsdkqra .gt_indent_4 { text-indent: calc(5px * 4); }
 #qeqcsdkqra .gt_indent_5 { text-indent: calc(5px * 5); }
 #qeqcsdkqra .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qeqcsdkqra .gt_row_group_first td { border-top-width: 2px; }
 #qeqcsdkqra .gt_row_group_first th { border-top-width: 2px; }
 #qeqcsdkqra .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qeqcsdkqra .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeqcsdkqra .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qeqcsdkqra .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qeqcsdkqra .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeqcsdkqra .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qeqcsdkqra .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qeqcsdkqra .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qeqcsdkqra .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeqcsdkqra .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qeqcsdkqra .gt_left { text-align: left; }
 #qeqcsdkqra .gt_center { text-align: center; }
 #qeqcsdkqra .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qeqcsdkqra .gt_font_normal { font-weight: normal; }
 #qeqcsdkqra .gt_font_bold { font-weight: bold; }
 #qeqcsdkqra .gt_font_italic { font-style: italic; }
 #qeqcsdkqra .gt_super { font-size: 65%; }
 #qeqcsdkqra .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeqcsdkqra .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qeqcsdkqra .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeqcsdkqra .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qeqcsdkqra .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qeqcsdkqra .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bagsomepzj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bagsomepzj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bagsomepzj p { margin: 0; padding: 0; }
 #bagsomepzj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bagsomepzj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bagsomepzj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bagsomepzj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bagsomepzj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bagsomepzj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bagsomepzj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bagsomepzj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bagsomepzj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bagsomepzj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bagsomepzj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bagsomepzj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bagsomepzj .gt_spanner_row { border-bottom-style: hidden; }
 #bagsomepzj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bagsomepzj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bagsomepzj .gt_from_md> :first-child { margin-top: 0; }
 #bagsomepzj .gt_from_md> :last-child { margin-bottom: 0; }
 #bagsomepzj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bagsomepzj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bagsomepzj .gt_indent_1 { text-indent: 5px; }
 #bagsomepzj .gt_indent_2 { text-indent: calc(5px * 2); }
 #bagsomepzj .gt_indent_3 { text-indent: calc(5px * 3); }
 #bagsomepzj .gt_indent_4 { text-indent: calc(5px * 4); }
 #bagsomepzj .gt_indent_5 { text-indent: calc(5px * 5); }
 #bagsomepzj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bagsomepzj .gt_row_group_first td { border-top-width: 2px; }
 #bagsomepzj .gt_row_group_first th { border-top-width: 2px; }
 #bagsomepzj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bagsomepzj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bagsomepzj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bagsomepzj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bagsomepzj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bagsomepzj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bagsomepzj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bagsomepzj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bagsomepzj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bagsomepzj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bagsomepzj .gt_left { text-align: left; }
 #bagsomepzj .gt_center { text-align: center; }
 #bagsomepzj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bagsomepzj .gt_font_normal { font-weight: normal; }
 #bagsomepzj .gt_font_bold { font-weight: bold; }
 #bagsomepzj .gt_font_italic { font-style: italic; }
 #bagsomepzj .gt_super { font-size: 65%; }
 #bagsomepzj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bagsomepzj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bagsomepzj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bagsomepzj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bagsomepzj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bagsomepzj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bjxszuqafz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bjxszuqafz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bjxszuqafz p { margin: 0; padding: 0; }
 #bjxszuqafz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bjxszuqafz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bjxszuqafz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bjxszuqafz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bjxszuqafz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bjxszuqafz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bjxszuqafz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bjxszuqafz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bjxszuqafz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bjxszuqafz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bjxszuqafz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bjxszuqafz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bjxszuqafz .gt_spanner_row { border-bottom-style: hidden; }
 #bjxszuqafz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bjxszuqafz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bjxszuqafz .gt_from_md> :first-child { margin-top: 0; }
 #bjxszuqafz .gt_from_md> :last-child { margin-bottom: 0; }
 #bjxszuqafz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bjxszuqafz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bjxszuqafz .gt_indent_1 { text-indent: 5px; }
 #bjxszuqafz .gt_indent_2 { text-indent: calc(5px * 2); }
 #bjxszuqafz .gt_indent_3 { text-indent: calc(5px * 3); }
 #bjxszuqafz .gt_indent_4 { text-indent: calc(5px * 4); }
 #bjxszuqafz .gt_indent_5 { text-indent: calc(5px * 5); }
 #bjxszuqafz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bjxszuqafz .gt_row_group_first td { border-top-width: 2px; }
 #bjxszuqafz .gt_row_group_first th { border-top-width: 2px; }
 #bjxszuqafz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bjxszuqafz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bjxszuqafz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bjxszuqafz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bjxszuqafz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bjxszuqafz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bjxszuqafz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bjxszuqafz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bjxszuqafz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bjxszuqafz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bjxszuqafz .gt_left { text-align: left; }
 #bjxszuqafz .gt_center { text-align: center; }
 #bjxszuqafz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bjxszuqafz .gt_font_normal { font-weight: normal; }
 #bjxszuqafz .gt_font_bold { font-weight: bold; }
 #bjxszuqafz .gt_font_italic { font-style: italic; }
 #bjxszuqafz .gt_super { font-size: 65%; }
 #bjxszuqafz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bjxszuqafz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bjxszuqafz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bjxszuqafz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bjxszuqafz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bjxszuqafz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lqilsnwmux table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lqilsnwmux thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lqilsnwmux p { margin: 0; padding: 0; }
 #lqilsnwmux .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lqilsnwmux .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lqilsnwmux .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lqilsnwmux .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lqilsnwmux .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lqilsnwmux .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lqilsnwmux .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lqilsnwmux .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lqilsnwmux .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lqilsnwmux .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lqilsnwmux .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lqilsnwmux .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lqilsnwmux .gt_spanner_row { border-bottom-style: hidden; }
 #lqilsnwmux .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lqilsnwmux .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lqilsnwmux .gt_from_md> :first-child { margin-top: 0; }
 #lqilsnwmux .gt_from_md> :last-child { margin-bottom: 0; }
 #lqilsnwmux .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lqilsnwmux .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lqilsnwmux .gt_indent_1 { text-indent: 5px; }
 #lqilsnwmux .gt_indent_2 { text-indent: calc(5px * 2); }
 #lqilsnwmux .gt_indent_3 { text-indent: calc(5px * 3); }
 #lqilsnwmux .gt_indent_4 { text-indent: calc(5px * 4); }
 #lqilsnwmux .gt_indent_5 { text-indent: calc(5px * 5); }
 #lqilsnwmux .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lqilsnwmux .gt_row_group_first td { border-top-width: 2px; }
 #lqilsnwmux .gt_row_group_first th { border-top-width: 2px; }
 #lqilsnwmux .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lqilsnwmux .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lqilsnwmux .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lqilsnwmux .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lqilsnwmux .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lqilsnwmux .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lqilsnwmux .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lqilsnwmux .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lqilsnwmux .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lqilsnwmux .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lqilsnwmux .gt_left { text-align: left; }
 #lqilsnwmux .gt_center { text-align: center; }
 #lqilsnwmux .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lqilsnwmux .gt_font_normal { font-weight: normal; }
 #lqilsnwmux .gt_font_bold { font-weight: bold; }
 #lqilsnwmux .gt_font_italic { font-style: italic; }
 #lqilsnwmux .gt_super { font-size: 65%; }
 #lqilsnwmux .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lqilsnwmux .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lqilsnwmux .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lqilsnwmux .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lqilsnwmux .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lqilsnwmux .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wmwvsfddux table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wmwvsfddux thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wmwvsfddux p { margin: 0; padding: 0; }
 #wmwvsfddux .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wmwvsfddux .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wmwvsfddux .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wmwvsfddux .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wmwvsfddux .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wmwvsfddux .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wmwvsfddux .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wmwvsfddux .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wmwvsfddux .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wmwvsfddux .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wmwvsfddux .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wmwvsfddux .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wmwvsfddux .gt_spanner_row { border-bottom-style: hidden; }
 #wmwvsfddux .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wmwvsfddux .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wmwvsfddux .gt_from_md> :first-child { margin-top: 0; }
 #wmwvsfddux .gt_from_md> :last-child { margin-bottom: 0; }
 #wmwvsfddux .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wmwvsfddux .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wmwvsfddux .gt_indent_1 { text-indent: 5px; }
 #wmwvsfddux .gt_indent_2 { text-indent: calc(5px * 2); }
 #wmwvsfddux .gt_indent_3 { text-indent: calc(5px * 3); }
 #wmwvsfddux .gt_indent_4 { text-indent: calc(5px * 4); }
 #wmwvsfddux .gt_indent_5 { text-indent: calc(5px * 5); }
 #wmwvsfddux .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wmwvsfddux .gt_row_group_first td { border-top-width: 2px; }
 #wmwvsfddux .gt_row_group_first th { border-top-width: 2px; }
 #wmwvsfddux .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wmwvsfddux .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wmwvsfddux .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wmwvsfddux .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wmwvsfddux .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wmwvsfddux .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wmwvsfddux .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wmwvsfddux .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wmwvsfddux .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wmwvsfddux .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wmwvsfddux .gt_left { text-align: left; }
 #wmwvsfddux .gt_center { text-align: center; }
 #wmwvsfddux .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wmwvsfddux .gt_font_normal { font-weight: normal; }
 #wmwvsfddux .gt_font_bold { font-weight: bold; }
 #wmwvsfddux .gt_font_italic { font-style: italic; }
 #wmwvsfddux .gt_super { font-size: 65%; }
 #wmwvsfddux .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wmwvsfddux .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wmwvsfddux .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wmwvsfddux .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wmwvsfddux .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wmwvsfddux .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jzcpscajta table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jzcpscajta thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jzcpscajta p { margin: 0; padding: 0; }
 #jzcpscajta .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jzcpscajta .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jzcpscajta .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jzcpscajta .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jzcpscajta .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jzcpscajta .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jzcpscajta .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jzcpscajta .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jzcpscajta .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jzcpscajta .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jzcpscajta .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jzcpscajta .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jzcpscajta .gt_spanner_row { border-bottom-style: hidden; }
 #jzcpscajta .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jzcpscajta .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jzcpscajta .gt_from_md> :first-child { margin-top: 0; }
 #jzcpscajta .gt_from_md> :last-child { margin-bottom: 0; }
 #jzcpscajta .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jzcpscajta .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jzcpscajta .gt_indent_1 { text-indent: 5px; }
 #jzcpscajta .gt_indent_2 { text-indent: calc(5px * 2); }
 #jzcpscajta .gt_indent_3 { text-indent: calc(5px * 3); }
 #jzcpscajta .gt_indent_4 { text-indent: calc(5px * 4); }
 #jzcpscajta .gt_indent_5 { text-indent: calc(5px * 5); }
 #jzcpscajta .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jzcpscajta .gt_row_group_first td { border-top-width: 2px; }
 #jzcpscajta .gt_row_group_first th { border-top-width: 2px; }
 #jzcpscajta .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jzcpscajta .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jzcpscajta .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jzcpscajta .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jzcpscajta .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jzcpscajta .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jzcpscajta .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jzcpscajta .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jzcpscajta .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jzcpscajta .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jzcpscajta .gt_left { text-align: left; }
 #jzcpscajta .gt_center { text-align: center; }
 #jzcpscajta .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jzcpscajta .gt_font_normal { font-weight: normal; }
 #jzcpscajta .gt_font_bold { font-weight: bold; }
 #jzcpscajta .gt_font_italic { font-style: italic; }
 #jzcpscajta .gt_super { font-size: 65%; }
 #jzcpscajta .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jzcpscajta .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jzcpscajta .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jzcpscajta .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jzcpscajta .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jzcpscajta .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fjhmjmfpuq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fjhmjmfpuq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fjhmjmfpuq p { margin: 0; padding: 0; }
 #fjhmjmfpuq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fjhmjmfpuq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fjhmjmfpuq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fjhmjmfpuq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fjhmjmfpuq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fjhmjmfpuq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fjhmjmfpuq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fjhmjmfpuq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fjhmjmfpuq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fjhmjmfpuq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fjhmjmfpuq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fjhmjmfpuq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fjhmjmfpuq .gt_spanner_row { border-bottom-style: hidden; }
 #fjhmjmfpuq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fjhmjmfpuq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fjhmjmfpuq .gt_from_md> :first-child { margin-top: 0; }
 #fjhmjmfpuq .gt_from_md> :last-child { margin-bottom: 0; }
 #fjhmjmfpuq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fjhmjmfpuq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fjhmjmfpuq .gt_indent_1 { text-indent: 5px; }
 #fjhmjmfpuq .gt_indent_2 { text-indent: calc(5px * 2); }
 #fjhmjmfpuq .gt_indent_3 { text-indent: calc(5px * 3); }
 #fjhmjmfpuq .gt_indent_4 { text-indent: calc(5px * 4); }
 #fjhmjmfpuq .gt_indent_5 { text-indent: calc(5px * 5); }
 #fjhmjmfpuq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fjhmjmfpuq .gt_row_group_first td { border-top-width: 2px; }
 #fjhmjmfpuq .gt_row_group_first th { border-top-width: 2px; }
 #fjhmjmfpuq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fjhmjmfpuq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fjhmjmfpuq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fjhmjmfpuq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fjhmjmfpuq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fjhmjmfpuq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fjhmjmfpuq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fjhmjmfpuq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fjhmjmfpuq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fjhmjmfpuq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fjhmjmfpuq .gt_left { text-align: left; }
 #fjhmjmfpuq .gt_center { text-align: center; }
 #fjhmjmfpuq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fjhmjmfpuq .gt_font_normal { font-weight: normal; }
 #fjhmjmfpuq .gt_font_bold { font-weight: bold; }
 #fjhmjmfpuq .gt_font_italic { font-style: italic; }
 #fjhmjmfpuq .gt_super { font-size: 65%; }
 #fjhmjmfpuq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fjhmjmfpuq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fjhmjmfpuq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fjhmjmfpuq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fjhmjmfpuq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fjhmjmfpuq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
