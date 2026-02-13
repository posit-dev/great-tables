# %%
from ast import NodeVisitor, Import, ImportFrom, parse
from pathlib import Path
from os import walk


# %%
class NaughtyImportChecker(NodeVisitor):
    def __init__(self):
        self.import_crimes: list["Import | ImportFrom"] = []

    def visit_Import(self, node: Import):
        for el in node.names:
            if el.name.split(".")[0] == "pandas":
                self.import_crimes.append(node)

    def visit_ImportFrom(self, node: ImportFrom):
        if node.module and node.module.split(".")[0] == "pandas":
            self.import_crimes.append(node)

    @classmethod
    def validate_file(cls, fname: str):
        with open(fname) as f:
            tree = parse(f.read(), filename=fname)

        visitor = cls()
        visitor.visit(tree)

        return visitor.import_crimes

    @classmethod
    def validate_folder(cls, folder: str) -> dict[Path, list["ImportFrom | Import"]]:
        all_crimes: dict[Path, list["ImportFrom | Import"]] = {}
        for dirpath, _, filenames in walk(folder):
            for fname in filenames:
                if fname.endswith(".py"):
                    p = Path(dirpath) / fname
                    crimes = cls.validate_file(str(p))
                    if len(crimes):
                        all_crimes[p.relative_to(folder)] = crimes

        return all_crimes


def report_details(results: list["ImportFrom | Import"]):
    n_entries = len(results)
    return f"{n_entries} imports"


def report(results: dict[str, list["ImportFrom | Import"]], forgiveable: "list[str] | None" = None):
    if forgiveable is None:
        forgiveable = []

    lines = []
    for path, crimes in results.items():
        if str(path) in forgiveable:
            continue
        lines.append(f"{path}: {report_details(crimes)}")

    if lines:
        raise Exception("Pandas imports detected.\n\n" + "\n".join(lines))


# %%
if __name__ == "__main__":
    import sys

    folder, *forgiveable = sys.argv[1:]
    print(forgiveable)

    crimes = NaughtyImportChecker.validate_folder(folder)
    report(crimes, forgiveable=forgiveable)
