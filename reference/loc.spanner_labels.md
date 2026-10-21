# loc.spanner_labels

Target spanner labels.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_locations.py#L361-L414)

``` python
loc.spanner_labels(ids=None)
```

With [loc.spanner_labels()](../reference/loc.spanner_labels.md#great_tables.loc.spanner_labels), we can target the cells containing the spanner labels. This is useful for applying custom styling with the [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style) method. That method has a `locations=` argument and this class should be used there to perform the targeting.

## Parameters

`ids: SelectExpr = None`  
The ID values for the spanner labels to target. A list of one or more ID values is required.

## Returns

`LocSpannerLabels`  
A LocSpannerLabels object, which is used for a `locations=` argument if specifying the table's spanner labels.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We create two spanner labels through two separate calls of the [`tab_spanner()`](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) method. In each of those, the text supplied to `label=` argument is used as the ID value (though they have to be explicitly set via the `id=` argument). We will style only the spanner label having the text `"performance"` by using `locations=loc.spanner_labels(ids=["performance"])` within [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style).

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
        style=style.text(color="blue", weight="bold"),
        locations=loc.spanner_labels(ids=["performance"])
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
