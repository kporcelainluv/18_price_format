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
    parser = argparse.ArgumentParser()
    if str(price).isalpha():
        parser.error("Please only enter numbers")
    if not bool(type(price)):
        parser.error("Please enter only numeric digits")

    price = float(price)
    if price % 1 == 0:
        price = '{:,.0f}'.format(price).replace(",", " ")
        return price
    else:
        price = "{:,.2f}".format(float(price)).replace(",", " ").replace(".", ",")
        return price


if __name__ == "__main__":
    args = parse_command_line_args()
    print(format_price(args.price))
