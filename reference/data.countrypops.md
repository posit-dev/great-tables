# data.countrypops

Yearly populations of countries from 1960 to 2022.

`data.countrypops=_read_csv(_countrypops_fname, dtype=_countrypops_dtype)`

A dataset that presents yearly, total populations of countries. Total population is based on counts of all residents regardless of legal status or citizenship. Country identifiers include the English-language country names, and the 2- and 3-letter ISO 3166-1 country codes. Each row contains a population value for a given year (from 1960 to 2022). Any missing values for populations indicate the non-existence of the entity during that year.

## Details

This is a dataset with 13,545 rows and 5 columns.

- `country_name`: The name of the country.
- `country_code_2`, `country_code_3`: The 2- and 3-letter ISO 3166-1 country codes.
- `year`: The year for the population estimate.
- `population`: The population estimate, midway through the year.

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column. It's a large table (13,545 rows of 5 columns), so it can take a few seconds to load, and longer on a phone.

| country_name | country_code_2 | country_code_3 | year | population |
|--------------|----------------|----------------|------|------------|
| Aruba        | AW             | ABW            | 1960 | 54608      |
| Aruba        | AW             | ABW            | 1961 | 55811      |
| Aruba        | AW             | ABW            | 1962 | 56682      |
| Aruba        | AW             | ABW            | 1963 | 57475      |
| Aruba        | AW             | ABW            | 1964 | 58178      |
| Aruba        | AW             | ABW            | 1965 | 58782      |
| Aruba        | AW             | ABW            | 1966 | 59291      |
| Aruba        | AW             | ABW            | 1967 | 59522      |
| Aruba        | AW             | ABW            | 1968 | 59471      |
| Aruba        | AW             | ABW            | 1969 | 59330      |
