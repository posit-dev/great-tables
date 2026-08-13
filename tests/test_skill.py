import pytest

from great_tables.skill import install
from great_tables.skill.__main__ import main


def test_install_copies_skill_md_and_references(tmp_path):
    dest = tmp_path / "great-tables"

    result = install(dest)

    assert result == dest.resolve()
    assert (dest / "SKILL.md").is_file()
    assert (dest / "references" / "RULES.md").is_file()
    assert (dest / "references" / "data.md").is_file()
    assert (dest / "scripts" / "house_table.py").is_file()
    assert (dest / "scripts" / "house_table.png").is_file()
    # only the skill's own content is copied, not the installer module itself
    assert not (dest / "__init__.py").exists()
    assert not (dest / "__main__.py").exists()
    assert not (dest / "__pycache__").exists()


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


def test_cli_install_writes_to_requested_dest(tmp_path, capsys):
    dest = tmp_path / "great-tables"

    exit_code = main(["install", str(dest)])

    assert exit_code == 0
    assert (dest / "SKILL.md").is_file()
    assert str(dest.resolve()) in capsys.readouterr().out


def test_cli_install_without_force_reports_error(tmp_path, capsys):
    dest = tmp_path / "great-tables"
    dest.mkdir()

    exit_code = main(["install", str(dest)])

    assert exit_code == 1
    assert "already exists" in capsys.readouterr().err


def test_cli_install_with_force_overwrites(tmp_path, capsys):
    dest = tmp_path / "great-tables"
    dest.mkdir()
    (dest / "marker.txt").write_text("do not touch")

    exit_code = main(["install", str(dest), "--force"])

    assert exit_code == 0
    assert (dest / "SKILL.md").is_file()
    assert not (dest / "marker.txt").exists()


def test_cli_requires_a_subcommand():
    with pytest.raises(SystemExit):
        main([])
