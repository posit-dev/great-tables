## GT.cols_move_to_end()


Move one or more columns to the end.


Usage

``` python
GT.cols_move_to_end(columns)
```


We can easily move set of columns to the beginning of the column series and we only need to specify which [columns](loc.body.md#great_tables.loc.body.columns). It's possible to do this upstream of **Great Tables**, however, it is easier with this method and it presents less possibility for error. The ordering of the [columns](loc.body.md#great_tables.loc.body.columns) that are moved to the end is preserved (same with the ordering of all other columns in the table).


## Parameters


`columns: SelectExpr`  
The columns to target. Can either be a single column name or a series of column names provided in a list.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

For this example, we'll use a portion of the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a simple table. Let's move the `year` column, which is the middle column, to the end of the column series with the [cols_move_to_end()](GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end) method.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Benin"][
    ["country_name", "year", "population"]
].tail(5)

GT(countrypops_mini).cols_move_to_end(columns="year")
```


| country_name | population | year |
|--------------|------------|------|
| Benin        | 11940683   | 2018 |
| Benin        | 12290444   | 2019 |
| Benin        | 12643123   | 2020 |
| Benin        | 12996895   | 2021 |
| Benin        | 13352864   | 2022 |


We can also move multiple columns at a time. With the same [countrypops](data.countrypops.md#great_tables.data.countrypops)-based table (`countrypops_mini`), let's move both the `year` and `country_name` columns to the end of the column series.


``` python
GT(countrypops_mini).cols_move_to_end(columns=["year", "country_name"])
```


| population | year | country_name |
|------------|------|--------------|
| 11940683   | 2018 | Benin        |
| 12290444   | 2019 | Benin        |
| 12643123   | 2020 | Benin        |
| 12996895   | 2021 | Benin        |
| 13352864   | 2022 | Benin        |
