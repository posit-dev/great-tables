# data.reactions

Reaction rates for gas-phase atmospheric reactions of organic compounds.

`data.reactions=_read_csv(_reactions_fname, dtype=_reactions_dtype)`

The [reactions](../reference/data.reactions.md#great_tables.data.reactions) dataset contains kinetic data for second-order (two body) gas-phase chemical reactions for 1,683 organic compounds. The reaction-rate values and parameters within this dataset are useful for studies of the atmospheric environment. Organic pollutants, which are present in trace amounts in the atmosphere, have been extensively studied by research groups since their persistence in the atmosphere requires specific attention. Many researchers have reported kinetic data on specific gas-phase reactions and these mainly involve oxidation reactions with OH, nitrate radicals, ozone, and chlorine atoms.

This compilation of rate constant (*k*) data as contains the values for rate constants at 298 K (in units of `cm^3 molecules^-1 s^-1`) as well as parameters that allow for the calculation of rate constants at different temperatures (the temperature dependence parameters: `A`, `B`, and `n`). Uncertainty values/factors and temperature limits are also provided here where information is available.

## Details

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

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

| cmpd_name | cmpd_mwt | cmpd_formula | cmpd_type | cmpd_smiles | cmpd_inchi | cmpd_inchikey | OH_k298 | OH_uncert | OH_u_fac | OH_A | OH_B | OH_n | OH_t_low | OH_t_high | O3_k298 | O3_uncert | O3_u_fac | O3_A | O3_B | O3_n | O3_t_low | O3_t_high | NO3_k298 | NO3_uncert | NO3_u_fac | NO3_A | NO3_B | NO3_n | NO3_t_low | NO3_t_high | Cl_k298 | Cl_uncert | Cl_u_fac | Cl_A | Cl_B | Cl_n | Cl_t_low | Cl_t_high |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| methane | 16.04 | CH4 | normal alkane | C | InChI=1S/CH4/h1H4 | VNWKTOKETHGBQD-UHFFFAOYSA-N | 6.36E-15 | 0.1 | None | 3.62E-13 | 1200.35 | 2.17994 | 200.0 | 2025.0 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | 1E-13 | 0.15 | None | 6.6E-12 | 1240.0 | None | 200.0 | 300.0 |
| formaldehyde | 30.03 | CH2O | aldehyde | C=O | InChI=1S/CH2O/c1-2/h1H2 | WSFSSNUMVMOOMR-UHFFFAOYSA-N | 8.5E-12 | 0.2 | None | 5.4E-12 | -135.0 | None | 200.0 | 300.0 | None | None | None | None | None | None | None | None | 5.5E-16 | None | 1.6 | None | None | None | None | None | 7.2E-11 | 0.15 | None | 8.1E-11 | 34.0 | None | 200.0 | 500.0 |
| methanol | 32.04 | CH4O | alcohol or glycol | CO | InChI=1S/CH4O/c1-2/h2H,1H3 | OKKJLVBELUTLKV-UHFFFAOYSA-N | 8.78E-13 | 0.1 | None | 2.32E-13 | -402.0 | 2.72 | 210.0 | 1344.0 | None | None | None | None | None | None | None | None | 1.3E-16 | None | 3.0 | 9.4E-13 | 2650.0 | None | 250.0 | 370.0 | 5.1E-11 | 0.2 | None | 5.1E-11 | 0.0 | None | 225.0 | 950.0 |
| fluoromethane | 34.03 | CH3F | haloalkane (separated) | CF | InChI=1S/CH3F/c1-2/h1H3 | NBVXSUQYWXRMNV-UHFFFAOYSA-N | 1.97E-14 | 0.1 | None | 1.99E-13 | 685.42 | 2.04018 | 240.0 | 1800.0 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | 3.6E-13 | None | 1.4 | 4.9E-12 | 781.0 | None | 200.0 | 300.0 |
| formic acid | 46.03 | CH2O2 | carboxylic acid | OC=O | InChI=1S/CH2O2/c2-1-3/h1H,(H,2,3) | BDAGIHXWWSANSR-UHFFFAOYSA-N | 4.5E-13 | None | 1.4 | 4.5E-13 | None | None | 290.0 | 450.0 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | 1.9E-13 | None | 1.4 | None | None | None | None | None |
| formyl fluoride | 48.02 | CHOF | saturated halogen-containing oxygenate (halogens separated) | FC=O | InChI=1S/CHFO/c2-1-3/h1H | NHGVZTMBVDFPHJ-UHFFFAOYSA-N | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | 1.9E-15 | 0.11 | None | None | None | None | None | None |
| methyl hydroperoxide | 48.04 | CH4O2 | hydroperoxide | COO | InChI=1S/CH4O2/c1-3-2/h2H,1H3 | MEUKEBNAABNAEX-UHFFFAOYSA-N | 1E-11 | None | 2.0 | 5.3E-12 | -190.0 | None | 220.0 | 430.0 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | 5.9E-11 | None | 3.0 | None | None | None | None | None |
| chloromethane | 50.49 | CH3Cl | haloalkane (separated) | CCl | InChI=1S/CH3Cl/c1-2/h1H3 | NEHMKBQYUWJMIP-UHFFFAOYSA-N | 3.6E-14 | 0.2 | None | 2.1E-12 | 1210.0 | None | 220.0 | 330.0 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | 4.89E-13 | 0.1 | None | 4.32E-12 | 646.4 | 1.3057 | 222.0 | 843.0 |
| difluoromethane | 52.02 | CH2F2 | haloalkane (multiple) | FCF | InChI=1S/CH2F2/c2-1-3/h1H2 | RWRIWBAIICGTTQ-UHFFFAOYSA-N | 1.05E-14 | 0.1 | None | 2.21E-13 | 904.359 | 1.86009 | 220.0 | 1800.0 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | 3.3E-14 | 0.15 | None | 6.93E-12 | 1591.0 | None | 250.0 | 300.0 |
| nitromethane | 61.04 | CH3NO2 | nitro organic | \[O-\]\[N+\](=O)C | InChI=1S/CH3NO2/c1-2(3)4/h1H3 | LYGJENNIWJXYER-UHFFFAOYSA-N | 1.4E-14 | 0.21 | None | 5.8E-13 | 1102.0 | None | 298.0 | 671.0 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None |
