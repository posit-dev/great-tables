from importlib_resources import files

try:
    import pandas as pd
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Currently, importing great_tables.data requires pandas. "
        "This will change in the future. Most of great_tables can be used without pandas."
    )


DATA_MOD = files("great_tables.data")

_countrypops_fname = DATA_MOD / "01-countrypops.csv"
_countrypops_dtype = {
    "country_name": "object",
    "country_code_2": "object",
    "country_code_3": "object",
    "year": "Int64",
    "population": "Int64",
}

_sza_fname = DATA_MOD / "02-sza.csv"
_sza_dtype = {
    "latitude": "object",
    "month": "object",
    "tst": "object",
    "sza": "float64",
}

_gtcars_fname = DATA_MOD / "03-gtcars.csv"
_gtcars_dtype = {
    "mfr": "object",
    "model": "object",
    "year": "int64",
    "trim": "object",
    "bdy_style": "object",
    "hp": "float64",
    "hp_rpm": "float64",
    "trq": "float64",
    "trq_rpm": "float64",
    "mpg_c": "float64",
    "mpg_h": "float64",
    "drivetrain": "object",
    "trsmn": "object",
    "ctry_origin": "object",
    "msrp": "float64",
}

_sp500_fname = DATA_MOD / "04-sp500.csv"
_sp500_dtype = {
    "date": "object",
    "open": "float64",
    "high": "float64",
    "low": "float64",
    "close": "float64",
    "volume": "float64",
    "adj_close": "float64",
}

_pizzaplace_fname = DATA_MOD / "05-pizzaplace.csv"
_pizzaplace_dtype = {
    "id": "object",
    "date": "object",
    "time": "object",
    "name": "object",
    "size": "object",
    "type": "object",
    "price": "float64",
}

_exibble_fname = DATA_MOD / "06-exibble.csv"
_exibble_dtype = {
    "num": "float64",
    "char": "object",
    "fctr": "object",
    "date": "object",
    "time": "object",
    "datetime": "object",
    "currency": "float64",
    "row": "object",
    "group": "object",
}

_towny_fname = DATA_MOD / "07-towny.csv"
_towny_dtype = {
    "name": "object",
    "website": "object",
    "status": "object",
    "csd_type": "object",
    "census_div": "object",
    "latitude": "float64",
    "longitude": "float64",
    "land_area_km2": "float64",
    "population_1996": "Int64",
    "population_2001": "Int64",
    "population_2006": "Int64",
    "population_2011": "Int64",
    "population_2016": "Int64",
    "population_2021": "Int64",
    "density_1996": "float64",
    "density_2001": "float64",
    "density_2006": "float64",
    "density_2011": "float64",
    "density_2016": "float64",
    "density_2021": "float64",
    "pop_change_1996_2001_pct": "float64",
    "pop_change_2001_2006_pct": "float64",
    "pop_change_2006_2011_pct": "float64",
    "pop_change_2011_2016_pct": "float64",
    "pop_change_2016_2021_pct": "float64",
}

_peeps_fname = DATA_MOD / "08-peeps.csv"
_peeps_dtype = {
    "name_given": "object",
    "name_family": "object",
    "address": "object",
    "city": "object",
    "state_prov": "object",
    "postcode": "object",
    "country": "object",
    "email_addr": "object",
    "phone_number": "object",
    "country_code": "object",
    "gender": "object",
    "dob": "object",
    "height_cm": "Int64",
    "weight_kg": "float64",
}

_films_fname = DATA_MOD / "09-films.csv"
_films_dtype = {
    "year": "Int64",
    "title": "object",
    "original_title": "object",
    "director": "object",
    "languages": "object",
    "countries_of_origin": "object",
    "run_time": "object",
    "imdb_url": "object",
}

_metro_fname = DATA_MOD / "10-metro.csv"
_metro_dtype = {
    "name": "object",
    "caption": "object",
    "lines": "object",
    "connect_rer": "object",
    "connect_tramway": "object",
    "connect_transilien": "object",
    "connect_other": "object",
    "passengers": "Int64",
    "latitude": "float64",
    "longitude": "float64",
    "location": "object",
}

_gibraltar_fname = DATA_MOD / "11-gibraltar.csv"
_gibraltar_dtype = {
    "date": "object",
    "time": "object",
    "temp": "float64",
    "dew_point": "float64",
    "humidity": "float64",
    "wind_dir": "object",
    "wind_speed": "float64",
    "wind_gust": "float64",
    "pressure": "float64",
    "condition": "object",
}

_constants_fname = DATA_MOD / "12-constants.csv"
_constants_dtype = {
    "name": "object",
    "value": "float64",
    "uncert": "float64",
    "sf_value": "Int64",
    "sf_uncert": "Int64",
    "units": "object",
}

_illness_fname = DATA_MOD / "13-illness.csv"
_illness_dtype = {
    "test": "object",
    "units": "object",
    "day_3": "float64",
    "day_4": "float64",
    "day_5": "float64",
    "day_6": "float64",
    "day_7": "float64",
    "day_8": "float64",
    "day_9": "float64",
    "norm_l": "float64",
    "norm_u": "float64",
}

_reactions_fname = DATA_MOD / "14-reactions.csv"
_reactions_dtype = {
    "cmpd_name": "object",
    "cmpd_mwt": "float64",
    "cmpd_formula": "object",
    "cmpd_type": "object",
    "cmpd_smiles": "object",
    "cmpd_inchi": "object",
    "cmpd_inchikey": "object",
    "OH_k298": "float64",
    "OH_uncert": "float64",
    "OH_u_fac": "float64",
    "OH_A": "float64",
    "OH_B": "float64",
    "OH_n": "float64",
    "OH_t_low": "float64",
    "OH_t_high": "float64",
    "O3_k298": "float64",
    "O3_uncert": "float64",
    "O3_u_fac": "float64",
    "O3_A": "float64",
    "O3_B": "float64",
    "O3_n": "float64",
    "O3_t_low": "float64",
    "O3_t_high": "float64",
    "NO3_k298": "float64",
    "NO3_uncert": "float64",
    "NO3_u_fac": "float64",
    "NO3_A": "float64",
    "NO3_B": "float64",
    "NO3_n": "float64",
    "NO3_t_low": "float64",
    "NO3_t_high": "float64",
    "Cl_k298": "float64",
    "Cl_uncert": "float64",
    "Cl_u_fac": "float64",
    "Cl_A": "float64",
    "Cl_B": "float64",
    "Cl_n": "float64",
    "Cl_t_low": "float64",
    "Cl_t_high": "float64",
}

_photolysis_fname = DATA_MOD / "15-photolysis.csv"
_photolysis_dtype = {
    "cmpd_name": "object",
    "cmpd_formula": "object",
    "products": "object",
    "type": "object",
    "l": "float64",
    "m": "float64",
    "n": "float64",
    "quantum_yield": "float64",
    "wavelength_nm": "object",
    "sigma_298_cm2": "object",
}

_nuclides_fname = DATA_MOD / "16-nuclides.csv"
_nuclides_dtype = {
    "nuclide": "object",
    "z": "Int64",
    "n": "Int64",
    "element": "object",
    "radius": "float64",
    "radius_uncert": "float64",
    "abundance": "float64",
    "abundance_uncert": "float64",
    "is_stable": "object",
    "half_life": "float64",
    "half_life_uncert": "float64",
    "isospin": "object",
    "decay_1": "object",
    "decay_1_pct": "float64",
    "decay_1_pct_uncert": "float64",
    "decay_2": "object",
    "decay_2_pct": "float64",
    "decay_2_pct_uncert": "float64",
    "decay_3": "object",
    "decay_3_pct": "float64",
    "decay_3_pct_uncert": "float64",
    "magnetic_dipole": "float64",
    "magnetic_dipole_uncert": "float64",
    "electric_quadrupole": "float64",
    "electric_quadrupole_uncert": "float64",
    "atomic_mass": "float64",
    "atomic_mass_uncert": "float64",
    "mass_excess": "float64",
    "mass_excess_uncert": "float64",
}

