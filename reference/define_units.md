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
#ryzjwvwmxh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ryzjwvwmxh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ryzjwvwmxh p { margin: 0; padding: 0; }
 #ryzjwvwmxh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ryzjwvwmxh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ryzjwvwmxh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ryzjwvwmxh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ryzjwvwmxh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ryzjwvwmxh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ryzjwvwmxh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ryzjwvwmxh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ryzjwvwmxh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ryzjwvwmxh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ryzjwvwmxh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ryzjwvwmxh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ryzjwvwmxh .gt_spanner_row { border-bottom-style: hidden; }
 #ryzjwvwmxh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ryzjwvwmxh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ryzjwvwmxh .gt_from_md> :first-child { margin-top: 0; }
 #ryzjwvwmxh .gt_from_md> :last-child { margin-bottom: 0; }
 #ryzjwvwmxh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ryzjwvwmxh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ryzjwvwmxh .gt_indent_1 { text-indent: 5px; }
 #ryzjwvwmxh .gt_indent_2 { text-indent: calc(5px * 2); }
 #ryzjwvwmxh .gt_indent_3 { text-indent: calc(5px * 3); }
 #ryzjwvwmxh .gt_indent_4 { text-indent: calc(5px * 4); }
 #ryzjwvwmxh .gt_indent_5 { text-indent: calc(5px * 5); }
 #ryzjwvwmxh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ryzjwvwmxh .gt_row_group_first td { border-top-width: 2px; }
 #ryzjwvwmxh .gt_row_group_first th { border-top-width: 2px; }
 #ryzjwvwmxh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ryzjwvwmxh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ryzjwvwmxh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ryzjwvwmxh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ryzjwvwmxh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ryzjwvwmxh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ryzjwvwmxh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ryzjwvwmxh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ryzjwvwmxh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ryzjwvwmxh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ryzjwvwmxh .gt_left { text-align: left; }
 #ryzjwvwmxh .gt_center { text-align: center; }
 #ryzjwvwmxh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ryzjwvwmxh .gt_font_normal { font-weight: normal; }
 #ryzjwvwmxh .gt_font_bold { font-weight: bold; }
 #ryzjwvwmxh .gt_font_italic { font-style: italic; }
 #ryzjwvwmxh .gt_super { font-size: 65%; }
 #ryzjwvwmxh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ryzjwvwmxh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ryzjwvwmxh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ryzjwvwmxh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ryzjwvwmxh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ryzjwvwmxh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sciwrxmdxu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sciwrxmdxu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sciwrxmdxu p { margin: 0; padding: 0; }
 #sciwrxmdxu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sciwrxmdxu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sciwrxmdxu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sciwrxmdxu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sciwrxmdxu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sciwrxmdxu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sciwrxmdxu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sciwrxmdxu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sciwrxmdxu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sciwrxmdxu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sciwrxmdxu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sciwrxmdxu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sciwrxmdxu .gt_spanner_row { border-bottom-style: hidden; }
 #sciwrxmdxu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sciwrxmdxu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sciwrxmdxu .gt_from_md> :first-child { margin-top: 0; }
 #sciwrxmdxu .gt_from_md> :last-child { margin-bottom: 0; }
 #sciwrxmdxu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sciwrxmdxu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sciwrxmdxu .gt_indent_1 { text-indent: 5px; }
 #sciwrxmdxu .gt_indent_2 { text-indent: calc(5px * 2); }
 #sciwrxmdxu .gt_indent_3 { text-indent: calc(5px * 3); }
 #sciwrxmdxu .gt_indent_4 { text-indent: calc(5px * 4); }
 #sciwrxmdxu .gt_indent_5 { text-indent: calc(5px * 5); }
 #sciwrxmdxu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sciwrxmdxu .gt_row_group_first td { border-top-width: 2px; }
 #sciwrxmdxu .gt_row_group_first th { border-top-width: 2px; }
 #sciwrxmdxu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sciwrxmdxu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sciwrxmdxu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sciwrxmdxu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sciwrxmdxu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sciwrxmdxu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sciwrxmdxu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sciwrxmdxu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sciwrxmdxu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sciwrxmdxu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sciwrxmdxu .gt_left { text-align: left; }
 #sciwrxmdxu .gt_center { text-align: center; }
 #sciwrxmdxu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sciwrxmdxu .gt_font_normal { font-weight: normal; }
 #sciwrxmdxu .gt_font_bold { font-weight: bold; }
 #sciwrxmdxu .gt_font_italic { font-style: italic; }
 #sciwrxmdxu .gt_super { font-size: 65%; }
 #sciwrxmdxu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sciwrxmdxu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sciwrxmdxu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sciwrxmdxu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sciwrxmdxu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sciwrxmdxu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cywitokcnv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cywitokcnv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cywitokcnv p { margin: 0; padding: 0; }
 #cywitokcnv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cywitokcnv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cywitokcnv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cywitokcnv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cywitokcnv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cywitokcnv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cywitokcnv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cywitokcnv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cywitokcnv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cywitokcnv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cywitokcnv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cywitokcnv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cywitokcnv .gt_spanner_row { border-bottom-style: hidden; }
 #cywitokcnv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cywitokcnv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cywitokcnv .gt_from_md> :first-child { margin-top: 0; }
 #cywitokcnv .gt_from_md> :last-child { margin-bottom: 0; }
 #cywitokcnv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cywitokcnv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cywitokcnv .gt_indent_1 { text-indent: 5px; }
 #cywitokcnv .gt_indent_2 { text-indent: calc(5px * 2); }
 #cywitokcnv .gt_indent_3 { text-indent: calc(5px * 3); }
 #cywitokcnv .gt_indent_4 { text-indent: calc(5px * 4); }
 #cywitokcnv .gt_indent_5 { text-indent: calc(5px * 5); }
 #cywitokcnv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cywitokcnv .gt_row_group_first td { border-top-width: 2px; }
 #cywitokcnv .gt_row_group_first th { border-top-width: 2px; }
 #cywitokcnv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cywitokcnv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cywitokcnv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cywitokcnv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cywitokcnv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cywitokcnv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cywitokcnv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cywitokcnv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cywitokcnv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cywitokcnv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cywitokcnv .gt_left { text-align: left; }
 #cywitokcnv .gt_center { text-align: center; }
 #cywitokcnv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cywitokcnv .gt_font_normal { font-weight: normal; }
 #cywitokcnv .gt_font_bold { font-weight: bold; }
 #cywitokcnv .gt_font_italic { font-style: italic; }
 #cywitokcnv .gt_super { font-size: 65%; }
 #cywitokcnv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cywitokcnv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cywitokcnv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cywitokcnv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cywitokcnv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cywitokcnv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
