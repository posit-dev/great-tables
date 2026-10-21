# GT.fmt_chem()

Format chemical formulas.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats.py#L3058-L3247)

``` python
GT.fmt_chem(
    columns=None,
    rows=None,
)
```

With [`fmt_chem()`](../reference/GT.fmt_chem.md#great_tables.GT.fmt_chem) you can format chemical formulas and reactions in the table body. Often the input text will be in a common form representing single compounds (like `"C2H4O"` for acetaldehyde) but chemical reactions can also be used (e.g., `"2 CH3OH -> CH3OCH3 + H2O"`). So long as the text within the targeted cells conforms to the specialized chemistry notation, the appropriate conversions will occur. Details on chemistry notation can be found in the section entitled *How to use chemistry notation*.

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

Let's use the [reactions](../reference/data.reactions.md#great_tables.data.reactions) dataset and create a table of gas-phase reaction rate constants for selected terminal alkenes. The `cmpd_formula` column contains chemical formulas and [`fmt_chem()`](../reference/GT.fmt_chem.md#great_tables.GT.fmt_chem) will render them with properly subscripted numerals. Notice that the column labels for O₃ and NO₃ use the `{%...%}` chemistry notation within [cols_label()](../reference/GT.cols_label.md#great_tables.GT.cols_label).

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

| Gas-Phase Reactions of Selected Terminal Alkenes |  |  |  |  |  |
|----|----|----|----|----|----|
| Alkene | Formula | Reaction Rate Constant at 298 K |  |  |  |
|  |  | OH | O₃ | NO₃ | Cl |
| 1-butene | C₄H₈ | 3.10 × 10⁻¹¹ | 1.00 × 10⁻¹⁷ | 1.30 × 10⁻¹⁴ | 3.00 × 10⁻¹⁰ |
| 1-pentene | C₅H₁₀ | 3.22 × 10⁻¹¹ | 1.06 × 10⁻¹⁷ | 1.50 × 10⁻¹⁴ | 4.20 × 10⁻¹⁰ |
| 1-hexene | C₆H₁₂ | 3.70 × 10⁻¹¹ | 1.15 × 10⁻¹⁷ | 1.80 × 10⁻¹⁴ | 4.00 × 10⁻¹⁰ |
| 1-heptene | C₇H₁₄ | 3.88 × 10⁻¹¹ | 1.16 × 10⁻¹⁷ | 2.00 × 10⁻¹⁴ | 4.40 × 10⁻¹⁰ |
| 1-octene | C₈H₁₆ | 3.44 × 10⁻¹¹ | 1.01 × 10⁻¹⁷ | 2.50 × 10⁻¹⁴ | 5.50 × 10⁻¹⁰ |
| 1-nonene | C₉H₁₈ | 4.32 × 10⁻¹¹ | 9.90 × 10⁻¹⁸ | -- | 5.90 × 10⁻¹⁰ |
| 1-decene | C₁₀H₂₀ | 4.61 × 10⁻¹¹ | 1.11 × 10⁻¹⁷ | 2.60 × 10⁻¹⁴ | -- |
| 1-undecene | C₁₁H₂₂ | 4.79 × 10⁻¹¹ | 1.03 × 10⁻¹⁷ | -- | -- |
| 1-dodecene | C₁₂H₂₄ | 5.03 × 10⁻¹¹ | 1.03 × 10⁻¹⁷ | 2.80 × 10⁻¹⁴ | -- |
| 1-tridecene | C₁₃H₂₆ | 5.09 × 10⁻¹¹ | 9.60 × 10⁻¹⁸ | -- | -- |
| 1-tetradecene | C₁₄H₂₈ | 4.96 × 10⁻¹¹ | 9.70 × 10⁻¹⁸ | 2.80 × 10⁻¹⁴ | -- |

The [photolysis](../reference/data.photolysis.md#great_tables.data.photolysis) dataset contains photolysis pathways where both the `cmpd_formula` and `products` columns hold chemistry notation. We can format both columns with [`fmt_chem()`](../reference/GT.fmt_chem.md#great_tables.GT.fmt_chem) and use [cols_merge()](../reference/GT.cols_merge.md#great_tables.GT.cols_merge) to combine the compound name with its formatted formula.

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

| Photolysis Pathways of Selected VOCs |                 |
|--------------------------------------|-----------------|
| Compound                             | Products        |
| hydrogen peroxide, H₂O₂              | → OH + OH       |
| nitrous acid, HONO                   | → OH + NO       |
| nitric acid, HNO₃                    | → OH + NO₂      |
| acetaldehyde, CH₃CHO                 | → HCO + CH₃     |
| methyl peroxide, CH₃OOH              | → CH₃O + OH     |
| methyl nitrate, CH₃ONO₂              | → CH₃O + NO₂    |
| ethyl nitrate, C₂H₅ONO₂              | → C₂H₅O + NO₂   |
| isopropyl nitrate, i-C₃H₇ONO₂        | → i-C₃H₇O + NO₂ |

The [nuclides](../reference/data.nuclides.md#great_tables.data.nuclides) dataset contains isotope data with nuclide notation (e.g., `"^{12}_{6}C"`) that [`fmt_chem()`](../reference/GT.fmt_chem.md#great_tables.GT.fmt_chem) renders with properly overstruck mass and atomic numbers. Here we show isotopes of hydrogen and carbon.

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

[TABLE]
