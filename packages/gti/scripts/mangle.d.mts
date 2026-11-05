import type { BuildOptions } from "esbuild";

export function mangleable(sources: string[], bundle: string, kept?: Iterable<string>): string[];

export function mangledNames(pkgDir: string, options: BuildOptions): Promise<string[]>;
