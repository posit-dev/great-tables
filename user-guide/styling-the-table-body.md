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
#kxxqvcbxax table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kxxqvcbxax thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kxxqvcbxax p { margin: 0; padding: 0; }
 #kxxqvcbxax .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kxxqvcbxax .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kxxqvcbxax .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kxxqvcbxax .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kxxqvcbxax .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kxxqvcbxax .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kxxqvcbxax .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kxxqvcbxax .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kxxqvcbxax .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kxxqvcbxax .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kxxqvcbxax .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kxxqvcbxax .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kxxqvcbxax .gt_spanner_row { border-bottom-style: hidden; }
 #kxxqvcbxax .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kxxqvcbxax .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kxxqvcbxax .gt_from_md> :first-child { margin-top: 0; }
 #kxxqvcbxax .gt_from_md> :last-child { margin-bottom: 0; }
 #kxxqvcbxax .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kxxqvcbxax .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kxxqvcbxax .gt_indent_1 { text-indent: 5px; }
 #kxxqvcbxax .gt_indent_2 { text-indent: calc(5px * 2); }
 #kxxqvcbxax .gt_indent_3 { text-indent: calc(5px * 3); }
 #kxxqvcbxax .gt_indent_4 { text-indent: calc(5px * 4); }
 #kxxqvcbxax .gt_indent_5 { text-indent: calc(5px * 5); }
 #kxxqvcbxax .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kxxqvcbxax .gt_row_group_first td { border-top-width: 2px; }
 #kxxqvcbxax .gt_row_group_first th { border-top-width: 2px; }
 #kxxqvcbxax .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kxxqvcbxax .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kxxqvcbxax .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kxxqvcbxax .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kxxqvcbxax .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kxxqvcbxax .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kxxqvcbxax .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kxxqvcbxax .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kxxqvcbxax .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kxxqvcbxax .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kxxqvcbxax .gt_left { text-align: left; }
 #kxxqvcbxax .gt_center { text-align: center; }
 #kxxqvcbxax .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kxxqvcbxax .gt_font_normal { font-weight: normal; }
 #kxxqvcbxax .gt_font_bold { font-weight: bold; }
 #kxxqvcbxax .gt_font_italic { font-style: italic; }
 #kxxqvcbxax .gt_super { font-size: 65%; }
 #kxxqvcbxax .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kxxqvcbxax .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kxxqvcbxax .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kxxqvcbxax .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kxxqvcbxax .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kxxqvcbxax .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


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
#xcndxpjuqu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xcndxpjuqu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xcndxpjuqu p { margin: 0; padding: 0; }
 #xcndxpjuqu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xcndxpjuqu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xcndxpjuqu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xcndxpjuqu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xcndxpjuqu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xcndxpjuqu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xcndxpjuqu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xcndxpjuqu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xcndxpjuqu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xcndxpjuqu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xcndxpjuqu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xcndxpjuqu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xcndxpjuqu .gt_spanner_row { border-bottom-style: hidden; }
 #xcndxpjuqu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xcndxpjuqu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xcndxpjuqu .gt_from_md> :first-child { margin-top: 0; }
 #xcndxpjuqu .gt_from_md> :last-child { margin-bottom: 0; }
 #xcndxpjuqu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xcndxpjuqu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xcndxpjuqu .gt_indent_1 { text-indent: 5px; }
 #xcndxpjuqu .gt_indent_2 { text-indent: calc(5px * 2); }
 #xcndxpjuqu .gt_indent_3 { text-indent: calc(5px * 3); }
 #xcndxpjuqu .gt_indent_4 { text-indent: calc(5px * 4); }
 #xcndxpjuqu .gt_indent_5 { text-indent: calc(5px * 5); }
 #xcndxpjuqu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xcndxpjuqu .gt_row_group_first td { border-top-width: 2px; }
 #xcndxpjuqu .gt_row_group_first th { border-top-width: 2px; }
 #xcndxpjuqu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xcndxpjuqu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xcndxpjuqu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xcndxpjuqu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xcndxpjuqu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xcndxpjuqu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xcndxpjuqu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xcndxpjuqu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xcndxpjuqu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xcndxpjuqu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xcndxpjuqu .gt_left { text-align: left; }
 #xcndxpjuqu .gt_center { text-align: center; }
 #xcndxpjuqu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xcndxpjuqu .gt_font_normal { font-weight: normal; }
 #xcndxpjuqu .gt_font_bold { font-weight: bold; }
 #xcndxpjuqu .gt_font_italic { font-style: italic; }
 #xcndxpjuqu .gt_super { font-size: 65%; }
 #xcndxpjuqu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xcndxpjuqu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xcndxpjuqu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xcndxpjuqu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xcndxpjuqu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xcndxpjuqu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


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
#oqgojkazlw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oqgojkazlw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oqgojkazlw p { margin: 0; padding: 0; }
 #oqgojkazlw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oqgojkazlw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oqgojkazlw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oqgojkazlw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oqgojkazlw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oqgojkazlw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oqgojkazlw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oqgojkazlw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oqgojkazlw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oqgojkazlw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oqgojkazlw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oqgojkazlw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oqgojkazlw .gt_spanner_row { border-bottom-style: hidden; }
 #oqgojkazlw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oqgojkazlw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oqgojkazlw .gt_from_md> :first-child { margin-top: 0; }
 #oqgojkazlw .gt_from_md> :last-child { margin-bottom: 0; }
 #oqgojkazlw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oqgojkazlw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oqgojkazlw .gt_indent_1 { text-indent: 5px; }
 #oqgojkazlw .gt_indent_2 { text-indent: calc(5px * 2); }
 #oqgojkazlw .gt_indent_3 { text-indent: calc(5px * 3); }
 #oqgojkazlw .gt_indent_4 { text-indent: calc(5px * 4); }
 #oqgojkazlw .gt_indent_5 { text-indent: calc(5px * 5); }
 #oqgojkazlw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oqgojkazlw .gt_row_group_first td { border-top-width: 2px; }
 #oqgojkazlw .gt_row_group_first th { border-top-width: 2px; }
 #oqgojkazlw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oqgojkazlw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oqgojkazlw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oqgojkazlw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oqgojkazlw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oqgojkazlw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oqgojkazlw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oqgojkazlw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oqgojkazlw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oqgojkazlw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oqgojkazlw .gt_left { text-align: left; }
 #oqgojkazlw .gt_center { text-align: center; }
 #oqgojkazlw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oqgojkazlw .gt_font_normal { font-weight: normal; }
 #oqgojkazlw .gt_font_bold { font-weight: bold; }
 #oqgojkazlw .gt_font_italic { font-style: italic; }
 #oqgojkazlw .gt_super { font-size: 65%; }
 #oqgojkazlw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oqgojkazlw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oqgojkazlw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oqgojkazlw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oqgojkazlw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oqgojkazlw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


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
#pplukgkguc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pplukgkguc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pplukgkguc p { margin: 0; padding: 0; }
 #pplukgkguc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pplukgkguc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pplukgkguc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pplukgkguc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pplukgkguc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pplukgkguc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pplukgkguc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pplukgkguc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pplukgkguc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pplukgkguc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pplukgkguc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pplukgkguc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pplukgkguc .gt_spanner_row { border-bottom-style: hidden; }
 #pplukgkguc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pplukgkguc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pplukgkguc .gt_from_md> :first-child { margin-top: 0; }
 #pplukgkguc .gt_from_md> :last-child { margin-bottom: 0; }
 #pplukgkguc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pplukgkguc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pplukgkguc .gt_indent_1 { text-indent: 5px; }
 #pplukgkguc .gt_indent_2 { text-indent: calc(5px * 2); }
 #pplukgkguc .gt_indent_3 { text-indent: calc(5px * 3); }
 #pplukgkguc .gt_indent_4 { text-indent: calc(5px * 4); }
 #pplukgkguc .gt_indent_5 { text-indent: calc(5px * 5); }
 #pplukgkguc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pplukgkguc .gt_row_group_first td { border-top-width: 2px; }
 #pplukgkguc .gt_row_group_first th { border-top-width: 2px; }
 #pplukgkguc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pplukgkguc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pplukgkguc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pplukgkguc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pplukgkguc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pplukgkguc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pplukgkguc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pplukgkguc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pplukgkguc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pplukgkguc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pplukgkguc .gt_left { text-align: left; }
 #pplukgkguc .gt_center { text-align: center; }
 #pplukgkguc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pplukgkguc .gt_font_normal { font-weight: normal; }
 #pplukgkguc .gt_font_bold { font-weight: bold; }
 #pplukgkguc .gt_font_italic { font-style: italic; }
 #pplukgkguc .gt_super { font-size: 65%; }
 #pplukgkguc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pplukgkguc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pplukgkguc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pplukgkguc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pplukgkguc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pplukgkguc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#knteajeyta table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#knteajeyta thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#knteajeyta p { margin: 0; padding: 0; }
 #knteajeyta .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #knteajeyta .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #knteajeyta .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #knteajeyta .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #knteajeyta .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #knteajeyta .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #knteajeyta .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #knteajeyta .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #knteajeyta .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #knteajeyta .gt_column_spanner_outer:first-child { padding-left: 0; }
 #knteajeyta .gt_column_spanner_outer:last-child { padding-right: 0; }
 #knteajeyta .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #knteajeyta .gt_spanner_row { border-bottom-style: hidden; }
 #knteajeyta .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #knteajeyta .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #knteajeyta .gt_from_md> :first-child { margin-top: 0; }
 #knteajeyta .gt_from_md> :last-child { margin-bottom: 0; }
 #knteajeyta .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #knteajeyta .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #knteajeyta .gt_indent_1 { text-indent: 5px; }
 #knteajeyta .gt_indent_2 { text-indent: calc(5px * 2); }
 #knteajeyta .gt_indent_3 { text-indent: calc(5px * 3); }
 #knteajeyta .gt_indent_4 { text-indent: calc(5px * 4); }
 #knteajeyta .gt_indent_5 { text-indent: calc(5px * 5); }
 #knteajeyta .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #knteajeyta .gt_row_group_first td { border-top-width: 2px; }
 #knteajeyta .gt_row_group_first th { border-top-width: 2px; }
 #knteajeyta .gt_striped { color: #333333; background-color: #F4F4F4; }
 #knteajeyta .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #knteajeyta .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #knteajeyta .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #knteajeyta .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #knteajeyta .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #knteajeyta .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #knteajeyta .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #knteajeyta .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #knteajeyta .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #knteajeyta .gt_left { text-align: left; }
 #knteajeyta .gt_center { text-align: center; }
 #knteajeyta .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #knteajeyta .gt_font_normal { font-weight: normal; }
 #knteajeyta .gt_font_bold { font-weight: bold; }
 #knteajeyta .gt_font_italic { font-style: italic; }
 #knteajeyta .gt_super { font-size: 65%; }
 #knteajeyta .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #knteajeyta .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #knteajeyta .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #knteajeyta .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #knteajeyta .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #knteajeyta .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


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
#jigluhmndq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jigluhmndq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jigluhmndq p { margin: 0; padding: 0; }
 #jigluhmndq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jigluhmndq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jigluhmndq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jigluhmndq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jigluhmndq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jigluhmndq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jigluhmndq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jigluhmndq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jigluhmndq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jigluhmndq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jigluhmndq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jigluhmndq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jigluhmndq .gt_spanner_row { border-bottom-style: hidden; }
 #jigluhmndq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jigluhmndq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jigluhmndq .gt_from_md> :first-child { margin-top: 0; }
 #jigluhmndq .gt_from_md> :last-child { margin-bottom: 0; }
 #jigluhmndq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jigluhmndq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jigluhmndq .gt_indent_1 { text-indent: 5px; }
 #jigluhmndq .gt_indent_2 { text-indent: calc(5px * 2); }
 #jigluhmndq .gt_indent_3 { text-indent: calc(5px * 3); }
 #jigluhmndq .gt_indent_4 { text-indent: calc(5px * 4); }
 #jigluhmndq .gt_indent_5 { text-indent: calc(5px * 5); }
 #jigluhmndq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jigluhmndq .gt_row_group_first td { border-top-width: 2px; }
 #jigluhmndq .gt_row_group_first th { border-top-width: 2px; }
 #jigluhmndq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jigluhmndq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jigluhmndq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jigluhmndq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jigluhmndq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jigluhmndq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jigluhmndq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jigluhmndq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jigluhmndq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jigluhmndq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jigluhmndq .gt_left { text-align: left; }
 #jigluhmndq .gt_center { text-align: center; }
 #jigluhmndq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jigluhmndq .gt_font_normal { font-weight: normal; }
 #jigluhmndq .gt_font_bold { font-weight: bold; }
 #jigluhmndq .gt_font_italic { font-style: italic; }
 #jigluhmndq .gt_super { font-size: 65%; }
 #jigluhmndq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jigluhmndq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jigluhmndq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jigluhmndq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jigluhmndq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jigluhmndq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dkioargopm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dkioargopm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dkioargopm p { margin: 0; padding: 0; }
 #dkioargopm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dkioargopm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dkioargopm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dkioargopm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dkioargopm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dkioargopm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dkioargopm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dkioargopm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dkioargopm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dkioargopm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dkioargopm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dkioargopm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dkioargopm .gt_spanner_row { border-bottom-style: hidden; }
 #dkioargopm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dkioargopm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dkioargopm .gt_from_md> :first-child { margin-top: 0; }
 #dkioargopm .gt_from_md> :last-child { margin-bottom: 0; }
 #dkioargopm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dkioargopm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dkioargopm .gt_indent_1 { text-indent: 5px; }
 #dkioargopm .gt_indent_2 { text-indent: calc(5px * 2); }
 #dkioargopm .gt_indent_3 { text-indent: calc(5px * 3); }
 #dkioargopm .gt_indent_4 { text-indent: calc(5px * 4); }
 #dkioargopm .gt_indent_5 { text-indent: calc(5px * 5); }
 #dkioargopm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dkioargopm .gt_row_group_first td { border-top-width: 2px; }
 #dkioargopm .gt_row_group_first th { border-top-width: 2px; }
 #dkioargopm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dkioargopm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dkioargopm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dkioargopm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dkioargopm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dkioargopm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dkioargopm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dkioargopm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dkioargopm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dkioargopm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dkioargopm .gt_left { text-align: left; }
 #dkioargopm .gt_center { text-align: center; }
 #dkioargopm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dkioargopm .gt_font_normal { font-weight: normal; }
 #dkioargopm .gt_font_bold { font-weight: bold; }
 #dkioargopm .gt_font_italic { font-style: italic; }
 #dkioargopm .gt_super { font-size: 65%; }
 #dkioargopm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dkioargopm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dkioargopm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dkioargopm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dkioargopm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dkioargopm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


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
#bcwfzqkiju table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bcwfzqkiju thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bcwfzqkiju p { margin: 0; padding: 0; }
 #bcwfzqkiju .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bcwfzqkiju .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bcwfzqkiju .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bcwfzqkiju .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bcwfzqkiju .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bcwfzqkiju .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bcwfzqkiju .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bcwfzqkiju .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bcwfzqkiju .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bcwfzqkiju .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bcwfzqkiju .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bcwfzqkiju .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bcwfzqkiju .gt_spanner_row { border-bottom-style: hidden; }
 #bcwfzqkiju .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bcwfzqkiju .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bcwfzqkiju .gt_from_md> :first-child { margin-top: 0; }
 #bcwfzqkiju .gt_from_md> :last-child { margin-bottom: 0; }
 #bcwfzqkiju .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bcwfzqkiju .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bcwfzqkiju .gt_indent_1 { text-indent: 5px; }
 #bcwfzqkiju .gt_indent_2 { text-indent: calc(5px * 2); }
 #bcwfzqkiju .gt_indent_3 { text-indent: calc(5px * 3); }
 #bcwfzqkiju .gt_indent_4 { text-indent: calc(5px * 4); }
 #bcwfzqkiju .gt_indent_5 { text-indent: calc(5px * 5); }
 #bcwfzqkiju .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bcwfzqkiju .gt_row_group_first td { border-top-width: 2px; }
 #bcwfzqkiju .gt_row_group_first th { border-top-width: 2px; }
 #bcwfzqkiju .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bcwfzqkiju .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bcwfzqkiju .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bcwfzqkiju .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bcwfzqkiju .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bcwfzqkiju .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bcwfzqkiju .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bcwfzqkiju .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bcwfzqkiju .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bcwfzqkiju .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bcwfzqkiju .gt_left { text-align: left; }
 #bcwfzqkiju .gt_center { text-align: center; }
 #bcwfzqkiju .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bcwfzqkiju .gt_font_normal { font-weight: normal; }
 #bcwfzqkiju .gt_font_bold { font-weight: bold; }
 #bcwfzqkiju .gt_font_italic { font-style: italic; }
 #bcwfzqkiju .gt_super { font-size: 65%; }
 #bcwfzqkiju .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bcwfzqkiju .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bcwfzqkiju .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bcwfzqkiju .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bcwfzqkiju .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bcwfzqkiju .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#viuliudppf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#viuliudppf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#viuliudppf p { margin: 0; padding: 0; }
 #viuliudppf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #viuliudppf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #viuliudppf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #viuliudppf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #viuliudppf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #viuliudppf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #viuliudppf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #viuliudppf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #viuliudppf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #viuliudppf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #viuliudppf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #viuliudppf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #viuliudppf .gt_spanner_row { border-bottom-style: hidden; }
 #viuliudppf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #viuliudppf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #viuliudppf .gt_from_md> :first-child { margin-top: 0; }
 #viuliudppf .gt_from_md> :last-child { margin-bottom: 0; }
 #viuliudppf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #viuliudppf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #viuliudppf .gt_indent_1 { text-indent: 5px; }
 #viuliudppf .gt_indent_2 { text-indent: calc(5px * 2); }
 #viuliudppf .gt_indent_3 { text-indent: calc(5px * 3); }
 #viuliudppf .gt_indent_4 { text-indent: calc(5px * 4); }
 #viuliudppf .gt_indent_5 { text-indent: calc(5px * 5); }
 #viuliudppf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #viuliudppf .gt_row_group_first td { border-top-width: 2px; }
 #viuliudppf .gt_row_group_first th { border-top-width: 2px; }
 #viuliudppf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #viuliudppf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #viuliudppf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #viuliudppf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #viuliudppf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #viuliudppf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #viuliudppf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #viuliudppf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #viuliudppf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #viuliudppf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #viuliudppf .gt_left { text-align: left; }
 #viuliudppf .gt_center { text-align: center; }
 #viuliudppf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #viuliudppf .gt_font_normal { font-weight: normal; }
 #viuliudppf .gt_font_bold { font-weight: bold; }
 #viuliudppf .gt_font_italic { font-style: italic; }
 #viuliudppf .gt_super { font-size: 65%; }
 #viuliudppf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #viuliudppf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #viuliudppf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #viuliudppf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #viuliudppf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #viuliudppf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


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
#iishkpciky table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iishkpciky thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iishkpciky p { margin: 0; padding: 0; }
 #iishkpciky .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iishkpciky .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iishkpciky .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iishkpciky .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iishkpciky .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iishkpciky .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iishkpciky .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iishkpciky .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iishkpciky .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iishkpciky .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iishkpciky .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iishkpciky .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iishkpciky .gt_spanner_row { border-bottom-style: hidden; }
 #iishkpciky .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iishkpciky .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iishkpciky .gt_from_md> :first-child { margin-top: 0; }
 #iishkpciky .gt_from_md> :last-child { margin-bottom: 0; }
 #iishkpciky .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iishkpciky .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iishkpciky .gt_indent_1 { text-indent: 5px; }
 #iishkpciky .gt_indent_2 { text-indent: calc(5px * 2); }
 #iishkpciky .gt_indent_3 { text-indent: calc(5px * 3); }
 #iishkpciky .gt_indent_4 { text-indent: calc(5px * 4); }
 #iishkpciky .gt_indent_5 { text-indent: calc(5px * 5); }
 #iishkpciky .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iishkpciky .gt_row_group_first td { border-top-width: 2px; }
 #iishkpciky .gt_row_group_first th { border-top-width: 2px; }
 #iishkpciky .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iishkpciky .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iishkpciky .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iishkpciky .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iishkpciky .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iishkpciky .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iishkpciky .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iishkpciky .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iishkpciky .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iishkpciky .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iishkpciky .gt_left { text-align: left; }
 #iishkpciky .gt_center { text-align: center; }
 #iishkpciky .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iishkpciky .gt_font_normal { font-weight: normal; }
 #iishkpciky .gt_font_bold { font-weight: bold; }
 #iishkpciky .gt_font_italic { font-style: italic; }
 #iishkpciky .gt_super { font-size: 65%; }
 #iishkpciky .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iishkpciky .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iishkpciky .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iishkpciky .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iishkpciky .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iishkpciky .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


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
#jlaejdpwzm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jlaejdpwzm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jlaejdpwzm p { margin: 0; padding: 0; }
 #jlaejdpwzm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jlaejdpwzm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jlaejdpwzm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jlaejdpwzm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jlaejdpwzm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jlaejdpwzm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jlaejdpwzm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jlaejdpwzm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jlaejdpwzm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jlaejdpwzm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jlaejdpwzm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jlaejdpwzm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jlaejdpwzm .gt_spanner_row { border-bottom-style: hidden; }
 #jlaejdpwzm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jlaejdpwzm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jlaejdpwzm .gt_from_md> :first-child { margin-top: 0; }
 #jlaejdpwzm .gt_from_md> :last-child { margin-bottom: 0; }
 #jlaejdpwzm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jlaejdpwzm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jlaejdpwzm .gt_indent_1 { text-indent: 5px; }
 #jlaejdpwzm .gt_indent_2 { text-indent: calc(5px * 2); }
 #jlaejdpwzm .gt_indent_3 { text-indent: calc(5px * 3); }
 #jlaejdpwzm .gt_indent_4 { text-indent: calc(5px * 4); }
 #jlaejdpwzm .gt_indent_5 { text-indent: calc(5px * 5); }
 #jlaejdpwzm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jlaejdpwzm .gt_row_group_first td { border-top-width: 2px; }
 #jlaejdpwzm .gt_row_group_first th { border-top-width: 2px; }
 #jlaejdpwzm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jlaejdpwzm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jlaejdpwzm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jlaejdpwzm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jlaejdpwzm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jlaejdpwzm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jlaejdpwzm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jlaejdpwzm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jlaejdpwzm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jlaejdpwzm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jlaejdpwzm .gt_left { text-align: left; }
 #jlaejdpwzm .gt_center { text-align: center; }
 #jlaejdpwzm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jlaejdpwzm .gt_font_normal { font-weight: normal; }
 #jlaejdpwzm .gt_font_bold { font-weight: bold; }
 #jlaejdpwzm .gt_font_italic { font-style: italic; }
 #jlaejdpwzm .gt_super { font-size: 65%; }
 #jlaejdpwzm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jlaejdpwzm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jlaejdpwzm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jlaejdpwzm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jlaejdpwzm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jlaejdpwzm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Ozone | Solar_R | Wind | Temp | Month | Day |
