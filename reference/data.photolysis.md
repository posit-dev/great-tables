## data.photolysis


Data on photolysis rates for gas-phase organic compounds.


`data.photolysis=_read_csv(_photolysis_fname, dtype=_photolysis_dtype)`  


The [photolysis](data.photolysis.md#great_tables.data.photolysis) dataset contains numerical values for describing the photolytic degradation pathways of 25 compounds of relevance in atmospheric chemistry. Many volatile organic compounds (VOCs) are emitted in substantial quantities from both biogenic and anthropogenic sources, and they can have a major influence on the chemistry of the lower atmosphere. A portion of these can be transformed into other VOCs via the energy provided from light.

In order to realistically predict the composition of the atmosphere and how it evolves over time, we need accurate estimates of photolysis rates. The data provided here in [photolysis](data.photolysis.md#great_tables.data.photolysis) allows for computations of photolysis rates (*J*, having units of `s^-1`) as a function of the solar zenith angle (SZA). Having such values is essential when deploying atmospheric chemistry models.


This is a dataset with 34 rows and 10 columns.

- `compd_name`: The name of the primary compound undergoing photolysis.
- `cmpd_formula`: The chemical formula of the compound.
- `products`: A product pathway for the photolysis of the compound.
- `type`: The type of organic compound undergoing photolysis.
- `l`, `m`, `n`: The parameter values given in the `l`, `m`, and `n` columnscan be used to calculate the photolysis rate (*J*) as a function of the solar zenith angle (*X*, in radians) through the expression: `J = l * cos(X)^m * exp(-n * sec(X))`.
- `quantum_yield`: In the context of photolysis reactions, this is the efficiency of a given photolytic reaction. In other words, it's the number of product molecules formed over the number of photons absorbed.
- `wavelength_nm`, `sigma_298_cm2`: The `wavelength_nm` and `sigma_298_cm2` columns provide photoabsorption data for the compound undergoing photolysis. The values in `wavelength_nm` provide the wavelength of light in nanometer units; the `sigma_298_cm2` values are paired with the `wavelength_nm` values and they are in units of `cm^2 molecule^-1`.


    Rows: 34
    Columns: 10
    $ cmpd_name     <str> 'ozone', 'ozone', 'hydrogen peroxide'
    $ cmpd_formula  <str> 'O3', 'O3', 'H2O2'
    $ products      <str> '-> O(^1D) + O2', '-> O(^3P) + O2', '-> OH + OH'
    $ type          <str> 'inorganic reactions', 'inorganic reactions', 'inorganic reactions'
    $ l             <f64> 6.073e-05, 0.0004775, 1.041e-05
    $ m             <f64> 1.743, 0.298, 0.723
    $ n             <f64> 0.474, 0.08, 0.279
    $ quantum_yield <f64> None, None, 1.0
    $ wavelength_nm <str> '290,291,292,...', '290,291,292,...', '190,195,200,...'
    $ sigma_298_cm2 <str> '1.43E-18,1.27E-18,1.11E-18,...',
                          '1.43E-18,1.27E-18,1.11E-18,...',
                          '6.72E-19,5.63E-19,4.75E-19,...'
