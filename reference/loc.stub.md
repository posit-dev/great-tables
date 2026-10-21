# loc.stub

Target the table stub.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_locations.py#L417-L491)

``` python
loc.stub(
    rows=None,
    columns=None,
)
```

With [loc.stub()](../reference/loc.stub.md#great_tables.loc.stub) we can target the cells containing the row labels, which reside in the table stub. This is useful for applying custom styling with the [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style) method. That method has a `locations=` argument and this class should be used there to perform the targeting.

## Parameters

`rows: RowSelectExpr = None`  
The rows to target within the stub. Can either be a single row name or a series of row names provided in a list. If no rows are specified, all rows are targeted. With a hierarchical stub and no `columns=`, row names are matched against the values in every stub column, so the name of an outer level targets all of the rows under it.

`columns: str | list[str] | None = None`  
For a hierarchical stub (where `rowname_col=` is a list of columns), the stub column(s) to target, as a column name or a list of names. By default, all of the stub columns are targeted. When `columns=` is given, row names in `rows=` are matched against the values in those columns (rather than against the row labels), and a cell that is merged across several rows is targeted if any of its rows are.

## Returns

`LocStub`  
A LocStub object, which is used for a `locations=` argument if specifying the table's stub.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style the entire table stub (the row labels) by using `locations=loc.stub()` within [`tab_style()`](../reference/GT.tab_style.md#great_tables.GT.tab_style).

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
        locations=loc.stub()
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

With a hierarchical stub, `columns=` targets a single level. Here, the manufacturer cells for the Ferrari rows are highlighted, leaving the model names as they are.

``` python
(
    GT(gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(6), rowname_col=["mfr", "model"])
    .tab_style(
        style=style.fill(color="lightgray"),
        locations=loc.stub(rows="Ferrari", columns="mfr")
    )
    .fmt_integer(columns=["hp", "trq"])
    .fmt_currency(columns="msrp", decimals=0)
)
```

|         |              | hp  | trq | msrp      |
|---------|--------------|-----|-----|-----------|
| Ford    | GT           | 647 | 550 | \$447,000 |
| Ferrari | 458 Speciale | 597 | 398 | \$291,744 |
|         | 458 Spider   | 562 | 398 | \$263,553 |
|         | 458 Italia   | 562 | 398 | \$233,509 |
|         | 488 GTB      | 661 | 561 | \$245,400 |
|         | California   | 553 | 557 | \$198,973 |
