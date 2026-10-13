# Location Selection

The `loc` module is what connects your styling intentions to specific parts of the table. Each location specifier identifies a region of the table (such as the header, body, stub, or footer) and many of them also support targeting specific columns or rows within that region. This page provides a comprehensive overview of all available location specifiers and how to use them effectively.

Understanding the `loc` module is valuable because it provides a single, consistent vocabulary for addressing any part of the table. Rather than learning separate APIs for styling the header vs. the body vs. the stub, you use the same `loc.*()` specifiers everywhere. This means that once you know how to style a column label, the pattern for styling a row group label or a source note is immediately familiar.


# Overview

Great Tables uses the `loc` module to specify locations for styling in [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style). Some location specifiers also allow selecting specific columns and rows of data.

For example, you might style a particular row name, group, column, or spanner label.

The table below shows the different location specifiers, along with the types of column or row selection they allow.


<style>
#degvcedyla table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#degvcedyla thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#degvcedyla p { margin: 0; padding: 0; }
 #degvcedyla .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #degvcedyla .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #degvcedyla .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #degvcedyla .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #degvcedyla .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #degvcedyla .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #degvcedyla .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #degvcedyla .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #degvcedyla .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #degvcedyla .gt_column_spanner_outer:first-child { padding-left: 0; }
 #degvcedyla .gt_column_spanner_outer:last-child { padding-right: 0; }
 #degvcedyla .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #degvcedyla .gt_spanner_row { border-bottom-style: hidden; }
 #degvcedyla .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #degvcedyla .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #degvcedyla .gt_from_md> :first-child { margin-top: 0; }
 #degvcedyla .gt_from_md> :last-child { margin-bottom: 0; }
 #degvcedyla .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #degvcedyla .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #degvcedyla .gt_indent_1 { text-indent: 5px; }
 #degvcedyla .gt_indent_2 { text-indent: calc(5px * 2); }
 #degvcedyla .gt_indent_3 { text-indent: calc(5px * 3); }
 #degvcedyla .gt_indent_4 { text-indent: calc(5px * 4); }
 #degvcedyla .gt_indent_5 { text-indent: calc(5px * 5); }
 #degvcedyla .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #degvcedyla .gt_row_group_first td { border-top-width: 2px; }
 #degvcedyla .gt_row_group_first th { border-top-width: 2px; }
 #degvcedyla .gt_striped { color: #333333; background-color: #F4F4F4; }
 #degvcedyla .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #degvcedyla .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #degvcedyla .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #degvcedyla .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #degvcedyla .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #degvcedyla .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #degvcedyla .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #degvcedyla .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #degvcedyla .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #degvcedyla .gt_left { text-align: left; }
 #degvcedyla .gt_center { text-align: center; }
 #degvcedyla .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #degvcedyla .gt_font_normal { font-weight: normal; }
 #degvcedyla .gt_font_bold { font-weight: bold; }
 #degvcedyla .gt_font_italic { font-style: italic; }
 #degvcedyla .gt_super { font-size: 65%; }
 #degvcedyla .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #degvcedyla .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #degvcedyla .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #degvcedyla .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #degvcedyla .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #degvcedyla .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vemizppxey table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vemizppxey thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vemizppxey p { margin: 0; padding: 0; }
 #vemizppxey .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vemizppxey .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vemizppxey .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vemizppxey .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vemizppxey .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vemizppxey .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vemizppxey .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vemizppxey .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vemizppxey .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vemizppxey .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vemizppxey .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vemizppxey .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vemizppxey .gt_spanner_row { border-bottom-style: hidden; }
 #vemizppxey .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vemizppxey .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vemizppxey .gt_from_md> :first-child { margin-top: 0; }
 #vemizppxey .gt_from_md> :last-child { margin-bottom: 0; }
 #vemizppxey .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vemizppxey .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vemizppxey .gt_indent_1 { text-indent: 5px; }
 #vemizppxey .gt_indent_2 { text-indent: calc(5px * 2); }
 #vemizppxey .gt_indent_3 { text-indent: calc(5px * 3); }
 #vemizppxey .gt_indent_4 { text-indent: calc(5px * 4); }
 #vemizppxey .gt_indent_5 { text-indent: calc(5px * 5); }
 #vemizppxey .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vemizppxey .gt_row_group_first td { border-top-width: 2px; }
 #vemizppxey .gt_row_group_first th { border-top-width: 2px; }
 #vemizppxey .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vemizppxey .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vemizppxey .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vemizppxey .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vemizppxey .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vemizppxey .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vemizppxey .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vemizppxey .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vemizppxey .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vemizppxey .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vemizppxey .gt_left { text-align: left; }
 #vemizppxey .gt_center { text-align: center; }
 #vemizppxey .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vemizppxey .gt_font_normal { font-weight: normal; }
 #vemizppxey .gt_font_bold { font-weight: bold; }
 #vemizppxey .gt_font_italic { font-style: italic; }
 #vemizppxey .gt_super { font-size: 65%; }
 #vemizppxey .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vemizppxey .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vemizppxey .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vemizppxey .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vemizppxey .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vemizppxey .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lblqjobggv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lblqjobggv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lblqjobggv p { margin: 0; padding: 0; }
 #lblqjobggv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lblqjobggv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lblqjobggv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lblqjobggv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lblqjobggv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lblqjobggv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lblqjobggv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lblqjobggv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lblqjobggv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lblqjobggv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lblqjobggv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lblqjobggv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lblqjobggv .gt_spanner_row { border-bottom-style: hidden; }
 #lblqjobggv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lblqjobggv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lblqjobggv .gt_from_md> :first-child { margin-top: 0; }
 #lblqjobggv .gt_from_md> :last-child { margin-bottom: 0; }
 #lblqjobggv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lblqjobggv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lblqjobggv .gt_indent_1 { text-indent: 5px; }
 #lblqjobggv .gt_indent_2 { text-indent: calc(5px * 2); }
 #lblqjobggv .gt_indent_3 { text-indent: calc(5px * 3); }
 #lblqjobggv .gt_indent_4 { text-indent: calc(5px * 4); }
 #lblqjobggv .gt_indent_5 { text-indent: calc(5px * 5); }
 #lblqjobggv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lblqjobggv .gt_row_group_first td { border-top-width: 2px; }
 #lblqjobggv .gt_row_group_first th { border-top-width: 2px; }
 #lblqjobggv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lblqjobggv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lblqjobggv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lblqjobggv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lblqjobggv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lblqjobggv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lblqjobggv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lblqjobggv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lblqjobggv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lblqjobggv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lblqjobggv .gt_left { text-align: left; }
 #lblqjobggv .gt_center { text-align: center; }
 #lblqjobggv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lblqjobggv .gt_font_normal { font-weight: normal; }
 #lblqjobggv .gt_font_bold { font-weight: bold; }
 #lblqjobggv .gt_font_italic { font-style: italic; }
 #lblqjobggv .gt_super { font-size: 65%; }
 #lblqjobggv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lblqjobggv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lblqjobggv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lblqjobggv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lblqjobggv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lblqjobggv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ecsflikrhi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ecsflikrhi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ecsflikrhi p { margin: 0; padding: 0; }
 #ecsflikrhi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ecsflikrhi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ecsflikrhi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ecsflikrhi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ecsflikrhi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ecsflikrhi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ecsflikrhi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ecsflikrhi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ecsflikrhi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ecsflikrhi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ecsflikrhi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ecsflikrhi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ecsflikrhi .gt_spanner_row { border-bottom-style: hidden; }
 #ecsflikrhi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ecsflikrhi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ecsflikrhi .gt_from_md> :first-child { margin-top: 0; }
 #ecsflikrhi .gt_from_md> :last-child { margin-bottom: 0; }
 #ecsflikrhi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ecsflikrhi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ecsflikrhi .gt_indent_1 { text-indent: 5px; }
 #ecsflikrhi .gt_indent_2 { text-indent: calc(5px * 2); }
 #ecsflikrhi .gt_indent_3 { text-indent: calc(5px * 3); }
 #ecsflikrhi .gt_indent_4 { text-indent: calc(5px * 4); }
 #ecsflikrhi .gt_indent_5 { text-indent: calc(5px * 5); }
 #ecsflikrhi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ecsflikrhi .gt_row_group_first td { border-top-width: 2px; }
 #ecsflikrhi .gt_row_group_first th { border-top-width: 2px; }
 #ecsflikrhi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ecsflikrhi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ecsflikrhi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ecsflikrhi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ecsflikrhi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ecsflikrhi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ecsflikrhi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ecsflikrhi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ecsflikrhi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ecsflikrhi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ecsflikrhi .gt_left { text-align: left; }
 #ecsflikrhi .gt_center { text-align: center; }
 #ecsflikrhi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ecsflikrhi .gt_font_normal { font-weight: normal; }
 #ecsflikrhi .gt_font_bold { font-weight: bold; }
 #ecsflikrhi .gt_font_italic { font-style: italic; }
 #ecsflikrhi .gt_super { font-size: 65%; }
 #ecsflikrhi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ecsflikrhi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ecsflikrhi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ecsflikrhi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ecsflikrhi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ecsflikrhi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ktljkidivb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ktljkidivb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ktljkidivb p { margin: 0; padding: 0; }
 #ktljkidivb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ktljkidivb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ktljkidivb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ktljkidivb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ktljkidivb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ktljkidivb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ktljkidivb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ktljkidivb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ktljkidivb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ktljkidivb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ktljkidivb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ktljkidivb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ktljkidivb .gt_spanner_row { border-bottom-style: hidden; }
 #ktljkidivb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ktljkidivb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ktljkidivb .gt_from_md> :first-child { margin-top: 0; }
 #ktljkidivb .gt_from_md> :last-child { margin-bottom: 0; }
 #ktljkidivb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ktljkidivb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ktljkidivb .gt_indent_1 { text-indent: 5px; }
 #ktljkidivb .gt_indent_2 { text-indent: calc(5px * 2); }
 #ktljkidivb .gt_indent_3 { text-indent: calc(5px * 3); }
 #ktljkidivb .gt_indent_4 { text-indent: calc(5px * 4); }
 #ktljkidivb .gt_indent_5 { text-indent: calc(5px * 5); }
 #ktljkidivb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ktljkidivb .gt_row_group_first td { border-top-width: 2px; }
 #ktljkidivb .gt_row_group_first th { border-top-width: 2px; }
 #ktljkidivb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ktljkidivb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ktljkidivb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ktljkidivb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ktljkidivb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ktljkidivb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ktljkidivb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ktljkidivb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ktljkidivb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ktljkidivb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ktljkidivb .gt_left { text-align: left; }
 #ktljkidivb .gt_center { text-align: center; }
 #ktljkidivb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ktljkidivb .gt_font_normal { font-weight: normal; }
 #ktljkidivb .gt_font_bold { font-weight: bold; }
 #ktljkidivb .gt_font_italic { font-style: italic; }
 #ktljkidivb .gt_super { font-size: 65%; }
 #ktljkidivb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ktljkidivb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ktljkidivb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ktljkidivb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ktljkidivb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ktljkidivb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#nkqkkpxhij table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nkqkkpxhij thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nkqkkpxhij p { margin: 0; padding: 0; }
 #nkqkkpxhij .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nkqkkpxhij .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nkqkkpxhij .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nkqkkpxhij .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nkqkkpxhij .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nkqkkpxhij .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nkqkkpxhij .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nkqkkpxhij .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nkqkkpxhij .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nkqkkpxhij .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nkqkkpxhij .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nkqkkpxhij .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nkqkkpxhij .gt_spanner_row { border-bottom-style: hidden; }
 #nkqkkpxhij .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nkqkkpxhij .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nkqkkpxhij .gt_from_md> :first-child { margin-top: 0; }
 #nkqkkpxhij .gt_from_md> :last-child { margin-bottom: 0; }
 #nkqkkpxhij .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nkqkkpxhij .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nkqkkpxhij .gt_indent_1 { text-indent: 5px; }
 #nkqkkpxhij .gt_indent_2 { text-indent: calc(5px * 2); }
 #nkqkkpxhij .gt_indent_3 { text-indent: calc(5px * 3); }
 #nkqkkpxhij .gt_indent_4 { text-indent: calc(5px * 4); }
 #nkqkkpxhij .gt_indent_5 { text-indent: calc(5px * 5); }
 #nkqkkpxhij .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nkqkkpxhij .gt_row_group_first td { border-top-width: 2px; }
 #nkqkkpxhij .gt_row_group_first th { border-top-width: 2px; }
 #nkqkkpxhij .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nkqkkpxhij .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nkqkkpxhij .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nkqkkpxhij .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nkqkkpxhij .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nkqkkpxhij .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nkqkkpxhij .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nkqkkpxhij .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nkqkkpxhij .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nkqkkpxhij .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nkqkkpxhij .gt_left { text-align: left; }
 #nkqkkpxhij .gt_center { text-align: center; }
 #nkqkkpxhij .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nkqkkpxhij .gt_font_normal { font-weight: normal; }
 #nkqkkpxhij .gt_font_bold { font-weight: bold; }
 #nkqkkpxhij .gt_font_italic { font-style: italic; }
 #nkqkkpxhij .gt_super { font-size: 65%; }
 #nkqkkpxhij .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nkqkkpxhij .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nkqkkpxhij .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nkqkkpxhij .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nkqkkpxhij .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nkqkkpxhij .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gzupjqqgft table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gzupjqqgft thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gzupjqqgft p { margin: 0; padding: 0; }
 #gzupjqqgft .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gzupjqqgft .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gzupjqqgft .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gzupjqqgft .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gzupjqqgft .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gzupjqqgft .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gzupjqqgft .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gzupjqqgft .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gzupjqqgft .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gzupjqqgft .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gzupjqqgft .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gzupjqqgft .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gzupjqqgft .gt_spanner_row { border-bottom-style: hidden; }
 #gzupjqqgft .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gzupjqqgft .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gzupjqqgft .gt_from_md> :first-child { margin-top: 0; }
 #gzupjqqgft .gt_from_md> :last-child { margin-bottom: 0; }
 #gzupjqqgft .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gzupjqqgft .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gzupjqqgft .gt_indent_1 { text-indent: 5px; }
 #gzupjqqgft .gt_indent_2 { text-indent: calc(5px * 2); }
 #gzupjqqgft .gt_indent_3 { text-indent: calc(5px * 3); }
 #gzupjqqgft .gt_indent_4 { text-indent: calc(5px * 4); }
 #gzupjqqgft .gt_indent_5 { text-indent: calc(5px * 5); }
 #gzupjqqgft .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gzupjqqgft .gt_row_group_first td { border-top-width: 2px; }
 #gzupjqqgft .gt_row_group_first th { border-top-width: 2px; }
 #gzupjqqgft .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gzupjqqgft .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gzupjqqgft .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gzupjqqgft .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gzupjqqgft .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gzupjqqgft .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gzupjqqgft .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gzupjqqgft .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gzupjqqgft .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gzupjqqgft .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gzupjqqgft .gt_left { text-align: left; }
 #gzupjqqgft .gt_center { text-align: center; }
 #gzupjqqgft .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gzupjqqgft .gt_font_normal { font-weight: normal; }
 #gzupjqqgft .gt_font_bold { font-weight: bold; }
 #gzupjqqgft .gt_font_italic { font-style: italic; }
 #gzupjqqgft .gt_super { font-size: 65%; }
 #gzupjqqgft .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gzupjqqgft .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gzupjqqgft .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gzupjqqgft .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gzupjqqgft .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gzupjqqgft .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="2" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow" scope="row">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow" scope="row">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow" scope="row">None</td>
