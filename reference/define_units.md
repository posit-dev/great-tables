# define_units()


With [define_units()](define_units.md#great_tables.define_units) you can work with a specially-crafted units notation string and emit the


Usage

``` python
define_units(units_notation)
```


units as HTML (with the `.to_html()` method). This function is useful as a standalone utility and it powers the [fmt_units()](GT.fmt_units.md#great_tables.GT.fmt_units) method in **Great Tables**.


## Parameters


`units_notation: str`  
A string of units notation.


## Returns


`UnitDefinitionList`  
A list of unit definitions.


## Specification Of Units Notation

The following table demonstrates the various ways in which units can be specified in the `units_notation` string and how the input is processed by the [define_units()](define_units.md#great_tables.define_units) function. The concluding step for display of the units in HTML is to use the `to_html()` method.


<style>
#djdbfjjpxt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#djdbfjjpxt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#djdbfjjpxt p { margin: 0; padding: 0; }
 #djdbfjjpxt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #djdbfjjpxt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #djdbfjjpxt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #djdbfjjpxt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #djdbfjjpxt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #djdbfjjpxt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djdbfjjpxt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #djdbfjjpxt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #djdbfjjpxt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #djdbfjjpxt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #djdbfjjpxt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #djdbfjjpxt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #djdbfjjpxt .gt_spanner_row { border-bottom-style: hidden; }
 #djdbfjjpxt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #djdbfjjpxt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #djdbfjjpxt .gt_from_md> :first-child { margin-top: 0; }
 #djdbfjjpxt .gt_from_md> :last-child { margin-bottom: 0; }
 #djdbfjjpxt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #djdbfjjpxt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #djdbfjjpxt .gt_indent_1 { text-indent: 5px; }
 #djdbfjjpxt .gt_indent_2 { text-indent: calc(5px * 2); }
 #djdbfjjpxt .gt_indent_3 { text-indent: calc(5px * 3); }
 #djdbfjjpxt .gt_indent_4 { text-indent: calc(5px * 4); }
 #djdbfjjpxt .gt_indent_5 { text-indent: calc(5px * 5); }
 #djdbfjjpxt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #djdbfjjpxt .gt_row_group_first td { border-top-width: 2px; }
 #djdbfjjpxt .gt_row_group_first th { border-top-width: 2px; }
 #djdbfjjpxt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #djdbfjjpxt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djdbfjjpxt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #djdbfjjpxt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #djdbfjjpxt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djdbfjjpxt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #djdbfjjpxt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #djdbfjjpxt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #djdbfjjpxt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djdbfjjpxt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #djdbfjjpxt .gt_left { text-align: left; }
 #djdbfjjpxt .gt_center { text-align: center; }
 #djdbfjjpxt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #djdbfjjpxt .gt_font_normal { font-weight: normal; }
 #djdbfjjpxt .gt_font_bold { font-weight: bold; }
 #djdbfjjpxt .gt_font_italic { font-style: italic; }
 #djdbfjjpxt .gt_super { font-size: 65%; }
 #djdbfjjpxt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djdbfjjpxt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #djdbfjjpxt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djdbfjjpxt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #djdbfjjpxt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #djdbfjjpxt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="rule" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">rule</th>
<th id="input" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">input</th>
<th id="output" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">output</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">'^' creates a superscript</td>
<td class="gt_row gt_left" style="font-family: courier">m^2</td>
<td class="gt_row gt_left">m<span style="white-space:nowrap;"><sup>2</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">'_' creates a subscript</td>
<td class="gt_row gt_left" style="font-family: courier">h_0</td>
<td class="gt_row gt_left">h<span style="white-space:nowrap;"><sub>0</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left">subscripts and superscripts can be combined</td>
<td class="gt_row gt_left" style="font-family: courier">h_0^3</td>
<td class="gt_row gt_left">h<span style="white-space:nowrap;"><sub>0</sub></span><span style="white-space:nowrap;"><sup>3</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">use '[_subscript^superscript]' to create an overstrike</td>
<td class="gt_row gt_left" style="font-family: courier">h[_0^3]</td>
<td class="gt_row gt_left">h<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">3<br />
0</span></td>
</tr>
<tr>
<td class="gt_row gt_left">a '/' at the beginning adds the superscript '-1'</td>
<td class="gt_row gt_left" style="font-family: courier">/s</td>
<td class="gt_row gt_left">s<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">hyphen is transformed to minus sign when preceding a unit</td>
<td class="gt_row gt_left" style="font-family: courier">-h^2</td>
<td class="gt_row gt_left">−h<span style="white-space:nowrap;"><sup>2</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">'x' at the beginning is transformed to '×'</td>
<td class="gt_row gt_left" style="font-family: courier">x10^3 kg^2 m^-1</td>
<td class="gt_row gt_left">×10<span style="white-space:nowrap;"><sup>3</sup></span> kg<span style="white-space:nowrap;"><sup>2</sup></span> m<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">ASCII terms from biology/chemistry turned into terminology forms</td>
<td class="gt_row gt_left" style="font-family: courier">ug</td>
<td class="gt_row gt_left">µg</td>
</tr>
<tr>
<td class="gt_row gt_left">can create italics with '*' or '_'; create bold text with '**' or '__'</td>
<td class="gt_row gt_left" style="font-family: courier">*m*^**2**</td>
<td class="gt_row gt_left"><em>m</em><span style="white-space:nowrap;"><sup><strong>2</strong></sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">special symbol set surrounded by colons</td>
<td class="gt_row gt_left" style="font-family: courier">:permille:C</td>
<td class="gt_row gt_left">‰C</td>
</tr>
<tr>
<td class="gt_row gt_left">chemistry notation: '%C6H6%'</td>
<td class="gt_row gt_left" style="font-family: courier">g/L %C6H12O6%</td>
<td class="gt_row gt_left">g/L C<span style="white-space:nowrap;"><sub>6</sub></span>H<span style="white-space:nowrap;"><sub>12</sub></span>O<span style="white-space:nowrap;"><sub>6</sub></span></td>
</tr>
</tbody>
</table>


## Examples

Let's demonstrate a use case where we utilize [define_units()](define_units.md#great_tables.define_units) to render an equation as the subtitle in the table header, which currently doesn't accept unit notation as input.

We'll start by creating a Polars DataFrame representing the calculations of the equation y= a_2x^2 + a_1x + a_0.


Code

``` python
import polars as pl
from great_tables import GT, html, define_units

df = pl.DataFrame(
    {"x": [1, 2, 3], "a2": [2, 3, 4], "a1": [3, 4, 5], "a0": [4, 5, 6]}
).with_columns(
    y=(
        pl.col("a2").mul(pl.col("x").pow(2))
        + pl.col("a1").mul(pl.col("x"))
        + pl.col("a0")
    )
)

df
```


shape: (3, 5)

| x   | a2  | a1  | a0  | y   |
|-----|-----|-----|-----|-----|
| i64 | i64 | i64 | i64 | i64 |
| 1   | 2   | 3   | 4   | 9   |
| 2   | 3   | 4   | 5   | 25  |
| 3   | 4   | 5   | 6   | 57  |


If we try to use unit annotations to format the equation as the subtitle in the header, it won't work as expected:


``` python
(
    GT(df)
    .cols_label(a2="{{a_2}}", a1="{{a_1}}", a0="{{a_0}}")
    .tab_header(title="Linear Algebra", subtitle="y={{a_2}}{{x^2}}+{{a_1}}x+{{a_0}}")
)
```


<style>
#vtrrilyrlz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vtrrilyrlz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vtrrilyrlz p { margin: 0; padding: 0; }
 #vtrrilyrlz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vtrrilyrlz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vtrrilyrlz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vtrrilyrlz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vtrrilyrlz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vtrrilyrlz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vtrrilyrlz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vtrrilyrlz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vtrrilyrlz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vtrrilyrlz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vtrrilyrlz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vtrrilyrlz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vtrrilyrlz .gt_spanner_row { border-bottom-style: hidden; }
 #vtrrilyrlz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vtrrilyrlz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vtrrilyrlz .gt_from_md> :first-child { margin-top: 0; }
 #vtrrilyrlz .gt_from_md> :last-child { margin-bottom: 0; }
 #vtrrilyrlz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vtrrilyrlz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vtrrilyrlz .gt_indent_1 { text-indent: 5px; }
 #vtrrilyrlz .gt_indent_2 { text-indent: calc(5px * 2); }
 #vtrrilyrlz .gt_indent_3 { text-indent: calc(5px * 3); }
 #vtrrilyrlz .gt_indent_4 { text-indent: calc(5px * 4); }
 #vtrrilyrlz .gt_indent_5 { text-indent: calc(5px * 5); }
 #vtrrilyrlz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vtrrilyrlz .gt_row_group_first td { border-top-width: 2px; }
 #vtrrilyrlz .gt_row_group_first th { border-top-width: 2px; }
 #vtrrilyrlz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vtrrilyrlz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vtrrilyrlz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vtrrilyrlz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vtrrilyrlz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vtrrilyrlz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vtrrilyrlz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vtrrilyrlz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vtrrilyrlz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vtrrilyrlz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vtrrilyrlz .gt_left { text-align: left; }
 #vtrrilyrlz .gt_center { text-align: center; }
 #vtrrilyrlz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vtrrilyrlz .gt_font_normal { font-weight: normal; }
 #vtrrilyrlz .gt_font_bold { font-weight: bold; }
 #vtrrilyrlz .gt_font_italic { font-style: italic; }
 #vtrrilyrlz .gt_super { font-size: 65%; }
 #vtrrilyrlz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vtrrilyrlz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vtrrilyrlz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vtrrilyrlz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vtrrilyrlz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vtrrilyrlz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_title gt_font_normal">Linear Algebra</th>
</tr>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">y={{a_2}}{{x^2}}+{{a_1}}x+{{a_0}}</th>
</tr>
<tr class="gt_col_headings">
<th id="x" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">x</th>
<th id="a2" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">a<span style="white-space:nowrap;"><sub>2</sub></span></th>
<th id="a1" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">a<span style="white-space:nowrap;"><sub>1</sub></span></th>
<th id="a0" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">a<span style="white-space:nowrap;"><sub>0</sub></span></th>
<th id="y" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">y</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">9</td>
</tr>
<tr>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">25</td>
</tr>
<tr>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">6</td>
<td class="gt_row gt_right">57</td>
</tr>
</tbody>
</table>


To address this, we can create a small helper function, `u2html()`, which wraps a given string in [define_units()](define_units.md#great_tables.define_units) and emits the units to HTML. Next, we can build the subtitle by applying `u2html()` to the string with unit annotations. Finally, we pass the assembled subtitle string through [html()](html.md#great_tables.html) to ensure it renders correctly.


``` python
def u2html(x: str) -> str:
    return define_units(x).to_html()


subtitle = (
    "y"
    + "="
    + u2html("{{a_2}}")
    + u2html("{{x^2}}")
    + "+"
    + u2html("{{a_1}}")
    + "x"
    + "+"
    + u2html("{{a_0}}")
)

(
    GT(df)
    .cols_label(a2="{{a_2}}", a1="{{a_1}}", a0="{{a_0}}")
    .tab_header(title="Linear Algebra", subtitle=html(subtitle))
)
```


<style>
#znqodtslvu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#znqodtslvu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#znqodtslvu p { margin: 0; padding: 0; }
 #znqodtslvu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #znqodtslvu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #znqodtslvu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #znqodtslvu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #znqodtslvu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #znqodtslvu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #znqodtslvu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #znqodtslvu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #znqodtslvu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #znqodtslvu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #znqodtslvu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #znqodtslvu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #znqodtslvu .gt_spanner_row { border-bottom-style: hidden; }
 #znqodtslvu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #znqodtslvu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #znqodtslvu .gt_from_md> :first-child { margin-top: 0; }
 #znqodtslvu .gt_from_md> :last-child { margin-bottom: 0; }
 #znqodtslvu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #znqodtslvu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #znqodtslvu .gt_indent_1 { text-indent: 5px; }
 #znqodtslvu .gt_indent_2 { text-indent: calc(5px * 2); }
 #znqodtslvu .gt_indent_3 { text-indent: calc(5px * 3); }
 #znqodtslvu .gt_indent_4 { text-indent: calc(5px * 4); }
 #znqodtslvu .gt_indent_5 { text-indent: calc(5px * 5); }
 #znqodtslvu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #znqodtslvu .gt_row_group_first td { border-top-width: 2px; }
 #znqodtslvu .gt_row_group_first th { border-top-width: 2px; }
 #znqodtslvu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #znqodtslvu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #znqodtslvu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #znqodtslvu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #znqodtslvu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #znqodtslvu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #znqodtslvu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #znqodtslvu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #znqodtslvu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #znqodtslvu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #znqodtslvu .gt_left { text-align: left; }
 #znqodtslvu .gt_center { text-align: center; }
 #znqodtslvu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #znqodtslvu .gt_font_normal { font-weight: normal; }
 #znqodtslvu .gt_font_bold { font-weight: bold; }
 #znqodtslvu .gt_font_italic { font-style: italic; }
 #znqodtslvu .gt_super { font-size: 65%; }
 #znqodtslvu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #znqodtslvu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #znqodtslvu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #znqodtslvu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #znqodtslvu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #znqodtslvu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_title gt_font_normal">Linear Algebra</th>
</tr>
<tr class="gt_heading">
<th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">y=a<span style="white-space:nowrap;"><sub>2</sub></span>x<span style="white-space:nowrap;"><sup>2</sup></span>+a<span style="white-space:nowrap;"><sub>1</sub></span>x+a<span style="white-space:nowrap;"><sub>0</sub></span></th>
</tr>
<tr class="gt_col_headings">
<th id="x" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">x</th>
<th id="a2" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">a<span style="white-space:nowrap;"><sub>2</sub></span></th>
<th id="a1" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">a<span style="white-space:nowrap;"><sub>1</sub></span></th>
<th id="a0" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">a<span style="white-space:nowrap;"><sub>0</sub></span></th>
<th id="y" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">y</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_right">1</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">9</td>
</tr>
<tr>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">25</td>
</tr>
<tr>
<td class="gt_row gt_right">3</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right">5</td>
<td class="gt_row gt_right">6</td>
<td class="gt_row gt_right">57</td>
</tr>
</tbody>
</table>
