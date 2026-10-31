import { afterEach, describe, expect, it } from "vitest";
import { define, GtTable, TAG_NAME } from "../src/index";

// Let mutation observers run.
const tick = () => new Promise((resolve) => setTimeout(resolve, 0));

async function mount(html: string): Promise<GtTable> {
  document.body.innerHTML = html;
  await tick();
  return document.querySelector(TAG_NAME) as GtTable;
}

afterEach(() => {
  document.body.innerHTML = "";
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
  it("finds the static table it wraps", async () => {
    const el = await mount(
      `<gt-table><div id="t"><table class="gt_table"><tbody><tr><td>1</td></tr></tbody></table></div></gt-table>`,
    );
    expect(el).toBeInstanceOf(GtTable);
    expect(el.table).toBe(el.querySelector("table.gt_table"));
    expect(el.getAttribute("data-gti-state")).toBe("ready");
  });

  it("marks itself empty when there is no table", async () => {
    const el = await mount(`<gt-table></gt-table>`);
    expect(el.table).toBeNull();
    expect(el.getAttribute("data-gti-state")).toBe("empty");
  });

  it("hydrates a table added after it was connected", async () => {
    const el = await mount(`<gt-table></gt-table>`);
    const table = document.createElement("table");
    el.append(table);
    await tick();
    expect(el.table).toBe(table);
    expect(el.getAttribute("data-gti-state")).toBe("ready");
  });

  it("resets when removed from the document", async () => {
    const el = await mount(`<gt-table><table></table></gt-table>`);
    el.remove();
    expect(el.table).toBeNull();
    expect(el.hasAttribute("data-gti-state")).toBe(false);
  });

  it("hydrates again when moved", async () => {
    const el = await mount(`<gt-table><table></table></gt-table>`);
    const host = document.createElement("section");
    document.body.append(host);
    host.append(el);
    await tick();
    expect(el.table).toBe(el.querySelector("table"));
    expect(el.getAttribute("data-gti-state")).toBe("ready");
  });
});
