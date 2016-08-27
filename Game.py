# python 3

import pandas as pd
import numpy as np


class Game():
    """
    Class for making a new game.
    """
    def __init__(self, game_name):
        self.columns = ['1', '2', '3',
                        '4', '5', '6',
                        '7', '8', '9',
                        '10', '11', '12']
        self.rows = ['A', 'B', 'C',
                     'D', 'E', 'F',
                     'G', 'H', 'I']

        self.properties = ['Luxor', 'Tower',
                      'American', 'Festival', 'Worldwide',
                      'Continental', 'Imperial']
        self.name = game_name
        self.players = []
        self.board = self.board_generator()
        self.sack = self.sack_generator(self.columns, self.rows)


    def add_player(self, player):
        self.players.append(player)


    def remove_player(self):
        rplayer = input("Players: {1}. Remove which player? >> ".format(str(self.players)))
        self.players.remove(rplayer)


    def board_generator(self):
        """
        Generates a board matrix as a Pandas DataFrame
        made from cols & rows vars.
        """
        board = pd.DataFrame(index=self.rows, columns=self.columns)
        return board


    def sack_generator(self, cols, rows):
        """
        Function returns a list called 'sack' filled with tile names made from cols & rows vars
        """
        sack = self.sack
        for c in cols:
            for r in rows:
                sack.append(c + r)
        return sack


    def start(self):
        command = input('Start new game - 1; Continue saved game - 2;')

        if command == '1':
            self.name = input('Game name? >>')
            players = []
            inp = input('Add player by name (no quotes), <enter> if done:')
            while inp is True:
                players.append(inp)
        elif command == '2':
            pass
            # create file for saved games,
            # this will access that file using game name as the key...
        else:
            quit()


class Player():
    def __init__(self, name, game):
        self.game = game
        self.name = name
        self.tiles = populate_tiles(game.sack) #this is just a template, doesn't work yet
        self.money = 6000
        self.properties = {'Luxor': 0, 'Tower': 0,
                         'American': 0,  'Festival': 0,
                         'Worldwide': 0, 'Continental': 0,
                         'Imperial': 0}
        print('Player "{0}" created with ${2}'.format(self.Name))

    def draw_tile(self, number):
        if len(self.Tiles) > 5:
            print("Max number of tiles reached.")
            pass
        else:
            # self.Tiles.append(draw_tile(number))
            pass

    def play_tile(self):
        pass


    def player_purchase(self, Property, TileCount):
        pass

    def merger(self, maj_prop, maj_tile_count, min_prop, min_tile_count):
        pass

    def end_game(self):
        pass