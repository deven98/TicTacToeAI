from board import Board
import os
from computer import AI

board = Board()

ai = AI(100)

board.move(1,1)
board.move(1,2)
board.move(2,2)
board.move(2,3)
board.move(3,3)

if board.isWin() is 1 :
    print("Won!")

board.displayBoard()