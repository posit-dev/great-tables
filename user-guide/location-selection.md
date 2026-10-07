# Location Selection

The `loc` module is what connects your styling intentions to specific parts of the table. Each location specifier identifies a region of the table (such as the header, body, stub, or footer) and many of them also support targeting specific columns or rows within that region. This page provides a comprehensive overview of all available location specifiers and how to use them effectively.

Understanding the `loc` module is valuable because it provides a single, consistent vocabulary for addressing any part of the table. Rather than learning separate APIs for styling the header vs. the body vs. the stub, you use the same `loc.*()` specifiers everywhere. This means that once you know how to style a column label, the pattern for styling a row group label or a source note is immediately familiar.


# Overview

Great Tables uses the `loc` module to specify locations for styling in [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style). Some location specifiers also allow selecting specific columns and rows of data.

For example, you might style a particular row name, group, column, or spanner label.

The table below shows the different location specifiers, along with the types of column or row selection they allow.


<style>
#tocezvcvhz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tocezvcvhz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tocezvcvhz p { margin: 0; padding: 0; }
 #tocezvcvhz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tocezvcvhz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tocezvcvhz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tocezvcvhz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tocezvcvhz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tocezvcvhz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tocezvcvhz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tocezvcvhz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tocezvcvhz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tocezvcvhz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tocezvcvhz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tocezvcvhz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tocezvcvhz .gt_spanner_row { border-bottom-style: hidden; }
 #tocezvcvhz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tocezvcvhz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tocezvcvhz .gt_from_md> :first-child { margin-top: 0; }
 #tocezvcvhz .gt_from_md> :last-child { margin-bottom: 0; }
 #tocezvcvhz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tocezvcvhz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tocezvcvhz .gt_indent_1 { text-indent: 5px; }
 #tocezvcvhz .gt_indent_2 { text-indent: calc(5px * 2); }
 #tocezvcvhz .gt_indent_3 { text-indent: calc(5px * 3); }
 #tocezvcvhz .gt_indent_4 { text-indent: calc(5px * 4); }
 #tocezvcvhz .gt_indent_5 { text-indent: calc(5px * 5); }
 #tocezvcvhz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tocezvcvhz .gt_row_group_first td { border-top-width: 2px; }
 #tocezvcvhz .gt_row_group_first th { border-top-width: 2px; }
 #tocezvcvhz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tocezvcvhz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tocezvcvhz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tocezvcvhz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tocezvcvhz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tocezvcvhz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tocezvcvhz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tocezvcvhz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tocezvcvhz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tocezvcvhz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tocezvcvhz .gt_left { text-align: left; }
 #tocezvcvhz .gt_center { text-align: center; }
 #tocezvcvhz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tocezvcvhz .gt_font_normal { font-weight: normal; }
 #tocezvcvhz .gt_font_bold { font-weight: bold; }
 #tocezvcvhz .gt_font_italic { font-style: italic; }
 #tocezvcvhz .gt_super { font-size: 65%; }
 #tocezvcvhz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tocezvcvhz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tocezvcvhz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tocezvcvhz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tocezvcvhz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tocezvcvhz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| table part | name                     | selection        |
|------------|--------------------------|------------------|
| header     | loc.header()             | composite        |
|            | loc.title()              |                  |
|            | loc.subtitle()           |                  |
| boxhead    | loc.column_header()      | composite        |
|            | loc.spanner_labels()     | columns          |
|            | loc.column_labels()      | columns          |
| row stub   | loc.stub()               | rows             |
|            | loc.row_groups()         | rows             |
|            | loc.grand_summary_stub() | rows             |
| table body | loc.body()               | columns and rows |
|            | loc.grand_summary_rows() | columns and rows |
| footer     | loc.footer()             | composite        |
|            | loc.source_notes()       |                  |


