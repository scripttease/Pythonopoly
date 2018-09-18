from ..game_logic import dice
from ..game_logic import turn
from ..game_logic import state_of_game
# from state_of_game import Player
from django.test import TestCase
import unittest

class TestGame(unittest.TestCase):
    "Player Test"

    def test_player_init_with_name(self):
        player1 = state_of_game.Player("Al")
        self.assertEqual(player1.name, "Al")
