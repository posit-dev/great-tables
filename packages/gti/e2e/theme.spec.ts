import { expect, type Page, test, type TestInfo } from "@playwright/test";
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// GT's themed tables, as the CSS variables draw them against the same tables as literal CSS (which
// is what GT drew before themes): the two must be pixel for pixel the same, and a table must go
// dark with the page's color scheme, or the host's theme, as designed. No pictures are kept, as fonts
// are drawn differently from one platform to the next: each test draws its reference itself.

const fixtures = join(dirname(fileURLToPath(import.meta.url)), ".fixtures", "theme");

const TABLES = ["plain", "stylized", "themed", "navy"];
// (A table with its own background colors, which "auto" mode leaves light, is left out of the tests of what goes dark)
const SWITCHING = ["plain", "themed", "navy"];
// (A table with colors written on its cells draws them as written in dark, so it is the same as its literal CSS only in light)
const CELLS = "cells";
// (A table with border colors set for both modes blends them in dark, so it is the same as its literal CSS only in light)
const BLENDED = ["stylized"];

type Scheme = "light" | "dark";
type Host = { body?: string; html?: string };
type PageParts = Host & { head?: string; around?: [string, string] };

// (A page that follows the reader's preference, as the pages GT makes do)
const FOLLOWS = { head: "<style>:root { color-scheme: light dark }</style>" };

const DARK: Host[] = [
  { body: 'data-jp-theme-light="false"' },
  { body: 'class="vscode-dark"' },
  { body: 'class="vscode-high-contrast"' },
  { body: 'class="quarto-dark"' },
  { html: 'data-bs-theme="dark"' },
  { body: 'class="dark-theme" data-theme="dark"' },
];
const LIGHT: Host[] = [
  { body: 'data-jp-theme-light="true"' },
  { body: 'class="vscode-light"' },
  { body: 'class="vscode-high-contrast vscode-high-contrast-light"' },
  { body: 'class="quarto-light"' },
  { html: 'data-bs-theme="light"' },
  { body: 'class="light-theme" data-theme="light"' },
];

const fragment = (name: string) => readFileSync(join(fixtures, `${name}.html`), "utf-8");

const pageHtml = ({ body = "", html = "", head = "", around = ["", ""] }: PageParts, content: string) =>
  `<!doctype html><html ${html}><head><meta charset="utf-8">${head}</head><body ${body}>${around[0]}${content}${around[1]}</body></html>`;

/** A table fragment (`<table>.<variant>`) in a page with the given `<html>` and `<body>` attributes and `<head>` (and elements around it), as a picture. */
async function shot(page: Page, name: string, { scheme, ...parts }: PageParts & { scheme: Scheme }): Promise<Buffer> {
  await page.emulateMedia({ colorScheme: scheme });
  await page.setContent(pageHtml(parts, fragment(name)));
  return page.locator(".gt_table").screenshot();
}

async function expectSame(a: Buffer, b: Buffer, testInfo: TestInfo, label = ""): Promise<void> {
  const same = a.equals(b);
  if (!same) {
    await testInfo.attach(`${label}-actual.png`, { body: a, contentType: "image/png" });
    await testInfo.attach(`${label}-expected.png`, { body: b, contentType: "image/png" });
  }
  expect(same, `${label}: the table isn't drawn as its literal CSS is`).toBe(true);
}

const lowContrast = (page: Page) =>
  page.evaluate(() => {
    // (An engine may serialize a mixed color as `color(srgb r g b)`, with channels from 0 to 1)
    const rgb = (s: string) => {
      const n = (s.match(/[\d.]+/g) ?? []).map(Number);
      return s.startsWith("color(srgb") ? n.map((v, i) => (i < 3 ? v * 255 : v)) : n;
    };
    const lum = ([r, g, b]: number[]) =>
      [r, g, b]
        .map((v) => (v as number) / 255)
        .map((v) => (v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4))
        .reduce((sum, v, i) => sum + v * [0.2126, 0.7152, 0.0722][i]!, 0);
    const background = (el: Element | null): number[] => {
      for (; el; el = el.parentElement) {
        const c = rgb(getComputedStyle(el).backgroundColor);
        if (c.length === 3 || c[3] === 1) return c;
      }
      return [255, 255, 255];
    };
    return [...document.querySelectorAll(".gt_table th, .gt_table td")]
      .filter((el) => el.textContent?.trim())
      .map((el) => {
        const [hi, lo] = [lum(rgb(getComputedStyle(el).color)), lum(background(el))].sort((a, b) => b - a);
        return { text: el.textContent!.trim().slice(0, 20), ratio: (hi! + 0.05) / (lo! + 0.05) };
      })
      .filter((cell) => cell.ratio < 4.5);
  });

test("variables render as today's CSS", async ({ page }, testInfo) => {
  for (const table of [...TABLES, CELLS]) {
    const auto = await shot(page, `${table}.auto`, { scheme: "light" });
    const literal = await shot(page, `${table}.light-literal`, { scheme: "light" });
    await expectSame(auto, literal, testInfo, table);
  }
});

