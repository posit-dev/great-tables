# data.exibble

A toy example table for testing with great_tables: exibble.

`data.exibble=_read_csv(_exibble_fname, dtype=_exibble_dtype)`

This table contains data of a few different classes, which makes it well-suited for quick experimentation with the functions in this package. It contains only eight rows with numeric and string columns. The last 4 rows contain missing values in the majority of this table's columns (1 missing value per column). The date, time, and datetime columns are string-based dates/times in the familiar ISO 8601 format. The row and group columns provide for unique rownames and two groups (grp_a and grp_b) for experimenting with the `rowname_col` and `groupname_col` arguments.

## Details

This is a dataset with 8 rows and 9 columns.

- `num`: A numeric column ordered with increasingly larger values.
- `char`: A string-based column composed of names of fruits from `a` to `h`.
- `fctr`: A factor column with numbers from `1` to `8`, written out.
- `date`, `time`, `datetime`: String-based columns with dates, times, and datetimes.
- `currency`: A numeric column that is useful for testing currency-based formatting.
- `row`: A string-based column in the format `row_X` which can be useful for testing with row labels in a table stub.
- `group`: A string-based column with four `"grp_a"` values and four `"grp_b"` values which can be useful for testing tables that contain row groups.

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |
