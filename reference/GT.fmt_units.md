# GT.fmt_units()


Format measurement units.


Usage

``` python
GT.fmt_units(
    columns=None,
    rows=None,
    pattern="{x}",
)
```


The [fmt_units()](GT.fmt_units.md#great_tables.GT.fmt_units) method lets you better format measurement units in the table body. These must conform to the **Great Tables** *units notation*; as an example of this, `"J Hz^-1 mol^-1"` can be used to generate units for the *molar Planck constant*. The notation here provides several conveniences for defining units, so as long as the values to be formatted conform to this syntax, you'll obtain nicely-formatted inline units. Details pertaining to *units notation* can be found in the section entitled *How to use units notation*.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.


## How To Use Units Notation

The **Great Tables** units notation involves a shorthand of writing units that feels familiar and is fine-tuned for the task at hand. Each unit is treated as a separate entity (parentheses and other symbols included) and the addition of subscript text and exponents is flexible and relatively easy to formulate. This is all best shown with examples:

- `"m/s"` and `"m / s"` both render as `"m/s"`
- `"m s^-1"` will appear with the `"-1"` exponent intact
- `"m /s"` gives the the same result, as `"/<unit>"` is equivalent to `"<unit>^-1"`
- `"E_h"` will render an `"E"` with the `"h"` subscript
- `"t_i^2.5"` provides a `t` with an `"i"` subscript and a `"2.5"` exponent
- `"m[_0^2]"` will use overstriking to set both scripts vertically
- `"g/L %C6H12O6%"` uses a chemical formula (enclosed in a pair of `"%"` characters) as a unit partial, and the formula will render correctly with subscripted numbers
- Common units that are difficult to write using ASCII text may be implicitly converted to the correct characters (e.g., the `"u"` in `"ug"`, `"um"`, `"uL"`, and `"umol"` will be converted to the Greek *mu* symbol; `"degC"` and `"degF"` will render a degree sign before the temperature unit)
- We can transform shorthand symbol/unit names enclosed in `":"` (e.g., `":angstrom:"`, `":ohm:"`, etc.) into proper symbols
- Greek letters can added by enclosing the letter name in `":"`; you can use lowercase letters (e.g., `":beta:"`, `":sigma:"`, etc.) and uppercase letters too (e.g., `":Alpha:"`, `":Zeta:"`, etc.)
- The components of a unit (unit name, subscript, and exponent) can be fully or partially italicized/emboldened by surrounding text with `"*"` or `"**"`


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [illness](data.illness.md#great_tables.data.illness) dataset and create a new table. The `units` column happens to contain string values in *units notation* (e.g., `"x10^9 / L"`). Using the [fmt_units()](GT.fmt_units.md#great_tables.GT.fmt_units) method here will improve the formatting of those measurement units.


``` python
from great_tables import GT, style, loc
from great_tables.data import illness

(
    GT(illness, rowname_col="test")
    .fmt_units(columns="units")
    .fmt_number(columns=lambda x: x.startswith("day"), decimals=2, drop_trailing_zeros=True)
    .tab_header(title="Laboratory Findings for the YF Patient")
    .tab_spanner(label="Day", columns=lambda x: x.startswith("day"))
    .tab_spanner(label="Normal Range", columns=lambda x: x.startswith("norm"))
    .cols_label(
      norm_l="Lower",
      norm_u="Upper",
      units="Units"
    )
    .opt_vertical_padding(scale=0.4)
    .opt_align_table_header(align="left")
    .tab_options(heading_padding="10px")
    .tab_style(
        locations=loc.body(columns="norm_l"),
        style=style.borders(sides="left")
    )
    .opt_vertical_padding(scale=0.5)
)
```


<style>
#zixrjrltyk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zixrjrltyk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zixrjrltyk p { margin: 0; padding: 0; }
 #zixrjrltyk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zixrjrltyk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zixrjrltyk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zixrjrltyk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 4px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zixrjrltyk .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zixrjrltyk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zixrjrltyk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zixrjrltyk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 1px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zixrjrltyk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zixrjrltyk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zixrjrltyk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zixrjrltyk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 1px; padding-bottom: 1px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zixrjrltyk .gt_spanner_row { border-bottom-style: hidden; }
 #zixrjrltyk .gt_group_heading { padding-top: 1.6px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zixrjrltyk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zixrjrltyk .gt_from_md> :first-child { margin-top: 0; }
 #zixrjrltyk .gt_from_md> :last-child { margin-bottom: 0; }
 #zixrjrltyk .gt_row { padding-top: 1.6px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zixrjrltyk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zixrjrltyk .gt_indent_1 { text-indent: 5px; }
 #zixrjrltyk .gt_indent_2 { text-indent: calc(5px * 2); }
 #zixrjrltyk .gt_indent_3 { text-indent: calc(5px * 3); }
 #zixrjrltyk .gt_indent_4 { text-indent: calc(5px * 4); }
 #zixrjrltyk .gt_indent_5 { text-indent: calc(5px * 5); }
 #zixrjrltyk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zixrjrltyk .gt_row_group_first td { border-top-width: 2px; }
 #zixrjrltyk .gt_row_group_first th { border-top-width: 2px; }
 #zixrjrltyk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zixrjrltyk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zixrjrltyk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zixrjrltyk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zixrjrltyk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zixrjrltyk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zixrjrltyk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zixrjrltyk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zixrjrltyk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zixrjrltyk .gt_sourcenote { font-size: 90%; padding-top: 0.8px; padding-bottom: 0.8px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zixrjrltyk .gt_left { text-align: left; }
 #zixrjrltyk .gt_center { text-align: center; }
 #zixrjrltyk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zixrjrltyk .gt_font_normal { font-weight: normal; }
 #zixrjrltyk .gt_font_bold { font-weight: bold; }
 #zixrjrltyk .gt_font_italic { font-style: italic; }
 #zixrjrltyk .gt_super { font-size: 65%; }
 #zixrjrltyk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zixrjrltyk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zixrjrltyk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zixrjrltyk .gt_sourcenote { font-size: 90%; padding-top: 0.8px; padding-bottom: 0.8px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zixrjrltyk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zixrjrltyk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="11" id="title" class="gt_heading gt_title gt_font_normal">Laboratory Findings for the YF Patient</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th rowspan="2" id="units" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Units</th>
<th colspan="7" id="Day" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Day</th>
<th colspan="2" id="Normal-Range" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Normal Range</th>
</tr>
<tr class="gt_col_headings">
<th id="day_3" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">day_3</th>
<th id="day_4" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">day_4</th>
<th id="day_5" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">day_5</th>
<th id="day_6" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">day_6</th>
<th id="day_7" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">day_7</th>
<th id="day_8" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">day_8</th>
<th id="day_9" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">day_9</th>
<th id="norm_l" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Lower</th>
<th id="norm_u" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Upper</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">Viral load</th>
<td class="gt_row gt_left" headers="stub-1 units">copies per mL</td>
<td class="gt_row gt_right" headers="stub-1 Day day_3">12,000</td>
<td class="gt_row gt_right" headers="stub-1 Day day_4">4,200</td>
<td class="gt_row gt_right" headers="stub-1 Day day_5">1,600</td>
<td class="gt_row gt_right" headers="stub-1 Day day_6">830</td>
<td class="gt_row gt_right" headers="stub-1 Day day_7">760</td>
<td class="gt_row gt_right" headers="stub-1 Day day_8">520</td>
<td class="gt_row gt_right" headers="stub-1 Day day_9">250</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-1 Normal-Range norm_l">None</td>
<td class="gt_row gt_right" headers="stub-1 Normal-Range norm_u">None</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">WBC</th>
<td class="gt_row gt_left" headers="stub-2 units">×10<span style="white-space:nowrap;"><sup>9</sup></span>/L</td>
<td class="gt_row gt_right" headers="stub-2 Day day_3">5.26</td>
<td class="gt_row gt_right" headers="stub-2 Day day_4">4.26</td>
<td class="gt_row gt_right" headers="stub-2 Day day_5">9.92</td>
<td class="gt_row gt_right" headers="stub-2 Day day_6">10.49</td>
<td class="gt_row gt_right" headers="stub-2 Day day_7">24.77</td>
<td class="gt_row gt_right" headers="stub-2 Day day_8">30.26</td>
<td class="gt_row gt_right" headers="stub-2 Day day_9">19.03</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-2 Normal-Range norm_l">4.0</td>
<td class="gt_row gt_right" headers="stub-2 Normal-Range norm_u">10.0</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">Neutrophils</th>
<td class="gt_row gt_left" headers="stub-3 units">×10<span style="white-space:nowrap;"><sup>9</sup></span>/L</td>
<td class="gt_row gt_right" headers="stub-3 Day day_3">4.87</td>
<td class="gt_row gt_right" headers="stub-3 Day day_4">4.72</td>
<td class="gt_row gt_right" headers="stub-3 Day day_5">7.92</td>
<td class="gt_row gt_right" headers="stub-3 Day day_6">18.21</td>
<td class="gt_row gt_right" headers="stub-3 Day day_7">22.08</td>
<td class="gt_row gt_right" headers="stub-3 Day day_8">27.17</td>
<td class="gt_row gt_right" headers="stub-3 Day day_9">16.59</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-3 Normal-Range norm_l">2.0</td>
<td class="gt_row gt_right" headers="stub-3 Normal-Range norm_u">8.0</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">RBC</th>
<td class="gt_row gt_left" headers="stub-4 units">×10<span style="white-space:nowrap;"><sup>12</sup></span>/L</td>
<td class="gt_row gt_right" headers="stub-4 Day day_3">5.72</td>
<td class="gt_row gt_right" headers="stub-4 Day day_4">5.98</td>
<td class="gt_row gt_right" headers="stub-4 Day day_5">4.23</td>
<td class="gt_row gt_right" headers="stub-4 Day day_6">4.83</td>
<td class="gt_row gt_right" headers="stub-4 Day day_7">4.12</td>
<td class="gt_row gt_right" headers="stub-4 Day day_8">2.68</td>
<td class="gt_row gt_right" headers="stub-4 Day day_9">3.32</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-4 Normal-Range norm_l">4.0</td>
<td class="gt_row gt_right" headers="stub-4 Normal-Range norm_u">5.5</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row">Hb</th>
<td class="gt_row gt_left" headers="stub-5 units">g/L</td>
<td class="gt_row gt_right" headers="stub-5 Day day_3">153</td>
<td class="gt_row gt_right" headers="stub-5 Day day_4">135</td>
<td class="gt_row gt_right" headers="stub-5 Day day_5">126</td>
<td class="gt_row gt_right" headers="stub-5 Day day_6">115</td>
<td class="gt_row gt_right" headers="stub-5 Day day_7">75</td>
<td class="gt_row gt_right" headers="stub-5 Day day_8">87</td>
<td class="gt_row gt_right" headers="stub-5 Day day_9">95</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-5 Normal-Range norm_l">120.0</td>
<td class="gt_row gt_right" headers="stub-5 Normal-Range norm_u">160.0</td>
</tr>
<tr>
<th id="stub-6" class="gt_row gt_left gt_stub" scope="row">PLT</th>
<td class="gt_row gt_left" headers="stub-6 units">×10<span style="white-space:nowrap;"><sup>9</sup></span>/L</td>
<td class="gt_row gt_right" headers="stub-6 Day day_3">67</td>
<td class="gt_row gt_right" headers="stub-6 Day day_4">38.6</td>
<td class="gt_row gt_right" headers="stub-6 Day day_5">27.4</td>
<td class="gt_row gt_right" headers="stub-6 Day day_6">26.2</td>
<td class="gt_row gt_right" headers="stub-6 Day day_7">74.1</td>
<td class="gt_row gt_right" headers="stub-6 Day day_8">36.2</td>
<td class="gt_row gt_right" headers="stub-6 Day day_9">25.6</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-6 Normal-Range norm_l">100.0</td>
<td class="gt_row gt_right" headers="stub-6 Normal-Range norm_u">300.0</td>
</tr>
<tr>
<th id="stub-7" class="gt_row gt_left gt_stub" scope="row">ALT</th>
<td class="gt_row gt_left" headers="stub-7 units">U/L</td>
<td class="gt_row gt_right" headers="stub-7 Day day_3">12,835</td>
<td class="gt_row gt_right" headers="stub-7 Day day_4">12,632</td>
<td class="gt_row gt_right" headers="stub-7 Day day_5">6,426.7</td>
<td class="gt_row gt_right" headers="stub-7 Day day_6">4,263.1</td>
<td class="gt_row gt_right" headers="stub-7 Day day_7">1,623.7</td>
<td class="gt_row gt_right" headers="stub-7 Day day_8">672.6</td>
<td class="gt_row gt_right" headers="stub-7 Day day_9">512.4</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-7 Normal-Range norm_l">9.0</td>
<td class="gt_row gt_right" headers="stub-7 Normal-Range norm_u">50.0</td>
</tr>
<tr>
<th id="stub-8" class="gt_row gt_left gt_stub" scope="row">AST</th>
<td class="gt_row gt_left" headers="stub-8 units">U/L</td>
<td class="gt_row gt_right" headers="stub-8 Day day_3">23,672</td>
<td class="gt_row gt_right" headers="stub-8 Day day_4">21,368</td>
<td class="gt_row gt_right" headers="stub-8 Day day_5">14,730</td>
<td class="gt_row gt_right" headers="stub-8 Day day_6">8,691</td>
<td class="gt_row gt_right" headers="stub-8 Day day_7">2,189</td>
<td class="gt_row gt_right" headers="stub-8 Day day_8">1,145</td>
<td class="gt_row gt_right" headers="stub-8 Day day_9">782.5</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-8 Normal-Range norm_l">15.0</td>
<td class="gt_row gt_right" headers="stub-8 Normal-Range norm_u">40.0</td>
</tr>
<tr>
<th id="stub-9" class="gt_row gt_left gt_stub" scope="row">TBIL</th>
<td class="gt_row gt_left" headers="stub-9 units">µmol/L</td>
<td class="gt_row gt_right" headers="stub-9 Day day_3">117.2</td>
<td class="gt_row gt_right" headers="stub-9 Day day_4">143.8</td>
<td class="gt_row gt_right" headers="stub-9 Day day_5">137.2</td>
<td class="gt_row gt_right" headers="stub-9 Day day_6">158.1</td>
<td class="gt_row gt_right" headers="stub-9 Day day_7">127.3</td>
<td class="gt_row gt_right" headers="stub-9 Day day_8">105.1</td>
<td class="gt_row gt_right" headers="stub-9 Day day_9">163.2</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-9 Normal-Range norm_l">0.0</td>
<td class="gt_row gt_right" headers="stub-9 Normal-Range norm_u">18.8</td>
</tr>
<tr>
<th id="stub-10" class="gt_row gt_left gt_stub" scope="row">DBIL</th>
<td class="gt_row gt_left" headers="stub-10 units">µmol/L</td>
<td class="gt_row gt_right" headers="stub-10 Day day_3">71.4</td>
<td class="gt_row gt_right" headers="stub-10 Day day_4">104.6</td>
<td class="gt_row gt_right" headers="stub-10 Day day_5">94.6</td>
<td class="gt_row gt_right" headers="stub-10 Day day_6">143.9</td>
<td class="gt_row gt_right" headers="stub-10 Day day_7">117.8</td>
<td class="gt_row gt_right" headers="stub-10 Day day_8">83.6</td>
<td class="gt_row gt_right" headers="stub-10 Day day_9">126.3</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-10 Normal-Range norm_l">0.0</td>
<td class="gt_row gt_right" headers="stub-10 Normal-Range norm_u">6.8</td>
</tr>
<tr>
<th id="stub-11" class="gt_row gt_left gt_stub" scope="row">NH3</th>
<td class="gt_row gt_left" headers="stub-11 units">mmol/L</td>
<td class="gt_row gt_right" headers="stub-11 Day day_3">115.2</td>
<td class="gt_row gt_right" headers="stub-11 Day day_4">135.2</td>
<td class="gt_row gt_right" headers="stub-11 Day day_5">131</td>
<td class="gt_row gt_right" headers="stub-11 Day day_6">176.7</td>
<td class="gt_row gt_right" headers="stub-11 Day day_7">84.2</td>
<td class="gt_row gt_right" headers="stub-11 Day day_8">72.4</td>
<td class="gt_row gt_right" headers="stub-11 Day day_9">91.9</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-11 Normal-Range norm_l">10.0</td>
<td class="gt_row gt_right" headers="stub-11 Normal-Range norm_u">47.0</td>
</tr>
<tr>
<th id="stub-12" class="gt_row gt_left gt_stub" scope="row">PT</th>
<td class="gt_row gt_left" headers="stub-12 units">s</td>
<td class="gt_row gt_right" headers="stub-12 Day day_3">24.6</td>
<td class="gt_row gt_right" headers="stub-12 Day day_4">42.4</td>
<td class="gt_row gt_right" headers="stub-12 Day day_5">53.7</td>
<td class="gt_row gt_right" headers="stub-12 Day day_6">54</td>
<td class="gt_row gt_right" headers="stub-12 Day day_7">22.6</td>
<td class="gt_row gt_right" headers="stub-12 Day day_8">16.8</td>
<td class="gt_row gt_right" headers="stub-12 Day day_9">29.5</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-12 Normal-Range norm_l">9.4</td>
<td class="gt_row gt_right" headers="stub-12 Normal-Range norm_u">12.5</td>
</tr>
<tr>
<th id="stub-13" class="gt_row gt_left gt_stub" scope="row">APTT</th>
<td class="gt_row gt_left" headers="stub-13 units">s</td>
<td class="gt_row gt_right" headers="stub-13 Day day_3">39.2</td>
<td class="gt_row gt_right" headers="stub-13 Day day_4">57.2</td>
<td class="gt_row gt_right" headers="stub-13 Day day_5">65.9</td>
<td class="gt_row gt_right" headers="stub-13 Day day_6">68.3</td>
<td class="gt_row gt_right" headers="stub-13 Day day_7">62.4</td>
<td class="gt_row gt_right" headers="stub-13 Day day_8">61.7</td>
<td class="gt_row gt_right" headers="stub-13 Day day_9">114.7</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-13 Normal-Range norm_l">25.1</td>
<td class="gt_row gt_right" headers="stub-13 Normal-Range norm_u">36.5</td>
</tr>
<tr>
<th id="stub-14" class="gt_row gt_left gt_stub" scope="row">PTA</th>
<td class="gt_row gt_left" headers="stub-14 units">%</td>
<td class="gt_row gt_right" headers="stub-14 Day day_3">41</td>
<td class="gt_row gt_right" headers="stub-14 Day day_4">25</td>
<td class="gt_row gt_right" headers="stub-14 Day day_5">19</td>
<td class="gt_row gt_right" headers="stub-14 Day day_6">14</td>
<td class="gt_row gt_right" headers="stub-14 Day day_7">51</td>
<td class="gt_row gt_right" headers="stub-14 Day day_8">55</td>
<td class="gt_row gt_right" headers="stub-14 Day day_9">31</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-14 Normal-Range norm_l">70.0</td>
<td class="gt_row gt_right" headers="stub-14 Normal-Range norm_u">130.0</td>
</tr>
<tr>
<th id="stub-15" class="gt_row gt_left gt_stub" scope="row">DD</th>
<td class="gt_row gt_left" headers="stub-15 units">mg/L</td>
<td class="gt_row gt_right" headers="stub-15 Day day_3">32.9</td>
<td class="gt_row gt_right" headers="stub-15 Day day_4">35.1</td>
<td class="gt_row gt_right" headers="stub-15 Day day_5">24.5</td>
<td class="gt_row gt_right" headers="stub-15 Day day_6">25.6</td>
<td class="gt_row gt_right" headers="stub-15 Day day_7">18.7</td>
<td class="gt_row gt_right" headers="stub-15 Day day_8">24.7</td>
<td class="gt_row gt_right" headers="stub-15 Day day_9">64.8</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-15 Normal-Range norm_l">0.0</td>
<td class="gt_row gt_right" headers="stub-15 Normal-Range norm_u">5.0</td>
</tr>
<tr>
<th id="stub-16" class="gt_row gt_left gt_stub" scope="row">FDP</th>
<td class="gt_row gt_left" headers="stub-16 units">µg/mL</td>
<td class="gt_row gt_right" headers="stub-16 Day day_3">84.7</td>
<td class="gt_row gt_right" headers="stub-16 Day day_4">92.5</td>
<td class="gt_row gt_right" headers="stub-16 Day day_5">77.2</td>
<td class="gt_row gt_right" headers="stub-16 Day day_6">None</td>
<td class="gt_row gt_right" headers="stub-16 Day day_7">None</td>
<td class="gt_row gt_right" headers="stub-16 Day day_8">157.2</td>
<td class="gt_row gt_right" headers="stub-16 Day day_9">291.7</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-16 Normal-Range norm_l">0.0</td>
<td class="gt_row gt_right" headers="stub-16 Normal-Range norm_u">5.0</td>
</tr>
<tr>
<th id="stub-17" class="gt_row gt_left gt_stub" scope="row">Fibrinogen</th>
<td class="gt_row gt_left" headers="stub-17 units">mg/dL</td>
<td class="gt_row gt_right" headers="stub-17 Day day_3">238.1</td>
<td class="gt_row gt_right" headers="stub-17 Day day_4">216.8</td>
<td class="gt_row gt_right" headers="stub-17 Day day_5">135</td>
<td class="gt_row gt_right" headers="stub-17 Day day_6">85.2</td>
<td class="gt_row gt_right" headers="stub-17 Day day_7">105.7</td>
<td class="gt_row gt_right" headers="stub-17 Day day_8">None</td>
<td class="gt_row gt_right" headers="stub-17 Day day_9">64.3</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-17 Normal-Range norm_l">200.0</td>
<td class="gt_row gt_right" headers="stub-17 Normal-Range norm_u">400.0</td>
</tr>
<tr>
<th id="stub-18" class="gt_row gt_left gt_stub" scope="row">LDH</th>
<td class="gt_row gt_left" headers="stub-18 units">U/L</td>
<td class="gt_row gt_right" headers="stub-18 Day day_3">5,727.3</td>
<td class="gt_row gt_right" headers="stub-18 Day day_4">2,622.8</td>
<td class="gt_row gt_right" headers="stub-18 Day day_5">2,418.7</td>
<td class="gt_row gt_right" headers="stub-18 Day day_6">546.3</td>
<td class="gt_row gt_right" headers="stub-18 Day day_7">None</td>
<td class="gt_row gt_right" headers="stub-18 Day day_8">637.2</td>
<td class="gt_row gt_right" headers="stub-18 Day day_9">None</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-18 Normal-Range norm_l">80.0</td>
<td class="gt_row gt_right" headers="stub-18 Normal-Range norm_u">285.0</td>
</tr>
<tr>
<th id="stub-19" class="gt_row gt_left gt_stub" scope="row">HBDH</th>
<td class="gt_row gt_left" headers="stub-19 units">None</td>
<td class="gt_row gt_right" headers="stub-19 Day day_3">5,971.2</td>
<td class="gt_row gt_right" headers="stub-19 Day day_4">5,826.9</td>
<td class="gt_row gt_right" headers="stub-19 Day day_5">4,826.9</td>
<td class="gt_row gt_right" headers="stub-19 Day day_6">2,871.2</td>
<td class="gt_row gt_right" headers="stub-19 Day day_7">None</td>
<td class="gt_row gt_right" headers="stub-19 Day day_8">1,163.6</td>
<td class="gt_row gt_right" headers="stub-19 Day day_9">None</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-19 Normal-Range norm_l">74.0</td>
<td class="gt_row gt_right" headers="stub-19 Normal-Range norm_u">182.0</td>
</tr>
<tr>
<th id="stub-20" class="gt_row gt_left gt_stub" scope="row">CK</th>
<td class="gt_row gt_left" headers="stub-20 units">U/L</td>
<td class="gt_row gt_right" headers="stub-20 Day day_3">725</td>
<td class="gt_row gt_right" headers="stub-20 Day day_4">792.1</td>
<td class="gt_row gt_right" headers="stub-20 Day day_5">760.2</td>
<td class="gt_row gt_right" headers="stub-20 Day day_6">1,263.6</td>
<td class="gt_row gt_right" headers="stub-20 Day day_7">None</td>
<td class="gt_row gt_right" headers="stub-20 Day day_8">1,294.2</td>
<td class="gt_row gt_right" headers="stub-20 Day day_9">None</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-20 Normal-Range norm_l">38.0</td>
<td class="gt_row gt_right" headers="stub-20 Normal-Range norm_u">174.0</td>
</tr>
<tr>
<th id="stub-21" class="gt_row gt_left gt_stub" scope="row">CKMB</th>
<td class="gt_row gt_left" headers="stub-21 units">U/L</td>
<td class="gt_row gt_right" headers="stub-21 Day day_3">75</td>
<td class="gt_row gt_right" headers="stub-21 Day day_4">71</td>
<td class="gt_row gt_right" headers="stub-21 Day day_5">58</td>
<td class="gt_row gt_right" headers="stub-21 Day day_6">65</td>
<td class="gt_row gt_right" headers="stub-21 Day day_7">None</td>
<td class="gt_row gt_right" headers="stub-21 Day day_8">68</td>
<td class="gt_row gt_right" headers="stub-21 Day day_9">None</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-21 Normal-Range norm_l">None</td>
<td class="gt_row gt_right" headers="stub-21 Normal-Range norm_u">25.0</td>
</tr>
<tr>
<th id="stub-22" class="gt_row gt_left gt_stub" scope="row">BNP</th>
<td class="gt_row gt_left" headers="stub-22 units">pg/mL</td>
<td class="gt_row gt_right" headers="stub-22 Day day_3">37</td>
<td class="gt_row gt_right" headers="stub-22 Day day_4">None</td>
<td class="gt_row gt_right" headers="stub-22 Day day_5">73</td>
<td class="gt_row gt_right" headers="stub-22 Day day_6">None</td>
<td class="gt_row gt_right" headers="stub-22 Day day_7">482</td>
<td class="gt_row gt_right" headers="stub-22 Day day_8">421</td>
<td class="gt_row gt_right" headers="stub-22 Day day_9">1,332</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-22 Normal-Range norm_l">None</td>
<td class="gt_row gt_right" headers="stub-22 Normal-Range norm_u">100.0</td>
</tr>
<tr>
<th id="stub-23" class="gt_row gt_left gt_stub" scope="row">MYO</th>
<td class="gt_row gt_left" headers="stub-23 units">ng/mL</td>
<td class="gt_row gt_right" headers="stub-23 Day day_3">636.6</td>
<td class="gt_row gt_right" headers="stub-23 Day day_4">762.1</td>
<td class="gt_row gt_right" headers="stub-23 Day day_5">364.6</td>
<td class="gt_row gt_right" headers="stub-23 Day day_6">9,999</td>
<td class="gt_row gt_right" headers="stub-23 Day day_7">9,999</td>
<td class="gt_row gt_right" headers="stub-23 Day day_8">9,999</td>
<td class="gt_row gt_right" headers="stub-23 Day day_9">9,999</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-23 Normal-Range norm_l">0.0</td>
<td class="gt_row gt_right" headers="stub-23 Normal-Range norm_u">140.0</td>
</tr>
<tr>
<th id="stub-24" class="gt_row gt_left gt_stub" scope="row">TnI</th>
<td class="gt_row gt_left" headers="stub-24 units">ng/mL</td>
<td class="gt_row gt_right" headers="stub-24 Day day_3">0.03</td>
<td class="gt_row gt_right" headers="stub-24 Day day_4">0.04</td>
<td class="gt_row gt_right" headers="stub-24 Day day_5">0.05</td>
<td class="gt_row gt_right" headers="stub-24 Day day_6">0.16</td>
<td class="gt_row gt_right" headers="stub-24 Day day_7">0.14</td>
<td class="gt_row gt_right" headers="stub-24 Day day_8">2.84</td>
<td class="gt_row gt_right" headers="stub-24 Day day_9">8.94</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-24 Normal-Range norm_l">0.0</td>
<td class="gt_row gt_right" headers="stub-24 Normal-Range norm_u">0.028</td>
</tr>
<tr>
<th id="stub-25" class="gt_row gt_left gt_stub" scope="row">CREA</th>
<td class="gt_row gt_left" headers="stub-25 units">µmol/L</td>
<td class="gt_row gt_right" headers="stub-25 Day day_3">705.6</td>
<td class="gt_row gt_right" headers="stub-25 Day day_4">683.6</td>
<td class="gt_row gt_right" headers="stub-25 Day day_5">523.6</td>
<td class="gt_row gt_right" headers="stub-25 Day day_6">374</td>
<td class="gt_row gt_right" headers="stub-25 Day day_7">259.6</td>
<td class="gt_row gt_right" headers="stub-25 Day day_8">241.8</td>
<td class="gt_row gt_right" headers="stub-25 Day day_9">211.4</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-25 Normal-Range norm_l">59.0</td>
<td class="gt_row gt_right" headers="stub-25 Normal-Range norm_u">104.0</td>
</tr>
<tr>
<th id="stub-26" class="gt_row gt_left gt_stub" scope="row">BUN</th>
<td class="gt_row gt_left" headers="stub-26 units">mmol/L</td>
<td class="gt_row gt_right" headers="stub-26 Day day_3">20.13</td>
<td class="gt_row gt_right" headers="stub-26 Day day_4">25.33</td>
<td class="gt_row gt_right" headers="stub-26 Day day_5">13.33</td>
<td class="gt_row gt_right" headers="stub-26 Day day_6">7.84</td>
<td class="gt_row gt_right" headers="stub-26 Day day_7">4.23</td>
<td class="gt_row gt_right" headers="stub-26 Day day_8">3.92</td>
<td class="gt_row gt_right" headers="stub-26 Day day_9">3.41</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-26 Normal-Range norm_l">1.7</td>
<td class="gt_row gt_right" headers="stub-26 Normal-Range norm_u">8.3</td>
</tr>
<tr>
<th id="stub-27" class="gt_row gt_left gt_stub" scope="row">AMY</th>
<td class="gt_row gt_left" headers="stub-27 units">U/L</td>
<td class="gt_row gt_right" headers="stub-27 Day day_3">None</td>
<td class="gt_row gt_right" headers="stub-27 Day day_4">232.8</td>
<td class="gt_row gt_right" headers="stub-27 Day day_5">394.6</td>
<td class="gt_row gt_right" headers="stub-27 Day day_6">513.7</td>
<td class="gt_row gt_right" headers="stub-27 Day day_7">None</td>
<td class="gt_row gt_right" headers="stub-27 Day day_8">642.9</td>
<td class="gt_row gt_right" headers="stub-27 Day day_9">538.9</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-27 Normal-Range norm_l">0.0</td>
<td class="gt_row gt_right" headers="stub-27 Normal-Range norm_u">115.0</td>
</tr>
<tr>
<th id="stub-28" class="gt_row gt_left gt_stub" scope="row">LPS</th>
<td class="gt_row gt_left" headers="stub-28 units">U/L</td>
<td class="gt_row gt_right" headers="stub-28 Day day_3">None</td>
<td class="gt_row gt_right" headers="stub-28 Day day_4">227.6</td>
<td class="gt_row gt_right" headers="stub-28 Day day_5">526.9</td>
<td class="gt_row gt_right" headers="stub-28 Day day_6">487.9</td>
<td class="gt_row gt_right" headers="stub-28 Day day_7">None</td>
<td class="gt_row gt_right" headers="stub-28 Day day_8">437.8</td>
<td class="gt_row gt_right" headers="stub-28 Day day_9">414.5</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-28 Normal-Range norm_l">5.6</td>
<td class="gt_row gt_right" headers="stub-28 Normal-Range norm_u">51.3</td>
</tr>
<tr>
<th id="stub-29" class="gt_row gt_left gt_stub" scope="row">K</th>
<td class="gt_row gt_left" headers="stub-29 units">mmol/L</td>
<td class="gt_row gt_right" headers="stub-29 Day day_3">4.19</td>
<td class="gt_row gt_right" headers="stub-29 Day day_4">4.64</td>
<td class="gt_row gt_right" headers="stub-29 Day day_5">4.34</td>
<td class="gt_row gt_right" headers="stub-29 Day day_6">4.83</td>
<td class="gt_row gt_right" headers="stub-29 Day day_7">4.53</td>
<td class="gt_row gt_right" headers="stub-29 Day day_8">4.37</td>
<td class="gt_row gt_right" headers="stub-29 Day day_9">5.74</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-29 Normal-Range norm_l">3.5</td>
<td class="gt_row gt_right" headers="stub-29 Normal-Range norm_u">5.3</td>
</tr>
<tr>
<th id="stub-30" class="gt_row gt_left gt_stub" scope="row">Na</th>
<td class="gt_row gt_left" headers="stub-30 units">mmol/L</td>
<td class="gt_row gt_right" headers="stub-30 Day day_3">136.3</td>
<td class="gt_row gt_right" headers="stub-30 Day day_4">135.7</td>
<td class="gt_row gt_right" headers="stub-30 Day day_5">142.1</td>
<td class="gt_row gt_right" headers="stub-30 Day day_6">140.8</td>
<td class="gt_row gt_right" headers="stub-30 Day day_7">144.8</td>
<td class="gt_row gt_right" headers="stub-30 Day day_8">143.6</td>
<td class="gt_row gt_right" headers="stub-30 Day day_9">144.2</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-30 Normal-Range norm_l">137.0</td>
<td class="gt_row gt_right" headers="stub-30 Normal-Range norm_u">147.0</td>
</tr>
<tr>
<th id="stub-31" class="gt_row gt_left gt_stub" scope="row">Cl</th>
<td class="gt_row gt_left" headers="stub-31 units">mmol/L</td>
<td class="gt_row gt_right" headers="stub-31 Day day_3">91.2</td>
<td class="gt_row gt_right" headers="stub-31 Day day_4">92.9</td>
<td class="gt_row gt_right" headers="stub-31 Day day_5">96.6</td>
<td class="gt_row gt_right" headers="stub-31 Day day_6">99.2</td>
<td class="gt_row gt_right" headers="stub-31 Day day_7">102.1</td>
<td class="gt_row gt_right" headers="stub-31 Day day_8">99.5</td>
<td class="gt_row gt_right" headers="stub-31 Day day_9">105.2</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-31 Normal-Range norm_l">99.0</td>
<td class="gt_row gt_right" headers="stub-31 Normal-Range norm_u">110.0</td>
</tr>
<tr>
<th id="stub-32" class="gt_row gt_left gt_stub" scope="row">Ca</th>
<td class="gt_row gt_left" headers="stub-32 units">mmol/L</td>
<td class="gt_row gt_right" headers="stub-32 Day day_3">1.74</td>
<td class="gt_row gt_right" headers="stub-32 Day day_4">1.64</td>
<td class="gt_row gt_right" headers="stub-32 Day day_5">2.25</td>
<td class="gt_row gt_right" headers="stub-32 Day day_6">2.35</td>
<td class="gt_row gt_right" headers="stub-32 Day day_7">2.16</td>
<td class="gt_row gt_right" headers="stub-32 Day day_8">2.03</td>
<td class="gt_row gt_right" headers="stub-32 Day day_9">2.29</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-32 Normal-Range norm_l">2.2</td>
<td class="gt_row gt_right" headers="stub-32 Normal-Range norm_u">2.55</td>
</tr>
<tr>
<th id="stub-33" class="gt_row gt_left gt_stub" scope="row">P</th>
<td class="gt_row gt_left" headers="stub-33 units">mmol/L</td>
<td class="gt_row gt_right" headers="stub-33 Day day_3">2.96</td>
<td class="gt_row gt_right" headers="stub-33 Day day_4">3.23</td>
<td class="gt_row gt_right" headers="stub-33 Day day_5">1.47</td>
<td class="gt_row gt_right" headers="stub-33 Day day_6">1.15</td>
<td class="gt_row gt_right" headers="stub-33 Day day_7">0.97</td>
<td class="gt_row gt_right" headers="stub-33 Day day_8">1.57</td>
<td class="gt_row gt_right" headers="stub-33 Day day_9">1.63</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-33 Normal-Range norm_l">0.81</td>
<td class="gt_row gt_right" headers="stub-33 Normal-Range norm_u">1.45</td>
</tr>
<tr>
<th id="stub-34" class="gt_row gt_left gt_stub" scope="row">Lac</th>
<td class="gt_row gt_left" headers="stub-34 units">mmol/L</td>
<td class="gt_row gt_right" headers="stub-34 Day day_3">2.32</td>
<td class="gt_row gt_right" headers="stub-34 Day day_4">2.42</td>
<td class="gt_row gt_right" headers="stub-34 Day day_5">2.19</td>
<td class="gt_row gt_right" headers="stub-34 Day day_6">2.66</td>
<td class="gt_row gt_right" headers="stub-34 Day day_7">None</td>
<td class="gt_row gt_right" headers="stub-34 Day day_8">6.15</td>
<td class="gt_row gt_right" headers="stub-34 Day day_9">5.46</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-34 Normal-Range norm_l">1.33</td>
<td class="gt_row gt_right" headers="stub-34 Normal-Range norm_u">1.78</td>
</tr>
<tr>
<th id="stub-35" class="gt_row gt_left gt_stub" scope="row">CRP</th>
<td class="gt_row gt_left" headers="stub-35 units">mg/L</td>
<td class="gt_row gt_right" headers="stub-35 Day day_3">43.6</td>
<td class="gt_row gt_right" headers="stub-35 Day day_4">38.6</td>
<td class="gt_row gt_right" headers="stub-35 Day day_5">28.6</td>
<td class="gt_row gt_right" headers="stub-35 Day day_6">21.5</td>
<td class="gt_row gt_right" headers="stub-35 Day day_7">None</td>
<td class="gt_row gt_right" headers="stub-35 Day day_8">4.3</td>
<td class="gt_row gt_right" headers="stub-35 Day day_9">6.4</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-35 Normal-Range norm_l">0.0</td>
<td class="gt_row gt_right" headers="stub-35 Normal-Range norm_u">5.0</td>
</tr>
<tr>
<th id="stub-36" class="gt_row gt_left gt_stub" scope="row">PCT</th>
<td class="gt_row gt_left" headers="stub-36 units">ng/mL</td>
<td class="gt_row gt_right" headers="stub-36 Day day_3">0.57</td>
<td class="gt_row gt_right" headers="stub-36 Day day_4">None</td>
<td class="gt_row gt_right" headers="stub-36 Day day_5">1.35</td>
<td class="gt_row gt_right" headers="stub-36 Day day_6">2.26</td>
<td class="gt_row gt_right" headers="stub-36 Day day_7">1.79</td>
<td class="gt_row gt_right" headers="stub-36 Day day_8">3.48</td>
<td class="gt_row gt_right" headers="stub-36 Day day_9">5.92</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-36 Normal-Range norm_l">None</td>
<td class="gt_row gt_right" headers="stub-36 Normal-Range norm_u">0.05</td>
</tr>
<tr>
<th id="stub-37" class="gt_row gt_left gt_stub" scope="row">IL-6</th>
<td class="gt_row gt_left" headers="stub-37 units">None</td>
<td class="gt_row gt_right" headers="stub-37 Day day_3">None</td>
<td class="gt_row gt_right" headers="stub-37 Day day_4">None</td>
<td class="gt_row gt_right" headers="stub-37 Day day_5">165.9</td>
<td class="gt_row gt_right" headers="stub-37 Day day_6">58.3</td>
<td class="gt_row gt_right" headers="stub-37 Day day_7">74.6</td>
<td class="gt_row gt_right" headers="stub-37 Day day_8">737.2</td>
<td class="gt_row gt_right" headers="stub-37 Day day_9">None</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-37 Normal-Range norm_l">None</td>
<td class="gt_row gt_right" headers="stub-37 Normal-Range norm_u">7.0</td>
</tr>
<tr>
<th id="stub-38" class="gt_row gt_left gt_stub" scope="row">CD3+CD4+</th>
<td class="gt_row gt_left" headers="stub-38 units">T cells per µL</td>
<td class="gt_row gt_right" headers="stub-38 Day day_3">None</td>
<td class="gt_row gt_right" headers="stub-38 Day day_4">174</td>
<td class="gt_row gt_right" headers="stub-38 Day day_5">153</td>
<td class="gt_row gt_right" headers="stub-38 Day day_6">184</td>
<td class="gt_row gt_right" headers="stub-38 Day day_7">243</td>
<td class="gt_row gt_right" headers="stub-38 Day day_8">370</td>
<td class="gt_row gt_right" headers="stub-38 Day day_9">252</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-38 Normal-Range norm_l">706.0</td>
<td class="gt_row gt_right" headers="stub-38 Normal-Range norm_u">1125.0</td>
</tr>
<tr>
<th id="stub-39" class="gt_row gt_left gt_stub" scope="row">CD3+CD8+</th>
<td class="gt_row gt_left" headers="stub-39 units">T cells per µL</td>
<td class="gt_row gt_right" headers="stub-39 Day day_3">None</td>
<td class="gt_row gt_right" headers="stub-39 Day day_4">142</td>
<td class="gt_row gt_right" headers="stub-39 Day day_5">135</td>
<td class="gt_row gt_right" headers="stub-39 Day day_6">126</td>
<td class="gt_row gt_right" headers="stub-39 Day day_7">132</td>
<td class="gt_row gt_right" headers="stub-39 Day day_8">511</td>
<td class="gt_row gt_right" headers="stub-39 Day day_9">410</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000" headers="stub-39 Normal-Range norm_l">323.0</td>
<td class="gt_row gt_right" headers="stub-39 Normal-Range norm_u">836.0</td>
</tr>
</tbody>
</table>


The [constants](data.constants.md#great_tables.data.constants) dataset contains values for hundreds of fundamental physical constants. We'll take a subset of values that have some molar basis and generate a new display table from that. Like the [illness](data.illness.md#great_tables.data.illness) dataset, this one has a `units` column so, again, the [fmt_units()](GT.fmt_units.md#great_tables.GT.fmt_units) method will be used to format those units. Here, the preference for typesetting measurement units is to have positive and negative exponents (e.g., not `"<unit_1> / <unit_2>"` but rather `"<unit_1> <unit_2>^-1"`).


``` python
from great_tables.data import constants
import polars as pl
import polars.selectors as cs

constants_mini = (
    pl.from_pandas(constants)
    .filter(pl.col("name").str.contains("molar")).sort("value")
    .with_columns(
        name=pl.col("name")
        .str.to_titlecase()
        .str.replace("Kpa", "kpa")
        .str.replace("Of", "of")
    )
)

(
    GT(constants_mini)
    .cols_hide(columns=["uncert", "sf_value", "sf_uncert"])
    .fmt_units(columns="units")
    .fmt_scientific(columns="value", decimals=3)
    .tab_header(title="Physical Constants Having a Molar Basis")
    .tab_options(column_labels_hidden=True)
)
```


<style>
#washisoofv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#washisoofv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#washisoofv p { margin: 0; padding: 0; }
 #washisoofv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #washisoofv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #washisoofv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #washisoofv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #washisoofv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #washisoofv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #washisoofv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #washisoofv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #washisoofv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #washisoofv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #washisoofv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #washisoofv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #washisoofv .gt_spanner_row { border-bottom-style: hidden; }
 #washisoofv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #washisoofv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #washisoofv .gt_from_md> :first-child { margin-top: 0; }
 #washisoofv .gt_from_md> :last-child { margin-bottom: 0; }
 #washisoofv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #washisoofv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #washisoofv .gt_indent_1 { text-indent: 5px; }
 #washisoofv .gt_indent_2 { text-indent: calc(5px * 2); }
 #washisoofv .gt_indent_3 { text-indent: calc(5px * 3); }
 #washisoofv .gt_indent_4 { text-indent: calc(5px * 4); }
 #washisoofv .gt_indent_5 { text-indent: calc(5px * 5); }
 #washisoofv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #washisoofv .gt_row_group_first td { border-top-width: 2px; }
 #washisoofv .gt_row_group_first th { border-top-width: 2px; }
 #washisoofv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #washisoofv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #washisoofv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #washisoofv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #washisoofv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #washisoofv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #washisoofv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #washisoofv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #washisoofv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #washisoofv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #washisoofv .gt_left { text-align: left; }
 #washisoofv .gt_center { text-align: center; }
 #washisoofv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #washisoofv .gt_font_normal { font-weight: normal; }
 #washisoofv .gt_font_bold { font-weight: bold; }
 #washisoofv .gt_font_italic { font-style: italic; }
 #washisoofv .gt_super { font-size: 65%; }
 #washisoofv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #washisoofv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #washisoofv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #washisoofv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #washisoofv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #washisoofv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" id="title" class="gt_heading gt_title gt_font_normal">Physical Constants Having a Molar Basis</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Molar Planck Constant</td>
<td class="gt_row gt_right">3.990 × 10<sup>−10</sup></td>
<td class="gt_row gt_left">J Hz<span style="white-space:nowrap;"><sup>−1</sup></span> mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Electron Molar Mass</td>
<td class="gt_row gt_right">5.486 × 10<sup>−7</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Volume of Silicon</td>
<td class="gt_row gt_right">1.206 × 10<sup>−5</sup></td>
<td class="gt_row gt_left">m<span style="white-space:nowrap;"><sup>3</sup></span> mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Muon Molar Mass</td>
<td class="gt_row gt_right">1.134 × 10<sup>−4</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Mass Constant</td>
<td class="gt_row gt_right">1.000 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Proton Molar Mass</td>
<td class="gt_row gt_right">1.007 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Neutron Molar Mass</td>
<td class="gt_row gt_right">1.009 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Tau Molar Mass</td>
<td class="gt_row gt_right">1.908 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Deuteron Molar Mass</td>
<td class="gt_row gt_right">2.014 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Helion Molar Mass</td>
<td class="gt_row gt_right">3.015 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Triton Molar Mass</td>
<td class="gt_row gt_right">3.016 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Alpha Particle Molar Mass</td>
<td class="gt_row gt_right">4.002 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Mass of Carbon-12</td>
<td class="gt_row gt_right">1.200 × 10<sup>−2</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Volume of Ideal Gas (273.15 K, 101.325 kpa)</td>
<td class="gt_row gt_right">2.241 × 10<sup>−2</sup></td>
<td class="gt_row gt_left">m<span style="white-space:nowrap;"><sup>3</sup></span> mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Volume of Ideal Gas (273.15 K, 100 kpa)</td>
<td class="gt_row gt_right">2.271 × 10<sup>−2</sup></td>
<td class="gt_row gt_left">m<span style="white-space:nowrap;"><sup>3</sup></span> mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Gas Constant</td>
<td class="gt_row gt_right">8.314</td>
<td class="gt_row gt_left">J mol<span style="white-space:nowrap;"><sup>−1</sup></span> K<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
</tbody>
</table>
