# load_dataset()


Load a dataset from the library as a specified table type.


Usage

``` python
load_dataset(
    dataset="exibble",
    tbl_type="pandas",
)
```


The Great Tables library includes several datasets that can be loaded using the [load_dataset()](load_dataset.md#great_tables.load_dataset) function. The datasets can be loaded as either a Pandas DataFrame or a Polars DataFrame. These datasets are used throughout the documentation's examples and are useful for experimenting with the library's functionality.


## Parameters


`dataset: _DatasetNames = ``"exibble"`  
The name of the dataset to load. Available datasets are: `"countrypops"`, `"sza"`, `"gtcars"`, `"sp500"`, `"pizzaplace"`, `"exibble"`, `"towny"`, `"peeps"`, `"films"`, `"metro"`, `"gibraltar"`, `"constants"`, `"illness"`, `"reactions"`, `"photolysis"`, and `"nuclides"`.

`tbl_type: _TblTypes = ``"pandas"`  
The type of table to generate from the dataset. Options are `"pandas"` (the default) and `"polars"`.


## Returns


`Any`  
A Pandas DataFrame or Polars DataFrame, depending on the value of `tbl_type`.


## Examples

Load the `"exibble"` dataset as a Pandas DataFrame (the default):

``` python
from great_tables.data import load_dataset

exibble_pd = load_dataset(dataset="exibble", tbl_type="pandas")
```

Load the `"gtcars"` dataset as a Polars DataFrame:

``` python
gtcars_pl = load_dataset(dataset="gtcars", tbl_type="polars")
```
