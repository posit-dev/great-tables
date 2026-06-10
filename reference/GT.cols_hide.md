## GT.cols_hide()


Hide one or more columns.


Usage

``` python
GT.cols_hide(columns)
```


The [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) method allows us to hide one or more columns from appearing in the final output table. While it's possible and often desirable to omit columns from the input table data before introduction to the [GT()](GT.md#great_tables.GT) class, there can be cases where the data in certain columns is useful (as a column reference during formatting of other columns) but the final display of those columns is not necessary.


## Parameters


`columns: SelectExpr`  
The columns to hide in the output display table. Can either be a single column name or a series of column names provided in a list.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

For this example, we'll use a portion of the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a simple table. Let's hide the `year` column with the [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) method.


``` python
from great_tables import GT
from great_tables.data import countrypops

countrypops_mini = countrypops.loc[countrypops["country_name"] == "Benin"][
    ["country_name", "year", "population"]
].tail(5)

GT(countrypops_mini).cols_hide(columns="year")
```


| country_name | population |
|--------------|------------|
| Benin        | 11940683   |
| Benin        | 12290444   |
| Benin        | 12643123   |
| Benin        | 12996895   |
| Benin        | 13352864   |


## Details

The hiding of columns is internally a rendering directive, so, all columns that are 'hidden' are still accessible and useful in any expression provided to a [rows](loc.stub.md#great_tables.loc.stub.rows) argument. Furthermore, the [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) method (as with many of the methods available in **Great Tables**) can be placed anywhere in a chain of calls (acting as a promise to hide columns when the timing is right). However there's perhaps greater readability when placing this call closer to the end of such a chain. The [cols_hide()](GT.cols_hide.md#great_tables.GT.cols_hide) method quietly changes the visible state of a column and doesn't yield warnings when changing the state of already-invisible columns.
