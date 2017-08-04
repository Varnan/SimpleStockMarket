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
