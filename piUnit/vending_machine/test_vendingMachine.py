import unittest
from main.vendingMachine import *

class vendingMachine(unittest.TestCase):

    def test_currency_counter(self):
        result = (currency_counter(500))
        self.assertEqual(result,("500 : 1,"))
        result = (currency_counter(5555))
        self.assertEqual(result,("1000 : 5,500 : 1,50 : 1,5 : 1,"))
        result = (currency_counter(21))
        self.assertEqual(result,("10 : 2,1 : 1,"))
        result = (currency_counter(-5))
        self.assertEqual(result,(""))

if __name__ == "__main__":
    unittest.main()    