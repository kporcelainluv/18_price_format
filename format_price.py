import argparse
import os


def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--price",
        required=True,
        help="Enter the price"
    )
    return parser.parse_args()


def is_digit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def find_errors_in_input(price):
    parser = argparse.ArgumentParser()
    if str(price).isalpha():
        parser.error("Please only enter numbers")
    if not is_digit(price):
        parser.error("Please enter only numeric digits")
    return True

def count_banknotes(banknotes):
    if len(banknotes) > 3:
        banknotes = int(float(banknotes))
        banknotes = list(str(banknotes))[::-1]
        price_with_whitespaces = list("".join(l + " " * (n % 3 == 2) for n, l in enumerate(banknotes)))
        banknotes = "".join(price_with_whitespaces)[::-1]
        if banknotes[0] == " ":
            banknotes = banknotes[1:]
    return banknotes

def count_coins(price):
    coins = os.path.splitext(price)[1][1:]
    if coins is "":
        return False
    if all([int(coins)]) == 0:
        return False
    else:
        coins_list = list(coins)
        for digit in reversed(coins_list):
            if digit == "0":
                coins_list.pop()
            else:
                break
        cents = "".join(coins_list)
    return "," + cents


def format_price(price):
    banknotes, coins = count_banknotes(price), count_coins(price)
    return banknotes if coins is False else banknotes + coins


if __name__ == "__main__":
    args = parse_command_line_args()

    if find_errors_in_input(args.price):
        banknotes, coins = count_banknotes(args.price), count_coins(args.price)
        print(format_price(args.price))
