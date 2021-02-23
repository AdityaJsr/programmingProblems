import unittest
import tempConversion

class testTemp(unittest.TestCase):

    def test_convertor(Self):
        result = tempConversion.convertor(45)
        Self.assertEqual(result, 113.0)
