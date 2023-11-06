import pytest

from great_tables._locations import LocColumnSpanners, resolve
from great_tables._gt_data import Spanners, SpannerInfo


def test_resolve_column_spanners_simple():
    # note that this essentially a no-op
    ids = ["a", "b", "c"]

    spanners = Spanners([SpannerInfo(spanner_id=id) for id in ids])
    loc = LocColumnSpanners(ids=["a", "c"])

    new_loc = resolve(loc, spanners)

    assert new_loc == loc
    assert new_loc.ids == ["a", "c"]


def test_resolve_column_spanners_error_missing():
    # note that this essentially a no-op
    ids = ["a", "b", "c"]

    spanners = Spanners([SpannerInfo(spanner_id=id) for id in ids])
    loc = LocColumnSpanners(ids=["a", "d"])

    with pytest.raises(ValueError):
        resolve(loc, spanners)
