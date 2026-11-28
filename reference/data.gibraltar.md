# data.gibraltar

Weather conditions in Gibraltar, May 2023.

`data.gibraltar=_read_csv(_gibraltar_fname, dtype=_gibraltar_dtype)`

The [gibraltar](../reference/data.gibraltar.md#great_tables.data.gibraltar) dataset has meteorological data for the Gibraltar Airport Station from May 1 to May 31, 2023. Gibraltar is a British Overseas Territory and city located at the southern end of the Iberian Peninsula, on the Bay of Gibraltar. This weather station is located at the airport (GIB), where it's at an elevation of 5 meters above mean sea level (AMSL).

## Details

This is a dataset with 1,431 rows and 10 columns.

- `date`, `time`: The date and time of the observation.
- `temp`, `dew_point`: The air temperature and dew point values, both in degrees Celsius.
- `humidity`: The relative humidity as a value between `0` and `1`
- `wind_dir`, `wind_speed`, `wind_gust`: Observations related to wind. The wind direction is given as the typical 'blowing from' value, simplified to one of 16 compass directions. The wind speed is provided in units of meters per second. If there was a measurable wind gust, the maximum gust speed is recorded as m/s values (otherwise the value is `0`).
- `pressure`: The atmospheric pressure in hectopascals (hPa).
- `condition`: The weather condition.

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

| date | time | temp | dew_point | humidity | wind_dir | wind_speed | wind_gust | pressure | condition |
|----|----|----|----|----|----|----|----|----|----|
| 2023-05-01 | 00:20 | 18.9 | 12.8 | 0.68 | W | 6.7 | 0.0 | 1015.2 | Fair |
| 2023-05-01 | 00:50 | 18.9 | 13.9 | 0.73 | WSW | 7.2 | 0.0 | 1015.2 | Fair |
| 2023-05-01 | 01:20 | 17.8 | 13.9 | 0.77 | W | 6.7 | 0.0 | 1014.6 | Fair |
| 2023-05-01 | 01:50 | 18.9 | 13.9 | 0.73 | W | 6.7 | 0.0 | 1014.6 | Fair |
| 2023-05-01 | 02:20 | 18.9 | 12.8 | 0.68 | WSW | 6.7 | 0.0 | 1014.6 | Fair |
| 2023-05-01 | 02:50 | 17.8 | 12.8 | 0.73 | WSW | 6.7 | 0.0 | 1014.6 | Fair |
| 2023-05-01 | 03:20 | 17.8 | 12.8 | 0.73 | W | 7.2 | 0.0 | 1014.6 | Fair |
| 2023-05-01 | 03:50 | 17.8 | 12.8 | 0.73 | SW | 6.3 | 0.0 | 1013.5 | Fair |
| 2023-05-01 | 04:20 | 18.9 | 12.2 | 0.64 | SW | 4.0 | 0.0 | 1014.6 | Fair |
| 2023-05-01 | 04:50 | 18.9 | 12.2 | 0.64 | WSW | 3.1 | 0.0 | 1014.6 | Fair |
