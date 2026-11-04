import { expect, type Locator, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// The query box, in the control bar of a GTI table (the filters' table, 24 rows) whose view is
// filtered by every column (keeping 3 rows); and the same in a container 300px wide.

const VIEW = 'num >= 1000 and char contains "a" and fctr in ("eight", "one", "seven", "two")';

const el = (page: Page) => page.locator("gt-table");
const toggle = (page: Page) => el(page).getByRole("button", { name: "Edit the filters as text" });
const query = (page: Page) => el(page).getByRole("combobox", { name: "Filters as text" });
const list = (page: Page) => el(page).getByRole("listbox", { name: "Suggestions" });
const options = (page: Page) => list(page).getByRole("option");
const error = (page: Page) => el(page).locator(".gt-i-query-error");
const tokens = (page: Page) => el(page).getByRole("list", { name: "Filters" });
const live = (page: Page) => el(page).locator(".gt-i-live");
const matched = (page: Page) => el(page).evaluate((node) => (node as any).matchCount as number);
const box = (locator: Locator) =>
  locator.evaluate((node) => {
    const { left, right, top, bottom, width, height } = node.getBoundingClientRect();
    return { left, right, top, bottom, width, height };
  });
// The text each of the query's highlights has
const highlighted = (page: Page) =>
  page.evaluate(() =>
    Object.fromEntries(
      ["keyword", "string", "number", "error"].map((name) => [
        name,
        Array.from(CSS.highlights.get(`gt-i-query-${name}`) ?? [], (range) => range.toString()),
      ]),
    ),
  );

test("edits the filters as text, applied on Enter", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await toggle(page).click();
  await expect(query(page)).toBeFocused();
  await expect(query(page)).toHaveValue(VIEW);
  await expect(toggle(page)).toHaveAttribute("aria-expanded", "true");
  // (In the tokens' place)
  await expect(tokens(page)).toBeHidden();

  await query(page).fill("");
  await page.keyboard.type("num <= 10");
  await page.keyboard.press("Enter");
  await expect(query(page)).toBeHidden();
  await expect(toggle(page)).toBeFocused();
  await expect(tokens(page)).toBeVisible();
  await expect(tokens(page).locator(".gt-i-token-open")).toHaveText(["num ≤ 10"]);
  expect(await el(page).evaluate((node) => (node as any).filter)).toEqual({
    and: [{ col: "num", op: "lte", value: 10 }],
  });
  await expect(live(page)).toHaveText(/^Showing \d+ of 24 rows$/);
  expect(errors).toEqual([]);
});

test("shows a group of the text as a token, edited as text and removed", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await toggle(page).click();
  await query(page).fill('fctr in ("four", "one", "three", "two") and (num >= 100 OR not char contains "a")');
  await page.keyboard.press("Enter");
  await expect(query(page)).toBeHidden();
  // (Of each copy of exibble, "three" has no "a" and "four" is at least 100)
  expect(await matched(page)).toBe(6);
  const group = tokens(page).locator("li.gt-i-token[data-gti-group]");
  const text = 'num >= 100 or not char contains "a"';
  await expect(group.locator(".gt-i-token-open")).toHaveText(text);
  await expect(group).toHaveCSS("outline-style", "dashed");

  // (Opened in the query box with its text selected)
  await group.locator(".gt-i-token-open").click();
  await expect(query(page)).toBeFocused();
  const value = `fctr in ("four", "one", "three", "two") and (${text})`;
  await expect(query(page)).toHaveValue(value);
  expect(
    await query(page).evaluate((node: HTMLInputElement) => [node.selectionStart, node.selectionEnd]),
  ).toEqual([value.indexOf(text), value.indexOf(text) + text.length]);
  await page.keyboard.press("Escape");
  await expect(query(page)).toBeHidden();

  await tokens(page).getByRole("button", { name: `Remove the filter ${text}`, exact: true }).click();
  await expect(group).toHaveCount(0);
  expect(await matched(page)).toBe(12);
  expect(await el(page).evaluate((node) => (node as any).filter.and.map((item: any) => item.col))).toEqual([
    "fctr",
  ]);
  expect(errors).toEqual([]);
});

