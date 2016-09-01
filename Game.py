# python 3

import pandas as pd
import numpy as np
import random as rand

# my_game = Game("Game1_8_28_2016_1", "stanton", "russ", "jeff", "peter")
# my_game.start_game


class Game:
    """
    Instantiate a new game by passing a game name and player names as arguments.
    """
    def __init__(self, gamename, *arg):
        self.game_name = gamename
        self.player_list = self.generate_player_list(*arg)
        for player in self.player_list:
            self.generate_player(player)
            #create a Player instance for each player in the list, set player attributes to local game attributes
        self.columns =      ['1', '2', '3',
                              '4', '5', '6',
                              '7', '8', '9',
                              '10', '11', '12']
        self.rows =         ['A', 'B', 'C',
                             'D', 'E', 'F',
                             'G', 'H', 'I']
        self.properties =   ['Luxor', 'Tower',
                             'American', 'Festival', 'Worldwide',
                             'Continental', 'Imperial']
        self.board = self.generate_board()
        self.sack = self.generate_sack(self.columns, self.rows)


    def __str__(self):
        return "Game name: {0}.\nPlayer list: {1}.\n Properties: {2}".format(self.game_name, ", ".join(self.player_list), ", ".join(self.properties))

    @staticmethod
    def generate_player_list(*arg):
        playerlist = []
        for a in arg:
            playerlist.append(a)
        print("\n\nPlayer list generated.")
        print("There are", len(playerlist), "players:\n", ", ".join(playerlist))
        return playerlist


    def generate_player(self, playername):
        # create an instance of class Player for each name in self.playerlist
        playername = Player(playername, self.game_name)

    def generate_board(self):
        """
        Generates a board matrix as a Pandas DataFrame
        made from cols & rows vars.
        """
        board = pd.DataFrame(index=self.rows, columns=self.columns)
        print("\nBoard generated.")
        print(board)
        return board


    def remove_player(self):
        removed_player = input("Players: {0}. Remove which players?".format(" ".join(self.player_list)))
        self.player_list.remove(removed_player)


    def generate_sack(self, cols, rows):
        """
        Return a list filled with tile names made from cols & rows
        """
        sack = []
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
        pass


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