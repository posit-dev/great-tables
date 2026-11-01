import type { Page } from "@playwright/test";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const fixtures = join(dirname(fileURLToPath(import.meta.url)), ".fixtures");

/** Open a fixture page, returning the errors it logs (filled in as they happen). */
export async function open(page: Page, name: string): Promise<string[]> {
  const errors: string[] = [];
  page.on("pageerror", (err) => errors.push(err.message));
  page.on("console", (msg) => {
    if (msg.type() === "error") {
      errors.push(msg.text());
    }
  });
  await page.goto(pathToFileURL(join(fixtures, name)).href);
  return errors;
}
