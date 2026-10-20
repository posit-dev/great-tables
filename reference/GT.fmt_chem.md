# GT.fmt_chem()


Format chemical formulas.


Usage

``` python
GT.fmt_chem(
    columns=None,
    rows=None,
)
```


With <a href="../reference/GT.fmt_chem.html#great_tables.GT.fmt_chem" class="gdls-link"><code>fmt_chem()</code></a> you can format chemical formulas and reactions in the table body. Often the input text will be in a common form representing single compounds (like `"C2H4O"` for acetaldehyde) but chemical reactions can also be used (e.g., `"2 CH3OH -> CH3OCH3 + H2O"`). So long as the text within the targeted cells conforms to the specialized chemistry notation, the appropriate conversions will occur. Details on chemistry notation can be found in the section entitled *How to use chemistry notation*.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## How To Use Chemistry Notation

The chemistry notation involves a shorthand for writing chemical formulas and reactions. It should feel familiar in its basic usage and the more advanced typesetting tries to limit the amount of syntax needed. Here are examples of the supported features:

- `"CH3O2"` and `"(NH4)2S"` will render with subscripted numerals

- Charges can be expressed with terminating `"+"` or `"-"`, as in `"H+"` and `"[AgCl2]-"`; numbered charges use: `"CrO4^2-"`, `"Fe^n+"`, `"Y^99+"`, or `"Y^{99+}"`

- Stoichiometric values can prepend formulas: `"2H2O2"`, `"2 H2O2"`, `"0.5 H2O"`, `"1/2 H2O"`, `"(1/2) H2O"`

- Certain standalone lowercase letters are automatically italicized: `"NO_x"` and `"x Na(NH4)HPO4"` will have italic *x* characters; you can always italicize with `"*"` (as in `"*n* H2O"`)

- Chemical isotopes can be rendered as: `"^{227}_{90}Th"` or `"^227_90Th"`; nuclides are similar: `"^{0}_{-1}n^{-}"`, `"^0_-1n-"`

- Chemical reactions can use `"+"` signs and a variety of reaction arrows: `"->"`, `"<-"`, `"<->"`, `"<-->"`, `"<=>"`, `"<=>>"`, `"<<=>"`

- Center dots (for addition compounds) use a single `"."` or `"*"` surrounded by spaces: `"KCr(SO4)2 . 12 H2O"` or `"KCr(SO4)2 * 12 H2O"`

- Single and double bonds between adjacent characters use `"-"` or `"="`: `"C6H5-CHO"`, `"CH3CH=CH2"`

- Greek letters can be inserted using colon notation: `":delta: ^13C"`


## Examples

Let's use the [reactions](data.reactions.md#great_tables.data.reactions) dataset and create a table of gas-phase reaction rate constants for selected terminal alkenes. The `cmpd_formula` column contains chemical formulas and <a href="../reference/GT.fmt_chem.html#great_tables.GT.fmt_chem" class="gdls-link"><code>fmt_chem()</code></a> will render them with properly subscripted numerals. Notice that the column labels for O₃ and NO₃ use the `{%...%}` chemistry notation within [cols_label()](GT.cols_label.md#great_tables.GT.cols_label).


``` python
import polars as pl
import polars.selectors as cs
from great_tables import GT, data

reactions_mini = (
    data.pl.reactions
    .filter(
        (pl.col("cmpd_type") == "terminal monoalkene")
        & pl.col("cmpd_name").str.starts_with("1-")
    )
    .select("cmpd_name", "cmpd_formula", cs.ends_with("k298"))
)

(
    GT(reactions_mini)
    .tab_header(title="Gas-Phase Reactions of Selected Terminal Alkenes")
    .tab_spanner(
        label="Reaction Rate Constant at 298 K",
        columns=cs.ends_with("k298"),
    )
    .fmt_chem(columns="cmpd_formula")
    .fmt_scientific(columns=cs.ends_with("k298"))
    .sub_missing()
    .cols_label(
        cmpd_name="Alkene",
        cmpd_formula="Formula",
        OH_k298="OH",
        O3_k298="{{%O3%}}",
        NO3_k298="{{%NO3%}}",
        Cl_k298="Cl",
    )
    .opt_align_table_header(align="left")
)
```


