## data.constants


The fundamental physical constants.


`data.constants=_read_csv(_constants_fname, dtype=_constants_dtype)`  


This dataset contains values for over 300 basic fundamental constants in nature. The values originate from the 2018 adjustment which is based on the latest relevant precision measurements and improvements of theoretical calculations. Such work has been carried out under the authority of the Task Group on Fundamental Constants (TGFC) of the Committee on Data of the International Science Council (CODATA). These updated values became available on May 20, 2019. They are published at http://physics.nist.gov/constants, a website of the Fundamental Constants Data Center of the National Institute of Standards and Technology (NIST), Gaithersburg, Maryland, USA.


This is a dataset with 354 rows and 6 columns.

- `name`: The name of the constant.
- `value`: The value of the constant.
- `uncert`: The uncertainty associated with the value. If missing then the value is seen as an 'exact' value (e.g., an electron volt has the exact value of 1.602 176 634 e-19 J).
- `sf_value`, `sf_uncert`: The number of significant figures associated with the value and any uncertainty value.
- `units`: The units associated with the constant.


    Rows: 354
    Columns: 6
    $ name      <str> 'alpha particle-electron mass ratio',
                      'alpha particle mass',
                      'alpha particle mass energy equivalent'
    $ value     <f64> 7294.29954142, 6.6446573357e-27, 5.9719201914e-10
    $ uncert    <f64> 2.4e-07, 2e-36, 1.8e-19
    $ sf_value  <i64> 12, 11, 11
    $ sf_uncert <i64> 2, 2, 2
    $ units     <str> None, 'kg', 'J'
