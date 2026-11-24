from __future__ import annotations

from typing import TYPE_CHECKING

from ._gt_data import Heading, Spanners
from ._spanners import _resolve_spanner_ids

if TYPE_CHECKING:
    from ._types import GTSelf


def rm_header(self: GTSelf) -> GTSelf:
    """
    Remove the table header.

    We can remove the table header (i.e., the part containing the title and the subtitle) with the
    `rm_header()` method. This function is useful when you have received a `GT` object with a header
    (perhaps from another function or a saved table) and you'd like to start from a clean slate.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset to create a table with a header. We can then remove
    that header with the `rm_header()` method.

    ```{python}
    from great_tables import GT, md
    from great_tables.data import gtcars

    gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

    (
        GT(gtcars_mini)
        .tab_header(title=md("Data listing from **gtcars**"), subtitle="Just five cars")
        .rm_header()
    )
    ```

    See Also
    --------
    [`tab_header()`](`great_tables.GT.tab_header`) to add a header to a table.
    """

    return self._replace(_heading=Heading())


def rm_stubhead(self: GTSelf) -> GTSelf:
    """
    Remove the stubhead label.

    We can remove the stubhead label (i.e., the label positioned above the table stub) with the
    `rm_stubhead()` method. This is useful when a stubhead label is present but no longer wanted.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using a subset of the `gtcars` dataset, we create a table with a stub and a stubhead label. The
    label is then removed with the `rm_stubhead()` method.

    ```{python}
    from great_tables import GT
    from great_tables.data import gtcars

    gtcars_mini = gtcars[["model", "mfr", "msrp"]].head(5)

    (
        GT(gtcars_mini, rowname_col="model")
        .tab_stubhead(label="car")
        .rm_stubhead()
    )
    ```

    See Also
    --------
    [`tab_stubhead()`](`great_tables.GT.tab_stubhead`) to add a stubhead label to a table.
    """

    return self._replace(_stubhead=None)


def rm_source_notes(self: GTSelf, source_notes: int | list[int] | None = None) -> GTSelf:
    """
    Remove table source notes.

    Source notes are added to the footer part of the table with the
    [`tab_source_note()`](`great_tables.GT.tab_source_note`) method. With `rm_source_notes()` we
    can remove all of them at once or, by supplying the `source_notes=` argument, only those at
    specific indices.

    Parameters
    ----------
    source_notes
        The source notes to remove. Supplied as a single index or a list of indices (`0`-based, in
        the order the source notes were added). If `None` (the default), then all source notes will
        be removed.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using a subset of the `gtcars` dataset, let's create a table with two source notes. We then
    remove the first of the two with the `source_notes=` argument.

    ```{python}
    from great_tables import GT
    from great_tables.data import gtcars

    gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

    (
        GT(gtcars_mini)
        .tab_source_note(source_note="From edmunds.com")
        .tab_source_note(source_note="Prices in USD.")
        .rm_source_notes(source_notes=0)
    )
    ```

    See Also
    --------
    [`tab_source_note()`](`great_tables.GT.tab_source_note`) to add a source note to a table.
    """

    idx_to_remove = _resolve_footer_idx(source_notes, len(self._source_notes), "source_notes")

    new_source_notes = [
        note for ii, note in enumerate(self._source_notes) if ii not in idx_to_remove
    ]

    return self._replace(_source_notes=new_source_notes)


def rm_footnotes(self: GTSelf, footnotes: int | list[int] | None = None) -> GTSelf:
    """
    Remove table footnotes.

    Footnotes are added to targeted locations with the
    [`tab_footnote()`](`great_tables.GT.tab_footnote`) method. With `rm_footnotes()` we can remove
    all of them at once or, by supplying the `footnotes=` argument, only those at specific indices.

    Parameters
    ----------
    footnotes
        The footnotes to remove. Supplied as a single index or a list of indices (`0`-based, in the
        order the footnotes were added). If `None` (the default), then all footnotes will be
        removed.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using a subset of the `gtcars` dataset, let's create a table with two footnotes. We then remove
    all footnotes by calling `rm_footnotes()` without any arguments.

    ```{python}
    from great_tables import GT
    from great_tables.loc import body
    from great_tables.data import gtcars

    gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

    (
        GT(gtcars_mini)
        .tab_footnote(footnote="Manufacturer.", locations=body(columns="mfr", rows=[0]))
        .tab_footnote(footnote="Price.", locations=body(columns="msrp", rows=[0]))
        .rm_footnotes()
    )
    ```

    See Also
    --------
    [`tab_footnote()`](`great_tables.GT.tab_footnote`) to add a footnote to a table.
    """

    idx_to_remove = _resolve_footer_idx(footnotes, len(self._footnotes), "footnotes")

    new_footnotes = [note for ii, note in enumerate(self._footnotes) if ii not in idx_to_remove]

    return self._replace(_footnotes=new_footnotes)


def rm_spanners(
    self: GTSelf,
    spanners: str | list[str] | None = None,
    levels: int | list[int] | None = None,
) -> GTSelf:
    """
    Remove column spanners.

    Column spanners are added with the [`tab_spanner()`](`great_tables.GT.tab_spanner`) method. The
    `rm_spanners()` method allows for the removal of spanners while leaving the columns themselves
    intact. We can either target spanners by their ID values (with the `spanners=` argument) or by
    their levels (with the `levels=` argument).

    Parameters
    ----------
    spanners
        The spanners to remove. Supplied as a single spanner ID or a list of spanner ID values. If
        `None` (the default), then all spanners will be considered for removal (subject to any
        constraint imposed by `levels=`).
    levels
        The spanner levels to remove, supplied as a single level or a list of levels. Spanners are
        placed on levels starting from `0` (the level closest to the column labels). If `None` (the
        default), then no levels-based constraint is applied. When supplied, only spanners residing
        on the specified levels (and also matching `spanners=`) are removed.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using a subset of the `gtcars` dataset, let's create a table with two spanners. We then remove
    the spanner with the ID `"performance"` while leaving the other spanner in place.

    ```{python}
    from great_tables import GT
    from great_tables.data import gtcars

    gtcars_mini = gtcars[["mfr", "model", "hp", "trq", "mpg_c"]].head(5)

    (
        GT(gtcars_mini)
        .tab_spanner(label="performance", columns=["hp", "trq"])
        .tab_spanner(label="economy", columns=["mpg_c"])
        .rm_spanners(spanners="performance")
    )
    ```

    See Also
    --------
    [`tab_spanner()`](`great_tables.GT.tab_spanner`) to add a spanner to a table.
    """

    crnt_spanners = self._spanners

    if not len(crnt_spanners):
        return self

    ids_to_remove = _resolve_spanner_ids(crnt_spanners, spanners=spanners, levels=levels)

    new_spanners = Spanners(
        [span for span in crnt_spanners if span.spanner_id not in ids_to_remove]
    )

    return self._replace(_spanners=new_spanners)


def _resolve_footer_idx(selection: int | list[int] | None, n: int, arg_name: str) -> set[int]:
    """Resolve a footer selection to a set of valid `0`-based indices to remove."""

    if selection is None:
        return set(range(n))

    idx = [selection] if isinstance(selection, int) else list(selection)

    out_of_range = [i for i in idx if not (0 <= i < n)]
    if out_of_range:
        raise ValueError(
            f"These `{arg_name}=` indices are out of range (table has {n}): {out_of_range}."
        )

    return set(idx)
