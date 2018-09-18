from ..game_logic import dice
from django.test import TestCase
import unittest

class TestDice(unittest.TestCase):
    "Dice Tests"

    def test_never_rolls_above_six(self):
        for i in range(100):
            x = dice.roll()
            self.assertTrue(x <= 6)
        
    def test_never_rolls_below_one(self):
        for i in range(100):
            x = dice.roll()
            self.assertTrue(x >= 1)

