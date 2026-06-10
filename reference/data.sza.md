## data.sza


Twice hourly solar zenith angles by month & latitude.


`data.sza=_read_csv(_sza_fname, dtype=_sza_dtype)`  


This dataset contains solar zenith angles (in degrees, with the range of 0-90) every half hour from 04:00 to 12:00, true solar time. This set of values is calculated on the first of every month for 4 different northern hemisphere latitudes. For determination of afternoon values, the presented tabulated values are symmetric about noon.

The solar zenith angle (SZA) is one measure that helps to describe the sun's path across the sky. It's defined as the angle of the sun relative to a line perpendicular to the earth's surface. It is useful to calculate the SZA in relation to the true solar time. True solar time relates to the position of the sun with respect to the observer, which is different depending on the exact longitude. For example, two hours before the sun crosses the meridian (the highest point it would reach that day) corresponds to a true solar time of 10 a.m. The SZA has a strong dependence on the observer's latitude. For example, at a latitude of 50 degrees N at the start of January, the noontime SZA is 73.0 but a different observer at 20 degrees N would measure the noontime SZA to be 43.0 degrees.


This is a dataset with 816 rows and 4 columns.

- `latitude`: The latitude in decimal degrees for the observations.
- `month`: The measurement month. All calculations where conducted for the first day of each month.
- `tst`: The true solar time at the given `latitude` and date (first of `month`) for which the solar zenith angle is calculated.
- [sza](data.sza.md#great_tables.data.sza): The solar zenith angle in degrees, where missing values indicate that sunrise hadn't yet occurred by the `tst` value.


    Rows: 816
    Columns: 4
    $ latitude <str> '20', '20', '20'
    $ month    <str> 'jan', 'jan', 'jan'
    $ tst      <str> '0400', '0430', '0500'
    $ sza      <f64> None, None, None


Calculated Actinic Fluxes (290 - 700 nm) for Air Pollution Photochemistry Applications (Peterson, 1976), available at: <https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9100JA26.txt>.
