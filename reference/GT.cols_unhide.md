## GT.cols_unhide()


Unhide one or more columns.


Usage

``` python
GT.cols_unhide(columns)
```


The [cols_unhide()](GT.cols_unhide.md#great_tables.GT.cols_unhide) method allows us to unhide one or more columns from appearing in the final output table. This may be important in cases where the user obtains a [GT](GT.md#great_tables.GT) instance with hidden columns and there is motivation to reveal one or more of those.


## Parameters


`columns: SelectExpr`  
The columns to unhide in the output display table. Can either be a single column name or a series of column names provided in a list.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

For this example, we'll use a portion of the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a simple table. We'll hide the `year` column using [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) and then unhide it with [cols_unhide()](GT.cols_unhide.md#great_tables.GT.cols_unhide), ensuring that the `year` column remains visible in the table.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Benin"][
    ["country_name", "year", "population"]
].tail(5)

GT(countrypops_mini).cols_hide(columns="year").cols_unhide(columns="year")
```


| country_name | year | population |
|--------------|------|------------|
| Benin        | 2018 | 11940683   |
| Benin        | 2019 | 12290444   |
| Benin        | 2020 | 12643123   |
| Benin        | 2021 | 12996895   |
| Benin        | 2022 | 13352864   |
