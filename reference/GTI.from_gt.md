# GTI.from_gt()

Make an interactive table from a [GT](../reference/GT.md#great_tables.GT) table.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L264-L326)

``` python
GTI.from_gt(gt)
```

The new [GTI](../reference/GTI.md#great_tables.GTI) table has everything the [GT](../reference/GT.md#great_tables.GT) table has (its data, formats, styles, and options). Readers can do with it what they can with any new [GTI](../reference/GTI.md#great_tables.GTI) table, unless [`opt_interactive()`](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive) was used on the [GT](../reference/GT.md#great_tables.GT) table: then they can do what it set (sorting, searching, filtering, and so on), with [GTI](../reference/GTI.md#great_tables.GTI)'s control bar, page controls and way of fitting a narrow container.

## Parameters

`gt: GT`  
A [GT](../reference/GT.md#great_tables.GT) table.

## Returns

`GTI`  
A new GTI object.

## Examples

A table made with [GT()](../reference/GT.md#great_tables.GT) can become interactive at the end.

``` python
from great_tables import GT, GTI, data

towny_mini = data.pl.towny.select("name", "population_2021")

gt_tbl = GT(towny_mini).fmt_integer(columns="population_2021")

GTI.from_gt(gt_tbl)
```

| name | population_2021 |
|----|----|
| Addington Highlands | 2,534 |
| Adelaide Metcalfe | 3,011 |
| Adjala-Tosorontio | 10,989 |
| Admaston/Bromley | 2,995 |
| Ajax | 126,666 |
| Alberton | 954 |
| Alfred and Plantagenet | 9,949 |
| Algonquin Highlands | 2,588 |
| Alnwick/Haldimand | 7,473 |
| Amaranth | 4,327 |
| Amherstburg | 23,524 |
| The Archipelago | 979 |
| Armour | 1,459 |
| Armstrong | 1,199 |
| Arnprior | 9,629 |
| Arran-Elderslie | 6,913 |
| Ashfield-Colborne-Wawanosh | 5,884 |
| Asphodel-Norwood | 4,658 |
| Assiginack | 1,008 |
| Athens | 3,042 |
| Atikokan | 2,642 |
| Augusta | 7,386 |
| Aurora | 62,057 |
| Aylmer | 7,699 |
| Baldwin | 579 |
| Bancroft | 4,065 |
| Barrie | 147,829 |
| Bayham | 7,096 |
| Beckwith | 9,021 |
| Belleville | 55,071 |
| Billings | 753 |
| Black River-Matheson | 2,572 |
| Blandford-Blenheim | 7,565 |
| Blind River | 3,422 |
| The Blue Mountains | 9,390 |
| Bluewater | 7,540 |
| Bonfield | 2,146 |
| Bonnechere Valley | 3,898 |
| Bracebridge | 17,305 |
| Bradford West Gwillimbury | 42,880 |
| Brampton | 656,480 |
| Brant | 39,474 |
| Brantford | 104,688 |
| Brethour | 105 |
| Brighton | 12,108 |
| Brock | 12,567 |
| Brockton | 9,784 |
| Brockville | 22,116 |
| Brooke-Alvinston | 2,359 |
| Bruce Mines | 582 |
| Brudenell, Lyndoch and Raglan | 1,552 |
| Burk's Falls | 957 |
| Burlington | 186,948 |
| Burpee and Mills | 382 |
| Caledon | 76,581 |
| Callander | 3,964 |
| Calvin | 557 |
| Cambridge | 138,479 |
| Carleton Place | 12,517 |
| Carling | 1,491 |
| Carlow/Mayo | 953 |
| Casey | 341 |
| Casselman | 3,960 |
| Cavan Monaghan | 10,016 |
| Central Elgin | 13,746 |
| Central Frontenac | 4,892 |
| Central Huron | 7,799 |
| Central Manitoulin | 2,235 |
| Centre Hastings | 4,801 |
| Centre Wellington | 31,093 |
| Chamberlain | 311 |
| Champlain | 8,665 |
| Chapleau | 1,942 |
| Chapple | 763 |
| Charlton and Dack | 686 |
| Chatham-Kent | 103,988 |
| Chatsworth | 7,080 |
| Chisholm | 1,312 |
| Clarence-Rockland | 26,505 |
| Clarington | 101,427 |
| Clearview | 14,814 |
| Cobalt | 989 |
| Cobourg | 20,519 |
| Cochrane | 5,390 |
| Cockburn Island | 16 |
| Coleman | 517 |
| Collingwood | 24,811 |
| Conmee | 798 |
| Cornwall | 47,845 |
| Cramahe | 6,509 |
| Dawn-Euphemia | 1,968 |
| Dawson | 399 |
| Deep River | 4,175 |
| Deseronto | 1,747 |
| Dorion | 375 |
| Douro-Dummer | 7,632 |
| Drummond/North Elmsley | 8,183 |
| Dryden | 7,388 |
| Dubreuilville | 576 |
| Dutton/Dunwich | 4,152 |
| Dysart, Dudley, Harcourt, Guilford, Harburn, Bruton, Havelock, Eyre and Clyde | 7,182 |
| Ear Falls | 924 |
| East Ferris | 4,946 |
| East Garafraxa | 2,794 |
| East Gwillimbury | 34,637 |
| East Hawkesbury | 3,418 |
| East Zorra-Tavistock | 7,841 |
| Edwardsburgh/Cardinal | 7,505 |
| Elizabethtown-Kitley | 9,545 |
| Elliot Lake | 11,372 |
| Emo | 1,204 |
| Englehart | 1,442 |
| Enniskillen | 2,825 |
| Erin | 11,981 |
| Espanola | 5,185 |
| Essa | 22,970 |
| Essex | 21,216 |
| Evanturel | 502 |
| Faraday | 1,612 |
| Fauquier-Strickland | 467 |
| Fort Erie | 32,901 |
| Fort Frances | 7,466 |
| French River | 2,828 |
| Front of Yonge | 2,595 |
| Frontenac Islands | 1,930 |
| Gananoque | 5,383 |
| Gauthier | 151 |
| Georgian Bay | 3,441 |
| Georgian Bluffs | 11,100 |
| Georgina | 47,642 |
| Gillies | 441 |
| Goderich | 7,881 |
| Gordon/Barrie Island | 613 |
| Gore Bay | 808 |
| Grand Valley | 3,851 |
| Gravenhurst | 13,157 |
| Greater Madawaska | 2,864 |
| Greater Napanee | 16,879 |
| Greater Sudbury | 166,004 |
| Greenstone | 4,309 |
| Grey Highlands | 10,424 |
| Grimsby | 28,883 |
| Guelph | 143,740 |
| Guelph/Eramosa | 13,904 |
| Haldimand | 49,216 |
| Halton Hills | 62,951 |
| Hamilton | 11,059 |
| Hamilton | 569,353 |
| Hanover | 7,967 |
| Harley | 524 |
| Harris | 530 |
| Hastings Highlands | 4,385 |
| Havelock-Belmont-Methuen | 5,083 |
| Hawkesbury | 10,194 |
| Head, Clara and Maria | 267 |
| Hearst | 4,794 |
| Highlands East | 3,830 |
| Hilliard | 215 |
| Hilton | 382 |
| Hilton Beach | 198 |
| Hornepayne | 968 |
| Horton | 3,182 |
| Howick | 4,045 |
| Hudson | 530 |
| Huntsville | 21,147 |
| Huron East | 9,512 |
| Huron Shores | 1,860 |
| Huron-Kinloss | 7,723 |
| Ignace | 1,206 |
| Ingersoll | 13,693 |
| Innisfil | 43,326 |
| Iroquois Falls | 4,418 |
| James | 348 |
| Jocelyn | 314 |
| Johnson | 749 |
| Joly | 293 |
| Kapuskasing | 8,057 |
| Kawartha Lakes | 79,247 |
| Kearney | 974 |
| Kenora | 14,967 |
| Kerns | 330 |
| Killaloe, Hagarty and Richards | 2,410 |
| Killarney | 397 |
| Kincardine | 12,268 |
| King | 27,333 |
| Kingston | 132,485 |
| Kingsville | 22,119 |
| Kirkland Lake | 7,750 |
| Kitchener | 256,885 |
| La Vallee | 788 |
| Laird | 1,121 |
| Lake of Bays | 3,759 |
| Lake of the Woods | 308 |
| Lakeshore | 40,410 |
| Lambton Shores | 11,876 |
| Lanark Highlands | 5,737 |
| Larder Lake | 745 |
| LaSalle | 32,721 |
| Latchford | 355 |
| Laurentian Hills | 2,885 |
| Laurentian Valley | 9,450 |
| Leamington | 29,680 |
| Leeds and the Thousand Islands | 9,804 |
| Limerick | 436 |
| Lincoln | 25,719 |
| London | 422,324 |
| Loyalist | 17,943 |
| Lucan Biddulph | 5,680 |
| Macdonald, Meredith and Aberdeen Additional | 1,513 |
| Machar | 969 |
| Machin | 1,012 |
| Madawaska Valley | 3,927 |
| Madoc | 2,233 |
| Magnetawan | 1,753 |
| Malahide | 9,308 |
| Manitouwadge | 1,974 |
| Mapleton | 10,839 |
| Marathon | 3,138 |
| Markham | 338,503 |
| Markstay-Warren | 2,708 |
| Marmora and Lake | 4,267 |
| Matachewan | 268 |
| Mattawa | 1,881 |
| Mattawan | 153 |
| Mattice-Val Côté | 542 |
| McDougall | 2,744 |
| McGarry | 579 |
| McKellar | 1,419 |
| McMurrich/Monteith | 907 |
| McNab/Braeside | 7,591 |
| Meaford | 11,485 |
| Melancthon | 3,132 |
| Merrickville-Wolford | 3,135 |
| Middlesex Centre | 18,928 |
| Midland | 17,817 |
| Milton | 132,979 |
| Minden Hills | 6,971 |
| Minto | 9,094 |
| Mississauga | 717,961 |
| Mississippi Mills | 14,740 |
| Mono | 9,421 |
| Montague | 3,914 |
| Moonbeam | 1,157 |
| Moosonee | 1,512 |
| Morley | 493 |
| Morris-Turnberry | 3,590 |
| Mulmur | 3,571 |
| Muskoka Lakes | 7,652 |
| Nairn and Hyman | 373 |
| The Nation | 13,350 |
| Neebing | 2,241 |
| New Tecumseth | 43,948 |
| Newbury | 440 |
| Newmarket | 87,942 |
| Niagara Falls | 94,415 |
| Niagara-on-the-Lake | 19,088 |
| Nipigon | 1,473 |
| Nipissing | 1,769 |
| Norfolk | 67,490 |
| North Algona Wilberforce | 3,111 |
| North Bay | 52,662 |
| North Dumfries | 10,619 |
| North Dundas | 11,304 |
| North Frontenac | 2,285 |
| North Glengarry | 10,144 |
| North Grenville | 17,964 |
| North Huron | 5,052 |
| North Kawartha | 2,877 |
| North Middlesex | 6,307 |
| North Perth | 15,538 |
| The North Shore | 531 |
| North Stormont | 7,400 |
| Northeastern Manitoulin and the Islands | 2,641 |
| Northern Bruce Peninsula | 4,404 |
| Norwich | 11,151 |
| Oakville | 213,759 |
| O'Connor | 689 |
| Oil Springs | 647 |
| Oliver Paipoonge | 6,035 |
| Opasatika | 200 |
| Orangeville | 30,167 |
| Orillia | 33,411 |
| Oro-Medonte | 23,017 |
| Oshawa | 175,383 |
| Otonabee-South Monaghan | 7,087 |
| Ottawa | 1,017,449 |
| Owen Sound | 21,612 |
| Papineau-Cameron | 982 |
| Parry Sound | 6,879 |
| Pelee | 230 |
| Pelham | 18,192 |
| Pembroke | 14,364 |
| Penetanguishene | 10,077 |
| Perry | 2,650 |
| Perth | 6,469 |
| Perth East | 12,595 |
| Perth South | 3,776 |
| Petawawa | 18,160 |
| Peterborough | 83,651 |
| Petrolia | 6,013 |
| Pickering | 99,186 |
| Pickle Lake | 398 |
| Plummer Additional | 757 |
| Plympton-Wyoming | 8,308 |
| Point Edward | 1,930 |
| Port Colborne | 20,033 |
| Port Hope | 17,294 |
| Powassan | 3,346 |
| Prescott | 4,078 |
| Prince | 975 |
| Prince Edward | 25,704 |
| Puslinch | 7,944 |
| Quinte West | 46,560 |
| Rainy River | 752 |
| Ramara | 10,377 |
| Red Lake | 4,094 |
| Red Rock | 895 |
| Renfrew | 8,190 |
| Richmond Hill | 202,022 |
| Rideau Lakes | 10,883 |
| Russell | 19,598 |
| Ryerson | 745 |
| Sables-Spanish Rivers | 3,237 |
| Sarnia | 72,047 |
| Saugeen Shores | 15,908 |
| Sault Ste. Marie | 72,051 |
| Schreiber | 1,039 |
| Scugog | 21,581 |
| Seguin | 5,280 |
| Selwyn | 18,653 |
| Severn | 14,576 |
| Shelburne | 8,994 |
| Shuniah | 3,247 |
| Sioux Lookout | 5,839 |
| Sioux Narrows-Nestor Falls | 727 |
| Smiths Falls | 9,254 |
| Smooth Rock Falls | 1,200 |
| South Algonquin | 1,055 |
| South Bruce | 5,880 |
| South Bruce Peninsula | 9,137 |
| South Dundas | 11,044 |
| South Frontenac | 20,188 |
| South Glengarry | 13,330 |
| South Huron | 10,063 |
| South River | 1,101 |
| South Stormont | 13,570 |
| Southgate | 8,716 |
| Southwest Middlesex | 5,893 |
| South-West Oxford | 7,583 |
| Southwold | 4,851 |
| Spanish | 670 |
| Springwater | 21,701 |
| St. Catharines | 136,803 |
| St. Clair | 14,659 |
| St. Joseph | 1,426 |
| St. Marys | 7,386 |
| St. Thomas | 42,840 |
| St.-Charles | 1,357 |
| Stirling-Rawdon | 5,015 |
| Stone Mills | 7,826 |
| Stratford | 33,232 |
| Strathroy-Caradoc | 23,871 |
| Strong | 1,566 |
| Sundridge | 938 |
| Tarbutt | 573 |
| Tay | 11,091 |
| Tay Valley | 5,925 |
| Tecumseh | 23,300 |
| Tehkummah | 450 |
| Temagami | 862 |
| Temiskaming Shores | 9,634 |
| Terrace Bay | 1,528 |
| Thames Centre | 13,980 |
| Thessalon | 1,260 |
| Thornloe | 92 |
| Thorold | 23,816 |
| Thunder Bay | 108,843 |
| Tillsonburg | 18,615 |
| Timmins | 41,145 |
| Tiny | 12,966 |
| Toronto | 2,794,356 |
| Trent Hills | 13,861 |
| Trent Lakes | 6,439 |
| Tudor and Cashel | 740 |
| Tweed | 6,067 |
| Tyendinaga | 4,538 |
| Uxbridge | 21,556 |
| Val Rita-Harty | 757 |
| Vaughan | 323,103 |
| Wainfleet | 6,887 |
| Warwick | 3,641 |
| Wasaga Beach | 24,862 |
| Waterloo | 121,436 |
| Wawa | 2,705 |
| Welland | 55,750 |
| Wellesley | 11,318 |
| Wellington North | 12,431 |
| West Elgin | 5,060 |
| West Grey | 13,131 |
| West Lincoln | 15,454 |
| West Nipissing | 14,583 |
| West Perth | 9,038 |
| Westport | 634 |
| Whitby | 138,501 |
| Whitchurch-Stouffville | 49,864 |
| White River | 557 |
| Whitestone | 1,075 |
| Whitewater | 7,225 |
| Wilmot | 21,429 |
| Windsor | 229,660 |
| Wollaston | 721 |
| Woodstock | 46,705 |
| Woolwich | 26,999 |
| Zorra | 8,628 |

A Polars DataFrame's `.style` property makes a [GT](../reference/GT.md#great_tables.GT) table too, so a table started from it can become interactive in the same way.

``` python
GTI.from_gt(towny_mini.style.fmt_integer(columns="population_2021")).i_cols_profile()
```

| name | population_2021 |
|----|----|
| Addington Highlands | 2,534 |
| Adelaide Metcalfe | 3,011 |
| Adjala-Tosorontio | 10,989 |
| Admaston/Bromley | 2,995 |
| Ajax | 126,666 |
| Alberton | 954 |
| Alfred and Plantagenet | 9,949 |
| Algonquin Highlands | 2,588 |
| Alnwick/Haldimand | 7,473 |
| Amaranth | 4,327 |
| Amherstburg | 23,524 |
| The Archipelago | 979 |
| Armour | 1,459 |
| Armstrong | 1,199 |
| Arnprior | 9,629 |
| Arran-Elderslie | 6,913 |
| Ashfield-Colborne-Wawanosh | 5,884 |
| Asphodel-Norwood | 4,658 |
| Assiginack | 1,008 |
| Athens | 3,042 |
| Atikokan | 2,642 |
| Augusta | 7,386 |
| Aurora | 62,057 |
| Aylmer | 7,699 |
| Baldwin | 579 |
| Bancroft | 4,065 |
| Barrie | 147,829 |
| Bayham | 7,096 |
| Beckwith | 9,021 |
| Belleville | 55,071 |
| Billings | 753 |
| Black River-Matheson | 2,572 |
| Blandford-Blenheim | 7,565 |
| Blind River | 3,422 |
| The Blue Mountains | 9,390 |
| Bluewater | 7,540 |
| Bonfield | 2,146 |
| Bonnechere Valley | 3,898 |
| Bracebridge | 17,305 |
| Bradford West Gwillimbury | 42,880 |
| Brampton | 656,480 |
| Brant | 39,474 |
| Brantford | 104,688 |
| Brethour | 105 |
| Brighton | 12,108 |
| Brock | 12,567 |
| Brockton | 9,784 |
| Brockville | 22,116 |
| Brooke-Alvinston | 2,359 |
| Bruce Mines | 582 |
| Brudenell, Lyndoch and Raglan | 1,552 |
| Burk's Falls | 957 |
| Burlington | 186,948 |
| Burpee and Mills | 382 |
| Caledon | 76,581 |
| Callander | 3,964 |
| Calvin | 557 |
| Cambridge | 138,479 |
| Carleton Place | 12,517 |
| Carling | 1,491 |
| Carlow/Mayo | 953 |
| Casey | 341 |
| Casselman | 3,960 |
| Cavan Monaghan | 10,016 |
| Central Elgin | 13,746 |
| Central Frontenac | 4,892 |
| Central Huron | 7,799 |
| Central Manitoulin | 2,235 |
| Centre Hastings | 4,801 |
| Centre Wellington | 31,093 |
| Chamberlain | 311 |
| Champlain | 8,665 |
| Chapleau | 1,942 |
| Chapple | 763 |
| Charlton and Dack | 686 |
| Chatham-Kent | 103,988 |
| Chatsworth | 7,080 |
| Chisholm | 1,312 |
| Clarence-Rockland | 26,505 |
| Clarington | 101,427 |
| Clearview | 14,814 |
| Cobalt | 989 |
| Cobourg | 20,519 |
| Cochrane | 5,390 |
| Cockburn Island | 16 |
| Coleman | 517 |
| Collingwood | 24,811 |
| Conmee | 798 |
| Cornwall | 47,845 |
| Cramahe | 6,509 |
| Dawn-Euphemia | 1,968 |
| Dawson | 399 |
| Deep River | 4,175 |
| Deseronto | 1,747 |
| Dorion | 375 |
| Douro-Dummer | 7,632 |
| Drummond/North Elmsley | 8,183 |
| Dryden | 7,388 |
| Dubreuilville | 576 |
| Dutton/Dunwich | 4,152 |
| Dysart, Dudley, Harcourt, Guilford, Harburn, Bruton, Havelock, Eyre and Clyde | 7,182 |
| Ear Falls | 924 |
| East Ferris | 4,946 |
| East Garafraxa | 2,794 |
| East Gwillimbury | 34,637 |
| East Hawkesbury | 3,418 |
| East Zorra-Tavistock | 7,841 |
| Edwardsburgh/Cardinal | 7,505 |
| Elizabethtown-Kitley | 9,545 |
| Elliot Lake | 11,372 |
| Emo | 1,204 |
| Englehart | 1,442 |
| Enniskillen | 2,825 |
| Erin | 11,981 |
| Espanola | 5,185 |
| Essa | 22,970 |
| Essex | 21,216 |
| Evanturel | 502 |
| Faraday | 1,612 |
| Fauquier-Strickland | 467 |
| Fort Erie | 32,901 |
| Fort Frances | 7,466 |
| French River | 2,828 |
| Front of Yonge | 2,595 |
| Frontenac Islands | 1,930 |
| Gananoque | 5,383 |
| Gauthier | 151 |
| Georgian Bay | 3,441 |
| Georgian Bluffs | 11,100 |
| Georgina | 47,642 |
| Gillies | 441 |
| Goderich | 7,881 |
| Gordon/Barrie Island | 613 |
| Gore Bay | 808 |
| Grand Valley | 3,851 |
| Gravenhurst | 13,157 |
| Greater Madawaska | 2,864 |
| Greater Napanee | 16,879 |
| Greater Sudbury | 166,004 |
| Greenstone | 4,309 |
| Grey Highlands | 10,424 |
| Grimsby | 28,883 |
| Guelph | 143,740 |
| Guelph/Eramosa | 13,904 |
| Haldimand | 49,216 |
| Halton Hills | 62,951 |
| Hamilton | 11,059 |
| Hamilton | 569,353 |
| Hanover | 7,967 |
| Harley | 524 |
| Harris | 530 |
| Hastings Highlands | 4,385 |
| Havelock-Belmont-Methuen | 5,083 |
| Hawkesbury | 10,194 |
| Head, Clara and Maria | 267 |
| Hearst | 4,794 |
| Highlands East | 3,830 |
| Hilliard | 215 |
| Hilton | 382 |
| Hilton Beach | 198 |
| Hornepayne | 968 |
| Horton | 3,182 |
| Howick | 4,045 |
| Hudson | 530 |
| Huntsville | 21,147 |
| Huron East | 9,512 |
| Huron Shores | 1,860 |
| Huron-Kinloss | 7,723 |
| Ignace | 1,206 |
| Ingersoll | 13,693 |
| Innisfil | 43,326 |
| Iroquois Falls | 4,418 |
| James | 348 |
| Jocelyn | 314 |
| Johnson | 749 |
| Joly | 293 |
| Kapuskasing | 8,057 |
| Kawartha Lakes | 79,247 |
| Kearney | 974 |
| Kenora | 14,967 |
| Kerns | 330 |
| Killaloe, Hagarty and Richards | 2,410 |
| Killarney | 397 |
| Kincardine | 12,268 |
| King | 27,333 |
| Kingston | 132,485 |
| Kingsville | 22,119 |
| Kirkland Lake | 7,750 |
| Kitchener | 256,885 |
| La Vallee | 788 |
| Laird | 1,121 |
| Lake of Bays | 3,759 |
| Lake of the Woods | 308 |
| Lakeshore | 40,410 |
| Lambton Shores | 11,876 |
| Lanark Highlands | 5,737 |
| Larder Lake | 745 |
| LaSalle | 32,721 |
| Latchford | 355 |
| Laurentian Hills | 2,885 |
| Laurentian Valley | 9,450 |
| Leamington | 29,680 |
| Leeds and the Thousand Islands | 9,804 |
| Limerick | 436 |
| Lincoln | 25,719 |
| London | 422,324 |
| Loyalist | 17,943 |
| Lucan Biddulph | 5,680 |
| Macdonald, Meredith and Aberdeen Additional | 1,513 |
| Machar | 969 |
| Machin | 1,012 |
| Madawaska Valley | 3,927 |
| Madoc | 2,233 |
| Magnetawan | 1,753 |
| Malahide | 9,308 |
| Manitouwadge | 1,974 |
| Mapleton | 10,839 |
| Marathon | 3,138 |
| Markham | 338,503 |
| Markstay-Warren | 2,708 |
| Marmora and Lake | 4,267 |
| Matachewan | 268 |
| Mattawa | 1,881 |
| Mattawan | 153 |
| Mattice-Val Côté | 542 |
| McDougall | 2,744 |
| McGarry | 579 |
| McKellar | 1,419 |
| McMurrich/Monteith | 907 |
| McNab/Braeside | 7,591 |
| Meaford | 11,485 |
| Melancthon | 3,132 |
| Merrickville-Wolford | 3,135 |
| Middlesex Centre | 18,928 |
| Midland | 17,817 |
| Milton | 132,979 |
| Minden Hills | 6,971 |
| Minto | 9,094 |
| Mississauga | 717,961 |
| Mississippi Mills | 14,740 |
| Mono | 9,421 |
| Montague | 3,914 |
| Moonbeam | 1,157 |
| Moosonee | 1,512 |
| Morley | 493 |
| Morris-Turnberry | 3,590 |
| Mulmur | 3,571 |
| Muskoka Lakes | 7,652 |
| Nairn and Hyman | 373 |
| The Nation | 13,350 |
| Neebing | 2,241 |
| New Tecumseth | 43,948 |
| Newbury | 440 |
| Newmarket | 87,942 |
| Niagara Falls | 94,415 |
| Niagara-on-the-Lake | 19,088 |
| Nipigon | 1,473 |
| Nipissing | 1,769 |
| Norfolk | 67,490 |
| North Algona Wilberforce | 3,111 |
| North Bay | 52,662 |
| North Dumfries | 10,619 |
| North Dundas | 11,304 |
| North Frontenac | 2,285 |
| North Glengarry | 10,144 |
| North Grenville | 17,964 |
| North Huron | 5,052 |
| North Kawartha | 2,877 |
| North Middlesex | 6,307 |
| North Perth | 15,538 |
| The North Shore | 531 |
| North Stormont | 7,400 |
| Northeastern Manitoulin and the Islands | 2,641 |
| Northern Bruce Peninsula | 4,404 |
| Norwich | 11,151 |
| Oakville | 213,759 |
| O'Connor | 689 |
| Oil Springs | 647 |
| Oliver Paipoonge | 6,035 |
| Opasatika | 200 |
| Orangeville | 30,167 |
| Orillia | 33,411 |
| Oro-Medonte | 23,017 |
| Oshawa | 175,383 |
| Otonabee-South Monaghan | 7,087 |
| Ottawa | 1,017,449 |
| Owen Sound | 21,612 |
| Papineau-Cameron | 982 |
| Parry Sound | 6,879 |
| Pelee | 230 |
| Pelham | 18,192 |
| Pembroke | 14,364 |
| Penetanguishene | 10,077 |
| Perry | 2,650 |
| Perth | 6,469 |
| Perth East | 12,595 |
| Perth South | 3,776 |
| Petawawa | 18,160 |
| Peterborough | 83,651 |
| Petrolia | 6,013 |
| Pickering | 99,186 |
| Pickle Lake | 398 |
| Plummer Additional | 757 |
| Plympton-Wyoming | 8,308 |
| Point Edward | 1,930 |
| Port Colborne | 20,033 |
| Port Hope | 17,294 |
| Powassan | 3,346 |
| Prescott | 4,078 |
| Prince | 975 |
| Prince Edward | 25,704 |
| Puslinch | 7,944 |
| Quinte West | 46,560 |
| Rainy River | 752 |
| Ramara | 10,377 |
| Red Lake | 4,094 |
| Red Rock | 895 |
| Renfrew | 8,190 |
| Richmond Hill | 202,022 |
| Rideau Lakes | 10,883 |
| Russell | 19,598 |
| Ryerson | 745 |
| Sables-Spanish Rivers | 3,237 |
| Sarnia | 72,047 |
| Saugeen Shores | 15,908 |
| Sault Ste. Marie | 72,051 |
| Schreiber | 1,039 |
| Scugog | 21,581 |
| Seguin | 5,280 |
| Selwyn | 18,653 |
| Severn | 14,576 |
| Shelburne | 8,994 |
| Shuniah | 3,247 |
| Sioux Lookout | 5,839 |
| Sioux Narrows-Nestor Falls | 727 |
| Smiths Falls | 9,254 |
| Smooth Rock Falls | 1,200 |
| South Algonquin | 1,055 |
| South Bruce | 5,880 |
| South Bruce Peninsula | 9,137 |
| South Dundas | 11,044 |
| South Frontenac | 20,188 |
| South Glengarry | 13,330 |
| South Huron | 10,063 |
| South River | 1,101 |
| South Stormont | 13,570 |
| Southgate | 8,716 |
| Southwest Middlesex | 5,893 |
| South-West Oxford | 7,583 |
| Southwold | 4,851 |
| Spanish | 670 |
| Springwater | 21,701 |
| St. Catharines | 136,803 |
| St. Clair | 14,659 |
| St. Joseph | 1,426 |
| St. Marys | 7,386 |
| St. Thomas | 42,840 |
| St.-Charles | 1,357 |
| Stirling-Rawdon | 5,015 |
| Stone Mills | 7,826 |
| Stratford | 33,232 |
| Strathroy-Caradoc | 23,871 |
| Strong | 1,566 |
| Sundridge | 938 |
| Tarbutt | 573 |
| Tay | 11,091 |
| Tay Valley | 5,925 |
| Tecumseh | 23,300 |
| Tehkummah | 450 |
| Temagami | 862 |
| Temiskaming Shores | 9,634 |
| Terrace Bay | 1,528 |
| Thames Centre | 13,980 |
| Thessalon | 1,260 |
| Thornloe | 92 |
| Thorold | 23,816 |
| Thunder Bay | 108,843 |
| Tillsonburg | 18,615 |
| Timmins | 41,145 |
| Tiny | 12,966 |
| Toronto | 2,794,356 |
| Trent Hills | 13,861 |
| Trent Lakes | 6,439 |
| Tudor and Cashel | 740 |
| Tweed | 6,067 |
| Tyendinaga | 4,538 |
| Uxbridge | 21,556 |
| Val Rita-Harty | 757 |
| Vaughan | 323,103 |
| Wainfleet | 6,887 |
| Warwick | 3,641 |
| Wasaga Beach | 24,862 |
| Waterloo | 121,436 |
| Wawa | 2,705 |
| Welland | 55,750 |
| Wellesley | 11,318 |
| Wellington North | 12,431 |
| West Elgin | 5,060 |
| West Grey | 13,131 |
| West Lincoln | 15,454 |
| West Nipissing | 14,583 |
| West Perth | 9,038 |
| Westport | 634 |
| Whitby | 138,501 |
| Whitchurch-Stouffville | 49,864 |
| White River | 557 |
| Whitestone | 1,075 |
| Whitewater | 7,225 |
| Wilmot | 21,429 |
| Windsor | 229,660 |
| Wollaston | 721 |
| Woodstock | 46,705 |
| Woolwich | 26,999 |
| Zorra | 8,628 |
