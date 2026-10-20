# Introduction

The **Great Tables** package is all about making it simple to produce nice-looking display tables. Display tables? Well yes, we are trying to distinguish between data tables (i.e., DataFrames) and those tables you'd find in a web page, a journal article, or in a magazine. Such tables can likewise be called presentation tables, summary tables, or just tables really. Here are some examples, ripped straight from the web:

<img src="../assets/tables_from_the_web.png" class="img-fluid" />

Display tables exist because raw DataFrames are working artifacts, not communication tools. When you share findings with colleagues, stakeholders, or readers, the formatting of your table directly affects how well your message lands. Good structure and styling reduce cognitive load, draw attention to what matters, and help your audience reach the right conclusions faster. A well-built table is an act of respect for your reader's time.

We can think of display tables as output only, where we'd not want to use them as input ever again. Other features include annotations, table element styling, and text transformations that serve to communicate the subject matter more clearly.


# Let's Install

The installation really couldn't be much easier. Use this:

``` bash
pip install great_tables
```

Once installed, you are ready to build your first table.


# A Basic Table using **Great Tables**

> **Note: Note**
>
> The example below requires the Pandas library to be installed. But Pandas is not required to use Great Tables. You can also use a Polars DataFrame.

Let's use a subset of the [countrypops](../reference/data.countrypops.md#great_tables.data.countrypops) dataset available within `great_tables.data`, keeping the ten most populous countries in 2022:


``` python
from great_tables import GT, md, html
from great_tables.data import countrypops

countries_mini = (
    countrypops[countrypops["year"] == 2022]
    .sort_values("population", ascending=False)
    .head(10)[["country_name", "population"]]
)
```


The `countries_mini` data is a simple **Pandas** DataFrame with 2 columns and that'll serve as a great start. Speaking of which, the main entry point into the **Great Tables** API is the [GT](../reference/GT.md#great_tables.GT) class. Let's use that to make a presentable table:


``` python
# Create a display table showing the ten most populous countries
gt_tbl = GT(countries_mini)

# Show the output table
gt_tbl
```


<style>
#icgonxsgji table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#icgonxsgji thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#icgonxsgji p { margin: 0; padding: 0; }
 #icgonxsgji .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #icgonxsgji .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #icgonxsgji .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #icgonxsgji .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #icgonxsgji .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #icgonxsgji .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #icgonxsgji .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #icgonxsgji .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #icgonxsgji .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #icgonxsgji .gt_column_spanner_outer:first-child { padding-left: 0; }
 #icgonxsgji .gt_column_spanner_outer:last-child { padding-right: 0; }
 #icgonxsgji .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #icgonxsgji .gt_spanner_row { border-bottom-style: hidden; }
 #icgonxsgji .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #icgonxsgji .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #icgonxsgji .gt_from_md> :first-child { margin-top: 0; }
 #icgonxsgji .gt_from_md> :last-child { margin-bottom: 0; }
 #icgonxsgji .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #icgonxsgji .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #icgonxsgji .gt_indent_1 { text-indent: 5px; }
 #icgonxsgji .gt_indent_2 { text-indent: calc(5px * 2); }
 #icgonxsgji .gt_indent_3 { text-indent: calc(5px * 3); }
 #icgonxsgji .gt_indent_4 { text-indent: calc(5px * 4); }
 #icgonxsgji .gt_indent_5 { text-indent: calc(5px * 5); }
 #icgonxsgji .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #icgonxsgji .gt_row_group_first td { border-top-width: 2px; }
 #icgonxsgji .gt_row_group_first th { border-top-width: 2px; }
 #icgonxsgji .gt_striped { color: #333333; background-color: #F4F4F4; }
 #icgonxsgji .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #icgonxsgji .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #icgonxsgji .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #icgonxsgji .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #icgonxsgji .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #icgonxsgji .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #icgonxsgji .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #icgonxsgji .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #icgonxsgji .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #icgonxsgji .gt_left { text-align: left; }
 #icgonxsgji .gt_center { text-align: center; }
 #icgonxsgji .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #icgonxsgji .gt_font_normal { font-weight: normal; }
 #icgonxsgji .gt_font_bold { font-weight: bold; }
 #icgonxsgji .gt_font_italic { font-style: italic; }
 #icgonxsgji .gt_super { font-size: 65%; }
 #icgonxsgji .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #icgonxsgji .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #icgonxsgji .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #icgonxsgji .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #icgonxsgji .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #icgonxsgji .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| country_name       | population |
