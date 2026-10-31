import { afterEach, describe, expect, it, vi } from "vitest";
import { type BodyRow, define, GtTable, SPEC_VERSION, TAG_NAME } from "../src/index";

// Let mutation observers run.
const tick = () => new Promise((resolve) => setTimeout(resolve, 0));

async function mount(html: string): Promise<GtTable> {
  document.body.innerHTML = html;
  await tick();
  return document.querySelector(TAG_NAME) as GtTable;
}

const specScript = (spec: object | string) =>
  `<script type="application/json" data-gti-spec>${
    typeof spec === "string" ? spec : JSON.stringify(spec)
  }</script>`;

function makeSpec(nrows: number, body: BodyRow[]) {
  return {
    version: SPEC_VERSION,
    nrows,
    columns: [],
    spanners: [],
    stub: { columns: [], groups_as_column: false },
    groups: [],
    body,
    ranks: {},
  };
}

// A grouped table shaped like GT's: group "b" shows first, rows out of data order, summaries.
const groupedRows = [
  `<tr class="gt_group_heading_row"><th>b</th></tr>`,
  `<tr><th class="gt_row gt_stub">row_3</th></tr>`,
  `<tr><th class="gt_row gt_stub">row_1</th></tr>`,
  `<tr><th class="gt_summary_row">Total</th></tr>`,
  `<tr class="gt_group_heading_row"><th>a</th></tr>`,
  `<tr><th class="gt_row gt_stub">row_2</th></tr>`,
  `<tr><th class="gt_grand_summary_row">Max</th></tr>`,
];
const groupedBody: BodyRow[] = [
  { group: "b" },
  2,
  0,
  { summary: "Total", group: "b", side: "bottom" },
  { group: "a" },
  1,
  { grand_summary: "Max", side: "bottom" },
];

const table = (rows: string[]) =>
  `<div id="t"><table class="gt_table"><thead><tr><th>x</th></tr></thead>` +
  `<tbody class="gt_table_body">${rows.join("")}</tbody></table></div>`;

afterEach(() => {
  document.body.innerHTML = "";
  vi.restoreAllMocks();
});

describe("define()", () => {
  it("registers <gt-table> on import", () => {
    expect(customElements.get(TAG_NAME)).toBe(GtTable);
  });

  it("keeps the first registration when called again", () => {
    expect(define()).toBe(GtTable);
    expect(customElements.get(TAG_NAME)).toBe(GtTable);
  });

  it("returns the class already registered under the tag name", () => {
    class Other extends HTMLElement {}
    const registry = {
      get: (name: string) => (name === TAG_NAME ? Other : undefined),
      define: () => {
        throw new Error("should not be called");
      },
    } as unknown as CustomElementRegistry;
    expect(define(registry)).toBe(Other);
  });
});

describe("<gt-table>", () => {
  it("leaves a table without a spec static", async () => {
    const el = await mount(`<gt-table>${table([`<tr><td>1</td></tr>`])}</gt-table>`);
    expect(el).toBeInstanceOf(GtTable);
    expect(el.table).toBe(el.querySelector("table.gt_table"));
    expect(el.spec).toBeNull();
    expect(el.state).toBe("static");
  });

  it("marks itself empty when there is no table", async () => {
    const el = await mount(`<gt-table></gt-table>`);
    expect(el.table).toBeNull();
    expect(el.state).toBe("empty");
  });

  it("hydrates a table added after it was connected", async () => {
    const el = await mount(`<gt-table></gt-table>`);
    el.insertAdjacentHTML("beforeend", table(groupedRows) + specScript(makeSpec(3, groupedBody)));
    await tick();
    expect(el.table).toBe(el.querySelector("table"));
    expect(el.state).toBe("ready");
  });

  it("resets when removed from the document", async () => {
    const el = await mount(
      `<gt-table>${table(groupedRows)}${specScript(makeSpec(3, groupedBody))}</gt-table>`,
    );
    const tr = el.rowElement(0);
    el.remove();
    expect(el.table).toBeNull();
    expect(el.spec).toBeNull();
    expect(el.rowElement(0)).toBeNull();
    expect(el.bodyRow(tr as HTMLTableRowElement)).toBeNull();
    expect(el.hasAttribute("data-gti-state")).toBe(false);
  });

  it("hydrates again when moved", async () => {
    const el = await mount(
      `<gt-table>${table(groupedRows)}${specScript(makeSpec(3, groupedBody))}</gt-table>`,
    );
    const host = document.createElement("section");
    document.body.append(host);
    host.append(el);
    await tick();
    expect(el.table).toBe(el.querySelector("table"));
    expect(el.rowElement(1)?.textContent).toBe("row_2");
    expect(el.state).toBe("ready");
  });
});

describe("<gt-table> with a spec", () => {
  it("maps every body row to its spec entry", async () => {
    const spec = makeSpec(3, groupedBody);
    const el = await mount(`<gt-table>${table(groupedRows)}${specScript(spec)}</gt-table>`);

    expect(el.state).toBe("ready");
    expect(el.spec).toEqual(spec);

    const trs = Array.from(el.querySelectorAll("tbody tr")) as HTMLTableRowElement[];
    expect(trs.map((tr) => el.bodyRow(tr))).toEqual(groupedBody);
    for (const i of [0, 1, 2]) {
      expect(el.rowElement(i)?.textContent).toBe(`row_${i + 1}`);
    }
    expect(el.rowElement(3)).toBeNull();
    expect(el.bodyRow(el.querySelector("thead tr") as HTMLTableRowElement)).toBeNull();
  });

  it("only reads its own spec", async () => {
    // A nested <gt-table>'s spec isn't this one's.
    const el = await mount(
      `<gt-table>${table([])}<div>${specScript(makeSpec(1, [0]))}</div></gt-table>`,
    );
    expect(el.state).toBe("static");
  });

  it.each([
    ["an unusable spec", specScript("{"), /valid JSON/],
    ["another spec version", specScript({ ...makeSpec(3, groupedBody), version: 99 }), /version 99/],
    ["a spec for other rows", specScript(makeSpec(3, groupedBody.slice(1))), /7 rows .* 6/],
  ])("stays static and warns with %s", async (_, script, message) => {
    const warn = vi.spyOn(console, "warn").mockImplementation(() => {});
    const el = await mount(`<gt-table>${table(groupedRows)}${script}</gt-table>`);

    expect(el.state).toBe("error");
    expect(el.table).not.toBeNull();
    expect(el.spec).toBeNull();
    expect(el.rowElement(0)).toBeNull();
    expect(warn).toHaveBeenCalledOnce();
    expect(warn.mock.calls[0]?.[0]).toMatch(message);
  });
});