# Unadvertised/internal datasets
_islands_fname = DATA_MOD / "x-islands.csv"
_airquality_fname = DATA_MOD / "x-airquality.csv"

countrypops: pd.DataFrame = pd.read_csv(_countrypops_fname, dtype=_countrypops_dtype)  # type: ignore
countrypops.__doc__ = """
Yearly populations of countries from 1960 to 2022.

A dataset that presents yearly, total populations of countries. Total population is based on counts
of all residents regardless of legal status or citizenship. Country identifiers include the
English-language country names, and the 2- and 3-letter ISO 3166-1 country codes. Each row contains
a population value for a given year (from 1960 to 2022). Any missing values for populations indicate
the non-existence of the entity during that year.

Details
-------
This is a dataset with 13,545 rows and 5 columns.

- `country_name`: The name of the country.
- `country_code_2`, `country_code_3`: The 2- and 3-letter ISO 3166-1 country codes.
- `year`: The year for the population estimate.
- `population`: The population estimate, midway through the year.

Preview
-------
```
Rows: 13545
Columns: 5
$ country_name   <str> 'Aruba', 'Aruba', 'Aruba'
$ country_code_2 <str> 'AW', 'AW', 'AW'
$ country_code_3 <str> 'ABW', 'ABW', 'ABW'
$ year           <i64> 1960, 1961, 1962
$ population     <i64> 54608, 55811, 56682
```

Source
------
<https://data.worldbank.org/indicator/SP.POP.TOTL>
"""

sza: pd.DataFrame = pd.read_csv(_sza_fname, dtype=_sza_dtype)  # type: ignore
sza.__doc__ = """
Twice hourly solar zenith angles by month & latitude.

This dataset contains solar zenith angles (in degrees, with the range of 0-90) every half hour from
04:00 to 12:00, true solar time. This set of values is calculated on the first of every month for 4
different northern hemisphere latitudes. For determination of afternoon values, the presented
tabulated values are symmetric about noon.

The solar zenith angle (SZA) is one measure that helps to describe the sun's path across the sky.
It's defined as the angle of the sun relative to a line perpendicular to the earth's surface. It is
useful to calculate the SZA in relation to the true solar time. True solar time relates to the
position of the sun with respect to the observer, which is different depending on the exact
longitude. For example, two hours before the sun crosses the meridian (the highest point it would
reach that day) corresponds to a true solar time of 10 a.m. The SZA has a strong dependence on the
observer's latitude. For example, at a latitude of 50 degrees N at the start of January, the
noontime SZA is 73.0 but a different observer at 20 degrees N would measure the noontime SZA to be
43.0 degrees.

Details
-------
This is a dataset with 816 rows and 4 columns.

- `latitude`: The latitude in decimal degrees for the observations.
- `month`: The measurement month. All calculations where conducted for the first day of each month.
- `tst`: The true solar time at the given `latitude` and date (first of `month`) for which the solar
zenith angle is calculated.
- `sza`: The solar zenith angle in degrees, where missing values indicate that sunrise hadn't yet
occurred by the `tst` value.

Preview
-------
```
Rows: 816
Columns: 4
$ latitude <str> '20', '20', '20'
$ month    <str> 'jan', 'jan', 'jan'
$ tst      <str> '0400', '0430', '0500'
$ sza      <f64> None, None, None
```

Source
------
Calculated Actinic Fluxes (290 - 700 nm) for Air Pollution Photochemistry Applications (Peterson,
1976), available at: <https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9100JA26.txt>.
"""

gtcars: pd.DataFrame = pd.read_csv(_gtcars_fname, dtype=_gtcars_dtype)  # type: ignore
gtcars.__doc__ = """
Deluxe automobiles from the 2014-2017 period.

Expensive and fast cars. Each row describes a car of a certain make, model, year, and trim. Basic
specifications such as horsepower, torque, EPA MPG ratings, type of drivetrain, and transmission
characteristics are provided. The country of origin for the car manufacturer is also given.

All of the `gtcars` have something else in common (aside from the high asking prices): they are all
grand tourer vehicles. These are proper GT cars that blend pure driving thrills with a level of
comfort that is more expected from a fine limousine (e.g., a Rolls-Royce Phantom EWB). You'll find
that, with these cars, comfort is emphasized over all-out performance. Nevertheless, the driving
experience should also mean motoring at speed, doing so in style and safety.

Details
-------
This is a dataset with 47 rows and 15 columns.

- `mfr`: The name of the car manufacturer.
- `model`: The car's model name.
- `year`: The car's model year.
- `trim`: A short description of the car model's trim.
- `bdy_style`: An identifier of the car's body style, which is either `"coupe"`, `"convertible"`,
`"sedan"`, or `"hatchback"`.
- `hp`, `hp_rpm`: The car's horsepower and the associated RPM level.
- `trq`, `trq_rpm`: The car's torque and the associated RPM level.
- `mpg_c`, `mpg_h`: The miles per gallon fuel efficiency rating for city and highway driving.
- `drivetrain`: The car's drivetrain which, for this dataset, is either `"rwd"` (Rear Wheel Drive)
or `"awd"` (All Wheel Drive).
- `trsmn`: An encoding of the transmission type, where the number part is the number of gears. The
car could have automatic transmission (`"a"`), manual transmission (`"m"`), an option to switch
between both types (`"am"`), or, direct drive (`"dd"`)
- `ctry_origin`: The country name for where the vehicle manufacturer is headquartered.
- `msrp`: Manufacturer's suggested retail price in U.S. dollars (USD).

Preview
-------
```
Rows: 47
Columns: 15
$ mfr         <str> 'Ford', 'Ferrari', 'Ferrari'
$ model       <str> 'GT', '458 Speciale', '458 Spider'
$ year        <i64> 2017, 2015, 2015
$ trim        <str> 'Base Coupe', 'Base Coupe', 'Base'
$ bdy_style   <str> 'coupe', 'coupe', 'convertible'
$ hp          <f64> 647.0, 597.0, 562.0
$ hp_rpm      <f64> 6250.0, 9000.0, 9000.0
$ trq         <f64> 550.0, 398.0, 398.0
$ trq_rpm     <f64> 5900.0, 6000.0, 6000.0
$ mpg_c       <f64> 11.0, 13.0, 13.0
$ mpg_h       <f64> 18.0, 17.0, 17.0
$ drivetrain  <str> 'rwd', 'rwd', 'rwd'
$ trsmn       <str> '7a', '7a', '7a'
$ ctry_origin <str> 'United States', 'Italy', 'Italy'
$ msrp        <f64> 447000.0, 291744.0, 263553.0
```

"""

sp500: pd.DataFrame = pd.read_csv(_sp500_fname, dtype=_sp500_dtype)  # type: ignore
sp500.__doc__ = """
Daily S&P 500 Index data from 1950 to 2015.

This dataset provides daily price indicators for the S&P 500 index from the beginning of 1950 to the
end of 2015. The index includes 500 leading companies and captures about 80 percent coverage of
available market capitalization.

Details
-------
This is a dataset with 16,607 rows and 7 columns.

- `date`: The date expressed as `Date` values.
- `open`, `high`, `low`, `close`: The day's opening, high, low, and closing prices in USD. The
`close` price is adjusted for splits.
- `volume`: The number of trades for the given `date`.
- `adj_close`: The close price adjusted for both dividends and splits.

Preview
-------
```
Rows: 16607
Columns: 7
$ date      <str> '2015-12-31', '2015-12-30', '2015-12-29'
$ open      <f64> 2060.5901, 2077.3401, 2060.54
$ high      <f64> 2062.54, 2077.3401, 2081.5601
$ low       <f64> 2043.62, 2061.97, 2060.54
$ close     <f64> 2043.9399, 2063.3601, 2078.3601
$ volume    <f64> 2655330000.0, 2367430000.0, 2542000000.0
$ adj_close <f64> 2043.9399, 2063.3601, 2078.3601
```

"""

