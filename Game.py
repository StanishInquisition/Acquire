# python 3

import pandas as pd
import numpy as np
import random as rand
from pprint import pprint, PrettyPrinter
import logging

pp = PrettyPrinter(width=100, indent=5, compact=False)


class Game:
    """
    Initialize a new game by passing a game name and player names as string arguments.
    e.g. : my_game = Game("my_game", "Chris", "Terry", "Pat", "Ramsey")
    This will also generate instaces of the Player class for each of those names and
    insert those objects into self.player_dict attribute
    """



    def __init__(self, gamename, *args):
        self.game_name = gamename

        self.player_dict = {}
        self.generate_players(args)

        self.columns = ['01', '02', '03',
                        '04', '05', '06',
                        '07', '08', '09',
                        '10', '11', '12']
        self.altcolumns = ['@',
                           '01', '02', '03',
                           '04', '05', '06',
                           '07', '08', '09',
                           '10', '11', '12']
        # self.altcolumns = list(self.columns)
        self.rows = ['A', 'B', 'C',
                     'D', 'E', 'F',
                     'G', 'H', 'I']
        self.altrows = list(self.rows)
        self.board = self.generate_board()
        self.altboard = self.generate_altboard()

        self.properties = ['Luxor', 'Tower',
                           'American', 'Festival', 'Worldwide',
                           'Continental', 'Imperial']

        self.sack = self.generate_sack(self.columns, self.rows)
        # pprint(vars(self))


    def __str__(self):
        return """Game name: {0}.
                \n Player list: {1}.
                \n Properties: {2}.
                \n Sack: {3}.
                \n Board:\n{4},
                \n Player stats:
                \n {5} """.format(
            self.game_name,
            ", ".join(self.player_dict.keys()),
            ", ".join(self.properties),
            ', '.join(self.sack),
            self.board,
            [pprint(self.player_dict[player]) for player in self.player_dict])

    def generate_players(self, names):
        """
            Create an instance of class Player for each name argument (*args) passed to Game
            and insert into self.player_dict
        """
        for name in names:
            self.player_dict[name] = Player(name, self.game_name)

    def generate_board(self):
        """
        Generates a board matrix as a Pandas DataFrame
        made from cols & rows vars.
        """
        board = pd.DataFrame(index=self.rows, columns=self.columns)
        print("\n Board created.")
        pprint(board)
        return board

    def generate_altboard(self):
        """
        Create a board that works on pythonista using nested list.
        Should function exactly the same in order to work correclty
        """

        grid = [["[]"] * (len(self.altcolumns) - 1) for x in range(len(self.altrows))]

        for i in range(len(self.altrows)):
            grid[i].insert(0, self.altrows[i])
        grid.insert(0, self.altcolumns[:])

        print("\n Alternative board created.")
        self.print_altboard(grid)
        return grid

    @staticmethod
    def print_altboard(board):
        pp.pprint(board)

    def remove_player(self):
        removed_player = input("Players: {0}. Remove which players?".format(" ".join(self.player_dict)))
        self.player_dict.remove(removed_player)

    @staticmethod
    def generate_sack(cols, rows):
        """
        Return a list filled with tile names made from cols & rows
        """
        sack = []
        for c in cols:
            for r in rows:
                sack.append(c + r)
        return sack

    def start_game(self):
        command = input('Start new game - 1; Browse and continue saved game - 2;')

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

    def draw_tiles(self, player, number_of_tiles):
        pass


class Engine:
    def __init__(self):
        pass


class Player:
    def __init__(self, name, game):
        self.game = game
        self.name = name
        self.tiles = []
        self.money = 6000
        self.properties = {'Luxor': 0, 'Tower': 0,
                         'American': 0,  'Festival': 0,
                         'Worldwide': 0, 'Continental': 0,
                         'Imperial': 0}

        print('\n\n Player "{0}" created'.format(self.name))
        pp.pprint(vars(self))

    def __str__(self):
        return 'Player: {0} \n Game: {1} \n Tiles: {2} \n Money: {3} \n Properties: {4}'.format(self.name, self.game, self.tiles, self.money, self.properties)

    def populate_tiles(self, sackname):
        #take tiles from sack
        return True

    def draw_tile(self, number):
        if len(self.tiles) > 5:
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