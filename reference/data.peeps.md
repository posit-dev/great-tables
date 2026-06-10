## data.peeps


A table of personal information for people all over the world.


`data.peeps=_read_csv(_peeps_fname, dtype=_peeps_dtype)`  


The [peeps](data.peeps.md#great_tables.data.peeps) dataset contains records for one hundred people residing in ten different countries. Each person in the table has address information along with their email address and phone number. There are also personal characteristics like date of birth, height, and weight. This data has been synthesized, and so the names within the table have not been taken or based on individuals in real life. The street addresses were generated from actual street names within real geographic localities, however, the street numbers were assigned randomly from a constrained number set. While these records do not relate to real people, efforts were made to make the data as realistic as possible.


This is a dataset with 100 rows and 14 columns.

- `name_given`, `name_family`: The given and family name of individual.
- `address`: The street address of the individual.
- `city`: The name of the city or locality in which the individual resides.
- `state_prov`: The state or province associated with the `city` and `address`. This is `None` for individuals residing in countries where subdivision data is not needed for generating a valid mailing address.
- `postcode`: The post code associated with the `city` and `address`.
- `country`: The 3-letter ISO 3166-1 country code representative of the individual's country.
- `email_addr`: The individual's email address.
- `phone_number`, `country_code`: The individual's phone number and the country code associated with the phone number.
- `gender`: The gender of the individual.
- `dob`: The individual's date of birth (DOB) in the ISO 8601 form of `YYYY-MM-DD`.
- `height_cm`, `weight_kg`: The height and weight of the individual in centimeters (cm) and kilograms (kg), respectively.


    Rows: 100
    Columns: 14
    $ name_given   <str> 'Ruth', 'Peter', 'Fanette'
    $ name_family  <str> 'Conte', 'Möller', 'Gadbois'
    $ address      <str> '4299 Bobcat Drive', '3705 Hidden Pond Road', '4200 Swick Hill Street'
    $ city         <str> 'Baileys Crossroads', 'Red Boiling Springs', 'New Orleans'
    $ state_prov   <str> 'MD', 'TN', 'LA'
    $ postcode     <str> '22041', '37150', '70112'
    $ country      <str> 'USA', 'USA', 'USA'
    $ email_addr   <str> 'rcconte@example.com', 'pmoeller@example.com', 'fan_gadbois@example.com'
    $ phone_number <str> '240-783-7630', '615-699-3517', '985-205-2970'
    $ country_code <str> '1', '1', '1'
    $ gender       <str> 'female', 'male', 'female'
    $ dob          <str> '1949-03-16', '1939-11-22', '1970-12-20'
    $ height_cm    <i64> 153, 175, 167
    $ weight_kg    <f64> 76.4, 74.9, 61.6
