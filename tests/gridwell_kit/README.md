# gridwell's conformance kit

`GT.as_gridwell()` writes the IR of [gridwell](https://github.com/rich-iannone/gridwell), and
these files are what its tests check that IR against. They're copies from gridwell: don't edit
them here. Change them in gridwell, then sync them:

```bash
python scripts/sync_gridwell_kit.py ../gridwell          # copy the kit from a checkout
python scripts/sync_gridwell_kit.py --check ../gridwell  # check the copy is current
```

| File | From gridwell | What it is |
|------|---------------|------------|
| `cases.py` | `conformance/cases.py` | The conformance cases, as Great Tables tables |
| `expected/*.json` | `conformance/expected/great_tables/` | Each case's expected grid, to tier L3 |
| `html_grid.py` | `conformance/html_grid.py` | Reads the L1 grid of a table from Great Tables' own HTML |
| `ir-1.0.schema.json` | `crates/gridwell-ir/schema/ir-1.0.schema.json` | The JSON Schema of IR 1.0 |
| `SYNCED_FROM` | | The gridwell commit the copies are from |

The tests:

- `tests/test_gridwell.py` checks the IR without gridwell installed, against the JSON Schema
  (tier L0) and as Great Tables draws the table.
- `tests/test_gridwell_conformance.py` checks each case against its expected grid with
  `gridwell.conformance.assert_conforms()` (tiers L1 to L3), and other tables against the grid of
  their HTML. It's skipped when gridwell isn't installed.