<td class="gt_row gt_right">5550.0</td>
</tr>
</tbody>
</table>


All row labels in the stub are highlighted in yellow.


``` python
gt.tab_style(style.fill("yellow"), loc.stub("banana"))
```


<style>
#ceypjdhywc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ceypjdhywc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ceypjdhywc p { margin: 0; padding: 0; }
 #ceypjdhywc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ceypjdhywc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ceypjdhywc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ceypjdhywc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ceypjdhywc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ceypjdhywc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ceypjdhywc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ceypjdhywc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ceypjdhywc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ceypjdhywc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ceypjdhywc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ceypjdhywc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ceypjdhywc .gt_spanner_row { border-bottom-style: hidden; }
 #ceypjdhywc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ceypjdhywc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ceypjdhywc .gt_from_md> :first-child { margin-top: 0; }
 #ceypjdhywc .gt_from_md> :last-child { margin-bottom: 0; }
 #ceypjdhywc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ceypjdhywc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ceypjdhywc .gt_indent_1 { text-indent: 5px; }
 #ceypjdhywc .gt_indent_2 { text-indent: calc(5px * 2); }
 #ceypjdhywc .gt_indent_3 { text-indent: calc(5px * 3); }
 #ceypjdhywc .gt_indent_4 { text-indent: calc(5px * 4); }
 #ceypjdhywc .gt_indent_5 { text-indent: calc(5px * 5); }
 #ceypjdhywc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ceypjdhywc .gt_row_group_first td { border-top-width: 2px; }
 #ceypjdhywc .gt_row_group_first th { border-top-width: 2px; }
 #ceypjdhywc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ceypjdhywc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ceypjdhywc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ceypjdhywc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ceypjdhywc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ceypjdhywc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ceypjdhywc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ceypjdhywc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ceypjdhywc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ceypjdhywc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ceypjdhywc .gt_left { text-align: left; }
 #ceypjdhywc .gt_center { text-align: center; }
 #ceypjdhywc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ceypjdhywc .gt_font_normal { font-weight: normal; }
 #ceypjdhywc .gt_font_bold { font-weight: bold; }
 #ceypjdhywc .gt_font_italic { font-style: italic; }
 #ceypjdhywc .gt_super { font-size: 65%; }
 #ceypjdhywc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ceypjdhywc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ceypjdhywc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ceypjdhywc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ceypjdhywc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ceypjdhywc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="2" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow" scope="row">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">None</td>