|--------------------|------------|
| India              | 1417173173 |
| China              | 1412175000 |
| United States      | 333287557  |
| Indonesia          | 275501339  |
| Pakistan           | 235824862  |
| Nigeria            | 218541212  |
| Brazil             | 215313498  |
| Bangladesh         | 171186372  |
| Russian Federation | 143555736  |
| Mexico             | 127504125  |


That doesn't look too bad! Sure, it's basic but we really didn't really ask for much. We did receive a proper table with column labels and the data. Even this minimal output is an improvement over a raw DataFrame: you get proper HTML rendering, consistent spacing, and a clean visual structure that works in notebooks, reports, and web pages alike. But the real power of Great Tables comes from layering on the structural components described next.

Oftentimes however, you'll want a bit more: a **Table header**, a **Stub**, and sometimes *source notes* in the **Table Footer** component.

> **Note: Note**
>
> Typically we use Great Tables in an notebook environment or within a Quarto document. Tables won't print to the console, but using the [show()](../reference/GT.show.md#great_tables.GT.show) method on a table object while in the console will open the HTML table in your default browser.


# **Polars** DataFrame support

[GT](../reference/GT.md#great_tables.GT) accepts both **Pandas** and **Polars** DataFrames. You can pass a **Polars** DataFrame to [GT](../reference/GT.md#great_tables.GT), or use its `DataFrame.style` property. Supporting both backends matters because teams often have mixed workflows, and you shouldn't have to rewrite your table code just because a project uses a different DataFrame library.


``` python
import polars as pl

df_polars = pl.from_pandas(countries_mini)

# Approach 1: call GT ----
GT(df_polars)

# Approach 2: Polars style property ----
df_polars.style
```


<style>
#punzalnwri table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#punzalnwri thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#punzalnwri p { margin: 0; padding: 0; }
 #punzalnwri .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #punzalnwri .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #punzalnwri .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #punzalnwri .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #punzalnwri .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #punzalnwri .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #punzalnwri .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #punzalnwri .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #punzalnwri .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #punzalnwri .gt_column_spanner_outer:first-child { padding-left: 0; }
 #punzalnwri .gt_column_spanner_outer:last-child { padding-right: 0; }
 #punzalnwri .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #punzalnwri .gt_spanner_row { border-bottom-style: hidden; }
 #punzalnwri .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #punzalnwri .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #punzalnwri .gt_from_md> :first-child { margin-top: 0; }
 #punzalnwri .gt_from_md> :last-child { margin-bottom: 0; }
 #punzalnwri .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #punzalnwri .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #punzalnwri .gt_indent_1 { text-indent: 5px; }
 #punzalnwri .gt_indent_2 { text-indent: calc(5px * 2); }
 #punzalnwri .gt_indent_3 { text-indent: calc(5px * 3); }
 #punzalnwri .gt_indent_4 { text-indent: calc(5px * 4); }
 #punzalnwri .gt_indent_5 { text-indent: calc(5px * 5); }
 #punzalnwri .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #punzalnwri .gt_row_group_first td { border-top-width: 2px; }
 #punzalnwri .gt_row_group_first th { border-top-width: 2px; }
 #punzalnwri .gt_striped { color: #333333; background-color: #F4F4F4; }
 #punzalnwri .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #punzalnwri .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #punzalnwri .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #punzalnwri .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #punzalnwri .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #punzalnwri .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #punzalnwri .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #punzalnwri .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #punzalnwri .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #punzalnwri .gt_left { text-align: left; }
 #punzalnwri .gt_center { text-align: center; }
 #punzalnwri .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #punzalnwri .gt_font_normal { font-weight: normal; }
 #punzalnwri .gt_font_bold { font-weight: bold; }
 #punzalnwri .gt_font_italic { font-style: italic; }
 #punzalnwri .gt_super { font-size: 65%; }
 #punzalnwri .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #punzalnwri .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #punzalnwri .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #punzalnwri .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #punzalnwri .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #punzalnwri .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| country_name       | population |
|--------------------|------------|
| India              | 1417173173 |
| China              | 1412175000 |
| United States      | 333287557  |
| Indonesia          | 275501339  |
| Pakistan           | 235824862  |
| Nigeria            | 218541212  |
| Brazil             | 215313498  |
| Bangladesh         | 171186372  |
| Russian Federation | 143555736  |
| Mexico             | 127504125  |


> **Note: Note**
>
> The `polars.DataFrame.style` property is currently considered [unstable](https://docs.pola.rs/api/python/stable/reference/dataframe/style.html#polars.DataFrame.style), and may change in the future. Using [GT](../reference/GT.md#great_tables.GT) on a **Polars** DataFrame will always work.


# Some Beautiful Examples

In the following pages we'll use **Great Tables** to turn DataFrames into beautiful tables, like the ones below.


Show the Code

``` python
from great_tables import GT, md, html
from great_tables.data import countrypops

countries_mini = (
    countrypops[countrypops["year"] == 2022]
    .sort_values("population", ascending=False)
    .head(10)[["country_name", "population"]]
)

(
    GT(countries_mini, rowname_col="country_name")
    .tab_header(
        title="The World's Most Populous Countries",
        subtitle="The top ten in 2022 are presented"
    )
    .fmt_integer(columns="population")
    .tab_source_note(
        source_note="Total population counts all residents regardless of legal status or citizenship."
    )
    .tab_source_note(
        source_note=md("Source: [The World Bank](https://data.worldbank.org/indicator/SP.POP.TOTL).")
    )
    .tab_stubhead(label="country")
)
```


<style>
#bzrcpexdyj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bzrcpexdyj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bzrcpexdyj p { margin: 0; padding: 0; }
 #bzrcpexdyj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bzrcpexdyj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bzrcpexdyj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bzrcpexdyj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bzrcpexdyj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bzrcpexdyj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bzrcpexdyj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bzrcpexdyj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bzrcpexdyj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bzrcpexdyj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bzrcpexdyj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bzrcpexdyj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bzrcpexdyj .gt_spanner_row { border-bottom-style: hidden; }
 #bzrcpexdyj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bzrcpexdyj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bzrcpexdyj .gt_from_md> :first-child { margin-top: 0; }
 #bzrcpexdyj .gt_from_md> :last-child { margin-bottom: 0; }
 #bzrcpexdyj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bzrcpexdyj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bzrcpexdyj .gt_indent_1 { text-indent: 5px; }
 #bzrcpexdyj .gt_indent_2 { text-indent: calc(5px * 2); }
 #bzrcpexdyj .gt_indent_3 { text-indent: calc(5px * 3); }
 #bzrcpexdyj .gt_indent_4 { text-indent: calc(5px * 4); }
 #bzrcpexdyj .gt_indent_5 { text-indent: calc(5px * 5); }
 #bzrcpexdyj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bzrcpexdyj .gt_row_group_first td { border-top-width: 2px; }
 #bzrcpexdyj .gt_row_group_first th { border-top-width: 2px; }
 #bzrcpexdyj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bzrcpexdyj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bzrcpexdyj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bzrcpexdyj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bzrcpexdyj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bzrcpexdyj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bzrcpexdyj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bzrcpexdyj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bzrcpexdyj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bzrcpexdyj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bzrcpexdyj .gt_left { text-align: left; }
 #bzrcpexdyj .gt_center { text-align: center; }
 #bzrcpexdyj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bzrcpexdyj .gt_font_normal { font-weight: normal; }
 #bzrcpexdyj .gt_font_bold { font-weight: bold; }
 #bzrcpexdyj .gt_font_italic { font-style: italic; }
 #bzrcpexdyj .gt_super { font-size: 65%; }
 #bzrcpexdyj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bzrcpexdyj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bzrcpexdyj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bzrcpexdyj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bzrcpexdyj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bzrcpexdyj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" id="title" class="gt_heading gt_title gt_font_normal">The World's Most Populous Countries</th>
</tr>
<tr class="gt_heading">
<th colspan="2" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">The top ten in 2022 are presented</th>
</tr>
<tr class="gt_col_headings">
<th id="country" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">country</th>
<th id="population" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">population</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">India</th>
<td class="gt_row gt_right" headers="stub-1 population">1,417,173,173</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">China</th>
<td class="gt_row gt_right" headers="stub-2 population">1,412,175,000</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">United States</th>
<td class="gt_row gt_right" headers="stub-3 population">333,287,557</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">Indonesia</th>
<td class="gt_row gt_right" headers="stub-4 population">275,501,339</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">Pakistan</th>
<td class="gt_row gt_right" headers="stub-5 population">235,824,862</td>
</tr>
<tr>
<th id="stub-6" class="gt_row gt_left gt_stub" scope="row">Nigeria</th>
<td class="gt_row gt_right" headers="stub-6 population">218,541,212</td>
</tr>
<tr>
<th id="stub-7" class="gt_row gt_left gt_stub" scope="row">Brazil</th>
<td class="gt_row gt_right" headers="stub-7 population">215,313,498</td>
</tr>
<tr>
<th id="stub-8" class="gt_row gt_left gt_stub" scope="row">Bangladesh</th>
<td class="gt_row gt_right" headers="stub-8 population">171,186,372</td>
</tr>
<tr>
<th id="stub-9" class="gt_row gt_left gt_stub" scope="row">Russian Federation</th>
<td class="gt_row gt_right" headers="stub-9 population">143,555,736</td>
</tr>
<tr>
<th id="stub-10" class="gt_row gt_left gt_stub" scope="row">Mexico</th>
<td class="gt_row gt_right" headers="stub-10 population">127,504,125</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="2" class="gt_sourcenote">Total population counts all residents regardless of legal status or citizenship.</td>
</tr>
<tr class="gt_sourcenotes">
<td colspan="2" class="gt_sourcenote">Source: [The World Bank](https://data.worldbank.org/indicator/SP.POP.TOTL).</td>
</tr>
</tfoot>

</table>


Show the Code

``` python
from great_tables import GT, html
from great_tables.data import gibraltar

gibraltar_m = gibraltar.head(10)[["date", "time", "temp", "humidity", "wind_speed", "pressure"]]

gt_gibraltar = (
    GT(gibraltar_m)
    .tab_header(
        title="Weather at Gibraltar Airport",
        subtitle="Observations from the early hours of May 1, 2023",
    )
    .tab_spanner(label="Observed", columns=["date", "time"])
    .tab_spanner(label="Measurement", columns=["temp", "humidity", "wind_speed", "pressure"])
    .fmt_percent(columns="humidity", decimals=0)
    .cols_label(
        date="Date",
        time="Time",
        temp=html("Temp,<br>°C"),
        humidity="Humidity",
        wind_speed=html("Wind,<br>m/s"),
        pressure=html("Pressure,<br>hPa"),
    )
)

gt_gibraltar
```


<style>
#tqnoqkqbtj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tqnoqkqbtj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tqnoqkqbtj p { margin: 0; padding: 0; }
 #tqnoqkqbtj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tqnoqkqbtj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tqnoqkqbtj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tqnoqkqbtj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tqnoqkqbtj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tqnoqkqbtj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tqnoqkqbtj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tqnoqkqbtj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tqnoqkqbtj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tqnoqkqbtj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tqnoqkqbtj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tqnoqkqbtj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tqnoqkqbtj .gt_spanner_row { border-bottom-style: hidden; }
 #tqnoqkqbtj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tqnoqkqbtj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tqnoqkqbtj .gt_from_md> :first-child { margin-top: 0; }
 #tqnoqkqbtj .gt_from_md> :last-child { margin-bottom: 0; }
 #tqnoqkqbtj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tqnoqkqbtj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tqnoqkqbtj .gt_indent_1 { text-indent: 5px; }
 #tqnoqkqbtj .gt_indent_2 { text-indent: calc(5px * 2); }
 #tqnoqkqbtj .gt_indent_3 { text-indent: calc(5px * 3); }
 #tqnoqkqbtj .gt_indent_4 { text-indent: calc(5px * 4); }
 #tqnoqkqbtj .gt_indent_5 { text-indent: calc(5px * 5); }
 #tqnoqkqbtj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tqnoqkqbtj .gt_row_group_first td { border-top-width: 2px; }
 #tqnoqkqbtj .gt_row_group_first th { border-top-width: 2px; }
 #tqnoqkqbtj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tqnoqkqbtj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tqnoqkqbtj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tqnoqkqbtj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tqnoqkqbtj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tqnoqkqbtj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tqnoqkqbtj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tqnoqkqbtj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tqnoqkqbtj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tqnoqkqbtj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tqnoqkqbtj .gt_left { text-align: left; }
 #tqnoqkqbtj .gt_center { text-align: center; }
 #tqnoqkqbtj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tqnoqkqbtj .gt_font_normal { font-weight: normal; }
 #tqnoqkqbtj .gt_font_bold { font-weight: bold; }
 #tqnoqkqbtj .gt_font_italic { font-style: italic; }
 #tqnoqkqbtj .gt_super { font-size: 65%; }
 #tqnoqkqbtj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tqnoqkqbtj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tqnoqkqbtj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tqnoqkqbtj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tqnoqkqbtj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tqnoqkqbtj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" style="width:100%;" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
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
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Weather at Gibraltar Airport</th>
</tr>
<tr class="gt_heading">
<th colspan="6" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Observations from the early hours of May 1, 2023</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="2" id="Observed" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Observed</th>
<th colspan="4" id="Measurement" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Measurement</th>
</tr>
<tr class="gt_col_headings">
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Time</th>
<th id="temp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Temp,<br />
°C</th>
<th id="humidity" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Humidity</th>
<th id="wind_speed" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Wind,<br />
m/s</th>
<th id="pressure" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Pressure,<br />
hPa</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">00:20</td>
<td class="gt_row gt_right" headers="Measurement temp">18.9</td>
<td class="gt_row gt_right" headers="Measurement humidity">68%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">6.7</td>
<td class="gt_row gt_right" headers="Measurement pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">00:50</td>
<td class="gt_row gt_right" headers="Measurement temp">18.9</td>
<td class="gt_row gt_right" headers="Measurement humidity">73%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">7.2</td>
<td class="gt_row gt_right" headers="Measurement pressure">1015.2</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">01:20</td>
<td class="gt_row gt_right" headers="Measurement temp">17.8</td>
<td class="gt_row gt_right" headers="Measurement humidity">77%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">6.7</td>
<td class="gt_row gt_right" headers="Measurement pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">01:50</td>
<td class="gt_row gt_right" headers="Measurement temp">18.9</td>
<td class="gt_row gt_right" headers="Measurement humidity">73%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">6.7</td>
<td class="gt_row gt_right" headers="Measurement pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">02:20</td>
<td class="gt_row gt_right" headers="Measurement temp">18.9</td>
<td class="gt_row gt_right" headers="Measurement humidity">68%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">6.7</td>
<td class="gt_row gt_right" headers="Measurement pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">02:50</td>
<td class="gt_row gt_right" headers="Measurement temp">17.8</td>
<td class="gt_row gt_right" headers="Measurement humidity">73%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">6.7</td>
<td class="gt_row gt_right" headers="Measurement pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">03:20</td>
<td class="gt_row gt_right" headers="Measurement temp">17.8</td>
<td class="gt_row gt_right" headers="Measurement humidity">73%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">7.2</td>
<td class="gt_row gt_right" headers="Measurement pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">03:50</td>
<td class="gt_row gt_right" headers="Measurement temp">17.8</td>
<td class="gt_row gt_right" headers="Measurement humidity">73%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">6.3</td>
<td class="gt_row gt_right" headers="Measurement pressure">1013.5</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">04:20</td>
<td class="gt_row gt_right" headers="Measurement temp">18.9</td>
<td class="gt_row gt_right" headers="Measurement humidity">64%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">4.0</td>
<td class="gt_row gt_right" headers="Measurement pressure">1014.6</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="Observed date">2023-05-01</td>
<td class="gt_row gt_right" headers="Observed time">04:50</td>
<td class="gt_row gt_right" headers="Measurement temp">18.9</td>
<td class="gt_row gt_right" headers="Measurement humidity">64%</td>
<td class="gt_row gt_right" headers="Measurement wind_speed">3.1</td>
<td class="gt_row gt_right" headers="Measurement pressure">1014.6</td>
</tr>
</tbody>
</table>


These examples show just a glimpse of what's possible with **Great Tables**. The rest of this User Guide will walk you through each capability in detail, from structuring your table with headers, stubs, and column labels, to formatting values, adding visual styles, and embedding nanoplots directly in your cells.


# The Anatomy of a Table

Every table produced by **Great Tables** is composed of a set of structural components. Understanding these components and how they relate to each other is key to building effective presentation tables.

The **Great Tables** package makes it relatively easy to add components so that the resulting output table better conveys the information you want to present. These table components work well together and the possible variations in arrangement can handle even the most demanding table presentation needs. The previous output table we showed had only two components: the **Column Labels** and the **Table Body**. The next few examples will show all of the other table parts that are available.

This is the way the main parts of a table (and their subparts) fit together:

<img src="../assets/gt_parts_of_a_table.svg" class="img-fluid" />

The following list describes each major component of a **Great Tables** output, ordered from top to bottom:

- the **Table Header** (optional, with a **title** and possibly a **subtitle**)
- the **Stub** and the **Stub Head** (optional, contains *row labels*, optionally within *row groups* having *row group labels*)
- the **Column Labels** (contains *column labels*, optionally under *spanner labels*)
- the **Table Body** (contains *columns* and *rows* of *cells*)
- the **Table Footer** (optional, possibly with one or more **source notes**)

Not every table needs every component. A simple table may only require column labels and a body, and that is perfectly fine. The components listed above are opt-in: you add whichever ones help your reader understand the data, and leave the rest out. A title might be essential for a published report but unnecessary in an exploratory notebook. Source notes matter when provenance is important but can be skipped for internal dashboards. Let the context guide your choices.

Each of these parts is covered in detail throughout the rest of this User Guide. The pages that follow will show you how to add a header and footer, create a stub with row labels and groupings, organize your column labels with spanners, format cell values, and apply styling to any part of the table.
