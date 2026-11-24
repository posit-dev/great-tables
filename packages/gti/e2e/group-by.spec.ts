import { expect, type Locator, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// Grouping rows: twelve towns (name as the stub, then region, which town_3 and town_9 lack, size,
// and pop), 5 rows to a page, whose region and size readers can group the rows by (and hide, as
// they can pop), with a search, the view kept in the URL and changes undone. And all on one page,
// in a body 200px high, grouped by region to start with.
//
// By region (east, north, south, then the missing), the towns are: east 5, 11; north 1, 4, 7, 10;
// south 2, 6, 8, 12; and (Missing) 3, 9.

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const toggle = (page: Page) => bar(page).getByRole("button", { name: "Group rows", exact: true });
const panel = (page: Page) => bar(page).getByRole("group", { name: "Group rows", exact: true });
const radio = (page: Page, name: string) => panel(page).getByRole("radio", { name, exact: true });
const groupBy = (page: Page) => el(page).evaluate((node) => (node as any).groupBy as string | null);
const search = (page: Page) => decodeURIComponent(new URL(page.url()).search);
const live = (page: Page) => el(page).locator(".gt-i-live");
const next = (page: Page) => bar(page).getByRole("button", { name: "Next page", exact: true });
const headings = (page: Page) => el(page).locator("tbody tr.gt_group_heading_row");

type Box = { top: number; bottom: number; left: number; right: number };
const rect = (locator: Locator): Promise<Box> =>
  locator.evaluate((node) => {
    const { top, bottom, left, right } = node.getBoundingClientRect();
    return { top, bottom, left, right };
  });

// The body's rows a reader sees: each group's heading (its text) and each town (its name)
const body = (page: Page) =>
  el(page).evaluate((node) =>
    Array.from(node.querySelectorAll<HTMLTableRowElement>("tbody.gt_table_body > tr"))
      .filter((tr) => tr.getClientRects().length > 0 && !tr.matches(".gt-i-filler, .gt-i-empty"))
      .map((tr) => (tr.matches(".gt_group_heading_row") ? `# ${tr.textContent?.trim()}` : (tr.cells[0]?.textContent?.trim() ?? ""))),
  );

async function group(page: Page, name: string): Promise<void> {
  await toggle(page).click();
  await radio(page, name).check();
  await page.keyboard.press("Escape");
}

test.describe("grouping rows", () => {
  test("groups the rows by a column chosen in the bar, under headings with their counts", async ({ page }) => {
    const errors = await ready(page, "group.html");
    await expect(headings(page)).toHaveCount(0);
    await toggle(page).click();
    await expect(panel(page)).toBeVisible();
    await expect(panel(page).getByRole("radio")).toHaveCount(3);
    await expect(radio(page, "None")).toBeChecked();
    await expect(panel(page).getByRole("radiogroup", { name: "Group rows by" })).toBeVisible();

    await radio(page, "region").check();
    await expect(live(page)).toHaveText("Rows grouped by region");
    expect(await groupBy(page)).toBe("region");
    // Each page has its 5 rows, under the headings of the groups they're in
    expect(await body(page)).toEqual(["# east (2)", "town_5", "town_11", "# north (4)", "town_1", "town_4", "town_7"]);
    await expect(headings(page).first().locator("th")).toHaveAttribute("scope", "colgroup");
    await page.keyboard.press("Escape");
    await next(page).click();
    expect(await body(page)).toEqual(["# north (4)", "town_10", "# south (4)", "town_2", "town_6", "town_8", "town_12"]);
    await next(page).click();
    // (The missing values last)
    expect(await body(page)).toEqual(["# (Missing) (2)", "town_3", "town_9"]);

    // Back to page 1 for another column, and none
    await group(page, "size");
    expect(await el(page).evaluate((node) => (node as any).page)).toBe(1);
    expect(await body(page)).toEqual(["# big (6)", "town_1", "town_4", "town_6", "town_8", "town_9"]);
    await group(page, "None");
    await expect(live(page)).toHaveText("Rows not grouped");
    await expect(headings(page)).toHaveCount(0);
    expect(await body(page)).toEqual(["town_1", "town_2", "town_3", "town_4", "town_5"]);
    expect(errors).toEqual([]);
  });

  test("sorts the rows within their groups, and the groups by the grouped column's sort", async ({ page }) => {
    await ready(page, "group.html");
    await group(page, "region");
    await el(page).evaluate((node) => ((node as any).sort = [{ column: "pop", descending: true }]));
    expect(await body(page)).toEqual(["# east (2)", "town_11", "town_5", "# north (4)", "town_4", "town_7", "town_10"]);
    await el(page).evaluate((node) => ((node as any).sort = [{ column: "region", descending: true }]));
    expect(await body(page)).toEqual(["# south (4)", "town_2", "town_6", "town_8", "town_12", "# north (4)", "town_1"]);
    await next(page).click();
    expect(await body(page)).toEqual(["# north (4)", "town_4", "town_7", "town_10", "# east (2)", "town_5", "town_11"]);
    await next(page).click();
    // (Still last)
    expect(await body(page)).toEqual(["# (Missing) (2)", "town_3", "town_9"]);
  });

  test("counts the rows of each group that match, and leaves out the groups without any", async ({ page }) => {
    await ready(page, "group.html");
    await group(page, "region");
    await bar(page).getByRole("button", { name: "Search the table" }).click();
    await el(page).locator("input.gt-i-search").fill("big");
    await expect.poll(() => body(page)).toEqual([
      "# north (2)",
      "town_1",
      "town_4",
      "# south (3)",
      "town_6",
      "town_8",
      "town_12",
    ]);
    // (The search box, open, takes the page buttons' place)
    await el(page).evaluate((node) => ((node as any).page = 2));
    expect(await body(page)).toEqual(["# (Missing) (1)", "town_9"]);
  });

  test("spans the headings across the columns shown", async ({ page }) => {
    await ready(page, "group.html");
    await group(page, "region");
    const heading = headings(page).first().locator("th");
    await expect(heading).toHaveAttribute("colspan", "4");
    await el(page).evaluate((node) => ((node as any).hiddenColumns = ["pop"]));
    await expect(heading).toHaveAttribute("colspan", "3");
    const row = await rect(el(page).locator("tbody tr:not(.gt_group_heading_row)").first());
    const box = await rect(heading);
    expect(box.left).toBeCloseTo(row.left, 0);
    expect(box.right).toBeCloseTo(row.right, 0);
  });

  test("keeps the grouping in the URL, and undoes it", async ({ page }) => {
    await ready(page, "group.html");
    await group(page, "region");
    expect(search(page)).toBe("?g.group=region");
    await bar(page).getByRole("button", { name: "Undo", exact: true }).click();
    expect(await groupBy(page)).toBeNull();
    await expect(headings(page)).toHaveCount(0);
    expect(search(page)).toBe("");
    await bar(page).getByRole("button", { name: "Redo", exact: true }).click();
    expect(await groupBy(page)).toBe("region");

    await page.reload();
    await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
    expect(await groupBy(page)).toBe("region");
    expect((await body(page))[0]).toBe("# east (2)");
    await toggle(page).click();
    await expect(radio(page, "region")).toBeChecked();
  });

  test("leaves out a grouping from the URL by a column the rows can't be grouped by", async ({ page }) => {
    const warnings: string[] = [];
    page.on("console", (msg) => {
      if (msg.type() === "warning") {
        warnings.push(msg.text());
      }
    });
    await ready(page, "group.html");
    await page.goto(`${page.url()}?g.group=pop`);
    await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
    expect(await groupBy(page)).toBeNull();
    expect(warnings.some((text) => text.includes('grouping by "pop" is left out'))).toBe(true);
  });

  test("starts grouped as set, and sticks the headings under the column labels as their rows go by", async ({
    page,
  }) => {
    const errors = await ready(page, "group-scroll.html");
    expect(await groupBy(page)).toBe("region");
    expect(await body(page)).toEqual([
      "# east (2)",
      "town_5",
      "town_11",
      "# north (4)",
      "town_1",
      "town_4",
      "town_7",
      "town_10",
      "# south (4)",
      "town_2",
      "town_6",
      "town_8",
      "town_12",
      "# (Missing) (2)",
      "town_3",
      "town_9",
    ]);
    const north = headings(page).nth(1).locator("th");
    await expect(north).toHaveCSS("position", "sticky");
    // Scroll town_7 up to the column labels: north's heading sticks there, over it (its own top
    // border under theirs)
    const thead = el(page).locator("thead");
    const town7 = el(page).locator("tbody tr", { has: page.locator('th:text-is("town_7")') });
    const by = (await rect(town7)).top - (await rect(thead)).bottom;
    await el(page)
      .locator(".gt-i-scroller")
      .evaluate((div, by) => (div.scrollTop += by), by);
    await expect
      .poll(async () => Math.abs((await rect(north)).top - (await rect(thead)).bottom))
      .toBeLessThanOrEqual(2);
    // (And south's isn't stuck)
    expect((await rect(headings(page).nth(2).locator("th"))).top).toBeGreaterThan((await rect(north)).bottom);

    // Grouped by another column, its headings stick
    await group(page, "size");
    await expect(headings(page).first().locator("th")).toHaveCSS("position", "sticky");
    expect(errors).toEqual([]);
  });
});
