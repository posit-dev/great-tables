## data.illness


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


This is a dataset with 39 rows and 11 columns.

- `test`: The name of the test.
- `units`: The measurement units for the test.
- `day_3`, `day_4`, `day_5`, `day_6`, `day_7`, `day_8`, `day_9`: Measurement values associated with each test administered from days 3 to 9. A missing value indicates that the test could not be performed that day.
- `norm_l`, `norm_u`: Lower and upper bounds for the normal range associated with the test.


    Rows: 39
    Columns: 11
    $ test   <str> 'Viral load', 'WBC', 'Neutrophils'
    $ units  <str> 'copies per mL', 'x10^9 / L', 'x10^9 / L'
    $ day_3  <f64> 12000.0, 5.26, 4.87
    $ day_4  <f64> 4200.0, 4.26, 4.72
    $ day_5  <f64> 1600.0, 9.92, 7.92
    $ day_6  <f64> 830.0, 10.49, 18.21
    $ day_7  <f64> 760.0, 24.77, 22.08
    $ day_8  <f64> 520.0, 30.26, 27.17
    $ day_9  <f64> 250.0, 19.03, 16.59
    $ norm_l <f64> None, 4.0, 2.0
    $ norm_u <f64> None, 10.0, 8.0
