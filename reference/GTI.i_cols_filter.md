# GTI.i_cols_filter()

Let readers filter the table by its columns.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L844-L981)

``` python
GTI.i_cols_filter(
    columns=None,
    type="auto",
)
```

A filtered column has a filter button in its label, which opens the column's filter. Its rows are filtered by the text they show (`"text"`: those with a cell containing what's typed, ignoring case and accents, as the search does), by a choice of the column's values (`"facet"`: a checklist of them, each with the number of rows that have it, given the other filters and the search), by a range of its numbers (`"range"`: at least one value, and at most another), by a range of its dates (`"date"`: from one date, to another, picked in date fields, or date and time fields for a column with times), or by one of its booleans (`"bool"`: any value, true, false, or missing, with the number of rows that have each, and their text as the table shows it). The facets, ranges, date ranges and booleans go by the column's values, not by how they're formatted. Rows are shown when they pass every filter, and the search; the info panel (from the (i) button in the control bar) says how many filters there are, and can clear them. The bar also shows the filters that are on, and its `{ }` button opens them as text, a query as [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view) takes it, which readers can edit (with suggestions as they type, and a column's label in place of its name, which is put there for it). Filters are off by default.

Each call sets the filters of the columns it's given, so that some columns can be filtered one way, and others another; a later call for a column replaces what an earlier one set.

## Parameters

