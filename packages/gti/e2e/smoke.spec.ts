import { expect, test, type Page } from "@playwright/test";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const fixtures = join(dirname(fileURLToPath(import.meta.url)), ".fixtures");

async function open(page: Page, name: string): Promise<string[]> {
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

for (const name of ["after.html", "head.html"]) {
  test(`hydrates a GT table (${name})`, async ({ page }) => {
    const errors = await open(page, name);
    const el = page.locator("gt-table");

    await expect(el).toHaveAttribute("data-gti-state", "ready");
    expect(await el.evaluate((node) => (node as any).table === node.querySelector("table.gt_table"))).toBe(true);
    expect(await page.evaluate(() => (window as any).GTI.VERSION)).toMatch(/^\d+\.\d+\.\d+/);
    await expect(el).toHaveCSS("display", "block");

    // Hydrating doesn't change the table GT rendered.
    await expect(el.locator("table.gt_table tbody tr")).not.toHaveCount(0);
    await expect(el.locator(".gt_title")).toHaveText("exibble");
    expect(errors).toEqual([]);
  });
}

test("a runtime inlined twice registers once and hydrates every table", async ({ page }) => {
  const errors = await open(page, "twice.html");
  const els = page.locator("gt-table");

  await expect(els).toHaveCount(2);
  for (const el of await els.all()) {
    await expect(el).toHaveAttribute("data-gti-state", "ready");
  }
  expect(errors).toEqual([]);
});