test("shows an is-null clause as a token saying the column's missing, edited as text and removed", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await toggle(page).click();
  await query(page).fill("");
  await page.keyboard.type("char is n");
  await expect(options(page)).toHaveText(["nullmissing", "not nullnot missing"]);
  await page.keyboard.press("ArrowDown");
  await page.keyboard.press("Enter");
  await expect(query(page)).toHaveValue("char is not null ");
  await page.keyboard.type("and num is null");
  await page.keyboard.press("Enter");
  await expect(query(page)).toBeHidden();
  // (Of each copy of exibble, `num` is NaN in one row, whose `char` isn't missing)
  expect(await matched(page)).toBe(3);
  expect(await el(page).evaluate((node) => (node as any).filter)).toEqual({
    and: [{ not: { col: "char", op: "is_null" } }, { col: "num", op: "is_null" }],
  });
  const groups = tokens(page).locator("li.gt-i-token[data-gti-group]");
  await expect(groups.locator(".gt-i-token-open")).toHaveText(["char is not missing", "num is missing"]);
  await expect(groups.first()).toHaveCSS("outline-style", "dashed");

  // (Opened in the query box with its text selected)
  await groups.nth(1).locator(".gt-i-token-open").click();
  await expect(query(page)).toBeFocused();
  const value = "char is not null and num is null";
  await expect(query(page)).toHaveValue(value);
  expect(
    await query(page).evaluate((node: HTMLInputElement) => [node.selectionStart, node.selectionEnd]),
  ).toEqual([value.indexOf("num"), value.length]);
  await page.keyboard.press("Escape");

  await tokens(page).getByRole("button", { name: "Remove the filter num is missing", exact: true }).click();
  await expect(groups).toHaveCount(1);
  // (Of each copy, `char` is missing in one row)
  expect(await matched(page)).toBe(21);
  expect(errors).toEqual([]);
});

test("highlights the text by what each part is, over the input's own", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await toggle(page).click();
  expect(await highlighted(page)).toEqual({
    keyword: [">=", "and", "contains", "and", "in"],
    string: ['"a"', '"eight"', '"one"', '"seven"', '"two"'],
    number: ["1000"],
    error: [],
  });
  // (The input's text is drawn by its copy, under it, but not its caret)
  await expect(query(page)).toHaveCSS("-webkit-text-fill-color", "rgba(0, 0, 0, 0)");
  const color = await query(page).evaluate((node) => getComputedStyle(node).color);
  await expect(query(page)).toHaveCSS("caret-color", color);
  const mirror = el(page).locator(".gt-i-query-mirror");
  await expect(mirror).toHaveText(`${VIEW} `);
  const [field, copy] = [await box(query(page)), await box(mirror)];
  expect(copy).toEqual(field);

  // (Its placeholder shows, though)
  await query(page).fill("");
  await expect(query(page)).not.toHaveCSS("-webkit-text-fill-color", "rgba(0, 0, 0, 0)");
  expect(errors).toEqual([]);
});

