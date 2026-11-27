# GTI.i_responsive()

Set how the table fits a narrow container.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L601-L686)

``` python
GTI.i_responsive(
    mode="auto",
    *,
    stack_below=420,
)
```

A table wider than its container can scroll sideways, with its stub (and any pinned columns) staying in view (`"scroll"`). Or, in a container narrower than `stack_below` pixels (on a phone, say), it can be stacked (`"stack"`): each row becomes a card, titled by its stub, with each column's label next to its value (labels under a spanner are prefixed with it). Row groups become headings between the cards, and summary rows become cards of their own. The table is stacked by its CSS alone, so it's stacked before its script runs (or without it); once it runs, the column labels are shown above the cards as chips, which readers can sort and filter by as with the labels themselves.

Or it can drop columns until it fits (`"collapse"`): those without a priority first (from the last), then those with the highest numbers, as [`i_cols_priority()`](../reference/GTI.i_cols_priority.md#great_tables.GTI.i_cols_priority) set them. Each row then has a button by its first cell that shows the columns dropped from it, under it, as labels and values. Columns come back as the container widens. A column is never dropped if it has priority 1, nor the stub (or the row group column); with only those left, the table scrolls. Dropped columns are still searched, filtered and exported, and they're dropped by the table's script, so without it the table scrolls.

With `"auto"` (the default), the table drops columns if any have a priority; otherwise it's stacked if it shows no more than six columns (not counting the stub), and scrolls if it shows more. With `"stack"` or `"auto"`, a table in a container as wide as `stack_below` or wider is as with `"scroll"`. So is one in a container that's only as wide as what's in it (a table's cell, or an inline block), once its script runs: before that, such a table has no width.

Whatever the mode, in a container narrower than 30em (480 pixels, at 16px text), the control bar folds its search, its filters as text and its "Columns" button into one "Filter & sort" button, which opens a sheet from the foot of the window with all of them, and the table's sort and filters; on a touch screen, so does a bar that's 30em wide or less. A search stays in the sheet (the button is then in the accent color), and the keyboard shortcuts and the naming of the table's parts are left out. There, a long press on a column's label opens a sheet for that column (to sort it, filter it, or hide it), while a tap still sorts by it.

## Parameters

`mode: ResponsiveMode = "auto"`  
How the table fits a narrow container: `"scroll"`, `"stack"`, `"collapse"`, or `"auto"`.

`stack_below: float = 420`  
The container width (in pixels) below which the table is stacked, with `"stack"` or `"auto"`.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table that's stacked in a container narrower than 420 pixels (narrow the window to see its cards).

``` python
from great_tables import GTI
from great_tables.data import towny

towny_mini = towny[["name", "status", "population_2021", "density_2021"]]

GTI(towny_mini, rowname_col="name").i_responsive("stack")
```

