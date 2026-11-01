import { expect, type Locator, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// exibble's num, currency (under a "Numbers" spanner) and char, with group headings (or groups as
// a column), searchable, 3 rows to a page, with resize handles; and the table of display.spec.ts
// without text wrapping (row 2's long char value in a column 90px wide), with resize handles.

const label = (page: Page, column: string) => page.locator(`gt-table th[id$="-${column}"]`);
const handle = (page: Page, column: string) => label(page, column).locator("> .gt-i-resizer");

/** The width of each body cell in the first data row shown. */
function widths(page: Page): Promise<number[]> {
  return page.locator("gt-table").evaluate((node) => {
    const el = node as any;
    const tr = Array.from(node.querySelectorAll<HTMLTableRowElement>("tbody.gt_table_body > tr")).find(
      (tr) => typeof el.bodyRow(tr) === "number" && tr.getClientRects().length > 0,
    ) as HTMLTableRowElement;
    return Array.from(tr.cells, (cell) => cell.getBoundingClientRect().width);
  });
}

const tableWidth = (page: Page) =>
  page.locator("gt-table table").evaluate((table) => table.getBoundingClientRect().width);

// (Once the page has laid out and painted, with any resize observers run)
const settled = (page: Page) =>
  page.evaluate(() => new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve))));

/** Drag a handle across by `dx` with the mouse. */
async function drag(page: Page, target: Locator, dx: number) {
  const box = (await target.boundingBox()) as { x: number; y: number; width: number; height: number };
  const x = box.x + box.width / 2;
  const y = box.y + box.height / 2;
  await page.mouse.move(x, y);
  await page.mouse.down();
  await page.mouse.move(x + dx, y, { steps: 5 });
  await page.mouse.up();
}

/** The resize events the table fires, from now on. */
async function resizes(page: Page) {
  await page.locator("gt-table").evaluate((node) => {
    (window as any).resizes = [];
    node.addEventListener("gt-table-resize", (event) => (window as any).resizes.push((event as CustomEvent).detail));
  });
  return () => page.evaluate(() => (window as any).resizes);
}

// The widths a column gets once the reader resizes one: whole pixels, rounded up
const px = (width: number) => Math.ceil(width - 0.01);

const near = (actual: number[], expected: number[]) => {
  expect(actual).toHaveLength(expected.length);
  actual.forEach((width, i) => expect(Math.abs(width - (expected[i] as number))).toBeLessThan(1));
};

test.describe("resizing by mouse", () => {
  test("widens and narrows a column, leaving the others and the sort alone", async ({ page }) => {
    const errors = await ready(page, "resize.html");
    const events = await resizes(page);
    const [stub, num, currency, char] = (await widths(page)) as [number, number, number, number];
    const before = await tableWidth(page);

    await drag(page, handle(page, "num"), 60);
    near(await widths(page), [stub, num + 60, currency, char]);
    expect(Math.abs((await tableWidth(page)) - (before + 60))).toBeLessThan(4);
    // The label is as wide as its column
    near([await label(page, "num").evaluate((th) => th.getBoundingClientRect().width)], [px(num) + 60]);

    await drag(page, handle(page, "char"), -20);
    near(await widths(page), [stub, num + 60, currency, char - 20]);
    // (No sort on the way)
    await expect(page.locator("gt-table th[aria-sort]")).toHaveCount(0);
    expect(await events()).toEqual([
      { column: "num", index: 1, width: px(num) + 60 },
      { column: "char", index: 3, width: px(char) - 20 },
    ]);
    expect(errors).toEqual([]);
  });

  test("makes a column no narrower than 2em", async ({ page }) => {
    const errors = await ready(page, "resize.html");
    await drag(page, handle(page, "currency"), -500);
    const em = await label(page, "currency").evaluate((th) => parseFloat(getComputedStyle(th).fontSize));
    expect((await widths(page))[2]).toBeCloseTo(Math.ceil(2 * em), 0);
    expect(errors).toEqual([]);
  });

  test("shows the cursor and selects no text while dragging", async ({ page }) => {
    await ready(page, "resize.html");
    const target = handle(page, "num");
    const box = (await target.boundingBox()) as { x: number; y: number; width: number; height: number };
    await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
    await page.mouse.down();
    await page.mouse.move(box.x + 200, box.y + 200, { steps: 5 });
    const el = page.locator("gt-table");
    await expect(el).toHaveAttribute("data-gti-resizing", "");
    expect(await page.locator("gt-table td").first().evaluate((td) => getComputedStyle(td).cursor)).toBe("col-resize");
    expect(await page.evaluate(() => String(getSelection()))).toBe("");
    await page.mouse.up();
    await expect(el).not.toHaveAttribute("data-gti-resizing");
  });

  test("puts a column back with a double-click", async ({ page }) => {
    await ready(page, "resize.html");
    const before = await widths(page);
    await drag(page, handle(page, "num"), 60);
    await handle(page, "num").dblclick();
    near(await widths(page), before);
  });
});