test("says what's wrong with text, marks where, and doesn't apply it", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await toggle(page).click();
  await query(page).fill("num >= lots and fctr in (1)");
  await page.keyboard.press("Enter");
  await expect(error(page)).toHaveText("Expected a number, or a date in double quotes");
  await expect(query(page)).toHaveAttribute("aria-invalid", "true");
  await expect(query(page)).toHaveAccessibleDescription("Expected a number, or a date in double quotes");
  await expect(live(page)).toHaveText("Expected a number, or a date in double quotes");
  expect((await highlighted(page)).error).toEqual(["lots"]);
  expect(await query(page).evaluate((node: HTMLInputElement) => node.selectionStart)).toBe(7);
  await expect(el(page).locator(".gt-i-query-field")).toHaveCSS("border-top-color", "rgb(198, 40, 40)");
  expect(await matched(page)).toBe(3);

  // (A clause the table can't have)
  await query(page).fill("num >= 1 and fctr in (1)");
  await expect(error(page)).toBeHidden();
  await page.keyboard.press("Enter");
  await expect(error(page)).toHaveText("1 isn't a value of fctr");
  expect((await highlighted(page)).error).toEqual(["fctr in (1)"]);

  // (One at the end, on the room after the text)
  await query(page).fill("num >=");
  await page.keyboard.press("Enter");
  await expect(error(page)).toHaveText("Expected a number, or a date in double quotes");
  expect((await highlighted(page)).error).toEqual([" "]);

  await query(page).fill('fctr in ("one")');
  await expect(query(page)).not.toHaveAttribute("aria-invalid");
  await page.keyboard.press("Enter");
  await expect(query(page)).toBeHidden();
  expect(await matched(page)).toBe(3);
  expect(errors).toEqual([]);
});

test("suggests what can go at the caret, above it, taken with Tab or Enter", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await toggle(page).click();
  await query(page).fill("");
  await page.keyboard.type("f");
  await expect(list(page)).toBeVisible();
  await expect(options(page)).toHaveText(["fctr"]);
  await expect(query(page)).toHaveAttribute("aria-expanded", "true");
  await page.keyboard.press("Tab");
  await expect(query(page)).toHaveValue("fctr ");
  await expect(query(page)).toBeFocused();
  // (Each with what it means, if it says)
  await expect(options(page)).toHaveText(["in (…)", "is nullmissing", "is not nullnot missing"]);
  await page.keyboard.press("Enter");
  await expect(query(page)).toHaveValue("fctr in (");
  await expect(options(page).first()).toHaveText("eight");
  await page.keyboard.type("tw");
  await expect(options(page)).toHaveText(["two"]);
  await page.keyboard.press("Enter");
  await expect(query(page)).toHaveValue('fctr in ("two"');
  await page.keyboard.type(", s");
  // (Those starting with what's typed first)
  await expect(options(page)).toHaveText(["seven", "six"]);
  await page.keyboard.press("ArrowDown");
  await expect(options(page).nth(1)).toHaveAttribute("aria-selected", "true");
  await expect(query(page)).toHaveAttribute("aria-activedescendant", (await options(page).nth(1).getAttribute("id")) ?? "");
  await page.keyboard.press("Enter");
  await expect(query(page)).toHaveValue('fctr in ("two", "six"');
  await page.keyboard.type(")");
  await expect(list(page)).toBeHidden();
  await page.keyboard.press("Enter");
  await expect(query(page)).toBeHidden();
  expect(await el(page).evaluate((node) => (node as any).filter)).toEqual({
    and: [{ col: "fctr", op: "in", value: ["six", "two"] }],
  });
  expect(errors).toEqual([]);
});

test("puts the suggestions above the text they're for, closing them on Escape", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await toggle(page).click();
  await query(page).fill("");
  await page.keyboard.type("num >= 1 and c");
  await expect(options(page)).toHaveText(["char", "fctr"]);
  const [shown, field] = [await box(list(page)), await box(el(page).locator(".gt-i-query-field"))];
  expect(shown.bottom).toBeLessThanOrEqual(field.top);
  expect(field.top - shown.bottom).toBeLessThan(8);
  // (Where the column starts)
  const start = await el(page)
    .locator(".gt-i-query-mirror")
    .evaluate((node) => {
      const range = document.createRange();
      range.setStart(node.firstChild as Text, "num >= 1 and ".length);
      return range.getBoundingClientRect().left;
    });
  expect(Math.abs(shown.left - start)).toBeLessThan(1);
  // (Not over the table's own colours)
  const background = await list(page).evaluate((node) => getComputedStyle(node).backgroundColor);
  expect(background).toBe("rgb(255, 255, 255)");

  await page.keyboard.press("Escape");
  await expect(list(page)).toBeHidden();
  await expect(query(page)).toBeVisible();
  await page.keyboard.press("Escape");
  await expect(query(page)).toBeHidden();
  await expect(toggle(page)).toBeFocused();
  expect(await matched(page)).toBe(3);
  expect(errors).toEqual([]);
});

