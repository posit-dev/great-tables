# data.illness

Lab tests for one suffering from an illness.

`data.illness=_read_csv(_illness_fname, dtype=_illness_dtype)`

A dataset with artificial daily lab data for a patient with Yellow Fever (YF). The table comprises laboratory findings for the patient from day 3 of illness onset until day 9 (after which the patient died). YF viral DNA was found in serum samples from day 3, where the viral load reached 14,000 copies per mL. Several medical interventions were taken to help the patient, including the administration of fresh frozen plasma, platelets, red cells, and coagulation factor VIII. The patient also received advanced support treatment in the form of mechanical ventilation and plasmapheresis. Though the patient's temperature remained stable during their illness, unfortunately, the patient's condition did not improve. On days 7 and 8, the patient's health declined further, with symptoms such as nosebleeds, gastrointestinal bleeding, and hematoma.

The various tests are identified in the `test` column. The following listing provides the full names of any abbreviations seen in that column.

- `"WBC"`: white blood cells.
- `"RBC"`: red blood cells.
- `"Hb"`: hemoglobin.
- `"PLT"`: platelets.
- `"ALT"`: alanine aminotransferase.
- `"AST"`: aspartate aminotransferase.
- `"TBIL"`: total bilirubin.
- `"DBIL"`: direct bilirubin.
- `"NH3"`: hydrogen nitride.
- `"PT"`: prothrombin time.
- `"APTT"`: activated partial thromboplastin time.
- `"PTA"`: prothrombin time activity.
- `"DD"`: D-dimer.
- `"FDP"`: fibrinogen degradation products.
- `"LDH"`: lactate dehydrogenase.
- `"HBDH"`: hydroxybutyrate dehydrogenase.
- `"CK"`: creatine kinase.
- `"CKMB"`: the MB fraction of creatine kinase.
- `"BNP"`: B-type natriuetic peptide.
- `"MYO"`: myohemoglobin.
- `"TnI"`: troponin inhibitory.
- `"CREA"`: creatinine.
- `"BUN"`: blood urea nitrogen.
- `"AMY"`: amylase.
- `"LPS"`: lipase.
- `"K"`: kalium.
- `"Na"`: sodium.
- `"Cl"`: chlorine.
- `"Ca"`: calcium.
- `"P"`: phosphorus.
- `"Lac"`: lactate, blood.
- `"CRP"`: c-reactive protein.
- `"PCT"`: procalcitonin.
- `"IL-6"`: interleukin-6.
- `"CD3+CD4+"`: CD4+T lymphocytes.
- `"CD3+CD8+"`: CD8+T lymphocytes.

## Details

This is a dataset with 39 rows and 11 columns.

- `test`: The name of the test.
- `units`: The measurement units for the test.
- `day_3`, `day_4`, `day_5`, `day_6`, `day_7`, `day_8`, `day_9`: Measurement values associated with each test administered from days 3 to 9. A missing value indicates that the test could not be performed that day.
- `norm_l`, `norm_u`: Lower and upper bounds for the normal range associated with the test.

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

