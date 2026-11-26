# data.metro

The stations of the Paris Metro.

`data.metro=_read_csv(_metro_fname, dtype=_metro_dtype)`

A dataset with information on all 314 Paris Metro stations as of June 2024. Each record represents a station, describing which Metro lines are serviced by the station, which other connections are available, and annual passenger volumes. Basic location information is provided for each station in terms where they reside on a municipal level, and, through latitude/longitude coordinates.

The system has 16 lines (numbered from 1 to 14, with two additional lines: 3bis and 7bis) and covers over 200 kilometers of track. The Metro runs on standard gauge tracks (1,435 mm) and operates using a variety of rolling stock, including rubber-tired trains and steel-wheeled trains (which are far more common).

The Metro is operated by the RATP, which also operates other transit systems in the region, including buses, trams, and the RER. The RER is an important component of the region's transit infrastructure, and several RER stations have connectivity with the Metro. This integration allows passengers to transfer between those two systems seamlessly. The Metro also has connections to the Transilien rail network, tramway stations, several major train stations (e.g., Gare du Nord, Gare de l'Est, etc.), and many bus lines.

## Details

This is a dataset with 314 rows and 11 columns.

- `name`: The name of the station.
- `caption`: In some cases, a station will have a caption that might describe a nearby place of interest. This is missing if there isn't a caption for the station name.
- `lines`: All Metro lines associated with the station. This is a string-based, comma-separated series of line names.
- `connect_rer`: Station connections with the RER. The RER system has five lines (A, B, C, D, and E) with 257 stations and several interchanges with the Metro.
- `connect_tramway`: Connections with tramway lines. This system has twelve lines in operation (T1, T2, T3a, T3b, T4, T5, T6, T7, T8, T9, T11, and T13) with 235 stations.
- `connect_transilien`: Connections with Transilien lines. This system has eight lines in operation (H, J, K, L, N, P, R, and U).
- `connect_other`: Other connections with transportation infrastructure such as regional, intercity, night, and high-speed trains (typically at railway stations).
- `latitude`, `longitude`: The location of the station, given as latitude and longitude values in decimal degrees.
- `location`: The arrondissement of Paris or municipality in which the station resides. For some stations located at borders, the grouping of locations will be presented as a comma-separated series.
- `passengers`: The total number of Metro station entries during 2021. Some of the newest stations in the Metro system do not have this data, thus they show as missing values.

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