pizzaplace: pd.DataFrame = pd.read_csv(_pizzaplace_fname, dtype=_pizzaplace_dtype)  # type: ignore
pizzaplace.__doc__ = """
A year of pizza sales from a pizza place.

A synthetic dataset that describes pizza sales for a pizza place somewhere in the US. While the
contents are artificial, the ingredients used to make the pizzas are far from it. There are 32
different pizzas that fall into 4 different categories: classic (classic pizzas: 'You probably had
one like it before, but never like this!'), chicken (pizzas with chicken as a major ingredient: 'Try
the Southwest Chicken Pizza! You'll love it!'), supreme (pizzas that try a little harder: 'My
Soppressata pizza uses only the finest salami from my personal salumist!'), and, veggie (pizzas
without any meats whatsoever: 'My Five Cheese pizza has so many cheeses, I can only offer it in
Large Size!').

Each pizza in the dataset is identified by a short `name`. The following listings provide the full
names of each pizza and their main ingredients.

**Classic Pizzas**

- `"classic_dlx"`: The Classic Deluxe Pizza (Pepperoni, Mushrooms, Red Onions, Red Peppers, Bacon)
- `"big_meat"`: The Big Meat Pizza (Bacon, Pepperoni, Italian Sausage, Chorizo Sausage)
- `"pepperoni"`: The Pepperoni Pizza (Mozzarella Cheese, Pepperoni)
- `"hawaiian"`: The Hawaiian Pizza (Sliced Ham, Pineapple, Mozzarella Cheese)
- `"pep_msh_pep"`: The Pepperoni, Mushroom, and Peppers Pizza (Pepperoni, Mushrooms, and Green
Peppers)
- `"ital_cpcllo"`: The Italian Capocollo Pizza (Capocollo, Red Peppers, Tomatoes, Goat Cheese,
Garlic, Oregano)
- `"napolitana"`: The Napolitana Pizza (Tomatoes, Anchovies, Green Olives, Red Onions, Garlic)
- `"the_greek"`: The Greek Pizza (Kalamata Olives, Feta Cheese, Tomatoes, Garlic, Beef Chuck Roast,
Red Onions)

**Chicken Pizzas**

- `"thai_ckn"`: The Thai Chicken Pizza (Chicken, Pineapple, Tomatoes, Red Peppers, Thai Sweet Chilli
Sauce)
- `"bbq_ckn"`: The Barbecue Chicken Pizza (Barbecued Chicken, Red Peppers, Green Peppers, Tomatoes,
Red Onions, Barbecue Sauce)
- `"southw_ckn"`: The Southwest Chicken Pizza (Chicken, Tomatoes, Red Peppers, Red Onions, Jalapeno
Peppers, Corn, Cilantro, Chipotle Sauce)
- `"cali_ckn"`: The California Chicken Pizza (Chicken, Artichoke, Spinach, Garlic, Jalapeno Peppers,
Fontina Cheese, Gouda Cheese)
- `"ckn_pesto"`: The Chicken Pesto Pizza (Chicken, Tomatoes, Red Peppers, Spinach, Garlic, Pesto
Sauce)
- `"ckn_alfredo"`: The Chicken Alfredo Pizza (Chicken, Red Onions, Red Peppers, Mushrooms, Asiago
Cheese, Alfredo Sauce)

**Supreme Pizzas**

- `"brie_carre"`: The Brie Carre Pizza (Brie Carre Cheese, Prosciutto, Caramelized Onions, Pears,
Thyme, Garlic)
- `"calabrese"`: The Calabrese Pizza (‘Nduja Salami, Pancetta, Tomatoes, Red Onions, Friggitello
Peppers, Garlic)
- `"soppressata"`: The Soppressata Pizza (Soppressata Salami, Fontina Cheese, Mozzarella Cheese,
Mushrooms, Garlic)
- `"sicilian"`: The Sicilian Pizza (Coarse Sicilian Salami, Tomatoes, Green Olives, Luganega
Sausage, Onions, Garlic)
- `"ital_supr"`: The Italian Supreme Pizza (Calabrese Salami, Capocollo, Tomatoes, Red Onions, Green
Olives, Garlic)
- `"peppr_salami"`: The Pepper Salami Pizza (Genoa Salami, Capocollo, Pepperoni, Tomatoes, Asiago
Cheese, Garlic)
- `"prsc_argla"`: The Prosciutto and Arugula Pizza (Prosciutto di San Daniele, Arugula, Mozzarella
Cheese)
- `"spinach_supr"`: The Spinach Supreme Pizza (Spinach, Red Onions, Pepperoni, Tomatoes, Artichokes,
Kalamata Olives, Garlic, Asiago Cheese)
- `"spicy_ital"`: The Spicy Italian Pizza (Capocollo, Tomatoes, Goat Cheese, Artichokes, Peperoncini
verdi, Garlic)

**Vegetable Pizzas**

- `"mexicana"`: The Mexicana Pizza (Tomatoes, Red Peppers, Jalapeno Peppers, Red Onions, Cilantro,
Corn, Chipotle Sauce, Garlic)
- `"four_cheese"`: The Four Cheese Pizza (Ricotta Cheese, Gorgonzola Piccante Cheese, Mozzarella
Cheese, Parmigiano Reggiano Cheese, Garlic)
- `"five_cheese"`: The Five Cheese Pizza (Mozzarella Cheese, Provolone Cheese, Smoked Gouda Cheese,
Romano Cheese, Blue Cheese, Garlic)
- `"spin_pesto"`: The Spinach Pesto Pizza (Spinach, Artichokes, Tomatoes, Sun-dried Tomatoes,
Garlic, Pesto Sauce)
- `"veggie_veg"`: The Vegetables + Vegetables Pizza (Mushrooms, Tomatoes, Red Peppers, Green
Peppers, Red Onions, Zucchini, Spinach, Garlic)
- `"green_garden"`: The Green Garden Pizza (Spinach, Mushrooms, Tomatoes, Green Olives, Feta Cheese)
- `"mediterraneo"`: The Mediterranean Pizza (Spinach, Artichokes, Kalamata Olives, Sun-dried
Tomatoes, Feta Cheese, Plum Tomatoes, Red Onions)
- `"spinach_fet"`: The Spinach and Feta Pizza (Spinach, Mushrooms, Red Onions, Feta Cheese, Garlic)
- `"ital_veggie"`: The Italian Vegetables Pizza (Eggplant, Artichokes, Tomatoes, Zucchini, Red
Peppers, Garlic, Pesto Sauce)

Details
-------
This is a dataset with 49,574 rows and 7 columns.

- `id`: The ID for the order, which consists of one or more pizzas at a given `date` and `time`.
- `date`: A string-based representation of the order date, expressed in the ISO 8601 date format
('YYYY-MM-DD').
- `time`: A string-based representation of the order time, expressed as a 24-hour time the ISO 8601
extended time format ('hh:mm:ss').
- `name`: The short name for the pizza.
- `size`: The size of the pizza, which can either be `"S"`, `"M"`, `"L"`, `"XL"` (rare!), or `"XXL"`
(even rarer!); most pizzas are available in the `"S"`, `"M"`, and `"L"` sizes but exceptions apply.
- `type`: The category or type of pizza, which can either be `"classic"`, `"chicken"`, `"supreme"`,
or `"veggie"`.
- `price`: The price of the pizza and the amount that it sold for (in USD).

Preview
-------
```
Rows: 49574
Columns: 7
$ id    <str> '2015-000001', '2015-000002', '2015-000002'
$ date  <str> '2015-01-01', '2015-01-01', '2015-01-01'
$ time  <str> '11:38:36', '11:57:40', '11:57:40'
$ name  <str> 'hawaiian', 'classic_dlx', 'mexicana'
$ size  <str> 'M', 'M', 'M'
$ type  <str> 'classic', 'classic', 'veggie'
$ price <f64> 13.25, 16.0, 16.0
```

"""

