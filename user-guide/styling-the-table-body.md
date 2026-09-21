# Styling the Table Body

Visual styling helps draw attention to important values and makes patterns in your data easier to spot. **Great Tables** provides a flexible system for applying fills, borders, and text styles to cells in the table body. This page covers the fundamentals of cell-level styling, from targeting specific cells to using column values and expressions to drive dynamic styles.

Targeted styling is most effective when used sparingly to draw attention to specific values (outliers, thresholds, or key comparisons). Overusing color and borders can make a table harder to read rather than easier. A good rule of thumb: if everything is highlighted, nothing is. Start with the most important insight you want the reader to take away, and style just enough to guide their eye there.

**Great Tables** can add styles (like color, text properties, and borders) on many different parts of the displayed table. The following set of examples shows how to set styles on the body of table, where the data cells are located.

For the examples on this page, we'll use the included airquality dataset to set up [GT](../reference/GT.md#great_tables.GT) objects for both **Pandas** and **Polars** DataFrames.


``` python
import polars as pl

from great_tables import GT, from_column, style, loc
from great_tables.data import airquality

air_head = airquality.head()

gt_air = GT(air_head)
gt_pl_air = GT(pl.from_pandas(air_head))
```


> **Note: Note**
>
> When using Great Tables with VS Code, the IDE suppresses some forms of table styling displayed in notebooks. For example, border styles might not appear. Use `.show("browser")` to see the styled GT table in a separate browser window.


# Style basics