<td class="gt_row gt_right">5550.0</td>
</tr>
</tbody>
</table>


Only the `"banana"` row label is styled, demonstrating name-based targeting.


``` python
gt.tab_style(style.fill("yellow"), loc.stub(["apricot", 2]))
```


<style>
#ycbhipnvuz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ycbhipnvuz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ycbhipnvuz p { margin: 0; padding: 0; }
 #ycbhipnvuz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ycbhipnvuz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ycbhipnvuz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ycbhipnvuz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ycbhipnvuz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ycbhipnvuz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ycbhipnvuz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ycbhipnvuz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ycbhipnvuz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ycbhipnvuz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ycbhipnvuz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ycbhipnvuz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ycbhipnvuz .gt_spanner_row { border-bottom-style: hidden; }
 #ycbhipnvuz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ycbhipnvuz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ycbhipnvuz .gt_from_md> :first-child { margin-top: 0; }
 #ycbhipnvuz .gt_from_md> :last-child { margin-bottom: 0; }
 #ycbhipnvuz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ycbhipnvuz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ycbhipnvuz .gt_indent_1 { text-indent: 5px; }
 #ycbhipnvuz .gt_indent_2 { text-indent: calc(5px * 2); }
 #ycbhipnvuz .gt_indent_3 { text-indent: calc(5px * 3); }
 #ycbhipnvuz .gt_indent_4 { text-indent: calc(5px * 4); }
 #ycbhipnvuz .gt_indent_5 { text-indent: calc(5px * 5); }
 #ycbhipnvuz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ycbhipnvuz .gt_row_group_first td { border-top-width: 2px; }
 #ycbhipnvuz .gt_row_group_first th { border-top-width: 2px; }
 #ycbhipnvuz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ycbhipnvuz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ycbhipnvuz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ycbhipnvuz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ycbhipnvuz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ycbhipnvuz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ycbhipnvuz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ycbhipnvuz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ycbhipnvuz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ycbhipnvuz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ycbhipnvuz .gt_left { text-align: left; }
 #ycbhipnvuz .gt_center { text-align: center; }
 #ycbhipnvuz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ycbhipnvuz .gt_font_normal { font-weight: normal; }
 #ycbhipnvuz .gt_font_bold { font-weight: bold; }
 #ycbhipnvuz .gt_font_italic { font-style: italic; }
 #ycbhipnvuz .gt_super { font-size: 65%; }
 #ycbhipnvuz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ycbhipnvuz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ycbhipnvuz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ycbhipnvuz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ycbhipnvuz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ycbhipnvuz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="2" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow" scope="row">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow" scope="row">None</td>
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
#etkrmoqvpb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#etkrmoqvpb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#etkrmoqvpb p { margin: 0; padding: 0; }
 #etkrmoqvpb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #etkrmoqvpb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #etkrmoqvpb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #etkrmoqvpb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #etkrmoqvpb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #etkrmoqvpb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #etkrmoqvpb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #etkrmoqvpb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #etkrmoqvpb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #etkrmoqvpb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #etkrmoqvpb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #etkrmoqvpb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #etkrmoqvpb .gt_spanner_row { border-bottom-style: hidden; }
 #etkrmoqvpb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #etkrmoqvpb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #etkrmoqvpb .gt_from_md> :first-child { margin-top: 0; }
 #etkrmoqvpb .gt_from_md> :last-child { margin-bottom: 0; }
 #etkrmoqvpb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #etkrmoqvpb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #etkrmoqvpb .gt_indent_1 { text-indent: 5px; }
 #etkrmoqvpb .gt_indent_2 { text-indent: calc(5px * 2); }
 #etkrmoqvpb .gt_indent_3 { text-indent: calc(5px * 3); }
 #etkrmoqvpb .gt_indent_4 { text-indent: calc(5px * 4); }
 #etkrmoqvpb .gt_indent_5 { text-indent: calc(5px * 5); }
 #etkrmoqvpb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #etkrmoqvpb .gt_row_group_first td { border-top-width: 2px; }
 #etkrmoqvpb .gt_row_group_first th { border-top-width: 2px; }
 #etkrmoqvpb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #etkrmoqvpb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #etkrmoqvpb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #etkrmoqvpb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #etkrmoqvpb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #etkrmoqvpb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #etkrmoqvpb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #etkrmoqvpb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #etkrmoqvpb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #etkrmoqvpb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #etkrmoqvpb .gt_left { text-align: left; }
 #etkrmoqvpb .gt_center { text-align: center; }
 #etkrmoqvpb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #etkrmoqvpb .gt_font_normal { font-weight: normal; }
 #etkrmoqvpb .gt_font_bold { font-weight: bold; }
 #etkrmoqvpb .gt_font_italic { font-style: italic; }
 #etkrmoqvpb .gt_super { font-size: 65%; }
 #etkrmoqvpb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #etkrmoqvpb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #etkrmoqvpb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #etkrmoqvpb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #etkrmoqvpb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #etkrmoqvpb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="2" class="gt_group_heading" scope="colgroup" style="background-color: yellow">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">None</td>
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
#uzcneotgdx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uzcneotgdx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uzcneotgdx p { margin: 0; padding: 0; }
 #uzcneotgdx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uzcneotgdx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uzcneotgdx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uzcneotgdx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uzcneotgdx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uzcneotgdx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uzcneotgdx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uzcneotgdx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uzcneotgdx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uzcneotgdx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uzcneotgdx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uzcneotgdx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uzcneotgdx .gt_spanner_row { border-bottom-style: hidden; }
 #uzcneotgdx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uzcneotgdx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uzcneotgdx .gt_from_md> :first-child { margin-top: 0; }
 #uzcneotgdx .gt_from_md> :last-child { margin-bottom: 0; }
 #uzcneotgdx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uzcneotgdx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uzcneotgdx .gt_indent_1 { text-indent: 5px; }
 #uzcneotgdx .gt_indent_2 { text-indent: calc(5px * 2); }
 #uzcneotgdx .gt_indent_3 { text-indent: calc(5px * 3); }
 #uzcneotgdx .gt_indent_4 { text-indent: calc(5px * 4); }
 #uzcneotgdx .gt_indent_5 { text-indent: calc(5px * 5); }
 #uzcneotgdx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uzcneotgdx .gt_row_group_first td { border-top-width: 2px; }
 #uzcneotgdx .gt_row_group_first th { border-top-width: 2px; }
 #uzcneotgdx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uzcneotgdx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uzcneotgdx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uzcneotgdx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uzcneotgdx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uzcneotgdx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uzcneotgdx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uzcneotgdx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uzcneotgdx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uzcneotgdx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uzcneotgdx .gt_left { text-align: left; }
 #uzcneotgdx .gt_center { text-align: center; }
 #uzcneotgdx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uzcneotgdx .gt_font_normal { font-weight: normal; }
 #uzcneotgdx .gt_font_bold { font-weight: bold; }
 #uzcneotgdx .gt_font_italic { font-style: italic; }
 #uzcneotgdx .gt_super { font-size: 65%; }
 #uzcneotgdx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uzcneotgdx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uzcneotgdx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uzcneotgdx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uzcneotgdx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uzcneotgdx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="2" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading" scope="colgroup" style="background-color: yellow">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">None</td>
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
#nthtxtegfu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nthtxtegfu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nthtxtegfu p { margin: 0; padding: 0; }
 #nthtxtegfu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nthtxtegfu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nthtxtegfu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nthtxtegfu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nthtxtegfu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nthtxtegfu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nthtxtegfu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nthtxtegfu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nthtxtegfu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nthtxtegfu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nthtxtegfu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nthtxtegfu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nthtxtegfu .gt_spanner_row { border-bottom-style: hidden; }
 #nthtxtegfu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nthtxtegfu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nthtxtegfu .gt_from_md> :first-child { margin-top: 0; }
 #nthtxtegfu .gt_from_md> :last-child { margin-bottom: 0; }
 #nthtxtegfu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nthtxtegfu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nthtxtegfu .gt_indent_1 { text-indent: 5px; }
 #nthtxtegfu .gt_indent_2 { text-indent: calc(5px * 2); }
 #nthtxtegfu .gt_indent_3 { text-indent: calc(5px * 3); }
 #nthtxtegfu .gt_indent_4 { text-indent: calc(5px * 4); }
 #nthtxtegfu .gt_indent_5 { text-indent: calc(5px * 5); }
 #nthtxtegfu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nthtxtegfu .gt_row_group_first td { border-top-width: 2px; }
 #nthtxtegfu .gt_row_group_first th { border-top-width: 2px; }
 #nthtxtegfu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nthtxtegfu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nthtxtegfu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nthtxtegfu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nthtxtegfu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nthtxtegfu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nthtxtegfu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nthtxtegfu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nthtxtegfu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nthtxtegfu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nthtxtegfu .gt_left { text-align: left; }
 #nthtxtegfu .gt_center { text-align: center; }
 #nthtxtegfu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nthtxtegfu .gt_font_normal { font-weight: normal; }
 #nthtxtegfu .gt_font_bold { font-weight: bold; }
 #nthtxtegfu .gt_font_italic { font-style: italic; }
 #nthtxtegfu .gt_super { font-size: 65%; }
 #nthtxtegfu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nthtxtegfu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nthtxtegfu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nthtxtegfu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nthtxtegfu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nthtxtegfu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="2" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">apricot</td>
<td class="gt_row gt_right">0.1111</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">banana</td>
<td class="gt_row gt_right">2.222</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading" scope="colgroup" style="background-color: yellow">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">None</td>
<td class="gt_row gt_right">5550.0</td>
</tr>
</tbody>
</table>


The `loc` module provides a complete vocabulary for addressing any part of your table. By combining location specifiers with column selectors, row filters, and Polars expressions, you can apply styles to exactly the right cells. For more details on styling itself, see [Styling the Table Body](styling-the-table-body.md) and [Styling the Whole Table](styling-the-whole-table.md).
