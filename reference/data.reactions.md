## data.reactions


Reaction rates for gas-phase atmospheric reactions of organic compounds.


`data.reactions=_read_csv(_reactions_fname, dtype=_reactions_dtype)`  


The [reactions](data.reactions.md#great_tables.data.reactions) dataset contains kinetic data for second-order (two body) gas-phase chemical reactions for 1,683 organic compounds. The reaction-rate values and parameters within this dataset are useful for studies of the atmospheric environment. Organic pollutants, which are present in trace amounts in the atmosphere, have been extensively studied by research groups since their persistence in the atmosphere requires specific attention. Many researchers have reported kinetic data on specific gas-phase reactions and these mainly involve oxidation reactions with OH, nitrate radicals, ozone, and chlorine atoms.

This compilation of rate constant (*k*) data as contains the values for rate constants at 298 K (in units of `cm^3 molecules^-1 s^-1`) as well as parameters that allow for the calculation of rate constants at different temperatures (the temperature dependence parameters: `A`, `B`, and `n`). Uncertainty values/factors and temperature limits are also provided here where information is available.


This is a dataset with 1,683 rows and 39 columns.

- `compd_name`: The name of the primary compound undergoing reaction with OH, nitrate radicals, ozone, or chlorine atoms.
- `cmpd_mwt`: The molecular weight of the compound in units of g/mol.
- `cmpd_formula`: The chemical formula of the compound.
- `cmpd_type`: The category of compounds that the `compd_name` falls under.
- `cmpd_smiles`: The SMILES (simplified molecular-input line-entry system) representation for the compound.
- `cmpd_inchi`: The InChI (International Chemical Identifier) representation for the compound.
- `cmpd_inchikey`: The InChIKey, which is a hashed InChI value, has a fixed length of 27 characters. These values can be used to more easily perform database searches of chemical compounds.
- `OH_k298`: Rate constant at 298 K for OH reactions.
- `OH_uncert`: Uncertainty as a percentage for certain OH reactions.
- `OH_u_fac`: Uncertainty as a plus/minus difference for certain OH reactions.
- `OH_a`, `OH_b`, `OH_n`: Extended temperature dependence parameters for bimolecular OH reactions, to be used in the Arrhenius expression: `k(T)=A exp(-B/T) (T/300)^n`. In that, `A` is expressed as cm^3 molecules^-1 s^-1, `B` is in units of K, and `n` is dimensionless. Any missing values indicate that data is not available.
- `OH_t_low`, `OH_t_high`: The low and high temperature boundaries (in units of K) for which the `OH_a`, `OH_b`, and `OH_n` parameters are valid.
- `O3_k298`: Rate constant at 298 K for ozone reactions.
- `O3_uncert`: Uncertainty as a percentage for certain ozone reactions.
- `O3_u_fac`: Uncertainty as a plus/minus difference for certain ozone reactions.
- `O3_a`, `O3_b`, `O3_n`: Extended temperature dependence parameters for bimolecular ozone reactions, to be used in the Arrhenius expression: `k(T)=A exp(-B/T) (T/300)^n`. In that, `A` is expressed as cm^3 molecules^-1 s^-1, `B` is in units of K, and `n` is dimensionless. Any missing values indicate that data is not available.
- `O3_t_low`, `O3_t_high`: The low and high temperature boundaries (in units of K) for which the `O3_a`, `O3_b`, and `O3_n` parameters are valid.
- `NO3_k298`: Rate constant at 298 K for NO3 reactions.
- `NO3_uncert`: Uncertainty as a percentage for certain NO3 reactions.
- `NO3_u_fac`: Uncertainty as a plus/minus difference for certain NO3 reactions.
- `NO3_a`, `NO3_b`, `NO3_n`: Extended temperature dependence parameters for bimolecular NO3 reactions, to be used in the Arrhenius expression: `k(T)=A exp(-B/T) (T/300)^n`. In that, `A` is expressed as cm^3 molecules^-1 s^-1, `B` is in units of K, and `n` is dimensionless. Any missing values indicate that data is not available.
- `NO3_t_low`, `NO3_t_high`: The low and high temperature boundaries (in units of K) for which the `NO3_a`, `NO3_b`, and `NO3_n` parameters are valid.
- `Cl_k298`: Rate constant at 298 K for Cl reactions.
- `Cl_uncert`: Uncertainty as a percentage for certain Cl reactions.
- `Cl_u_fac`: Uncertainty as a plus/minus difference for certain Cl reactions.
- `Cl_a`, `Cl_b`, `Cl_n`: Extended temperature dependence parameters for bimolecular Cl reactions, to be used in the Arrhenius expression: `k(T)=A exp(-B/T) (T/300)^n`. In that, `A` is expressed as cm^3 molecules^-1 s^-1, `B` is in units of K, and `n` is dimensionless. Any missing values indicate that data is not available.
- `Cl_t_low`, `Cl_t_high`: The low and high temperature boundaries (in units of K) for which the `Cl_a`, `Cl_b`, and `Cl_n` parameters are valid.


    Rows: 1683
    Columns: 39
    $ cmpd_name     <str> 'methane', 'formaldehyde', 'methanol'
    $ cmpd_mwt      <f64> 16.04, 30.03, 32.04
    $ cmpd_formula  <str> 'CH4', 'CH2O', 'CH4O'
    $ cmpd_type     <str> 'normal alkane', 'aldehyde', 'alcohol or glycol'
    $ cmpd_smiles   <str> 'C', 'C=O', 'CO'
    $ cmpd_inchi    <str> 'InChI=1S/CH4/h1H4', 'InChI=1S/CH2O/c1-2/h1H2', 'InChI=1S/CH4O/c1-2/h2H,1H3'
    $ cmpd_inchikey <str> 'VNWKTOKETHGBQD-UHFFFAOYSA-N',
                          'WSFSSNUMVMOOMR-UHFFFAOYSA-N',
                          'OKKJLVBELUTLKV-UHFFFAOYSA-N'
    $ OH_k298       <f64> 6.36e-15, 8.5e-12, 8.78e-13
    $ OH_uncert     <f64> 0.1, 0.2, 0.1
    $ OH_u_fac      <f64> None, None, None
    $ OH_A          <f64> 3.62e-13, 5.4e-12, 2.32e-13
    $ OH_B          <f64> 1200.34866000493, -135.0, -402.0
    $ OH_n          <f64> 2.17993581535803, None, 2.72
    $ OH_t_low      <f64> 200.0, 200.0, 210.0
    $ OH_t_high     <f64> 2025.0, 300.0, 1344.0
    $ O3_k298       <f64> None, None, None
    $ O3_uncert     <f64> None, None, None
    $ O3_u_fac      <f64> None, None, None
    $ O3_A          <f64> None, None, None
    $ O3_B          <f64> None, None, None
    $ O3_n          <f64> None, None, None
    $ O3_t_low      <f64> None, None, None
    $ O3_t_high     <f64> None, None, None
    $ NO3_k298      <f64> None, 5.5e-16, 1.3e-16
    $ NO3_uncert    <f64> None, None, None
    $ NO3_u_fac     <f64> None, 1.6, 3.0
    $ NO3_A         <f64> None, None, 9.4e-13
    $ NO3_B         <f64> None, None, 2650.0
    $ NO3_n         <f64> None, None, None
    $ NO3_t_low     <f64> None, None, 250.0
    $ NO3_t_high    <f64> None, None, 370.0
    $ Cl_k298       <f64> 1e-13, 7.2e-11, 5.1e-11
    $ Cl_uncert     <f64> 0.15, 0.15, 0.2
    $ Cl_u_fac      <f64> None, None, None
    $ Cl_A          <f64> 6.6e-12, 8.1e-11, 5.1e-11
    $ Cl_B          <f64> 1240.0, 34.0, 0.0
    $ Cl_n          <f64> None, None, None
    $ Cl_t_low      <f64> 200.0, 200.0, 225.0
    $ Cl_t_high     <f64> 300.0, 500.0, 950.0
