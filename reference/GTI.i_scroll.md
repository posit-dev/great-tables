# GTI.i_scroll()

Make the table's body scroll, within a height.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L554-L597)

``` python
GTI.i_scroll(height)
```

The table takes up no more than `height`, and its body scrolls within it, with the column labels (and the table's header) staying in view. By default, a table grows with its rows.

With the control bar, readers can drag the foot of the body down or up (or use the arrow keys and Page Up and Page Down on it) for a taller or shorter one: from a row's height to all of the rows. Double-clicking it (or pressing Enter) puts `height` back, as resetting the view does; the height is kept with the view (see [`i_view_state()`](../reference/GTI.i_view_state.md#great_tables.GTI.i_view_state)).

## Parameters

`height: str | float | None`  
The most the table can take up: a CSS length (e.g., `"400px"` or `"60vh"`) or a number of pixels. With `None` (or `"auto"`), the table grows with its rows.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table of all its rows, in a body that scrolls.

``` python
from great_tables import GTI
from great_tables.data import towny

GTI(towny[["name", "population_2021"]]).i_pagination(False).i_scroll(400)
```

| name | population_2021 |
|----|----|
| Addington Highlands | 2534 |
| Adelaide Metcalfe | 3011 |
| Adjala-Tosorontio | 10989 |
| Admaston/Bromley | 2995 |
| Ajax | 126666 |
| Alberton | 954 |
| Alfred and Plantagenet | 9949 |
| Algonquin Highlands | 2588 |
| Alnwick/Haldimand | 7473 |
| Amaranth | 4327 |
| Amherstburg | 23524 |
| The Archipelago | 979 |
| Armour | 1459 |
| Armstrong | 1199 |
| Arnprior | 9629 |
| Arran-Elderslie | 6913 |
| Ashfield-Colborne-Wawanosh | 5884 |
| Asphodel-Norwood | 4658 |
| Assiginack | 1008 |
| Athens | 3042 |
| Atikokan | 2642 |
| Augusta | 7386 |
| Aurora | 62057 |
| Aylmer | 7699 |
| Baldwin | 579 |
| Bancroft | 4065 |
| Barrie | 147829 |
| Bayham | 7096 |
| Beckwith | 9021 |
| Belleville | 55071 |
| Billings | 753 |
| Black River-Matheson | 2572 |
| Blandford-Blenheim | 7565 |
| Blind River | 3422 |
| The Blue Mountains | 9390 |
| Bluewater | 7540 |
| Bonfield | 2146 |
| Bonnechere Valley | 3898 |
| Bracebridge | 17305 |
| Bradford West Gwillimbury | 42880 |
| Brampton | 656480 |
| Brant | 39474 |
| Brantford | 104688 |
| Brethour | 105 |
| Brighton | 12108 |
| Brock | 12567 |
| Brockton | 9784 |
| Brockville | 22116 |
| Brooke-Alvinston | 2359 |
| Bruce Mines | 582 |
| Brudenell, Lyndoch and Raglan | 1552 |
| Burk's Falls | 957 |
| Burlington | 186948 |
| Burpee and Mills | 382 |
| Caledon | 76581 |
| Callander | 3964 |
| Calvin | 557 |
| Cambridge | 138479 |
| Carleton Place | 12517 |
| Carling | 1491 |
| Carlow/Mayo | 953 |
| Casey | 341 |
| Casselman | 3960 |
| Cavan Monaghan | 10016 |
| Central Elgin | 13746 |
| Central Frontenac | 4892 |
| Central Huron | 7799 |
| Central Manitoulin | 2235 |
| Centre Hastings | 4801 |
| Centre Wellington | 31093 |
| Chamberlain | 311 |
| Champlain | 8665 |
| Chapleau | 1942 |
| Chapple | 763 |
| Charlton and Dack | 686 |
| Chatham-Kent | 103988 |
| Chatsworth | 7080 |
| Chisholm | 1312 |
| Clarence-Rockland | 26505 |
| Clarington | 101427 |
| Clearview | 14814 |
| Cobalt | 989 |
| Cobourg | 20519 |
| Cochrane | 5390 |
| Cockburn Island | 16 |
| Coleman | 517 |
| Collingwood | 24811 |
| Conmee | 798 |
| Cornwall | 47845 |
| Cramahe | 6509 |
| Dawn-Euphemia | 1968 |
| Dawson | 399 |
| Deep River | 4175 |
| Deseronto | 1747 |
| Dorion | 375 |
| Douro-Dummer | 7632 |
| Drummond/North Elmsley | 8183 |
| Dryden | 7388 |
| Dubreuilville | 576 |
| Dutton/Dunwich | 4152 |
| Dysart, Dudley, Harcourt, Guilford, Harburn, Bruton, Havelock, Eyre and Clyde | 7182 |
| Ear Falls | 924 |
| East Ferris | 4946 |
| East Garafraxa | 2794 |
| East Gwillimbury | 34637 |
| East Hawkesbury | 3418 |
| East Zorra-Tavistock | 7841 |
| Edwardsburgh/Cardinal | 7505 |
| Elizabethtown-Kitley | 9545 |
| Elliot Lake | 11372 |
| Emo | 1204 |
| Englehart | 1442 |
| Enniskillen | 2825 |
| Erin | 11981 |
| Espanola | 5185 |
| Essa | 22970 |
| Essex | 21216 |
| Evanturel | 502 |
| Faraday | 1612 |
| Fauquier-Strickland | 467 |
| Fort Erie | 32901 |
| Fort Frances | 7466 |
| French River | 2828 |
| Front of Yonge | 2595 |
| Frontenac Islands | 1930 |
| Gananoque | 5383 |
| Gauthier | 151 |
| Georgian Bay | 3441 |
| Georgian Bluffs | 11100 |
| Georgina | 47642 |
| Gillies | 441 |
| Goderich | 7881 |
| Gordon/Barrie Island | 613 |
| Gore Bay | 808 |
| Grand Valley | 3851 |
| Gravenhurst | 13157 |
| Greater Madawaska | 2864 |
| Greater Napanee | 16879 |
| Greater Sudbury | 166004 |
| Greenstone | 4309 |
| Grey Highlands | 10424 |
| Grimsby | 28883 |
| Guelph | 143740 |
| Guelph/Eramosa | 13904 |
| Haldimand | 49216 |
| Halton Hills | 62951 |
| Hamilton | 11059 |
| Hamilton | 569353 |
| Hanover | 7967 |
| Harley | 524 |
| Harris | 530 |
| Hastings Highlands | 4385 |
| Havelock-Belmont-Methuen | 5083 |
| Hawkesbury | 10194 |
| Head, Clara and Maria | 267 |
| Hearst | 4794 |
| Highlands East | 3830 |
| Hilliard | 215 |
| Hilton | 382 |
| Hilton Beach | 198 |
| Hornepayne | 968 |
| Horton | 3182 |
| Howick | 4045 |
| Hudson | 530 |
| Huntsville | 21147 |
| Huron East | 9512 |
| Huron Shores | 1860 |
| Huron-Kinloss | 7723 |
| Ignace | 1206 |
| Ingersoll | 13693 |
| Innisfil | 43326 |
| Iroquois Falls | 4418 |
| James | 348 |
| Jocelyn | 314 |
| Johnson | 749 |
| Joly | 293 |
| Kapuskasing | 8057 |
| Kawartha Lakes | 79247 |
| Kearney | 974 |
| Kenora | 14967 |
| Kerns | 330 |
| Killaloe, Hagarty and Richards | 2410 |
| Killarney | 397 |
| Kincardine | 12268 |
| King | 27333 |
| Kingston | 132485 |
| Kingsville | 22119 |
| Kirkland Lake | 7750 |
| Kitchener | 256885 |
| La Vallee | 788 |
| Laird | 1121 |
| Lake of Bays | 3759 |
| Lake of the Woods | 308 |
| Lakeshore | 40410 |
| Lambton Shores | 11876 |
| Lanark Highlands | 5737 |
| Larder Lake | 745 |
| LaSalle | 32721 |
| Latchford | 355 |
| Laurentian Hills | 2885 |
| Laurentian Valley | 9450 |
| Leamington | 29680 |
| Leeds and the Thousand Islands | 9804 |
| Limerick | 436 |
| Lincoln | 25719 |
| London | 422324 |
| Loyalist | 17943 |
| Lucan Biddulph | 5680 |
| Macdonald, Meredith and Aberdeen Additional | 1513 |
| Machar | 969 |
| Machin | 1012 |
| Madawaska Valley | 3927 |
| Madoc | 2233 |
| Magnetawan | 1753 |
| Malahide | 9308 |
| Manitouwadge | 1974 |
| Mapleton | 10839 |
| Marathon | 3138 |
| Markham | 338503 |
| Markstay-Warren | 2708 |
| Marmora and Lake | 4267 |
| Matachewan | 268 |
| Mattawa | 1881 |
| Mattawan | 153 |
| Mattice-Val Côté | 542 |
| McDougall | 2744 |
| McGarry | 579 |
| McKellar | 1419 |
| McMurrich/Monteith | 907 |
| McNab/Braeside | 7591 |
| Meaford | 11485 |
| Melancthon | 3132 |
| Merrickville-Wolford | 3135 |
| Middlesex Centre | 18928 |
| Midland | 17817 |
| Milton | 132979 |
| Minden Hills | 6971 |
| Minto | 9094 |
| Mississauga | 717961 |
| Mississippi Mills | 14740 |
| Mono | 9421 |
| Montague | 3914 |
| Moonbeam | 1157 |
| Moosonee | 1512 |
| Morley | 493 |
| Morris-Turnberry | 3590 |
| Mulmur | 3571 |
| Muskoka Lakes | 7652 |
| Nairn and Hyman | 373 |
| The Nation | 13350 |
| Neebing | 2241 |
| New Tecumseth | 43948 |
| Newbury | 440 |
| Newmarket | 87942 |
| Niagara Falls | 94415 |
| Niagara-on-the-Lake | 19088 |
| Nipigon | 1473 |
| Nipissing | 1769 |
| Norfolk | 67490 |
| North Algona Wilberforce | 3111 |
| North Bay | 52662 |
| North Dumfries | 10619 |
| North Dundas | 11304 |
| North Frontenac | 2285 |
| North Glengarry | 10144 |
| North Grenville | 17964 |
| North Huron | 5052 |
| North Kawartha | 2877 |
| North Middlesex | 6307 |
| North Perth | 15538 |
| The North Shore | 531 |
| North Stormont | 7400 |
| Northeastern Manitoulin and the Islands | 2641 |
| Northern Bruce Peninsula | 4404 |
| Norwich | 11151 |
| Oakville | 213759 |
| O'Connor | 689 |
| Oil Springs | 647 |
| Oliver Paipoonge | 6035 |
| Opasatika | 200 |
| Orangeville | 30167 |
| Orillia | 33411 |
| Oro-Medonte | 23017 |
| Oshawa | 175383 |
| Otonabee-South Monaghan | 7087 |
| Ottawa | 1017449 |
| Owen Sound | 21612 |
| Papineau-Cameron | 982 |
| Parry Sound | 6879 |
| Pelee | 230 |
| Pelham | 18192 |
| Pembroke | 14364 |
| Penetanguishene | 10077 |
| Perry | 2650 |
| Perth | 6469 |
| Perth East | 12595 |
| Perth South | 3776 |
| Petawawa | 18160 |
| Peterborough | 83651 |
| Petrolia | 6013 |
| Pickering | 99186 |
| Pickle Lake | 398 |
| Plummer Additional | 757 |
| Plympton-Wyoming | 8308 |
| Point Edward | 1930 |
| Port Colborne | 20033 |
| Port Hope | 17294 |
| Powassan | 3346 |
| Prescott | 4078 |
| Prince | 975 |
| Prince Edward | 25704 |
| Puslinch | 7944 |
| Quinte West | 46560 |
| Rainy River | 752 |
| Ramara | 10377 |
| Red Lake | 4094 |
| Red Rock | 895 |
| Renfrew | 8190 |
| Richmond Hill | 202022 |
| Rideau Lakes | 10883 |
| Russell | 19598 |
| Ryerson | 745 |
| Sables-Spanish Rivers | 3237 |
| Sarnia | 72047 |
| Saugeen Shores | 15908 |
| Sault Ste. Marie | 72051 |
| Schreiber | 1039 |
| Scugog | 21581 |
| Seguin | 5280 |
| Selwyn | 18653 |
| Severn | 14576 |
| Shelburne | 8994 |
| Shuniah | 3247 |
| Sioux Lookout | 5839 |
| Sioux Narrows-Nestor Falls | 727 |
| Smiths Falls | 9254 |
| Smooth Rock Falls | 1200 |
| South Algonquin | 1055 |
| South Bruce | 5880 |
| South Bruce Peninsula | 9137 |
| South Dundas | 11044 |
| South Frontenac | 20188 |
| South Glengarry | 13330 |
| South Huron | 10063 |
| South River | 1101 |
| South Stormont | 13570 |
| Southgate | 8716 |
| Southwest Middlesex | 5893 |
| South-West Oxford | 7583 |
| Southwold | 4851 |
| Spanish | 670 |
| Springwater | 21701 |
| St. Catharines | 136803 |
| St. Clair | 14659 |
| St. Joseph | 1426 |
| St. Marys | 7386 |
| St. Thomas | 42840 |
| St.-Charles | 1357 |
| Stirling-Rawdon | 5015 |
| Stone Mills | 7826 |
| Stratford | 33232 |
| Strathroy-Caradoc | 23871 |
| Strong | 1566 |
| Sundridge | 938 |
| Tarbutt | 573 |
| Tay | 11091 |
| Tay Valley | 5925 |
| Tecumseh | 23300 |
| Tehkummah | 450 |
| Temagami | 862 |
| Temiskaming Shores | 9634 |
| Terrace Bay | 1528 |
| Thames Centre | 13980 |
| Thessalon | 1260 |
| Thornloe | 92 |
| Thorold | 23816 |
| Thunder Bay | 108843 |
| Tillsonburg | 18615 |
| Timmins | 41145 |
| Tiny | 12966 |
| Toronto | 2794356 |
| Trent Hills | 13861 |
| Trent Lakes | 6439 |
| Tudor and Cashel | 740 |
| Tweed | 6067 |
| Tyendinaga | 4538 |
| Uxbridge | 21556 |
| Val Rita-Harty | 757 |
| Vaughan | 323103 |
| Wainfleet | 6887 |
| Warwick | 3641 |
| Wasaga Beach | 24862 |
| Waterloo | 121436 |
| Wawa | 2705 |
| Welland | 55750 |
| Wellesley | 11318 |
| Wellington North | 12431 |
| West Elgin | 5060 |
| West Grey | 13131 |
| West Lincoln | 15454 |
| West Nipissing | 14583 |
| West Perth | 9038 |
| Westport | 634 |
| Whitby | 138501 |
| Whitchurch-Stouffville | 49864 |
| White River | 557 |
| Whitestone | 1075 |
| Whitewater | 7225 |
| Wilmot | 21429 |
| Windsor | 229660 |
| Wollaston | 721 |
| Woodstock | 46705 |
| Woolwich | 26999 |
| Zorra | 8628 |
