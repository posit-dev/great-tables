# data.films

Feature films in competition at the Cannes Film Festival.

`data.films=_read_csv(_films_fname, dtype=_films_dtype)`

Each entry in the [films](../reference/data.films.md#great_tables.data.films) is a feature film that appeared in the official selection during a festival year (starting in 1946 and active to the present day). The `year` column refers to the year of the festival and this figure doesn't always coincide with the release year of the film. The film's title reflects the most common title of the film in English, where the `original_title` column provides the title of the film in its spoken language (transliterated to Roman script where necessary).

## Details

This is a dataset with 1,851 rows and 8 columns.

- `year`: The year of the festival in which the film was in competition.
- [title](../reference/loc.title.md#great_tables.loc.title), `original_title`: The [title](../reference/loc.title.md#great_tables.loc.title) field provides the film title used for English-speaking audiences. The `original_title` field is populated when [title](../reference/loc.title.md#great_tables.loc.title) differs greatly from the non-English original.
- `director`: The director or set of co-directors for the film. Multiple directors are separated by a comma.
- `languages`: The languages spoken in the film in the order of appearance. This consists of ISO 639 language codes (primarily as two-letter codes, but using three-letter codes where necessary).
- `countries_of_origin`: The country or countries of origin for the production. Here, 2-letter ISO 3166-1 country codes (set in uppercase) are used.
- `run_time`: The run time of the film in hours and minutes. This is given as a string in the format `<x>h <y>m`.
- `imdb_url`: The URL of the film's information page in the Internet Movie Database (IMDB).

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

| year | title | original_title | director | languages | countries_of_origin | run_time | imdb_url |
|----|----|----|----|----|----|----|----|
| 1946 | The Lovers | Amanti in fuga | Giacomo Gentilomo | it | IT | 1h 30m | https://www.imdb.com/title/tt0038297/ |
| 1946 | Anna and the King of Siam | None | John Cromwell | en | US | 2h 8m | https://www.imdb.com/title/tt0038303/ |
| 1946 | Blood and Fire | Blod och eld | Anders Henrikson | sv | SE | 1h 40m | https://www.imdb.com/title/tt0037544/ |
| 1946 | Letter from the Dead | Brevet fra afdøde | Johan Jacobsen | da | DK | 1h 18m | https://www.imdb.com/title/tt0124300/ |
| 1946 | Brief Encounter | None | David Lean | en,fr | GB | 1h 26m | https://www.imdb.com/title/tt0037558/ |
| 1946 | Caesar and Cleopatra | None | Gabriel Pascal | en | GB | 2h 18m | https://www.imdb.com/title/tt0038390/ |
| 1946 | Camões | None | José Leitão de Barros | pt | PT | 1h 58m | https://www.imdb.com/title/tt0038394/ |
| 1946 | Girl No. 217 | Chelovek No. 217 | Mikhail Romm | ru | SU | 1h 31m | https://www.imdb.com/title/tt0037589/ |
| 1946 | Red Meadows | De røde enge | Bodil Ipsen, Lau Lauritzen | da,de | DK | 1h 25m | https://www.imdb.com/title/tt0038043/ |
| 1946 | The Last Chance | Die letzte Chance | Leopold Lindtberg | en,it,de,fr | CH | 1h 53m | https://www.imdb.com/title/tt0037871/ |
