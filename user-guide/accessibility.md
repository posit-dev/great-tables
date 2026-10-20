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
#bxgbtmkoqr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bxgbtmkoqr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bxgbtmkoqr p { margin: 0; padding: 0; }
 #bxgbtmkoqr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bxgbtmkoqr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bxgbtmkoqr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bxgbtmkoqr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bxgbtmkoqr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bxgbtmkoqr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxgbtmkoqr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bxgbtmkoqr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bxgbtmkoqr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bxgbtmkoqr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bxgbtmkoqr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bxgbtmkoqr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bxgbtmkoqr .gt_spanner_row { border-bottom-style: hidden; }
 #bxgbtmkoqr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bxgbtmkoqr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bxgbtmkoqr .gt_from_md> :first-child { margin-top: 0; }
 #bxgbtmkoqr .gt_from_md> :last-child { margin-bottom: 0; }
 #bxgbtmkoqr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bxgbtmkoqr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bxgbtmkoqr .gt_indent_1 { text-indent: 5px; }
 #bxgbtmkoqr .gt_indent_2 { text-indent: calc(5px * 2); }
 #bxgbtmkoqr .gt_indent_3 { text-indent: calc(5px * 3); }
 #bxgbtmkoqr .gt_indent_4 { text-indent: calc(5px * 4); }
 #bxgbtmkoqr .gt_indent_5 { text-indent: calc(5px * 5); }
 #bxgbtmkoqr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bxgbtmkoqr .gt_row_group_first td { border-top-width: 2px; }
 #bxgbtmkoqr .gt_row_group_first th { border-top-width: 2px; }
 #bxgbtmkoqr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bxgbtmkoqr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxgbtmkoqr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bxgbtmkoqr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bxgbtmkoqr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxgbtmkoqr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bxgbtmkoqr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bxgbtmkoqr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bxgbtmkoqr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxgbtmkoqr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bxgbtmkoqr .gt_left { text-align: left; }
 #bxgbtmkoqr .gt_center { text-align: center; }
 #bxgbtmkoqr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bxgbtmkoqr .gt_font_normal { font-weight: normal; }
 #bxgbtmkoqr .gt_font_bold { font-weight: bold; }
 #bxgbtmkoqr .gt_font_italic { font-style: italic; }
 #bxgbtmkoqr .gt_super { font-size: 65%; }
 #bxgbtmkoqr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxgbtmkoqr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bxgbtmkoqr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxgbtmkoqr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bxgbtmkoqr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bxgbtmkoqr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xfxapokksm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xfxapokksm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xfxapokksm p { margin: 0; padding: 0; }
 #xfxapokksm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xfxapokksm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xfxapokksm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xfxapokksm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xfxapokksm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xfxapokksm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xfxapokksm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xfxapokksm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xfxapokksm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xfxapokksm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xfxapokksm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xfxapokksm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xfxapokksm .gt_spanner_row { border-bottom-style: hidden; }
 #xfxapokksm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xfxapokksm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xfxapokksm .gt_from_md> :first-child { margin-top: 0; }
 #xfxapokksm .gt_from_md> :last-child { margin-bottom: 0; }
 #xfxapokksm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xfxapokksm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xfxapokksm .gt_indent_1 { text-indent: 5px; }
 #xfxapokksm .gt_indent_2 { text-indent: calc(5px * 2); }
 #xfxapokksm .gt_indent_3 { text-indent: calc(5px * 3); }
 #xfxapokksm .gt_indent_4 { text-indent: calc(5px * 4); }
 #xfxapokksm .gt_indent_5 { text-indent: calc(5px * 5); }
 #xfxapokksm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xfxapokksm .gt_row_group_first td { border-top-width: 2px; }
 #xfxapokksm .gt_row_group_first th { border-top-width: 2px; }
 #xfxapokksm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xfxapokksm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xfxapokksm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xfxapokksm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xfxapokksm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xfxapokksm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xfxapokksm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xfxapokksm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xfxapokksm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xfxapokksm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xfxapokksm .gt_left { text-align: left; }
 #xfxapokksm .gt_center { text-align: center; }
 #xfxapokksm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xfxapokksm .gt_font_normal { font-weight: normal; }
 #xfxapokksm .gt_font_bold { font-weight: bold; }
 #xfxapokksm .gt_font_italic { font-style: italic; }
 #xfxapokksm .gt_super { font-size: 65%; }
 #xfxapokksm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xfxapokksm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xfxapokksm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xfxapokksm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xfxapokksm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xfxapokksm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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

