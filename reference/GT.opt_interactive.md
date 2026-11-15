# GT.opt_interactive()

Option to enable an interactive table.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L1845-L1974)

``` python
GT.opt_interactive(
    active=True,
    use_pagination=True,
    use_pagination_info=True,
    use_sorting=True,
    use_search=False,
    use_filters=False,
    use_resizers=False,
    use_highlight=False,
    use_compact_mode=False,
    use_text_wrapping=True,
    use_page_size_select=False,
    page_size_default=10,
    page_size_values=None,
    pagination_type="numbers",
    height="auto",
    selection_mode=None,
)
```

With [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive), a GT table becomes one that readers can browse in the browser: they can sort it by its columns, search and filter its rows, and page through them. Everything else about the table stays as it is: its formatting, styles, header and footer, stub, row groups, spanners and summary rows are all kept, as they'd be in the static table. The interactivity is added to the table's own HTML by a small script that comes with it, so no server, internet connection, or other library is needed, and the table can be read before (or without) the script running. The table is interactive wherever its HTML is shown: in notebooks, in Quarto documents, and in HTML files written with [`write_raw_html()`](../reference/GT.write_raw_html.md#great_tables.GT.write_raw_html).

The options here are those of R gt's [opt_interactive()](../reference/GT.opt_interactive.md#great_tables.GT.opt_interactive), so that a published table can be made browsable without changing what it is. For a table that's more of an interface (with filters chosen column by column, exports, views that can be saved and shared, pinned and hideable columns, and a control bar that brings these together), use [GTI](../reference/GTI.md#great_tables.GTI), or turn a finished table into one with [GTI.from_gt()](../reference/GTI.from_gt.md#great_tables.GTI.from_gt). Both render the table with the same engine.

## Parameters

`active: bool = True`  
Whether to activate interactive mode. Set to `False` to disable while keeping the stored options.

`use_pagination: bool = True`  
Whether to paginate rows. Enabled by default.

`use_pagination_info: bool = True`  
Whether to show which rows are on the page, next to the page controls (e.g., "1-10 of 100 rows").

`use_sorting: bool = True`  
Whether to enable column sorting by clicking the column labels. Columns are sorted by their values, not by how they're formatted.

`use_search: bool = False`  
Whether to add a global search box above the table. It searches the text shown in the cells.

`use_filters: bool = False`  
Whether readers can filter the rows by each column, with a filter button on its column label (the stub and the row group column don't have one). The filter is suited to the column's type: a range of numbers or dates, a choice of values for a column with only a few of them (or a categorical one), true or false for a boolean column, and text to match for the rest.

`use_resizers: bool = False`  
Whether to allow columns to be resized by dragging their edges.

`use_highlight: bool = False`  
Whether to highlight the row under the cursor on hover.

`use_compact_mode: bool = False`  
Whether to use compact row padding to fit more rows on screen.

`use_text_wrapping: bool = True`  
Whether to allow cell text to wrap. When `False`, cell text stays on one line, ending with an ellipsis where it doesn't fit.

`use_page_size_select: bool = False`  
Whether to show a dropdown for the user to change the number of rows per page.

`page_size_default: int = 10`  
The default number of rows displayed per page.

`page_size_values: list[int] | None = None`  
The list of page-size options available in the page-size dropdown. Defaults to `[10, 25, 50, 100]`.

`pagination_type: str = "numbers"`  
The pagination control style. One of `"numbers"` (page number buttons), `"simple"` (previous/next only), `"full"` (first/previous/next/last, with the page number), or `"jump"` (previous/next, with a box to type the page number in).

`height: str | float = "auto"`  
The most the table can be in height. Use `"auto"` (the default) to let the table grow with its content, or supply a CSS length (e.g., `"400px"` or `"60vh"`) or a number of pixels to limit the height and have the table scroll within it, with its header and column labels staying in view.

`selection_mode: str | None = None`  
Row selection mode. One of `"single"`, `"multiple"`, or `None` (the default, which disables row selection). Rows are selected by clicking them or their checkboxes. With `"single"`, selecting a row clears the one selected before; with `"multiple"`, Shift-click selects a range of rows, and a checkbox in the column labels selects every row that matches the search.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset, create an interactive table with search and filtering enabled.

``` python
from great_tables import GT, exibble

GT(exibble).opt_interactive(use_search=True, use_filters=True)
```

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |
