# GTI.i_view_state()

Keep the reader's view of the table, for when the page is opened again, and let them undo

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L1589-L1657)

``` python
GTI.i_view_state(
    url=True,
    storage=False,
    undo=True,
)
```

their changes to it.

The view is the table's filters, sort, search, page, page size, hidden columns, and the column its rows are grouped by, and the height of a body that scrolls (see [`i_scroll()`](../reference/GTI.i_scroll.md#great_tables.GTI.i_scroll)) as the reader drags it (not the rows selected, or the columns' widths). As the reader changes it, it can be kept in the page's URL (`url=`), so that reloading the page, or sharing its link, opens the table as it was; and in the browser's storage (`storage=`), so that the reader finds it as they left it when they come back to the page. The table's info panel then has a button that goes back to the view the table is first shown with (see [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view)), which is also what's kept as no view at all.

In the URL, the view is in the query string, with each part of it named after the table's ID (e.g., `?towny.filter=population_2021+%3E%3D+10000&towny.sort=-population_2021`, the filter written as [i_view()](../reference/GTI.i_view.md#great_tables.GTI.i_view) takes it as text), so that tables with different IDs keep their own views, and the page's other parameters are left alone. A link that has the view of a table opens it with that view, rather than the one in the browser's storage. A part of the view the table can't have (say, a filter on a column that has none, after the table is changed) is left out, with a warning in the browser's console, and the rest kept.

With `undo=` (the default), the control bar has buttons that undo and redo the reader's changes to the view, as do Ctrl+Z and Ctrl+Y (⌘Z and ⇧⌘Z on a Mac) in the table. Typing a search, or changing one filter, a little at a time is one change; going to another page isn't one, but is undone with the change after it. Resetting the view is a change too, so it can be undone. The changes are kept while the page is open, not with the view.

The view is kept by the table's ID, so the table needs one: set it with `GTI(id=)` (or [`with_id()`](../reference/GT.with_id.md#great_tables.GT.with_id)). Undo alone (`url=False, storage=False`) doesn't need one.

## Parameters

`url: bool = True`  
Whether to keep the view in the page's URL (the default).

`storage: bool = False`  
Whether to keep the view in the browser's storage (`localStorage`), for the page.

`undo: bool = True`  
Whether readers can undo and redo their changes to the view (the default).

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table of Ontario's municipalities whose filters, sort, search and page are kept in the page's URL as they're changed, so that a link to the page shows what the reader sees; the undo and redo buttons in the control bar step back and forth through those changes.

``` python
from great_tables import GTI
from great_tables.data import towny

(
    GTI(towny[["name", "status", "population_2021"]], rowname_col="name", id="towny")
    .fmt_integer(columns="population_2021")
    .i_cols_filter(columns=["status", "population_2021"])
    .i_view_state()
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
