## data.sp500


Daily S&P 500 Index data from 1950 to 2015.


`data.sp500=_read_csv(_sp500_fname, dtype=_sp500_dtype)`  


This dataset provides daily price indicators for the S&P 500 index from the beginning of 1950 to the end of 2015. The index includes 500 leading companies and captures about 80 percent coverage of available market capitalization.


This is a dataset with 16,607 rows and 7 columns.

- `date`: The date expressed as `Date` values.
- `open`, `high`, `low`, `close`: The day's opening, high, low, and closing prices in USD. The `close` price is adjusted for splits.
- `volume`: The number of trades for the given `date`.
- `adj_close`: The close price adjusted for both dividends and splits.


    Rows: 16607
    Columns: 7
    $ date      <str> '2015-12-31', '2015-12-30', '2015-12-29'
    $ open      <f64> 2060.5901, 2077.3401, 2060.54
    $ high      <f64> 2062.54, 2077.3401, 2081.5601
    $ low       <f64> 2043.62, 2061.97, 2060.54
    $ close     <f64> 2043.9399, 2063.3601, 2078.3601
    $ volume    <f64> 2655330000.0, 2367430000.0, 2542000000.0
    $ adj_close <f64> 2043.9399, 2063.3601, 2078.3601
