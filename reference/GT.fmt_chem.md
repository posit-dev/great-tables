# GT.fmt_chem()


Format chemical formulas.


Usage

``` python
GT.fmt_chem(
    columns=None,
    rows=None,
)
```


With `fmt_chem()` you can format chemical formulas and reactions in the table body. Often the input text will be in a common form representing single compounds (like `"C2H4O"` for acetaldehyde) but chemical reactions can also be used (e.g., `"2 CH3OH -> CH3OCH3 + H2O"`). So long as the text within the targeted cells conforms to the specialized chemistry notation, the appropriate conversions will occur. Details on chemistry notation can be found in the section entitled *How to use chemistry notation*.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.


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

Let's use the [reactions](data.reactions.md#great_tables.data.reactions) dataset and create a table of gas-phase reaction rate constants for selected terminal alkenes. The `cmpd_formula` column contains chemical formulas and `fmt_chem()` will render them with properly subscripted numerals. Notice that the column labels for O₃ and NO₃ use the `{%...%}` chemistry notation within [cols_label()](GT.cols_label.md#great_tables.GT.cols_label).


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
#gwvouhmwkh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gwvouhmwkh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gwvouhmwkh p { margin: 0; padding: 0; }
 #gwvouhmwkh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gwvouhmwkh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gwvouhmwkh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gwvouhmwkh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gwvouhmwkh .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gwvouhmwkh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gwvouhmwkh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gwvouhmwkh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gwvouhmwkh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gwvouhmwkh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gwvouhmwkh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gwvouhmwkh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gwvouhmwkh .gt_spanner_row { border-bottom-style: hidden; }
 #gwvouhmwkh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gwvouhmwkh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gwvouhmwkh .gt_from_md> :first-child { margin-top: 0; }
 #gwvouhmwkh .gt_from_md> :last-child { margin-bottom: 0; }
 #gwvouhmwkh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gwvouhmwkh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gwvouhmwkh .gt_indent_1 { text-indent: 5px; }
 #gwvouhmwkh .gt_indent_2 { text-indent: calc(5px * 2); }
 #gwvouhmwkh .gt_indent_3 { text-indent: calc(5px * 3); }
 #gwvouhmwkh .gt_indent_4 { text-indent: calc(5px * 4); }
 #gwvouhmwkh .gt_indent_5 { text-indent: calc(5px * 5); }
 #gwvouhmwkh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gwvouhmwkh .gt_row_group_first td { border-top-width: 2px; }
 #gwvouhmwkh .gt_row_group_first th { border-top-width: 2px; }
 #gwvouhmwkh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gwvouhmwkh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gwvouhmwkh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gwvouhmwkh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gwvouhmwkh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gwvouhmwkh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gwvouhmwkh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gwvouhmwkh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gwvouhmwkh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gwvouhmwkh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gwvouhmwkh .gt_left { text-align: left; }
 #gwvouhmwkh .gt_center { text-align: center; }
 #gwvouhmwkh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gwvouhmwkh .gt_font_normal { font-weight: normal; }
 #gwvouhmwkh .gt_font_bold { font-weight: bold; }
 #gwvouhmwkh .gt_font_italic { font-style: italic; }
 #gwvouhmwkh .gt_super { font-size: 65%; }
 #gwvouhmwkh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gwvouhmwkh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gwvouhmwkh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gwvouhmwkh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gwvouhmwkh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gwvouhmwkh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Gas-Phase Reactions of Selected Terminal Alkenes</th>
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
<td class="gt_row gt_left">1-butene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>4</sub></span>H<span style="white-space:nowrap;"><sub>8</sub></span></td>
<td class="gt_row gt_right">3.10 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">1.00 × 10<sup>−17</sup></td>
<td class="gt_row gt_right">1.30 × 10<sup>−14</sup></td>
<td class="gt_row gt_right">3.00 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left">1-pentene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>5</sub></span>H<span style="white-space:nowrap;"><sub>10</sub></span></td>
<td class="gt_row gt_right">3.22 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">1.06 × 10<sup>−17</sup></td>
<td class="gt_row gt_right">1.50 × 10<sup>−14</sup></td>
<td class="gt_row gt_right">4.20 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left">1-hexene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>6</sub></span>H<span style="white-space:nowrap;"><sub>12</sub></span></td>
<td class="gt_row gt_right">3.70 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">1.15 × 10<sup>−17</sup></td>
<td class="gt_row gt_right">1.80 × 10<sup>−14</sup></td>
<td class="gt_row gt_right">4.00 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left">1-heptene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>7</sub></span>H<span style="white-space:nowrap;"><sub>14</sub></span></td>
<td class="gt_row gt_right">3.88 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">1.16 × 10<sup>−17</sup></td>
<td class="gt_row gt_right">2.00 × 10<sup>−14</sup></td>
<td class="gt_row gt_right">4.40 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left">1-octene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>8</sub></span>H<span style="white-space:nowrap;"><sub>16</sub></span></td>
<td class="gt_row gt_right">3.44 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">1.01 × 10<sup>−17</sup></td>
<td class="gt_row gt_right">2.50 × 10<sup>−14</sup></td>
<td class="gt_row gt_right">5.50 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left">1-nonene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>9</sub></span>H<span style="white-space:nowrap;"><sub>18</sub></span></td>
<td class="gt_row gt_right">4.32 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">9.90 × 10<sup>−18</sup></td>
<td class="gt_row gt_right">--</td>
<td class="gt_row gt_right">5.90 × 10<sup>−10</sup></td>
</tr>
<tr>
<td class="gt_row gt_left">1-decene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>10</sub></span>H<span style="white-space:nowrap;"><sub>20</sub></span></td>
<td class="gt_row gt_right">4.61 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">1.11 × 10<sup>−17</sup></td>
<td class="gt_row gt_right">2.60 × 10<sup>−14</sup></td>
<td class="gt_row gt_right">--</td>
</tr>
<tr>
<td class="gt_row gt_left">1-undecene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>11</sub></span>H<span style="white-space:nowrap;"><sub>22</sub></span></td>
<td class="gt_row gt_right">4.79 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">1.03 × 10<sup>−17</sup></td>
<td class="gt_row gt_right">--</td>
<td class="gt_row gt_right">--</td>
</tr>
<tr>
<td class="gt_row gt_left">1-dodecene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>12</sub></span>H<span style="white-space:nowrap;"><sub>24</sub></span></td>
<td class="gt_row gt_right">5.03 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">1.03 × 10<sup>−17</sup></td>
<td class="gt_row gt_right">2.80 × 10<sup>−14</sup></td>
<td class="gt_row gt_right">--</td>
</tr>
<tr>
<td class="gt_row gt_left">1-tridecene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>13</sub></span>H<span style="white-space:nowrap;"><sub>26</sub></span></td>
<td class="gt_row gt_right">5.09 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">9.60 × 10<sup>−18</sup></td>
<td class="gt_row gt_right">--</td>
<td class="gt_row gt_right">--</td>
</tr>
<tr>
<td class="gt_row gt_left">1-tetradecene</td>
<td class="gt_row gt_left">C<span style="white-space:nowrap;"><sub>14</sub></span>H<span style="white-space:nowrap;"><sub>28</sub></span></td>
<td class="gt_row gt_right">4.96 × 10<sup>−11</sup></td>
<td class="gt_row gt_right">9.70 × 10<sup>−18</sup></td>
<td class="gt_row gt_right">2.80 × 10<sup>−14</sup></td>
<td class="gt_row gt_right">--</td>
</tr>
</tbody>
</table>


