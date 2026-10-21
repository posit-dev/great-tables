# GT.tab_stub_indent()

Control indentation of row labels in the stub.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_tab_stub_indent.py#L13-L124)

``` python
GT.tab_stub_indent(
    rows,
    indent="increase",
)
```

Indentation of row labels is an effective way to establish visual hierarchy in a table stub. [tab_stub_indent()](../reference/GT.tab_stub_indent.md#great_tables.GT.tab_stub_indent) allows for fine-grained control over row label indentation in the stub. You can use an explicit integer indentation level (between `0` and `5`), or use a keyword directive: `"increase"` (the default) or `"decrease"`.

## Parameters

`rows: RowSelectExpr`  
The rows to target for the indentation change. We can supply a list of row indices, a single row index integer, or a callable that takes the table data and returns a boolean Series. When targeting rows by name, provide a list of row label strings.

`indent: Union[int, Literal["increase", "decrease"]] = "increase"`  
An indentation directive or explicit integer level. The keyword `"increase"` (the default) increments the indentation level by `1`; `"decrease"` decrements it by `1`. The minimum indentation level is `0` (no indentation) and the maximum is `5`. An integer value directly sets the indentation level (clamped to the `0`-`5` range).

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's use a subset of the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset to create a gt table with row groups and row labels. We'll use [tab_stub_indent()](../reference/GT.tab_stub_indent.md#great_tables.GT.tab_stub_indent) to add indentation to all the row labels in the stub.

``` python
from great_tables import GT
from great_tables.data import exibble

exibble_mini = exibble[["num", "char", "row", "group"]].head(8)

(
    GT(exibble_mini, rowname_col="row", groupname_col="group")
    .tab_stub_indent(rows=True, indent=2)
)
```

|       | num       | char       |
|-------|-----------|------------|
| grp_a |           |            |
| row_1 | 0.1111    | apricot    |
| row_2 | 2.222     | banana     |
| row_3 | 33.33     | coconut    |
| row_4 | 444.4     | durian     |
| grp_b |           |            |
| row_5 | 5550.0    | None       |
| row_6 | None      | fig        |
| row_7 | 777000.0  | grapefruit |
| row_8 | 8880000.0 | honeydew   |

Here's a more advanced example using the [constants](../reference/data.constants.md#great_tables.data.constants) dataset. We filter for three groups of physical constants and rename the sub-entries to start with `"..."` so it's clear they belong to a parent constant. Then [tab_stub_indent()](../reference/GT.tab_stub_indent.md#great_tables.GT.tab_stub_indent) targets those sub-rows (via a Polars expression) and indents them by 4 levels.

``` python
from great_tables import GT, stub
from great_tables.data import constants
import polars as pl

constants_mini = (
    pl.from_pandas(constants)
    .select(["name", "value", "uncert", "units"])
    .filter(
        pl.col("name").str.starts_with("atomic mass constant")
        | pl.col("name").str.starts_with("Rydberg constant")
        | pl.col("name").str.starts_with("Bohr magneton")
    )
    .with_columns(
        name=pl.when(
            pl.col("name").str.contains("constant ")
            | pl.col("name").str.contains("magneton ")
        )
        .then(pl.col("name").str.replace(r".*?(?:constant |magneton )", "..."))
        .otherwise(pl.col("name"))
    )
)

(
    GT(constants_mini, rowname_col="name")
    .tab_stubhead(label="Physical Constant")
    .tab_stub_indent(
        rows=pl.col("name").str.starts_with("..."),
        indent=4,
    )
    .fmt_scientific(columns=["value", "uncert"])
    .fmt_units(columns="units")
    .cols_label(value="Value", uncert="Uncertainty", units="Units")
    .cols_width(cases={stub: "250px", "value": "150px", "uncert": "150px", "units": "80px"})
)
```

    /home/runner/work/great-tables/great-tables/great_tables/_render_checks.py:37: RenderWarning: Rendering table with .cols_width() in Quarto may result in unexpected behavior. This is because Quarto performs custom table processing. Either use all percentage widths, or set .tab_options(quarto_disable_processing=True) to disable Quarto table processing.
      warnings.warn(

| Physical Constant             | Value        | Uncertainty  | Units   |
|-------------------------------|--------------|--------------|---------|
| atomic mass constant          | 1.66 × 10⁻²⁷ | 5.00 × 10⁻³⁷ | kg      |
| ...energy equivalent          | 1.49 × 10⁻¹⁰ | 4.50 × 10⁻²⁰ | J       |
| ...energy equivalent in MeV   | 9.31 × 10²   | 2.80 × 10⁻⁷  | MeV     |
| Bohr magneton                 | 9.27 × 10⁻²⁴ | 2.80 × 10⁻³³ | J T⁻¹   |
| ...in eV/T                    | 5.79 × 10⁻⁵  | 1.70 × 10⁻¹⁴ | eV T⁻¹  |
| ...in Hz/T                    | 1.40 × 10¹⁰  | 4.20         | Hz T⁻¹  |
| ...in inverse meter per tesla | 4.67 × 10¹   | 1.40 × 10⁻⁸  | m⁻¹ T⁻¹ |
| ...in K/T                     | 6.72 × 10⁻¹  | 2.00 × 10⁻¹⁰ | K T⁻¹   |
| Rydberg constant              | 1.10 × 10⁷   | 2.10 × 10⁻⁵  | m⁻¹     |
| ...times c in Hz              | 3.29 × 10¹⁵  | 6.40 × 10³   | Hz      |
| ...times hc in eV             | 1.36 × 10¹   | 2.60 × 10⁻¹¹ | eV      |
| ...times hc in J              | 2.18 × 10⁻¹⁸ | 4.20 × 10⁻³⁰ | J       |
