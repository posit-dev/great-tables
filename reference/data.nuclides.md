# data.nuclides

Nuclide data.

`data.nuclides=_read_csv(_nuclides_fname, dtype=_nuclides_dtype)`

The [nuclides](../reference/data.nuclides.md#great_tables.data.nuclides) dataset contains information on all known nuclides, providing data on nuclear structure and decay modes across 118 elements. There is data here on natural abundances, atomic mass, spin, half-life, and more. The typical users for such a dataset include researchers in fields such as nuclear physics, radiochemistry, and nuclear medicine.

## Details

This is a dataset with 3,383 rows and 29 columns.

- `nuclide`: The symbol for the nuclide.
- `z`, `n`: The number of protons and neutrons.
- `element`: The element symbol.
- `radius`, `radius_uncert`: The charge radius and its associated uncertainty. In units of fm.
- `abundance`, `abundance_uncert`: The abundance of the stable isotope as a mole fraction (in relation to other stable isotopes of the same element). Values are provided for the nuclide only if `is_stable` is `"TRUE"`.
- `is_stable`: Is the nuclide a stable isotope?
- `half_life`, `half_life_uncert`: The nuclide's half life represented as seconds.
- `isospin`: The isospin, or the quantum number related to the up and down quark content of the particle.
- `decay_1`, `decay_2`, `decay_3`: The 1st, 2nd, and 3rd decay modes.
- `decay_1_pct`, `decay_1_pct_uncert`, `decay_2_pct`, `decay_2_pct_uncert`, `decay_3_pct`, `decay_3_pct_uncert`: The branching proportions for the 1st, 2nd, and 3rd decays (along with uncertainty values).
- `magnetic_dipole`, `magnetic_dipole_uncert`: The magnetic dipole and its associated uncertainty. Expressed in units of micro N, or nuclear magneton values.
- `electric_quadrupole`, `electric_quadrupole_uncert`: The electric quadrupole and its associated uncertainty. In units of barn (b).
- `atomic_mass`, `atomic_mass_uncert`: The atomic mass and its associated uncertainty. In units of micro AMU.
- `mass_excess`, `mass_excess_uncert`: The mass excess and its associated uncertainty. In units of keV.

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column. It's a large table (3,383 rows of 29 columns), so it can take a few seconds to load, and longer on a phone.

| nuclide | z | n | element | radius | radius_uncert | abundance | abundance_uncert | is_stable | half_life | half_life_uncert | isospin | decay_1 | decay_1_pct | decay_1_pct_uncert | decay_2 | decay_2_pct | decay_2_pct_uncert | decay_3 | decay_3_pct | decay_3_pct_uncert | magnetic_dipole | magnetic_dipole_uncert | electric_quadrupole | electric_quadrupole_uncert | atomic_mass | atomic_mass_uncert | mass_excess | mass_excess_uncert |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ^{1}\_{1}H0 | 1 | 0 | H | 0.8783 | 0.0086 | 0.999855 | 7.8E-05 | TRUE | None | None | None | None | None | None | None | None | None | None | None | None | 2.792847351 | 9E-09 | None | None | 1.00783E+06 | 1.4E-05 | 7288.971064 | 1.3E-05 |
| ^{2}\_{1}H1 | 1 | 1 | H | 2.1421 | 0.0088 | 0.000145 | 7.8E-05 | TRUE | None | None | None | None | None | None | None | None | None | None | None | None | 0.857438231 | 5E-09 | 0.0028578 | 3E-07 | 2.0141E+06 | 1.5E-05 | 13135.722895 | 1.5E-05 |
| ^{3}\_{1}H2 | 1 | 2 | H | 1.7591 | 0.0363 | None | None | FALSE | 3.88781E+08 | 631139 | None | B- | 1.0 | None | None | None | None | None | None | None | 2.97896246 | 1.4E-08 | None | None | 3.01605E+06 | 8E-05 | 14949.8109 | 8E-05 |
| ^{4}\_{1}H3 | 1 | 3 | H | None | None | None | None | FALSE | None | None | 1 | N | 1.0 | None | None | None | None | None | None | None | None | None | None | None | 4026431.867 | 107.354 | 24621.129 | 100.0 |
| ^{5}\_{1}H4 | 1 | 4 | H | None | None | None | None | FALSE | 8.60826E-23 | 6.4968E-24 | None | 2N | 1.0 | None | None | None | None | None | None | None | None | None | None | None | 5035311.492 | 96.02 | 32892.447 | 89.443 |
| ^{6}\_{1}H5 | 1 | 5 | H | None | None | None | None | FALSE | 2.94347E-22 | 8.35565E-23 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | 6044955.437 | 272.816 | 41875.725 | 254.127 |
| ^{7}\_{1}H6 | 1 | 6 | H | None | None | None | None | FALSE | 5.06931E-21 | 2.81628E-20 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | 7052749.0 | 1078.0 | 49135.0 | 1004.0 |
| ^{3}\_{2}He1 | 2 | 1 | He | 1.9661 | 0.003 | 2E-06 | 2E-06 | TRUE | None | None | None | None | None | None | None | None | None | None | None | None | -2.12762531 | 3E-08 | None | None | 3.01603E+06 | 6E-05 | 14931.21888 | 6E-05 |
| ^{4}\_{2}He2 | 2 | 2 | He | 1.6755 | 0.0028 | 0.999998 | 2E-06 | TRUE | None | None | 0 | None | None | None | None | None | None | None | None | None | None | None | None | None | 4.0026E+06 | 0.00016 | 2424.91587 | 0.00015 |
| ^{5}\_{2}He3 | 2 | 3 | He | None | None | None | None | FALSE | 7.04071E-22 | 0.0 | 1/2 | N | None | None | None | None | None | None | None | None | None | None | None | None | 5012057.224 | 21.47 | 11231.234 | 20.0 |
