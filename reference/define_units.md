# define_units()

With [define_units()](../reference/define_units.md#great_tables.define_units) you can work with a specially-crafted units notation string and emit the

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_helpers.py#L1326-L1473)

``` python
define_units(units_notation)
```

units as HTML (with the `.to_html()` method). This function is useful as a standalone utility and it powers the [fmt_units()](../reference/GT.fmt_units.md#great_tables.GT.fmt_units) method in **Great Tables**.

## Parameters

`units_notation: str`  
A string of units notation.

## Returns

`UnitDefinitionList`  
A list of unit definitions.

## Specification Of Units Notation

The following table demonstrates the various ways in which units can be specified in the `units_notation` string and how the input is processed by the [define_units()](../reference/define_units.md#great_tables.define_units) function. The concluding step for display of the units in HTML is to use the `to_html()` method.

[TABLE]

## Examples

Let's demonstrate a use case where we utilize [define_units()](../reference/define_units.md#great_tables.define_units) to render an equation as the subtitle in the table header, which currently doesn't accept unit notation as input.

We'll start by creating a Polars DataFrame representing the calculations of the equation $`y= a_2x^2 + a_1x + a_0`$.

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

| Linear Algebra                    |     |     |     |     |
|-----------------------------------|-----|-----|-----|-----|
| y={{a_2}}{{x^2}}+{{a_1}}x+{{a_0}} |     |     |     |     |
| x                                 | a₂  | a₁  | a₀  | y   |
| 1                                 | 2   | 3   | 4   | 9   |
| 2                                 | 3   | 4   | 5   | 25  |
| 3                                 | 4   | 5   | 6   | 57  |

To address this, we can create a small helper function, `u2html()`, which wraps a given string in [define_units()](../reference/define_units.md#great_tables.define_units) and emits the units to HTML. Next, we can build the subtitle by applying `u2html()` to the string with unit annotations. Finally, we pass the assembled subtitle string through [html()](../reference/html.md#great_tables.md) to ensure it renders correctly.

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

| Linear Algebra |     |     |     |     |
|----------------|-----|-----|-----|-----|
| y=a₂x²+a₁x+a₀  |     |     |     |     |
| x              | a₂  | a₁  | a₀  | y   |
| 1              | 2   | 3   | 4   | 9   |
| 2              | 3   | 4   | 5   | 25  |
| 3              | 4   | 5   | 6   | 57  |
