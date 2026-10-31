import { spawnSync } from "node:child_process";
import { existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));

// $PYTHON if set, else the repo's .venv, else python3 on PATH.
function python(): string {
  if (process.env.PYTHON) {
    return process.env.PYTHON;
  }
  const venv = join(here, "..", "..", "..", ".venv", "bin", "python");
  return existsSync(venv) ? venv : "python3";
}

export default function globalSetup(): void {
  const exe = python();
  const result = spawnSync(exe, [join(here, "make_fixtures.py")], { stdio: "inherit" });
  if (result.error !== undefined || result.status !== 0) {
    throw new Error(
      `Couldn't write the e2e fixtures with ${exe} (set $PYTHON to a Python with great_tables installed)`,
    );
  }
}