test("a page that follows the preference takes the table with it", async ({ page }, testInfo) => {
  for (const table of SWITCHING) {
    for (const scheme of ["light", "dark"] as const) {
      const auto = await shot(page, `${table}.auto`, { scheme, ...FOLLOWS });
      const literal = await shot(page, `${table}.${scheme}-literal`, { scheme, ...FOLLOWS });
      await expectSame(auto, literal, testInfo, `${table} ${scheme}`);
    }
  }
});

test("a page with no color scheme keeps the table light under a dark preference", async ({ page }, testInfo) => {
  for (const table of [...SWITCHING, CELLS]) {
    const auto = await shot(page, `${table}.auto`, { scheme: "dark" });
    const literal = await shot(page, `${table}.light-literal`, { scheme: "dark" });
    await expectSame(auto, literal, testInfo, table);
  }
});

test("a dark page takes the table with it under a light preference", async ({ page }, testInfo) => {
  const dark = { head: "<style>:root { color-scheme: dark }</style>" };
  for (const table of SWITCHING) {
    const auto = await shot(page, `${table}.auto`, { scheme: "light", ...dark });
    const literal = await shot(page, `${table}.dark-literal`, { scheme: "light", ...dark });
    await expectSame(auto, literal, testInfo, table);
  }
});

test("a dark host wins over a light preference", async ({ page }, testInfo) => {
  for (const table of SWITCHING) {
    const literal = await shot(page, `${table}.dark-literal`, { scheme: "light" });
    for (const host of DARK) {
      const auto = await shot(page, `${table}.auto`, { scheme: "light", ...host });
      await expectSame(auto, literal, testInfo, `${table} ${JSON.stringify(host)}`);
    }
  }
});

test("a light host wins over a dark preference", async ({ page }, testInfo) => {
  for (const table of [...SWITCHING, CELLS]) {
    const literal = await shot(page, `${table}.light-literal`, { scheme: "dark", ...FOLLOWS });
    for (const host of LIGHT) {
      const auto = await shot(page, `${table}.auto`, { scheme: "dark", ...FOLLOWS, ...host });
      await expectSame(auto, literal, testInfo, `${table} ${JSON.stringify(host)}`);
    }
  }
});

test("the nearest host's theme wins", async ({ page }, testInfo) => {
  const nested: [PageParts, Scheme][] = [
    [{ html: 'data-bs-theme="dark"', around: ['<div data-bs-theme="light">', "</div>"] }, "light"],
    [{ html: 'data-bs-theme="light"', around: ['<div data-bs-theme="dark">', "</div>"] }, "dark"],
    [{ body: 'class="quarto-dark"', around: ['<div data-bs-theme="light">', "</div>"] }, "light"],
    [{ body: 'class="quarto-light"', around: ['<div data-bs-theme="dark">', "</div>"] }, "dark"],
  ];
  for (const table of SWITCHING) {
    for (const [host, scheme] of nested) {
      const auto = await shot(page, `${table}.auto`, { scheme: "light", ...host });
      const literal = await shot(page, `${table}.${scheme}-literal`, { scheme: "light", ...host });
      await expectSame(auto, literal, testInfo, `${table} ${JSON.stringify(host)}`);
    }
  }
});

test("a table with its own background colors stays light", async ({ page }, testInfo) => {
  const literal = await shot(page, "stylized.light-literal", { scheme: "dark", ...FOLLOWS });
  await expectSame(
    await shot(page, "stylized.auto", { scheme: "dark", ...FOLLOWS }),
    literal,
    testInfo,
    "preference",
  );
  await expectSame(
    await shot(page, "stylized.auto", { scheme: "dark", ...FOLLOWS, ...DARK[0]! }),
    literal,
    testInfo,
    "dark host",
  );
});

test("fixed modes ignore host and preference", async ({ page }, testInfo) => {
  for (const table of TABLES) {
    const light = await shot(page, `${table}.light`, { scheme: "dark", ...DARK[0]! });
    const lightLiteral = await shot(page, `${table}.light-literal`, { scheme: "dark", ...DARK[0]! });
    await expectSame(light, lightLiteral, testInfo, `${table} light`);
    if (BLENDED.includes(table)) {
      continue;
    }
    const dark = await shot(page, `${table}.dark`, { scheme: "light", ...LIGHT[0]! });
    const darkLiteral = await shot(page, `${table}.dark-literal`, { scheme: "light", ...LIGHT[0]! });
    await expectSame(dark, darkLiteral, testInfo, `${table} dark`);
  }
});

// The computed colors of an element (by selector) in a table fragment, as RGB channels from 0 to 255
async function colors(page: Page, name: string, scheme: Scheme, selector: string, properties: string[]) {
  await shot(page, name, { scheme, ...FOLLOWS });
  return page.locator(selector).first().evaluate((el, properties) => {
    // (An engine may serialize a mixed color as `color(srgb r g b)`, with channels from 0 to 1)
    const rgb = (s: string) => {
      const n = (s.match(/[\d.]+/g) ?? []).map(Number).slice(0, 3);
      return s.startsWith("color(srgb") ? n.map((v) => v * 255) : n;
    };
    const style = getComputedStyle(el);
    return properties.map((property) => rgb(style.getPropertyValue(property)));
  }, properties);
}

