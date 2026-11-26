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
| alpha particle-electron mass ratio | 7294.29954142 | 2.4e-07 | 12 | 2 | None |
| alpha particle mass | 6.6446573357e-27 | 2e-36 | 11 | 2 | kg |
| alpha particle mass energy equivalent | 5.9719201914e-10 | 1.8e-19 | 11 | 2 | J |
| alpha particle mass energy equivalent in MeV | 3727.3794066 | 1.1e-06 | 11 | 2 | MeV |
| alpha particle mass in u | 4.001506179127 | 6.3e-11 | 13 | 2 | u |
| alpha particle molar mass | 0.0040015061777 | 1.2e-12 | 11 | 2 | kg mol^-1 |
| alpha particle-proton mass ratio | 3.97259969009 | 2.2e-10 | 12 | 2 | None |
| alpha particle relative atomic mass | 4.001506179127 | 6.3e-11 | 13 | 2 | None |
| Angstrom star | 1.00001495e-10 | 9e-17 | 9 | 2 | m |
| atomic mass constant | 1.6605390666e-27 | 5e-37 | 12 | 2 | kg |
| atomic mass constant energy equivalent | 1.4924180856e-10 | 4.5e-20 | 12 | 2 | J |
| atomic mass constant energy equivalent in MeV | 931.49410242 | 2.8e-07 | 11 | 2 | MeV |
| atomic mass unit-electron volt relationship | 931494102\.42 | 0.28 | 11 | 2 | eV |
| atomic mass unit-hartree relationship | 34231776.874 | 0.01 | 11 | 2 | E_h |
| atomic mass unit-hertz relationship | 2.25234271871e+23 | 68000000000000.0 | 12 | 2 | Hz |
| atomic mass unit-inverse meter relationship | 751300661040000.0 | 230000.0 | 11 | 2 | m^-1 |
| atomic mass unit-joule relationship | 1.4924180856e-10 | 4.5e-20 | 12 | 2 | J |
| atomic mass unit-kelvin relationship | 10809540191600.0 | 3300.0 | 12 | 2 | K |
| atomic mass unit-kilogram relationship | 1.6605390666e-27 | 5e-37 | 12 | 2 | kg |
| atomic unit of 1st hyperpolarizability | 3.2063613061e-53 | 1.4999999999999998e-62 | 11 | 2 | C^3 m^3 J^-2 |
| atomic unit of 2nd hyperpolarizability | 6.2353799904999995e-65 | 3.8e-74 | 11 | 2 | C^4 m^4 J^-3 |
| atomic unit of action | 1.054571817e-34 | None | 10 | None | J s |
| atomic unit of charge | 1.6021766340000001e-19 | None | 10 | None | C |
| atomic unit of charge density | 1081202384570.0 | 490.0 | 12 | 2 | C m^-3 |
| atomic unit of current | 0.00662361823751 | 1.3e-14 | 13 | 2 | A |
| atomic unit of electric dipole mom. | 8.4783536255e-30 | 1.3e-39 | 11 | 2 | C m |
| atomic unit of electric field | 514220674763.0 | 78.0 | 12 | 2 | V m^-1 |
| atomic unit of electric field gradient | 9.7173624292e+21 | 2900000000000.0 | 11 | 2 | V m^-2 |
| atomic unit of electric polarizability | 1.64877727436e-41 | 5e-51 | 12 | 2 | C^2 m^2 J^-1 |
| atomic unit of electric potential | 27.211386245988 | 5.3e-11 | 14 | 2 | V |
| atomic unit of electric quadrupole mom. | 4.4865515246e-40 | 1.4e-49 | 11 | 2 | C m^2 |
| atomic unit of energy | 4.3597447222071e-18 | 8.500000000000001e-30 | 14 | 2 | J |
| atomic unit of force | 8.2387234983e-08 | 1.2e-17 | 11 | 2 | N |
| atomic unit of length | 5.29177210903e-11 | 8e-21 | 12 | 2 | m |
| atomic unit of mag. dipole mom. | 1.8548020156599998e-23 | 5.6e-33 | 12 | 2 | J T^-1 |
| atomic unit of mag. flux density | 235051.756758 | 7.1e-05 | 12 | 2 | T |
| atomic unit of magnetizability | 7.8910366008e-29 | 4.799999999999999e-38 | 11 | 2 | J T^-2 |
| atomic unit of mass | 9.1093837015e-31 | 2.8e-40 | 11 | 2 | kg |
| atomic unit of momentum | 1.9928519141e-24 | 3e-34 | 12 | 2 | kg m s^-1 |
| atomic unit of permittivity | 1.11265005545e-10 | 1.7e-20 | 12 | 2 | F m^-1 |
| atomic unit of time | 2.4188843265857e-17 | 4.7e-29 | 14 | 2 | s |
| atomic unit of velocity | 2187691.26364 | 0.00033 | 12 | 2 | m s^-1 |
| Avogadro constant | 6.02214076e+23 | None | 9 | None | mol^-1 |
| Bohr magneton | 9.274010078299999e-24 | 2.8e-33 | 11 | 2 | J T^-1 |
| Bohr magneton in eV/T | 5.788381806e-05 | 1.7e-14 | 11 | 2 | eV T^-1 |
| Bohr magneton in Hz/T | 13996244936.1 | 4.2 | 12 | 2 | Hz T^-1 |
| Bohr magneton in inverse meter per tesla | 46.686447783 | 1.4e-08 | 11 | 2 | m^-1 T^-1 |
| Bohr magneton in K/T | 0.67171381563 | 2e-10 | 11 | 2 | K T^-1 |
| Bohr radius | 5.29177210903e-11 | 8e-21 | 12 | 2 | m |
| Boltzmann constant | 1.380649e-23 | None | 7 | None | J K^-1 |
| Boltzmann constant in eV/K | 8.617333262e-05 | None | 10 | None | eV K^-1 |
| Boltzmann constant in Hz/K | 20836619120.0 | None | 10 | None | Hz K^-1 |
| Boltzmann constant in inverse meter per kelvin | 69.50348004 | None | 10 | None | m^-1 K^-1 |
| characteristic impedance of vacuum | 376.730313668 | 5.7e-08 | 12 | 2 | ohm |
| classical electron radius | 2.8179403261999996e-15 | 1.2999999999999998e-24 | 11 | 2 | m |
| Compton wavelength | 2.4263102386700002e-12 | 7.3e-22 | 12 | 2 | m |
| conductance quantum | 7.748091729e-05 | None | 10 | None | S |
| conventional value of ampere-90 | 1.00000008887 | None | 12 | None | A |
| conventional value of coulomb-90 | 1.00000008887 | None | 12 | None | C |
| conventional value of farad-90 | 0.9999999822 | None | 11 | None | F |
| conventional value of henry-90 | 1.00000001779 | None | 12 | None | H |
| conventional value of Josephson constant | 483597900000000.0 | None | 7 | None | Hz V^-1 |
| conventional value of ohm-90 | 1.00000001779 | None | 12 | None | ohm |
| conventional value of volt-90 | 1.00000010666 | None | 12 | None | V |
| conventional value of von Klitzing constant | 25812.807 | None | 8 | None | ohm |
| conventional value of watt-90 | 1.00000019553 | None | 12 | None | W |
| Copper x unit | 1.00207697e-13 | 2.8e-20 | 9 | 2 | m |
| deuteron-electron mag. mom. ratio | -0.0004664345551 | 1.2e-12 | 10 | 2 | None |
| deuteron-electron mass ratio | 3670.48296788 | 1.3e-07 | 12 | 2 | None |
| deuteron g factor | 0.8574382338 | 2.2e-09 | 10 | 2 | None |
| deuteron mag. mom. | 4.330735094e-27 | 1.1e-35 | 10 | 2 | J T^-1 |
| deuteron mag. mom. to Bohr magneton ratio | 0.000466975457 | 1.2e-12 | 10 | 2 | None |
| deuteron mag. mom. to nuclear magneton ratio | 0.8574382338 | 2.2e-09 | 10 | 2 | None |
| deuteron mass | 3.3435837724e-27 | 1e-36 | 11 | 2 | kg |
| deuteron mass energy equivalent | 3.00506323102e-10 | 9.1e-20 | 12 | 2 | J |
| deuteron mass energy equivalent in MeV | 1875.61294257 | 5.7e-07 | 12 | 2 | MeV |
| deuteron mass in u | 2.013553212745 | 4e-11 | 13 | 2 | u |
| deuteron molar mass | 0.00201355321205 | 6.1e-13 | 12 | 2 | kg mol^-1 |
| deuteron-neutron mag. mom. ratio | -0.44820653 | 1.1e-07 | 8 | 2 | None |
| deuteron-proton mag. mom. ratio | 0.30701220939 | 7.9e-10 | 11 | 2 | None |
| deuteron-proton mass ratio | 1.99900750139 | 1.1e-10 | 12 | 2 | None |
| deuteron relative atomic mass | 2.013553212745 | 4e-11 | 13 | 2 | None |
| deuteron rms charge radius | 2.12799e-15 | 7.4e-19 | 6 | 2 | m |
| electron charge to mass quotient | -175882001076.0 | 53.0 | 12 | 2 | C kg^-1 |
| electron-deuteron mag. mom. ratio | -2143.9234915 | 5.6e-06 | 11 | 2 | None |
| electron-deuteron mass ratio | 0.0002724437107462 | 9.6e-15 | 13 | 2 | None |
| electron g factor | -2.00231930436256 | 3.5e-13 | 15 | 2 | None |
| electron gyromag. ratio | 176085963023.0 | 53.0 | 12 | 2 | s^-1 T^-1 |
| electron gyromag. ratio in MHz/T | 28024.9514242 | 8.5e-06 | 12 | 2 | MHz T^-1 |
| electron-helion mass ratio | 0.0001819543074573 | 7.9e-15 | 13 | 2 | None |
| electron mag. mom. | -9.284764704299999e-24 | 2.8e-33 | 11 | 2 | J T^-1 |
| electron mag. mom. anomaly | 0.00115965218128 | 1.8e-13 | 12 | 2 | None |
| electron mag. mom. to Bohr magneton ratio | -1.00115965218128 | 1.8e-13 | 15 | 2 | None |
| electron mag. mom. to nuclear magneton ratio | -1838.28197188 | 1.1e-07 | 12 | 2 | None |
| electron mass | 9.1093837015e-31 | 2.8e-40 | 11 | 2 | kg |
| electron mass energy equivalent | 8.1871057769e-14 | 2.5e-23 | 11 | 2 | J |
| electron mass energy equivalent in MeV | 0.51099895 | 1.5e-10 | 11 | 2 | MeV |
| electron mass in u | 0.000548579909065 | 1.6e-14 | 12 | 2 | u |
| electron molar mass | 5.4857990888e-07 | 1.7e-16 | 11 | 2 | kg mol^-1 |
| electron-muon mag. mom. ratio | 206.7669883 | 4.6e-06 | 10 | 2 | None |
| electron-muon mass ratio | 0.00483633169 | 1.1e-10 | 9 | 2 | None |
| electron-neutron mag. mom. ratio | 960.9205 | 0.00023 | 8 | 2 | None |
| electron-neutron mass ratio | 0.00054386734424 | 2.6e-13 | 11 | 2 | None |
| electron-proton mag. mom. ratio | -658.21068789 | 2e-07 | 11 | 2 | None |
| electron-proton mass ratio | 0.000544617021487 | 3.3e-14 | 12 | 2 | None |
| electron relative atomic mass | 0.000548579909065 | 1.6e-14 | 12 | 2 | None |
| electron-tau mass ratio | 0.000287585 | 1.9e-08 | 6 | 2 | None |
| electron to alpha particle mass ratio | 0.0001370933554787 | 4.5e-15 | 13 | 2 | None |
| electron to shielded helion mag. mom. ratio | 864.058257 | 1e-05 | 9 | 2 | None |
| electron to shielded proton mag. mom. ratio | -658.2275971 | 7.2e-06 | 10 | 2 | None |
| electron-triton mass ratio | 0.0001819200062251 | 9e-15 | 13 | 2 | None |
| electron volt | 1.6021766340000001e-19 | None | 10 | None | J |
| electron volt-atomic mass unit relationship | 1.07354410233e-09 | 3.2e-19 | 12 | 2 | u |
| electron volt-hartree relationship | 0.036749322175655 | 7.1e-14 | 14 | 2 | E_h |
| electron volt-hertz relationship | 241798924200000.0 | None | 10 | None | Hz |
| electron volt-inverse meter relationship | 806554.3937 | None | 10 | None | m^-1 |
| electron volt-joule relationship | 1.6021766340000001e-19 | None | 10 | None | J |
| electron volt-kelvin relationship | 11604.51812 | None | 10 | None | K |
| electron volt-kilogram relationship | 1.782661921e-36 | None | 10 | None | kg |
| elementary charge | 1.6021766340000001e-19 | None | 10 | None | C |
| elementary charge over h-bar | 1519267447000000.0 | None | 10 | None | A J^-1 |
| Faraday constant | 96485.33212 | None | 10 | None | C mol^-1 |
| Fermi coupling constant | 1.1663787e-05 | 6e-12 | 8 | 1 | GeV^-2 |
| fine-structure constant | 0.0072973525693 | 1.1e-12 | 11 | 2 | None |
| first radiation constant | 3.7417718519999997e-16 | None | 10 | None | W m^2 |
| first radiation constant for spectral radiance | 1.1910429719999999e-16 | None | 10 | None | W m^2 sr^-1 |
| hartree-atomic mass unit relationship | 2.92126232205e-08 | 8.8e-18 | 12 | 2 | u |
| hartree-electron volt relationship | 27.211386245988 | 5.3e-11 | 14 | 2 | eV |
| Hartree energy | 4.3597447222071e-18 | 8.500000000000001e-30 | 14 | 2 | J |
| Hartree energy in eV | 27.211386245988 | 5.3e-11 | 14 | 2 | eV |
| hartree-hertz relationship | 6579683920502000.0 | 13000.0 | 13 | 2 | Hz |
| hartree-inverse meter relationship | 21947463.13632 | 4.3e-05 | 14 | 2 | m^-1 |
| hartree-joule relationship | 4.3597447222071e-18 | 8.500000000000001e-30 | 14 | 2 | J |
| hartree-kelvin relationship | 315775.02480407 | 6.1e-07 | 14 | 2 | K |
| hartree-kilogram relationship | 4.850870209543199e-35 | 9.4e-47 | 14 | 2 | kg |
| helion-electron mass ratio | 5495.88528007 | 2.4e-07 | 12 | 2 | None |
| helion g factor | -4.255250615 | 5e-08 | 10 | 2 | None |
| helion mag. mom. | -1.0746175320000001e-26 | 1.3e-34 | 10 | 2 | J T^-1 |
| helion mag. mom. to Bohr magneton ratio | -0.001158740958 | 1.4e-11 | 10 | 2 | None |
| helion mag. mom. to nuclear magneton ratio | -2.127625307 | 2.5e-08 | 10 | 2 | None |
| helion mass | 5.0064127795999995e-27 | 1.4999999999999999e-36 | 11 | 2 | kg |
| helion mass energy equivalent | 4.4995394125e-10 | 1.4e-19 | 11 | 2 | J |
| helion mass energy equivalent in MeV | 2808.39160743 | 8.5e-07 | 12 | 2 | MeV |
| helion mass in u | 3.014932247175 | 9.7e-11 | 13 | 2 | u |
| helion molar mass | 0.00301493224613 | 9.1e-13 | 12 | 2 | kg mol^-1 |
| helion-proton mass ratio | 2.99315267167 | 1.3e-10 | 12 | 2 | None |
| helion relative atomic mass | 3.014932247175 | 9.7e-11 | 13 | 2 | None |
| helion shielding shift | 5.996743e-05 | 1e-10 | 7 | 2 | None |
| hertz-atomic mass unit relationship | 4.4398216651999995e-24 | 1.3e-33 | 11 | 2 | u |
| hertz-electron volt relationship | 4.135667696e-15 | None | 10 | None | eV |
| hertz-hartree relationship | 1.5198298460570002e-16 | 2.9e-28 | 14 | 2 | E_h |
| hertz-inverse meter relationship | 3.335640951e-09 | None | 10 | None | m^-1 |
| hertz-joule relationship | 6.62607015e-34 | None | 9 | None | J |
| hertz-kelvin relationship | 4.799243073e-11 | None | 10 | None | K |
| hertz-kilogram relationship | 7.372497323000001e-51 | None | 10 | None | kg |
| hyperfine transition frequency of Cs-133 | 9192631770.0 | None | 10 | None | Hz |
| inverse fine-structure constant | 137.035999084 | 2.1e-08 | 12 | 2 | None |
| inverse meter-atomic mass unit relationship | 1.3310250501e-15 | 3.9999999999999997e-25 | 12 | 2 | u |
| inverse meter-electron volt relationship | 1.239841984e-06 | None | 10 | None | eV |
| inverse meter-hartree relationship | 4.556335252912e-08 | 8.8e-20 | 14 | 2 | E_h |
| inverse meter-hertz relationship | 299792458\.0 | None | 9 | None | Hz |
| inverse meter-joule relationship | 1.986445857e-25 | None | 10 | None | J |
| inverse meter-kelvin relationship | 0.01438776877 | None | 10 | None | K |
| inverse meter-kilogram relationship | 2.210219094e-42 | None | 10 | None | kg |
| inverse of conductance quantum | 12906.40372 | None | 10 | None | ohm |
| Josephson constant | 483597848400000.0 | None | 10 | None | Hz V^-1 |
| joule-atomic mass unit relationship | 6700535256.5 | 2.0 | 11 | 2 | u |
| joule-electron volt relationship | 6.241509074e+18 | None | 10 | None | eV |
| joule-hartree relationship | 2.2937122783963e+17 | 450000.0 | 14 | 2 | E_h |
| joule-hertz relationship | 1.509190179e+33 | None | 10 | None | Hz |
| joule-inverse meter relationship | 5.034116567e+24 | None | 10 | None | m^-1 |
| joule-kelvin relationship | 7.242970516e+22 | None | 10 | None | K |
| joule-kilogram relationship | 1.112650056e-17 | None | 10 | None | kg |
| kelvin-atomic mass unit relationship | 9.2510873014e-14 | 2.8000000000000003e-23 | 11 | 2 | u |
| kelvin-electron volt relationship | 8.617333262e-05 | None | 10 | None | eV |
| kelvin-hartree relationship | 3.1668115634556e-06 | 6.1e-18 | 14 | 2 | E_h |
| kelvin-hertz relationship | 20836619120.0 | None | 10 | None | Hz |
| kelvin-inverse meter relationship | 69.50348004 | None | 10 | None | m^-1 |
| kelvin-joule relationship | 1.380649e-23 | None | 7 | None | J |
| kelvin-kilogram relationship | 1.5361791869999999e-40 | None | 10 | None | kg |
| kilogram-atomic mass unit relationship | 6.0221407621e+26 | 1.8e+17 | 11 | 2 | u |
| kilogram-electron volt relationship | 5.6095886030000005e+35 | None | 10 | None | eV |
| kilogram-hartree relationship | 2.0614857887409e+34 | 4e+22 | 14 | 2 | E_h |
| kilogram-hertz relationship | 1.356392489e+50 | None | 10 | None | Hz |
| kilogram-inverse meter relationship | 4.5244383350000006e+41 | None | 10 | None | m^-1 |
| kilogram-joule relationship | 8.987551787e+16 | None | 10 | None | J |
| kilogram-kelvin relationship | 6.50965726e+39 | None | 10 | None | K |
| lattice parameter of silicon | 5.431020511e-10 | 8.9e-18 | 10 | 2 | m |
| lattice spacing of ideal Si (220) | 1.920155716e-10 | 3.2e-18 | 10 | 2 | m |
| Loschmidt constant (273.15 K, 100 kPa) | 2.651645804e+25 | None | 10 | None | m^-3 |
| Loschmidt constant (273.15 K, 101.325 kPa) | 2.686780111e+25 | None | 10 | None | m^-3 |
| luminous efficacy | 683.0 | None | 3 | None | lm W^-1 |
| mag. flux quantum | 2.067833848e-15 | None | 10 | None | Wb |
| molar gas constant | 8.314462618 | None | 10 | None | J mol^-1 K^-1 |
| molar mass constant | 0.00099999999965 | 3e-13 | 11 | 2 | kg mol^-1 |
| molar mass of carbon-12 | 0.0119999999958 | 3.6e-12 | 12 | 2 | kg mol^-1 |
| molar Planck constant | 3.990312712e-10 | None | 10 | None | J Hz^-1 mol^-1 |
| molar volume of ideal gas (273.15 K, 100 kPa) | 0.02271095464 | None | 10 | None | m^3 mol^-1 |
| molar volume of ideal gas (273.15 K, 101.325 kPa) | 0.02241396954 | None | 10 | None | m^3 mol^-1 |
| molar volume of silicon | 1.205883199e-05 | 6e-13 | 10 | 2 | m^3 mol^-1 |
| Molybdenum x unit | 1.00209952e-13 | 5.3e-20 | 9 | 2 | m |
| muon Compton wavelength | 1.1734441100000001e-14 | 2.6e-22 | 10 | 2 | m |
| muon-electron mass ratio | 206.768283 | 4.6e-06 | 10 | 2 | None |
| muon g factor | -2.0023318418 | 1.3e-09 | 11 | 2 | None |
| muon mag. mom. | -4.4904483e-26 | 9.999999999999999e-34 | 9 | 2 | J T^-1 |
| muon mag. mom. anomaly | 0.00116592089 | 6.3e-10 | 9 | 2 | None |
| muon mag. mom. to Bohr magneton ratio | -0.00484197047 | 1.1e-10 | 9 | 2 | None |
| muon mag. mom. to nuclear magneton ratio | -8.89059703 | 2e-07 | 9 | 2 | None |
| muon mass | 1.8835316269999999e-28 | 4.2e-36 | 10 | 2 | kg |
| muon mass energy equivalent | 1.692833804e-11 | 3.8e-19 | 10 | 2 | J |
| muon mass energy equivalent in MeV | 105.6583755 | 2.3e-06 | 10 | 2 | MeV |
| muon mass in u | 0.1134289259 | 2.5e-09 | 10 | 2 | u |
| muon molar mass | 0.0001134289259 | 2.5e-12 | 10 | 2 | kg mol^-1 |
| muon-neutron mass ratio | 0.112454517 | 2.5e-09 | 10 | 2 | None |
| muon-proton mag. mom. ratio | -3.183345142 | 7.1e-08 | 10 | 2 | None |
| muon-proton mass ratio | 0.1126095264 | 2.5e-09 | 10 | 2 | None |
| muon-tau mass ratio | 0.0594635 | 4e-06 | 6 | 2 | None |
| natural unit of action | 1.054571817e-34 | None | 10 | None | J s |
| natural unit of action in eV s | 6.582119568999999e-16 | None | 10 | None | eV s |
| natural unit of energy | 8.1871057769e-14 | 2.5e-23 | 11 | 2 | J |
| natural unit of energy in MeV | 0.51099895 | 1.5e-10 | 11 | 2 | MeV |
| natural unit of length | 3.8615926796000003e-13 | 1.2e-22 | 11 | 2 | m |
| natural unit of mass | 9.1093837015e-31 | 2.8e-40 | 11 | 2 | kg |
| natural unit of momentum | 2.7309245307499995e-22 | 8.2e-32 | 12 | 2 | kg m s^-1 |
| natural unit of momentum in MeV/c | 0.51099895 | 1.5e-10 | 11 | 2 | MeV / c |
| natural unit of time | 1.28808866819e-21 | 3.8999999999999997e-31 | 12 | 2 | s |
| natural unit of velocity | 299792458\.0 | None | 9 | None | m s^-1 |
| neutron Compton wavelength | 1.3195909058099999e-15 | 7.5e-25 | 12 | 2 | m |
| neutron-electron mag. mom. ratio | 0.00104066882 | 2.5e-10 | 9 | 2 | None |
| neutron-electron mass ratio | 1838.68366173 | 8.9e-07 | 12 | 2 | None |
| neutron g factor | -3.82608545 | 9e-07 | 9 | 2 | None |
| neutron gyromag. ratio | 183247171\.0 | 43.0 | 9 | 2 | s^-1 T^-1 |
| neutron gyromag. ratio in MHz/T | 29.1646931 | 6.9e-06 | 9 | 2 | MHz T^-1 |
| neutron mag. mom. | -9.662365099999999e-27 | 2.3e-33 | 8 | 2 | J T^-1 |
| neutron mag. mom. to Bohr magneton ratio | -0.00104187563 | 2.5e-10 | 9 | 2 | None |
| neutron mag. mom. to nuclear magneton ratio | -1.91304273 | 4.5e-07 | 9 | 2 | None |
| neutron mass | 1.67492749804e-27 | 9.500000000000001e-37 | 12 | 2 | kg |
| neutron mass energy equivalent | 1.50534976287e-10 | 8.6e-20 | 12 | 2 | J |
| neutron mass energy equivalent in MeV | 939.56542052 | 5.4e-07 | 11 | 2 | MeV |
| neutron mass in u | 1.00866491595 | 4.9e-10 | 12 | 2 | u |
| neutron molar mass | 0.0010086649156 | 5.7e-13 | 12 | 2 | kg mol^-1 |
| neutron-muon mass ratio | 8.89248406 | 2e-07 | 9 | 2 | None |
| neutron-proton mag. mom. ratio | -0.68497934 | 1.6e-07 | 8 | 2 | None |
| neutron-proton mass difference | 2.3055743500000002e-30 | 8.2e-37 | 9 | 2 | kg |
| neutron-proton mass difference energy equivalent | 2.07214689e-13 | 7.4e-20 | 9 | 2 | J |
| neutron-proton mass difference energy equivalent in MeV | 1.29333236 | 4.6e-07 | 9 | 2 | MeV |
| neutron-proton mass difference in u | 0.00138844933 | 4.9e-10 | 9 | 2 | u |
| neutron-proton mass ratio | 1.00137841931 | 4.9e-10 | 12 | 2 | None |
| neutron relative atomic mass | 1.00866491595 | 4.9e-10 | 12 | 2 | None |
| neutron-tau mass ratio | 0.528779 | 3.6e-05 | 6 | 2 | None |
| neutron to shielded proton mag. mom. ratio | -0.68499694 | 1.6e-07 | 8 | 2 | None |
| Newtonian constant of gravitation | 6.6743e-11 | 1.5e-15 | 6 | 2 | m^3 kg^-1 s^-2 |
| Newtonian constant of gravitation over h-bar c | 6.708829999999999e-39 | 1.4999999999999998e-43 | 6 | 2 | ( GeV / c^2 )^-2 |
| nuclear magneton | 5.0507837460999996e-27 | 1.4999999999999999e-36 | 11 | 2 | J T^-1 |
| nuclear magneton in eV/T | 3.15245125844e-08 | 9.6e-18 | 12 | 2 | eV T^-1 |
| nuclear magneton in inverse meter per tesla | 0.0254262341353 | 7.8e-12 | 12 | 2 | m^-1 T^-1 |
| nuclear magneton in K/T | 0.00036582677756 | 1.1e-13 | 11 | 2 | K T^-1 |
| nuclear magneton in MHz/T | 7.6225932291 | 2.3e-09 | 11 | 2 | MHz T^-1 |
| Planck constant | 6.62607015e-34 | None | 9 | None | J Hz^-1 |
| Planck constant in eV/Hz | 4.135667696e-15 | None | 10 | None | eV Hz^-1 |
| Planck length | 1.616255e-35 | 1.8e-40 | 7 | 2 | m |
| Planck mass | 2.176434e-08 | 2.4e-13 | 7 | 2 | kg |
| Planck mass energy equivalent in GeV | 1.22089e+19 | 140000000000000.0 | 7 | 2 | GeV |
| Planck temperature | 1.416784e+32 | 1.6e+27 | 7 | 2 | K |
| Planck time | 5.391246999999999e-44 | 5.999999999999999e-49 | 7 | 2 | s |
| proton charge to mass quotient | 95788331.56 | 0.029 | 11 | 2 | C kg^-1 |
| proton Compton wavelength | 1.32140985539e-15 | 3.9999999999999997e-25 | 12 | 2 | m |
| proton-electron mass ratio | 1836.15267343 | 1.1e-07 | 12 | 2 | None |
| proton g factor | 5.5856946893 | 1.6e-09 | 11 | 2 | None |
| proton gyromag. ratio | 267522187\.44 | 0.11 | 11 | 2 | s^-1 T^-1 |
| proton gyromag. ratio in MHz/T | 42.577478518 | 1.8e-08 | 11 | 2 | MHz T^-1 |
| proton mag. mom. | 1.41060679736e-26 | 5.9999999999999996e-36 | 12 | 2 | J T^-1 |
| proton mag. mom. to Bohr magneton ratio | 0.0015210322023 | 4.6e-13 | 12 | 2 | None |
| proton mag. mom. to nuclear magneton ratio | 2.79284734463 | 8.2e-10 | 12 | 2 | None |
| proton mag. shielding correction | 2.5689e-05 | 1.1e-08 | 5 | 2 | None |
| proton mass | 1.67262192369e-27 | 5.1e-37 | 12 | 2 | kg |
| proton mass energy equivalent | 1.50327761598e-10 | 4.6e-20 | 12 | 2 | J |
| proton mass energy equivalent in MeV | 938.27208816 | 2.9e-07 | 11 | 2 | MeV |
| proton mass in u | 1.007276466621 | 5.3e-11 | 13 | 2 | u |
| proton molar mass | 0.00100727646627 | 3.1e-13 | 12 | 2 | kg mol^-1 |
| proton-muon mass ratio | 8.88024337 | 2e-07 | 9 | 2 | None |
| proton-neutron mag. mom. ratio | -1.45989805 | 3.4e-07 | 9 | 2 | None |
| proton-neutron mass ratio | 0.99862347812 | 4.9e-10 | 11 | 2 | None |
| proton relative atomic mass | 1.007276466621 | 5.3e-11 | 13 | 2 | None |
| proton rms charge radius | 8.414e-16 | 1.9e-18 | 4 | 2 | m |
| proton-tau mass ratio | 0.528051 | 3.6e-05 | 6 | 2 | None |
| quantum of circulation | 0.00036369475516 | 1.1e-13 | 11 | 2 | m^2 s^-1 |
| quantum of circulation times 2 | 0.00072738951032 | 2.2e-13 | 11 | 2 | m^2 s^-1 |
| reduced Compton wavelength | 3.8615926796000003e-13 | 1.2e-22 | 11 | 2 | m |
| reduced muon Compton wavelength | 1.867594306e-15 | 4.2e-23 | 10 | 2 | m |
| reduced neutron Compton wavelength | 2.1001941552e-16 | 1.2e-25 | 11 | 2 | m |
| reduced Planck constant | 1.054571817e-34 | None | 10 | None | J s |
| reduced Planck constant in eV s | 6.582119568999999e-16 | None | 10 | None | eV s |
| reduced Planck constant times c in MeV fm | 197.3269804 | None | 10 | None | MeV fm |
| reduced proton Compton wavelength | 2.10308910336e-16 | 6.4e-26 | 12 | 2 | m |
| reduced tau Compton wavelength | 1.110538e-16 | 7.5e-21 | 7 | 2 | m |
| Rydberg constant | 10973731.56816 | 2.1e-05 | 14 | 2 | m^-1 |
| Rydberg constant times c in Hz | 3289841960250800.0 | 6400.0 | 14 | 2 | Hz |
| Rydberg constant times hc in eV | 13.605693122994 | 2.6e-11 | 14 | 2 | eV |
| Rydberg constant times hc in J | 2.1798723611035e-18 | 4.2e-30 | 14 | 2 | J |
| Sackur-Tetrode constant (1 K, 100 kPa) | -1.15170753706 | 4.5e-10 | 12 | 2 | None |
| Sackur-Tetrode constant (1 K, 101.325 kPa) | -1.16487052358 | 4.5e-10 | 12 | 2 | None |
| second radiation constant | 0.01438776877 | None | 10 | None | m K |
| shielded helion gyromag. ratio | 203789456\.9 | 2.4 | 10 | 2 | s^-1 T^-1 |
| shielded helion gyromag. ratio in MHz/T | 32.43409942 | 3.8e-07 | 10 | 2 | MHz T^-1 |
| shielded helion mag. mom. | -1.07455309e-26 | 1.3e-34 | 10 | 2 | J T^-1 |
| shielded helion mag. mom. to Bohr magneton ratio | -0.001158671471 | 1.4e-11 | 10 | 2 | None |
| shielded helion mag. mom. to nuclear magneton ratio | -2.127497719 | 2.5e-08 | 10 | 2 | None |
| shielded helion to proton mag. mom. ratio | -0.7617665618 | 8.9e-09 | 10 | 2 | None |
| shielded helion to shielded proton mag. mom. ratio | -0.7617861313 | 3.3e-09 | 10 | 2 | None |
| shielded proton gyromag. ratio | 267515315\.1 | 2.9 | 10 | 2 | s^-1 T^-1 |
| shielded proton gyromag. ratio in MHz/T | 42.57638474 | 4.6e-07 | 10 | 2 | MHz T^-1 |
| shielded proton mag. mom. | 1.41057056e-26 | 1.5e-34 | 10 | 2 | J T^-1 |
| shielded proton mag. mom. to Bohr magneton ratio | 0.001520993128 | 1.7e-11 | 10 | 2 | None |
| shielded proton mag. mom. to nuclear magneton ratio | 2.792775599 | 3e-08 | 10 | 2 | None |
| shielding difference of d and p in HD | 2.02e-08 | 2e-11 | 5 | 2 | None |
| shielding difference of t and p in HT | 2.414e-08 | 2e-11 | 5 | 2 | None |
| speed of light in vacuum | 299792458\.0 | None | 9 | None | m s^-1 |
| standard acceleration of gravity | 9.80665 | None | 6 | None | m s^-2 |
| standard atmosphere | 101325.0 | None | 6 | None | Pa |
| standard-state pressure | 100000.0 | None | 6 | None | Pa |
| Stefan-Boltzmann constant | 5.670374419e-08 | None | 10 | None | W m^-2 K^-4 |
| tau Compton wavelength | 6.97771e-16 | 4.7e-20 | 6 | 2 | m |
| tau-electron mass ratio | 3477.23 | 0.23 | 6 | 2 | None |
| tau energy equivalent | 1776.86 | 0.12 | 6 | 2 | MeV |
| tau mass | 3.16754e-27 | 2.1e-31 | 6 | 2 | kg |
| tau mass energy equivalent | 2.84684e-10 | 1.9e-14 | 6 | 2 | J |
| tau mass in u | 1.90754 | 0.00013 | 6 | 2 | u |
| tau molar mass | 0.00190754 | 1.3e-07 | 6 | 2 | kg mol^-1 |
| tau-muon mass ratio | 16.817 | 0.0011 | 6 | 2 | None |
| tau-neutron mass ratio | 1.89115 | 0.00013 | 6 | 2 | None |
| tau-proton mass ratio | 1.89376 | 0.00013 | 6 | 2 | None |
| Thomson cross section | 6.652458732099999e-29 | 6e-38 | 11 | 2 | m^2 |
| triton-electron mass ratio | 5496.92153573 | 2.7e-07 | 12 | 2 | None |
| triton g factor | 5.957924931 | 1.2e-08 | 10 | 2 | None |
| triton mag. mom. | 1.5046095202e-26 | 3e-35 | 11 | 2 | J T^-1 |
| triton mag. mom. to Bohr magneton ratio | 0.0016223936651 | 3.2e-12 | 11 | 2 | None |
| triton mag. mom. to nuclear magneton ratio | 2.9789624656 | 5.9e-09 | 11 | 2 | None |
| triton mass | 5.0073567445999994e-27 | 1.4999999999999999e-36 | 11 | 2 | kg |
| triton mass energy equivalent | 4.500387806e-10 | 1.4e-19 | 11 | 2 | J |
| triton mass energy equivalent in MeV | 2808.92113298 | 8.5e-07 | 12 | 2 | MeV |
| triton mass in u | 3.01550071621 | 1.2e-10 | 12 | 2 | u |
| triton molar mass | 0.00301550071517 | 9.2e-13 | 12 | 2 | kg mol^-1 |
| triton-proton mass ratio | 2.99371703414 | 1.5e-10 | 12 | 2 | None |
| triton relative atomic mass | 3.01550071621 | 1.2e-10 | 12 | 2 | None |
| triton to proton mag. mom. ratio | 1.0666399191 | 2.1e-09 | 11 | 2 | None |
| unified atomic mass unit | 1.6605390666e-27 | 5e-37 | 12 | 2 | kg |
| vacuum electric permittivity | 8.8541878128e-12 | 1.3e-21 | 11 | 2 | F m^-1 |
| vacuum mag. permeability | 1.25663706212e-06 | 1.9e-16 | 12 | 2 | N A^-2 |
| von Klitzing constant | 25812.80745 | None | 10 | None | ohm |
| weak mixing angle | 0.2229 | 0.0003 | 5 | 2 | None |
| Wien frequency displacement law constant | 58789257570.0 | None | 10 | None | Hz K^-1 |
| Wien wavelength displacement law constant | 0.002897771955 | None | 10 | None | m K |
| W to Z mass ratio | 0.88153 | 0.00017 | 5 | 2 | None |
