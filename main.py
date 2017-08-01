from board import Board
import os
from computer import AI

board = Board()

ai = AI(100)

ai.iterate(board)

board.displayBoard()