exibble: pd.DataFrame = pd.read_csv(_exibble_fname, dtype=_exibble_dtype)  # type: ignore
exibble.__doc__ = """
A toy example table for testing with great_tables: exibble.

This table contains data of a few different classes, which makes it well-suited for quick
experimentation with the functions in this package. It contains only eight rows with numeric and
string columns. The last 4 rows contain missing values in the majority of this table's columns (1
missing value per column). The date, time, and datetime columns are string-based dates/times in
the familiar ISO 8601 format. The row and group columns provide for unique rownames and two groups
(grp_a and grp_b) for experimenting with the `rowname_col` and `groupname_col` arguments.

Details
-------
This is a dataset with 8 rows and 9 columns.

- `num`: A numeric column ordered with increasingly larger values.
- `char`: A string-based column composed of names of fruits from `a` to `h`.
- `fctr`: A factor column with numbers from `1` to `8`, written out.
- `date`, `time`, `datetime`: String-based columns with dates, times, and datetimes.
- `currency`: A numeric column that is useful for testing currency-based formatting.
- `row`: A string-based column in the format `row_X` which can be useful for testing with row labels
in a table stub.
- `group`: A string-based column with four `"grp_a"` values and four `"grp_b"` values which can be
useful for testing tables that contain row groups.

Preview
-------
```
Rows: 8
Columns: 9
$ num      <f64> 0.1111, 2.222, 33.33
$ char     <str> 'apricot', 'banana', 'coconut'
$ fctr     <str> 'one', 'two', 'three'
$ date     <str> '2015-01-15', '2015-02-15', '2015-03-15'
$ time     <str> '13:35', '14:40', '15:45'
$ datetime <str> '2018-01-01 02:22', '2018-02-02 14:33', '2018-03-03 03:44'
$ currency <f64> 49.95, 17.95, 1.39
$ row      <str> 'row_1', 'row_2', 'row_3'
$ group    <str> 'grp_a', 'grp_a', 'grp_a'
```

"""

towny: pd.DataFrame = pd.read_csv(_towny_fname, dtype=_towny_dtype)  # type: ignore
towny.__doc__ = """
Populations of all municipalities in Ontario from 1996 to 2021.

A dataset containing census population data from six census years (1996 to 2021) for all 414 of
Ontario's local municipalities. The Municipal Act of Ontario (2001) defines a local municipality as
"a single-tier municipality or a lower-tier municipality". There are 173 single-tier municipalities
and 241 lower-tier municipalities representing 99 percent of Ontario's population and 17 percent of
its land use.

In the towny dataset we include information specific to each municipality such as location (in the
latitude and longitude columns), their website URLs, their classifications, and land area sizes
according to 2021 boundaries. Additionally, there are computed columns containing population density
values for each census year and population change values from adjacent census years.

Details
-------
This is a dataset with 414 rows and 25 columns.

- `name`: The name of the municipality.
- `website`: The website for the municipality. This is missing if there isn't an official site.
- `status`: The status of the municipality. This is either `"lower-tier"` or `"single-tier"`. A
single-tier municipality, which takes on all municipal duties outlined in the Municipal Act and
other Provincial laws, is independent of an upper-tier municipality. Part of an upper-tier
municipality is a lower-tier municipality. The upper-tier and lower-tier municipalities are
responsible for carrying out the duties laid out in the Municipal Act and other provincial laws.
- `csd_type`: The Census Subdivision Type. This can be one of `"village"`, `"town"`, `"township"`,
`"municipality"`, or `"city"`.
- `census_div`: The Census division, of which there are 49. This is made up of single-tier
municipalities, regional municipalities, counties, and districts.
- `latitude`, `longitude`: The location of the municipality, given as latitude and longitude values
in decimal degrees.
- `land_area_km2`: The total area of the local municipality in square kilometers.
- `population_1996`, `population_2001`, `population_2006`, `population_2011`, `population_2016`,
`population_2021`: Population values for each municipality from the 1996 to 2021 census years.
- `density_1996`, `density_2001`, `density_2006`, `density_2011`, `density_2016`, `density_2021`:
Population density values, calculated as persons per square kilometer, for each municipality from
the 1996 to 2021 census years.
- `pop_change_1996_2001_pct`, `pop_change_2001_2006_pct`, `pop_change_2006_2011_pct`,
`pop_change_2011_2016_pct`, `pop_change_2016_2021_pct`:  Population changes between adjacent pairs
of census years, from 1996 to 2021.

Preview
-------
```
Rows: 414
Columns: 25
$ name                     <str> 'Addington Highlands', 'Adelaide Metcalfe', 'Adjala-Tosorontio'
$ website                  <str> 'https://addingtonhighlands.ca',
                                 'https://adelaidemetcalfe.on.ca',
                                 'https://www.adjtos.ca'
$ status                   <str> 'lower-tier', 'lower-tier', 'lower-tier'
$ csd_type                 <str> 'township', 'township', 'township'
$ census_div               <str> 'Lennox and Addington', 'Middlesex', 'Simcoe'
$ latitude                 <f64> 45.0, 42.95, 44.133333
$ longitude                <f64> -77.25, -81.7, -79.933333
$ land_area_km2            <f64> 1293.99, 331.11, 371.53
$ population_1996          <i64> 2429, 3128, 9359
$ population_2001          <i64> 2402, 3149, 10082
$ population_2006          <i64> 2512, 3135, 10695
$ population_2011          <i64> 2517, 3028, 10603
$ population_2016          <i64> 2318, 2990, 10975
$ population_2021          <i64> 2534, 3011, 10989
$ density_1996             <f64> 1.88, 9.45, 25.19
$ density_2001             <f64> 1.86, 9.51, 27.14
$ density_2006             <f64> 1.94, 9.47, 28.79
$ density_2011             <f64> 1.95, 9.14, 28.54
$ density_2016             <f64> 1.79, 9.03, 29.54
$ density_2021             <f64> 1.96, 9.09, 29.58
$ pop_change_1996_2001_pct <f64> -0.0111, 0.0067, 0.0773
$ pop_change_2001_2006_pct <f64> 0.0458, -0.0044, 0.0608
$ pop_change_2006_2011_pct <f64> 0.002, -0.0341, -0.0086
$ pop_change_2011_2016_pct <f64> -0.0791, -0.0125, 0.0351
$ pop_change_2016_2021_pct <f64> 0.0932, 0.007, 0.0013
```

"""

