# from game import Game
from game import *


pgn = [["d4", "e5"], ["e3", "Bb4"], ["c3", "f6"] ,["Nf3", "f5"], ["Ne5", "Bc3"], ["Nc3", "f4"]]


game = Game()
print(game.analyse(pgn))