# GT.fmt_units()

Format measurement units.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats.py#L6381-L6531)

``` python
GT.fmt_units(
    columns=None,
    rows=None,
    pattern="{x}",
)
```

The [fmt_units()](../reference/GT.fmt_units.md#great_tables.GT.fmt_units) method lets you better format measurement units in the table body. These must conform to the **Great Tables** *units notation*; as an example of this, `"J Hz^-1 mol^-1"` can be used to generate units for the *molar Planck constant*. The notation here provides several conveniences for defining units, so as long as the values to be formatted conform to this syntax, you'll obtain nicely-formatted inline units. Details pertaining to *units notation* can be found in the section entitled *How to use units notation*.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`pattern: str = "{x}"`  
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

Let's use the [illness](../reference/data.illness.md#great_tables.data.illness) dataset and create a new table. The `units` column happens to contain string values in *units notation* (e.g., `"x10^9 / L"`). Using the [fmt_units()](../reference/GT.fmt_units.md#great_tables.GT.fmt_units) method here will improve the formatting of those measurement units.

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

| Laboratory Findings for the YF Patient |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
|  | Units | Day |  |  |  |  |  |  | Normal Range |  |
|  |  | day_3 | day_4 | day_5 | day_6 | day_7 | day_8 | day_9 | Lower | Upper |
| Viral load | copies per mL | 12,000 | 4,200 | 1,600 | 830 | 760 | 520 | 250 | None | None |
| WBC | ×10⁹/L | 5.26 | 4.26 | 9.92 | 10.49 | 24.77 | 30.26 | 19.03 | 4.0 | 10.0 |
| Neutrophils | ×10⁹/L | 4.87 | 4.72 | 7.92 | 18.21 | 22.08 | 27.17 | 16.59 | 2.0 | 8.0 |
| RBC | ×10¹²/L | 5.72 | 5.98 | 4.23 | 4.83 | 4.12 | 2.68 | 3.32 | 4.0 | 5.5 |
| Hb | g/L | 153 | 135 | 126 | 115 | 75 | 87 | 95 | 120.0 | 160.0 |
| PLT | ×10⁹/L | 67 | 38.6 | 27.4 | 26.2 | 74.1 | 36.2 | 25.6 | 100.0 | 300.0 |
| ALT | U/L | 12,835 | 12,632 | 6,426.7 | 4,263.1 | 1,623.7 | 672.6 | 512.4 | 9.0 | 50.0 |
| AST | U/L | 23,672 | 21,368 | 14,730 | 8,691 | 2,189 | 1,145 | 782.5 | 15.0 | 40.0 |
| TBIL | µmol/L | 117.2 | 143.8 | 137.2 | 158.1 | 127.3 | 105.1 | 163.2 | 0.0 | 18.8 |
| DBIL | µmol/L | 71.4 | 104.6 | 94.6 | 143.9 | 117.8 | 83.6 | 126.3 | 0.0 | 6.8 |
| NH3 | mmol/L | 115.2 | 135.2 | 131 | 176.7 | 84.2 | 72.4 | 91.9 | 10.0 | 47.0 |
| PT | s | 24.6 | 42.4 | 53.7 | 54 | 22.6 | 16.8 | 29.5 | 9.4 | 12.5 |
| APTT | s | 39.2 | 57.2 | 65.9 | 68.3 | 62.4 | 61.7 | 114.7 | 25.1 | 36.5 |
| PTA | % | 41 | 25 | 19 | 14 | 51 | 55 | 31 | 70.0 | 130.0 |
| DD | mg/L | 32.9 | 35.1 | 24.5 | 25.6 | 18.7 | 24.7 | 64.8 | 0.0 | 5.0 |
| FDP | µg/mL | 84.7 | 92.5 | 77.2 | None | None | 157.2 | 291.7 | 0.0 | 5.0 |
| Fibrinogen | mg/dL | 238.1 | 216.8 | 135 | 85.2 | 105.7 | None | 64.3 | 200.0 | 400.0 |
| LDH | U/L | 5,727.3 | 2,622.8 | 2,418.7 | 546.3 | None | 637.2 | None | 80.0 | 285.0 |
| HBDH | None | 5,971.2 | 5,826.9 | 4,826.9 | 2,871.2 | None | 1,163.6 | None | 74.0 | 182.0 |
| CK | U/L | 725 | 792.1 | 760.2 | 1,263.6 | None | 1,294.2 | None | 38.0 | 174.0 |
| CKMB | U/L | 75 | 71 | 58 | 65 | None | 68 | None | None | 25.0 |
| BNP | pg/mL | 37 | None | 73 | None | 482 | 421 | 1,332 | None | 100.0 |
| MYO | ng/mL | 636.6 | 762.1 | 364.6 | 9,999 | 9,999 | 9,999 | 9,999 | 0.0 | 140.0 |
| TnI | ng/mL | 0.03 | 0.04 | 0.05 | 0.16 | 0.14 | 2.84 | 8.94 | 0.0 | 0.028 |
| CREA | µmol/L | 705.6 | 683.6 | 523.6 | 374 | 259.6 | 241.8 | 211.4 | 59.0 | 104.0 |
| BUN | mmol/L | 20.13 | 25.33 | 13.33 | 7.84 | 4.23 | 3.92 | 3.41 | 1.7 | 8.3 |
| AMY | U/L | None | 232.8 | 394.6 | 513.7 | None | 642.9 | 538.9 | 0.0 | 115.0 |
| LPS | U/L | None | 227.6 | 526.9 | 487.9 | None | 437.8 | 414.5 | 5.6 | 51.3 |
| K | mmol/L | 4.19 | 4.64 | 4.34 | 4.83 | 4.53 | 4.37 | 5.74 | 3.5 | 5.3 |
| Na | mmol/L | 136.3 | 135.7 | 142.1 | 140.8 | 144.8 | 143.6 | 144.2 | 137.0 | 147.0 |
| Cl | mmol/L | 91.2 | 92.9 | 96.6 | 99.2 | 102.1 | 99.5 | 105.2 | 99.0 | 110.0 |
| Ca | mmol/L | 1.74 | 1.64 | 2.25 | 2.35 | 2.16 | 2.03 | 2.29 | 2.2 | 2.55 |
| P | mmol/L | 2.96 | 3.23 | 1.47 | 1.15 | 0.97 | 1.57 | 1.63 | 0.81 | 1.45 |
| Lac | mmol/L | 2.32 | 2.42 | 2.19 | 2.66 | None | 6.15 | 5.46 | 1.33 | 1.78 |
| CRP | mg/L | 43.6 | 38.6 | 28.6 | 21.5 | None | 4.3 | 6.4 | 0.0 | 5.0 |
| PCT | ng/mL | 0.57 | None | 1.35 | 2.26 | 1.79 | 3.48 | 5.92 | None | 0.05 |
| IL-6 | None | None | None | 165.9 | 58.3 | 74.6 | 737.2 | None | None | 7.0 |
| CD3+CD4+ | T cells per µL | None | 174 | 153 | 184 | 243 | 370 | 252 | 706.0 | 1125.0 |
| CD3+CD8+ | T cells per µL | None | 142 | 135 | 126 | 132 | 511 | 410 | 323.0 | 836.0 |

The [constants](../reference/data.constants.md#great_tables.data.constants) dataset contains values for hundreds of fundamental physical constants. We'll take a subset of values that have some molar basis and generate a new display table from that. Like the [illness](../reference/data.illness.md#great_tables.data.illness) dataset, this one has a `units` column so, again, the [fmt_units()](../reference/GT.fmt_units.md#great_tables.GT.fmt_units) method will be used to format those units. Here, the preference for typesetting measurement units is to have positive and negative exponents (e.g., not `"<unit_1> / <unit_2>"` but rather `"<unit_1> <unit_2>^-1"`).

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

| Physical Constants Having a Molar Basis |  |  |
|----|----|----|
| Molar Planck Constant | 3.990 × 10⁻¹⁰ | J Hz⁻¹ mol⁻¹ |
| Electron Molar Mass | 5.486 × 10⁻⁷ | kg mol⁻¹ |
| Molar Volume of Silicon | 1.206 × 10⁻⁵ | m³ mol⁻¹ |
| Muon Molar Mass | 1.134 × 10⁻⁴ | kg mol⁻¹ |
| Molar Mass Constant | 1.000 × 10⁻³ | kg mol⁻¹ |
| Proton Molar Mass | 1.007 × 10⁻³ | kg mol⁻¹ |
| Neutron Molar Mass | 1.009 × 10⁻³ | kg mol⁻¹ |
| Tau Molar Mass | 1.908 × 10⁻³ | kg mol⁻¹ |
| Deuteron Molar Mass | 2.014 × 10⁻³ | kg mol⁻¹ |
| Helion Molar Mass | 3.015 × 10⁻³ | kg mol⁻¹ |
| Triton Molar Mass | 3.016 × 10⁻³ | kg mol⁻¹ |
| Alpha Particle Molar Mass | 4.002 × 10⁻³ | kg mol⁻¹ |
| Molar Mass of Carbon-12 | 1.200 × 10⁻² | kg mol⁻¹ |
| Molar Volume of Ideal Gas (273.15 K, 101.325 kpa) | 2.241 × 10⁻² | m³ mol⁻¹ |
| Molar Volume of Ideal Gas (273.15 K, 100 kpa) | 2.271 × 10⁻² | m³ mol⁻¹ |
| Molar Gas Constant | 8.314 | J mol⁻¹ K⁻¹ |
