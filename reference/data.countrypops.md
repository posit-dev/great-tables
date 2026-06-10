## data.countrypops


Yearly populations of countries from 1960 to 2022.


`data.countrypops=_read_csv(_countrypops_fname, dtype=_countrypops_dtype)`  


A dataset that presents yearly, total populations of countries. Total population is based on counts of all residents regardless of legal status or citizenship. Country identifiers include the English-language country names, and the 2- and 3-letter ISO 3166-1 country codes. Each row contains a population value for a given year (from 1960 to 2022). Any missing values for populations indicate the non-existence of the entity during that year.


This is a dataset with 13,545 rows and 5 columns.

- `country_name`: The name of the country.
- `country_code_2`, `country_code_3`: The 2- and 3-letter ISO 3166-1 country codes.
- `year`: The year for the population estimate.
- `population`: The population estimate, midway through the year.


    Rows: 13545
    Columns: 5
    $ country_name   <str> 'Aruba', 'Aruba', 'Aruba'
    $ country_code_2 <str> 'AW', 'AW', 'AW'
    $ country_code_3 <str> 'ABW', 'ABW', 'ABW'
    $ year           <i64> 1960, 1961, 1962
    $ population     <i64> 54608, 55811, 56682


<https://data.worldbank.org/indicator/SP.POP.TOTL>
