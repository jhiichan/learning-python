import unittest
import main

class TestMain(unittest.TestCase):
    def test_should_drink_coffee_sleepy(self):
        is_sleepy = True
        expected = 'Drink Coffee!'
        actual = main.should_drink_coffee(is_sleepy)
        self.assertEquals(actual, expected)

    def test_should_drink_coffee_not_sleepy(self):
        is_sleepy = False
        expected = 'Continue what you are doing...'
        actual = main.should_drink_coffee(is_sleepy)
        self.assertEquals(actual, expected)

unittest.main()