Note that composite specifiers are ones that target multiple locations. For example, [loc.header()](../reference/loc.header.md#great_tables.loc.header) specifies both [loc.title()](../reference/loc.title.md#great_tables.loc.title) and [loc.subtitle()](../reference/loc.subtitle.md#great_tables.loc.subtitle).


# Setting up data

The examples below will use this small dataset to show selecting different locations, as well as specific rows and columns within a location (where supported).


``` python
import polars as pl
import polars.selectors as cs

from great_tables import GT, loc, style, exibble

pl_exibble = pl.from_pandas(exibble)[[0, 1, 4], ["num", "char", "group"]]

pl_exibble
```


shape: (3, 3)

| num    | char      | group   |
|--------|-----------|---------|
| f64    | str       | str     |
| 0.1111 | "apricot" | "grp_a" |
| 2.222  | "banana"  | "grp_a" |
| 5550.0 | null      | "grp_b" |


This small three-row, three-column dataset gives us enough structure to demonstrate row and column targeting without cluttering the output.


# Simple locations

Simple locations don't take any arguments.

For example, styling the title uses [loc.title()](../reference/loc.title.md#great_tables.loc.title).


``` python
(
    GT(pl_exibble)
    .tab_header("A title", "A subtitle")
    .tab_style(
        style.fill("yellow"),
        loc.title(),
    )
)
```


<style>
#yvzyehyfgw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yvzyehyfgw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yvzyehyfgw p { margin: 0; padding: 0; }
 #yvzyehyfgw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yvzyehyfgw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yvzyehyfgw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yvzyehyfgw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yvzyehyfgw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yvzyehyfgw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yvzyehyfgw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yvzyehyfgw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yvzyehyfgw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yvzyehyfgw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yvzyehyfgw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yvzyehyfgw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yvzyehyfgw .gt_spanner_row { border-bottom-style: hidden; }
 #yvzyehyfgw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yvzyehyfgw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yvzyehyfgw .gt_from_md> :first-child { margin-top: 0; }
 #yvzyehyfgw .gt_from_md> :last-child { margin-bottom: 0; }
 #yvzyehyfgw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yvzyehyfgw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yvzyehyfgw .gt_indent_1 { text-indent: 5px; }
 #yvzyehyfgw .gt_indent_2 { text-indent: calc(5px * 2); }
 #yvzyehyfgw .gt_indent_3 { text-indent: calc(5px * 3); }
 #yvzyehyfgw .gt_indent_4 { text-indent: calc(5px * 4); }
 #yvzyehyfgw .gt_indent_5 { text-indent: calc(5px * 5); }
 #yvzyehyfgw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yvzyehyfgw .gt_row_group_first td { border-top-width: 2px; }
 #yvzyehyfgw .gt_row_group_first th { border-top-width: 2px; }
 #yvzyehyfgw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yvzyehyfgw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yvzyehyfgw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yvzyehyfgw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yvzyehyfgw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yvzyehyfgw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yvzyehyfgw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yvzyehyfgw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yvzyehyfgw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yvzyehyfgw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yvzyehyfgw .gt_left { text-align: left; }
 #yvzyehyfgw .gt_center { text-align: center; }
 #yvzyehyfgw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yvzyehyfgw .gt_font_normal { font-weight: normal; }
 #yvzyehyfgw .gt_font_bold { font-weight: bold; }
 #yvzyehyfgw .gt_font_italic { font-style: italic; }
 #yvzyehyfgw .gt_super { font-size: 65%; }
 #yvzyehyfgw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yvzyehyfgw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yvzyehyfgw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yvzyehyfgw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yvzyehyfgw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yvzyehyfgw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal" style="background-color: yellow">A title</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">A subtitle</th>
</tr>
<tr class="gt_col_headings">
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="group" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">group</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">grp_a</td>
</tr>
<tr>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">grp_a</td>
</tr>
<tr>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">grp_b</td>
</tr>
</tbody>
</table>


Only the title receives the yellow fill; the subtitle and the rest of the table remain unstyled. Simple locations are useful when you want precise control over a single element.


# Composite locations

Composite locations target multiple simple locations.

For example, [loc.header()](../reference/loc.header.md#great_tables.loc.header) includes both [loc.title()](../reference/loc.title.md#great_tables.loc.title) and [loc.subtitle()](../reference/loc.subtitle.md#great_tables.loc.subtitle).


``` python
(
    GT(pl_exibble)
    .tab_header("A title", "A subtitle")
    .tab_style(
        style.fill("yellow"),
        loc.header(),
    )
)
```


<style>
#tiagzysnhd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tiagzysnhd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tiagzysnhd p { margin: 0; padding: 0; }
 #tiagzysnhd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tiagzysnhd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tiagzysnhd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tiagzysnhd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tiagzysnhd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tiagzysnhd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tiagzysnhd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tiagzysnhd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tiagzysnhd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tiagzysnhd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tiagzysnhd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tiagzysnhd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tiagzysnhd .gt_spanner_row { border-bottom-style: hidden; }
 #tiagzysnhd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tiagzysnhd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tiagzysnhd .gt_from_md> :first-child { margin-top: 0; }
 #tiagzysnhd .gt_from_md> :last-child { margin-bottom: 0; }
 #tiagzysnhd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tiagzysnhd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tiagzysnhd .gt_indent_1 { text-indent: 5px; }
 #tiagzysnhd .gt_indent_2 { text-indent: calc(5px * 2); }
 #tiagzysnhd .gt_indent_3 { text-indent: calc(5px * 3); }
 #tiagzysnhd .gt_indent_4 { text-indent: calc(5px * 4); }
 #tiagzysnhd .gt_indent_5 { text-indent: calc(5px * 5); }
 #tiagzysnhd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tiagzysnhd .gt_row_group_first td { border-top-width: 2px; }
 #tiagzysnhd .gt_row_group_first th { border-top-width: 2px; }
 #tiagzysnhd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tiagzysnhd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tiagzysnhd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tiagzysnhd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tiagzysnhd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tiagzysnhd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tiagzysnhd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tiagzysnhd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tiagzysnhd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tiagzysnhd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tiagzysnhd .gt_left { text-align: left; }
 #tiagzysnhd .gt_center { text-align: center; }
 #tiagzysnhd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tiagzysnhd .gt_font_normal { font-weight: normal; }
 #tiagzysnhd .gt_font_bold { font-weight: bold; }
 #tiagzysnhd .gt_font_italic { font-style: italic; }
 #tiagzysnhd .gt_super { font-size: 65%; }
 #tiagzysnhd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tiagzysnhd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tiagzysnhd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tiagzysnhd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tiagzysnhd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tiagzysnhd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal" style="background-color: yellow">A title</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="background-color: yellow">A subtitle</th>
</tr>
<tr class="gt_col_headings">
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="group" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">group</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">grp_a</td>
</tr>
<tr>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">grp_a</td>
</tr>
<tr>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">grp_b</td>
</tr>
</tbody>
</table>


Both the title and subtitle are filled with yellow because [loc.header()](../reference/loc.header.md#great_tables.loc.header) targets the entire header region. Composite locations are a convenient shorthand when you want the same style on all sub-parts.


# Body columns, rows and mask

Use `columns=` and `rows=` in [loc.body()](../reference/loc.body.md#great_tables.loc.body) to style specific cells in the table body.


``` python
(
    GT(pl_exibble).tab_style(
        style.fill("yellow"),
        loc.body(
            columns=cs.starts_with("cha"),
            rows=pl.col("char").str.contains("a"),
        ),
    )
)
```


<style>
#dyeetbcxoc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dyeetbcxoc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dyeetbcxoc p { margin: 0; padding: 0; }
 #dyeetbcxoc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dyeetbcxoc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dyeetbcxoc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dyeetbcxoc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dyeetbcxoc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dyeetbcxoc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dyeetbcxoc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dyeetbcxoc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dyeetbcxoc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dyeetbcxoc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dyeetbcxoc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dyeetbcxoc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dyeetbcxoc .gt_spanner_row { border-bottom-style: hidden; }
 #dyeetbcxoc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dyeetbcxoc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dyeetbcxoc .gt_from_md> :first-child { margin-top: 0; }
 #dyeetbcxoc .gt_from_md> :last-child { margin-bottom: 0; }
 #dyeetbcxoc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dyeetbcxoc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dyeetbcxoc .gt_indent_1 { text-indent: 5px; }
 #dyeetbcxoc .gt_indent_2 { text-indent: calc(5px * 2); }
 #dyeetbcxoc .gt_indent_3 { text-indent: calc(5px * 3); }
 #dyeetbcxoc .gt_indent_4 { text-indent: calc(5px * 4); }
 #dyeetbcxoc .gt_indent_5 { text-indent: calc(5px * 5); }
 #dyeetbcxoc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dyeetbcxoc .gt_row_group_first td { border-top-width: 2px; }
 #dyeetbcxoc .gt_row_group_first th { border-top-width: 2px; }
 #dyeetbcxoc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dyeetbcxoc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dyeetbcxoc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dyeetbcxoc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dyeetbcxoc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dyeetbcxoc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dyeetbcxoc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dyeetbcxoc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dyeetbcxoc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dyeetbcxoc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dyeetbcxoc .gt_left { text-align: left; }
 #dyeetbcxoc .gt_center { text-align: center; }
 #dyeetbcxoc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dyeetbcxoc .gt_font_normal { font-weight: normal; }
 #dyeetbcxoc .gt_font_bold { font-weight: bold; }
 #dyeetbcxoc .gt_font_italic { font-style: italic; }
 #dyeetbcxoc .gt_super { font-size: 65%; }
 #dyeetbcxoc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dyeetbcxoc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dyeetbcxoc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dyeetbcxoc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dyeetbcxoc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dyeetbcxoc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | group |
|--------|---------|-------|
| 0.1111 | apricot | grp_a |
| 2.222  | banana  | grp_a |
| 5550.0 | None    | grp_b |


Alternatively, use `mask=` in [loc.body()](../reference/loc.body.md#great_tables.loc.body) to apply conditional styling to rows on a per-column basis.


``` python
(
    GT(pl_exibble).tab_style(
        style.fill("yellow"),
        loc.body(mask=cs.string().str.contains("p")),
    )
)
```


<style>
#hbjjmwislr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hbjjmwislr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hbjjmwislr p { margin: 0; padding: 0; }
 #hbjjmwislr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hbjjmwislr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hbjjmwislr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hbjjmwislr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hbjjmwislr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hbjjmwislr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hbjjmwislr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hbjjmwislr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hbjjmwislr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hbjjmwislr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hbjjmwislr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hbjjmwislr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hbjjmwislr .gt_spanner_row { border-bottom-style: hidden; }
 #hbjjmwislr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hbjjmwislr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hbjjmwislr .gt_from_md> :first-child { margin-top: 0; }
 #hbjjmwislr .gt_from_md> :last-child { margin-bottom: 0; }
 #hbjjmwislr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hbjjmwislr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hbjjmwislr .gt_indent_1 { text-indent: 5px; }
 #hbjjmwislr .gt_indent_2 { text-indent: calc(5px * 2); }
 #hbjjmwislr .gt_indent_3 { text-indent: calc(5px * 3); }
 #hbjjmwislr .gt_indent_4 { text-indent: calc(5px * 4); }
 #hbjjmwislr .gt_indent_5 { text-indent: calc(5px * 5); }
 #hbjjmwislr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hbjjmwislr .gt_row_group_first td { border-top-width: 2px; }
 #hbjjmwislr .gt_row_group_first th { border-top-width: 2px; }
 #hbjjmwislr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hbjjmwislr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hbjjmwislr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hbjjmwislr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hbjjmwislr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hbjjmwislr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hbjjmwislr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hbjjmwislr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hbjjmwislr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hbjjmwislr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hbjjmwislr .gt_left { text-align: left; }
 #hbjjmwislr .gt_center { text-align: center; }
 #hbjjmwislr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hbjjmwislr .gt_font_normal { font-weight: normal; }
 #hbjjmwislr .gt_font_bold { font-weight: bold; }
 #hbjjmwislr .gt_font_italic { font-style: italic; }
 #hbjjmwislr .gt_super { font-size: 65%; }
 #hbjjmwislr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hbjjmwislr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hbjjmwislr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hbjjmwislr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hbjjmwislr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hbjjmwislr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | group |
|--------|---------|-------|
| 0.1111 | apricot | grp_a |
| 2.222  | banana  | grp_a |
| 5550.0 | None    | grp_b |


This is discussed in detail in [Styling the Table Body](styling-the-table-body.md).


# Column labels

Locations like [loc.spanner_labels()](../reference/loc.spanner_labels.md#great_tables.loc.spanner_labels) and [loc.column_labels()](../reference/loc.column_labels.md#great_tables.loc.column_labels) can select specific column and spanner labels.

You can use name strings, index position, or polars selectors.


``` python
GT(pl_exibble).tab_style(
    style.fill("yellow"),
    loc.column_labels(
        cs.starts_with("cha"),
    ),
)
```


<style>
#crciniepjh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#crciniepjh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#crciniepjh p { margin: 0; padding: 0; }
 #crciniepjh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #crciniepjh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #crciniepjh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #crciniepjh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #crciniepjh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #crciniepjh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #crciniepjh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #crciniepjh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #crciniepjh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #crciniepjh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #crciniepjh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #crciniepjh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #crciniepjh .gt_spanner_row { border-bottom-style: hidden; }
 #crciniepjh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #crciniepjh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #crciniepjh .gt_from_md> :first-child { margin-top: 0; }
 #crciniepjh .gt_from_md> :last-child { margin-bottom: 0; }
 #crciniepjh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #crciniepjh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #crciniepjh .gt_indent_1 { text-indent: 5px; }
 #crciniepjh .gt_indent_2 { text-indent: calc(5px * 2); }
 #crciniepjh .gt_indent_3 { text-indent: calc(5px * 3); }
 #crciniepjh .gt_indent_4 { text-indent: calc(5px * 4); }
 #crciniepjh .gt_indent_5 { text-indent: calc(5px * 5); }
 #crciniepjh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #crciniepjh .gt_row_group_first td { border-top-width: 2px; }
 #crciniepjh .gt_row_group_first th { border-top-width: 2px; }
 #crciniepjh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #crciniepjh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #crciniepjh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #crciniepjh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #crciniepjh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #crciniepjh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #crciniepjh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #crciniepjh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #crciniepjh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #crciniepjh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #crciniepjh .gt_left { text-align: left; }
 #crciniepjh .gt_center { text-align: center; }
 #crciniepjh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #crciniepjh .gt_font_normal { font-weight: normal; }
 #crciniepjh .gt_font_bold { font-weight: bold; }
 #crciniepjh .gt_font_italic { font-style: italic; }
 #crciniepjh .gt_super { font-size: 65%; }
 #crciniepjh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #crciniepjh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #crciniepjh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #crciniepjh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #crciniepjh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #crciniepjh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | group |
|--------|---------|-------|
| 0.1111 | apricot | grp_a |
| 2.222  | banana  | grp_a |
| 5550.0 | None    | grp_b |


However, note that [loc.spanner_labels()](../reference/loc.spanner_labels.md#great_tables.loc.spanner_labels) currently only accepts list of string names.


# Row and group names

Row and group names in [loc.stub()](../reference/loc.stub.md#great_tables.loc.stub) and [loc.row_groups()](../reference/loc.row_groups.md#great_tables.loc.row_groups) may be specified three ways:

- by name
- by index
- by polars expression


``` python
gt = GT(pl_exibble).tab_stub(
    rowname_col="char",
    groupname_col="group",
)

gt.tab_style(style.fill("yellow"), loc.stub())
```


<style>
#rdwphcscqt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rdwphcscqt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rdwphcscqt p { margin: 0; padding: 0; }
 #rdwphcscqt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rdwphcscqt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rdwphcscqt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rdwphcscqt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rdwphcscqt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rdwphcscqt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdwphcscqt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rdwphcscqt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rdwphcscqt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rdwphcscqt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rdwphcscqt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rdwphcscqt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rdwphcscqt .gt_spanner_row { border-bottom-style: hidden; }
 #rdwphcscqt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rdwphcscqt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rdwphcscqt .gt_from_md> :first-child { margin-top: 0; }
 #rdwphcscqt .gt_from_md> :last-child { margin-bottom: 0; }
 #rdwphcscqt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rdwphcscqt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rdwphcscqt .gt_indent_1 { text-indent: 5px; }
 #rdwphcscqt .gt_indent_2 { text-indent: calc(5px * 2); }
 #rdwphcscqt .gt_indent_3 { text-indent: calc(5px * 3); }
 #rdwphcscqt .gt_indent_4 { text-indent: calc(5px * 4); }
 #rdwphcscqt .gt_indent_5 { text-indent: calc(5px * 5); }
 #rdwphcscqt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rdwphcscqt .gt_row_group_first td { border-top-width: 2px; }
 #rdwphcscqt .gt_row_group_first th { border-top-width: 2px; }
 #rdwphcscqt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rdwphcscqt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdwphcscqt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rdwphcscqt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rdwphcscqt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdwphcscqt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rdwphcscqt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rdwphcscqt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rdwphcscqt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdwphcscqt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rdwphcscqt .gt_left { text-align: left; }
 #rdwphcscqt .gt_center { text-align: center; }
 #rdwphcscqt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rdwphcscqt .gt_font_normal { font-weight: normal; }
 #rdwphcscqt .gt_font_bold { font-weight: bold; }
 #rdwphcscqt .gt_font_italic { font-style: italic; }
 #rdwphcscqt .gt_super { font-size: 65%; }
 #rdwphcscqt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdwphcscqt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rdwphcscqt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdwphcscqt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rdwphcscqt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rdwphcscqt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow">None</td>
<td class="gt_row gt_right">5550.0</td>
</tr>
</tbody>
</table>


All row labels in the stub are highlighted in yellow.


``` python
gt.tab_style(style.fill("yellow"), loc.stub("banana"))
```


<style>
#uvlzijqrli table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uvlzijqrli thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uvlzijqrli p { margin: 0; padding: 0; }
 #uvlzijqrli .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uvlzijqrli .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uvlzijqrli .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uvlzijqrli .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uvlzijqrli .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvlzijqrli .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvlzijqrli .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvlzijqrli .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uvlzijqrli .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uvlzijqrli .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uvlzijqrli .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uvlzijqrli .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uvlzijqrli .gt_spanner_row { border-bottom-style: hidden; }
 #uvlzijqrli .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uvlzijqrli .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uvlzijqrli .gt_from_md> :first-child { margin-top: 0; }
 #uvlzijqrli .gt_from_md> :last-child { margin-bottom: 0; }
 #uvlzijqrli .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uvlzijqrli .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uvlzijqrli .gt_indent_1 { text-indent: 5px; }
 #uvlzijqrli .gt_indent_2 { text-indent: calc(5px * 2); }
 #uvlzijqrli .gt_indent_3 { text-indent: calc(5px * 3); }
 #uvlzijqrli .gt_indent_4 { text-indent: calc(5px * 4); }
 #uvlzijqrli .gt_indent_5 { text-indent: calc(5px * 5); }
 #uvlzijqrli .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uvlzijqrli .gt_row_group_first td { border-top-width: 2px; }
 #uvlzijqrli .gt_row_group_first th { border-top-width: 2px; }
 #uvlzijqrli .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uvlzijqrli .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvlzijqrli .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvlzijqrli .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uvlzijqrli .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvlzijqrli .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvlzijqrli .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uvlzijqrli .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uvlzijqrli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvlzijqrli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvlzijqrli .gt_left { text-align: left; }
 #uvlzijqrli .gt_center { text-align: center; }
 #uvlzijqrli .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uvlzijqrli .gt_font_normal { font-weight: normal; }
 #uvlzijqrli .gt_font_bold { font-weight: bold; }
 #uvlzijqrli .gt_font_italic { font-style: italic; }
 #uvlzijqrli .gt_super { font-size: 65%; }
 #uvlzijqrli .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvlzijqrli .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uvlzijqrli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvlzijqrli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvlzijqrli .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uvlzijqrli .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">None</td>
<td class="gt_row gt_right">5550.0</td>
</tr>
</tbody>
</table>


Only the `"banana"` row label is styled, demonstrating name-based targeting.


``` python
gt.tab_style(style.fill("yellow"), loc.stub(["apricot", 2]))
```


<style>
#rloktaoebx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rloktaoebx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rloktaoebx p { margin: 0; padding: 0; }
 #rloktaoebx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rloktaoebx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rloktaoebx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rloktaoebx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rloktaoebx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rloktaoebx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rloktaoebx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rloktaoebx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rloktaoebx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rloktaoebx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rloktaoebx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rloktaoebx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rloktaoebx .gt_spanner_row { border-bottom-style: hidden; }
 #rloktaoebx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rloktaoebx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rloktaoebx .gt_from_md> :first-child { margin-top: 0; }
 #rloktaoebx .gt_from_md> :last-child { margin-bottom: 0; }
 #rloktaoebx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rloktaoebx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rloktaoebx .gt_indent_1 { text-indent: 5px; }
 #rloktaoebx .gt_indent_2 { text-indent: calc(5px * 2); }
 #rloktaoebx .gt_indent_3 { text-indent: calc(5px * 3); }
 #rloktaoebx .gt_indent_4 { text-indent: calc(5px * 4); }
 #rloktaoebx .gt_indent_5 { text-indent: calc(5px * 5); }
 #rloktaoebx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rloktaoebx .gt_row_group_first td { border-top-width: 2px; }
 #rloktaoebx .gt_row_group_first th { border-top-width: 2px; }
 #rloktaoebx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rloktaoebx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rloktaoebx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rloktaoebx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rloktaoebx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rloktaoebx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rloktaoebx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rloktaoebx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rloktaoebx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rloktaoebx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rloktaoebx .gt_left { text-align: left; }
 #rloktaoebx .gt_center { text-align: center; }
 #rloktaoebx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rloktaoebx .gt_font_normal { font-weight: normal; }
 #rloktaoebx .gt_font_bold { font-weight: bold; }
 #rloktaoebx .gt_font_italic { font-style: italic; }
 #rloktaoebx .gt_super { font-size: 65%; }
 #rloktaoebx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rloktaoebx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rloktaoebx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rloktaoebx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rloktaoebx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rloktaoebx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow">None</td>
<td class="gt_row gt_right">5550.0</td>
</tr>
</tbody>
</table>


You can mix names and integer indices in a list to target multiple specific rows at once.


## Groups by name and position

Note that for specifying row groups, the group corresponding to the group name or row number in the original data is used.

For example, the code below styles the group corresponding to the row at index 1 (i.e., the second row) in the data.


``` python
gt.tab_style(
    style.fill("yellow"),
    loc.row_groups(1),
)
```


<style>
#bpwscswvhq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bpwscswvhq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bpwscswvhq p { margin: 0; padding: 0; }
 #bpwscswvhq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bpwscswvhq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bpwscswvhq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bpwscswvhq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bpwscswvhq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpwscswvhq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpwscswvhq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpwscswvhq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bpwscswvhq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bpwscswvhq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bpwscswvhq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bpwscswvhq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bpwscswvhq .gt_spanner_row { border-bottom-style: hidden; }
 #bpwscswvhq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bpwscswvhq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bpwscswvhq .gt_from_md> :first-child { margin-top: 0; }
 #bpwscswvhq .gt_from_md> :last-child { margin-bottom: 0; }
 #bpwscswvhq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bpwscswvhq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bpwscswvhq .gt_indent_1 { text-indent: 5px; }
 #bpwscswvhq .gt_indent_2 { text-indent: calc(5px * 2); }
 #bpwscswvhq .gt_indent_3 { text-indent: calc(5px * 3); }
 #bpwscswvhq .gt_indent_4 { text-indent: calc(5px * 4); }
 #bpwscswvhq .gt_indent_5 { text-indent: calc(5px * 5); }
 #bpwscswvhq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bpwscswvhq .gt_row_group_first td { border-top-width: 2px; }
 #bpwscswvhq .gt_row_group_first th { border-top-width: 2px; }
 #bpwscswvhq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bpwscswvhq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpwscswvhq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpwscswvhq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bpwscswvhq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpwscswvhq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpwscswvhq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bpwscswvhq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bpwscswvhq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpwscswvhq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpwscswvhq .gt_left { text-align: left; }
 #bpwscswvhq .gt_center { text-align: center; }
 #bpwscswvhq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bpwscswvhq .gt_font_normal { font-weight: normal; }
 #bpwscswvhq .gt_font_bold { font-weight: bold; }
 #bpwscswvhq .gt_font_italic { font-style: italic; }
 #bpwscswvhq .gt_super { font-size: 65%; }
 #bpwscswvhq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpwscswvhq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bpwscswvhq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpwscswvhq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpwscswvhq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bpwscswvhq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading" style="background-color: yellow">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">None</td>
<td class="gt_row gt_right">5550.0</td>
</tr>
</tbody>
</table>


Since the second row (starting with "banana") is in "grp_a", that is the group that gets styled.

This means you can use a polars expression to select groups:


``` python
gt.tab_style(
    style.fill("yellow"),
    loc.row_groups(pl.col("group") == "grp_b"),
)
```


<style>
#mecqnrgyzp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mecqnrgyzp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mecqnrgyzp p { margin: 0; padding: 0; }
 #mecqnrgyzp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mecqnrgyzp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mecqnrgyzp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mecqnrgyzp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mecqnrgyzp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mecqnrgyzp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mecqnrgyzp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mecqnrgyzp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mecqnrgyzp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mecqnrgyzp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mecqnrgyzp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mecqnrgyzp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mecqnrgyzp .gt_spanner_row { border-bottom-style: hidden; }
 #mecqnrgyzp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mecqnrgyzp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mecqnrgyzp .gt_from_md> :first-child { margin-top: 0; }
 #mecqnrgyzp .gt_from_md> :last-child { margin-bottom: 0; }
 #mecqnrgyzp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mecqnrgyzp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mecqnrgyzp .gt_indent_1 { text-indent: 5px; }
 #mecqnrgyzp .gt_indent_2 { text-indent: calc(5px * 2); }
 #mecqnrgyzp .gt_indent_3 { text-indent: calc(5px * 3); }
 #mecqnrgyzp .gt_indent_4 { text-indent: calc(5px * 4); }
 #mecqnrgyzp .gt_indent_5 { text-indent: calc(5px * 5); }
 #mecqnrgyzp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mecqnrgyzp .gt_row_group_first td { border-top-width: 2px; }
 #mecqnrgyzp .gt_row_group_first th { border-top-width: 2px; }
 #mecqnrgyzp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mecqnrgyzp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mecqnrgyzp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mecqnrgyzp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mecqnrgyzp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mecqnrgyzp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mecqnrgyzp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mecqnrgyzp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mecqnrgyzp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mecqnrgyzp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mecqnrgyzp .gt_left { text-align: left; }
 #mecqnrgyzp .gt_center { text-align: center; }
 #mecqnrgyzp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mecqnrgyzp .gt_font_normal { font-weight: normal; }
 #mecqnrgyzp .gt_font_bold { font-weight: bold; }
 #mecqnrgyzp .gt_font_italic { font-style: italic; }
 #mecqnrgyzp .gt_super { font-size: 65%; }
 #mecqnrgyzp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mecqnrgyzp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mecqnrgyzp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mecqnrgyzp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mecqnrgyzp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mecqnrgyzp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading" style="background-color: yellow">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">None</td>
<td class="gt_row gt_right">5550.0</td>
</tr>
</tbody>
</table>


You can also specify group names using a string (or list of strings).


``` python
gt.tab_style(
    style.fill("yellow"),
    loc.row_groups("grp_b"),
)
```


<style>
#yclbuysliw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yclbuysliw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yclbuysliw p { margin: 0; padding: 0; }
 #yclbuysliw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yclbuysliw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yclbuysliw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yclbuysliw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yclbuysliw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yclbuysliw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yclbuysliw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yclbuysliw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yclbuysliw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yclbuysliw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yclbuysliw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yclbuysliw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yclbuysliw .gt_spanner_row { border-bottom-style: hidden; }
 #yclbuysliw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yclbuysliw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yclbuysliw .gt_from_md> :first-child { margin-top: 0; }
 #yclbuysliw .gt_from_md> :last-child { margin-bottom: 0; }
 #yclbuysliw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yclbuysliw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yclbuysliw .gt_indent_1 { text-indent: 5px; }
 #yclbuysliw .gt_indent_2 { text-indent: calc(5px * 2); }
 #yclbuysliw .gt_indent_3 { text-indent: calc(5px * 3); }
 #yclbuysliw .gt_indent_4 { text-indent: calc(5px * 4); }
 #yclbuysliw .gt_indent_5 { text-indent: calc(5px * 5); }
 #yclbuysliw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yclbuysliw .gt_row_group_first td { border-top-width: 2px; }
 #yclbuysliw .gt_row_group_first th { border-top-width: 2px; }
 #yclbuysliw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yclbuysliw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yclbuysliw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yclbuysliw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yclbuysliw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yclbuysliw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yclbuysliw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yclbuysliw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yclbuysliw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yclbuysliw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yclbuysliw .gt_left { text-align: left; }
 #yclbuysliw .gt_center { text-align: center; }
 #yclbuysliw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yclbuysliw .gt_font_normal { font-weight: normal; }
 #yclbuysliw .gt_font_bold { font-weight: bold; }
 #yclbuysliw .gt_font_italic { font-style: italic; }
 #yclbuysliw .gt_super { font-size: 65%; }
 #yclbuysliw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yclbuysliw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yclbuysliw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yclbuysliw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yclbuysliw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yclbuysliw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading" style="background-color: yellow">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">None</td>
<td class="gt_row gt_right">5550.0</td>
</tr>
</tbody>
</table>


The `loc` module provides a complete vocabulary for addressing any part of your table. By combining location specifiers with column selectors, row filters, and Polars expressions, you can apply styles to exactly the right cells. For more details on styling itself, see [Styling the Table Body](styling-the-table-body.md) and [Styling the Whole Table](styling-the-whole-table.md).
