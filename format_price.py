import argparse


def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--price",
        required=True,
        help="Enter the price"
    )
    return parser.parse_args()


def format_price(price):
    price = float(price)
    if price.is_integer():
        price = '{:,}'.format(int(price))
        return price.replace(",", " ")
    else:
        price = "{0:.2f}".format(round(float(price), 2))
        price = '{:,}'.format(float(price)).replace(",", " ").replace(".", ",")
        return price


if __name__ == "__main__":
    args = parse_command_line_args()
    try:
        if bool(float(args.price)):
            print(format_price(args.price))
    except ValueError:
        exit("Enter a float of numeric digits")