| name | caption | lines | connect_rer | connect_tramway | connect_transilien | connect_other | passengers | latitude | longitude | location |
|----|----|----|----|----|----|----|----|----|----|----|
| Argentine | None | 1 | None | None | None | None | 2079212 | 48.875278 | 2.29 | Paris 16th, Paris 17th |
| Bastille | None | 1, 5, 8 | None | None | None | None | 8069243 | 48.853082 | 2.369077 | Paris 4th, Paris 11th, Paris 12th |
| Bérault | None | 1 | None | None | None | None | 2106827 | 48.845278 | 2.428333 | Saint-Mandé, Vincennes |
| Champs-Élysées--Clemenceau | Grand Palais | 1, 13 | None | None | None | None | 1909005 | 48.8675 | 2.3135 | Paris 8th |
| Charles de Gaulle--Étoile | None | 1, 2, 6 | A | None | None | None | 4291663 | 48.873889 | 2.295 | Paris 8th, Paris 16th, Paris 17th |
| Château de Vincennes | None | 1 | None | None | None | None | 3617738 | 48.844444 | 2.44 | Paris 12th, Vincennes |
| Châtelet | None | 1, 4, 7, 11, 14 | A, B, D | None | None | None | 8350794 | 48.858352 | 2.347324 | Paris 1st, Paris 4th |
| Concorde | None | 1, 8, 12 | None | None | None | None | 3401219 | 48.86541 | 2.32111 | Paris 1st |
| Esplanade de La Défense | None | 1 | None | None | None | None | 4708183 | 48.888333 | 2.25 | Courbevoie, Puteaux |
| Franklin D. Roosevelt | None | 1, 9 | None | None | None | None | 6173830 | 48.868977 | 2.30989 | Paris 8th |
| Gare de Lyon | None | 1, 14 | A, D | None | R | TGV, TGV Lyria, Renfe-SNCF, OUIGO, Frecciarossa | 28640475 | 48.844722 | 2.373889 | Paris 12th |
| George V | None | 1 | None | None | None | None | 3842260 | 48.871944 | 2.300556 | Paris 8th |
| Hôtel de Ville | None | 1, 11 | None | None | None | None | 7251729 | 48.857487 | 2.351525 | Paris 4th |
| La Défense | Grande Arche | 1 | A, E | T2 | L, U | None | 9256802 | 48.891852 | 2.238539 | Puteaux |
| Les Sablons | Jardin d'Acclimatation | 1 | None | None | None | None | 3954920 | 48.880833 | 2.272222 | Neuilly-sur-Seine |
| Louvre--Rivoli | None | 1 | None | None | None | None | 1869612 | 48.86108 | 2.340283 | Paris 1st |
| Nation | None | 1, 2, 6, 9 | A | None | None | None | 6050797 | 48.848333 | 2.395833 | Paris 11th, Paris 12th |
| Palais Royal-Musée du Louvre | None | 1, 7 | None | None | None | None | 4822599 | 48.862644 | 2.336578 | Paris 1st |
| Pont de Neuilly | None | 1 | None | None | None | None | 4809503 | 48.885 | 2.259722 | Neuilly-sur-Seine |
| Porte de Vincennes | None | 1 | None | T3a, T3b | None | None | 5446602 | 48.847326 | 2.407759 | Paris 12th, Paris 20th |
| Porte Maillot | Palais des Congrès | 1 | C | None | None | None | 4138301 | 48.878056 | 2.281944 | Paris 16th, Paris 17th |
| Reuilly--Diderot | None | 1, 8 | None | None | None | None | 4580091 | 48.846944 | 2.386389 | Paris 12th |
| Saint-Mandé | None | 1 | None | None | None | None | 3944640 | 48.846111 | 2.418889 | Saint-Mandé |
| Saint-Paul | Le Marais | 1 | None | None | None | None | 4295823 | 48.855214 | 2.360859 | Paris 4th |
| Tuileries | None | 1 | None | None | None | None | 1859552 | 48.864531 | 2.329617 | Paris 1st |
| Alexandre Dumas | None | 2 | None | None | None | None | 2476608 | 48.855907 | 2.39479 | Paris 11th, Paris 20th |
| Anvers | Sacré-Cœur | 2 | None | None | None | Funiculaire de Montmartre | 3420749 | 48.883007 | 2.344849 | Paris 9th, Paris 18th |
| Avron | None | 2 | None | None | None | None | 1345521 | 48.85194 | 2.397863 | Paris 11th |
| Barbès--Rochechouart | None | 2, 4 | None | None | None | None | 5390939 | 48.883611 | 2.350556 | Paris 9th, Paris 10th, Paris 18th |
| Belleville | None | 2, 11 | None | None | None | None | 7314438 | 48.872083 | 2.376947 | Paris 10th |
| Blanche | None | 2 | None | None | None | None | 2167570 | 48.883459 | 2.333703 | Paris 9th |
| Colonel Fabien | None | 2 | None | None | None | None | 3043606 | 48.877136 | 2.37116 | Paris 10th |
| Courcelles | None | 2 | None | None | None | None | 1583429 | 48.879167 | 2.304167 | Paris 8th, Paris 17th |
| Couronnes | None | 2 | None | None | None | None | 2151515 | 48.869521 | 2.379861 | Paris 11th, Paris 20th |
| Jaurès | None | 2, 5, 7bis | None | None | None | None | 4055461 | 48.88292 | 2.37067 | Paris 10th, Paris 19th |
| La Chapelle | None | 2 | B, D, E | None | H, K | TGV, TER, Thalys, Eurostar | 4855531 | 48.884411 | 2.360288 | Paris 10th, Paris 18th |
| Ménilmontant | None | 2 | None | None | None | None | 2847264 | 48.866248 | 2.383618 | Paris 11th, Paris 20th |
| Monceau | None | 2 | None | None | None | None | 1148677 | 48.88 | 2.308333 | Paris 8th, Paris 17th |
| Père Lachaise | None | 2, 3 | None | None | None | None | 3465307 | 48.862921 | 2.387388 | Paris 11th, Paris 20th |
| Philippe Auguste | None | 2 | None | None | None | None | 1262653 | 48.858021 | 2.390938 | Paris 11th, Paris 20th |
| Pigalle | None | 2, 12 | None | None | None | None | 3501831 | 48.882255 | 2.337573 | Paris 9th, Paris 18th |
| Place de Clichy | None | 2, 13 | None | None | None | None | 5161932 | 48.883889 | 2.3275 | Paris 8th, Paris 9th, Paris 17th, Paris 18th |
| Porte Dauphine | None | 2 | C | None | None | None | 2021656 | 48.87139 | 2.27667 | Paris 16th |
| Rome | None | 2 | None | None | None | None | 1696331 | 48.882425 | 2.322052 | Paris 8th, Paris 17th |
| Stalingrad | None | 2, 5, 7 | None | None | None | None | 4924583 | 48.88429 | 2.36586 | Paris 10th, Paris 19th |
| Ternes | None | 2 | None | None | None | None | 2292256 | 48.877778 | 2.298611 | Paris 8th, Paris 17th |
| Victor Hugo | None | 2 | None | None | None | None | 2801041 | 48.86972 | 2.285 | Paris 16th |
| Villiers | None | 2, 3 | None | None | None | None | 3586376 | 48.88113 | 2.314867 | Paris 8th, Paris 17th |
| Anatole France | None | 3 | None | None | None | None | 2311825 | 48.892022 | 2.285536 | Levallois-Perret |
| Arts et Métiers | None | 3, 11 | None | None | None | None | 2403042 | 48.8655 | 2.3561 | Paris 3rd |
| Bourse | None | 3 | None | None | None | None | 1725043 | 48.868738 | 2.34137 | Paris 2nd |
| Europe | None | 3 | None | None | None | None | 1106459 | 48.878821 | 2.32238 | Paris 8th |
| Gallieni | Parc de Bagnolet | 3 | None | None | None | None | 3899195 | 48.8635 | 2.41578 | Bagnolet |
| Gambetta | None | 3 | None | None | None | None | 4796724 | 48.864947 | 2.398451 | Paris 20th |
| Havre--Caumartin | None | 3, 9 | A, E | None | None | None | 5894982 | 48.873465 | 2.327968 | Paris 9th |
| Louise Michel | None | 3 | None | None | None | None | 2319185 | 48.889273 | 2.288073 | Levallois-Perret |
| Malesherbes | None | 3 | None | None | None | None | 1427143 | 48.882476 | 2.311002 | Paris 17th |
| Opéra | None | 3, 7, 8 | A | None | None | None | 5193831 | 48.870636 | 2.332353 | Paris 2nd, Paris 9th |
| Parmentier | None | 3 | None | None | None | None | 2037234 | 48.865299 | 2.374381 | Paris 11th |
| Pereire | None | 3 | C | None | None | None | 3130190 | 48.884648 | 2.299211 | Paris 17th |
| Pont de Levallois--Bécon | None | 3 | None | None | None | None | 2984777 | 48.897313 | 2.280787 | Levallois-Perret |
| Porte de Bagnolet | None | 3 | None | T3b | None | None | 3085790 | 48.864565 | 2.407278 | Paris 20th |
| Porte de Champerret | None | 3 | None | None | None | None | 2101673 | 48.885851 | 2.293487 | Paris 17th |
| Quatre-Septembre | None | 3 | None | None | None | None | 1165004 | 48.869574 | 2.336633 | Paris 2nd |
| Réaumur--Sébastopol | None | 3, 4 | None | None | None | None | 3579544 | 48.866111 | 2.3525 | Paris 2nd, Paris 3rd |
| République | None | 3, 5, 8, 9, 11 | None | None | None | None | 11079708 | 48.867503 | 2.363811 | Paris 3rd, Paris 10th, Paris 11th |
| Rue Saint-Maur | None | 3 | None | None | None | None | 2004445 | 48.864335 | 2.379448 | Paris 11th |
| Saint-Lazare | None | 3, 12, 13, 14 | E | None | J, L | TGV, TER, Intercités | 33128384 | 48.87549 | 2.32664 | Paris 8th, Paris 9th |
| Sentier | None | 3 | None | None | None | None | 2222744 | 48.8676 | 2.3464 | Paris 2nd |
| Temple | None | 3 | None | None | None | None | 891858 | 48.866488 | 2.360595 | Paris 3rd |
| Wagram | None | 3 | None | None | None | None | 1508617 | 48.884057 | 2.303668 | Paris 17th |
| Pelleport | None | 3bis | None | None | None | None | 229524 | 48.868671 | 2.401752 | Paris 20th |
| Porte des Lilas | None | 3bis, 11 | None | T3b | None | None | 3105016 | 48.877183 | 2.406655 | Paris 19th, Paris 20th |
| Saint-Fargeau | None | 3bis | None | None | None | None | 472258 | 48.872083 | 2.40452 | Paris 20th |
| Alésia | None | 4 | None | None | None | None | 3098136 | 48.828333 | 2.326667 | Paris 14th |
| Bagneux--Lucie Aubrac | None | 4 | None | None | None | None | None | 48.8027 | 2.3173 | Bagneux |
| Barbara | None | 4 | None | None | None | None | None | 48.8092 | 2.3176 | Montrouge, Bagneux |
| Château d'Eau | None | 4 | None | None | None | None | 2687103 | 48.872778 | 2.356111 | Paris 10th |
| Château Rouge | None | 4 | None | None | None | None | 5841122 | 48.886667 | 2.349444 | Paris 18th |
| Cité | None | 4 | None | None | None | None | 1004657 | 48.855278 | 2.346389 | Paris 4th |
| Denfert-Rochereau | None | 4, 6 | B | None | None | None | 2543959 | 48.833901 | 2.332728 | Paris 14th |
| Étienne Marcel | None | 4 | None | None | None | None | 1705639 | 48.864167 | 2.350556 | Paris 1st |
| Gare de l'Est | None | 4, 5, 7 | None | None | P | TGV, TER, OUIGO, Nightjet | 15538471 | 48.876111 | 2.358333 | Paris 10th |
| Gare du Nord | None | 4, 5 | B, D, E | None | H, K | TGV, TER, Thalys, Eurostar | 34503097 | 48.880556 | 2.355 | Paris 10th |
| Les Halles | None | 4 | A, B, D | None | None | None | 10623876 | 48.8625 | 2.34611 | Paris 1st |
| Mairie de Montrouge | None | 4 | None | None | None | None | 4316647 | 48.81843 | 2.31953 | Montrouge |
| Marcadet--Poissonniers | None | 4, 12 | None | None | None | None | 3982005 | 48.890278 | 2.35 | Paris 18th |
| Montparnasse--Bienvenüe | None | 4, 6, 12, 13 | None | None | N | TGV, TER, Intercités, OUIGO | 20407224 | 48.843466 | 2.323072 | Paris 6th, Paris 14th, Paris 15th |
| Mouton-Duvernet | None | 4 | None | None | None | None | 1131403 | 48.832139 | 2.330325 | Paris 14th |
| Odéon | None | 4, 10 | None | None | None | None | 3478491 | 48.851944 | 2.338889 | Paris 6th |
| Porte d'Orléans | None | 4 | None | T3a | None | None | 4175817 | 48.823189 | 2.325364 | Paris 14th |
| Porte de Clignancourt | Puces de Saint-Ouen | 4 | None | T3b | None | None | 5611814 | 48.896944 | 2.345 | Paris 18th |
| Raspail | None | 4, 6 | None | None | None | None | 1238357 | 48.839194 | 2.330606 | Paris 14th |
| Saint-Germain-des-Prés | None | 4 | None | None | None | None | 2378860 | 48.853889 | 2.333333 | Paris 6th |
| Saint-Michel | None | 4 | B, C | None | None | None | 3747385 | 48.853611 | 2.343889 | Paris 5th, Paris 6th |
| Saint-Placide | None | 4 | None | None | None | None | 2391205 | 48.846844 | 2.326914 | Paris 6th |
| Saint-Sulpice | None | 4 | None | None | None | None | 1571987 | 48.850909 | 2.330652 | Paris 6th |
| Simplon | None | 4 | None | None | None | None | 2056501 | 48.893333 | 2.348333 | Paris 18th |
| Strasbourg--Saint-Denis | None | 4, 8, 9 | None | None | None | None | 6345770 | 48.869722 | 2.353889 | Paris 2nd, Paris 3rd, Paris 10th |
| Vavin | None | 4 | None | None | None | None | 1322588 | 48.842233 | 2.32895 | Paris 6th, Paris 14th |
| Bobigny--Pablo Picasso | Préfecture--Hôtel du Département | 5 | None | T1 | None | None | 6561327 | 48.906538 | 2.449994 | Bobigny |
| Bobigny--Pantin--Raymond Queneau | None | 5 | None | None | None | None | 2335465 | 48.895 | 2.425 | Bobigny |
| Bréguet--Sabin | None | 5 | None | None | None | None | 1490160 | 8.856 | 2.37 | Paris 11th |
| Campo Formio | None | 5 | None | None | None | None | 1016150 | 48.835 | 2.358 | Paris 13th |
| Église de Pantin | None | 5 | None | None | None | None | 2832467 | 48.894 | 2.413 | Pantin |
| Gare d'Austerlitz | None | 5, 10 | C | None | None | TGV, TER, Intercités | 6318543 | 48.842626 | 2.364971 | Paris 13th |
| Hoche | None | 5 | None | None | None | None | 3928404 | 48.891 | 2.403 | Pantin |
| Jacques Bonsergent | None | 5 | None | None | None | None | 1743989 | 48.871 | 2.361 | Paris 10th |
| Laumière | None | 5 | None | None | None | None | 3258568 | 48.885 | 2.379 | Paris 19th |
| Oberkampf | None | 5, 9 | None | None | None | None | 3205110 | 48.8635 | 2.37025 | Paris 11th |
| Ourcq | None | 5 | None | None | None | None | 2862337 | 48.887 | 2.386 | Paris 19th |
| Place d'Italie | None | 5, 6, 7 | None | None | None | None | 7119097 | 48.831483 | 2.355692 | Paris 13th |
| Porte de Pantin | Parc de la Villette | 5 | None | T3b | None | None | 3374733 | 48.88971 | 2.39629 | Paris 19th |
| Quai de la Rapée | None | 5 | None | None | None | None | 798728 | 48.846 | 2.366 | Paris 12th |
| Richard-Lenoir | None | 5 | None | None | None | None | 1544636 | 48.86 | 2.372 | Paris 11th |
| Saint-Marcel | None | 5 | None | None | None | None | 1666744 | 48.838 | 2.36 | Paris 13th |
| Bel-Air | None | 6 | None | None | None | None | 1605573 | 48.841344 | 2.400912 | Paris 12th |
| Bercy | None | 6, 14 | None | None | None | TER, Intercités | 3884212 | 48.83993 | 2.380418 | Paris 12th |
| Bir-Hakeim | Tour Eiffel | 6 | C | None | None | None | 3362908 | 48.853917 | 2.289332 | Paris 15th |
| Boissière | None | 6 | None | None | None | None | 1224181 | 48.867386 | 2.290392 | Paris 16th |
| Cambronne | None | 6 | None | None | None | None | 1636566 | 48.847537 | 2.302937 | Paris 15th |
| Chevaleret | None | 6 | None | None | None | None | 2748696 | 48.834938 | 2.368082 | Paris 13th |
| Corvisart | None | 6 | None | None | None | None | 1570331 | 48.829807 | 2.350508 | Paris 13th |
| Daumesnil | None | 6, 8 | None | None | None | None | 3634023 | 48.839644 | 2.395792 | Paris 12th |
| Dugommier | None | 6 | None | None | None | None | 1725412 | 48.83905 | 2.389964 | Paris 12th |
| Dupleix | None | 6 | None | None | None | None | 2028963 | 48.850392 | 2.293611 | Paris 15th |
| Edgar Quinet | None | 6 | None | None | None | None | 1349178 | 48.841048 | 2.325084 | Paris 14th |
| Glacière | None | 6 | None | None | None | None | 3005750 | 48.83115 | 2.343384 | Paris 13th |
| Kléber | None | 6 | None | None | None | None | 724215 | 48.871138 | 2.293118 | Paris 16th |
| La Motte-Picquet--Grenelle | None | 6, 8, 10 | None | None | None | None | 5117708 | 48.849143 | 2.29809 | Paris 15th |
| Nationale | None | 6 | None | None | None | None | 1320290 | 48.833183 | 2.362718 | Paris 13th |
| Passy | None | 6 | None | None | None | None | 2080548 | 48.857445 | 2.285779 | Paris 16th |
| Pasteur | None | 6, 12 | None | None | None | None | 3026286 | 48.842836 | 2.312681 | Paris 15th |
| Picpus | None | 6 | None | None | None | None | 931602 | 48.84515 | 2.400494 | Paris 12th |
| Quai de la Gare | None | 6 | None | None | None | None | 1735465 | 48.837069 | 2.372773 | Paris 13th |
| Saint-Jacques | None | 6 | None | None | None | None | 1407837 | 48.832913 | 2.337081 | Paris 14th |
| Sèvres--Lecourbe | None | 6 | None | None | None | None | 1257040 | 48.845634 | 2.309476 | Paris 15th |
| Trocadéro | None | 6, 9 | None | None | None | None | 5284134 | 48.863301 | 2.287061 | Paris 16th |
| Aubervilliers--Pantin--Quatre Chemins | None | 7 | None | None | None | None | 5616435 | 48.9039 | 2.3925 | Aubervilliers |
| Cadet | None | 7 | None | None | None | None | 1843984 | 48.876135 | 2.344876 | Paris 9th |
| Censier--Daubenton | None | 7 | None | None | None | None | 2291843 | 48.840597 | 2.351774 | Paris 5th |
| Château-Landon | None | 7 | None | None | P | TGV, TER | 1140353 | 48.87846 | 2.362071 | Paris 10th |
| Chaussée d'Antin--La Fayette | None | 7, 9 | None | None | None | None | 4251916 | 48.87307 | 2.33393 | Paris 9th |
| Corentin Cariou | None | 7 | None | None | None | None | 1697076 | 48.89434 | 2.381745 | Paris 19th |
| Crimée | None | 7 | None | None | None | None | 3543952 | 48.89158 | 2.37707 | Paris 19th |
| Fort d'Aubervilliers | None | 7 | None | None | None | None | 3103518 | 48.91424 | 2.403785 | Aubervilliers |
| Jussieu | None | 7, 10 | None | None | None | None | 2889642 | 48.846052 | 2.355738 | Paris 5th |
| La Courneuve--8 Mai 1945 | None | 7 | None | T1 | None | None | 4924444 | 48.920777 | 2.410668 | La Courneuve |
| Le Kremlin--Bicêtre | None | 7 | None | None | None | None | 2925325 | 48.810388 | 2.361849 | Le Kremlin-Bicêtre |
| Le Peletier | None | 7 | None | None | None | None | 1677832 | 48.87472 | 2.33955 | Paris 9th |
| Les Gobelins | None | 7 | None | None | None | None | 2365942 | 48.8364 | 2.35225 | Paris 5th, Paris 13th |
| Louis Blanc | None | 7 | None | None | None | None | 1548029 | 48.881137 | 2.364839 | Paris 10th |
| Mairie d'Ivry | None | 7 | None | None | None | None | 2042071 | 48.81112 | 2.38339 | Ivry-sur-Seine |
| Maison Blanche | None | 7 | None | None | None | None | 1203631 | 48.822155 | 2.358531 | Paris 13th |
| Pierre et Marie Curie | None | 7 | None | None | None | None | 1100552 | 48.81592 | 2.37789 | Ivry-sur-Seine |
| Place Monge | Jardin des Plantes--Arènes de Lutèce | 7 | None | None | None | None | 1837996 | 48.84359 | 2.352279 | Paris 5th |
| Poissonnière | None | 7 | None | None | None | None | 2306725 | 48.87708 | 2.34845 | Paris 9th, Paris 10th |
| Pont Marie | Cité des Arts | 7 | None | None | None | None | 1101482 | 48.85329 | 2.35762 | Paris 4th |
| Pont Neuf | None | 7 | None | None | None | None | 1188930 | 48.85868 | 2.34149 | Paris 1st |
| Porte d'Italie | None | 7 | None | T3a | None | None | 1507152 | 48.819196 | 2.360805 | Paris 13th |
| Porte d'Ivry | None | 7 | None | T3a | None | None | 1282199 | 48.82096 | 2.37044 | Paris 13th |
| Porte de Choisy | None | 7 | None | T3a, T9 | None | None | 1592144 | 48.82032 | 2.36529 | Paris 13th |
| Porte de la Villette | Cité des Sciences et de l'Industrie | 7 | None | T3b | None | None | 2706288 | 48.89709 | 2.38588 | Paris 19th |
| Pyramides | None | 7, 14 | None | None | None | None | 3962698 | 48.86587 | 2.33467 | Paris 1st |
| Riquet | None | 7 | None | None | None | None | 1588438 | 48.88788 | 2.373578 | Paris 19th |
| Sully--Morland | None | 7 | None | None | None | None | 1124169 | 48.851425 | 2.361894 | Paris 4th |
| Tolbiac | None | 7 | None | None | None | None | 2287918 | 48.826665 | 2.357678 | Paris 13th |
| Villejuif--Léo Lagrange | None | 7 | None | T7 | None | None | 1952627 | 48.803768 | 2.363927 | Villejuif |
| Villejuif--Louis Aragon | None | 7 | None | None | None | None | 5218070 | 48.787175 | 2.367564 | Villejuif |
| Villejuif--Paul Vaillant-Couturier | Hôpital Paul Brousse | 7 | None | None | None | None | 1764879 | 48.795991 | 2.368248 | Villejuif |
| Bolivar | None | 7bis | None | None | None | None | 367598 | 48.880502 | 2.374922 | Paris 19th |
| Botzaris | None | 7bis | None | None | None | None | 669323 | 48.879552 | 2.38804 | Paris 19th |
| Buttes Chaumont | None | 7bis | None | None | None | None | 358301 | 48.8785 | 2.381772 | Paris 19th |
| Danube | None | 7bis | None | None | None | None | 400157 | 48.881808 | 2.394201 | Paris 19th |
| Place des Fêtes | None | 7bis, 11 | None | None | None | None | 2318764 | 48.87684 | 2.39296 | Paris 19th |
| Pré-Saint-Gervais | None | 7bis | None | T3b | None | None | 282626 | 48.88025 | 2.39891 | Paris 19th |
| Balard | None | 8 | None | T2, T3a | None | None | 3236801 | 48.83597 | 2.278212 | Paris 15th |
| Bonne Nouvelle | None | 8, 9 | None | None | None | None | 2806227 | 48.870639 | 2.348875 | Paris 2nd |
| Boucicaut | None | 8 | None | None | None | None | 2288055 | 48.840578 | 2.286621 | Paris 15th |
| Charenton--Écoles | None | 8 | None | None | None | None | 2164023 | 48.82149 | 2.41386 | Charenton-le-Pont |
| Chemin Vert | None | 8 | None | None | None | None | 1018958 | 48.856778 | 2.368348 | Paris 3rd |
| Commerce | None | 8 | None | None | None | None | 2212666 | 48.845093 | 2.294215 | Paris 15th |
| Créteil--L'Échat | Hôpital Henri Mondor | 8 | None | None | None | None | 1660120 | 48.795963 | 2.449356 | Créteil |
| Créteil--Préfecture | Hôtel de Ville | 8 | None | None | None | None | 3330602 | 48.779772 | 2.459317 | Créteil |
| Créteil--Université | None | 8 | None | None | None | None | 2496595 | 48.789754 | 2.450785 | Créteil |
| École Militaire | None | 8 | None | None | None | None | 2805976 | 48.85511 | 2.306737 | Paris 7th |
| École Vétérinaire de Maisons-Alfort | None | 8 | None | None | None | None | 2269487 | 48.81519 | 2.421882 | Maisons-Alfort |
| Faidherbe--Chaligny | None | 8 | None | None | None | None | 2190416 | 48.850158 | 2.383398 | Paris 11th |
| Félix Faure | None | 8 | None | None | None | None | 1161978 | 48.842351 | 2.291004 | Paris 15th |
| Filles du Calvaire | None | 8 | None | None | None | None | 1093673 | 48.864167 | 2.366111 | Paris 3rd |
| Grands Boulevards | None | 8, 9 | None | None | None | None | 3737316 | 48.871426 | 2.344342 | Paris 2nd, Paris 9th |
| Invalides | None | 8, 13 | C | None | None | None | 3482080 | 48.86299 | 2.31333 | Paris 7th |
| La Tour-Maubourg | None | 8 | None | None | None | None | 1361723 | 48.857667 | 2.310399 | Paris 7th |
| Ledru-Rollin | None | 8 | None | None | None | None | 2570283 | 48.851529 | 2.37516 | Paris 11th, Paris 12th |
| Liberté | None | 8 | None | None | None | None | 1704609 | 48.825882 | 2.407022 | Charenton-le-Pont |
| Lourmel | None | 8 | None | None | None | None | 1696432 | 48.838604 | 2.281817 | Paris 15th |
| Madeleine | None | 8, 12, 14 | None | None | None | None | 5330928 | 48.86977 | 2.3244 | Paris 8th |
| Maisons-Alfort--Les Juilliottes | None | 8 | None | None | None | None | 1297495 | 48.802567 | 2.446432 | Maisons-Alfort |
| Maisons-Alfort--Stade | None | 8 | None | None | None | None | 1702479 | 48.808681 | 2.436073 | Maisons-Alfort |
| Michel Bizot | None | 8 | None | None | None | None | 1403416 | 48.837485 | 2.401234 | Paris 12th |
| Montgallet | None | 8 | None | None | None | None | 1108395 | 48.844276 | 2.389974 | Paris 12th |
| Pointe du Lac | Créteil | 8 | None | None | None | None | 2114438 | 48.76889 | 2.46472 | Créteil |
| Porte de Charenton | None | 8 | None | T3a | None | None | 1529778 | 48.83278 | 2.4004 | Paris 12th |
| Porte Dorée | None | 8 | None | T3a | None | None | 1918182 | 48.835481 | 2.4061 | Paris 12th |
| Richelieu--Drouot | None | 8 | None | None | None | None | 2994510 | 48.871987 | 2.338741 | Paris 2nd, Paris 9th |
| Saint-Sébastien--Froissart | None | 8 | None | None | None | None | 1151192 | 48.86048 | 2.367358 | Paris 3rd, Paris 11th |
| Alma--Marceau | None | 9 | None | None | None | None | 2564842 | 48.864904 | 2.300234 | Paris 8th, Paris 16th |
| Billancourt | None | 9 | None | None | None | None | 1967532 | 48.83209 | 2.238177 | Boulogne-Billancourt |
| Buzenval | None | 9 | None | None | None | None | 1448855 | 48.851976 | 2.402045 | Paris 20th |
| Charonne | None | 9 | None | None | None | None | 2705320 | 48.855103 | 2.384639 | Paris 11th |
| Croix de Chavaux | None | 9 | None | None | None | None | 3729545 | 48.858055 | 2.435764 | Montreuil |
| Exelmans | None | 9 | None | None | None | None | 1607223 | 48.842405 | 2.259549 | Paris 16th |
| Iéna | None | 9 | None | None | None | None | 1646925 | 48.864466 | 2.29338 | Paris 16th |
| Jasmin | None | 9 | None | None | None | None | 1418238 | 48.851898 | 2.267856 | Paris 16th |
| La Muette | None | 9 | C | None | None | None | 3010370 | 48.857718 | 2.273719 | Paris 16th |
| Mairie de Montreuil | None | 9 | None | None | None | None | 6158487 | 48.862283 | 2.441847 | Montreuil |
| Maraîchers | None | 9 | None | None | None | None | 1994064 | 48.852851 | 2.40699 | Paris 20th |
| Marcel Sembat | None | 9 | None | None | None | None | 3874792 | 48.83367 | 2.243579 | Boulogne-Billancourt |
| Michel-Ange--Auteuil | None | 9, 10 | None | None | None | None | 1512050 | 48.8475 | 2.263611 | Paris 16th |
| Michel-Ange--Molitor | None | 9, 10 | None | None | None | None | 1420552 | 48.84496 | 2.261194 | Paris 16th |
| Miromesnil | None | 9, 13 | None | None | None | None | 3647255 | 48.87367 | 2.31446 | Paris 8th |
| Pont de Sèvres | None | 9 | None | T2 | None | None | 3430203 | 48.829747 | 2.231035 | Boulogne-Billancourt |
| Porte de Montreuil | None | 9 | None | T3b | None | None | 3067413 | 48.853792 | 2.412245 | Paris 20th |
| Porte de Saint-Cloud | Parc des Princes | 9 | None | None | None | None | 3485946 | 48.838082 | 2.256956 | Paris 16th |
| Ranelagh | None | 9 | None | None | None | None | 1779206 | 48.85502 | 2.269634 | Paris 16th |
| Robespierre | None | 9 | None | None | None | None | 2986308 | 48.855683 | 2.423678 | Montreuil |
| Rue de la Pompe | None | 9 | None | None | None | None | 2449458 | 48.863912 | 2.279052 | Paris 16th |
| Rue des Boulets | None | 9 | None | None | None | None | 1832442 | 48.851811 | 2.390151 | Paris 11th |
| Saint-Ambroise | None | 9 | None | None | None | None | 2158466 | 48.861295 | 2.374211 | Paris 11th |
| Saint-Augustin | None | 9 | None | None | None | None | 1934106 | 48.874441 | 2.322133 | Paris 8th |
| Saint-Philippe du Roule | None | 9 | None | None | None | None | 1935004 | 48.871941 | 2.310036 | Paris 8th |
| Voltaire | None | 9 | None | None | None | None | 3454006 | 48.857803 | 2.380106 | Paris 11th |
| Avenue Émile Zola | None | 10 | None | None | None | None | 1041233 | 48.846977 | 2.294512 | Paris 15th |
| Boulogne--Jean Jaurès | None | 10 | None | None | None | None | 2700354 | 48.842278 | 2.238877 | Boulogne-Billancourt |
| Boulogne--Pont de Saint-Cloud | None | 10 | None | T2 | None | None | 2182738 | 48.840684 | 2.228331 | Boulogne-Billancourt |
| Cardinal Lemoine | None | 10 | None | None | None | None | 1121854 | 48.847139 | 2.351203 | Paris 5th |
| Chardon Lagache | None | 10 | None | None | None | None | 482053 | 48.845138 | 2.266214 | Paris 16th |
| Charles Michels | None | 10 | None | None | None | None | 3079569 | 48.846591 | 2.286942 | Paris 15th |
| Cluny--La Sorbonne | None | 10 | B, C | None | None | None | 1261818 | 48.851019 | 2.344583 | Paris 5th |
| Duroc | None | 10, 13 | None | None | None | None | 2645064 | 48.846829 | 2.316479 | Paris 6th, Paris 7th, Paris 15th |
| Église d'Auteuil | None | 10 | None | None | None | None | 124941 | 48.847169 | 2.26902 | Paris 16th |
| Javel--André Citroën | None | 10 | C | None | None | None | 1589561 | 48.846165 | 2.278716 | Paris 15th |
| Mabillon | None | 10 | None | None | None | None | 1195051 | 48.852775 | 2.335322 | Paris 6th |
| Maubert--Mutualité | None | 10 | None | None | None | None | 1280387 | 48.850193 | 2.347936 | Paris 5th |
| Mirabeau | None | 10 | None | None | None | None | 1001302 | 48.8469 | 2.2721 | Paris 16th |
| Porte d'Auteuil | None | 10 | None | None | None | None | 375748 | 48.848025 | 2.25875 | Paris 16th |
| Ségur | None | 10 | None | None | None | None | 1100151 | 48.847434 | 2.306853 | Paris 7th, Paris 15th |
| Sèvres--Babylone | None | 10, 12 | None | None | None | None | 3392504 | 48.85151 | 2.326655 | Paris 6th, Paris 7th |
| Vaneau | None | 10 | None | None | None | None | 725826 | 48.848947 | 2.321557 | Paris 6th, Paris 7th |
| Côteaux Beauclair | None | 11 | None | None | None | None | None | 48.882319 | 2.467539 | Rosny-sous-Bois, Noisy-le-Sec |
| La Dhuys | None | 11 | None | None | None | None | None | 48.877536 | 2.4651 | Montreuil, Rosny-sous-Bois |
| Montreuil-Hôpital | None | 11 | None | None | None | None | None | 48.8783 | 2.454617 | Montreuil |
| Romainville--Carnot | None | 11 | None | None | None | None | None | 48.883253 | 2.440822 | Romainville |
| Rosny-Bois Perrier | None | 11 | E | None | None | None | None | 48.88264 | 2.4815 | Rosny-sous-Bois |
| Serge Gainsbourg | None | 11 | None | None | None | None | None | 48.881258 | 2.427228 | Les Lilas |
| Goncourt | Hôpital Saint-Louis | 11 | None | None | None | None | 2199170 | 48.869831 | 2.370687 | Paris 10th, Paris 11th |
| Jourdain | None | 11 | None | None | None | None | 1881321 | 48.8752 | 2.389508 | Paris 19th, Paris 20th |
| Mairie des Lilas | None | 11 | None | None | None | None | 2894622 | 48.879788 | 2.416289 | Les Lilas |
| Pyrénées | None | 11 | None | None | None | None | 2288587 | 48.873875 | 2.385259 | Paris 19th, Paris 20th |
| Rambuteau | Centre Georges Pompidou | 11 | None | None | None | None | 2127291 | 48.86119 | 2.35343 | Paris 3rd, Paris 4th |
| Télégraphe | None | 11 | None | None | None | None | 1636898 | 48.875463 | 2.398434 | Paris 19th, Paris 20th |
| Abbesses | Butte Montmartre | 12 | None | None | None | Funiculaire de Montmartre | 1513884 | 48.884849 | 2.338688 | Paris 18th |
| Aimé Césaire | None | 12 | None | None | None | None | None | 48.908317 | 2.37802 | Aubervilliers |
| Assemblée Nationale | None | 12 | None | None | None | None | 611512 | 48.860655 | 2.32113 | Paris 7th |
| Convention | None | 12 | None | None | None | None | 3734750 | 48.837419 | 2.296795 | Paris 15th |
| Corentin Celton | None | 12 | None | None | None | None | 2504682 | 48.826833 | 2.278985 | Issy-les-Moulineaux |
| Falguière | None | 12 | None | None | None | None | 650291 | 48.844566 | 2.318287 | Paris 15th |
| Front Populaire | None | 12 | None | None | None | None | 1948542 | 48.9068 | 2.366 | Aubervilliers, Saint-Denis |
| Jules Joffrin | None | 12 | None | None | None | None | 2854819 | 48.892437 | 2.344782 | Paris 18th |
| Lamarck--Caulaincourt | None | 12 | None | None | None | None | 1875717 | 48.889139 | 2.338159 | Paris 18th |
| Mairie d'Aubervilliers | Plaine des Vertus | 12 | None | None | None | None | None | 48.913829 | 2.380651 | Aubervilliers |
| Mairie d'Issy | None | 12 | None | None | None | None | 2874138 | 48.824152 | 2.273434 | Issy-les-Moulineaux |
| Marx Dormoy | None | 12 | None | None | None | None | 2425928 | 48.891213 | 2.359909 | Paris 18th |
| Notre-Dame-de-Lorette | None | 12 | None | None | None | None | 1893828 | 48.87604 | 2.337341 | Paris 9th |
| Notre-Dame-des-Champs | None | 12 | None | None | None | None | 1487256 | 48.844568 | 2.328788 | Paris 6th |
| Porte de la Chapelle | None | 12 | None | T3b | None | None | 1866281 | 48.897274 | 2.359191 | Paris 18th |
| Porte de Versailles | Parc des Expositions | 12 | None | T2, T3a | None | None | 3268157 | 48.832328 | 2.287841 | Paris 15th |
| Rennes | None | 12 | None | None | None | None | 861334 | 48.848193 | 2.327763 | Paris 6th |
| Rue du Bac | None | 12 | None | None | None | None | 1423364 | 48.85569 | 2.325607 | Paris 7th |
| Saint-Georges | None | 12 | None | None | None | None | 1258381 | 48.878449 | 2.337382 | Paris 9th |
| Solférino | Musée d'Orsay | 12 | None | None | None | None | 1269143 | 48.858249 | 2.323225 | Paris 7th |
| Trinité--d'Estienne d'Orves | None | 12 | None | None | None | None | 1051982 | 48.876302 | 2.333197 | Paris 9th |
| Vaugirard | None | 12 | None | None | None | None | 2482886 | 48.839649 | 2.301491 | Paris 15th |
| Volontaires | None | 12 | None | None | None | None | 1734848 | 48.841343 | 2.307504 | Paris 15th |
| Basilique de Saint-Denis | Hôtel de Ville | 13 | None | T1, T5 | None | None | 3991395 | 48.93806 | 2.36083 | Saint-Denis |
| Brochant | None | 13 | None | None | None | None | 1543298 | 48.890833 | 2.319722 | Paris 17th |
| Carrefour Pleyel | None | 13 | None | None | None | None | 1535528 | 48.92 | 2.34389 | Saint-Denis |
| Châtillon--Montrouge | None | 13 | None | T6 | None | None | 5034012 | 48.810539 | 2.301826 | Châtillon, Montrouge |
| Gabriel Péri | None | 13 | None | None | None | None | 3790573 | 48.916667 | 2.294444 | Asnières-sur-Seine, Gennevilliers |
| Gaîté | None | 13 | None | None | None | None | 1644148 | 48.838654 | 2.322637 | Paris 14th |
| Garibaldi | None | 13 | None | None | None | None | 1965002 | 48.90639 | 2.33194 | Saint-Ouen-sur-Seine |
| Guy Môquet | None | 13 | None | None | None | None | 2205313 | 48.892222 | 2.327222 | Paris 17th, Paris 18th |
| La Fourche | None | 13 | None | None | None | None | 1829271 | 48.886944 | 2.325833 | Paris 17th, Paris 18th |
| Les Agnettes | None | 13 | None | None | None | None | 1890356 | 48.923056 | 2.285833 | Asnières-sur-Seine, Gennevilliers |
| Les Courtilles | Asnières--Gennevilliers | 13 | None | T1 | None | None | 2802689 | 48.930556 | 2.283889 | Asnières-sur-Seine, Gennevilliers |
| Liège | None | 13 | None | None | None | None | 1143956 | 48.879722 | 2.326944 | Paris 8th, Paris 9th |
| Mairie de Clichy | None | 13 | None | None | None | None | 4043071 | 48.903056 | 2.306111 | Clichy |
| Mairie de Saint-Ouen | Région Île-de-France | 13, 14 | None | None | None | None | 4830810 | 48.91167 | 2.33389 | Saint-Ouen-sur-Seine |
| Malakoff--Plateau de Vanves | None | 13 | None | None | None | None | 2242320 | 48.82284 | 2.29834 | Malakoff |
| Malakoff--Rue Étienne Dolet | None | 13 | None | None | None | None | 1450451 | 48.8147 | 2.2973 | Malakoff |
| Pernety | None | 13 | None | None | None | None | 2173567 | 48.83421 | 2.31851 | Paris 14th |
| Plaisance | None | 13 | None | None | None | None | 3521753 | 48.831553 | 2.313741 | Paris 14th |
| Porte de Clichy | Tribunal de Paris | 13, 14 | C | T3b | None | None | 5278497 | 48.893889 | 2.314444 | Paris 17th |
| Porte de Saint-Ouen | None | 13 | None | T3b | None | None | 2710638 | 48.896667 | 2.328611 | Paris 17th, Paris 18th |
| Porte de Vanves | None | 13 | None | T3a | None | None | 3395358 | 48.82794 | 2.30588 | Paris 14th |
| Saint-Denis--Porte de Paris | Stade de France | 13 | None | T8 | None | None | 3355836 | 48.93028 | 2.35778 | Saint-Denis |
| Saint-Denis--Université | None | 13 | None | T5 | None | None | 3569990 | 48.94583 | 2.36361 | Saint-Denis |
| Saint-François-Xavier | None | 13 | None | None | None | None | 1213378 | 48.851951 | 2.314475 | Paris 7th |
| Varenne | None | 13 | None | None | None | None | 782697 | 48.856238 | 2.314921 | Paris 7th |
| Bibliothèque François Mitterrand | None | 14 | C | T3a | None | None | 11104474 | 48.829822 | 2.376781 | Paris 13th |
| Cour Saint-Émilion | None | 14 | None | None | None | None | 2985122 | 48.834 | 2.386 | Paris 12th |
| Olympiades | None | 14 | None | None | None | None | 5214595 | 48.827222 | 2.368333 | Paris 13th |
| Pont Cardinet | None | 14 | None | None | L | None | 4168538 | 48.889481 | 2.315206 | Paris 17th |
| Saint-Ouen | None | 14 | C | None | None | None | 3420852 | 48.904497 | 2.321806 | Clichy, Saint-Ouen-sur-Seine |
