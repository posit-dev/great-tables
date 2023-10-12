import pandas as pd
import pkg_resources

_countrypops_fname = pkg_resources.resource_filename('gt.data', 'countrypops.csv')
_countrypops_dtype = {
    'country_name': 'object',
    'country_code_2': 'object',
    'country_code_3': 'object',
    'year': 'int64',
    'population': 'int64',
}

_sza_fname = pkg_resources.resource_filename('gt.data', 'sza.csv')
_sza_dtype = {
    'latitude': 'object',
    'month': 'object',
    'tst': 'object',
    'sza': 'float64',
}

_gtcars_fname = pkg_resources.resource_filename('gt.data', 'gtcars.csv')
_gtcars_dtype = {
    'mfr': 'object',
    'model': 'object',
    'year': 'int64',
    'trim': 'object',
    'bdy_style': 'object',
    'hp': 'int64',
    'hp_rpm': 'int64',
    'trq': 'int64',
    'trq_rpm': 'int64',
    'mpg_c': 'int64',
    'mpg_h': 'int64',
    'drivetrain': 'object',
    'trsmn': 'object',
    'ctry_origin': 'object',
    'msrp': 'int64'
}

_sp500_fname = pkg_resources.resource_filename('gt.data', 'sp500.csv')
_sp500_dtype = {
    'date': 'object',
    'open': 'int64',
    'high': 'int64',
    'low': 'int64',
    'close': 'int64',
    'volume': 'int64',
    'adj_close': 'float64',
}

_pizzaplace_fname = pkg_resources.resource_filename('gt.data', 'pizzaplace.csv')
_pizzaplace_dtype = {
    'id': 'object',
    'date': 'object',
    'time': 'object',
    'name': 'object',
    'size': 'object',
    'type': 'object',
    'price': 'float64',
}

_exibble_fname = pkg_resources.resource_filename('gt.data', 'exibble.csv')
_exibble_dtype = {
    'num': 'float64',
    'char': 'object',
    'fctr': 'object',
    'date': 'object',
    'time': 'object',
    'datetime': 'object',
    'currency': 'float64',
    'row': 'object',
    'group': 'object',
}

_towny_fname = pkg_resources.resource_filename('gt.data', 'towny.csv')
_towny_dtype = {
    'name': 'object',
    'website': 'object',
    'status': 'object',
    'csd_type': 'object',
    'census_div': 'object',
    'latitude': 'float64',
    'longitude': 'float64',
    'land_area_km2': 'float64',
    'population_1996': 'int64',
    'population_2001': 'int64',
    'population_2006': 'int64',
    'population_2011': 'int64',
    'population_2016': 'int64',
    'population_2021': 'int64',
    'density_1996': 'float64',
    'density_2001': 'float64',
    'density_2006': 'float64',
    'density_2011': 'float64',
    'density_2016': 'float64',
    'density_2021': 'float64',
    'pop_change_1996_2001_pct': 'float64',
    'pop_change_2001_2006_pct': 'float64',
    'pop_change_2006_2011_pct': 'float64',
    'pop_change_2011_2016_pct': 'float64',
    'pop_change_2016_2021_pct': 'float64',
}

_metro_fname = pkg_resources.resource_filename('gt.data', 'metro.csv')
_metro_dtype = {
    'name': 'object',
    'caption': 'object',
    'lines': 'object',
    'connect_rer': 'object',
    'connect_tramway': 'object',
    'connect_transilien': 'object',
    'connect_other': 'object',
    'passengers': 'int64',
    'latitude': 'float64',
    'longitude': 'float64',
    'location': 'object',
}

_constants_fname = pkg_resources.resource_filename('gt.data', 'constants.csv')
_constants_dtype = {
    'name': 'object',
    'value': 'float64',
    'uncert': 'float64',
    'sf_value': 'int64',
    'sf_uncert': 'int64',
    'units': 'object',
}

_illness_fname = pkg_resources.resource_filename('gt.data', 'illness.csv')
_illness_dtype = {
    'test': 'object',
    'units': 'object',
    'day_3': 'float64',
    'day_4': 'float64',
    'day_5': 'float64',
    'day_6': 'float64',
    'day_7': 'float64',
    'day_8': 'float64',
    'day_9': 'float64',
    'norm_l': 'float64',
    'norm_u': 'float64',
}

countrypops: pd.DataFrame = pd.read_csv(_countrypops_fname, dtype=_countrypops_dtype)  # type: ignore
countrypops.__doc__ = '''
Yearly populations of countries from 1960 to 2022

A dataset that presents yearly, total populations of countries. Total population
is based on counts of all residents regardless of legal status or citizenship.
Country identifiers include the English-language country names, and the 2- and
3-letter ISO 3166-1 country codes. Each row contains a population value for a
given year (from 1960 to 2022). Any missing values for populations indicate the
non-existence of the entity during that year.
'''


sza: pd.DataFrame = pd.read_csv(_sza_fname, dtype=_sza_dtype)  # type: ignore
sza.__doc__ = '''
Twice hourly solar zenith angles by month & latitude

This dataset contains solar zenith angles (in degrees, with the range of 0-90)
every half hour from 04:00 to 12:00, true solar time. This set of values is
calculated on the first of every month for 4 different northern hemisphere
latitudes. For determination of afternoon values, the presented tabulated values
are symmetric about noon.
'''


