# data.gtcars

Deluxe automobiles from the 2014-2017 period.

`data.gtcars=_read_csv(_gtcars_fname, dtype=_gtcars_dtype)`

Expensive and fast cars. Each row describes a car of a certain make, model, year, and trim. Basic specifications such as horsepower, torque, EPA MPG ratings, type of drivetrain, and transmission characteristics are provided. The country of origin for the car manufacturer is also given.

All of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) have something else in common (aside from the high asking prices): they are all grand tourer vehicles. These are proper GT cars that blend pure driving thrills with a level of comfort that is more expected from a fine limousine (e.g., a Rolls-Royce Phantom EWB). You'll find that, with these cars, comfort is emphasized over all-out performance. Nevertheless, the driving experience should also mean motoring at speed, doing so in style and safety.

## Details

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

## Preview

Here is the dataset as an interactive table. Each column has its dtype and a profile of its values, and the rows can be sorted, searched, and filtered by any column.

``` python
from great_tables import GTI
from great_tables.data import gtcars

GTI(gtcars, preset="explorer").i_responsive("scroll")
```

| mfr | model | year | trim | bdy_style | hp | hp_rpm | trq | trq_rpm | mpg_c | mpg_h | drivetrain | trsmn | ctry_origin | msrp |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Ford | GT | 2017 | Base Coupe | coupe | 647.0 | 6250.0 | 550.0 | 5900.0 | 11.0 | 18.0 | rwd | 7a | United States | 447000.0 |
| Ferrari | 458 Speciale | 2015 | Base Coupe | coupe | 597.0 | 9000.0 | 398.0 | 6000.0 | 13.0 | 17.0 | rwd | 7a | Italy | 291744.0 |
| Ferrari | 458 Spider | 2015 | Base | convertible | 562.0 | 9000.0 | 398.0 | 6000.0 | 13.0 | 17.0 | rwd | 7a | Italy | 263553.0 |
| Ferrari | 458 Italia | 2014 | Base Coupe | coupe | 562.0 | 9000.0 | 398.0 | 6000.0 | 13.0 | 17.0 | rwd | 7a | Italy | 233509.0 |
| Ferrari | 488 GTB | 2016 | Base Coupe | coupe | 661.0 | 8000.0 | 561.0 | 3000.0 | 15.0 | 22.0 | rwd | 7a | Italy | 245400.0 |
| Ferrari | California | 2015 | Base Convertible | convertible | 553.0 | 7500.0 | 557.0 | 4750.0 | 16.0 | 23.0 | rwd | 7a | Italy | 198973.0 |
| Ferrari | GTC4Lusso | 2017 | Base Coupe | coupe | 680.0 | 8250.0 | 514.0 | 5750.0 | 12.0 | 17.0 | awd | 7a | Italy | 298000.0 |
| Ferrari | FF | 2015 | Base Coupe | coupe | 652.0 | 8000.0 | 504.0 | 6000.0 | 11.0 | 16.0 | awd | 7a | Italy | 295000.0 |
| Ferrari | F12Berlinetta | 2015 | Base Coupe | coupe | 731.0 | 8250.0 | 509.0 | 6000.0 | 11.0 | 16.0 | rwd | 7a | Italy | 319995.0 |
| Ferrari | LaFerrari | 2015 | Base Coupe | coupe | 949.0 | 9000.0 | 664.0 | 6750.0 | 12.0 | 16.0 | rwd | 7a | Italy | 1416362.0 |
| Acura | NSX | 2017 | Base Coupe | coupe | 573.0 | 6500.0 | 476.0 | 2000.0 | 21.0 | 22.0 | awd | 9a | Japan | 156000.0 |
| Nissan | GT-R | 2016 | Premium Coupe | coupe | 545.0 | 6400.0 | 436.0 | 3200.0 | 16.0 | 22.0 | awd | 6a | Japan | 101770.0 |
| Lamborghini | Aventador | 2015 | LP 700-4 Coupe | coupe | 700.0 | 8250.0 | 507.0 | 5500.0 | 11.0 | 18.0 | awd | 7a | Italy | 397500.0 |
| Lamborghini | Huracan | 2015 | LP 610-4 Coupe | coupe | 610.0 | 8250.0 | 413.0 | 6500.0 | 16.0 | 20.0 | rwd | 7a | Italy | 237250.0 |
| Lamborghini | Gallardo | 2014 | LP 550-2 Coupe | coupe | 550.0 | 8000.0 | 398.0 | 6500.0 | 12.0 | 20.0 | rwd | 6a | Italy | 191900.0 |
| Bentley | Continental GT | 2016 | V8 Coupe | coupe | 500.0 | 6000.0 | 487.0 | 1700.0 | 15.0 | 25.0 | awd | 8am | United Kingdom | 198500.0 |
| Maserati | Granturismo | 2016 | Sport Coupe | coupe | 454.0 | 7600.0 | 384.0 | 4750.0 | 13.0 | 21.0 | rwd | 6am | Italy | 132825.0 |
| Maserati | Quattroporte | 2016 | S Sedan | sedan | 404.0 | 5500.0 | 406.0 | 1500.0 | 16.0 | 23.0 | rwd | 8am | Italy | 99900.0 |
| Maserati | Ghibli | 2016 | Base Sedan | sedan | 345.0 | 5250.0 | 369.0 | 1750.0 | 17.0 | 24.0 | rwd | 8am | Italy | 70600.0 |
| BMW | 6-Series | 2016 | 640 I Coupe | coupe | 315.0 | 5800.0 | 330.0 | 1400.0 | 20.0 | 30.0 | rwd | 8am | Germany | 77300.0 |
| BMW | i8 | 2016 | Mega World Coupe | coupe | 357.0 | 5800.0 | 420.0 | 3700.0 | 28.0 | 29.0 | awd | 6am | Germany | 140700.0 |
| BMW | M4 | 2016 | Base Coupe | coupe | 425.0 | 5500.0 | 406.0 | 1850.0 | 17.0 | 24.0 | rwd | 6m | Germany | 65700.0 |
| BMW | M5 | 2016 | Base Sedan | sedan | 560.0 | 6000.0 | 500.0 | 1500.0 | 15.0 | 22.0 | rwd | 7am | Germany | 94100.0 |
| BMW | M6 | 2016 | Base Coupe | coupe | 560.0 | 6000.0 | 500.0 | 1500.0 | 15.0 | 22.0 | rwd | 7a | Germany | 113400.0 |
| Aston Martin | DB11 | 2017 | Base Coupe | coupe | 608.0 | 6500.0 | 516.0 | 1500.0 | 15.0 | 21.0 | rwd | 8am | United Kingdom | 211195.0 |
| Aston Martin | Rapide S | 2016 | Base Sedan | sedan | 552.0 | 6650.0 | 465.0 | 5500.0 | 14.0 | 21.0 | rwd | 8am | United Kingdom | 205300.0 |
| Aston Martin | Vanquish | 2016 | Base Coupe | coupe | 568.0 | 6650.0 | 465.0 | 5500.0 | 13.0 | 21.0 | rwd | 8am | United Kingdom | 287250.0 |
| Aston Martin | Vantage | 2016 | V8 GT (Manual) Coupe | coupe | 430.0 | 7300.0 | 361.0 | 5000.0 | 13.0 | 19.0 | rwd | 6m | United Kingdom | 103300.0 |
| Chevrolet | Corvette | 2016 | Z06 Coupe | coupe | 650.0 | 6400.0 | 650.0 | 3600.0 | 15.0 | 22.0 | rwd | 7m | United States | 88345.0 |
| Dodge | Viper | 2017 | GT Coupe | coupe | 645.0 | 5000.0 | 600.0 | 5000.0 | 12.0 | 19.0 | rwd | 6m | United States | 95895.0 |
| Audi | R8 | 2015 | 4.2 (Manual) Coupe | coupe | 430.0 | 7900.0 | 317.0 | 4500.0 | 11.0 | 20.0 | awd | 6m | Germany | 115900.0 |
| Audi | RS 7 | 2016 | Quattro Hatchback | hatchback | 560.0 | 5700.0 | 516.0 | 1750.0 | 15.0 | 25.0 | awd | 8am | Germany | 108900.0 |
| Audi | S6 | 2016 | Premium Plus quattro Sedan | sedan | 450.0 | 5800.0 | 406.0 | 1400.0 | 18.0 | 27.0 | awd | 7a | Germany | 70900.0 |
| Audi | S7 | 2016 | Prestige quattro Hatchback | hatchback | 450.0 | 5800.0 | 406.0 | 1400.0 | 17.0 | 27.0 | awd | 7a | Germany | 82900.0 |
| Audi | S8 | 2016 | Base Sedan | sedan | 520.0 | 5800.0 | 481.0 | 1700.0 | 15.0 | 25.0 | awd | 8am | Germany | 114900.0 |
| Lotus | Evora | 2017 | 2+2 Coupe | coupe | 400.0 | 7000.0 | 302.0 | 3500.0 | 16.0 | 24.0 | rwd | 6m | United Kingdom | 91900.0 |
| Jaguar | F-Type | 2016 | Base (Manual) Coupe | coupe | 340.0 | 6500.0 | 332.0 | 3500.0 | 16.0 | 24.0 | rwd | 6m | United Kingdom | 65000.0 |
| Mercedes-Benz | AMG GT | 2016 | S Coupe | coupe | 503.0 | 6250.0 | 479.0 | 1750.0 | 16.0 | 22.0 | rwd | 7a | Germany | 129900.0 |
| Mercedes-Benz | SL-Class | 2016 | SL400 Convertible | convertible | 329.0 | 5250.0 | 354.0 | 1600.0 | 20.0 | 27.0 | rwd | 7am | Germany | 85050.0 |
| Tesla | Model S | 2017 | 75D | sedan | 259.0 | 6100.0 | 243.0 | None | None | None | awd | 1dd | United States | 74500.0 |
| Porsche | 718 Boxster | 2017 | Base Convertible | convertible | 300.0 | 6500.0 | 280.0 | 1950.0 | 21.0 | 28.0 | rwd | 6m | Germany | 56000.0 |
| Porsche | 718 Cayman | 2017 | Base Coupe | coupe | 300.0 | 6500.0 | 280.0 | 1950.0 | 20.0 | 29.0 | rwd | 6m | Germany | 53900.0 |
| Porsche | 911 | 2016 | Carrera Coupe | coupe | 350.0 | 7400.0 | 287.0 | 5600.0 | 20.0 | 28.0 | rwd | 7m | Germany | 84300.0 |
| Porsche | Panamera | 2016 | Base Sedan | sedan | 310.0 | 6200.0 | 295.0 | 3750.0 | 18.0 | 28.0 | rwd | 7a | Germany | 78100.0 |
| McLaren | 570 | 2016 | Base Coupe | coupe | 570.0 | 7500.0 | 443.0 | 5000.0 | 16.0 | 23.0 | rwd | 7a | United Kingdom | 184900.0 |
| Rolls-Royce | Dawn | 2016 | Base Convertible | convertible | 563.0 | 5250.0 | 575.0 | 1500.0 | 12.0 | 19.0 | rwd | 8a | United Kingdom | 335000.0 |
| Rolls-Royce | Wraith | 2016 | Base Coupe | coupe | 624.0 | 5600.0 | 590.0 | 1500.0 | 13.0 | 21.0 | rwd | 8a | United Kingdom | 304350.0 |
