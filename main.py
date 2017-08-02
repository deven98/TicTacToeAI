from board import Board
import os
from computer import AI

board = Board()

ai = AI(5)
ai.iterate(board)

board.displayBoard()