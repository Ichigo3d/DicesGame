import unittest
from dice import *


class Test_Dice(unittest.TestCase):
    def test_generate_numbers(self):
        self.assertLess(generate_number(), 7)
        self.assertGreater(generate_number(), 0)
        self.assertTrue(type(generate_number()), int)

    def test_connect_side(self):
        self.assertEqual(connect_side(1), Dice.SIDE1)

    def test_construct_sides(self):
        self.assertEqual(construct_sides(Dice.SIDE5, Dice.SIDE1), ['_____________    _____________ ',
                                                                   '|  *     *  |    |           | ',
                                                                   '|     *     |    |     *     | ',
                                                                   '|  *     *  |    |           | ',
                                                                   '|___________|    |___________| '])





