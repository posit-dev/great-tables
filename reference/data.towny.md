## data.towny


Populations of all municipalities in Ontario from 1996 to 2021.


`data.towny=_read_csv(_towny_fname, dtype=_towny_dtype)`  


A dataset containing census population data from six census years (1996 to 2021) for all 414 of Ontario's local municipalities. The Municipal Act of Ontario (2001) defines a local municipality as "a single-tier municipality or a lower-tier municipality". There are 173 single-tier municipalities and 241 lower-tier municipalities representing 99 percent of Ontario's population and 17 percent of its land use.

In the towny dataset we include information specific to each municipality such as location (in the latitude and longitude columns), their website URLs, their classifications, and land area sizes according to 2021 boundaries. Additionally, there are computed columns containing population density values for each census year and population change values from adjacent census years.


This is a dataset with 414 rows and 25 columns.

- `name`: The name of the municipality.
- `website`: The website for the municipality. This is missing if there isn't an official site.
- `status`: The status of the municipality. This is either `"lower-tier"` or `"single-tier"`. A single-tier municipality, which takes on all municipal duties outlined in the Municipal Act and other Provincial laws, is independent of an upper-tier municipality. Part of an upper-tier municipality is a lower-tier municipality. The upper-tier and lower-tier municipalities are responsible for carrying out the duties laid out in the Municipal Act and other provincial laws.
- `csd_type`: The Census Subdivision Type. This can be one of `"village"`, `"town"`, `"township"`, `"municipality"`, or `"city"`.
- `census_div`: The Census division, of which there are 49. This is made up of single-tier municipalities, regional municipalities, counties, and districts.
- `latitude`, `longitude`: The location of the municipality, given as latitude and longitude values in decimal degrees.
- `land_area_km2`: The total area of the local municipality in square kilometers.
- `population_1996`, `population_2001`, `population_2006`, `population_2011`, `population_2016`, `population_2021`: Population values for each municipality from the 1996 to 2021 census years.
- `density_1996`, `density_2001`, `density_2006`, `density_2011`, `density_2016`, `density_2021`: Population density values, calculated as persons per square kilometer, for each municipality from the 1996 to 2021 census years.
- `pop_change_1996_2001_pct`, `pop_change_2001_2006_pct`, `pop_change_2006_2011_pct`, `pop_change_2011_2016_pct`, `pop_change_2016_2021_pct`: Population changes between adjacent pairs of census years, from 1996 to 2021.


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
