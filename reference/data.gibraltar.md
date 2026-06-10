## data.gibraltar


Weather conditions in Gibraltar, May 2023.


`data.gibraltar=_read_csv(_gibraltar_fname, dtype=_gibraltar_dtype)`  


The [gibraltar](data.gibraltar.md#great_tables.data.gibraltar) dataset has meteorological data for the Gibraltar Airport Station from May 1 to May 31, 2023. Gibraltar is a British Overseas Territory and city located at the southern end of the Iberian Peninsula, on the Bay of Gibraltar. This weather station is located at the airport (GIB), where it's at an elevation of 5 meters above mean sea level (AMSL).


This is a dataset with 1,431 rows and 10 columns.

- `date`, `time`: The date and time of the observation.
- `temp`, `dew_point`: The air temperature and dew point values, both in degrees Celsius.
- `humidity`: The relative humidity as a value between `0` and `1`
- `wind_dir`, `wind_speed`, `wind_gust`: Observations related to wind. The wind direction is given as the typical 'blowing from' value, simplified to one of 16 compass directions. The wind speed is provided in units of meters per second. If there was a measurable wind gust, the maximum gust speed is recorded as m/s values (otherwise the value is `0`).
- `pressure`: The atmospheric pressure in hectopascals (hPa).
- `condition`: The weather condition.


    Rows: 1431
    Columns: 10
    $ date       <str> '2023-05-01', '2023-05-01', '2023-05-01'
    $ time       <str> '00:20', '00:50', '01:20'
    $ temp       <f64> 18.9, 18.9, 17.8
    $ dew_point  <f64> 12.8, 13.9, 13.9
    $ humidity   <f64> 0.68, 0.73, 0.77
    $ wind_dir   <str> 'W', 'WSW', 'W'
    $ wind_speed <f64> 6.7, 7.2, 6.7
    $ wind_gust  <f64> 0.0, 0.0, 0.0
    $ pressure   <f64> 1015.2, 1015.2, 1014.6
    $ condition  <str> 'Fair', 'Fair', 'Fair'