|  | status | population_2021 | density_2021 |
|----|----|----|----|
| Addington Highlands | lower-tier | 2534 | 1.96 |
| Adelaide Metcalfe | lower-tier | 3011 | 9.09 |
| Adjala-Tosorontio | lower-tier | 10989 | 29.58 |
| Admaston/Bromley | lower-tier | 2995 | 5.76 |
| Ajax | lower-tier | 126666 | 1900.75 |
| Alberton | single-tier | 954 | 8.18 |
| Alfred and Plantagenet | lower-tier | 9949 | 25.39 |
| Algonquin Highlands | lower-tier | 2588 | 2.59 |
| Alnwick/Haldimand | lower-tier | 7473 | 18.76 |
| Amaranth | lower-tier | 4327 | 16.33 |
| Amherstburg | lower-tier | 23524 | 128.01 |
| The Archipelago | single-tier | 979 | 1.65 |
| Armour | single-tier | 1459 | 8.92 |
| Armstrong | single-tier | 1199 | 13.3 |
| Arnprior | lower-tier | 9629 | 738.42 |
| Arran-Elderslie | lower-tier | 6913 | 15.07 |
| Ashfield-Colborne-Wawanosh | lower-tier | 5884 | 10.03 |
| Asphodel-Norwood | lower-tier | 4658 | 28.82 |
| Assiginack | single-tier | 1008 | 4.48 |
| Athens | lower-tier | 3042 | 23.48 |
| Atikokan | single-tier | 2642 | 8.42 |
| Augusta | lower-tier | 7386 | 23.54 |
| Aurora | lower-tier | 62057 | 1241.14 |
| Aylmer | lower-tier | 7699 | 1208.63 |
| Baldwin | single-tier | 579 | 7.02 |
| Bancroft | lower-tier | 4065 | 17.86 |
| Barrie | single-tier | 147829 | 1493.07 |
| Bayham | lower-tier | 7096 | 29.01 |
| Beckwith | lower-tier | 9021 | 37.7 |
| Belleville | single-tier | 55071 | 222.82 |
| Billings | single-tier | 753 | 3.61 |
| Black River-Matheson | single-tier | 2572 | 2.21 |
| Blandford-Blenheim | lower-tier | 7565 | 19.8 |
| Blind River | single-tier | 3422 | 6.66 |
| The Blue Mountains | lower-tier | 9390 | 32.99 |
| Bluewater | lower-tier | 7540 | 18.09 |
| Bonfield | single-tier | 2146 | 10.41 |
| Bonnechere Valley | lower-tier | 3898 | 6.63 |
| Bracebridge | lower-tier | 17305 | 28.13 |
| Bradford West Gwillimbury | lower-tier | 42880 | 213.67 |
| Brampton | lower-tier | 656480 | 2468.99 |
| Brant | single-tier | 39474 | 48.28 |
| Brantford | single-tier | 104688 | 1061.21 |
| Brethour | single-tier | 105 | 1.28 |
| Brighton | lower-tier | 12108 | 54.24 |
| Brock | lower-tier | 12567 | 29.73 |
| Brockton | lower-tier | 9784 | 17.33 |
| Brockville | single-tier | 22116 | 1057.68 |
| Brooke-Alvinston | lower-tier | 2359 | 7.58 |
| Bruce Mines | single-tier | 582 | 95.57 |
| Brudenell, Lyndoch and Raglan | lower-tier | 1552 | 2.21 |
| Burk's Falls | single-tier | 957 | 309.71 |
| Burlington | lower-tier | 186948 | 1004.45 |
| Burpee and Mills | single-tier | 382 | 1.76 |
| Caledon | lower-tier | 76581 | 111.18 |
| Callander | single-tier | 3964 | 38.49 |
| Calvin | single-tier | 557 | 3.97 |
| Cambridge | lower-tier | 138479 | 1225.59 |
| Carleton Place | lower-tier | 12517 | 1259.26 |
| Carling | single-tier | 1491 | 6.1 |
| Carlow/Mayo | lower-tier | 953 | 2.47 |
| Casey | single-tier | 341 | 4.22 |
| Casselman | lower-tier | 3960 | 771.93 |
| Cavan Monaghan | lower-tier | 10016 | 32.69 |
| Central Elgin | lower-tier | 13746 | 49.12 |
| Central Frontenac | lower-tier | 4892 | 4.93 |
| Central Huron | lower-tier | 7799 | 17.35 |
| Central Manitoulin | single-tier | 2235 | 5.23 |
| Centre Hastings | lower-tier | 4801 | 21.55 |
| Centre Wellington | lower-tier | 31093 | 75.95 |
| Chamberlain | single-tier | 311 | 2.81 |
| Champlain | lower-tier | 8665 | 41.86 |
| Chapleau | single-tier | 1942 | 147.12 |
| Chapple | single-tier | 763 | 1.37 |
| Charlton and Dack | single-tier | 686 | 7.4 |
| Chatham-Kent | single-tier | 103988 | 42.41 |
| Chatsworth | lower-tier | 7080 | 11.91 |
| Chisholm | single-tier | 1312 | 6.38 |
| Clarence-Rockland | lower-tier | 26505 | 89.1 |
| Clarington | lower-tier | 101427 | 166.05 |
| Clearview | lower-tier | 14814 | 26.63 |
| Cobalt | single-tier | 989 | 477.78 |
| Cobourg | lower-tier | 20519 | 915.62 |
| Cochrane | single-tier | 5390 | 10.02 |
| Cockburn Island | single-tier | 16 | 0.09 |
| Coleman | single-tier | 517 | 2.91 |
| Collingwood | lower-tier | 24811 | 748.45 |
| Conmee | single-tier | 798 | 4.76 |
| Cornwall | single-tier | 47845 | 777.97 |
| Cramahe | lower-tier | 6509 | 32.19 |
| Dawn-Euphemia | lower-tier | 1968 | 4.42 |
| Dawson | single-tier | 399 | 1.16 |
| Deep River | lower-tier | 4175 | 83.05 |
| Deseronto | lower-tier | 1747 | 693.25 |
| Dorion | single-tier | 375 | 1.78 |
| Douro-Dummer | lower-tier | 7632 | 16.61 |
| Drummond/North Elmsley | lower-tier | 8183 | 22.38 |
| Dryden | single-tier | 7388 | 112.66 |
| Dubreuilville | single-tier | 576 | 6.58 |
| Dutton/Dunwich | lower-tier | 4152 | 14.1 |
| Dysart, Dudley, Harcourt, Guilford, Harburn, Bruton, Havelock, Eyre and Clyde | lower-tier | 7182 | 4.87 |
| Ear Falls | single-tier | 924 | 2.74 |
| East Ferris | single-tier | 4946 | 32.55 |
| East Garafraxa | lower-tier | 2794 | 16.78 |
| East Gwillimbury | lower-tier | 34637 | 141.43 |
| East Hawkesbury | lower-tier | 3418 | 14.54 |
| East Zorra-Tavistock | lower-tier | 7841 | 32.41 |
| Edwardsburgh/Cardinal | lower-tier | 7505 | 24.22 |
| Elizabethtown-Kitley | lower-tier | 9545 | 17.17 |
| Elliot Lake | single-tier | 11372 | 16.34 |
| Emo | single-tier | 1204 | 5.95 |
| Englehart | single-tier | 1442 | 493.84 |
| Enniskillen | lower-tier | 2825 | 8.36 |
| Erin | lower-tier | 11981 | 40.1 |
| Espanola | single-tier | 5185 | 64.01 |
| Essa | lower-tier | 22970 | 82.06 |
| Essex | lower-tier | 21216 | 76.45 |
| Evanturel | single-tier | 502 | 5.63 |
| Faraday | lower-tier | 1612 | 7.41 |
| Fauquier-Strickland | single-tier | 467 | 0.46 |
| Fort Erie | lower-tier | 32901 | 197.91 |
| Fort Frances | single-tier | 7466 | 292.21 |
| French River | single-tier | 2828 | 3.94 |
| Front of Yonge | lower-tier | 2595 | 20.72 |
| Frontenac Islands | lower-tier | 1930 | 10.92 |
| Gananoque | single-tier | 5383 | 767.9 |
| Gauthier | single-tier | 151 | 1.72 |
| Georgian Bay | lower-tier | 3441 | 6.55 |
| Georgian Bluffs | lower-tier | 11100 | 18.5 |
| Georgina | lower-tier | 47642 | 165.6 |
| Gillies | single-tier | 441 | 4.76 |
| Goderich | lower-tier | 7881 | 922.83 |
| Gordon/Barrie Island | single-tier | 613 | 2.33 |
| Gore Bay | single-tier | 808 | 157.2 |
| Grand Valley | lower-tier | 3851 | 24.28 |
| Gravenhurst | lower-tier | 13157 | 26.9 |
| Greater Madawaska | lower-tier | 2864 | 2.81 |
| Greater Napanee | lower-tier | 16879 | 36.51 |
| Greater Sudbury | single-tier | 166004 | 52.1 |
| Greenstone | single-tier | 4309 | 1.58 |
| Grey Highlands | lower-tier | 10424 | 11.86 |
| Grimsby | lower-tier | 28883 | 420.36 |
| Guelph | single-tier | 143740 | 1644.06 |
| Guelph/Eramosa | lower-tier | 13904 | 47.48 |
| Haldimand | single-tier | 49216 | 39.36 |
| Halton Hills | lower-tier | 62951 | 227.42 |
| Hamilton | lower-tier | 11059 | 43.19 |
| Hamilton | single-tier | 569353 | 509.12 |
| Hanover | lower-tier | 7967 | 814.62 |
| Harley | single-tier | 524 | 5.67 |
| Harris | single-tier | 530 | 10.64 |
| Hastings Highlands | lower-tier | 4385 | 4.54 |
| Havelock-Belmont-Methuen | lower-tier | 5083 | 9.6 |
| Hawkesbury | lower-tier | 10194 | 1009.31 |
| Head, Clara and Maria | lower-tier | 267 | 0.37 |
| Hearst | single-tier | 4794 | 48.89 |
| Highlands East | lower-tier | 3830 | 5.57 |
| Hilliard | single-tier | 215 | 2.36 |
| Hilton | single-tier | 382 | 3.33 |
| Hilton Beach | single-tier | 198 | 78.57 |
| Hornepayne | single-tier | 968 | 4.77 |
| Horton | lower-tier | 3182 | 20.14 |
| Howick | lower-tier | 4045 | 14.12 |
| Hudson | single-tier | 530 | 5.87 |
| Huntsville | lower-tier | 21147 | 29.99 |
| Huron East | lower-tier | 9512 | 14.22 |
| Huron Shores | single-tier | 1860 | 4.12 |
| Huron-Kinloss | lower-tier | 7723 | 17.52 |
| Ignace | single-tier | 1206 | 16.72 |
| Ingersoll | lower-tier | 13693 | 1075.65 |
| Innisfil | lower-tier | 43326 | 165.12 |
| Iroquois Falls | single-tier | 4418 | 7.38 |
| James | single-tier | 348 | 4.07 |
| Jocelyn | single-tier | 314 | 2.41 |
| Johnson | single-tier | 749 | 6.27 |
| Joly | single-tier | 293 | 1.51 |
| Kapuskasing | single-tier | 8057 | 95.94 |
| Kawartha Lakes | single-tier | 79247 | 26.12 |
| Kearney | single-tier | 974 | 1.84 |
| Kenora | single-tier | 14967 | 70.72 |
| Kerns | single-tier | 330 | 3.64 |
| Killaloe, Hagarty and Richards | lower-tier | 2410 | 6.15 |
| Killarney | single-tier | 397 | 0.27 |
| Kincardine | lower-tier | 12268 | 22.81 |
| King | lower-tier | 27333 | 82.3 |
| Kingston | single-tier | 132485 | 293.38 |
| Kingsville | lower-tier | 22119 | 89.89 |
| Kirkland Lake | single-tier | 7750 | 29.66 |
| Kitchener | lower-tier | 256885 | 1877.68 |
| La Vallee | single-tier | 788 | 3.32 |
| Laird | single-tier | 1121 | 10.86 |
| Lake of Bays | lower-tier | 3759 | 5.63 |
| Lake of the Woods | single-tier | 308 | 0.41 |
| Lakeshore | lower-tier | 40410 | 76.39 |
| Lambton Shores | lower-tier | 11876 | 35.93 |
| Lanark Highlands | lower-tier | 5737 | 5.56 |
| Larder Lake | single-tier | 745 | 3.27 |
| LaSalle | lower-tier | 32721 | 503.71 |
| Latchford | single-tier | 355 | 2.33 |
| Laurentian Hills | lower-tier | 2885 | 4.55 |
| Laurentian Valley | lower-tier | 9450 | 17.53 |
| Leamington | lower-tier | 29680 | 113.61 |
| Leeds and the Thousand Islands | lower-tier | 9804 | 16.12 |
| Limerick | lower-tier | 436 | 2.17 |
| Lincoln | lower-tier | 25719 | 158.04 |
| London | single-tier | 422324 | 1004.34 |
| Loyalist | lower-tier | 17943 | 52.35 |
| Lucan Biddulph | lower-tier | 5680 | 33.59 |
| Macdonald, Meredith and Aberdeen Additional | single-tier | 1513 | 9.27 |
| Machar | single-tier | 969 | 5.31 |
| Machin | single-tier | 1012 | 3.49 |
| Madawaska Valley | lower-tier | 3927 | 5.9 |
| Madoc | lower-tier | 2233 | 8.13 |
| Magnetawan | single-tier | 1753 | 3.33 |
| Malahide | lower-tier | 9308 | 23.61 |
| Manitouwadge | single-tier | 1974 | 5.61 |
| Mapleton | lower-tier | 10839 | 20.24 |
| Marathon | single-tier | 3138 | 18.79 |
| Markham | lower-tier | 338503 | 1604.81 |
| Markstay-Warren | single-tier | 2708 | 5.35 |
| Marmora and Lake | lower-tier | 4267 | 7.93 |
| Matachewan | single-tier | 268 | 0.5 |
| Mattawa | single-tier | 1881 | 512.53 |
| Mattawan | single-tier | 153 | 0.76 |
| Mattice-Val Côté | single-tier | 542 | 1.31 |
| McDougall | single-tier | 2744 | 10.39 |
| McGarry | single-tier | 579 | 6.76 |
| McKellar | single-tier | 1419 | 8.06 |
| McMurrich/Monteith | single-tier | 907 | 3.3 |
| McNab/Braeside | lower-tier | 7591 | 29.74 |
| Meaford | lower-tier | 11485 | 19.55 |
| Melancthon | lower-tier | 3132 | 10.09 |
| Merrickville-Wolford | lower-tier | 3135 | 14.63 |
| Middlesex Centre | lower-tier | 18928 | 32.18 |
| Midland | lower-tier | 17817 | 504.3 |
| Milton | lower-tier | 132979 | 365.5 |
| Minden Hills | lower-tier | 6971 | 8.23 |
| Minto | lower-tier | 9094 | 30.29 |
| Mississauga | lower-tier | 717961 | 2452.56 |
| Mississippi Mills | lower-tier | 14740 | 28.83 |
| Mono | lower-tier | 9421 | 33.84 |
| Montague | lower-tier | 3914 | 14.06 |
| Moonbeam | single-tier | 1157 | 4.93 |
| Moosonee | single-tier | 1512 | 2.76 |
| Morley | single-tier | 493 | 1.27 |
| Morris-Turnberry | lower-tier | 3590 | 9.53 |
| Mulmur | lower-tier | 3571 | 12.48 |
| Muskoka Lakes | lower-tier | 7652 | 9.88 |
| Nairn and Hyman | single-tier | 373 | 2.34 |
| The Nation | lower-tier | 13350 | 20.26 |
| Neebing | single-tier | 2241 | 2.56 |
| New Tecumseth | lower-tier | 43948 | 160.47 |
| Newbury | lower-tier | 440 | 248.59 |
| Newmarket | lower-tier | 87942 | 2284.21 |
| Niagara Falls | lower-tier | 94415 | 449.06 |
| Niagara-on-the-Lake | lower-tier | 19088 | 145.32 |
| Nipigon | single-tier | 1473 | 13.65 |
| Nipissing | single-tier | 1769 | 4.56 |
| Norfolk | single-tier | 67490 | 42.24 |
| North Algona Wilberforce | lower-tier | 3111 | 8.43 |
| North Bay | single-tier | 52662 | 166.9 |
| North Dumfries | lower-tier | 10619 | 56.46 |
| North Dundas | lower-tier | 11304 | 22.5 |
| North Frontenac | lower-tier | 2285 | 1.97 |
| North Glengarry | lower-tier | 10144 | 15.77 |
| North Grenville | lower-tier | 17964 | 51.05 |
| North Huron | lower-tier | 5052 | 28.22 |
| North Kawartha | lower-tier | 2877 | 3.85 |
| North Middlesex | lower-tier | 6307 | 10.54 |
| North Perth | lower-tier | 15538 | 31.51 |
| The North Shore | single-tier | 531 | 2.31 |
| North Stormont | lower-tier | 7400 | 14.36 |
| Northeastern Manitoulin and the Islands | single-tier | 2641 | 5.4 |
| Northern Bruce Peninsula | lower-tier | 4404 | 5.68 |
| Norwich | lower-tier | 11151 | 26.3 |
| Oakville | lower-tier | 213759 | 1538.5 |
| O'Connor | single-tier | 689 | 6.35 |
| Oil Springs | lower-tier | 647 | 79.48 |
| Oliver Paipoonge | single-tier | 6035 | 17.22 |
| Opasatika | single-tier | 200 | 0.61 |
| Orangeville | lower-tier | 30167 | 1989.91 |
| Orillia | single-tier | 33411 | 1171.08 |
| Oro-Medonte | lower-tier | 23017 | 39.32 |
| Oshawa | lower-tier | 175383 | 1203.56 |
| Otonabee-South Monaghan | lower-tier | 7087 | 20.47 |
| Ottawa | single-tier | 1017449 | 364.91 |
| Owen Sound | lower-tier | 21612 | 892.69 |
| Papineau-Cameron | single-tier | 982 | 1.74 |
| Parry Sound | single-tier | 6879 | 525.11 |
| Pelee | single-tier | 230 | 5.61 |
| Pelham | lower-tier | 18192 | 143.98 |
| Pembroke | single-tier | 14364 | 1003.07 |
| Penetanguishene | lower-tier | 10077 | 396.42 |
| Perry | single-tier | 2650 | 14.22 |
| Perth | lower-tier | 6469 | 529.81 |
| Perth East | lower-tier | 12595 | 17.69 |
| Perth South | lower-tier | 3776 | 9.64 |
| Petawawa | lower-tier | 18160 | 110.26 |
| Peterborough | single-tier | 83651 | 1291.71 |
| Petrolia | lower-tier | 6013 | 482.58 |
| Pickering | lower-tier | 99186 | 429.19 |
| Pickle Lake | single-tier | 398 | 1.61 |
| Plummer Additional | single-tier | 757 | 3.45 |
| Plympton-Wyoming | lower-tier | 8308 | 26.06 |
| Point Edward | lower-tier | 1930 | 584.85 |
| Port Colborne | lower-tier | 20033 | 164.22 |
| Port Hope | lower-tier | 17294 | 62.03 |
| Powassan | single-tier | 3346 | 14.99 |
| Prescott | single-tier | 4078 | 825.51 |
| Prince | single-tier | 975 | 11.47 |
| Prince Edward | single-tier | 25704 | 24.42 |
| Puslinch | lower-tier | 7944 | 36.98 |
| Quinte West | single-tier | 46560 | 93.98 |
| Rainy River | single-tier | 752 | 241.03 |
| Ramara | lower-tier | 10377 | 25.01 |
| Red Lake | single-tier | 4094 | 6.79 |
| Red Rock | single-tier | 895 | 14.41 |
| Renfrew | lower-tier | 8190 | 639.34 |
| Richmond Hill | lower-tier | 202022 | 2004.39 |
| Rideau Lakes | lower-tier | 10883 | 15.29 |
| Russell | lower-tier | 19598 | 98.59 |
| Ryerson | single-tier | 745 | 4.01 |
| Sables-Spanish Rivers | single-tier | 3237 | 4.04 |
| Sarnia | lower-tier | 72047 | 439.58 |
| Saugeen Shores | lower-tier | 15908 | 93.47 |
| Sault Ste. Marie | single-tier | 72051 | 324.57 |
| Schreiber | single-tier | 1039 | 29.01 |
| Scugog | lower-tier | 21581 | 45.49 |
| Seguin | single-tier | 5280 | 9.0 |
| Selwyn | lower-tier | 18653 | 59.01 |
| Severn | lower-tier | 14576 | 27.87 |
| Shelburne | lower-tier | 8994 | 1371.04 |
| Shuniah | single-tier | 3247 | 5.68 |
| Sioux Lookout | single-tier | 5839 | 15.45 |
| Sioux Narrows-Nestor Falls | single-tier | 727 | 0.6 |
| Smiths Falls | single-tier | 9254 | 957.97 |
| Smooth Rock Falls | single-tier | 1200 | 6.01 |
| South Algonquin | single-tier | 1055 | 1.22 |
| South Bruce | lower-tier | 5880 | 12.08 |
| South Bruce Peninsula | lower-tier | 9137 | 17.22 |
| South Dundas | lower-tier | 11044 | 21.18 |
| South Frontenac | lower-tier | 20188 | 21.29 |
| South Glengarry | lower-tier | 13330 | 22.03 |
| South Huron | lower-tier | 10063 | 23.67 |
| South River | single-tier | 1101 | 267.88 |
| South Stormont | lower-tier | 13570 | 30.31 |
| Southgate | lower-tier | 8716 | 13.55 |
| Southwest Middlesex | lower-tier | 5893 | 13.77 |
| South-West Oxford | lower-tier | 7583 | 20.52 |
| Southwold | lower-tier | 4851 | 16.1 |
| Spanish | single-tier | 670 | 6.27 |
| Springwater | lower-tier | 21701 | 40.5 |
| St. Catharines | lower-tier | 136803 | 1422.07 |
| St. Clair | lower-tier | 14659 | 23.7 |
| St. Joseph | single-tier | 1426 | 11.17 |
| St. Marys | single-tier | 7386 | 593.73 |
| St. Thomas | single-tier | 42840 | 1203.03 |
| St.-Charles | single-tier | 1357 | 4.32 |
| Stirling-Rawdon | lower-tier | 5015 | 17.75 |
| Stone Mills | lower-tier | 7826 | 11.28 |
| Stratford | single-tier | 33232 | 1107.0 |
| Strathroy-Caradoc | lower-tier | 23871 | 88.13 |
| Strong | single-tier | 1566 | 9.86 |
| Sundridge | single-tier | 938 | 416.89 |
| Tarbutt | single-tier | 573 | 10.85 |
| Tay | lower-tier | 11091 | 80.45 |
| Tay Valley | lower-tier | 5925 | 11.21 |
| Tecumseh | lower-tier | 23300 | 246.33 |
| Tehkummah | single-tier | 450 | 3.42 |
| Temagami | single-tier | 862 | 0.46 |
| Temiskaming Shores | single-tier | 9634 | 54.53 |
| Terrace Bay | single-tier | 1528 | 10.09 |
| Thames Centre | lower-tier | 13980 | 32.21 |
| Thessalon | single-tier | 1260 | 287.67 |
| Thornloe | single-tier | 92 | 13.96 |
| Thorold | lower-tier | 23816 | 285.94 |
| Thunder Bay | single-tier | 108843 | 332.07 |
| Tillsonburg | lower-tier | 18615 | 838.51 |
| Timmins | single-tier | 41145 | 13.92 |
| Tiny | lower-tier | 12966 | 38.7 |
| Toronto | single-tier | 2794356 | 4427.75 |
| Trent Hills | lower-tier | 13861 | 26.97 |
| Trent Lakes | lower-tier | 6439 | 7.72 |
| Tudor and Cashel | lower-tier | 740 | 1.71 |
| Tweed | lower-tier | 6067 | 6.6 |
| Tyendinaga | lower-tier | 4538 | 14.53 |
| Uxbridge | lower-tier | 21556 | 51.26 |
| Val Rita-Harty | single-tier | 757 | 2.0 |
| Vaughan | lower-tier | 323103 | 1185.96 |
| Wainfleet | lower-tier | 6887 | 31.66 |
| Warwick | lower-tier | 3641 | 12.55 |
| Wasaga Beach | lower-tier | 24862 | 432.99 |
| Waterloo | lower-tier | 121436 | 1895.66 |
| Wawa | single-tier | 2705 | 6.57 |
| Welland | lower-tier | 55750 | 686.91 |
| Wellesley | lower-tier | 11318 | 40.75 |
| Wellington North | lower-tier | 12431 | 23.62 |
| West Elgin | lower-tier | 5060 | 15.71 |
| West Grey | lower-tier | 13131 | 15.0 |
| West Lincoln | lower-tier | 15454 | 39.93 |
| West Nipissing | single-tier | 14583 | 7.45 |
| West Perth | lower-tier | 9038 | 15.61 |
| Westport | lower-tier | 634 | 289.5 |
| Whitby | lower-tier | 138501 | 944.17 |
| Whitchurch-Stouffville | lower-tier | 49864 | 241.57 |
| White River | single-tier | 557 | 5.83 |
| Whitestone | single-tier | 1075 | 1.16 |
| Whitewater | lower-tier | 7225 | 13.49 |
| Wilmot | lower-tier | 21429 | 81.23 |
| Windsor | single-tier | 229660 | 1572.8 |
| Wollaston | lower-tier | 721 | 3.34 |
| Woodstock | lower-tier | 46705 | 827.22 |
| Woolwich | lower-tier | 26999 | 82.68 |
| Zorra | lower-tier | 8628 | 16.3 |

