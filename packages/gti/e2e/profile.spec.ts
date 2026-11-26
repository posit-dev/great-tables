import { expect, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// Column profiles: exibble (8 rows, grp_b then grp_a), searchable (from the bar) and filtered by
// fctr (a facet), with profiles under the labels of num (a histogram, with a NaN), char (its most
// common values: each in one row, with a missing value), fctr (each in one row), date (a histogram
// of datetimes) and kind (red in 2 rows, 6 others in 1 each), and none under currency's. In a
// container 800px wide; and stacked in one 360px wide.

const el = (page: Page) => page.locator("gt-table");
const th = (page: Page, column: string) => page.locator(`th#f-${column}`);
const profile = (page: Page, column: string) => th(page, column).locator(".gt-i-profile");
const caption = (page: Page, column: string) => profile(page, column).locator(".gt-i-profile-text");
const searchBox = (page: Page) => el(page).locator("input.gt-i-search");
// (From the bar, where the search is behind a button)
const search = async (page: Page, text: string) => {
  if (!(await searchBox(page).isVisible())) {
    await el(page).getByRole("button", { name: "Search the table" }).click();
  }
  await searchBox(page).fill(text);
};
const live = (page: Page) => el(page).locator(".gt-i-live");
const filterButton = (page: Page) => el(page).getByRole("button", { name: /^Filter fctr( \(on\))?$/ });
const panel = (page: Page) => el(page).getByRole("group", { name: "Filter fctr", exact: true });

const PROFILED = ["num", "char", "fctr", "date", "kind"];

/** Each column's caption. */
const captions = (page: Page) => Promise.all(PROFILED.map((column) => caption(page, column).textContent()));

/** A column's bars (a strip's parts' tracks aside), and their heights. */
const bars = (page: Page, column: string) => profile(page, column).locator("svg rect:not(.gt-i-profile-track)");
const heights = (page: Page, column: string) =>
  bars(page, column).evaluateAll((rects) => rects.map((rect) => Number(rect.getAttribute("height"))));

const tip = (page: Page) => el(page).locator(":scope > .gt-i-profile-tip");

/** The tooltip of a column's bar `i` (its value or range, then its rows), the mouse over the bar's middle. */
async function tipOf(page: Page, column: string, i: number): Promise<string> {
  const box = await profile(page, column).locator("svg").boundingBox();
  const bar = await bars(page, column).nth(i).boundingBox();
  if (box === null || bar === null) {
    throw new Error("no plot");
  }
  await page.mouse.move(bar.x + bar.width / 2, box.y + box.height / 2);
  await expect(tip(page)).toBeVisible();
  return tip(page).evaluate((shown) => `${shown.firstChild?.textContent}: ${shown.lastChild?.textContent}`);
}

/** Each of a column's bars' tooltips. */
async function tips(page: Page, column: string): Promise<string[]> {
  const n = await bars(page, column).count();
  const all: string[] = [];
  for (let i = 0; i < n; i++) {
    all.push(await tipOf(page, column, i));
  }
  return all;
}

const view = (page: Page, column: string) => el(page).getByRole("group", { name: `Profile of ${column}`, exact: true });

test.describe("column profiles", () => {
  test("are drawn under the labels of the columns with them, of the whole table", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    expect(await captions(page)).toEqual([
      "0.11 – 8,880,000.00 · 13% missing",
      "7 values · 13% missing",
      "8 values",
      "2015/01/15 – 2015/08/15 · 13% missing",
      "7 values",
    ]);
    for (const column of PROFILED) {
      await expect(profile(page, column)).toBeVisible();
      await expect(profile(page, column)).toHaveRole("button");
      await expect(profile(page, column)).toHaveAccessibleName(`Show the profile of ${column}`);
    }
    // A histogram of 20 bins, from the lowest number to the highest, then the missing values' bar
    const num = await heights(page, "num");
    expect(num).toHaveLength(21);
    expect([num[0], num[19], num[20]]).toEqual([1, 0.2, 0.2]);
    expect(await tipOf(page, "num", 0)).toBe("0.111 – 444K: 5 rows (63%)");
    expect(await tipOf(page, "num", 19)).toBe("8.44M – 8.88M: 1 row (13%)");
    expect(await tipOf(page, "num", 20)).toBe("Missing: 1 row (13%)");
    // The values most rows have, then those in one row each, by their text in the table
    expect(await tips(page, "kind")).toEqual(["red: 2 rows (25%)", "6 unique values: 6 rows (75%)"]);
    expect(await tipOf(page, "date", 0)).toBe("Jan 15, 2015 – Jan 25, 2015: 1 row (13%)");
    // An empty one under the labels without one, so that the labels line up
    await expect(profile(page, "currency").locator("svg")).toHaveCount(0);
    await expect(th(page, "currency")).not.toHaveClass(/gt-i-profiled/);
    expect(errors).toEqual([]);
  });

  test("draw the most common values as a strip, with the names that fit in it; or say a column's values are each in one row", async ({
    page,
  }) => {
    const errors = await ready(page, "profile.html");
    // kind's parts, each as wide as its share of the column, with its name in it, within the part
    const parts = await th(page, "kind").evaluate((cell) => {
      const plot = (cell.querySelector(".gt-i-profile svg") as SVGElement).getBoundingClientRect();
      const rects = Array.from(cell.querySelectorAll(".gt-i-profile svg rect:not(.gt-i-profile-track)"), (rect) => rect.getBoundingClientRect());
      const names = Array.from(cell.querySelectorAll<HTMLElement>(".gt-i-profile-names > span"), (name) => ({
        text: name.textContent,
        box: name.getBoundingClientRect(),
      }));
      return {
        shares: rects.map((rect) => rect.width / plot.width),
        names: names.map((name) => name.text),
        inside: names.every((name, i) => {
          const rect = rects[i] as DOMRect;
          return name.box.left >= rect.left - 1 && name.box.right <= rect.right + 1 && name.box.top >= plot.top && name.box.bottom <= plot.bottom + 0.5;
        }),
      };
    });
    // (Less a sliver between them)
    expect(parts).toEqual({ shares: [expect.closeTo(0.25, 1), expect.closeTo(0.75, 1)], names: ["red", "unique"], inside: true });
    // char's and fctr's values are each in one row: said in an outline, as high as a plot, without one
    for (const [column, text] of [
      ["char", "7 unique values"],
      ["fctr", "8 unique values"],
    ] as const) {
      const pill = profile(page, column).locator(".gt-i-profile-pill");
      await expect(pill).toHaveText(text);
      await expect(profile(page, column).locator("svg")).toBeHidden();
      await expect(profile(page, column).locator(".gt-i-profile-names")).toHaveCount(0);
      expect((await pill.boundingBox())?.height).toBeCloseTo((await profile(page, "kind").locator("svg").boundingBox())?.height ?? 0, 0);
      // (With no tooltip)
      await pill.hover();
      await page.waitForTimeout(100);
      await expect(tip(page)).toBeHidden();
    }
    // A histogram's missing values' bar is red, marked "∅" under it, clear of the caption
    const num = await th(page, "num").evaluate((cell) => {
      const rect = (Array.from(cell.querySelectorAll(".gt-i-profile svg rect")).pop() as SVGRectElement).getBoundingClientRect();
      const mark = cell.querySelector(".gt-i-profile-null") as HTMLElement;
      const box = mark.getBoundingClientRect();
      const caption = cell.querySelector(".gt-i-profile-text") as HTMLElement;
      const text = caption.getBoundingClientRect();
      const end = text.right - parseFloat(getComputedStyle(caption).paddingRight);
      return {
        text: mark.textContent,
        color: getComputedStyle(mark).color,
        fill: getComputedStyle(cell.querySelector(".gt-i-profile rect.gt-i-profile-missing") as Element).fill,
        under: Math.abs(box.left + box.width / 2 - (rect.left + rect.width / 2)) < 1 && box.top >= rect.bottom,
        clear: end <= box.left,
      };
    });
    expect(num).toEqual({ text: "∅", color: "rgb(217, 48, 37)", fill: "rgb(217, 48, 37)", under: true, clear: true });
    expect(errors).toEqual([]);
  });

  test("line up under the labels", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    const boxes = await el(page)
      .locator("thead tr.gt_col_headings th")
      .evaluateAll((cells) =>
        cells.map((cell) => {
          const slot = cell.querySelector(".gt-i-profile") as HTMLElement;
          return { bottom: cell.getBoundingClientRect().bottom, top: slot.getBoundingClientRect().top, height: slot.offsetHeight };
        }),
      );
    // (The stubhead's, the six columns')
    expect(boxes).toHaveLength(7);
    for (const box of boxes) {
      expect(box.bottom).toBeCloseTo(boxes[0]?.bottom as number, 0);
      expect(box.top).toBeCloseTo(boxes[0]?.top as number, 0);
      expect(box.height).toBe(boxes[0]?.height);
    }
    // (Within its cell, across it)
    const inside = await th(page, "kind").evaluate((cell) => {
      const outer = cell.getBoundingClientRect();
      const svg = (cell.querySelector(".gt-i-profile svg") as SVGElement).getBoundingClientRect();
      return svg.left >= outer.left && svg.right <= outer.right && svg.width > outer.width / 2;
    });
    expect(inside).toBe(true);
    expect(errors).toEqual([]);
  });

  test("count the rows a search keeps", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    await search(page, "fig");
    await expect(live(page)).toHaveText("Showing 1 of 8 rows");
    await expect(caption(page, "num")).toHaveText("100% missing");
    expect(await captions(page)).toEqual(["100% missing", "1 value", "1 value", "2015/06/15", "1 value"]);
    await expect(profile(page, "char").locator(".gt-i-profile-pill")).toHaveText("1 unique value");
    // (Its part filled as high as its share of its rows the search keeps)
    expect(await heights(page, "kind")).toEqual([0, 1 / 6]);

    await search(page, "zzz");
    await expect(caption(page, "num")).toHaveText("No rows");
    expect((await heights(page, "num")).every((height) => height === 0)).toBe(true);

    await search(page, "");
    await expect(caption(page, "num")).toHaveText("0.11 – 8,880,000.00 · 13% missing");
    expect(errors).toEqual([]);
  });

  test("count the rows a filter keeps, in its own column too", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    await filterButton(page).click();
    await panel(page).getByRole("checkbox", { name: /^one\b/ }).check();
    await panel(page).getByRole("checkbox", { name: /^five\b/ }).check();
    await expect(live(page)).toHaveText("Showing 2 of 8 rows");
    expect(await captions(page)).toEqual([
      "0.11 – 5,550.00",
      "1 value · 50% missing",
      "2 values",
      "2015/01/15 – 2015/05/15",
      "2 values",
    ]);
    await expect(profile(page, "fctr").locator(".gt-i-profile-pill")).toHaveText("2 unique values");
    // (Its panel closed, which is over the profile)
    await page.keyboard.press("Escape");
    await expect(panel(page)).toBeHidden();
    expect(await tips(page, "kind")).toEqual(["red: 1 row (50%)", "6 unique values: 1 row (50%)"]);
    expect(errors).toEqual([]);
  });

  test("stay as they are as the rows are sorted, and aren't a way to sort", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    const before = await Promise.all(PROFILED.map((column) => heights(page, column)));
    await th(page, "num").locator("button.gt-i-sort").click();
    await expect(th(page, "num")).toHaveAttribute("aria-sort", "ascending");
    expect(await Promise.all(PROFILED.map((column) => heights(page, column)))).toEqual(before);

    await profile(page, "kind").locator("svg").click();
    await profile(page, "char").locator(".gt-i-profile-pill").click();
    await profile(page, "date").locator(".gt-i-profile-text").click();
    await expect(th(page, "kind")).not.toHaveAttribute("aria-sort");
    await expect(th(page, "char")).not.toHaveAttribute("aria-sort");
    await expect(th(page, "date")).not.toHaveAttribute("aria-sort");
    await expect(th(page, "num")).toHaveAttribute("aria-sort", "ascending");
    expect(errors).toEqual([]);
  });

  test("have their edge bars' tooltips, not the resize handles beside them, which are still in the labels' padding", async ({
    page,
  }) => {
    const errors = await ready(page, "profile.html");
    for (const column of PROFILED) {
      const hits = await th(page, column).evaluate((cell) => {
        // (Or what says its values are each in one row, instead)
        const plot = (cell.querySelector(".gt-i-profile-pill") ?? (cell.querySelector(".gt-i-profile svg") as Element)).getBoundingClientRect();
        const y = plot.top + plot.height / 2;
        const at = (x: number) => {
          const hit = document.elementFromPoint(x, y);
          return hit?.closest(".gt-i-profile") !== null ? "profile" : (hit?.className ?? null);
        };
        return [at(plot.left + 1), at(plot.right - 1), at(cell.getBoundingClientRect().right - 1)];
      });
      expect(hits).toEqual(["profile", "profile", "gt-i-resizer"]);
    }
    expect(errors).toEqual([]);
  });

  test("show a bar's tooltip within the element, with a line to the bar (its foot, from under the label)", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    // Where the tooltip is, and the line's end from the bar's top's middle and from its foot's (in
    // whole px, -0 as 0)
    const place = async (column: string, i: number) => {
      await tipOf(page, column, i);
      return el(page).evaluate(
        (host, [name, at]) => {
          const box = host.getBoundingClientRect();
          const shown = (host.querySelector(":scope > .gt-i-profile-tip") as HTMLElement).getBoundingClientRect();
          const lead = host.querySelector(":scope > .gt-i-profile-lead") as HTMLElement;
          const angle = parseFloat(/rotate\(([-\d.e]+)rad\)/.exec(lead.style.transform)?.[1] ?? "NaN");
          const length = parseFloat(lead.style.width);
          const x = box.left + parseFloat(lead.style.left) + length * Math.cos(angle);
          const y = box.top + parseFloat(lead.style.top) + length * Math.sin(angle);
          const bar = (host.querySelectorAll(`th#f-${name} .gt-i-profile rect`)[at] as SVGRectElement).getBoundingClientRect();
          const label = (host.querySelector(`th#f-${name}`) as HTMLElement).getBoundingClientRect();
          return {
            inside: shown.left >= box.left && shown.right <= box.right && shown.top >= box.top && shown.bottom <= box.bottom,
            side: shown.top > label.bottom ? "under" : shown.bottom < label.top ? "over" : "across",
            dx: Math.round(x - (bar.left + bar.width / 2)) + 0,
            top: Math.round(y - bar.top) + 0,
            foot: Math.round(y - bar.bottom) + 0,
          };
        },
        [column, i] as const,
      );
    };
    // (Under the labels, at the element's top)
    for (const [column, i] of [
      ["num", 0],
      ["num", 19],
      ["date", 0],
    ] as const) {
      expect(await place(column, i)).toEqual({ inside: true, side: "under", dx: 0, top: expect.any(Number), foot: 0 });
    }
    // (Over them, with room)
    await el(page).evaluate((host) => (host.style.paddingTop = "60px"));
    await page.mouse.move(0, 0);
    expect(await place("num", 19)).toEqual({ inside: true, side: "over", dx: 0, top: 0, foot: expect.any(Number) });
    // (And it goes as the mouse leaves)
    await page.mouse.move(0, 0);
    await expect(tip(page)).toBeHidden();
    expect(errors).toEqual([]);
  });

  test("open a larger view on a double click, under the label, which reads out its bars", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    await profile(page, "num").locator("svg").dblclick();
    await expect(view(page, "num")).toBeVisible();
    await expect(profile(page, "num")).toHaveAttribute("aria-expanded", "true");
    await expect(view(page, "num").locator(".gt-i-profile-sum")).toHaveText("8 rows · 0.11 – 8,880,000.00 · 13% missing");
    await expect(view(page, "num").locator(".gt-i-profile-x > span")).toHaveText(["0.111", "4.44M", "8.88M"]);
    const boxes = await el(page).evaluate((host) => {
      const panel = host.querySelector(":scope > .gt-i-profile-panel") as HTMLElement;
      const bars = Array.from(panel.querySelectorAll<HTMLElement>(".gt-i-profile-plot > i"), (bar) => bar.offsetHeight);
      const [plotBox, apart] = Array.from(panel.querySelectorAll(".gt-i-profile-plot"), (part) => part.getBoundingClientRect());
      const mark = (panel.querySelector(".gt-i-profile-chart > .gt-i-profile-null") as HTMLElement).getBoundingClientRect();
      const plot = (panel.querySelector(".gt-i-profile-plot") as HTMLElement).clientHeight;
      const box = panel.getBoundingClientRect();
      const label = (host.querySelector("th#f-num") as HTMLElement).getBoundingClientRect();
      const outer = host.getBoundingClientRect();
      return {
        bars,
        plot,
        top: box.top - label.bottom,
        inside: box.left >= outer.left && box.right <= outer.right,
        // (The missing values' bar after the plot, apart, on its foot, and "∅" under it)
        apart: [Math.round((apart as DOMRect).left - (plotBox as DOMRect).right) > 0, (apart as DOMRect).bottom === (plotBox as DOMRect).bottom],
        mark: Math.abs(mark.left + mark.width / 2 - ((apart as DOMRect).left + (apart as DOMRect).width / 2)) < 1 && mark.top >= (apart as DOMRect).bottom,
      };
    });
    // (A bin of a few rows still seen)
    expect(boxes.bars[0]).toBe(boxes.plot);
    expect(boxes.bars[19]).toBeGreaterThanOrEqual(2);
    expect(boxes.bars[19]).toBeLessThan(boxes.plot);
    expect(boxes.top).toBeCloseTo(4, 0);
    expect(boxes.inside).toBe(true);
    expect(boxes.bars).toHaveLength(21);
    expect(boxes.bars[20]).toBe(boxes.bars[19]);
    expect(boxes.apart).toEqual([true, true]);
    expect(boxes.mark).toBe(true);
    await view(page, "num").locator(".gt-i-profile-plot").nth(1).hover();
    await expect(view(page, "num").locator(".gt-i-profile-read")).toHaveText("Missing: 1 row (13%)");

    const plot = view(page, "num").locator(".gt-i-profile-plot").first();
    const box = await plot.boundingBox();
    await page.mouse.move((box?.x ?? 0) + (box?.width ?? 0) - 1, (box?.y ?? 0) + 10);
    await expect(view(page, "num").locator(".gt-i-profile-read")).toHaveText("8.44M – 8.88M: 1 row (13%)");
    await plot.focus();
    await page.keyboard.press("Home");
    await expect(view(page, "num").locator(".gt-i-profile-read")).toHaveText("0.111 – 444K: 5 rows (63%)");

    // Escape closes it, back to its profile; a press outside it does too
    await page.keyboard.press("Escape");
    await expect(view(page, "num")).toBeHidden();
    await expect(profile(page, "num")).toBeFocused();
    await page.keyboard.press("Enter");
    await expect(view(page, "num")).toBeVisible();
    await page.mouse.click(5, 5);
    await expect(view(page, "num")).toBeHidden();
    expect(errors).toEqual([]);
  });

  test("aren't shown in a stacked table", async ({ page }) => {
    const errors = await ready(page, "profile-stack.html");
    await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
    for (const column of PROFILED) {
      await expect(profile(page, column)).toBeHidden();
    }
    // (And are, once its container is wide enough for a table, counting the rows a search keeps:
    // made in the "Filter & sort" sheet, which the narrow bar folds the search into)
    await el(page).getByRole("button", { name: "Filter & sort" }).click();
    await page.getByRole("dialog").getByRole("searchbox").fill("fig");
    await page.getByRole("dialog").getByRole("button", { name: "Done" }).click();
    await page.locator("body > div").evaluate((div) => ((div as HTMLElement).style.width = "800px"));
    await expect(el(page)).not.toHaveAttribute("data-gti-stacked");
    await expect(profile(page, "char")).toBeVisible();
    await expect(caption(page, "char")).toHaveText("1 value");
    expect(errors).toEqual([]);
  });
});
