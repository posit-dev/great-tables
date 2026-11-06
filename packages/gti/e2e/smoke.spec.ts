import { expect, test } from "@playwright/test";
import { open } from "./helpers";

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

test("maps every body row of a grouped table with summary rows", async ({ page }) => {
  const errors = await open(page, "after.html");
  await expect(page.locator("gt-table")).toHaveAttribute("data-gti-state", "ready");

  // For each <tr>: its spec entry, and how GT rendered it.
  const rows = await page.locator("gt-table").evaluate((node) => {
    const el = node as any;
    return Array.from(node.querySelectorAll("tbody.gt_table_body > tr")).map((tr) => {
      const entry = el.bodyRow(tr);
      return {
        entry,
        heading: tr.classList.contains("gt_group_heading_row"),
        summary: tr.querySelector(".gt_summary_row") !== null,
        grand: tr.querySelector(".gt_grand_summary_row") !== null,
        first: tr.querySelector("th, td")?.textContent?.trim(),
        found: typeof entry === "number" ? el.rowElement(entry) === tr : null,
      };
    });
  });

  // The groups are shown in the opposite order to the data, with summaries.
  expect(rows).toHaveLength(13);
  expect(rows.map((r) => r.entry).filter((e) => typeof e === "number")).toEqual([4, 5, 6, 7, 0, 1, 2, 3]);
  for (const r of rows) {
    if (typeof r.entry === "number") {
      expect(r.first).toBe(`row_${r.entry + 1}`);
      expect(r.found).toBe(true);
    } else if ("grand_summary" in r.entry) {
      expect(r.grand).toBe(true);
      expect(r.first).toBe(r.entry.grand_summary);
    } else if ("summary" in r.entry) {
      expect(r.summary).toBe(true);
      expect(r.first).toBe(r.entry.summary);
    } else {
      expect(r.heading).toBe(true);
      expect(r.first).toBe(r.entry.group);
    }
  }
  expect(errors).toEqual([]);
});

test("a runtime inlined twice registers once and hydrates every table", async ({ page }) => {
  const errors = await open(page, "twice.html");
  const els = page.locator("gt-table");

  await expect(els).toHaveCount(2);
  for (const el of await els.all()) {
    await expect(el).toHaveAttribute("data-gti-state", "ready");
  }
  expect(errors).toEqual([]);
});
