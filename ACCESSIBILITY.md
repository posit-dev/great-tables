# Accessibility

Great Tables aims for the HTML tables it makes to meet [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
Level AA, and it writes the markup they need for you. A screen reader can announce each cell together
with its row and column headers. Most of this needs no setup: it is the default output of every table.
The [Accessibility](https://posit-dev.github.io/great-tables/user-guide/accessibility.html) page of
the user guide covers it in detail, with a checklist for authors.

## What Great Tables does

Column labels, spanners, row labels, row group headings, and summary row labels are header cells
(`<th>`) with a `scope`, and every data cell lists all of its headers in a `headers` attribute, so
tables with spanners or a hierarchical stub are read correctly. This follows the W3C's
[Tables Tutorial](https://www.w3.org/WAI/tutorials/tables/). A table with a title (`tab_header()`)
is labelled by it, and described by its subtitle.

`data_color()` picks a text color that contrasts with each fill (APCA by default, or WCAG 2 with
`contrast_algo="wcag"`), and themes and dark mode do the same for filled cells that have no text
color of their own. Images from `fmt_image()` take alternative text with `alt=`. Nanoplots are
described by a summary of their values, flags are named after their country, and icons are hidden
from assistive technology as decoration.

Interactive tables, made with `opt_interactive()` or as `GTI` tables, keep the same `<table>`
markup rather than becoming an application grid, so a screen reader's table commands still move
from cell to cell. Sort buttons say how a column is sorted, the filter menus and the query box
follow the patterns of the WAI-ARIA Authoring Practices, and every control works with the keyboard
(the keyboard button in the control bar lists the table's keys). The changes a reader makes are
announced, as in "Sorted by HP, descending. 12 of 47 rows." The controls respect forced colors and
reduced motion, and their targets are at least 24 pixels across (44 on touch screens).

Some things are still missing from interactive tables. A row's position is given within the rows
shown, not the whole table (row 3 of a page, rather than row 23 of 310), there is no
cell-by-cell keyboard navigation of the table's own, and the browser tests don't run automated
accessibility checks yet.

LaTeX output and images saved with `gtsave()` have no equivalent markup, so describe those tables in
the text or the alternative text around them. Colors that you set on cells yourself are written as
you gave them.

Changes to accessibility are listed in the
[release notes](https://github.com/posit-dev/great-tables/releases).

## Reporting accessibility issues

Before opening a new issue, please search the
[existing issues](https://github.com/posit-dev/great-tables/issues?q=is%3Aissue+accessibility) for
accessibility.

When opening an [issue](https://github.com/posit-dev/great-tables/issues/new/choose), include
"accessibility" in the title or description so maintainers can label it, and if possible include:

- A small example of the code that makes the table
- The Great Tables version, and where the table is shown (a notebook, a Quarto document, a web page,
  an email, and so on)
- Operating system and browser
- Assistive technology and version (e.g., NVDA 2025.1, VoiceOver, JAWS)
- What you expected to hear or see, and what happened instead

For general questions, start a thread in
[GitHub Discussions](https://github.com/posit-dev/great-tables/discussions).
