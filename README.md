# Price Formatter

The program reads the price from input, strips cents if they are zeros and uses whitespaces to separate numbers. For example check tests.py. Coins are rounded to 2 digits.

# How to launch
The program uses argparse library to read from input.
```
python format_price --price [your number here]
```
# Example
input
```
python format_price.py --price 123456.754000000000
```
output
```
123 456,75
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
