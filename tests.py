import unittest
from format_price import format_price


class PriceFormattingTestCase(unittest.TestCase):

    def test_solves_trillions(self):
        input_price = "1000000000000000000.0000"
        output_price = "1 000 000 000 000 000 000"
        formatted_price = format_price(input_price)
        self.assertEqual(formatted_price, output_price)

    def test_solves_millions(self):
        input_price = "15999777.000000"
        output_price = "15 999 777"
        formatted_price = format_price(input_price)
        self.assertEqual(formatted_price, output_price)

    def test_solves_hundreds_thousands(self):
        input_price = "555777.000000"
        output_price = "555 777"
        formatted_price = format_price(input_price)
        self.assertEqual(formatted_price, output_price)

    def test_solves_thousands(self):
        input_price = "5678.000"
        output_price = "5 678"
        formatted_price = format_price(input_price)
        self.assertEqual(formatted_price, output_price)

    def test_solves_hundreds(self):
        input_price = "678.000000"
        output_price = "678"
        formatted_price = format_price(input_price)
        self.assertEqual(formatted_price, output_price)

    def test_solves_cents(self):
        input_price = "123456.00345000000000"
        output_price = "123 456"
        formatted_price = format_price(input_price)
        self.assertEqual(formatted_price, output_price)

    def test_solves_cents(self):
        input_price = "123456.365"
        output_price = "123 456,37"
        formatted_price = format_price(input_price)
        self.assertEqual(formatted_price, output_price)

    def test_string_of_letters(self):
        input_price = "hello, world"
        self.assertIsNone(format_price(input_price))

    def test_string_of_numbers_and_a_letter(self):
        input_price = "1234567k.0000000"
        self.assertIsNone(format_price(input_price))

    def test_list_of_prices(self):
        input_price = "['12345.000', '123456.000', '123456.000']"
        self.assertIsNone(format_price(input_price))

    def test_touple_of_prices(self):
        input_price = "('12345.000', '123456.000', '123456.000')"
        self.assertIsNone(format_price(input_price))

    def test_dict_of_prices(self):
        input_price = "{1: '12345.000', 2: '123456.000', 3: '123456.000'}"
        self.assertIsNone(format_price(input_price))

    def test_list_of_types(self):
        input_price = "[10, False, [], {}]"
        self.assertIsNone(format_price(input_price))


if __name__ == '__main__':
    unittest.main()
