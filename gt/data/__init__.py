import pandas as pd
import pkg_resources

_countrypops_fname = pkg_resources.resource_filename("gt.data", "exibble.csv")
_sza_fname = pkg_resources.resource_filename("gt.data", "sza.csv")
_gtcars_fname = pkg_resources.resource_filename("gt.data", "gtcars.csv")
_sp500_fname = pkg_resources.resource_filename("gt.data", "sp500.csv")
_pizzaplace_fname = pkg_resources.resource_filename("gt.data", "pizzaplace.csv")
_exibble_fname = pkg_resources.resource_filename("gt.data", "exibble.csv")


countrypops: pd.DataFrame = pd.read_csv(_countrypops_fname)  # type: ignore
countrypops.__doc__ = """
Yearly populations of countries from 1960 to 2017

A dataset that presents yearly, total populations of countries. Total population
is based on counts of all residents regardless of legal status or citizenship.
Country identifiers include the English-language country names, and the 2- and
3-letter ISO 3166-1 country codes. Each row contains a population value for a
given year (from 1960 to 2017). Any missing values for populations indicate the
non-existence of the country during that year.
"""


sza: pd.DataFrame = pd.read_csv(_sza_fname)  # type: ignore
sza.__doc__ = """
Twice hourly solar zenith angles by month & latitude

This dataset contains solar zenith angles (in degrees, with the range of 0-90)
every half hour from 04:00 to 12:00, true solar time. This set of values is
calculated on the first of every month for 4 different northern hemisphere
latitudes. For determination of afternoon values, the presented tabulated values
are symmetric about noon.
"""


gtcars: pd.DataFrame = pd.read_csv(_gtcars_fname)  # type: ignore
gtcars.__doc__ = """
Deluxe automobiles from the 2014-2017 period

Expensive and fast cars. Each row describes a car of a certain make, model,
year, and trim. Basic specifications such as horsepower, torque, EPA MPG
ratings, type of drivetrain, and transmission characteristics are provided. The
country of origin for the car manufacturer is also given.
"""


sp500: pd.DataFrame = pd.read_csv(_sp500_fname)  # type: ignore
sp500.__doc__ = """
Daily S&P 500 Index data from 1950 to 2015

This dataset provides daily price indicators for the S&P 500 index from the
beginning of 1950 to the end of 2015. The index includes 500 leading
companies and captures about 80 percent coverage of available market
capitalization.
"""


pizzaplace: pd.DataFrame = pd.read_csv(_pizzaplace_fname)  # type: ignore
pizzaplace.__doc__ = """
A year of pizza sales from a pizza place

A synthetic dataset that describes pizza sales for a pizza place somewhere in
the US. While the contents are artificial, the ingredients used to make the
pizzas are far from it. There are 32 different pizzas that fall into 4 different
categories: classic (classic pizzas: 'You probably had one like it before, but
never like this!'), chicken (pizzas with chicken as a major ingredient: 'Try
the Southwest Chicken Pizza! You'll love it!'), supreme (pizzas that try a
little harder: 'My Soppressata pizza uses only the finest salami from my
personal salumist!'), and, veggie (pizzas without any meats whatsoever: 'My Five
Cheese pizza has so many cheeses, I can only offer it in Large Size!').
"""


exibble: pd.DataFrame = pd.read_csv(_exibble_fname)  # type: ignore
exibble.__doc__ = """
A toy example tibble for testing with gt: exibble

This tibble contains data of a few different classes, which makes it well-suited
for quick experimentation with the functions in this package. It contains only
eight rows with numeric and character columns. The last 4 rows contain missing
values in the majority of this tibble's columns (1 missing value per column).
The date, time, and datetime columns are character-based dates/times in the
familiar ISO 8601 format. The row and group columns provide for unique rownames
and two groups (grp_a and grp_b) for experimenting with the `rowname_col` and
`groupname_col` arguments.
"""
