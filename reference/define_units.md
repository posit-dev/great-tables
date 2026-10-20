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
#ktflujxrbx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ktflujxrbx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ktflujxrbx p { margin: 0; padding: 0; }
 #ktflujxrbx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ktflujxrbx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ktflujxrbx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ktflujxrbx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ktflujxrbx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ktflujxrbx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ktflujxrbx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ktflujxrbx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ktflujxrbx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ktflujxrbx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ktflujxrbx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ktflujxrbx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ktflujxrbx .gt_spanner_row { border-bottom-style: hidden; }
 #ktflujxrbx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ktflujxrbx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ktflujxrbx .gt_from_md> :first-child { margin-top: 0; }
 #ktflujxrbx .gt_from_md> :last-child { margin-bottom: 0; }
 #ktflujxrbx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ktflujxrbx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ktflujxrbx .gt_indent_1 { text-indent: 5px; }
 #ktflujxrbx .gt_indent_2 { text-indent: calc(5px * 2); }
 #ktflujxrbx .gt_indent_3 { text-indent: calc(5px * 3); }
 #ktflujxrbx .gt_indent_4 { text-indent: calc(5px * 4); }
 #ktflujxrbx .gt_indent_5 { text-indent: calc(5px * 5); }
 #ktflujxrbx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ktflujxrbx .gt_row_group_first td { border-top-width: 2px; }
 #ktflujxrbx .gt_row_group_first th { border-top-width: 2px; }
 #ktflujxrbx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ktflujxrbx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ktflujxrbx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ktflujxrbx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ktflujxrbx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ktflujxrbx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ktflujxrbx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ktflujxrbx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ktflujxrbx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ktflujxrbx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ktflujxrbx .gt_left { text-align: left; }
 #ktflujxrbx .gt_center { text-align: center; }
 #ktflujxrbx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ktflujxrbx .gt_font_normal { font-weight: normal; }
 #ktflujxrbx .gt_font_bold { font-weight: bold; }
 #ktflujxrbx .gt_font_italic { font-style: italic; }
 #ktflujxrbx .gt_super { font-size: 65%; }
 #ktflujxrbx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ktflujxrbx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ktflujxrbx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ktflujxrbx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ktflujxrbx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ktflujxrbx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<td class="gt_row gt_left" headers="rule">'^' creates a superscript</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">m^2</td>
<td class="gt_row gt_left" headers="output">m<span style="white-space:nowrap;"><sup>2</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">'_' creates a subscript</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">h_0</td>
<td class="gt_row gt_left" headers="output">h<span style="white-space:nowrap;"><sub>0</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">subscripts and superscripts can be combined</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">h_0^3</td>
<td class="gt_row gt_left" headers="output">h<span style="white-space:nowrap;"><sub>0</sub></span><span style="white-space:nowrap;"><sup>3</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">use '[_subscript^superscript]' to create an overstrike</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">h[_0^3]</td>
<td class="gt_row gt_left" headers="output">h<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">3<br />
0</span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">a '/' at the beginning adds the superscript '-1'</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">/s</td>
<td class="gt_row gt_left" headers="output">s<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">hyphen is transformed to minus sign when preceding a unit</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">-h^2</td>
<td class="gt_row gt_left" headers="output">−h<span style="white-space:nowrap;"><sup>2</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">'x' at the beginning is transformed to '×'</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">x10^3 kg^2 m^-1</td>
<td class="gt_row gt_left" headers="output">×10<span style="white-space:nowrap;"><sup>3</sup></span> kg<span style="white-space:nowrap;"><sup>2</sup></span> m<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">ASCII terms from biology/chemistry turned into terminology forms</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">ug</td>
<td class="gt_row gt_left" headers="output">µg</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">can create italics with '*' or '_'; create bold text with '**' or '__'</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">*m*^**2**</td>
<td class="gt_row gt_left" headers="output"><em>m</em><span style="white-space:nowrap;"><sup><strong>2</strong></sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">special symbol set surrounded by colons</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">:permille:C</td>
<td class="gt_row gt_left" headers="output">‰C</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="rule">chemistry notation: '%C6H6%'</td>
<td class="gt_row gt_left" style="font-family: courier" headers="input">g/L %C6H12O6%</td>
<td class="gt_row gt_left" headers="output">g/L C<span style="white-space:nowrap;"><sub>6</sub></span>H<span style="white-space:nowrap;"><sub>12</sub></span>O<span style="white-space:nowrap;"><sub>6</sub></span></td>
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
#jnrktvnlnp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jnrktvnlnp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jnrktvnlnp p { margin: 0; padding: 0; }
 #jnrktvnlnp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jnrktvnlnp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jnrktvnlnp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jnrktvnlnp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jnrktvnlnp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jnrktvnlnp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jnrktvnlnp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jnrktvnlnp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jnrktvnlnp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jnrktvnlnp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jnrktvnlnp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jnrktvnlnp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jnrktvnlnp .gt_spanner_row { border-bottom-style: hidden; }
 #jnrktvnlnp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jnrktvnlnp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jnrktvnlnp .gt_from_md> :first-child { margin-top: 0; }
 #jnrktvnlnp .gt_from_md> :last-child { margin-bottom: 0; }
 #jnrktvnlnp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jnrktvnlnp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jnrktvnlnp .gt_indent_1 { text-indent: 5px; }
 #jnrktvnlnp .gt_indent_2 { text-indent: calc(5px * 2); }
 #jnrktvnlnp .gt_indent_3 { text-indent: calc(5px * 3); }
 #jnrktvnlnp .gt_indent_4 { text-indent: calc(5px * 4); }
 #jnrktvnlnp .gt_indent_5 { text-indent: calc(5px * 5); }
 #jnrktvnlnp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jnrktvnlnp .gt_row_group_first td { border-top-width: 2px; }
 #jnrktvnlnp .gt_row_group_first th { border-top-width: 2px; }
 #jnrktvnlnp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jnrktvnlnp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jnrktvnlnp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jnrktvnlnp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jnrktvnlnp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jnrktvnlnp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jnrktvnlnp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jnrktvnlnp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jnrktvnlnp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jnrktvnlnp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jnrktvnlnp .gt_left { text-align: left; }
 #jnrktvnlnp .gt_center { text-align: center; }
 #jnrktvnlnp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jnrktvnlnp .gt_font_normal { font-weight: normal; }
 #jnrktvnlnp .gt_font_bold { font-weight: bold; }
 #jnrktvnlnp .gt_font_italic { font-style: italic; }
 #jnrktvnlnp .gt_super { font-size: 65%; }
 #jnrktvnlnp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jnrktvnlnp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jnrktvnlnp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jnrktvnlnp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jnrktvnlnp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jnrktvnlnp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" id="title" class="gt_heading gt_title gt_font_normal">Linear Algebra</th>