<style>
#gdbdjksprq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gdbdjksprq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gdbdjksprq p { margin: 0; padding: 0; }
 #gdbdjksprq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gdbdjksprq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gdbdjksprq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gdbdjksprq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gdbdjksprq .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gdbdjksprq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gdbdjksprq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gdbdjksprq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gdbdjksprq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gdbdjksprq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gdbdjksprq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gdbdjksprq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gdbdjksprq .gt_spanner_row { border-bottom-style: hidden; }
 #gdbdjksprq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gdbdjksprq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gdbdjksprq .gt_from_md> :first-child { margin-top: 0; }
 #gdbdjksprq .gt_from_md> :last-child { margin-bottom: 0; }
 #gdbdjksprq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gdbdjksprq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gdbdjksprq .gt_indent_1 { text-indent: 5px; }
 #gdbdjksprq .gt_indent_2 { text-indent: calc(5px * 2); }
 #gdbdjksprq .gt_indent_3 { text-indent: calc(5px * 3); }
 #gdbdjksprq .gt_indent_4 { text-indent: calc(5px * 4); }
 #gdbdjksprq .gt_indent_5 { text-indent: calc(5px * 5); }
 #gdbdjksprq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gdbdjksprq .gt_row_group_first td { border-top-width: 2px; }
 #gdbdjksprq .gt_row_group_first th { border-top-width: 2px; }
 #gdbdjksprq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gdbdjksprq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gdbdjksprq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gdbdjksprq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gdbdjksprq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gdbdjksprq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gdbdjksprq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gdbdjksprq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gdbdjksprq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gdbdjksprq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gdbdjksprq .gt_left { text-align: left; }
 #gdbdjksprq .gt_center { text-align: center; }
 #gdbdjksprq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gdbdjksprq .gt_font_normal { font-weight: normal; }
 #gdbdjksprq .gt_font_bold { font-weight: bold; }
 #gdbdjksprq .gt_font_italic { font-style: italic; }
 #gdbdjksprq .gt_super { font-size: 65%; }
 #gdbdjksprq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gdbdjksprq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gdbdjksprq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gdbdjksprq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gdbdjksprq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gdbdjksprq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" id="title" class="gt_heading gt_title gt_font_normal">Gas-Phase Reactions of Selected Terminal Alkenes</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="cmpd_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Alkene</th>
<th rowspan="2" id="cmpd_formula" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Formula</th>
<th colspan="4" id="Reaction-Rate-Constant-at-298-K" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Reaction Rate Constant at 298 K</th>
</tr>
<tr class="gt_col_headings">
<th id="OH_k298" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">OH</th>
<th id="O3_k298" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">O<span style="white-space:nowrap;"><sub>3</sub></span></th>
<th id="NO3_k298" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">NO<span style="white-space:nowrap;"><sub>3</sub></span></th>
<th id="Cl_k298" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">Cl</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-butene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>4</sub></span>H<span style="white-space:nowrap;"><sub>8</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">3.10 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">1.00 × 10<sup>−17</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">1.30 × 10<sup>−14</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">3.00 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-pentene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>5</sub></span>H<span style="white-space:nowrap;"><sub>10</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">3.22 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">1.06 × 10<sup>−17</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">1.50 × 10<sup>−14</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">4.20 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-hexene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>6</sub></span>H<span style="white-space:nowrap;"><sub>12</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">3.70 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">1.15 × 10<sup>−17</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">1.80 × 10<sup>−14</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">4.00 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-heptene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>7</sub></span>H<span style="white-space:nowrap;"><sub>14</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">3.88 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">1.16 × 10<sup>−17</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">2.00 × 10<sup>−14</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">4.40 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-octene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>8</sub></span>H<span style="white-space:nowrap;"><sub>16</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">3.44 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">1.01 × 10<sup>−17</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">2.50 × 10<sup>−14</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">5.50 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-nonene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>9</sub></span>H<span style="white-space:nowrap;"><sub>18</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">4.32 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">9.90 × 10<sup>−18</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">--</td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">5.90 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-decene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>10</sub></span>H<span style="white-space:nowrap;"><sub>20</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">4.61 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">1.11 × 10<sup>−17</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">2.60 × 10<sup>−14</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">--</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-undecene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>11</sub></span>H<span style="white-space:nowrap;"><sub>22</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">4.79 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">1.03 × 10<sup>−17</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">--</td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">--</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-dodecene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>12</sub></span>H<span style="white-space:nowrap;"><sub>24</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">5.03 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">1.03 × 10<sup>−17</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">2.80 × 10<sup>−14</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">--</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-tridecene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>13</sub></span>H<span style="white-space:nowrap;"><sub>26</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">5.09 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">9.60 × 10<sup>−18</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">--</td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">--</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">1-tetradecene</td>
<td class="gt_row gt_left" headers="cmpd_formula">C<span style="white-space:nowrap;"><sub>14</sub></span>H<span style="white-space:nowrap;"><sub>28</sub></span></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K OH_k298">4.96 × 10<sup>−11</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K O3_k298">9.70 × 10<sup>−18</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K NO3_k298">2.80 × 10<sup>−14</sup></td>
<td class="gt_row gt_right" headers="Reaction-Rate-Constant-at-298-K Cl_k298">--</td>
</tr>
</tbody>
</table>