The [photolysis](data.photolysis.md#great_tables.data.photolysis) dataset contains photolysis pathways where both the `cmpd_formula` and `products` columns hold chemistry notation. We can format both columns with `fmt_chem()` and use [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge) to combine the compound name with its formatted formula.


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
#nvzgvekzcn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nvzgvekzcn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nvzgvekzcn p { margin: 0; padding: 0; }
 #nvzgvekzcn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nvzgvekzcn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nvzgvekzcn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nvzgvekzcn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nvzgvekzcn .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nvzgvekzcn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvzgvekzcn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nvzgvekzcn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nvzgvekzcn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nvzgvekzcn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nvzgvekzcn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nvzgvekzcn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nvzgvekzcn .gt_spanner_row { border-bottom-style: hidden; }
 #nvzgvekzcn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nvzgvekzcn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nvzgvekzcn .gt_from_md> :first-child { margin-top: 0; }
 #nvzgvekzcn .gt_from_md> :last-child { margin-bottom: 0; }
 #nvzgvekzcn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nvzgvekzcn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nvzgvekzcn .gt_indent_1 { text-indent: 5px; }
 #nvzgvekzcn .gt_indent_2 { text-indent: calc(5px * 2); }
 #nvzgvekzcn .gt_indent_3 { text-indent: calc(5px * 3); }
 #nvzgvekzcn .gt_indent_4 { text-indent: calc(5px * 4); }
 #nvzgvekzcn .gt_indent_5 { text-indent: calc(5px * 5); }
 #nvzgvekzcn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nvzgvekzcn .gt_row_group_first td { border-top-width: 2px; }
 #nvzgvekzcn .gt_row_group_first th { border-top-width: 2px; }
 #nvzgvekzcn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nvzgvekzcn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvzgvekzcn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nvzgvekzcn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nvzgvekzcn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nvzgvekzcn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nvzgvekzcn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nvzgvekzcn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nvzgvekzcn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvzgvekzcn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nvzgvekzcn .gt_left { text-align: left; }
 #nvzgvekzcn .gt_center { text-align: center; }
 #nvzgvekzcn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nvzgvekzcn .gt_font_normal { font-weight: normal; }
 #nvzgvekzcn .gt_font_bold { font-weight: bold; }
 #nvzgvekzcn .gt_font_italic { font-style: italic; }
 #nvzgvekzcn .gt_super { font-size: 65%; }
 #nvzgvekzcn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvzgvekzcn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nvzgvekzcn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nvzgvekzcn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nvzgvekzcn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nvzgvekzcn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_title gt_font_normal">Photolysis Pathways of Selected VOCs</th>
</tr>
<tr class="gt_col_headings">
<th id="cmpd_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Compound</th>
<th id="products" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Products</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">hydrogen peroxide, H<span style="white-space:nowrap;"><sub>2</sub></span>O<span style="white-space:nowrap;"><sub>2</sub></span></td>
<td class="gt_row gt_left">→ OH + OH</td>
</tr>
<tr>
<td class="gt_row gt_left">nitrous acid, HONO</td>
<td class="gt_row gt_left">→ OH + NO</td>
</tr>
<tr>
<td class="gt_row gt_left">nitric acid, HNO<span style="white-space:nowrap;"><sub>3</sub></span></td>
<td class="gt_row gt_left">→ OH + NO<span style="white-space:nowrap;"><sub>2</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left">acetaldehyde, CH<span style="white-space:nowrap;"><sub>3</sub></span>CHO</td>
<td class="gt_row gt_left">→ HCO + CH<span style="white-space:nowrap;"><sub>3</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left">methyl peroxide, CH<span style="white-space:nowrap;"><sub>3</sub></span>OOH</td>
<td class="gt_row gt_left">→ CH<span style="white-space:nowrap;"><sub>3</sub></span>O + OH</td>
</tr>
<tr>
<td class="gt_row gt_left">methyl nitrate, CH<span style="white-space:nowrap;"><sub>3</sub></span>ONO<span style="white-space:nowrap;"><sub>2</sub></span></td>
<td class="gt_row gt_left">→ CH<span style="white-space:nowrap;"><sub>3</sub></span>O + NO<span style="white-space:nowrap;"><sub>2</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left">ethyl nitrate, C<span style="white-space:nowrap;"><sub>2</sub></span>H<span style="white-space:nowrap;"><sub>5</sub></span>ONO<span style="white-space:nowrap;"><sub>2</sub></span></td>
<td class="gt_row gt_left">→ C<span style="white-space:nowrap;"><sub>2</sub></span>H<span style="white-space:nowrap;"><sub>5</sub></span>O + NO<span style="white-space:nowrap;"><sub>2</sub></span></td>
</tr>
<tr>
<td class="gt_row gt_left">isopropyl nitrate, i-C<span style="white-space:nowrap;"><sub>3</sub></span>H<span style="white-space:nowrap;"><sub>7</sub></span>ONO<span style="white-space:nowrap;"><sub>2</sub></span></td>
<td class="gt_row gt_left">→ i-C<span style="white-space:nowrap;"><sub>3</sub></span>H<span style="white-space:nowrap;"><sub>7</sub></span>O + NO<span style="white-space:nowrap;"><sub>2</sub></span></td>
</tr>
</tbody>
</table>


The [nuclides](data.nuclides.md#great_tables.data.nuclides) dataset contains isotope data with nuclide notation (e.g., `"^{12}_{6}C"`) that `fmt_chem()` renders with properly overstruck mass and atomic numbers. Here we show isotopes of hydrogen and carbon.


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
#ppaajtluox table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ppaajtluox thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ppaajtluox p { margin: 0; padding: 0; }
 #ppaajtluox .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ppaajtluox .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ppaajtluox .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ppaajtluox .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ppaajtluox .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ppaajtluox .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ppaajtluox .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ppaajtluox .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ppaajtluox .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ppaajtluox .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ppaajtluox .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ppaajtluox .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ppaajtluox .gt_spanner_row { border-bottom-style: hidden; }
 #ppaajtluox .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ppaajtluox .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ppaajtluox .gt_from_md> :first-child { margin-top: 0; }
 #ppaajtluox .gt_from_md> :last-child { margin-bottom: 0; }
 #ppaajtluox .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ppaajtluox .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ppaajtluox .gt_indent_1 { text-indent: 5px; }
 #ppaajtluox .gt_indent_2 { text-indent: calc(5px * 2); }
 #ppaajtluox .gt_indent_3 { text-indent: calc(5px * 3); }
 #ppaajtluox .gt_indent_4 { text-indent: calc(5px * 4); }
 #ppaajtluox .gt_indent_5 { text-indent: calc(5px * 5); }
 #ppaajtluox .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ppaajtluox .gt_row_group_first td { border-top-width: 2px; }
 #ppaajtluox .gt_row_group_first th { border-top-width: 2px; }
 #ppaajtluox .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ppaajtluox .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ppaajtluox .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ppaajtluox .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ppaajtluox .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ppaajtluox .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ppaajtluox .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ppaajtluox .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ppaajtluox .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ppaajtluox .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ppaajtluox .gt_left { text-align: left; }
 #ppaajtluox .gt_center { text-align: center; }
 #ppaajtluox .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ppaajtluox .gt_font_normal { font-weight: normal; }
 #ppaajtluox .gt_font_bold { font-weight: bold; }
 #ppaajtluox .gt_font_italic { font-style: italic; }
 #ppaajtluox .gt_super { font-size: 65%; }
 #ppaajtluox .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ppaajtluox .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ppaajtluox .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ppaajtluox .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ppaajtluox .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ppaajtluox .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Isotopes of Hydrogen and Carbon</th>
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
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">1<br />
1</span>H</th>
<td class="gt_row gt_right">1.0078</td>
<td class="gt_row gt_right"><strong>STABLE</strong></td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">2<br />
1</span>H</th>
<td class="gt_row gt_right">2.0141</td>
<td class="gt_row gt_right"><strong>STABLE</strong></td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">3<br />
1</span>H</th>
<td class="gt_row gt_right">3.0160</td>
<td class="gt_row gt_right">3.89 × 10<sup>8</sup></td>
<td class="gt_row gt_center">B-</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">4<br />
1</span>H</th>
<td class="gt_row gt_right">4.0264</td>
<td class="gt_row gt_right">--</td>
<td class="gt_row gt_center">N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">5<br />
1</span>H</th>
<td class="gt_row gt_right">5.0353</td>
<td class="gt_row gt_right">8.61 × 10<sup>−23</sup></td>
<td class="gt_row gt_center">2N</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">6<br />
1</span>H</th>
<td class="gt_row gt_right">6.0450</td>
<td class="gt_row gt_right">2.94 × 10<sup>−22</sup></td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">7<br />
1</span>H</th>
<td class="gt_row gt_right">7.0527</td>
<td class="gt_row gt_right">5.07 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">8<br />
6</span>C</th>
<td class="gt_row gt_right">8.0376</td>
<td class="gt_row gt_right">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2P</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">9<br />
6</span>C</th>
<td class="gt_row gt_right">9.0310</td>
<td class="gt_row gt_right">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">EC+B+</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">10<br />
6</span>C</th>
<td class="gt_row gt_right">10.0169</td>
<td class="gt_row gt_right">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">EC+B+</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">11<br />
6</span>C</th>
<td class="gt_row gt_right">11.0114</td>
<td class="gt_row gt_right">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">EC+B+</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">12<br />
6</span>C</th>
<td class="gt_row gt_right">12.0000</td>
<td class="gt_row gt_right"><strong>STABLE</strong></td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">13<br />
6</span>C</th>
<td class="gt_row gt_right">13.0034</td>
<td class="gt_row gt_right"><strong>STABLE</strong></td>
<td class="gt_row gt_center">--</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">14<br />
6</span>C</th>
<td class="gt_row gt_right">14.0032</td>
<td class="gt_row gt_right">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">B-</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">15<br />
6</span>C</th>
<td class="gt_row gt_right">15.0106</td>
<td class="gt_row gt_right">2.45</td>
<td class="gt_row gt_center">B-</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">16<br />
6</span>C</th>
<td class="gt_row gt_right">16.0147</td>
<td class="gt_row gt_right">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">B-</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">17<br />
6</span>C</th>
<td class="gt_row gt_right">17.0226</td>
<td class="gt_row gt_right">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">B-</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">18<br />
6</span>C</th>
<td class="gt_row gt_right">18.0268</td>
<td class="gt_row gt_right">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">B-</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">19<br />
6</span>C</th>
<td class="gt_row gt_right">19.0348</td>
<td class="gt_row gt_right">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">B-</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">20<br />
6</span>C</th>
<td class="gt_row gt_right">20.0403</td>
<td class="gt_row gt_right">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">B-</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub"><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">22<br />
6</span>C</th>
<td class="gt_row gt_right">22.0576</td>
<td class="gt_row gt_right">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">B-</td>
</tr>
</tbody>
</table>
