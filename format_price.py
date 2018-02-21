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
        price = float(price)
        if price % 1 == 0:
            price = '{:,.0f}'.format(price).replace(",", " ")
            return price
        else:
            price = "{:,.2f}".format(float(price)).replace(",", " ")
            price = price.replace(".", ",").replace(',00', '')
            return price
    except ValueError or TypeError:
        return None


if __name__ == "__main__":
    args = parse_command_line_args()
    if format_price(args.price) is not None:
        print(format_price(args.price))
    else:
        print("Enter numeric digits only")
