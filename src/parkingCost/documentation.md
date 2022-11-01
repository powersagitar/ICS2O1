# Parking Cost

Table of Contents
- [Parking Cost](#parking-cost)
  - [Information](#information)
  - [Need to know](#need-to-know)
  - [Need to calculate](#need-to-calculate)
  - [IPO table](#ipo-table)
  - [Storage](#storage)
  - [Pseudocode](#pseudocode)
  - [Test cases](#test-cases)
    - [Top-5 valueable cases](#top-5-valueable-cases)
    - [All cases](#all-cases)

## Information

* Charge: $1.75 per every period of half an hour that has started

## Need to know

* User's in time and out time

## Need to calculate

* Duration of stay
* Time periods of stay

## IPO table

![figure 1 - IPO Table](./figure%201.png)

## Storage

| Variable name |   Variable use    | Data type |
| :-----------: | :---------------: | :-------: |
|      HST      |  Store tax rate   |   float   |
|    CHARGE     | Store unit price  |   float   |
|    inHour     |   Store in-time   |    int    |
|     inMin     |   Store in-time   |    int    |
|    outHour    |  Store out-time   |    int    |
|    outMin     |  Store out-time   |    int    |
|   duration    | Duration of stay  |    int    |
|    period     |  Period of stay   |    int    |
|   subtotal    | Subtotal of price |   float   |
|      tax      |     Store tax     |   float   |

## Pseudocode

* Initialize variables and fetch inputs then store them in variables
* Check inputs' validation
* Calculate duration of stay (3 situations in total)
    1. inHour > outHour (the next day): `duration = ((23 - inHour) * 60) + (60 - inMin) + (outHour * 60) + outMin`
    2. inHour = outHour
        1. inMin >= outMin (the next day): `duration = ((23 - inHour) * 60) + (60 - inMin) + (outHour * 60) + outMin`
        2. else (the same day): `duration = outMin - inMin`
    3. else (the same day):
        1. `duration = ((outHour - inHour - 1) * 60) + (60 - inMin) + outMin`
* Calculate periods of stay
    * Do duration / 30. If there's a remainder, then `period = duration // 30 + 1`; else, `period = duration // 30`. (Use `//` to format `period` to int)
* Calculate price: subtotal (`CHARGE * period`) and tax (`round((subtotal * HST), 2)`)
* Calculate total price (`str(round(subtotal + tax, 2))`) and output results

## Test cases

### Top-5 valueable cases

| in-time | out-time | duration (min) | period | subtotal |  tax  | total |
| :-----: | :------: | :------------: | :----: | :------: | :---: | :---: |
|  00:00  |  00:00   |      1440      |   48   |    84    | 10.92 | 94.92 |
|  00:00  |  12:00   |      720       |   24   |    42    | 5.46  | 47.46 |
|  12:00  |  10:00   |      1320      |   44   |    77    | 10.01 | 87.01 |
|  00:02  |  01:01   |       59       |   2    |   3.5    | 0.46  | 3.96  |
|  12:01  |  11:59   |      1438      |   48   |    84    | 10.92 | 94.92 |

### All cases

| in-time | out-time | duration (min) | period | subtotal |  tax  | total |
| :-----: | :------: | :------------: | :----: | :------: | :---: | :---: |
|  00:00  |  00:00   |      1440      |   48   |    84    | 10.92 | 94.92 |
|  00:00  |  12:00   |      720       |   24   |    42    | 5.46  | 47.46 |
|  12:00  |  10:00   |      1320      |   44   |    77    | 10.01 | 87.01 |
|  00:02  |  01:01   |       59       |   2    |   3.5    | 0.46  | 3.96  |
|  12:01  |  11:59   |      1438      |   48   |    84    | 10.92 | 94.92 |
|  00:05  |  01:15   |       70       |   3    |   5.25   | 0.68  | 5.93  |
|  00:01  |  01:02   |       61       |   3    |   5.25   | 0.68  | 5.93  |
|  00:10  |  01:05   |       55       |   2    |   3.5    | 0.46  | 3.96  |
|  00:10  |  00:15   |       5        |   1    |   1.75   | 0.23  | 1.98  |