And a wider one that drops its columns from the last as the window narrows, keeping the latest population (narrow the window, then use a row's button to see what it dropped).

``` python
years = [f"population_{year}" for year in (1996, 2001, 2006, 2011, 2016, 2021)]

(
    GTI(towny[["name", "status", *years]].head(10), rowname_col="name")
    .fmt_integer(columns=years)
    .i_cols_priority(columns="population_2021")
    .i_responsive("collapse")
)
```

|  | status | population_1996 | population_2001 | population_2006 | population_2011 | population_2016 | population_2021 |
|----|----|----|----|----|----|----|----|
| Addington Highlands | lower-tier | 2,429 | 2,402 | 2,512 | 2,517 | 2,318 | 2,534 |
| Adelaide Metcalfe | lower-tier | 3,128 | 3,149 | 3,135 | 3,028 | 2,990 | 3,011 |
| Adjala-Tosorontio | lower-tier | 9,359 | 10,082 | 10,695 | 10,603 | 10,975 | 10,989 |
| Admaston/Bromley | lower-tier | 2,837 | 2,824 | 2,716 | 2,844 | 2,935 | 2,995 |
| Ajax | lower-tier | 64,430 | 73,753 | 90,167 | 109,600 | 119,677 | 126,666 |
| Alberton | single-tier | 1,027 | 956 | 958 | 864 | 969 | 954 |
| Alfred and Plantagenet | lower-tier | 8,315 | 8,593 | 8,654 | 9,196 | 9,680 | 9,949 |
| Algonquin Highlands | lower-tier | 1,687 | 1,827 | 1,976 | 2,186 | 2,351 | 2,588 |
| Alnwick/Haldimand | lower-tier | 5,528 | 5,846 | 6,435 | 6,617 | 6,869 | 7,473 |
| Amaranth | lower-tier | 3,450 | 3,770 | 3,845 | 3,963 | 4,079 | 4,327 |