| test | units | day_3 | day_4 | day_5 | day_6 | day_7 | day_8 | day_9 | norm_l | norm_u |
|----|----|----|----|----|----|----|----|----|----|----|
| Viral load | copies per mL | 12000.0 | 4200.0 | 1600.0 | 830.0 | 760.0 | 520.0 | 250.0 | None | None |
| WBC | x10^9 / L | 5.26 | 4.26 | 9.92 | 10.49 | 24.77 | 30.26 | 19.03 | 4.0 | 10.0 |
| Neutrophils | x10^9 / L | 4.87 | 4.72 | 7.92 | 18.21 | 22.08 | 27.17 | 16.59 | 2.0 | 8.0 |
| RBC | x10^12 / L | 5.72 | 5.98 | 4.23 | 4.83 | 4.12 | 2.68 | 3.32 | 4.0 | 5.5 |
| Hb | g / L | 153.0 | 135.0 | 126.0 | 115.0 | 75.0 | 87.0 | 95.0 | 120.0 | 160.0 |
| PLT | x10^9 / L | 67.0 | 38.6 | 27.4 | 26.2 | 74.1 | 36.2 | 25.6 | 100.0 | 300.0 |
| ALT | U/L | 12835.0 | 12632.0 | 6426.7 | 4263.1 | 1623.7 | 672.6 | 512.4 | 9.0 | 50.0 |
| AST | U/L | 23672.0 | 21368.0 | 14730.0 | 8691.0 | 2189.0 | 1145.0 | 782.5 | 15.0 | 40.0 |
| TBIL | umol/L | 117.2 | 143.8 | 137.2 | 158.1 | 127.3 | 105.1 | 163.2 | 0.0 | 18.8 |
| DBIL | umol/L | 71.4 | 104.6 | 94.6 | 143.9 | 117.8 | 83.6 | 126.3 | 0.0 | 6.8 |
| NH3 | mmol/L | 115.2 | 135.2 | 131.0 | 176.7 | 84.2 | 72.4 | 91.9 | 10.0 | 47.0 |
| PT | s | 24.6 | 42.4 | 53.7 | 54.0 | 22.6 | 16.8 | 29.5 | 9.4 | 12.5 |
| APTT | s | 39.2 | 57.2 | 65.9 | 68.3 | 62.4 | 61.7 | 114.7 | 25.1 | 36.5 |
| PTA | % | 41.0 | 25.0 | 19.0 | 14.0 | 51.0 | 55.0 | 31.0 | 70.0 | 130.0 |
| DD | mg / L | 32.9 | 35.1 | 24.5 | 25.6 | 18.7 | 24.7 | 64.8 | 0.0 | 5.0 |
| FDP | ug / mL | 84.7 | 92.5 | 77.2 | None | None | 157.2 | 291.7 | 0.0 | 5.0 |
| Fibrinogen | mg / dL | 238.1 | 216.8 | 135.0 | 85.2 | 105.7 | None | 64.3 | 200.0 | 400.0 |
| LDH | U/L | 5727.3 | 2622.8 | 2418.7 | 546.3 | None | 637.2 | None | 80.0 | 285.0 |
| HBDH | None | 5971.2 | 5826.9 | 4826.9 | 2871.2 | None | 1163.6 | None | 74.0 | 182.0 |
| CK | U/L | 725.0 | 792.1 | 760.2 | 1263.6 | None | 1294.2 | None | 38.0 | 174.0 |
| CKMB | U/L | 75.0 | 71.0 | 58.0 | 65.0 | None | 68.0 | None | None | 25.0 |
| BNP | pg / mL | 37.0 | None | 73.0 | None | 482.0 | 421.0 | 1332.0 | None | 100.0 |
| MYO | ng / mL | 636.6 | 762.1 | 364.6 | 9999.0 | 9999.0 | 9999.0 | 9999.0 | 0.0 | 140.0 |
| TnI | ng / mL | 0.026 | 0.041 | 0.046 | 0.164 | 0.141 | 2.839 | 8.937 | 0.0 | 0.028 |
| CREA | umol / L | 705.6 | 683.6 | 523.6 | 374.0 | 259.6 | 241.8 | 211.4 | 59.0 | 104.0 |
| BUN | mmol / L | 20.13 | 25.33 | 13.33 | 7.84 | 4.23 | 3.92 | 3.41 | 1.7 | 8.3 |
| AMY | U / L | None | 232.8 | 394.6 | 513.7 | None | 642.9 | 538.9 | 0.0 | 115.0 |
| LPS | U / L | None | 227.6 | 526.9 | 487.9 | None | 437.8 | 414.5 | 5.6 | 51.3 |
| K | mmol / L | 4.19 | 4.64 | 4.34 | 4.83 | 4.53 | 4.37 | 5.74 | 3.5 | 5.3 |
| Na | mmol / L | 136.3 | 135.7 | 142.1 | 140.8 | 144.8 | 143.6 | 144.2 | 137.0 | 147.0 |
| Cl | mmol / L | 91.2 | 92.9 | 96.6 | 99.2 | 102.1 | 99.5 | 105.2 | 99.0 | 110.0 |
| Ca | mmol / L | 1.74 | 1.64 | 2.25 | 2.35 | 2.16 | 2.03 | 2.29 | 2.2 | 2.55 |
| P | mmol / L | 2.96 | 3.23 | 1.47 | 1.15 | 0.97 | 1.57 | 1.63 | 0.81 | 1.45 |
| Lac | mmol / L | 2.32 | 2.42 | 2.19 | 2.66 | None | 6.15 | 5.46 | 1.33 | 1.78 |
| CRP | mg / L | 43.6 | 38.6 | 28.6 | 21.5 | None | 4.3 | 6.4 | 0.0 | 5.0 |
| PCT | ng / mL | 0.57 | None | 1.35 | 2.26 | 1.79 | 3.48 | 5.92 | None | 0.05 |
| IL-6 | None | None | None | 165.9 | 58.3 | 74.6 | 737.2 | None | None | 7.0 |
| CD3+CD4+ | T cells per uL | None | 174.0 | 153.0 | 184.0 | 243.0 | 370.0 | 252.0 | 706.0 | 1125.0 |
| CD3+CD8+ | T cells per uL | None | 142.0 | 135.0 | 126.0 | 132.0 | 511.0 | 410.0 | 323.0 | 836.0 |