peeps: pd.DataFrame = pd.read_csv(_peeps_fname, dtype=_peeps_dtype)  # type: ignore
peeps.__doc__ = """
A table of personal information for people all over the world.

The `peeps` dataset contains records for one hundred people residing in ten different countries.
Each person in the table has address information along with their email address and phone number.
There are also personal characteristics like date of birth, height, and weight. This data has been
synthesized, and so the names within the table have not been taken or based on individuals in real
life. The street addresses were generated from actual street names within real geographic
localities, however, the street numbers were assigned randomly from a constrained number set. While
these records do not relate to real people, efforts were made to make the data as realistic as
possible.

Details
-------
This is a dataset with 100 rows and 14 columns.

- `name_given`, `name_family`: The given and family name of individual.
- `address`: The street address of the individual.
- `city`: The name of the city or locality in which the individual resides.
- `state_prov`: The state or province associated with the `city` and `address`. This is `None` for
individuals residing in countries where subdivision data is not needed for generating a valid
mailing address.
- `postcode`: The post code associated with the `city` and `address`.
- `country`: The 3-letter ISO 3166-1 country code representative of the individual's country.
- `email_addr`: The individual's email address.
- `phone_number`, `country_code`: The individual's phone number and the country code associated with
the phone number.
- `gender`: The gender of the individual.
- `dob`: The individual's date of birth (DOB) in the ISO 8601 form of `YYYY-MM-DD`.
- `height_cm`, `weight_kg`: The height and weight of the individual in centimeters (cm) and
kilograms (kg), respectively.

Preview
-------
```
Rows: 100
Columns: 14
$ name_given   <str> 'Ruth', 'Peter', 'Fanette'
$ name_family  <str> 'Conte', 'Möller', 'Gadbois'
$ address      <str> '4299 Bobcat Drive', '3705 Hidden Pond Road', '4200 Swick Hill Street'
$ city         <str> 'Baileys Crossroads', 'Red Boiling Springs', 'New Orleans'
$ state_prov   <str> 'MD', 'TN', 'LA'
$ postcode     <str> '22041', '37150', '70112'
$ country      <str> 'USA', 'USA', 'USA'
$ email_addr   <str> 'rcconte@example.com', 'pmoeller@example.com', 'fan_gadbois@example.com'
$ phone_number <str> '240-783-7630', '615-699-3517', '985-205-2970'
$ country_code <str> '1', '1', '1'
$ gender       <str> 'female', 'male', 'female'
$ dob          <str> '1949-03-16', '1939-11-22', '1970-12-20'
$ height_cm    <i64> 153, 175, 167
$ weight_kg    <f64> 76.4, 74.9, 61.6
```

"""

films: pd.DataFrame = pd.read_csv(_films_fname, dtype=_films_dtype)  # type: ignore
films.__doc__ = """
Feature films in competition at the Cannes Film Festival.

Each entry in the `films` is a feature film that appeared in the official selection during a
festival year (starting in 1946 and active to the present day). The `year` column refers to the
year of the festival and this figure doesn't always coincide with the release year of the film. The
film's title reflects the most common title of the film in English, where the `original_title`
column provides the title of the film in its spoken language (transliterated to Roman script where
necessary).

Details
-------
This is a dataset with 1,851 rows and 8 columns.

- `year`: The year of the festival in which the film was in competition.
- `title`, `original_title`: The `title` field provides the film title used for English-speaking
audiences. The `original_title` field is populated when `title` differs greatly from the non-English
original.
- `director`: The director or set of co-directors for the film. Multiple directors are separated by
a comma.
- `languages`: The languages spoken in the film in the order of appearance. This consists of ISO 639
language codes (primarily as two-letter codes, but using three-letter codes where necessary).
- `countries_of_origin`: The country or countries of origin for the production. Here, 2-letter ISO
3166-1 country codes (set in uppercase) are used.
- `run_time`: The run time of the film in hours and minutes. This is given as a string in the format
`<x>h <y>m`.
- `imdb_url`: The URL of the film's information page in the Internet Movie Database (IMDB).

Preview
-------
```
Rows: 1851
Columns: 8
$ year                <i64> 1946, 1946, 1946
$ title               <str> 'The Lovers', 'Anna and the King of Siam', 'Blood and Fire'
$ original_title      <str> 'Amanti in fuga', None, 'Blod och eld'
$ director            <str> 'Giacomo Gentilomo', 'John Cromwell', 'Anders Henrikson'
$ languages           <str> 'it', 'en', 'sv'
$ countries_of_origin <str> 'IT', 'US', 'SE'
$ run_time            <str> '1h 30m', '2h 8m', '1h 40m'
$ imdb_url            <str> 'https://www.imdb.com/title/tt0038297/',
                            'https://www.imdb.com/title/tt0038303/',
                            'https://www.imdb.com/title/tt0037544/'
```

"""

metro: pd.DataFrame = pd.read_csv(_metro_fname, dtype=_metro_dtype)  # type: ignore
metro.__doc__ = """
The stations of the Paris Metro.

A dataset with information on all 314 Paris Metro stations as of June 2024. Each record represents a
station, describing which Metro lines are serviced by the station, which other connections are
available, and annual passenger volumes. Basic location information is provided for each station in
terms where they reside on a municipal level, and, through latitude/longitude coordinates.

The system has 16 lines (numbered from 1 to 14, with two additional lines: 3bis and 7bis) and covers
over 200 kilometers of track. The Metro runs on standard gauge tracks (1,435 mm) and operates using
a variety of rolling stock, including rubber-tired trains and steel-wheeled trains (which are far
more common).

The Metro is operated by the RATP, which also operates other transit systems in the region,
including buses, trams, and the RER. The RER is an important component of the region's transit
infrastructure, and several RER stations have connectivity with the Metro. This integration allows
passengers to transfer between those two systems seamlessly. The Metro also has connections to the
Transilien rail network, tramway stations, several major train stations (e.g., Gare du Nord, Gare de
l'Est, etc.), and many bus lines.

Details
-------
This is a dataset with 314 rows and 11 columns.

- `name`: The name of the station.
- `caption`: In some cases, a station will have a caption that might describe a nearby place of
interest. This is missing if there isn't a caption for the station name.
- `lines`: All Metro lines associated with the station. This is a string-based, comma-separated
series of line names.
- `connect_rer`: Station connections with the RER. The RER system has five lines (A, B, C, D, and E)
with 257 stations and several interchanges with the Metro.
- `connect_tramway`: Connections with tramway lines. This system has twelve lines in operation (T1,
T2, T3a, T3b, T4, T5, T6, T7, T8, T9, T11, and T13) with 235 stations.
- `connect_transilien`: Connections with Transilien lines. This system has eight lines in operation
(H, J, K, L, N, P, R, and U).
- `connect_other`: Other connections with transportation infrastructure such as regional, intercity,
night, and high-speed trains (typically at railway stations).
- `latitude`, `longitude`: The location of the station, given as latitude and longitude values in
decimal degrees.
- `location`: The arrondissement of Paris or municipality in which the station resides. For some
stations located at borders, the grouping of locations will be presented as a comma-separated
series.
- `passengers`: The total number of Metro station entries during 2021. Some of the newest stations
in the Metro system do not have this data, thus they show as missing values.

Preview
-------
```
Rows: 314
Columns: 11
$ name               <str> 'Argentine', 'Bastille', 'Bérault'
$ caption            <str> None, None, None
$ lines              <str> '1', '1, 5, 8', '1'
$ connect_rer        <str> None, None, None
$ connect_tramway    <str> None, None, None
$ connect_transilien <str> None, None, None
$ connect_other      <str> None, None, None
$ passengers         <i64> 2079212, 8069243, 2106827
$ latitude           <f64> 48.875278, 48.853082, 48.845278
$ longitude          <f64> 2.29, 2.369077, 2.428333
$ location           <str> 'Paris 16th, Paris 17th',
                           'Paris 4th, Paris 11th, Paris 12th',
                           'Saint-Mandé, Vincennes'
```

"""

