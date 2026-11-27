# data.sp500

Daily S&P 500 Index data from 1950 to 2015.

`data.sp500=_read_csv(_sp500_fname, dtype=_sp500_dtype)`

This dataset provides daily price indicators for the S&P 500 index from the beginning of 1950 to the end of 2015. The index includes 500 leading companies and captures about 80 percent coverage of available market capitalization.

## Details

This is a dataset with 16,607 rows and 7 columns.

- `date`: The date expressed as `Date` values.
- `open`, `high`, `low`, `close`: The day's opening, high, low, and closing prices in USD. The `close` price is adjusted for splits.
- `volume`: The number of trades for the given `date`.
- `adj_close`: The close price adjusted for both dividends and splits.

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

| date       | open      | high      | low       | close     | volume       | adj_close |
|------------|-----------|-----------|-----------|-----------|--------------|-----------|
| 2015-12-31 | 2060.5901 | 2062.54   | 2043.62   | 2043.9399 | 2655330000.0 | 2043.9399 |
| 2015-12-30 | 2077.3401 | 2077.3401 | 2061.97   | 2063.3601 | 2367430000.0 | 2063.3601 |
| 2015-12-29 | 2060.54   | 2081.5601 | 2060.54   | 2078.3601 | 2542000000.0 | 2078.3601 |
| 2015-12-28 | 2057.77   | 2057.77   | 2044.2    | 2056.5    | 2492510000.0 | 2056.5    |
| 2015-12-24 | 2063.52   | 2067.3601 | 2058.73   | 2060.99   | 1411860000.0 | 2060.99   |
| 2015-12-23 | 2042.2    | 2064.73   | 2042.2    | 2064.29   | 3484090000.0 | 2064.29   |
| 2015-12-22 | 2023.15   | 2042.74   | 2020.49   | 2038.97   | 3520860000.0 | 2038.97   |
| 2015-12-21 | 2010.27   | 2022.9    | 2005.9301 | 2021.15   | 3760280000.0 | 2021.15   |
| 2015-12-18 | 2040.8101 | 2040.8101 | 2005.33   | 2005.55   | 6683070000.0 | 2005.55   |
| 2015-12-17 | 2073.76   | 2076.3701 | 2041.66   | 2041.89   | 4327390000.0 | 2041.89   |
