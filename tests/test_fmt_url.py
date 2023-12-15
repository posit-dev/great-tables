from great_tables import GT
from great_tables.data import towny
from great_tables._utils_render_html import create_body_component_h

towny_mini = towny[["name", "website"]].head(3)


def assert_rendered_body(snapshot, gt):
    built = gt._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def test_fmt_url_01(snapshot):
    new_gt = GT(towny_mini).fmt_url(columns="website")

    assert_rendered_body(snapshot, new_gt)


def test_fmt_url_02(snapshot):
    new_gt = GT(towny_mini).fmt_url(columns="website", as_button=True)

    assert_rendered_body(snapshot, new_gt)


def test_fmt_url_03(snapshot):
    new_gt = GT(towny_mini).fmt_url(columns="website", color="red")

    assert_rendered_body(snapshot, new_gt)


def test_fmt_url_04(snapshot):
    new_gt = GT(towny_mini).fmt_url(columns="website", as_button=True, color="green")

    assert_rendered_body(snapshot, new_gt)


def test_fmt_url_05(snapshot):
    new_gt = GT(towny_mini).fmt_url(columns="website", show_underline=False, color="green")

    assert_rendered_body(snapshot, new_gt)
