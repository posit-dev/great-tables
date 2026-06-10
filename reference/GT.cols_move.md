## GT.cols_move()


Move one or more columns.


Usage

``` python
GT.cols_move(
    columns,
    after,
)
```


On those occasions where you need to move columns this way or that way, we can make use of the [cols_move()](GT.cols_move.md#great_tables.GT.cols_move) method. While it's true that the movement of columns can be done upstream of **Great Tables**, it is much easier and less error prone to use the method provided here. The movement procedure here takes one or more specified columns (in the [columns](loc.body.md#great_tables.loc.body.columns) argument) and places them to the right of a different column (the `after` argument). The ordering of the [columns](loc.body.md#great_tables.loc.body.columns) to be moved is preserved, as is the ordering of all other columns in the table.

The columns supplied in [columns](loc.body.md#great_tables.loc.body.columns) must all exist in the table and none of them can be in the `after` argument. The `after` column must also exist and only one column should be provided here. If you need to place one more or columns at the beginning of the column series, the [cols_move_to_start()](GT.cols_move_to_start.md#great_tables.GT.cols_move_to_start) method should be used. Similarly, if those columns to move should be placed at the end of the column series then use [cols_move_to_end()](GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end).


## Parameters


`columns: SelectExpr`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`after: str`  
The column after which the [columns](loc.body.md#great_tables.loc.body.columns) should be placed. This can be any column name that exists in the table.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a table. We'll choose to position the `population` column after the `country_name` column by using the [cols_move()](GT.cols_move.md#great_tables.GT.cols_move) method.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Japan"][
    ["country_name", "year", "population"]
].tail(5)

(
    GT(countrypops_mini)
    .cols_move(
        columns="population",
        after="country_name"
    )
)
```


| country_name | population | year |
|--------------|------------|------|
| Japan        | 126811000  | 2018 |
| Japan        | 126633000  | 2019 |
| Japan        | 126261000  | 2020 |
| Japan        | 125681593  | 2021 |
| Japan        | 125124989  | 2022 |