gibraltar: pd.DataFrame = pd.read_csv(_gibraltar_fname, dtype=_gibraltar_dtype)  # type: ignore
gibraltar.__doc__ = """
Weather conditions in Gibraltar, May 2023.

The `gibraltar` dataset has meteorological data for the Gibraltar Airport Station from May 1 to May
31, 2023. Gibraltar is a British Overseas Territory and city located at the southern end of the
Iberian Peninsula, on the Bay of Gibraltar. This weather station is located at the airport (GIB),
where it's at an elevation of 5 meters above mean sea level (AMSL).

Details
-------
This is a dataset with 1,431 rows and 10 columns.

- `date`, `time`: The date and time of the observation.
- `temp`, `dew_point`: The air temperature and dew point values, both in degrees Celsius.
- `humidity`: The relative humidity as a value between `0` and `1`
- `wind_dir`, `wind_speed`, `wind_gust`: Observations related to wind. The wind direction is given
as the typical 'blowing from' value, simplified to one of 16 compass directions. The wind speed is
provided in units of meters per second. If there was a measurable wind gust, the maximum gust speed
is recorded as m/s values (otherwise the value is `0`).
- `pressure`: The atmospheric pressure in hectopascals (hPa).
- `condition`: The weather condition.

Preview
-------
```
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
```

"""

constants: pd.DataFrame = pd.read_csv(_constants_fname, dtype=_constants_dtype)  # type: ignore
constants.__doc__ = """
The fundamental physical constants.

This dataset contains values for over 300 basic fundamental constants in nature. The values
originate from the 2018 adjustment which is based on the latest relevant precision measurements and
improvements of theoretical calculations. Such work has been carried out under the authority of the
Task Group on Fundamental Constants (TGFC) of the Committee on Data of the International Science
Council (CODATA). These updated values became available on May 20, 2019. They are published at
http://physics.nist.gov/constants, a website of the Fundamental Constants Data Center of the
National Institute of Standards and Technology (NIST), Gaithersburg, Maryland, USA.

Details
-------
This is a dataset with 354 rows and 6 columns.

- `name`: The name of the constant.
- `value`: The value of the constant.
- `uncert`: The uncertainty associated with the value. If missing then the value is seen as an
'exact' value (e.g., an electron volt has the exact value of 1.602 176 634 e-19 J).
- `sf_value`, `sf_uncert`: The number of significant figures associated with the value and any
uncertainty value.
- `units`: The units associated with the constant.

Preview
-------
```
Rows: 354
Columns: 6
$ name      <str> 'alpha particle-electron mass ratio',
                  'alpha particle mass',
                  'alpha particle mass energy equivalent'
$ value     <f64> 7294.29954142, 6.6446573357e-27, 5.9719201914e-10
$ uncert    <f64> 2.4e-07, 2e-36, 1.8e-19
$ sf_value  <i64> 12, 11, 11
$ sf_uncert <i64> 2, 2, 2
$ units     <str> None, 'kg', 'J'
```

"""

illness: pd.DataFrame = pd.read_csv(_illness_fname, dtype=_illness_dtype)  # type: ignore
illness.__doc__ = """
Lab tests for one suffering from an illness.

A dataset with artificial daily lab data for a patient with Yellow Fever (YF). The table comprises
laboratory findings for the patient from day 3 of illness onset until day 9 (after which the patient
died). YF viral DNA was found in serum samples from day 3, where the viral load reached 14,000
copies per mL. Several medical interventions were taken to help the patient, including the
administration of fresh frozen plasma, platelets, red cells, and coagulation factor VIII. The
patient also received advanced support treatment in the form of mechanical ventilation and
plasmapheresis. Though the patient's temperature remained stable during their illness,
unfortunately, the patient's condition did not improve. On days 7 and 8, the patient's health
declined further, with symptoms such as nosebleeds, gastrointestinal bleeding, and hematoma.

The various tests are identified in the `test` column. The following listing provides the full names
of any abbreviations seen in that column.

- `"WBC"`: white blood cells.
- `"RBC"`: red blood cells.
- `"Hb"`: hemoglobin.
- `"PLT"`: platelets.
- `"ALT"`: alanine aminotransferase.
- `"AST"`: aspartate aminotransferase.
- `"TBIL"`: total bilirubin.
- `"DBIL"`: direct bilirubin.
- `"NH3"`: hydrogen nitride.
- `"PT"`: prothrombin time.
- `"APTT"`: activated partial thromboplastin time.
- `"PTA"`: prothrombin time activity.
- `"DD"`: D-dimer.
- `"FDP"`: fibrinogen degradation products.
- `"LDH"`: lactate dehydrogenase.
- `"HBDH"`: hydroxybutyrate dehydrogenase.
- `"CK"`: creatine kinase.
- `"CKMB"`: the MB fraction of creatine kinase.
- `"BNP"`: B-type natriuetic peptide.
- `"MYO"`: myohemoglobin.
- `"TnI"`: troponin inhibitory.
- `"CREA"`: creatinine.
- `"BUN"`: blood urea nitrogen.
- `"AMY"`: amylase.
- `"LPS"`: lipase.
- `"K"`: kalium.
- `"Na"`: sodium.
- `"Cl"`: chlorine.
- `"Ca"`: calcium.
- `"P"`: phosphorus.
- `"Lac"`: lactate, blood.
- `"CRP"`: c-reactive protein.
- `"PCT"`: procalcitonin.
- `"IL-6"`: interleukin-6.
- `"CD3+CD4+"`: CD4+T lymphocytes.
- `"CD3+CD8+"`: CD8+T lymphocytes.

Details
-------
This is a dataset with 39 rows and 11 columns.

- `test`: The name of the test.
- `units`: The measurement units for the test.
- `day_3`, `day_4`, `day_5`, `day_6`, `day_7`, `day_8`, `day_9`: Measurement values associated with
each test administered from days 3 to 9. A missing value indicates that the test could not be
performed that day.
- `norm_l`, `norm_u`: Lower and upper bounds for the normal range associated with the test.

Preview
-------
```
Rows: 39
Columns: 11
$ test   <str> 'Viral load', 'WBC', 'Neutrophils'
$ units  <str> 'copies per mL', 'x10^9 / L', 'x10^9 / L'
$ day_3  <f64> 12000.0, 5.26, 4.87
$ day_4  <f64> 4200.0, 4.26, 4.72
$ day_5  <f64> 1600.0, 9.92, 7.92
$ day_6  <f64> 830.0, 10.49, 18.21
$ day_7  <f64> 760.0, 24.77, 22.08
$ day_8  <f64> 520.0, 30.26, 27.17
$ day_9  <f64> 250.0, 19.03, 16.59
$ norm_l <f64> None, 4.0, 2.0
$ norm_u <f64> None, 10.0, 8.0
```

"""

