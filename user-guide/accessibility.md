# Accessibility

Tables are read by people using screen readers and other assistive technology as well as by sighted readers. A screen reader announces a data cell together with its headers (e.g., "Germany, GDP, 4.1"), but it can only do that when the table's structure is marked up. **Great Tables** writes that markup into its HTML output for you, following the patterns in the W3C's [Tables Tutorial](https://www.w3.org/WAI/tutorials/tables/). This page describes what's covered, what isn't, and what you can do to make your tables easier for everyone to read.


# Row and column headers

Every header in a **Great Tables** table is a header cell (`<th>`) with a `scope` that says what it labels:

- column labels and spanners are column headers (`scope="col"`, or `"colgroup"` over several columns)
- stub cells (the row labels) are row headers (`scope="row"`)
- an outer level of a hierarchical stub that's merged across rows, and the row group label when `row_group_as_column=True`, head the group of rows they span (`scope="rowgroup"`)
- row group headings and summary row labels are headers too

In tables with spanners or a hierarchical stub, `scope` alone isn't enough to tell which headers apply to a cell, so every data cell also lists the ids of all of its headers in a `headers` attribute. Here's a table with all of these parts:


``` python
import polars as pl
from great_tables import GT
from great_tables.data import towny

towny_mini = (
    pl.from_pandas(towny)
    .filter(pl.col("csd_type").is_in(["city", "town"]))
    .sort("population_2021", descending=True)
    .group_by("csd_type", maintain_order=True)
    .head(3)
    .select("name", "csd_type", "population_1996", "population_2021")
)

gt_tbl = (
    GT(towny_mini, rowname_col="name", groupname_col="csd_type")
    .tab_header(title="Largest Cities and Towns in Ontario")
    .tab_spanner(label="Population", columns=["population_1996", "population_2021"])
    .cols_label(population_1996="1996", population_2021="2021")
    .fmt_integer(columns=["population_1996", "population_2021"])
)

gt_tbl
```


<style>
#pfxxdcplry table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pfxxdcplry thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pfxxdcplry p { margin: 0; padding: 0; }
 #pfxxdcplry .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pfxxdcplry .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pfxxdcplry .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pfxxdcplry .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pfxxdcplry .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pfxxdcplry .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfxxdcplry .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pfxxdcplry .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pfxxdcplry .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pfxxdcplry .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pfxxdcplry .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pfxxdcplry .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pfxxdcplry .gt_spanner_row { border-bottom-style: hidden; }
 #pfxxdcplry .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pfxxdcplry .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pfxxdcplry .gt_from_md> :first-child { margin-top: 0; }
 #pfxxdcplry .gt_from_md> :last-child { margin-bottom: 0; }
 #pfxxdcplry .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pfxxdcplry .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pfxxdcplry .gt_indent_1 { text-indent: 5px; }
 #pfxxdcplry .gt_indent_2 { text-indent: calc(5px * 2); }
 #pfxxdcplry .gt_indent_3 { text-indent: calc(5px * 3); }
 #pfxxdcplry .gt_indent_4 { text-indent: calc(5px * 4); }
 #pfxxdcplry .gt_indent_5 { text-indent: calc(5px * 5); }
 #pfxxdcplry .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pfxxdcplry .gt_row_group_first td { border-top-width: 2px; }
 #pfxxdcplry .gt_row_group_first th { border-top-width: 2px; }
 #pfxxdcplry .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pfxxdcplry .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfxxdcplry .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pfxxdcplry .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pfxxdcplry .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfxxdcplry .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pfxxdcplry .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pfxxdcplry .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pfxxdcplry .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfxxdcplry .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pfxxdcplry .gt_left { text-align: left; }
 #pfxxdcplry .gt_center { text-align: center; }
 #pfxxdcplry .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pfxxdcplry .gt_font_normal { font-weight: normal; }
 #pfxxdcplry .gt_font_bold { font-weight: bold; }
 #pfxxdcplry .gt_font_italic { font-style: italic; }
 #pfxxdcplry .gt_super { font-size: 65%; }
 #pfxxdcplry .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfxxdcplry .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pfxxdcplry .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfxxdcplry .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pfxxdcplry .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pfxxdcplry .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Largest Cities and Towns in Ontario</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th colspan="2" id="Population" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Population</th>
</tr>
<tr class="gt_col_headings">
<th id="population_1996" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1996</th>
<th id="population_2021" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2021</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="city" class="gt_group_heading" scope="colgroup">city</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Toronto</td>
<td class="gt_row gt_right" headers="city stub-1 Population population_1996">2,385,421</td>
<td class="gt_row gt_right" headers="city stub-1 Population population_2021">2,794,356</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Ottawa</td>
<td class="gt_row gt_right" headers="city stub-2 Population population_1996">721,136</td>
<td class="gt_row gt_right" headers="city stub-2 Population population_2021">1,017,449</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Mississauga</td>
<td class="gt_row gt_right" headers="city stub-3 Population population_1996">544,382</td>
<td class="gt_row gt_right" headers="city stub-3 Population population_2021">717,961</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="town" class="gt_group_heading" scope="colgroup">town</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Oakville</td>
<td class="gt_row gt_right" headers="town stub-4 Population population_1996">128,405</td>
<td class="gt_row gt_right" headers="town stub-4 Population population_2021">213,759</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Whitby</td>
<td class="gt_row gt_right" headers="town stub-5 Population population_1996">73,794</td>
<td class="gt_row gt_right" headers="town stub-5 Population population_2021">138,501</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Milton</td>
<td class="gt_row gt_right" headers="town stub-6 Population population_1996">32,104</td>
<td class="gt_row gt_right" headers="town stub-6 Population population_2021">132,979</td>
</tr>
</tbody>
</table>


The first data cell's `headers` attribute refers to the row group heading, the row label, the spanner and the column label above it:


``` python
import re

first_cell = re.search(r"<td headers=[^>]*>", gt_tbl.as_raw_html())
print(first_cell.group(0))
```


    <td headers="city stub-1 Population population_1996" class="gt_row gt_right">


There's nothing to set up for any of this. Placing identifying columns in the stub with `rowname_col=` (rather than leaving them as ordinary columns) is what makes them row headers, so do that whenever the first column says what a row is about.


# Naming the table

A table with a title, added with [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header), is named after it: `<table>` refers to the title with `aria-labelledby` (and to the subtitle with `aria-describedby`), so a screen reader announces the title when the reader reaches the table. That's another good reason to give tables a title, even when the surrounding text describes them.

If a page shows several tables, give each one an id with `GT(id=)`. Header ids are then prefixed by the table's id, which keeps them unique across all of the tables on the page.


# Color and contrast

When [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) fills cells with color, it also picks a text color (light or dark) that contrasts with each fill, using the APCA contrast algorithm by default (`contrast_algo="wcag"` switches to the WCAG 2 formula). Keep `autocolor_text=True` unless you're setting text colors yourself.

Color shouldn't be the only way a table conveys meaning, since some readers can't see it or can't tell certain colors apart. [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) keeps the values visible, so the color reinforces them rather than replacing them. When you highlight cells with [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style), pair the color with another cue such as bold text, and prefer palettes that work for color-blind readers, such as the viridis family:


``` python
from great_tables import style, loc

(
    gt_tbl
    .data_color(columns="population_2021", palette="cividis")
    .tab_style(
        style=style.text(weight="bold"),
        locations=loc.body(columns="population_2021", rows=pl.col("population_2021") > 500000),
    )
)
```


<style>
#cfpwdfsvqg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cfpwdfsvqg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cfpwdfsvqg p { margin: 0; padding: 0; }
 #cfpwdfsvqg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cfpwdfsvqg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cfpwdfsvqg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cfpwdfsvqg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cfpwdfsvqg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cfpwdfsvqg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cfpwdfsvqg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cfpwdfsvqg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cfpwdfsvqg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cfpwdfsvqg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cfpwdfsvqg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cfpwdfsvqg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cfpwdfsvqg .gt_spanner_row { border-bottom-style: hidden; }
 #cfpwdfsvqg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cfpwdfsvqg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cfpwdfsvqg .gt_from_md> :first-child { margin-top: 0; }
 #cfpwdfsvqg .gt_from_md> :last-child { margin-bottom: 0; }
 #cfpwdfsvqg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cfpwdfsvqg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cfpwdfsvqg .gt_indent_1 { text-indent: 5px; }
 #cfpwdfsvqg .gt_indent_2 { text-indent: calc(5px * 2); }
 #cfpwdfsvqg .gt_indent_3 { text-indent: calc(5px * 3); }
 #cfpwdfsvqg .gt_indent_4 { text-indent: calc(5px * 4); }
 #cfpwdfsvqg .gt_indent_5 { text-indent: calc(5px * 5); }
 #cfpwdfsvqg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cfpwdfsvqg .gt_row_group_first td { border-top-width: 2px; }
 #cfpwdfsvqg .gt_row_group_first th { border-top-width: 2px; }
 #cfpwdfsvqg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cfpwdfsvqg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cfpwdfsvqg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cfpwdfsvqg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cfpwdfsvqg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cfpwdfsvqg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cfpwdfsvqg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cfpwdfsvqg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cfpwdfsvqg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cfpwdfsvqg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cfpwdfsvqg .gt_left { text-align: left; }
 #cfpwdfsvqg .gt_center { text-align: center; }
 #cfpwdfsvqg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cfpwdfsvqg .gt_font_normal { font-weight: normal; }
 #cfpwdfsvqg .gt_font_bold { font-weight: bold; }
 #cfpwdfsvqg .gt_font_italic { font-style: italic; }
 #cfpwdfsvqg .gt_super { font-size: 65%; }
 #cfpwdfsvqg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cfpwdfsvqg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cfpwdfsvqg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cfpwdfsvqg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cfpwdfsvqg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cfpwdfsvqg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Largest Cities and Towns in Ontario</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th colspan="2" id="Population" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Population</th>
</tr>
<tr class="gt_col_headings">
<th id="population_1996" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1996</th>
<th id="population_2021" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2021</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" id="city" class="gt_group_heading" scope="colgroup">city</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Toronto</td>
<td class="gt_row gt_right" headers="city stub-1 Population population_1996">2,385,421</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ffea46; font-weight: bold" headers="city stub-1 Population population_2021">2,794,356</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Ottawa</td>
<td class="gt_row gt_right" headers="city stub-2 Population population_1996">721,136</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #575c6d; font-weight: bold" headers="city stub-2 Population population_2021">1,017,449</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Mississauga</td>
<td class="gt_row gt_right" headers="city stub-3 Population population_1996">544,382</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #38486b; font-weight: bold" headers="city stub-3 Population population_2021">717,961</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="town" class="gt_group_heading" scope="colgroup">town</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Oakville</td>
<td class="gt_row gt_right" headers="town stub-4 Population population_1996">128,405</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #002556" headers="town stub-4 Population population_2021">213,759</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Whitby</td>
<td class="gt_row gt_right" headers="town stub-5 Population population_1996">73,794</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #00204e" headers="town stub-5 Population population_2021">138,501</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Milton</td>
<td class="gt_row gt_right" headers="town stub-6 Population population_1996">32,104</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #00204d" headers="town stub-6 Population population_2021">132,979</td>
</tr>
</tbody>
</table>


# Images, icons, flags and nanoplots

Some cell contents are graphics, and these don't yet carry text alternatives:

- images from [fmt_image()](../reference/GT.fmt_image.md#great_tables.GT.fmt_image) have no alternative text (`alt`)
- nanoplots from [fmt_nanoplot()](../reference/GT.fmt_nanoplot.md#great_tables.GT.fmt_nanoplot) have no accessible name or description
- icons from [fmt_icon()](../reference/GT.fmt_icon.md#great_tables.GT.fmt_icon) and flags from [fmt_flag()](../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag) are hidden from assistive technology, so they're treated as decoration

Until they do, make sure the information they show is also in the table as text. Keep the country name beside a flag, a label beside an icon, and the values (or a summary like the latest value) beside a nanoplot.


# Other kinds of output

Everything above applies to the static HTML that **Great Tables** renders in notebooks, Quarto documents and web pages. Interactive tables made with `opt_interactive()` are built by a separate widget with its own markup. LaTeX output and images saved with [gtsave()](../reference/GT.gtsave.md#great_tables.GT.gtsave) have no equivalent markup, so when you place a table image in a document, describe the table in that image's alternative text or in the text around it.


# A short checklist

- Put the identifying column in the stub (`rowname_col=`), and group rows with `groupname_col=`
- Give the table a title with [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header)
- Use clear column labels and spanners, since they're read aloud with every cell
- Don't rely on color alone, and keep `autocolor_text=True` with [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color)
- Give tables an id (`GT(id=)`) when a page has more than one
- Pair images, icons, flags and nanoplots with text that carries the same information