`columns: SelectExpr = None`  
The columns to filter by: a column name, a list of them, or a selector (e.g., Polars' `cs.numeric()`). With `None` (the default), every column but the stub (which can be named). The row group column can't be filtered.

`type: FilterType | None = "auto"`  
How the columns are filtered: `"text"`, `"facet"`, `"range"` (for columns of numbers), `"date"` (for columns of dates, or dates and times without a time zone), or `"bool"` (for columns of booleans), or `"auto"` to choose by the column: a range for numbers, a date range for dates, a bool filter for booleans, a facet for categories (and text columns with only a few values, each repeated), and text otherwise. With `None`, the columns aren't filtered.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table of Ontario's municipalities that can be filtered by status (a facet, as there are only a few of them) and population (a range).

``` python
from great_tables import GTI
from great_tables.data import towny

(
    GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
    .fmt_integer(columns="population_2021")
    .i_cols_filter(columns=["status", "population_2021"])
)
```

|  | status | population_2021 |
|----|----|----|
| Addington Highlands | lower-tier | 2,534 |
| Adelaide Metcalfe | lower-tier | 3,011 |
| Adjala-Tosorontio | lower-tier | 10,989 |
| Admaston/Bromley | lower-tier | 2,995 |
| Ajax | lower-tier | 126,666 |
| Alberton | single-tier | 954 |
| Alfred and Plantagenet | lower-tier | 9,949 |
| Algonquin Highlands | lower-tier | 2,588 |
| Alnwick/Haldimand | lower-tier | 7,473 |
| Amaranth | lower-tier | 4,327 |
| Amherstburg | lower-tier | 23,524 |
| The Archipelago | single-tier | 979 |
| Armour | single-tier | 1,459 |
| Armstrong | single-tier | 1,199 |
| Arnprior | lower-tier | 9,629 |
| Arran-Elderslie | lower-tier | 6,913 |
| Ashfield-Colborne-Wawanosh | lower-tier | 5,884 |
| Asphodel-Norwood | lower-tier | 4,658 |
| Assiginack | single-tier | 1,008 |
| Athens | lower-tier | 3,042 |
| Atikokan | single-tier | 2,642 |
| Augusta | lower-tier | 7,386 |
| Aurora | lower-tier | 62,057 |
| Aylmer | lower-tier | 7,699 |
| Baldwin | single-tier | 579 |
| Bancroft | lower-tier | 4,065 |
| Barrie | single-tier | 147,829 |
| Bayham | lower-tier | 7,096 |
| Beckwith | lower-tier | 9,021 |
| Belleville | single-tier | 55,071 |
| Billings | single-tier | 753 |
| Black River-Matheson | single-tier | 2,572 |
| Blandford-Blenheim | lower-tier | 7,565 |
| Blind River | single-tier | 3,422 |
| The Blue Mountains | lower-tier | 9,390 |
| Bluewater | lower-tier | 7,540 |
| Bonfield | single-tier | 2,146 |
| Bonnechere Valley | lower-tier | 3,898 |
| Bracebridge | lower-tier | 17,305 |
| Bradford West Gwillimbury | lower-tier | 42,880 |
| Brampton | lower-tier | 656,480 |
| Brant | single-tier | 39,474 |
| Brantford | single-tier | 104,688 |
| Brethour | single-tier | 105 |
| Brighton | lower-tier | 12,108 |
| Brock | lower-tier | 12,567 |
| Brockton | lower-tier | 9,784 |
| Brockville | single-tier | 22,116 |
| Brooke-Alvinston | lower-tier | 2,359 |
| Bruce Mines | single-tier | 582 |
| Brudenell, Lyndoch and Raglan | lower-tier | 1,552 |
| Burk's Falls | single-tier | 957 |
| Burlington | lower-tier | 186,948 |
| Burpee and Mills | single-tier | 382 |
| Caledon | lower-tier | 76,581 |
| Callander | single-tier | 3,964 |
| Calvin | single-tier | 557 |
| Cambridge | lower-tier | 138,479 |
| Carleton Place | lower-tier | 12,517 |
| Carling | single-tier | 1,491 |
| Carlow/Mayo | lower-tier | 953 |
| Casey | single-tier | 341 |
| Casselman | lower-tier | 3,960 |
| Cavan Monaghan | lower-tier | 10,016 |
| Central Elgin | lower-tier | 13,746 |
| Central Frontenac | lower-tier | 4,892 |
| Central Huron | lower-tier | 7,799 |
| Central Manitoulin | single-tier | 2,235 |
| Centre Hastings | lower-tier | 4,801 |
| Centre Wellington | lower-tier | 31,093 |
| Chamberlain | single-tier | 311 |
| Champlain | lower-tier | 8,665 |
| Chapleau | single-tier | 1,942 |
| Chapple | single-tier | 763 |
| Charlton and Dack | single-tier | 686 |
| Chatham-Kent | single-tier | 103,988 |
| Chatsworth | lower-tier | 7,080 |
| Chisholm | single-tier | 1,312 |
| Clarence-Rockland | lower-tier | 26,505 |
| Clarington | lower-tier | 101,427 |
| Clearview | lower-tier | 14,814 |
| Cobalt | single-tier | 989 |
| Cobourg | lower-tier | 20,519 |
| Cochrane | single-tier | 5,390 |
| Cockburn Island | single-tier | 16 |
| Coleman | single-tier | 517 |
| Collingwood | lower-tier | 24,811 |
| Conmee | single-tier | 798 |
| Cornwall | single-tier | 47,845 |
| Cramahe | lower-tier | 6,509 |
| Dawn-Euphemia | lower-tier | 1,968 |
| Dawson | single-tier | 399 |
| Deep River | lower-tier | 4,175 |
| Deseronto | lower-tier | 1,747 |
| Dorion | single-tier | 375 |
| Douro-Dummer | lower-tier | 7,632 |
| Drummond/North Elmsley | lower-tier | 8,183 |
| Dryden | single-tier | 7,388 |
| Dubreuilville | single-tier | 576 |
| Dutton/Dunwich | lower-tier | 4,152 |
| Dysart, Dudley, Harcourt, Guilford, Harburn, Bruton, Havelock, Eyre and Clyde | lower-tier | 7,182 |
| Ear Falls | single-tier | 924 |
| East Ferris | single-tier | 4,946 |
| East Garafraxa | lower-tier | 2,794 |
| East Gwillimbury | lower-tier | 34,637 |
| East Hawkesbury | lower-tier | 3,418 |
| East Zorra-Tavistock | lower-tier | 7,841 |
| Edwardsburgh/Cardinal | lower-tier | 7,505 |
| Elizabethtown-Kitley | lower-tier | 9,545 |
| Elliot Lake | single-tier | 11,372 |
| Emo | single-tier | 1,204 |
| Englehart | single-tier | 1,442 |
| Enniskillen | lower-tier | 2,825 |
| Erin | lower-tier | 11,981 |
| Espanola | single-tier | 5,185 |
| Essa | lower-tier | 22,970 |
| Essex | lower-tier | 21,216 |
| Evanturel | single-tier | 502 |
| Faraday | lower-tier | 1,612 |
| Fauquier-Strickland | single-tier | 467 |
| Fort Erie | lower-tier | 32,901 |
| Fort Frances | single-tier | 7,466 |
| French River | single-tier | 2,828 |
| Front of Yonge | lower-tier | 2,595 |
| Frontenac Islands | lower-tier | 1,930 |
| Gananoque | single-tier | 5,383 |
| Gauthier | single-tier | 151 |
| Georgian Bay | lower-tier | 3,441 |
| Georgian Bluffs | lower-tier | 11,100 |
| Georgina | lower-tier | 47,642 |
| Gillies | single-tier | 441 |
| Goderich | lower-tier | 7,881 |
| Gordon/Barrie Island | single-tier | 613 |
| Gore Bay | single-tier | 808 |
| Grand Valley | lower-tier | 3,851 |
| Gravenhurst | lower-tier | 13,157 |
| Greater Madawaska | lower-tier | 2,864 |
| Greater Napanee | lower-tier | 16,879 |
| Greater Sudbury | single-tier | 166,004 |
| Greenstone | single-tier | 4,309 |
| Grey Highlands | lower-tier | 10,424 |
| Grimsby | lower-tier | 28,883 |
| Guelph | single-tier | 143,740 |
| Guelph/Eramosa | lower-tier | 13,904 |
| Haldimand | single-tier | 49,216 |
| Halton Hills | lower-tier | 62,951 |
| Hamilton | lower-tier | 11,059 |
| Hamilton | single-tier | 569,353 |
| Hanover | lower-tier | 7,967 |
| Harley | single-tier | 524 |
| Harris | single-tier | 530 |
| Hastings Highlands | lower-tier | 4,385 |
| Havelock-Belmont-Methuen | lower-tier | 5,083 |
| Hawkesbury | lower-tier | 10,194 |
| Head, Clara and Maria | lower-tier | 267 |
| Hearst | single-tier | 4,794 |
| Highlands East | lower-tier | 3,830 |
| Hilliard | single-tier | 215 |
| Hilton | single-tier | 382 |
| Hilton Beach | single-tier | 198 |
| Hornepayne | single-tier | 968 |
| Horton | lower-tier | 3,182 |
| Howick | lower-tier | 4,045 |
| Hudson | single-tier | 530 |
| Huntsville | lower-tier | 21,147 |
| Huron East | lower-tier | 9,512 |
| Huron Shores | single-tier | 1,860 |
| Huron-Kinloss | lower-tier | 7,723 |
| Ignace | single-tier | 1,206 |
| Ingersoll | lower-tier | 13,693 |
| Innisfil | lower-tier | 43,326 |
| Iroquois Falls | single-tier | 4,418 |
| James | single-tier | 348 |
| Jocelyn | single-tier | 314 |
| Johnson | single-tier | 749 |
| Joly | single-tier | 293 |
| Kapuskasing | single-tier | 8,057 |
| Kawartha Lakes | single-tier | 79,247 |
| Kearney | single-tier | 974 |
| Kenora | single-tier | 14,967 |
| Kerns | single-tier | 330 |
| Killaloe, Hagarty and Richards | lower-tier | 2,410 |
| Killarney | single-tier | 397 |
| Kincardine | lower-tier | 12,268 |
| King | lower-tier | 27,333 |
| Kingston | single-tier | 132,485 |
| Kingsville | lower-tier | 22,119 |
| Kirkland Lake | single-tier | 7,750 |
| Kitchener | lower-tier | 256,885 |
| La Vallee | single-tier | 788 |
| Laird | single-tier | 1,121 |
| Lake of Bays | lower-tier | 3,759 |
| Lake of the Woods | single-tier | 308 |
| Lakeshore | lower-tier | 40,410 |
| Lambton Shores | lower-tier | 11,876 |
| Lanark Highlands | lower-tier | 5,737 |
| Larder Lake | single-tier | 745 |
| LaSalle | lower-tier | 32,721 |
| Latchford | single-tier | 355 |
| Laurentian Hills | lower-tier | 2,885 |
| Laurentian Valley | lower-tier | 9,450 |
| Leamington | lower-tier | 29,680 |
| Leeds and the Thousand Islands | lower-tier | 9,804 |
| Limerick | lower-tier | 436 |
| Lincoln | lower-tier | 25,719 |
| London | single-tier | 422,324 |
| Loyalist | lower-tier | 17,943 |
| Lucan Biddulph | lower-tier | 5,680 |
| Macdonald, Meredith and Aberdeen Additional | single-tier | 1,513 |
| Machar | single-tier | 969 |
| Machin | single-tier | 1,012 |
| Madawaska Valley | lower-tier | 3,927 |
| Madoc | lower-tier | 2,233 |
| Magnetawan | single-tier | 1,753 |
| Malahide | lower-tier | 9,308 |
| Manitouwadge | single-tier | 1,974 |
| Mapleton | lower-tier | 10,839 |
| Marathon | single-tier | 3,138 |
| Markham | lower-tier | 338,503 |
| Markstay-Warren | single-tier | 2,708 |
| Marmora and Lake | lower-tier | 4,267 |
| Matachewan | single-tier | 268 |
| Mattawa | single-tier | 1,881 |
| Mattawan | single-tier | 153 |
| Mattice-Val Côté | single-tier | 542 |
| McDougall | single-tier | 2,744 |
| McGarry | single-tier | 579 |
| McKellar | single-tier | 1,419 |
| McMurrich/Monteith | single-tier | 907 |
| McNab/Braeside | lower-tier | 7,591 |
| Meaford | lower-tier | 11,485 |
| Melancthon | lower-tier | 3,132 |
| Merrickville-Wolford | lower-tier | 3,135 |
| Middlesex Centre | lower-tier | 18,928 |
| Midland | lower-tier | 17,817 |
| Milton | lower-tier | 132,979 |
| Minden Hills | lower-tier | 6,971 |
| Minto | lower-tier | 9,094 |
| Mississauga | lower-tier | 717,961 |
| Mississippi Mills | lower-tier | 14,740 |
| Mono | lower-tier | 9,421 |
| Montague | lower-tier | 3,914 |
| Moonbeam | single-tier | 1,157 |
| Moosonee | single-tier | 1,512 |
| Morley | single-tier | 493 |
| Morris-Turnberry | lower-tier | 3,590 |
| Mulmur | lower-tier | 3,571 |
| Muskoka Lakes | lower-tier | 7,652 |
| Nairn and Hyman | single-tier | 373 |
| The Nation | lower-tier | 13,350 |
| Neebing | single-tier | 2,241 |
| New Tecumseth | lower-tier | 43,948 |
| Newbury | lower-tier | 440 |
| Newmarket | lower-tier | 87,942 |
| Niagara Falls | lower-tier | 94,415 |
| Niagara-on-the-Lake | lower-tier | 19,088 |
| Nipigon | single-tier | 1,473 |
| Nipissing | single-tier | 1,769 |
| Norfolk | single-tier | 67,490 |
| North Algona Wilberforce | lower-tier | 3,111 |
| North Bay | single-tier | 52,662 |
| North Dumfries | lower-tier | 10,619 |
| North Dundas | lower-tier | 11,304 |
| North Frontenac | lower-tier | 2,285 |
| North Glengarry | lower-tier | 10,144 |
| North Grenville | lower-tier | 17,964 |
| North Huron | lower-tier | 5,052 |
| North Kawartha | lower-tier | 2,877 |
| North Middlesex | lower-tier | 6,307 |
| North Perth | lower-tier | 15,538 |
| The North Shore | single-tier | 531 |
| North Stormont | lower-tier | 7,400 |
| Northeastern Manitoulin and the Islands | single-tier | 2,641 |
| Northern Bruce Peninsula | lower-tier | 4,404 |
| Norwich | lower-tier | 11,151 |
| Oakville | lower-tier | 213,759 |
| O'Connor | single-tier | 689 |
| Oil Springs | lower-tier | 647 |
| Oliver Paipoonge | single-tier | 6,035 |
| Opasatika | single-tier | 200 |
| Orangeville | lower-tier | 30,167 |
| Orillia | single-tier | 33,411 |
| Oro-Medonte | lower-tier | 23,017 |
| Oshawa | lower-tier | 175,383 |
| Otonabee-South Monaghan | lower-tier | 7,087 |
| Ottawa | single-tier | 1,017,449 |
| Owen Sound | lower-tier | 21,612 |
| Papineau-Cameron | single-tier | 982 |
| Parry Sound | single-tier | 6,879 |
| Pelee | single-tier | 230 |
| Pelham | lower-tier | 18,192 |
| Pembroke | single-tier | 14,364 |
| Penetanguishene | lower-tier | 10,077 |
| Perry | single-tier | 2,650 |
| Perth | lower-tier | 6,469 |
| Perth East | lower-tier | 12,595 |
| Perth South | lower-tier | 3,776 |
| Petawawa | lower-tier | 18,160 |
| Peterborough | single-tier | 83,651 |
| Petrolia | lower-tier | 6,013 |
| Pickering | lower-tier | 99,186 |
| Pickle Lake | single-tier | 398 |
| Plummer Additional | single-tier | 757 |
| Plympton-Wyoming | lower-tier | 8,308 |
| Point Edward | lower-tier | 1,930 |
| Port Colborne | lower-tier | 20,033 |
| Port Hope | lower-tier | 17,294 |
| Powassan | single-tier | 3,346 |
| Prescott | single-tier | 4,078 |
| Prince | single-tier | 975 |
| Prince Edward | single-tier | 25,704 |
| Puslinch | lower-tier | 7,944 |
| Quinte West | single-tier | 46,560 |
| Rainy River | single-tier | 752 |
| Ramara | lower-tier | 10,377 |
| Red Lake | single-tier | 4,094 |
| Red Rock | single-tier | 895 |
| Renfrew | lower-tier | 8,190 |
| Richmond Hill | lower-tier | 202,022 |
| Rideau Lakes | lower-tier | 10,883 |
| Russell | lower-tier | 19,598 |
| Ryerson | single-tier | 745 |
| Sables-Spanish Rivers | single-tier | 3,237 |
| Sarnia | lower-tier | 72,047 |
| Saugeen Shores | lower-tier | 15,908 |
| Sault Ste. Marie | single-tier | 72,051 |
| Schreiber | single-tier | 1,039 |
| Scugog | lower-tier | 21,581 |
| Seguin | single-tier | 5,280 |
| Selwyn | lower-tier | 18,653 |
| Severn | lower-tier | 14,576 |
| Shelburne | lower-tier | 8,994 |
| Shuniah | single-tier | 3,247 |
| Sioux Lookout | single-tier | 5,839 |
| Sioux Narrows-Nestor Falls | single-tier | 727 |
| Smiths Falls | single-tier | 9,254 |
| Smooth Rock Falls | single-tier | 1,200 |
| South Algonquin | single-tier | 1,055 |
| South Bruce | lower-tier | 5,880 |
| South Bruce Peninsula | lower-tier | 9,137 |
| South Dundas | lower-tier | 11,044 |
| South Frontenac | lower-tier | 20,188 |
| South Glengarry | lower-tier | 13,330 |
| South Huron | lower-tier | 10,063 |
| South River | single-tier | 1,101 |
| South Stormont | lower-tier | 13,570 |
| Southgate | lower-tier | 8,716 |
| Southwest Middlesex | lower-tier | 5,893 |
| South-West Oxford | lower-tier | 7,583 |
| Southwold | lower-tier | 4,851 |
| Spanish | single-tier | 670 |
| Springwater | lower-tier | 21,701 |
| St. Catharines | lower-tier | 136,803 |
| St. Clair | lower-tier | 14,659 |
| St. Joseph | single-tier | 1,426 |
| St. Marys | single-tier | 7,386 |
| St. Thomas | single-tier | 42,840 |
| St.-Charles | single-tier | 1,357 |
| Stirling-Rawdon | lower-tier | 5,015 |
| Stone Mills | lower-tier | 7,826 |
| Stratford | single-tier | 33,232 |
| Strathroy-Caradoc | lower-tier | 23,871 |
| Strong | single-tier | 1,566 |
| Sundridge | single-tier | 938 |
| Tarbutt | single-tier | 573 |
| Tay | lower-tier | 11,091 |
| Tay Valley | lower-tier | 5,925 |
| Tecumseh | lower-tier | 23,300 |
| Tehkummah | single-tier | 450 |
| Temagami | single-tier | 862 |
| Temiskaming Shores | single-tier | 9,634 |
| Terrace Bay | single-tier | 1,528 |
| Thames Centre | lower-tier | 13,980 |
| Thessalon | single-tier | 1,260 |
| Thornloe | single-tier | 92 |
| Thorold | lower-tier | 23,816 |
| Thunder Bay | single-tier | 108,843 |
| Tillsonburg | lower-tier | 18,615 |
| Timmins | single-tier | 41,145 |
| Tiny | lower-tier | 12,966 |
| Toronto | single-tier | 2,794,356 |
| Trent Hills | lower-tier | 13,861 |
| Trent Lakes | lower-tier | 6,439 |
| Tudor and Cashel | lower-tier | 740 |
| Tweed | lower-tier | 6,067 |
| Tyendinaga | lower-tier | 4,538 |
| Uxbridge | lower-tier | 21,556 |
| Val Rita-Harty | single-tier | 757 |
| Vaughan | lower-tier | 323,103 |
| Wainfleet | lower-tier | 6,887 |
| Warwick | lower-tier | 3,641 |
| Wasaga Beach | lower-tier | 24,862 |
| Waterloo | lower-tier | 121,436 |
| Wawa | single-tier | 2,705 |
| Welland | lower-tier | 55,750 |
| Wellesley | lower-tier | 11,318 |
| Wellington North | lower-tier | 12,431 |
| West Elgin | lower-tier | 5,060 |
| West Grey | lower-tier | 13,131 |
| West Lincoln | lower-tier | 15,454 |
| West Nipissing | single-tier | 14,583 |
| West Perth | lower-tier | 9,038 |
| Westport | lower-tier | 634 |
| Whitby | lower-tier | 138,501 |
| Whitchurch-Stouffville | lower-tier | 49,864 |
| White River | single-tier | 557 |
| Whitestone | single-tier | 1,075 |
| Whitewater | lower-tier | 7,225 |
| Wilmot | lower-tier | 21,429 |
| Windsor | single-tier | 229,660 |
| Wollaston | lower-tier | 721 |
| Woodstock | lower-tier | 46,705 |
| Woolwich | lower-tier | 26,999 |
| Zorra | lower-tier | 8,628 |

A column of dates (here, made from the dataset's text) is filtered by a date range, from one date to another.

``` python
import pandas as pd
from great_tables.data import sp500

sp500_2015 = sp500[sp500["date"] >= "2015-01-01"].assign(
    date=lambda df: pd.to_datetime(df["date"])
)

(
    GTI(sp500_2015[["date", "open", "close"]])
    .fmt_date(columns="date", date_style="month_day_year")
    .fmt_currency(columns=["open", "close"])
    .i_cols_filter(columns="date")
)
```

| date               | open       | close      |
|--------------------|------------|------------|
| December 31, 2015  | \$2,060.59 | \$2,043.94 |
| December 30, 2015  | \$2,077.34 | \$2,063.36 |
| December 29, 2015  | \$2,060.54 | \$2,078.36 |
| December 28, 2015  | \$2,057.77 | \$2,056.50 |
| December 24, 2015  | \$2,063.52 | \$2,060.99 |
| December 23, 2015  | \$2,042.20 | \$2,064.29 |
| December 22, 2015  | \$2,023.15 | \$2,038.97 |
| December 21, 2015  | \$2,010.27 | \$2,021.15 |
| December 18, 2015  | \$2,040.81 | \$2,005.55 |
| December 17, 2015  | \$2,073.76 | \$2,041.89 |
| December 16, 2015  | \$2,046.50 | \$2,073.07 |
| December 15, 2015  | \$2,025.55 | \$2,043.41 |
| December 14, 2015  | \$2,013.37 | \$2,021.94 |
| December 11, 2015  | \$2,047.27 | \$2,012.37 |
| December 10, 2015  | \$2,047.93 | \$2,052.23 |
| December 9, 2015   | \$2,061.17 | \$2,047.62 |
| December 8, 2015   | \$2,073.39 | \$2,063.59 |
| December 7, 2015   | \$2,090.42 | \$2,077.07 |
| December 4, 2015   | \$2,051.24 | \$2,091.69 |
| December 3, 2015   | \$2,080.71 | \$2,049.62 |
| December 2, 2015   | \$2,101.71 | \$2,079.51 |
| December 1, 2015   | \$2,082.93 | \$2,102.63 |
| November 30, 2015  | \$2,090.95 | \$2,080.41 |
| November 27, 2015  | \$2,088.82 | \$2,090.11 |
| November 25, 2015  | \$2,089.30 | \$2,088.87 |
| November 24, 2015  | \$2,084.42 | \$2,089.14 |
| November 23, 2015  | \$2,089.41 | \$2,086.59 |
| November 20, 2015  | \$2,082.82 | \$2,089.17 |
| November 19, 2015  | \$2,083.70 | \$2,081.24 |
| November 18, 2015  | \$2,051.99 | \$2,083.58 |
| November 17, 2015  | \$2,053.67 | \$2,050.44 |
| November 16, 2015  | \$2,022.08 | \$2,053.19 |
| November 13, 2015  | \$2,044.64 | \$2,023.04 |
| November 12, 2015  | \$2,072.29 | \$2,045.97 |
| November 11, 2015  | \$2,083.41 | \$2,075.00 |
| November 10, 2015  | \$2,077.19 | \$2,081.72 |
| November 9, 2015   | \$2,096.56 | \$2,078.58 |
| November 6, 2015   | \$2,098.60 | \$2,099.20 |
| November 5, 2015   | \$2,101.68 | \$2,099.93 |
| November 4, 2015   | \$2,110.60 | \$2,102.31 |
| November 3, 2015   | \$2,102.63 | \$2,109.79 |
| November 2, 2015   | \$2,080.76 | \$2,104.05 |
| October 30, 2015   | \$2,090.00 | \$2,079.36 |
| October 29, 2015   | \$2,088.35 | \$2,089.41 |
| October 28, 2015   | \$2,066.48 | \$2,090.35 |
| October 27, 2015   | \$2,068.75 | \$2,065.89 |
| October 26, 2015   | \$2,075.08 | \$2,071.18 |
| October 23, 2015   | \$2,058.19 | \$2,075.15 |
| October 22, 2015   | \$2,021.88 | \$2,052.51 |
| October 21, 2015   | \$2,033.47 | \$2,018.94 |
| October 20, 2015   | \$2,033.13 | \$2,030.77 |
| October 19, 2015   | \$2,031.73 | \$2,033.66 |
| October 16, 2015   | \$2,024.37 | \$2,033.11 |
| October 15, 2015   | \$1,996.47 | \$2,023.86 |
| October 14, 2015   | \$2,003.66 | \$1,994.24 |
| October 13, 2015   | \$2,015.00 | \$2,003.69 |
| October 12, 2015   | \$2,015.65 | \$2,017.46 |
| October 9, 2015    | \$2,013.73 | \$2,014.89 |
| October 8, 2015    | \$1,994.01 | \$2,013.43 |
| October 7, 2015    | \$1,982.34 | \$1,995.83 |
| October 6, 2015    | \$1,986.63 | \$1,979.92 |
| October 5, 2015    | \$1,954.33 | \$1,987.05 |
| October 2, 2015    | \$1,921.77 | \$1,951.36 |
| October 1, 2015    | \$1,919.65 | \$1,923.82 |
| September 30, 2015 | \$1,887.14 | \$1,920.03 |
| September 29, 2015 | \$1,881.90 | \$1,884.09 |
| September 28, 2015 | \$1,929.18 | \$1,881.77 |
| September 25, 2015 | \$1,935.93 | \$1,931.34 |
| September 24, 2015 | \$1,934.81 | \$1,932.24 |
| September 23, 2015 | \$1,943.24 | \$1,938.76 |
| September 22, 2015 | \$1,961.39 | \$1,942.74 |
| September 21, 2015 | \$1,960.84 | \$1,966.97 |
| September 18, 2015 | \$1,989.66 | \$1,958.03 |
| September 17, 2015 | \$1,995.33 | \$1,990.20 |
| September 16, 2015 | \$1,978.02 | \$1,995.31 |
| September 15, 2015 | \$1,955.10 | \$1,978.09 |
| September 14, 2015 | \$1,963.06 | \$1,953.03 |
| September 11, 2015 | \$1,951.45 | \$1,961.05 |
| September 10, 2015 | \$1,941.59 | \$1,952.29 |
| September 9, 2015  | \$1,971.45 | \$1,942.04 |
| September 8, 2015  | \$1,927.30 | \$1,969.41 |
| September 4, 2015  | \$1,947.76 | \$1,921.22 |
| September 3, 2015  | \$1,950.79 | \$1,951.13 |
| September 2, 2015  | \$1,916.52 | \$1,948.86 |
| September 1, 2015  | \$1,970.09 | \$1,913.85 |
| August 31, 2015    | \$1,986.73 | \$1,972.18 |
| August 28, 2015    | \$1,986.06 | \$1,988.87 |
| August 27, 2015    | \$1,942.77 | \$1,987.66 |
| August 26, 2015    | \$1,872.75 | \$1,940.51 |
| August 25, 2015    | \$1,898.08 | \$1,867.61 |
| August 24, 2015    | \$1,965.15 | \$1,893.21 |
| August 21, 2015    | \$2,034.08 | \$1,970.89 |
| August 20, 2015    | \$2,076.61 | \$2,035.73 |
| August 19, 2015    | \$2,095.69 | \$2,079.61 |
| August 18, 2015    | \$2,101.99 | \$2,096.92 |
| August 17, 2015    | \$2,089.70 | \$2,102.44 |
| August 14, 2015    | \$2,083.15 | \$2,091.54 |
| August 13, 2015    | \$2,086.19 | \$2,083.39 |
| August 12, 2015    | \$2,081.10 | \$2,086.05 |
| August 11, 2015    | \$2,102.66 | \$2,084.07 |
| August 10, 2015    | \$2,080.98 | \$2,104.18 |
| August 7, 2015     | \$2,082.61 | \$2,077.57 |
| August 6, 2015     | \$2,100.75 | \$2,083.56 |
| August 5, 2015     | \$2,095.27 | \$2,099.84 |
| August 4, 2015     | \$2,097.68 | \$2,093.32 |
| August 3, 2015     | \$2,104.49 | \$2,098.04 |
| July 31, 2015      | \$2,111.60 | \$2,103.84 |
| July 30, 2015      | \$2,106.78 | \$2,108.63 |
| July 29, 2015      | \$2,094.70 | \$2,108.57 |
| July 28, 2015      | \$2,070.75 | \$2,093.25 |
| July 27, 2015      | \$2,078.19 | \$2,067.64 |
| July 24, 2015      | \$2,102.24 | \$2,079.65 |
| July 23, 2015      | \$2,114.16 | \$2,102.15 |
| July 22, 2015      | \$2,118.21 | \$2,114.15 |
| July 21, 2015      | \$2,127.55 | \$2,119.21 |
| July 20, 2015      | \$2,126.85 | \$2,128.28 |
| July 17, 2015      | \$2,126.80 | \$2,126.64 |
| July 16, 2015      | \$2,110.55 | \$2,124.29 |
| July 15, 2015      | \$2,109.01 | \$2,107.40 |
| July 14, 2015      | \$2,099.72 | \$2,108.95 |
| July 13, 2015      | \$2,080.03 | \$2,099.60 |
| July 10, 2015      | \$2,052.74 | \$2,076.62 |
| July 9, 2015       | \$2,049.73 | \$2,051.31 |
| July 8, 2015       | \$2,077.66 | \$2,046.68 |
| July 7, 2015       | \$2,069.52 | \$2,081.34 |
| July 6, 2015       | \$2,073.95 | \$2,068.76 |
| July 2, 2015       | \$2,078.03 | \$2,076.78 |
| July 1, 2015       | \$2,067.00 | \$2,077.42 |
| June 30, 2015      | \$2,061.19 | \$2,063.11 |
| June 29, 2015      | \$2,098.63 | \$2,057.64 |
| June 26, 2015      | \$2,102.62 | \$2,101.49 |
| June 25, 2015      | \$2,109.96 | \$2,102.31 |
| June 24, 2015      | \$2,123.65 | \$2,108.58 |
| June 23, 2015      | \$2,123.16 | \$2,124.20 |
| June 22, 2015      | \$2,112.50 | \$2,122.85 |
| June 19, 2015      | \$2,121.06 | \$2,109.99 |
| June 18, 2015      | \$2,101.58 | \$2,121.24 |
| June 17, 2015      | \$2,097.40 | \$2,100.44 |
| June 16, 2015      | \$2,084.26 | \$2,096.29 |
| June 15, 2015      | \$2,091.34 | \$2,084.43 |
| June 12, 2015      | \$2,107.43 | \$2,094.11 |
| June 11, 2015      | \$2,106.24 | \$2,108.86 |
| June 10, 2015      | \$2,081.12 | \$2,105.20 |
| June 9, 2015       | \$2,079.07 | \$2,080.15 |
| June 8, 2015       | \$2,092.34 | \$2,079.28 |
| June 5, 2015       | \$2,095.09 | \$2,092.83 |
| June 4, 2015       | \$2,112.35 | \$2,095.84 |
| June 3, 2015       | \$2,110.64 | \$2,114.07 |
| June 2, 2015       | \$2,110.41 | \$2,109.60 |
| June 1, 2015       | \$2,108.64 | \$2,111.73 |
| May 29, 2015       | \$2,120.66 | \$2,107.39 |
| May 28, 2015       | \$2,122.27 | \$2,120.79 |
| May 27, 2015       | \$2,105.13 | \$2,123.48 |
| May 26, 2015       | \$2,125.34 | \$2,104.20 |
| May 22, 2015       | \$2,130.36 | \$2,126.06 |
| May 21, 2015       | \$2,125.55 | \$2,130.82 |
| May 20, 2015       | \$2,127.79 | \$2,125.85 |
| May 19, 2015       | \$2,129.45 | \$2,127.83 |
| May 18, 2015       | \$2,121.30 | \$2,129.20 |
| May 15, 2015       | \$2,122.07 | \$2,122.73 |
| May 14, 2015       | \$2,100.43 | \$2,121.10 |
| May 13, 2015       | \$2,099.62 | \$2,098.48 |
| May 12, 2015       | \$2,102.87 | \$2,099.12 |
| May 11, 2015       | \$2,115.56 | \$2,105.33 |
| May 8, 2015        | \$2,092.13 | \$2,116.10 |
| May 7, 2015        | \$2,079.96 | \$2,088.00 |
| May 6, 2015        | \$2,091.26 | \$2,080.15 |
| May 5, 2015        | \$2,112.63 | \$2,089.46 |
| May 4, 2015        | \$2,110.23 | \$2,114.49 |
| May 1, 2015        | \$2,087.38 | \$2,108.29 |
| April 30, 2015     | \$2,105.52 | \$2,085.51 |
| April 29, 2015     | \$2,112.49 | \$2,106.85 |
| April 28, 2015     | \$2,108.35 | \$2,114.76 |
| April 27, 2015     | \$2,119.29 | \$2,108.92 |
| April 24, 2015     | \$2,112.80 | \$2,117.69 |
| April 23, 2015     | \$2,107.21 | \$2,112.93 |
| April 22, 2015     | \$2,098.27 | \$2,107.96 |
| April 21, 2015     | \$2,102.82 | \$2,097.29 |
| April 20, 2015     | \$2,084.11 | \$2,100.40 |
| April 17, 2015     | \$2,102.58 | \$2,081.18 |
| April 16, 2015     | \$2,105.96 | \$2,104.99 |
| April 15, 2015     | \$2,097.82 | \$2,106.63 |
| April 14, 2015     | \$2,092.28 | \$2,095.84 |
| April 13, 2015     | \$2,102.03 | \$2,092.43 |
| April 10, 2015     | \$2,091.51 | \$2,102.06 |
| April 9, 2015      | \$2,081.29 | \$2,091.18 |
| April 8, 2015      | \$2,076.94 | \$2,081.90 |
| April 7, 2015      | \$2,080.79 | \$2,076.33 |
| April 6, 2015      | \$2,064.87 | \$2,080.62 |
| April 2, 2015      | \$2,060.03 | \$2,066.96 |
| April 1, 2015      | \$2,067.63 | \$2,059.69 |
| March 31, 2015     | \$2,084.05 | \$2,067.89 |
| March 30, 2015     | \$2,064.11 | \$2,086.24 |
| March 27, 2015     | \$2,055.78 | \$2,061.02 |
| March 26, 2015     | \$2,059.94 | \$2,056.15 |
| March 25, 2015     | \$2,093.10 | \$2,061.05 |
| March 24, 2015     | \$2,103.94 | \$2,091.50 |
| March 23, 2015     | \$2,107.99 | \$2,104.42 |
| March 20, 2015     | \$2,090.32 | \$2,108.10 |
| March 19, 2015     | \$2,098.69 | \$2,089.27 |
| March 18, 2015     | \$2,072.84 | \$2,099.50 |
| March 17, 2015     | \$2,080.59 | \$2,074.28 |
| March 16, 2015     | \$2,055.35 | \$2,081.19 |
| March 13, 2015     | \$2,064.56 | \$2,053.40 |
| March 12, 2015     | \$2,041.10 | \$2,065.95 |
| March 11, 2015     | \$2,044.69 | \$2,040.24 |
| March 10, 2015     | \$2,076.14 | \$2,044.16 |
| March 9, 2015      | \$2,072.25 | \$2,079.43 |
| March 6, 2015      | \$2,100.91 | \$2,071.26 |
| March 5, 2015      | \$2,098.54 | \$2,101.04 |
| March 4, 2015      | \$2,107.72 | \$2,098.53 |
| March 3, 2015      | \$2,115.76 | \$2,107.78 |
| March 2, 2015      | \$2,105.23 | \$2,117.39 |
| February 27, 2015  | \$2,110.88 | \$2,104.50 |
| February 26, 2015  | \$2,113.91 | \$2,110.74 |
| February 25, 2015  | \$2,115.30 | \$2,113.86 |
| February 24, 2015  | \$2,109.10 | \$2,115.48 |
| February 23, 2015  | \$2,109.83 | \$2,109.66 |
| February 20, 2015  | \$2,097.65 | \$2,110.30 |
| February 19, 2015  | \$2,099.25 | \$2,097.45 |
| February 18, 2015  | \$2,099.16 | \$2,099.68 |
| February 17, 2015  | \$2,096.47 | \$2,100.34 |
| February 13, 2015  | \$2,088.78 | \$2,096.99 |
| February 12, 2015  | \$2,069.98 | \$2,088.48 |
| February 11, 2015  | \$2,068.55 | \$2,068.53 |
| February 10, 2015  | \$2,049.38 | \$2,068.59 |
| February 9, 2015   | \$2,053.47 | \$2,046.74 |
| February 6, 2015   | \$2,062.28 | \$2,055.47 |
| February 5, 2015   | \$2,043.45 | \$2,062.52 |
| February 4, 2015   | \$2,048.86 | \$2,041.51 |
| February 3, 2015   | \$2,022.71 | \$2,050.03 |
| February 2, 2015   | \$1,996.67 | \$2,020.85 |
| January 30, 2015   | \$2,019.35 | \$1,994.99 |
| January 29, 2015   | \$2,002.45 | \$2,021.25 |
| January 28, 2015   | \$2,032.34 | \$2,002.16 |
| January 27, 2015   | \$2,047.86 | \$2,029.55 |
| January 26, 2015   | \$2,050.42 | \$2,057.09 |
| January 23, 2015   | \$2,062.98 | \$2,051.82 |
| January 22, 2015   | \$2,034.30 | \$2,063.15 |
| January 21, 2015   | \$2,020.19 | \$2,032.12 |
| January 20, 2015   | \$2,020.76 | \$2,022.55 |
| January 16, 2015   | \$1,992.25 | \$2,019.42 |
| January 15, 2015   | \$2,013.75 | \$1,992.67 |
| January 14, 2015   | \$2,018.40 | \$2,011.27 |
| January 13, 2015   | \$2,031.58 | \$2,023.03 |
| January 12, 2015   | \$2,046.13 | \$2,028.26 |
| January 9, 2015    | \$2,063.45 | \$2,044.81 |
| January 8, 2015    | \$2,030.61 | \$2,062.14 |
| January 7, 2015    | \$2,005.55 | \$2,025.90 |
| January 6, 2015    | \$2,022.15 | \$2,002.61 |
| January 5, 2015    | \$2,054.44 | \$2,020.58 |
| January 2, 2015    | \$2,058.90 | \$2,058.20 |

A column of booleans (here, whether a nuclide is stable) is filtered by one of its values, shown as the table shows them.

``` python
from great_tables.data import nuclides

nuclides_mini = nuclides[["nuclide", "z", "n", "is_stable"]].head(20).assign(
    is_stable=lambda df: df["is_stable"] == "TRUE"
)

(
    GTI(nuclides_mini)
    .fmt_tf(columns="is_stable", tf_style="yes-no")
    .i_cols_filter(columns="is_stable")
)
```

| nuclide       | z   | n   | is_stable |
|---------------|-----|-----|-----------|
| ^{1}\_{1}H0   | 1   | 0   | yes       |
| ^{2}\_{1}H1   | 1   | 1   | yes       |
| ^{3}\_{1}H2   | 1   | 2   | no        |
| ^{4}\_{1}H3   | 1   | 3   | no        |
| ^{5}\_{1}H4   | 1   | 4   | no        |
| ^{6}\_{1}H5   | 1   | 5   | no        |
| ^{7}\_{1}H6   | 1   | 6   | no        |
| ^{3}\_{2}He1  | 2   | 1   | yes       |
| ^{4}\_{2}He2  | 2   | 2   | yes       |
| ^{5}\_{2}He3  | 2   | 3   | no        |
| ^{6}\_{2}He4  | 2   | 4   | no        |
| ^{7}\_{2}He5  | 2   | 5   | no        |
| ^{8}\_{2}He6  | 2   | 6   | no        |
| ^{9}\_{2}He7  | 2   | 7   | no        |
| ^{10}\_{2}He8 | 2   | 8   | no        |
| ^{4}\_{3}Li1  | 3   | 1   | no        |
| ^{5}\_{3}Li2  | 3   | 2   | no        |
| ^{6}\_{3}Li3  | 3   | 3   | yes       |
| ^{7}\_{3}Li4  | 3   | 4   | yes       |
| ^{8}\_{3}Li5  | 3   | 5   | no        |