|-------|---------|------|------|-------|-----|
| 41.0  | 190.0   | 7.4  | 67   | 5     | 1   |
| 36.0  | 118.0   | 8.0  | 72   | 5     | 2   |
| 12.0  | 149.0   | 12.6 | 74   | 5     | 3   |
| 18.0  | 313.0   | 11.5 | 62   | 5     | 4   |
| None  | None    | 14.3 | 56   | 5     | 5   |


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
#qvkszuhscr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qvkszuhscr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qvkszuhscr p { margin: 0; padding: 0; }
 #qvkszuhscr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qvkszuhscr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qvkszuhscr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qvkszuhscr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qvkszuhscr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qvkszuhscr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvkszuhscr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qvkszuhscr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qvkszuhscr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qvkszuhscr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qvkszuhscr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qvkszuhscr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qvkszuhscr .gt_spanner_row { border-bottom-style: hidden; }
 #qvkszuhscr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qvkszuhscr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qvkszuhscr .gt_from_md> :first-child { margin-top: 0; }
 #qvkszuhscr .gt_from_md> :last-child { margin-bottom: 0; }
 #qvkszuhscr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qvkszuhscr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qvkszuhscr .gt_indent_1 { text-indent: 5px; }
 #qvkszuhscr .gt_indent_2 { text-indent: calc(5px * 2); }
 #qvkszuhscr .gt_indent_3 { text-indent: calc(5px * 3); }
 #qvkszuhscr .gt_indent_4 { text-indent: calc(5px * 4); }
 #qvkszuhscr .gt_indent_5 { text-indent: calc(5px * 5); }
 #qvkszuhscr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qvkszuhscr .gt_row_group_first td { border-top-width: 2px; }
 #qvkszuhscr .gt_row_group_first th { border-top-width: 2px; }
 #qvkszuhscr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qvkszuhscr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvkszuhscr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qvkszuhscr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qvkszuhscr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvkszuhscr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qvkszuhscr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qvkszuhscr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qvkszuhscr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvkszuhscr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qvkszuhscr .gt_left { text-align: left; }
 #qvkszuhscr .gt_center { text-align: center; }
 #qvkszuhscr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qvkszuhscr .gt_font_normal { font-weight: normal; }
 #qvkszuhscr .gt_font_bold { font-weight: bold; }
 #qvkszuhscr .gt_font_italic { font-style: italic; }
 #qvkszuhscr .gt_super { font-size: 65%; }
 #qvkszuhscr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvkszuhscr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qvkszuhscr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvkszuhscr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qvkszuhscr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qvkszuhscr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rncstzdkad table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rncstzdkad thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rncstzdkad p { margin: 0; padding: 0; }
 #rncstzdkad .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rncstzdkad .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rncstzdkad .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rncstzdkad .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rncstzdkad .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rncstzdkad .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rncstzdkad .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rncstzdkad .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rncstzdkad .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rncstzdkad .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rncstzdkad .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rncstzdkad .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rncstzdkad .gt_spanner_row { border-bottom-style: hidden; }
 #rncstzdkad .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rncstzdkad .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rncstzdkad .gt_from_md> :first-child { margin-top: 0; }
 #rncstzdkad .gt_from_md> :last-child { margin-bottom: 0; }
 #rncstzdkad .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rncstzdkad .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rncstzdkad .gt_indent_1 { text-indent: 5px; }
 #rncstzdkad .gt_indent_2 { text-indent: calc(5px * 2); }
 #rncstzdkad .gt_indent_3 { text-indent: calc(5px * 3); }
 #rncstzdkad .gt_indent_4 { text-indent: calc(5px * 4); }
 #rncstzdkad .gt_indent_5 { text-indent: calc(5px * 5); }
 #rncstzdkad .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rncstzdkad .gt_row_group_first td { border-top-width: 2px; }
 #rncstzdkad .gt_row_group_first th { border-top-width: 2px; }
 #rncstzdkad .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rncstzdkad .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rncstzdkad .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rncstzdkad .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rncstzdkad .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rncstzdkad .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rncstzdkad .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rncstzdkad .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rncstzdkad .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rncstzdkad .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rncstzdkad .gt_left { text-align: left; }
 #rncstzdkad .gt_center { text-align: center; }
 #rncstzdkad .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rncstzdkad .gt_font_normal { font-weight: normal; }
 #rncstzdkad .gt_font_bold { font-weight: bold; }
 #rncstzdkad .gt_font_italic { font-style: italic; }
 #rncstzdkad .gt_super { font-size: 65%; }
 #rncstzdkad .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rncstzdkad .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rncstzdkad .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rncstzdkad .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rncstzdkad .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rncstzdkad .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