reactions: pd.DataFrame = pd.read_csv(_reactions_fname, dtype=_reactions_dtype)  # type: ignore
reactions.__doc__ = """
Reaction rates for gas-phase atmospheric reactions of organic compounds.

The `reactions` dataset contains kinetic data for second-order (two body) gas-phase chemical
reactions for 1,683 organic compounds. The reaction-rate values and parameters within this dataset
are useful for studies of the atmospheric environment. Organic pollutants, which are present in
trace amounts in the atmosphere, have been extensively studied by research groups since their
persistence in the atmosphere requires specific attention. Many researchers have reported kinetic
data on specific gas-phase reactions and these mainly involve oxidation reactions with OH, nitrate
radicals, ozone, and chlorine atoms.

This compilation of rate constant (*k*) data as contains the values for rate constants at 298 K (in
units of `cm^3 molecules^-1 s^-1`) as well as parameters that allow for the calculation of rate
constants at different temperatures (the temperature dependence parameters: `A`, `B`, and `n`).
Uncertainty values/factors and temperature limits are also provided here where information is
available.

Details
-------
This is a dataset with 1,683 rows and 39 columns.

- `compd_name`: The name of the primary compound undergoing reaction with OH, nitrate radicals,
ozone, or chlorine atoms.
- `cmpd_mwt`: The molecular weight of the compound in units of g/mol.
- `cmpd_formula`: The chemical formula of the compound.
- `cmpd_type`: The category of compounds that the `compd_name` falls under.
- `cmpd_smiles`: The SMILES (simplified molecular-input line-entry system) representation for the
compound.
- `cmpd_inchi`: The InChI (International Chemical Identifier) representation for the compound.
- `cmpd_inchikey`: The InChIKey, which is a hashed InChI value, has a fixed length of 27 characters.
These values can be used to more easily perform database searches of chemical compounds.
- `OH_k298`: Rate constant at 298 K for OH reactions.
- `OH_uncert`: Uncertainty as a percentage for certain OH reactions.
- `OH_u_fac`: Uncertainty as a plus/minus difference for certain OH reactions.
- `OH_a`, `OH_b`, `OH_n`: Extended temperature dependence parameters for bimolecular OH reactions,
to be used in the Arrhenius expression: `k(T)=A exp(-B/T) (T/300)^n`. In that, `A` is expressed as
cm^3 molecules^-1 s^-1, `B` is in units of K, and `n` is dimensionless. Any missing values indicate
that data is not available.
- `OH_t_low`, `OH_t_high`: The low and high temperature boundaries (in units of K) for which the
`OH_a`, `OH_b`, and `OH_n` parameters are valid.
- `O3_k298`: Rate constant at 298 K for ozone reactions.
- `O3_uncert`: Uncertainty as a percentage for certain ozone reactions.
- `O3_u_fac`: Uncertainty as a plus/minus difference for certain ozone reactions.
- `O3_a`, `O3_b`, `O3_n`: Extended temperature dependence parameters for bimolecular ozone
reactions, to be used in the Arrhenius expression: `k(T)=A exp(-B/T) (T/300)^n`. In that, `A` is
expressed as cm^3 molecules^-1 s^-1, `B` is in units of K, and `n` is dimensionless. Any missing
values indicate that data is not available.
- `O3_t_low`, `O3_t_high`: The low and high temperature boundaries (in units of K) for which the
`O3_a`, `O3_b`, and `O3_n` parameters are valid.
- `NO3_k298`: Rate constant at 298 K for NO3 reactions.
- `NO3_uncert`: Uncertainty as a percentage for certain NO3 reactions.
- `NO3_u_fac`: Uncertainty as a plus/minus difference for certain NO3 reactions.
- `NO3_a`, `NO3_b`, `NO3_n`: Extended temperature dependence parameters for bimolecular NO3
reactions, to be used in the Arrhenius expression: `k(T)=A exp(-B/T) (T/300)^n`. In that, `A` is
expressed as cm^3 molecules^-1 s^-1, `B` is in units of K, and `n` is dimensionless. Any missing
values indicate that data is not available.
- `NO3_t_low`, `NO3_t_high`: The low and high temperature boundaries (in units of K) for which the
`NO3_a`, `NO3_b`, and `NO3_n` parameters are valid.
- `Cl_k298`: Rate constant at 298 K for Cl reactions.
- `Cl_uncert`: Uncertainty as a percentage for certain Cl reactions.
- `Cl_u_fac`: Uncertainty as a plus/minus difference for certain Cl reactions.
- `Cl_a`, `Cl_b`, `Cl_n`: Extended temperature dependence parameters for bimolecular Cl reactions,
to be used in the Arrhenius expression: `k(T)=A exp(-B/T) (T/300)^n`. In that, `A` is expressed as
cm^3 molecules^-1 s^-1, `B` is in units of K, and `n` is dimensionless. Any missing values indicate
that data is not available.
- `Cl_t_low`, `Cl_t_high`: The low and high temperature boundaries (in units of K) for which the
`Cl_a`, `Cl_b`, and `Cl_n` parameters are valid.

Preview
-------
```
Rows: 1683
Columns: 39
$ cmpd_name     <str> 'methane', 'formaldehyde', 'methanol'
$ cmpd_mwt      <f64> 16.04, 30.03, 32.04
$ cmpd_formula  <str> 'CH4', 'CH2O', 'CH4O'
$ cmpd_type     <str> 'normal alkane', 'aldehyde', 'alcohol or glycol'
$ cmpd_smiles   <str> 'C', 'C=O', 'CO'
$ cmpd_inchi    <str> 'InChI=1S/CH4/h1H4', 'InChI=1S/CH2O/c1-2/h1H2', 'InChI=1S/CH4O/c1-2/h2H,1H3'
$ cmpd_inchikey <str> 'VNWKTOKETHGBQD-UHFFFAOYSA-N',
                      'WSFSSNUMVMOOMR-UHFFFAOYSA-N',
                      'OKKJLVBELUTLKV-UHFFFAOYSA-N'
$ OH_k298       <f64> 6.36e-15, 8.5e-12, 8.78e-13
$ OH_uncert     <f64> 0.1, 0.2, 0.1
$ OH_u_fac      <f64> None, None, None
$ OH_A          <f64> 3.62e-13, 5.4e-12, 2.32e-13
$ OH_B          <f64> 1200.34866000493, -135.0, -402.0
$ OH_n          <f64> 2.17993581535803, None, 2.72
$ OH_t_low      <f64> 200.0, 200.0, 210.0
$ OH_t_high     <f64> 2025.0, 300.0, 1344.0
$ O3_k298       <f64> None, None, None
$ O3_uncert     <f64> None, None, None
$ O3_u_fac      <f64> None, None, None
$ O3_A          <f64> None, None, None
$ O3_B          <f64> None, None, None
$ O3_n          <f64> None, None, None
$ O3_t_low      <f64> None, None, None
$ O3_t_high     <f64> None, None, None
$ NO3_k298      <f64> None, 5.5e-16, 1.3e-16
$ NO3_uncert    <f64> None, None, None
$ NO3_u_fac     <f64> None, 1.6, 3.0
$ NO3_A         <f64> None, None, 9.4e-13
$ NO3_B         <f64> None, None, 2650.0
$ NO3_n         <f64> None, None, None
$ NO3_t_low     <f64> None, None, 250.0
$ NO3_t_high    <f64> None, None, 370.0
$ Cl_k298       <f64> 1e-13, 7.2e-11, 5.1e-11
$ Cl_uncert     <f64> 0.15, 0.15, 0.2
$ Cl_u_fac      <f64> None, None, None
$ Cl_A          <f64> 6.6e-12, 8.1e-11, 5.1e-11
$ Cl_B          <f64> 1240.0, 34.0, 0.0
$ Cl_n          <f64> None, None, None
$ Cl_t_low      <f64> 200.0, 200.0, 225.0
$ Cl_t_high     <f64> 300.0, 500.0, 950.0
```

"""

