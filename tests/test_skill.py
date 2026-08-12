import pytest

from great_tables.skill import install


def test_install_copies_skill_md_and_references(tmp_path):
    dest = tmp_path / "great-tables"

    result = install(dest)

    assert result == dest.resolve()
    assert (dest / "SKILL.md").is_file()
    assert (dest / "references" / "REFERENCE.md").is_file()
    assert (dest / "references" / "big_color" / "diverging_fill.md").is_file()
    # only the skill's own content is copied, not the installer module itself
    assert not (dest / "__init__.py").exists()


def test_install_refuses_to_overwrite_without_force(tmp_path):
    dest = tmp_path / "great-tables"
    dest.mkdir()
    (dest / "marker.txt").write_text("do not touch")

    with pytest.raises(FileExistsError):
        install(dest)

    assert (dest / "marker.txt").is_file()


def test_install_overwrites_with_force(tmp_path):
    dest = tmp_path / "great-tables"
    dest.mkdir()
    (dest / "marker.txt").write_text("do not touch")

    result = install(dest, force=True)

    assert result == dest.resolve()
    assert (dest / "SKILL.md").is_file()
    assert not (dest / "marker.txt").exists()
