# python 3

import pandas as pd
import numpy as np
import random as rand

# my_game = Game("Game1_8_28_2016_1", "stanton", "russ", "jeff", "peter")
# my_game.start_game


class Game:
    """
    Class for making a new game.
    """
    def __init__(self, gamename, *arg):
        self.game_name = gamename
        self.player_list = self.generate_player_list(*arg)
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
        self.board = self.generate_board()
        self.sack = self.generate_sack(self.columns, self.rows)


    def generate_player_list(self, *arg):
        playerlist = []
        for a in *arg:
            playerlist.append(a)
        print("There are ", len(player_list), "players.")
        print("The players are: ", self.player_list)
        return playerlist


    def generate_board(self):
        """
        Generates a board matrix as a Pandas DataFrame
        made from cols & rows vars.
        """
        board = pd.DataFrame(index=self.rows, columns=self.columns)
        return board


    def remove_player(self):
        rplayer = input("Players: {1}. Remove which player? >> ".format(str(self.players)))
        self.player_list.remove(rplayer)


    def generate_sack(self, cols, rows):
        """
        Function returns a list called 'sack' filled with tile names made from cols & rows vars
        """
        sack = self.sack
        for c in cols:
            for r in rows:
                sack.append(c + r)
        return sack


    def start_game(self):
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


class Engine:
    def __init__(self):
        self.



class Player:
    def __init__(self, name, game):
        self.game = game
        self.name = name
        self.tiles = populate_tiles(game.sack) #must interact with game.sack...
        self.money = 6000
        self.properties = {'Luxor': 0, 'Tower': 0,
                         'American': 0,  'Festival': 0,
                         'Worldwide': 0, 'Continental': 0,
                         'Imperial': 0}

        print('Player "{0}" created with ${1}'.format(self.name, self.money))



    def populate_tiles(self, sackname):
        #take random tiles from sack
        pass

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