# Great Tables `v0.13.0`: Applying styles to all table locations

We did something in Great Tables (`0.13.0`) that'll make your tables that much more customizable: super *fine-grained* ways of setting styles throughout the table. Before you were largely constrained to styling through the following strategies:

1.  use a limited set of styles (e.g., background color, font weight, etc.) to different table locations like the stub, the column labels, etc., through [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options)
2.  use [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) with a larger set of styling options for the table body cells (specified by [loc.body()](../../reference/loc.body.md#great_tables.loc.body))

In `v0.13.0`, we can target much more than just the table body! Here is the expanded set of `loc.*()` methods along with the locations that they can target.

<img src="./GT-locations-map.png" class="img-fluid" />

This augmentation of the `loc` module to include all locations in the table means that there won't be a spot in the table to which you can't add styling. This is terrific because it gives you free rein to fully customize the look of your table.

Let's make a table and see how this new feature could be used.


## Starting things off with a big GT table

The table we'll make uses the [nuclides](../../reference/data.nuclides.md#great_tables.data.nuclides) dataset (available in the `great_tables.data` module). Through use of the `tab_*()` methods, quite a few table components (hence *locations*) will be added. We have hidden the code here because it is quite lengthy but you're encouraged to check it out to glean some interesting GT tricks.


Show the code

``` python
from great_tables import GT, md, style, loc, google_font
from great_tables.data import nuclides
import polars as pl
import polars.selectors as cs

nuclides_mini = (
    pl.from_pandas(nuclides)
    .filter(pl.col("element") == "C")
    .with_columns(pl.col("nuclide").str.replace(r"[0-9]+$", ""))
    .with_columns(mass_number=pl.col("z") + pl.col("n"))
    .with_columns(
        isotope=pl.concat_str(pl.col("element") + "-" + pl.col("mass_number").cast(pl.String))
    )
    .select(["isotope", "atomic_mass", "half_life", "isospin", "decay_1", "decay_2", "decay_3"])
)

gt_tbl = (
    GT(nuclides_mini, rowname_col="isotope")
    .tab_header(
        title="Isotopes of Carbon",
        subtitle="There are two stable isotopes of carbon and twelve that are unstable.",
    )
    .tab_spanner(label="Decay Mode", columns=cs.starts_with("decay"))
    .tab_source_note(md("Data obtained from the *nuclides* dataset."))
    .tab_stubhead(label="Isotope")
    .fmt_scientific(columns="half_life")
    .fmt_number(
        columns="atomic_mass",
        decimals=4,
        scale_by=1 / 1e6,
    )
    .sub_missing(columns="half_life", missing_text=md("**STABLE**"))
    .sub_missing(columns=cs.starts_with("decay"))
    .cols_label(
        atomic_mass="Atomic Mass",
        half_life="Half Life, s",
        isospin="Isospin",
        decay_1="1",
        decay_2="2",
        decay_3="3",
    )
    .cols_align(align="center", columns=[cs.starts_with("decay"), "isospin"])
    .opt_align_table_header(align="left")
    .opt_table_font(font=google_font(name="IBM Plex Sans"))
    .opt_vertical_padding(scale=0.5)
    .opt_horizontal_padding(scale=2)
)

gt_tbl
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#zebcmwzujy table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zebcmwzujy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zebcmwzujy p { margin: 0; padding: 0; }
 #zebcmwzujy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zebcmwzujy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zebcmwzujy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zebcmwzujy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zebcmwzujy .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zebcmwzujy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zebcmwzujy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zebcmwzujy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #zebcmwzujy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zebcmwzujy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zebcmwzujy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zebcmwzujy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zebcmwzujy .gt_spanner_row { border-bottom-style: hidden; }
 #zebcmwzujy .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zebcmwzujy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zebcmwzujy .gt_from_md> :first-child { margin-top: 0; }
 #zebcmwzujy .gt_from_md> :last-child { margin-bottom: 0; }
 #zebcmwzujy .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zebcmwzujy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #zebcmwzujy .gt_indent_1 { text-indent: 5px; }
 #zebcmwzujy .gt_indent_2 { text-indent: calc(5px * 2); }
 #zebcmwzujy .gt_indent_3 { text-indent: calc(5px * 3); }
 #zebcmwzujy .gt_indent_4 { text-indent: calc(5px * 4); }
 #zebcmwzujy .gt_indent_5 { text-indent: calc(5px * 5); }
 #zebcmwzujy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #zebcmwzujy .gt_row_group_first td { border-top-width: 2px; }
 #zebcmwzujy .gt_row_group_first th { border-top-width: 2px; }
 #zebcmwzujy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zebcmwzujy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zebcmwzujy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zebcmwzujy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zebcmwzujy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zebcmwzujy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zebcmwzujy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zebcmwzujy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zebcmwzujy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zebcmwzujy .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #zebcmwzujy .gt_left { text-align: left; }
 #zebcmwzujy .gt_center { text-align: center; }
 #zebcmwzujy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zebcmwzujy .gt_font_normal { font-weight: normal; }
 #zebcmwzujy .gt_font_bold { font-weight: bold; }
 #zebcmwzujy .gt_font_italic { font-style: italic; }
 #zebcmwzujy .gt_super { font-size: 65%; }
 #zebcmwzujy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zebcmwzujy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zebcmwzujy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zebcmwzujy .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #zebcmwzujy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zebcmwzujy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Decay Mode</th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">C-8</th>
<td class="gt_row gt_right">8.0376</td>
<td class="gt_row gt_right">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-9</th>
<td class="gt_row gt_right">9.0310</td>
<td class="gt_row gt_right">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-10</th>
<td class="gt_row gt_right">10.0169</td>
<td class="gt_row gt_right">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-11</th>
<td class="gt_row gt_right">11.0114</td>
<td class="gt_row gt_right">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-12</th>
<td class="gt_row gt_right">12.0000</td>
<td class="gt_row gt_right"><strong>STABLE</strong></td>
<td class="gt_row gt_center">0</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-13</th>
<td class="gt_row gt_right">13.0034</td>
<td class="gt_row gt_right"><strong>STABLE</strong></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-14</th>
<td class="gt_row gt_right">14.0032</td>
<td class="gt_row gt_right">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-15</th>
<td class="gt_row gt_right">15.0106</td>
<td class="gt_row gt_right">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-16</th>
<td class="gt_row gt_right">16.0147</td>
<td class="gt_row gt_right">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-17</th>
<td class="gt_row gt_right">17.0226</td>
<td class="gt_row gt_right">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-18</th>
<td class="gt_row gt_right">18.0268</td>
<td class="gt_row gt_right">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-19</th>
<td class="gt_row gt_right">19.0348</td>
<td class="gt_row gt_right">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-20</th>
<td class="gt_row gt_right">20.0403</td>
<td class="gt_row gt_right">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-22</th>
<td class="gt_row gt_right">22.0576</td>
<td class="gt_row gt_right">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>

</table>


This table will serve as a great starting point for demonstrating all the things you can now do with [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style). And the following checklist will serve as a rough plan for how we will style the table:

- use [loc.body()](../../reference/loc.body.md#great_tables.loc.body) to emphasize isotope half-life values
- employ [loc.stub()](../../reference/loc.stub.md#great_tables.loc.stub) to draw attention to isotope names (and also point out the 'STABLE' rows)
- use [style.css()](../../reference/style.css.md#great_tables.style.css) for creating custom CSS styles (e.g., to indent row labels for stable isotopes)
- work with composite locations and style the whole header and footer quite simply
- set the default table body fill with [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options)

Really this'll be [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) like you've never seen it before, so let's get on with it.


## Styling the body

First, we'll use [loc.body()](../../reference/loc.body.md#great_tables.loc.body) to emphasize half life values in two ways:

- Make the values in the `atomic_mass` and `half_life` use a monospace font.
- fill the background of isotopes with STABLE half lives to be PaleTurquoise.


``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body(columns=["atomic_mass", "half_life"])
    )
    .tab_style(
        style=[style.text(color="Navy"), style.fill(color="PaleTurquoise")],
        locations=loc.body(columns="half_life", rows=pl.col("half_life").is_not_null())
    )
)

gt_tbl
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#msypmkakry table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#msypmkakry thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#msypmkakry p { margin: 0; padding: 0; }
 #msypmkakry .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #msypmkakry .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #msypmkakry .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #msypmkakry .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #msypmkakry .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #msypmkakry .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #msypmkakry .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #msypmkakry .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #msypmkakry .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #msypmkakry .gt_column_spanner_outer:first-child { padding-left: 0; }
 #msypmkakry .gt_column_spanner_outer:last-child { padding-right: 0; }
 #msypmkakry .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #msypmkakry .gt_spanner_row { border-bottom-style: hidden; }
 #msypmkakry .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #msypmkakry .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #msypmkakry .gt_from_md> :first-child { margin-top: 0; }
 #msypmkakry .gt_from_md> :last-child { margin-bottom: 0; }
 #msypmkakry .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #msypmkakry .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #msypmkakry .gt_indent_1 { text-indent: 5px; }
 #msypmkakry .gt_indent_2 { text-indent: calc(5px * 2); }
 #msypmkakry .gt_indent_3 { text-indent: calc(5px * 3); }
 #msypmkakry .gt_indent_4 { text-indent: calc(5px * 4); }
 #msypmkakry .gt_indent_5 { text-indent: calc(5px * 5); }
 #msypmkakry .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #msypmkakry .gt_row_group_first td { border-top-width: 2px; }
 #msypmkakry .gt_row_group_first th { border-top-width: 2px; }
 #msypmkakry .gt_striped { color: #333333; background-color: #F4F4F4; }
 #msypmkakry .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #msypmkakry .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #msypmkakry .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #msypmkakry .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #msypmkakry .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #msypmkakry .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #msypmkakry .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #msypmkakry .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #msypmkakry .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #msypmkakry .gt_left { text-align: left; }
 #msypmkakry .gt_center { text-align: center; }
 #msypmkakry .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #msypmkakry .gt_font_normal { font-weight: normal; }
 #msypmkakry .gt_font_bold { font-weight: bold; }
 #msypmkakry .gt_font_italic { font-style: italic; }
 #msypmkakry .gt_super { font-size: 65%; }
 #msypmkakry .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #msypmkakry .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #msypmkakry .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #msypmkakry .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #msypmkakry .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #msypmkakry .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Decay Mode</th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">C-8</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-9</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-10</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-11</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-12</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono"><strong>STABLE</strong></td>
<td class="gt_row gt_center">0</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-13</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono"><strong>STABLE</strong></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-14</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-15</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-16</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-17</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-18</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-19</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-20</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">C-22</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>

</table>


Note these important pieces in the code:

- setting monospace font: we used [`google_font()`](../../reference/google_font.md) (added in the previous release) to apply the monospaced font IBM Plex Mono.
- filling unstable half lives to turquoise: because the half life cells with the value STABLE are actually missing in the underlying data, and filled in using [GT.sub_missing()](../../reference/GT.sub_missing.md#great_tables.GT.sub_missing), we used the polars expression `pl.col("half_life").is_not_null()` to target everything that isn't STABLE.

This is mainly a reminder that Polars expressions are quite something. And targeting cells in the body with `loc.body(rows=...)` can be powerful by extension.


## Don't forget the stub!

We mustn't forget the stub. It's a totally separate location, being off to the side and having the important responsibility of holding the row labels. Here, we are going to do two things:

1.  Change the fill color (to 'Linen') and make the text bold for the *entire stub*
2.  Highlight the rows where we have stable isotopes (the extent is both for the stub and the body cells)


``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=[style.fill(color="Linen"), style.text(weight="bold")],
        locations=loc.stub()
    )
    .tab_style(
        style=style.fill(color="LightCyan"),
        locations=[
            loc.body(rows=pl.col("half_life").is_null()),
            loc.stub(rows=pl.col("half_life").is_null())
        ]
    )
 )

gt_tbl
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#izprxykpta table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#izprxykpta thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#izprxykpta p { margin: 0; padding: 0; }
 #izprxykpta .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #izprxykpta .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #izprxykpta .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #izprxykpta .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #izprxykpta .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #izprxykpta .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izprxykpta .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #izprxykpta .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #izprxykpta .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #izprxykpta .gt_column_spanner_outer:first-child { padding-left: 0; }
 #izprxykpta .gt_column_spanner_outer:last-child { padding-right: 0; }
 #izprxykpta .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #izprxykpta .gt_spanner_row { border-bottom-style: hidden; }
 #izprxykpta .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #izprxykpta .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #izprxykpta .gt_from_md> :first-child { margin-top: 0; }
 #izprxykpta .gt_from_md> :last-child { margin-bottom: 0; }
 #izprxykpta .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #izprxykpta .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #izprxykpta .gt_indent_1 { text-indent: 5px; }
 #izprxykpta .gt_indent_2 { text-indent: calc(5px * 2); }
 #izprxykpta .gt_indent_3 { text-indent: calc(5px * 3); }
 #izprxykpta .gt_indent_4 { text-indent: calc(5px * 4); }
 #izprxykpta .gt_indent_5 { text-indent: calc(5px * 5); }
 #izprxykpta .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #izprxykpta .gt_row_group_first td { border-top-width: 2px; }
 #izprxykpta .gt_row_group_first th { border-top-width: 2px; }
 #izprxykpta .gt_striped { color: #333333; background-color: #F4F4F4; }
 #izprxykpta .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izprxykpta .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #izprxykpta .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #izprxykpta .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izprxykpta .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #izprxykpta .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #izprxykpta .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #izprxykpta .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izprxykpta .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #izprxykpta .gt_left { text-align: left; }
 #izprxykpta .gt_center { text-align: center; }
 #izprxykpta .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #izprxykpta .gt_font_normal { font-weight: normal; }
 #izprxykpta .gt_font_bold { font-weight: bold; }
 #izprxykpta .gt_font_italic { font-style: italic; }
 #izprxykpta .gt_super { font-size: 65%; }
 #izprxykpta .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izprxykpta .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #izprxykpta .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izprxykpta .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #izprxykpta .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #izprxykpta .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Decay Mode</th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-8</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-9</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-10</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-11</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan">C-12</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan">C-13</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-14</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-15</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-16</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-17</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-18</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-19</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-20</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-22</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>

</table>


For task \#1, a simple `.tab_style(..., locations=loc.stub())` targeted the entire stub.

Task \#2 is more interesting. Like [loc.body()](../../reference/loc.body.md#great_tables.loc.body), [loc.stub()](../../reference/loc.stub.md#great_tables.loc.stub) has a `rows=` argument that can target specific rows with Polars expressions. We used the same Polars expression as in the previous section to target those rows that belong to the stable isotopes.

We've dressed up the stub so that it is that much more prominent. And that linen-colored stub goes so well with the light-cyan rows, representative of carbon-12 and carbon-13!


## Using custom style rules with the new [style.css()](../../reference/style.css.md#great_tables.style.css)

Aside from decking out the `loc` module with all manner of location methods, we've added a little something to the [style](../../reference/style.borders.md#great_tables.style.borders.style) module: [style.css()](../../reference/style.css.md#great_tables.style.css)! What's it for? It lets you supply style declarations to its single `rule=` argument.

As an example, I might want to indent some text in one or more table cells. You can't really do that with the [style.text()](../../reference/style.text.md#great_tables.style.text) method since it doesn't have an `indent=` argument. So, in Great Tables `0.13.0` you can manually indent the row label text for the 'STABLE' rows using a CSS style rule:


``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=style.css(rule="text-indent: 4px;"),
        locations=loc.stub(rows=pl.col("half_life").is_null())
    )
)

gt_tbl
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#aoqqefmlzu table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aoqqefmlzu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aoqqefmlzu p { margin: 0; padding: 0; }
 #aoqqefmlzu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aoqqefmlzu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aoqqefmlzu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aoqqefmlzu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aoqqefmlzu .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aoqqefmlzu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aoqqefmlzu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aoqqefmlzu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #aoqqefmlzu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aoqqefmlzu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aoqqefmlzu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aoqqefmlzu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aoqqefmlzu .gt_spanner_row { border-bottom-style: hidden; }
 #aoqqefmlzu .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aoqqefmlzu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aoqqefmlzu .gt_from_md> :first-child { margin-top: 0; }
 #aoqqefmlzu .gt_from_md> :last-child { margin-bottom: 0; }
 #aoqqefmlzu .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aoqqefmlzu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #aoqqefmlzu .gt_indent_1 { text-indent: 5px; }
 #aoqqefmlzu .gt_indent_2 { text-indent: calc(5px * 2); }
 #aoqqefmlzu .gt_indent_3 { text-indent: calc(5px * 3); }
 #aoqqefmlzu .gt_indent_4 { text-indent: calc(5px * 4); }
 #aoqqefmlzu .gt_indent_5 { text-indent: calc(5px * 5); }
 #aoqqefmlzu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #aoqqefmlzu .gt_row_group_first td { border-top-width: 2px; }
 #aoqqefmlzu .gt_row_group_first th { border-top-width: 2px; }
 #aoqqefmlzu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aoqqefmlzu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aoqqefmlzu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aoqqefmlzu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aoqqefmlzu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aoqqefmlzu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aoqqefmlzu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aoqqefmlzu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aoqqefmlzu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aoqqefmlzu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #aoqqefmlzu .gt_left { text-align: left; }
 #aoqqefmlzu .gt_center { text-align: center; }
 #aoqqefmlzu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aoqqefmlzu .gt_font_normal { font-weight: normal; }
 #aoqqefmlzu .gt_font_bold { font-weight: bold; }
 #aoqqefmlzu .gt_font_italic { font-style: italic; }
 #aoqqefmlzu .gt_super { font-size: 65%; }
 #aoqqefmlzu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aoqqefmlzu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aoqqefmlzu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aoqqefmlzu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #aoqqefmlzu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aoqqefmlzu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Decay Mode</th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-8</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-9</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-10</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-11</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-14</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-15</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-16</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-17</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-18</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-19</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-20</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-22</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>

</table>


We targeted the cells in the stub that corresponded to the stable isotopes (carbon-12 and -13) with a Polars expression (same one as in the previous code cell) and now we have a 4px indentation of the 'C-12' and 'C-13' text! This new bonus functionality really allows almost any type of styling possible, provided you have those CSS skillz.


## The *combined* location helpers: [loc.column_header()](../../reference/loc.column_header.md#great_tables.loc.column_header) and [loc.footer()](../../reference/loc.footer.md#great_tables.loc.footer)

Look, I know we brought up the expression *fine-grained* before--right in the first paragraph--but sometimes you need just the opposite. There are lots of little locations in a GT table and some make for logical groupings. To that end, we have the concept of *combined* location helpers.

Let's set a grey background fill on the stubhead, column header, and footer:


``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=[style.text(v_align="middle"), style.fill(color="#EEEEEE")],
        locations=[loc.stubhead(), loc.column_header(), loc.footer()]
    )
)

gt_tbl
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#pxujoczbbb table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pxujoczbbb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pxujoczbbb p { margin: 0; padding: 0; }
 #pxujoczbbb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pxujoczbbb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pxujoczbbb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pxujoczbbb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pxujoczbbb .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pxujoczbbb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pxujoczbbb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pxujoczbbb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #pxujoczbbb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pxujoczbbb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pxujoczbbb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pxujoczbbb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pxujoczbbb .gt_spanner_row { border-bottom-style: hidden; }
 #pxujoczbbb .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pxujoczbbb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pxujoczbbb .gt_from_md> :first-child { margin-top: 0; }
 #pxujoczbbb .gt_from_md> :last-child { margin-bottom: 0; }
 #pxujoczbbb .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pxujoczbbb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #pxujoczbbb .gt_indent_1 { text-indent: 5px; }
 #pxujoczbbb .gt_indent_2 { text-indent: calc(5px * 2); }
 #pxujoczbbb .gt_indent_3 { text-indent: calc(5px * 3); }
 #pxujoczbbb .gt_indent_4 { text-indent: calc(5px * 4); }
 #pxujoczbbb .gt_indent_5 { text-indent: calc(5px * 5); }
 #pxujoczbbb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #pxujoczbbb .gt_row_group_first td { border-top-width: 2px; }
 #pxujoczbbb .gt_row_group_first th { border-top-width: 2px; }
 #pxujoczbbb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pxujoczbbb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pxujoczbbb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pxujoczbbb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pxujoczbbb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pxujoczbbb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pxujoczbbb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pxujoczbbb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pxujoczbbb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pxujoczbbb .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #pxujoczbbb .gt_left { text-align: left; }
 #pxujoczbbb .gt_center { text-align: center; }
 #pxujoczbbb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pxujoczbbb .gt_font_normal { font-weight: normal; }
 #pxujoczbbb .gt_font_bold { font-weight: bold; }
 #pxujoczbbb .gt_font_italic { font-style: italic; }
 #pxujoczbbb .gt_super { font-size: 65%; }
 #pxujoczbbb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pxujoczbbb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pxujoczbbb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pxujoczbbb .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #pxujoczbbb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pxujoczbbb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup">Decay Mode</th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-8</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-9</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-10</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-11</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-14</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-15</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-16</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-17</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-18</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-19</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-20</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-22</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>

</table>


The [`loc.column_header()`](../../reference/loc.column_header.md) location always targets both [loc.column_labels()](../../reference/loc.column_labels.md#great_tables.loc.column_labels) and [loc.spanner_labels()](../../reference/loc.spanner_labels.md#great_tables.loc.spanner_labels).

A good strategy for your tables would be to style with combined location helpers first and then drill into the specific cells of those super locations with more fine-grained styles in a later [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) call.


## Styling the title and the subtitle

Although it really doesn't appear to have separate locations, the table header (produced by way of [tab_header()](../../reference/GT.tab_header.md#great_tables.GT.tab_header)) can have two of them: the title and the subtitle (the latter is optional). These can be targeted via [loc.title()](../../reference/loc.title.md#great_tables.loc.title) and [loc.subtitle()](../../reference/loc.subtitle.md#great_tables.loc.subtitle). Let's focus in on the title location and set an aliceblue background fill on the title, along with some font and border adjustments.


``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=[
            style.text(size="24px"),
            style.fill(color="aliceblue"),
            style.borders(sides="bottom", color="#BFDFF6", weight="2px")
        ],
        locations=loc.title()
    )
)

gt_tbl
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#cdevfnsylf table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cdevfnsylf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cdevfnsylf p { margin: 0; padding: 0; }
 #cdevfnsylf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cdevfnsylf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cdevfnsylf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cdevfnsylf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cdevfnsylf .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cdevfnsylf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cdevfnsylf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cdevfnsylf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #cdevfnsylf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cdevfnsylf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cdevfnsylf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cdevfnsylf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cdevfnsylf .gt_spanner_row { border-bottom-style: hidden; }
 #cdevfnsylf .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cdevfnsylf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cdevfnsylf .gt_from_md> :first-child { margin-top: 0; }
 #cdevfnsylf .gt_from_md> :last-child { margin-bottom: 0; }
 #cdevfnsylf .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cdevfnsylf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #cdevfnsylf .gt_indent_1 { text-indent: 5px; }
 #cdevfnsylf .gt_indent_2 { text-indent: calc(5px * 2); }
 #cdevfnsylf .gt_indent_3 { text-indent: calc(5px * 3); }
 #cdevfnsylf .gt_indent_4 { text-indent: calc(5px * 4); }
 #cdevfnsylf .gt_indent_5 { text-indent: calc(5px * 5); }
 #cdevfnsylf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #cdevfnsylf .gt_row_group_first td { border-top-width: 2px; }
 #cdevfnsylf .gt_row_group_first th { border-top-width: 2px; }
 #cdevfnsylf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cdevfnsylf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cdevfnsylf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cdevfnsylf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cdevfnsylf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cdevfnsylf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cdevfnsylf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cdevfnsylf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cdevfnsylf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cdevfnsylf .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #cdevfnsylf .gt_left { text-align: left; }
 #cdevfnsylf .gt_center { text-align: center; }
 #cdevfnsylf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cdevfnsylf .gt_font_normal { font-weight: normal; }
 #cdevfnsylf .gt_font_bold { font-weight: bold; }
 #cdevfnsylf .gt_font_italic { font-style: italic; }
 #cdevfnsylf .gt_super { font-size: 65%; }
 #cdevfnsylf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cdevfnsylf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cdevfnsylf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cdevfnsylf .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #cdevfnsylf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cdevfnsylf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal" style="font-size: 24px; background-color: aliceblue; border-bottom: 2px solid #BFDFF6">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup">Decay Mode</th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-8</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-9</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-10</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-11</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-14</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-15</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-16</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-17</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-18</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-19</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-20</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-22</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>

</table>


Looks good. Notice that the title location is separate from the subtitle one, the background fill reveals the extent of its area.

A subtitle is an optional part of the header. We do have one in our table example, so let's style that as well. The [style.css()](../../reference/style.css.md#great_tables.style.css) method will be used to give the subtitle text some additional top and bottom padding, and, we'll put in a fancy background involving a linear gradient.


``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=style.css(rule="padding-top: 5px;"
            "padding-bottom: 5px;"
            "background-image: linear-gradient(120deg, #d4fc79 0%, #96f6a1 100%);"
        ),
        locations=loc.subtitle()
    )
)

gt_tbl
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#eyugrtnfwl table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eyugrtnfwl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eyugrtnfwl p { margin: 0; padding: 0; }
 #eyugrtnfwl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eyugrtnfwl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eyugrtnfwl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eyugrtnfwl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eyugrtnfwl .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eyugrtnfwl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyugrtnfwl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eyugrtnfwl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #eyugrtnfwl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eyugrtnfwl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eyugrtnfwl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eyugrtnfwl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eyugrtnfwl .gt_spanner_row { border-bottom-style: hidden; }
 #eyugrtnfwl .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eyugrtnfwl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eyugrtnfwl .gt_from_md> :first-child { margin-top: 0; }
 #eyugrtnfwl .gt_from_md> :last-child { margin-bottom: 0; }
 #eyugrtnfwl .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eyugrtnfwl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #eyugrtnfwl .gt_indent_1 { text-indent: 5px; }
 #eyugrtnfwl .gt_indent_2 { text-indent: calc(5px * 2); }
 #eyugrtnfwl .gt_indent_3 { text-indent: calc(5px * 3); }
 #eyugrtnfwl .gt_indent_4 { text-indent: calc(5px * 4); }
 #eyugrtnfwl .gt_indent_5 { text-indent: calc(5px * 5); }
 #eyugrtnfwl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #eyugrtnfwl .gt_row_group_first td { border-top-width: 2px; }
 #eyugrtnfwl .gt_row_group_first th { border-top-width: 2px; }
 #eyugrtnfwl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eyugrtnfwl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyugrtnfwl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eyugrtnfwl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eyugrtnfwl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyugrtnfwl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eyugrtnfwl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eyugrtnfwl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eyugrtnfwl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyugrtnfwl .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #eyugrtnfwl .gt_left { text-align: left; }
 #eyugrtnfwl .gt_center { text-align: center; }
 #eyugrtnfwl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eyugrtnfwl .gt_font_normal { font-weight: normal; }
 #eyugrtnfwl .gt_font_bold { font-weight: bold; }
 #eyugrtnfwl .gt_font_italic { font-style: italic; }
 #eyugrtnfwl .gt_super { font-size: 65%; }
 #eyugrtnfwl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyugrtnfwl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eyugrtnfwl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyugrtnfwl .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #eyugrtnfwl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eyugrtnfwl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal" style="font-size: 24px; background-color: aliceblue; border-bottom: 2px solid #BFDFF6">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="padding-top: 5px; padding-bottom: 5px; background-image: linear-gradient(120deg, #d4fc79 0%, #96f6a1 100%)">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup">Decay Mode</th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-8</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-9</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-10</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-11</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-14</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-15</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-16</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-17</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-18</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-19</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-20</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-22</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>

</table>


None of what was done above could be done prior to `v0.13.0`. The [style.css()](../../reference/style.css.md#great_tables.style.css) method makes this all possible.

The combined location helper for the title and the subtitle locations is [loc.header()](../../reference/loc.header.md#great_tables.loc.header). As mentioned before, it can be used as a shorthand for `locations=[loc.title(), loc_subtitle()]` and it's useful here where we want to change the font for the title and subtitle text.


``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=style.text(font=google_font("IBM Plex Serif")),
        locations=loc.header()
    )
)

gt_tbl
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Serif&display=swap');
#cpeslkchql table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cpeslkchql thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cpeslkchql p { margin: 0; padding: 0; }
 #cpeslkchql .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cpeslkchql .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cpeslkchql .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cpeslkchql .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cpeslkchql .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cpeslkchql .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cpeslkchql .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cpeslkchql .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #cpeslkchql .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cpeslkchql .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cpeslkchql .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cpeslkchql .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cpeslkchql .gt_spanner_row { border-bottom-style: hidden; }
 #cpeslkchql .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cpeslkchql .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cpeslkchql .gt_from_md> :first-child { margin-top: 0; }
 #cpeslkchql .gt_from_md> :last-child { margin-bottom: 0; }
 #cpeslkchql .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cpeslkchql .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #cpeslkchql .gt_indent_1 { text-indent: 5px; }
 #cpeslkchql .gt_indent_2 { text-indent: calc(5px * 2); }
 #cpeslkchql .gt_indent_3 { text-indent: calc(5px * 3); }
 #cpeslkchql .gt_indent_4 { text-indent: calc(5px * 4); }
 #cpeslkchql .gt_indent_5 { text-indent: calc(5px * 5); }
 #cpeslkchql .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #cpeslkchql .gt_row_group_first td { border-top-width: 2px; }
 #cpeslkchql .gt_row_group_first th { border-top-width: 2px; }
 #cpeslkchql .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cpeslkchql .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cpeslkchql .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cpeslkchql .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cpeslkchql .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cpeslkchql .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cpeslkchql .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cpeslkchql .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cpeslkchql .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cpeslkchql .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #cpeslkchql .gt_left { text-align: left; }
 #cpeslkchql .gt_center { text-align: center; }
 #cpeslkchql .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cpeslkchql .gt_font_normal { font-weight: normal; }
 #cpeslkchql .gt_font_bold { font-weight: bold; }
 #cpeslkchql .gt_font_italic { font-style: italic; }
 #cpeslkchql .gt_super { font-size: 65%; }
 #cpeslkchql .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cpeslkchql .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cpeslkchql .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cpeslkchql .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #cpeslkchql .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cpeslkchql .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal" style="font-family: IBM Plex Serif; font-size: 24px; background-color: aliceblue; border-bottom: 2px solid #BFDFF6">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="font-family: IBM Plex Serif; padding-top: 5px; padding-bottom: 5px; background-image: linear-gradient(120deg, #d4fc79 0%, #96f6a1 100%)">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup">Decay Mode</th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-8</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-9</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-10</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-11</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-14</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-15</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-16</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-17</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-18</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-19</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-20</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-22</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>

</table>


Though the order of things matters when setting styles via [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style), it's not a problem here to set a style for the combined 'header' location after doing so for the 'title' and 'subtitle' locations because the 'font' attribute *wasn't* set by [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) for those smaller locations.


## How [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) fits in with [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options)

When it comes to styling, you can use [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options) for some of the basics and use [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) for the more demanding styling tasks. And you could combine the usage of both in your table. Let's set a default honeydew background fill on the body values:


``` python
gt_tbl = gt_tbl.tab_options(table_background_color="HoneyDew")

gt_tbl
```


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Serif&display=swap');
#vfjzogzbvs table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vfjzogzbvs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vfjzogzbvs p { margin: 0; padding: 0; }
 #vfjzogzbvs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: HoneyDew; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vfjzogzbvs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vfjzogzbvs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: HoneyDew; border-bottom-width: 0; }
 #vfjzogzbvs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: HoneyDew; border-top-width: 0; }
 #vfjzogzbvs .gt_heading { background-color: HoneyDew; text-align: left; border-bottom-color: HoneyDew; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vfjzogzbvs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vfjzogzbvs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vfjzogzbvs .gt_col_heading { color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #vfjzogzbvs .gt_column_spanner_outer { color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vfjzogzbvs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vfjzogzbvs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vfjzogzbvs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vfjzogzbvs .gt_spanner_row { border-bottom-style: hidden; }
 #vfjzogzbvs .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vfjzogzbvs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vfjzogzbvs .gt_from_md> :first-child { margin-top: 0; }
 #vfjzogzbvs .gt_from_md> :last-child { margin-bottom: 0; }
 #vfjzogzbvs .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vfjzogzbvs .gt_stub { color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #vfjzogzbvs .gt_indent_1 { text-indent: 5px; }
 #vfjzogzbvs .gt_indent_2 { text-indent: calc(5px * 2); }
 #vfjzogzbvs .gt_indent_3 { text-indent: calc(5px * 3); }
 #vfjzogzbvs .gt_indent_4 { text-indent: calc(5px * 4); }
 #vfjzogzbvs .gt_indent_5 { text-indent: calc(5px * 5); }
 #vfjzogzbvs .gt_stub_row_group { color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #vfjzogzbvs .gt_row_group_first td { border-top-width: 2px; }
 #vfjzogzbvs .gt_row_group_first th { border-top-width: 2px; }
 #vfjzogzbvs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vfjzogzbvs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vfjzogzbvs .gt_summary_row { color: #333333; background-color: HoneyDew; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vfjzogzbvs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vfjzogzbvs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vfjzogzbvs .gt_grand_summary_row { color: #333333; background-color: HoneyDew; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vfjzogzbvs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vfjzogzbvs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vfjzogzbvs .gt_sourcenotes { color: #333333; background-color: HoneyDew; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vfjzogzbvs .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #vfjzogzbvs .gt_left { text-align: left; }
 #vfjzogzbvs .gt_center { text-align: center; }
 #vfjzogzbvs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vfjzogzbvs .gt_font_normal { font-weight: normal; }
 #vfjzogzbvs .gt_font_bold { font-weight: bold; }
 #vfjzogzbvs .gt_font_italic { font-style: italic; }
 #vfjzogzbvs .gt_super { font-size: 65%; }
 #vfjzogzbvs .gt_footnotes { color: font-color(HoneyDew); background-color: HoneyDew; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vfjzogzbvs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vfjzogzbvs .gt_sourcenotes { color: #333333; background-color: HoneyDew; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vfjzogzbvs .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #vfjzogzbvs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vfjzogzbvs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal" style="font-family: IBM Plex Serif; font-size: 24px; background-color: aliceblue; border-bottom: 2px solid #BFDFF6">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="font-family: IBM Plex Serif; padding-top: 5px; padding-bottom: 5px; background-image: linear-gradient(120deg, #d4fc79 0%, #96f6a1 100%)">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup">Decay Mode</th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-8</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-9</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-10</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-11</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
<td class="gt_row gt_center" style="background-color: LightCyan">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-14</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-15</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">--</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-16</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-17</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-18</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-19</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-20</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" style="background-color: Linen; font-weight: bold">C-22</th>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>

</table>


In the example, we asked for the HoneyDew background fill on the entire table with [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options). However, even though [tab_options()](../../reference/GT.tab_options.md#great_tables.GT.tab_options) was used after those [tab_style()](../../reference/GT.tab_style.md#great_tables.GT.tab_style) invocations, the 'HoneyDew' background color was only applied to the locations that didn't have a background color set through `tab_style(). The important takeaway here is that the precedence (or priority) is *always* given to`tab_style()\`, regardless of the order of invocation.


## Wrapping up

We'd like to thank [Tim Paine](https://github.com/timkpaine) for getting the expanded `loc` work off the ground. Additionally, we are grateful to [Jerry Wu](https://github.com/jrycw) for his contributions to the `v0.13.0` release of the package.

We'd be very pleased to receive comments or suggestions on the new functionality. [GitHub Issues](https://github.com/posit-dev/great-tables/issues) or [GitHub Discussions](https://github.com/posit-dev/great-tables/discussions) are both fine venues for getting in touch with us. Finally, if ever you want to talk about tables with us, you're always welcome to jump into our [Discord Server](https://discord.com/invite/Ux7nrcXHVV).
