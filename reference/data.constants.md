# data.constants

The fundamental physical constants.

`data.constants=_read_csv(_constants_fname, dtype=_constants_dtype)`

This dataset contains values for over 300 basic fundamental constants in nature. The values originate from the 2018 adjustment which is based on the latest relevant precision measurements and improvements of theoretical calculations. Such work has been carried out under the authority of the Task Group on Fundamental Constants (TGFC) of the Committee on Data of the International Science Council (CODATA). These updated values became available on May 20, 2019. They are published at http://physics.nist.gov/constants, a website of the Fundamental Constants Data Center of the National Institute of Standards and Technology (NIST), Gaithersburg, Maryland, USA.

## Details

This is a dataset with 354 rows and 6 columns.

- `name`: The name of the constant.
- `value`: The value of the constant.
- `uncert`: The uncertainty associated with the value. If missing then the value is seen as an 'exact' value (e.g., an electron volt has the exact value of 1.602 176 634 e-19 J).
- `sf_value`, `sf_uncert`: The number of significant figures associated with the value and any uncertainty value.
- `units`: The units associated with the constant.

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

``` python
from great_tables import GTI
from great_tables.data import constants

GTI(constants, preset="explorer").i_responsive("scroll")
```

| name | value | uncert | sf_value | sf_uncert | units |
|----|----|----|----|----|----|
| alpha particle-electron mass ratio | 7294.3 | 2.4E-07 | 12 | 2 | None |
| alpha particle mass | 6.64466E-27 | 2E-36 | 11 | 2 | kg |
| alpha particle mass energy equivalent | 5.97192E-10 | 1.8E-19 | 11 | 2 | J |
| alpha particle mass energy equivalent in MeV | 3727.3794066 | 1.1E-06 | 11 | 2 | MeV |
| alpha particle mass in u | 4.00151 | 6.3E-11 | 13 | 2 | u |
| alpha particle molar mass | 0.00400151 | 1.2E-12 | 11 | 2 | kg mol^-1 |
| alpha particle-proton mass ratio | 3.9726 | 2.2E-10 | 12 | 2 | None |
| alpha particle relative atomic mass | 4.00151 | 6.3E-11 | 13 | 2 | None |
| Angstrom star | 1.00001E-10 | 9E-17 | 9 | 2 | m |
| atomic mass constant | 1.66054E-27 | 5E-37 | 12 | 2 | kg |
| atomic mass constant energy equivalent | 1.49242E-10 | 4.5E-20 | 12 | 2 | J |
| atomic mass constant energy equivalent in MeV | 931.49410242 | 2.8E-07 | 11 | 2 | MeV |
| atomic mass unit-electron volt relationship | 931494102\.42 | 0.28 | 11 | 2 | eV |
| atomic mass unit-hartree relationship | 34231776.874 | 0.01 | 11 | 2 | E_h |
| atomic mass unit-hertz relationship | 2.25234E+23 | 6.8E+13 | 12 | 2 | Hz |
| atomic mass unit-inverse meter relationship | 7.51301E+14 | 230000.0 | 11 | 2 | m^-1 |
| atomic mass unit-joule relationship | 1.49242E-10 | 4.5E-20 | 12 | 2 | J |
| atomic mass unit-kelvin relationship | 1.08095E+13 | 3300.0 | 12 | 2 | K |
| atomic mass unit-kilogram relationship | 1.66054E-27 | 5E-37 | 12 | 2 | kg |
| atomic unit of 1st hyperpolarizability | 3.20636E-53 | 1.5E-62 | 11 | 2 | C^3 m^3 J^-2 |
| atomic unit of 2nd hyperpolarizability | 6.23538E-65 | 3.8E-74 | 11 | 2 | C^4 m^4 J^-3 |
| atomic unit of action | 1.05457E-34 | None | 10 | None | J s |
| atomic unit of charge | 1.60218E-19 | None | 10 | None | C |
| atomic unit of charge density | 1.0812E+12 | 490.0 | 12 | 2 | C m^-3 |
| atomic unit of current | 0.00662362 | 1.3E-14 | 13 | 2 | A |
| atomic unit of electric dipole mom. | 8.47835E-30 | 1.3E-39 | 11 | 2 | C m |
| atomic unit of electric field | 514220674763 | 78.0 | 12 | 2 | V m^-1 |
| atomic unit of electric field gradient | 9.71736E+21 | 2.9E+12 | 11 | 2 | V m^-2 |
| atomic unit of electric polarizability | 1.64878E-41 | 5E-51 | 12 | 2 | C^2 m^2 J^-1 |
| atomic unit of electric potential | 27.2114 | 5.3E-11 | 14 | 2 | V |
| atomic unit of electric quadrupole mom. | 4.48655E-40 | 1.4E-49 | 11 | 2 | C m^2 |
| atomic unit of energy | 4.35974E-18 | 8.5E-30 | 14 | 2 | J |
| atomic unit of force | 8.23872E-08 | 1.2E-17 | 11 | 2 | N |
| atomic unit of length | 5.29177E-11 | 8E-21 | 12 | 2 | m |
| atomic unit of mag. dipole mom. | 1.8548E-23 | 5.6E-33 | 12 | 2 | J T^-1 |
| atomic unit of mag. flux density | 235052 | 7.1E-05 | 12 | 2 | T |
| atomic unit of magnetizability | 7.89104E-29 | 4.8E-38 | 11 | 2 | J T^-2 |
| atomic unit of mass | 9.10938E-31 | 2.8E-40 | 11 | 2 | kg |
| atomic unit of momentum | 1.99285E-24 | 3E-34 | 12 | 2 | kg m s^-1 |
| atomic unit of permittivity | 1.11265E-10 | 1.7E-20 | 12 | 2 | F m^-1 |
| atomic unit of time | 2.41888E-17 | 4.7E-29 | 14 | 2 | s |
| atomic unit of velocity | 2.18769E+06 | 0.00033 | 12 | 2 | m s^-1 |
| Avogadro constant | 6.02214E+23 | None | 9 | None | mol^-1 |
| Bohr magneton | 9.27401E-24 | 2.8E-33 | 11 | 2 | J T^-1 |
| Bohr magneton in eV/T | 5.78838E-05 | 1.7E-14 | 11 | 2 | eV T^-1 |
| Bohr magneton in Hz/T | 1.39962E+10 | 4.2 | 12 | 2 | Hz T^-1 |
| Bohr magneton in inverse meter per tesla | 46.686447783 | 1.4E-08 | 11 | 2 | m^-1 T^-1 |
| Bohr magneton in K/T | 0.671714 | 2E-10 | 11 | 2 | K T^-1 |
| Bohr radius | 5.29177E-11 | 8E-21 | 12 | 2 | m |
| Boltzmann constant | 1.380649E-23 | None | 7 | None | J K^-1 |
| Boltzmann constant in eV/K | 8.61733E-05 | None | 10 | None | eV K^-1 |
| Boltzmann constant in Hz/K | 20836619120 | None | 10 | None | Hz K^-1 |
| Boltzmann constant in inverse meter per kelvin | 69.50348004 | None | 10 | None | m^-1 K^-1 |
| characteristic impedance of vacuum | 376.73 | 5.7E-08 | 12 | 2 | ohm |
| classical electron radius | 2.81794E-15 | 1.3E-24 | 11 | 2 | m |
| Compton wavelength | 2.42631E-12 | 7.3E-22 | 12 | 2 | m |
| conductance quantum | 7.74809E-05 | None | 10 | None | S |
| conventional value of ampere-90 | 1 | None | 12 | None | A |
| conventional value of coulomb-90 | 1 | None | 12 | None | C |
| conventional value of farad-90 | 0.9999999822 | None | 11 | None | F |
| conventional value of henry-90 | 1 | None | 12 | None | H |
| conventional value of Josephson constant | 4.83598E+14 | None | 7 | None | Hz V^-1 |
| conventional value of ohm-90 | 1 | None | 12 | None | ohm |
| conventional value of volt-90 | 1 | None | 12 | None | V |
| conventional value of von Klitzing constant | 25812.807 | None | 8 | None | ohm |
| conventional value of watt-90 | 1 | None | 12 | None | W |
| Copper x unit | 1.00208E-13 | 2.8E-20 | 9 | 2 | m |
| deuteron-electron mag. mom. ratio | -0.000466435 | 1.2E-12 | 10 | 2 | None |
| deuteron-electron mass ratio | 3670.48 | 1.3E-07 | 12 | 2 | None |
| deuteron g factor | 0.8574382338 | 2.2E-09 | 10 | 2 | None |
| deuteron mag. mom. | 4.33074E-27 | 1.1E-35 | 10 | 2 | J T^-1 |
| deuteron mag. mom. to Bohr magneton ratio | 0.000466975 | 1.2E-12 | 10 | 2 | None |
| deuteron mag. mom. to nuclear magneton ratio | 0.8574382338 | 2.2E-09 | 10 | 2 | None |
| deuteron mass | 3.34358E-27 | 1E-36 | 11 | 2 | kg |
| deuteron mass energy equivalent | 3.00506E-10 | 9.1E-20 | 12 | 2 | J |
| deuteron mass energy equivalent in MeV | 1875.61 | 5.7E-07 | 12 | 2 | MeV |
| deuteron mass in u | 2.01355 | 4E-11 | 13 | 2 | u |
| deuteron molar mass | 0.00201355 | 6.1E-13 | 12 | 2 | kg mol^-1 |
| deuteron-neutron mag. mom. ratio | -0.44820653 | 1.1E-07 | 8 | 2 | None |
| deuteron-proton mag. mom. ratio | 0.307012 | 7.9E-10 | 11 | 2 | None |
| deuteron-proton mass ratio | 1.99901 | 1.1E-10 | 12 | 2 | None |
| deuteron relative atomic mass | 2.01355 | 4E-11 | 13 | 2 | None |
| deuteron rms charge radius | 2.12799E-15 | 7.4E-19 | 6 | 2 | m |
| electron charge to mass quotient | -1.75882E+11 | 53.0 | 12 | 2 | C kg^-1 |
| electron-deuteron mag. mom. ratio | -2143.92 | 5.6E-06 | 11 | 2 | None |
| electron-deuteron mass ratio | 0.000272444 | 9.6E-15 | 13 | 2 | None |
| electron g factor | -2.00232 | 3.5E-13 | 15 | 2 | None |
| electron gyromag. ratio | 176085963023 | 53.0 | 12 | 2 | s^-1 T^-1 |
| electron gyromag. ratio in MHz/T | 28025 | 8.5E-06 | 12 | 2 | MHz T^-1 |
| electron-helion mass ratio | 0.000181954 | 7.9E-15 | 13 | 2 | None |
| electron mag. mom. | -9.28476E-24 | 2.8E-33 | 11 | 2 | J T^-1 |
| electron mag. mom. anomaly | 0.00115965 | 1.8E-13 | 12 | 2 | None |
| electron mag. mom. to Bohr magneton ratio | -1.00116 | 1.8E-13 | 15 | 2 | None |
| electron mag. mom. to nuclear magneton ratio | -1838.28 | 1.1E-07 | 12 | 2 | None |
| electron mass | 9.10938E-31 | 2.8E-40 | 11 | 2 | kg |
| electron mass energy equivalent | 8.18711E-14 | 2.5E-23 | 11 | 2 | J |
| electron mass energy equivalent in MeV | 0.51099895 | 1.5E-10 | 11 | 2 | MeV |
| electron mass in u | 0.00054858 | 1.6E-14 | 12 | 2 | u |
| electron molar mass | 5.4858E-07 | 1.7E-16 | 11 | 2 | kg mol^-1 |
| electron-muon mag. mom. ratio | 206.7669883 | 4.6E-06 | 10 | 2 | None |
| electron-muon mass ratio | 0.00483633 | 1.1E-10 | 9 | 2 | None |
| electron-neutron mag. mom. ratio | 960.9205 | 0.00023 | 8 | 2 | None |
| electron-neutron mass ratio | 0.000543867 | 2.6E-13 | 11 | 2 | None |
| electron-proton mag. mom. ratio | -658.211 | 2E-07 | 11 | 2 | None |
| electron-proton mass ratio | 0.000544617 | 3.3E-14 | 12 | 2 | None |
| electron relative atomic mass | 0.00054858 | 1.6E-14 | 12 | 2 | None |
| electron-tau mass ratio | 0.000287585 | 1.9E-08 | 6 | 2 | None |
| electron to alpha particle mass ratio | 0.000137093 | 4.5E-15 | 13 | 2 | None |
| electron to shielded helion mag. mom. ratio | 864.058257 | 1E-05 | 9 | 2 | None |
| electron to shielded proton mag. mom. ratio | -658.2275971 | 7.2E-06 | 10 | 2 | None |
| electron-triton mass ratio | 0.00018192 | 9E-15 | 13 | 2 | None |
| electron volt | 1.60218E-19 | None | 10 | None | J |
| electron volt-atomic mass unit relationship | 1.07354E-09 | 3.2E-19 | 12 | 2 | u |
| electron volt-hartree relationship | 0.0367493 | 7.1E-14 | 14 | 2 | E_h |
| electron volt-hertz relationship | 2.41799E+14 | None | 10 | None | Hz |
| electron volt-inverse meter relationship | 806554.3937 | None | 10 | None | m^-1 |
| electron volt-joule relationship | 1.60218E-19 | None | 10 | None | J |
| electron volt-kelvin relationship | 11604.51812 | None | 10 | None | K |
| electron volt-kilogram relationship | 1.78266E-36 | None | 10 | None | kg |
| elementary charge | 1.60218E-19 | None | 10 | None | C |
| elementary charge over h-bar | 1.51927E+15 | None | 10 | None | A J^-1 |
| Faraday constant | 96485.33212 | None | 10 | None | C mol^-1 |
| Fermi coupling constant | 1.16638E-05 | 6E-12 | 8 | 1 | GeV^-2 |
| fine-structure constant | 0.00729735 | 1.1E-12 | 11 | 2 | None |
| first radiation constant | 3.74177E-16 | None | 10 | None | W m^2 |
| first radiation constant for spectral radiance | 1.19104E-16 | None | 10 | None | W m^2 sr^-1 |
| hartree-atomic mass unit relationship | 2.92126E-08 | 8.8E-18 | 12 | 2 | u |
| hartree-electron volt relationship | 27.2114 | 5.3E-11 | 14 | 2 | eV |
| Hartree energy | 4.35974E-18 | 8.5E-30 | 14 | 2 | J |
| Hartree energy in eV | 27.2114 | 5.3E-11 | 14 | 2 | eV |
| hartree-hertz relationship | 6.57968E+15 | 13000.0 | 13 | 2 | Hz |
| hartree-inverse meter relationship | 2.19475E+07 | 4.3E-05 | 14 | 2 | m^-1 |
| hartree-joule relationship | 4.35974E-18 | 8.5E-30 | 14 | 2 | J |
| hartree-kelvin relationship | 315775 | 6.1E-07 | 14 | 2 | K |
| hartree-kilogram relationship | 4.85087E-35 | 9.4E-47 | 14 | 2 | kg |
| helion-electron mass ratio | 5495.89 | 2.4E-07 | 12 | 2 | None |
| helion g factor | -4.255250615 | 5E-08 | 10 | 2 | None |
| helion mag. mom. | -1.07462E-26 | 1.3E-34 | 10 | 2 | J T^-1 |
| helion mag. mom. to Bohr magneton ratio | -0.00115874 | 1.4E-11 | 10 | 2 | None |
| helion mag. mom. to nuclear magneton ratio | -2.127625307 | 2.5E-08 | 10 | 2 | None |
| helion mass | 5.00641E-27 | 1.5E-36 | 11 | 2 | kg |
| helion mass energy equivalent | 4.49954E-10 | 1.4E-19 | 11 | 2 | J |
| helion mass energy equivalent in MeV | 2808.39 | 8.5E-07 | 12 | 2 | MeV |
| helion mass in u | 3.01493 | 9.7E-11 | 13 | 2 | u |
| helion molar mass | 0.00301493 | 9.1E-13 | 12 | 2 | kg mol^-1 |
| helion-proton mass ratio | 2.99315 | 1.3E-10 | 12 | 2 | None |
| helion relative atomic mass | 3.01493 | 9.7E-11 | 13 | 2 | None |
| helion shielding shift | 5.996743E-05 | 1E-10 | 7 | 2 | None |
| hertz-atomic mass unit relationship | 4.43982E-24 | 1.3E-33 | 11 | 2 | u |
| hertz-electron volt relationship | 4.13567E-15 | None | 10 | None | eV |
| hertz-hartree relationship | 1.51983E-16 | 2.9E-28 | 14 | 2 | E_h |
| hertz-inverse meter relationship | 3.33564E-09 | None | 10 | None | m^-1 |
| hertz-joule relationship | 6.62607E-34 | None | 9 | None | J |
| hertz-kelvin relationship | 4.79924E-11 | None | 10 | None | K |
| hertz-kilogram relationship | 7.3725E-51 | None | 10 | None | kg |
| hyperfine transition frequency of Cs-133 | 9192631770.0 | None | 10 | None | Hz |
| inverse fine-structure constant | 137.036 | 2.1E-08 | 12 | 2 | None |
| inverse meter-atomic mass unit relationship | 1.33103E-15 | 4E-25 | 12 | 2 | u |
| inverse meter-electron volt relationship | 1.23984E-06 | None | 10 | None | eV |
| inverse meter-hartree relationship | 4.55634E-08 | 8.8E-20 | 14 | 2 | E_h |
| inverse meter-hertz relationship | 299792458\.0 | None | 9 | None | Hz |
| inverse meter-joule relationship | 1.98645E-25 | None | 10 | None | J |
| inverse meter-kelvin relationship | 0.0143878 | None | 10 | None | K |
| inverse meter-kilogram relationship | 2.21022E-42 | None | 10 | None | kg |
| inverse of conductance quantum | 12906.40372 | None | 10 | None | ohm |
| Josephson constant | 4.83598E+14 | None | 10 | None | Hz V^-1 |
| joule-atomic mass unit relationship | 6700535256.5 | 2.0 | 11 | 2 | u |
| joule-electron volt relationship | 6.24151E+18 | None | 10 | None | eV |
| joule-hartree relationship | 2.29371E+17 | 450000.0 | 14 | 2 | E_h |
| joule-hertz relationship | 1.50919E+33 | None | 10 | None | Hz |
| joule-inverse meter relationship | 5.03412E+24 | None | 10 | None | m^-1 |
| joule-kelvin relationship | 7.24297E+22 | None | 10 | None | K |
| joule-kilogram relationship | 1.11265E-17 | None | 10 | None | kg |
| kelvin-atomic mass unit relationship | 9.25109E-14 | 2.8E-23 | 11 | 2 | u |
| kelvin-electron volt relationship | 8.61733E-05 | None | 10 | None | eV |
| kelvin-hartree relationship | 3.16681E-06 | 6.1E-18 | 14 | 2 | E_h |
| kelvin-hertz relationship | 20836619120 | None | 10 | None | Hz |
| kelvin-inverse meter relationship | 69.50348004 | None | 10 | None | m^-1 |
| kelvin-joule relationship | 1.380649E-23 | None | 7 | None | J |
| kelvin-kilogram relationship | 1.53618E-40 | None | 10 | None | kg |
| kilogram-atomic mass unit relationship | 6.02214E+26 | 1.8E+17 | 11 | 2 | u |
| kilogram-electron volt relationship | 5.60959E+35 | None | 10 | None | eV |
| kilogram-hartree relationship | 2.06149E+34 | 4E+22 | 14 | 2 | E_h |
| kilogram-hertz relationship | 1.35639E+50 | None | 10 | None | Hz |
| kilogram-inverse meter relationship | 4.52444E+41 | None | 10 | None | m^-1 |
| kilogram-joule relationship | 8.98755E+16 | None | 10 | None | J |
| kilogram-kelvin relationship | 6.50966E+39 | None | 10 | None | K |
| lattice parameter of silicon | 5.43102E-10 | 8.9E-18 | 10 | 2 | m |
| lattice spacing of ideal Si (220) | 1.92016E-10 | 3.2E-18 | 10 | 2 | m |
| Loschmidt constant (273.15 K, 100 kPa) | 2.65165E+25 | None | 10 | None | m^-3 |
| Loschmidt constant (273.15 K, 101.325 kPa) | 2.68678E+25 | None | 10 | None | m^-3 |
| luminous efficacy | 683.0 | None | 3 | None | lm W^-1 |
| mag. flux quantum | 2.06783E-15 | None | 10 | None | Wb |
| molar gas constant | 8.314462618 | None | 10 | None | J mol^-1 K^-1 |
| molar mass constant | 0.001 | 3E-13 | 11 | 2 | kg mol^-1 |
| molar mass of carbon-12 | 0.012 | 3.6E-12 | 12 | 2 | kg mol^-1 |
| molar Planck constant | 3.99031E-10 | None | 10 | None | J Hz^-1 mol^-1 |
| molar volume of ideal gas (273.15 K, 100 kPa) | 0.022711 | None | 10 | None | m^3 mol^-1 |
| molar volume of ideal gas (273.15 K, 101.325 kPa) | 0.022414 | None | 10 | None | m^3 mol^-1 |
| molar volume of silicon | 1.20588E-05 | 6E-13 | 10 | 2 | m^3 mol^-1 |
| Molybdenum x unit | 1.0021E-13 | 5.3E-20 | 9 | 2 | m |
| muon Compton wavelength | 1.17344E-14 | 2.6E-22 | 10 | 2 | m |
| muon-electron mass ratio | 206.768283 | 4.6E-06 | 10 | 2 | None |
| muon g factor | -2.00233 | 1.3E-09 | 11 | 2 | None |
| muon mag. mom. | -4.49045E-26 | 1E-33 | 9 | 2 | J T^-1 |
| muon mag. mom. anomaly | 0.00116592 | 6.3E-10 | 9 | 2 | None |
| muon mag. mom. to Bohr magneton ratio | -0.00484197 | 1.1E-10 | 9 | 2 | None |
| muon mag. mom. to nuclear magneton ratio | -8.89059703 | 2E-07 | 9 | 2 | None |
| muon mass | 1.88353E-28 | 4.2E-36 | 10 | 2 | kg |
| muon mass energy equivalent | 1.69283E-11 | 3.8E-19 | 10 | 2 | J |
| muon mass energy equivalent in MeV | 105.6583755 | 2.3E-06 | 10 | 2 | MeV |
| muon mass in u | 0.1134289259 | 2.5E-09 | 10 | 2 | u |
| muon molar mass | 0.000113429 | 2.5E-12 | 10 | 2 | kg mol^-1 |
| muon-neutron mass ratio | 0.112454517 | 2.5E-09 | 10 | 2 | None |
| muon-proton mag. mom. ratio | -3.183345142 | 7.1E-08 | 10 | 2 | None |
| muon-proton mass ratio | 0.1126095264 | 2.5E-09 | 10 | 2 | None |
| muon-tau mass ratio | 0.0594635 | 4E-06 | 6 | 2 | None |
| natural unit of action | 1.05457E-34 | None | 10 | None | J s |
| natural unit of action in eV s | 6.58212E-16 | None | 10 | None | eV s |
| natural unit of energy | 8.18711E-14 | 2.5E-23 | 11 | 2 | J |
| natural unit of energy in MeV | 0.51099895 | 1.5E-10 | 11 | 2 | MeV |
| natural unit of length | 3.86159E-13 | 1.2E-22 | 11 | 2 | m |
| natural unit of mass | 9.10938E-31 | 2.8E-40 | 11 | 2 | kg |
| natural unit of momentum | 2.73092E-22 | 8.2E-32 | 12 | 2 | kg m s^-1 |
| natural unit of momentum in MeV/c | 0.51099895 | 1.5E-10 | 11 | 2 | MeV / c |
| natural unit of time | 1.28809E-21 | 3.9E-31 | 12 | 2 | s |
| natural unit of velocity | 299792458\.0 | None | 9 | None | m s^-1 |
| neutron Compton wavelength | 1.31959E-15 | 7.5E-25 | 12 | 2 | m |
| neutron-electron mag. mom. ratio | 0.00104067 | 2.5E-10 | 9 | 2 | None |
| neutron-electron mass ratio | 1838.68 | 8.9E-07 | 12 | 2 | None |
| neutron g factor | -3.82608545 | 9E-07 | 9 | 2 | None |
| neutron gyromag. ratio | 183247171\.0 | 43.0 | 9 | 2 | s^-1 T^-1 |
| neutron gyromag. ratio in MHz/T | 29.1646931 | 6.9E-06 | 9 | 2 | MHz T^-1 |
| neutron mag. mom. | -9.66237E-27 | 2.3E-33 | 8 | 2 | J T^-1 |
| neutron mag. mom. to Bohr magneton ratio | -0.00104188 | 2.5E-10 | 9 | 2 | None |
| neutron mag. mom. to nuclear magneton ratio | -1.91304273 | 4.5E-07 | 9 | 2 | None |
| neutron mass | 1.67493E-27 | 9.5E-37 | 12 | 2 | kg |
| neutron mass energy equivalent | 1.50535E-10 | 8.6E-20 | 12 | 2 | J |
| neutron mass energy equivalent in MeV | 939.56542052 | 5.4E-07 | 11 | 2 | MeV |
| neutron mass in u | 1.00866 | 4.9E-10 | 12 | 2 | u |
| neutron molar mass | 0.00100866 | 5.7E-13 | 12 | 2 | kg mol^-1 |
| neutron-muon mass ratio | 8.89248406 | 2E-07 | 9 | 2 | None |
| neutron-proton mag. mom. ratio | -0.68497934 | 1.6E-07 | 8 | 2 | None |
| neutron-proton mass difference | 2.30557E-30 | 8.2E-37 | 9 | 2 | kg |
| neutron-proton mass difference energy equivalent | 2.07215E-13 | 7.4E-20 | 9 | 2 | J |
| neutron-proton mass difference energy equivalent in MeV | 1.29333236 | 4.6E-07 | 9 | 2 | MeV |
| neutron-proton mass difference in u | 0.00138845 | 4.9E-10 | 9 | 2 | u |
| neutron-proton mass ratio | 1.00138 | 4.9E-10 | 12 | 2 | None |
| neutron relative atomic mass | 1.00866 | 4.9E-10 | 12 | 2 | None |
| neutron-tau mass ratio | 0.528779 | 3.6E-05 | 6 | 2 | None |
| neutron to shielded proton mag. mom. ratio | -0.68499694 | 1.6E-07 | 8 | 2 | None |
| Newtonian constant of gravitation | 6.6743E-11 | 1.5E-15 | 6 | 2 | m^3 kg^-1 s^-2 |
| Newtonian constant of gravitation over h-bar c | 6.70883E-39 | 1.5E-43 | 6 | 2 | ( GeV / c^2 )^-2 |
| nuclear magneton | 5.05078E-27 | 1.5E-36 | 11 | 2 | J T^-1 |
| nuclear magneton in eV/T | 3.15245E-08 | 9.6E-18 | 12 | 2 | eV T^-1 |
| nuclear magneton in inverse meter per tesla | 0.0254262 | 7.8E-12 | 12 | 2 | m^-1 T^-1 |
| nuclear magneton in K/T | 0.000365827 | 1.1E-13 | 11 | 2 | K T^-1 |
| nuclear magneton in MHz/T | 7.6225932291 | 2.3E-09 | 11 | 2 | MHz T^-1 |
| Planck constant | 6.62607E-34 | None | 9 | None | J Hz^-1 |
| Planck constant in eV/Hz | 4.13567E-15 | None | 10 | None | eV Hz^-1 |
| Planck length | 1.616255E-35 | 1.8E-40 | 7 | 2 | m |
| Planck mass | 2.176434E-08 | 2.4E-13 | 7 | 2 | kg |
| Planck mass energy equivalent in GeV | 1.22089E+19 | 1.4E+14 | 7 | 2 | GeV |
| Planck temperature | 1.416784E+32 | 1.6E+27 | 7 | 2 | K |
| Planck time | 5.39125E-44 | 6E-49 | 7 | 2 | s |
| proton charge to mass quotient | 95788331.56 | 0.029 | 11 | 2 | C kg^-1 |
| proton Compton wavelength | 1.32141E-15 | 4E-25 | 12 | 2 | m |
| proton-electron mass ratio | 1836.15 | 1.1E-07 | 12 | 2 | None |
| proton g factor | 5.5856946893 | 1.6E-09 | 11 | 2 | None |
| proton gyromag. ratio | 267522187\.44 | 0.11 | 11 | 2 | s^-1 T^-1 |
| proton gyromag. ratio in MHz/T | 42.577478518 | 1.8E-08 | 11 | 2 | MHz T^-1 |
| proton mag. mom. | 1.41061E-26 | 6E-36 | 12 | 2 | J T^-1 |
| proton mag. mom. to Bohr magneton ratio | 0.00152103 | 4.6E-13 | 12 | 2 | None |
| proton mag. mom. to nuclear magneton ratio | 2.79285 | 8.2E-10 | 12 | 2 | None |
| proton mag. shielding correction | 2.5689E-05 | 1.1E-08 | 5 | 2 | None |
| proton mass | 1.67262E-27 | 5.1E-37 | 12 | 2 | kg |
| proton mass energy equivalent | 1.50328E-10 | 4.6E-20 | 12 | 2 | J |
| proton mass energy equivalent in MeV | 938.27208816 | 2.9E-07 | 11 | 2 | MeV |
| proton mass in u | 1.00728 | 5.3E-11 | 13 | 2 | u |
| proton molar mass | 0.00100728 | 3.1E-13 | 12 | 2 | kg mol^-1 |
| proton-muon mass ratio | 8.88024337 | 2E-07 | 9 | 2 | None |
| proton-neutron mag. mom. ratio | -1.45989805 | 3.4E-07 | 9 | 2 | None |
| proton-neutron mass ratio | 0.998623 | 4.9E-10 | 11 | 2 | None |
| proton relative atomic mass | 1.00728 | 5.3E-11 | 13 | 2 | None |
| proton rms charge radius | 8.414E-16 | 1.9E-18 | 4 | 2 | m |
| proton-tau mass ratio | 0.528051 | 3.6E-05 | 6 | 2 | None |
| quantum of circulation | 0.000363695 | 1.1E-13 | 11 | 2 | m^2 s^-1 |
| quantum of circulation times 2 | 0.00072739 | 2.2E-13 | 11 | 2 | m^2 s^-1 |
| reduced Compton wavelength | 3.86159E-13 | 1.2E-22 | 11 | 2 | m |
| reduced muon Compton wavelength | 1.86759E-15 | 4.2E-23 | 10 | 2 | m |
| reduced neutron Compton wavelength | 2.10019E-16 | 1.2E-25 | 11 | 2 | m |
| reduced Planck constant | 1.05457E-34 | None | 10 | None | J s |
| reduced Planck constant in eV s | 6.58212E-16 | None | 10 | None | eV s |
| reduced Planck constant times c in MeV fm | 197.3269804 | None | 10 | None | MeV fm |
| reduced proton Compton wavelength | 2.10309E-16 | 6.4E-26 | 12 | 2 | m |
| reduced tau Compton wavelength | 1.110538E-16 | 7.5E-21 | 7 | 2 | m |
| Rydberg constant | 1.09737E+07 | 2.1E-05 | 14 | 2 | m^-1 |
| Rydberg constant times c in Hz | 3.28984E+15 | 6400.0 | 14 | 2 | Hz |
| Rydberg constant times hc in eV | 13.6057 | 2.6E-11 | 14 | 2 | eV |
| Rydberg constant times hc in J | 2.17987E-18 | 4.2E-30 | 14 | 2 | J |
| Sackur-Tetrode constant (1 K, 100 kPa) | -1.15171 | 4.5E-10 | 12 | 2 | None |
| Sackur-Tetrode constant (1 K, 101.325 kPa) | -1.16487 | 4.5E-10 | 12 | 2 | None |
| second radiation constant | 0.0143878 | None | 10 | None | m K |
| shielded helion gyromag. ratio | 203789456\.9 | 2.4 | 10 | 2 | s^-1 T^-1 |
| shielded helion gyromag. ratio in MHz/T | 32.43409942 | 3.8E-07 | 10 | 2 | MHz T^-1 |
| shielded helion mag. mom. | -1.07455E-26 | 1.3E-34 | 10 | 2 | J T^-1 |
| shielded helion mag. mom. to Bohr magneton ratio | -0.00115867 | 1.4E-11 | 10 | 2 | None |
| shielded helion mag. mom. to nuclear magneton ratio | -2.127497719 | 2.5E-08 | 10 | 2 | None |
| shielded helion to proton mag. mom. ratio | -0.761767 | 8.9E-09 | 10 | 2 | None |
| shielded helion to shielded proton mag. mom. ratio | -0.761786 | 3.3E-09 | 10 | 2 | None |
| shielded proton gyromag. ratio | 267515315\.1 | 2.9 | 10 | 2 | s^-1 T^-1 |
| shielded proton gyromag. ratio in MHz/T | 42.57638474 | 4.6E-07 | 10 | 2 | MHz T^-1 |
| shielded proton mag. mom. | 1.41057E-26 | 1.5E-34 | 10 | 2 | J T^-1 |
| shielded proton mag. mom. to Bohr magneton ratio | 0.00152099 | 1.7E-11 | 10 | 2 | None |
| shielded proton mag. mom. to nuclear magneton ratio | 2.792775599 | 3E-08 | 10 | 2 | None |
| shielding difference of d and p in HD | 2.02E-08 | 2E-11 | 5 | 2 | None |
| shielding difference of t and p in HT | 2.414E-08 | 2E-11 | 5 | 2 | None |
| speed of light in vacuum | 299792458\.0 | None | 9 | None | m s^-1 |
| standard acceleration of gravity | 9.80665 | None | 6 | None | m s^-2 |
| standard atmosphere | 101325.0 | None | 6 | None | Pa |
| standard-state pressure | 100000.0 | None | 6 | None | Pa |
| Stefan-Boltzmann constant | 5.67037E-08 | None | 10 | None | W m^-2 K^-4 |
| tau Compton wavelength | 6.97771E-16 | 4.7E-20 | 6 | 2 | m |
| tau-electron mass ratio | 3477.23 | 0.23 | 6 | 2 | None |
| tau energy equivalent | 1776.86 | 0.12 | 6 | 2 | MeV |
| tau mass | 3.16754E-27 | 2.1E-31 | 6 | 2 | kg |
| tau mass energy equivalent | 2.84684E-10 | 1.9E-14 | 6 | 2 | J |
| tau mass in u | 1.90754 | 0.00013 | 6 | 2 | u |
| tau molar mass | 0.00190754 | 1.3E-07 | 6 | 2 | kg mol^-1 |
| tau-muon mass ratio | 16.817 | 0.0011 | 6 | 2 | None |
| tau-neutron mass ratio | 1.89115 | 0.00013 | 6 | 2 | None |
| tau-proton mass ratio | 1.89376 | 0.00013 | 6 | 2 | None |
| Thomson cross section | 6.65246E-29 | 6E-38 | 11 | 2 | m^2 |
| triton-electron mass ratio | 5496.92 | 2.7E-07 | 12 | 2 | None |
| triton g factor | 5.957924931 | 1.2E-08 | 10 | 2 | None |
| triton mag. mom. | 1.50461E-26 | 3E-35 | 11 | 2 | J T^-1 |
| triton mag. mom. to Bohr magneton ratio | 0.00162239 | 3.2E-12 | 11 | 2 | None |
| triton mag. mom. to nuclear magneton ratio | 2.9789624656 | 5.9E-09 | 11 | 2 | None |
| triton mass | 5.00736E-27 | 1.5E-36 | 11 | 2 | kg |
| triton mass energy equivalent | 4.50039E-10 | 1.4E-19 | 11 | 2 | J |
| triton mass energy equivalent in MeV | 2808.92 | 8.5E-07 | 12 | 2 | MeV |
| triton mass in u | 3.0155 | 1.2E-10 | 12 | 2 | u |
| triton molar mass | 0.0030155 | 9.2E-13 | 12 | 2 | kg mol^-1 |
| triton-proton mass ratio | 2.99372 | 1.5E-10 | 12 | 2 | None |
| triton relative atomic mass | 3.0155 | 1.2E-10 | 12 | 2 | None |
| triton to proton mag. mom. ratio | 1.0666399191 | 2.1E-09 | 11 | 2 | None |
| unified atomic mass unit | 1.66054E-27 | 5E-37 | 12 | 2 | kg |
| vacuum electric permittivity | 8.85419E-12 | 1.3E-21 | 11 | 2 | F m^-1 |
| vacuum mag. permeability | 1.25664E-06 | 1.9E-16 | 12 | 2 | N A^-2 |
| von Klitzing constant | 25812.80745 | None | 10 | None | ohm |
| weak mixing angle | 0.2229 | 0.0003 | 5 | 2 | None |
| Wien frequency displacement law constant | 58789257570 | None | 10 | None | Hz K^-1 |
| Wien wavelength displacement law constant | 0.00289777 | None | 10 | None | m K |
| W to Z mass ratio | 0.88153 | 0.00017 | 5 | 2 | None |
