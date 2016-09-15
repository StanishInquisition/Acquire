from Game import *

my_game = Game("my_game", ('Ohyoon', 'Stan', 'Peter', 'Russ', 'John', 'Jeff'))
# print(my_game)

for player in my_game.player_dict:
    print(my_game.player_dict[player])
# print(my_game.player_dict['Ohyoon'])
# print(my_game)