test("closes as focus leaves it, unless it's been changed", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await toggle(page).click();
  await el(page).getByRole("button", { name: "Table info", exact: true }).focus();
  await expect(query(page)).toBeHidden();
  await toggle(page).click();
  await page.keyboard.type(" and");
  await el(page).getByRole("button", { name: "Table info", exact: true }).focus();
  await expect(query(page)).toBeVisible();
  expect(errors).toEqual([]);
});

test("uses lighter colours on a dark background", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await page.evaluate(() => {
    document.body.style.background = "#111";
    document.body.style.color = "#eee";
  });
  await toggle(page).click();
  await expect(el(page).locator(".gt-i-query")).toHaveAttribute("data-gti-dark", "");
  await query(page).fill("num >= x");
  await page.keyboard.press("Enter");
  await expect(error(page)).toHaveCSS("color", "rgb(255, 123, 114)");
  expect(errors).toEqual([]);
});

test("fits a narrow container, with long text scrolled under the input's", async ({ page }) => {
  const errors = await ready(page, "tokens-container.html");
  const container = await box(page.locator("body > div"));
  await toggle(page).click();
  const root = await box(el(page).locator(".gt-i-query"));
  expect(root.left).toBeGreaterThanOrEqual(container.left - 0.5);
  expect(root.right).toBeLessThanOrEqual(container.right + 0.5);
  // (At the end of the text, with the copy scrolled as far)
  const scroll = () =>
    el(page).evaluate((node) => {
      const input = node.querySelector(".gt-i-query input") as HTMLInputElement;
      const mirror = node.querySelector(".gt-i-query-mirror") as HTMLElement;
      return [input.scrollLeft, mirror.scrollLeft] as [number, number];
    });
  const [input, mirror] = await scroll();
  expect(input).toBeGreaterThan(0);
  expect(mirror).toBe(input);
  await page.keyboard.press("Home");
  expect(await scroll()).toEqual([0, 0]);
  await page.keyboard.press("End");
  await page.keyboard.type(" and ");
  const [after, copy] = await scroll();
  expect(after).toBeGreaterThan(input);
  expect(copy).toBe(after);

  // (The suggestions too, as wide as they need)
  await expect(list(page)).toBeVisible();
  const shown = await box(list(page));
  expect(shown.left).toBeGreaterThanOrEqual(container.left - 0.5);
  expect(shown.right).toBeLessThanOrEqual(container.right + 0.5);
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("has controls big enough to tap, and text big enough not to zoom", async ({ page }) => {
    const errors = await ready(page, "tokens.html");
    await toggle(page).tap();
    await expect(query(page)).toBeVisible();
    // (The field's buttons fill its height)
    expect((await box(toggle(page))).height).toBeGreaterThanOrEqual(44);
    expect((await box(el(page).locator(".gt-i-query-field"))).height).toBeGreaterThanOrEqual(44);
    for (const name of ["Apply the filters", "Cancel"]) {
      expect((await box(el(page).getByRole("button", { name }))).width).toBeGreaterThanOrEqual(44);
    }
    expect(Number.parseFloat(await query(page).evaluate((node) => getComputedStyle(node).fontSize))).toBeGreaterThanOrEqual(16);
    await query(page).fill("");
    await query(page).pressSequentially("fctr in (");
    await expect(options(page).first()).toBeVisible();
    expect((await box(options(page).first())).height).toBeGreaterThanOrEqual(44);
    await options(page).nth(1).tap();
    await expect(query(page)).toHaveValue('fctr in ("five"');
    await expect(query(page)).toBeFocused();
    await el(page).getByRole("button", { name: "Cancel" }).tap();
    await expect(query(page)).toBeHidden();
    expect(errors).toEqual([]);
  });
});