test.describe("resized columns", () => {
  test("keep their widths as the window resizes, the table scrolling in its container", async ({ page }) => {
    const errors = await ready(page, "resize.html");
    await drag(page, handle(page, "char"), 300);
    const after = await widths(page);

    await page.setViewportSize({ width: 360, height: 700 });
    await settled(page);
    near(await widths(page), after);
    const wrapper = page.locator("gt-table table").locator("..");
    expect(await wrapper.evaluate((div) => div.scrollWidth > div.clientWidth)).toBe(true);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);

    await page.setViewportSize({ width: 1280, height: 720 });
    await settled(page);
    near(await widths(page), after);
    expect(errors).toEqual([]);
  });

  test("keep their widths across pages, searches and sorts", async ({ page }) => {
    const errors = await ready(page, "resize.html");
    await drag(page, handle(page, "num"), 40);
    const after = await widths(page);
    await page.getByRole("button", { name: "Next", exact: true }).click();
    near(await widths(page), after);
    await page.getByRole("searchbox").fill("e");
    await settled(page);
    near(await widths(page), after);
    await label(page, "char").getByRole("button").click();
    near(await widths(page), after);
    expect(errors).toEqual([]);
  });

  test("leave the group column alone when groups are a column", async ({ page }) => {
    const errors = await ready(page, "resize-column.html");
    const events = await resizes(page);
    // (No handle on the label over the group column and the stub)
    await expect(page.locator("gt-table .gt-i-resizer")).toHaveCount(3);
    const [group, stub, num, currency, char] = (await widths(page)) as [number, number, number, number, number];
    await drag(page, handle(page, "currency"), 50);
    near(await widths(page), [group, stub, num, currency + 50, char]);
    expect(await events()).toEqual([{ column: "currency", index: 3, width: px(currency) + 50 }]);
    expect(errors).toEqual([]);
  });
});

test.describe("resizing by keyboard", () => {
  test("follows each column's sort button in the tab order, and steps with the arrow keys", async ({ page }) => {
    const errors = await ready(page, "resize.html");
    const events = await resizes(page);
    const num = (await widths(page))[1] as number;
    await label(page, "num").getByRole("button").focus();
    await page.keyboard.press("Tab");
    const target = page.getByRole("separator", { name: "Resize num" });
    await expect(target).toBeFocused();
    // A focus ring, as for the sort buttons
    expect(await target.evaluate((node) => getComputedStyle(node).outlineStyle)).toBe("solid");

    await page.keyboard.press("ArrowRight");
    await page.keyboard.press("Shift+ArrowRight");
    near([(await widths(page))[1] as number], [px(num) + 60]);
    await expect(target).toHaveAttribute("aria-valuenow", String(px(num) + 60));
    await page.keyboard.press("ArrowLeft");
    near([(await widths(page))[1] as number], [px(num) + 50]);
    await page.keyboard.press("Enter");
    near([(await widths(page))[1] as number], [px(num)]);
    // (Enter doesn't sort)
    await expect(page.locator("gt-table th[aria-sort]")).toHaveCount(0);
    expect((await events()).map((detail: { width: number }) => detail.width)).toEqual(
      [10, 60, 50, 0].map((dx) => px(num) + dx),
    );
    expect(errors).toEqual([]);
  });
});

test.describe("resizing by touch", () => {
  test.use({ hasTouch: true, viewport: { width: 360, height: 700 } });

  test("drags a handle a finger can hit, without scrolling", async ({ page }) => {
    const errors = await ready(page, "resize.html");
    const target = handle(page, "num");
    expect((await target.boundingBox())?.width).toBe(24);
    const num = (await widths(page))[1] as number;
    const box = (await target.boundingBox()) as { x: number; y: number; width: number; height: number };
    const x = box.x + box.width / 2;
    const y = box.y + box.height / 2;

    // A real touch drag, which would scroll the table's container if the handle let it
    const cdp = await page.context().newCDPSession(page);
    const touch = (type: "touchStart" | "touchMove" | "touchEnd", points: { x: number; y: number }[]) =>
      cdp.send("Input.dispatchTouchEvent", { type, touchPoints: points });
    await touch("touchStart", [{ x, y }]);
    for (let dx = 10; dx <= 80; dx += 10) {
      await touch("touchMove", [{ x: x + dx, y }]);
    }
    await touch("touchEnd", []);
    await settled(page);

    near([(await widths(page))[1] as number], [px(num) + 80]);
    const wrapper = page.locator("gt-table table").locator("..");
    expect(await wrapper.evaluate((div) => div.scrollLeft)).toBe(0);
    expect(await page.evaluate(() => scrollX)).toBe(0);
    await expect(page.locator("gt-table th[aria-sort]")).toHaveCount(0);
    expect(errors).toEqual([]);
  });
});

test.describe("resizing without text wrapping", () => {
  const cut = (page: Page) =>
    page
      .locator("gt-table td", { hasText: "a coconut, cracked open at noon" })
      .evaluate((td) => td.scrollWidth > td.clientWidth);

  test("starts from the author's width, and shows or cuts text as the column changes", async ({ page }) => {
    const errors = await ready(page, "resize-nowrap.html");
    // (Stub, num, char, currency)
    expect((await widths(page))[2]).toBeCloseTo(90, 0);
    expect(await cut(page)).toBe(true);
    await drag(page, handle(page, "char"), 200);
    expect(await cut(page)).toBe(false);
    await drag(page, handle(page, "char"), -150);
    expect(await cut(page)).toBe(true);
    expect(errors).toEqual([]);
  });
});
