# GTI

Create an interactive **Great Tables** object.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L54-L2204)

``` python
GTI(
    data,
    rowname_col=None,
    groupname_col=None,
    auto_align=True,
    id=None,
    locale=None,
    preset="report",
    order_by=None,
)
```

The [GTI()](../reference/GTI.md#great_tables.GTI) class makes a table that readers can work with in the browser: they can sort it by its columns, search it, page through it, resize its columns, and (if allowed) select its rows. It's a [GT](../reference/GT.md#great_tables.GT) table in every other way, so all of [GT](../reference/GT.md#great_tables.GT)'s methods (formatting, styling, spanners, summary rows, and the rest) can be used to make it. What readers can do with it is set by the methods beginning with `i_` (e.g., [`i_pagination()`](../reference/GTI.i_pagination.md#great_tables.GTI.i_pagination) or [`i_search()`](../reference/GTI.i_search.md#great_tables.GTI.i_search)), which only [GTI](../reference/GTI.md#great_tables.GTI) tables have.

A [GTI](../reference/GTI.md#great_tables.GTI) table is always rendered as interactive HTML: the table's own HTML, made as for a [GT](../reference/GT.md#great_tables.GT) table, inside a `<gt-table>` element that adds the controls. The element needs no other libraries, and the table can be read before (or without) its script running. A [GTI](../reference/GTI.md#great_tables.GTI) table can't be saved as an image or a PDF, or rendered as LaTeX; for those, use a [GT](../reference/GT.md#great_tables.GT) table.

To make a published [GT](../reference/GT.md#great_tables.GT) table browsable (sortable, searchable, filterable, and paged), with the options R gt has for that, [`opt_interactive()`](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive) may be all that's needed; it renders the table with the same engine. [GTI](../reference/GTI.md#great_tables.GTI) is for a table that's an interface, one readers work with, and [`GTI.from_gt()`](../reference/GTI.from_gt.md#great_tables.GTI.from_gt) turns a [GT](../reference/GT.md#great_tables.GT) table into one.

A table of a lazy frame (a Polars LazyFrame, a DuckDB relation or an Ibis table) is made, formatted and styled as any other, but its rows are collected only as they're shown. Shown as a widget (with [`i_as_widget()`](../reference/GTI.i_as_widget.md#great_tables.GTI.i_as_widget)) or in a Shiny app (with [`render_gt()`](../reference/shiny.render_gt.md#great_tables.shiny.render_gt)), a table of more rows than the browser is quick with keeps them in Python (see [`i_scale()`](../reference/GTI.i_scale.md#great_tables.GTI.i_scale)): each view is found with a query on the frame, and only the rows of the page shown are collected, formatted and rendered. Anywhere else (or with few rows), all the rows are collected and the table is shown as a table of them would be.

The table is made again from the rows shown, by the same methods: so what depends on every row can't be used ([data_color()](../reference/GT.data_color.md#great_tables.GT.data_color), a footnote on the body or the stub, or rows chosen by their positions, rather than by an expression or their names in the stub); and a method that looks at the rows it's given looks only at the page's (as an expression of a column's mean does, in [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style)'s rows, or [cols_align_decimal()](../reference/GT.cols_align_decimal.md#great_tables.GT.cols_align_decimal), or a nanoplot's scale). A table with summary rows or row groups has all its rows collected. In Python, its search, and its filters' "contains" and "matches" clauses, match the rows' values as text (e.g., `1000.5`), not the text of their cells (`1,000.50`), and a missing value matches nothing.

A DuckDB relation's or an Ibis table's rows have no order that's kept from one query to the next, so they're shown in the order of their values: sorted by the columns of `order_by=`, then by every other column (but those of lists, structs and objects). A Polars LazyFrame's are in its own order, unless it's given an `order_by=`. The collected rows, and their data (as the widget's `view()` gives it), are of the frame's backend: a Polars DataFrame, for a LazyFrame, and a PyArrow table, for DuckDB and Ibis.

> **Warning**
>
> [GTI()](../reference/GTI.md#great_tables.GTI) is experimental: its methods, and what they do, may change.

## Parameters

`data: Any`  
A DataFrame object, or a lazy frame: a Polars LazyFrame, a DuckDB relation or an Ibis table (whose rows are collected as they're shown: see above).

`rowname_col: str | list[str] | None = None`  
The column name in the input `data=` table to use as row labels to be placed in the table stub. A list of column names creates a hierarchical stub.

`groupname_col: str | None = None`  
The column name in the input `data=` table to use as group labels for generation of row groups.

`auto_align: bool = True`  
Optionally have column data be aligned depending on the content contained in each column of the input `data=`.

`id: str | None = None`  
By default (with `None`) the table ID will be a random, ten-letter string as generated through internal use of the `random_id()` function. A custom table ID can be used here by providing a string.

`locale: str | None = None`  
An optional locale identifier that can be set as the default locale for all functions that take a `locale` argument.

`preset: Preset = "report"`  
The settings the table starts with: `"report"` (the default) for a table to be read, with the controls above; or `"explorer"` for a look through data, as if made with [i_cols_filter()](../reference/GTI.i_cols_filter.md#great_tables.GTI.i_cols_filter) and [i_cols_profile()](../reference/GTI.i_cols_profile.md#great_tables.GTI.i_cols_profile) (every column filtered and profiled, as its kind suggests), `i_cols_controls(hideable=True, reorderable=True)` (every column can be hidden and moved), `i_display(compact=True, wrap=False, monospace=True)` (compact rows of one line each, in a monospaced font), `i_export("csv")` and [i_inspect()](../reference/GTI.i_inspect.md#great_tables.GTI.i_inspect) (row numbers, dtypes under the labels, what the data is and its number of rows and columns, and missing values tinted). The stub is left out of these, as those methods leave it out. The `i_` methods change a preset as they change any table: each sets all of its feature's settings (so `i_display(wrap=True)` on an explorer lets its text wrap, but also makes its rows less compact and puts them in the table's own font, unless it's given `compact=True` and `monospace=True` too), and the `i_cols_` methods set those of the columns they're given.

`order_by: str | list[str] | None = None`  
For a lazy frame, the columns its rows are in the order of (and numbered by): the rows sort by them first, then by the frame's other columns (see above). A column of unique values (an ID) is best, which leaves them nothing to sort. Not for a DataFrame (which can be sorted first, for the table).

## Returns

`GTI`  
A GTI object is returned.

## Examples

Out of the box, a [GTI](../reference/GTI.md#great_tables.GTI) table can be sorted by its columns (with the arrows under their labels), searched, and paged through, ten rows at a time, and its columns can be resized.

``` python
from great_tables import GTI
from great_tables.data import towny

towny_mini = towny[["name", "status", "csd_type", "population_2021"]]

GTI(towny_mini, rowname_col="name").fmt_integer(columns="population_2021")
```

|  | status | csd_type | population_2021 |
|----|----|----|----|
| Addington Highlands | lower-tier | township | 2,534 |
| Adelaide Metcalfe | lower-tier | township | 3,011 |
| Adjala-Tosorontio | lower-tier | township | 10,989 |
| Admaston/Bromley | lower-tier | township | 2,995 |
| Ajax | lower-tier | town | 126,666 |
| Alberton | single-tier | township | 954 |
| Alfred and Plantagenet | lower-tier | township | 9,949 |
| Algonquin Highlands | lower-tier | township | 2,588 |
| Alnwick/Haldimand | lower-tier | township | 7,473 |
| Amaranth | lower-tier | township | 4,327 |
| Amherstburg | lower-tier | town | 23,524 |
| The Archipelago | single-tier | township | 979 |
| Armour | single-tier | township | 1,459 |
| Armstrong | single-tier | township | 1,199 |
| Arnprior | lower-tier | town | 9,629 |
| Arran-Elderslie | lower-tier | municipality | 6,913 |
| Ashfield-Colborne-Wawanosh | lower-tier | township | 5,884 |
| Asphodel-Norwood | lower-tier | township | 4,658 |
| Assiginack | single-tier | township | 1,008 |
| Athens | lower-tier | township | 3,042 |
| Atikokan | single-tier | town | 2,642 |
| Augusta | lower-tier | township | 7,386 |
| Aurora | lower-tier | town | 62,057 |
| Aylmer | lower-tier | town | 7,699 |
| Baldwin | single-tier | township | 579 |
| Bancroft | lower-tier | town | 4,065 |
| Barrie | single-tier | city | 147,829 |
| Bayham | lower-tier | municipality | 7,096 |
| Beckwith | lower-tier | township | 9,021 |
| Belleville | single-tier | city | 55,071 |
| Billings | single-tier | township | 753 |
| Black River-Matheson | single-tier | township | 2,572 |
| Blandford-Blenheim | lower-tier | township | 7,565 |
| Blind River | single-tier | town | 3,422 |
| The Blue Mountains | lower-tier | town | 9,390 |
| Bluewater | lower-tier | municipality | 7,540 |
| Bonfield | single-tier | township | 2,146 |
| Bonnechere Valley | lower-tier | township | 3,898 |
| Bracebridge | lower-tier | town | 17,305 |
| Bradford West Gwillimbury | lower-tier | town | 42,880 |
| Brampton | lower-tier | city | 656,480 |
| Brant | single-tier | city | 39,474 |
| Brantford | single-tier | city | 104,688 |
| Brethour | single-tier | township | 105 |
| Brighton | lower-tier | municipality | 12,108 |
| Brock | lower-tier | township | 12,567 |
| Brockton | lower-tier | municipality | 9,784 |
| Brockville | single-tier | city | 22,116 |
| Brooke-Alvinston | lower-tier | municipality | 2,359 |
| Bruce Mines | single-tier | town | 582 |
| Brudenell, Lyndoch and Raglan | lower-tier | township | 1,552 |
| Burk's Falls | single-tier | village | 957 |
| Burlington | lower-tier | city | 186,948 |
| Burpee and Mills | single-tier | township | 382 |
| Caledon | lower-tier | town | 76,581 |
| Callander | single-tier | municipality | 3,964 |
| Calvin | single-tier | municipality | 557 |
| Cambridge | lower-tier | city | 138,479 |
| Carleton Place | lower-tier | town | 12,517 |
| Carling | single-tier | township | 1,491 |
| Carlow/Mayo | lower-tier | township | 953 |
| Casey | single-tier | township | 341 |
| Casselman | lower-tier | village | 3,960 |
| Cavan Monaghan | lower-tier | township | 10,016 |
| Central Elgin | lower-tier | municipality | 13,746 |
| Central Frontenac | lower-tier | township | 4,892 |
| Central Huron | lower-tier | municipality | 7,799 |
| Central Manitoulin | single-tier | municipality | 2,235 |
| Centre Hastings | lower-tier | municipality | 4,801 |
| Centre Wellington | lower-tier | township | 31,093 |
| Chamberlain | single-tier | township | 311 |
| Champlain | lower-tier | township | 8,665 |
| Chapleau | single-tier | township | 1,942 |
| Chapple | single-tier | township | 763 |
| Charlton and Dack | single-tier | municipality | 686 |
| Chatham-Kent | single-tier | municipality | 103,988 |
| Chatsworth | lower-tier | township | 7,080 |
| Chisholm | single-tier | township | 1,312 |
| Clarence-Rockland | lower-tier | city | 26,505 |
| Clarington | lower-tier | municipality | 101,427 |
| Clearview | lower-tier | township | 14,814 |
| Cobalt | single-tier | town | 989 |
| Cobourg | lower-tier | town | 20,519 |
| Cochrane | single-tier | town | 5,390 |
| Cockburn Island | single-tier | township | 16 |
| Coleman | single-tier | township | 517 |
| Collingwood | lower-tier | town | 24,811 |
| Conmee | single-tier | township | 798 |
| Cornwall | single-tier | city | 47,845 |
| Cramahe | lower-tier | township | 6,509 |
| Dawn-Euphemia | lower-tier | township | 1,968 |
| Dawson | single-tier | township | 399 |
| Deep River | lower-tier | town | 4,175 |
| Deseronto | lower-tier | town | 1,747 |
| Dorion | single-tier | township | 375 |
| Douro-Dummer | lower-tier | township | 7,632 |
| Drummond/North Elmsley | lower-tier | township | 8,183 |
| Dryden | single-tier | city | 7,388 |
| Dubreuilville | single-tier | township | 576 |
| Dutton/Dunwich | lower-tier | municipality | 4,152 |
| Dysart, Dudley, Harcourt, Guilford, Harburn, Bruton, Havelock, Eyre and Clyde | lower-tier | municipality | 7,182 |
| Ear Falls | single-tier | township | 924 |
| East Ferris | single-tier | municipality | 4,946 |
| East Garafraxa | lower-tier | township | 2,794 |
| East Gwillimbury | lower-tier | town | 34,637 |
| East Hawkesbury | lower-tier | township | 3,418 |
| East Zorra-Tavistock | lower-tier | township | 7,841 |
| Edwardsburgh/Cardinal | lower-tier | township | 7,505 |
| Elizabethtown-Kitley | lower-tier | township | 9,545 |
| Elliot Lake | single-tier | city | 11,372 |
| Emo | single-tier | township | 1,204 |
| Englehart | single-tier | town | 1,442 |
| Enniskillen | lower-tier | township | 2,825 |
| Erin | lower-tier | town | 11,981 |
| Espanola | single-tier | town | 5,185 |
| Essa | lower-tier | township | 22,970 |
| Essex | lower-tier | town | 21,216 |
| Evanturel | single-tier | township | 502 |
| Faraday | lower-tier | township | 1,612 |
| Fauquier-Strickland | single-tier | township | 467 |
| Fort Erie | lower-tier | town | 32,901 |
| Fort Frances | single-tier | town | 7,466 |
| French River | single-tier | municipality | 2,828 |
| Front of Yonge | lower-tier | township | 2,595 |
| Frontenac Islands | lower-tier | township | 1,930 |
| Gananoque | single-tier | town | 5,383 |
| Gauthier | single-tier | township | 151 |
| Georgian Bay | lower-tier | township | 3,441 |
| Georgian Bluffs | lower-tier | township | 11,100 |
| Georgina | lower-tier | town | 47,642 |
| Gillies | single-tier | township | 441 |
| Goderich | lower-tier | town | 7,881 |
| Gordon/Barrie Island | single-tier | municipality | 613 |
| Gore Bay | single-tier | town | 808 |
| Grand Valley | lower-tier | town | 3,851 |
| Gravenhurst | lower-tier | town | 13,157 |
| Greater Madawaska | lower-tier | township | 2,864 |
| Greater Napanee | lower-tier | town | 16,879 |
| Greater Sudbury | single-tier | city | 166,004 |
| Greenstone | single-tier | municipality | 4,309 |
| Grey Highlands | lower-tier | municipality | 10,424 |
| Grimsby | lower-tier | town | 28,883 |
| Guelph | single-tier | city | 143,740 |
| Guelph/Eramosa | lower-tier | township | 13,904 |
| Haldimand | single-tier | city | 49,216 |
| Halton Hills | lower-tier | town | 62,951 |
| Hamilton | lower-tier | township | 11,059 |
| Hamilton | single-tier | city | 569,353 |
| Hanover | lower-tier | town | 7,967 |
| Harley | single-tier | township | 524 |
| Harris | single-tier | township | 530 |
| Hastings Highlands | lower-tier | municipality | 4,385 |
| Havelock-Belmont-Methuen | lower-tier | township | 5,083 |
| Hawkesbury | lower-tier | town | 10,194 |
| Head, Clara and Maria | lower-tier | township | 267 |
| Hearst | single-tier | town | 4,794 |
| Highlands East | lower-tier | municipality | 3,830 |
| Hilliard | single-tier | township | 215 |
| Hilton | single-tier | township | 382 |
| Hilton Beach | single-tier | village | 198 |
| Hornepayne | single-tier | township | 968 |
| Horton | lower-tier | township | 3,182 |
| Howick | lower-tier | township | 4,045 |
| Hudson | single-tier | township | 530 |
| Huntsville | lower-tier | town | 21,147 |
| Huron East | lower-tier | municipality | 9,512 |
| Huron Shores | single-tier | municipality | 1,860 |
| Huron-Kinloss | lower-tier | township | 7,723 |
| Ignace | single-tier | township | 1,206 |
| Ingersoll | lower-tier | town | 13,693 |
| Innisfil | lower-tier | town | 43,326 |
| Iroquois Falls | single-tier | town | 4,418 |
| James | single-tier | township | 348 |
| Jocelyn | single-tier | township | 314 |
| Johnson | single-tier | township | 749 |
| Joly | single-tier | township | 293 |
| Kapuskasing | single-tier | town | 8,057 |
| Kawartha Lakes | single-tier | city | 79,247 |
| Kearney | single-tier | town | 974 |
| Kenora | single-tier | city | 14,967 |
| Kerns | single-tier | township | 330 |
| Killaloe, Hagarty and Richards | lower-tier | township | 2,410 |
| Killarney | single-tier | municipality | 397 |
| Kincardine | lower-tier | municipality | 12,268 |
| King | lower-tier | township | 27,333 |
| Kingston | single-tier | city | 132,485 |
| Kingsville | lower-tier | town | 22,119 |
| Kirkland Lake | single-tier | town | 7,750 |
| Kitchener | lower-tier | city | 256,885 |
| La Vallee | single-tier | township | 788 |
| Laird | single-tier | township | 1,121 |
| Lake of Bays | lower-tier | township | 3,759 |
| Lake of the Woods | single-tier | township | 308 |
| Lakeshore | lower-tier | town | 40,410 |
| Lambton Shores | lower-tier | municipality | 11,876 |
| Lanark Highlands | lower-tier | township | 5,737 |
| Larder Lake | single-tier | township | 745 |
| LaSalle | lower-tier | town | 32,721 |
| Latchford | single-tier | town | 355 |
| Laurentian Hills | lower-tier | town | 2,885 |
| Laurentian Valley | lower-tier | township | 9,450 |
| Leamington | lower-tier | municipality | 29,680 |
| Leeds and the Thousand Islands | lower-tier | township | 9,804 |
| Limerick | lower-tier | township | 436 |
| Lincoln | lower-tier | town | 25,719 |
| London | single-tier | city | 422,324 |
| Loyalist | lower-tier | township | 17,943 |
| Lucan Biddulph | lower-tier | township | 5,680 |
| Macdonald, Meredith and Aberdeen Additional | single-tier | township | 1,513 |
| Machar | single-tier | township | 969 |
| Machin | single-tier | municipality | 1,012 |
| Madawaska Valley | lower-tier | township | 3,927 |
| Madoc | lower-tier | township | 2,233 |
| Magnetawan | single-tier | municipality | 1,753 |
| Malahide | lower-tier | township | 9,308 |
| Manitouwadge | single-tier | township | 1,974 |
| Mapleton | lower-tier | township | 10,839 |
| Marathon | single-tier | town | 3,138 |
| Markham | lower-tier | city | 338,503 |
| Markstay-Warren | single-tier | municipality | 2,708 |
| Marmora and Lake | lower-tier | municipality | 4,267 |
| Matachewan | single-tier | township | 268 |
| Mattawa | single-tier | town | 1,881 |
| Mattawan | single-tier | township | 153 |
| Mattice-Val Côté | single-tier | township | 542 |
| McDougall | single-tier | municipality | 2,744 |
| McGarry | single-tier | township | 579 |
| McKellar | single-tier | township | 1,419 |
| McMurrich/Monteith | single-tier | township | 907 |
| McNab/Braeside | lower-tier | township | 7,591 |
| Meaford | lower-tier | municipality | 11,485 |
| Melancthon | lower-tier | township | 3,132 |
| Merrickville-Wolford | lower-tier | village | 3,135 |
| Middlesex Centre | lower-tier | municipality | 18,928 |
| Midland | lower-tier | town | 17,817 |
| Milton | lower-tier | town | 132,979 |
| Minden Hills | lower-tier | township | 6,971 |
| Minto | lower-tier | town | 9,094 |
| Mississauga | lower-tier | city | 717,961 |
| Mississippi Mills | lower-tier | town | 14,740 |
| Mono | lower-tier | town | 9,421 |
| Montague | lower-tier | township | 3,914 |
| Moonbeam | single-tier | township | 1,157 |
| Moosonee | single-tier | town | 1,512 |
| Morley | single-tier | township | 493 |
| Morris-Turnberry | lower-tier | municipality | 3,590 |
| Mulmur | lower-tier | township | 3,571 |
| Muskoka Lakes | lower-tier | township | 7,652 |
| Nairn and Hyman | single-tier | township | 373 |
| The Nation | lower-tier | municipality | 13,350 |
| Neebing | single-tier | municipality | 2,241 |
| New Tecumseth | lower-tier | town | 43,948 |
| Newbury | lower-tier | village | 440 |
| Newmarket | lower-tier | town | 87,942 |
| Niagara Falls | lower-tier | city | 94,415 |
| Niagara-on-the-Lake | lower-tier | town | 19,088 |
| Nipigon | single-tier | township | 1,473 |
| Nipissing | single-tier | township | 1,769 |
| Norfolk | single-tier | city | 67,490 |
| North Algona Wilberforce | lower-tier | township | 3,111 |
| North Bay | single-tier | city | 52,662 |
| North Dumfries | lower-tier | township | 10,619 |
| North Dundas | lower-tier | township | 11,304 |
| North Frontenac | lower-tier | township | 2,285 |
| North Glengarry | lower-tier | township | 10,144 |
| North Grenville | lower-tier | municipality | 17,964 |
| North Huron | lower-tier | township | 5,052 |
| North Kawartha | lower-tier | township | 2,877 |
| North Middlesex | lower-tier | municipality | 6,307 |
| North Perth | lower-tier | municipality | 15,538 |
| The North Shore | single-tier | township | 531 |
| North Stormont | lower-tier | township | 7,400 |
| Northeastern Manitoulin and the Islands | single-tier | municipality | 2,641 |
| Northern Bruce Peninsula | lower-tier | municipality | 4,404 |
| Norwich | lower-tier | township | 11,151 |
| Oakville | lower-tier | town | 213,759 |
| O'Connor | single-tier | township | 689 |
| Oil Springs | lower-tier | village | 647 |
| Oliver Paipoonge | single-tier | municipality | 6,035 |
| Opasatika | single-tier | township | 200 |
| Orangeville | lower-tier | town | 30,167 |
| Orillia | single-tier | city | 33,411 |
| Oro-Medonte | lower-tier | township | 23,017 |
| Oshawa | lower-tier | city | 175,383 |
| Otonabee-South Monaghan | lower-tier | township | 7,087 |
| Ottawa | single-tier | city | 1,017,449 |
| Owen Sound | lower-tier | city | 21,612 |
| Papineau-Cameron | single-tier | township | 982 |
| Parry Sound | single-tier | town | 6,879 |
| Pelee | single-tier | township | 230 |
| Pelham | lower-tier | town | 18,192 |
| Pembroke | single-tier | city | 14,364 |
| Penetanguishene | lower-tier | town | 10,077 |
| Perry | single-tier | township | 2,650 |
| Perth | lower-tier | town | 6,469 |
| Perth East | lower-tier | township | 12,595 |
| Perth South | lower-tier | township | 3,776 |
| Petawawa | lower-tier | town | 18,160 |
| Peterborough | single-tier | city | 83,651 |
| Petrolia | lower-tier | town | 6,013 |
| Pickering | lower-tier | city | 99,186 |
| Pickle Lake | single-tier | township | 398 |
| Plummer Additional | single-tier | township | 757 |
| Plympton-Wyoming | lower-tier | town | 8,308 |
| Point Edward | lower-tier | village | 1,930 |
| Port Colborne | lower-tier | city | 20,033 |
| Port Hope | lower-tier | municipality | 17,294 |
| Powassan | single-tier | municipality | 3,346 |
| Prescott | single-tier | town | 4,078 |
| Prince | single-tier | township | 975 |
| Prince Edward | single-tier | city | 25,704 |
| Puslinch | lower-tier | township | 7,944 |
| Quinte West | single-tier | city | 46,560 |
| Rainy River | single-tier | town | 752 |
| Ramara | lower-tier | township | 10,377 |
| Red Lake | single-tier | municipality | 4,094 |
| Red Rock | single-tier | township | 895 |
| Renfrew | lower-tier | town | 8,190 |
| Richmond Hill | lower-tier | city | 202,022 |
| Rideau Lakes | lower-tier | township | 10,883 |
| Russell | lower-tier | township | 19,598 |
| Ryerson | single-tier | township | 745 |
| Sables-Spanish Rivers | single-tier | township | 3,237 |
| Sarnia | lower-tier | city | 72,047 |
| Saugeen Shores | lower-tier | town | 15,908 |
| Sault Ste. Marie | single-tier | city | 72,051 |
| Schreiber | single-tier | township | 1,039 |
| Scugog | lower-tier | township | 21,581 |
| Seguin | single-tier | township | 5,280 |
| Selwyn | lower-tier | township | 18,653 |
| Severn | lower-tier | township | 14,576 |
| Shelburne | lower-tier | town | 8,994 |
| Shuniah | single-tier | municipality | 3,247 |
| Sioux Lookout | single-tier | municipality | 5,839 |
| Sioux Narrows-Nestor Falls | single-tier | township | 727 |
| Smiths Falls | single-tier | town | 9,254 |
| Smooth Rock Falls | single-tier | town | 1,200 |
| South Algonquin | single-tier | township | 1,055 |
| South Bruce | lower-tier | municipality | 5,880 |
| South Bruce Peninsula | lower-tier | town | 9,137 |
| South Dundas | lower-tier | municipality | 11,044 |
| South Frontenac | lower-tier | township | 20,188 |
| South Glengarry | lower-tier | township | 13,330 |
| South Huron | lower-tier | municipality | 10,063 |
| South River | single-tier | village | 1,101 |
| South Stormont | lower-tier | township | 13,570 |
| Southgate | lower-tier | township | 8,716 |
| Southwest Middlesex | lower-tier | municipality | 5,893 |
| South-West Oxford | lower-tier | township | 7,583 |
| Southwold | lower-tier | township | 4,851 |
| Spanish | single-tier | town | 670 |
| Springwater | lower-tier | township | 21,701 |
| St. Catharines | lower-tier | city | 136,803 |
| St. Clair | lower-tier | township | 14,659 |
| St. Joseph | single-tier | township | 1,426 |
| St. Marys | single-tier | town | 7,386 |
| St. Thomas | single-tier | city | 42,840 |
| St.-Charles | single-tier | municipality | 1,357 |
| Stirling-Rawdon | lower-tier | township | 5,015 |
| Stone Mills | lower-tier | township | 7,826 |
| Stratford | single-tier | city | 33,232 |
| Strathroy-Caradoc | lower-tier | municipality | 23,871 |
| Strong | single-tier | township | 1,566 |
| Sundridge | single-tier | village | 938 |
| Tarbutt | single-tier | township | 573 |
| Tay | lower-tier | township | 11,091 |
| Tay Valley | lower-tier | township | 5,925 |
| Tecumseh | lower-tier | town | 23,300 |
| Tehkummah | single-tier | township | 450 |
| Temagami | single-tier | municipality | 862 |
| Temiskaming Shores | single-tier | city | 9,634 |
| Terrace Bay | single-tier | township | 1,528 |
| Thames Centre | lower-tier | municipality | 13,980 |
| Thessalon | single-tier | town | 1,260 |
| Thornloe | single-tier | village | 92 |
| Thorold | lower-tier | city | 23,816 |
| Thunder Bay | single-tier | city | 108,843 |
| Tillsonburg | lower-tier | town | 18,615 |
| Timmins | single-tier | city | 41,145 |
| Tiny | lower-tier | township | 12,966 |
| Toronto | single-tier | city | 2,794,356 |
| Trent Hills | lower-tier | municipality | 13,861 |
| Trent Lakes | lower-tier | municipality | 6,439 |
| Tudor and Cashel | lower-tier | township | 740 |
| Tweed | lower-tier | municipality | 6,067 |
| Tyendinaga | lower-tier | township | 4,538 |
| Uxbridge | lower-tier | township | 21,556 |
| Val Rita-Harty | single-tier | township | 757 |
| Vaughan | lower-tier | city | 323,103 |
| Wainfleet | lower-tier | township | 6,887 |
| Warwick | lower-tier | township | 3,641 |
| Wasaga Beach | lower-tier | town | 24,862 |
| Waterloo | lower-tier | city | 121,436 |
| Wawa | single-tier | municipality | 2,705 |
| Welland | lower-tier | city | 55,750 |
| Wellesley | lower-tier | township | 11,318 |
| Wellington North | lower-tier | township | 12,431 |
| West Elgin | lower-tier | municipality | 5,060 |
| West Grey | lower-tier | municipality | 13,131 |
| West Lincoln | lower-tier | township | 15,454 |
| West Nipissing | single-tier | municipality | 14,583 |
| West Perth | lower-tier | municipality | 9,038 |
| Westport | lower-tier | village | 634 |
| Whitby | lower-tier | town | 138,501 |
| Whitchurch-Stouffville | lower-tier | town | 49,864 |
| White River | single-tier | township | 557 |
| Whitestone | single-tier | municipality | 1,075 |
| Whitewater | lower-tier | township | 7,225 |
| Wilmot | lower-tier | township | 21,429 |
| Windsor | single-tier | city | 229,660 |
| Wollaston | lower-tier | township | 721 |
| Woodstock | lower-tier | city | 46,705 |
| Woolwich | lower-tier | township | 26,999 |
| Zorra | lower-tier | township | 8,628 |

The `i_` methods change what readers can do. Here, they get 25 rows to a page and can select rows, and the table is compact.

``` python
(
    GTI(towny_mini, rowname_col="name")
    .fmt_integer(columns="population_2021")
    .i_pagination(page_size=25)
    .i_selection("multiple")
    .i_display(compact=True)
)
```

|  | status | csd_type | population_2021 |
|----|----|----|----|
| Addington Highlands | lower-tier | township | 2,534 |
| Adelaide Metcalfe | lower-tier | township | 3,011 |
| Adjala-Tosorontio | lower-tier | township | 10,989 |
| Admaston/Bromley | lower-tier | township | 2,995 |
| Ajax | lower-tier | town | 126,666 |
| Alberton | single-tier | township | 954 |
| Alfred and Plantagenet | lower-tier | township | 9,949 |
| Algonquin Highlands | lower-tier | township | 2,588 |
| Alnwick/Haldimand | lower-tier | township | 7,473 |
| Amaranth | lower-tier | township | 4,327 |
| Amherstburg | lower-tier | town | 23,524 |
| The Archipelago | single-tier | township | 979 |
| Armour | single-tier | township | 1,459 |
| Armstrong | single-tier | township | 1,199 |
| Arnprior | lower-tier | town | 9,629 |
| Arran-Elderslie | lower-tier | municipality | 6,913 |
| Ashfield-Colborne-Wawanosh | lower-tier | township | 5,884 |
| Asphodel-Norwood | lower-tier | township | 4,658 |
| Assiginack | single-tier | township | 1,008 |
| Athens | lower-tier | township | 3,042 |
| Atikokan | single-tier | town | 2,642 |
| Augusta | lower-tier | township | 7,386 |
| Aurora | lower-tier | town | 62,057 |
| Aylmer | lower-tier | town | 7,699 |
| Baldwin | single-tier | township | 579 |
| Bancroft | lower-tier | town | 4,065 |
| Barrie | single-tier | city | 147,829 |
| Bayham | lower-tier | municipality | 7,096 |
| Beckwith | lower-tier | township | 9,021 |
| Belleville | single-tier | city | 55,071 |
| Billings | single-tier | township | 753 |
| Black River-Matheson | single-tier | township | 2,572 |
| Blandford-Blenheim | lower-tier | township | 7,565 |
| Blind River | single-tier | town | 3,422 |
| The Blue Mountains | lower-tier | town | 9,390 |
| Bluewater | lower-tier | municipality | 7,540 |
| Bonfield | single-tier | township | 2,146 |
| Bonnechere Valley | lower-tier | township | 3,898 |
| Bracebridge | lower-tier | town | 17,305 |
| Bradford West Gwillimbury | lower-tier | town | 42,880 |
| Brampton | lower-tier | city | 656,480 |
| Brant | single-tier | city | 39,474 |
| Brantford | single-tier | city | 104,688 |
| Brethour | single-tier | township | 105 |
| Brighton | lower-tier | municipality | 12,108 |
| Brock | lower-tier | township | 12,567 |
| Brockton | lower-tier | municipality | 9,784 |
| Brockville | single-tier | city | 22,116 |
| Brooke-Alvinston | lower-tier | municipality | 2,359 |
| Bruce Mines | single-tier | town | 582 |
| Brudenell, Lyndoch and Raglan | lower-tier | township | 1,552 |
| Burk's Falls | single-tier | village | 957 |
| Burlington | lower-tier | city | 186,948 |
| Burpee and Mills | single-tier | township | 382 |
| Caledon | lower-tier | town | 76,581 |
| Callander | single-tier | municipality | 3,964 |
| Calvin | single-tier | municipality | 557 |
| Cambridge | lower-tier | city | 138,479 |
| Carleton Place | lower-tier | town | 12,517 |
| Carling | single-tier | township | 1,491 |
| Carlow/Mayo | lower-tier | township | 953 |
| Casey | single-tier | township | 341 |
| Casselman | lower-tier | village | 3,960 |
| Cavan Monaghan | lower-tier | township | 10,016 |
| Central Elgin | lower-tier | municipality | 13,746 |
| Central Frontenac | lower-tier | township | 4,892 |
| Central Huron | lower-tier | municipality | 7,799 |
| Central Manitoulin | single-tier | municipality | 2,235 |
| Centre Hastings | lower-tier | municipality | 4,801 |
| Centre Wellington | lower-tier | township | 31,093 |
| Chamberlain | single-tier | township | 311 |
| Champlain | lower-tier | township | 8,665 |
| Chapleau | single-tier | township | 1,942 |
| Chapple | single-tier | township | 763 |
| Charlton and Dack | single-tier | municipality | 686 |
| Chatham-Kent | single-tier | municipality | 103,988 |
| Chatsworth | lower-tier | township | 7,080 |
| Chisholm | single-tier | township | 1,312 |
| Clarence-Rockland | lower-tier | city | 26,505 |
| Clarington | lower-tier | municipality | 101,427 |
| Clearview | lower-tier | township | 14,814 |
| Cobalt | single-tier | town | 989 |
| Cobourg | lower-tier | town | 20,519 |
| Cochrane | single-tier | town | 5,390 |
| Cockburn Island | single-tier | township | 16 |
| Coleman | single-tier | township | 517 |
| Collingwood | lower-tier | town | 24,811 |
| Conmee | single-tier | township | 798 |
| Cornwall | single-tier | city | 47,845 |
| Cramahe | lower-tier | township | 6,509 |
| Dawn-Euphemia | lower-tier | township | 1,968 |
| Dawson | single-tier | township | 399 |
| Deep River | lower-tier | town | 4,175 |
| Deseronto | lower-tier | town | 1,747 |
| Dorion | single-tier | township | 375 |
| Douro-Dummer | lower-tier | township | 7,632 |
| Drummond/North Elmsley | lower-tier | township | 8,183 |
| Dryden | single-tier | city | 7,388 |
| Dubreuilville | single-tier | township | 576 |
| Dutton/Dunwich | lower-tier | municipality | 4,152 |
| Dysart, Dudley, Harcourt, Guilford, Harburn, Bruton, Havelock, Eyre and Clyde | lower-tier | municipality | 7,182 |
| Ear Falls | single-tier | township | 924 |
| East Ferris | single-tier | municipality | 4,946 |
| East Garafraxa | lower-tier | township | 2,794 |
| East Gwillimbury | lower-tier | town | 34,637 |
| East Hawkesbury | lower-tier | township | 3,418 |
| East Zorra-Tavistock | lower-tier | township | 7,841 |
| Edwardsburgh/Cardinal | lower-tier | township | 7,505 |
| Elizabethtown-Kitley | lower-tier | township | 9,545 |
| Elliot Lake | single-tier | city | 11,372 |
| Emo | single-tier | township | 1,204 |
| Englehart | single-tier | town | 1,442 |
| Enniskillen | lower-tier | township | 2,825 |
| Erin | lower-tier | town | 11,981 |
| Espanola | single-tier | town | 5,185 |
| Essa | lower-tier | township | 22,970 |
| Essex | lower-tier | town | 21,216 |
| Evanturel | single-tier | township | 502 |
| Faraday | lower-tier | township | 1,612 |
| Fauquier-Strickland | single-tier | township | 467 |
| Fort Erie | lower-tier | town | 32,901 |
| Fort Frances | single-tier | town | 7,466 |
| French River | single-tier | municipality | 2,828 |
| Front of Yonge | lower-tier | township | 2,595 |
| Frontenac Islands | lower-tier | township | 1,930 |
| Gananoque | single-tier | town | 5,383 |
| Gauthier | single-tier | township | 151 |
| Georgian Bay | lower-tier | township | 3,441 |
| Georgian Bluffs | lower-tier | township | 11,100 |
| Georgina | lower-tier | town | 47,642 |
| Gillies | single-tier | township | 441 |
| Goderich | lower-tier | town | 7,881 |
| Gordon/Barrie Island | single-tier | municipality | 613 |
| Gore Bay | single-tier | town | 808 |
| Grand Valley | lower-tier | town | 3,851 |
| Gravenhurst | lower-tier | town | 13,157 |
| Greater Madawaska | lower-tier | township | 2,864 |
| Greater Napanee | lower-tier | town | 16,879 |
| Greater Sudbury | single-tier | city | 166,004 |
| Greenstone | single-tier | municipality | 4,309 |
| Grey Highlands | lower-tier | municipality | 10,424 |
| Grimsby | lower-tier | town | 28,883 |
| Guelph | single-tier | city | 143,740 |
| Guelph/Eramosa | lower-tier | township | 13,904 |
| Haldimand | single-tier | city | 49,216 |
| Halton Hills | lower-tier | town | 62,951 |
| Hamilton | lower-tier | township | 11,059 |
| Hamilton | single-tier | city | 569,353 |
| Hanover | lower-tier | town | 7,967 |
| Harley | single-tier | township | 524 |
| Harris | single-tier | township | 530 |
| Hastings Highlands | lower-tier | municipality | 4,385 |
| Havelock-Belmont-Methuen | lower-tier | township | 5,083 |
| Hawkesbury | lower-tier | town | 10,194 |
| Head, Clara and Maria | lower-tier | township | 267 |
| Hearst | single-tier | town | 4,794 |
| Highlands East | lower-tier | municipality | 3,830 |
| Hilliard | single-tier | township | 215 |
| Hilton | single-tier | township | 382 |
| Hilton Beach | single-tier | village | 198 |
| Hornepayne | single-tier | township | 968 |
| Horton | lower-tier | township | 3,182 |
| Howick | lower-tier | township | 4,045 |
| Hudson | single-tier | township | 530 |
| Huntsville | lower-tier | town | 21,147 |
| Huron East | lower-tier | municipality | 9,512 |
| Huron Shores | single-tier | municipality | 1,860 |
| Huron-Kinloss | lower-tier | township | 7,723 |
| Ignace | single-tier | township | 1,206 |
| Ingersoll | lower-tier | town | 13,693 |
| Innisfil | lower-tier | town | 43,326 |
| Iroquois Falls | single-tier | town | 4,418 |
| James | single-tier | township | 348 |
| Jocelyn | single-tier | township | 314 |
| Johnson | single-tier | township | 749 |
| Joly | single-tier | township | 293 |
| Kapuskasing | single-tier | town | 8,057 |
| Kawartha Lakes | single-tier | city | 79,247 |
| Kearney | single-tier | town | 974 |
| Kenora | single-tier | city | 14,967 |
| Kerns | single-tier | township | 330 |
| Killaloe, Hagarty and Richards | lower-tier | township | 2,410 |
| Killarney | single-tier | municipality | 397 |
| Kincardine | lower-tier | municipality | 12,268 |
| King | lower-tier | township | 27,333 |
| Kingston | single-tier | city | 132,485 |
| Kingsville | lower-tier | town | 22,119 |
| Kirkland Lake | single-tier | town | 7,750 |
| Kitchener | lower-tier | city | 256,885 |
| La Vallee | single-tier | township | 788 |
| Laird | single-tier | township | 1,121 |
| Lake of Bays | lower-tier | township | 3,759 |
| Lake of the Woods | single-tier | township | 308 |
| Lakeshore | lower-tier | town | 40,410 |
| Lambton Shores | lower-tier | municipality | 11,876 |
| Lanark Highlands | lower-tier | township | 5,737 |
| Larder Lake | single-tier | township | 745 |
| LaSalle | lower-tier | town | 32,721 |
| Latchford | single-tier | town | 355 |
| Laurentian Hills | lower-tier | town | 2,885 |
| Laurentian Valley | lower-tier | township | 9,450 |
| Leamington | lower-tier | municipality | 29,680 |
| Leeds and the Thousand Islands | lower-tier | township | 9,804 |
| Limerick | lower-tier | township | 436 |
| Lincoln | lower-tier | town | 25,719 |
| London | single-tier | city | 422,324 |
| Loyalist | lower-tier | township | 17,943 |
| Lucan Biddulph | lower-tier | township | 5,680 |
| Macdonald, Meredith and Aberdeen Additional | single-tier | township | 1,513 |
| Machar | single-tier | township | 969 |
| Machin | single-tier | municipality | 1,012 |
| Madawaska Valley | lower-tier | township | 3,927 |
| Madoc | lower-tier | township | 2,233 |
| Magnetawan | single-tier | municipality | 1,753 |
| Malahide | lower-tier | township | 9,308 |
| Manitouwadge | single-tier | township | 1,974 |
| Mapleton | lower-tier | township | 10,839 |
| Marathon | single-tier | town | 3,138 |
| Markham | lower-tier | city | 338,503 |
| Markstay-Warren | single-tier | municipality | 2,708 |
| Marmora and Lake | lower-tier | municipality | 4,267 |
| Matachewan | single-tier | township | 268 |
| Mattawa | single-tier | town | 1,881 |
| Mattawan | single-tier | township | 153 |
| Mattice-Val Côté | single-tier | township | 542 |
| McDougall | single-tier | municipality | 2,744 |
| McGarry | single-tier | township | 579 |
| McKellar | single-tier | township | 1,419 |
| McMurrich/Monteith | single-tier | township | 907 |
| McNab/Braeside | lower-tier | township | 7,591 |
| Meaford | lower-tier | municipality | 11,485 |
| Melancthon | lower-tier | township | 3,132 |
| Merrickville-Wolford | lower-tier | village | 3,135 |
| Middlesex Centre | lower-tier | municipality | 18,928 |
| Midland | lower-tier | town | 17,817 |
| Milton | lower-tier | town | 132,979 |
| Minden Hills | lower-tier | township | 6,971 |
| Minto | lower-tier | town | 9,094 |
| Mississauga | lower-tier | city | 717,961 |
| Mississippi Mills | lower-tier | town | 14,740 |
| Mono | lower-tier | town | 9,421 |
| Montague | lower-tier | township | 3,914 |
| Moonbeam | single-tier | township | 1,157 |
| Moosonee | single-tier | town | 1,512 |
| Morley | single-tier | township | 493 |
| Morris-Turnberry | lower-tier | municipality | 3,590 |
| Mulmur | lower-tier | township | 3,571 |
| Muskoka Lakes | lower-tier | township | 7,652 |
| Nairn and Hyman | single-tier | township | 373 |
| The Nation | lower-tier | municipality | 13,350 |
| Neebing | single-tier | municipality | 2,241 |
| New Tecumseth | lower-tier | town | 43,948 |
| Newbury | lower-tier | village | 440 |
| Newmarket | lower-tier | town | 87,942 |
| Niagara Falls | lower-tier | city | 94,415 |
| Niagara-on-the-Lake | lower-tier | town | 19,088 |
| Nipigon | single-tier | township | 1,473 |
| Nipissing | single-tier | township | 1,769 |
| Norfolk | single-tier | city | 67,490 |
| North Algona Wilberforce | lower-tier | township | 3,111 |
| North Bay | single-tier | city | 52,662 |
| North Dumfries | lower-tier | township | 10,619 |
| North Dundas | lower-tier | township | 11,304 |
| North Frontenac | lower-tier | township | 2,285 |
| North Glengarry | lower-tier | township | 10,144 |
| North Grenville | lower-tier | municipality | 17,964 |
| North Huron | lower-tier | township | 5,052 |
| North Kawartha | lower-tier | township | 2,877 |
| North Middlesex | lower-tier | municipality | 6,307 |
| North Perth | lower-tier | municipality | 15,538 |
| The North Shore | single-tier | township | 531 |
| North Stormont | lower-tier | township | 7,400 |
| Northeastern Manitoulin and the Islands | single-tier | municipality | 2,641 |
| Northern Bruce Peninsula | lower-tier | municipality | 4,404 |
| Norwich | lower-tier | township | 11,151 |
| Oakville | lower-tier | town | 213,759 |
| O'Connor | single-tier | township | 689 |
| Oil Springs | lower-tier | village | 647 |
| Oliver Paipoonge | single-tier | municipality | 6,035 |
| Opasatika | single-tier | township | 200 |
| Orangeville | lower-tier | town | 30,167 |
| Orillia | single-tier | city | 33,411 |
| Oro-Medonte | lower-tier | township | 23,017 |
| Oshawa | lower-tier | city | 175,383 |
| Otonabee-South Monaghan | lower-tier | township | 7,087 |
| Ottawa | single-tier | city | 1,017,449 |
| Owen Sound | lower-tier | city | 21,612 |
| Papineau-Cameron | single-tier | township | 982 |
| Parry Sound | single-tier | town | 6,879 |
| Pelee | single-tier | township | 230 |
| Pelham | lower-tier | town | 18,192 |
| Pembroke | single-tier | city | 14,364 |
| Penetanguishene | lower-tier | town | 10,077 |
| Perry | single-tier | township | 2,650 |
| Perth | lower-tier | town | 6,469 |
| Perth East | lower-tier | township | 12,595 |
| Perth South | lower-tier | township | 3,776 |
| Petawawa | lower-tier | town | 18,160 |
| Peterborough | single-tier | city | 83,651 |
| Petrolia | lower-tier | town | 6,013 |
| Pickering | lower-tier | city | 99,186 |
| Pickle Lake | single-tier | township | 398 |
| Plummer Additional | single-tier | township | 757 |
| Plympton-Wyoming | lower-tier | town | 8,308 |
| Point Edward | lower-tier | village | 1,930 |
| Port Colborne | lower-tier | city | 20,033 |
| Port Hope | lower-tier | municipality | 17,294 |
| Powassan | single-tier | municipality | 3,346 |
| Prescott | single-tier | town | 4,078 |
| Prince | single-tier | township | 975 |
| Prince Edward | single-tier | city | 25,704 |
| Puslinch | lower-tier | township | 7,944 |
| Quinte West | single-tier | city | 46,560 |
| Rainy River | single-tier | town | 752 |
| Ramara | lower-tier | township | 10,377 |
| Red Lake | single-tier | municipality | 4,094 |
| Red Rock | single-tier | township | 895 |
| Renfrew | lower-tier | town | 8,190 |
| Richmond Hill | lower-tier | city | 202,022 |
| Rideau Lakes | lower-tier | township | 10,883 |
| Russell | lower-tier | township | 19,598 |
| Ryerson | single-tier | township | 745 |
| Sables-Spanish Rivers | single-tier | township | 3,237 |
| Sarnia | lower-tier | city | 72,047 |
| Saugeen Shores | lower-tier | town | 15,908 |
| Sault Ste. Marie | single-tier | city | 72,051 |
| Schreiber | single-tier | township | 1,039 |
| Scugog | lower-tier | township | 21,581 |
| Seguin | single-tier | township | 5,280 |
| Selwyn | lower-tier | township | 18,653 |
| Severn | lower-tier | township | 14,576 |
| Shelburne | lower-tier | town | 8,994 |
| Shuniah | single-tier | municipality | 3,247 |
| Sioux Lookout | single-tier | municipality | 5,839 |
| Sioux Narrows-Nestor Falls | single-tier | township | 727 |
| Smiths Falls | single-tier | town | 9,254 |
| Smooth Rock Falls | single-tier | town | 1,200 |
| South Algonquin | single-tier | township | 1,055 |
| South Bruce | lower-tier | municipality | 5,880 |
| South Bruce Peninsula | lower-tier | town | 9,137 |
| South Dundas | lower-tier | municipality | 11,044 |
| South Frontenac | lower-tier | township | 20,188 |
| South Glengarry | lower-tier | township | 13,330 |
| South Huron | lower-tier | municipality | 10,063 |
| South River | single-tier | village | 1,101 |
| South Stormont | lower-tier | township | 13,570 |
| Southgate | lower-tier | township | 8,716 |
| Southwest Middlesex | lower-tier | municipality | 5,893 |
| South-West Oxford | lower-tier | township | 7,583 |
| Southwold | lower-tier | township | 4,851 |
| Spanish | single-tier | town | 670 |
| Springwater | lower-tier | township | 21,701 |
| St. Catharines | lower-tier | city | 136,803 |
| St. Clair | lower-tier | township | 14,659 |
| St. Joseph | single-tier | township | 1,426 |
| St. Marys | single-tier | town | 7,386 |
| St. Thomas | single-tier | city | 42,840 |
| St.-Charles | single-tier | municipality | 1,357 |
| Stirling-Rawdon | lower-tier | township | 5,015 |
| Stone Mills | lower-tier | township | 7,826 |
| Stratford | single-tier | city | 33,232 |
| Strathroy-Caradoc | lower-tier | municipality | 23,871 |
| Strong | single-tier | township | 1,566 |
| Sundridge | single-tier | village | 938 |
| Tarbutt | single-tier | township | 573 |
| Tay | lower-tier | township | 11,091 |
| Tay Valley | lower-tier | township | 5,925 |
| Tecumseh | lower-tier | town | 23,300 |
| Tehkummah | single-tier | township | 450 |
| Temagami | single-tier | municipality | 862 |
| Temiskaming Shores | single-tier | city | 9,634 |
| Terrace Bay | single-tier | township | 1,528 |
| Thames Centre | lower-tier | municipality | 13,980 |
| Thessalon | single-tier | town | 1,260 |
| Thornloe | single-tier | village | 92 |
| Thorold | lower-tier | city | 23,816 |
| Thunder Bay | single-tier | city | 108,843 |
| Tillsonburg | lower-tier | town | 18,615 |
| Timmins | single-tier | city | 41,145 |
| Tiny | lower-tier | township | 12,966 |
| Toronto | single-tier | city | 2,794,356 |
| Trent Hills | lower-tier | municipality | 13,861 |
| Trent Lakes | lower-tier | municipality | 6,439 |
| Tudor and Cashel | lower-tier | township | 740 |
| Tweed | lower-tier | municipality | 6,067 |
| Tyendinaga | lower-tier | township | 4,538 |
| Uxbridge | lower-tier | township | 21,556 |
| Val Rita-Harty | single-tier | township | 757 |
| Vaughan | lower-tier | city | 323,103 |
| Wainfleet | lower-tier | township | 6,887 |
| Warwick | lower-tier | township | 3,641 |
| Wasaga Beach | lower-tier | town | 24,862 |
| Waterloo | lower-tier | city | 121,436 |
| Wawa | single-tier | municipality | 2,705 |
| Welland | lower-tier | city | 55,750 |
| Wellesley | lower-tier | township | 11,318 |
| Wellington North | lower-tier | township | 12,431 |
| West Elgin | lower-tier | municipality | 5,060 |
| West Grey | lower-tier | municipality | 13,131 |
| West Lincoln | lower-tier | township | 15,454 |
| West Nipissing | single-tier | municipality | 14,583 |
| West Perth | lower-tier | municipality | 9,038 |
| Westport | lower-tier | village | 634 |
| Whitby | lower-tier | town | 138,501 |
| Whitchurch-Stouffville | lower-tier | town | 49,864 |
| White River | single-tier | township | 557 |
| Whitestone | single-tier | municipality | 1,075 |
| Whitewater | lower-tier | township | 7,225 |
| Wilmot | lower-tier | township | 21,429 |
| Windsor | single-tier | city | 229,660 |
| Wollaston | lower-tier | township | 721 |
| Woodstock | lower-tier | city | 46,705 |
| Woolwich | lower-tier | township | 26,999 |
| Zorra | lower-tier | township | 8,628 |

With `preset="explorer"`, the table is set up for looking through data: each column can be filtered (from the button by its label) and has a profile of its values, with its dtype, the rows are numbered, compact and monospaced, missing values are tinted, the status line above the table says what the data is and how much of it there is, and the rows can be downloaded.

``` python
from great_tables.data import gtcars

GTI(gtcars[["mfr", "model", "year", "hp", "msrp", "ctry_origin"]], preset="explorer")
```

| mfr           | model          | year | hp    | msrp      | ctry_origin    |
|---------------|----------------|------|-------|-----------|----------------|
| Ford          | GT             | 2017 | 647.0 | 447000.0  | United States  |
| Ferrari       | 458 Speciale   | 2015 | 597.0 | 291744.0  | Italy          |
| Ferrari       | 458 Spider     | 2015 | 562.0 | 263553.0  | Italy          |
| Ferrari       | 458 Italia     | 2014 | 562.0 | 233509.0  | Italy          |
| Ferrari       | 488 GTB        | 2016 | 661.0 | 245400.0  | Italy          |
| Ferrari       | California     | 2015 | 553.0 | 198973.0  | Italy          |
| Ferrari       | GTC4Lusso      | 2017 | 680.0 | 298000.0  | Italy          |
| Ferrari       | FF             | 2015 | 652.0 | 295000.0  | Italy          |
| Ferrari       | F12Berlinetta  | 2015 | 731.0 | 319995.0  | Italy          |
| Ferrari       | LaFerrari      | 2015 | 949.0 | 1416362.0 | Italy          |
| Acura         | NSX            | 2017 | 573.0 | 156000.0  | Japan          |
| Nissan        | GT-R           | 2016 | 545.0 | 101770.0  | Japan          |
| Lamborghini   | Aventador      | 2015 | 700.0 | 397500.0  | Italy          |
| Lamborghini   | Huracan        | 2015 | 610.0 | 237250.0  | Italy          |
| Lamborghini   | Gallardo       | 2014 | 550.0 | 191900.0  | Italy          |
| Bentley       | Continental GT | 2016 | 500.0 | 198500.0  | United Kingdom |
| Maserati      | Granturismo    | 2016 | 454.0 | 132825.0  | Italy          |
| Maserati      | Quattroporte   | 2016 | 404.0 | 99900.0   | Italy          |
| Maserati      | Ghibli         | 2016 | 345.0 | 70600.0   | Italy          |
| BMW           | 6-Series       | 2016 | 315.0 | 77300.0   | Germany        |
| BMW           | i8             | 2016 | 357.0 | 140700.0  | Germany        |
| BMW           | M4             | 2016 | 425.0 | 65700.0   | Germany        |
| BMW           | M5             | 2016 | 560.0 | 94100.0   | Germany        |
| BMW           | M6             | 2016 | 560.0 | 113400.0  | Germany        |
| Aston Martin  | DB11           | 2017 | 608.0 | 211195.0  | United Kingdom |
| Aston Martin  | Rapide S       | 2016 | 552.0 | 205300.0  | United Kingdom |
| Aston Martin  | Vanquish       | 2016 | 568.0 | 287250.0  | United Kingdom |
| Aston Martin  | Vantage        | 2016 | 430.0 | 103300.0  | United Kingdom |
| Chevrolet     | Corvette       | 2016 | 650.0 | 88345.0   | United States  |
| Dodge         | Viper          | 2017 | 645.0 | 95895.0   | United States  |
| Audi          | R8             | 2015 | 430.0 | 115900.0  | Germany        |
| Audi          | RS 7           | 2016 | 560.0 | 108900.0  | Germany        |
| Audi          | S6             | 2016 | 450.0 | 70900.0   | Germany        |
| Audi          | S7             | 2016 | 450.0 | 82900.0   | Germany        |
| Audi          | S8             | 2016 | 520.0 | 114900.0  | Germany        |
| Lotus         | Evora          | 2017 | 400.0 | 91900.0   | United Kingdom |
| Jaguar        | F-Type         | 2016 | 340.0 | 65000.0   | United Kingdom |
| Mercedes-Benz | AMG GT         | 2016 | 503.0 | 129900.0  | Germany        |
| Mercedes-Benz | SL-Class       | 2016 | 329.0 | 85050.0   | Germany        |
| Tesla         | Model S        | 2017 | 259.0 | 74500.0   | United States  |
| Porsche       | 718 Boxster    | 2017 | 300.0 | 56000.0   | Germany        |
| Porsche       | 718 Cayman     | 2017 | 300.0 | 53900.0   | Germany        |
| Porsche       | 911            | 2016 | 350.0 | 84300.0   | Germany        |
| Porsche       | Panamera       | 2016 | 310.0 | 78100.0   | Germany        |
| McLaren       | 570            | 2016 | 570.0 | 184900.0  | United Kingdom |
| Rolls-Royce   | Dawn           | 2016 | 563.0 | 335000.0  | United Kingdom |
| Rolls-Royce   | Wraith         | 2016 | 624.0 | 304350.0  | United Kingdom |

A [GT](../reference/GT.md#great_tables.GT) table can be made into a [GTI](../reference/GTI.md#great_tables.GTI) table with [`GTI.from_gt()`](../reference/GTI.from_gt.md#great_tables.GTI.from_gt).

A table of a Polars LazyFrame keeps its rows there until they're shown.

``` python
import polars as pl
from great_tables import GTI

lf = pl.scan_parquet("trips.parquet")

GTI(lf).fmt_number(columns="fare", decimals=2).i_cols_filter("payment").i_as_widget()
```

And so does a table of a DuckDB relation, in DuckDB, its rows in the order of a column of IDs.

``` python
import duckdb

trips = duckdb.read_parquet("trips.parquet")

GTI(trips, order_by="trip_id").i_cols_filter("payment").i_as_widget()
```
