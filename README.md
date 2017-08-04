# Simple Stock Market
Simple example to calculate metrics for given stocks

## Description
The source code that will :

- For a given stock, 
    - calculate the dividend yield
    - calculate the P/E Ratio
    - record a trade, with timestamp, quantity of shares, buy or sell indicator and price
    - Calculate Stock Price based on trades recorded in past 15 minutes
- Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

##### Constraints & Notes

1.	No database or GUI is required, all data need only be held in memory.

2.	Formulas and data provided are simplified representations for the purpose of this exercise.

##### Global Beverage Corporation Exchange

Stock Symbol  | Type | Last Dividend | Fixed Dividend | Par Value
------------- | ---- | ------------: | :------------: | --------: 
TEA           | Common    | 0  |    | 100
POP           | Common    | 8  |    | 100
ALE           | Common    | 23 |    | 60
GIN           | Preferred | 8  | 2% | 100
JOE           | Common    | 13 |    | 250




## Requirements

- Python 2.7
- Tested on MacOS X

## Run

Make sure that inside the project folder SimpleStockMarket.

```
python main.py
```

## Console window

```
---------------------------------------
Enter the number of the Option you want:
----------------------------------------
| 1 | Calculate dividend yield
| 2 | Calculate the P/E Ratio
| 3 | Record Trade
| 4 | Calculate Volume Weighted Stock Price 
| 5 | Calculate the GBCE All Share Index
| 6 | To quit
----------------------------------------
>


```

Choose the option according to the need.


## Tests

tests suits are in test.py to run it

```
python test.py
```

## Author

Varnan Kanjhinghat


