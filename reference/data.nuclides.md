## data.nuclides


Nuclide data.


`data.nuclides=_read_csv(_nuclides_fname, dtype=_nuclides_dtype)`  


The [nuclides](data.nuclides.md#great_tables.data.nuclides) dataset contains information on all known nuclides, providing data on nuclear structure and decay modes across 118 elements. There is data here on natural abundances, atomic mass, spin, half-life, and more. The typical users for such a dataset include researchers in fields such as nuclear physics, radiochemistry, and nuclear medicine.


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


    Rows: 3383
    Columns: 29
    $ nuclide                    <str> '^{1}_{1}H0', '^{2}_{1}H1', '^{3}_{1}H2'
    $ z                          <i64> 1, 1, 1
    $ n                          <i64> 0, 1, 2
    $ element                    <str> 'H', 'H', 'H'
    $ radius                     <f64> 0.8783, 2.1421, 1.7591
    $ radius_uncert              <f64> 0.0086, 0.0088, 0.0363
    $ abundance                  <f64> 0.999855, 0.000145, None
    $ abundance_uncert           <f64> 7.8e-05, 7.8e-05, None
    $ is_stable                  <str> 'TRUE', 'TRUE', 'FALSE'
    $ half_life                  <f64> None, None, 388781328.00697297
    $ half_life_uncert           <f64> None, None, 631138.51949184
    $ isospin                    <str> None, None, None
    $ decay_1                    <str> None, None, 'B-'
    $ decay_1_pct                <f64> None, None, 1.0
    $ decay_1_pct_uncert         <f64> None, None, None
    $ decay_2                    <str> None, None, None
    $ decay_2_pct                <f64> None, None, None
    $ decay_2_pct_uncert         <f64> None, None, None
    $ decay_3                    <str> None, None, None
    $ decay_3_pct                <f64> None, None, None
    $ decay_3_pct_uncert         <f64> None, None, None
    $ magnetic_dipole            <f64> 2.792847351, 0.857438231, 2.97896246
    $ magnetic_dipole_uncert     <f64> 9e-09, 5e-09, 1.4e-08
    $ electric_quadrupole        <f64> None, 0.0028578, None
    $ electric_quadrupole_uncert <f64> None, 3e-07, None
    $ atomic_mass                <f64> 1007825.031898, 2014101.777844, 3016049.28132
    $ atomic_mass_uncert         <f64> 1.4e-05, 1.5e-05, 8e-05
    $ mass_excess                <f64> 7288.971064, 13135.722895, 14949.8109
    $ mass_excess_uncert         <f64> 1.3e-05, 1.5e-05, 8e-05
