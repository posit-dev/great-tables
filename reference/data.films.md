## data.films


Feature films in competition at the Cannes Film Festival.


`data.films=_read_csv(_films_fname, dtype=_films_dtype)`  


Each entry in the [films](data.films.md#great_tables.data.films) is a feature film that appeared in the official selection during a festival year (starting in 1946 and active to the present day). The `year` column refers to the year of the festival and this figure doesn't always coincide with the release year of the film. The film's title reflects the most common title of the film in English, where the `original_title` column provides the title of the film in its spoken language (transliterated to Roman script where necessary).


This is a dataset with 1,851 rows and 8 columns.

- `year`: The year of the festival in which the film was in competition.
- [title](loc.title.md#great_tables.loc.title), `original_title`: The [title](loc.title.md#great_tables.loc.title) field provides the film title used for English-speaking audiences. The `original_title` field is populated when [title](loc.title.md#great_tables.loc.title) differs greatly from the non-English original.
- `director`: The director or set of co-directors for the film. Multiple directors are separated by a comma.
- `languages`: The languages spoken in the film in the order of appearance. This consists of ISO 639 language codes (primarily as two-letter codes, but using three-letter codes where necessary).
- `countries_of_origin`: The country or countries of origin for the production. Here, 2-letter ISO 3166-1 country codes (set in uppercase) are used.
- `run_time`: The run time of the film in hours and minutes. This is given as a string in the format `<x>h <y>m`.
- `imdb_url`: The URL of the film's information page in the Internet Movie Database (IMDB).


    Rows: 1851
    Columns: 8
    $ year                <i64> 1946, 1946, 1946
    $ title               <str> 'The Lovers', 'Anna and the King of Siam', 'Blood and Fire'
    $ original_title      <str> 'Amanti in fuga', None, 'Blod och eld'
    $ director            <str> 'Giacomo Gentilomo', 'John Cromwell', 'Anders Henrikson'
    $ languages           <str> 'it', 'en', 'sv'
    $ countries_of_origin <str> 'IT', 'US', 'SE'
    $ run_time            <str> '1h 30m', '2h 8m', '1h 40m'
    $ imdb_url            <str> 'https://www.imdb.com/title/tt0038297/',
                                'https://www.imdb.com/title/tt0038303/',
                                'https://www.imdb.com/title/tt0037544/'
