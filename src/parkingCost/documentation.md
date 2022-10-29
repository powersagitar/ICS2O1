# Parking Cost

## Information

* Charge: $1.75 per every period of half an hour that has started

## Need to know

* User's in time and out time

## Need to calculate

* Duration of stay
* Time periods of stay

## IPO table

![]()

## Storage

| Variable name | Variable use | Data type |
| :-: | :-: | :-:|
| HST | Store tax rate | float |
|CHARGE | Store unit price | float |
| inHour | Store in-time | int |
| inMin | Store in-time | int |
| outHour | Store out-time | int |
| outMin | Store out-time | int |
| duration | Duration of stay | int |
| period | Period of stay | int |
| subtotal | Subtotal of price | float |
| tax | Store tax | float |

## Pseudocode

* Initialize variables and fetch inputs then store them in variables
* Check inputs' validation
* Calculate duration of stay (3 situations in total)
    1. inHour > outHour (the next day): `duration = ((23 - inHour) * 60) + (60 - inMin) + (outHour* 60) + outMin`
    2. inHour = outHour
        1. inMin >= outMin (the next day): `duration = ((23 - inHour) * 60) + (60 - inMin) + (outHour* 60) + outMin`
        2. else (the same day): `duration = outMin - inMin`
    3. else (the same day): `duration = ((outHour - inHour) * 60) + (60 - inMin) + outMin; if inMin =  0, duration -= 60`
* Calculate periods of stay
    * Let duration / 30. If there's a remainder, then `period = duration // 30 + 1`; else, `period = duration // 30`. (Use `//` to format `period` to int)
* Calculate price: subtotal and tax
* Calculate total price and output results

## Test cases

|  |  |  |
| :-: | :-: | :-: |