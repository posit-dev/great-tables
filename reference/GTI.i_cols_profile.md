# GTI.i_cols_profile()

Show how the columns' values are spread, in a small plot under their labels.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L1318-L1420)

``` python
GTI.i_cols_profile(
    columns=None,
    plot="auto",
)
```

A column's profile is a plot under its label of the values in the rows the table shows: a histogram of its numbers or dates (`"histogram"`: how many rows have a value in each of up to 20 equal ranges, from the column's lowest value to its highest; or one per value, for whole numbers or days a few apart), or bars for its most common values (`"top"`: the 5 that most rows have, with a bar for the others). Under the plot are the lowest and highest values the rows show (for a histogram) or the number of values they have (for the others), as the table formats them, and the share of the rows with a missing value. Pointing at a bar shows its values and its number of rows. As the reader searches and filters the table, the profiles show only the rows that are left (their ranges and values stay the same, so that they're easy to compare), but not as the table is sorted, or paged. Profiles are off by default, and aren't shown in a table stacked as cards.

Each call sets the profiles of the columns it's given, so that some columns can have one plot, and others another; a later call for a column replaces what an earlier one set.

## Parameters

`columns: SelectExpr = None`  
The columns to profile: a column name, a list of them, or a selector (e.g., Polars' `cs.numeric()`). With `None` (the default), every column but the stub (which can be named). The row group column can't be profiled, and neither can a column left out of the table.

`plot: ProfilePlot | None = "auto"`  
The plot: `"histogram"` (for columns of numbers, dates, or dates and times), or `"top"` (the most common values), or `"auto"` to choose by the column: a histogram for numbers and dates, and the most common values otherwise. With `None`, the columns have no profile.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table of Ontario's municipalities with a profile of their statuses (their most common ones) and of their populations (a histogram), which follow the rows a search or a filter leaves (try searching for "county").

``` python
from great_tables import GTI
from great_tables.data import towny

(
    GTI(
        towny[["name", "status", "density_2021", "population_2021"]],
        rowname_col="name",
    )
    .fmt_integer(columns=["density_2021", "population_2021"])
    .i_cols_filter(columns="status")
    .i_cols_profile(columns=["status", "density_2021", "population_2021"])
)
```

|  | status | density_2021 | population_2021 |
|----|----|----|----|
| Addington Highlands | lower-tier | 2 | 2,534 |
| Adelaide Metcalfe | lower-tier | 9 | 3,011 |
| Adjala-Tosorontio | lower-tier | 30 | 10,989 |
| Admaston/Bromley | lower-tier | 6 | 2,995 |
| Ajax | lower-tier | 1,901 | 126,666 |
| Alberton | single-tier | 8 | 954 |
| Alfred and Plantagenet | lower-tier | 25 | 9,949 |
| Algonquin Highlands | lower-tier | 3 | 2,588 |
| Alnwick/Haldimand | lower-tier | 19 | 7,473 |
| Amaranth | lower-tier | 16 | 4,327 |
| Amherstburg | lower-tier | 128 | 23,524 |
| The Archipelago | single-tier | 2 | 979 |
| Armour | single-tier | 9 | 1,459 |
| Armstrong | single-tier | 13 | 1,199 |
| Arnprior | lower-tier | 738 | 9,629 |
| Arran-Elderslie | lower-tier | 15 | 6,913 |
| Ashfield-Colborne-Wawanosh | lower-tier | 10 | 5,884 |
| Asphodel-Norwood | lower-tier | 29 | 4,658 |
| Assiginack | single-tier | 4 | 1,008 |
| Athens | lower-tier | 23 | 3,042 |
| Atikokan | single-tier | 8 | 2,642 |
| Augusta | lower-tier | 24 | 7,386 |
| Aurora | lower-tier | 1,241 | 62,057 |
| Aylmer | lower-tier | 1,209 | 7,699 |
| Baldwin | single-tier | 7 | 579 |
| Bancroft | lower-tier | 18 | 4,065 |
| Barrie | single-tier | 1,493 | 147,829 |
| Bayham | lower-tier | 29 | 7,096 |
| Beckwith | lower-tier | 38 | 9,021 |
| Belleville | single-tier | 223 | 55,071 |
| Billings | single-tier | 4 | 753 |
| Black River-Matheson | single-tier | 2 | 2,572 |
| Blandford-Blenheim | lower-tier | 20 | 7,565 |
| Blind River | single-tier | 7 | 3,422 |
| The Blue Mountains | lower-tier | 33 | 9,390 |
| Bluewater | lower-tier | 18 | 7,540 |
| Bonfield | single-tier | 10 | 2,146 |
| Bonnechere Valley | lower-tier | 7 | 3,898 |
| Bracebridge | lower-tier | 28 | 17,305 |
| Bradford West Gwillimbury | lower-tier | 214 | 42,880 |
| Brampton | lower-tier | 2,469 | 656,480 |
| Brant | single-tier | 48 | 39,474 |
| Brantford | single-tier | 1,061 | 104,688 |
| Brethour | single-tier | 1 | 105 |
| Brighton | lower-tier | 54 | 12,108 |
| Brock | lower-tier | 30 | 12,567 |
| Brockton | lower-tier | 17 | 9,784 |
| Brockville | single-tier | 1,058 | 22,116 |
| Brooke-Alvinston | lower-tier | 8 | 2,359 |
| Bruce Mines | single-tier | 96 | 582 |
| Brudenell, Lyndoch and Raglan | lower-tier | 2 | 1,552 |
| Burk's Falls | single-tier | 310 | 957 |
| Burlington | lower-tier | 1,004 | 186,948 |
| Burpee and Mills | single-tier | 2 | 382 |
| Caledon | lower-tier | 111 | 76,581 |
| Callander | single-tier | 38 | 3,964 |
| Calvin | single-tier | 4 | 557 |
| Cambridge | lower-tier | 1,226 | 138,479 |
| Carleton Place | lower-tier | 1,259 | 12,517 |
| Carling | single-tier | 6 | 1,491 |
| Carlow/Mayo | lower-tier | 2 | 953 |
| Casey | single-tier | 4 | 341 |
| Casselman | lower-tier | 772 | 3,960 |
| Cavan Monaghan | lower-tier | 33 | 10,016 |
| Central Elgin | lower-tier | 49 | 13,746 |
| Central Frontenac | lower-tier | 5 | 4,892 |
| Central Huron | lower-tier | 17 | 7,799 |
| Central Manitoulin | single-tier | 5 | 2,235 |
| Centre Hastings | lower-tier | 22 | 4,801 |
| Centre Wellington | lower-tier | 76 | 31,093 |
| Chamberlain | single-tier | 3 | 311 |
| Champlain | lower-tier | 42 | 8,665 |
| Chapleau | single-tier | 147 | 1,942 |
| Chapple | single-tier | 1 | 763 |
| Charlton and Dack | single-tier | 7 | 686 |
| Chatham-Kent | single-tier | 42 | 103,988 |
| Chatsworth | lower-tier | 12 | 7,080 |
| Chisholm | single-tier | 6 | 1,312 |
| Clarence-Rockland | lower-tier | 89 | 26,505 |
| Clarington | lower-tier | 166 | 101,427 |
| Clearview | lower-tier | 27 | 14,814 |
| Cobalt | single-tier | 478 | 989 |
| Cobourg | lower-tier | 916 | 20,519 |
| Cochrane | single-tier | 10 | 5,390 |
| Cockburn Island | single-tier | 0 | 16 |
| Coleman | single-tier | 3 | 517 |
| Collingwood | lower-tier | 748 | 24,811 |
| Conmee | single-tier | 5 | 798 |
| Cornwall | single-tier | 778 | 47,845 |
| Cramahe | lower-tier | 32 | 6,509 |
| Dawn-Euphemia | lower-tier | 4 | 1,968 |
| Dawson | single-tier | 1 | 399 |
| Deep River | lower-tier | 83 | 4,175 |
| Deseronto | lower-tier | 693 | 1,747 |
| Dorion | single-tier | 2 | 375 |
| Douro-Dummer | lower-tier | 17 | 7,632 |
| Drummond/North Elmsley | lower-tier | 22 | 8,183 |
| Dryden | single-tier | 113 | 7,388 |
| Dubreuilville | single-tier | 7 | 576 |
| Dutton/Dunwich | lower-tier | 14 | 4,152 |
| Dysart, Dudley, Harcourt, Guilford, Harburn, Bruton, Havelock, Eyre and Clyde | lower-tier | 5 | 7,182 |
| Ear Falls | single-tier | 3 | 924 |
| East Ferris | single-tier | 33 | 4,946 |
| East Garafraxa | lower-tier | 17 | 2,794 |
| East Gwillimbury | lower-tier | 141 | 34,637 |
| East Hawkesbury | lower-tier | 15 | 3,418 |
| East Zorra-Tavistock | lower-tier | 32 | 7,841 |
| Edwardsburgh/Cardinal | lower-tier | 24 | 7,505 |
| Elizabethtown-Kitley | lower-tier | 17 | 9,545 |
| Elliot Lake | single-tier | 16 | 11,372 |
| Emo | single-tier | 6 | 1,204 |
| Englehart | single-tier | 494 | 1,442 |
| Enniskillen | lower-tier | 8 | 2,825 |
| Erin | lower-tier | 40 | 11,981 |
| Espanola | single-tier | 64 | 5,185 |
| Essa | lower-tier | 82 | 22,970 |
| Essex | lower-tier | 76 | 21,216 |
| Evanturel | single-tier | 6 | 502 |
| Faraday | lower-tier | 7 | 1,612 |
| Fauquier-Strickland | single-tier | 0 | 467 |
| Fort Erie | lower-tier | 198 | 32,901 |
| Fort Frances | single-tier | 292 | 7,466 |
| French River | single-tier | 4 | 2,828 |
| Front of Yonge | lower-tier | 21 | 2,595 |
| Frontenac Islands | lower-tier | 11 | 1,930 |
| Gananoque | single-tier | 768 | 5,383 |
| Gauthier | single-tier | 2 | 151 |
| Georgian Bay | lower-tier | 7 | 3,441 |
| Georgian Bluffs | lower-tier | 18 | 11,100 |
| Georgina | lower-tier | 166 | 47,642 |
| Gillies | single-tier | 5 | 441 |
| Goderich | lower-tier | 923 | 7,881 |
| Gordon/Barrie Island | single-tier | 2 | 613 |
| Gore Bay | single-tier | 157 | 808 |
| Grand Valley | lower-tier | 24 | 3,851 |
| Gravenhurst | lower-tier | 27 | 13,157 |
| Greater Madawaska | lower-tier | 3 | 2,864 |
| Greater Napanee | lower-tier | 37 | 16,879 |
| Greater Sudbury | single-tier | 52 | 166,004 |
| Greenstone | single-tier | 2 | 4,309 |
| Grey Highlands | lower-tier | 12 | 10,424 |
| Grimsby | lower-tier | 420 | 28,883 |
| Guelph | single-tier | 1,644 | 143,740 |
| Guelph/Eramosa | lower-tier | 47 | 13,904 |
| Haldimand | single-tier | 39 | 49,216 |
| Halton Hills | lower-tier | 227 | 62,951 |
| Hamilton | lower-tier | 43 | 11,059 |
| Hamilton | single-tier | 509 | 569,353 |
| Hanover | lower-tier | 815 | 7,967 |
| Harley | single-tier | 6 | 524 |
| Harris | single-tier | 11 | 530 |
| Hastings Highlands | lower-tier | 5 | 4,385 |
| Havelock-Belmont-Methuen | lower-tier | 10 | 5,083 |
| Hawkesbury | lower-tier | 1,009 | 10,194 |
| Head, Clara and Maria | lower-tier | 0 | 267 |
| Hearst | single-tier | 49 | 4,794 |
| Highlands East | lower-tier | 6 | 3,830 |
| Hilliard | single-tier | 2 | 215 |
| Hilton | single-tier | 3 | 382 |
| Hilton Beach | single-tier | 79 | 198 |
| Hornepayne | single-tier | 5 | 968 |
| Horton | lower-tier | 20 | 3,182 |
| Howick | lower-tier | 14 | 4,045 |
| Hudson | single-tier | 6 | 530 |
| Huntsville | lower-tier | 30 | 21,147 |
| Huron East | lower-tier | 14 | 9,512 |
| Huron Shores | single-tier | 4 | 1,860 |
| Huron-Kinloss | lower-tier | 18 | 7,723 |
| Ignace | single-tier | 17 | 1,206 |
| Ingersoll | lower-tier | 1,076 | 13,693 |
| Innisfil | lower-tier | 165 | 43,326 |
| Iroquois Falls | single-tier | 7 | 4,418 |
| James | single-tier | 4 | 348 |
| Jocelyn | single-tier | 2 | 314 |
| Johnson | single-tier | 6 | 749 |
| Joly | single-tier | 2 | 293 |
| Kapuskasing | single-tier | 96 | 8,057 |
| Kawartha Lakes | single-tier | 26 | 79,247 |
| Kearney | single-tier | 2 | 974 |
| Kenora | single-tier | 71 | 14,967 |
| Kerns | single-tier | 4 | 330 |
| Killaloe, Hagarty and Richards | lower-tier | 6 | 2,410 |
| Killarney | single-tier | 0 | 397 |
| Kincardine | lower-tier | 23 | 12,268 |
| King | lower-tier | 82 | 27,333 |
| Kingston | single-tier | 293 | 132,485 |
| Kingsville | lower-tier | 90 | 22,119 |
| Kirkland Lake | single-tier | 30 | 7,750 |
| Kitchener | lower-tier | 1,878 | 256,885 |
| La Vallee | single-tier | 3 | 788 |
| Laird | single-tier | 11 | 1,121 |
| Lake of Bays | lower-tier | 6 | 3,759 |
| Lake of the Woods | single-tier | 0 | 308 |
| Lakeshore | lower-tier | 76 | 40,410 |
| Lambton Shores | lower-tier | 36 | 11,876 |
| Lanark Highlands | lower-tier | 6 | 5,737 |
| Larder Lake | single-tier | 3 | 745 |
| LaSalle | lower-tier | 504 | 32,721 |
| Latchford | single-tier | 2 | 355 |
| Laurentian Hills | lower-tier | 5 | 2,885 |
| Laurentian Valley | lower-tier | 18 | 9,450 |
| Leamington | lower-tier | 114 | 29,680 |
| Leeds and the Thousand Islands | lower-tier | 16 | 9,804 |
| Limerick | lower-tier | 2 | 436 |
| Lincoln | lower-tier | 158 | 25,719 |
| London | single-tier | 1,004 | 422,324 |
| Loyalist | lower-tier | 52 | 17,943 |
| Lucan Biddulph | lower-tier | 34 | 5,680 |
| Macdonald, Meredith and Aberdeen Additional | single-tier | 9 | 1,513 |
| Machar | single-tier | 5 | 969 |
| Machin | single-tier | 3 | 1,012 |
| Madawaska Valley | lower-tier | 6 | 3,927 |
| Madoc | lower-tier | 8 | 2,233 |
| Magnetawan | single-tier | 3 | 1,753 |
| Malahide | lower-tier | 24 | 9,308 |
| Manitouwadge | single-tier | 6 | 1,974 |
| Mapleton | lower-tier | 20 | 10,839 |
| Marathon | single-tier | 19 | 3,138 |
| Markham | lower-tier | 1,605 | 338,503 |
| Markstay-Warren | single-tier | 5 | 2,708 |
| Marmora and Lake | lower-tier | 8 | 4,267 |
| Matachewan | single-tier | 0 | 268 |
| Mattawa | single-tier | 513 | 1,881 |
| Mattawan | single-tier | 1 | 153 |
| Mattice-Val Côté | single-tier | 1 | 542 |
| McDougall | single-tier | 10 | 2,744 |
| McGarry | single-tier | 7 | 579 |
| McKellar | single-tier | 8 | 1,419 |
| McMurrich/Monteith | single-tier | 3 | 907 |
| McNab/Braeside | lower-tier | 30 | 7,591 |
| Meaford | lower-tier | 20 | 11,485 |
| Melancthon | lower-tier | 10 | 3,132 |
| Merrickville-Wolford | lower-tier | 15 | 3,135 |
| Middlesex Centre | lower-tier | 32 | 18,928 |
| Midland | lower-tier | 504 | 17,817 |
| Milton | lower-tier | 366 | 132,979 |
| Minden Hills | lower-tier | 8 | 6,971 |
| Minto | lower-tier | 30 | 9,094 |
| Mississauga | lower-tier | 2,453 | 717,961 |
| Mississippi Mills | lower-tier | 29 | 14,740 |
| Mono | lower-tier | 34 | 9,421 |
| Montague | lower-tier | 14 | 3,914 |
| Moonbeam | single-tier | 5 | 1,157 |
| Moosonee | single-tier | 3 | 1,512 |
| Morley | single-tier | 1 | 493 |
| Morris-Turnberry | lower-tier | 10 | 3,590 |
| Mulmur | lower-tier | 12 | 3,571 |
| Muskoka Lakes | lower-tier | 10 | 7,652 |
| Nairn and Hyman | single-tier | 2 | 373 |
| The Nation | lower-tier | 20 | 13,350 |
| Neebing | single-tier | 3 | 2,241 |
| New Tecumseth | lower-tier | 160 | 43,948 |
| Newbury | lower-tier | 249 | 440 |
| Newmarket | lower-tier | 2,284 | 87,942 |
| Niagara Falls | lower-tier | 449 | 94,415 |
| Niagara-on-the-Lake | lower-tier | 145 | 19,088 |
| Nipigon | single-tier | 14 | 1,473 |
| Nipissing | single-tier | 5 | 1,769 |
| Norfolk | single-tier | 42 | 67,490 |
| North Algona Wilberforce | lower-tier | 8 | 3,111 |
| North Bay | single-tier | 167 | 52,662 |
| North Dumfries | lower-tier | 56 | 10,619 |
| North Dundas | lower-tier | 22 | 11,304 |
| North Frontenac | lower-tier | 2 | 2,285 |
| North Glengarry | lower-tier | 16 | 10,144 |
| North Grenville | lower-tier | 51 | 17,964 |
| North Huron | lower-tier | 28 | 5,052 |
| North Kawartha | lower-tier | 4 | 2,877 |
| North Middlesex | lower-tier | 11 | 6,307 |
| North Perth | lower-tier | 32 | 15,538 |
| The North Shore | single-tier | 2 | 531 |
| North Stormont | lower-tier | 14 | 7,400 |
| Northeastern Manitoulin and the Islands | single-tier | 5 | 2,641 |
| Northern Bruce Peninsula | lower-tier | 6 | 4,404 |
| Norwich | lower-tier | 26 | 11,151 |
| Oakville | lower-tier | 1,538 | 213,759 |
| O'Connor | single-tier | 6 | 689 |
| Oil Springs | lower-tier | 79 | 647 |
| Oliver Paipoonge | single-tier | 17 | 6,035 |
| Opasatika | single-tier | 1 | 200 |
| Orangeville | lower-tier | 1,990 | 30,167 |
| Orillia | single-tier | 1,171 | 33,411 |
| Oro-Medonte | lower-tier | 39 | 23,017 |
| Oshawa | lower-tier | 1,204 | 175,383 |
| Otonabee-South Monaghan | lower-tier | 20 | 7,087 |
| Ottawa | single-tier | 365 | 1,017,449 |
| Owen Sound | lower-tier | 893 | 21,612 |
| Papineau-Cameron | single-tier | 2 | 982 |
| Parry Sound | single-tier | 525 | 6,879 |
| Pelee | single-tier | 6 | 230 |
| Pelham | lower-tier | 144 | 18,192 |
| Pembroke | single-tier | 1,003 | 14,364 |
| Penetanguishene | lower-tier | 396 | 10,077 |
| Perry | single-tier | 14 | 2,650 |
| Perth | lower-tier | 530 | 6,469 |
| Perth East | lower-tier | 18 | 12,595 |
| Perth South | lower-tier | 10 | 3,776 |
| Petawawa | lower-tier | 110 | 18,160 |
| Peterborough | single-tier | 1,292 | 83,651 |
| Petrolia | lower-tier | 483 | 6,013 |
| Pickering | lower-tier | 429 | 99,186 |
| Pickle Lake | single-tier | 2 | 398 |
| Plummer Additional | single-tier | 3 | 757 |
| Plympton-Wyoming | lower-tier | 26 | 8,308 |
| Point Edward | lower-tier | 585 | 1,930 |
| Port Colborne | lower-tier | 164 | 20,033 |
| Port Hope | lower-tier | 62 | 17,294 |
| Powassan | single-tier | 15 | 3,346 |
| Prescott | single-tier | 826 | 4,078 |
| Prince | single-tier | 11 | 975 |
| Prince Edward | single-tier | 24 | 25,704 |
| Puslinch | lower-tier | 37 | 7,944 |
| Quinte West | single-tier | 94 | 46,560 |
| Rainy River | single-tier | 241 | 752 |
| Ramara | lower-tier | 25 | 10,377 |
| Red Lake | single-tier | 7 | 4,094 |
| Red Rock | single-tier | 14 | 895 |
| Renfrew | lower-tier | 639 | 8,190 |
| Richmond Hill | lower-tier | 2,004 | 202,022 |
| Rideau Lakes | lower-tier | 15 | 10,883 |
| Russell | lower-tier | 99 | 19,598 |
| Ryerson | single-tier | 4 | 745 |
| Sables-Spanish Rivers | single-tier | 4 | 3,237 |
| Sarnia | lower-tier | 440 | 72,047 |
| Saugeen Shores | lower-tier | 93 | 15,908 |
| Sault Ste. Marie | single-tier | 325 | 72,051 |
| Schreiber | single-tier | 29 | 1,039 |
| Scugog | lower-tier | 45 | 21,581 |
| Seguin | single-tier | 9 | 5,280 |
| Selwyn | lower-tier | 59 | 18,653 |
| Severn | lower-tier | 28 | 14,576 |
| Shelburne | lower-tier | 1,371 | 8,994 |
| Shuniah | single-tier | 6 | 3,247 |
| Sioux Lookout | single-tier | 15 | 5,839 |
| Sioux Narrows-Nestor Falls | single-tier | 1 | 727 |
| Smiths Falls | single-tier | 958 | 9,254 |
| Smooth Rock Falls | single-tier | 6 | 1,200 |
| South Algonquin | single-tier | 1 | 1,055 |
| South Bruce | lower-tier | 12 | 5,880 |
| South Bruce Peninsula | lower-tier | 17 | 9,137 |
| South Dundas | lower-tier | 21 | 11,044 |
| South Frontenac | lower-tier | 21 | 20,188 |
| South Glengarry | lower-tier | 22 | 13,330 |
| South Huron | lower-tier | 24 | 10,063 |
| South River | single-tier | 268 | 1,101 |
| South Stormont | lower-tier | 30 | 13,570 |
| Southgate | lower-tier | 14 | 8,716 |
| Southwest Middlesex | lower-tier | 14 | 5,893 |
| South-West Oxford | lower-tier | 21 | 7,583 |
| Southwold | lower-tier | 16 | 4,851 |
| Spanish | single-tier | 6 | 670 |
| Springwater | lower-tier | 40 | 21,701 |
| St. Catharines | lower-tier | 1,422 | 136,803 |
| St. Clair | lower-tier | 24 | 14,659 |
| St. Joseph | single-tier | 11 | 1,426 |
| St. Marys | single-tier | 594 | 7,386 |
| St. Thomas | single-tier | 1,203 | 42,840 |
| St.-Charles | single-tier | 4 | 1,357 |
| Stirling-Rawdon | lower-tier | 18 | 5,015 |
| Stone Mills | lower-tier | 11 | 7,826 |
| Stratford | single-tier | 1,107 | 33,232 |
| Strathroy-Caradoc | lower-tier | 88 | 23,871 |
| Strong | single-tier | 10 | 1,566 |
| Sundridge | single-tier | 417 | 938 |
| Tarbutt | single-tier | 11 | 573 |
| Tay | lower-tier | 80 | 11,091 |
| Tay Valley | lower-tier | 11 | 5,925 |
| Tecumseh | lower-tier | 246 | 23,300 |
| Tehkummah | single-tier | 3 | 450 |
| Temagami | single-tier | 0 | 862 |
| Temiskaming Shores | single-tier | 55 | 9,634 |
| Terrace Bay | single-tier | 10 | 1,528 |
| Thames Centre | lower-tier | 32 | 13,980 |
| Thessalon | single-tier | 288 | 1,260 |
| Thornloe | single-tier | 14 | 92 |
| Thorold | lower-tier | 286 | 23,816 |
| Thunder Bay | single-tier | 332 | 108,843 |
| Tillsonburg | lower-tier | 839 | 18,615 |
| Timmins | single-tier | 14 | 41,145 |
| Tiny | lower-tier | 39 | 12,966 |
| Toronto | single-tier | 4,428 | 2,794,356 |
| Trent Hills | lower-tier | 27 | 13,861 |
| Trent Lakes | lower-tier | 8 | 6,439 |
| Tudor and Cashel | lower-tier | 2 | 740 |
| Tweed | lower-tier | 7 | 6,067 |
| Tyendinaga | lower-tier | 15 | 4,538 |
| Uxbridge | lower-tier | 51 | 21,556 |
| Val Rita-Harty | single-tier | 2 | 757 |
| Vaughan | lower-tier | 1,186 | 323,103 |
| Wainfleet | lower-tier | 32 | 6,887 |
| Warwick | lower-tier | 13 | 3,641 |
| Wasaga Beach | lower-tier | 433 | 24,862 |
| Waterloo | lower-tier | 1,896 | 121,436 |
| Wawa | single-tier | 7 | 2,705 |
| Welland | lower-tier | 687 | 55,750 |
| Wellesley | lower-tier | 41 | 11,318 |
| Wellington North | lower-tier | 24 | 12,431 |
| West Elgin | lower-tier | 16 | 5,060 |
| West Grey | lower-tier | 15 | 13,131 |
| West Lincoln | lower-tier | 40 | 15,454 |
| West Nipissing | single-tier | 7 | 14,583 |
| West Perth | lower-tier | 16 | 9,038 |
| Westport | lower-tier | 290 | 634 |
| Whitby | lower-tier | 944 | 138,501 |
| Whitchurch-Stouffville | lower-tier | 242 | 49,864 |
| White River | single-tier | 6 | 557 |
| Whitestone | single-tier | 1 | 1,075 |
| Whitewater | lower-tier | 13 | 7,225 |
| Wilmot | lower-tier | 81 | 21,429 |
| Windsor | single-tier | 1,573 | 229,660 |
| Wollaston | lower-tier | 3 | 721 |
| Woodstock | lower-tier | 827 | 46,705 |
| Woolwich | lower-tier | 83 | 26,999 |
| Zorra | lower-tier | 16 | 8,628 |

A column of dates (here, made from the dataset's text) has a histogram of them, from its first date to its last.

``` python
import pandas as pd
from great_tables.data import sp500

sp500_2015 = sp500[sp500["date"] >= "2015-01-01"].assign(
    date=lambda df: pd.to_datetime(df["date"])
)

(
    GTI(sp500_2015[["date", "open", "close", "volume"]])
    .fmt_date(columns="date", date_style="month_day_year")
    .fmt_currency(columns=["open", "close"])
    .fmt_number(columns="volume", compact=True)
    .i_cols_profile()
)
```

| date               | open       | close      | volume  |
|--------------------|------------|------------|---------|
| December 31, 2015  | \$2,060.59 | \$2,043.94 | 2.66B   |
| December 30, 2015  | \$2,077.34 | \$2,063.36 | 2.37B   |
| December 29, 2015  | \$2,060.54 | \$2,078.36 | 2.54B   |
| December 28, 2015  | \$2,057.77 | \$2,056.50 | 2.49B   |
| December 24, 2015  | \$2,063.52 | \$2,060.99 | 1.41B   |
| December 23, 2015  | \$2,042.20 | \$2,064.29 | 3.48B   |
| December 22, 2015  | \$2,023.15 | \$2,038.97 | 3.52B   |
| December 21, 2015  | \$2,010.27 | \$2,021.15 | 3.76B   |
| December 18, 2015  | \$2,040.81 | \$2,005.55 | 6.68B   |
| December 17, 2015  | \$2,073.76 | \$2,041.89 | 4.33B   |
| December 16, 2015  | \$2,046.50 | \$2,073.07 | 4.64B   |
| December 15, 2015  | \$2,025.55 | \$2,043.41 | 4.35B   |
| December 14, 2015  | \$2,013.37 | \$2,021.94 | 4.61B   |
| December 11, 2015  | \$2,047.27 | \$2,012.37 | 4.30B   |
| December 10, 2015  | \$2,047.93 | \$2,052.23 | 3.72B   |
| December 9, 2015   | \$2,061.17 | \$2,047.62 | 4.39B   |
| December 8, 2015   | \$2,073.39 | \$2,063.59 | 4.17B   |
| December 7, 2015   | \$2,090.42 | \$2,077.07 | 4.04B   |
| December 4, 2015   | \$2,051.24 | \$2,091.69 | 4.21B   |
| December 3, 2015   | \$2,080.71 | \$2,049.62 | 4.31B   |
| December 2, 2015   | \$2,101.71 | \$2,079.51 | 3.95B   |
| December 1, 2015   | \$2,082.93 | \$2,102.63 | 3.71B   |
| November 30, 2015  | \$2,090.95 | \$2,080.41 | 4.25B   |
| November 27, 2015  | \$2,088.82 | \$2,090.11 | 1.47B   |
| November 25, 2015  | \$2,089.30 | \$2,088.87 | 2.85B   |
| November 24, 2015  | \$2,084.42 | \$2,089.14 | 3.88B   |
| November 23, 2015  | \$2,089.41 | \$2,086.59 | 3.59B   |
| November 20, 2015  | \$2,082.82 | \$2,089.17 | 3.93B   |
| November 19, 2015  | \$2,083.70 | \$2,081.24 | 3.63B   |
| November 18, 2015  | \$2,051.99 | \$2,083.58 | 3.93B   |
| November 17, 2015  | \$2,053.67 | \$2,050.44 | 4.43B   |
| November 16, 2015  | \$2,022.08 | \$2,053.19 | 3.74B   |
| November 13, 2015  | \$2,044.64 | \$2,023.04 | 4.28B   |
| November 12, 2015  | \$2,072.29 | \$2,045.97 | 4.02B   |
| November 11, 2015  | \$2,083.41 | \$2,075.00 | 3.69B   |
| November 10, 2015  | \$2,077.19 | \$2,081.72 | 3.82B   |
| November 9, 2015   | \$2,096.56 | \$2,078.58 | 3.88B   |
| November 6, 2015   | \$2,098.60 | \$2,099.20 | 4.37B   |
| November 5, 2015   | \$2,101.68 | \$2,099.93 | 4.05B   |
| November 4, 2015   | \$2,110.60 | \$2,102.31 | 4.08B   |
| November 3, 2015   | \$2,102.63 | \$2,109.79 | 4.27B   |
| November 2, 2015   | \$2,080.76 | \$2,104.05 | 3.76B   |
| October 30, 2015   | \$2,090.00 | \$2,079.36 | 4.26B   |
| October 29, 2015   | \$2,088.35 | \$2,089.41 | 4.01B   |
| October 28, 2015   | \$2,066.48 | \$2,090.35 | 4.70B   |
| October 27, 2015   | \$2,068.75 | \$2,065.89 | 4.22B   |
| October 26, 2015   | \$2,075.08 | \$2,071.18 | 3.39B   |
| October 23, 2015   | \$2,058.19 | \$2,075.15 | 4.11B   |
| October 22, 2015   | \$2,021.88 | \$2,052.51 | 4.43B   |
| October 21, 2015   | \$2,033.47 | \$2,018.94 | 3.63B   |
| October 20, 2015   | \$2,033.13 | \$2,030.77 | 3.33B   |
| October 19, 2015   | \$2,031.73 | \$2,033.66 | 3.29B   |
| October 16, 2015   | \$2,024.37 | \$2,033.11 | 3.60B   |
| October 15, 2015   | \$1,996.47 | \$2,023.86 | 3.75B   |
| October 14, 2015   | \$2,003.66 | \$1,994.24 | 3.64B   |
| October 13, 2015   | \$2,015.00 | \$2,003.69 | 3.40B   |
| October 12, 2015   | \$2,015.65 | \$2,017.46 | 2.89B   |
| October 9, 2015    | \$2,013.73 | \$2,014.89 | 3.71B   |
| October 8, 2015    | \$1,994.01 | \$2,013.43 | 3.94B   |
| October 7, 2015    | \$1,982.34 | \$1,995.83 | 4.67B   |
| October 6, 2015    | \$1,986.63 | \$1,979.92 | 4.20B   |
| October 5, 2015    | \$1,954.33 | \$1,987.05 | 4.33B   |
| October 2, 2015    | \$1,921.77 | \$1,951.36 | 4.38B   |
| October 1, 2015    | \$1,919.65 | \$1,923.82 | 3.98B   |
| September 30, 2015 | \$1,887.14 | \$1,920.03 | 4.53B   |
| September 29, 2015 | \$1,881.90 | \$1,884.09 | 4.13B   |
| September 28, 2015 | \$1,929.18 | \$1,881.77 | 4.33B   |
| September 25, 2015 | \$1,935.93 | \$1,931.34 | 3.72B   |
| September 24, 2015 | \$1,934.81 | \$1,932.24 | 4.09B   |
| September 23, 2015 | \$1,943.24 | \$1,938.76 | 3.19B   |
| September 22, 2015 | \$1,961.39 | \$1,942.74 | 3.81B   |
| September 21, 2015 | \$1,960.84 | \$1,966.97 | 3.27B   |
| September 18, 2015 | \$1,989.66 | \$1,958.03 | 6.02B   |
| September 17, 2015 | \$1,995.33 | \$1,990.20 | 4.18B   |
| September 16, 2015 | \$1,978.02 | \$1,995.31 | 3.63B   |
| September 15, 2015 | \$1,955.10 | \$1,978.09 | 3.24B   |
| September 14, 2015 | \$1,963.06 | \$1,953.03 | 3.00B   |
| September 11, 2015 | \$1,951.45 | \$1,961.05 | 3.22B   |
| September 10, 2015 | \$1,941.59 | \$1,952.29 | 3.63B   |
| September 9, 2015  | \$1,971.45 | \$1,942.04 | 3.65B   |
| September 8, 2015  | \$1,927.30 | \$1,969.41 | 3.55B   |
| September 4, 2015  | \$1,947.76 | \$1,921.22 | 3.17B   |
| September 3, 2015  | \$1,950.79 | \$1,951.13 | 3.52B   |
| September 2, 2015  | \$1,916.52 | \$1,948.86 | 3.74B   |
| September 1, 2015  | \$1,970.09 | \$1,913.85 | 4.37B   |
| August 31, 2015    | \$1,986.73 | \$1,972.18 | 3.92B   |
| August 28, 2015    | \$1,986.06 | \$1,988.87 | 3.95B   |
| August 27, 2015    | \$1,942.77 | \$1,987.66 | 5.01B   |
| August 26, 2015    | \$1,872.75 | \$1,940.51 | 5.34B   |
| August 25, 2015    | \$1,898.08 | \$1,867.61 | 5.18B   |
| August 24, 2015    | \$1,965.15 | \$1,893.21 | 6.61B   |
| August 21, 2015    | \$2,034.08 | \$1,970.89 | 5.02B   |
| August 20, 2015    | \$2,076.61 | \$2,035.73 | 3.92B   |
| August 19, 2015    | \$2,095.69 | \$2,079.61 | 3.51B   |
| August 18, 2015    | \$2,101.99 | \$2,096.92 | 2.95B   |
| August 17, 2015    | \$2,089.70 | \$2,102.44 | 2.87B   |
| August 14, 2015    | \$2,083.15 | \$2,091.54 | 2.80B   |
| August 13, 2015    | \$2,086.19 | \$2,083.39 | 3.22B   |
| August 12, 2015    | \$2,081.10 | \$2,086.05 | 4.27B   |
| August 11, 2015    | \$2,102.66 | \$2,084.07 | 3.71B   |
| August 10, 2015    | \$2,080.98 | \$2,104.18 | 3.51B   |
| August 7, 2015     | \$2,082.61 | \$2,077.57 | 3.60B   |
| August 6, 2015     | \$2,100.75 | \$2,083.56 | 4.25B   |
| August 5, 2015     | \$2,095.27 | \$2,099.84 | 3.97B   |
| August 4, 2015     | \$2,097.68 | \$2,093.32 | 3.55B   |
| August 3, 2015     | \$2,104.49 | \$2,098.04 | 3.48B   |
| July 31, 2015      | \$2,111.60 | \$2,103.84 | 3.68B   |
| July 30, 2015      | \$2,106.78 | \$2,108.63 | 3.58B   |
| July 29, 2015      | \$2,094.70 | \$2,108.57 | 4.04B   |
| July 28, 2015      | \$2,070.75 | \$2,093.25 | 4.12B   |
| July 27, 2015      | \$2,078.19 | \$2,067.64 | 3.84B   |
| July 24, 2015      | \$2,102.24 | \$2,079.65 | 3.87B   |
| July 23, 2015      | \$2,114.16 | \$2,102.15 | 3.77B   |
| July 22, 2015      | \$2,118.21 | \$2,114.15 | 3.69B   |
| July 21, 2015      | \$2,127.55 | \$2,119.21 | 3.34B   |
| July 20, 2015      | \$2,126.85 | \$2,128.28 | 3.25B   |
| July 17, 2015      | \$2,126.80 | \$2,126.64 | 3.36B   |
| July 16, 2015      | \$2,110.55 | \$2,124.29 | 3.23B   |
| July 15, 2015      | \$2,109.01 | \$2,107.40 | 3.26B   |
| July 14, 2015      | \$2,099.72 | \$2,108.95 | 3.00B   |
| July 13, 2015      | \$2,080.03 | \$2,099.60 | 3.10B   |
| July 10, 2015      | \$2,052.74 | \$2,076.62 | 3.07B   |
| July 9, 2015       | \$2,049.73 | \$2,051.31 | 3.45B   |
| July 8, 2015       | \$2,077.66 | \$2,046.68 | 3.61B   |
| July 7, 2015       | \$2,069.52 | \$2,081.34 | 4.46B   |
| July 6, 2015       | \$2,073.95 | \$2,068.76 | 3.49B   |
| July 2, 2015       | \$2,078.03 | \$2,076.78 | 3.00B   |
| July 1, 2015       | \$2,067.00 | \$2,077.42 | 3.73B   |
| June 30, 2015      | \$2,061.19 | \$2,063.11 | 4.08B   |
| June 29, 2015      | \$2,098.63 | \$2,057.64 | 3.68B   |
| June 26, 2015      | \$2,102.62 | \$2,101.49 | 5.03B   |
| June 25, 2015      | \$2,109.96 | \$2,102.31 | 3.21B   |
| June 24, 2015      | \$2,123.65 | \$2,108.58 | 3.10B   |
| June 23, 2015      | \$2,123.16 | \$2,124.20 | 3.09B   |
| June 22, 2015      | \$2,112.50 | \$2,122.85 | 3.03B   |
| June 19, 2015      | \$2,121.06 | \$2,109.99 | 4.45B   |
| June 18, 2015      | \$2,101.58 | \$2,121.24 | 3.52B   |
| June 17, 2015      | \$2,097.40 | \$2,100.44 | 3.22B   |
| June 16, 2015      | \$2,084.26 | \$2,096.29 | 2.92B   |
| June 15, 2015      | \$2,091.34 | \$2,084.43 | 3.06B   |
| June 12, 2015      | \$2,107.43 | \$2,094.11 | 2.72B   |
| June 11, 2015      | \$2,106.24 | \$2,108.86 | 3.13B   |
| June 10, 2015      | \$2,081.12 | \$2,105.20 | 3.41B   |
| June 9, 2015       | \$2,079.07 | \$2,080.15 | 3.03B   |
| June 8, 2015       | \$2,092.34 | \$2,079.28 | 2.92B   |
| June 5, 2015       | \$2,095.09 | \$2,092.83 | 3.24B   |
| June 4, 2015       | \$2,112.35 | \$2,095.84 | 3.20B   |
| June 3, 2015       | \$2,110.64 | \$2,114.07 | 3.10B   |
| June 2, 2015       | \$2,110.41 | \$2,109.60 | 3.05B   |
| June 1, 2015       | \$2,108.64 | \$2,111.73 | 3.01B   |
| May 29, 2015       | \$2,120.66 | \$2,107.39 | 3.93B   |
| May 28, 2015       | \$2,122.27 | \$2,120.79 | 2.98B   |
| May 27, 2015       | \$2,105.13 | \$2,123.48 | 3.13B   |
| May 26, 2015       | \$2,125.34 | \$2,104.20 | 3.34B   |
| May 22, 2015       | \$2,130.36 | \$2,126.06 | 2.57B   |
| May 21, 2015       | \$2,125.55 | \$2,130.82 | 3.07B   |
| May 20, 2015       | \$2,127.79 | \$2,125.85 | 3.03B   |
| May 19, 2015       | \$2,129.45 | \$2,127.83 | 3.30B   |
| May 18, 2015       | \$2,121.30 | \$2,129.20 | 2.89B   |
| May 15, 2015       | \$2,122.07 | \$2,122.73 | 3.09B   |
| May 14, 2015       | \$2,100.43 | \$2,121.10 | 3.23B   |
| May 13, 2015       | \$2,099.62 | \$2,098.48 | 3.37B   |
| May 12, 2015       | \$2,102.87 | \$2,099.12 | 3.14B   |
| May 11, 2015       | \$2,115.56 | \$2,105.33 | 2.99B   |
| May 8, 2015        | \$2,092.13 | \$2,116.10 | 3.40B   |
| May 7, 2015        | \$2,079.96 | \$2,088.00 | 3.68B   |
| May 6, 2015        | \$2,091.26 | \$2,080.15 | 3.79B   |
| May 5, 2015        | \$2,112.63 | \$2,089.46 | 3.79B   |
| May 4, 2015        | \$2,110.23 | \$2,114.49 | 3.09B   |
| May 1, 2015        | \$2,087.38 | \$2,108.29 | 3.38B   |
| April 30, 2015     | \$2,105.52 | \$2,085.51 | 4.51B   |
| April 29, 2015     | \$2,112.49 | \$2,106.85 | 4.07B   |
| April 28, 2015     | \$2,108.35 | \$2,114.76 | 3.55B   |
| April 27, 2015     | \$2,119.29 | \$2,108.92 | 3.44B   |
| April 24, 2015     | \$2,112.80 | \$2,117.69 | 3.38B   |
| April 23, 2015     | \$2,107.21 | \$2,112.93 | 3.64B   |
| April 22, 2015     | \$2,098.27 | \$2,107.96 | 3.35B   |
| April 21, 2015     | \$2,102.82 | \$2,097.29 | 3.24B   |
| April 20, 2015     | \$2,084.11 | \$2,100.40 | 3.00B   |
| April 17, 2015     | \$2,102.58 | \$2,081.18 | 3.63B   |
| April 16, 2015     | \$2,105.96 | \$2,104.99 | 3.43B   |
| April 15, 2015     | \$2,097.82 | \$2,106.63 | 4.01B   |
| April 14, 2015     | \$2,092.28 | \$2,095.84 | 3.30B   |
| April 13, 2015     | \$2,102.03 | \$2,092.43 | 2.91B   |
| April 10, 2015     | \$2,091.51 | \$2,102.06 | 536.20M |
| April 9, 2015      | \$2,081.29 | \$2,091.18 | 3.17B   |
| April 8, 2015      | \$2,076.94 | \$2,081.90 | 3.27B   |
| April 7, 2015      | \$2,080.79 | \$2,076.33 | 3.07B   |
| April 6, 2015      | \$2,064.87 | \$2,080.62 | 3.30B   |
| April 2, 2015      | \$2,060.03 | \$2,066.96 | 3.10B   |
| April 1, 2015      | \$2,067.63 | \$2,059.69 | 3.54B   |
| March 31, 2015     | \$2,084.05 | \$2,067.89 | 3.38B   |
| March 30, 2015     | \$2,064.11 | \$2,086.24 | 2.92B   |
| March 27, 2015     | \$2,055.78 | \$2,061.02 | 3.01B   |
| March 26, 2015     | \$2,059.94 | \$2,056.15 | 3.51B   |
| March 25, 2015     | \$2,093.10 | \$2,061.05 | 3.52B   |
| March 24, 2015     | \$2,103.94 | \$2,091.50 | 3.19B   |
| March 23, 2015     | \$2,107.99 | \$2,104.42 | 3.27B   |
| March 20, 2015     | \$2,090.32 | \$2,108.10 | 5.55B   |
| March 19, 2015     | \$2,098.69 | \$2,089.27 | 3.31B   |
| March 18, 2015     | \$2,072.84 | \$2,099.50 | 4.13B   |
| March 17, 2015     | \$2,080.59 | \$2,074.28 | 3.22B   |
| March 16, 2015     | \$2,055.35 | \$2,081.19 | 3.30B   |
| March 13, 2015     | \$2,064.56 | \$2,053.40 | 3.50B   |
| March 12, 2015     | \$2,041.10 | \$2,065.95 | 3.41B   |
| March 11, 2015     | \$2,044.69 | \$2,040.24 | 3.41B   |
| March 10, 2015     | \$2,076.14 | \$2,044.16 | 3.67B   |
| March 9, 2015      | \$2,072.25 | \$2,079.43 | 3.35B   |
| March 6, 2015      | \$2,100.91 | \$2,071.26 | 3.85B   |
| March 5, 2015      | \$2,098.54 | \$2,101.04 | 3.10B   |
| March 4, 2015      | \$2,107.72 | \$2,098.53 | 3.42B   |
| March 3, 2015      | \$2,115.76 | \$2,107.78 | 3.26B   |
| March 2, 2015      | \$2,105.23 | \$2,117.39 | 3.41B   |
| February 27, 2015  | \$2,110.88 | \$2,104.50 | 3.55B   |
| February 26, 2015  | \$2,113.91 | \$2,110.74 | 3.41B   |
| February 25, 2015  | \$2,115.30 | \$2,113.86 | 3.31B   |
| February 24, 2015  | \$2,109.10 | \$2,115.48 | 3.20B   |
| February 23, 2015  | \$2,109.83 | \$2,109.66 | 3.09B   |
| February 20, 2015  | \$2,097.65 | \$2,110.30 | 3.28B   |
| February 19, 2015  | \$2,099.25 | \$2,097.45 | 3.25B   |
| February 18, 2015  | \$2,099.16 | \$2,099.68 | 3.37B   |
| February 17, 2015  | \$2,096.47 | \$2,100.34 | 3.36B   |
| February 13, 2015  | \$2,088.78 | \$2,096.99 | 3.53B   |
| February 12, 2015  | \$2,069.98 | \$2,088.48 | 3.79B   |
| February 11, 2015  | \$2,068.55 | \$2,068.53 | 3.60B   |
| February 10, 2015  | \$2,049.38 | \$2,068.59 | 3.67B   |
| February 9, 2015   | \$2,053.47 | \$2,046.74 | 3.55B   |
| February 6, 2015   | \$2,062.28 | \$2,055.47 | 4.23B   |
| February 5, 2015   | \$2,043.45 | \$2,062.52 | 3.82B   |
| February 4, 2015   | \$2,048.86 | \$2,041.51 | 4.14B   |
| February 3, 2015   | \$2,022.71 | \$2,050.03 | 4.62B   |
| February 2, 2015   | \$1,996.67 | \$2,020.85 | 4.01B   |
| January 30, 2015   | \$2,019.35 | \$1,994.99 | 4.54B   |
| January 29, 2015   | \$2,002.45 | \$2,021.25 | 4.13B   |
| January 28, 2015   | \$2,032.34 | \$2,002.16 | 4.07B   |
| January 27, 2015   | \$2,047.86 | \$2,029.55 | 3.33B   |
| January 26, 2015   | \$2,050.42 | \$2,057.09 | 3.47B   |
| January 23, 2015   | \$2,062.98 | \$2,051.82 | 3.57B   |
| January 22, 2015   | \$2,034.30 | \$2,063.15 | 4.18B   |
| January 21, 2015   | \$2,020.19 | \$2,032.12 | 3.73B   |
| January 20, 2015   | \$2,020.76 | \$2,022.55 | 3.94B   |
| January 16, 2015   | \$1,992.25 | \$2,019.42 | 4.06B   |
| January 15, 2015   | \$2,013.75 | \$1,992.67 | 4.28B   |
| January 14, 2015   | \$2,018.40 | \$2,011.27 | 4.38B   |
| January 13, 2015   | \$2,031.58 | \$2,023.03 | 4.11B   |
| January 12, 2015   | \$2,046.13 | \$2,028.26 | 3.46B   |
| January 9, 2015    | \$2,063.45 | \$2,044.81 | 3.36B   |
| January 8, 2015    | \$2,030.61 | \$2,062.14 | 3.93B   |
| January 7, 2015    | \$2,005.55 | \$2,025.90 | 3.81B   |
| January 6, 2015    | \$2,022.15 | \$2,002.61 | 4.46B   |
| January 5, 2015    | \$2,054.44 | \$2,020.58 | 3.80B   |
| January 2, 2015    | \$2,058.90 | \$2,058.20 | 2.71B   |
