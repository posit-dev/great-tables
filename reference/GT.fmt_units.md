## GT.fmt_units()


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

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="11" class="gt_heading gt_title gt_font_normal">Laboratory Findings for the YF Patient</th>
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
<th class="gt_row gt_left gt_stub">Viral load</th>
<td class="gt_row gt_left">copies per mL</td>
<td class="gt_row gt_right">12,000</td>
<td class="gt_row gt_right">4,200</td>
<td class="gt_row gt_right">1,600</td>
<td class="gt_row gt_right">830</td>
<td class="gt_row gt_right">760</td>
<td class="gt_row gt_right">520</td>
<td class="gt_row gt_right">250</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000"></td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">WBC</th>
<td class="gt_row gt_left">×10<span style="white-space:nowrap;"><sup>9</sup></span>/L</td>
<td class="gt_row gt_right">5.26</td>
<td class="gt_row gt_right">4.26</td>
<td class="gt_row gt_right">9.92</td>
<td class="gt_row gt_right">10.49</td>
<td class="gt_row gt_right">24.77</td>
<td class="gt_row gt_right">30.26</td>
<td class="gt_row gt_right">19.03</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">4.0</td>
<td class="gt_row gt_right">10.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Neutrophils</th>
<td class="gt_row gt_left">×10<span style="white-space:nowrap;"><sup>9</sup></span>/L</td>
<td class="gt_row gt_right">4.87</td>
<td class="gt_row gt_right">4.72</td>
<td class="gt_row gt_right">7.92</td>
<td class="gt_row gt_right">18.21</td>
<td class="gt_row gt_right">22.08</td>
<td class="gt_row gt_right">27.17</td>
<td class="gt_row gt_right">16.59</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">2.0</td>
<td class="gt_row gt_right">8.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">RBC</th>
<td class="gt_row gt_left">×10<span style="white-space:nowrap;"><sup>12</sup></span>/L</td>
<td class="gt_row gt_right">5.72</td>
<td class="gt_row gt_right">5.98</td>
<td class="gt_row gt_right">4.23</td>
<td class="gt_row gt_right">4.83</td>
<td class="gt_row gt_right">4.12</td>
<td class="gt_row gt_right">2.68</td>
<td class="gt_row gt_right">3.32</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">4.0</td>
<td class="gt_row gt_right">5.5</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Hb</th>
<td class="gt_row gt_left">g/L</td>
<td class="gt_row gt_right">153</td>
<td class="gt_row gt_right">135</td>
<td class="gt_row gt_right">126</td>
<td class="gt_row gt_right">115</td>
<td class="gt_row gt_right">75</td>
<td class="gt_row gt_right">87</td>
<td class="gt_row gt_right">95</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">120.0</td>
<td class="gt_row gt_right">160.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">PLT</th>
<td class="gt_row gt_left">×10<span style="white-space:nowrap;"><sup>9</sup></span>/L</td>
<td class="gt_row gt_right">67</td>
<td class="gt_row gt_right">38.6</td>
<td class="gt_row gt_right">27.4</td>
<td class="gt_row gt_right">26.2</td>
<td class="gt_row gt_right">74.1</td>
<td class="gt_row gt_right">36.2</td>
<td class="gt_row gt_right">25.6</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">100.0</td>
<td class="gt_row gt_right">300.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">ALT</th>
<td class="gt_row gt_left">U/L</td>
<td class="gt_row gt_right">12,835</td>
<td class="gt_row gt_right">12,632</td>
<td class="gt_row gt_right">6,426.7</td>
<td class="gt_row gt_right">4,263.1</td>
<td class="gt_row gt_right">1,623.7</td>
<td class="gt_row gt_right">672.6</td>
<td class="gt_row gt_right">512.4</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">9.0</td>
<td class="gt_row gt_right">50.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">AST</th>
<td class="gt_row gt_left">U/L</td>
<td class="gt_row gt_right">23,672</td>
<td class="gt_row gt_right">21,368</td>
<td class="gt_row gt_right">14,730</td>
<td class="gt_row gt_right">8,691</td>
<td class="gt_row gt_right">2,189</td>
<td class="gt_row gt_right">1,145</td>
<td class="gt_row gt_right">782.5</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">15.0</td>
<td class="gt_row gt_right">40.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">TBIL</th>
<td class="gt_row gt_left">µmol/L</td>
<td class="gt_row gt_right">117.2</td>
<td class="gt_row gt_right">143.8</td>
<td class="gt_row gt_right">137.2</td>
<td class="gt_row gt_right">158.1</td>
<td class="gt_row gt_right">127.3</td>
<td class="gt_row gt_right">105.1</td>
<td class="gt_row gt_right">163.2</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">0.0</td>
<td class="gt_row gt_right">18.8</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">DBIL</th>
<td class="gt_row gt_left">µmol/L</td>
<td class="gt_row gt_right">71.4</td>
<td class="gt_row gt_right">104.6</td>
<td class="gt_row gt_right">94.6</td>
<td class="gt_row gt_right">143.9</td>
<td class="gt_row gt_right">117.8</td>
<td class="gt_row gt_right">83.6</td>
<td class="gt_row gt_right">126.3</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">0.0</td>
<td class="gt_row gt_right">6.8</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">NH3</th>
<td class="gt_row gt_left">mmol/L</td>
<td class="gt_row gt_right">115.2</td>
<td class="gt_row gt_right">135.2</td>
<td class="gt_row gt_right">131</td>
<td class="gt_row gt_right">176.7</td>
<td class="gt_row gt_right">84.2</td>
<td class="gt_row gt_right">72.4</td>
<td class="gt_row gt_right">91.9</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">10.0</td>
<td class="gt_row gt_right">47.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">PT</th>
<td class="gt_row gt_left">s</td>
<td class="gt_row gt_right">24.6</td>
<td class="gt_row gt_right">42.4</td>
<td class="gt_row gt_right">53.7</td>
<td class="gt_row gt_right">54</td>
<td class="gt_row gt_right">22.6</td>
<td class="gt_row gt_right">16.8</td>
<td class="gt_row gt_right">29.5</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">9.4</td>
<td class="gt_row gt_right">12.5</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">APTT</th>
<td class="gt_row gt_left">s</td>
<td class="gt_row gt_right">39.2</td>
<td class="gt_row gt_right">57.2</td>
<td class="gt_row gt_right">65.9</td>
<td class="gt_row gt_right">68.3</td>
<td class="gt_row gt_right">62.4</td>
<td class="gt_row gt_right">61.7</td>
<td class="gt_row gt_right">114.7</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">25.1</td>
<td class="gt_row gt_right">36.5</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">PTA</th>
<td class="gt_row gt_left">%</td>
<td class="gt_row gt_right">41</td>
<td class="gt_row gt_right">25</td>
<td class="gt_row gt_right">19</td>
<td class="gt_row gt_right">14</td>
<td class="gt_row gt_right">51</td>
<td class="gt_row gt_right">55</td>
<td class="gt_row gt_right">31</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">70.0</td>
<td class="gt_row gt_right">130.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">DD</th>
<td class="gt_row gt_left">mg/L</td>
<td class="gt_row gt_right">32.9</td>
<td class="gt_row gt_right">35.1</td>
<td class="gt_row gt_right">24.5</td>
<td class="gt_row gt_right">25.6</td>
<td class="gt_row gt_right">18.7</td>
<td class="gt_row gt_right">24.7</td>
<td class="gt_row gt_right">64.8</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">0.0</td>
<td class="gt_row gt_right">5.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">FDP</th>
<td class="gt_row gt_left">µg/mL</td>
<td class="gt_row gt_right">84.7</td>
<td class="gt_row gt_right">92.5</td>
<td class="gt_row gt_right">77.2</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">157.2</td>
<td class="gt_row gt_right">291.7</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">0.0</td>
<td class="gt_row gt_right">5.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Fibrinogen</th>
<td class="gt_row gt_left">mg/dL</td>
<td class="gt_row gt_right">238.1</td>
<td class="gt_row gt_right">216.8</td>
<td class="gt_row gt_right">135</td>
<td class="gt_row gt_right">85.2</td>
<td class="gt_row gt_right">105.7</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">64.3</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">200.0</td>
<td class="gt_row gt_right">400.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">LDH</th>
<td class="gt_row gt_left">U/L</td>
<td class="gt_row gt_right">5,727.3</td>
<td class="gt_row gt_right">2,622.8</td>
<td class="gt_row gt_right">2,418.7</td>
<td class="gt_row gt_right">546.3</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">637.2</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">80.0</td>
<td class="gt_row gt_right">285.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">HBDH</th>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">5,971.2</td>
<td class="gt_row gt_right">5,826.9</td>
<td class="gt_row gt_right">4,826.9</td>
<td class="gt_row gt_right">2,871.2</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">1,163.6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">74.0</td>
<td class="gt_row gt_right">182.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">CK</th>
<td class="gt_row gt_left">U/L</td>
<td class="gt_row gt_right">725</td>
<td class="gt_row gt_right">792.1</td>
<td class="gt_row gt_right">760.2</td>
<td class="gt_row gt_right">1,263.6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">1,294.2</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">38.0</td>
<td class="gt_row gt_right">174.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">CKMB</th>
<td class="gt_row gt_left">U/L</td>
<td class="gt_row gt_right">75</td>
<td class="gt_row gt_right">71</td>
<td class="gt_row gt_right">58</td>
<td class="gt_row gt_right">65</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">68</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000"></td>
<td class="gt_row gt_right">25.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">BNP</th>
<td class="gt_row gt_left">pg/mL</td>
<td class="gt_row gt_right">37</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">73</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">482</td>
<td class="gt_row gt_right">421</td>
<td class="gt_row gt_right">1,332</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000"></td>
<td class="gt_row gt_right">100.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">MYO</th>
<td class="gt_row gt_left">ng/mL</td>
<td class="gt_row gt_right">636.6</td>
<td class="gt_row gt_right">762.1</td>
<td class="gt_row gt_right">364.6</td>
<td class="gt_row gt_right">9,999</td>
<td class="gt_row gt_right">9,999</td>
<td class="gt_row gt_right">9,999</td>
<td class="gt_row gt_right">9,999</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">0.0</td>
<td class="gt_row gt_right">140.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">TnI</th>
<td class="gt_row gt_left">ng/mL</td>
<td class="gt_row gt_right">0.03</td>
<td class="gt_row gt_right">0.04</td>
<td class="gt_row gt_right">0.05</td>
<td class="gt_row gt_right">0.16</td>
<td class="gt_row gt_right">0.14</td>
<td class="gt_row gt_right">2.84</td>
<td class="gt_row gt_right">8.94</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">0.0</td>
<td class="gt_row gt_right">0.028</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">CREA</th>
<td class="gt_row gt_left">µmol/L</td>
<td class="gt_row gt_right">705.6</td>
<td class="gt_row gt_right">683.6</td>
<td class="gt_row gt_right">523.6</td>
<td class="gt_row gt_right">374</td>
<td class="gt_row gt_right">259.6</td>
<td class="gt_row gt_right">241.8</td>
<td class="gt_row gt_right">211.4</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">59.0</td>
<td class="gt_row gt_right">104.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">BUN</th>
<td class="gt_row gt_left">mmol/L</td>
<td class="gt_row gt_right">20.13</td>
<td class="gt_row gt_right">25.33</td>
<td class="gt_row gt_right">13.33</td>
<td class="gt_row gt_right">7.84</td>
<td class="gt_row gt_right">4.23</td>
<td class="gt_row gt_right">3.92</td>
<td class="gt_row gt_right">3.41</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">1.7</td>
<td class="gt_row gt_right">8.3</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">AMY</th>
<td class="gt_row gt_left">U/L</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">232.8</td>
<td class="gt_row gt_right">394.6</td>
<td class="gt_row gt_right">513.7</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">642.9</td>
<td class="gt_row gt_right">538.9</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">0.0</td>
<td class="gt_row gt_right">115.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">LPS</th>
<td class="gt_row gt_left">U/L</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">227.6</td>
<td class="gt_row gt_right">526.9</td>
<td class="gt_row gt_right">487.9</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">437.8</td>
<td class="gt_row gt_right">414.5</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">5.6</td>
<td class="gt_row gt_right">51.3</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">K</th>
<td class="gt_row gt_left">mmol/L</td>
<td class="gt_row gt_right">4.19</td>
<td class="gt_row gt_right">4.64</td>
<td class="gt_row gt_right">4.34</td>
<td class="gt_row gt_right">4.83</td>
<td class="gt_row gt_right">4.53</td>
<td class="gt_row gt_right">4.37</td>
<td class="gt_row gt_right">5.74</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">3.5</td>
<td class="gt_row gt_right">5.3</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Na</th>
<td class="gt_row gt_left">mmol/L</td>
<td class="gt_row gt_right">136.3</td>
<td class="gt_row gt_right">135.7</td>
<td class="gt_row gt_right">142.1</td>
<td class="gt_row gt_right">140.8</td>
<td class="gt_row gt_right">144.8</td>
<td class="gt_row gt_right">143.6</td>
<td class="gt_row gt_right">144.2</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">137.0</td>
<td class="gt_row gt_right">147.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Cl</th>
<td class="gt_row gt_left">mmol/L</td>
<td class="gt_row gt_right">91.2</td>
<td class="gt_row gt_right">92.9</td>
<td class="gt_row gt_right">96.6</td>
<td class="gt_row gt_right">99.2</td>
<td class="gt_row gt_right">102.1</td>
<td class="gt_row gt_right">99.5</td>
<td class="gt_row gt_right">105.2</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">99.0</td>
<td class="gt_row gt_right">110.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Ca</th>
<td class="gt_row gt_left">mmol/L</td>
<td class="gt_row gt_right">1.74</td>
<td class="gt_row gt_right">1.64</td>
<td class="gt_row gt_right">2.25</td>
<td class="gt_row gt_right">2.35</td>
<td class="gt_row gt_right">2.16</td>
<td class="gt_row gt_right">2.03</td>
<td class="gt_row gt_right">2.29</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">2.2</td>
<td class="gt_row gt_right">2.55</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">P</th>
<td class="gt_row gt_left">mmol/L</td>
<td class="gt_row gt_right">2.96</td>
<td class="gt_row gt_right">3.23</td>
<td class="gt_row gt_right">1.47</td>
<td class="gt_row gt_right">1.15</td>
<td class="gt_row gt_right">0.97</td>
<td class="gt_row gt_right">1.57</td>
<td class="gt_row gt_right">1.63</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">0.81</td>
<td class="gt_row gt_right">1.45</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Lac</th>
<td class="gt_row gt_left">mmol/L</td>
<td class="gt_row gt_right">2.32</td>
<td class="gt_row gt_right">2.42</td>
<td class="gt_row gt_right">2.19</td>
<td class="gt_row gt_right">2.66</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">6.15</td>
<td class="gt_row gt_right">5.46</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">1.33</td>
<td class="gt_row gt_right">1.78</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">CRP</th>
<td class="gt_row gt_left">mg/L</td>
<td class="gt_row gt_right">43.6</td>
<td class="gt_row gt_right">38.6</td>
<td class="gt_row gt_right">28.6</td>
<td class="gt_row gt_right">21.5</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">4.3</td>
<td class="gt_row gt_right">6.4</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">0.0</td>
<td class="gt_row gt_right">5.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">PCT</th>
<td class="gt_row gt_left">ng/mL</td>
<td class="gt_row gt_right">0.57</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">1.35</td>
<td class="gt_row gt_right">2.26</td>
<td class="gt_row gt_right">1.79</td>
<td class="gt_row gt_right">3.48</td>
<td class="gt_row gt_right">5.92</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000"></td>
<td class="gt_row gt_right">0.05</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">IL-6</th>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">165.9</td>
<td class="gt_row gt_right">58.3</td>
<td class="gt_row gt_right">74.6</td>
<td class="gt_row gt_right">737.2</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000"></td>
<td class="gt_row gt_right">7.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">CD3+CD4+</th>
<td class="gt_row gt_left">T cells per µL</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">174</td>
<td class="gt_row gt_right">153</td>
<td class="gt_row gt_right">184</td>
<td class="gt_row gt_right">243</td>
<td class="gt_row gt_right">370</td>
<td class="gt_row gt_right">252</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">706.0</td>
<td class="gt_row gt_right">1125.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">CD3+CD8+</th>
<td class="gt_row gt_left">T cells per µL</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_right">142</td>
<td class="gt_row gt_right">135</td>
<td class="gt_row gt_right">126</td>
<td class="gt_row gt_right">132</td>
<td class="gt_row gt_right">511</td>
<td class="gt_row gt_right">410</td>
<td class="gt_row gt_right" style="border-left: 1px solid #000000">323.0</td>
<td class="gt_row gt_right">836.0</td>
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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Physical Constants Having a Molar Basis</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Molar Planck Constant</td>
<td class="gt_row gt_right">3.990 × 10<sup>−10</sup></td>
<td class="gt_row gt_left">J Hz<span style="white-space:nowrap;"><sup>−1</sup></span> mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Electron Molar Mass</td>
<td class="gt_row gt_right">5.486 × 10<sup>−7</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Volume of Silicon</td>
<td class="gt_row gt_right">1.206 × 10<sup>−5</sup></td>
<td class="gt_row gt_left">m<span style="white-space:nowrap;"><sup>3</sup></span> mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Muon Molar Mass</td>
<td class="gt_row gt_right">1.134 × 10<sup>−4</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Mass Constant</td>
<td class="gt_row gt_right">1.000 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Proton Molar Mass</td>
<td class="gt_row gt_right">1.007 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Neutron Molar Mass</td>
<td class="gt_row gt_right">1.009 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Tau Molar Mass</td>
<td class="gt_row gt_right">1.908 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Deuteron Molar Mass</td>
<td class="gt_row gt_right">2.014 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Helion Molar Mass</td>
<td class="gt_row gt_right">3.015 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Triton Molar Mass</td>
<td class="gt_row gt_right">3.016 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Alpha Particle Molar Mass</td>
<td class="gt_row gt_right">4.002 × 10<sup>−3</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Mass of Carbon-12</td>
<td class="gt_row gt_right">1.200 × 10<sup>−2</sup></td>
<td class="gt_row gt_left">kg mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Volume of Ideal Gas (273.15 K, 101.325 kpa)</td>
<td class="gt_row gt_right">2.241 × 10<sup>−2</sup></td>
<td class="gt_row gt_left">m<span style="white-space:nowrap;"><sup>3</sup></span> mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Volume of Ideal Gas (273.15 K, 100 kpa)</td>
<td class="gt_row gt_right">2.271 × 10<sup>−2</sup></td>
<td class="gt_row gt_left">m<span style="white-space:nowrap;"><sup>3</sup></span> mol<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
<tr>
<td class="gt_row gt_left">Molar Gas Constant</td>
<td class="gt_row gt_right">8.314</td>
<td class="gt_row gt_left">J mol<span style="white-space:nowrap;"><sup>−1</sup></span> K<span style="white-space:nowrap;"><sup>−1</sup></span></td>
</tr>
</tbody>
</table>
