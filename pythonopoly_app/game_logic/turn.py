from ..game_logic import dice
from ..game_logic import state_of_game

# Init Players
# player1 = state_of_game.Player("Al")
# player2 = state_of_game.Player("Louis")

# Init Game
# game = state_of_game.Gamestate()
# game.add_player(player1)
# game.add_player(player2)

def take_turn(game, player, dice):
   roll = dice.roll()
   # roll = 3
   player = game.players.pop[0]



   # At end of turn
   Gamestate.players.append(player)
