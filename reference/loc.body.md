# loc.body

Target data cells in the table body.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_locations.py#L669-L734)

``` python
loc.body(
    columns=None,
    rows=None,
    mask=None,
)
```

With [loc.body()](../reference/loc.body.md#great_tables.loc.body), we can target the data cells in the table body. This is useful for applying custom styling with the [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style) method. That method has a `locations=` argument and this class should be used there to perform the targeting.

> **Warning**
>
> `mask=` is still experimental.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. The stub and row group columns aren't part of the body: naming one raises an error (use [`loc.stub()`](../reference/loc.stub.md#great_tables.loc.stub) or [`loc.row_groups()`](../reference/loc.row_groups.md#great_tables.loc.row_groups) instead), and column selectors skip them.

`rows: RowSelectExpr = None`  
The rows to target. Can either be a single row name or a series of row names provided in a list.

`mask: PlExpr | None = None`  
The cells to target. If the underlying wrapped DataFrame is a Polars DataFrame, you can pass a Polars expression for cell-based selection. This argument must be used exclusively and cannot be combined with the `columns=` or `rows=` arguments.

## Returns

`LocBody`  
A LocBody object, which is used for a `locations=` argument if specifying the table body.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style all of the body cells by using `locations=loc.body()` within [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style).

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
            style.text(color="darkblue", weight="bold"),
            style.fill(color="gainsboro")
        ],
        locations=loc.body()
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