Some cell contents are graphics, which screen readers can't see, so they need a text alternative:

- images from [fmt_image()](../reference/GT.fmt_image.md#great_tables.GT.fmt_image) are decorative (an empty `alt=""`) unless you give them alternative text with `alt=`, as a string (with `{x}` for each image's reference in the cell) or from a column with [from_column()](../reference/from_column.md#great_tables.from_column)
- nanoplots from [fmt_nanoplot()](../reference/GT.fmt_nanoplot.md#great_tables.GT.fmt_nanoplot) are described by a summary of their values (e.g., "Line plot of 8 values from 12.0 to 47.0, ending at 30.0"); use `alt=` to replace or extend it (`{x}` is the summary)
- flags from [fmt_flag()](../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag) are named after their country (with the default `use_title=True`)
- icons from [fmt_icon()](../reference/GT.fmt_icon.md#great_tables.GT.fmt_icon) are treated as decoration and hidden from assistive technology

Give images alternative text whenever they carry information, and keep a label beside any icon that means something, since the icon itself isn't announced.


``` python
from great_tables import from_column

flags_df = pl.DataFrame(
    {
        "flag": ["CA", "GB", "JP"],
        "trend": ["3,5,4,8,9", "6,5,5,4,3", "2,3,3,4,6"],
    }
)

(
    GT(flags_df)
    .fmt_flag(columns="flag")
    .fmt_nanoplot(columns="trend", alt="Trend: {x}")
)
```


<style>
#mvptiksiqk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mvptiksiqk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mvptiksiqk p { margin: 0; padding: 0; }
 #mvptiksiqk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mvptiksiqk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mvptiksiqk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mvptiksiqk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mvptiksiqk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mvptiksiqk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mvptiksiqk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mvptiksiqk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mvptiksiqk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mvptiksiqk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mvptiksiqk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mvptiksiqk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mvptiksiqk .gt_spanner_row { border-bottom-style: hidden; }
 #mvptiksiqk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mvptiksiqk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mvptiksiqk .gt_from_md> :first-child { margin-top: 0; }
 #mvptiksiqk .gt_from_md> :last-child { margin-bottom: 0; }
 #mvptiksiqk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mvptiksiqk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mvptiksiqk .gt_indent_1 { text-indent: 5px; }
 #mvptiksiqk .gt_indent_2 { text-indent: calc(5px * 2); }
 #mvptiksiqk .gt_indent_3 { text-indent: calc(5px * 3); }
 #mvptiksiqk .gt_indent_4 { text-indent: calc(5px * 4); }
 #mvptiksiqk .gt_indent_5 { text-indent: calc(5px * 5); }
 #mvptiksiqk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mvptiksiqk .gt_row_group_first td { border-top-width: 2px; }
 #mvptiksiqk .gt_row_group_first th { border-top-width: 2px; }
 #mvptiksiqk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mvptiksiqk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mvptiksiqk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mvptiksiqk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mvptiksiqk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mvptiksiqk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mvptiksiqk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mvptiksiqk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mvptiksiqk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mvptiksiqk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mvptiksiqk .gt_left { text-align: left; }
 #mvptiksiqk .gt_center { text-align: center; }
 #mvptiksiqk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mvptiksiqk .gt_font_normal { font-weight: normal; }
 #mvptiksiqk .gt_font_bold { font-weight: bold; }
 #mvptiksiqk .gt_font_italic { font-style: italic; }
 #mvptiksiqk .gt_super { font-size: 65%; }
 #mvptiksiqk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mvptiksiqk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mvptiksiqk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mvptiksiqk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mvptiksiqk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mvptiksiqk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="flag" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">flag</th>
<th id="trend" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">trend</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left" headers="flag"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iQ2FuYWRhIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPkNhbmFkYTwvdGl0bGU+PG1hc2sgaWQ9ImZsYWctMC1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjZmxhZy0wLWEpIj48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAwdjUxMmgxNDRsMTEyLTY0IDExMiA2NGgxNDRWMEgzNjhMMjU2IDY0IDE0NCAwWiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTQ0IDBoMjI0djUxMkgxNDRaIiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Im0zMDEgMjg5IDQ0LTIyLTIyLTExdi0yMmwtNDUgMjIgMjMtNDRoLTIzbC0yMi0zNC0yMiAzM2gtMjNsMjMgNDUtNDUtMjJ2MjJsLTIyIDExIDQ1IDIyLTEyIDIzaDQ1djMzaDIydi0zM2g0NXoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left" headers="trend"><div>
<img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZ3QtbmFub3Bsb3QtODg1NTRjMzEiIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iVHJlbmQ6IExpbmUgcGxvdCBvZiA1IHZhbHVlcyBmcm9tIDMuMDAgdG8gOS4wMCwgZW5kaW5nIGF0IDkuMDAiIHZpZXdib3g9IjAgMCAzNTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9InRyZW5kLTAtYXJlYV9wYXR0ZXJuXzQwNTRhMzg5IiB3aWR0aD0iOCIgaGVpZ2h0PSI4IiBwYXR0ZXJudW5pdHM9InVzZXJTcGFjZU9uVXNlIj48cGF0aCBjbGFzcz0icGF0dGVybi1saW5lIiBkPSJNIDAsOCBsIDgsLTggTSAtMSwxIGwgNCwtNCBNIDYsMTAgbCA0LC00IiBzdHJva2U9IiNGRjAwMDAiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIiAvPjwvcGF0dGVybj48L2RlZnM+PHN0eWxlPiAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLmd0LW5hbm9wbG90LTg4NTU0YzMxIC52ZXJ0LWxpbmU6aG92ZXIgcmVjdCB7IGZpbGw6ICM5MTFFQjQ7IGZpbGwtb3BhY2l0eTogNDAlOyBzdHJva2U6ICNGRkZGRkY2MDsgY29sb3I6IHJlZDsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnZlcnQtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgZmlsbDogIzIxMjQyNzsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgZmlsbDogIzIxMjQyNzsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnJlZi1saW5lOmhvdmVyIHJlY3QgeyBzdHJva2U6ICNGRkZGRkY2MDsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLmd0LW5hbm9wbG90LTg4NTU0YzMxIC5yZWYtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgZmlsbDogIzIxMjQyNzsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnktYXhpcy1saW5lOmhvdmVyIHJlY3QgeyBmaWxsOiAjRURFREVEOyBmaWxsLW9wYWNpdHk6IDYwJTsgc3Ryb2tlOiAjRkZGRkZGNjA7IGNvbG9yOiByZWQ7IH0gLmd0LW5hbm9wbG90LTg4NTU0YzMxIC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCwxMTUuMCAxMTIuNSw4MS42NjY2NjY2NjY2NjY2NyAxNzUuMCw5OC4zMzMzMzMzMzMzMzMzNCAyMzcuNSwzMS42NjY2NjY2NjY2NjY2NjQgMzAwLjAsMTUuMCAzMDAuMCwxMjUgNTAuMCwxMjUgWiIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJ1cmwoI3RyZW5kLTAtYXJlYV9wYXR0ZXJuXzQwNTRhMzg5KSIgZmlsbC1vcGFjaXR5PSIwLjciIC8+PHBhdGggZD0iTSA1MC4wLDExNS4wIEMgNzUuMCwxMTUuMCA4Ny41LDgxLjY2NjY2NjY2NjY2NjY3IDExMi41LDgxLjY2NjY2NjY2NjY2NjY3IEMgMTM3LjUsODEuNjY2NjY2NjY2NjY2NjcgMTUwLjAsOTguMzMzMzMzMzMzMzMzMzQgMTc1LjAsOTguMzMzMzMzMzMzMzMzMzQgQyAyMDAuMCw5OC4zMzMzMzMzMzMzMzMzNCAyMTIuNSwzMS42NjY2NjY2NjY2NjY2NjQgMjM3LjUsMzEuNjY2NjY2NjY2NjY2NjY0IEMgMjYyLjUsMzEuNjY2NjY2NjY2NjY2NjY0IDI3NS4wLDE1LjAgMzAwLjAsMTUuMCIgc3Ryb2tlPSIjNDY4MkI0IiBzdHJva2Utd2lkdGg9IjgiIGZpbGw9Im5vbmUiIC8+PGNpcmNsZSBjeD0iNTAuMCIgY3k9IjExNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjExMi41IiBjeT0iODEuNjY2NjY2NjY2NjY2NjciIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTc1LjAiIGN5PSI5OC4zMzMzMzMzMzMzMzMzNCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIyMzcuNSIgY3k9IjMxLjY2NjY2NjY2NjY2NjY2NCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIzMDAuMCIgY3k9IjE1LjAiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGcgY2xhc3M9InktYXhpcy1saW5lIj48cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iNjUiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjAiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjAiIHk9IjE5LjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjI1Ij45PC90ZXh0Pjx0ZXh0IHg9IjAiIHk9IjEyNi4wIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIyNSI+MzwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iNDAuMCIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iNjAuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjM8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjEwMi41IiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIxMjIuNSIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjU8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjE2NS4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIxODUuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjQ8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjIyNy41IiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIyNDcuNSIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjg8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjI5MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIzMTAuMCIgeT0iMjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjMwcHgiPjk8L3RleHQ+PC9nPjwvc3ZnPg==" class="gt-nanoplot-88554c31" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="flag"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iVW5pdGVkIEtpbmdkb20iIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+VW5pdGVkIEtpbmdkb208L3RpdGxlPjxtYXNrIGlkPSJmbGFnLTEtYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2ZsYWctMS1hKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0ibTAgMCA4IDIyLTggMjN2MjNsMzIgNTQtMzIgNTR2MzJsMzIgNDgtMzIgNDh2MzJsMzIgNTQtMzIgNTR2NjhsMjItOCAyMyA4aDIzbDU0LTMyIDU0IDMyaDMybDQ4LTMyIDQ4IDMyaDMybDU0LTMyIDU0IDMyaDY4bC04LTIyIDgtMjN2LTIzbC0zMi01NCAzMi01NHYtMzJsLTMyLTQ4IDMyLTQ4di0zMmwtMzItNTQgMzItNTRWMGwtMjIgOC0yMy04aC0yM2wtNTQgMzItNTQtMzJoLTMybC00OCAzMi00OC0zMmgtMzJsLTU0IDMyTDY4IDBIMHoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTMzNiAwdjEwOEw0NDQgMFptMTc2IDY4TDQwNCAxNzZoMTA4ek0wIDE3NmgxMDhMMCA2OFpNNjggMGwxMDggMTA4VjBabTEwOCA1MTJWNDA0TDY4IDUxMlpNMCA0NDRsMTA4LTEwOEgwWm01MTItMTA4SDQwNGwxMDggMTA4Wm0tNjggMTc2TDMzNiA0MDR2MTA4eiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAwdjQ1bDEzMSAxMzFoNDVMMCAwem0yMDggMHYyMDhIMHY5NmgyMDh2MjA4aDk2VjMwNGgyMDh2LTk2SDMwNFYwaC05NnptMjU5IDBMMzM2IDEzMXY0NUw1MTIgMGgtNDV6TTE3NiAzMzYgMCA1MTJoNDVsMTMxLTEzMXYtNDV6bTE2MCAwIDE3NiAxNzZ2LTQ1TDM4MSAzMzZoLTQ1eiIgLz48L2c+PC9zdmc+" /></span></td>
<td class="gt_row gt_left" headers="trend"><div>
<img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZ3QtbmFub3Bsb3QtODg1NTRjMzEiIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iVHJlbmQ6IExpbmUgcGxvdCBvZiA1IHZhbHVlcyBmcm9tIDMuMDAgdG8gNi4wMCwgZW5kaW5nIGF0IDMuMDAiIHZpZXdib3g9IjAgMCAzNTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9InRyZW5kLTEtYXJlYV9wYXR0ZXJuXzQwNTRhMzg5IiB3aWR0aD0iOCIgaGVpZ2h0PSI4IiBwYXR0ZXJudW5pdHM9InVzZXJTcGFjZU9uVXNlIj48cGF0aCBjbGFzcz0icGF0dGVybi1saW5lIiBkPSJNIDAsOCBsIDgsLTggTSAtMSwxIGwgNCwtNCBNIDYsMTAgbCA0LC00IiBzdHJva2U9IiNGRjAwMDAiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIiAvPjwvcGF0dGVybj48L2RlZnM+PHN0eWxlPiAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLmd0LW5hbm9wbG90LTg4NTU0YzMxIC52ZXJ0LWxpbmU6aG92ZXIgcmVjdCB7IGZpbGw6ICM5MTFFQjQ7IGZpbGwtb3BhY2l0eTogNDAlOyBzdHJva2U6ICNGRkZGRkY2MDsgY29sb3I6IHJlZDsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnZlcnQtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgZmlsbDogIzIxMjQyNzsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgZmlsbDogIzIxMjQyNzsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnJlZi1saW5lOmhvdmVyIHJlY3QgeyBzdHJva2U6ICNGRkZGRkY2MDsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLmd0LW5hbm9wbG90LTg4NTU0YzMxIC5yZWYtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgZmlsbDogIzIxMjQyNzsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnktYXhpcy1saW5lOmhvdmVyIHJlY3QgeyBmaWxsOiAjRURFREVEOyBmaWxsLW9wYWNpdHk6IDYwJTsgc3Ryb2tlOiAjRkZGRkZGNjA7IGNvbG9yOiByZWQ7IH0gLmd0LW5hbm9wbG90LTg4NTU0YzMxIC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCwxNS4wIDExMi41LDQ4LjMzMzMzMzMzMzMzMzMzNiAxNzUuMCw0OC4zMzMzMzMzMzMzMzMzMzYgMjM3LjUsODEuNjY2NjY2NjY2NjY2NjcgMzAwLjAsMTE1LjAgMzAwLjAsMTI1IDUwLjAsMTI1IFoiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMiIgZmlsbD0idXJsKCN0cmVuZC0xLWFyZWFfcGF0dGVybl80MDU0YTM4OSkiIGZpbGwtb3BhY2l0eT0iMC43IiAvPjxwYXRoIGQ9Ik0gNTAuMCwxNS4wIEMgNzUuMCwxNS4wIDg3LjUsNDguMzMzMzMzMzMzMzMzMzM2IDExMi41LDQ4LjMzMzMzMzMzMzMzMzMzNiBDIDEzNy41LDQ4LjMzMzMzMzMzMzMzMzMzNiAxNTAuMCw0OC4zMzMzMzMzMzMzMzMzMzYgMTc1LjAsNDguMzMzMzMzMzMzMzMzMzM2IEMgMjAwLjAsNDguMzMzMzMzMzMzMzMzMzM2IDIxMi41LDgxLjY2NjY2NjY2NjY2NjY3IDIzNy41LDgxLjY2NjY2NjY2NjY2NjY3IEMgMjYyLjUsODEuNjY2NjY2NjY2NjY2NjcgMjc1LjAsMTE1LjAgMzAwLjAsMTE1LjAiIHN0cm9rZT0iIzQ2ODJCNCIgc3Ryb2tlLXdpZHRoPSI4IiBmaWxsPSJub25lIiAvPjxjaXJjbGUgY3g9IjUwLjAiIGN5PSIxNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjExMi41IiBjeT0iNDguMzMzMzMzMzMzMzMzMzM2IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjE3NS4wIiBjeT0iNDguMzMzMzMzMzMzMzMzMzM2IiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjIzNy41IiBjeT0iODEuNjY2NjY2NjY2NjY2NjciIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMzAwLjAiIGN5PSIxMTUuMCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48ZyBjbGFzcz0ieS1heGlzLWxpbmUiPjxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSI2NSIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMCIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMCIgeT0iMTkuMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMjUiPjY8L3RleHQ+PHRleHQgeD0iMCIgeT0iMTI2LjAiIGZpbGw9InRyYW5zcGFyZW50IiBzdHJva2U9InRyYW5zcGFyZW50IiBmb250LXNpemU9IjI1Ij4zPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSI0MC4wIiB5PSIwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTMwIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjEyIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSI2MC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NjwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMTAyLjUiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjEyMi41IiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NTwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMTY1LjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjE4NS4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NTwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjI3LjUiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjI0Ny41IiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+NDwvdGV4dD48L2c+PGcgY2xhc3M9InZlcnQtbGluZSI+PHJlY3QgeD0iMjkwLjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjMxMC4wIiB5PSIyMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMzBweCI+MzwvdGV4dD48L2c+PC9zdmc+" class="gt-nanoplot-88554c31" />
</div></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="flag"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iSmFwYW4iIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+SmFwYW48L3RpdGxlPjxtYXNrIGlkPSJmbGFnLTItYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2ZsYWctMi1hKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMGg1MTJ2NTEySDB6IiAvPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMTExLjMiIGZpbGw9IiNkODAwMjciPjwvY2lyY2xlPjwvZz48L3N2Zz4=" /></span></td>
<td class="gt_row gt_left" headers="trend"><div>
<img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZ3QtbmFub3Bsb3QtODg1NTRjMzEiIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iVHJlbmQ6IExpbmUgcGxvdCBvZiA1IHZhbHVlcyBmcm9tIDIuMDAgdG8gNi4wMCwgZW5kaW5nIGF0IDYuMDAiIHZpZXdib3g9IjAgMCAzNTAgMTMwIiBzdHlsZT0iaGVpZ2h0OiAyZW07IG1hcmdpbi1sZWZ0OiBhdXRvOyBtYXJnaW4tcmlnaHQ6IGF1dG87IGZvbnQtc2l6ZTogaW5oZXJpdDsgb3ZlcmZsb3c6IHZpc2libGU7IHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7IHBvc2l0aW9uOnJlbGF0aXZlOyI+PGRlZnM+PHBhdHRlcm4gaWQ9InRyZW5kLTItYXJlYV9wYXR0ZXJuXzQwNTRhMzg5IiB3aWR0aD0iOCIgaGVpZ2h0PSI4IiBwYXR0ZXJudW5pdHM9InVzZXJTcGFjZU9uVXNlIj48cGF0aCBjbGFzcz0icGF0dGVybi1saW5lIiBkPSJNIDAsOCBsIDgsLTggTSAtMSwxIGwgNCwtNCBNIDYsMTAgbCA0LC00IiBzdHJva2U9IiNGRjAwMDAiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIiAvPjwvcGF0dGVybj48L2RlZnM+PHN0eWxlPiAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgdGV4dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsICdDYXNjYWRpYSBDb2RlJywgJ1NvdXJjZSBDb2RlIFBybycsIE1lbmxvLCBDb25zb2xhcywgJ0RlamFWdSBTYW5zIE1vbm8nLCBtb25vc3BhY2U7IHN0cm9rZS13aWR0aDogMC4xNWVtOyBwYWludC1vcmRlcjogc3Ryb2tlOyBzdHJva2UtbGluZWpvaW46IHJvdW5kOyBjdXJzb3I6IGRlZmF1bHQ7IH0gLmd0LW5hbm9wbG90LTg4NTU0YzMxIC52ZXJ0LWxpbmU6aG92ZXIgcmVjdCB7IGZpbGw6ICM5MTFFQjQ7IGZpbGwtb3BhY2l0eTogNDAlOyBzdHJva2U6ICNGRkZGRkY2MDsgY29sb3I6IHJlZDsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnZlcnQtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgZmlsbDogIzIxMjQyNzsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLmhvcml6b250YWwtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgZmlsbDogIzIxMjQyNzsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnJlZi1saW5lOmhvdmVyIHJlY3QgeyBzdHJva2U6ICNGRkZGRkY2MDsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnJlZi1saW5lOmhvdmVyIGxpbmUgeyBzdHJva2U6ICNGRjAwMDA7IH0gLmd0LW5hbm9wbG90LTg4NTU0YzMxIC5yZWYtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgZmlsbDogIzIxMjQyNzsgfSAuZ3QtbmFub3Bsb3QtODg1NTRjMzEgLnktYXhpcy1saW5lOmhvdmVyIHJlY3QgeyBmaWxsOiAjRURFREVEOyBmaWxsLW9wYWNpdHk6IDYwJTsgc3Ryb2tlOiAjRkZGRkZGNjA7IGNvbG9yOiByZWQ7IH0gLmd0LW5hbm9wbG90LTg4NTU0YzMxIC55LWF4aXMtbGluZTpob3ZlciB0ZXh0IHsgc3Ryb2tlOiB3aGl0ZTsgc3Ryb2tlLXdpZHRoOiAwLjIwZW07IGZpbGw6ICMxQTFDMUY7IH0gPC9zdHlsZT48cGF0aCBjbGFzcz0iYXJlYS1jbG9zZWQiIGQ9Ik0gNTAuMCwxMTUuMCAxMTIuNSw5MC4wIDE3NS4wLDkwLjAgMjM3LjUsNjUuMCAzMDAuMCwxNS4wIDMwMC4wLDEyNSA1MC4wLDEyNSBaIiBzdHJva2U9InRyYW5zcGFyZW50IiBzdHJva2Utd2lkdGg9IjIiIGZpbGw9InVybCgjdHJlbmQtMi1hcmVhX3BhdHRlcm5fNDA1NGEzODkpIiBmaWxsLW9wYWNpdHk9IjAuNyIgLz48cGF0aCBkPSJNIDUwLjAsMTE1LjAgQyA3NS4wLDExNS4wIDg3LjUsOTAuMCAxMTIuNSw5MC4wIEMgMTM3LjUsOTAuMCAxNTAuMCw5MC4wIDE3NS4wLDkwLjAgQyAyMDAuMCw5MC4wIDIxMi41LDY1LjAgMjM3LjUsNjUuMCBDIDI2Mi41LDY1LjAgMjc1LjAsMTUuMCAzMDAuMCwxNS4wIiBzdHJva2U9IiM0NjgyQjQiIHN0cm9rZS13aWR0aD0iOCIgZmlsbD0ibm9uZSIgLz48Y2lyY2xlIGN4PSI1MC4wIiBjeT0iMTE1LjAiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTEyLjUiIGN5PSI5MC4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjE3NS4wIiBjeT0iOTAuMCIgcj0iMTAiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI0IiBmaWxsPSIjRkYwMDAwIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIyMzcuNSIgY3k9IjY1LjAiIHI9IjEwIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNCIgZmlsbD0iI0ZGMDAwMCI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMzAwLjAiIGN5PSIxNS4wIiByPSIxMCIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjQiIGZpbGw9IiNGRjAwMDAiPjwvY2lyY2xlPjxnIGNsYXNzPSJ5LWF4aXMtbGluZSI+PHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjY1IiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgLz48dGV4dCB4PSIwIiB5PSIxOS4wIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIyNSI+NjwvdGV4dD48dGV4dCB4PSIwIiB5PSIxMjYuMCIgZmlsbD0idHJhbnNwYXJlbnQiIHN0cm9rZT0idHJhbnNwYXJlbnQiIGZvbnQtc2l6ZT0iMjUiPjI8L3RleHQ+PC9nPjxnIGNsYXNzPSJ2ZXJ0LWxpbmUiPjxyZWN0IHg9IjQwLjAiIHk9IjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMzAiIHN0cm9rZT0idHJhbnNwYXJlbnQiIHN0cm9rZS13aWR0aD0iMTIiIGZpbGw9InRyYW5zcGFyZW50IiAvPjx0ZXh0IHg9IjYwLjAiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4yPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIxMDIuNSIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMTIyLjUiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4zPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIxNjUuMCIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMTg1LjAiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij4zPC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIyMjcuNSIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMjQ3LjUiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij40PC90ZXh0PjwvZz48ZyBjbGFzcz0idmVydC1saW5lIj48cmVjdCB4PSIyOTAuMCIgeT0iMCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEzMCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLXdpZHRoPSIxMiIgZmlsbD0idHJhbnNwYXJlbnQiIC8+PHRleHQgeD0iMzEwLjAiIHk9IjIwIiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlPSJ0cmFuc3BhcmVudCIgZm9udC1zaXplPSIzMHB4Ij42PC90ZXh0PjwvZz48L3N2Zz4=" class="gt-nanoplot-88554c31" />
</div></td>
</tr>
</tbody>
</table>


# Other kinds of output

Everything above applies to the static HTML that **Great Tables** renders in notebooks, Quarto documents and web pages. Interactive tables made with `opt_interactive()` are built by a separate widget with its own markup. LaTeX output and images saved with [gtsave()](../reference/GT.gtsave.md#great_tables.GT.gtsave) have no equivalent markup, so when you place a table image in a document, describe the table in that image's alternative text or in the text around it.


# A short checklist

- Put the identifying column in the stub (`rowname_col=`), and group rows with `groupname_col=`
- Give the table a title with [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header)
- Use clear column labels and spanners, since they're read aloud with every cell
- Don't rely on color alone, and keep `autocolor_text=True` with [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color)
- Give tables an id (`GT(id=)`) when a page has more than one
- Give informative images alternative text (`fmt_image(alt=)`), and pair icons with a text label
