import { describe, expect, it } from "vitest";
import { parseSpec, SPEC_VERSION, SpecError } from "../src/index";

const valid = {
  version: SPEC_VERSION,
  nrows: 2,
  columns: [{ id: "x", role: "data", kind: "number", align: "right", header: "t-x" }],
  spanners: [],
  stub: { columns: [], groups_as_column: false },
  groups: [],
  body: [{ group: "a" }, 1, 0, { summary: "Total", group: "a", side: "bottom" }],
  ranks: { x: [1, null] },
  striping: { stub: false, body: true },
  controls: { sorting: true, search: false, resizing: false },
  pagination: { enabled: true, page_size: 10, page_sizes: [10, 25], size_select: false, info: true, type: "numbers" },
  display: { highlight: false, compact: false, wrap: true },
};

const pagination = (fields: object) => JSON.stringify({ ...valid, pagination: { ...valid.pagination, ...fields } });

const parse = (spec: object) => parseSpec(JSON.stringify(spec));

describe("parseSpec()", () => {
  it("returns a valid spec as it is", () => {
    expect(parse(valid)).toEqual(valid);
  });

  it("ignores fields it doesn't know", () => {
    expect(parse({ ...valid, later: { anything: true } }).nrows).toBe(2);
  });

  it("accepts every kind of body row", () => {
    const body = [
      { grand_summary: "Max", side: "top" },
      { group: null },
      0,
      { summary: "Total", group: null, side: "top" },
      1,
    ];
    expect(parse({ ...valid, body }).body).toEqual(body);
  });

  it.each([
    ["isn't JSON", "{", /valid JSON/],
    ["isn't an object", "[1]", /no version/],
    ["has no version", JSON.stringify({ ...valid, version: undefined }), /no version/],
    ["has another version", JSON.stringify({ ...valid, version: 2 }), /version 2 isn't supported/],
    ["has a bad nrows", JSON.stringify({ ...valid, nrows: -1 }), /nrows/],
    ["has a bad nrows", JSON.stringify({ ...valid, nrows: 1.5 }), /nrows/],
    ["has no body", JSON.stringify({ ...valid, body: undefined }), /`body` must be an array/],
    ["has no ranks", JSON.stringify({ ...valid, ranks: [] }), /`ranks` must be objects/],
    ["has a row out of range", JSON.stringify({ ...valid, body: [0, 2] }), /`body\[1\]`/],
    ["has a negative row", JSON.stringify({ ...valid, body: [-1] }), /`body\[0\]`/],
    ["has an unknown row", JSON.stringify({ ...valid, body: [0, { other: 1 }] }), /`body\[1\]`/],
    ["has a row that isn't a number", JSON.stringify({ ...valid, body: ["0"] }), /`body\[0\]`/],
    ["has short ranks", JSON.stringify({ ...valid, ranks: { x: [1] } }), /`ranks.x`/],
    ["has no striping", JSON.stringify({ ...valid, striping: undefined }), /`striping`/],
    ["has a bad striping", JSON.stringify({ ...valid, striping: { stub: 1, body: true } }), /`striping`/],
    ["has no controls", JSON.stringify({ ...valid, controls: undefined }), /`controls`/],
    ["has a bad controls", JSON.stringify({ ...valid, controls: { sorting: true } }), /`controls`/],
    ["has a bad controls", JSON.stringify({ ...valid, controls: { sorting: 1, search: false } }), /`controls`/],
    ["has no resizing flag", JSON.stringify({ ...valid, controls: { sorting: true, search: false } }), /`controls`/],
    ["has no pagination", JSON.stringify({ ...valid, pagination: undefined }), /`pagination`/],
    ["has a page size of 0", pagination({ page_size: 0 }), /`pagination`/],
    ["has a fractional page size", pagination({ page_size: 2.5 }), /`pagination`/],
    ["has a bad page sizes", pagination({ page_sizes: [10, -1] }), /`pagination`/],
    ["has page sizes that aren't an array", pagination({ page_sizes: 10 }), /`pagination`/],
    ["has an unknown pagination type", pagination({ type: "scroll" }), /`pagination`/],
    ["has a bad pagination flag", pagination({ size_select: "yes" }), /`pagination`/],
    ["has no pagination info flag", pagination({ info: undefined }), /`pagination`/],
    ["has no display", JSON.stringify({ ...valid, display: undefined }), /`display`/],
    ["has a bad display flag", JSON.stringify({ ...valid, display: { ...valid.display, wrap: 0 } }), /`display`/],
    ["has no highlight flag", JSON.stringify({ ...valid, display: { compact: false, wrap: true } }), /`display`/],
  ])("rejects a spec that %s", (_, text, message) => {
    expect(() => parseSpec(text)).toThrow(SpecError);
    expect(() => parseSpec(text)).toThrow(message);
  });
});
