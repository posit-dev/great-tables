# loc.column_header

Target column spanners and column labels.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_locations.py#L266-L314)

``` python
loc.column_header()
```

With [loc.column_header()](../reference/loc.column_header.md#great_tables.loc.column_header), we can target the column header which contains all of the column labels and any spanner labels that are present. This is useful for applying custom styling with the [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style) method. That method has a `locations=` argument and this class should be used there to perform the targeting.

## Returns

`LocColumnHeader`  
A LocColumnHeader object, which is used for a `locations=` argument if specifying the column header of the table.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We create spanner labels through use of the [`tab_spanner()`](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) method; this gives us a column header with a mix of column labels and spanner labels. We will style the entire column header at once by using `locations=loc.column_header()` within [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style).

``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5))
    .tab_spanner(
        label="performance",
        columns=["hp", "trq"]
    )
    .tab_spanner(
        label="make and model",
        columns=["mfr", "model"]
    )
    .tab_style(
        style=[
            style.text(color="white", weight="bold"),
            style.fill(color="steelblue")
        ],
        locations=loc.column_header()
    )
    .fmt_integer(columns=["hp", "trq"])
    .fmt_currency(columns="msrp", decimals=0)
)
```

| make and model |              | performance |     | msrp      |
|----------------|--------------|-------------|-----|-----------|
| mfr            | model        | hp          | trq |           |
| Ford           | GT           | 647         | 550 | \$447,000 |
| Ferrari        | 458 Speciale | 597         | 398 | \$291,744 |
| Ferrari        | 458 Spider   | 562         | 398 | \$263,553 |
| Ferrari        | 458 Italia   | 562         | 398 | \$233,509 |
| Ferrari        | 488 GTB      | 661         | 561 | \$245,400 |
