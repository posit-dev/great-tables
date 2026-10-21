# GT.cols_align()

Set the alignment of one or more columns.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_boxhead.py#L239-L304)

``` python
GT.cols_align(
    align="left",
    columns=None,
)
```

The [cols_align()](../reference/GT.cols_align.md#great_tables.GT.cols_align) method sets the alignment of one or more columns. The `align` argument can be set to one of `"left"`, `"center"`, or `"right"` and the `columns` argument can be used to specify which columns to apply the alignment to. If `columns` is not specified, the alignment is applied to all columns.

## Parameters

`align: str = "left"`  
The alignment to apply. Must be one of `"left"`, `"center"`, or `"right"`.

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. If `None`, the alignment is applied to all columns.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's use the [countrypops](../reference/data.countrypops.md#great_tables.data.countrypops) to create a small table. We can change the alignment of the `population` column with [cols_align()](../reference/GT.cols_align.md#great_tables.GT.cols_align). In this example, the column label and body cells of `population` will be aligned to the left.

``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "San Marino"][
    ["country_name", "year", "population"]
].tail(5)

(
    GT(countrypops_mini, rowname_col="year", groupname_col="country_name")
    .cols_align(align="left", columns="population")
)
```

|            | population |
|------------|------------|
| San Marino |            |
| 2018       | 34156      |
| 2019       | 34178      |
| 2020       | 34007      |
| 2021       | 33745      |
| 2022       | 33660      |
