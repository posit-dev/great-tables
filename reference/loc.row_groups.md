# loc.row_groups

Target row groups.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_locations.py#L494-L545)

``` python
loc.row_groups(rows=None)
```

With [loc.row_groups()](../reference/loc.row_groups.md#great_tables.loc.row_groups) we can target the cells containing the row group labels, which span across the table body. This is useful for applying custom styling with the [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style) method. That method has a `locations=` argument and this class should be used there to perform the targeting.

## Parameters

`rows: RowSelectExpr = None`  
The row groups to target. Can either be a single group name or a series of group names provided in a list. If no groups are specified, all are targeted.

## Returns

`LocRowGroups`  
A LocRowGroups object, which is used for a `locations=` argument if specifying the table's row groups.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style all of the cells comprising the row group labels by using `locations=loc.row_groups()` within [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style).

``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(
        gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
        rowname_col="model",
        groupname_col="mfr"
    )
    .tab_stubhead(label="car")
    .tab_style(
        style=[
            style.text(color="crimson", weight="bold"),
            style.fill(color="lightgray")
        ],
        locations=loc.row_groups()
    )
    .fmt_integer(columns=["hp", "trq"])
    .fmt_currency(columns="msrp", decimals=0)
)
```

| car          | hp  | trq | msrp      |
|--------------|-----|-----|-----------|
| Ford         |     |     |           |
| GT           | 647 | 550 | \$447,000 |
| Ferrari      |     |     |           |
| 458 Speciale | 597 | 398 | \$291,744 |
| 458 Spider   | 562 | 398 | \$263,553 |
| 458 Italia   | 562 | 398 | \$233,509 |
| 488 GTB      | 661 | 561 | \$245,400 |