We use the [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) method in combination with [loc.body()](../reference/loc.body.md#great_tables.loc.body) to set styles on cells of data in the table body. For example, the table-making code below applies a yellow background color to specific cells.


``` python
gt_air.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(columns="Temp", rows=[1, 2])
)
```


<style>
#gicbnhdakw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gicbnhdakw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gicbnhdakw p { margin: 0; padding: 0; }
 #gicbnhdakw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gicbnhdakw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gicbnhdakw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gicbnhdakw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gicbnhdakw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gicbnhdakw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gicbnhdakw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gicbnhdakw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gicbnhdakw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gicbnhdakw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gicbnhdakw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gicbnhdakw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gicbnhdakw .gt_spanner_row { border-bottom-style: hidden; }
 #gicbnhdakw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gicbnhdakw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gicbnhdakw .gt_from_md> :first-child { margin-top: 0; }
 #gicbnhdakw .gt_from_md> :last-child { margin-bottom: 0; }
 #gicbnhdakw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gicbnhdakw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gicbnhdakw .gt_indent_1 { text-indent: 5px; }
 #gicbnhdakw .gt_indent_2 { text-indent: calc(5px * 2); }
 #gicbnhdakw .gt_indent_3 { text-indent: calc(5px * 3); }
 #gicbnhdakw .gt_indent_4 { text-indent: calc(5px * 4); }
 #gicbnhdakw .gt_indent_5 { text-indent: calc(5px * 5); }
 #gicbnhdakw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gicbnhdakw .gt_row_group_first td { border-top-width: 2px; }
 #gicbnhdakw .gt_row_group_first th { border-top-width: 2px; }
 #gicbnhdakw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gicbnhdakw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gicbnhdakw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gicbnhdakw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gicbnhdakw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gicbnhdakw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gicbnhdakw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gicbnhdakw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gicbnhdakw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gicbnhdakw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gicbnhdakw .gt_left { text-align: left; }
 #gicbnhdakw .gt_center { text-align: center; }
 #gicbnhdakw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gicbnhdakw .gt_font_normal { font-weight: normal; }
 #gicbnhdakw .gt_font_bold { font-weight: bold; }
 #gicbnhdakw .gt_font_italic { font-style: italic; }
 #gicbnhdakw .gt_super { font-size: 65%; }
 #gicbnhdakw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gicbnhdakw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gicbnhdakw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gicbnhdakw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gicbnhdakw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gicbnhdakw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
|       |         | 14.3 | 56   | 5     | 5   |


There are two important arguments to [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style): `style=` and `locations=`. We are calling a specific function for each of these:

- [style.fill()](../reference/style.fill.md#great_tables.style.fill): the type of style to apply. In this case the *fill* (or background color).
- [loc.body()](../reference/loc.body.md#great_tables.loc.body): the area we want to style. In this case, it's the table body with specific columns and rows specified.

In addition to [style.fill()](../reference/style.fill.md#great_tables.style.fill), several other styling functions exist. We'll look at styling borders and text in the following sections.


## Customizing Borders

Let's use [style.borders()](../reference/style.borders.md#great_tables.style.borders) to place borders around targeted cells. In this next example, the table has a red dashed border above two rows.


``` python
gt_air.tab_style(
    style=style.borders(sides="top", color="red", style="dashed", weight="3px"),
    locations=loc.body(rows=[1, 2])
)
```


<style>
#pfgeqjswnb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pfgeqjswnb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pfgeqjswnb p { margin: 0; padding: 0; }
 #pfgeqjswnb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pfgeqjswnb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pfgeqjswnb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pfgeqjswnb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pfgeqjswnb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pfgeqjswnb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfgeqjswnb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pfgeqjswnb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pfgeqjswnb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pfgeqjswnb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pfgeqjswnb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pfgeqjswnb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pfgeqjswnb .gt_spanner_row { border-bottom-style: hidden; }
 #pfgeqjswnb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pfgeqjswnb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pfgeqjswnb .gt_from_md> :first-child { margin-top: 0; }
 #pfgeqjswnb .gt_from_md> :last-child { margin-bottom: 0; }
 #pfgeqjswnb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pfgeqjswnb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pfgeqjswnb .gt_indent_1 { text-indent: 5px; }
 #pfgeqjswnb .gt_indent_2 { text-indent: calc(5px * 2); }
 #pfgeqjswnb .gt_indent_3 { text-indent: calc(5px * 3); }
 #pfgeqjswnb .gt_indent_4 { text-indent: calc(5px * 4); }
 #pfgeqjswnb .gt_indent_5 { text-indent: calc(5px * 5); }
 #pfgeqjswnb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pfgeqjswnb .gt_row_group_first td { border-top-width: 2px; }
 #pfgeqjswnb .gt_row_group_first th { border-top-width: 2px; }
 #pfgeqjswnb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pfgeqjswnb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfgeqjswnb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pfgeqjswnb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pfgeqjswnb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfgeqjswnb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pfgeqjswnb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pfgeqjswnb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pfgeqjswnb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfgeqjswnb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pfgeqjswnb .gt_left { text-align: left; }
 #pfgeqjswnb .gt_center { text-align: center; }
 #pfgeqjswnb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pfgeqjswnb .gt_font_normal { font-weight: normal; }
 #pfgeqjswnb .gt_font_bold { font-weight: bold; }
 #pfgeqjswnb .gt_font_italic { font-style: italic; }
 #pfgeqjswnb .gt_super { font-size: 65%; }
 #pfgeqjswnb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfgeqjswnb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pfgeqjswnb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfgeqjswnb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pfgeqjswnb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pfgeqjswnb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
|       |         | 14.3 | 56   | 5     | 5   |


The red dashed border appears above rows 1 and 2, providing a visual separator. You can control the side (`"top"`, `"bottom"`, `"left"`, `"right"`), color, style, and weight of the border.


## Customizing Text

We can style text with by using the [style.text()](../reference/style.text.md#great_tables.style.text) function. This gives us many customization possibilities for any text we target. For example, the `Solar_R` column below has green, bolded text in a custom font.


``` python
gt_air.tab_style(
    style=style.text(color="green", font="Times New Roman", weight="bold"),
    locations=loc.body(columns="Solar_R")
)
```


<style>
#rjkshdvfpt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rjkshdvfpt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rjkshdvfpt p { margin: 0; padding: 0; }
 #rjkshdvfpt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rjkshdvfpt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rjkshdvfpt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rjkshdvfpt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rjkshdvfpt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rjkshdvfpt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rjkshdvfpt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rjkshdvfpt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rjkshdvfpt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rjkshdvfpt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rjkshdvfpt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rjkshdvfpt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rjkshdvfpt .gt_spanner_row { border-bottom-style: hidden; }
 #rjkshdvfpt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rjkshdvfpt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rjkshdvfpt .gt_from_md> :first-child { margin-top: 0; }
 #rjkshdvfpt .gt_from_md> :last-child { margin-bottom: 0; }
 #rjkshdvfpt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rjkshdvfpt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rjkshdvfpt .gt_indent_1 { text-indent: 5px; }
 #rjkshdvfpt .gt_indent_2 { text-indent: calc(5px * 2); }
 #rjkshdvfpt .gt_indent_3 { text-indent: calc(5px * 3); }
 #rjkshdvfpt .gt_indent_4 { text-indent: calc(5px * 4); }
 #rjkshdvfpt .gt_indent_5 { text-indent: calc(5px * 5); }
 #rjkshdvfpt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rjkshdvfpt .gt_row_group_first td { border-top-width: 2px; }
 #rjkshdvfpt .gt_row_group_first th { border-top-width: 2px; }
 #rjkshdvfpt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rjkshdvfpt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rjkshdvfpt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rjkshdvfpt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rjkshdvfpt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rjkshdvfpt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rjkshdvfpt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rjkshdvfpt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rjkshdvfpt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rjkshdvfpt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rjkshdvfpt .gt_left { text-align: left; }
 #rjkshdvfpt .gt_center { text-align: center; }
 #rjkshdvfpt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rjkshdvfpt .gt_font_normal { font-weight: normal; }
 #rjkshdvfpt .gt_font_bold { font-weight: bold; }
 #rjkshdvfpt .gt_font_italic { font-style: italic; }
 #rjkshdvfpt .gt_super { font-size: 65%; }
 #rjkshdvfpt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rjkshdvfpt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rjkshdvfpt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rjkshdvfpt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rjkshdvfpt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rjkshdvfpt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
|       |         | 14.3 | 56   | 5     | 5   |


The `Solar_R` column text appears in green, bold, and in the Times New Roman font. The [style.text()](../reference/style.text.md#great_tables.style.text) function supports additional options like `size=`, `style=` (italic), and `decorate=` (underline, line-through).


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
#xirknmhyyo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xirknmhyyo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xirknmhyyo p { margin: 0; padding: 0; }
 #xirknmhyyo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xirknmhyyo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xirknmhyyo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xirknmhyyo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xirknmhyyo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xirknmhyyo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xirknmhyyo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xirknmhyyo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xirknmhyyo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xirknmhyyo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xirknmhyyo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xirknmhyyo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xirknmhyyo .gt_spanner_row { border-bottom-style: hidden; }
 #xirknmhyyo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xirknmhyyo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xirknmhyyo .gt_from_md> :first-child { margin-top: 0; }
 #xirknmhyyo .gt_from_md> :last-child { margin-bottom: 0; }
 #xirknmhyyo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xirknmhyyo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xirknmhyyo .gt_indent_1 { text-indent: 5px; }
 #xirknmhyyo .gt_indent_2 { text-indent: calc(5px * 2); }
 #xirknmhyyo .gt_indent_3 { text-indent: calc(5px * 3); }
 #xirknmhyyo .gt_indent_4 { text-indent: calc(5px * 4); }
 #xirknmhyyo .gt_indent_5 { text-indent: calc(5px * 5); }
 #xirknmhyyo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xirknmhyyo .gt_row_group_first td { border-top-width: 2px; }
 #xirknmhyyo .gt_row_group_first th { border-top-width: 2px; }
 #xirknmhyyo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xirknmhyyo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xirknmhyyo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xirknmhyyo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xirknmhyyo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xirknmhyyo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xirknmhyyo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xirknmhyyo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xirknmhyyo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xirknmhyyo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xirknmhyyo .gt_left { text-align: left; }
 #xirknmhyyo .gt_center { text-align: center; }
 #xirknmhyyo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xirknmhyyo .gt_font_normal { font-weight: normal; }
 #xirknmhyyo .gt_font_bold { font-weight: bold; }
 #xirknmhyyo .gt_font_italic { font-style: italic; }
 #xirknmhyyo .gt_super { font-size: 65%; }
 #xirknmhyyo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xirknmhyyo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xirknmhyyo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xirknmhyyo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xirknmhyyo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xirknmhyyo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| x   | background  |
|-----|-------------|
| 1   | lightyellow |
| 2   | lightblue   |


Notice that in the code above, we used values from the `background` column to specify the fill color for each styled row.

In the next few sections, we'll first show how this combines nicely with the [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide) method, then, we'll demonstrate how to use **Polars** expressions to do everything much more simply.


## Combining Styling with [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide)

One common approach is to specify a style from a column, and then hide that column in the final output. For example, we can add a background column to our `airquality` data:


``` python
color_map = {
    True: "lightyellow",
    False: "lightblue"
}

with_color = air_head.assign(
    background=(air_head["Temp"] > 70).replace(color_map)
)

with_color
```


|     | Ozone | Solar_R | Wind | Temp | Month | Day | background  |
|-----|-------|---------|------|------|-------|-----|-------------|
| 0   | 41.0  | 190.0   | 7.4  | 67   | 5     | 1   | lightblue   |
| 1   | 36.0  | 118.0   | 8.0  | 72   | 5     | 2   | lightyellow |
| 2   | 12.0  | 149.0   | 12.6 | 74   | 5     | 3   | lightyellow |
| 3   | 18.0  | 313.0   | 11.5 | 62   | 5     | 4   | lightblue   |
| 4   | NaN   | NaN     | 14.3 | 56   | 5     | 5   | lightblue   |


Notice that the dataset now has a `background` column set to either `"lightyellow"` or `"lightblue"`, depending on whether `Temp` is above `70`.

We can then use this `background` column to set the fill color of certain body cells, and then hide the `background` column since we don't need that in our finalized display table:


``` python
(
    GT(with_color)
    .tab_style(
        style=style.fill(color=from_column(column="background")),
        locations=loc.body(columns="Temp")
    )
    .cols_hide(columns="background")
)
```


<style>
#lzlmaeatmx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lzlmaeatmx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lzlmaeatmx p { margin: 0; padding: 0; }
 #lzlmaeatmx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lzlmaeatmx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lzlmaeatmx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lzlmaeatmx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lzlmaeatmx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lzlmaeatmx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lzlmaeatmx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lzlmaeatmx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lzlmaeatmx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lzlmaeatmx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lzlmaeatmx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lzlmaeatmx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lzlmaeatmx .gt_spanner_row { border-bottom-style: hidden; }
 #lzlmaeatmx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lzlmaeatmx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lzlmaeatmx .gt_from_md> :first-child { margin-top: 0; }
 #lzlmaeatmx .gt_from_md> :last-child { margin-bottom: 0; }
 #lzlmaeatmx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lzlmaeatmx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lzlmaeatmx .gt_indent_1 { text-indent: 5px; }
 #lzlmaeatmx .gt_indent_2 { text-indent: calc(5px * 2); }
 #lzlmaeatmx .gt_indent_3 { text-indent: calc(5px * 3); }
 #lzlmaeatmx .gt_indent_4 { text-indent: calc(5px * 4); }
 #lzlmaeatmx .gt_indent_5 { text-indent: calc(5px * 5); }
 #lzlmaeatmx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lzlmaeatmx .gt_row_group_first td { border-top-width: 2px; }
 #lzlmaeatmx .gt_row_group_first th { border-top-width: 2px; }
 #lzlmaeatmx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lzlmaeatmx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lzlmaeatmx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lzlmaeatmx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lzlmaeatmx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lzlmaeatmx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lzlmaeatmx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lzlmaeatmx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lzlmaeatmx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lzlmaeatmx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lzlmaeatmx .gt_left { text-align: left; }
 #lzlmaeatmx .gt_center { text-align: center; }
 #lzlmaeatmx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lzlmaeatmx .gt_font_normal { font-weight: normal; }
 #lzlmaeatmx .gt_font_bold { font-weight: bold; }
 #lzlmaeatmx .gt_font_italic { font-style: italic; }
 #lzlmaeatmx .gt_super { font-size: 65%; }
 #lzlmaeatmx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lzlmaeatmx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lzlmaeatmx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lzlmaeatmx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lzlmaeatmx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lzlmaeatmx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
|       |         | 14.3 | 56   | 5     | 5   |


Note the two methods used above:

- [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style): uses [from_column()](../reference/from_column.md#great_tables.from_column) to set the color using the values of the `background` column.
- [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide): prevents the `background` column from being displayed in the output.


## Using **Polars** expressions

Styles can also be specified using **Polars** expressions. For example, the code below uses the `Temp` column to set color to `"lightyellow"` or `"lightblue"`.


``` python
# A Polars expression defines color based on `Temp`
temp_color = (
    pl.when(pl.col("Temp") > 70)
    .then(pl.lit("lightyellow"))
    .otherwise(pl.lit("lightblue"))
)

gt_pl_air.tab_style(
    style=style.fill(color=temp_color),
    locations=loc.body("Temp")
)
```


<style>
#ksilpuhabs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ksilpuhabs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ksilpuhabs p { margin: 0; padding: 0; }
 #ksilpuhabs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ksilpuhabs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ksilpuhabs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ksilpuhabs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ksilpuhabs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ksilpuhabs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksilpuhabs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ksilpuhabs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ksilpuhabs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ksilpuhabs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ksilpuhabs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ksilpuhabs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ksilpuhabs .gt_spanner_row { border-bottom-style: hidden; }
 #ksilpuhabs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ksilpuhabs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ksilpuhabs .gt_from_md> :first-child { margin-top: 0; }
 #ksilpuhabs .gt_from_md> :last-child { margin-bottom: 0; }
 #ksilpuhabs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ksilpuhabs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ksilpuhabs .gt_indent_1 { text-indent: 5px; }
 #ksilpuhabs .gt_indent_2 { text-indent: calc(5px * 2); }
 #ksilpuhabs .gt_indent_3 { text-indent: calc(5px * 3); }
 #ksilpuhabs .gt_indent_4 { text-indent: calc(5px * 4); }
 #ksilpuhabs .gt_indent_5 { text-indent: calc(5px * 5); }
 #ksilpuhabs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ksilpuhabs .gt_row_group_first td { border-top-width: 2px; }
 #ksilpuhabs .gt_row_group_first th { border-top-width: 2px; }
 #ksilpuhabs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ksilpuhabs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksilpuhabs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ksilpuhabs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ksilpuhabs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ksilpuhabs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ksilpuhabs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ksilpuhabs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ksilpuhabs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksilpuhabs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ksilpuhabs .gt_left { text-align: left; }
 #ksilpuhabs .gt_center { text-align: center; }
 #ksilpuhabs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ksilpuhabs .gt_font_normal { font-weight: normal; }
 #ksilpuhabs .gt_font_bold { font-weight: bold; }
 #ksilpuhabs .gt_font_italic { font-style: italic; }
 #ksilpuhabs .gt_super { font-size: 65%; }
 #ksilpuhabs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksilpuhabs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ksilpuhabs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ksilpuhabs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ksilpuhabs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ksilpuhabs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


The Polars expression evaluates per row and produces a color string for each cell. This approach avoids creating and hiding an extra column, keeping the code concise.

Each of the three approaches ([from_column()](../reference/from_column.md#great_tables.from_column) with [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide), Polars expressions, and functions) has its strengths. Polars expressions are the most concise for Polars DataFrames and keep the styling logic self-contained. The [from_column()](../reference/from_column.md#great_tables.from_column) approach works with both Pandas and Polars backends but requires an extra column. Functions are the most flexible option for Pandas workflows. Choose whichever matches your data library and preference.


## Using functions

You can also use a function, that takes the DataFrame and returns a Series with a style value for each row.

This is shown below on a pandas DataFrame.


``` python
def map_color(df):
    return (df["Temp"] > 70).map(
        {True: "lightyellow", False: "lightblue"}
    )

gt_air.tab_style(
    style=style.fill(
        color=map_color),
    locations=loc.body("Temp")
)
```


<style>
#alixgahsey table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#alixgahsey thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#alixgahsey p { margin: 0; padding: 0; }
 #alixgahsey .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #alixgahsey .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #alixgahsey .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #alixgahsey .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #alixgahsey .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #alixgahsey .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #alixgahsey .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #alixgahsey .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #alixgahsey .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #alixgahsey .gt_column_spanner_outer:first-child { padding-left: 0; }
 #alixgahsey .gt_column_spanner_outer:last-child { padding-right: 0; }
 #alixgahsey .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #alixgahsey .gt_spanner_row { border-bottom-style: hidden; }
 #alixgahsey .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #alixgahsey .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #alixgahsey .gt_from_md> :first-child { margin-top: 0; }
 #alixgahsey .gt_from_md> :last-child { margin-bottom: 0; }
 #alixgahsey .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #alixgahsey .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #alixgahsey .gt_indent_1 { text-indent: 5px; }
 #alixgahsey .gt_indent_2 { text-indent: calc(5px * 2); }
 #alixgahsey .gt_indent_3 { text-indent: calc(5px * 3); }
 #alixgahsey .gt_indent_4 { text-indent: calc(5px * 4); }
 #alixgahsey .gt_indent_5 { text-indent: calc(5px * 5); }
 #alixgahsey .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #alixgahsey .gt_row_group_first td { border-top-width: 2px; }
 #alixgahsey .gt_row_group_first th { border-top-width: 2px; }
 #alixgahsey .gt_striped { color: #333333; background-color: #F4F4F4; }
 #alixgahsey .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #alixgahsey .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #alixgahsey .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #alixgahsey .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #alixgahsey .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #alixgahsey .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #alixgahsey .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #alixgahsey .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #alixgahsey .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #alixgahsey .gt_left { text-align: left; }
 #alixgahsey .gt_center { text-align: center; }
 #alixgahsey .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #alixgahsey .gt_font_normal { font-weight: normal; }
 #alixgahsey .gt_font_bold { font-weight: bold; }
 #alixgahsey .gt_font_italic { font-style: italic; }
 #alixgahsey .gt_super { font-size: 65%; }
 #alixgahsey .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #alixgahsey .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #alixgahsey .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #alixgahsey .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #alixgahsey .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #alixgahsey .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
|       |         | 14.3 | 56   | 5     | 5   |


The function receives the full DataFrame and returns a Series of color values aligned with the rows. This pattern works well with Pandas when you want to derive styles from data logic without Polars expressions.


# Specifying columns and rows


## Using polars selectors

If you are using **Polars**, you can use column selectors and expressions for selecting specific columns and rows:


``` python
import polars.selectors as cs

gt_pl_air.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(
        columns=cs.starts_with("Te"),
        rows=pl.col("Temp") > 70
    )
)
```


<style>
#amtzxgospo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#amtzxgospo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#amtzxgospo p { margin: 0; padding: 0; }
 #amtzxgospo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #amtzxgospo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #amtzxgospo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #amtzxgospo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #amtzxgospo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #amtzxgospo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #amtzxgospo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #amtzxgospo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #amtzxgospo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #amtzxgospo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #amtzxgospo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #amtzxgospo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #amtzxgospo .gt_spanner_row { border-bottom-style: hidden; }
 #amtzxgospo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #amtzxgospo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #amtzxgospo .gt_from_md> :first-child { margin-top: 0; }
 #amtzxgospo .gt_from_md> :last-child { margin-bottom: 0; }
 #amtzxgospo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #amtzxgospo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #amtzxgospo .gt_indent_1 { text-indent: 5px; }
 #amtzxgospo .gt_indent_2 { text-indent: calc(5px * 2); }
 #amtzxgospo .gt_indent_3 { text-indent: calc(5px * 3); }
 #amtzxgospo .gt_indent_4 { text-indent: calc(5px * 4); }
 #amtzxgospo .gt_indent_5 { text-indent: calc(5px * 5); }
 #amtzxgospo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #amtzxgospo .gt_row_group_first td { border-top-width: 2px; }
 #amtzxgospo .gt_row_group_first th { border-top-width: 2px; }
 #amtzxgospo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #amtzxgospo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #amtzxgospo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #amtzxgospo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #amtzxgospo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #amtzxgospo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #amtzxgospo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #amtzxgospo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #amtzxgospo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #amtzxgospo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #amtzxgospo .gt_left { text-align: left; }
 #amtzxgospo .gt_center { text-align: center; }
 #amtzxgospo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #amtzxgospo .gt_font_normal { font-weight: normal; }
 #amtzxgospo .gt_font_bold { font-weight: bold; }
 #amtzxgospo .gt_font_italic { font-style: italic; }
 #amtzxgospo .gt_super { font-size: 65%; }
 #amtzxgospo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #amtzxgospo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #amtzxgospo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #amtzxgospo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #amtzxgospo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #amtzxgospo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


See [Column Selection](column-selection.md) for details on selecting columns.


## Using a function

For tools like **pandas**, you can use a function (or lambda) to select rows. The function should take a DataFrame, and output a boolean Series.


``` python
gt_air.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(
        columns=lambda col_name: col_name.startswith("Te"),
        rows=lambda D: D["Temp"] > 70,
    )
)
```


<style>
#hqgkeqdksg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hqgkeqdksg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hqgkeqdksg p { margin: 0; padding: 0; }
 #hqgkeqdksg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hqgkeqdksg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hqgkeqdksg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hqgkeqdksg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hqgkeqdksg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hqgkeqdksg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hqgkeqdksg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hqgkeqdksg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hqgkeqdksg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hqgkeqdksg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hqgkeqdksg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hqgkeqdksg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hqgkeqdksg .gt_spanner_row { border-bottom-style: hidden; }
 #hqgkeqdksg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hqgkeqdksg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hqgkeqdksg .gt_from_md> :first-child { margin-top: 0; }
 #hqgkeqdksg .gt_from_md> :last-child { margin-bottom: 0; }
 #hqgkeqdksg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hqgkeqdksg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hqgkeqdksg .gt_indent_1 { text-indent: 5px; }
 #hqgkeqdksg .gt_indent_2 { text-indent: calc(5px * 2); }
 #hqgkeqdksg .gt_indent_3 { text-indent: calc(5px * 3); }
 #hqgkeqdksg .gt_indent_4 { text-indent: calc(5px * 4); }
 #hqgkeqdksg .gt_indent_5 { text-indent: calc(5px * 5); }
 #hqgkeqdksg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hqgkeqdksg .gt_row_group_first td { border-top-width: 2px; }
 #hqgkeqdksg .gt_row_group_first th { border-top-width: 2px; }
 #hqgkeqdksg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hqgkeqdksg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hqgkeqdksg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hqgkeqdksg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hqgkeqdksg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hqgkeqdksg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hqgkeqdksg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hqgkeqdksg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hqgkeqdksg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hqgkeqdksg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hqgkeqdksg .gt_left { text-align: left; }
 #hqgkeqdksg .gt_center { text-align: center; }
 #hqgkeqdksg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hqgkeqdksg .gt_font_normal { font-weight: normal; }
 #hqgkeqdksg .gt_font_bold { font-weight: bold; }
 #hqgkeqdksg .gt_font_italic { font-style: italic; }
 #hqgkeqdksg .gt_super { font-size: 65%; }
 #hqgkeqdksg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hqgkeqdksg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hqgkeqdksg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hqgkeqdksg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hqgkeqdksg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hqgkeqdksg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
|       |         | 14.3 | 56   | 5     | 5   |


The function-based row selection gives you full flexibility: any callable that takes a DataFrame and returns a boolean Series can serve as a row filter.


# Multiple styles and locations

We can use a list within `style=` to apply multiple styles at once. For example, the code below sets fill and border styles on the same set of body cells.


``` python
gt_air.tab_style(
    style=[style.fill(color="yellow"), style.borders(sides="all")],
    locations=loc.body(columns="Temp", rows=[1, 2]),
)
```


<style>
#pzmhvurxca table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pzmhvurxca thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pzmhvurxca p { margin: 0; padding: 0; }
 #pzmhvurxca .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pzmhvurxca .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pzmhvurxca .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pzmhvurxca .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pzmhvurxca .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pzmhvurxca .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pzmhvurxca .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pzmhvurxca .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pzmhvurxca .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pzmhvurxca .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pzmhvurxca .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pzmhvurxca .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pzmhvurxca .gt_spanner_row { border-bottom-style: hidden; }
 #pzmhvurxca .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pzmhvurxca .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pzmhvurxca .gt_from_md> :first-child { margin-top: 0; }
 #pzmhvurxca .gt_from_md> :last-child { margin-bottom: 0; }
 #pzmhvurxca .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pzmhvurxca .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pzmhvurxca .gt_indent_1 { text-indent: 5px; }
 #pzmhvurxca .gt_indent_2 { text-indent: calc(5px * 2); }
 #pzmhvurxca .gt_indent_3 { text-indent: calc(5px * 3); }
 #pzmhvurxca .gt_indent_4 { text-indent: calc(5px * 4); }
 #pzmhvurxca .gt_indent_5 { text-indent: calc(5px * 5); }
 #pzmhvurxca .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pzmhvurxca .gt_row_group_first td { border-top-width: 2px; }
 #pzmhvurxca .gt_row_group_first th { border-top-width: 2px; }
 #pzmhvurxca .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pzmhvurxca .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pzmhvurxca .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pzmhvurxca .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pzmhvurxca .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pzmhvurxca .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pzmhvurxca .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pzmhvurxca .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pzmhvurxca .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pzmhvurxca .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pzmhvurxca .gt_left { text-align: left; }
 #pzmhvurxca .gt_center { text-align: center; }
 #pzmhvurxca .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pzmhvurxca .gt_font_normal { font-weight: normal; }
 #pzmhvurxca .gt_font_bold { font-weight: bold; }
 #pzmhvurxca .gt_font_italic { font-style: italic; }
 #pzmhvurxca .gt_super { font-size: 65%; }
 #pzmhvurxca .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pzmhvurxca .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pzmhvurxca .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pzmhvurxca .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pzmhvurxca .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pzmhvurxca .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
|       |         | 14.3 | 56   | 5     | 5   |


Note that you can also pass a list to `locations=`!


``` python
gt_air.tab_style(
    style=style.fill(color="yellow"),
    locations=[
        loc.body(columns="Temp", rows=[1, 2]),
        loc.body(columns="Ozone", rows=[0])
    ]
)
```


<style>
#eerkjyyfrn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eerkjyyfrn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eerkjyyfrn p { margin: 0; padding: 0; }
 #eerkjyyfrn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eerkjyyfrn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eerkjyyfrn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eerkjyyfrn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eerkjyyfrn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eerkjyyfrn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eerkjyyfrn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eerkjyyfrn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eerkjyyfrn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eerkjyyfrn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eerkjyyfrn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eerkjyyfrn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eerkjyyfrn .gt_spanner_row { border-bottom-style: hidden; }
 #eerkjyyfrn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eerkjyyfrn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eerkjyyfrn .gt_from_md> :first-child { margin-top: 0; }
 #eerkjyyfrn .gt_from_md> :last-child { margin-bottom: 0; }
 #eerkjyyfrn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eerkjyyfrn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eerkjyyfrn .gt_indent_1 { text-indent: 5px; }
 #eerkjyyfrn .gt_indent_2 { text-indent: calc(5px * 2); }
 #eerkjyyfrn .gt_indent_3 { text-indent: calc(5px * 3); }
 #eerkjyyfrn .gt_indent_4 { text-indent: calc(5px * 4); }
 #eerkjyyfrn .gt_indent_5 { text-indent: calc(5px * 5); }
 #eerkjyyfrn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eerkjyyfrn .gt_row_group_first td { border-top-width: 2px; }
 #eerkjyyfrn .gt_row_group_first th { border-top-width: 2px; }
 #eerkjyyfrn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eerkjyyfrn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eerkjyyfrn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eerkjyyfrn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eerkjyyfrn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eerkjyyfrn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eerkjyyfrn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eerkjyyfrn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eerkjyyfrn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eerkjyyfrn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eerkjyyfrn .gt_left { text-align: left; }
 #eerkjyyfrn .gt_center { text-align: center; }
 #eerkjyyfrn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eerkjyyfrn .gt_font_normal { font-weight: normal; }
 #eerkjyyfrn .gt_font_bold { font-weight: bold; }
 #eerkjyyfrn .gt_font_italic { font-style: italic; }
 #eerkjyyfrn .gt_super { font-size: 65%; }
 #eerkjyyfrn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eerkjyyfrn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eerkjyyfrn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eerkjyyfrn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eerkjyyfrn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eerkjyyfrn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
|       |         | 14.3 | 56   | 5     | 5   |


You can also combine **Polars** selectors with a row filtering expression, in order to select a combination of columns and rows.


``` python
import polars.selectors as cs

gt_pl_air.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(
        columns=cs.exclude(["Month", "Day"]),
        rows=pl.col("Temp") == pl.col("Temp").max()
    )
)
```


<style>
#oydtcqtnsl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oydtcqtnsl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oydtcqtnsl p { margin: 0; padding: 0; }
 #oydtcqtnsl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oydtcqtnsl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oydtcqtnsl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oydtcqtnsl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oydtcqtnsl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oydtcqtnsl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oydtcqtnsl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oydtcqtnsl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oydtcqtnsl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oydtcqtnsl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oydtcqtnsl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oydtcqtnsl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oydtcqtnsl .gt_spanner_row { border-bottom-style: hidden; }
 #oydtcqtnsl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oydtcqtnsl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oydtcqtnsl .gt_from_md> :first-child { margin-top: 0; }
 #oydtcqtnsl .gt_from_md> :last-child { margin-bottom: 0; }
 #oydtcqtnsl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oydtcqtnsl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oydtcqtnsl .gt_indent_1 { text-indent: 5px; }
 #oydtcqtnsl .gt_indent_2 { text-indent: calc(5px * 2); }
 #oydtcqtnsl .gt_indent_3 { text-indent: calc(5px * 3); }
 #oydtcqtnsl .gt_indent_4 { text-indent: calc(5px * 4); }
 #oydtcqtnsl .gt_indent_5 { text-indent: calc(5px * 5); }
 #oydtcqtnsl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oydtcqtnsl .gt_row_group_first td { border-top-width: 2px; }
 #oydtcqtnsl .gt_row_group_first th { border-top-width: 2px; }
 #oydtcqtnsl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oydtcqtnsl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oydtcqtnsl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oydtcqtnsl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oydtcqtnsl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oydtcqtnsl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oydtcqtnsl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oydtcqtnsl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oydtcqtnsl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oydtcqtnsl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oydtcqtnsl .gt_left { text-align: left; }
 #oydtcqtnsl .gt_center { text-align: center; }
 #oydtcqtnsl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oydtcqtnsl .gt_font_normal { font-weight: normal; }
 #oydtcqtnsl .gt_font_bold { font-weight: bold; }
 #oydtcqtnsl .gt_font_italic { font-style: italic; }
 #oydtcqtnsl .gt_super { font-size: 65%; }
 #oydtcqtnsl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oydtcqtnsl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oydtcqtnsl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oydtcqtnsl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oydtcqtnsl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oydtcqtnsl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


Lastly, you can use **Polars** selectors or expressions to conditionally select rows on a per-column basis.


``` python
import polars.selectors as cs

gt_pl_air.tab_style(
    style=style.fill(color="yellow"),
    locations=loc.body(mask=cs.all().eq(cs.all().max())),
)
```


<style>
#wzednfzeuw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wzednfzeuw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wzednfzeuw p { margin: 0; padding: 0; }
 #wzednfzeuw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wzednfzeuw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wzednfzeuw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wzednfzeuw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wzednfzeuw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wzednfzeuw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wzednfzeuw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wzednfzeuw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wzednfzeuw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wzednfzeuw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wzednfzeuw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wzednfzeuw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wzednfzeuw .gt_spanner_row { border-bottom-style: hidden; }
 #wzednfzeuw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wzednfzeuw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wzednfzeuw .gt_from_md> :first-child { margin-top: 0; }
 #wzednfzeuw .gt_from_md> :last-child { margin-bottom: 0; }
 #wzednfzeuw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wzednfzeuw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wzednfzeuw .gt_indent_1 { text-indent: 5px; }
 #wzednfzeuw .gt_indent_2 { text-indent: calc(5px * 2); }
 #wzednfzeuw .gt_indent_3 { text-indent: calc(5px * 3); }
 #wzednfzeuw .gt_indent_4 { text-indent: calc(5px * 4); }
 #wzednfzeuw .gt_indent_5 { text-indent: calc(5px * 5); }
 #wzednfzeuw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wzednfzeuw .gt_row_group_first td { border-top-width: 2px; }
 #wzednfzeuw .gt_row_group_first th { border-top-width: 2px; }
 #wzednfzeuw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wzednfzeuw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wzednfzeuw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wzednfzeuw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wzednfzeuw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wzednfzeuw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wzednfzeuw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wzednfzeuw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wzednfzeuw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wzednfzeuw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wzednfzeuw .gt_left { text-align: left; }
 #wzednfzeuw .gt_center { text-align: center; }
 #wzednfzeuw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wzednfzeuw .gt_font_normal { font-weight: normal; }
 #wzednfzeuw .gt_font_bold { font-weight: bold; }
 #wzednfzeuw .gt_font_italic { font-style: italic; }
 #wzednfzeuw .gt_super { font-size: 65%; }
 #wzednfzeuw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wzednfzeuw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wzednfzeuw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wzednfzeuw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wzednfzeuw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wzednfzeuw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


The `mask=` argument applies row/column logic jointly, highlighting only the cells where a column's value equals its own maximum. This is a powerful way to perform per-column conditional formatting in a single statement.


# Learning more

The combination of [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style), location specifiers, and the various style functions gives you precise control over the visual presentation of your table body. Whether you are highlighting outliers, applying conditional formatting, or using column-driven styles, these tools let you communicate data insights through visual cues that complement the numeric values themselves.

For further reference, consult the API documentation:

- API Docs:
  - [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style)
  - [`style.*` and `loc.*` functions](../reference/index.md#location-targeting-and-styling-classes)
  - [from_column()](../reference/from_column.md#great_tables.from_column)