</tr>
<tr class="gt_heading">
<th colspan="5" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">y={{a_2}}{{x^2}}+{{a_1}}x+{{a_0}}</th>
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
<td class="gt_row gt_right" headers="x">1</td>
<td class="gt_row gt_right" headers="a2">2</td>
<td class="gt_row gt_right" headers="a1">3</td>
<td class="gt_row gt_right" headers="a0">4</td>
<td class="gt_row gt_right" headers="y">9</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="x">2</td>
<td class="gt_row gt_right" headers="a2">3</td>
<td class="gt_row gt_right" headers="a1">4</td>
<td class="gt_row gt_right" headers="a0">5</td>
<td class="gt_row gt_right" headers="y">25</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="x">3</td>
<td class="gt_row gt_right" headers="a2">4</td>
<td class="gt_row gt_right" headers="a1">5</td>
<td class="gt_row gt_right" headers="a0">6</td>
<td class="gt_row gt_right" headers="y">57</td>
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
#bawyqxaiff table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bawyqxaiff thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bawyqxaiff p { margin: 0; padding: 0; }
 #bawyqxaiff .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bawyqxaiff .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bawyqxaiff .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bawyqxaiff .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bawyqxaiff .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bawyqxaiff .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bawyqxaiff .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bawyqxaiff .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bawyqxaiff .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bawyqxaiff .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bawyqxaiff .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bawyqxaiff .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bawyqxaiff .gt_spanner_row { border-bottom-style: hidden; }
 #bawyqxaiff .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bawyqxaiff .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bawyqxaiff .gt_from_md> :first-child { margin-top: 0; }
 #bawyqxaiff .gt_from_md> :last-child { margin-bottom: 0; }
 #bawyqxaiff .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bawyqxaiff .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bawyqxaiff .gt_indent_1 { text-indent: 5px; }
 #bawyqxaiff .gt_indent_2 { text-indent: calc(5px * 2); }
 #bawyqxaiff .gt_indent_3 { text-indent: calc(5px * 3); }
 #bawyqxaiff .gt_indent_4 { text-indent: calc(5px * 4); }
 #bawyqxaiff .gt_indent_5 { text-indent: calc(5px * 5); }
 #bawyqxaiff .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bawyqxaiff .gt_row_group_first td { border-top-width: 2px; }
 #bawyqxaiff .gt_row_group_first th { border-top-width: 2px; }
 #bawyqxaiff .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bawyqxaiff .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bawyqxaiff .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bawyqxaiff .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bawyqxaiff .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bawyqxaiff .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bawyqxaiff .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bawyqxaiff .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bawyqxaiff .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bawyqxaiff .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bawyqxaiff .gt_left { text-align: left; }
 #bawyqxaiff .gt_center { text-align: center; }
 #bawyqxaiff .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bawyqxaiff .gt_font_normal { font-weight: normal; }
 #bawyqxaiff .gt_font_bold { font-weight: bold; }
 #bawyqxaiff .gt_font_italic { font-style: italic; }
 #bawyqxaiff .gt_super { font-size: 65%; }
 #bawyqxaiff .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bawyqxaiff .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bawyqxaiff .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bawyqxaiff .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bawyqxaiff .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bawyqxaiff .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="5" id="title" class="gt_heading gt_title gt_font_normal">Linear Algebra</th>
</tr>
<tr class="gt_heading">
<th colspan="5" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">y=a<span style="white-space:nowrap;"><sub>2</sub></span>x<span style="white-space:nowrap;"><sup>2</sup></span>+a<span style="white-space:nowrap;"><sub>1</sub></span>x+a<span style="white-space:nowrap;"><sub>0</sub></span></th>
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
<td class="gt_row gt_right" headers="x">1</td>
<td class="gt_row gt_right" headers="a2">2</td>
<td class="gt_row gt_right" headers="a1">3</td>
<td class="gt_row gt_right" headers="a0">4</td>
<td class="gt_row gt_right" headers="y">9</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="x">2</td>
<td class="gt_row gt_right" headers="a2">3</td>
<td class="gt_row gt_right" headers="a1">4</td>
<td class="gt_row gt_right" headers="a0">5</td>
<td class="gt_row gt_right" headers="y">25</td>
</tr>
<tr>
<td class="gt_row gt_right" headers="x">3</td>
<td class="gt_row gt_right" headers="a2">4</td>
<td class="gt_row gt_right" headers="a1">5</td>
<td class="gt_row gt_right" headers="a0">6</td>
<td class="gt_row gt_right" headers="y">57</td>
</tr>
</tbody>
</table>
