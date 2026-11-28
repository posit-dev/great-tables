# data.towny

Populations of all municipalities in Ontario from 1996 to 2021.

`data.towny=_read_csv(_towny_fname, dtype=_towny_dtype)`

A dataset containing census population data from six census years (1996 to 2021) for all 414 of Ontario's local municipalities. The Municipal Act of Ontario (2001) defines a local municipality as "a single-tier municipality or a lower-tier municipality". There are 173 single-tier municipalities and 241 lower-tier municipalities representing 99 percent of Ontario's population and 17 percent of its land use.

In the towny dataset we include information specific to each municipality such as location (in the latitude and longitude columns), their website URLs, their classifications, and land area sizes according to 2021 boundaries. Additionally, there are computed columns containing population density values for each census year and population change values from adjacent census years.

## Details

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

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

| name | website | status | csd_type | census_div | latitude | longitude | land_area_km2 | population_1996 | population_2001 | population_2006 | population_2011 | population_2016 | population_2021 | density_1996 | density_2001 | density_2006 | density_2011 | density_2016 | density_2021 | pop_change_1996_2001_pct | pop_change_2001_2006_pct | pop_change_2006_2011_pct | pop_change_2011_2016_pct | pop_change_2016_2021_pct |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Addington Highlands | https://addingtonhighlands.ca | lower-tier | township | Lennox and Addington | 45.0 | -77.25 | 1293.99 | 2429 | 2402 | 2512 | 2517 | 2318 | 2534 | 1.88 | 1.86 | 1.94 | 1.95 | 1.79 | 1.96 | -0.0111 | 0.0458 | 0.002 | -0.0791 | 0.0932 |
| Adelaide Metcalfe | https://adelaidemetcalfe.on.ca | lower-tier | township | Middlesex | 42.95 | -81.7 | 331.11 | 3128 | 3149 | 3135 | 3028 | 2990 | 3011 | 9.45 | 9.51 | 9.47 | 9.14 | 9.03 | 9.09 | 0.0067 | -0.0044 | -0.0341 | -0.0125 | 0.007 |
| Adjala-Tosorontio | https://www.adjtos.ca | lower-tier | township | Simcoe | 44.133333 | -79.933333 | 371.53 | 9359 | 10082 | 10695 | 10603 | 10975 | 10989 | 25.19 | 27.14 | 28.79 | 28.54 | 29.54 | 29.58 | 0.0773 | 0.0608 | -0.0086 | 0.0351 | 0.0013 |
| Admaston/Bromley | https://admastonbromley.com | lower-tier | township | Renfrew | 45.529167 | -76.896944 | 519.59 | 2837 | 2824 | 2716 | 2844 | 2935 | 2995 | 5.46 | 5.44 | 5.23 | 5.47 | 5.65 | 5.76 | -0.0046 | -0.0382 | 0.0471 | 0.032 | 0.0204 |
| Ajax | https://www.ajax.ca | lower-tier | town | Durham | 43.858333 | -79.036389 | 66.64 | 64430 | 73753 | 90167 | 109600 | 119677 | 126666 | 966.84 | 1106.74 | 1353.05 | 1644.66 | 1795.87 | 1900.75 | 0.1447 | 0.2226 | 0.2155 | 0.0919 | 0.0584 |
| Alberton | https://alberton.ca | single-tier | township | Rainy River | 48.6 | -93.533333 | 116.6 | 1027 | 956 | 958 | 864 | 969 | 954 | 8.81 | 8.2 | 8.22 | 7.41 | 8.31 | 8.18 | -0.0691 | 0.0021 | -0.0981 | 0.1215 | -0.0155 |
| Alfred and Plantagenet | https://www.alfred-plantagenet.com | lower-tier | township | Prescott and Russell | 45.566667 | -74.916667 | 391.79 | 8315 | 8593 | 8654 | 9196 | 9680 | 9949 | 21.22 | 21.93 | 22.09 | 23.47 | 24.71 | 25.39 | 0.0334 | 0.0071 | 0.0626 | 0.0526 | 0.0278 |
| Algonquin Highlands | https://www.algonquinhighlands.ca | lower-tier | township | Haliburton | 45.4 | -78.75 | 999.69 | 1687 | 1827 | 1976 | 2186 | 2351 | 2588 | 1.69 | 1.83 | 1.98 | 2.19 | 2.35 | 2.59 | 0.083 | 0.0816 | 0.1063 | 0.0755 | 0.1008 |
| Alnwick/Haldimand | https://www.ahtwp.ca | lower-tier | township | Northumberland | 44.083333 | -78.033333 | 398.25 | 5528 | 5846 | 6435 | 6617 | 6869 | 7473 | 13.88 | 14.68 | 16.16 | 16.62 | 17.25 | 18.76 | 0.0575 | 0.1008 | 0.0283 | 0.0381 | 0.0879 |
| Amaranth | https://www.amaranth.ca | lower-tier | township | Dufferin | 43.983333 | -80.233333 | 265.02 | 3450 | 3770 | 3845 | 3963 | 4079 | 4327 | 13.02 | 14.23 | 14.51 | 14.95 | 15.39 | 16.33 | 0.0928 | 0.0199 | 0.0307 | 0.0293 | 0.0608 |