gtcars: pd.DataFrame = pd.read_csv(_gtcars_fname, dtype=_gtcars_dtype)  # type: ignore
gtcars.__doc__ = '''
Deluxe automobiles from the 2014-2017 period

Expensive and fast cars. Each row describes a car of a certain make, model,
year, and trim. Basic specifications such as horsepower, torque, EPA MPG
ratings, type of drivetrain, and transmission characteristics are provided. The
country of origin for the car manufacturer is also given.
'''


sp500: pd.DataFrame = pd.read_csv(_sp500_fname, dtype=_sp500_dtype)  # type: ignore
sp500.__doc__ = '''
Daily S&P 500 Index data from 1950 to 2015

This dataset provides daily price indicators for the S&P 500 index from the
beginning of 1950 to the end of 2015. The index includes 500 leading
companies and captures about 80 percent coverage of available market
capitalization.
'''


pizzaplace: pd.DataFrame = pd.read_csv(_pizzaplace_fname, dtype=_pizzaplace_dtype)  # type: ignore
pizzaplace.__doc__ = '''
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
'''


exibble: pd.DataFrame = pd.read_csv(_exibble_fname, dtype=_exibble_dtype)  # type: ignore
exibble.__doc__ = '''
A toy example table for testing with gt: exibble

This table contains data of a few different classes, which makes it well-suited
for quick experimentation with the functions in this package. It contains only
eight rows with numeric and character columns. The last 4 rows contain missing
values in the majority of this table's columns (1 missing value per column).
The date, time, and datetime columns are character-based dates/times in the
familiar ISO 8601 format. The row and group columns provide for unique rownames
and two groups (grp_a and grp_b) for experimenting with the `rowname_col` and
`groupname_col` arguments.
'''


towny: pd.DataFrame = pd.read_csv(_towny_fname, dtype=_towny_dtype)  # type: ignore
towny.__doc__ = '''
Populations of all municipalities in Ontario from 1996 to 2021

A dataset containing census population data from six census years (1996 to 2021)
for all 414 of Ontario's local municipalities. The Municipal Act of Ontario
(2001) defines a local municipality as "a single-tier municipality or a
lower-tier municipality". There are 173 single-tier municipalities and 241
lower-tier municipalities representing 99 percent of Ontario's population and 17
percent of its land use.

In the towny dataset we include information specific to each municipality such
as location (in the latitude and longitude columns), their website URLs, their
classifications, and land area sizes according to 2021 boundaries. Additionally,
there are computed columns containing population density values for each census
year and population change values from adjacent census years.
'''


metro: pd.DataFrame = pd.read_csv(_metro_fname, dtype=_metro_dtype)  # type: ignore
metro.__doc__ = '''
The stations of the Paris Metro

A dataset with information on all 308 Paris Metro stations as of February 2023.
Each record represents a station, describing which Metro lines are serviced by
the station, which other connections are available, and annual passenger
volumes. Basic location information is provided for each station in terms where
they reside on a municipal level, and, through latitude/longitude coordinates.

The system has 16 lines (numbered from 1 to 14, with two additional lines: 3bis
and 7bis) and covers over 200 kilometers of track. The Metro runs on standard
gauge tracks (1,435 mm) and operates using a variety of rolling stock, including
rubber-tired trains and steel-wheeled trains (which are far more common).

The Metro is operated by the RATP, which also operates other transit systems in
the region, including buses, trams, and the RER. The RER is an important
component of the region's transit infrastructure, and several RER stations have
connectivity with the Metro. This integration allows passengers to transfer
between those two systems seamlessly. The Metro also has connections to the
Transilien rail network, tramway stations, several major train stations (e.g.,
Gare du Nord, Gare de l'Est, etc.), and many bus lines.
'''

constants: pd.DataFrame = pd.read_csv(_constants_fname, dtype=_constants_dtype)  # type: ignore
constants.__doc__ = '''
The fundamental physical constants

This dataset contains values for over 300 basic fundamental constants in nature.
The values originate from the 2018 adjustment which is based on the latest
relevant precision measurements and improvements of theoretical calculations.
Such work has been carried out under the authority of the Task Group on
Fundamental Constants (TGFC) of the Committee on Data of the International
Science Council (CODATA). These updated values became available on May 20, 2019.
They are published at http://physics.nist.gov/constants, a website of the
Fundamental Constants Data Center of the National Institute of Standards and
Technology (NIST), Gaithersburg, Maryland, USA.
'''


illness: pd.DataFrame = pd.read_csv(_illness_fname, dtype=_illness_dtype)  # type: ignore
illness.__doc__ = '''
Lab tests for one suffering from an illness

A dataset with artificial daily lab data for a patient with Yellow Fever (YF).
The table comprises laboratory findings for the patient from day 3 of illness
onset until day 9 (after which the patient died). YF viral DNA was found in
serum samples from day 3, where the viral load reached 14,000 copies per mL.
Several medical interventions were taken to help the patient, including the
administration of fresh frozen plasma, platelets, red cells, and coagulation
factor VIII. The patient also received advanced support treatment in the form of
mechanical ventilation and plasmapheresis. Though the patient's temperature
remained stable during their illness, unfortunately, the patient's condition did
not improve. On days 7 and 8, the patient's health declined further, with
symptoms such as nosebleeds, gastrointestinal bleeding, and hematoma.
'''
