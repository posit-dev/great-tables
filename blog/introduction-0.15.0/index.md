# Great Tables `v0.15.0`: Flags, Icons, and Other Formatting Goodies

The development of Great Tables is really moving along these days. We just released version `0.15.0` and it adds quite a few nice things to the package. The features we'll highlight in this post are:

- adding flag icons with the new [fmt_flag()](../../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag) method
- peppering your table cells with Font Awesome icons via [fmt_icon()](../../reference/GT.fmt_icon.md#great_tables.GT.fmt_icon)
- support for displaying accounting notation with four number-based formatting methods

Let's look at each of these in turn!


## Using [fmt_flag()](../../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag) to incorporate country flag icons

When tables contain country-level data, having a more visual representation for a country can help the reader more quickly parse the table contents. The new [fmt_flag()](../../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag) method makes this easy to accomplish. You just need to have either [two-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or [three-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) in a column.

Here's an example where country flags, shown as simplified circular icons, can be added to a table with [fmt_flag()](../../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag):


``` python
from great_tables import GT
from great_tables.data import peeps
import polars as pl

peeps_mini = (
    pl.from_pandas(peeps)
    .filter(pl.col("dob").str.slice(offset=0, length=4) == "1988")
    .with_columns(name=pl.col("name_given") + " " + pl.col("name_family"))
    .fill_null(value="")
    .select(["country", "name", "address", "city", "state_prov", "postcode"])
)

(
    GT(peeps_mini)
    .tab_header(title="Our Contacts (Born in 1988)")
    .fmt_flag(columns="country")
    .opt_vertical_padding(scale=0.5)
    .cols_label(
        country="",
        name="Name",
        address="Address",
        city="City",
        state_prov="State/Prov.",
        postcode="Zip/Postcode",
    )
)
```


<style>
#lsexdprsnh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lsexdprsnh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lsexdprsnh p { margin: 0; padding: 0; }
 #lsexdprsnh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lsexdprsnh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lsexdprsnh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lsexdprsnh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lsexdprsnh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lsexdprsnh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lsexdprsnh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lsexdprsnh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lsexdprsnh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lsexdprsnh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lsexdprsnh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lsexdprsnh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lsexdprsnh .gt_spanner_row { border-bottom-style: hidden; }
 #lsexdprsnh .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lsexdprsnh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lsexdprsnh .gt_from_md> :first-child { margin-top: 0; }
 #lsexdprsnh .gt_from_md> :last-child { margin-bottom: 0; }
 #lsexdprsnh .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lsexdprsnh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lsexdprsnh .gt_indent_1 { text-indent: 5px; }
 #lsexdprsnh .gt_indent_2 { text-indent: calc(5px * 2); }
 #lsexdprsnh .gt_indent_3 { text-indent: calc(5px * 3); }
 #lsexdprsnh .gt_indent_4 { text-indent: calc(5px * 4); }
 #lsexdprsnh .gt_indent_5 { text-indent: calc(5px * 5); }
 #lsexdprsnh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lsexdprsnh .gt_row_group_first td { border-top-width: 2px; }
 #lsexdprsnh .gt_row_group_first th { border-top-width: 2px; }
 #lsexdprsnh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lsexdprsnh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lsexdprsnh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lsexdprsnh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lsexdprsnh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lsexdprsnh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lsexdprsnh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lsexdprsnh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lsexdprsnh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lsexdprsnh .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lsexdprsnh .gt_left { text-align: left; }
 #lsexdprsnh .gt_center { text-align: center; }
 #lsexdprsnh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lsexdprsnh .gt_font_normal { font-weight: normal; }
 #lsexdprsnh .gt_font_bold { font-weight: bold; }
 #lsexdprsnh .gt_font_italic { font-style: italic; }
 #lsexdprsnh .gt_super { font-size: 65%; }
 #lsexdprsnh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lsexdprsnh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lsexdprsnh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lsexdprsnh .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lsexdprsnh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lsexdprsnh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Our Contacts (Born in 1988)</th>
</tr>
<tr class="gt_col_headings">
<th id="country" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Name</th>
<th id="address" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Address</th>
<th id="city" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">City</th>
<th id="state_prov" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">State/Prov.</th>
<th id="postcode" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Zip/Postcode</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+VW5pdGVkIFN0YXRlczwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTI1NiAwaDI1NnY2NGwtMzIgMzIgMzIgMzJ2NjRsLTMyIDMyIDMyIDMydjY0bC0zMiAzMiAzMiAzMnY2NGwtMjU2IDMyTDAgNDQ4di02NGwzMi0zMi0zMi0zMnYtNjR6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0yMjQgNjRoMjg4djY0SDIyNFptMCAxMjhoMjg4djY0SDI1NlpNMCAzMjBoNTEydjY0SDBabTAgMTI4aDUxMnY2NEgwWiIgLz48cGF0aCBmaWxsPSIjMDA1MmI0IiBkPSJNMCAwaDI1NnYyNTZIMFoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0ibTE4NyAyNDMgNTctNDFoLTcwbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUg5M2w1NyA0MS0yMi02N3ptLTgxIDAgNTctNDFIMTJsNTcgNDEtMjItNjd6bTE2Mi04MSA1Ny00MWgtNzBsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDkzbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUgxMmw1NyA0MS0yMi02N1ptMTYyLTgyIDU3LTQxaC03MGw1NyA0MS0yMi02N1ptLTgxIDAgNTctNDFIOTNsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDEybDU3IDQxLTIyLTY3WiIgLz48L2c+PC9zdmc+" /></span></td>
<td class="gt_row gt_left">Martin Bartůněk</td>
<td class="gt_row gt_left">1850 Valley Lane</td>
<td class="gt_row gt_left">Austin</td>
<td class="gt_row gt_left">TX</td>
<td class="gt_row gt_left">78744</td>
</tr>
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2xvdmVuaWE8L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Im0wIDE2NyAyNTMuOC0xOS4zTDUxMiAxNjd2MTc4bC0yNTQuOSAzMi4zTDAgMzQ1eiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMCAwaDUxMnYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMzQ1aDUxMnYxNjdIMHoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTIyMi43IDE2N3YtNjYuOEg4OVYxNjdsNjcgODIuNnoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTg5IDE2N3YyMi4yYzAgNTEuMSA2Ni44IDY2LjggNjYuOCA2Ni44czY2LjgtMTUuNyA2Ni44LTY2LjhWMTY3bC0yMi4zIDIyLjItNDQuNS0zMy40LTQ0LjUgMzMuNHoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left">Feride Šijan</td>
<td class="gt_row gt_left">Tavcarjeva 58</td>
<td class="gt_row gt_left">Sodražica</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_left">1317</td>
</tr>
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2xvdmVuaWE8L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Im0wIDE2NyAyNTMuOC0xOS4zTDUxMiAxNjd2MTc4bC0yNTQuOSAzMi4zTDAgMzQ1eiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMCAwaDUxMnYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMzQ1aDUxMnYxNjdIMHoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTIyMi43IDE2N3YtNjYuOEg4OVYxNjdsNjcgODIuNnoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTg5IDE2N3YyMi4yYzAgNTEuMSA2Ni44IDY2LjggNjYuOCA2Ni44czY2LjgtMTUuNyA2Ni44LTY2LjhWMTY3bC0yMi4zIDIyLjItNDQuNS0zMy40LTQ0LjUgMzMuNHoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left">Vejsil Crevar</td>
<td class="gt_row gt_left">Gosposka ulica 60</td>
<td class="gt_row gt_left">Novo mesto</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_left">8501</td>
</tr>
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+Q2FuYWRhPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAwdjUxMmgxNDRsMTEyLTY0IDExMiA2NGgxNDRWMEgzNjhMMjU2IDY0IDE0NCAwWiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTQ0IDBoMjI0djUxMkgxNDRaIiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Im0zMDEgMjg5IDQ0LTIyLTIyLTExdi0yMmwtNDUgMjIgMjMtNDRoLTIzbC0yMi0zNC0yMiAzM2gtMjNsMjMgNDUtNDUtMjJ2MjJsLTIyIDExIDQ1IDIyLTEyIDIzaDQ1djMzaDIydi0zM2g0NXoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left">Matilda Bates</td>
<td class="gt_row gt_left">582 Islington Ave</td>
<td class="gt_row gt_left">Toronto</td>
<td class="gt_row gt_left">ON</td>
<td class="gt_row gt_left">M8V 3B6</td>
</tr>
</tbody>
</table>


This slice of the [peeps](../../reference/data.peeps.md#great_tables.data.peeps) dataset has country codes in their 3-letter form (i.e., `"USA"`, `"SVN"`, and `"CAN"`) within the `country` column. So long as they are correct, [fmt_flag()](../../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag) will perform the conversion to flag icons. Also, there's a little bit of interactivity here: when hovering over a flag, the country name will appear as a tooltip!

We have the power to display multiple flag icons within a single cell. To make this happen, the country codes need to be combined in a single string where each code is separated by a comma (e.g., `"US,DE,GB"`). Here's an example that uses a portion of the [films](../../reference/data.films.md#great_tables.data.films) dataset:


``` python
from great_tables import GT, google_font
from great_tables.data import films
import polars as pl

films_mini = (
    pl.from_pandas(films)
    .filter(pl.col("director") == "Michael Haneke")
    .with_columns(title=pl.col("title") + " (" + pl.col("year").cast(pl.String) + ")")
    .select(["title", "run_time", "countries_of_origin"])
)

(
    GT(films_mini)
    .fmt_flag(columns="countries_of_origin")
    .tab_header(title="In Competition Films by Michael Haneke")
    .opt_stylize()
    .tab_options(column_labels_hidden=True)
    .opt_table_font(font=google_font("PT Sans"))
)
```


<style>
@import url('https://fonts.googleapis.com/css2?family=PT+Sans&display=swap');
#qliawalres table {
          font-family: 'PT Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qliawalres thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qliawalres p { margin: 0; padding: 0; }
 #qliawalres .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qliawalres .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qliawalres .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qliawalres .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qliawalres .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qliawalres .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #qliawalres .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qliawalres .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qliawalres .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qliawalres .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qliawalres .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qliawalres .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qliawalres .gt_spanner_row { border-bottom-style: hidden; }
 #qliawalres .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qliawalres .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #qliawalres .gt_from_md> :first-child { margin-top: 0; }
 #qliawalres .gt_from_md> :last-child { margin-bottom: 0; }
 #qliawalres .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #qliawalres .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #qliawalres .gt_indent_1 { text-indent: 5px; }
 #qliawalres .gt_indent_2 { text-indent: calc(5px * 2); }
 #qliawalres .gt_indent_3 { text-indent: calc(5px * 3); }
 #qliawalres .gt_indent_4 { text-indent: calc(5px * 4); }
 #qliawalres .gt_indent_5 { text-indent: calc(5px * 5); }
 #qliawalres .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qliawalres .gt_row_group_first td { border-top-width: 2px; }
 #qliawalres .gt_row_group_first th { border-top-width: 2px; }
 #qliawalres .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qliawalres .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #qliawalres .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qliawalres .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qliawalres .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qliawalres .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qliawalres .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qliawalres .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qliawalres .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qliawalres .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qliawalres .gt_left { text-align: left; }
 #qliawalres .gt_center { text-align: center; }
 #qliawalres .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qliawalres .gt_font_normal { font-weight: normal; }
 #qliawalres .gt_font_bold { font-weight: bold; }
 #qliawalres .gt_font_italic { font-style: italic; }
 #qliawalres .gt_super { font-size: 65%; }
 #qliawalres .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qliawalres .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qliawalres .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qliawalres .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qliawalres .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qliawalres .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">In Competition Films by Michael Haneke</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Funny Games (1997)</td>
<td class="gt_row gt_left">1h 48m</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QXVzdHJpYTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MTY3bC0yMy4yIDg5LjdMNTEyIDM0NXYxNjdIMFYzNDVsMjkuNC04OUwwIDE2N3oiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMTY3aDUxMnYxNzhIMHoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Code Unknown (2000)</td>
<td class="gt_row gt_left gt_striped">1h 58m</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+RnJhbmNlPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTY3IDBoMTc4bDI1LjkgMjUyLjNMMzQ1IDUxMkgxNjdsLTI5LjgtMjUzLjR6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMTY3djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6IiAvPjwvZz48L3N2Zz4=" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QXVzdHJpYTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MTY3bC0yMy4yIDg5LjdMNTEyIDM0NXYxNjdIMFYzNDVsMjkuNC04OUwwIDE2N3oiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMTY3aDUxMnYxNzhIMHoiIC8+PC9nPjwvc3ZnPg==" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+Um9tYW5pYTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0iTTE2NyAwaDE3OGwyNS45IDI1Mi4zTDM0NSA1MTJIMTY3bC0yOS44LTI1My40eiIgLz48cGF0aCBmaWxsPSIjMDA1MmI0IiBkPSJNMCAwaDE2N3Y1MTJIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTM0NSAwaDE2N3Y1MTJIMzQ1eiIgLz48L2c+PC9zdmc+" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+R2VybWFueTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTAgMzQ1IDI1Ni43LTI1LjVMNTEyIDM0NXYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTAgMTY3IDI1NS0yMyAyNTcgMjN2MTc4SDB6IiAvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+" /></span></td>
</tr>
<tr>
<td class="gt_row gt_left">The Piano Teacher (2001)</td>
<td class="gt_row gt_left">2h 11m</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+RnJhbmNlPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTY3IDBoMTc4bDI1LjkgMjUyLjNMMzQ1IDUxMkgxNjdsLTI5LjgtMjUzLjR6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMTY3djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6IiAvPjwvZz48L3N2Zz4=" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QXVzdHJpYTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MTY3bC0yMy4yIDg5LjdMNTEyIDM0NXYxNjdIMFYzNDVsMjkuNC04OUwwIDE2N3oiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMTY3aDUxMnYxNzhIMHoiIC8+PC9nPjwvc3ZnPg==" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+R2VybWFueTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTAgMzQ1IDI1Ni43LTI1LjVMNTEyIDM0NXYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTAgMTY3IDI1NS0yMyAyNTcgMjN2MTc4SDB6IiAvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+" /></span></td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Caché (2005)</td>
<td class="gt_row gt_left gt_striped">1h 57m</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+RnJhbmNlPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTY3IDBoMTc4bDI1LjkgMjUyLjNMMzQ1IDUxMkgxNjdsLTI5LjgtMjUzLjR6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMTY3djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6IiAvPjwvZz48L3N2Zz4=" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QXVzdHJpYTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MTY3bC0yMy4yIDg5LjdMNTEyIDM0NXYxNjdIMFYzNDVsMjkuNC04OUwwIDE2N3oiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMTY3aDUxMnYxNzhIMHoiIC8+PC9nPjwvc3ZnPg==" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+R2VybWFueTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTAgMzQ1IDI1Ni43LTI1LjVMNTEyIDM0NXYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTAgMTY3IDI1NS0yMyAyNTcgMjN2MTc4SDB6IiAvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+SXRhbHk8L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0xNjcgMGgxNzhsMjUuOSAyNTIuM0wzNDUgNTEySDE2N2wtMjkuOC0yNTMuNHoiIC8+PHBhdGggZmlsbD0iIzZkYTU0NCIgZD0iTTAgMGgxNjd2NTEySDB6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0zNDUgMGgxNjd2NTEySDM0NXoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
</tr>
<tr>
<td class="gt_row gt_left">The White Ribbon (2009)</td>
<td class="gt_row gt_left">2h 24m</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+R2VybWFueTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTAgMzQ1IDI1Ni43LTI1LjVMNTEyIDM0NXYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTAgMTY3IDI1NS0yMyAyNTcgMjN2MTc4SDB6IiAvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QXVzdHJpYTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MTY3bC0yMy4yIDg5LjdMNTEyIDM0NXYxNjdIMFYzNDVsMjkuNC04OUwwIDE2N3oiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMTY3aDUxMnYxNzhIMHoiIC8+PC9nPjwvc3ZnPg==" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+RnJhbmNlPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTY3IDBoMTc4bDI1LjkgMjUyLjNMMzQ1IDUxMkgxNjdsLTI5LjgtMjUzLjR6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMTY3djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6IiAvPjwvZz48L3N2Zz4=" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+SXRhbHk8L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0xNjcgMGgxNzhsMjUuOSAyNTIuM0wzNDUgNTEySDE2N2wtMjkuOC0yNTMuNHoiIC8+PHBhdGggZmlsbD0iIzZkYTU0NCIgZD0iTTAgMGgxNjd2NTEySDB6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0zNDUgMGgxNjd2NTEySDM0NXoiIC8+PC9nPjwvc3ZnPg==" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+Q2FuYWRhPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAwdjUxMmgxNDRsMTEyLTY0IDExMiA2NGgxNDRWMEgzNjhMMjU2IDY0IDE0NCAwWiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTQ0IDBoMjI0djUxMkgxNDRaIiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Im0zMDEgMjg5IDQ0LTIyLTIyLTExdi0yMmwtNDUgMjIgMjMtNDRoLTIzbC0yMi0zNC0yMiAzM2gtMjNsMjMgNDUtNDUtMjJ2MjJsLTIyIDExIDQ1IDIyLTEyIDIzaDQ1djMzaDIydi0zM2g0NXoiIC8+PC9nPjwvc3ZnPg==" /></span></td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Amour (2012)</td>
<td class="gt_row gt_left gt_striped">2h 7m</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QXVzdHJpYTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MTY3bC0yMy4yIDg5LjdMNTEyIDM0NXYxNjdIMFYzNDVsMjkuNC04OUwwIDE2N3oiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMTY3aDUxMnYxNzhIMHoiIC8+PC9nPjwvc3ZnPg==" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+RnJhbmNlPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTY3IDBoMTc4bDI1LjkgMjUyLjNMMzQ1IDUxMkgxNjdsLTI5LjgtMjUzLjR6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMTY3djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6IiAvPjwvZz48L3N2Zz4=" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+R2VybWFueTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTAgMzQ1IDI1Ni43LTI1LjVMNTEyIDM0NXYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTAgMTY3IDI1NS0yMyAyNTcgMjN2MTc4SDB6IiAvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+" /></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Happy End (2017)</td>
<td class="gt_row gt_left">1h 47m</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+RnJhbmNlPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTY3IDBoMTc4bDI1LjkgMjUyLjNMMzQ1IDUxMkgxNjdsLTI5LjgtMjUzLjR6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMTY3djUxMkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6IiAvPjwvZz48L3N2Zz4=" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QXVzdHJpYTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MTY3bC0yMy4yIDg5LjdMNTEyIDM0NXYxNjdIMFYzNDVsMjkuNC04OUwwIDE2N3oiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMTY3aDUxMnYxNzhIMHoiIC8+PC9nPjwvc3ZnPg==" /> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+R2VybWFueTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTAgMzQ1IDI1Ni43LTI1LjVMNTEyIDM0NXYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTAgMTY3IDI1NS0yMyAyNTcgMjN2MTc4SDB6IiAvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+" /></span></td>
</tr>
</tbody>
</table>


The column `countries_of_origin` has these combined strings for each of the co-production films, where countries are arranged by decreasing level of contribution (e.g., `"FR,AT,RO,DE"` in the second row). The [fmt_flag()](../../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag) method parses these strings into a sequence of flag icons that are displayed in the order provided. Each of the flags is separated by a space character but you can always change that default separator with the `sep=` argument.


## Using [fmt_icon()](../../reference/GT.fmt_icon.md#great_tables.GT.fmt_icon) to include Font Awesome icons

The new [fmt_icon()](../../reference/GT.fmt_icon.md#great_tables.GT.fmt_icon) method gives you the ability to easily include Font Awesome icons in a table. It uses a similar input/output scheme as with [fmt_flag()](../../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag): provide the *short* icon name (e.g., `"table"`, `"music"`, `"globe"`, etc.) or a comma-separated list of them, and [fmt_icon()](../../reference/GT.fmt_icon.md#great_tables.GT.fmt_icon) will provide the Font Awesome icon in place. Let's see it in action with an example that uses the [metro](../../reference/data.metro.md#great_tables.data.metro) dataset:


``` python
from great_tables import GT
from great_tables.data import metro
import polars as pl

metro_mini = (
    pl.from_pandas(metro).tail(10)
    .with_columns(
        services = (
            pl.when(pl.col("connect_tramway").is_not_null())
            .then(pl.lit("train, train-tram"))
            .otherwise(pl.lit("train"))
        )
    )
    .select(["name", "services", "location"])
)

(
    GT(metro_mini)
    .tab_header("Services Available at Select Stations")
    .fmt_icon(columns="services", sep=" / ")
    .tab_options(column_labels_hidden=True)
    .opt_stylize(color="green")
    .opt_horizontal_padding(scale=3)
    .opt_align_table_header(align="left")
)
```


<style>
#zphfjougyn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zphfjougyn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zphfjougyn p { margin: 0; padding: 0; }
 #zphfjougyn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #027101; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #027101; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zphfjougyn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zphfjougyn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zphfjougyn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 15px; padding-right: 15px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zphfjougyn .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zphfjougyn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; }
 #zphfjougyn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #038901; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zphfjougyn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 15px; padding-right: 15px; overflow-x: hidden; }
 #zphfjougyn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zphfjougyn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zphfjougyn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zphfjougyn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zphfjougyn .gt_spanner_row { border-bottom-style: hidden; }
 #zphfjougyn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 15px; padding-right: 15px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #038901; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zphfjougyn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #038901; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; vertical-align: middle; }
 #zphfjougyn .gt_from_md> :first-child { margin-top: 0; }
 #zphfjougyn .gt_from_md> :last-child { margin-bottom: 0; }
 #zphfjougyn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 15px; padding-right: 15px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #CAFFAF; border-left-style: none; border-left-width: 1px; border-left-color: #CAFFAF; border-right-style: none; border-right-width: 1px; border-right-color: #CAFFAF; vertical-align: middle; overflow-x: hidden; }
 #zphfjougyn .gt_stub { color: #FFFFFF; background-color: #038901; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #038901; padding-left: 15px; padding-right: 15px; }
 #zphfjougyn .gt_indent_1 { text-indent: 5px; }
 #zphfjougyn .gt_indent_2 { text-indent: calc(5px * 2); }
 #zphfjougyn .gt_indent_3 { text-indent: calc(5px * 3); }
 #zphfjougyn .gt_indent_4 { text-indent: calc(5px * 4); }
 #zphfjougyn .gt_indent_5 { text-indent: calc(5px * 5); }
 #zphfjougyn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; vertical-align: top; }
 #zphfjougyn .gt_row_group_first td { border-top-width: 2px; }
 #zphfjougyn .gt_row_group_first th { border-top-width: 2px; }
 #zphfjougyn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zphfjougyn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #038901; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; }
 #zphfjougyn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zphfjougyn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zphfjougyn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zphfjougyn .gt_grand_summary_row { color: #333333; background-color: #CAFFAF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zphfjougyn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zphfjougyn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zphfjougyn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zphfjougyn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #zphfjougyn .gt_left { text-align: left; }
 #zphfjougyn .gt_center { text-align: center; }
 #zphfjougyn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zphfjougyn .gt_font_normal { font-weight: normal; }
 #zphfjougyn .gt_font_bold { font-weight: bold; }
 #zphfjougyn .gt_font_italic { font-style: italic; }
 #zphfjougyn .gt_super { font-size: 65%; }
 #zphfjougyn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zphfjougyn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zphfjougyn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zphfjougyn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #zphfjougyn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zphfjougyn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Services Available at Select Stations</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Porte de Vanves</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /> / <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik04Ni44IDQ4Yy0xMi4yIDAtMjMuNiA1LjUtMzEuMiAxNUw0Mi43IDc5QzM0LjUgODkuMyAxOS40IDkxIDkgODIuN1MtMyA1OS40IDUuMyA0OUwxOCAzM0MzNC43IDEyLjIgNjAgMCA4Ni44IDBIMzYxLjJjMjYuNyAwIDUyIDEyLjIgNjguNyAzM2wxMi44IDE2YzguMyAxMC40IDYuNiAyNS41LTMuNyAzMy43cy0yNS41IDYuNi0zMy43LTMuN0wzOTIuNSA2M2MtNy42LTkuNS0xOS4xLTE1LTMxLjItMTVIMjQ4Vjk2aDQwYzUzIDAgOTYgNDMgOTYgOTZWMzUyYzAgMzAuNi0xNC4zIDU3LjgtMzYuNiA3NS40bDY1LjUgNjUuNWM3LjEgNy4xIDIuMSAxOS4xLTcuOSAxOS4xSDM2NS4zYy04LjUgMC0xNi42LTMuNC0yMi42LTkuNEwyODggNDQ4SDE2MGwtNTQuNiA1NC42Yy02IDYtMTQuMSA5LjQtMjIuNiA5LjRINDNjLTEwIDAtMTUtMTIuMS03LjktMTkuMWw2NS41LTY1LjVDNzguMyA0MDkuOCA2NCAzODIuNiA2NCAzNTJWMTkyYzAtNTMgNDMtOTYgOTYtOTZoNDBWNDhIODYuOHpNMTYwIDE2MGMtMTcuNyAwLTMyIDE0LjMtMzIgMzJ2MzJjMCAxNy43IDE0LjMgMzIgMzIgMzJIMjg4YzE3LjcgMCAzMi0xNC4zIDMyLTMyVjE5MmMwLTE3LjctMTQuMy0zMi0zMi0zMkgxNjB6bTMyIDE5MmMwLTE3LjctMTQuMy0zMi0zMi0zMnMtMzIgMTQuMy0zMiAzMnMxNC4zIDMyIDMyIDMyczMyLTE0LjMgMzItMzJ6bTk2IDMyYzE3LjcgMCAzMi0xNC4zIDMyLTMycy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMyczE0LjMgMzIgMzIgMzJ6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left">Paris 14th</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Saint-Denis--Porte de Paris</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /> / <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik04Ni44IDQ4Yy0xMi4yIDAtMjMuNiA1LjUtMzEuMiAxNUw0Mi43IDc5QzM0LjUgODkuMyAxOS40IDkxIDkgODIuN1MtMyA1OS40IDUuMyA0OUwxOCAzM0MzNC43IDEyLjIgNjAgMCA4Ni44IDBIMzYxLjJjMjYuNyAwIDUyIDEyLjIgNjguNyAzM2wxMi44IDE2YzguMyAxMC40IDYuNiAyNS41LTMuNyAzMy43cy0yNS41IDYuNi0zMy43LTMuN0wzOTIuNSA2M2MtNy42LTkuNS0xOS4xLTE1LTMxLjItMTVIMjQ4Vjk2aDQwYzUzIDAgOTYgNDMgOTYgOTZWMzUyYzAgMzAuNi0xNC4zIDU3LjgtMzYuNiA3NS40bDY1LjUgNjUuNWM3LjEgNy4xIDIuMSAxOS4xLTcuOSAxOS4xSDM2NS4zYy04LjUgMC0xNi42LTMuNC0yMi42LTkuNEwyODggNDQ4SDE2MGwtNTQuNiA1NC42Yy02IDYtMTQuMSA5LjQtMjIuNiA5LjRINDNjLTEwIDAtMTUtMTIuMS03LjktMTkuMWw2NS41LTY1LjVDNzguMyA0MDkuOCA2NCAzODIuNiA2NCAzNTJWMTkyYzAtNTMgNDMtOTYgOTYtOTZoNDBWNDhIODYuOHpNMTYwIDE2MGMtMTcuNyAwLTMyIDE0LjMtMzIgMzJ2MzJjMCAxNy43IDE0LjMgMzIgMzIgMzJIMjg4YzE3LjcgMCAzMi0xNC4zIDMyLTMyVjE5MmMwLTE3LjctMTQuMy0zMi0zMi0zMkgxNjB6bTMyIDE5MmMwLTE3LjctMTQuMy0zMi0zMi0zMnMtMzIgMTQuMy0zMiAzMnMxNC4zIDMyIDMyIDMyczMyLTE0LjMgMzItMzJ6bTk2IDMyYzE3LjcgMCAzMi0xNC4zIDMyLTMycy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMyczE0LjMgMzIgMzIgMzJ6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left gt_striped">Saint-Denis</td>
</tr>
<tr>
<td class="gt_row gt_left">Saint-Denis--Université</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /> / <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik04Ni44IDQ4Yy0xMi4yIDAtMjMuNiA1LjUtMzEuMiAxNUw0Mi43IDc5QzM0LjUgODkuMyAxOS40IDkxIDkgODIuN1MtMyA1OS40IDUuMyA0OUwxOCAzM0MzNC43IDEyLjIgNjAgMCA4Ni44IDBIMzYxLjJjMjYuNyAwIDUyIDEyLjIgNjguNyAzM2wxMi44IDE2YzguMyAxMC40IDYuNiAyNS41LTMuNyAzMy43cy0yNS41IDYuNi0zMy43LTMuN0wzOTIuNSA2M2MtNy42LTkuNS0xOS4xLTE1LTMxLjItMTVIMjQ4Vjk2aDQwYzUzIDAgOTYgNDMgOTYgOTZWMzUyYzAgMzAuNi0xNC4zIDU3LjgtMzYuNiA3NS40bDY1LjUgNjUuNWM3LjEgNy4xIDIuMSAxOS4xLTcuOSAxOS4xSDM2NS4zYy04LjUgMC0xNi42LTMuNC0yMi42LTkuNEwyODggNDQ4SDE2MGwtNTQuNiA1NC42Yy02IDYtMTQuMSA5LjQtMjIuNiA5LjRINDNjLTEwIDAtMTUtMTIuMS03LjktMTkuMWw2NS41LTY1LjVDNzguMyA0MDkuOCA2NCAzODIuNiA2NCAzNTJWMTkyYzAtNTMgNDMtOTYgOTYtOTZoNDBWNDhIODYuOHpNMTYwIDE2MGMtMTcuNyAwLTMyIDE0LjMtMzIgMzJ2MzJjMCAxNy43IDE0LjMgMzIgMzIgMzJIMjg4YzE3LjcgMCAzMi0xNC4zIDMyLTMyVjE5MmMwLTE3LjctMTQuMy0zMi0zMi0zMkgxNjB6bTMyIDE5MmMwLTE3LjctMTQuMy0zMi0zMi0zMnMtMzIgMTQuMy0zMiAzMnMxNC4zIDMyIDMyIDMyczMyLTE0LjMgMzItMzJ6bTk2IDMyYzE3LjcgMCAzMi0xNC4zIDMyLTMycy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMyczE0LjMgMzIgMzIgMzJ6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left">Saint-Denis</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Saint-François-Xavier</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left gt_striped">Paris 7th</td>
</tr>
<tr>
<td class="gt_row gt_left">Varenne</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left">Paris 7th</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Bibliothèque François Mitterrand</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /> / <img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik04Ni44IDQ4Yy0xMi4yIDAtMjMuNiA1LjUtMzEuMiAxNUw0Mi43IDc5QzM0LjUgODkuMyAxOS40IDkxIDkgODIuN1MtMyA1OS40IDUuMyA0OUwxOCAzM0MzNC43IDEyLjIgNjAgMCA4Ni44IDBIMzYxLjJjMjYuNyAwIDUyIDEyLjIgNjguNyAzM2wxMi44IDE2YzguMyAxMC40IDYuNiAyNS41LTMuNyAzMy43cy0yNS41IDYuNi0zMy43LTMuN0wzOTIuNSA2M2MtNy42LTkuNS0xOS4xLTE1LTMxLjItMTVIMjQ4Vjk2aDQwYzUzIDAgOTYgNDMgOTYgOTZWMzUyYzAgMzAuNi0xNC4zIDU3LjgtMzYuNiA3NS40bDY1LjUgNjUuNWM3LjEgNy4xIDIuMSAxOS4xLTcuOSAxOS4xSDM2NS4zYy04LjUgMC0xNi42LTMuNC0yMi42LTkuNEwyODggNDQ4SDE2MGwtNTQuNiA1NC42Yy02IDYtMTQuMSA5LjQtMjIuNiA5LjRINDNjLTEwIDAtMTUtMTIuMS03LjktMTkuMWw2NS41LTY1LjVDNzguMyA0MDkuOCA2NCAzODIuNiA2NCAzNTJWMTkyYzAtNTMgNDMtOTYgOTYtOTZoNDBWNDhIODYuOHpNMTYwIDE2MGMtMTcuNyAwLTMyIDE0LjMtMzIgMzJ2MzJjMCAxNy43IDE0LjMgMzIgMzIgMzJIMjg4YzE3LjcgMCAzMi0xNC4zIDMyLTMyVjE5MmMwLTE3LjctMTQuMy0zMi0zMi0zMkgxNjB6bTMyIDE5MmMwLTE3LjctMTQuMy0zMi0zMi0zMnMtMzIgMTQuMy0zMiAzMnMxNC4zIDMyIDMyIDMyczMyLTE0LjMgMzItMzJ6bTk2IDMyYzE3LjcgMCAzMi0xNC4zIDMyLTMycy0xNC4zLTMyLTMyLTMycy0zMiAxNC4zLTMyIDMyczE0LjMgMzIgMzIgMzJ6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left gt_striped">Paris 13th</td>
</tr>
<tr>
<td class="gt_row gt_left">Cour Saint-Émilion</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left">Paris 12th</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Olympiades</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left gt_striped">Paris 13th</td>
</tr>
<tr>
<td class="gt_row gt_left">Pont Cardinet</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left">Paris 17th</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Saint-Ouen</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNDQ4IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC44OGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik05NiAwQzQzIDAgMCA0MyAwIDk2VjM1MmMwIDQ4IDM1LjIgODcuNyA4MS4xIDk0LjlsLTQ2IDQ2QzI4LjEgNDk5LjkgMzMuMSA1MTIgNDMgNTEySDgyLjdjOC41IDAgMTYuNi0zLjQgMjIuNi05LjRMMTYwIDQ0OEgyODhsNTQuNiA1NC42YzYgNiAxNC4xIDkuNCAyMi42IDkuNEg0MDVjMTAgMCAxNS0xMi4xIDcuOS0xOS4xbC00Ni00NmM0Ni03LjEgODEuMS00Ni45IDgxLjEtOTQuOVY5NmMwLTUzLTQzLTk2LTk2LTk2SDk2ek02NCA5NmMwLTE3LjcgMTQuMy0zMiAzMi0zMkgzNTJjMTcuNyAwIDMyIDE0LjMgMzIgMzJ2OTZjMCAxNy43LTE0LjMgMzItMzIgMzJIOTZjLTE3LjcgMC0zMi0xNC4zLTMyLTMyVjk2ek0yMjQgMzg0Yy0yNi41IDAtNDgtMjEuNS00OC00OHMyMS41LTQ4IDQ4LTQ4czQ4IDIxLjUgNDggNDhzLTIxLjUgNDgtNDggNDh6IiAvPjwvc3ZnPg==" class="fa" /></span></td>
<td class="gt_row gt_left gt_striped">Clichy, Saint-Ouen-sur-Seine</td>
</tr>
</tbody>
</table>


In the code, we added in the icon names `"train"` and `"train-tram"` to the `services` column, and there could either be just the train icon or the pair that includes the tramway service. We wanted a little separation between the icons in the latter case, so `sep=" / "` was used to place a slash with spacing between any pair of icons. The icons appear here with a black fill color, but that can be changed with the `fill_color=` argument (and there are several other arguments for controlling style attributes).

For a list of available icons, their names, and what they look like, check out [this listing on the Font Awesome website](https://fontawesome.com/search?m=free&o=r). The icons draw from the Font Awesome 'free' set (2000+ icons in total) but are not obtained via the web. Rather, we use the [faicons library](https://pypi.org/project/faicons/) so that this can be done entirely offline (directly using the SVG icons stored within faicons).


## Accounting notation in select numeric formatting methods

For certain types of tables, it may be preferable to use accounting notation for numerical figures. This type of notation renders negative values in parentheses while omitting the minus sign. This is often seen for monetary and percentage figures but it's also sensible for plain numbers in the right context. We've added support for accounting notation in four formatting methods:

- [fmt_number()](../../reference/GT.fmt_number.md#great_tables.GT.fmt_number)
- [fmt_integer()](../../reference/GT.fmt_integer.md#great_tables.GT.fmt_integer)
- [fmt_currency()](../../reference/GT.fmt_currency.md#great_tables.GT.fmt_currency)
- [fmt_percent()](../../reference/GT.fmt_percent.md#great_tables.GT.fmt_percent)

Here's a comprehensive example table that demonstrates how this type of formatting looks.


Show the code

``` python
from great_tables import GT
import polars as pl

df = pl.DataFrame({
    "number_type": ["negative", "positive"],
    "number": [-1.2, 23.6],
    "integer": [-2323, 23213],
    "currency": [-24334.23, 7323.253],
    "percent": [-0.0523, 0.363]
    }
).with_columns(
    number_acc = pl.col("number"),
    integer_acc = pl.col("integer"),
    currency_acc = pl.col("currency"),
    percent_acc = pl.col("percent")
)

(
    GT(df, rowname_col="number_type")
    .fmt_number(columns="number")
    .fmt_percent(columns="percent")
    .fmt_integer(columns="integer")
    .fmt_currency(columns="currency")
    .fmt_number(columns="number_acc", accounting=True)
    .fmt_percent(columns="percent_acc", accounting=True)
    .fmt_integer(columns="integer_acc", accounting=True)
    .fmt_currency(columns="currency_acc", accounting=True)
    .tab_spanner(label="default formatting", columns=[1, 2, 3, 4])
    .tab_spanner(label="with accounting notation", columns=[5, 6, 7, 8])
    .cols_label(
        number_acc="number",
        integer_acc="integer",
        currency_acc="currency",
        percent_acc="percent"
    )
)
```


<style>
#ilmnckgorl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ilmnckgorl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ilmnckgorl p { margin: 0; padding: 0; }
 #ilmnckgorl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ilmnckgorl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ilmnckgorl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ilmnckgorl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ilmnckgorl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ilmnckgorl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ilmnckgorl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ilmnckgorl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ilmnckgorl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ilmnckgorl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ilmnckgorl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ilmnckgorl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ilmnckgorl .gt_spanner_row { border-bottom-style: hidden; }
 #ilmnckgorl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ilmnckgorl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ilmnckgorl .gt_from_md> :first-child { margin-top: 0; }
 #ilmnckgorl .gt_from_md> :last-child { margin-bottom: 0; }
 #ilmnckgorl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ilmnckgorl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ilmnckgorl .gt_indent_1 { text-indent: 5px; }
 #ilmnckgorl .gt_indent_2 { text-indent: calc(5px * 2); }
 #ilmnckgorl .gt_indent_3 { text-indent: calc(5px * 3); }
 #ilmnckgorl .gt_indent_4 { text-indent: calc(5px * 4); }
 #ilmnckgorl .gt_indent_5 { text-indent: calc(5px * 5); }
 #ilmnckgorl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ilmnckgorl .gt_row_group_first td { border-top-width: 2px; }
 #ilmnckgorl .gt_row_group_first th { border-top-width: 2px; }
 #ilmnckgorl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ilmnckgorl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ilmnckgorl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ilmnckgorl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ilmnckgorl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ilmnckgorl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ilmnckgorl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ilmnckgorl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ilmnckgorl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ilmnckgorl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ilmnckgorl .gt_left { text-align: left; }
 #ilmnckgorl .gt_center { text-align: center; }
 #ilmnckgorl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ilmnckgorl .gt_font_normal { font-weight: normal; }
 #ilmnckgorl .gt_font_bold { font-weight: bold; }
 #ilmnckgorl .gt_font_italic { font-style: italic; }
 #ilmnckgorl .gt_super { font-size: 65%; }
 #ilmnckgorl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ilmnckgorl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ilmnckgorl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ilmnckgorl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ilmnckgorl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ilmnckgorl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th colspan="4" id="default-formatting" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">default formatting</th>
<th colspan="4" id="with-accounting-notation" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">with accounting notation</th>
</tr>
<tr class="gt_col_headings">
<th id="number" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">number</th>
<th id="integer" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">integer</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
<th id="percent" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">percent</th>
<th id="number_acc" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">number</th>
<th id="integer_acc" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">integer</th>
<th id="currency_acc" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
<th id="percent_acc" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">percent</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">negative</th>
<td class="gt_row gt_right">−1.20</td>
<td class="gt_row gt_right">−2,323</td>
<td class="gt_row gt_right">−$24,334.23</td>
<td class="gt_row gt_right">−5.23%</td>
<td class="gt_row gt_right">(1.20)</td>
<td class="gt_row gt_right">(2,323)</td>
<td class="gt_row gt_right">($24,334.23)</td>
<td class="gt_row gt_right">(5.23%)</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">positive</th>
<td class="gt_row gt_right">23.60</td>
<td class="gt_row gt_right">23,213</td>
<td class="gt_row gt_right">$7,323.25</td>
<td class="gt_row gt_right">36.30%</td>
<td class="gt_row gt_right">23.60</td>
<td class="gt_row gt_right">23,213</td>
<td class="gt_row gt_right">$7,323.25</td>
<td class="gt_row gt_right">36.30%</td>
</tr>
</tbody>
</table>


For the formatting in the final four columns, we use `accounting=True` to get the values into accounting notation. This is only apparent for the negative values (first row) as the positive values won't change their appearance, looking the same as they do when `accounting=False` (the default).


## Acknowledgements and how to contact us

We are *very* grateful for the work that [Jerry Wu](https://github.com/jrycw) has done during this release, some of which includes:

- enhancing the [fmt_image()](../../reference/GT.fmt_image.md#great_tables.GT.fmt_image) to support `http`/`https` schema in the `columns=` parameter, and writing an [incredible blog post](https://posit-dev.github.io/great-tables/blog/rendering-images/) about incorporating images in your tables
- improving the `save()` method, giving it the ability to perform intermediate saves (since the method returns itself)
- adding the [pipe()](../../reference/GT.pipe.md#great_tables.GT.pipe) method, which operates similarly to that of the Pandas and Polars APIs
- all sorts of little QoL fixes

We extend our gratitude also to [Alessandro Molina](https://github.com/amol-) for adding experimental support for `pyarrow.Table` inputs in this release.

Finally, we thank [Luke Manley](https://github.com/lukemanley) and [Guillaume Lemaitre](https://github.com/glemaitre) for their first contributions to the project!

We're always happy to get feedback. There are three good ways to talk to us:

1.  [GitHub Issues](https://github.com/posit-dev/great-tables/issues)
2.  [GitHub Discussions](https://github.com/posit-dev/great-tables/discussions)
3.  [Discord](https://discord.com/invite/Ux7nrcXHVV)

Don't be shy. We love talking tables (and how we can make them better)!
