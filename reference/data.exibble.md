## data.exibble


A toy example table for testing with great_tables: exibble.


`data.exibble=_read_csv(_exibble_fname, dtype=_exibble_dtype)`  


This table contains data of a few different classes, which makes it well-suited for quick experimentation with the functions in this package. It contains only eight rows with numeric and string columns. The last 4 rows contain missing values in the majority of this table's columns (1 missing value per column). The date, time, and datetime columns are string-based dates/times in the familiar ISO 8601 format. The row and group columns provide for unique rownames and two groups (grp_a and grp_b) for experimenting with the `rowname_col` and `groupname_col` arguments.


This is a dataset with 8 rows and 9 columns.

- `num`: A numeric column ordered with increasingly larger values.
- `char`: A string-based column composed of names of fruits from `a` to `h`.
- `fctr`: A factor column with numbers from `1` to `8`, written out.
- `date`, `time`, `datetime`: String-based columns with dates, times, and datetimes.
- `currency`: A numeric column that is useful for testing currency-based formatting.
- `row`: A string-based column in the format `row_X` which can be useful for testing with row labels in a table stub.
- `group`: A string-based column with four `"grp_a"` values and four `"grp_b"` values which can be useful for testing tables that contain row groups.


    Rows: 8
    Columns: 9
    $ num      <f64> 0.1111, 2.222, 33.33
    $ char     <str> 'apricot', 'banana', 'coconut'
    $ fctr     <str> 'one', 'two', 'three'
    $ date     <str> '2015-01-15', '2015-02-15', '2015-03-15'
    $ time     <str> '13:35', '14:40', '15:45'
    $ datetime <str> '2018-01-01 02:22', '2018-02-02 14:33', '2018-03-03 03:44'
    $ currency <f64> 49.95, 17.95, 1.39
    $ row      <str> 'row_1', 'row_2', 'row_3'
    $ group    <str> 'grp_a', 'grp_a', 'grp_a'