The [photolysis](data.photolysis.md#great_tables.data.photolysis) dataset contains photolysis pathways where both the `cmpd_formula` and `products` columns hold chemistry notation. We can format both columns with <a href="../reference/GT.fmt_chem.html#great_tables.GT.fmt_chem" class="gdls-link"><code>fmt_chem()</code></a> and use [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge) to combine the compound name with its formatted formula.


``` python
photolysis_mini = (
    data.pl.photolysis
    .filter(pl.col("cmpd_name").is_in([
        "hydrogen peroxide", "nitrous acid",
        "nitric acid", "acetaldehyde",
        "methyl peroxide", "methyl nitrate",
        "ethyl nitrate", "isopropyl nitrate",
    ]))
    .select(pl.exclude("l", "m", "n", "quantum_yield", "type"))
)

(
    GT(photolysis_mini)
    .tab_header(title="Photolysis Pathways of Selected VOCs")
    .fmt_chem(columns=["cmpd_formula", "products"])
    .cols_merge(
        columns=["cmpd_name", "cmpd_formula"],
        pattern="{0}, {1}",
    )
    .cols_label(cmpd_name="Compound", products="Products")
    .cols_hide(columns=["wavelength_nm", "sigma_298_cm2"])
    .opt_align_table_header(align="left")
)
```


<style>
#rzeswjnxxq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rzeswjnxxq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rzeswjnxxq p { margin: 0; padding: 0; }
 #rzeswjnxxq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rzeswjnxxq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rzeswjnxxq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rzeswjnxxq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rzeswjnxxq .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rzeswjnxxq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rzeswjnxxq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rzeswjnxxq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rzeswjnxxq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rzeswjnxxq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rzeswjnxxq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rzeswjnxxq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rzeswjnxxq .gt_spanner_row { border-bottom-style: hidden; }
 #rzeswjnxxq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rzeswjnxxq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rzeswjnxxq .gt_from_md> :first-child { margin-top: 0; }
 #rzeswjnxxq .gt_from_md> :last-child { margin-bottom: 0; }
 #rzeswjnxxq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rzeswjnxxq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rzeswjnxxq .gt_indent_1 { text-indent: 5px; }
 #rzeswjnxxq .gt_indent_2 { text-indent: calc(5px * 2); }
 #rzeswjnxxq .gt_indent_3 { text-indent: calc(5px * 3); }
 #rzeswjnxxq .gt_indent_4 { text-indent: calc(5px * 4); }
 #rzeswjnxxq .gt_indent_5 { text-indent: calc(5px * 5); }
 #rzeswjnxxq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rzeswjnxxq .gt_row_group_first td { border-top-width: 2px; }
 #rzeswjnxxq .gt_row_group_first th { border-top-width: 2px; }
 #rzeswjnxxq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rzeswjnxxq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rzeswjnxxq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rzeswjnxxq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rzeswjnxxq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rzeswjnxxq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rzeswjnxxq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rzeswjnxxq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rzeswjnxxq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rzeswjnxxq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rzeswjnxxq .gt_left { text-align: left; }
 #rzeswjnxxq .gt_center { text-align: center; }
 #rzeswjnxxq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rzeswjnxxq .gt_font_normal { font-weight: normal; }
 #rzeswjnxxq .gt_font_bold { font-weight: bold; }
 #rzeswjnxxq .gt_font_italic { font-style: italic; }
 #rzeswjnxxq .gt_super { font-size: 65%; }
 #rzeswjnxxq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rzeswjnxxq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rzeswjnxxq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rzeswjnxxq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rzeswjnxxq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rzeswjnxxq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" id="title" class="gt_heading gt_title gt_font_normal">Photolysis Pathways of Selected VOCs</th>
</tr>
<tr class="gt_col_headings">
<th id="cmpd_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Compound</th>
<th id="products" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Products</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left" headers="cmpd_name">hydrogen peroxide, H<span style="white-space:nowrap;"><sub>2</sub></span>O<span style="white-space:nowrap;"><sub>2</sub></span></td>
<td class="gt_row gt_left" headers="products">→ OH + OH</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">nitrous acid, HONO</td>
<td class="gt_row gt_left" headers="products">→ OH + NO</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">nitric acid, HNO<span style="white-space:nowrap;"><sub>3</sub></span></td>
<td class="gt_row gt_left" headers="products">→ OH + NO<span style="white-space:nowrap;"><sub>2</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">acetaldehyde, CH<span style="white-space:nowrap;"><sub>3</sub></span>CHO</td>
<td class="gt_row gt_left" headers="products">→ HCO + CH<span style="white-space:nowrap;"><sub>3</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">methyl peroxide, CH<span style="white-space:nowrap;"><sub>3</sub></span>OOH</td>
<td class="gt_row gt_left" headers="products">→ CH<span style="white-space:nowrap;"><sub>3</sub></span>O + OH</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">methyl nitrate, CH<span style="white-space:nowrap;"><sub>3</sub></span>ONO<span style="white-space:nowrap;"><sub>2</sub></span></td>
<td class="gt_row gt_left" headers="products">→ CH<span style="white-space:nowrap;"><sub>3</sub></span>O + NO<span style="white-space:nowrap;"><sub>2</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">ethyl nitrate, C<span style="white-space:nowrap;"><sub>2</sub></span>H<span style="white-space:nowrap;"><sub>5</sub></span>ONO<span style="white-space:nowrap;"><sub>2</sub></span></td>
<td class="gt_row gt_left" headers="products">→ C<span style="white-space:nowrap;"><sub>2</sub></span>H<span style="white-space:nowrap;"><sub>5</sub></span>O + NO<span style="white-space:nowrap;"><sub>2</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left" headers="cmpd_name">isopropyl nitrate, i-C<span style="white-space:nowrap;"><sub>3</sub></span>H<span style="white-space:nowrap;"><sub>7</sub></span>ONO<span style="white-space:nowrap;"><sub>2</sub></span></td>
<td class="gt_row gt_left" headers="products">→ i-C<span style="white-space:nowrap;"><sub>3</sub></span>H<span style="white-space:nowrap;"><sub>7</sub></span>O + NO<span style="white-space:nowrap;"><sub>2</sub></span></td>
</tr>
</tbody>
</table>


The [nuclides](data.nuclides.md#great_tables.data.nuclides) dataset contains isotope data with nuclide notation (e.g., `"^{12}_{6}C"`) that <a href="../reference/GT.fmt_chem.html#great_tables.GT.fmt_chem" class="gdls-link"><code>fmt_chem()</code></a> renders with properly overstruck mass and atomic numbers. Here we show isotopes of hydrogen and carbon.


``` python
from great_tables import md

nuclides_mini = (
    data.pl.nuclides
    .filter(pl.col("element").is_in(["H", "C"]))
    .with_columns(pl.col("nuclide").str.replace(r"[0-9]+$", ""))
    .select("nuclide", "atomic_mass", "half_life", "decay_1", "is_stable")
)

stable = (
    nuclides_mini.with_row_index()
    .filter(pl.col("is_stable") == "TRUE")["index"].to_list()
)
unstable = (
    nuclides_mini.with_row_index()
    .filter(pl.col("is_stable") == "FALSE")["index"].to_list()
)

(
    GT(nuclides_mini, rowname_col="nuclide")
    .tab_header(title="Isotopes of Hydrogen and Carbon")
    .tab_stubhead(label="Isotope")
    .fmt_chem(columns="nuclide")
    .fmt_scientific(columns="half_life")
    .fmt_number(columns="atomic_mass", decimals=4, scale_by=1 / 1e6)
    .sub_missing(
        columns="half_life", rows=stable, missing_text=md("**STABLE**")
    )
    .sub_missing(columns="half_life", rows=unstable)
    .sub_missing(columns="decay_1")
    .cols_hide(columns="is_stable")
    .cols_align(align="center", columns="decay_1")
    .cols_label(decay_1="Decay Mode")
    .opt_align_table_header(align="left")
    .opt_vertical_padding(scale=0.5)
)
```


<style>
#ynzqwgzugp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ynzqwgzugp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ynzqwgzugp p { margin: 0; padding: 0; }
 #ynzqwgzugp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ynzqwgzugp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ynzqwgzugp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ynzqwgzugp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ynzqwgzugp .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ynzqwgzugp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ynzqwgzugp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ynzqwgzugp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ynzqwgzugp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ynzqwgzugp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ynzqwgzugp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ynzqwgzugp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ynzqwgzugp .gt_spanner_row { border-bottom-style: hidden; }
 #ynzqwgzugp .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ynzqwgzugp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ynzqwgzugp .gt_from_md> :first-child { margin-top: 0; }
 #ynzqwgzugp .gt_from_md> :last-child { margin-bottom: 0; }
 #ynzqwgzugp .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ynzqwgzugp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ynzqwgzugp .gt_indent_1 { text-indent: 5px; }
 #ynzqwgzugp .gt_indent_2 { text-indent: calc(5px * 2); }
 #ynzqwgzugp .gt_indent_3 { text-indent: calc(5px * 3); }
 #ynzqwgzugp .gt_indent_4 { text-indent: calc(5px * 4); }
 #ynzqwgzugp .gt_indent_5 { text-indent: calc(5px * 5); }
 #ynzqwgzugp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ynzqwgzugp .gt_row_group_first td { border-top-width: 2px; }
 #ynzqwgzugp .gt_row_group_first th { border-top-width: 2px; }
 #ynzqwgzugp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ynzqwgzugp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ynzqwgzugp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ynzqwgzugp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ynzqwgzugp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ynzqwgzugp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ynzqwgzugp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ynzqwgzugp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ynzqwgzugp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ynzqwgzugp .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ynzqwgzugp .gt_left { text-align: left; }
 #ynzqwgzugp .gt_center { text-align: center; }
 #ynzqwgzugp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ynzqwgzugp .gt_font_normal { font-weight: normal; }
 #ynzqwgzugp .gt_font_bold { font-weight: bold; }
 #ynzqwgzugp .gt_font_italic { font-style: italic; }
 #ynzqwgzugp .gt_super { font-size: 65%; }
 #ynzqwgzugp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ynzqwgzugp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ynzqwgzugp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ynzqwgzugp .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ynzqwgzugp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ynzqwgzugp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">Isotopes of Hydrogen and Carbon</th>
</tr>
<tr class="gt_col_headings">
<th id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Isotope</th>
<th id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">atomic_mass</th>
<th id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">half_life</th>
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" scope="col">Decay Mode</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">1<br />
1</span>H</th>
<td class="gt_row gt_right" headers="stub-1 atomic_mass">1.0078</td>
<td class="gt_row gt_right" headers="stub-1 half_life"><strong>STABLE</strong></td>
<td class="gt_row gt_center" headers="stub-1 decay_1">--</td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">2<br />
1</span>H</th>
<td class="gt_row gt_right" headers="stub-2 atomic_mass">2.0141</td>
<td class="gt_row gt_right" headers="stub-2 half_life"><strong>STABLE</strong></td>
<td class="gt_row gt_center" headers="stub-2 decay_1">--</td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">3<br />
1</span>H</th>
<td class="gt_row gt_right" headers="stub-3 atomic_mass">3.0160</td>
<td class="gt_row gt_right" headers="stub-3 half_life">3.89 × 10<sup>8</sup></td>
<td class="gt_row gt_center" headers="stub-3 decay_1">B-</td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">4<br />
1</span>H</th>
<td class="gt_row gt_right" headers="stub-4 atomic_mass">4.0264</td>
<td class="gt_row gt_right" headers="stub-4 half_life">--</td>
<td class="gt_row gt_center" headers="stub-4 decay_1">N</td>
</tr>
<tr>
<th id="stub-5" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">5<br />
1</span>H</th>
<td class="gt_row gt_right" headers="stub-5 atomic_mass">5.0353</td>
<td class="gt_row gt_right" headers="stub-5 half_life">8.61 × 10<sup>−23</sup></td>
<td class="gt_row gt_center" headers="stub-5 decay_1">2N</td>
</tr>
<tr>
<th id="stub-6" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">6<br />
1</span>H</th>
<td class="gt_row gt_right" headers="stub-6 atomic_mass">6.0450</td>
<td class="gt_row gt_right" headers="stub-6 half_life">2.94 × 10<sup>−22</sup></td>
<td class="gt_row gt_center" headers="stub-6 decay_1">--</td>
</tr>
<tr>
<th id="stub-7" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">7<br />
1</span>H</th>
<td class="gt_row gt_right" headers="stub-7 atomic_mass">7.0527</td>
<td class="gt_row gt_right" headers="stub-7 half_life">5.07 × 10<sup>−21</sup></td>
<td class="gt_row gt_center" headers="stub-7 decay_1">--</td>
</tr>
<tr>
<th id="stub-8" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">8<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-8 atomic_mass">8.0376</td>
<td class="gt_row gt_right" headers="stub-8 half_life">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center" headers="stub-8 decay_1">2P</td>
</tr>
<tr>
<th id="stub-9" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">9<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-9 atomic_mass">9.0310</td>
<td class="gt_row gt_right" headers="stub-9 half_life">1.27 × 10<sup>−1</sup></td>
<td class="gt_row gt_center" headers="stub-9 decay_1">EC+B+</td>
</tr>
<tr>
<th id="stub-10" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">10<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-10 atomic_mass">10.0169</td>
<td class="gt_row gt_right" headers="stub-10 half_life">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center" headers="stub-10 decay_1">EC+B+</td>
</tr>
<tr>
<th id="stub-11" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">11<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-11 atomic_mass">11.0114</td>
<td class="gt_row gt_right" headers="stub-11 half_life">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center" headers="stub-11 decay_1">EC+B+</td>
</tr>
<tr>
<th id="stub-12" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">12<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-12 atomic_mass">12.0000</td>
<td class="gt_row gt_right" headers="stub-12 half_life"><strong>STABLE</strong></td>
<td class="gt_row gt_center" headers="stub-12 decay_1">--</td>
</tr>
<tr>
<th id="stub-13" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">13<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-13 atomic_mass">13.0034</td>
<td class="gt_row gt_right" headers="stub-13 half_life"><strong>STABLE</strong></td>
<td class="gt_row gt_center" headers="stub-13 decay_1">--</td>
</tr>
<tr>
<th id="stub-14" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">14<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-14 atomic_mass">14.0032</td>
<td class="gt_row gt_right" headers="stub-14 half_life">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center" headers="stub-14 decay_1">B-</td>
</tr>
<tr>
<th id="stub-15" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">15<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-15 atomic_mass">15.0106</td>
<td class="gt_row gt_right" headers="stub-15 half_life">2.45</td>
<td class="gt_row gt_center" headers="stub-15 decay_1">B-</td>
</tr>
<tr>
<th id="stub-16" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">16<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-16 atomic_mass">16.0147</td>
<td class="gt_row gt_right" headers="stub-16 half_life">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center" headers="stub-16 decay_1">B-</td>
</tr>
<tr>
<th id="stub-17" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">17<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-17 atomic_mass">17.0226</td>
<td class="gt_row gt_right" headers="stub-17 half_life">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center" headers="stub-17 decay_1">B-</td>
</tr>
<tr>
<th id="stub-18" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">18<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-18 atomic_mass">18.0268</td>
<td class="gt_row gt_right" headers="stub-18 half_life">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center" headers="stub-18 decay_1">B-</td>
</tr>
<tr>
<th id="stub-19" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">19<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-19 atomic_mass">19.0348</td>
<td class="gt_row gt_right" headers="stub-19 half_life">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center" headers="stub-19 decay_1">B-</td>
</tr>
<tr>
<th id="stub-20" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">20<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-20 atomic_mass">20.0403</td>
<td class="gt_row gt_right" headers="stub-20 half_life">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center" headers="stub-20 decay_1">B-</td>
</tr>
<tr>
<th id="stub-21" class="gt_row gt_left gt_stub" scope="row"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">22<br />
6</span>C</th>
<td class="gt_row gt_right" headers="stub-21 atomic_mass">22.0576</td>
<td class="gt_row gt_right" headers="stub-21 half_life">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center" headers="stub-21 decay_1">B-</td>
</tr>
</tbody>
</table>
