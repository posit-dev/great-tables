from __future__ import annotations

import shutil
from pathlib import Path

from importlib_resources import as_file, files

SKILL_MOD = files("great_tables.skill")

DEFAULT_DEST = Path(".claude/skills/great-tables")


def install(dest: str | Path = DEFAULT_DEST, *, force: bool = False) -> Path:
    """Copy the bundled `great-tables` Agent Skill to `dest`.

    The skill teaches an AI coding agent to drive every `great_tables` build
    through the same deterministic design flowchart, so tables built by an
    agent look consistent from one run to the next. This copies the skill's
    `SKILL.md` and `references/` folder, unmodified, out of the installed
    `great_tables` package.

    Parameters
    ----------
    dest
        Where to copy the skill folder. Defaults to `.claude/skills/great-tables`,
        relative to the current working directory.
    force
        Overwrite `dest` if it already exists. By default, an existing `dest`
        raises `FileExistsError` rather than silently overwriting it.

    Returns
    -------
    Path
        The resolved destination path the skill was copied to.
    """
    dest_path = Path(dest)

    if dest_path.exists():
        if not force:
            raise FileExistsError(
                f"{dest_path} already exists. Pass force=True "
                "(or --force on the command line) to overwrite it."
            )
        shutil.rmtree(dest_path)

    dest_path.mkdir(parents=True)

    with as_file(SKILL_MOD / "SKILL.md") as src_file:
        shutil.copy2(src_file, dest_path / "SKILL.md")

    with as_file(SKILL_MOD / "references") as src_refs:
        shutil.copytree(src_refs, dest_path / "references")

    return dest_path.resolve()