photolysis: pd.DataFrame = pd.read_csv(_photolysis_fname, dtype=_photolysis_dtype)  # type: ignore
photolysis.__doc__ = """
Data on photolysis rates for gas-phase organic compounds.

The `photolysis` dataset contains numerical values for describing the photolytic degradation
pathways of 25 compounds of relevance in atmospheric chemistry. Many volatile organic compounds
(VOCs) are emitted in substantial quantities from both biogenic and anthropogenic sources, and they
can have a major influence on the chemistry of the lower atmosphere. A portion of these can be
transformed into other VOCs via the energy provided from light.

In order to realistically predict the composition of the atmosphere and how it evolves over time, we
need accurate estimates of photolysis rates. The data provided here in `photolysis` allows for
computations of photolysis rates (*J*, having units of `s^-1`) as a function of the solar zenith
angle (SZA). Having such values is essential when deploying atmospheric chemistry models.

Details
-------
This is a dataset with 34 rows and 10 columns.

- `compd_name`: The name of the primary compound undergoing photolysis.
- `cmpd_formula`: The chemical formula of the compound.
- `products`: A product pathway for the photolysis of the compound.
- `type`: The type of organic compound undergoing photolysis.
- `l`, `m`, `n`: The parameter values given in the `l`, `m`, and `n` columnscan be used to calculate
the photolysis rate (*J*) as a function of the solar zenith angle (*X*, in radians) through the
expression: `J = l * cos(X)^m * exp(-n * sec(X))`.
- `quantum_yield`: In the context of photolysis reactions, this is the efficiency of a given
photolytic reaction. In other words, it's the number of product molecules formed over the number of
photons absorbed.
- `wavelength_nm`, `sigma_298_cm2`: The `wavelength_nm` and `sigma_298_cm2` columns provide
photoabsorption data for the compound undergoing photolysis. The values in `wavelength_nm` provide
the wavelength of light in nanometer units; the `sigma_298_cm2` values are paired with the
`wavelength_nm` values and they are in units of `cm^2 molecule^-1`.

Preview
-------
```
Rows: 34
Columns: 10
$ cmpd_name     <str> 'ozone', 'ozone', 'hydrogen peroxide'
$ cmpd_formula  <str> 'O3', 'O3', 'H2O2'
$ products      <str> '-> O(^1D) + O2', '-> O(^3P) + O2', '-> OH + OH'
$ type          <str> 'inorganic reactions', 'inorganic reactions', 'inorganic reactions'
$ l             <f64> 6.073e-05, 0.0004775, 1.041e-05
$ m             <f64> 1.743, 0.298, 0.723
$ n             <f64> 0.474, 0.08, 0.279
$ quantum_yield <f64> None, None, 1.0
$ wavelength_nm <str> '290,291,292,...', '290,291,292,...', '190,195,200,...'
$ sigma_298_cm2 <str> '1.43E-18,1.27E-18,1.11E-18,...',
                      '1.43E-18,1.27E-18,1.11E-18,...',
                      '6.72E-19,5.63E-19,4.75E-19,...'
```

"""

nuclides: pd.DataFrame = pd.read_csv(_nuclides_fname, dtype=_nuclides_dtype)  # type: ignore
nuclides.__doc__ = """
Nuclide data.

The `nuclides` dataset contains information on all known nuclides, providing data on nuclear
structure and decay modes across 118 elements. There is data here on natural abundances, atomic
mass, spin, half-life, and more. The typical users for such a dataset include researchers in fields
such as nuclear physics, radiochemistry, and nuclear medicine.

Details
-------
This is a dataset with 3,383 rows and 29 columns.

- `nuclide`: The symbol for the nuclide.
- `z`, `n`: The number of protons and neutrons.
- `element`: The element symbol.
- `radius`, `radius_uncert`: The charge radius and its associated uncertainty. In units of fm.
- `abundance`, `abundance_uncert`: The abundance of the stable isotope as a mole fraction (in
relation to other stable isotopes of the same element). Values are provided for the nuclide only if
`is_stable` is `"TRUE"`.
- `is_stable`: Is the nuclide a stable isotope?
- `half_life`, `half_life_uncert`: The nuclide's half life represented as seconds.
- `isospin`: The isospin, or the quantum number related to the up and down quark content of the
particle.
- `decay_1`, `decay_2`, `decay_3`: The 1st, 2nd, and 3rd decay modes.
- `decay_1_pct`, `decay_1_pct_uncert`, `decay_2_pct`, `decay_2_pct_uncert`, `decay_3_pct`,
`decay_3_pct_uncert`: The branching proportions for the 1st, 2nd, and 3rd decays (along with
uncertainty values).
- `magnetic_dipole`, `magnetic_dipole_uncert`: The magnetic dipole and its associated uncertainty.
Expressed in units of micro N, or nuclear magneton values.
- `electric_quadrupole`, `electric_quadrupole_uncert`: The electric quadrupole and its associated
uncertainty. In units of barn (b).
- `atomic_mass`, `atomic_mass_uncert`: The atomic mass and its associated uncertainty. In units of
micro AMU.
- `mass_excess`, `mass_excess_uncert`: The mass excess and its associated uncertainty. In units of
keV.

Preview
-------
```
Rows: 3383
Columns: 29
$ nuclide                    <str> '^{1}_{1}H0', '^{2}_{1}H1', '^{3}_{1}H2'
$ z                          <i64> 1, 1, 1
$ n                          <i64> 0, 1, 2
$ element                    <str> 'H', 'H', 'H'
$ radius                     <f64> 0.8783, 2.1421, 1.7591
$ radius_uncert              <f64> 0.0086, 0.0088, 0.0363
$ abundance                  <f64> 0.999855, 0.000145, None
$ abundance_uncert           <f64> 7.8e-05, 7.8e-05, None
$ is_stable                  <str> 'TRUE', 'TRUE', 'FALSE'
$ half_life                  <f64> None, None, 388781328.00697297
$ half_life_uncert           <f64> None, None, 631138.51949184
$ isospin                    <str> None, None, None
$ decay_1                    <str> None, None, 'B-'
$ decay_1_pct                <f64> None, None, 1.0
$ decay_1_pct_uncert         <f64> None, None, None
$ decay_2                    <str> None, None, None
$ decay_2_pct                <f64> None, None, None
$ decay_2_pct_uncert         <f64> None, None, None
$ decay_3                    <str> None, None, None
$ decay_3_pct                <f64> None, None, None
$ decay_3_pct_uncert         <f64> None, None, None
$ magnetic_dipole            <f64> 2.792847351, 0.857438231, 2.97896246
$ magnetic_dipole_uncert     <f64> 9e-09, 5e-09, 1.4e-08
$ electric_quadrupole        <f64> None, 0.0028578, None
$ electric_quadrupole_uncert <f64> None, 3e-07, None
$ atomic_mass                <f64> 1007825.031898, 2014101.777844, 3016049.28132
$ atomic_mass_uncert         <f64> 1.4e-05, 1.5e-05, 8e-05
$ mass_excess                <f64> 7288.971064, 13135.722895, 14949.8109
$ mass_excess_uncert         <f64> 1.3e-05, 1.5e-05, 8e-05
```

"""

islands: pd.DataFrame = pd.read_csv(_islands_fname)  # type: ignore
airquality: pd.DataFrame = pd.read_csv(_airquality_fname)  # type: ignore


_x_locales_fname = DATA_MOD / "x_locales.csv"
_x_locales_dtype = {
    "country_name": "object",
    "country_code_2": "object",
    "country_code_3": "object",
    "year": "Int64",
    "population": "Int64",
    "locale": "object",
    "lang_name": "object",
    "lang_desc": "object",
    "script_name": "object",
    "script_desc": "object",
    "territory_name": "object",
    "territory_desc": "object",
    "variant_name": "object",
    "variant_desc": "object",
    "chr_index": "object",
    "decimal": "object",
    "group": "object",
    "percent_sign": "object",
    "plus_sign": "object",
    "minus_sign": "object",
    "approx_sign": "object",
    "exp_sign": "object",
    "sup_exp": "object",
    "per_mille": "object",
    "infinity": "object",
    "nan": "object",
    "approx_pattern": "object",
    "at_least_pattern": "object",
    "at_most_pattern": "object",
    "range_pattern": "object",
    "decimal_format": "object",
    "sci_format": "object",
    "percent_format": "object",
    "currency_format": "object",
    "accounting_format": "object",
    "default_numbering_system": "object",
    "minimum_grouping_digits": "Int64",
    "currency_code": "object",
    "no_table_data_text": "object",
    "sort_label_text": "object",
    "filter_label_text": "object",
    "search_placeholder_text": "object",
    "page_next_text": "object",
    "page_previous_text": "object",
    "page_numbers_text": "object",
    "page_info_text": "object",
    "page_size_options_text": "object",
    "page_next_label_text": "object",
    "page_previous_label_text": "object",
    "page_number_label_text": "object",
    "page_jump_label_text": "object",
    "page_size_options_label_text": "object",
}

__x_locales: pd.DataFrame = pd.read_csv(_x_locales_fname, dtype=_x_locales_dtype)  # type: ignore
