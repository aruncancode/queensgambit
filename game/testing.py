# from game import Game
from game import *


# pgn = [["d4", "e5"], ["e3", "Bb4"], ["c3", "f6"] ,["Nf3", "f5"], ["Ne5", "Bc3"], ["Nc3", "f4"]]
# pgn = ["e4", "e5", "Bb5", "a6", "Bd7"]
# pgn = ['e4', 'e5', 'Qh5', 'Nc6', 'Qf7']
pgn = ['e4', 'e5', 'Qh5', 'Nc6', 'Qf7', 'Kf7', 'Bc4', "Ke8"]
# pgn = ["e4", "e5", "Nf3", "Nf6","Bd3", "Bd6","Ke2", "c5" ,"Ke1" ,"c4", "O-O"]
# pgn = ['e4', 'e5', 'Nf3', 'Nc6', 'Bb5', 'a6', 'O-O', 'ab5', 'Re1', 'Na7', 'Re3', 'Nc6', 'Ra3', 'Ra3', 'Qe2', 'Ne7', 'Nh4', 'd6', 'Qh5', 'Re3', 'a3', 'Re1']
# pgn= ["e4", 'e5', "Nf3", "Nc6", "Bd3", "Qh4", "O-O", "Nd4", "Nd4", "Nf6", "Re1", "Qh3", "Kf1", "Qh2", "Be2"]
# pgn = ["e4", "e5", "Qh5", "d6", "Qf7"]
game = Game()

# print(game.pgn_parser(pgn))
# print(pgn)
print(game.analyse(pgn))
# print(pgn)