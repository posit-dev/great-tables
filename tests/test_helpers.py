from great_tables._helpers import LETTERS, letters, pct, px, random_id


def test_px():
    assert str(px(12)) == "12px"


def test_pct():
    assert str(pct(80)) == "80%"


def test_random_id():
    rid = random_id()
    assert len(rid) == 10
    assert not set(rid).difference(letters())
    assert len(random_id(5)) == 5


def test_lowercases():
    lowercases = letters()
    assert isinstance(lowercases, list)
    assert len(lowercases) == 26

    good_letters = "greattables"
    assert not set(good_letters).difference(lowercases)

    bad_letters = "#$!^%#TABLES"
    assert set(bad_letters).difference(lowercases)


def test_uppercases():
    uppercases = LETTERS()
    assert isinstance(uppercases, list)
    assert len(uppercases) == 26

    good_letters = "GREATTABLES"
    assert not set(good_letters).difference(uppercases)

    bad_letters = "#$!^%#tables"
    assert set(bad_letters).difference(uppercases)
