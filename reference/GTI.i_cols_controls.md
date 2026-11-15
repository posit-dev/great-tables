# GTI.i_cols_controls()

Choose which columns readers can sort by, search, resize, hide, move, and group the rows by,

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L928-L1155)

``` python
GTI.i_cols_controls(
    columns=None,
    *,
    sortable=None,
    searchable=None,
    resizable=None,
    hideable=None,
    reorderable=None,
    groupable=None,
    display=None,
    data_color=None,
)
```

which are only for querying, and whose colors follow the rows kept.

Where the table lets readers sort it ([`i_sorting()`](../reference/GTI.i_sorting.md#great_tables.GTI.i_sorting)), search it ([`i_search()`](../reference/GTI.i_search.md#great_tables.GTI.i_search)), and resize its columns ([`i_resizing()`](../reference/GTI.i_resizing.md#great_tables.GTI.i_resizing)), they can do so with every column, by default. This leaves some columns out: an unsortable column's label has no sort button (though the column can still be filtered, and [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view) can still sort by it), the search doesn't look in (or highlight) an unsearchable column's cells (though its own filter does), and an unresizable column's label has no handle.

Readers can't hide any column, by default. Making some hideable puts a "Columns" button in the control bar, whose panel has a checkbox for each of them, to hide it or show it again. A hidden column's cells are hidden in every row (with a spanner over only hidden columns), the search doesn't look in it, and exports leave it out, but a filter on it still keeps the rows it keeps. The stub and the row group column can't be hidden (naming them for `hideable=` does nothing), and neither can columns [`cols_hide()`](../reference/GT.cols_hide.md#great_tables.GT.cols_hide) hid, which aren't in the table at all.

Nor can readers move any column, by default. Making some reorderable lists them in the "Columns" panel too, in the order shown, where each can be dragged to another place, or moved one place at a time with its arrow buttons (or Alt+↑ and Alt+↓). A column's cells move in every row, and exports have the columns in the order shown. A column moves only among the reorderable columns next to it with the same spanners over them (and pinned to the same side, if pinned): it can't leave its spanner, or pass a column readers can't move. The author's order (as [`cols_move()`](../reference/GT.cols_move.md#great_tables.GT.cols_move) and the like set it) is the one the table is first shown in, and the one resetting the view goes back to. The stub and the row group column can't be moved (naming them for `reorderable=` does nothing).

Nor can readers group the rows by any column, by default. Making some groupable puts a "Group rows" button in the control bar, whose panel lists them (and "None"), to group the rows by one of them: each of its values gets a heading (with its text, as its first row's cell shows it, and the number of rows the search and filters keep), and the rows with it come under it, sorted as the table is. The groups are in the order of their values (ascending, or descending if the table is sorted by the column so), with the rows missing a value last, under "(Missing)". On a page, each group with rows on it has its heading. The grouping is part of the view, as [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view) can set it. A column the table can't be sorted by (one of images, say) can't be grouped by, nor can the stub (naming them for `groupable=` does nothing), and a table with row groups or summary rows can't have any groupable column.

A column can also be left out of the table but kept for querying, with `display=False`. It isn't shown (as with [`cols_hide()`](../reference/GT.cols_hide.md#great_tables.GT.cols_hide), and readers can't show it), but a filter on it ([`i_cols_filter()`](../reference/GTI.i_cols_filter.md#great_tables.GTI.i_cols_filter)) works, from the query bar, and the table can be sorted by it, as by an unsortable column (with [`i_view()`](../reference/GTI.i_view.md#great_tables.GTI.i_view), or by a view kept in the URL). Its filter goes by the text its cells would show (a facet lists its values with that text, too). The search doesn't look in it, and exports leave it out, but the code copied for the view filters and sorts by it. This is also how a column that [cols_hide()](../reference/GT.cols_hide.md#great_tables.GT.cols_hide) hid can be kept for querying. The stub and the row group column can't be left out (naming them for `display=False` is an error), and neither can every column of a table without a stub.

A column's colors from [`data_color()`](../reference/GT.data_color.md#great_tables.GT.data_color) are made from all of its rows, and stay as they are when the rows are searched or filtered, by default (`data_color="keep"`). With `data_color="recompute"`, they're made again from the rows the search and filters keep (and a linked table's selection, with [`i_link()`](../reference/GTI.i_link.md#great_tables.GTI.i_link)), as [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) would make them from those rows alone, so that its whole palette is spread over them (the table's first colors come back once every row is shown again). Sorting the rows or turning the page doesn't change them. Only colors that depend on the rows can change: those [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) made down a column (not with `direction="row"`), from a domain it found in the values (not with `domain=`, nor from an ordered categorical's levels), and without `fn=`. A missing value keeps its `na_color=`, and a cell a later style colors (with [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style), or another [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color)) keeps that style's colors.

Each call sets what it's given for the columns it's given, so that some columns can be left out of one thing, and others another; a later call for a column replaces what an earlier one set.

## Parameters

`columns: SelectExpr = None`  
The columns: a column name, a list of them, or a selector (e.g., Polars' `cs.numeric()`). With `None` (the default), every column but the stub (which can be named). The row group column can't be one of them.

`sortable: bool | None = None`  
Whether readers can sort by the columns, search them, resize them, hide them, move them, and group the rows by them. With `None` (the default), the columns are left as they are.

`searchable: bool | None = None`  
Whether readers can sort by the columns, search them, resize them, hide them, move them, and group the rows by them. With `None` (the default), the columns are left as they are.

`resizable: bool | None = None`  
Whether readers can sort by the columns, search them, resize them, hide them, move them, and group the rows by them. With `None` (the default), the columns are left as they are.

`hideable: bool | None = None`  
Whether readers can sort by the columns, search them, resize them, hide them, move them, and group the rows by them. With `None` (the default), the columns are left as they are.

`reorderable: bool | None = None`  
Whether readers can sort by the columns, search them, resize them, hide them, move them, and group the rows by them. With `None` (the default), the columns are left as they are.

`groupable: bool | None = None`  
Whether readers can sort by the columns, search them, resize them, hide them, move them, and group the rows by them. With `None` (the default), the columns are left as they are.

`display: bool | None = None`  
Whether the columns are in the table (`True`), or left out of it and kept only for querying (`False`). With `None` (the default), the columns are left as they are.

`data_color: DataColorMode | None = None`  
Whether the columns' colors from [data_color()](../reference/GT.data_color.md#great_tables.GT.data_color) stay as they are when the rows are searched or filtered (`"keep"`), or are made again from the rows kept (`"recompute"`). With `None` (the default), the columns are left as they are.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table of Ontario's municipalities whose search looks only at their names, and that can't be sorted by status.

``` python
from great_tables import GTI
from great_tables.data import towny

(
    GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
    .fmt_integer(columns="population_2021")
    .i_cols_controls(columns=["status", "population_2021"], searchable=False)
    .i_cols_controls(columns="status", sortable=False)
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

A wider table whose readers can hide any of its census years, from the "Columns" button in the control bar:

``` python
years = [f"population_{year}" for year in range(1996, 2022, 5)]

(
    GTI(towny[["name", *years]].head(10), rowname_col="name")
    .fmt_integer(columns=years)
    .i_cols_controls(columns=years, hideable=True)
)
```

|  | population_1996 | population_2001 | population_2006 | population_2011 | population_2016 | population_2021 |
|----|----|----|----|----|----|----|
| Addington Highlands | 2,429 | 2,402 | 2,512 | 2,517 | 2,318 | 2,534 |
| Adelaide Metcalfe | 3,128 | 3,149 | 3,135 | 3,028 | 2,990 | 3,011 |
| Adjala-Tosorontio | 9,359 | 10,082 | 10,695 | 10,603 | 10,975 | 10,989 |
| Admaston/Bromley | 2,837 | 2,824 | 2,716 | 2,844 | 2,935 | 2,995 |
| Ajax | 64,430 | 73,753 | 90,167 | 109,600 | 119,677 | 126,666 |
| Alberton | 1,027 | 956 | 958 | 864 | 969 | 954 |
| Alfred and Plantagenet | 8,315 | 8,593 | 8,654 | 9,196 | 9,680 | 9,949 |
| Algonquin Highlands | 1,687 | 1,827 | 1,976 | 2,186 | 2,351 | 2,588 |
| Alnwick/Haldimand | 5,528 | 5,846 | 6,435 | 6,617 | 6,869 | 7,473 |
| Amaranth | 3,450 | 3,770 | 3,845 | 3,963 | 4,079 | 4,327 |

The same years, which readers can put in another order (but not the municipality's status, which stays first):

``` python
(
    GTI(towny[["name", "status", *years]].head(10), rowname_col="name")
    .fmt_integer(columns=years)
    .i_cols_controls(columns=years, reorderable=True)
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

A table whose readers can group the municipalities by their status, from the "Group rows" button in the control bar:

``` python
(
    GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
    .fmt_integer(columns="population_2021")
    .i_cols_controls(columns="status", groupable=True)
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

A table of the municipalities' names and populations that can be filtered by their status, which it doesn't show (the filter is in the query bar, from the `<>` button in the control bar):

``` python
(
    GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
    .fmt_integer(columns="population_2021")
    .i_cols_controls(columns="status", display=False)
    .i_cols_filter(columns="status")
    .i_view(filter='status in ("single-tier")')
)
```

|  | population_2021 |
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

A table whose populations are colored from the rows the search keeps: search for "lake", and the darkest blue goes to the most populous of the municipalities named for one (Kawartha Lakes), rather than to Toronto.

``` python
(
    GTI(towny[["name", "status", "population_2021"]], rowname_col="name")
    .fmt_integer(columns="population_2021")
    .data_color(columns="population_2021", palette="Blues")
    .i_cols_controls(columns="population_2021", data_color="recompute")
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
