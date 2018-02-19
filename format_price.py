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
    try:
        if float(price) % 1 == 0:
            price = '{:,}'.format(int(price)).replace(",", " ")
            return price
        else:
            price = "{:,.2f}".format(round(float(price), 2)).replace(",", " ").replace(".", ",")
            return price
    except ValueError:
        return ("Enter a float of numeric digits")


if __name__ == "__main__":
    args = parse_command_line_args()
    print(format_price(args.price))
