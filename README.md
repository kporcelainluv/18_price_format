# Price Formatter

The program reads the price from input, strips cents if they are zeros and uses whitespaces to separate numbers. For example check tests.py.

# How to launch
The program uses argparse library to read from input.
```
python format_price --price [your number here]
```
# Example
input
```
python format_price.py --price 1234565434567654.00054000000000
```
output
```
1 234 565 434 567 654,00054
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
