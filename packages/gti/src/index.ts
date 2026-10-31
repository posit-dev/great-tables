import { define, GtTable, TAG_NAME, VERSION } from "./gt-table";
import { parseSpec, SPEC_VERSION, SpecError } from "./spec";

define();

export type { State } from "./gt-table";
export type * from "./spec";
export { define, GtTable, parseSpec, SPEC_VERSION, SpecError, TAG_NAME, VERSION };
