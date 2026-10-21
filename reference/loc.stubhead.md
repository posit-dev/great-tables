# loc.stubhead

Target the stubhead.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_locations.py#L217-L258)

``` python
loc.stubhead()
```

With [loc.stubhead()](../reference/loc.stubhead.md#great_tables.loc.stubhead), we can target the part of table that resides both at the top of the stub and also beside the column header. This is useful for applying custom styling with the [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style) method. That method has a `locations=` argument and this class should be used there to perform the targeting.

## Returns

`LocStubhead`  
A LocStubhead object, which is used for a `locations=` argument if specifying the stubhead of the table.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset in a new table. This table contains a stub (produced by setting `rowname_col="model"` in the initial [GT()](../reference/GT.md#great_tables.GT) call). The stubhead is given a label by way of the [`tab_stubhead()`](../reference/GT.tab_stubhead.md#great_tables.GT.tab_stubhead) method and this label can be styled by using `locations=loc.stubhead()` within [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style).

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
        style=style.text(color="red", weight="bold"),
        locations=loc.stubhead()
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
