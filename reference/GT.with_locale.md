## GT.with_locale()


Set a column to be the default locale.


Usage

``` python
GT.with_locale(locale=None)
```


Setting a default locale affects formatters like [fmt_number()](GT.fmt_number.md#great_tables.GT.fmt_number), and [fmt_date()](GT.fmt_date.md#great_tables.GT.fmt_date), by having them default to locale-specific features (e.g. representing one thousand as 1.000,00)


## Parameters


`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's create a table and set its `locale=` to `"ja"` for Japan. Then, we call [fmt_currency()](GT.fmt_currency.md#great_tables.GT.fmt_currency) to format the `"currency"` column. Since we didn't specify a `locale=` for [fmt_currency()](GT.fmt_currency.md#great_tables.GT.fmt_currency), it will adopt the globally set `"ja"` locale.


``` python
from great_tables import GT, exibble


(
    GT(exibble)
    .with_locale("ja")
    .fmt_currency(
        columns="currency",
        decimals=3,
        use_seps=False
    )
)
```


| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | ¥49.950 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | ¥17.950 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | ¥1.390 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | ¥65100.000 | row_4 | grp_a |
| 5550.0 |  | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | ¥1325.810 | row_5 | grp_b |
|  | fig | six | 2015-06-15 |  | 2018-06-06 16:11 | ¥13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven |  | 19:10 | 2018-07-07 05:22 |  | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 |  | ¥0.440 | row_8 | grp_b |


**Great Tables** internally supports many locale options. You can find the available locales in the following table:


``` python
from great_tables.data import __x_locales

columns = ["locale", "lang_name", "lang_desc", "territory_name", "territory_desc"]
GT(__x_locales.loc[:, columns]).cols_align("right")
```


| locale | lang_name | lang_desc | territory_name | territory_desc |
|----|----|----|----|----|
| af | af | Afrikaans | ZA | South Africa |
| af-NA | af | Afrikaans |  | Namibia |
| agq | agq | Aghem | CM | Cameroon |
| ak | ak | Akan | GH | Ghana |
| am | am | Amharic | ET | Ethiopia |
| ar | ar | Arabic | 001 | world |
| ar-AE | ar | Arabic | AE | United Arab Emirates |
| ar-BH | ar | Arabic | BH | Bahrain |
| ar-DJ | ar | Arabic | DJ | Djibouti |
| ar-DZ | ar | Arabic | DZ | Algeria |
| ar-EG | ar | Arabic | EG | Egypt |
| ar-EH | ar | Arabic | EH | Western Sahara |
| ar-ER | ar | Arabic | ER | Eritrea |
| ar-IL | ar | Arabic | IL | Israel |
| ar-IQ | ar | Arabic | IQ | Iraq |
| ar-JO | ar | Arabic | JO | Jordan |
| ar-KM | ar | Arabic | KM | Comoros |
| ar-KW | ar | Arabic | KW | Kuwait |
| ar-LB | ar | Arabic | LB | Lebanon |
| ar-LY | ar | Arabic | LY | Libya |
| ar-MA | ar | Arabic | MA | Morocco |
| ar-MR | ar | Arabic | MR | Mauritania |
| ar-OM | ar | Arabic | OM | Oman |
| ar-PS | ar | Arabic | PS | Palestinian Territories |
| ar-QA | ar | Arabic | QA | Qatar |
| ar-SA | ar | Arabic | SA | Saudi Arabia |
| ar-SD | ar | Arabic | SD | Sudan |
| ar-SO | ar | Arabic | SO | Somalia |
| ar-SS | ar | Arabic | SS | South Sudan |
| ar-SY | ar | Arabic | SY | Syria |
| ar-TD | ar | Arabic | TD | Chad |
| ar-TN | ar | Arabic | TN | Tunisia |
| ar-YE | ar | Arabic | YE | Yemen |
| as | as | Assamese | IN | India |
| asa | asa | Asu | TZ | Tanzania |
| ast | ast | Asturian | ES | Spain |
| az | az | Azerbaijani | AZ | Azerbaijan |
| az-Cyrl | az | Azerbaijani | AZ | Azerbaijan |
| az-Latn | az | Azerbaijani | AZ | Azerbaijan |
| bas | bas | Basaa | CM | Cameroon |
| be | be | Belarusian | BY | Belarus |
| be-tarask | be | Belarusian | BY | Belarus |
| bem | bem | Bemba | ZM | Zambia |
| bez | bez | Bena | TZ | Tanzania |
| bg | bg | Bulgarian | BG | Bulgaria |
| bm | bm | Bambara | ML | Mali |
| bn | bn | Bangla | BD | Bangladesh |
| bn-IN | bn | Bangla | IN | India |
| bo | bo | Tibetan | CN | China |
| bo-IN | bo | Tibetan | IN | India |
| br | br | Breton | FR | France |
| brx | brx | Bodo | IN | India |
| bs | bs | Bosnian | BA | Bosnia & Herzegovina |
| bs-Cyrl | bs | Bosnian | BA | Bosnia & Herzegovina |
| bs-Latn | bs | Bosnian | BA | Bosnia & Herzegovina |
| ca | ca | Catalan | ES | Spain |
| ca-AD | ca | Catalan | AD | Andorra |
| ca-ES-valencia | ca | Catalan | ES | Spain |
| ca-FR | ca | Catalan | FR | France |
| ca-IT | ca | Catalan | IT | Italy |
| ccp | ccp | Chakma | BD | Bangladesh |
| ccp-IN | ccp | Chakma | IN | India |
| ce | ce | Chechen | RU | Russia |
| ceb | ceb | Cebuano | PH | Philippines |
| cgg | cgg | Chiga | UG | Uganda |
| chr | chr | Cherokee | US | United States |
| ckb | ckb | Central Kurdish | IQ | Iraq |
| ckb-IR | ckb | Central Kurdish | IR | Iran |
| cs | cs | Czech | CZ | Czechia |
| cy | cy | Welsh | GB | United Kingdom |
| da | da | Danish | DK | Denmark |
| da-GL | da | Danish | GL | Greenland |
| dav | dav | Taita | KE | Kenya |
| de | de | German | DE | Germany |
| de-AT | de | German | AT | Austria |
| de-BE | de | German | BE | Belgium |
| de-CH | de | German | CH | Switzerland |
| de-IT | de | German | IT | Italy |
| de-LI | de | German | LI | Liechtenstein |
| de-LU | de | German | LU | Luxembourg |
| dje | dje | Zarma | NE | Niger |
| doi | doi | Dogri | IN | India |
| dsb | dsb | Lower Sorbian | DE | Germany |
| dua | dua | Duala | CM | Cameroon |
| dyo | dyo | Jola-Fonyi | SN | Senegal |
| dz | dz | Dzongkha | BT | Bhutan |
| ebu | ebu | Embu | KE | Kenya |
| ee | ee | Ewe | GH | Ghana |
| ee-TG | ee | Ewe | TG | Togo |
| el | el | Greek | GR | Greece |
| el-CY | el | Greek | CY | Cyprus |
| en | en | English | US | United States |
| en-001 | en | English | 001 | world |
| en-150 | en | English | 150 | Europe |
| en-AE | en | English | AE | United Arab Emirates |
| en-AG | en | English | AG | Antigua & Barbuda |
| en-AI | en | English | AI | Anguilla |
| en-AS | en | English | AS | American Samoa |
| en-AT | en | English | AT | Austria |
| en-AU | en | English | AU | Australia |
| en-BB | en | English | BB | Barbados |
| en-BE | en | English | BE | Belgium |
| en-BI | en | English | BI | Burundi |
| en-BM | en | English | BM | Bermuda |
| en-BS | en | English | BS | Bahamas |
| en-BW | en | English | BW | Botswana |
| en-BZ | en | English | BZ | Belize |
| en-CA | en | English | CA | Canada |
| en-CC | en | English | CC | Cocos (Keeling) Islands |
| en-CH | en | English | CH | Switzerland |
| en-CK | en | English | CK | Cook Islands |
| en-CM | en | English | CM | Cameroon |
| en-CX | en | English | CX | Christmas Island |
| en-CY | en | English | CY | Cyprus |
| en-DE | en | English | DE | Germany |
| en-DG | en | English | DG | Diego Garcia |
| en-DK | en | English | DK | Denmark |
| en-DM | en | English | DM | Dominica |
| en-ER | en | English | ER | Eritrea |
| en-FI | en | English | FI | Finland |
| en-FJ | en | English | FJ | Fiji |
| en-FK | en | English | FK | Falkland Islands |
| en-FM | en | English | FM | Micronesia |
| en-GB | en | English | GB | United Kingdom |
| en-GD | en | English | GD | Grenada |
| en-GG | en | English | GG | Guernsey |
| en-GH | en | English | GH | Ghana |
| en-GI | en | English | GI | Gibraltar |
| en-GM | en | English | GM | Gambia |
| en-GU | en | English | GU | Guam |
| en-GY | en | English | GY | Guyana |
| en-HK | en | English | HK | Hong Kong SAR China |
| en-IE | en | English | IE | Ireland |
| en-IL | en | English | IL | Israel |
| en-IM | en | English | IM | Isle of Man |
| en-IN | en | English | IN | India |
| en-IO | en | English | IO | British Indian Ocean Territory |
| en-JE | en | English | JE | Jersey |
| en-JM | en | English | JM | Jamaica |
| en-KE | en | English | KE | Kenya |
| en-KI | en | English | KI | Kiribati |
| en-KN | en | English | KN | St. Kitts & Nevis |
| en-KY | en | English | KY | Cayman Islands |
| en-LC | en | English | LC | St. Lucia |
| en-LR | en | English | LR | Liberia |
| en-LS | en | English | LS | Lesotho |
| en-MG | en | English | MG | Madagascar |
| en-MH | en | English | MH | Marshall Islands |
| en-MO | en | English | MO | Macao SAR China |
| en-MP | en | English | MP | Northern Mariana Islands |
| en-MS | en | English | MS | Montserrat |
| en-MT | en | English | MT | Malta |
| en-MU | en | English | MU | Mauritius |
| en-MV | en | English | MV | Maldives |
| en-MW | en | English | MW | Malawi |
| en-MY | en | English | MY | Malaysia |
| en-NA | en | English |  | Namibia |
| en-NF | en | English | NF | Norfolk Island |
| en-NG | en | English | NG | Nigeria |
| en-NL | en | English | NL | Netherlands |
| en-NR | en | English | NR | Nauru |
| en-NU | en | English | NU | Niue |
| en-NZ | en | English | NZ | New Zealand |
| en-PG | en | English | PG | Papua New Guinea |
| en-PH | en | English | PH | Philippines |
| en-PK | en | English | PK | Pakistan |
| en-PN | en | English | PN | Pitcairn Islands |
| en-PR | en | English | PR | Puerto Rico |
| en-PW | en | English | PW | Palau |
| en-RW | en | English | RW | Rwanda |
| en-SB | en | English | SB | Solomon Islands |
| en-SC | en | English | SC | Seychelles |
| en-SD | en | English | SD | Sudan |
| en-SE | en | English | SE | Sweden |
| en-SG | en | English | SG | Singapore |
| en-SH | en | English | SH | St. Helena |
| en-SI | en | English | SI | Slovenia |
| en-SL | en | English | SL | Sierra Leone |
| en-SS | en | English | SS | South Sudan |
| en-SX | en | English | SX | Sint Maarten |
| en-SZ | en | English | SZ | Eswatini |
| en-TC | en | English | TC | Turks & Caicos Islands |
| en-TK | en | English | TK | Tokelau |
| en-TO | en | English | TO | Tonga |
| en-TT | en | English | TT | Trinidad & Tobago |
| en-TV | en | English | TV | Tuvalu |
| en-TZ | en | English | TZ | Tanzania |
| en-UG | en | English | UG | Uganda |
| en-UM | en | English | UM | U.S. Outlying Islands |
| en-VC | en | English | VC | St. Vincent & Grenadines |
| en-VG | en | English | VG | British Virgin Islands |
| en-VI | en | English | VI | U.S. Virgin Islands |
| en-VU | en | English | VU | Vanuatu |
| en-WS | en | English | WS | Samoa |
| en-ZA | en | English | ZA | South Africa |
| en-ZM | en | English | ZM | Zambia |
| en-ZW | en | English | ZW | Zimbabwe |
| eo | eo | Esperanto | 001 | world |
| es | es | Spanish | ES | Spain |
| es-419 | es | Spanish | 419 | Latin America |
| es-AR | es | Spanish | AR | Argentina |
| es-BO | es | Spanish | BO | Bolivia |
| es-BR | es | Spanish | BR | Brazil |
| es-BZ | es | Spanish | BZ | Belize |
| es-CL | es | Spanish | CL | Chile |
| es-CO | es | Spanish | CO | Colombia |
| es-CR | es | Spanish | CR | Costa Rica |
| es-CU | es | Spanish | CU | Cuba |
| es-DO | es | Spanish | DO | Dominican Republic |
| es-EA | es | Spanish | EA | Ceuta & Melilla |
| es-EC | es | Spanish | EC | Ecuador |
| es-GQ | es | Spanish | GQ | Equatorial Guinea |
| es-GT | es | Spanish | GT | Guatemala |
| es-HN | es | Spanish | HN | Honduras |
| es-IC | es | Spanish | IC | Canary Islands |
| es-MX | es | Spanish | MX | Mexico |
| es-NI | es | Spanish | NI | Nicaragua |
| es-PA | es | Spanish | PA | Panama |
| es-PE | es | Spanish | PE | Peru |
| es-PH | es | Spanish | PH | Philippines |
| es-PR | es | Spanish | PR | Puerto Rico |
| es-PY | es | Spanish | PY | Paraguay |
| es-SV | es | Spanish | SV | El Salvador |
| es-US | es | Spanish | US | United States |
| es-UY | es | Spanish | UY | Uruguay |
| es-VE | es | Spanish | VE | Venezuela |
| et | et | Estonian | EE | Estonia |
| eu | eu | Basque | ES | Spain |
| ewo | ewo | Ewondo | CM | Cameroon |
| fa | fa | Persian | IR | Iran |
| fa-AF | fa | Persian | AF | Afghanistan |
| ff | ff | Fulah | GN | Guinea |
| ff-Adlm | ff | Fulah | GN | Guinea |
| ff-Adlm-BF | ff | Fulah | BF | Burkina Faso |
| ff-Adlm-CM | ff | Fulah | CM | Cameroon |
| ff-Adlm-GH | ff | Fulah | GH | Ghana |
| ff-Adlm-GM | ff | Fulah | GM | Gambia |
| ff-Adlm-GW | ff | Fulah | GW | Guinea-Bissau |
| ff-Adlm-LR | ff | Fulah | LR | Liberia |
| ff-Adlm-MR | ff | Fulah | MR | Mauritania |
| ff-Adlm-NE | ff | Fulah | NE | Niger |
| ff-Adlm-NG | ff | Fulah | NG | Nigeria |
| ff-Adlm-SL | ff | Fulah | SL | Sierra Leone |
| ff-Adlm-SN | ff | Fulah | SN | Senegal |
| ff-Latn | ff | Fulah | SN | Senegal |
| ff-Latn-BF | ff | Fulah | BF | Burkina Faso |
| ff-Latn-CM | ff | Fulah | CM | Cameroon |
| ff-Latn-GH | ff | Fulah | GH | Ghana |
| ff-Latn-GM | ff | Fulah | GM | Gambia |
| ff-Latn-GN | ff | Fulah | GN | Guinea |
| ff-Latn-GW | ff | Fulah | GW | Guinea-Bissau |
| ff-Latn-LR | ff | Fulah | LR | Liberia |
| ff-Latn-MR | ff | Fulah | MR | Mauritania |
| ff-Latn-NE | ff | Fulah | NE | Niger |
| ff-Latn-NG | ff | Fulah | NG | Nigeria |
| ff-Latn-SL | ff | Fulah | SL | Sierra Leone |
| fi | fi | Finnish | FI | Finland |
| fil | fil | Filipino | PH | Philippines |
| fo | fo | Faroese | FO | Faroe Islands |
| fo-DK | fo | Faroese | DK | Denmark |
| fr | fr | French | FR | France |
| fr-BE | fr | French | BE | Belgium |
| fr-BF | fr | French | BF | Burkina Faso |
| fr-BI | fr | French | BI | Burundi |
| fr-BJ | fr | French | BJ | Benin |
| fr-BL | fr | French | BL | St. Barthélemy |
| fr-CA | fr | French | CA | Canada |
| fr-CD | fr | French | CD | Congo - Kinshasa |
| fr-CF | fr | French | CF | Central African Republic |
| fr-CG | fr | French | CG | Congo - Brazzaville |
| fr-CH | fr | French | CH | Switzerland |
| fr-CI | fr | French | CI | Côte d'Ivoire |
| fr-CM | fr | French | CM | Cameroon |
| fr-DJ | fr | French | DJ | Djibouti |
| fr-DZ | fr | French | DZ | Algeria |
| fr-GA | fr | French | GA | Gabon |
| fr-GF | fr | French | GF | French Guiana |
| fr-GN | fr | French | GN | Guinea |
| fr-GP | fr | French | GP | Guadeloupe |
| fr-GQ | fr | French | GQ | Equatorial Guinea |
| fr-HT | fr | French | HT | Haiti |
| fr-KM | fr | French | KM | Comoros |
| fr-LU | fr | French | LU | Luxembourg |
| fr-MA | fr | French | MA | Morocco |
| fr-MC | fr | French | MC | Monaco |
| fr-MF | fr | French | MF | St. Martin |
| fr-MG | fr | French | MG | Madagascar |
| fr-ML | fr | French | ML | Mali |
| fr-MQ | fr | French | MQ | Martinique |
| fr-MR | fr | French | MR | Mauritania |
| fr-MU | fr | French | MU | Mauritius |
| fr-NC | fr | French | NC | New Caledonia |
| fr-NE | fr | French | NE | Niger |
| fr-PF | fr | French | PF | French Polynesia |
| fr-PM | fr | French | PM | St. Pierre & Miquelon |
| fr-RE | fr | French | RE | Réunion |
| fr-RW | fr | French | RW | Rwanda |
| fr-SC | fr | French | SC | Seychelles |
| fr-SN | fr | French | SN | Senegal |
| fr-SY | fr | French | SY | Syria |
| fr-TD | fr | French | TD | Chad |
| fr-TG | fr | French | TG | Togo |
| fr-TN | fr | French | TN | Tunisia |
| fr-VU | fr | French | VU | Vanuatu |
| fr-WF | fr | French | WF | Wallis & Futuna |
| fr-YT | fr | French | YT | Mayotte |
| fur | fur | Friulian | IT | Italy |
| fy | fy | Western Frisian | NL | Netherlands |
| ga | ga | Irish | IE | Ireland |
| ga-GB | ga | Irish | GB | United Kingdom |
| gd | gd | Scottish Gaelic | GB | United Kingdom |
| gl | gl | Galician | ES | Spain |
| gsw | gsw | Swiss German | CH | Switzerland |
| gsw-FR | gsw | Swiss German | FR | France |
| gsw-LI | gsw | Swiss German | LI | Liechtenstein |
| gu | gu | Gujarati | IN | India |
| guz | guz | Gusii | KE | Kenya |
| gv | gv | Manx | IM | Isle of Man |
| ha | ha | Hausa | NG | Nigeria |
| ha-GH | ha | Hausa | GH | Ghana |
| ha-NE | ha | Hausa | NE | Niger |
| haw | haw | Hawaiian | US | United States |
| he | he | Hebrew | IL | Israel |
| hi | hi | Hindi | IN | India |
| hi-Latn | hi | Hindi | IN | India |
| hr | hr | Croatian | HR | Croatia |
| hr-BA | hr | Croatian | BA | Bosnia & Herzegovina |
| hsb | hsb | Upper Sorbian | DE | Germany |
| hu | hu | Hungarian | HU | Hungary |
| hy | hy | Armenian | AM | Armenia |
| ia | ia | Interlingua | 001 | world |
| id | id | Indonesian | ID | Indonesia |
| ig | ig | Igbo | NG | Nigeria |
| ii | ii | Sichuan Yi | CN | China |
| is | is | Icelandic | IS | Iceland |
| it | it | Italian | IT | Italy |
| it-CH | it | Italian | CH | Switzerland |
| it-SM | it | Italian | SM | San Marino |
| it-VA | it | Italian | VA | Vatican City |
| ja | ja | Japanese | JP | Japan |
| jgo | jgo | Ngomba | CM | Cameroon |
| jmc | jmc | Machame | TZ | Tanzania |
| jv | jv | Javanese | ID | Indonesia |
| ka | ka | Georgian | GE | Georgia |
| kab | kab | Kabyle | DZ | Algeria |
| kam | kam | Kamba | KE | Kenya |
| kde | kde | Makonde | TZ | Tanzania |
| kea | kea | Kabuverdianu | CV | Cape Verde |
| kgp | kgp | Kaingang | BR | Brazil |
| khq | khq | Koyra Chiini | ML | Mali |
| ki | ki | Kikuyu | KE | Kenya |
| kk | kk | Kazakh | KZ | Kazakhstan |
| kkj | kkj | Kako | CM | Cameroon |
| kl | kl | Kalaallisut | GL | Greenland |
| kln | kln | Kalenjin | KE | Kenya |
| km | km | Khmer | KH | Cambodia |
| kn | kn | Kannada | IN | India |
| ko | ko | Korean | KR | South Korea |
| ko-KP | ko | Korean | KP | North Korea |
| kok | kok | Konkani | IN | India |
| ks | ks | Kashmiri | IN | India |
| ks-Arab | ks | Kashmiri | IN | India |
| ks-Deva | ks | Kashmiri | IN | India |
| ksb | ksb | Shambala | TZ | Tanzania |
| ksf | ksf | Bafia | CM | Cameroon |
| ksh | ksh | Colognian | DE | Germany |
| ku | ku | Kurdish | TR | Turkey |
| kw | kw | Cornish | GB | United Kingdom |
| ky | ky | Kyrgyz | KG | Kyrgyzstan |
| lag | lag | Langi | TZ | Tanzania |
| lb | lb | Luxembourgish | LU | Luxembourg |
| lg | lg | Ganda | UG | Uganda |
| lkt | lkt | Lakota | US | United States |
| ln | ln | Lingala | CD | Congo - Kinshasa |
| ln-AO | ln | Lingala | AO | Angola |
| ln-CF | ln | Lingala | CF | Central African Republic |
| ln-CG | ln | Lingala | CG | Congo - Brazzaville |
| lo | lo | Lao | LA | Laos |
| lrc | lrc | Northern Luri | IR | Iran |
| lrc-IQ | lrc | Northern Luri | IQ | Iraq |
| lt | lt | Lithuanian | LT | Lithuania |
| lu | lu | Luba-Katanga | CD | Congo - Kinshasa |
| luo | luo | Luo | KE | Kenya |
| luy | luy | Luyia | KE | Kenya |
| lv | lv | Latvian | LV | Latvia |
| mai | mai | Maithili | IN | India |
| mas | mas | Masai | KE | Kenya |
| mas-TZ | mas | Masai | TZ | Tanzania |
| mer | mer | Meru | KE | Kenya |
| mfe | mfe | Morisyen | MU | Mauritius |
| mg | mg | Malagasy | MG | Madagascar |
| mgh | mgh | Makhuwa-Meetto | MZ | Mozambique |
| mgo | mgo | Metaʼ | CM | Cameroon |
| mi | mi | Māori | NZ | New Zealand |
| mk | mk | Macedonian | MK | North Macedonia |
| ml | ml | Malayalam | IN | India |
| mn | mn | Mongolian | MN | Mongolia |
| mni | mni | Manipuri | IN | India |
| mni-Beng | mni | Manipuri | IN | India |
| mr | mr | Marathi | IN | India |
| ms | ms | Malay | MY | Malaysia |
| ms-BN | ms | Malay | BN | Brunei |
| ms-ID | ms | Malay | ID | Indonesia |
| ms-SG | ms | Malay | SG | Singapore |
| mt | mt | Maltese | MT | Malta |
| mua | mua | Mundang | CM | Cameroon |
| my | my | Burmese | MM | Myanmar (Burma) |
| mzn | mzn | Mazanderani | IR | Iran |
| naq | naq | Nama |  | Namibia |
| nb | nb | Norwegian Bokmål | NO | Norway |
| nb-SJ | nb | Norwegian Bokmål | SJ | Svalbard & Jan Mayen |
| nd | nd | North Ndebele | ZW | Zimbabwe |
| nds | nds | Low German | DE | Germany |
| nds-NL | nds | Low German | NL | Netherlands |
| ne | ne | Nepali | NP | Nepal |
| ne-IN | ne | Nepali | IN | India |
| nl | nl | Dutch | NL | Netherlands |
| nl-AW | nl | Dutch | AW | Aruba |
| nl-BE | nl | Dutch | BE | Belgium |
| nl-BQ | nl | Dutch | BQ | Caribbean Netherlands |
| nl-CW | nl | Dutch | CW | Curaçao |
| nl-SR | nl | Dutch | SR | Suriname |
| nl-SX | nl | Dutch | SX | Sint Maarten |
| nmg | nmg | Kwasio | CM | Cameroon |
| nn | nn | Norwegian Nynorsk | NO | Norway |
| nnh | nnh | Ngiemboon | CM | Cameroon |
| no | no | Norwegian | NO | Norway |
| nus | nus | Nuer | SS | South Sudan |
| nyn | nyn | Nyankole | UG | Uganda |
| om | om | Oromo | ET | Ethiopia |
| om-KE | om | Oromo | KE | Kenya |
| or | or | Odia | IN | India |
| os | os | Ossetic | GE | Georgia |
| os-RU | os | Ossetic | RU | Russia |
| pa | pa | Punjabi | PK | Pakistan |
| pa-Arab | pa | Punjabi | PK | Pakistan |
| pa-Guru | pa | Punjabi | IN | India |
| pcm | pcm | Nigerian Pidgin | NG | Nigeria |
| pl | pl | Polish | PL | Poland |
| ps | ps | Pashto | AF | Afghanistan |
| ps-PK | ps | Pashto | PK | Pakistan |
| pt | pt | Portuguese | BR | Brazil |
| pt-AO | pt | Portuguese | AO | Angola |
| pt-CH | pt | Portuguese | CH | Switzerland |
| pt-CV | pt | Portuguese | CV | Cape Verde |
| pt-GQ | pt | Portuguese | GQ | Equatorial Guinea |
| pt-GW | pt | Portuguese | GW | Guinea-Bissau |
| pt-LU | pt | Portuguese | LU | Luxembourg |
| pt-MO | pt | Portuguese | MO | Macao SAR China |
| pt-MZ | pt | Portuguese | MZ | Mozambique |
| pt-PT | pt | Portuguese | PT | Portugal |
| pt-ST | pt | Portuguese | ST | São Tomé & Príncipe |
| pt-TL | pt | Portuguese | TL | Timor-Leste |
| qu | qu | Quechua | PE | Peru |
| qu-BO | qu | Quechua | BO | Bolivia |
| qu-EC | qu | Quechua | EC | Ecuador |
| rm | rm | Romansh | CH | Switzerland |
| rn | rn | Rundi | BI | Burundi |
| ro | ro | Romanian | RO | Romania |
| ro-MD | ro | Romanian | MD | Moldova |
| rof | rof | Rombo | TZ | Tanzania |
| ru | ru | Russian | RU | Russia |
| ru-BY | ru | Russian | BY | Belarus |
| ru-KG | ru | Russian | KG | Kyrgyzstan |
| ru-KZ | ru | Russian | KZ | Kazakhstan |
| ru-MD | ru | Russian | MD | Moldova |
| ru-UA | ru | Russian | UA | Ukraine |
| rw | rw | Kinyarwanda | RW | Rwanda |
| rwk | rwk | Rwa | TZ | Tanzania |
| sa | sa | Sanskrit | IN | India |
| sah | sah | Sakha | RU | Russia |
| saq | saq | Samburu | KE | Kenya |
| sat | sat | Santali | IN | India |
| sat-Olck | sat | Santali | IN | India |
| sbp | sbp | Sangu | TZ | Tanzania |
| sc | sc | Sardinian | IT | Italy |
| sd | sd | Sindhi | PK | Pakistan |
| sd-Arab | sd | Sindhi | PK | Pakistan |
| sd-Deva | sd | Sindhi | IN | India |
| se | se | Northern Sami | NO | Norway |
| se-FI | se | Northern Sami | FI | Finland |
| se-SE | se | Northern Sami | SE | Sweden |
| seh | seh | Sena | MZ | Mozambique |
| ses | ses | Koyraboro Senni | ML | Mali |
| sg | sg | Sango | CF | Central African Republic |
| shi | shi | Tachelhit | MA | Morocco |
| shi-Latn | shi | Tachelhit | MA | Morocco |
| shi-Tfng | shi | Tachelhit | MA | Morocco |
| si | si | Sinhala | LK | Sri Lanka |
| sk | sk | Slovak | SK | Slovakia |
| sl | sl | Slovenian | SI | Slovenia |
| smn | smn | Inari Sami | FI | Finland |
| sn | sn | Shona | ZW | Zimbabwe |
| so | so | Somali | SO | Somalia |
| so-DJ | so | Somali | DJ | Djibouti |
| so-ET | so | Somali | ET | Ethiopia |
| so-KE | so | Somali | KE | Kenya |
| sq | sq | Albanian | AL | Albania |
| sq-MK | sq | Albanian | MK | North Macedonia |
| sq-XK | sq | Albanian | XK | Kosovo |
| sr | sr | Serbian | RS | Serbia |
| sr-Cyrl | sr | Serbian | RS | Serbia |
| sr-Cyrl-BA | sr | Serbian | BA | Bosnia & Herzegovina |
| sr-Cyrl-ME | sr | Serbian | ME | Montenegro |
| sr-Cyrl-XK | sr | Serbian | XK | Kosovo |
| sr-Latn | sr | Serbian | RS | Serbia |
| sr-Latn-BA | sr | Serbian | BA | Bosnia & Herzegovina |
| sr-Latn-ME | sr | Serbian | ME | Montenegro |
| sr-Latn-XK | sr | Serbian | XK | Kosovo |
| su | su | Sundanese | ID | Indonesia |
| su-Latn | su | Sundanese | ID | Indonesia |
| sv | sv | Swedish | SE | Sweden |
| sv-AX | sv | Swedish | AX | Åland Islands |
| sv-FI | sv | Swedish | FI | Finland |
| sw | sw | Swahili | TZ | Tanzania |
| sw-CD | sw | Swahili | CD | Congo - Kinshasa |
| sw-KE | sw | Swahili | KE | Kenya |
| sw-UG | sw | Swahili | UG | Uganda |
| ta | ta | Tamil | IN | India |
| ta-LK | ta | Tamil | LK | Sri Lanka |
| ta-MY | ta | Tamil | MY | Malaysia |
| ta-SG | ta | Tamil | SG | Singapore |
| te | te | Telugu | IN | India |
| teo | teo | Teso | UG | Uganda |
| teo-KE | teo | Teso | KE | Kenya |
| tg | tg | Tajik | TJ | Tajikistan |
| th | th | Thai | TH | Thailand |
| ti | ti | Tigrinya | ET | Ethiopia |
| ti-ER | ti | Tigrinya | ER | Eritrea |
| tk | tk | Turkmen | TM | Turkmenistan |
| to | to | Tongan | TO | Tonga |
| tr | tr | Turkish | TR | Turkey |
| tr-CY | tr | Turkish | CY | Cyprus |
| tt | tt | Tatar | RU | Russia |
| twq | twq | Tasawaq | NE | Niger |
| tzm | tzm | Central Atlas Tamazight | MA | Morocco |
| ug | ug | Uyghur | CN | China |
| uk | uk | Ukrainian | UA | Ukraine |
| und | und | Unknown language |  |  |
| ur | ur | Urdu | PK | Pakistan |
| ur-IN | ur | Urdu | IN | India |
| uz | uz | Uzbek | AF | Afghanistan |
| uz-Arab | uz | Uzbek | AF | Afghanistan |
| uz-Cyrl | uz | Uzbek | UZ | Uzbekistan |
| uz-Latn | uz | Uzbek | UZ | Uzbekistan |
| vai | vai | Vai | LR | Liberia |
| vai-Latn | vai | Vai | LR | Liberia |
| vai-Vaii | vai | Vai | LR | Liberia |
| vi | vi | Vietnamese | VN | Vietnam |
| vun | vun | Vunjo | TZ | Tanzania |
| wae | wae | Walser | CH | Switzerland |
| wo | wo | Wolof | SN | Senegal |
| xh | xh | Xhosa | ZA | South Africa |
| xog | xog | Soga | UG | Uganda |
| yav | yav | Yangben | CM | Cameroon |
| yi | yi | Yiddish | 001 | world |
| yo | yo | Yoruba | NG | Nigeria |
| yo-BJ | yo | Yoruba | BJ | Benin |
| yrl | yrl | Nheengatu | BR | Brazil |
| yrl-CO | yrl | Nheengatu | CO | Colombia |
| yrl-VE | yrl | Nheengatu | VE | Venezuela |
| yue | yue | Cantonese | CN | China |
| yue-Hans | yue | Cantonese | CN | China |
| yue-Hant | yue | Cantonese | HK | Hong Kong SAR China |
| zgh | zgh | Standard Moroccan Tamazight | MA | Morocco |
| zh | zh | Chinese | CN | China |
| zh-Hans | zh | Chinese | CN | China |
| zh-Hans-HK | zh | Chinese | HK | Hong Kong SAR China |
| zh-Hans-MO | zh | Chinese | MO | Macao SAR China |
| zh-Hans-SG | zh | Chinese | SG | Singapore |
| zh-Hant | zh | Chinese | TW | Taiwan |
| zh-Hant-HK | zh | Chinese | HK | Hong Kong SAR China |
| zh-Hant-MO | zh | Chinese | MO | Macao SAR China |
| zu | zu | Zulu | ZA | South Africa |