const blended = (color: number[], text: number[]) => color.map((v, i) => 0.35 * v + 0.65 * text[i]!);

function expectClose(actual: number[], expected: number[], label: string): void {
  expect(
    actual.every((v, i) => Math.abs(v - expected[i]!) <= 1),
    `${label}: ${actual} isn't ${expected.map(Math.round)}`,
  ).toBe(true);
}

test("border colors set for both modes are blended in dark", async ({ page }) => {
  // (A cell's border from `style.borders()`, black by default)
  const fig = "td:text-is('fig')";
  const [light] = await colors(page, "cells.auto", "light", fig, ["border-bottom-color"]);
  expect(light).toEqual([0, 0, 0]);
  const [dark, text] = await colors(page, "cells.auto", "dark", fig, ["border-bottom-color", "color"]);
  expectClose(dark!, blended([0, 0, 0], text!), "cell");

  // (A table's border color from `tab_options()`, here through `opt_stylize()`)
  const [literal] = await colors(page, "stylized.dark-literal", "light", ".gt_table", ["border-top-color"]);
  const [forced, tableText] = await colors(page, "stylized.dark", "light", ".gt_table", ["border-top-color", "color"]);
  expectClose(forced!, blended(literal!, tableText!), "table");
});

test("fills without contrast text get it in dark only", async ({ page }) => {
  // (The first row's `num` cell, with a white fill from `data_color(autocolor_text=False)`)
  const num = "td:text-is('0.11')";
  const [light] = await colors(page, "cells.auto", "light", num, ["color"]);
  const [table] = await colors(page, "cells.auto", "light", ".gt_table", ["color"]);
  expect(light).toEqual(table);
  const [dark] = await colors(page, "cells.auto", "dark", num, ["color"]);
  expect(dark).toEqual([51, 51, 51]);
});

test("a shadow root follows the page's color scheme only", async ({ page }) => {
  const background = async (parts: PageParts, scheme: Scheme) => {
    await page.emulateMedia({ colorScheme: scheme });
    await page.setContent(pageHtml(parts, '<div id="host"></div>'));
    await page.evaluate((html) => {
      document.getElementById("host")!.attachShadow({ mode: "open" }).innerHTML = html;
    }, fragment("plain.auto"));
    return page.locator(".gt_table").evaluate((el) => getComputedStyle(el).backgroundColor);
  };
  expect(await background(FOLLOWS, "dark")).toBe("rgb(30, 30, 30)");
  // (The host's theme isn't seen from inside it)
  expect(await background(DARK[0]!, "dark")).toBe("rgb(255, 255, 255)");
});

const PAGE_VARIABLES = "<style>:root { --gt-data-row-padding: 2px; --gt-color-border: #ff0000 }</style>";

test("page CSS sets variables", async ({ page }) => {
  await shot(page, "plain.auto", { scheme: "light", head: PAGE_VARIABLES });
  const cell = page.locator("td.gt_row").first();
  expect(await cell.evaluate((el) => getComputedStyle(el).paddingTop)).toBe("2px");
  expect(await cell.evaluate((el) => getComputedStyle(el).borderTopColor)).toBe("rgb(255, 0, 0)");
});

test("Python-set values beat page CSS", async ({ page }) => {
  await shot(page, "padded.auto", { scheme: "light", head: PAGE_VARIABLES });
  const cell = page.locator("td.gt_row").first();
  expect(await cell.evaluate((el) => getComputedStyle(el).paddingTop)).toBe("6px");
});

test("text is readable", async ({ page }) => {
  for (const table of [...TABLES, CELLS]) {
    for (const scheme of ["light", "dark"] as const) {
      await shot(page, `${table}.auto`, { scheme, ...FOLLOWS });
      expect(await lowContrast(page), `${table} ${scheme}`).toEqual([]);
    }
  }
});

test("gallery", async ({ page }, testInfo) => {
  for (const table of [...TABLES, CELLS]) {
    const pictures: Buffer[] = [];
    for (const scheme of ["light", "dark"] as const) {
      // (A table with its own background colors stays light in "auto" mode: its dark picture is the forced one)
      const picture = await shot(page, `${table}.${table === "stylized" && scheme === "dark" ? "dark" : "auto"}`, {
        scheme,
        ...FOLLOWS,
      });
      const path = testInfo.outputPath(`${table}-${scheme}.png`);
      writeFileSync(path, picture);
      await testInfo.attach(`${table}-${scheme}.png`, { path, contentType: "image/png" });
      pictures.push(picture);
    }
    expect(pictures[0]!.equals(pictures[1]!), `${table} looks the same in dark`).toBe(false);
  }
});
