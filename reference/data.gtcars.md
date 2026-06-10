## data.gtcars


Deluxe automobiles from the 2014-2017 period.


`data.gtcars=_read_csv(_gtcars_fname, dtype=_gtcars_dtype)`  


Expensive and fast cars. Each row describes a car of a certain make, model, year, and trim. Basic specifications such as horsepower, torque, EPA MPG ratings, type of drivetrain, and transmission characteristics are provided. The country of origin for the car manufacturer is also given.

All of the [gtcars](data.gtcars.md#great_tables.data.gtcars) have something else in common (aside from the high asking prices): they are all grand tourer vehicles. These are proper GT cars that blend pure driving thrills with a level of comfort that is more expected from a fine limousine (e.g., a Rolls-Royce Phantom EWB). You'll find that, with these cars, comfort is emphasized over all-out performance. Nevertheless, the driving experience should also mean motoring at speed, doing so in style and safety.


This is a dataset with 47 rows and 15 columns.

- `mfr`: The name of the car manufacturer.
- `model`: The car's model name.
- `year`: The car's model year.
- `trim`: A short description of the car model's trim.
- `bdy_style`: An identifier of the car's body style, which is either `"coupe"`, `"convertible"`, `"sedan"`, or `"hatchback"`.
- `hp`, `hp_rpm`: The car's horsepower and the associated RPM level.
- `trq`, `trq_rpm`: The car's torque and the associated RPM level.
- `mpg_c`, `mpg_h`: The miles per gallon fuel efficiency rating for city and highway driving.
- `drivetrain`: The car's drivetrain which, for this dataset, is either `"rwd"` (Rear Wheel Drive) or `"awd"` (All Wheel Drive).
- `trsmn`: An encoding of the transmission type, where the number part is the number of gears. The car could have automatic transmission (`"a"`), manual transmission (`"m"`), an option to switch between both types (`"am"`), or, direct drive (`"dd"`)
- `ctry_origin`: The country name for where the vehicle manufacturer is headquartered.
- `msrp`: Manufacturer's suggested retail price in U.S. dollars (USD).


    Rows: 47
    Columns: 15
    $ mfr         <str> 'Ford', 'Ferrari', 'Ferrari'
    $ model       <str> 'GT', '458 Speciale', '458 Spider'
    $ year        <i64> 2017, 2015, 2015
    $ trim        <str> 'Base Coupe', 'Base Coupe', 'Base'
    $ bdy_style   <str> 'coupe', 'coupe', 'convertible'
    $ hp          <f64> 647.0, 597.0, 562.0
    $ hp_rpm      <f64> 6250.0, 9000.0, 9000.0
    $ trq         <f64> 550.0, 398.0, 398.0
    $ trq_rpm     <f64> 5900.0, 6000.0, 6000.0
    $ mpg_c       <f64> 11.0, 13.0, 13.0
    $ mpg_h       <f64> 18.0, 17.0, 17.0
    $ drivetrain  <str> 'rwd', 'rwd', 'rwd'
    $ trsmn       <str> '7a', '7a', '7a'
    $ ctry_origin <str> 'United States', 'Italy', 'Italy'
    $ msrp        <f64> 447000.0, 291744.0, 263553.0
